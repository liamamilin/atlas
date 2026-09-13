# Research Notes — Golf Tracking / Handicap Application

## Research Goal

Understand what golfer-side golf score-tracking / handicap software actually is as an Application Type: the personal record system an individual player uses to record rounds, derive playing statistics, and maintain a personal handicap figure. Extract the smallest defining structure, the standard mature capabilities around it, the main variants (self-computed handicap vs officially licensed index; manual entry vs sensor tracking), and the boundaries against adjacent leaves (Golf Course Management, generic activity trackers, golf GPS utilities, tournament scoring software).

## Initial Boundary

- This is the **consumer/player side** of golf software. The operator side (tee sheets, bookings, member accounts, pro-shop POS) is the sibling leaf **Golf Course Management**, already documented. The two touch the same "round" concept from opposite sides: the operator schedules and sells capacity; the player records and measures what happened on the course.
- Nearest neighbors:
  - **Golf Course Management** — operator-side business system of record (separate leaf).
  - **Tournament management / live scoring software** (e.g. Golf Genius, or tournament modules inside sampled products) — organizer-side event scoring.
  - **Golf GPS / rangefinder apps** — play aids without a score history; usually a capability inside this Type rather than a separate one.
  - **Generic fitness / activity trackers** — same "log an activity, derive stats" loop but no course/hole/rating structure.
  - **Coaching / instruction platforms** — content and swing analysis; often bundled as a premium add-on.
- Likely confusion axes: (a) self-computed handicap vs officially licensed Handicap Index; (b) score tracking with vs without GPS play aids; (c) manual score entry vs sensor/watch-based shot tracking.

## Research Questions

1. What are the core objects in this software's world? (course, tee, rating/slope, round, hole score, posted score, handicap, stats)
2. What exactly is recorded for a round, and at what granularity (total score vs hole-by-hole)?
3. How does a handicap figure actually come into existence and change? What inputs does the calculation use?
4. What is the relationship between consumer apps and the official handicap infrastructure (World Handicap System, USGA/GHIN, regional associations)? When is a number "official"?
5. What rules govern eligibility and integrity (9-hole rounds, adjusted gross scores, peer review, deletions, course-data corrections)?
6. What statistics do products derive, and how are they used?
7. What play aids (GPS, shot tracking, games) attach to the same scorecard, and which are optional?
8. What interfaces exist (phone live scoring, watch, web, public lookup)?
9. Where are the boundaries against Golf Course Management, tournament software, GPS utilities, and fitness trackers?

## Representative Products

Selected for market representation, documentation quality, and different positioning on the handicap question:

| Product | Positioning | Why sampled |
|---|---|---|
| **18Birdies** | Free consumer all-in-one (GPS + scorecard + social + AI coach); computes its own "18Birdies Handicap" | consumer freemium pole; self-computed handicap posture; strong Tier-1 help center |
| **Golfshot** | Veteran GPS-first tracker (Shot Zoom); posts scores to the official USGA/GHIN Handicap Index via purchase/linking | established consumer pole; official-index posting-channel posture |
| **TheGrint** | Handicap-first consumer app; licensed USGA handicap data affiliate in the US, GHAP partner internationally | handicap-as-center philosophy; documents WHS rules operationally in FAQ |

Considered and not directly usable: Arccos (sensor-based auto shot tracking; transport error), Golf Australia (regional official body app; 403), GHIN (USGA official service; JS-only SPA), whs.com (403), usga.org (403), randa.org (404). See Sources — these gaps reduce assertion strength for the governing-body layer.

## Sources

Research date: **2026-09-08**. All fetches from the research environment; failures abandoned after 1–2 attempts per the network rule.

Fetched successfully [A — directly observed, official]:

