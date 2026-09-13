# Research Notes — Wearable Fitness Platform

Research date: 2026-09-09
Leaf: Wearable Fitness Platform (§28 Sports, Fitness & Recreation)
Slug: wearable-fitness-platform

## Research Goal

Understand what a Wearable Fitness Platform actually is as an Application Type: what the platform's world is organized around, what the device contributes vs what the software contributes, the core loop between wearer, device, and platform, the lifecycle of device and data, and the boundaries against the neighboring §28 Types (Running/Cycling/Swimming Applications, Workout Tracking, Fitness Progress Tracker, AI Fitness Coach, Sports Performance Analytics, Corporate Wellness) and against adjacent Types elsewhere in the directory (Remote Patient Monitoring, health platforms/aggregators, smartwatch territory).

## Initial Boundary Hypothesis

Four sibling passes already recorded seams toward this leaf (kept as forward flags):

- running-application / cycling-application / swimming-training-application passes: "that Type organizes around the device/wearable as the hub for all activity and health data; a Running/Cycling/Swimming Application organizes around the run/ride/swim even when it pairs watches."
- fitness-progress-tracker pass: "device platforms center the device ecosystem and continuous captured streams; [that Type] centers discrete person-scoped entries... Device-fed entries alone do not move a product into the wearable-platform Type; centering the device does." Reconciliation recommended.
- ai-fitness-coach pass: "wearable platforms center on measurement (recovery, strain, sleep, activity) with coaching as an optional add-on; this Type centers on deciding and adapting training."
- sports-performance-analytics pass: "consumer self-tracking surfaces center the individual's own data vs this Type's staff-facing organizational analysis over a population."

Working hypothesis to test: the Type is the consumer device-ecosystem platform — worn sensing device + companion software/service that manages the device and accumulates and interprets the wearer's body/activity data.

## Research Questions

1. What is the platform's center of gravity — the device, the person, the workout, or the program?
2. What exactly does the wearer do with the platform: setup, daily use, long-term use?
3. What flows up (device → platform) and what flows down (platform → device)?
4. Which objects live in the platform: days, metrics, sessions, scores, goals, devices, the person?
5. What lifecycle exists: device lifecycle (pair, configure, update, replace, remove) and data lifecycle (capture, sync, correct, export, delete)?
6. What rules matter: account-device binding, multi-device, data ownership/erasure, membership gating?
7. Where is the boundary against workout loggers, progress trackers, sport apps, health aggregators, RPM, corporate wellness?
8. Historical check: do older device generations (chest strap + desktop software, clip-on trackers) satisfy the same definition?

## Representative Products

| Product | Position / philosophy | Customer tier | Evidence quality |
|---|---|---|---|
| Fitbit (Google) | mass-market consumer companion app + trackers/watches/scale; freemium | consumer mass market | official Help Center content obtained via search after direct fetch timeouts (degraded access) |
| Garmin Connect | sport/outdoors device vendor ecosystem; web + mobile + desktop sync; free software with device | consumer sport/outdoor | strong — official owner's manual directly fetched + official product pages |
| Polar Flow | heritage training vendor; web service first; training-science centered | consumer sport/serious amateur | strong — official web service + support portal directly fetched |
| Whoop | screenless band; membership-first; recovery/strain methodology | performance consumers & pro athletes | official site content via search after 403 (degraded access) |
| Oura | ring form factor; sleep/readiness-first; membership model | consumer wellness | strong — official member-care help center directly fetched |

Selection rationale: market representation (two mass-market, two sport-vendor, two subscription-first poles), different product philosophies (screen-free vs smartwatch, training-first vs sleep-first vs recovery-first), different customer tiers, different business models (device purchase + free software vs membership including hardware).

## Sources

Directly fetched (2026-09-09):

