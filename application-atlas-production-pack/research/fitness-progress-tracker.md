# Research Notes — Fitness Progress Tracker

## Research Goal

Understand what software sits under the directory leaf "Fitness Progress Tracker" (§28 Sports, Fitness & Recreation, listed between "Fitness Assessment Application" and "Running Application"): what its core objects are, who tracks what, how entries accumulate into a longitudinal record, how progress is rendered, and where the boundary lies against Fitness Assessment Application (joint-review flag carried from that pass), Workout Tracking Application, Running/Cycling Applications, Endurance Training Platform, Wearable Fitness Platform, Food/Calorie Tracking Application, and Personal Training Management.

## Initial Boundary (hypothesis before research)

- Hypothesis: the center is **the person's self-tracked body/performance metrics over time** — weight, body measurements, body composition, progress photos, performance benchmarks — recorded as discrete dated entries and rendered as trends/comparisons against the person's own earlier values or a target. No defined test protocol, no assessor, no normative scoring.
- Likely neighbors: Fitness Assessment Application (protocol + evaluator + evaluative reference), Workout Tracking Application (workout session as unit of record), Running/Cycling Applications (sport activity as unit of record), Endurance Training Platform (planned training schedule as plan of record), Wearable Fitness Platform (device-captured continuous streams), Food/Calorie Tracking Application (intake as unit of record), Personal Training Management (client business relationship as center), AI Fitness Coach (plan adaptation as center).
- Prior passes' recorded seams: endurance-training-platform pass wrote "Fitness Progress Tracker centers body-metric progress (weight, measurements) rather than the training process"; fitness-assessment-application pass wrote "the tracker centers the person's self-tracked body metrics over time (weight, measurements, photos) with no protocol, no assessor, and no evaluative reference" and carried a joint-review recommendation for this leaf.

## Research Questions

1. What is a metric entry — what do people track, and how is an entry structured (metric, value, date)?
2. How is the longitudinal record organized (per-metric series, entries list, week views)?
3. What progress surfaces exist (charts, trend lines, weekly averages, comparisons, before/after photos, predictions)?
4. How do goals work (target values, milestone goals, goal lines)? Is goal-setting definitional or common?
5. How does data get in (manual entry, update-all entry, device/health-platform import, coach entry, client entry via tasks)?
6. Who is the subject of record in each realization (self, client), and what roles exist (person, coach)?
7. Where is the boundary against assessment (protocol/evaluator/reference), workout logging (session as unit), wearable platforms (device streams), and food tracking (intake as unit)?
8. What does the market realization look like — standalone products, modules, embedded sections?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer levels:

1. **Happy Scale** — minimal consumer pole: a single-metric (weight) trend tracker whose entire product is smoothing, milestone goals, and predictions. Product page (Tier-2) with feature claims; support/FAQ page reachable but not separately fetched.
2. **Everfit** — coaching-platform pole where progress tracking is a first-class module (metrics, metric groups, goals, charts, client app, tasks for photos). Tier-1 help-center articles fetched (Metric Group Library, Track Body Metrics, Metrics collection).
3. **Exercise.com** — fitness-business platform pole with dedicated progress-photo and performance-reporting modules. Tier-2 platform feature pages fetched (marketing-level for workflow).
4. **MyFitnessPal** — boundary sample: a food-tracking application with a dedicated Progress tab (weight chart, weekly insights). Tier-1 help article fetched (Progress Overview).

Rejected/considered per network rules: Fitstream (root and /app returned empty twice — abandoned), Hevy help center (help.hevyapp.com and support.hevyapp.com both transport errors — abandoned), Trainerize/TrueCoach (403 / JS-blocked, abandoned by the earlier fitness-assessment pass as well). Everfit root page + help center used as the reachable coaching-platform documentation.

## Sources

