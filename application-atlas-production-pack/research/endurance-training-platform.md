# Research Notes — Endurance Training Platform

Research date: 2026-09-07
Slug: endurance-training-platform
Directory leaf: Endurance Training Platform (§28 Sports, Fitness & Recreation)

---

## Research Goal

Understand what an Endurance Training Platform actually is as an Application Type: what objects it is built around, how the training process flows through it, which structures are definitional vs merely common in today's market, and where its boundaries sit against sport-specific training applications, generic workout software, coaching products, and AI-coach products.

---

## Initial Boundary (hypothesis before research)

- **What it is (hypothesis):** a system of record for the endurance training process — planning structured training over weeks/seasons, prescribing workouts, capturing completed training, analyzing it against the plan, and tracking accumulated training load/fitness — spanning endurance sports (running, cycling, swimming, triathlon, rowing…).
- **Primary users (hypothesis):** self-coached endurance athletes; endurance coaches managing athlete rosters; teams/clubs.
- **Nearest neighbors:** Running Application / Cycling Application / Swimming Training Application (sport-specific siblings), Workout Tracking Application, Workout Programming Application, Online Fitness Coaching, Personal Training Management, AI Fitness Coach, Wearable Fitness Platform, Fitness Progress Tracker, Race Management Platform, Nutrition Coaching Platform.
- **Prior passes that constrain this one:**
  - cycling-application (processed 2026-09-07): "vs Endurance Training Platform (plan/coach-centric vs ride-centric)" — this Type is plan- and coach-centric structured training across sports; the ride is training input, not the unit of record.
  - ai-fitness-coach (processed 2026-09-06): family test "who adapts the plan" — software (AI coach) vs human coach vs nobody; vendors increasingly bundle all three; gradient, not a wall.
- **Unknowns at start:** Is the coach layer definitional? Is adaptive/algorithmic planning definitional? Is structured-workout execution (indoor trainer control) definitional? Is the load-metric machinery (fitness/fatigue/form) definitional or common?

---

## Research Questions

1. What are the core objects? (athlete, coach, plan/calendar, workout planned vs completed, thresholds/zones, load metrics, events, equipment, wellness data)
2. What is the workout lifecycle? (plan → prescribe → execute → sync → analyze → adapt)
3. What coach–athlete machinery exists? (attachment, prescription, comments, monitoring)
4. Is the training-load science (TSS-style scoring, fitness/fatigue/form, power curves) definitional or common? Does it survive the historical check?
5. How do devices/files/structured workouts move in and out? (autosync, FIT/ZWO/ERG export, watch/trainer execution)
6. How is multi-sport modeled? (per-sport zones/thresholds, triathlon)
7. How are events/races handled? (priorities, periodization, taper)
8. What are the market poles/variants? (coach-first vs athlete-first vs algorithm-first; free vs paid; team/club layer)
9. Where exactly are the Type boundaries?
10. What is the commercial posture? (background only, not definitional)

---

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer levels:

| Product | Philosophy / pole | Primary customer |
|---|---|---|
| TrainingPeaks | canonical coach↔athlete multi-sport training system of record ("complete training platform"); plan marketplace + coach match; trademark holder of the industry's load vocabulary (TSS/IF/NP) | coaches + committed athletes, pro teams/federations |
| TrainerRoad | athlete-first, adaptive algorithmic training ("your personal coach" is software); cycling-lens with tri/off-road plans; indoor structured-workout execution | self-serve individual cyclists/triathletes |
| Intervals.icu | free, community-built, analytics-first platform that has grown planning + coaching surfaces; open API | individual data-oriented athletes, budget coaches |
| Final Surge | coach/team-side platform for coaching businesses, teams and clubs; free athlete tier; plan marketplace; attendance rosters | coaches, coaching companies, HS/college/pro/club teams |

Note on TrainerRoad sampling: TrainerRoad self-labels "cycling's #1 training app", but its structure is plan-first (Plan Builder → structured workouts → adaptation loop), with rides/runs/swims ingested as training inputs — structurally an instance of this Type with a cycling lens, not of Cycling Application (ride-centric). Recorded in Boundary Findings.

---

## Sources

Evidence quality per product (accessed 2026-09-07):

