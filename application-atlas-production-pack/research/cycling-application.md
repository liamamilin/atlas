# Research Notes — Cycling Application

Research date: 2026-09-07
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1 (internal; not referenced in the final document)

## Research Goal

Understand the "Cycling Application" Application Type from real products: what the world of such an application consists of (objects, users, surfaces), how work flows through it (record → analyze → share; plan → navigate → ride), which structures are definitional vs. common vs. variant vs. vendor-specific, and where its boundaries lie against neighboring sport/fitness Types in Directory §28.

## Initial Boundary (pre-research hypothesis)

- An end-user application for people who ride bicycles: record rides, analyze performance, plan/navigate routes, manage the bike as equipment, optionally train and socialize around riding.
- Nearest directory neighbors: Running Application (sibling), Workout Tracking Application, Fitness Progress Tracker, Endurance Training Platform, Wearable Fitness Platform, Hiking / Trail Application, Outdoor Recreation Discovery, Race Management Platform (organizer-side), Social Network (drift risk from the social-first pole).
- Initial risk: overfitting the definition to the social-activity-tracker pole (Strava) or to the route-planner pole (Komoot). The indoor-virtual pole (Zwift) must also fit the definition.

## Research Questions

1. What is the unit of record? (ride/activity?) What identifies and structures it?
2. What cycling-specific data does the system capture, and which metrics are baseline?
3. How does a ride enter the system — live recording, device sync, manual entry, file import?
4. How does route planning work, and what is bike-type-aware about it (surface, routing profiles, e-bike)?
5. How does navigation during the ride work?
6. What does post-ride analysis look like? Where does it become training science (FTP, load)?
7. How is the bike itself modeled (gear, components, mileage)?
8. What are the social structures (feed, segments, clubs, challenges)? Are they definitional?
9. How does indoor riding fit (trainers, virtual worlds, structured workouts)?
10. What device ecosystem relationships exist (bike computers, watches, e-bikes)?
11. Where does this Type end and Running / Workout Tracking / Endurance Training / Wearable Fitness begin?

## Representative Products

| Product | Pole | Customer level | Why selected |
|---|---|---|---|
| Strava | social-first ride/activity tracker with training analytics | consumer, freemium + subscription | largest consumer athletic network; cycling is a core sport; rich official help center |
| Komoot | route planning / navigation-first for outdoor riding | consumer, region-unlock + premium | navigation philosophy, bike-type-aware routing, community map contributions |
| Zwift | indoor virtual riding / training | consumer subscription, hardware-adjacent | exercises the "does the definition survive without real-world routes" test |

Attempted and excluded: Ride with GPS (ridewithgps.com/help — fetch failed twice, abandoned per network rule); Garmin Connect (garmin.com software page — 404). Zwift's own support site is JavaScript-rendered and returned no article content; only its Tier-2 product page was usable, so Zwift claims are kept at product-page strength.

## Sources

- Strava Help Center (Intercom-hosted): https://support.strava.com/hc/en-us (Getting Started index)
  - Supported Sport Types on Strava — https://support.strava.com/en-us/articles/15402005-supported-sport-types-on-strava
  - Adding Gear to Your Activities on Strava — https://support.strava.com/en-us/articles/15402143-adding-gear-to-your-activities-on-strava
  - Strava Training Glossary for Cycling — https://support.strava.com/en-us/articles/15402109-strava-training-glossary-for-cycling
  - Help-center collections observed: Recording and Uploading Activities; Maps and Navigation; Stats and Metrics Explained; Your Feed and Community; Glossaries and References. Related-article titles confirming surface existence: "Strava Live Segments on Bryton Devices", "Best Efforts - Cycling", "Power Curve - Cycling", "How to Get Power for Your Rides", "Uploading Route Files", "Uploading Manual Activities", "Recording an Activity", "Edit Past Activities", "Audio Announcements", "How to Get Your Activities to Strava".
