# Research Notes — Ski Resort Recreation Application

## Research Goal

Understand the guest-facing application Type that serves a person's skiing/snowboarding day at a ski resort: what objects make up its world (the mountain, its operating state, the guest's day), what workflows it carries (plan → ride → record), where the boundary lies against hiking/trail apps, pure activity trackers, snow-report apps, and operator-side resort systems.

## Initial Boundary

Working hypothesis at start:

- The Type is the **guest-side companion** for recreation at a ski resort — not the operator-side resort management system (lift operations, snowmaking, ticketing back office are operator territory).
- Two market poles expected: (a) resort-official / pass-ecosystem apps (the resort's own app, or a multi-resort pass app), (b) third-party cross-resort ski trackers.
- Nearest neighbors: Hiking / Trail Application (same spatial-navigation pattern, summer context), Workout Tracking Application (pure activity record), snow-report/weather apps (conditions without the mountain), theme-park guest apps (same pattern, different industry).

## Research Questions

1. What objects make up the mountain model? (runs/trails, lifts, difficulty grading, on-mountain POIs, facilities)
2. What is the operating-state model? (lift/trail open-closed, grooming, snow report, weather, webcams, alerts)
3. What does the guest's day look like in the system? (tracking: runs, vertical, speed, distance; GPS trace; season totals)
4. How does the pass/ticket work inside the app? (mobile pass, hands-free scan, entitlement rules, blackouts)
5. What commerce/booking is in-app? (tickets, passes, lessons, rentals, dining, parking)
6. What social and safety capabilities exist? (friend location, groups, leaderboards, patrol access, warnings)
7. What interfaces does the guest actually face?
8. Where are the boundaries: vs hiking/trail apps, vs pure ski trackers, vs snow-report apps, vs resort info publications?

## Representative Products

| Product | Operator | Pole | Why sampled |
|---|---|---|---|
| My Epic (formerly EpicMix) | Vail Resorts | resort-ecosystem official app (35+ resorts listed for mobile pass) | largest pass ecosystem; pass-first + tracking + safety |
| Ikon Pass | Alterra Mountain Company | pass-ecosystem official app (70+ destinations stated) | second ecosystem; pass management + crew + commerce |
| Slopes | Breakpoint Studio (indie) | third-party cross-resort tracker with resort context | tracker-first philosophy; subscription; privacy posture |
| Ski Tracks | Core Coders lineage (now Fitness & Sports apps SRL) | pure tracker, no resort context | boundary probe: oldest tracker lineage (2010), offline-first |
| Matterhorn app | Zermatt Matterhorn (Bonfire AG) | regional single-resort official app | European info-first pole; tickets + Peak Track; regional features |

Boundary anchors (fetched during research, used for boundary reasoning only):

- OnTheSnow Ski & Snow Report (Mountain News LLC) — snow-report/planning-first app
- Ski Tracker & Snow Forecast (LW Brands) — pure tracker with NOAA snow forecast
- EXA Ski Tracker (ExaMobile) — pure tracker
- Ski Tracks Lite & GPS Maps — sibling of Ski Tracks that adds 3D resort maps (evidence that maps are a separable layer)

## Sources

Research date: 2026-09-09.

Reachable official layer (all vendor-authored):

- Apple App Store listing metadata via iTunes Search/Lookup API (vendor-authored descriptions, release notes, screenshots):
  - My Epic: https://apps.apple.com/us/app/my-epic-skiing-snowboarding/id395375487 (lookup id395375487)
  - Ikon Pass: https://apps.apple.com/us/app/ikon-pass/id1482191120 (lookup id1482191120)
  - Slopes: https://apps.apple.com/us/app/slopes-ski-snowboard/id643351983 (lookup id643351983)
  - Ski Tracks: https://apps.apple.com/us/app/ski-tracks/id365724094 (lookup id365724094)
  - Ski Tracks Lite & GPS Maps: id368024976
  - Matterhorn (Zermatt): https://apps.apple.com/ch/app/matterhorn/id1440571628 (CH storefront, German description)
  - OnTheSnow: id300412347; Ski Tracker & Snow Forecast: id1448220616; EXA Ski Tracker: id1196252184
- Slopes official website: https://getslopes.com/ (fetched successfully; support docs at help.getslopes.com / slopes.helpscoutdocs.com linked but not fetched)
- Matterhorn app official page (seller URL, not fetched): https://zermatt.swiss/matterhorn-app

Source-access limitations:

- epicmix.com (root and /en/epicmix-app) returned a bot-block error page twice → abandoned per network rule; My Epic evidence relies on its App Store listing (vendor-authored).
- ikonpass.com is a JavaScript SPA; two fetches returned no content → abandoned; Ikon evidence relies on its App Store listing.
- slopesapp.com and slopesapp.com/help timed out twice → abandoned; getslopes.com fetched successfully instead.
- skitracks.app returned an empty response → abandoned; Ski Tracks evidence relies on its App Store listing.
- No vendor help-center article was fetched for any product. Therefore: no precise operational defaults (scan distances, refresh intervals, offline map counts, price points) are asserted anywhere; vendor-stated figures (e.g., "2,000+ resorts", "70+ destinations") are quoted as vendor claims, not verified counts.

## Product Observations

### My Epic (Vail Resorts) — Evidence layer A (official App Store listing)

App Store listing (bundle com.vail.EpicMix, lineage back to EpicMix released 2011-01-24; current name "My Epic: Skiing & Snowboarding"):

- **Mobile Pass & Lift Tickets** — "Scan hands-free at the lift, straight from your pocket and skip the ticket window." Mobile pass available at a listed set of 35+ Vail resorts.
- **Interactive Trail Maps and Lift Wait Times** — "maps, GPS location tracking plus real-time and predictive lift line wait times."
- **Personalized Stats** — "Track your turns with detailed stats that include your vertical feet, lifts taken, resorts visited, highest elevation and distance (enabling GPS tracking required). You can also share and compare your stats with friends and family."
- **Account and Pass Information** — "View resort access and any Restricted Peak Dates associated with your pass."
- **Mountain and Resort Alerts** — "operational updates including grooming reports, terrain and lift statuses, snow reports, and more."
- **Ski Patrol Assistance** — "direct access to ski patrol during an emergency with your GPS location."
- **Weather Updates and Snow Cams** — "weather updates and live snow cameras."
- **Epic Mountain Rewards** — pass-holder benefits/savings through the phone.
- **Resort Charge** — "Make payments on the mountain with ease, by paying directly through the app."
- Release notes (2026-08): purchase season passes directly in the app with Apple Pay / Google Pay.
- Screenshot titles: Mobile Pass & Lift Tickets; Explore & Shop Passes; Ski & Ride School; Personalized Stats; Resort Information; Find My Friends; My Epic Assistant (an AI assistant surface).
- Genres: Sports, Social Networking.

Observations: the pass is the spine (entitlement + access + payment + rewards); the mountain state (grooming, terrain/lift status, snow reports) is operator-published; tracking is GPS-based and personal; safety is a first-class surface; commerce is deep (passes, tickets, on-mountain payments, lessons).

### Ikon Pass (Alterra Mountain Company) — Evidence layer A

App Store listing (bundle com.alterramtnco.ikonpass.prod):

- Positioning: "your tool to maximize fun at over 70 Ikon Pass destinations worldwide. Whether you're an Ikon Pass holder or using a local pass or day ticket, the Ikon Pass app helps you make the most of your mountain experience – all in one place."
- **Manage your Pass**: days remaining, blackout dates, favorite destinations, deals/vouchers, mountain credits, family pass profile, pass photos.
- **Amplify Your Adventure**: track stats (vertical, run difficulty, current altitude), Apple Watch activity, weather and condition reports, find dining/retail/rentals with interactive maps, pay for food and drinks in-app, map you and your crew on the mountain, real-time parking availability, live events at destinations.
- **Connect With Your Crew**: daily friend groups to message, compare stats, track each other's locations; community leaderboard.
- Navigation at "60+ destinations"; in season 25/26 the app replaces the local apps at 17 named destinations (Arapahoe Basin, Mammoth, Steamboat, Winter Park, Tremblant, …).
- Genres: Sports, Travel.

Observations: pass management is the spine (days remaining, blackouts, credits, family); the mountain day is social (crew, daily groups, leaderboard); commerce extends to on-mountain food payment and parking; the ecosystem consolidates single-resort apps into one pass app — evidence that "resort app" and "pass app" are one Type at different scopes.

### Slopes (Breakpoint Studio) — Evidence layer A (official site + App Store listing)

Official site (getslopes.com) and App Store listing:

- **Trail maps**: "official trail maps for thousands of resorts world-wide"; "at 2,000+ supported resorts, go beyond the resort's official trail map and see where you are (and where you've been) with Slopes's interactive digital trail maps" (interactive maps are Premium; 2D and 3D).
- **Smart Recording**: select activity (ski, snowboard, monoski, sitski, telemark…); "Slopes will automatically detect uphill, lifts, and runs for you all day long"; auto-detects which resort you are at (with cell reception).
- **Detailed statistics**: top speed, lift vs run time, vertical, distance, average speed, calories, elevation, heart rate, season totals, lifetime totals; Premium adds per-run real-time stats, best-run/top-speed locations, full-day timeline.
- **Timeline editor**: day recording is a timeline of lift/run blocks the user can adjust (drag start/end, snap to lifts, movement heat-bar to exclude lift-line time).
- **Find your friends**: live location on the recording screen; "Location sharing is privacy-focused; you can always turn it on and off"; trips share location with all trip participants; private leaderboards over 8 stats.
- **Resort info and conditions**: community condition reports ("check what other skiers are saying the conditions are really like"), weather forecast, trail statistics, ski patrol contact info; Premium adds "Live Lift & Trail Status for 50+ resorts in North America".
- **Trip planning**: create trips, invite friends, keep tabs on resort conditions and who's coming.
- **Fitness**: Apple Watch, heart-rate zones, Apple Health rings; auto-post to Strava; import from Garmin/Suunto.
- **Privacy posture**: never sells data; accounts optional; Sign-in with Apple; free tier ad-free and "truly free" (find friends, unlimited tracking, key stats, snow conditions, season & lifetime overviews).
- **Offline**: "At your local resort, on an epic trip in another country, or deep in the backcountry in pursuit of fresh powder — no cell reception required."
- GPS required; will not work indoors; battery guidance in listing.

Observations: the tracker pole carries the same mountain model (maps, status, conditions) but acquires it independently of any resort; the day record (timeline of lifts and runs) is the product's center of gravity; resort context is a data layer Slopes licenses/curates, not an entitlement.

### Ski Tracks (Core Coders lineage) — Evidence layer A (boundary probe)

App Store listing (bundle com.corecoders.SkiTracks, released 2010-04-05):

- "the essential GPS companion for skiing, snowboarding, and winter mountain adventures."
- Accurate GPS tracking: speed, distance, altitude, vertical per run, automatically.
- Maps & saved routes: "View your recorded paths directly on the map" — the user's own trace, not the resort's trail map.
- Performance insights across days and season; music while skiing; photos linked to activity history; Apple Watch live data.
- How it works: start tracking → ski freely → view routes on map → review stats.
- Subscription premium; genre Navigation.
- The listing names no resort trail maps, no lift/trail status, no pass, no conditions.

Observation: a pure ski-day recorder with no resort context. Its sibling "Ski Tracks Lite & GPS Maps" adds "Interactive 3D Resort Maps … with lifts, pistes, elevation profiles, and difficulty levels" and route planning from trail/lift data — demonstrating that the resort map layer is separable and can be added to a tracker. Ski Tracks is the boundary pole: leg-3-only (personal day record without mountain space/state).

### Matterhorn app (Zermatt – Matterhorn, official app by Bonfire AG) — Evidence layer A

App Store listing, CH storefront, German (bundle com.bonfire.zermatt; seller URL zermatt.swiss/matterhorn-app):

- STARTSEITE (home): webcams, weather forecast, live panorama map, e-bus live timetable, online table reservation, events.
- LIVE: "welche Lifte und Pisten offen sind" (which lifts and pistes are open), weather for the stay, next cable-car departure, webcam images, current warnings/alerts from the Zermatt Bergbahnen (lift company).
- ENTDECKEN (discover): activities, restaurants, bars, SPA; map with filters.
- TICKETS: ticket shop for cable-car and arrival tickets, avoiding counter queues.
- PEAK TRACK: "Hinterlege deinen Skipass und verfolge deine persönlichen Skistatistiken. Erstelle Gruppen, miss dich mit Freunden oder nimm an der öffentlichen Rangliste teil" — link your ski pass, personal ski statistics, groups, compete with friends, public leaderboard (vertical meters).
- PROFIL: profile with interests, personalized content, push subscriptions to lift/piste warnings and road messages for the Visp–Zermatt access road; overview of purchased tickets, table reservations, favorites.
- Genre: Travel; TWINT payment fix in release notes.

Observations: the regional European pole is info-first (live mountain state + village/tourism layer blended: restaurants, SPA, events, bus timetable, road conditions); tracking exists but is pass-linked and leaderboard-shaped rather than recorder-shaped; the app spans the resort's winter recreation AND the destination's wider tourism life.

### Boundary anchors — Evidence layer A

- **OnTheSnow Ski & Snow Report** (Mountain News): "worldwide leader for snow reports and ski conditions"; 2,000+ ski areas' snow reports, webcams, firsthand reports/photos, weather, powder alerts, "My Resorts" favorites, view by pass (Ikon/Epic/Indy/Mountain Collective), "Mountain overview with stats, snow history graph, and trail maps." Genre: Weather. Center of gravity is planning/conditions, not the on-mountain day — yet it carries maps and favorites, showing the boundary against this Type is drawn by center of gravity (before-the-day planning vs the day itself), not by any single feature.
- **Ski Tracker & Snow Forecast** (LW Brands): runs on map color-coded by speed, "Ski lifts are NOT tracked", stats, 7-day NOAA snow forecast (USA), iCloud backup, no account needed, auto motion detection, battery optimization. Genre: Navigation. Pure tracker + forecast.
- **EXA Ski Tracker** (ExaMobile): max speed, tracks on map, distance split downhill vs lifts, time split skiing/lifts/rest, altitude, photos with data overlay, "To use this app do not need a mobile roaming data, just GPS is enough." Pure tracker.

## Cross-product Comparison

| Capability | My Epic | Ikon Pass | Slopes | Ski Tracks | Matterhorn |
|---|---|---|---|---|---|
| Resort trail/panorama map (official) | ✓ interactive + GPS | ✓ interactive (dining/retail/rentals; navigate 60+) | ✓ official maps (thousands); interactive 2D/3D at 2,000+ (Premium) | ✗ (own trace only) | ✓ live panorama map |
| Locate-me on the mountain | ✓ | ✓ (you + crew) | ✓ | ✗ | ✓ (live map) |
| Lift/trail operating status | ✓ terrain & lift statuses, grooming | ✓ (condition reports; status depth not explicit) | partial (live lift & trail status, 50+ NA resorts, Premium) | ✗ | ✓ lifts & pistes open + warnings |
| Snow/conditions report | ✓ snow reports | ✓ weather & condition reports | ✓ community reports + conditions | ✗ | ✓ weather + webcams |
| Webcams | ✓ live snow cams | not explicit | not explicit | ✗ | ✓ |
| Day tracking (runs/vertical/speed/distance) | ✓ vertical, lifts taken, resorts visited, highest elevation, distance | ✓ vertical, run difficulty, altitude | ✓ deepest (lift vs run, per-run, timeline) | ✓ speed/distance/altitude/vertical | ✓ Peak Track stats, vertical meters |
| Auto lift/run detection | not explicit | not explicit | ✓ | ✓ (auto track) | not explicit |
| Pass/ticket in app | ✓ mobile pass hands-free scan, restricted peak dates, buy in-app | ✓ days remaining, blackouts, credits, family | ✗ | ✗ | ✓ ticket shop + link skipass |
| Friends on mountain | ✓ Find My Friends | ✓ daily groups, message, locate | ✓ live location, trips | ✗ | ✓ groups, compete |
| Leaderboards/gamification | not explicit in listing | ✓ community leaderboard | ✓ private leaderboards (8 stats) | ✗ | ✓ public leaderboard |
| Safety | ✓ patrol assistance with GPS | not explicit | ✓ patrol locations on maps | ✗ | ✓ warnings/alerts |
| On-mountain commerce | ✓ resort charge, rewards, pass purchase | ✓ pay for food in-app, vouchers | ✗ (subscription only) | subscription | ✓ ticket shop, TWINT |
| Booking | ✓ (Ski & Ride School surface) | ✓ dining/retail/rentals finder, events | ✗ | ✗ | ✓ table reservation, tickets |
| Parking/transit | not explicit | ✓ real-time parking | ✗ | ✗ | ✓ e-bus live timetable, road messages |
| Offline capability | not explicit | not explicit | ✓ no reception required | ✓ GPS-only heritage | not explicit |
| Account posture | required (pass) | required (pass) | optional | none named | profile-based |
| Resort scope | 35+ (portfolio) | 70+ destinations | 2,000+ interactive / thousands official | resort-agnostic | 1 resort |

Reading of the comparison:

- **Universal across all five**: the guest's ski day as the organizing frame (every product records and/or serves "your day").
- **Universal across the four resort-context products** (all but Ski Tracks): the mountain as structured space (map with lifts/runs) and the mountain's live operating state (status/conditions).
- **Near-universal**: tracking with stats (4/5 in-type products; absent only where the product is info-first — and even there present in leaderboard form); friends-on-mountain (4/5).
- **Pole-dependent**: pass/ticket integration (resort/pass apps only), commerce/booking depth (resort/pass apps), auto run/lift detection and timeline editing (tracker pole deepest), offline posture (tracker pole explicit).
- **Regional**: European pole blends the resort with the destination's wider tourism life (bus timetable, road messages, table reservation, SPA/events); North American pole centers pass ecosystems, wait times, parking.

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being recognizable as this Type:

1. **The mountain as structured guest-facing space.** The resort's terrain held as a navigable model: named runs/trails with difficulty grading, lifts connecting them, on-mountain points of reference (lodges, restaurants, facilities, patrol). This is the spatial substrate of the day. (Present in My Epic, Ikon, Slopes, Matterhorn; absent from pure trackers.)
2. **The mountain's live operating state.** The current-day truth about that space, refreshed through the day: which lifts and runs are open, grooming, snow and weather conditions, webcams, operational alerts. The app reflects the resort's operational decisions; it does not make them. (Present in the same four; the third-party tracker acquires it as a data layer.)
3. **The guest's mountain day as the personal frame.** The application is organized around the individual guest's own day on the mountain — realized through personal surfaces: where they are on the mountain, what they did (tracked runs/vertical/speed), what entitles them to be there (pass/ticket), and who they are with. Every sampled product carries at least one realization; mature products carry several. (Present in all five, including the pure tracker.)

Joint load-bearing analysis:

- 1 alone = static trail map / outdoor navigation map
- 2 alone = snow report / weather feed (OnTheSnow anchor)
- 3 without 1+2 = pure ski activity tracker (Ski Tracks / EXA / LW Brands anchors) — Workout Tracking territory
- 1+2 without 3 = the resort's published information surface (a brochure/app-shaped publication, not a guest application)
- 1+3 without 2 = navigation over stale ground truth
- 2+3 without 1 = status feed with no spatial model

### L1 — Common Mature Structure

- GPS locate-me on the trail map
- Day/activity tracking with automatic run/lift segmentation (runs, vertical, distance, top speed, time on lifts vs runs)
- Season/lifetime totals and progression comparison
- Friend/crew location sharing and meet-up on the mountain
- Stats comparison and leaderboards (private or public)
- Webcams
- Weather + snow report detail
- Pass/ticket surfaced in the app (entitlement view, blackout/restricted dates) — resort/pass poles
- On-mountain commerce (pay for food, resort charge, rewards) — resort/pass poles
- Booking surfaces (tickets, lessons/rentals/dining) — resort/pass poles
- Safety: patrol/emergency access carrying GPS location; operational warnings
- On-mountain facility finder (dining, restrooms, rentals, patrol locations)
- Parking availability / resort transit info
- Offline capability (maps and recording without reception)

### L2 — Variant / Optional Structure

- Operator scope: single-resort official app ↔ pass-ecosystem app (replacing local apps) ↔ third-party cross-resort app
- Pass integration depth: hands-free pocket scan ↔ QR/display ↔ pass-linked stats only ↔ none
- Tracking depth: auto lift/run detection + editable timeline ↔ simple totals ↔ leaderboard-only
- Map depth: static official map ↔ interactive 2D/3D with facilities and friend positions
- Commerce depth: none ↔ tickets ↔ full on-mountain payments and rewards
- Regional shape: European destination-blended (public transport, road conditions, table reservation, piste grading, avalanche/warning culture) ↔ North American pass-ecosystem (wait times, parking, restricted peak dates) ↔ Asia/Pacific coverage as data expansion
- Seasonality: winter-only ↔ dual-season (summer hiking/biking modes in several resort apps)
- Business model: free operator app ↔ free-with-premium-subscription tracker ↔ subscription tracker
- Account posture: required (pass identity) ↔ optional ↔ none
- Gamification posture: none ↔ private leaderboards ↔ public/community leaderboards and pins

### L3 — Vendor-specific (Research Notes only)

- My Epic: hands-free pocket scan at lifts; real-time and predictive lift wait times; My Epic Assistant (AI surface); Epic Mountain Rewards; Resort Charge; Restricted Peak Dates; 35+-resort mobile-pass list.
- Ikon Pass: mountain credits; family pass profile; days remaining/blackouts; stated replacement of 17 local resort apps in 25/26; real-time parking.
- Slopes: timeline editor with movement heat-bar and lift snapping; 3D & AR replays; Strava auto-upload; Garmin/Suunto import; trips with automatic location sharing among participants; "truly free" ad-free tier; custom resort maps.
- Ski Tracks: music playback while recording; photos linked to activity history; GPS-only heritage.
- Matterhorn: Peak Track (pass-linked stats + public leaderboard); e-bus live timetable; online table reservation; Visp–Zermatt road push messages; TWINT payment.

## Rejected Findings

- **"Tracking defines the Type."** Rejected: all five sampled products track, but the info-first regional pole and many small-resort apps operate without recording; tracking is the strongest common-mature capability, not the invariant. The pure tracker (Ski Tracks) shows tracking alone is not the Type either.
- **"Pass/mobile ticket defines the Type."** Rejected: pass integration is absent from the entire third-party pole; it is the resort/pass-ecosystem realization of the guest-entitlement surface.
- **"Multi-resort scope defines the Type."** Rejected: single-resort (Matterhorn), portfolio (My Epic/Ikon), and cross-resort (Slopes) are all the same Type at different scopes.
- **"Webcams define the Type."** Rejected: common but not universal in-sample; a conditions surface without the mountain space is a snow-report app.
- **"Ski resort app = resort info app."** Rejected: every in-sample product carries a personal layer; the personal frame is what makes it a guest application rather than the resort's publication.

## Boundary Findings

- **vs Hiking / Trail Application**: same spatial-navigation grammar (map, named routes, locate-me, recorded track), but the ski Type's space is lift-connected terrain with difficulty-graded runs and its state is lift/trail/snow operations. Remove lifts, snow state, and the ski-day record → hiking/trail app. Several resort apps add summer modes (drift toward the hiking pattern in the off-season) without changing the Type.
- **vs Workout Tracking Application**: a pure ski tracker (Ski Tracks, EXA, LW Brands poles) holds leg 3 only — a personal activity record with no mountain space or operating state. That is workout-tracking territory specialized to snow sports. The boundary is the resort context, not the sport.
- **vs Snow-report / weather apps (OnTheSnow anchor)**: conditions without the on-mountain day frame = planning-first snow report. The seam is center of gravity: before-the-day planning vs the day itself (navigate, ride, safety, record). The seam is soft — OnTheSnow carries trail maps and favorites — and is drawn by what the product is *for*, not by feature presence.
- **vs the resort's public information surface**: space + state without any personal layer is the resort's publication (website/brochure in app form). The market's guest applications all carry a personal frame; the frame is the application boundary.
- **vs Theme Park / Attraction guest apps**: same guest-companion grammar (park map + live status/wait times + ticket in app) in a different industry; the ski Type's specificity is the mountain model (lifts/runs/snow) and the ski-day record.
- **vs operator-side resort systems** (lift operations, snowmaking, ticketing back office, ski-school management): guest-facing experience vs operator-facing operations. The app consumes the operator's state; it does not run the operation.
- **vs Outdoor Recreation Discovery**: discovery of destinations vs being the companion at the destination. Slopes' trip planning and OnTheSnow's resort discovery sit on this seam.

## Uncertainties

- Ikon's live lift/trail status depth is not explicit in the reachable listing (condition reports are); status depth per product could not be verified.
- Whether My Epic retains EpicMix-era gamification (pins/challenges) could not be verified from the reachable layer; the current listing emphasizes stats sharing instead.
- Offline behavior of the resort-official apps (My Epic, Ikon, Matterhorn) is not documented in the reachable layer; only the tracker pole documents offline explicitly.
- The exact data-supply relationship between third-party trackers and resorts (licensed feeds vs resort partnerships vs community reporting) is not documented in the reachable layer; Slopes' community condition reports are vendor-stated, the mechanism is not.
- Historical continuity: EpicMix's 2011 RFID-check-in gamification lineage is inferred from the bundle ID and release date (2011-01-24) plus the current product's positioning; the intermediate product history was not verifiable from the reachable layer.

## Final Synthesis

The Ski Resort Recreation Application is the guest's companion for a day (or stay) of skiing/snowboarding at a mountain resort. Its world has three jointly-held structures: the mountain as a structured, guest-facing space (trail map of named, difficulty-graded runs connected by lifts, with on-mountain points); the mountain's live operating state (lift/trail status, grooming, snow and weather conditions, alerts — the resort's operational truth, consumed not made); and the guest's own day as the personal frame (position on the mountain, tracked activity, entitlement, companions). The market realizes the Type in three scopes — single-resort official apps, multi-resort pass-ecosystem apps, and third-party cross-resort apps — with the pass/entitlement layer and commerce depth concentrated in the resort/pass poles and recording depth concentrated in the tracker pole. Pure trackers without mountain context and snow-report apps without the on-mountain day are the two boundary poles; both share capabilities with this Type but neither holds all three structures.