| Source | Status | Evidence value |
|---|---|---|
| TrainingPeaks root (trainingpeaks.com) | fetched, full | Tier 2 positioning: PLAN/TRAIN/LIFT, plan search, coach match, Virtual, strength, device logos |
| TrainingPeaks Athlete User Guide (/learn/trainingpeaks-athlete-user-guide/) | fetched, full | Tier 1: account/zones/calendar/QuickView/Expanded View/Athlete Home/Dashboard/ATP documentation |
| TrainingPeaks "What is TSS?" (/learn/articles/what-is-tss/) | fetched, full | Tier 1 education: TSS definition, all-sport applicability, PMC link |
| TrainingPeaks "What is the Performance Management Chart?" | fetched, full | Tier 1 education: CTL/ATL/TSB definitions (42-day/7-day/fitness−fatigue) |
| TrainingPeaks Help Center root (help.trainingpeaks.com) | fetched, root only | Category taxonomy: Athlete Support / Coach Support / Device & Sync / Account & Billing / TrainingPeaks Virtual / Training & Analysis; promoted articles: Structured Workout sync and Manual Export, Garmin Connect sync, Apple Watch workouts, Coach Account Pricing |
| TrainingPeaks help-center category pages | **403 / timeout — inaccessible** | limitation recorded; coach-side mechanics asserted from user guide + root taxonomy only |
| TrainerRoad root (trainerroad.com) | fetched, full | Tier 2: AI adaptive positioning, import→personalize→export→results loop, TSS/FTP vocabulary, RLGL |
| TrainerRoad Cycling Training Plans page | fetched, full | Tier 1-2: Plan Builder mechanics, Base/Build/Specialty, volumes, disciplines, structured-training philosophy |
| TrainerRoad support.trainerroad.com | **transport error — inaccessible** | limitation recorded; assertions kept at product-page strength |
| Intervals.icu root (intervals.icu) | fetched, full | Tier 2: four feature pillars, integrations, pricing/community model |
| Intervals.icu /features/plan/ | **JS-rendered; fallback static block only** | analyze-side mechanics from fallback; plan-side from homepage cards |
| Final Surge root (finalsurge.com) | fetched, full | Tier 2: athlete/coach/team positioning, autosync of planned+completed, plans, free tier |
| Final Surge /features | fetched, full | Tier 2: builder, structured sync, analysis, comments/mailbox, attachments, social walls, Premium |
| Final Surge /coaches | fetched, full | Tier 2: builder, multi-athlete calendars, libraries, coaching business, rosters, marketplace |

No paid/leaked materials used; no content taken from model memory where sources were unreachable — claims degraded instead.

---

## Product Observations

### TrainingPeaks (evidence: A on all items below unless noted)

**Positioning (root):** "Your complete training platform… Built for the world's most complete athletes and coaches." Separate athlete and coach signups. Three pillars: PLAN (structured workouts, training plans from top-tier coaches, find a coach), TRAIN ("train for any sport, with any device, any time indoors and out"; TrainingPeaks Virtual indoor riding), LIFT (strength training: 1,000+ video-guided movements; "Workouts sync to your calendar and factor directly into your fitness and fatigue scores"). Long integration list (Garmin, Zwift, Wahoo, Suunto, Polar, Coros, Apple Watch, Whoop, Oura…). Client logos include national federations and WorldTour teams.