- 18Birdies homepage — https://www.18birdies.com/
- 18Birdies handicap page — https://18birdies.com/golf-handicap/
- 18Birdies Knowledge Base: "How is 18Birdies Handicap Calculated?" — https://help.18birdies.com/article/603-18birdies-handicap-how-it-works (Tier 1)
- Golfshot homepage — https://www.golfshot.com/
- Golfshot Handicap Index® page — https://golfshot.com/best-handicap-tracking-golf-app
- TheGrint homepage + embedded FAQ — https://www.thegrint.com/ (Tier 1/2 mix: feature copy + operational FAQ)

Not reachable (recorded limitation, no memory-filling):

- https://www.ghin.com/ — JavaScript-only app shell, no content
- https://www.whs.com/ — 403
- https://www.usga.org/handicapping.html — 403
- https://www.randa.org/en/worldhandicapsystem — 404
- https://arccos.golf/ — transport error
- https://www.golf.org.au/ — 403

Consequence: World Handicap System mechanics are known here **only as operationalized by the sampled products** (which quote WHS rules in their own docs). Governing-body-layer claims are stated at reduced strength.

## Product Observations

### 18Birdies

Positioning and scope [A]:

- "Free Golf GPS App & Rangefinder … Golf Scorecard App … Golf Handicap Calculator … Golf Swing Analyzer - AI Coach … Track Game Results & Payouts … Connect & Compete With Friends."
- Community and discovery: course browser with reviews/photos ("Discover over 40,000 Courses", "46K Courses Worldwide" — vendor-reported), tournaments hosting with registration and live scoring, community section.
- Help-center categories confirm the surface map: Play a Round, Formats & Scoring, Round History & Performance, Shot Tracking, Statistics, Handicap, Courses, GPS, Wearables, Side Games, Tournaments & Leagues, Community, Practice, Tee Times. [A]
- Vendor-reported scale: 10M users, 120M rounds scored. [A — marketing claim, not generalized]

Handicap mechanics (Tier-1 help article) [A]:

- The "18Birdies Handicap" is calculated from **eligible rounds saved in the account** — a self-computed, free handicap figure, not described as a licensed official Index anywhere in fetched pages.
- Inputs per round: Score, Course Rating, Slope Rating, Round date, Round length, Tee selection, Eligible round status. "Course Rating and Slope Rating help account for course difficulty."
- Handicap differential concept, with the formula given verbatim: **Differential = (Score − Course Rating) × 113 / Slope Rating**; "a lower differential generally represents a stronger round."
- Round-count table: from 1–5 eligible rounds only 1 best round is used, scaling up until "20 or more eligible rounds … the most recent 20 … best 8 differentials are included."
- 9-hole rounds: eligible; "a 9-hole score may be converted into an 18-hole equivalent"; requires the 9-hole side's Course Rating and Slope.
- Philosophy: "Your handicap is not an average of all your scores. It is designed to represent your scoring potential based on your better eligible rounds." Newer rounds can replace older eligible rounds.
- Hole-by-hole entry "may help with handicap-related adjustments and more accurate round details" vs total-score entry.
- Integrity controls: a round can be **excluded** from the handicap calculation as a workaround while course data is reviewed; users may enter a **manual custom handicap** instead of the computed one; course-data corrections (rating, slope, par, yardage, hole handicaps) are requested via Support with scorecard evidence.

### Golfshot

Positioning and scope [A]:

- "The world's most powerful and trusted on-course GPS, scoring, statistics, and auto shot tracking app"; "TRUSTED BY 5 MILLION GOLFERS WORLDWIDE" (vendor-reported); "over 45,000 courses worldwide."
- Feature map: GPS distances (to green, hazards, targets), Auto Shot Tracking via Apple Watch, Auto Strokes Gained, Green Maps, Swing ID, Golfscape AR, Voice Assistant, Wearables, Golfplan instruction, Tournament Management, Scoring & Statistics ("Put away the pencil with digital scorecards and statistics"; a review notes "It knows whether you have a GIR by calculation").
- Tee times portal (play.golfshot.com/teetimes) — a consumer marketplace attachment.

Handicap mechanics [A]:

