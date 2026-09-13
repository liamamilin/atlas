# Research Notes — Swimming Training Application

Research date: 2026-09-09
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1 (internal; not referenced in the final document)

## Research Goal

Understand the "Swimming Training Application" Application Type from real products: what the world of such an application consists of (objects, users, surfaces), how work flows through it (workout → swim → log → analyze → train), which structures are definitional vs. common vs. variant vs. vendor-specific, and where its boundaries lie against neighboring Types in Directory §28 — especially the already-processed sport-family siblings (Running Application, Cycling Application, Endurance Training Platform), whose passes left explicit flags and discriminators for this one.

## Initial Boundary (pre-research hypothesis)

- An end-user application for people who swim: record swims (pool and open water), track swim-specific data (distance, pace, strokes, stroke type), follow structured workouts and training plans, log manually (the swim logbook tradition), connect swim watches/goggles, and socialize around swimming (clubs, leaderboards, challenges).
- Nearest directory neighbors: Running Application and Cycling Application (siblings — seam expected at the sport data model), Endurance Training Platform (plan-vs-record discriminator expected), Workout Tracking Application (swim semantics expected to be the seam), Wearable Fitness Platform (device-hub seam), Swim School Management (organizer-side seam — same directory family), Race Management Platform (organizer-side), Social Network (drift risk).
- Inherited flags to discharge:
  1. Endurance-training pass: "Running / Cycling / Swimming Training Application — sport-specific siblings organized around the activity record (the run/ride/swim as unit of record, with the sport's own data semantics); here the workout-in-plan is the unit and sport activities are inputs to the training process." This pass must confirm the swim side of that seam.
  2. Running pass: "apply the same sport-semantics + plan-vs-record discriminators" — plan-first swim products must be tested against the plan-vs-record discriminator rather than assumed in or out.
- Initial risk: overfitting to the structured-workout pole (MySwimPro) and treating the plan as definitional because the leaf name contains "Training"; the manual-log pole (the swim logbook tradition) and the platform-native capture pole (watch-native swim workouts) must be checked.
- Naming observation: the leaf name includes "Training" while its siblings are "Running Application" / "Cycling Application". Research must determine whether "training" makes plan-of-record definitional or is market naming only.

## Research Questions

1. What is the unit of record? (swim session? swim workout? planned vs completed?) What identifies and structures it (pool vs open water, stroke content)?
2. What swimming-specific data semantics exist? (pool course/length, lengths/laps, pace convention, stroke types, stroke count/rate, SWOLF-class efficiency, drills/kick)
3. How does a swim enter the system — swim watch, smart goggles, manual entry, imports (health platforms, pictures of paper workouts, other log formats)?
4. What is the structured-workout model? (sets, reps, intervals, send-offs, effort levels, equipment, set groups/phases)
5. How do training plans relate to the workout record — capability, wrapper, or the product's center? (plan-vs-record discriminator)
6. How does personalization work (seed times / best times per stroke → intervals/rest)?
7. What are the benchmark/progress structures (test sets, totals, goals)?
8. What are the social structures (clubs, pool leaderboards, challenges)? Are they definitional?
9. What device ecosystem relationships exist (swim watches, smart goggles, heart rate in water)?
10. Where does this Type end and Running/Cycling Applications, Endurance Training Platform, Workout Tracking, Wearable Fitness Platform, Swim School Management begin?

## Representative Products

| Product | Pole | Customer level | Why selected |
|---|---|---|---|
| MySwimPro | structured-training / workout-first pole (plans, guided workouts, logging, coach subscription) | consumer, free + subscription; coach product | the archetype swim training app; richest official help center (Intercom, 57 how-to articles) |
| Swim.com | tracking + community pole (device-agnostic tracking, workout library, clubs, pool leaderboards) | consumer, free; official platform of US Masters Swimming | exercises the community/competition layer and the pool-database model; multi-device breadth |
| FORM (Smart Swim Goggles) | device-ecosystem pole (smart goggles with in-goggle display + companion app + premium) | consumer, hardware + subscription | exercises the capture/display hardware pole and the triathlon-facing orientation |
| Strava (swim) | social-activity-tracker pole (swim as one core sport inside a multi-sport social network) | consumer, freemium + subscription | largest consumer athletic network; swim is a documented core sport; tests whether the Type survives as a sport module |