- Garmin — Forerunner 165 Series Owner's Manual, "Garmin Connect" chapter: https://www8.garmin.com/manuals-apac/webhelp/forerunner165series/EN-SG/GUID-FA3625A5-F7F3-4494-B5F0-35C3339BAF40-787.html (A)
- Garmin — connect.garmin.com and garmin.com/en-US/connectapp product pages (content obtained via search results) (A−)
- Polar — Polar Flow web service landing: https://flow.polar.com/ (A)
- Polar — Flow web service support portal: https://support.polar.com/support/flow (A)
- Oura — Member Care help center root: https://support.ouraring.com/hc/en-us (A)
- Oura — Oura App category listing: https://support.ouraring.com/hc/categories/27782541623059 (A)

Search-mediated official content (direct fetch failed; excerpts from official pages):

- Fitbit — Help Center articles: "How do I set up my Fitbit device?", "How do Fitbit devices sync their data?", help-center topic listing, fitbit.com/about (search excerpts; direct fetches of support.google.com/fitbit and fitbit.com timed out twice)
- Whoop — whoop.com "How WHOOP works", whoop.com/us/en, whoop.com/us/en/membership, App Store listing (search excerpts; direct fetches returned 403 twice)

Not researched (time/network budget): Xiaomi Mi Fitness / Huawei Health (regional super-app poles), Apple Watch + Apple Fitness/Health (platform-native hybrid), Amazfit/Zepp, Suunto.

Evidence layers used below: A = directly observed on official source; B = cross-product commonality; C = canonical inference.

## Product Observations

### Fitbit (Google) — evidence A− (official Help Center content via search excerpts)

- **Setup loop**: download Fitbit app → sign in with (Google) account → create account entering height/weight/sex "to calculate your stride length and to estimate distance, basal metabolic rate, and calorie burn" → pair ("connect") device to phone. Setup happens on the phone through the app; device connects to charger first.
- **Account-device binding**: devices attach to an account; "Add or replace a Fitbit device on an existing account"; "Can I sync more than one Fitbit device to the same account?" — yes, "for a complete view of your activity". Removing a device deletes unsynced data; erasing data before giving the device to someone else.
- **Sync definition** (verbatim, official help): "Syncing is the process that transfers the data your device collects to your Fitbit dashboard. The dashboard is where you can track your progress, see how you slept, set goals, log food and water, challenge friends, and much more." Automatic sync throughout the day; each app opening syncs when device nearby; manual Sync Now; last-synced time, firmware version, and battery level visible in the app.
- **Device population**: trackers, watches (plus Google Pixel Watch), Aria scales (Wi-Fi, sync after each weigh-in), Ace kids line.
- **Record content** (help topics): steps, Active Zone Minutes, heart rate, sleep score/stages, readiness score, SpO2, breathing rate, temperature, stress/mindfulness, menstrual health, workouts/GPS, food/water logging, goals.
- **Feedback loop**: dashboard/goals/progress; "challenge friends" (social); Premium tier (implied by topic structure).
- **Transition observation**: help center shows mid-migration branding — same articles appearing under "Google Health" app naming; topic list includes medical-adjacent features (ECG app, Irregular Rhythm Notifications, Loss of Pulse Detection on Pixel Watch) with medical disclaimers. Treated as vendor-current drift, not definitional.

### Garmin Connect — evidence A (owner's manual directly fetched) + A−

- **Self-definition** (connect.garmin.com): "the tool for tracking, analyzing and sharing health and fitness activities from your Garmin device"; "an extension of your Garmin device"; "Made for your Garmin device".
- **Function list from official manual** (Forerunner 165): store activities ("upload that activity to your Garmin Connect account and keep it as long as you want"), analyze data (time, distance, elevation, heart rate, calories, maps, pace/speed charts, customizable reports), plan training (fitness goals, day-by-day training plans, Garmin Coach adaptive plans), track progress (daily steps, goals, competition with connections), share (friends follow activities), manage settings ("customize your watch and user settings on your Garmin Connect account").
- **Device lifecycle through the platform**: pairing watch↔phone; automatic sync when in range; software updates pushed to the watch through the app; Garmin Express desktop application as the computer path (Add Device, upload activity data, send workouts/training plans to the watch, music, Connect IQ app management); manual sync from the watch's controls menu.
- **Two-way flow**: data up (activities, health stats) and content down (workouts, training plans, courses, settings, updates).
- **Record surfaces**: "Your day at a glance" — customizable health-stat display; weekly/monthly/yearly averages; historic tracking.
- **Common structure**: challenges, badges, groups, likes/comments; Connect+ premium plan now gating some features (workout database, animated exercises for new devices); companion apps family (Garmin Dive/Golf/Jr., Connect IQ Store).