- "Get Handicap Index® or link your existing one to Golfshot for easy score posting and tracking of your Handicap Index® directly from your phone."
- "Purchase your new Handicap Index® right through Golfshot" — via the USGA website in partnership with AGAs (Allied Golf Associations) and the USGA; "Link your existing Handicap Index and start posting immediately. **No kiosks required.**"
- "Handicap Index score posting and management is free to all U.S. Golfshot members"; links to a **GHIN® Number**.
- Interpretation: Golfshot does not present a proprietary handicap on fetched pages — its posture is a **posting channel into the official USGA/GHIN handicap infrastructure** (the phone replaces the club kiosk for posting scores).

### TheGrint

Positioning and scope [A]:

- "Manage your scores, link with your USGA Handicap™, powerful GPS maps, and so much more."
- Score tracking and stats: "18+ detailed stats modules" free / "50+ performance stats" on Pro; "Compare your stats to targets and benchmarks for your skill level"; "Insights — our version of strokes gained."
- GPS: "more than 40k courses worldwide" (vendor-reported), distances to pin/hazards/landing zones; green maps (13k–25k+ courses, figure inconsistent between page sections — vendor copy variance).
- Games & leaderboards: "From Medal and Stableford to Skins, Vegas, Wolf, and many more options … handle all the complex score calculations for you"; multi-games and presses; Teams Cup Mode.
- Smartwatch: Apple Watch / Wear OS — GPS distances, score tracking, shot tracking; health-app integration (iOS).
- Desktop member website for deeper analysis.
- Scorecard Picture Service (SPS): photograph a paper scorecard; the service transcribes and uploads it. Score import tool (spreadsheet copy/paste; vendor-assisted import from other services).

Handicap mechanics and WHS rules (FAQ, operational) [A]:

- "In the US, we are a **licensed handicap data affiliate of the USGA**. One-click upload at the end of your round for nightly handicap revisions. Internationally we have partnered with GHAP (Golf Handicap for Amateurs Platform)."
- Revision cadence: "Handicaps are revised every night, at midnight." Calculation: "Handicaps are calculated using the **lowest 8 Handicap Differentials out of your last 20 scores**. It is NOT calculated using your Scoring Average."
- Adjusted Gross Score: auto-calculated on hole-by-hole upload — "The formula is: **Par + 2 strokes + any Handicap strokes received on the Hole**" (the net-double-bogey cap); with total-score-only entry the golfer must compute it themselves.
- 9-hole / partial rounds: WHS "updated its methodology to allow for 9 hole rounds, or partial rounds (10-17 holes) to be submitted" (since Jan 2024); every two 9-hole scores are **automatically combined** by the USGA process into an 18-hole "Combined ( C )" score; Combined Scores can't be deleted directly — deleting one underlying 9-hole score deletes the combination and may leave the other "widow" score pending a match.
- Peer review & privacy: account can be private, "HOWEVER, your Scores and Handicap **will be visible for anyone who searches for your Name or GHIN#/Handicap ID#**, within the Handicap Lookup tool … because of Handicap Revisions and **for peer review**." Private Upload hides a score from the activity feed but it still counts and stays visible in the scoring record "for Handicap purposes."
- Round lifecycle: live rounds can be paused & exited, resumed from an "Unfinished Round" list, completed or deleted.
- Course data: community "Course Update Tool" — user edits are reviewed, verified, then approved/disapproved by the vendor.
- Handicap economics: official handicap is "sold separately" from the Pro membership; linking an existing HDCP ID (GHIN) is free.

## Cross-product Comparison