- Komoot Help Center (Zendesk-hosted): https://support.komoot.com/hc/en-us
  - Category "Using komoot" — sections: Get Started; komoot Map; Planning and Routes; Navigation and Recording; Community and Contributions
  - Supported sport types — https://support.komoot.com/hc/en-us/articles/10194685010970-Supported-sport-types
  - Plan routes on the website — https://support.komoot.com/hc/en-us/articles/10194270667034-Plan-routes-on-the-website
  - Category "Connected Devices and Integrations" ("smartwatches, GPS devices, and e-bikes")
- Zwift: https://www.zwift.com/how-it-works (equipment, devices, membership, racing/events, Companion app); https://support.zwift.com (root only, no article content extractable)

## Product Observations

### Strava (evidence layer: A — direct help-center articles)

- **Sport types**: many sport types; article states explicitly that "some of Strava's features are currently only available for our three core sport types, riding, running, and swimming." Cycle sports form their own family: Ride, E-Bike Ride, Mountain Bike Ride, E-Mountain Bike Ride, Gravel Ride, Velomobile, Handcycle — plus Virtual Rides. Sport type can be changed after upload.
- **Ride entry (multi-channel)**: mobile app recording ("Recording an Activity"); third-party device/app sync ("How to get Your Activities to Strava… instant app uploads to GPS device syncing and manual file uploads"); "Uploading Manual Activities"; "Uploading Route Files"; "Edit Past Activities". So: record / device-sync / file-import / manual-entry are all documented entry paths. (A)
- **Gear**: bikes and shoes as gear records (nickname, type, weight for bikes; brand/model for shoes). Bike weight+type used to calculate power. Bike **components** (website-only): add component type/brand/model/weight/date/notes; retire/delete with special rules (retired components cannot be un-retired; one component per type; frame retirement forces bike recreation). Default gear per sport type (bikes assignable to Ride/MTB/Gravel/E-Bike/EMTB/Handcycle/Virtual/Velomobile). Gear retire vs delete (retire keeps history but removes from selection). Gear accumulates mileage only via activities assigned to it; manual back-dating handled by creating a manual activity. Privacy: activity start time and bike used visible only to followers; shoe visibility differs. (A)
- **Training analytics (cycling-specific)**: FTP (functional threshold power) as the anchor; 20-min test minus 5% as recommended test (vendor method — L3 detail); Weighted Average Power; Total Work in kJ; Intensity vs FTP with named bands (Endurance/Recovery ≤65%, Moderate 65–80%, Tempo 80–95%, TT/Race 95–105%, Short TT/Race ≥105% — vendor scheme, L3); Segment Intensity (compares effort to best power for that segment duration over last 6 weeks — confirms segments as analysis objects); Training Load with recovery-time bands (L3 numeric detail); Power Curve (best average power 1s→ride length, W and W/kg, comparable across 6 weeks/year/all-time); Power Zones (7 zones as % of FTP with named riding states — vendor scheme); Fitness / Fatigue / Form scores via impulse-response model. (A)
- **Maps**: map layers, fullscreen maps, maps glossary, personal heatmaps, weekly/night heatmap (subscription-gated per related titles). (A, structure-level)
- **Segments**: not a standalone article fetched, but confirmed via "Segment Intensity" glossary entry and related-article titles "Strava Live Segments on Bryton Devices" (segments pushed to third-party bike computers). Segment/leaderboard existence: A- (title + glossary level; leaderboard mechanics not documented in fetched pages — no precise claims made).
- **Social**: "Following Athletes on Strava", "Feed Ordering", verified badges, content reporting, community standards. Feed + follow graph + community moderation documented at structure level. (A, structure-level)
- **Misc**: audio announcements during recording; units setting; profile customization; Year in Sport recap; Strava Shop; Runna acquisition (market signal). (A, structure-level)

### Komoot (evidence layer: A — direct help-center articles)

