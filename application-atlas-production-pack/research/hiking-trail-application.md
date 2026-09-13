# Research Notes — Hiking / Trail Application

Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1 (internal; not referenced in the final document)

## Research Goal

Understand the "Hiking / Trail Application" Application Type from real products: what its world consists of (objects, users, surfaces), how work flows through it (discover → prepare → walk → record → share), which structures are definitional vs common vs variant vs vendor-specific, and where its boundaries lie against neighboring Types in Directory §28 (Outdoor Recreation Discovery, Running/Cycling Applications, Ski Resort Recreation, Recreational Fishing) and against generic navigation/map/sport-tracker products.

## Initial Boundary (pre-research hypothesis)

- An end-user application for people who walk trails: discover trails, plan hikes, navigate on the trail, record hikes, share conditions/photos.
- Nearest directory neighbors: Outdoor Recreation Discovery (sibling, discovery emphasis), Ski Resort Recreation Application, Recreational Fishing Application, Running Application / Cycling Application (sport-specific siblings, both already documented), plus non-directory neighbors: generic Navigation Application, Map Application, Travel Itinerary Planner, Campground Booking Platform.
- Initial risks: (1) overfitting to the trail-database pole (AllTrails-shaped); (2) collapsing into "GPS sport tracker that supports hiking"; (3) confusing with Outdoor Recreation Discovery (content/discovery).

## Research Questions

1. What is the unit of record — the trail, the hike, or both? Which one is central?
2. What trail-specific attributes exist (difficulty, elevation, surface, way type)?
3. How do trails enter the system — curated database, community contribution, user planning, file import?
4. What role does the map play, and what map content matters (topo layers, trail networks, terrain)?
5. How does field navigation work — turn-by-turn, breadcrumb, corridor+waypoints? What is the wayfinding reference (trail distance vs straight line)?
6. How central is offline capability, and how is it implemented?
7. Is hike recording definitional or a byproduct? How do plan/record objects relate?
8. What community structures exist (reviews, condition reports, photos, comments)?
9. What safety structures exist (live location, check-ins, weather)?
10. What content-authority models exist (editorial, official agencies, trail organizations, community)?
11. Where does this Type end and Outdoor Recreation Discovery / Running / generic Navigation / sport trackers begin?

## Representative Products

| Product | Pole | Customer level | Why selected |
|---|---|---|---|
| Komoot | route-planning / navigation-first, multi-activity ("On foot" family includes Hiking) | consumer, free region + premium | navigation philosophy; sport-specific routing; strong help center |
| Outdooractive | trail-database / map-first platform, Europe, professional+community content | consumer freemium (Basic/Pro/Pro+) + B2B | largest European outdoor platform; official-topo-map ecosystem; rich knowledge pages |
| FarOut (formerly Guthook) | long-distance trail-guide pole (thru-hiking) | consumer, per-guide purchase + subscription | exercises "does the definition survive the corridor-guide shape" test; trail-organization partnerships |
| Strava | boundary counter-sample: generic activity tracker with Hike as a sport type | consumer freemium + subscription | confirms that recording a hike ≠ a Hiking/Trail Application |

Attempted and excluded (source-access limitation): AllTrails (support.alltrails.com and www.alltrails.com timed out repeatedly — abandoned per network rule), Gaia GPS (help.gaiagps.com and www.gaiagps.com timed out — abandoned), Wikiloc (wikiloc.com returned 403 — abandoned), FarOut support subdomain (transport error; faroutguides.com help pages used instead). The two most prominent consumer trail-database products (AllTrails, Gaia GPS) therefore could not be directly observed this pass; claims that would depend on them are kept out of the final document or softened.

## Sources

- Komoot Help Center (Zendesk-hosted): https://support.komoot.com/hc/en-us
  - Supported sport types — https://support.komoot.com/hc/en-us/articles/10194685010970-Supported-sport-types
  - Find routes and inspiration on komoot — https://support.komoot.com/hc/en-us/articles/10207999797530-Find-routes-and-inspiration-on-komoot
  - Navigate a saved route — https://support.komoot.com/hc/en-us/articles/10207935661338-Navigate-a-saved-route
  - Category "Using komoot" sections observed: Get Started; komoot Map (Map Layers, Highlights, Trail View photos, Places, 3D map view, Improve the map); Planning and Routes (plan on web/app, route suggestions, multi-day); Navigation and Recording (record, navigate, offline downloads, Live Tracking, edit activities); Community and Contributions (Highlights, Collections, Pioneer Programme, Peak Bagging, guidelines)
  - (Plus prior-pass observations from research/cycling-application.md, 2026-09-07: planner mechanics, region model, Highlights/POI content, offline use)