- Happy Scale: https://www.happyscale.com/ (fetched 2026-09-08)
- Everfit: https://everfit.io/ , https://help.everfit.io/ , https://help.everfit.io/en/collections/2945594-metrics , https://help.everfit.io/en/articles/8906868-overview-metric-group-library , https://help.everfit.io/en/articles/2836313-track-body-metrics (fetched 2026-09-08)
- Exercise.com: https://www.exercise.com/platform/progress-photos/ , https://www.exercise.com/platform/performance-reporting/ , https://www.exercise.com/platform-sitemap.xml (fetched 2026-09-08)
- MyFitnessPal: https://support.myfitnesspal.com/hc/en-us , https://support.myfitnesspal.com/hc/en-us/articles/45246617814669-Introducing-Progress-Overview-Your-Progress-Personalized (fetched 2026-09-08)
- Atlas sibling passes (context): research/fitness-assessment-application.md, applications/endurance-training-platform.md, applications/cycling-application.md, applications/ai-fitness-coach.md (2026-09-07)

Source-access limitations: no dedicated multi-metric consumer body-progress tracker with fetchable official documentation was found (Fitstream, Hevy help, Trainerize, TrueCoach all unreachable). Consequently the "multi-metric body tracker" consumer pole is evidenced only indirectly (via Everfit's client-app body metrics and Exercise.com's client-facing capabilities). Exercise.com evidence is product-page (Tier-2) strength; no operational help-center detail for that product. No precise numeric limits, formulas, plan gates, or region gates are asserted in the final document.

## Product Observations

### Happy Scale (evidence layer A — official product page)

- Positioning: "Dieting is hard enough… Happy Scale smooths out your daily scale weights and makes insightful predictions about when you'll hit your goals."
- Core loop: record weight entries over time → application computes a smoothed trend (moving average) → user sees the trend line rather than raw daily fluctuation ("see your trend line moving down… even when your scale won't budge").
- Goals: overall weight-loss goal plus "small, incremental milestone goals" ("Break your weight loss goal into… milestone goals so you can focus on short-term, achievable goals").
- Predictions: "predictions about what you'll weigh in the future… how many weeks until you hit a certain weight, or what you'll weigh by a special date."
- Data in: manual entry; automatic import from Apple Health (wireless scale or another app syncing weights); sync between the user's own devices.
- Privacy: per-profile passcode protection ("Protect your profile from prying eyes").
- Scope: weight only. No workouts, no measurements, no photos, no coach. The whole product is the trend/goal/prediction rendering of one metric. Minimal pole for this Type.

### Everfit (evidence layer A — Tier-1 help center; coaching platform, progress tracking as a module)

- Metrics feature: "enter and track client progress through a multitude of metrics."
- Metric catalog: large default list of metrics; coach checks/unchecks per client; **custom metrics** creatable with name, type, and unit of measurement; selected metrics collect into a default group ("All Metrics").
- Metric Group Library: named groups of metrics; groups are shared with or private to team coaches; a group is **assigned** to a client from the client profile's Metrics tab; editing the library group does not retroactively change groups already assigned to clients (assignment is snapshot-like).
- Entries: add a result per metric with value and date/time; "Update All" adds results for multiple/all metrics at once; entries editable and deletable from "By Week" and "All Entries" views.
- Goals: per-metric "Add Goal" target number; the goal "will show up on the chart and Client mobile app"; "keep track of their progress towards the goal."
- Progress surfaces: per-metric charts with configurable chart type, data points, color, unit; Daily vs Weekly calculation toggle (weekly default for ranges over 3 months); metric-to-metric compare mode; pinned metrics (a small fixed number) on the client overview and client app.
- Client side: client app shows Body Metrics; coach can assign **tasks** so clients log measurements and progress photos on a recurring schedule ("improve accountability"); metrics can be disabled per client.
- Device metrics: steps (manual add supported), sleep, and heart-rate tracking exist as additional metric families.
- No assessment protocol, no scoring, no norms anywhere in the metrics feature: raw numbers in, charts out. The assessment-type work in such platforms lives in separate assessment/form modules (per the fitness-assessment pass).

### Exercise.com (evidence layer A for module existence and stated capabilities; marketing-level for workflow — fitness-business platform)

