# Research Notes — Athlete Recruiting Marketplace

## Research Goal

Understand what software sits under the directory leaf "Athlete Recruiting Marketplace" (§28 Sports, Fitness & Recreation, between "Sports Scouting Platform" and "Athlete Injury / Availability Management"): what its core objects are, who the two sides are and what each does, how discovery and contact work, what states and rules govern a recruiting relationship, and where the boundary lies against Sports Scouting Platform, coach-side recruiting CRMs, Student Recruitment CRM / Admissions Management (§23), the HR recruiting family (§09), and team/registration sports software.

## Initial Boundary (hypothesis before research)

- Hypothesis: a two-sided marketplace connecting prospective student-athletes (and their families/club coaches) with college coaches; the athlete-side recruiting profile is the central object; the coach side discovers, evaluates, and contacts; the whole exchange is oriented to next-level (college) placement. No money flows between the two sides through the platform — the "market" is a connection market, not a transaction market.
- Likely neighbors: Sports Scouting Platform (scout-side talent identification, leaf directly above), coach-side recruiting CRM (products sold separately by a sampled vendor), Student Recruitment CRM / Admissions Management (§23, institution-side, no athlete registry), Talent Sourcing / Candidate Search / Job Board (§09, structural analog in a different domain), Team Management Application / Youth Sports Management / Sports Registration Platform (roster administration, not exposure), Casting Platform (§27, structural analog).
- Key uncertainties going in: (1) whether demand-side "postings" exist as first-class objects or only implicit needs; (2) whether video is definitional or just the current center of gravity; (3) how governing-body (NCAA/NAIA) rules shape the product; (4) the business-model split between sides; (5) how much of the workflow is human-service vs self-serve.

## Research Questions

1. What objects exist? (athlete recruiting profile, coach/program account, school/organization profile, video/highlight, academic record, target list, interest/favorite, message, view event, roster need/opening, evaluation, commitment)
2. Who are the two sides, and what intermediaries exist (parents, club coaches, high school staff, event operators)?
3. How does discovery work in both directions (coach search, athlete school search, algorithmic/expert matching, roster-need matching)?
4. What is the communication model, and what visibility/tracking affordances attach to it?
5. What states does the exchange pass through, and what is the recorded outcome (commitment)?
6. What rules matter (profile-completeness gates, class-year structure, compliance/standardized-information constraints, tier-gated features)?
7. What is the business model on each side?
8. Where is the boundary vs scouting platforms, recruiting CRMs, admissions/education CRM, and the HR recruiting family?

## Representative Products

| Product | Segment | Philosophy | Why sampled |
|---|---|---|---|
| NCSA College Recruiting (ncsasports.org) | largest US college recruiting network; all divisions D1–NAIA–NJCAA; many sports | service-heavy marketplace: human recruiting coaches and membership tiers atop a free network | market leader; shows the service-packaging pole and a published NCAA compliance posture |
| SportsRecruits (sportsrecruits.com) | club-centric sports (lacrosse, soccer, volleyball, softball, etc.); club/HS org accounts central | club-workflow-first marketplace: organization accounts, promotion on behalf of athletes, roster-need matching, coach side free | the club-mediated pole; richest documented object vocabulary (Roster Needs, Discover Feed, view tracking) |
| CaptainU (captainu.com, branded "Stack Athlete Recruiting") | mass-market freemium; athletes + colleges + teams + events as four product lines | app-first freemium marketplace with an events product line | shows four-sided packaging (events as a product line) and the freemium pole |

Rejected/adjusted samples:

- FieldLevel (fieldlevel.com) — intended as the network/endorsement-graph pole; both fetch attempts (www and bare domain) returned HTTP 403 (2026-09-06). Dropped per network rule; recorded as sample limitation.
- SportsRecruits Help Center (help.sportsrecruits.com) — timeout + transport error on two attempts. Dropped per network rule; no vendor help-center-level operational detail was obtained for any sampled product.
- BeRecruited (berecruited.com) — intended as the historical early-web sample; fetch returned empty. Dropped per network rule; historical breadth handled by structural argument (see Historical check under Canonical Model).
- NCSA sibling products (Front Rush — coach-side recruit CRM; Coach Packet, EventBeacon — live-event apps) observed only as described on NCSA's coach page; treated as boundary data points, not primary samples.

## Sources