**Athlete User Guide (Tier 1):**
- **Account/connections:** profile; subscriptions; **Coaches panel** ("view which coaches you are currently attached to or shared with, request a new coach, or share yourself with a coach by entering their email address"); calendar export URL to third-party calendars (Premium); **email digest of upcoming workouts**; **Apps and Devices** management (Garmin autosync, HRV data); notifications for "uploaded workouts, comments from your coach, or suggested threshold changes"; data export.
- **Zones:** "TrainingPeaks requires thresholds to calculate metrics for deeper workout analysis and modeling training load through the Performance Management Chart." Thresholds/zones set **per sport** (HR for bike/run, power for bike, pace for run/swim); default thresholds used if a sport's threshold is unset; zones calculator methods; **threshold-change detection** with optional auto-apply.
- **Nutrition:** calorie goals combining intake with workout expenditure; MyFitnessPal sync.
- **Equipment:** bikes/shoes tracked with **mileage automatically accrued from completed workouts**.
- **Calendar (the center):** add workout / metric / goal / event; **Workout Builder** — "create a structured workout containing detailed intervals based on your individual threshold"; **Strength Builder** — structured strength workouts from a stock exercise library with video demos, custom exercises; **workout libraries** for reuse (drag from library onto calendar); file upload via device, drag-and-drop onto the correct day, or autosync; **QuickView** (summary metrics; HR/power/pace sidebars); **Expanded View** (charts library, pre/post-activity comments, elevation correction, file download, recalculation).
- **Compliance colorization (layout option):** completed workouts colorized by compliance with planned duration/distance/TSS — green ±20%, yellow 50–79%/121–150%, orange >50% deviation, red not completed, grey unplanned. *(exact thresholds = vendor-specific, kept here only)*
- **Athlete Home:** weeks until next 'A' priority event; upcoming events; goals; upcoming workouts; **today's Fitness, Fatigue, Form + ramp rates**; zones for upcoming workouts; recent peak performances.
- **Dashboard:** drag-and-drop charts from a charts library; customize by date range/sport; **Performance Management Chart** to model Fitness/Fatigue/Form and "plan the perfect peak for your goal Event."
- **Annual Training Plan (ATP):** "periodizes (systematically varies the intensity and duration of workouts) planned training through a season… plan their peak to coincide with their goal Event." Creation wizard: name, date range, periodization type, current fitness, recovery cycle, methodology, planned by average weekly hours / TSS / target event Fitness (CTL); **events added with date and priority; one 'A' priority event required for automatic periodization**; ATP minimum length 9 months *(vendor-specific)*; recalculation; manual drag adjustment of planned CTL/ATL/TSB blocks.

**What is TSS (education):** TSS = Training Stress Score — "quantify workouts based on relative intensity, duration, and frequency"; "100 points earned by a pro is relatively the same as 100 points earned for a beginner because TSS is relative to each person's individual threshold"; "works for triathletes, cyclists, runners, and swimmers… any workout that contains power, pace, or heart rate data"; RPE-based estimation possible when no data; heritage: Bannister's TRIMP; Coggan & Allen. PMC tracks the "entire training program on one all-encompassing graph."

**PMC article (education):** daily TSS dot per day; Fatigue (ATL) = exponentially weighted 7-day average of stress; Fitness (CTL) = exponentially weighted 42-day average; Form (TSB) = yesterday's fitness − yesterday's fatigue; tapering sheds fatigue faster than fitness; performance-insights overtraining hints. *(exact windows/formulas = product-published detail; the concept = fitness/fatigue/form modeling)*

**Help-center root taxonomy (structural confirmation):** Athlete Support / Coach Support / **Device & Sync** / Account & Billing / **TrainingPeaks Virtual** / **Training & Analysis** / Product Updates. Promoted: Structured Workout sync and Manual Export; How to Sync Garmin Connect; Apple Watch workout visibility; Coach Account Pricing & Billing.

### TrainerRoad (evidence: A at product-page level; support site inaccessible)

**Positioning (root):** "Get Faster with the #1 Cycling Training App. TrainerRoad AI finds the right workout for every ride and adjusts to you in real time." Four-step loop: **Import Your Data** (analyzes workout history from Strava/Garmin) → **Personalized Training** (builds workouts and plans adapting to fitness/goals/performance) → **Workout Anywhere** (indoors or outside; Zwift, Garmin, Wahoo, Hammerhead export) → **Real Results** (progress insights). "Your Personal Coach — just sync your data, we'll handle the rest." "AI FTP Detection" replaces test days. **RLGL ("Real Life Gets in the Way")**: vacations, sickness, missed/crushed workouts, extra group rides → plan adapts; too-hard outside rides auto-assign rest days. Structured vs unstructured workout contrast. Runs, swims, hikes "automatically feed into your training plan for analysis and adjustment". Uses TSS progression charts; footnote: "NP, IF and TSS are trademarks of Peaksware, LLC" (industry adoption of TrainingPeaks vocabulary).

**Cycling Training Plans page:** **Plan Builder** — "enter your upcoming events, how much you can train and when you want to do it"; custom plans "up to two years into the future"; peaks fitness for the goal event. Discipline-specific plan catalogs: road (climbing road race, criterium, gran fondo, rolling road race, time trial), triathlon (full/half/Olympic/sprint), off-road (XCM, XCO, cyclocross, gravity, short track). **Base / Build / Specialty** phase cycle (28 weeks standard; Plan Builder compresses to your timeline). Volumes low/mid/high (≈3/5/6 structured workouts per week — vendor-specific). Science-based philosophy: structured power-based interval training, progressive stress, event-specific specialty with reduced volume. Indoor execution: pair trainer + sensors to the app; guided structured workouts; side-by-side Zwift or workouts pushed into Zwift.