- Progress Photos module (platform feature page): "capture and compare workout progress pictures over time directly in your branded app"; "custom fitness progress tracking, enabling clients to log body metrics and upload workout progress photos"; "Track compliance and progress over time with photos, measurements, charts, graphs, and more."
- Automation: "Send automations that remind clients to take progress photos via SMS, email, and text."
- Client surfaces: iOS/Android/web apps for uploading progress photos, custom-branded.
- Business use of photos: clients' progress photos can be used as testimonials; "Easily get permission with e-signature waivers and contracts" — an explicit consent mechanism around body photos.
- Performance Reporting module: "Track goals, records, rep maxes… workout trends over time with charts, graphs, leaderboards"; workout logger with "track progress over time with key metrics."
- Relationship to assessments (from the earlier pass): the Assessments module captures "progress photos, measurements, and performance" and auto-assigns workouts — assessments are a separate module from the photo/measurement progress machinery; the platform realizes both this Type and Fitness Assessment as distinct modules.

### MyFitnessPal (evidence layer A — Tier-1 help article; boundary sample: food tracker with an embedded progress surface)

- Help center has a dedicated category "Progress Tracking and Insights"; promoted article "Progress Overview."
- Progress tab: weekly overview "pulled directly from what you've logged" — calorie breakdown vs calorie goal; **weight: "a chart showing how your weight has changed over time, so you can spot trends and track momentum"**; macros vs targets; reports over time.
- Everything updates as the user logs; guidance emphasizes consistency ("the more consistently you track, the more useful your Progress view becomes") and trends over single days ("A single off day matters a lot less than the trend you're building").
- Explicit limits: the Progress view "cannot log food for you" and "cannot change your goals" — logging and goal-setting live in their own sections; Progress is a reading/insight surface over the accumulated record.
- Not medical advice disclaimer — health adjacency of weight/body metrics.
- The product's unit of record is the food diary; the weight trend is a derived view over occasional body-metric entries. Boundary evidence: the same structures (weight entries, trend chart, goal reference) appear, but as a section inside an intake-centric product.

### Atlas sibling-pass context (evidence layer B for this Type's boundaries)

- Endurance Training Platform: centers the planned training schedule and the training process; its Related-Types table places Fitness Progress Tracker as centering "body-metric progress (weight, measurements) rather than the training process."
- Cycling Application: the ride is the unit of record; totals/trends/personal bests are derived views over activities.
- Fitness Assessment Application: defining core = protocol + assessed person + assessment record + evaluative reference; its pass recorded this leaf as the "raw measurement log" pole reached by removing the protocol and the evaluative reference.
- AI Fitness Coach: progress metrics exist there as inputs to the plan-adaptation loop; the center is the adapting plan, not the record itself.

## Cross-product Comparison

| Structure | Happy Scale | Everfit | Exercise.com | MyFitnessPal |
|---|---|---|---|---|
| Person as subject of record | per-user profiles | client profile, Metrics tab | client record in branded app | user account |
| Metric definitions | weight only (fixed) | default catalog + custom metrics (name/type/unit), grouped | body metrics + photos + performance metrics | weight + derived intake metrics |
| Dated entries | weigh-ins over time, manual or imported | add result (value + date/time) per metric; update-all; edit/delete; week/all-entries views | measurements + photos uploaded over time | weight entries; diary logs |
| Trend/progress surface | smoothed trend line (moving average) | per-metric charts, daily/weekly averages, metric comparison | photos/measurement comparisons, charts/graphs | weight chart, weekly overview |
| Reference point | own trend + goal + milestone goals | own history + per-metric goal line | own history; before/after photos; goals/records | own goals; diary history |
| Photos | — | progress photos via assigned tasks | progress photos + reminders + consent for reuse | — |
| Who enters | the person | coach or client (tasks prompt the client) | client (uploads), platform reminders | the person (manual/device import) |
| Device/platform data in | Apple Health import | steps/sleep/heart-rate families | — | connected apps and devices |
| Motivation layer | "true progress" trend framing, predictions, milestones | pinned metrics, client app, recurring tasks | engagement/testimonial framing | weekly insights, trend framing |
| Protocol / evaluator / norms | absent | absent | absent (assessments are a separate module) | absent |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (all three jointly held)