All fetched 2026-09-06 (Layer A unless noted):

- NCSA — homepage: https://www.ncsasports.org/
- NCSA — College Coach page: https://www.ncsasports.org/college-coach
- NCSA — membership/cost page: https://www.ncsasports.org/who-is-ncsa/what-does-ncsa-do/what-does-ncsa-cost-how-much
- NCSA — NCAA Compliance Certification page: https://www.ncsasports.org/how-ncsa-works/ncaa-certification-compliance-scouting-services
- SportsRecruits — homepage: https://www.sportsrecruits.com/
- SportsRecruits — College Coaches page: https://www.sportsrecruits.com/colleges
- SportsRecruits — Student-Athletes page: https://www.sportsrecruits.com/athletes
- SportsRecruits — Clubs + High Schools page: https://www.sportsrecruits.com/clubs
- CaptainU — homepage: https://www.captainu.com/

Limitations:

- No vendor help center / knowledge base was reachable this session (SportsRecruits help center timed out twice; no other vendor's help center attempted after repeated failures). All workflow detail comes from official product/marketing surfaces, not step-by-step operational documentation. Precise field lists, message rules, eligibility gates, and numeric limits are therefore described conceptually.
- FieldLevel unreachable → the endorsement-graph/network pole is under-represented; cross-product claims rest on three products.
- BeRecruited unreachable → the early-web pole is represented only by structural reasoning and vendor longevity self-claims ("16 years powering recruiting online" — SportsRecruits; CaptainU copyright line since 2012).
- Statistical claims on vendor pages (profile-view counts, coach counts, commitment counts, search counts) are vendor-reported marketing figures; used only as existence evidence, never as facts in the final document.

## Product Observations

### NCSA College Recruiting

Key observations (Layer A):

- Positioning (homepage): "Get Recruited to Play College Sports. Build your profile, connect with college coaches, and find your best-fit college." Athlete promise: "Gain exposure to college coaches, get step-by-step guidance through the recruiting process, communicate directly with college coaches, access to development and tools to find the right college fit for you."
- Three named audiences: Student-Athletes; College Coaches ("find the right recruits for your program on the largest recruiting network. We offer tools to simplify communication, track an athlete's progress and an experienced staff dedicated to helping you succeed"); Club & High School Coaches (education/workshops-oriented offering).
- Dual authenticated surfaces: athlete/parent sign-in at a separate portal (recruit-match.ncsasports.org, a client "RMS") vs coach sign-in at coach.ncsasports.org ("Recruiting Management System" per the compliance page).
- Athlete-side capabilities: free recruiting profile ("Your NCSA profile offers a window into who you are as a student-athlete to make it easy for college coaches to make an evaluation"); College Search (filter by "athletic division, to academic selectivity, to location"); College Match (premium: "analyzing the student's personal preferences, expert evaluation of video/measurables, and feedback from college coaches"); direct messaging to college coaches with view tracking ("track when they view your messages and your profile"); upload of highlight videos and transcripts; 1-on-1 Recruiting Coach (premium human service).
- 4-step onboarding narrative (membership page): 1. Create profile (basic information, highlight videos, relevant stats, academic transcripts → "you're visible to college coaches looking for recruits"); 2. Get an assessment (expert call); 3. Pick tools/membership; 4. Meet goals.
- Membership ladder (no public prices — pricing via sales call): Free / Champion / Elite / MVP / MVP+. Feature rows include: digital recruiting resources; live and online workshops; College Coach Directory & Map; scholarship guidance; SAT/ACT prep; College Coach Message Center & Activity Reports; Roster Opening Notifications; professional highlight videos (quota grows by tier); Personalized Game Plan; Direct Promotion; 1-on-1 Personal Recruiting Coaching; IMG Academy+ coaching add-ons; camp voucher.
- Coach-side capabilities (coach page): free "NCSA Coach" membership — "Search and discover athletes in the NCSA network, promote your program and roster openings"; search filters ("Filter by grad year, location, position, and more"); interest tracking ("Get notified when athletes view your program, and when they mark that they are interested in your program"); follow athletes, add notes, export to CSV, add to Front Rush; "Directly message athletes — In just a few clicks, connect with any athlete in the world."
- Coach product family (same page): NCSA Coach (search/discover + promote roster openings); Coach Packet ("Everything you need to find and evaluate athletes at live events. Access event schedules, see team rosters and share scouting notes with your staff"); Front Rush ("Manage real-time recruiting data in customizable dashboards with access to communication tools... recruits, rosters, alumni and campers" — a coach-side recruit CRM sold separately); EventBeacon (event app with athlete profiles, notes, fit identification).
- Compliance page: NCSA describes itself as an NCAA-compliant recruiting/scouting service; quotes NCAA bylaw 13.14.3.1 (institutions may subscribe to recruiting or scouting services involving prospective student-athletes, limited to one annual subscription per service); states "every college and university has access to NCSA for free" and "We do not provide information in any form about prospective student-athletes beyond the standardized, consistent information that is provided to all coaches."
- Vendor-reported scale figures (existence evidence only): 50,000+ college coaches; 5M+ profile views by coaches (2025); 30,000+ commitments (2025); 330,000+ total commitments; 1,101,882+ coach searches (2024); 33,022 college teams favorited by athletes (2024); 40,000+ coaches / 23,000+ programs relationships; 14 national governing body partners (USA Swimming, USA Volleyball, US Youth Soccer, AAU, MaxPreps, Perfect Game, etc.); mobile app ("NCSA Athletic Recruiting").
- Bundling: part of IMG Academy; developmental coaching (mental performance, nutrition) bundled at top tiers.

### SportsRecruits

Key observations (Layer A):

- Positioning: "This is where recruiting happens... SportsRecruits unifies the college recruiting process to generate exposure, create connection, uncover opportunities, and help student-athletes play the sport they love at their best-fit college."
- Three audiences with separate signup flows: Student-Athlete; College Coach; Club/HS Organization.
- Hero statistics (existence evidence only): 21M+ athlete views by colleges; 74K+ athlete commitments logged; 17K+ "Roster Needs published by colleges"; 400,000+ athletes; 2,000+ club and high school organizations; "16 years powering recruiting online."
- Athlete-side: free profile "built to college coach specifications" (athletic, academic, personal information); video machinery ("Upload unlimited video, embed from Youtube, Vimeo or Hudl, sync film from our integration partners, and build highlight reels in-platform"); School Search (filter colleges by division, academic selectivity, location); target list ("Favorite schools... classify them based on fit, monitor progress with each"); Roster Needs visibility ("College coaches publish Roster Needs on their School Profile... Build out your Athlete Profile to see when you match"); real-time activity alerts (free) with the identity of viewers as a paid unlock ("Unlock college view activity and see which colleges are scouting your profile, reading your transcripts, visiting your press links, and watching your video" — Pro); messaging to "any college coach in the country" where "every message contains a tracked profile link" (Pro); commits page logging commitments; IMG Academy+ Essentials bundled.
- Coach-side: "Free for every college coach, forever" (regardless of division, budget, staff size); Discover Feed (filter "by athletic or academic stats, hometown, video availability, or interest in your program"); Publish Roster Needs ("Help student-athletes, guardians, and club and high school staff understand your team's recruiting needs for upcoming class years. Once published, Athlete Profiles matching your Roster Needs will funnel directly into a scoped feed"); Athlete Search by name ("database of over 400K PSAs... athletic stats and video, academic information, and contact details"); video library ("thousands of highlights and games from athletes, clubs, high schools, and events"); staff sync ("Favorite recruits that are a fit, skip those that aren't, and share evaluations across your program's account"); CRM export ("JumpForward, FrontRush, ARMs, etc."); messaging with copies forwarded to the athletic department email; .edu email as the login credential; EventBeacon sideline app (separate product, synced).
- Club/HS side: Athlete, Team + Organization Profiles; org-level view tracking ("Know who's scouting your athletes" — Recruiting Activity Feed, text/email alerts); unlimited video storage/distribution within the organization ("publish film to your Organization Profile with side-by-side rosters"); "Tag Fits for Athletes" (staff tag schools for athletes); messaging on behalf of athletes ("easily send profiles, messages and recommendations to colleges"); printable + embeddable rosters (PDF/iFrame); engagement data (org-wide metrics, weekly digests); dedicated account management.
- Ecosystem: co-branded official recruiting platforms for coaches' associations (IMLCARecruits, IWLCARecruits, NFHCARecruits — "The IMLCA, IWLCA, and NFHCA coaches associations have all partnered with SportsRecruits to power their official online recruiting platforms"); EventBeacon as sibling event app; video-capture integrations (sidelineHD, Balltime, Pixellot "coming soon").

### CaptainU ("Stack Athlete Recruiting")

Key observations (Layer A):

- Positioning: "GAIN EXPOSURE. GET RECRUITED." — "Join over 3 million high school athletes, colleges, teams, and events using CaptainU to connect & succeed." Now branded "Stack Athlete Recruiting" (Stack Sports family) while retaining the CaptainU name; copyright line "2012–2026 MLQ Ventures LLC dba CaptainU."
- Four product lines: Athletes; Colleges; Teams & Clubs; Events — each with its own pitch page and (apparently) separate surfaces: athlete login at app.captainu.com, college coach login at college.captainu.com.
- Athlete side: "Build a free or premium CaptainU recruiting profile, highlight your skills, and share your highlight videos. Gain instant access to all college coaches and communicate directly with them." "Team of experts provides helpful templates and easy, step-by-step guidance." Public price anchor exists ("paid plans... start at $22.50/month") — precise pricing kept out of the final document.
- College side: "More than 10,000 college coaches from every division use CaptainU College to recruit athletes... Discover your next great class of athletes, connect with them in powerful ways"; free coach account offered; carries an explicit NCAA statement: "This recruiting/scouting service has been approved in accordance with NCAA bylaws, policies, and procedures. NCAA Division I football and/or basketball coaches are permitted to subscribe to this recruiting/scouting service."
- Teams side: "More than 100,000 club and high school coaches have used CaptainU Teams to help their athletes get recruited. Advise your athletes, track their progress, and help them succeed."
- Events side: "More than 2,000 of the best tournaments use CaptainU Events to build great college recruiting events. Promote your event, get more college coaches to attend, and make it easy for them to connect with your teams and athletes." — events operators as a distinct participant.
- Supporting claims: "98% of high school athletes are lightly recruited" (marketing claim, existence evidence only); partners include tournaments/showcases (Big Shots, Insider Exposure, etc.); mobile app.

## Cross-product Comparison

| Aspect | NCSA | SportsRecruits | CaptainU |
|---|---|---|---|
| Athlete recruiting profile | free profile; basic info, highlight videos, stats, academic transcripts; tiered professional video production | free profile "built to college coach specifications"; athletic + academic + personal + contact info | free or premium profile; skills, highlight videos |
| Coach-side discovery | search largest athlete network; filters grad year/location/position/more; CSV export; follow + notes | Discover Feed + Athlete Search; filters athletic/academic stats, hometown, video availability, interest in program; favorite/skip + staff sharing | "Discover your next great class of athletes"; coach accounts free |
| Athlete-side program discovery | College Search (division, academic selectivity, location); College Match (premium, expert+algorithmic) | School Search; Roster Needs filter; target list with fit categories and progress | (not evidenced on fetched page) |
| Demand-side postings | "promote your program and roster openings"; free-tier "Roster Opening Notifications" | Roster Needs published by class year; profile-to-need matching funnels into scoped feed; sport-limited | (not evidenced) |
| Two-way contact | athlete→coach direct messaging w/ view tracking (tier-gated); coach→athlete direct messaging; coach notifications on athlete interest/views | athlete↔coach messaging (athlete side Pro; coach side free) with tracked profile links; email forwarding to .edu | "instant access to all college coaches"; "communicate directly" |
| View/interest tracking | "see when college coaches open your direct message"; coach sees who viewed/interested | profile/video/transcript/press-link view tracking (identity paid); org-level tracking for clubs; coach-side free | (not evidenced) |
| Video | upload highlights + transcripts; professional highlight video production in paid tiers | unlimited upload, embed YouTube/Vimeo/Hudl, partner sync, in-platform highlight reel editor, org film distribution | highlight video sharing |
| Club/HS organizations | education/workshops pole for club & HS coaches | full org platform: org/team/athlete profiles, staff-managed promotion, tag fits, engagement data, rosters | "CaptainU Teams": advise athletes, track progress |
| Events | camps/events directory + live-event products (Coach Packet, EventBeacon) as separate products | EventBeacon sibling app; event video in library | "CaptainU Events" as a product line for tournament operators |
| Matching/fit | College Match (premium): preferences + expert evaluation + coach feedback | profile↔Roster Needs matching; "best fit" framing | (not evidenced) |
| Commitment outcome | commitments counted/celebrated; "330,000+ helped commit" | "74K+ athlete commitments logged"; commits page | "3 million+ athletes... fulfill their dreams of getting recruited" |
| Compliance posture | NCAA-compliant scouting service; free + standardized info to all coaches | association co-branded official platforms (IMLCA/IWLCA/NFHCA) | posted NCAA approval statement for DI football/basketball |
| Business model | athlete/family memberships (free→premium ladder w/ human coaching); coach side free | athlete Pro subscription; club org licenses; coach side "free forever" | athlete freemium (public starting price); coach free; teams/events products |
| Surfaces | web portals (separate athlete vs coach domains) + mobile app | web (three signup flows) + coach .edu login + mobile event app | web + separate athlete/college apps |
| Parent involvement | parents addressed directly ("Parents Start Here"; parent workshops) | guardians named as Roster Needs audience | athletes & parents addressed |

## Canonical Model (Layer C synthesis)

L0 — Defining Invariant (smallest structure without which the Type is unrecognizable):

1. **Athlete-side recruiting profile registry** — identified prospective student-athletes, each with a recruiting profile carrying a recruiting-relevant identity (sport/position, recruiting class/graduation year, athletic attributes such as measurables and statistics, academic attributes, contact information), authored by or for the athlete (self, family, or club/high-school staff). Without self/club-side authoring by (or for) the athletes themselves, the product is a scouting platform, not a recruiting marketplace.
2. **Coach-side program accounts** — college coaches/recruiting staff as authenticated demand-side participants acting for their programs. Without the demand side, the product is a self-promotion or college-search tool.
3. **Coach-side searchable discovery over the athlete pool** — coaches search/filter across the athlete profile population by recruiting criteria. Without this, it is not a recruiting marketplace but an athlete-owned page//portfolio service.
4. **Two-way interest/contact channel between the sides** — athletes (or their proxies) can signal interest and initiate contact toward coaches, and coaches can signal interest and initiate contact toward athletes, inside the platform. Without any contact channel, the product degrades into a static scouting database/directory.
5. **Placement orientation** — the entire exchange exists to produce next-level recruiting outcomes (roster spots / scholarships), organized around recruiting class years; the platform records progression toward and attainment of that outcome (commitments), but does not itself transact the placement.

The defining workflow is the loop these imply: profile authored/completed → discovered (coach search, athlete school research, need/fit matching) → interest signaled → contact exchanged → evaluation → (off-platform) offer/visit → commitment recorded.

Historical check (§24): pre-web equivalents — showcase programs and camp packets, recruiting guides/newsletters distributed to coaches, athlete fact sheets and VHS highlight tapes mailed to programs — satisfy all five invariants (supply registry, demand side, coach-side discovery via the guide, contact via mail/phone, placement orientation) with no video hosting, no algorithms, no view tracking, no club org accounts, no subscription tiers. Early web-era recruiting services (text profiles + coach databases) also fit. Therefore video, matching, tracking, organization accounts, and tiering are common mature structure, not definition. The five invariants hold for older, regional, and differently positioned implementations.

L1 — Common Mature Structure (cross-product commonality, Layer B):

- Video/highlight machinery on profiles: upload, embedding from external hosts, in-platform highlight editing, team/game film libraries (all three sampled products center video in some form)
- Academic/eligibility attributes and documents on the athlete profile (GPA, transcripts, test scores)
- Athlete-side college discovery: searchable college/school database, target/favorite lists with fit classification and per-school progress
- Interest signaling in both directions + view tracking (who viewed profile/video/messages; often identity-of-viewer as a paid unlock)
- Demand-side postings: colleges publish roster needs/openings by class year; matching profiles funnel into scoped feeds (two of three products; treated as common)
- Matching/fit assistance: from deterministic profile↔need matching to expert-in-the-loop "best fit" analysis (packaging varies)
- Club/high-school organization accounts: org/team/athlete profile hierarchy, staff-managed promotion on behalf of athletes, guidance/tagging, org-level engagement dashboards
- Coach-side evaluation workflow: favorites/skips, notes, staff sharing/sync, export to CSV or external recruit CRMs
- Messaging affordances: tracked links, email forwarding/copying into institutional mailboxes, notification of interest
- Commitment logging/public commitment records
- Educational content layer: recruiting-process guides, eligibility resources, webinars/workshops
- Mobile apps for at least the athlete side
- Dual-surface architecture: separate authenticated portals/flows per side (athlete vs coach), sometimes separate domains/apps

L2 — Variant / Optional Structure:

- Human service layer: 1-on-1 recruiting coaches/consultants, assessments, personalized game plans, direct promotion (service-heavy pole) vs self-serve pole
- Compliance/regulatory posture: NCAA-compliant-scouting-service certification claims; standardized-information commitments; association co-branded official platforms (governance partnerships)
- Events layer: live-event companion apps, event rosters/schedules, event-operator products — sometimes packaged as separate products
- Business-model shape: free-for-coaches is cross-product; athlete side is freemium/subscription; org licensing; public price anchors vary
- Development/adjacent bundling: mental-performance/nutrition coaching, camps, SAT/ACT prep
- Video-capture/AI integrations (sideline capture products feeding film into profiles)
- Sport scope breadth (many-sport generalists vs club-sport concentration) and division coverage (D1–D3, NAIA, NJCAA/JUCO)

L3 — Vendor-specific (research notes only):

- NCSA: membership tier names (Free/Champion/Elite/MVP/MVP+), "Recruiting Coach" role, IMG Academy+ bundling, "Recruiting Management System" coach-portal naming, recruit-match clientrms subdomain, professional highlight video quota ladder (2/3/5/5), "Certified Compliant" badge, bylaw 13.14.3.1 quotation, standardized-info commitment, 9,884 D1–D3 football/basketball coaches figure, "NCSA vs Do-It-Yourself" comparison tables, toll-free sales numbers, governing-body partner roster, all scale figures
- SportsRecruits: "Roster Needs" product term and its sport-coverage lists, "Discover Feed", Pro tier naming, view-tracking scope list (transcripts/press links), org engagement digests, "Free for every college coach, forever", IMLCARecruits/IWLCARecruits/NFHCARecruits co-brands, EventBeacon, .edu login rule, 400K/2,000/21M/74K/17K figures, Zendesk help center (unreachable)
- CaptainU: Stack Sports/Stack Athlete Recruiting rebrand, four product-line split (Athletes/Colleges/Teams/Events), "$22.50/month" price anchor, "98% lightly recruited" claim, NCAA approval statement wording, MLQ Ventures ownership, 3M/10K/100K/2,000 figures
- Cross-vendor ownership note: NCSA and SportsRecruits both show IMG Academy ownership signals (shared privacy-policy links; Essentials bundling) — market consolidation observation only

## Vendor-specific Findings

- **Naming hazard**: vendors and regulators use "recruiting" and "scouting" interchangeably in this market — NCSA's legal name contains "Scouting Association", NCAA bylaws govern "recruiting or scouting services", NCSA's live-event tools mention "scouting notes". The directory's separate Sports Scouting Platform leaf must therefore be defined by structure (who participates, what the exchange is for), not by vendor vocabulary.
- **Demand-side postings exist but are not universal**: SportsRecruits makes Roster Needs a first-class object with matching feeds; NCSA exposes roster openings/promotion more lightly ("promote your program and roster openings", free-tier notifications). Demand postings are common mature structure, not the defining core — the supply-side profile remains the center of gravity in all sampled products.
- **The coach side is consistently free**: all three products provide free coach access, monetizing athletes/families (subscriptions), organizations (licenses), and services. NCSA ties the free coach side explicitly to compliance ("every college and university has access to NCSA for free" + standardized information for all coaches). This makes the free-coach-side pattern partly business-model, partly regulatory.
- **View tracking is monetized asymmetrically**: athletes see that they were viewed (and pay to see who); coaches see which athletes viewed/expressed interest in their program for free; clubs get org-wide view analytics. Interest visibility is a tiered permission surface across all sampled products.
- **Human services sit atop, not inside, the marketplace loop**: the service-heavy pole sells guidance/evaluation/promotion as membership layers; the marketplace objects and loops stay the same.

## Boundary Findings

1. **vs Sports Scouting Platform (leaf directly above)**: the recruiting marketplace's L0 requires athlete-side self/club-authored profiles and two-way participation; a scouting platform is evaluator-side talent identification and evaluation over athlete/video registries (often already-visible performers), with no athlete-as-participant exchange. Directional tests: remove athlete authorship/participation → scouting platform; add scout-side evaluation-report machinery → still a marketplace (evaluation is a common module here). The vocabulary overlap is real (NCAA "recruiting or scouting services"; NCSA's own name; Teamworks sells both "Recruiting" and "Scouting" products per sibling research notes) — joint check recommended when sports-scouting-platform is processed.
2. **vs coach-side recruiting CRMs (e.g., Front Rush, JumpForward, ARMs)**: a recruit CRM manages a college staff's recruiting pipeline (contacts, communications, boards); it has no athlete registry and no athlete-side participation. Marketplace products export to these CRMs (SportsRecruits: "Port data to your CRM"; NCSA: "adding to Front Rush"), proving separability. No dedicated directory leaf exists for sports recruit CRMs; they surface here as boundary data points.
3. **vs Student Recruitment CRM / Admissions Management (§23)**: institution-side admissions funnel over applicants; no athlete-authored athletic registry, no two-sided discovery, no athletic-evaluation semantics. The recruiting marketplace serves the coach's roster need, not the admissions office's class build.
4. **vs HR recruiting family (Talent Sourcing, Candidate Search, Job Board, §09)**: structural analog (registry + search + contact + hiring outcome) in a different domain; the athletic Type is defined by athletic-recruiting semantics (class years, eligibility, video evaluation, club intermediaries, governing-body rules) and its marketplace two-sidedness (candidate-side participation is native here, unlike coach-side recruiting CRMs).
5. **vs Team Management Application / Youth Sports Management / Sports Registration Platform**: those manage active-roster administration (schedules, registration, communication); the recruiting marketplace manages exposure and next-level placement for athletes who are about to leave their current team. A club may run both; the objects do not overlap definitionally.
6. **vs college search / college directory surfaces**: athlete products embed college search, but a college-search product without an athlete registry is not this Type.
7. **Structural analogs (not confusion risks)**: Casting Platform (§27) — talent profiles + role matching + submissions; Dating Application — two-sided profiles + interest signaling. Different domain semantics and outcomes throughout.