Boundary tests (not counted as representative products): TrainingPeaks / TriDot (plan-first triathlon platforms — plan-vs-record discriminator), Garmin Connect / Apple Watch native swim workouts (device-hub / platform-native capture poles).

## Sources

- MySwimPro Support Center (Intercom-hosted; fetched 2026-09-09):
  - How To Use MySwimPro collection (57 articles) — https://support.myswimpro.com/en/collections/3531502-how-to-use-myswimpro
  - Getting Started With MySwimPro — https://support.myswimpro.com/en/articles/6350436-getting-started-with-myswimpro
  - How To Log An Unguided Swim — https://support.myswimpro.com/en/articles/6350460-how-to-log-an-unguided-swim
  - Changing Pool Length — https://support.myswimpro.com/en/articles/6350461-changing-pool-length
  - How To Follow A Training Plan — https://support.myswimpro.com/en/articles/6350454-how-to-follow-a-training-plan
  - Setting Up Personalized Intervals — https://support.myswimpro.com/en/articles/6350457-setting-up-personalized-intervals
  - Test Sets — https://support.myswimpro.com/en/articles/6809628-test-sets
  - Import Swims From A Picture — https://support.myswimpro.com/en/articles/11677311-import-swims-from-a-picture
- Swim.com (fetched 2026-09-09):
  - Product site — https://swim.com/ (positioning, features, vendor-published user testimonials)
  - Clubs page — https://swim.com/clubs (club structure, USMS designation, pool course search facets)
  - Support base — http://support.swim.com (Zendesk; article bodies not extractable — see Uncertainties)
- FORM (fetched 2026-09-09):
  - Product site — https://www.formswim.com/ (goggles, HeadCoach, accuracy claims)
  - Workout & Plans page — https://www.formswim.com/pages/swimming-app (workout library/categories, Workout Builder, plans, TrainingPeaks/TriDot import)
- Strava Help Center (fetched 2026-09-09):
  - Supported Sport Types on Strava — https://support.strava.com/en-us/articles/15402005-supported-sport-types-on-strava
  - Swim Activities on Strava — https://support.strava.com/en-us/articles/15401830-swim-activities-on-strava
  - Indoor, Treadmill, and Bike Trainer Activities — https://support.strava.com/en-us/articles/15401956-indoor-treadmill-and-bike-trainer-activities

Failed / abandoned sources (per network rule, 1–2 attempts then abandon):
- TrainingPeaks help center — https://help.trainingpeaks.com/hc/en-us/articles/204282250-Swim-Workouts (timeout) and retry (transport error) — abandoned; boundary evidence for plan-first triathlon platforms taken from FORM's documented TrainingPeaks/TriDot import and MySwimPro's documented TrainingPeaks sync instead.
- Swim.com Zendesk article bodies (e.g., Compatible Devices article 360049230352) — title-only renders on direct fetch and API endpoint 404 — abandoned; Swim.com observations rest on product pages and vendor-published testimonials.

## Product Observations

### MySwimPro (evidence layer: A — direct help-center articles)