- **Route planning as the primary act**: web planner is "the easiest way to create and review routes in detail"; planner sidebar defines **sport type** ("affects the paths komoot chooses for planning, such as favoring more paved roads for Road Cycling") and **route type preferences** (prioritize, never guarantee). **E-bike toggle** "optimizes route duration and difficulty estimates for e-bikes". (A)
- **Planning mechanics**: start + destination as first two waypoints; click map to add waypoints; search places; reorder/reverse; one-way vs round trip; drag route line; crop/remove waypoints; undo/redo; hide route line. Refused segments explained (sport-inappropriate path, wrong direction, private property). (A)
- **Route review**: route overview with community photos along the route, Route Alerts, "additional route conditions such as elevation, way types, surfaces, weather and additional details"; weather-on-route is Premium; elevation profile with distance/estimated duration/difficulty/**adjustable speed**, switchable views (elevation, surfaces, way types, weather); interacting with profile highlights map section. (A)
- **Map content**: Highlights (community-recommended places/route sections), Places of Interest (accommodation, natural sights, **e-bike charging points**, parking, public transport…), Trail View photos, saved places, distance markers; users can improve the map and create/contribute Highlights. (A)
- **Sport types**: planning sports: Cycling (Road cycling, Gravel riding, Mountain biking; Enduro app-only) and On foot (Hiking, Running; Mountaineering app-only) — i.e., routing is sport-specific, cycling split by bike style. Completed-activity labels broader (adds Downhill MTB, Unicycling, etc.). Sport label editable after recording. (A)
- **Recording & navigation**: Record an activity; rename recorded activity; take photos while recording; Navigate a saved route; Navigation FAQ; Android settings for reliable navigation and **offline use**; planned route can be saved as a completed activity; dynamic route updates. (A, structure-level for most)
- **Data exchange**: "Export and import Routes and Activities" (title-level). Multi-day route planning (title-level). (A-)
- **Regions**: "Unlock your free region" — map/region gating model; Premium unlocks features. (A, title-level for limits — no numbers claimed)
- **Devices/integrations**: category "Connected Devices and Integrations" — smartwatches, GPS devices, **e-bikes**. (A, category-level)
- **Community**: Highlights contributions, Collections, Pioneer Programme badges, Peak Bagging, community guidelines — community shaped around map/route contribution more than feed competition. (A, structure-level)

### Zwift (evidence layer: A− — product page only; support site not extractable)

- **Indoor pole**: ride in a virtual environment; equipment is a smart trainer + outdoor bike, or a smart bike / dedicated indoor setup (Zwift Ride); "Zwift works with any Bluetooth or ANT+ smart trainer". (A−, product page)
- **Platforms**: PC, Mac, Android, iOS, Apple TV; plus a "Companion" phone app (control/metadata companion). (A−)
- **Membership**: subscription model; trial. (A−)
- **Organized activity**: Racing ("Home of Community Racing"), Events, group rides with friends ("ride with friends anytime… even if we're not in the same place" — testimonial, weak evidence, used only for direction not fact). (A−)
- **No real-world route planning / no outdoor navigation**: product page describes no maps of the real world; riding happens on trainer-controlled virtual courses. GPS real-world track capture is absent from the product page. (A− absence observation — used for boundary reasoning only)

## Cross-product Comparison

| Dimension | Strava | Komoot | Zwift |
|---|---|---|---|
| Unit of record | Ride/activity (GPS-based, sport-typed) | Tour/activity (recorded) + planned Route as first-class object | Indoor ride session in virtual world |
| Ride entry | app recording / device sync / file upload / manual | app recording / GPS-device sync / planned-route-as-activity | trainer sensors (power/speed/cadence) via trainer |
| Cycling metrics baseline | distance, time, speed, elevation; + power suite | distance, time, speed, elevation estimates (planning) | power-centric (trainer data) |
| Route planning | route files import; maps; (planner exists but not documented here) | core act; sport-specific routing; waypoints; round trip; elevation/surface review | none (virtual courses) |
| Navigation | audio announcements; live segments on devices | turn-by-turn on saved route; offline; dynamic updates | n/a |
| Bike/gear modeling | bikes/shoes/components + mileage + default-per-sport | e-bike routing toggle; e-bike charging POIs; device pairing | trainer/smart-bike as the "bike" |
| Analysis depth | very deep (FTP/load/curves/zones) | route-condition analysis (elevation/surfaces/weather) | in-app ride stats (not documented — support site unreachable) |
| Social | feed, follow graph, segments, clubs (structure-level) | contribution community (Highlights/collections), lighter social | events/racing community |
| Indoor | virtual ride sport type exists | no | the whole product |
| Business model | freemium + subscription | free region + premium + regions | subscription (+ hardware) |
| Platform | mobile + web + devices | mobile + web + devices | PC/Mac/mobile/TV + companion |

Stable across all three (B layer): ride/session as the unit of record tied to the individual cyclist; cycling-specific metric set (distance/duration/speed/elevation, with bike-type distinctions); multiple entry paths for a ride; map as a working surface (real or virtual); community or competitive layer around riding; subscription or tiered commerce.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

1. **Ride as the unit of record** — a persisted, dated cycling session belonging to the individual cyclist, with a named sport identity inside cycling (road / mountain / gravel / e-bike / virtual / …).
2. **Cycling-specific performance semantics** — the record carries cycling metrics (distance, duration, speed, elevation as the baseline set) computed for the bicycle context; the bike context (including bike-type/e-bike distinctions) is what the data means something against.
3. **Origin in the rider's own riding** — the record represents riding the user actually did (or plans to do): captured live, imported from devices/files, entered manually, or generated indoors from trainer data. The mechanism is not definitional; the first-person provenance is.

If the ride-as-record or the cycling semantics disappear, the product becomes a generic workout tracker, a map utility, or a social network — no longer a Cycling Application. Historical check: manual-entry cycling logs and regional products without GPS fit (1)–(3); device-first and app-first products fit; Zwift fits via indoor trainer provenance. GPS tracks, social feeds, route planning, power science are NOT required.

### L1 — Common Mature Structure (evidence layer B)

- GPS track + map visualization of rides
- Multiple ride-entry channels (live recording, device sync, file import, manual entry) and post-hoc editing of rides
- Route planning with bike-type-aware routing (surface/way-type preferences, elevation profile, estimated duration/difficulty; e-bike variants)
- Turn-by-turn navigation of saved routes, offline maps
- Device/sensor connectivity: bike computers, smartwatches, power meters, smart trainers, e-bikes
- Post-ride analysis surfaces (metrics detail, elevation profile, trends)
- Gear/bike management with accumulated mileage (and component-level detail in mature poles)
- Goals/progress tracking; training concepts (threshold-based intensity, load) in mature poles
- Social layer: feed/follow, clubs/groups, challenges or competition on route segments
- Subscription/tiered commerce over a free base

### L2 — Variant / Optional Structure

- Indoor virtual riding as the product's center (virtual worlds, racing, events)
- Training-science depth: FTP, power curves, zones, fitness/fatigue/form modeling
- Segment/leaderboard competition on real-world stretches
- Region-locked map commerce (buy/unlock regions)
- Community map contribution (crowdsourced highlights, POIs, conditions reporting)
- Event/club organization features; route sharing for group rides
- Privacy models over ride visibility (start time, location, gear)
- Recap/annual-review surfaces; hardware sales as part of the model

### L3 — Vendor-specific (research notes only)

- Strava: segment/leaderboard system as named feature ("Segment", "Live Segments" on partner computers like Bryton); named metrics Weighted Average Power / Intensity bands / Training Load recovery bands / 7 Power Zones; 20-min FTP test minus 5% method; Personal/Weekly/Night Heatmaps; Year in Sport; My Gear component rules (website-only components; one component per type; un-retirable retired components; frame-retirement forces bike recreation); Runna acquisition; Strava MCP Connector.
- Komoot: Highlights, Trail View, Regions + "Unlock your free region", Pioneer Programme, Peak Bagging, Collections, dynamic route updates, e-bike charging POIs, weather-on-route as Premium.
- Zwift: Zwift Ride / Zwift Cog / KICKR CORE Zwift One compatibility vocabulary, Companion app, Level system (testimonial shows "Level 38/50/100"), shipping regions for hardware, forums/status site.

## Vendor-specific Findings

See L3 above — none of these promoted to the canonical model. Notably, segment competition is the single most identity-defining feature for one vendor's user base but is absent in two of three sampled products, so it stays variant/vendor-specific.

## Rejected Findings

- "GPS track is definitional" — rejected: manual-entry rides are documented on the sampled tracker (manual activities), and indoor products generate rides without GPS. Higher abstraction: origin in the rider's own riding, mechanism variant.
- "Social feed/leaderboard is definitional" — rejected: navigation-first and indoor products fit the Type without them.
- "Route planning is definitional" — rejected: the social tracker's documented planning surface is thin relative to its recording surface; indoor product has none.
- "Cycling app = multi-sport athletic app" — rejected: the Type is sport-specific; multi-sport capability (running/swimming etc.) is common but the cycling data model is what the sampled products organize around (three "core sport types" with ride among them on the tracker; cycling-split routing on the planner; cycling-only on the indoor product).
- "Bike gear/component management is definitional" — rejected: documented in one product at depth, present as e-bike/device concepts in others; kept common-not-definitional.

## Boundary Findings

- **vs Running Application (sibling leaf)**: identical skeleton at high abstraction (record → analyze → share; plan → navigate), different sport semantics (pace/cadence/stride vs speed/elevation/bike types; shoes vs bikes+components). The seam is the sport data model. This leaf should stay a separate Type because the directory family deliberately enumerates sport-specific applications; joint-review flag recommended.
- **vs Workout Tracking Application**: generic workout tracker lacks cycling semantics (no bike context, no routing/elevation for cycling, no bike-type distinctions). Remove cycling semantics → workout tracker.
- **vs Endurance Training Platform**: that Type is plan/coach-centric (structured training plans, multi-sport, coach relationships); a Cycling Application is ride-centric. Training analytics inside a cycling app is a capability, not the defining center (Komoot barely has any; it is still a Cycling Application).
- **vs Wearable Fitness Platform**: that Type organizes around the device/wearable as the hub; a Cycling Application organizes around the ride. Device pairing is a capability here.
- **vs Hiking / Trail Application & Outdoor Recreation Discovery**: outdoor discovery serves many trail activities with POI/discovery emphasis; the cycling app's record-and-ride loop and bike semantics are absent there. Pure route-browsing without ride recording is discovery, not a Cycling Application.
- **vs Race Management Platform**: organizer-side event operations vs rider-side riding; event registration in a cycling app is a convenience surface, not the system of record for races.
- **vs Social Network**: when the feed/profile becomes primary and the ride record degenerates into shareable content, the product drifts toward a Social Network. The test: is the ride still the unit of record with cycling analysis attached?
- **"Remove what to become another Type" judgments**: remove cycling semantics → Workout Tracking Application; remove ride recording (keep only route discovery) → Outdoor Recreation Discovery / route utility; abstract the sport to running → Running Application; make it organizer-side → Race Management Platform; make the device the hub → Wearable Fitness Platform.

## Uncertainties

- Strava segments/leaderboard mechanics and club features were confirmed only via glossary/reference titles, not full articles — no leaderboard rules claimed anywhere.
- Zwift claims rest on one product page; its support site content was not extractable. In-app analysis depth, workout structure, and ride-file export for Zwift are unverified here.
- Ride with GPS (route-planning-for-clubs/events pole) could not be researched; if it shifts any commonality judgments, the impact is limited because Komoot already anchors the planning pole.
- Komoot region/premium pricing details deliberately not asserted (title-level evidence only).
- The "manual entry is definitional-eligible" judgment (historical check) relies on the sampled tracker's documented manual-activity support; very old/regional manual cycling diaries were not directly researched.

## Final Synthesis

A Cycling Application is an end-user application whose world is organized around the bicycle ride: a persisted, dated, sport-typed ride record per cyclist with cycling metrics, originating from the rider's own riding through whatever capture mechanism the product offers; mature products add maps/tracks, bike-aware route planning and navigation, device connectivity, gear management, analysis, and social/training layers; the indoor-virtual, social-tracker, and navigation-first realizations all satisfy the same invariant core. Boundaries are held against generic workout tracking (no cycling semantics), endurance training platforms (plan/coach-centric), wearable platforms (device-centric), outdoor discovery (no ride loop), and race management (organizer-side).