- Outdooractive: https://www.outdooractive.com/en/ (product page, Tier 2) and Help Center https://www.outdooractive.com/en/helpcenter/
  - What is a "Route"? — https://www.outdooractive.com/en/knowledgepage/what-is-a-route-/45483457/
  - What is a "Track"? — https://www.outdooractive.com/en/knowledgepage/what-is-a-track-/47519874/
  - The Outdooractive Map — https://www.outdooractive.com/en/knowledgepage/the-outdooractive-map/37514018/
  - How does the Route Planner work? — https://www.outdooractive.com/en/knowledgepage/how-does-the-route-planner-work-/50992312/
- FarOut: https://faroutguides.com (product page, Tier 2) and Help/FAQ https://faroutguides.com/help/ (Tier 1; tabs: iOS App, Android App, Website App, Waypoints, Check-ins, Town Guides, About, Comment Filtering, Comment Flagging, Waypoint Reporting)
- Strava Help Center: Supported Sport Types on Strava — https://support.strava.com/en-us/articles/15402005-supported-sport-types-on-strava

## Product Observations

### Komoot (evidence layer: A — direct help-center articles)

- **Sport types**: planning sports split into Cycling (road/gravel/MTB; enduro app-only) and "On foot" (Hiking, Running; Mountaineering app-only). Completed-activity labels broader (adds Nordic walking, Snowshoeing, etc.). Sport-specific routing: "sport type affects the paths komoot chooses". Hiking is a first-class planning sport. (A)
- **Discovery**: Home = personalized feed (routes/collections from people you follow, popular routes, community Highlights in your region, komoot-selected content) based on location, sports used, past activity, follows. "Routes" = active search for ready-made route suggestions: route suggestions for an area/starting point, **named trails and well-known routes** (e.g., famous hiking trails), Highlights (openable to find routes through them), Collections (themed groups). Filters: distance/duration, difficulty and elevation, surfaces and route types, starting options, scenery/nature/attractions. Map-based browsing (colored route suggestions on map). Curated/editorial: Topic Pages, editorial guides, curated Collections. Fallbacks: GPS-file import; partner/brand pages via external search; map layers (e.g., OpenCycleMap) to follow known routes. (A)
- **Planning**: web/app planner; start+destination+waypoints; sport type + route-type preferences; one-way/round trip; elevation profile with surfaces/way types/weather; Route Alerts; multi-day planning; drag route line; refused segments explained. (A, from this + prior pass)
- **Navigation**: turn-by-turn instructions + optional voice; live position on map; navigation panel (current instruction, distance/time to next waypoint and route end, speed, time in motion, elevation data, weather); map-layer switching and north-up/direction-of-travel orientation during navigation; **region around the starting point must be unlocked to enable navigation**; **offline navigation requires maps/routes downloaded beforehand**; automatic rerouting when deviating (requires stable internet); search during navigation pauses it; voice vs notification announcements (incl. waypoint/Highlight popups); Live Tracking (others follow your location); pause/finish → saved activity; post-activity review/edit (sport type, photos, highlights, description, visibility). (A)
- **Recording**: record an activity; rename; take photos while recording; planned route can be saved as a completed activity; edit completed activities. (A, structure-level)
- **Map content**: map layers (komoot map, satellite, OpenCycleMap), Highlights (community-recommended places/route sections), Trail View photos, Places/Saved places, 3D view, "Improve the komoot Map" (user contributions). (A, structure-level)
- **Community**: Highlights contributions, Collections, Pioneer Programme badges, Peak Bagging, Community Guidelines — contribution-shaped community. (A, structure-level)
- **Commerce**: free region unlock + Premium subscription; regions as the access unit. (A, structure-level)

### Outdooractive (evidence layer: A — knowledge pages + product page)