1. **The person as subject of record** — the application holds one person's own body/performance numbers; everything in the product is scoped to that person. In consumer realizations the person is the user; in coaching realizations it is the client, entered by the client or the coach on their behalf. Remove → aggregate/team dashboards or business software, not a personal progress record.
2. **Discrete dated metric entries accumulated over time** — the record consists of individual entries: a defined metric (a name/kind and, where configurable, a unit), a value, and a date. Entries may be manual, imported, or device-fed; they accumulate as the system of record and remain individually visible/correctable. Remove → a one-off calculator or a form with no history.
3. **The time-oriented progress view** — the accumulated entries are rendered as change across time: trend lines, charts with averaged views, comparisons against earlier values, timelines of photos, progress toward a target. The rendering is the product's purpose (making progress visible and motivating); without it the product is a data-entry log. Remove → a spreadsheet of numbers / a bare data logger.

Jointly-held is load-bearing: entries without a progress view = a log; a progress view without accumulated entries = an empty chart; a person without entries = a profile.

### L1 — Common Mature Structure (very common, not definitional)

- **Goal/target on a metric** — a target value the person (or their coach) sets; the goal is rendered on the chart as a reference line or as milestone sub-goals. Present in Happy Scale (goal + milestones), Everfit (per-metric goals), Exercise.com ("track goals"), MyFitnessPal (calorie/weight goals). Common — but progress against one's own earlier values is an equally valid reference, so goals are not required by the definition.
- **Multi-metric catalogs with custom metrics** — a default list of trackable metrics (weight, body measurements, composition, benchmarks, device metrics) plus user-/coach-defined metrics with name and unit. Single-metric products (Happy Scale) satisfy L0, so catalog breadth is not definitional.
- **Trend derivation** — smoothing or averaging over raw entries (moving averages, weekly averages) so progress reads through daily noise. Common; the underlying entries remain the record.
- **Entry conveniences** — one-shot "update all metrics," edit/delete of past entries, week and all-entries views.
- **Progress photos** — a dated photo timeline compared over time; common in coaching/business implementations, absent from minimal weight trackers. Not definitional.
- **Device/health-platform import** — weights from scales, steps/sleep/heart-rate from wearables, health-platform sync.
- **Prompting/reminder machinery** — recurring tasks or automated reminders so entries keep accumulating (coaching realizations).
- **Personal privacy posture** — the record is sensitive personal body data; profile passcode protection, client-scoped visibility, and (where photos are reused commercially) explicit consent mechanisms.

### L2 — Variant / Optional Structure

- Packaging pole: standalone consumer tracker (dedicated product) vs module inside a coaching/fitness-business platform vs embedded section inside a food tracker, workout logger, or wearable platform. The module/embedded realizations carry the same three L0 structures.
- Metric domain: weight-only; body measurements/composition; performance benchmarks (rep maxes, records); device metrics (steps/sleep/heart rate). Mixes vary per product.
- Who enters: the person; the coach on the person's behalf; devices/imports; task-prompted client entry.
- Prediction/forecast surfaces: trend-based projections ("when you'll hit your goal," "what you'll weigh by a date") — present in the trend-math pole; not required.
- Photo consent/compliance machinery for business reuse of progress photos (single-product documented in this sample; treated cautiously).
- Insight/analysis layers: weekly summaries, pattern highlights, AI-adjacent advice surfaces.

### L3 — Vendor-specific (research notes only)

- Happy Scale: moving-average smoothing, milestone-goal breakdown, date/weight predictions, Apple Health import, per-profile passcode.
- Everfit: Metric Group Library with shareable groups, snapshot semantics of assigned groups, pinning a small fixed number of metrics, per-client metric disabling, By Week/All Entries views, task-based photo/measurement logging, steps/sleep/heart-rate families.
- Exercise.com: progress-photo reminder automations (SMS/email), testimonial reuse with e-signature consent, leaderboards/gamification, rep-max progressions.
- MyFitnessPal: Progress tab gated by app version/region/language (not asserted in the final document), premium-gated macro tips, Plans tab relocation.