- **Positioning**: swim training app; phone + smartwatch; free base with "MySwimPro Coach" subscription; separate coach-facing product (myswimpro.com/coach).
- **Guided Workout structure** (Getting Started article): a guided Workout is composed of **Set Groups** (phases typically named Warm up, Drill Set, Pre-Set, Main Set, Post-Set, Cool Down; groups can repeat) which contain **Sets**. Each Set specifies: number of repetitions, distance per repetition, stroke type, interval, effort level, effort-level variation, equipment. Canonical set notation: "4 x 100m Free @ 2:45 Easy, Fins". A Set represents total distance (4 × 100 = 400m) and total duration (4 × 2:45).
- **Stroke types**: abbreviated stroke identities (Free = Freestyle/front crawl; Kick and IM/drill sets appear in examples; stroke-type misrecording is a documented troubleshooting topic).
- **Interval semantics**: "Interval = Swim Time + Rest Time for each rep" — the faster you swim, the more rest you get. SetBar™ visualizes target swim time vs rest per rep. The swim:rest ratio is computed by the vendor's DynamicSwim™ algorithm from interval + effort level.
- **Effort levels**: seven named levels (Easy, Moderate, Endurance, Threshold, Best Average, Race Pace, Sprint), color-coded. **Effort variations**: Build, Ascend, Descend, Negative Split.
- **Equipment**: sets commonly carry equipment recommendations (Paddles, Fins, Pull Buoy, Snorkel, Kickboard); the user's equipment inventory is part of the Swim Profile and workouts adjust to it; equipment use is recommended, not required.
- **Personalization**: Seed Times (best times per stroke, user-entered in Swim Profile) drive Personalized Intervals — "calculated as a function of the number of reps, distance, stroke type, energy zone, and your threshold ability for that particular stroke"; example: same 10×100 Free set at @1:10 (elite) vs @2:00 (intermediate). Rest between sets and between set groups is separately configurable. The app prompts when it detects a speed change.
- **Pool length**: default pool length setting ("My Pools" / Pool Course) applies to all Workout Library and Training Plan workouts; per-workout override with switching between pool lengths.
- **Workout visualization**: SwimGauge™ (full-workout visual: total distance, sets, reps, effort levels, laps in the selected pool), Set List.
- **Entry paths**: (1) guided workout executed on Apple Watch / Garmin / WearOS or phone ("Splash Mode" — follow the workout on the phone from the pool deck); (2) unguided swim tracked on watch (Pool Swim / Open Water modes; confirm pool size; Garmin auto-detects sets and logs stroke counts, SWOLF "and more"); (3) manual logging ("Log Activity" / custom workouts); (4) import from Apple Health; (5) **Import Swims From A Picture** — photograph a printed or handwritten workout, the app transcribes it into a structured workout, user reviews yardage, then swims or logs it.
- **Drill/kick handling**: Drill Mode on the watch during unguided swims — enter Drill Mode, perform the kick/drill set the watch cannot normally track, exit, and enter the total kick/drill distance manually.
- **Open water**: separate Open Water mode (Apple Watch: wait for GPS location accuracy "best"; troubleshooting article for open water distance/map).
- **Training plans**: weekly Swim Training Plans personalized to goals and speed; plan catalog spans beginner (Getting Started, Couch to 1k), fitness (Get Fit, weight loss), technique bootcamps (Freestyle Technique), IM (Intro to IM, Get Fit IM), open water (5k/10k/12-week), USRPT series; workouts editable (intervals/duration) before swimming; plan completion tracked ("Workout isn't marked complete in training plan" troubleshooting).
- **Paper workflow**: "tap the menu icon to print the Workout or sync it with a smartwatch, or write it on a piece of paper or whiteboard" — the paper/whiteboard path is officially documented.
- **Test Sets**: recurring benchmark workouts per energy zone; app recommends the next Test Set on the Home tab; results stored with per-rep splits; split times editable; previous attempts deletable; repeated across the season; distance/type determined by Swim Profile settings.
- **Other**: AI workout generation; Coach Chat (chat with a coach to edit workouts); Heart Rate Zones; Trends tab; widgets; share to social media; sync with Strava and TrainingPeaks; calories calculation; seed-time updates (race times) troubleshooting.

### Swim.com (evidence layer: A− — official product pages + vendor-published testimonials; Zendesk article bodies not extractable)