### Polar Flow — evidence A

- **Self-definition** (flow.polar.com): "Free online tool for planning and following up on your training, activity and sleep. Get the most out of your Polar device with Polar Flow." Device onboarding: "Connect your device with Polar Flow and you're ready to go" (flow.polar.com/start).
- **Device ecosystem** (support portal): watches (Vantage/Pacer/Grit/Ignite/Street X families), Loop screen-free band, chest straps (H10/H9), optical armbands (Verity Sense, OH1+), Polar Beat phone app as sibling capture app. "Polar Flow is an important part of the Polar ecosystem for our newest devices and all future products." Products are *registered* on the account: "manage the favorites for each Polar device you have registered on your Polar account."
- **Two-way sync**: create sport profiles, training targets, favorites, routes in the web service → sync to device; train → sessions sync up. Explicit troubleshooting topic: changes made in Flow must be synced down to the device. FlowSync desktop program for computer-based sync.
- **Record & diary**: Diary/calendar as the organizing surface (training sessions per day, activity); manual entry supported ("add a training session to Polar Flow web service manually" — date/time/sport/duration/notes); edit and trim sessions; session analysis views; relive (GPS sessions); export GPX/TCX/CSV/FIT; RR-interval CSV export from ECG-sensor sessions; download all personal data; account deletion.
- **Interpretation layer**: Training Load Pro (cardiovascular + perceived load), Recovery Status (cumulative load tolerance), Training Benefit textual feedback, Sleep Plus automatic sleep detection ("wear your Polar device to bed. No sleep mode activation is needed"), Polar Running Program (adaptive plan from personal attributes), Season Planner (periodized season planning), sport profiles (up to 20 on device, customizable training views).
- **Business/lifecycle**: Flow free with device; "minimum of five years of product support service from the sales start date"; firmware updates end after support window. Flow for Coach exists as a business-side sibling (variant). Third-party sync: Strava, TrainingPeaks (plans down + sessions up), MyFitnessPal (activity data out).
- **Polar Loop** description (own site): "screen-free, subscription-free fitness band" — a same-vendor counter-pole to Whoop's membership model.

### Whoop — evidence B (official site content via search excerpts; direct fetch 403)

- **Self-definition**: "The WHOOP device and app work together to turn your data into clear, personalized coaching." Loop: wear 24/7 → measure & monitor (sleep, strain, stress, recovery, heart health) → receive guidance → make changes (habit formation).
- **App Store listing** (official): "WHOOP is screenless, so all your data lives in the WHOOP app"; "The WHOOP app requires a WHOOP wearable." — the purest device-platform coupling statement in the sample.
- **Record & interpretation**: Sleep score/performance, Sleep Planner (sleep need from recent strain/debt/naps), Strain score (0–21 scale, cardiovascular + muscular load), Recovery (0–100% computed during sleep from HRV, resting HR, respiratory rate, SpO2, sleep performance, skin temperature), Journal (behavior logging, "over 140 behaviors"), Healthspan/"WHOOP Age", cycle/pregnancy insights, strength trainer muscular load.
- **Membership model**: hardware included in membership tiers ($199–359/yr documented); "Your WHOOP membership starts when you pair and activate your WHOOP device" — pairing/activation is the commercial trigger for the whole platform.
- **Strava integration** both directions.

### Oura — evidence A