| Structure / capability | 18Birdies | Golfshot | TheGrint | Reading |
|---|---|---|---|---|
| Round record: course + tee + date + score | ✔ | ✔ | ✔ | Universal [A×3] → defining-core candidate |
| Course database with tees, par, ratings (CR/Slope) | ✔ (corrections via Support) | ✔ (45k+) | ✔ (40k+, user-edit tool with verification) | Universal [A×3] → defining-core candidate |
| Hole-by-hole score entry | ✔ (recommended for adjustments) | ✔ (digital scorecards) | ✔ (enables auto AGS) | Universal [A×3]; total-score entry also supported → hole-level detail is common structure, not required |
| Personal scoring history archive | ✔ (Round History; handicap round status) | ✔ | ✔ (Scores list; scoring record) | Universal [A×3] → defining-core candidate |
| Handicap figure maintained from history | ✔ — self-computed "18Birdies Handicap" | ✔ — posting into official USGA/GHIN Index | ✔ — official via licensed USGA affiliate (US) / GHAP (intl.) | Universal [A×3], three different postures → defining-core candidate (concept), implementation varies |
| Differential-based potential model (best N of recent M) | ✔ (best 8 of last 20 at maturity, staged minimums) | (delegated to GHIN) | ✔ (lowest 8 of last 20) | [A×2 direct + product-attested WHS] → common mechanism of official-style handicapping |
| Score adjustments (AGS / net double bogey) | ✔ (hole-by-hole "handicap-related adjustments") | (delegated) | ✔ (auto: Par + 2 + handicap strokes) | [A×2] → common; total-score entry requires manual adjustment |
| 9-hole handling / combining | ✔ (converted to 18-hole equivalent) | — | ✔ (WHS combined scores, Rule 5.1b quoted) | [A×2] → common |
| Statistics modules | ✔ (categories incl. Strokes Gained) | ✔ (incl. Auto Strokes Gained, GIR computation) | ✔ (18+ / 50+ modules, benchmarks, Insights) | Universal [A×3] → standard, not defining |
| GPS distances / hole maps | ✔ | ✔ | ✔ | Universal [A×3] → standard play-aid layer |
| Watch/wearable companion | ✔ | ✔ | ✔ | Universal [A×3] → standard |
| Side games / formats computed from scorecard | ✔ (Skins, Wolf, Nassau, Vegas, … up to 10) | — (tournament mgmt instead) | ✔ (Medal, Stableford, Skins, Vegas, Wolf …) | [A×2] → common; format lists are vendor detail |
| Social layer (friends, live scoring, feeds) | ✔ | ✔ (community-ish) | ✔ (friend ranking, live score alerts) | [A×3] → common |
| Official-index channel: purchase / link GHIN | — | ✔ | ✔ (link free; obtain separately) | [A×2] → common in US market; posture varies |
| Score backfill: import / photo transcription | — | — | ✔ (SPS + import tool) | [A×1] → optional, product-specific |
| Manual custom handicap entry | ✔ | — | — | [A×1] → optional |
| Round exclusion from handicap | ✔ (workaround) | — | ✔ (delete/manage scores; combined-score rules) | [A×2] → common eligibility control |
| Course-data correction by users | ✔ (via Support) | — | ✔ (self-service tool + verification) | [A×2] → common |
| Tournament hosting (organizer-side) | ✔ | ✔ | ✔ (Tour events, groups & outings) | [A×3] as *adjacent capability* — organizer semantics |
| Tee times / booking attachment | ✔ (help category) | ✔ (portal) | — | [A×2] → optional commercial attachment |
| Instruction/coaching content | ✔ (School, AI Coach) | ✔ (Golfplan, Swing ID) | — | [A×2] → optional premium layer |

## Canonical Abstraction

### Level 0 — Defining Invariant

Three jointly-held structures; remove any one and the product stops being a Golf Tracking / Handicap Application:

1. **Course-structured round record** — a dated round at a named course and tee set, where the tee set carries course-difficulty ratings, recording the player's strokes (hole-by-hole or as a total). Remove → generic activity tracker with no golf semantics.
2. **Persistent personal scoring history** — the golfer's archive of round records that everything else derives from. Remove → disposable scorecard.
3. **A maintained personal handicap figure derived from that history under a defined handicapping method** — either computed by the application itself, or maintained through an officially authorized index service the application posts into. Remove → a round logger with no ability model (the "Handicap" half of the Type collapses).