- **Positioning**: "Compete, share and track your swimming workouts"; "the World's Most Advanced Swim Workout & Training Platform"; "The Official Swim Workout and Training Platform of United States Masters Swimming" (USMS). Free sign-up; Spiraledge/SwimOutlet ownership.
- **How it works** (product page): connect your swim tracking device → discover workouts and start swimming → connect, compete and conquer your goals.
- **Workouts**: "more than 1,000 workouts" (vendor-stated number) with recommendations "based on your pace, preferred stroke type, goal distance"; Build Your Own Workout "from hundreds of predefined sets or from scratch"; workouts download "directly to your swim watch" to follow during the swim.
- **Tracking** (vendor-published testimonials): counts lengths/laps and distance, times, heart rate, rest times, automatic pause at the wall, automatic stroke recognition ("recognises the change in stroke when I've gone from Freestyle to Breaststroke"), per-interval and per-length analysis views, correction of incorrect lap counts and stroke misreads, notes on workouts.
- **Manual entry**: "Easy to use and manually add my yardage" — manual yardage entry is a first-class path; one testimonial notes the distance field requires a multiple (user works around it for time-only swims) — evidence that distance is the expected unit of a logged swim.
- **Pool model**: custom pool lengths ("The option to set custom pool lengths allows any swimmer to start tracking"); pool database searchable by course (50 meters / 25 meters / 25 yards / other), public/private, indoor/outdoor; users report pool-name corrections.
- **Progress/goals**: track swims "by day, week, month, stroke type and more"; weekly, monthly, and annual goals.
- **Competition/community**: leaderboards per pool ("compete on your pool's leaderboards to see who's fastest or swims the most"); clubs ("Join or start a club and see who claims 'lane 4' first"); monthly challenges; virtual competition "compare to other swimmers by age, gender and type"; open water support (recently added per testimonials).
- **Clubs page**: find clubs on a map; "Official USMS Club" designation; club admins and ownership transfer; claim-club rules.
- **Devices**: Apple, Samsung, WearOS, Suunto, Garmin watch families on the landing page; Compatible Devices article exists (body not extractable); imports from Garmin Connect and USMS FLOG (testimonial); syncs to Strava (testimonial).
- **Swim AI**: announced "coming soon" (personalized workouts, intelligent set suggestions).

### FORM Smart Swim Goggles (evidence layer: A− — official product pages; support center not fetched)

- **Positioning**: smart swim goggles with an in-goggle augmented-reality display ("Seeing your data as you swim"); companion FORM Swim App (Apple/Android); Premium subscription; hardware tiers (Smart Swim 2 LT / 2 / 2 PRO with heart-rate monitoring in the higher tiers).
- **In-goggle experience**: real-time metrics while swimming; "FORM counts your laps, sets, and intervals so you can stay in the moment"; HeadCoach™ — "1-on-1 swim coach" instruction displayed in-goggle.
- **Workouts**: "1,500+ Workouts In Your Goggles" (vendor-stated number), coach-designed; "Automatically sync a workout to your goggles and see motivating lap-by-lap instructions"; Workout Builder to create custom workouts; workout categories: Endurance, Recovery, Technique, Power, Sprint, Test Set.
- **Import**: "Build your own workouts, or import from TrainingPeaks & TriDot" — documented integration with plan-first triathlon platforms.
- **Plans**: coach-designed swim training plans; "Follow a plan and your weekly workouts will automatically sync to your goggles"; plan families: Triathlon (Sprint 8wk / Olympic 12wk / Half Iron 16wk / Full Iron 24wk, with weekly frequency and average distance volumes), Fitness (Improve Your Pace, Boost Your Endurance, Swim 500 Non-Stop, …), Skill Development (Freestyle Foundations; equipment plans for kickboard, pull buoy, fins); "20+ training plans" in app (vendor-stated).
- **Metrics**: stroke rate, stroke length, pacing (professional-triathlete testimonial); all swim data logged and comparable across weeks.
- **Open water**: dedicated Open Water Swimming page (GPS-based).
- **Community**: "global swim community of 50,000 and growing" (vendor-stated number); integrations with fitness apps (Strava club presence); accuracy claims (99.8% distance / 96.6% time) citing a peer-reviewed study of AR swim goggles — vendor-selected marketing numbers, recorded here only.

### Strava — swim module (evidence layer: A — direct help-center articles)

