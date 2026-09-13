# Research Notes — Running Application

Research date: 2026-09-09
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1 (internal; not referenced in the final document)

## Research Goal

Understand the "Running Application" Application Type from real products: what the world of such an application consists of (objects, users, surfaces), how work flows through it (record → analyze → share; plan → run → train), which structures are definitional vs. common vs. variant vs. vendor-specific, and where its boundaries lie against neighboring sport/fitness Types in Directory §28 — especially the already-processed siblings Cycling Application and Endurance Training Platform, whose passes left explicit flags for this one.

## Initial Boundary (pre-research hypothesis)

- An end-user application for people who run: record runs (GPS or treadmill), track pace/distance/splits, analyze performance, train toward goals (plans, guided runs, coaching), manage shoes as gear, socialize around running (friends, challenges, clubs), optionally find routes and races.
- Nearest directory neighbors: Cycling Application (sibling, already processed — seam expected at the sport data model), Workout Tracking Application, Endurance Training Platform (already processed — plan-vs-record discriminator expected), Wearable Fitness Platform, Fitness Progress Tracker, AI Fitness Coach, Race Management Platform (organizer-side), Hiking / Trail Application, Outdoor Recreation Discovery, Social Network (drift risk).
- Inherited flags to discharge:
  1. Cycling pass: "sibling-seam note… the running-application pass should apply the same sport-semantics discriminator"; segment/leaderboard competition was single-vendor there — do not promote it to definitional here.
  2. Endurance-training pass: "apply the same plan-vs-record discriminator before classing plan-first products as sport-specific apps" (TrainerRoad → Endurance Training Platform, not Cycling Application).
- Initial risk: overfitting to the social-activity-tracker pole (Strava) or to the guided-coaching pole (Nike Run Club); the plan-first pole (Runna) must be tested against the plan-vs-record discriminator rather than assumed in or out.

## Research Questions

1. What is the unit of record? What identifies and structures it (sport identity, treadmill/indoor variants)?
2. What running-specific data does the system capture, and which metrics are baseline (pace vs speed, splits, elevation, cadence)?
3. How does a run enter the system — live recording, watch/device sync, file import, manual entry, treadmill?
4. What does post-run analysis look like (splits, elevation-adjusted pace, pace zones, benchmark PRs, predictions)? Where does it become training science?
5. How do training plans, guided runs, and coaching relate to the run record — capability, wrapper, or the product's center?
6. How are shoes/gear modeled (mileage, replacement)?
7. What are the social structures (friends, feed, challenges, clubs, segments/leaderboards)? Are they definitional?
8. How do routes and navigation fit running (weaker than cycling? safety features?)
9. What device ecosystem relationships exist (watches, HR straps, foot pods, treadmills)?
10. Where does this Type end and Cycling / Workout Tracking / Endurance Training / Wearable Fitness / Race Management begin?

## Representative Products

| Product | Pole | Customer level | Why selected |
|---|---|---|---|
| Strava | social-first activity tracker with deep running analytics | consumer, freemium + subscription | largest consumer athletic network; running is a core sport; richest official help center |
| Nike Run Club | guided/coached-run pole, brand-ecosystem, free | consumer, free | audio-guided runs and plans as first-class surfaces; exercises "does the definition survive without subscription commerce" |
| adidas Running | recording-first, multi-sport breadth, brand rewards | consumer, free + premium | Runtastic heritage (2009); recording + goals + challenges + rewards; exercises multi-sport breadth |
| ASICS Runkeeper | legacy/accessible pole (2008-era GPS running app lineage) | consumer, free + premium tier | oldest-generation running tracker still current; run-centric structure with plans/insights; historical-check anchor |
| Runna | plan-first personalized coaching (boundary test) | consumer, subscription | tests the plan-vs-record discriminator inherited from the endurance-training pass |

## Sources