Load-bearing jointly-held reasoning: ratings without rounds = course data service; rounds without handicap derivation = scorecard/logger; a handicap figure without the round history behind it = an empty number. All three appear together in every sampled product (in three different postures).

### Level 1 — Common Mature Structure

- Hole-by-hole scoring (live/on-course mode with pause/resume, plus post-round entry), with total-score entry as the fallback.
- Derived statistics: putts, fairways, greens in regulation, driving, penalties, scrambling, strokes-gained-style measures; benchmarks vs skill level.
- Official-index channel: purchasing or linking a GHIN/association handicap ID and posting scores from the app ("no kiosks required").
- Differential-based potential model: scores converted to differentials against course rating and slope; best N of the most recent M rounds; periodic revision.
- Adjusted-score computation (net-double-bogey style cap) from hole-by-hole data.
- 9-hole and partial-round handling, including combination rules.
- Course database at scale (vendor-reported tens of thousands of courses) with community/vendor correction mechanisms.
- GPS play aids: distances, hole maps, green maps; watch/wearable companions.
- Side games and formats computed from the same scorecard; leaderboards.
- Social layer: friends, live scoring alerts, shared rounds, feeds.

### Level 2 — Variant / Optional Structure

- Handicap posture: self-computed app handicap (free calculator) vs licensed affiliate issuing official revisions vs posting channel into association infrastructure (US GHIN-centric) vs international partners (GHAP) vs club/association-only (historical).
- Entry backfill: scorecard-photo transcription, spreadsheet/other-service import.
- Sensor-based shot tracking (hardware/watch automation) vs manual per-shot logging.
- Tee-time booking and tournament hosting attachments (organizer-side adjacency).
- Instruction content and AI swing analysis as premium layers.
- Monetization shape: freemium with stats/GPS gated, handicap sold separately, etc.

### Level 3 — Vendor-specific (Research Notes only)

- 18Birdies: exact staged best-rounds table (1–5→1 … 20→8); verbatim differential formula with the 113 constant; "10M users / 120M rounds scored"; AI Swing Analyzer/Coach; game-payout tracking; the specific game list (Sixes, Dots, Rolling Stroke, Targets…).
- Golfshot: Golfscape AR, Voice Assistant, Swing ID, Green Maps, Auto Shot Tracking via Apple Watch, USGA co-marketing funnel for Index purchase.
- TheGrint: Scorecard Picture Service workflow (press-and-hold upload, queue, transcription guidelines); "revised every night at midnight"; Combined-score widow logic; Drop Zone perks; TheGrint Tour; exact Pro pricing; green-map course-count inconsistency in vendor copy.

## Historical / Market-Sample Check

- **Club handicap computers / association kiosks (pre-smartphone, e.g. GHIN terminals)**: a golfer posts a score; the system maintains the index; no GPS, no stats, no social. Fits the core (round record + history + handicap figure) — confirms the core is not the modern smartphone feature set.
- **Paper scorecard era**: predates the software Type; the digital scorecard is the direct descendant.
- **Basic scorecard-only apps** (track scores, no handicap derivation): would drop core prong 3 — treated here as a **light variant / boundary case** rather than the canonical form, since the leaf names the handicap function and every major sampled product maintains one.
- **Regional variation**: the sampled products are US-centric (USGA/GHIN). TheGrint documents an international partner (GHAP); the WHS is the common global framework products cite. Regional official-body apps (Golf Australia etc.) could not be fetched — the definition keeps the governing layer abstract ("an officially authorized index service under the applicable handicapping rules") to avoid US-overfitting.
- **Rating frameworks**: the specific Course Rating + Slope pair is the current (WHS) implementation; older systems used different difficulty calibrations. The core is therefore stated as "tee sets carrying course-difficulty ratings," not as the specific rating formula.

## Vendor-specific Findings