- **Positioning**: "Europe's largest outdoor platform"; surfaces: Map, Route Finder, Route Planner, Travel Guide, Community. Activity taxonomy: Hiking family = Hiking Trail, Long-Distance Hiking, Pilgrim Walk, Nature Trail, City Walk; plus Cycling, Running (Trail Running), Mountaineering (Mountain Hike, Via Ferrata…), Winter Sports (Winter Hiking, Snowshoeing…), Water, Equestrian, Motorized. (A)
- **Map**: "based on official geodata" — national mapping agencies (Germany, Austria, Northern Italy, swisstopo, IGN France, BKG, BEV) plus OSM-derived worldwide coverage; "a defined and prepared route network for many activities"; POIs (commercial, landscape, religious sites, castles, leisure, traffic, infrastructure, mountain huts); terrain display in summer and winter formats; map legend; Pro-gated. Specialized map catalogs: Alpine Club (DAV/ÖAV), KOMPASS, HARVEY, ADFC-BVA, SHOCart, freytag & berndt; official topo maps (Swisstopo, OS, IGN, USGS, NRCan…). (A)
- **Route Planner**: choose activity → activity directly affects routing ("different trail types are prioritized, and an appropriate average speed is used for the calculation"; changing activity mid-plan recalculates route on the new activity's trail network). Points via map click / search / coordinates / GPX import; round-trip planner from desired duration; point list with reorder; elevation profile + **track/way types** (trail surface conditions) update automatically; climbs/descents, elevation gain, distance/duration; "Follow paths" toggle (follow trail network vs straight line, mixable per segment); trail-networks layer with **official trails and difficulties for hiking, cycling, mountain biking, winter sports, horseback riding**; reverse / same-way-back / back-to-start (loop); waypoints with name/description/symbol; **planning requires internet** ("Planning isn't possible on offline-saved maps because routing requires up-to-date data"); unsaved-plan warnings on web. (A)
- **Object model**: **Plan** (draft preparation) → **Route** ("a detailed description with key information, images and relevant data… always based on an existing plan or track"; add description/photos; rate difficulty, stamina requirements, landscape; visibility private/published; **Roadbook** view with overview, photos, key waypoints/POIs, highlights, current closures, tips; published routes receive comments, reviews, questions) and **Track** (GPS recording: route taken + time, distance, speed, elevation changes; start/pause/end; activity type; **navigate a route while tracking or just show it on the map**; live elevation; statistics incl. avg/max speed, uphill/downhill speed, highest/lowest point; crop track; **save track as a route** for editing/publishing). (A)
- **Field/safety features**: turn-by-turn speech navigation ("no matter how small the trail"); offline maps/routes/regions ("explore in Flight Mode to save battery"); BuddyBeacon live-location sharing; Skyline AR (identify peaks/lakes/places); weather forecasts; snow-depth layer; protected-area rules ("trail rights, access restrictions and official guidance"); GPX export to GPS devices; sync with Garmin/Strava/Suunto/Wahoo/Fitbit/Polar; watch apps; print routes. (A, product page + help index)
- **Content authority**: "approved routes recommended by thousands of mountain guides, trail wardens and other industry pros"; Premium Routes from professional authors/publishers (Pro+); "Alliance of the Officials" partnerships; map from official agencies. (A)
- **Commerce**: Basic / Pro / Pro+ subscriptions; B2B myBusiness SaaS for tourism destinations. (A)

### FarOut (evidence layer: A for FAQ pages; A− for product page)

- **Positioning**: "navigational app for the best long-distance trails in the world"; 250+ hiking, biking & paddling guides; "handcrafted guides created by thru-hikers"; official-app partnerships with trail organizations (Appalachian Trail Conservancy, Continental Divide Trail Coalition, and many more). (A− product page / A FAQ)
- **Guide as the unit of commerce and content**: trail guides purchased as **sections or bundles**; "Download Before Offline Use"; lifetime purchases; per-guide purchase + "FarOut Unlimited" subscription; purchases tied to platform stores; two-device simultaneous mobile limit. (A)
- **Three views of a loaded guide**: Map, Elevation profile, Waypoint list. (A)
- **Waypoint infrastructure**: water sources, campsites, key waypoints; waypoint photos as optional download; **custom waypoints** and **custom notes on waypoints**; waypoint reporting (corrections via support); **only legal campsites listed** (Leave No Trace advocacy; some guides list official campgrounds + no-camping areas). (A)
- **Wayfinding**: GPS current location; **distances to waypoints expressed along the trail** ("x miles ahead"/"x miles behind" by trail distance when on the trail; direct-line "as the crow flies" only when off trail); change direction; **custom routes** ("Draw New Route", accounting for side trails). (A)
- **Community condition knowledge**: comments attached to waypoints; **comment filtering by topic** (Water, Connectivity, Camping, Conditions, Trail Magic, Lost-N-Found); AI-assisted comment categorization (trained on manually categorized comments; private model; no comment generation); comment flagging + anonymous down-voting; "real-time trail updates from the community"; Water Status feature. (A)
- **Check-ins**: social location updates to followers; queued until connectivity; explicitly "CANNOT be used to contact Emergency Services"; optional/private profile. (A)
- **Town Guides**: businesses (lodging, food, shuttle services) as waypoints along the corridor; business-ad policy tied to official waypoints. (A)
- **Recorded tracks**: "Track your route & remember your adventures"; recorded tracks are account data (deletable). (A)
- **Offline**: guide download + offline map sets (resolution capped to keep download size reasonable; high-res online road/satellite maps need connectivity). (A)

### Strava (evidence layer: A — boundary counter-sample)

- Foot Sports family includes **Hike**, Walk, Trail Run, Run, Wheelchair; any outdoor sport type includes a map by default; sport type changeable after upload; some features limited to core sports (riding, running, swimming). (A)
- Structure: activity record + feed + segments + training analytics. **No trail objects**: no trail database, no trail attributes (difficulty/surface), no trail-following machinery, no offline trail maps as products. The map depicts the recorded activity, not a reusable trail. (A, absence observation)
- Confirms: "recording hikes" alone does not make a Hiking/Trail Application; the Type requires the trail-as-object machinery.

## Cross-product Comparison

| Dimension | Komoot | Outdooractive | FarOut | Strava (boundary) |
|---|---|---|---|---|
| Central object | Route (planned or suggested) on a sport-specific network | Route (publishable guide) built from Plan or Track; Map as substrate | Trail guide (long-distance corridor) with waypoint infrastructure | Activity record (Hike as sport label) |
| Trail as reusable object | named trails + ready-made suggestions + Highlights; savable | curated routes + trail networks + publishable routes | the guide itself = the trail corridor | none |
| Trail attributes | difficulty/elevation/surface filters; route-type preferences | difficulty, stamina, landscape ratings; way types; official trail difficulties | waypoint types (water/campsite); elevation profile | none (sport label only) |
| Map role | working surface (planner + navigation) | substrate + product (official topo layers, trail networks) | corridor map + elevation profile | activity depiction |
| Field wayfinding | turn-by-turn + voice + rerouting | turn-by-turn speech + show-only mode | corridor + waypoints + trail-distance readout | none (no navigation product) |
| Offline | downloads required for offline nav | offline maps/routes/regions; planning needs internet | guide download; capped-res offline maps | n/a |
| Recording | record activity; plan→activity conversion | track recording; track→route conversion | recorded tracks (secondary) | the core |
| Community | Highlights/collections contributions | comments/reviews on published routes; follow orgs | waypoint comments + topic filters + check-ins | feed/segments |
| Content authority | community + editorial curation | official agencies + professional authors + trail wardens | trail organizations + thru-hiker guides + moderated comments | user-generated activities |
| Commerce | free region + premium | Basic/Pro/Pro+; B2B | per-guide sections + subscription | freemium + subscription |
| Platform | mobile + web + devices | mobile + web + watch + devices | mobile + web app | mobile + web + devices |

Stable across the three primary products (B layer): the trail/route as a persistent reusable object with trail-specific attributes; terrain-map presentation as the working surface; field wayfinding on foot with the hiker's position relative to the trail; offline capability as a first-class concern; recording as a supported but secondary loop; community condition-knowledge around trails; tiered commerce.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The trail as a persistent, reusable object of record** — a named geographic route (out-and-back, loop, or long-distance corridor) held inside the application, carrying trail-specific attributes (distance, elevation gain, difficulty, route/surface type, location). Trails enter as curated database entries, organization/community contributions, user-planned routes, or imported files. The trail outlives any single hike: it is saved, shared, re-walked, re-planned. Remove → generic map/navigation utility (ephemeral point-to-point directions, no reusable trail objects).
2. **Terrain-map presentation** — trails are presented on a terrain-aware map (elevation, natural features, trail networks; topographic layers in mature products), because hiking decisions are terrain decisions. The map is the working surface, not a backdrop. Remove → trail content/review platform (lists and articles without an operational map).
3. **Field wayfinding on foot** — the application is built to be carried while walking the trail: it places the hiker relative to the trail (position on/near the route line), supports following it (turn-by-turn, breadcrumb, or corridor-with-waypoints), and is engineered to keep working where connectivity fails (offline downloads as the common implementation). Remove → discovery/content platform (Outdoor Recreation Discovery seam).

Jointly-held is load-bearing: 1+2 without 3 = trail atlas/catalog (browse-only); 2+3 without 1 = generic outdoor GPS navigation; 1+3 without 2 = text guidebook with a GPS dot (no terrain context).

Historical check (§24 reasoning): paper trail guidebooks + topographic map sheets + compass satisfy all three legs — the trail as described named route with distance/elevation/difficulty, the terrain map, and field wayfinding along blazed trails. Club waymarked trails with printed club maps satisfy. GPS recording, offline downloads, community reviews, difficulty scales, voice navigation, subscriptions are all absent from the paper era and are therefore NOT definitional. The L0 holds for the pre-digital practice and for all three sampled products.

### L1 — Common Mature Structure (evidence layer B)

- Trail discovery layer: searchable/filterable trail catalog (distance, duration, difficulty, elevation, surface, scenery), personalized suggestions, curated/editorial collections, map-based browsing (all 3)
- Trail detail content: description, photos, difficulty/stamina ratings, POIs, current conditions/closures (all 3, different shapes)
- Elevation profile with climbs/descents and surface/way-type breakdown (all 3)
- GPS recording of the hike with distance/duration/elevation stats; plan↔record conversion in both directions (Komoot: plan saved as completed activity; Outdooractive: track saved as route)
- Waypoints/POIs along the trail (water, campsites, viewpoints, huts, businesses) (FarOut core; Komoot Highlights; Outdooractive POIs/waypoints)
- Offline maps/routes as downloads (all 3, different mechanisms)
- Turn-by-turn or guided navigation with voice (Komoot, Outdooractive; FarOut corridor-style)
- Safety layer: live-location sharing (Komoot Live Tracking, Outdooractive BuddyBeacon, FarOut check-ins), weather on route (Komoot panel, Outdooractive)
- Device ecosystem: GPX import/export, watch/handheld GPS sync (Komoot, Outdooractive)
- Community condition-knowledge: comments, condition reports, photos, collections (all 3)
- Tiered commerce: freemium/subscription/region-unlock/per-guide (all 3)

### L2 — Variant / Optional Structure

- Product shape: trail-database-first (Outdooractive) vs planner/navigation-first (Komoot) vs long-distance trail-guide (FarOut); map-first backcountry navigation products exist in the market but were not directly observable this pass (see Uncertainties)
- Activity breadth: hiking-dedicated vs multi-activity outdoor platform (hiking as one "on foot" family among cycling/running/winter/water)
- Hike scale: day-hike/weekend pole vs long-distance/thru-hike pole (corridor guides, town guides, resupply logic)
- Regional ecosystem: European official-topo-map culture (national mapping agencies, Alpine Club maps) vs US long-distance trail culture (trail-organization partnerships, trail-town economies)
- Content-authority model: official agencies + professional authors (Outdooractive) vs community contribution (Komoot Highlights) vs trail-organization + moderated community (FarOut) — most products mix
- Business model: subscription tiers, region unlocks, per-guide purchases, freemium
- Winter/alpine extensions: snow-depth layers, avalanche info, slope angles, winter-hike sport types
- AR/3D presentation: 3D map views, skyline identification, flyover videos

### L3 — Vendor-specific Structure (stays in Research Notes)

- Komoot: region unlock model; Highlights/Trail View/Peak Bagging/Pioneer Programme; Home feed selection logic
- Outdooractive: Plan/Route/Track object chain and Roadbook; ATHM; Skyline AR; BuddyBeacon; myBusiness B2B; "Alliance of the Officials"; Pro-benefit partner discounts
- FarOut: guide sections/bundles with lifetime purchases; Town Guides; comment topic filters + AI categorization + Water Status; Trail Magic / Lost-N-Found filters; FarOut Scouts; two-device limit
- Strava: segments, heatmaps, training-glossary machinery (belongs to the activity-tracker Type)

## Vendor-specific Findings

See L3 above. None of these entered the canonical core. The FarOut trail-distance wayfinding readout ("ahead/behind" along the trail) is highlighted as a distinctive implementation of leg 3 but is treated as implementation, not invariant — Komoot/Outdooractive express the same "position relative to route" idea through turn-by-turn and map position.

## Boundary Findings

- **vs Outdoor Recreation Discovery**: the sharpest seam. Discovery products center on content/places/outfitters/inspiration; a Hiking/Trail Application holds the trail as an operational object and supports walking it (field wayfinding, offline, recording). Remove leg 3 (field use) and leg 1's operational character → Outdoor Recreation Discovery. Conversely, a discovery surface inside a trail app (Komoot Home/Routes, Outdooractive Route Finder) is a standard capability, not the Type's center.
- **vs Running Application / Cycling Application**: sport apps center on the activity record + sport performance semantics (the ride/run is the unit of record; routes are secondary inputs). Trail apps center on the trail object + terrain + wayfinding; the recorded hike is a byproduct of following a trail. Strava counter-sample: Hike exists as a sport type with a map, but there are no trail objects, no trail attributes, no trail-following machinery — so Strava is not a Hiking/Trail Application.
- **vs generic Navigation Application**: road-network point-to-point directions; no reusable trail objects, no trail attributes, no terrain/offline-trail semantics, no trail community.
- **vs Map Application**: map display/search without trail semantics.
- **vs Travel Itinerary Planner / Destination Discovery**: trip-level, multi-destination planning; not trail-level field navigation.
- **vs Campground Booking Platform**: commerce for overnight sites; adjacent at the camping-waypoint layer (FarOut lists campsites as waypoints but does not transact bookings).
- **vs Ski Resort Recreation Application**: winter-resort sibling; slope/piste/lift context instead of trail network. Winter hiking/snowshoeing inside trail platforms remains a variant of this Type.
- **"去掉什么就变成另一个 Type" 判据**: remove the trail-as-object → GPS navigation utility; remove the terrain map → trail content/review site; remove field use → Outdoor Recreation Discovery; remove trail semantics and keep the record loop → sport tracker (Running/Cycling).

## Uncertainties

- AllTrails and Gaia GPS (the two most-cited consumer products in this space) could not be fetched this pass; their shapes are inferred only from market position and are NOT used as evidence in the canonical model. If a later pass reaches them, check: (a) whether AllTrails' trail-detail/review machinery matches the L1 set; (b) whether Gaia GPS's map-layer-first posture still satisfies leg 1 (trail objects as layers) — expected yes via its trail/POI layers, but unverified.
- Wikiloc (community-contributed trail database) unreachable; the community-contributed trail-database pole is therefore evidenced only indirectly (Komoot Highlights, Outdooractive community routes, FarOut comments).
- Exact difficulty-rating scales, numeric limits (map-download sizes, region counts, guide prices) deliberately not stated in the final document; vendor-specific numbers live here in the notes only where directly observed (e.g., FarOut guide file size 200KB–8MB, FarOut app version 14.0 for comment filters, Outdooractive Pro €2.50/month billing-annually promo).
- Whether "offline" should be promoted to L0 was considered and rejected: the paper-era check shows the Type exists without digital offline machinery; offline is the common implementation of the field-use leg's constraint ("connectivity cannot be assumed"), not the invariant itself.

## Final Synthesis

The Hiking / Trail Application is defined by three jointly-held structures: the trail as a persistent reusable object of record with trail-specific attributes; terrain-map presentation as the working surface; and field wayfinding on foot that works where connectivity fails. Around this core, mature products add a discovery layer (searchable/filterable trail catalogs, suggestions, curated collections), trail detail content (descriptions, photos, difficulty, conditions), elevation profiles, GPS recording with plan↔record conversion, waypoint/POI infrastructure, safety features (live location, weather), device exchange (GPX, watches), community condition-knowledge, and tiered commerce. The Type's deepest splits are product shape (database-first vs planner-first vs corridor-guide), hike scale (day vs long-distance), and content-authority model (official/professional vs community). Its boundaries: discovery-only content → Outdoor Recreation Discovery; record-centric sport semantics → Running/Cycling Applications; ephemeral point-to-point routing → generic Navigation; no trail semantics at all → Map Application.