## Uncertainties

- Exact profile field vocabularies, message mechanics (reply rules, throttles), and eligibility/completeness gates were not evidenced from help-center documentation (unreachable); described conceptually.
- The endorsement-graph/network pole (FieldLevel) is unresearched due to HTTP 403; claims about how coach-to-coach endorsement models fit the L0 are unverified. Structurally they would still fit (profiles + discovery + contact), but this is inference, not observation.
- Whether the events layer should eventually be a separate Type: all three sampled products package live-event recruiting as separate apps/product lines (Coach Packet, EventBeacon, CaptainU Events), suggesting the market treats event operations as separable. The directory has an events family in §26 and this leaf keeps the recruiting-events slice.
- Whether commitment tracking is a defining state machine or just a logged outcome: sampled evidence shows logging/celebration ("commitments logged"), not in-platform offer/negotiation machinery. Treated as outcome recording, not a managed offer lifecycle.
- Precise compliance mechanics (what "standardized information" includes; how association co-brands constrain features) are vendor-stated only.

## Final Synthesis

An Athlete Recruiting Marketplace is two-sided recruiting software whose defining core is: a registry of identified prospective student-athletes, each carrying an athlete-authored (or club/family-authored) recruiting profile with sport, class year, athletic and academic attributes and contact details; authenticated college-coach/program accounts; coach-side searchable discovery across the athlete pool by recruiting criteria; and a two-way interest/contact channel between athletes (or their proxies) and coaches — all oriented toward next-level placement, organized by recruiting class years, with commitments recorded as outcomes rather than transacted. Around that core, mature products add video/highlight machinery, academic documents, athlete-side school research and target lists, bidirectional view/interest tracking, roster-need publishing and matching, fit/matching assistance, club and high-school organization accounts with staff-managed promotion, coach-side evaluation workflows with CRM export, tracked messaging, commitment logging, educational content, and mobile apps. The market implements the core across a packaging spectrum — service-heavy memberships with human recruiting coaches, club-workflow-first platforms, freemium app-first products, and events product lines — with the coach side consistently free (partly business model, partly compliance posture) and the athlete/organization side monetized. The boundary to Sports Scouting Platform is structural (who authors and who participates), not vocabulary, since this market uses "recruiting" and "scouting" interchangeably; the boundary to recruit CRMs and admissions systems is registry ownership and two-sidedness.