## Historical / Market-Sample Check

- Would older, regional, or platform-native products fit the L0? The paper era satisfies all three structures: a weight chart on the fridge with dated weigh-ins and a drawn trend toward a target weight; a bodybuilder's logbook with monthly tape measurements and progress photos compared against earlier ones; a training journal with benchmark lifts recorded over months. Person + dated entries + progress view, no apps, no device sync, no cloud, no AI.
- The definition does not depend on the modern consumer-mobile pattern: a coach's paper card tracking each client's weekly weight (the module realization without software) fits the same structures.
- Conclusion: L0 survives the historical/regional check. Device imports, smoothing math, predictions, photo consent machinery, and coaching-task automation stay in L1/L2/L3.

## Vendor-specific Findings

- Trend mathematics as the product's identity (Happy Scale's moving average) is unique in the sample; other products plot raw or weekly-averaged values.
- The metric-group library with assignment-snapshot semantics (Everfit) is unique in the sample; Exercise.com realizes per-client metric logging without a published group-library concept on the fetched pages.
- Commercial reuse of progress photos with explicit e-signature consent (Exercise.com) is unique in the sample and is business-model-driven, not Type-driven.
- Region/version-gated progress surfaces (MyFitnessPal) show that even embedded realizations treat Progress as a productized surface — but the gating is vendor distribution detail.

## Boundary Findings