- **Sport status**: Swim is a Water Sport type; "some of Strava's features are currently only available for our three core sport types, riding, running, and swimming" — swimming is a core sport. Sport type can be changed after upload.
- **Devices**: swim-capable devices listed (Garmin Swim 2, Forerunner/Fenix/Instinct series, TomTom, Polar Vantage, Suunto); "The Strava app for Apple Watch can record swimming activities but without GPS (distance and pace will not be reflected on the activity)"; Wear OS 3 supported.
- **Indoor (pool) swims**: no map; a **laps view** is displayed instead; pool length must be input before starting the activity; **"There is no way to update the pool length once the activity is on Strava"**; distance = sum of lap distances; moving time = sum of lap timer times.
- **Outdoor swims**: GPS map displayed; GPS-based moving time; pace chart built from GPS points with smoothing.
- **Pool-vs-open-water rule**: "If you are recording a swim activity in an outdoor lap pool, it is best to turn off the GPS and use the lap counter. In order to get the most accurate data, you should treat outdoor lap pools as indoor pools."

## Cross-product Comparison

| Dimension | MySwimPro | Swim.com | FORM | Strava (swim) |
|---|---|---|---|---|
| Unit of record | Swim Workout (guided: set groups → sets; unguided: watch-tracked swim; manual/custom) | Swim (watch-tracked or manually entered yardage) | Swim workout (synced to goggles; guided lap-by-lap) | Swim activity (pool swim with laps view / open water with GPS) |
| Swim context | Pool length setting + per-workout override; Open Water mode | Custom pool lengths; pool database (50m/25m/25yd/other, indoor/outdoor) | Pool course config; Open Water page | Pool length input before activity (locked after upload); outdoor lap pools treated as indoor |
| Structured workout model | Set groups → sets (reps × distance × stroke × interval × effort × equipment); 7 effort levels; variations | 1,000+ workout library; predefined sets; workout builder | 1,500+ workouts; categories incl. Test Set; Workout Builder | — (no workout authoring; activity record only) |
| Interval semantics | interval = swim + rest per rep; algorithm-computed; seed-time personalized | rest times tracked; interval views | lap-by-lap instructions in-goggle | lap timer times summed |
| Personalization | Seed Times per stroke → personalized intervals/rest | recommendations by pace/stroke/goal distance | plans by level; HeadCoach coaching | — |
| Benchmark structure | Test Sets per energy zone with split history | goals (weekly/monthly/annual); leaderboards | Test Set workout category | — |
| Stroke semantics | stroke type per set; stroke-type correction | automatic stroke recognition + correction | stroke rate, stroke length | stroke data from device |
| Technique metrics | stroke counts, SWOLF (via Garmin) | strokes, rest, per-length detail | stroke rate, stroke length, pacing | device-provided |
| Entry paths | guided (watch/phone) · unguided watch · manual · Apple Health import · picture import | watch sync (Garmin/Suunto/Apple/WearOS) · manual yardage · FLOG import | goggles capture · app · TrainingPeaks/TriDot import | device sync · Apple Watch (no GPS) · Wear OS |
| Open water | Open Water mode (GPS) | Open water support | Open water page | GPS map + smoothed pace |
| Plans | weekly personalized plans; catalog beginner→IM/open water/USRPT | — (workouts, not multi-week plans, at the documented surface) | 20+ plans (tri/fitness/skill) | — |
| Social/competition | share to social; coach chat | pool leaderboards; clubs (USMS); challenges; age/gender comparison | community; Strava club | full social network (feed, kudos, clubs, segments) |
| Commerce | free + Coach subscription; coach product | free | hardware + Premium subscription | freemium + subscription |
| Export/sync | Strava, TrainingPeaks, Apple Health | Strava, Garmin Connect | fitness apps, Strava | — (destination) |

Stable across the sample (B layer): the swim workout/session as the persisted, dated, per-swimmer unit of record; swimming semantics (pool-course distance via counted lengths, stroke identity, pace, stroke-based technique metrics where devices provide); multiple entry paths converging on one editable record (device capture, manual entry, imports); structured workouts with sets/intervals as the dominant training content; progress surfaces over time; device connectivity; a social/motivational layer in most products; free-base or hardware+subscription commerce.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