### Intervals.icu (evidence: A at product-page level)

**Positioning (root):** "Free Cycling, Running, Triathlon Training Platform… A free training platform built by athletes, for athletes. Powerful analytics, structured training, and a passionate community." 160,000+ active athletes; 193M+ activities analyzed; since 2018; free; Supporter tier $4/mo.

**Four pillars:**
- **Track Your Progress:** "Monitor fitness, fatigue, and form across all your sports" — **Fitness Chart** ("classic Performance Management Chart"; historical download from Strava/Garmin; **automatic eFTP estimation from single maximal efforts keeps zones up to date**); **Multisport** — "separate zones and settings per sport… tracks each discipline independently with appropriate metrics"; **Power Curve** — season comparison, W/kg, MAP estimation, power models (eFTP, Morton's 3P, Monod & Scherrer).
- **Analyze Your Activities:** activity timeline with Coggan metrics + own metrics; **automatic interval detection** (also: "automatically detects intervals so you can ride your favourite route… Forgot to hit the lap button? No problem!"); power charts (zone distribution, 42-day power curve, best efforts); **decoupling/cardiac-drift aerobic-efficiency analysis**; spike detection/correction; manual data editing.
- **Plan Your Training:** **Custom Zones** (zones for any stream, anchored to FTP/LTHR/custom fields; used for workout prescription and time-in-zone analysis); **Training Calendar** (drag-and-drop; import from third-party calendars; workout library; sync to devices/platforms; weekly totals); **Workout Builder** (structured steps targeting power/HR/pace/cadence; **import/export ZWO/FIT/MRC/ERG**; text-based).
- **Communicate:** **Chat** (share workouts/activities with team); **Ask A Coach** (connect with professional coaches inside the platform); **Athletes** management (follow and coach athletes; tag/organize).
- **Extend & Integrate:** **Open API** (REST; upload/download activities, wellness data, create workouts, webhooks; OAuth2/API key); 200+ third-party integrations (250+ claimed); **Custom JavaScript** extensions (computed fields, custom streams, custom charts) shared with community.

**Integrations:** Strava, Garmin, Wahoo, Zwift, Coros, Polar, Suunto, Amazfit, Huawei, Concept2, MyWhoosh, Hammerhead, Rouvy, Dropbox, Oura, WHOOP. **Community:** forum-driven features, 21 languages. **Supporter tier:** annual training plan builder, teams and coaching organizations, bulk athlete configuration, route matching. **Events:** grand-tour spectator dashboards (adjacent surface).

### Final Surge (evidence: A at product-page level)

**Positioning (root):** "Train and Coach with a Purpose. For athletes, coaches, teams and clubs." Flexible approaches to "Training, Tracking, Communication." **Auto-sync planned and completed data** from Garmin Connect, Strava, TrainerRoad, and more. "No Coach? No Problem" — training plans marketplace (instant access to world-class coaching). Coaches: "consistent athlete communication; quick access to all your athletes; workout builder and custom workout library; monitor athlete performance, recovery, and feedback data; great for individual coached athletes, coaching companies, high school, collegiate or club teams of any size." **Free from ads/charges/limits** — all features in the free athlete account. Client logos: New York Road Runners, Rock 'n' Roll Marathon Series, HOKA NAZ Elite, Tinman Elite, 80/20.

**Features page:** **Workout Builder** ("build structured workouts" and "sync or export planned workouts to platforms like Garmin Connect, Apple Watch, TrainerRoad, and ZWIFT"; structured workouts displayed on a Garmin watch); **Athlete Premium** in-app purchase (HRV & Morning Readiness, Weather & Forecasts, Route Builder, Athlete Page); **Apple Health + Watch** (sync workouts + health metrics: sleep, resting HR, HRV; **send planned structured workouts to Apple Watch**); **Pain and Injury Report (PAIR)** (track pain location/level/duration; share with coach); **Analyze Workout and Target Zone Details** (pace/HR/power/cadence; time-in-zone); **Communication** (workout comments; Mailbox messages to individuals, multiple athletes, teams); **Videos & Attachments** on workouts (video instruction, images, PDFs); **Team Social Walls** (private social experience for athletes/teams/clubs).

**Coaches page:** structured builder managing **multiple target types within one workout (pace, heart rate, power)**; multi-athlete management (**multi-calendar view** for teams/disciplines/training groups); planning from **workout library** (drag-drop onto athlete calendars, **copy weeks of training, save and apply full training plans**); data dashboards for athlete performance; PAIR; attachments; communication trio (comments/mailbox/social walls); **Coaching Business** (recurring monthly subscriptions, payments for programs/products, **intake questionnaires**, **waivers with digital signatures**); **Training Plan Marketplace** (sell plans); **Attendance Rosters** (group workouts/events; manual or **GPS self check-in**); teams of any size (HS/college/pro/club).

---

## Cross-product Comparison

| Structure | TrainingPeaks | TrainerRoad | Intervals.icu | Final Surge | Verdict |
|---|---|---|---|---|---|
| Planned-first training calendar (plan of record) | ✔ calendar + ATP (season) | ✔ Plan Builder calendar (adaptive) | ✔ drag-drop training calendar + ATP builder | ✔ athlete/team calendars + saved plans | **L0** — universal; the defining container |
| Planned workout vs completed workout compared | ✔ compliance colorization, planned vs actual | ✔ plan adapts to completed/uncompleted; outdoor rides feed plan | ✔ planned workouts vs completed activities on calendar; weekly totals | ✔ "auto-sync planned and completed data"; coach monitors | **L0** — universal closed loop |
| Completed-workout capture (device/file/manual) | ✔ autosync/drag-drop/upload | ✔ import from Strava/Garmin; indoor app records | ✔ from 250+ platforms; manual edit | ✔ Garmin/Strava/TrainerRoad/Apple Watch sync | **L0 capture** (mechanism variant) |
| Accumulated training-state accounting | ✔ PMC (CTL/ATL/TSB), ramp rate, dashboards | ✔ TSS progression, FTP/insights | ✔ fitness/fatigue/form chart, power curves, weekly stats | ✔ data dashboards, coach monitoring | **L0** (concept); specific formulas = L1/product |
| Multi-sport endurance scope | ✔ any endurance sport; per-sport zones | ✔ cycling lens; tri plans; runs/swims ingested | ✔ cycling/run/tri/row; per-sport zones | ✔ "any sport" (running-heavy client base) | **L0** (endurance domain), with sport-lens variants |
| Thresholds + zones machinery | ✔ per-sport thresholds anchor all metrics | ✔ FTP anchors everything | ✔ FTP/LTHR anchors; custom zones | ✔ target types pace/HR/power | **L1** — near-universal intensity backbone in mature products |
| Structured workout builder + export | ✔ builder (interval steps) + sync/manual export | ✔ native structured workouts; export to Garmin/Wahoo/Zwift | ✔ builder + ZWO/FIT/MRC/ERG import-export | ✔ builder + sync to Garmin/Watch/Zwift/TrainerRoad | **L1** |
| Two-way device/platform sync | ✔ planned out, completed in (Garmin etc.) | ✔ import in, workouts out | ✔ in + out, API | ✔ planned + completed auto-sync | **L1** |
| Fitness/fatigue/form modeling | ✔ PMC (defining vendor of the canon) | ✔ TSS-based progression, recovery-aware | ✔ "classic Performance Management Chart" | ✔ weaker evidence: dashboards/recovery monitoring | **L1** (concept universal at mature pole; FS depth unverified) |
| Events/races with priority + periodization | ✔ ATP: A/B/C priorities; automatic periodization | ✔ events drive Plan Builder; Base/Build/Specialty; taper | ✔ annual training plan builder (Supporter) | ✔ plans target events | **L1** |
| Plan/workout libraries + marketplace/templates | ✔ plan marketplace + workout libraries | ✔ plan catalog + Plan Builder | ✔ workout library; third-party calendar import | ✔ workout library + full-plan library + marketplace | **L1** |
| Coach–athlete attachment & feedback | ✔ attach/share coach; comments; notifications | ✖ (software-as-coach positioning) | ✔ follow/coach; chat; Ask A Coach | ✔ core: comments/mailbox/social walls; monitoring | **L1** — common but not definitional (self-coached mode exists in 3/4) |
| Multi-athlete coach roster/teams | ✔ coach accounts (Coach Support category; pro teams) | ✖ | ✔ athlete management, tags; teams (Supporter) | ✔ multi-calendar view, teams/clubs, attendance rosters | **L1/L2** |
| Wellness/recovery data intake (HRV, sleep) | ✔ HRV connections; notification of threshold suggestions | ✔ recovery-aware adaptation (indirect) | ✔ wellness data via API; Oura/WHOOP sync | ✔ Apple Health HRV/sleep; Morning Readiness (Premium) | **L1/L2** |
| Adaptive/algorithmic planning | ◐ threshold auto-apply; plan recalculation | ✔ core identity (AI adapts everything) | ◐ eFTP auto-estimation updates zones | ✖ human-led | **L2** — who adapts is a philosophy pole, not the Type |
| Indoor execution surface (virtual/guided player) | ◐ TrainingPeaks Virtual | ✔ native player + Zwift push | ✖ (exports to others) | ✖ (exports to others) | **L2** |
| Strength / nutrition adjacent modules | ✔ LIFT pillar; nutrition + MyFitnessPal | ◐ strength calculator | ✖ | ◐ (attachments/videos) | **L2** |
| Team/club layer (social walls, rosters) | ◐ pro/federation use | ✖ | ◐ teams (Supporter) | ✔ social walls, attendance rosters | **L2** |
| Open API / extensibility | ◐ data export | ✖ | ✔ REST API, webhooks, custom JS | ✖ (not evidenced) | **L2** |
| Free-tier / commercial posture | premium athlete + coach tiers | flat subscription | free + supporter | free athletes, paid coaches | **L3-adjacent** (background) |

Legend: ✔ observed; ◐ partial/indirect evidence; ✖ not observed.

---

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

An Endurance Training Platform is recognizable as such only if all three hold:

1. **The planned training schedule as plan of record.** A dated, persistent calendar/schedule of prescribed workouts that exists *before* execution and accumulates across weeks/seasons. It may be built by the athlete, received from a human coach, adopted from a template/marketplace plan, or generated by an algorithm — the author is not definitional. *Remove → a workout tracker / activity feed (log after the fact, nothing planned ahead as the governing object).*
2. **The workout as a planned-vs-completed unit.** Each planned workout can be executed (indoors, outdoors, guided or free) and its completion captured — by device/file sync, structured-workout import, or manual entry — and held *against the prescription* so that done-vs-planned is always expressible. *Remove → a plan-delivery/download service or a disconnected log.*
3. **Accumulated training-state accounting.** Completed training aggregates over time into load/progression/state views (however computed or assessed) that feed the next planning decision — the platform, not a spreadsheet beside it, carries the training state across the season. *Remove → a one-shot plan generator with disconnected logs.*

Historical check: paper training diaries + coach-by-mail plan sheets satisfy the loop (plan sheet = plan of record; diary = captured completions; coach's standing review = state assessment); pre-cloud desktop training logs with plan columns satisfy it. GPS tracks, power meters, cloud sync, structured-workout files, subscription billing — all modern implementations, none definitional.

### L1 — Common Mature Structure (cross-product commonality)

- **Threshold + zone machinery per sport** as the intensity backbone (FTP, LTHR, pace thresholds; zones drive prescription and analysis).
- **Structured workout builder** (interval steps with targets) + **structured-workout export/sync** to watches, head units, trainer platforms.
- **Two-way device/platform autosync**: planned workouts pushed out; completed activities pulled in.
- **Fitness/fatigue/form performance modeling** over the accumulated record (the "Performance Management Chart" canon; every sampled product at the mature pole has some fitness/fatigue/form or progression surface).
- **Event/race targeting**: dated events with priorities; periodized phases (base/build/specialty-class); taper/peak logic.
- **Plan & workout libraries**, template/plan marketplaces or catalogs; reuse machinery (copy weeks, apply plans).
- **Coach–athlete attachment** with prescription on the athlete's calendar, comments/feedback, and monitoring dashboards (present in 3/4 sampled; absent where software replaces the coach).
- **Coach/roster management** for coaching businesses and teams.
- **Wellness/recovery intake** (HRV, sleep, weight) informing the training picture.
- **Personal surfaces**: athlete home (next goal event, upcoming workouts, today's state), dashboards with configurable charts, weekly summaries.

### L2 — Variant / Optional Structure

- **Plan-authority pole** — who prescribes and adapts: human coach (TrainingPeaks, Final Surge), self-coached athlete (TrainingPeaks, Intervals.icu), adaptive algorithm (TrainerRoad; threshold auto-apply; eFTP auto-estimation). This is the ai-fitness-coach seam; here it is a variant, not the definition.
- **Sport lens** — cycling-first (TrainerRoad), triathlon-rooted multi-sport (TrainingPeaks), community multi-sport analytics (Intervals.icu), any-sport coaching business (Final Surge).
- **Indoor execution depth** — native guided player + trainer control (TrainerRoad), bundled virtual riding world (TrainingPeaks Virtual), export-only.
- **Team/club layer** — social walls, attendance rosters, group calendars (Final Surge deepest; pro-team use across sample).
- **Adjacent bundled domains** — strength training modules, nutrition/calorie machinery, virtual racing, spectator event dashboards.
- **Commercial posture** — free community (Intervals.icu), freemium athlete (Final Surge/TrainingPeaks), flat subscription (TrainerRoad), coach-paid tiers.
- **Extensibility** — open REST API, webhooks, custom charts/scripts (Intervals.icu), data export (TrainingPeaks).

### L3 — Vendor-specific (research notes only; must not enter the final document)

- TrainingPeaks: TSS®/IF®/NP®/CTL®/ATL®/TSB® are **registered trademarks of Peaksware LLC** (industry-wide adoption; TrainerRoad's footer acknowledges them); compliance color thresholds (±20% green etc.); ATP minimum 9 months; one 'A' event required for automatic periodization; 1,000+ strength movements; TrainingPeaks Virtual brand.
- TrainerRoad: pricing ($209.99/yr ≈ $17.45/mo; $21.99 monthly); 30-day guarantee; 28-week Base/Build/Specialty; low/mid/high = ~3/5/6 structured workouts/week; AI FTP Detection; RLGL; 30M+ workouts completed claim; Plan Builder horizon up to 2 years.
- Intervals.icu: eFTP estimation from a single 60s+ maximal effort; 42-day power curve; Morton's 3P and Monod & Scherrer power models; Supporter $4/mo; 250+ integrations; 200+ API consumers; 21 languages; custom JavaScript charting; grand-tour spectator dashboards; since 2018; 160k+ athletes / 193M+ activities claims.
- Final Surge: PAIR pain/injury report; attendance rosters with GPS self check-in; coaching-business subscriptions/waivers/intake questionnaires; "free from ads/charges/limits" posture; named client teams.

---

## Rejected Findings (considered, not promoted)

- **TSS/CTL/ATL/TSB as definitional.** Rejected: these are one vendor's trademarked implementation of load accounting; TrainerRoad and Intervals.icu adopt the vocabulary but the L0 concept is "accumulated training-state accounting," which older/traditional products satisfy without the formulas. Also fails the historical check (paper-era).
- **Thresholds/zones as definitional.** Rejected to L1: universal in mature products, but a coach running a paper-era program prescribes without computed zones; the loop still holds.
- **Structured workouts / indoor execution as definitional.** Rejected to L2/L1: structured prescription is common but plan-of-record + completed-capture works with plain-text prescriptions (paper-era; and Final Surge "no coach" plans are prose + targets).
- **Coach relationship as definitional.** Rejected to L1: self-coached mode is a first-class posture in 3/4 sampled products; TrainerRoad has no human coach layer at all.
- **Adaptive AI planning as definitional.** Rejected to L2: that would collapse this Type into AI Fitness Coach; here the plan-authority is a pole.
- **Multi-sport as definitional.** Retained in L0 as "endurance-sport scope" but per-sport configuration is L1. A cycling-only platform (TrainerRoad) still fits via "endurance sports with a dominant lens" — the domain is endurance training, not a single sport's activity record.
- **"Platform" = open API.** Rejected: extensibility is an L2 posture (Intervals.icu); the other sampled products are closed platforms.

---

## Boundary Findings

| Neighboring Type | Relationship | Distinction / "remove what → becomes the other" |
|---|---|---|
| Running / Cycling / Swimming Training Applications (sport-specific siblings) | adjacent, high traffic | Sport apps are **record-centric**: the GPS activity/ride/swim is the unit of record (cycling pass: "plan/coach-centric vs ride-centric"). Here the **workout-in-plan** is the unit; sport activities are inputs to the training process. Remove the plan-of-record → a sport training app; add a ride-record-first center of gravity → Cycling Application. TrainerRoad demonstrates the seam: self-labeled "cycling training app" but structurally plan-first → belongs HERE as a cycling-lens variant. |
| Workout Tracking Application | adjacent | Tracker logs workouts after the fact with no governing plan and no season arc. Remove the planned-first calendar → workout tracker. |
| Workout Programming Application | adjacent, gradient | Programming prescribes workouts (sets/reps or intervals) but the endurance platform closes the loop: prescription + capture + accumulated state + season periodization with endurance semantics (thresholds, load). Remove the record-and-accumulate loop → programming tool. |
| AI Fitness Coach | adjacent, gradient (already flagged by ai-fitness-coach pass) | There, *software performing the coach loop is the defining property*; here the managed training process is defining and the adapter's identity is a variant. TrainerRoad sits on the seam (adaptive AI + full system of record). Joint review recommended. |
| Online Fitness Coaching / Personal Training Management | adjacent | Those Types center the coaching relationship/business (general fitness); here the center is the training-process system of record; coach machinery is one L1 layer inside it. |
| Wearable Fitness Platform | adjacent | Device-hub + general wellness vs training-process record. Wearables appear here as data sources (HRV/sleep) — an L1/L2 intake, not the center. |
| Fitness Progress Tracker | adjacent | Body-metric progress (weight, measurements) vs training process. |
| Race Management Platform | different side of the same event | Organizer-side registration/results vs athlete-side preparation. Events appear here as *targets* the plan is built around (A/B/C priorities), not as operations. |
| Nutrition Coaching Platform / Meal Planning | adjacent domain | Nutrition appears here as an adjacent module (calorie goals, sync) — not the managed process. |
| Team Messaging / Community platforms | functional overlap only | Comments/mailbox/social walls here are coaching-collaboration surfaces bound to training objects, not standalone communication Types. |

Seam worth watching: **TrainerRoad-class products blur into AI Fitness Coach**, and **marketplace plans blur into Coaching Commerce** (Final Surge/TrainingPeaks sell plans; coaching-business tooling exists). Both recorded as gradients; no taxonomy change proposed.

---

## Uncertainties

1. TrainingPeaks help-center **category pages** were inaccessible (403/timeout; root reachable) — coach-side mechanics (roster permissions, plan exchange details) asserted from the Athlete User Guide + education articles at moderate strength.
2. TrainerRoad **support site** unreachable (transport error ×1, abandoned per policy) — TrainerRoad mechanics asserted at product-page level only; its two pages are unusually detailed (loop, phases, volumes) so confidence is adequate but not Tier-1.
3. Intervals.icu feature **subpages are JS-rendered**; plan-side details (ATP builder depth) come from the homepage cards + Supporter tier list; analyze-side from the fallback static page. Moderate strength.
4. Final Surge **help center** not fetched; mechanics from three product pages (consistent with each other), moderate strength. Depth of its fitness/fatigue/form modeling unverified — kept out of strong claims.
5. Evidence for wellness/recovery intake is Tier-2 across all products; treated as L1/L2, never L0.
6. Historical breadth: the paper-era check is an inference from the L0 structure (plan sheet + diary + standing review), not from documented paper-era software; flagged in the final document as reasoning, not citation.
7. Swimming Training Application and Running Application leaves are unprocessed; sport-family joint review (recommended by the cycling pass) should confirm the record-vs-plan seam from those sides.

---

## Final Synthesis

The Endurance Training Platform is the **endurance athlete's system of record for the training process**. Its world has three load-bearing structures: a **planned training schedule** that exists before execution and governs the season (built by athlete, coach, marketplace plan, or algorithm); the **workout as a planned-vs-completed unit** executed indoors or outdoors and captured back against the prescription (device/file sync or manual entry); and **accumulated training-state accounting** that turns completed training into load/progression views feeding the next planning decision. Around this core, mature products add the intensity backbone (per-sport thresholds and zones), structured-workout building and export, two-way device sync, fitness/fatigue/form modeling, event-targeted periodization, plan/workout libraries and marketplaces, coach attachment and roster machinery, and wellness data intake. The market organizes into poles by **who prescribes/adapts** (coach-first, self-serve algorithmic, self-coached analytics), by **sport lens**, and by **customer** (individual athlete, coaching business, team/club). The Type is distinct from sport-specific training applications (record-centric vs plan-centric), from workout tracking (no governing plan), from programming tools (no closed loop), and from AI fitness coaching (adapter identity is a variant, not the definition).