1. **vs Fitness Assessment Application** (joint review — see resolution below): the assessment Type's defining core is protocol + assessed person + assessment record + evaluative reference. This Type has no defined battery, no assessor role, no scoring against standards/norms; entries are raw personal metrics, and the reference is the person's own earlier values or a target, never a normative interpretation. A coach recording a client's weight weekly is this Type's structure; the same platform administering a scored test battery is the assessment Type's structure — the two coexist as separate modules in real platforms.
2. **vs Workout Tracking Application**: the workout tracker's unit of record is the executed session (exercises, sets, reps, load). Progress charts in workout loggers are a derived view over sessions. In this Type the metric entry about the person is the unit of record, and a product may carry no workouts at all (Happy Scale). When session logging is the center, the product is the workout Type; when person-metrics-over-time is the center, it is this Type.
3. **vs Running Application / Cycling Application**: sport applications center the captured activity (GPS track, ride/run metrics). Totals/trends/PRs are derived views. This Type centers body/performance metrics independent of any activity capture.
4. **vs Endurance Training Platform**: the endurance platform centers the planned training schedule and the training process (plan → execute → analyze). This Type centers the person's metric record; no plan, no scheduling, no load management.
5. **vs Wearable Fitness Platform** (unprocessed leaf): device platforms center the device ecosystem and continuous captured streams; dashboards aggregate device data. This Type centers discrete person-scoped entries, which may or may not come from devices. Device-fed entries alone do not move a product into the wearable-platform Type; centering the device ecosystem does.
6. **vs Food / Calorie Tracking Application** (unprocessed leaf): intake-centric products log meals; their weight chart is a derived view over occasional body entries (MyFitnessPal's own help states the Progress view cannot log food). When intake logging is the center, the product is the food-tracking Type; this Type is the reverse center of gravity.
7. **vs Personal Training Management** (unprocessed leaf): PT business software centers the client business relationship (programs, packages, billing, scheduling); progress tracking is one module. The market realizes this Type frequently as a module inside such platforms — the module carries the L0; the platform does not become this Type (same pattern as the assessment pass recorded).
8. **vs AI Fitness Coach** (processed): the coach centers the adapting plan; progress metrics are inputs. No plan/adaptation loop exists in this Type.
9. **"去掉什么就变成另一个 Type" 判据**: add a defined test battery + evaluator scoring + normative reference → Fitness Assessment Application; make the workout session the unit of record → Workout Tracking Application; make captured sport activities the unit of record → Running/Cycling Application; add the planned training schedule as plan of record → Endurance Training Platform; center the device ecosystem → Wearable Fitness Platform; center intake logging → Food/Calorie Tracking Application; center the client business relationship → Personal Training Management; strip the longitudinal accumulation → a calculator.

### Joint review resolution — fitness-assessment-application vs fitness-progress-tracker

The flag carried from the 2026-09-07 assessment pass is discharged from this side. Both passes, with disjoint samples (FitnessGram/FMS/Exercise.com/Hawkin/PT Distinction vs Happy Scale/Everfit/MyFitnessPal), converged on the same seam: assessment = protocol + evaluator + evaluative reference (scored records); progress tracker = self-/coach-tracked raw metrics referenced only to the person's own history or a target. The assessment pass's uncertainty about consumer self-assessment apps was checked from this side: no sampled consumer product exhibits protocol/scoring semantics (Happy Scale and MyFitnessPal carry raw metrics only; MyFitnessPal explicitly separates logging/goals from the progress view). The seam is symmetric and holds in both directions; both leaves stand as separate Types; the "module inside PT platforms" realization applies to both and does not merge them.

## Taxonomy Observation

The market realizes this Type in three packaging poles: (a) dedicated consumer trackers — market-documented strongest at the single-metric (weight) pole; (b) modules inside coaching/fitness-business platforms — with metric catalogs, goals, charts, photos, and client-task machinery; (c) embedded sections inside food trackers / workout loggers / wearable platforms — weight trends and weekly insights as a derived surface. No dedicated multi-metric consumer product with fetchable official documentation was found in this pass (Fitstream and several workout-logger help centers unreachable), so the "dedicated multi-metric" pole is evidenced indirectly and the final document asserts that pole cautiously. No directory change proposed; the leaf is legitimate as a Type (dedicated products exist; the three structures recur across all poles).

## Uncertainties

- Dedicated multi-metric consumer body-progress trackers (measurements + photos without coaching) could not be directly documented (source failures); their existence is asserted at low strength and their internal structure inferred from the module/embedded realizations.
- Happy Scale evidence is product-page strength; FAQ/support pages were not separately fetched; smoothing mechanics described qualitatively only.
- Exercise.com workflow detail (how clients log measurements step-by-step) is marketing-level, not help-center-level.
- Trainerize/TrueCoach progress modules unverified (blocked); the PT-platform pole is evidenced by Everfit only.
- Whether benchmark/performance metrics (rep maxes, records) belong more to workout tracking than to this Type is a soft seam; sampled platform realizations include them alongside body metrics, so they are treated here as an optional metric family, not a definitional one.
- Wearable Fitness Platform is unprocessed; the boundary finding recorded here will need reconciliation when that leaf is processed.

## Final Synthesis

A Fitness Progress Tracker is best understood as **the person-facing record of their own fitness metrics over time**: a set of defined metrics (weight, body measurements, composition, benchmarks, device metrics) is tracked for one person as discrete dated entries; the entries accumulate as the system of record and are rendered as time-oriented progress — trend lines, averaged views, comparisons against earlier values, before/after photos, and progress toward targets. The record is raw by construction: no test battery, no evaluator, no normative scoring; the only reference points are the person's own history and their own goals. The defining core is deliberately small (person + dated metric entries + progress view) so that it holds for the paper-chart era, the single-metric trend app, the coaching platform's client module, and the embedded weight-trend tab of a food tracker alike. Everything else — goal lines, custom metric catalogs, smoothing, photos, device imports, reminders, predictions, consent machinery — is common mature structure, variant, or vendor detail. The Type's edge is defined by what centers the product: the person's own metrics over time (here), the scored evaluation event (Fitness Assessment Application), the workout session (Workout Tracking Application), the training process (Endurance Training Platform), the sport activity (Running/Cycling), the device ecosystem (Wearable Fitness Platform), the intake diary (Food/Calorie Tracking), or the client business relationship (Personal Training Management).