1. **Swim workout/session as the unit of record** — a persisted, dated swimming session belonging to the individual swimmer, labeled with swim context (pool vs open water; the stroke content of the session). The record persists and accumulates into a personal training history.
2. **Swimming-specific performance semantics** — the record carries metrics that mean something for swimming: distance, duration, and pace in the sport's own terms. In pool swims, distance is grounded in the pool's course (counted lengths against a configured pool length); in open water, in GPS distance. Stroke identity (which stroke was swum) is part of the record's meaning, and stroke-based technique metrics (stroke count/rate, SWOLF-class efficiency) appear where devices provide them.
3. **Origin in the swimmer's own swimming** — the record represents swimming the user actually did (or is about to do): captured by a swim-proofed device (watch or goggles), entered manually, or imported. The mechanism is not definitional; the first-person provenance is.

If the swim record or the swim semantics disappear, the product becomes a generic workout tracker, a device hub, a plan-delivery service, or a social network — no longer a Swimming Training Application. Historical check: the paper swim logbook (decades of coach whiteboards, handwritten set sheets, yardage logs) satisfies all three via manual entry — and the sampled products still digitize exactly this practice (MySwimPro's picture import of handwritten workouts; Swim.com's manual yardage entry; MySwimPro's documented print/paper/whiteboard path). Platform-native capture (watch-native pool/open-water swim workouts feeding health platforms) satisfies via device provenance. Regional course conventions (25 yd vs 25 m vs 50 m) satisfy — course is configuration, not definition. GPS tracks, workout libraries, plans, leaderboards, and smart goggles are NOT required.

### L1 — Common Mature Structure (evidence layer B)

- **Structured workout model** — workouts composed of sets (repetitions × distance × stroke × interval × effort, commonly with equipment), grouped into phases (warm-up / main set / cool-down pattern); workout libraries (vendor-stated 1,000+ and 1,500+ in the two sampled library products) and workout builders.
- **Interval semantics** — the interval as swim time + rest per repetition; rest as a first-class training variable; personalization of intervals/rest from the swimmer's ability (seed/best times per stroke) in the deepest sampled product.
- **Training plans** — multi-week, goal-oriented plan structures (fitness, technique, competitive, open water, triathlon-swim); plan workouts flow into the same workout record.
- **Benchmark/progress structures** — test sets (recurring benchmark swims with split history), totals by day/week/month/stroke, goals, trends.
- **Device connectivity** — swim watches (multiple families) and smart goggles; automatic lap/length counting, stroke detection, stroke count/rate, SWOLF-class metrics, heart rate where hardware supports; workout sync down to the device.
- **Drill/kick handling** — explicit treatment of technique swimming that normal tracking cannot measure (drill modes with manual distance entry).
- **Multiple entry paths, one record** — guided in-app/watch/goggle execution, unguided watch swims, manual entry, imports (health platforms, other log formats, pictures of paper workouts); post-hoc editing (correct laps, fix stroke misreads, adjust splits).
- **Open water mode** — GPS-based swim recording with map, distinct from pool swims.
- **Social/motivational layer** — clubs (with formal club administration in the community-pole product), leaderboards (pool-scoped in the sampled product), challenges, sharing, goals.
- **Free base + subscription, or hardware + subscription** commerce; export/sync to other fitness platforms.

### L2 — Variant / Optional Structure

- In-goggle display and in-goggle coaching (device-realization of guidance)
- AI workout generation and AI set suggestions
- Human-coach services attached to the app (coach chat, coach products)
- Print / paper / whiteboard workflow; picture-import (OCR) of handwritten workouts
- Pool database with course/indoor-outdoor/public-private attributes; pool-scoped leaderboards
- Formal club administration (ownership transfer, claim rules); national-body integration (USMS official platform; FLOG import)
- Race seed times held in the swimmer profile
- Triathlon orientation (tri swim plans; import from triathlon training platforms)
- Course conventions as regional variants (25 yd short-course yards vs 25 m / 50 m metric)
- Multi-sport breadth (swim as one sport inside a multi-sport tracker)

### L3 — Vendor-specific (research notes only)

- MySwimPro: SetBar™, SwimGauge™, DynamicSwim™ algorithm, Splash Mode, Drill Mode flow, seven named effort levels, Import-Picture transcription, Coach Chat, WOD library location, seed-time troubleshooting flows.
- Swim.com: pool-scoped leaderboards, "lane 4" club competition framing, USMS FLOG import, Swim AI (announced), distance-field-multiple constraint reported in a testimonial.
- FORM: HeadCoach™, in-goggle AR display, goggle hardware tiers with in-goggle heart rate, accuracy percentages (99.8%/96.6%) with cited study, HSA/FSA payment.
- Strava: pool-length-locked-after-upload rule, outdoor-lap-pool-as-indoor guidance, core-sport feature gating (swim among three core sports), Apple Watch swim without GPS/distance.

## Vendor-specific Findings

See L3 — none promoted to the canonical model. Notably: pool-scoped leaderboards and formal club administration appear strongly in one sampled product (Swim.com) — kept variant. In-goggle display/coaching is unique to the hardware pole (FORM) — kept variant. The picture-import and print/whiteboard paths are documented in one product but express the general manual-log tradition — kept as variant realizations of the manual entry path.

## Rejected Findings

- "Training plans are definitional (the leaf says 'Training')" — rejected: the tracking+community pole (Swim.com) documents workouts and goals, not multi-week plans, at its documented surface, and the social-tracker pole (Strava) has no plans at all; both remain unmistakably swim training applications. The plan is a capability. The plan-vs-record discriminator (inherited from the endurance pass) holds: plan-first triathlon platforms (TrainingPeaks, TriDot) own the plan and push swim workouts INTO swim apps (documented import targets at FORM and sync target at MySwimPro) — they are not this Type.
- "GPS track/map is definitional" — rejected: pool swims — the majority context of the sport — have no usable GPS; the pool record is lengths × course with a laps view (Strava explicit; MySwimPro/Swim.com/FORM lap counting). GPS belongs to the open-water variant.
- "Structured sets/intervals are definitional" — rejected: a watch-tracked unguided swim or a manually entered yardage log satisfies the Type (all sampled products support unguided/manual records); the structured workout is the dominant training content but not the record's definition.
- "Stroke-technique metrics (SWOLF, stroke rate) are definitional" — rejected: device-dependent; manual logs carry none; kept as common mature structure where devices provide.
- "Social layer (clubs/leaderboards) is definitional" — rejected: MySwimPro's documented surface is personal-training-centric; a bare recorder+logger is still the Type.
- "Equipment (paddles/fins) tracking is definitional" — rejected: equipment appears as set annotations and profile inventory, not as mileage-tracked wear items; there is no shoe-mileage analog in the sampled products.
- "Swim app = triathlon app" — rejected: triathlon is a customer segment and plan family, not the Type's definition; the swim record remains the center in all sampled products.

## Boundary Findings

- **vs Running Application / Cycling Application (sibling leaves)**: identical skeleton at high abstraction (record → analyze → share; plan → train), different sport semantics. The swim data model: strokes instead of pace-only running or speed/elevation cycling; distance grounded in pool course + counted lengths (no GPS in pools) instead of GPS tracks; per-100-class pace convention; stroke-based technique metrics; equipment as training tools within sets rather than mileage-tracked wear items (no shoe/bike analog); no route planning/navigation (a pool has no route; open water is map-only); safety-live-location less prominent. **This pass discharges the sport-family joint-review flag from the swimming side**: seam confirmed at the sport data model; the directory family deliberately enumerates sport-specific applications.
- **vs Endurance Training Platform**: plan-vs-record discriminator (inherited) applied. Plan-first triathlon platforms (TrainingPeaks, TriDot) are structurally plan-first across sports; swim apps import/sync workouts FROM them (FORM documents TrainingPeaks/TriDot import; MySwimPro documents TrainingPeaks sync) while keeping the swim workout record as the unit — corroborating that the plan lives on the platform side and the swim record lives here. A swim-lens product whose center is the adaptive plan (with swims as inputs) would belong to the endurance family.
- **vs Workout Tracking Application**: a generic workout tracker lacks swim semantics — no stroke model, no pool course/lengths, no length-based distance, no swim pace convention. Remove swim semantics → workout tracker.
- **vs Wearable Fitness Platform**: that Type organizes around the device/wearable as the hub for all activity and health data; a swimming training application organizes around the swim workout even when it pairs watches and goggles. Garmin Connect (device hub) and watch-native swim workouts (platform-native capture) sit on the other side of this seam; swim apps ingest from them.
- **vs Swim School Management (same directory family)**: organizer-side vs swimmer-side. Swim School Management runs a swim school business (students, classes, instructors, scheduling, billing); a Swimming Training Application serves the individual swimmer's own training. Different user, different objects, different workflow. Clean seam.
- **vs Race Management Platform**: organizer-side event operations; a swim app's race seed times and open-water race plans are swimmer-side conveniences.
- **vs Social Network**: drift test — Swim.com's pool leaderboards, clubs, and age/gender comparison are strong, but the swim record with analysis remains the unit; when feed/profile become primary and swims degenerate into shareable content, the product drifts toward a Social Network (Strava is the multi-sport social pole that still keeps the activity record central).
- **"Remove what to become another Type" judgments**: remove swim semantics → Workout Tracking Application; make the plan the record (multi-sport) → Endurance Training Platform; make the device the hub → Wearable Fitness Platform; make it organizer-side → Swim School Management; abstract the sport to running/cycling → Running/Cycling Application; make the feed primary → Social Network.

## Uncertainties

- Swim.com's Zendesk help-center article bodies were not extractable (title-only renders; API endpoint 404). Swim.com observations rest on the official product site, the clubs page, and vendor-published user testimonials — capability-level claims only; no precise limits or defaults asserted for Swim.com.
- FORM's support center was not fetched; FORM observations rest on official product pages (marketing-level for numbers: "1,500+ workouts", "50,000 community", accuracy percentages — recorded as vendor-stated, not promoted).
- TrainingPeaks and TriDot were not directly fetched (2 failed attempts each path abandoned); the plan-first boundary evidence is indirect (documented import/sync integrations at FORM and MySwimPro) plus the endurance pass's established discriminator.
- The per-100 pace convention is cross-product sport knowledge but was not directly quoted in fetched text; kept hedged ("commonly expressed per 100") in the final document.
- Garmin Connect and Apple Watch native swim workouts were not directly researched; they appear in the evidence only as integration/capture surfaces described by sampled products.
- USMS FLOG import is evidenced by a single vendor-published testimonial.
- Very old manual logbooks were not directly researched as products; the historical check relies on the documented manual-entry, picture-import, and print/paper paths in current products, which directly digitize that practice.

## Final Synthesis

A Swimming Training Application is an end-user application whose world is organized around the swim workout: a persisted, dated, per-swimmer record of a swimming session — pool or open water — carrying swimming performance semantics (distance grounded in the pool's course and counted lengths or in GPS, duration, pace in the sport's convention, stroke identity, and stroke-based technique metrics where devices provide), originating from the swimmer's own swimming through whatever capture mechanism the product offers — swim watch, smart goggles, manual entry, or import. Mature products add the structured workout model (sets with repetitions, distance, stroke, interval, effort, equipment; phase grouping), workout libraries and builders, multi-week training plans, ability-based personalization (seed times → intervals/rest), test sets and progress surfaces, device connectivity with automatic lap/stroke tracking and drill handling, open-water GPS mode, and a social layer (clubs, pool leaderboards, challenges) over a free-base or hardware+subscription commerce model. The structured-training pole, the tracking+community pole, the device-ecosystem pole, and the social-tracker swim module all satisfy the same invariant core. Boundaries are held against generic workout tracking (no swim semantics), endurance training platforms (plan-as-record — TrainingPeaks/TriDot sit there and push workouts into swim apps), wearable platforms (device-centric hubs), swim school management (organizer-side business), the running/cycling siblings (sport data model), and social networks (feed-first drift).