- **Help-center structure** (Oura App category) — the app's world organized as: Readiness (score + contributors: resting HR, respiratory rate, HRV, body temperature), Sleep (score, stages, debt, graphs, Sleep Health Hub), Activity (score, workout recording, live tracking, automatic activity detection), Metabolic Health (meals, glucose tracking integration, Health Panels), Women's Health (cycle, pregnancy, menopause insights), Heart Health (cardiovascular age, VO2 max, live HR), Stress Management (daytime stress, resilience), Insights & Reports (Trends, Tags, Reports, EHR import, "Oura Advisor" AI), Mindfulness content.
- **App settings**: Set Up the Oura App (pairing/onboarding), notifications, airplane mode, Rest Mode.
- **Device lifecycle through platform**: firmware updates managed via app ("Enable Automatic Firmware Updates" article), charger/connection troubleshooting.
- **Business model**: Membership Hub ("manage your account and membership") — membership attached to ring ownership; HSA/FSA purchase article.
- **Integrations**: Apple Health, Health Connect (Android), Dexcom Stelo CGM, Apple Watch companion app.

## Cross-product Comparison

| Dimension | Fitbit | Garmin Connect | Polar Flow | Whoop | Oura |
|---|---|---|---|---|---|
| Worn device population | trackers/watches/scale/kids | watches/bands (+ sensors) | watches/Loop band/chest straps/armbands | screenless band (required) | ring |
| Pairing/activation via platform | ✔ account pairing, add/replace devices | ✔ pair watch, Add Device (Express) | ✔ "connect your device", register on account | ✔ pairing/activation starts membership | ✔ set-up app + ring pairing |
| Device management down-flow | settings, firmware, battery visible | settings, workouts, courses, music, updates, Connect IQ | sport profiles, targets, favorites, routes, firmware | (device has no screen; haptics/alarms configured in app) | firmware updates, modes |
| Automatic body capture | all-day steps/HR/sleep | 24/7 stats + activity recording | 24/7 HR/activity, automatic sleep detection | 24/7, "every second" claimed | continuous overnight + day |
| Personal longitudinal record | dashboard, trends | "keep as long as you want", averages, history | diary/calendar, history | app-based history | trends, hubs |
| Interpretation scores | sleep score, readiness, AZM | body battery-class stats, training status (vendor naming varies) | training load, recovery status, training benefit | recovery/strain/sleep scores, healthspan | readiness/sleep/activity scores |
| Goals/challenges/badges | ✔ + challenges with friends | ✔ challenges, badges | goals in training context | targets (strain target) | activity goal |
| Workouts/sessions | ✔ + GPS | ✔ core | ✔ core, manual add, edit/trim | ✔ auto-detected + logged | ✔ auto-detection + live tracking |
| Manual entry | ✔ (add/edit/delete data) | limited in consumer flow | ✔ explicit (sessions) | journal behaviors | tags/meals |
| Export/data ownership | add/edit/delete in app | ✔ | ✔ GPX/TCX/CSV/FIT, download all, delete account | (not observed) | ✔ reports, EHR import direction is inbound |
| Third-party sync | ✔ connect other apps | ✔ | ✔ Strava/TrainingPeaks/MyFitnessPal | ✔ Strava | ✔ Apple Health/Health Connect/CGM |
| Social layer | challenges/friends | ✔ strong | light (sharing links) | teams (minimal claim) | (not observed in fetch) |
| Business model | device purchase + freemium premium | device purchase, software free, + premium plan | device purchase, software free (subscription-free band pole) | membership incl. hardware | ring purchase + membership |
| Primary surface | phone app (web dashboard retiring) | phone app + web + desktop sync | web service + phone app + desktop sync | phone app only (screenless device) | phone app |

Reading of the comparison (B, cross-product):

1. Every product couples a **body-worn device population** to a **companion platform** — pairing/activation always happens through the platform, and the device is always identified per account (multi-device supported in several).
2. Every product carries a **two-way loop**: body data flows up; configuration, plans/workouts, and firmware flow down. The down-flow is the half that distinguishes a *platform* from a data sink.
3. Every product accumulates a **personal longitudinal record** organized around days and the wearer's body, rendered back as **daily status + scores/goals + trends**.
4. Every product supports **workout/exercise capture**, but no product is *only* workout capture — the always-on body record is present in all five.
5. Differences are concentrated in: form factor, which body signals are measured, score vocabulary, business model, social layer, and how much training planning lives in the platform. These are variant axes, not the Type's identity.