- Strava Help Center (Intercom-hosted; fetched 2026-09-09):
  - Supported Sport Types on Strava — https://support.strava.com/en-us/articles/15402005-supported-sport-types-on-strava
  - Help Center home (collection index) — https://support.strava.com/en-us/
  - Activity Analysis and Stats collection — https://support.strava.com/en-us/collections/19657597-activity-analysis-and-stats
  - Best Efforts – Running — https://support.strava.com/en-us/articles/15401661-best-efforts-running
  - Pace/Speed — https://support.strava.com/en-us/articles/15401806-pace-speed
  - Training Plans for Runners — https://support.strava.com/en-us/articles/15401942-training-plans-for-runners
  - Indoor, Treadmill, and Bike Trainer Activities — https://support.strava.com/en-us/articles/15401956-indoor-treadmill-and-bike-trainer-activities
- Nike Run Club — Apple App Store listing via iTunes Search API (vendor-authored description + release notes; track id 387771637; seller Nike, Inc.; seller URL https://www.nike.com/us/en_us/c/running/nike-run-club)
- adidas Running: Run tracker — Apple App Store listing via iTunes Search API (vendor-authored description; track id 336599882; seller Adidas International Marketing B.V.; seller URL runtastic.com)
- ASICS Runkeeper — https://runkeeper.com/ (product site: Start / Train / Race / Meet Us sections; guided workouts; training plans; insights; Running Routes search; race experiences) and Help Center — https://help.runkeeper.com/en/hc (categories: Account, iPhone, Android, Website, Partner Apps; iPhone sections Me / Start / Community; Training: Routes, Goals, Training Plans; Runkeeper Go; Editing)
- Runna — https://runna.com/ (plans 5k→ultramarathon, custom plans, "Runna Engine", device sync, strength/mobility, pricing, coach team; support.runna.com listed)
- Corroboration only (not a representative product): "RUN — Running Club & Tracker" App Store listing (independent small product; shoe mileage tracking, streaks/badges, beginner walk/run plans) — used solely to corroborate that shoe mileage and streak mechanics are widespread below the major-vendor tier.

Failed / abandoned sources (per network rule, 1–2 attempts then abandon):
- https://www.nike.com/gps-run-app — 404; https://www.nike.com/help/ — commerce-only help center (no NRC app articles reachable)
- https://www.adidas.com/us/adidas-running-app — 403 (bot protection); adidas web docs unreachable
- Google Play Store listings (Nike, adidas) — request timeouts ×2
- Guessed Strava running-glossary URL — 404; guessing abandoned (article surface confirmed via collection titles instead)

## Product Observations

### Strava (evidence layer: A — direct help-center articles)

- **Sport types / unit of record**: Foot Sports family includes Run, Trail Run, Hike, Walk, Wheelchair; treadmill/indoor runs and Virtual Runs exist as recording scenarios/sport types ("Except for virtual rides, runs, or rowing…" — virtual variants cannot be recorded with the mobile app itself). "Some of Strava's features are currently only available for our three core sport types, riding, running, and swimming" — running is a core sport. Sport type can be changed after upload. Any outdoor sport type includes a map by default. (A)
- **Run entry (multi-channel)**: mobile app recording; third-party device/app sync; manual file uploads; "Uploading Manual Activities"; "Edit Past Activities"; bulk editing; merge/combine activities; activity flagging. (A, from collection descriptions + cycling-pass article set still live)
- **Pace semantics**: "Pace (running) and Speed (cycling) measure the velocity at which you covered a distance. Running pace is measured in minutes per mile or kilometers… cycling speed… per hour." Average pace, splits "automatically created every mile or kilometer (depending on your preferred units)", Grade Adjusted Pace (GAP) "accounts for changes in elevation… estimates how fast you would have run on a flat course", Pace Zones (1–6; easier 1–3 vs intense 4–6) "determined by your past performances", Workout Analysis with lap data (lap button in app; device laps), performance settings (HR zones, pace zones, FTP). (A)
- **Benchmark PRs**: Best Efforts – Running: "Track your running PRs from 400m to 50k… top three lifetime efforts and top ten annual efforts at each distance, as well as your fastest efforts from each run"; found in the Progress tab "after you've uploaded at least one run"; times tracked automatically from GPS data; **uses elapsed time rather than moving time** ("much like a race where the clock does not stop when you stop moving"); edit time (e.g., chip time) / remove effort; distances tracked: 400m, 1K, 1/2 mile, 1 mile, 2 miles, 5K, 10K, 15K, 10 miles, 20K, half marathon, 30K, marathon, 50k. All-Time PRs article exists. (A)
- **Predictions**: Performance Predictions — "estimated 5K, 10K, half, and full marathon finish times based on your Strava running history… ML model". (A, description-level)
- **Training plans**: "Training Plans for Runners" — Strava has **sunset its own web running training plans**; "These plans will now be powered by Runna"; Strava+Runna subscription bundle; cycling plans unaffected (Carmichael Training Systems). Confirms plans are a capability that even the largest running tracker sources from a plan-first product. (A)
- **Indoor/treadmill**: mobile app cannot record indoor runs; Apple Watch app can (pedometer distance); third-party devices can (disable GPS recommended); indoor activity page has **no map** — performance graph instead; "you will still get credit for your elapsed time". (A)
- **Routes**: Routes tool "uses de-identified Strava data to intelligently recommend popular routes based on your preferences. You can also build your own" (app-store description, A−); Segments and Routes collection (60 articles) — "Discover and compete on segments… build or explore routes". (A, structure-level)
- **Gear**: shoes as gear records with accumulated mileage (from cycling-pass gear article, still live: bikes and shoes as gear; mileage accrues from assigned activities). (A)
- **Social/community**: Clubs/Challenges/Community collection ("Join clubs, take on challenges, and connect with athletes through your feed, kudos, and comments"); Sharing and Social collection; Group Activities. (A, structure-level)
- **Safety**: Safety and Security collection — "share your location with Beacon"; app-store description: "share your real-time location with loved ones while outdoors". (A/A−)
- **Other**: Athlete Intelligence (AI insights over workout data); Relative Effort; Heart Rate; Steps; Streaks; Goals (app/web); Month in Sport; heatmaps; Activity Event Match; subscription feature gating. (A, structure-level)

### Nike Run Club (evidence layer: A− — official app-store listing + release notes; Nike web help unreachable)

- **Positioning**: "Nike Run Club: Running Coach"; free; released 2010 (Nike+ GPS lineage); bundleId com.nike.nikeplus-gps.
- **Run tracker**: "Running speed, distance tracker, GPS route, elevation and heart rate are tracked and stored"; "Track progress towards your goals"; "Activity tracker syncs with your Apple watch and supported devices"; Apple Health sync for workouts and heart rate. (A−)
- **Training plans**: "NRC Training Plans give you a goal to run toward"; 4-Week Get Started plan; 12-week Marathon Training Plan; half-marathon training; **region-limited** ("Training Plans available in the US, UK, JP, CN, BR, FR, DE, ES, IT"). (A−)
- **Guided Runs**: "library of Guided Runs… Audio Guided Runs" with coaches/athletes (e.g., Eliud Kipchoge named); "you're never running by yourself"; select countries. Release note: finished runs show which Guided Run was listened to; can re-run it. (A−)
- **Challenges**: "earn badges and trophies for streaks and personal bests"; monthly mileage/distance goals; "create one and invite your friends"; share via social/messaging. (A−)
- **Shoe tagging**: "Track distance in every pair and let us remind you when it's time for a new pair"; "Record pace for each pair and learn which ones you run the fastest in". (A−)
- **Social in-run**: "Receive or send friends motivating in-run audio cheers". (A−)
- **Metrics detail**: release note — "Improved Average Pace… We now use your total time and total distance." (A−)
- **Music**: Apple Music integration for workout playback. (A−)

### adidas Running (evidence layer: A− — official app-store listing; adidas web unreachable, 403)

- **Positioning**: "adidas Running: Run tracker"; free; released 2009 (Runtastic lineage; seller URL runtastic.com); "all-in-one fitness companion".
- **Recording breadth**: "Track running, walking, cycling, and 90+ other sports with GPS and real-time stats"; "Monitor distance, pace, time, and calories burned"; "detailed activity summaries and progress tracking"; "Easily sync with your favourite wearable devices". (A−)
- **Guidance**: "personalized training plans for runners of all levels"; "voice coaching and insights to support every workout"; "Set goals and build routines". (A−)
- **Community/commerce**: "Join global challenges and virtual races"; "Connect with a worldwide fitness community"; "Share your progress"; "Earn rewards through activity and engagement… exclusive adidas experiences and products"; "70 million people" claim (marketing number — recorded here, not promoted). (A−)

### ASICS Runkeeper (evidence layer: A− product site + A− help-center structure; individual help articles not fetched)

- **Positioning**: "Track your Run - ASICS Runkeeper Running Tracker App"; site sections Start / Train / Race / Meet Us; ASICS-owned (Race Roster footer — same parent).
- **Recording**: help categories "Start" — Tracking Screen, GPS results/fix/signal, **Tracking indoors**, **Pocket Track**, **manually add an activity**; "Me" — edit existing activity, change activity type, share to social. (A−, title-level)
- **Training**: "flexible Training Plans, Guided Workouts and advanced Insights"; help Training section: Routes, Goals, Training Plans; Guided Workouts with named coaches (audio previews on site). (A−)
- **Community**: Group Challenge (iPhone/Android); friends (Account section). (A−)
- **Premium**: "Runkeeper Go" tier (help category). (A−)
- **Races**: "Find your finish line… premium race experiences near you" — links out to Race Roster event pages (organizer platform). (A−)
- **Routes**: "Running Routes" search at runkeeper.com/search/routes. (A−)

### Runna (evidence layer: A− — official product page; boundary test, not counted as a representative Running Application)

- **Plan-first structure**: "personalized training plans… from training for a faster 5k to completing your first marathon"; flow: "Set your goal → Choose your distance or race date and we'll build a plan around it → Start training → Follow your personalised workouts and track your runs using your favorite devices like Garmin or Apple Watch → Achieve more… progress tracking, community support, and coaching tips". (A−)
- **Plan catalog**: 5k / 10k / Half Marathon / Marathon / Ultramarathon; Run Faster / Run Further / Run to Maintain / Train Your Way; New to Running / Return to Running / Post-Race Recovery / Post-Injury; Custom Plan "6–26 weeks… any distance from 5–50km". (A−)
- **Engine & coaching**: "varied and exciting workouts powered by the Runna Engine"; human coach team (head coach, Olympians, physio); strength/mobility/nutrition support. (A−)
- **Device sync**: "Follow all of your workouts on your devices live as you run - we'll even help you set the correct pace" (Garmin, Apple Watch). (A−)
- **Commerce**: subscription ($19.99/mo, $119.99/yr — marketing-page numbers, recorded here only); free trial week. (A−)
- **Strava relationship**: screenshot alt text "by Strava Runna"; Strava help article "Strava is Acquiring Runna" + plans handoff (see Strava). (A/A−)

## Cross-product Comparison

| Dimension | Strava | Nike Run Club | adidas Running | ASICS Runkeeper | Runna (boundary test) |
|---|---|---|---|---|---|
| Unit of record | Activity (Run / Trail Run / treadmill / Virtual Run; re-typable) | Run (activity tab, re-runnable guided runs attached) | Activity (run/walk/90+ sports) | Activity (run-centric; type changeable) | Planned workout → executed run (plan is the organizing object) |
| Run entry | app recording / device sync / file upload / manual | app recording / Apple Watch / Apple Health sync | app recording / wearable sync | app recording / Apple Watch / wearables / manual / indoor / Pocket Track | device sync (Garmin/Apple Watch) + in-app tracking |
| Baseline metrics | distance, duration, pace (min/km or min/mile), splits, elevation, HR | distance, pace, GPS route, elevation, HR | distance, pace, time, calories | distance, pace, time (tracking screen) | pace targets per workout |
| Analysis depth | deep: GAP, pace zones, Workout Analysis, Best Efforts 400m–50k, predictions, Athlete Intelligence | activity details, average pace (total time/total distance), badges | activity summaries, progress tracking | Insights (premium tier) | plan progress/adaptation |
| Plans / coaching | plans sourced from Runna (own web plans sunset) | Training Plans + audio Guided Runs | personalized plans + voice coaching | Training Plans + Guided Workouts | the product IS the plan (Runna Engine) |
| Routes | Routes tool (recommended + build own); segments | not prominent | not prominent | Routes search | race-oriented |
| Gear/shoes | shoes as gear with mileage | shoe tagging + replacement reminder + per-pair pace | — | — | — |
| Social | feed/kudos/clubs/challenges/segments | challenges (create/share), in-run audio cheers | challenges, virtual races, community | Group Challenge, friends | community support |
| Indoor | treadmill via watch/devices; no map; elapsed time credited | treadmill guided runs | — | tracking indoors | treadmill workouts in plan |
| Commerce | freemium + subscription | free (brand ecosystem) | free + premium + rewards | free + Runkeeper Go | subscription |
| Safety | Beacon real-time location | — | — | — | — |

Stable across the four representative products (B layer): the run as the persisted, dated, per-runner unit of record; running metric semantics (distance/duration/pace, elevation, HR where available); multiple entry paths converging on one editable record; goals/progress surfaces; coaching or plans as a capability; device connectivity; a social/motivational layer; free-base commerce.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

1. **Run as the unit of record** — a persisted, dated running session belonging to the individual runner, labeled with a running sport identity (run / trail run / treadmill run / track or race / virtual run).
2. **Running-specific performance semantics** — the record carries metrics that mean something for running: distance, duration, and pace (time per distance unit) as the baseline set, with splits, elevation, and richer sensor data (heart rate, cadence) where devices provide it; shoe context at the mature pole.
3. **Origin in the runner's own running** — the record represents running the user actually did (or plans to do): captured live, synced from devices, imported from files, entered manually, or generated on a treadmill/indoors. The mechanism is not definitional; the first-person provenance is.

If the run-as-record or the running semantics disappear, the product becomes a generic workout tracker, a route utility, a device hub, or a social network — no longer a Running Application. Historical check: 2008–2010-era GPS running trackers (Runkeeper 2009, Runtastic 2009, Nike+ GPS 2010 — all in or ancestral to the sample) fit (1)–(3); a manual running diary without GPS fits; a treadmill-only product fits via indoor provenance. GPS tracks, maps, social feeds, training plans, and shoe mileage are NOT required.

### L1 — Common Mature Structure (evidence layer B)

- GPS track + map visualization of outdoor runs (absent by design for treadmill/indoor runs)
- Multiple run-entry channels (live recording, device sync, file import, manual entry) and post-hoc editing (rename, correct metrics, change activity type, merge)
- Pace analysis: average pace, per-km/per-mile splits, elevation-adjusted pace, pace zones (documented in depth in the sampled tracker; present as summaries elsewhere)
- Benchmark personal records at standard race/benchmark distances, with badges/trophies
- Goals, streaks, and progress surfaces (weekly/monthly distance, consistency)
- Training plans and/or guided (audio-coached) runs; voice coaching
- Device/sensor connectivity: smartwatches, heart-rate straps, foot pods, treadmills; health-platform sync
- Shoe/gear tracking with accumulated mileage (and replacement hints at the mature pole)
- Social layer: friends/followers, feed or share surfaces, challenges, groups/clubs
- Route discovery/search for running (weaker than in cycling; present in the tracker and the legacy product)
- Free base with subscription/premium tier (or brand-funded free)

### L2 — Variant / Optional Structure

- Guided/audio-coached runs as a first-class surface (coach voice during the run)
- Plan-first personalized coaching as the product's center (→ boundary with Endurance Training Platform)
- Route planning/building for running; segment/leaderboard competition on stretches
- Race-finish-time prediction from history
- Virtual races; race-experience partnerships
- Safety features: live-location sharing with contacts
- Brand-ecosystem rewards and commerce (products/experiences for activity)
- Multi-sport breadth (dozens of sport types) vs run-only focus
- Region-limited feature availability (plans in select countries)
- Community contribution to maps/routes

### L3 — Vendor-specific (research notes only)

- Strava: Best Efforts distance list (400m…50k) with top-3-lifetime/top-10-annual and elapsed-time basis; GAP and 6 pace zones from past performances; Performance Predictions ML; Athlete Intelligence; Relative Effort; Beacon; segments/leaderboards; heatmaps; Runna handoff with STRAVA-TP trial code and Strava+Runna bundle; Carmichael plans retained for cycling.
- Nike Run Club: Guided Runs with named coaches/athletes; in-run audio cheers; shoe tagging with replacement reminder and per-pair pace; average pace recomputed as total time / total distance (release note); plan region list; Apple Music integration.
- adidas Running: 90+ sports; rewards program with adidas products/experiences; virtual races; "70 million people" marketing claim; Runtastic bundle id heritage.
- ASICS Runkeeper: Pocket Track; GPS "Fix it" button; Runkeeper Go premium tier; Group Challenge; race experiences routed to Race Roster (sister organizer platform).
- Runna: Runna Engine; plan catalog and custom-plan parameters (6–26 weeks, 5–50km); coach roster; Strava bundle pricing.

## Vendor-specific Findings

See L3 — none promoted to the canonical model. Notably: segment/leaderboard competition appears as an identity-level feature in only one sampled product (Strava), matching the cycling pass's warning — kept variant. Guided audio runs are prominent in two products (Nike, Runkeeper) but absent as a documented surface in the tracker's fetched pages — kept variant-leaning-common, not definitional.

## Rejected Findings

- "GPS track/map is definitional" — rejected: treadmill/indoor runs are first-class (Strava indoor article: no map, elapsed time credited; Runkeeper "Tracking indoors"; Nike treadmill guided runs), and manual entry exists. Higher abstraction: origin in the runner's own running, mechanism variant.
- "Training plans are definitional" — rejected: the largest sampled tracker outsourced its running plans to a partner product while remaining the archetype of the Type; plans are a capability, not the record.
- "Social feed/challenges are definitional" — rejected: a bare recording+analysis product (or a manual log) is still a Running Application; social layers vary from absent to central.
- "Shoe mileage is definitional" — rejected: present in two sampled products and corroborated below the major tier, but a running app without gear tracking is unremarkable and common.
- "Pace zones / GAP are definitional" — rejected: analysis depth varies hugely; the baseline semantic is pace itself, not any particular analysis model.
- "Running app = multi-sport fitness app" — rejected: the Type is sport-specific; breadth (90+ sports in one product) is a variant, and the running data model is what all sampled products organize around.

## Boundary Findings

- **vs Cycling Application (sibling leaf)**: identical skeleton at high abstraction (record → analyze → share; plan → run), different sport semantics — pace/splits/shoe-mileage vs speed/elevation/bike/components; shoe as the wear item vs bike+components; route planning/navigation strong in cycling, weaker in running; safety-live-location more prominent in running. The seam is the sport data model. **This pass discharges the sport-family joint-review flag from the running side**: seam confirmed, both leaves stay separate Types (the directory family deliberately enumerates sport-specific applications).
- **vs Endurance Training Platform**: plan-vs-record discriminator (inherited from the endurance pass) applied. **Runna is structurally plan-first** (goal → personalized plan → structured workouts → device-synced execution → adaptation; runs are tracked in service of the plan) → classed as Endurance Training Platform (running-lens variant), NOT a Running Application. Corroboration: Strava's official handoff of running training plans to Runna while keeping the activity record itself. NRC/Runkeeper plans stay inside this Type because the run record remains the system of record and plans are one capability among several.
- **vs Workout Tracking Application**: a generic workout tracker lacks running semantics — no pace/splits model, no shoe mileage, no benchmark race distances. Remove running semantics → workout tracker.
- **vs Wearable Fitness Platform**: that Type organizes around the device/wearable as the hub for all activity and health data; a Running Application organizes around the run even when it pairs watches and straps.
- **vs Fitness Progress Tracker**: that Type centers body/performance metrics independent of activity capture; here totals/PRs are derived views over run records.
- **vs AI Fitness Coach**: when the software-performing-coach-loop is the product's center, it belongs there; running apps may embed plan generation without becoming that Type.
- **vs Race Management Platform**: organizer-side event operations vs runner-side running; Runkeeper's race-experience surface links out to a sister organizer platform (Race Roster) — a clean example of the seam. Race discovery/registration in a running app is a convenience surface.
- **vs Hiking / Trail Application & Outdoor Recreation Discovery**: trail objects/terrain/wayfinding vs the run record; Trail Run exists as a sport type inside running apps, but there are no trail objects or trail-following machinery.
- **vs Social Network**: drift test — when feed/profile become primary and runs degenerate into shareable content, the product drifts toward a Social Network. The test: is the run still the unit of record with running analysis attached?
- **"Remove what to become another Type" judgments**: remove running semantics → Workout Tracking Application; remove run recording (keep only route discovery) → Outdoor Recreation Discovery; abstract the sport to cycling → Cycling Application; make the plan the record → Endurance Training Platform; make the device the hub → Wearable Fitness Platform; make it organizer-side → Race Management Platform; make the coach loop the center → AI Fitness Coach.

## Uncertainties

- Nike Run Club and adidas Running evidence is official app-store-listing level (vendor-authored descriptions and release notes). Nike's web help center is commerce-only and adidas.com blocked fetches (403). Their capability claims are kept at capability level; no precise numbers, limits, or defaults asserted for them.
- Runkeeper help-center article titles observed but individual articles not fetched; "Insights" (premium) scope and Runkeeper Go feature list unverified.
- Strava segments for running: existence confirmed via collection description and sport-type article; leaderboard mechanics not documented in fetched pages — no rules claimed.
- Strava Best Efforts is mobile-app-only per the fetched article; web parity unverified.
- Very old/regional manual running diaries were not directly researched; the historical check for manual entry relies on documented manual-activity support in the sampled tracker plus the general plausibility of the invariant reading.
- The small indie corroboration product was not deeply researched (listing only).

## Final Synthesis

A Running Application is an end-user application whose world is organized around the run: a persisted, dated, sport-typed run record per runner with running performance semantics (distance, duration, pace as the baseline; splits, elevation, sensor data, shoe context at the mature pole), originating from the runner's own running through whatever capture mechanism the product offers — live GPS recording, watch/device sync, file import, manual entry, or treadmill/indoor capture. Mature products add maps/tracks, pace analysis (splits, elevation-adjusted pace, zones), benchmark PRs, goals and streaks, training plans and guided runs, device connectivity, shoe mileage, route discovery, and a social/motivational layer over a free base. The social-tracker, guided-coach, recording-first multi-sport, legacy-accessible, and treadmill/indoor realizations all satisfy the same invariant core. Boundaries are held against generic workout tracking (no running semantics), endurance training platforms (plan-as-record — Runna classed there), wearable platforms (device-centric), fitness progress trackers (body-metric-centric), race management (organizer-side), trail/outdoor discovery (no run-record loop), and social networks (feed-first drift).