- Golfshot does not present a proprietary handicap on its fetched pages — only posting/linking into GHIN. Whether it also computes an internal handicap is unverified; not asserted.
- 18Birdies never claims official/licensed status on fetched pages; its "18Birdies Handicap" is treated as a self-computed estimate. Its manual custom-handicap option exists specifically "if you want to use your own number."
- TheGrint is the only sampled product documenting the full WHS rule surface in user-facing operational terms (combined scores, AGS formula, revision cadence, peer-review lookup).

## Boundary Findings

| Neighbor | Relationship | Distinction test |
|---|---|---|
| **Golf Course Management** (separate leaf) | operator vs player | Operator side owns the tee sheet, reservations, revenue, member accounts; this Type owns the player's personal round history and ability model. Remove the operator's capacity/revenue structures and add a personal score history → this Type. |
| Tournament management / live-scoring software | adjacent capability, sometimes bundled | Organizer-first: event setup, flights, rule engines, published results for many players at once. Player-first: one golfer's ongoing history. Sampled products add tournament hosting as an attachment without changing their core. |
| Golf GPS / rangefinder utilities | subset capability | Pure GPS apps have play aids but no score history, no handicap. GPS is a standard layer of this Type, not its definition. |
| Generic fitness / activity tracker | different domain structure | Activity trackers log workouts with duration/heart-rate primitives. Remove course/tee/rating/hole structure → fitness tracker; that structure is what makes this Type golf. |
| Coaching / instruction platforms | adjacent content layer | Instruction-first products sell learning content and swing analysis; sampled products bundle them as premium layers. The record-keeping core is the Type. |
| Online golf communities / social feeds | partial overlap | Community features exist in all sampled products but attach to the score record; a product whose core is feeds/forums without round recording is a community product. |

"去掉什么就变成另一个 Type" judgments:
- Remove course/tee/hole/rating structure → generic activity tracker.
- Remove the personal history and keep only today's round → ephemeral scorecard / GPS utility.
- Remove the handicap derivation and keep history+stats → still golf tracking but no longer the "Handicap Application" named by the leaf (light variant).
- Add operator capacity/booking/revenue structures → Golf Course Management (other side of the same round).

Taxonomy check: the leaf stands as an independent Type. It partitions the golf domain cleanly against Golf Course Management (operator) and does not collide with any other directory node. No directory change proposed.

## Uncertainties

1. Governing-body primary sources (WHS, USGA, R&A, GHIN, Golf Australia) were unreachable from the research environment; WHS mechanics are known only as operationalized by sampled products. Claims about the official layer are stated at product-attested strength.
2. Whether self-computed consumer handicaps (18Birdies) are accepted anywhere as "official" is unknown from fetched pages; not asserted either way.
3. Golfshot's possible internal (non-GHIN) handicap computation is undocumented in fetched pages.
4. Sensor-based tracking products (Arccos, Shot Scope) were not directly observed; the sensor variant is documented only at the level of Golfshot/TheGrint watch-based auto-shot-tracking features.
5. Regional-official apps (outside the US) could not be observed; the international posture beyond GHAP is inferred from TheGrint's copy only.

## Final Synthesis

A Golf Tracking / Handicap Application is the golfer's personal record system for the game. Its world is built on the round record: a dated round at a named course and tee set, scored in strokes, joined to a course database whose tees carry difficulty ratings. The golfer's rounds accumulate into a persistent scoring history, and from that history the application maintains a personal handicap figure — computed by the application itself, or maintained by posting into an officially authorized index service — alongside derived statistics that profile the player's game. Mature products wrap this core with on-course play aids (GPS, hole and green maps, watch companions), side-game and format computation from the same scorecard, social layers, score backfill, and course-data correction mechanisms. Products differ most in handicap posture — self-computed estimate, licensed affiliate of the governing body, or posting channel into association infrastructure — and in how much of the game experience (games, coaching, tournaments, tee times) they bundle around the record-keeping core. The Type is the player-side mirror of Golf Course Management: the operator schedules and sells the round; the player records and measures it.