## Canonical Model (L0–L3)

### L0 — Defining Invariant (three jointly-held structures)

**1. The worn device population as the platform's origin and managed center.**
The platform exists around a body-worn sensing device (or family of them) defined by the platform's own ecosystem. The device is brought into the platform by pairing/activation/registration through the platform itself, is managed there (settings, firmware, modes), and its identity is bound to the wearer's account. Capture happens *on the body* — automatic during wear, not dependent on a user-initiated recording decision for the everyday body signal.
*Remove → a fitness/health application with manual entry and optional imports (Workout Tracking / progress-tracker / health-platform territory), or a plain device-management utility.*

**2. The wearer's longitudinal body-centered record.**
The platform accumulates the wearer's own captured body-signal and activity data as a persistent personal record organized around days (and dated sessions within days), held over time — the platform is the memory of the device. Sibling records: activity days, sleep nights, workouts, measured body signals.
*Remove → device firmware/companion utility with no accumulated record; or an anonymous telemetry store with no person-centered memory.*

**3. The wearer-facing interpretation loop.**
The platform renders the record back to the wearer as an actionable daily view — day-at-a-glance status, computed scores/feedback, progress against goals, trends — so the wearer adjusts behavior (train, rest, sleep, habits), and the loop repeats the next day. Compute vocabulary varies per product; the render-and-act loop is the invariant.
*Remove → a data store/export pipe with no consumer-facing meaning (a device data platform, not a fitness platform).*

Jointly-held load-bearing analysis (C):
- 1 alone = device management/firmware utility
- 2 alone = health data store / aggregator platform
- 3 alone = fitness app or progress tracker
- 1+2 without 3 = device telemetry pipeline
- 1+3 without 2 = companion with amnesia (no longitudinal value)
- 2+3 without 1 = workout tracker / fitness progress tracker / health platform

### L1 — Common Mature Structure (standard, market-expected, not definitional)

- Phone app as the primary daily surface; web and/or desktop companion surfaces (Garmin, Polar keep first-class web services; Fitbit has retired web dashboard emphasis; Whoop is app-only — so the *app* is common, the web is variant).
- All-day metric set: steps, calories/energy, active minutes, continuous/all-day heart rate.
- Automatic sleep tracking with a sleep score/stages.
- Workout/exercise sessions: GPS where relevant, per-sport profiles, session analysis.
- Goals, streaks, reminders, achievements/badges.
- Trends/averages over weeks/months/years.
- Multi-device support on one account; accessories (scales, straps) attached to the same record.
- Third-party integration: phone health platforms (Apple Health / Health Connect) and sport services (Strava, TrainingPeaks).
- Manual entry as a fallback for gaps.
- Privacy/consent controls and data export/delete paths.
- Firmware updates delivered through the platform.

### L2 — Variant / Optional Structure

- **Business model**: device purchase + free software (Garmin, Polar) vs membership including hardware (Whoop) vs ring + membership (Oura) vs freemium premium tiers (Fitbit). Subscription-free band pole exists (Polar Loop).
- **Form factor**: wrist band/watch, ring, chest strap, armband, clip-on (older generations), screenless vs display device; smartwatch drift (apps, payments, music — boundary to smartwatch territory).
- **Measured-signal breadth**: HRV, SpO2, skin temperature, respiratory rate, ECG/AFib-class features, blood-pressure-class insights, glucose integration. Regulatory posture varies (wellness claims vs regulated medical features with disclaimers).
- **Interpretation vocabulary**: readiness/recovery scores, training load/status, stress monitoring, healthspan/aging scores — vendor-specific names over the same render-and-act loop.
- **Coaching layer**: adaptive training plans (Garmin Coach, Polar Running Program), AI advisor (Oura Advisor), habit/journal coaching (Whoop). Present in most, absent or thin in some; the deciding authority may be algorithmic or plan-template — a variant axis, and the boundary marker toward AI Fitness Coach when coaching becomes the center.
- **Social layer**: challenges, groups, followers, sharing links — strong to absent across the sample.
- **Content**: mindfulness/meditation libraries, workouts databases.
- **Nutrition**: food/water logging present in some (Fitbit, Oura meals), absent in others.
- **Family/kids and regional editions** (Fitbit Ace; regional app stores).
- **Coach/business-facing sides** (Flow for Coach; enterprise dashboards) — sibling Types' territory.

### L3 — Vendor-specific (Research Notes only)

- Whoop strain scale 0–21; recovery 0–100% computed during sleep; Journal "140+ behaviors"; membership tiers One/Peak/Life with hardware included; lifetime warranty framing.
- Oura Advisor AI; Health Panels; Metabolic Hub; GLP-1 Insights; Circles-class social (not verified in fetch); Membership Hub naming.
- Garmin Connect IQ store, Livetrack, Garmin Coach, Connect+ plan gating workout database/animated exercises, Garmin Express desktop, Dive/Golf/Jr. companion apps, Garmin's announced TrainingPeaks/TrainHeroic acquisition (seen in site banner).
- Polar Season Planner, sport-profile limit "up to 20 on device", RR-interval export, FlowSync, five-year product-support policy, Polar Loop "screen-free, subscription-free" positioning, Polar Beat sibling app.
- Fitbit Aria scale Wi-Fi sync, Active Zone Minutes naming, Google-account migration, "Google Health app" rebranding transition, Pixel Watch bundling, Today tab UI naming.
- Fitbit help topic naming and premium gating specifics.

## Vendor-specific Findings

Summarized above in L3. Cross-cutting vendor-current drifts worth flagging (not definitional): (a) screen-free band + membership model (Whoop, and Polar Loop as the subscription-free counter-pole); (b) medical-adjacent feature expansion with disclaimers (Fitbit/Pixel Watch ECG/AFib, Whoop ECG tier); (c) platform-native absorption — Fitbit surfaces migrating under Google Health naming; (d) premium-plan gating creeping into historically-free software (Garmin Connect+).

## Boundary Findings

1. **vs Running / Cycling / Swimming Application** (sibling passes recorded the seam; ratified here from the device side): sport apps center the sport's dated session record with sport-specific performance semantics; the wearable platform centers the *device ecosystem and the wearer's continuous body record*, spanning all sports plus all-day health. A wearable platform can record runs/rides/swims; adding device-ecosystem centering to a sport app moves it into this Type; stripping it leaves the sport app. Seam confirmed symmetric: in this sample, run/ride/swim capture is one content family inside a broader device-centered world.
2. **vs Workout Tracking Application**: workout loggers center user-initiated exercise sessions (any source, manual-friendly). The wearable platform's invariant includes the automatic body record and the managed device — a workout logger without a device ecosystem stays out.
3. **vs Fitness Progress Tracker** (reconciliation requested by that pass — discharged here): progress trackers center discrete person-scoped metric entries and their change over time, source-agnostic. This Type centers the device ecosystem and the continuous capture streams feeding a day-structured record; a progress view inside a wearable platform is one surface of leg 3, not the product's center. Device-fed entries alone do not make a wearable platform; centering the device does. Both Types stand; seam is center-of-gravity, not feature presence.
4. **vs AI Fitness Coach** (their pass's seam; ratified): coaching products decide and adapt training; wearable platforms measure, record, and interpret, with coaching as an optional layer (Garmin Coach, Oura Advisor are add-on layers inside a measurement-centered world). When the adaptive-decision loop becomes the center, the product drifts to that Type.
5. **vs Sports Performance Analytics** (their pass's flag; ratified): staff-facing analysis over an organizational athlete population vs consumer self-tracking of one's own body. Different user, different subject of record, different decision loop.
6. **vs Corporate Wellness Platform**: employer-side program operation over an enrolled employee population; wearable platforms appear there as data sources and sync targets, not as the program operator.
7. **vs Remote Patient Monitoring**: clinician-side enrolled-patient monitoring with a clinical intervention loop and medical devices; wearable platforms are consumer self-service with wellness positioning (medical-adjacent features exist but no care-team loop of record). The EHR-import direction in Oura and the regulated-feature disclaimers in Fitbit/Whoop are the observable edge of this seam.
8. **vs Health platforms / aggregators** (Apple Health, Google Health, Health Connect class): aggregation hubs that centralize third-party data without (necessarily) their own worn device. The wearable platform originates data from its own device population. Hybrid cases exist (platform vendors whose OS health hub coexists with their wearable — Apple; and the Fitbit→Google Health transition observed mid-migration); recorded as a market-structure note, no directory change proposed.
9. **vs Smartwatch / device hardware territory**: the Application Type is the platform (software + service + ecosystem rules), not the device. When general-purpose computing on the wrist (apps, calls, payments) becomes the product's center, it leaves this Type's subject matter.
10. **Remove-what test (C)**: remove the worn-device population → generic fitness/health app; remove the longitudinal record → firmware utility; remove the interpretation loop → telemetry store; remove the account-bound device management → health aggregator. All four removals land outside the Type; the three structures are jointly necessary.

## Historical / Market-Sample Check (§24)

Would older, regional, platform-native products still fit the L0?

- **Chest-strap + desktop-software era** (the classic training-vendor setup that Polar's ecosystem descends from): body-worn strap capturing heart rate during exercise; desktop software registered to the user accumulating a longitudinal training record; analysis/feedback rendered back (train → upload → review → adjust). Satisfies all three L0 structures with no phone app, cloud, sleep staging, or subscription. The L0 deliberately does not require 24/7 wear, a phone, or a cloud.
- **Clip-on tracker era** (belt-clip step trackers syncing to a web dashboard): worn device, automatic step capture, web record, progress/goals view. Satisfies the core. The L0 does not require heart rate, sleep, or a wrist form factor.
- **Regional super-app wearable ecosystems** (vendor app stores outside the researched sample): structurally the same core with a larger app shell; treated as variants without direct evidence.
- **Platform-native hybrids** (watch + OS health hub): the wearable-platform core remains identifiable inside the hub; recorded as an edge variant.
- **Exclusions confirmed**: a mechanical pedometer (no platform) fails all three legs; a phone-only step-counter app (no worn device) fails leg 1 → health-platform/tracker territory; a hospital telemetry system (not consumer, not self-managed) is RPM/monitoring territory.

The definition names no smartphone, no cloud, no 24/7 wear, no heart rate, no sleep score, no subscription. Historical check passed.

## Uncertainties

1. Fitbit and Whoop official pages were not directly fetchable (timeouts / 403); their observations rest on official-page content obtained via search excerpts. Feature details for those two (especially current tier gating and the Google Health migration end-state) are time-sensitive and treated as indicative, not precise.
2. Regional wearable ecosystems (Xiaomi/Huawei/Amazfit) not directly researched; their inclusion in L2 "regional variants" is inference from market structure, not observation.
3. Social-layer depth (Oura social features) and data-export behavior (Whoop) were not observable in fetched material; left unasserted rather than filled from memory.
4. Precise numeric limits observed in the sample (Polar's 20 sport profiles, Whoop's 0–21/0–100% scales, membership prices) are vendor-specific and kept out of the final document.
5. The exact current boundary of "Google Health vs Fitbit app" is a moving target; the final document deliberately describes the Fitbit-class platform generically.

## Final Synthesis

A Wearable Fitness Platform is the consumer device-ecosystem platform: a population of body-worn sensing devices bound to the wearer's account, managed through the platform (pairing, configuration, firmware), continuously capturing the wearer's body signals and activity into a persistent longitudinal personal record, and rendering that record back to the wearer as daily status, scores, goals, and trends that close the loop into behavior. The defining core is exactly the three jointly-held structures above; everything the market associates with the category — phone apps, 24/7 heart rate, sleep scores, recovery analytics, challenges, subscriptions, AI advisors, medical-adjacent sensors — is common mature structure or variant layered on that spine. Sibling seams (sport-record Types, progress tracker, AI coach, staff-facing analytics) are ratified from this side; the leaf stands as a legitimate, device-ecosystem-centered Type.
