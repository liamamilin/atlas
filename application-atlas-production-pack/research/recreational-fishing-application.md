# Research Notes — Recreational Fishing Application

## Research Goal

Understand the "Recreational Fishing Application" Application Type from real products: what its world consists of (objects, users, surfaces), how the angler's work flows through it (plan → fish → log → share/analyze), which structures are definitional vs common vs variant vs vendor-specific, and where its boundaries sit against neighboring Types (Hiking/Trail, Outdoor Recreation Discovery, fisheries-management, charter/tour commerce, generic social networks, weather/tide utilities, marine navigation).

## Initial Boundary

- Directory position: §28 Sports, Fitness & Recreation, sibling of Hiking / Trail Application (processed 2026-09-08), Outdoor Recreation Discovery, Ski Resort Recreation Application, Running/Cycling Applications, Water Sports Management.
- Working hypothesis before research: consumer apps for recreational anglers organized around (a) catch logging, (b) fishing spots/waters, (c) conditions (weather/tides/solunar), (d) regulations, (e) community.
- Nearest non-sibling confusion risks: **fisheries-management** (§20, processed 2026-09-08 — wild-capture fishery *governance* system of record; different object world and users), charter/tour booking (Tour & Activity Marketplace territory), marine/boating navigation (chart-first, safety-of-navigation semantics), generic outdoor social networks.
- The hiking pass recorded this leaf as a sibling; no boundary flag was left for this pass to discharge.

## Research Questions

1. What is the central record object — the catch? the trip? the spot?
2. What role does the fishable water (lake/river/coastal area/spot/reef) play as an object?
3. How do regulations (season/bag/size limits) enter the product, and how are they scoped?
4. How do conditions (weather, tides, solunar, water data) enter, and are they definitional?
5. How does species knowledge (directories, identification) enter?
6. What does the social/community layer organize around (anglers? waters? species?)?
7. What privacy norms exist around fishing spots, and how are they implemented?
8. How does field use differ from at-home use (offline, one-hand logging, hands-free capture)?
9. What is monetized (tiers, ads, hardware)?
10. Where is the boundary to fisheries-management, charter commerce, and generic activity tracking?

## Representative Products

Selected for different product philosophies, documentation completeness, and market coverage:

| Product | Philosophy | Status of evidence |
|---|---|---|
| FishAngler | social + maps + forecast + logbook ("#1 fishing app" positioning) | Tier 1: homepage + full FAQ fetched |
| ANGLR | trip-recording / fishing analytics ("plan, record, relive"), connected hardware | Tier 1: homepage + full FAQ fetched |
| Fish Rules | regulations-compliance first, GPS-scoped; logging + citizen science | Tier 1: homepage fetched (owned by Fishbrain) |
| FishVerify | species ID + regulations reference first, catch log + license wallet | Tier 1: homepage fetched (note: site blog area carries spam-injected links; only product-feature copy used) |
| Fishbrain | market-leading social fishing app | **Direct docs unreachable** (fishbrain.com 403; help center closed; archive/play timed out). Indirect official evidence only via Fish Rules ownership cross-references. Claims kept weak. |

Rejected/abandoned samples: Fishing Points (site fetch failed 405 + transport error — abandoned per network rule), iFish Australia (ifish.com.au resolved to a TV-show site, not the app), Apple App Store / Google Play listings (geo-redirect to storefront home / timeout).

## Sources

- FishAngler — https://www.fishangler.com/ (homepage) and https://home.fishangler.com/faq/ (FAQ). Fetched 2026-09-09.
- ANGLR — http://anglr.com/ (homepage) and http://www.anglr.com/frequently-asked-questions (FAQ). Fetched 2026-09-09.
- Fish Rules — https://fishrulesapp.com/ (homepage). Fetched 2026-09-09.
- FishVerify — https://fishverify.com/ (homepage). Fetched 2026-09-09.
- Fishbrain — https://fishbrain.com/ (403), https://support.fishbrain.com/ (transport error), https://help.fishbrain.com/ (transport error), https://fishbrain.zendesk.com/hc/en-us (help center closed), web.archive.org (timeout ×2), Google Play listing (timeout). All attempted 2026-09-09.
- Cross-reference: STATUS.md entries for hiking-trail-application (2026-09-08) and fisheries-management (2026-09-08) for sibling boundaries.

## Product Observations

### FishAngler (evidence layer A unless noted)

Homepage pillars: **Maps / Weather / Logbook / Community**.

- Map: "extensive database of catches, fishing spots, reports, photos, buoys" as map layers; filters; intel.
- Forecast: 7-day marine forecasts (wind, wave, water temperature); real-time NOAA marine buoy & USGS inland station monitoring; tidal prediction, water flow & water level forecasts; solunar fish forecast as a percentage with an hourly chart (FAQ: algorithm based on Solunar Theory).
- Logbook: "over 45 catch attributes" (bait type, water temperature, water depth…); catches auto-tagged with weather/forecast data; Fish ID; gear; waters.
- Community: share catches, groups, conversations; newsfeeds Global / Local (radius 10–500 miles) / Following; following anglers, fish species, and bodies of water.
- Post types (FAQ): **Log a Catch / Mark a Fishing Spot / Log a Report / Post a Photo** — four first-class content objects.
- Waters as objects: searchable "Bodies of Water near me"; users can **report missing bodies of water** (name + alternate name + notes) — community-maintained water layer; public directory of countries/regions/cities/waters/fish species.
- Species: "over 33,000 fish species" directory.
- Privacy (FAQ): catches can be public, private, or posted to groups/clubs/pages; location can be excluded; "Keep your fishing spots a secret with our privacy settings."
- Waypoints: private by default, shareable (VIP).
- Tackle box: track baits, tackles, lines.
- Monetization: free tier (forecast, bait & lure recommendations, local reports, 10-day weather, intel, digital tacklebox, groups/pages, detailed catch log) vs VIP (exact catch positions, premium map layers incl. Navionics™ depth charts, 3D terrain, nautical charts, ocean contours, shaded relief, USGS water-flow direction, private waypoints, ad-free).
- Social mechanics: no direct messaging ("on the roadmap"); @-mentions in comments; block/report.
- Map data maintenance: region selection for premium charts limited to once per 30-day period (FAQ).

### ANGLR (evidence layer A unless noted)

- Central act: **trip recording** — "When you record a trip, you enable a variety of on-the-water features at once": log catches, drop waypoints, add friends to trips, mark when/where you swap gear, access minute-by-minute weather and water conditions. These "turn into personalized trip details that get saved to your profile"; stats and reliving/sharing afterwards.
- Positioning: "plan, record, and relive all of your favorite fishing memories… recording GPS routes, logging catches, studying conditions, analyzing tackle."
- Connected hardware: **Bullseye** Bluetooth button (one click = catch, two clicks = waypoint, press-and-hold = gear change; stores coordinates, date, time, environmental conditions); Abu Garcia **Virtual rod**; **Apple Watch** (start/end trips, log catches/waypoints from the wrist); **Lowrance** unit sync (bi-directional waypoints; water depth/temperature minute-by-minute; specific Elite Ti/HDS models listed).
- Offline: "Your logbook can be fully accessed without service"; tracking continues with low/intermittent service; recommendation to start trip before losing service.
- ANGLR PRO subscription: 14 advanced map layers, real-time weather and water overlays, USGS & NOAA gages, includes Bullseye hardware.
- Gamification/community: fishing challenges with badge screenshots for prize entries; "largest community of sport fishermen" claim.
- Privacy: "Your data is your data and will be kept private unless you choose to share trip details or catch details with select people."
- Coverage: North America focus ("not yet made a significant push towards country specific species, weathers/water data, or gear outside of North America").
- Marketing counters (homepage, not used as operational facts): 500K+ trips recorded, 2.5M waypoints, 4M+ fishing activities.

### Fish Rules (evidence layer A unless noted)

- Core value: "Saltwater and freshwater fishing regulations with an easy to understand format. With a glance, know if a fish is in season, how many you can keep, how big they have to be, and more."
- **GPS-controlled**: "uses your phone's GPS and calendar to show only the regulations you need. Out to sea with no signal? Manually select your fishing location to see relevant regulations." → regulations are scoped by location AND date.
- Coverage statement: saltwater federal/state waters Maine to Texas to Hawaii; freshwater for Florida, Alabama, Texas.
- Fish ID: illustrations + photos, swipe for ID clues; #ProStaff subscription adds pro-assisted ID ("within 48hr").
- #ProStaff tier: "10,000's of Reef Locations", bookmarked locations, "Drop waypoints and notes on the map", no ads.
- Logging: "The quickest logging experience… lets you log fish as fast as possible. Go back later to fill in details." Manage fishing trips; **participate in citizen science; tagging studies and programs** (separate citizen-science page).
- Printed regulations: custom regulation set printing from the web app (desktop).
- Separate products by the same company: a **Commercial angler app** (separate listing) and **Fisheries Management** (fish.management) — the vendor itself separates angler-facing recreational tooling from commercial and governance tooling.
- Ownership: Fish Rules, LLC — support/contact and advertising route through Fishbrain properties; co-branded "Fish Rules and Fishbrain" imagery. (Fishbrain family context.)

### FishVerify (evidence layer A unless noted; site-integrity caveat: blog area spam — only product copy used)

- Core value: "Species Identification and Regulation Guide… instantly identifies your saltwater or freshwater catch with advanced image recognition."
- ID: import photos or live scan, AI identification.
- Regulations: "in season, how many you can keep, the size limit, edibility"; bag & possession limits "in the waters you're fishing"; slot limits; state records; how to measure; state/federal seasonal closures "at a glance".
- Marine weather: wind, waves, tides, air & water temp, barometric pressure "and more"; fishing forecast with solunar.
- Catch log & catch map: "creates a catch log and captures the GPS coordinates of each catch so you can return to the same location"; **environmental data automatically recorded** with each catch: wind, air temperature, moon phase, barometric pressure, cloud coverage, water temperature, wave height, sunrise & sunset.
- Sharing: save and share catches with fishing buddies or social media.
- **Digital license wallet**: securely store fishing licenses, permits, boat insurance; expiration notifications.
- Species reference: searchable local species (site states 176 freshwater / 325 saltwater species).
- Monetization: subscription with 3-day free trial.

### Fishbrain (evidence layer B/C only — sourcing limitation)

- Direct documentation unreachable from the research environment (403 / closed help center / timeouts). 
- Indirect official evidence: Fish Rules (Fishbrain-owned) co-brands with Fishbrain and routes support/advertising through Fishbrain properties; Fish Rules' site positions the two as one family.
- Market position as the largest social fishing app is common knowledge but is NOT evidenced here at Tier 1; kept out of strong claims. No operational specifics asserted.

## Cross-product Comparison

| Structure | FishAngler | ANGLR | Fish Rules | FishVerify | Assessment |
|---|---|---|---|---|---|
| Catch as logged record (species+place+time) | ✓ (45+ attributes, auto-tagged) | ✓ (in-trip catches) | ✓ (quick log, details later) | ✓ (GPS + auto environment) | **All 4** → core (B) |
| Waters/spots/waypoints as mappable places | ✓ (bodies of water, spots, waypoints, missing-water reports) | ✓ (waypoints, 14 map layers) | ✓ (reefs, bookmarks, waypoints/notes) | ✓ (catch map) | **All 4** → core (B) |
| Species knowledge layer | ✓ (33k directory) | ✓ (NA species) | ✓ (ID illustrations) | ✓ (AI ID + reference) | **All 4** → common (B) |
| Regulations (season/bag/size) | not prominent in fetched copy | not prominent | ✓ core | ✓ core | 2/4 foreground → common, definitional only for regs-first pole |
| Conditions (weather/tide/solunar/water) | ✓ core pillar | ✓ (minute-by-minute in trip) | not prominent | ✓ (marine weather + auto-record) | 3/4 → common (B) |
| Auto-captured environmental context at catch time | ✓ | ✓ | implied (conditions stored) | ✓ explicit | 3–4/4 → common mature (B) |
| Social/community | ✓ deep (feeds, groups, follow objects) | ✓ (friends on trips, challenges) | ✓ light (citizen science) | ✓ light (share) | **All 4, variable depth** → common (B) |
| Spot privacy / secrecy norm | ✓ explicit (hide spots, exclude location) | ✓ explicit (private unless shared) | ✓ (private bookmarks/waypoints) | weak in fetched copy | 3/4 explicit → distinctive Type behavior (B) |
| Trip container | implicit (logbook timeline) | ✓ central | ✓ (manage trips) | not foregrounded | 2–3/4 → common, not definitional |
| Gear/tackle inventory | ✓ (tackle box) | ✓ (gear-change events, tackle analysis) | — | — | 2/4 → optional |
| Offline field use | not explicit in fetched copy | ✓ explicit | ✓ explicit (manual location) | not explicit | 2/4 explicit → common constraint of the field setting |
| Tiered free/premium | ✓ VIP | ✓ PRO | ✓ #ProStaff | ✓ trial/subscription | **All 4** → common business model (B) |
| Connected hardware | — | ✓ (Bullseye, rod, watch, sonar sync) | — | — | 1/4 → optional/vendor |
| License wallet | — | — | — | ✓ | 1/4 → optional |
| Citizen science / tagging | — | — | ✓ | — | 1/4 → optional |
| Printed regulation sets | — | — | ✓ | — | 1/4 → optional |

## Abstraction

### L0 — Defining Invariant (deliberately small)

Two jointly-held structures; remove either and the product stops being a recreational fishing application:

1. **Water-bound fishing knowledge.** The application holds fishable waters — lakes, rivers, coastal areas, named spots/reefs — as addressable places (presented on a map in all sampled products) and attaches fishing-relevant knowledge to them: where spots are, what species are present/caught there, what rules apply there, what the conditions are, what other anglers report. Fishing decisions are water-specific decisions; the water is the frame the whole product hangs on. Remove → a fish encyclopedia, a generic journal, or a generic weather app.

2. **The angler's catch record.** The angler logs catches as structured records — species (identified against the product's species knowledge), place, time, commonly with photo, gear/bait, and auto-captured environmental context — accumulating into a persistent personal log/history that the angler revisits, stats, and shares. Remove → a read-only reference/almanac with no memory of the user's fishing.

Jointly-held load-bearing analysis:

```text
water knowledge alone          → regs booklet / lake atlas / tide almanac (paper-era lineage)
catch record alone             → fishing diary (no operational water layer)
neither                        → generic map / social / weather product
both + the loop between them   → Recreational Fishing Application
```

The loop binding the two: knowledge informs the trip (where to go, what's allowed, what's biting) → the trip produces records (catches, spots, conditions) → records feed back as knowledge (community catches/reports become intel; private spots stay private). Neither structure alone carries the Type; the pair does.

### L1 — Common Mature Structure

Present in most sampled products; expected by the market; not definitional:

- Species layer: searchable species directories; identification aids (illustrations, photos, AI image recognition).
- Regulations layer: season/bag/size limits scoped to location and date; "at a glance" compliance framing.
- Conditions layer: weather, tides, solunar periods, water temperature/flow/level; buoy/gage/station data.
- Auto-capture of environmental context onto catch records.
- Social layer organized around **anglers, waters, and species** as followable objects; feeds (global/local/following); groups; challenges.
- Waypoints and private spots; granular catch visibility (public/private/group; exclude location).
- Trip container attaching catches/waypoints/gear events.
- Tackle/gear inventory.
- Offline-tolerant field use (offline logbook; manual location without signal; tracking through intermittent service).
- Tiered free/premium monetization.

### L2 — Variant / Optional Structure

- Regulations-first vs social/log-first vs analytics-first vs ID-first emphasis (all observed in-sample).
- Connected hardware ecosystems (Bluetooth catch buttons, instrumented rods, watches, sonar-unit sync).
- Digital license/permit wallet.
- Citizen science / tagging-program participation.
- On-demand printed regulation sets.
- Regional data coverage (North America-focused vs global; US state/federal reg splits; per-country species/regs data).
- Bait/lure recommendations; fish-forecast scoring.
- Freshwater vs saltwater emphasis.

### L3 — Vendor-specific (research notes only)

- FishAngler: 45+ catch attributes; 33,000 species; 10–500 mile feed radius; Navionics™ depth charts; 30-day region re-selection limit; VIP feature list; "no DM, on roadmap".
- ANGLR: Bullseye click semantics (1 catch / 2 waypoint / hold gear-change); up to 10 paired Bullseyes; 2-year battery claim; Lowrance model list; 14 map layers; PRO bundle with hardware; North America data scope.
- Fish Rules: #ProStaff 48-hour pro ID; "10,000's of reef locations"; coverage statement (Maine→Texas→Hawaii saltwater; FL/AL/TX freshwater); desktop print tool.
- FishVerify: 176/325 species counts; 3-day trial; license wallet contents.
- Fishbrain: unreachable — no L3 claims recorded.

## Vendor-specific Findings

See L3 above. Additionally: FishAngler's business solutions (advertising, "Pages" for businesses) and ANGLR's shop are commerce/advertising surfaces around the app, not part of the angler-facing core.

## Rejected Findings (anti-overfit)

- **"Fishing apps are social networks"** — rejected as definitional. Fish Rules and FishVerify are in-type with minimal social layers. Social depth is a variant axis.
- **"Solunar forecasts are definitional"** — rejected. Present in 3/4 but absent as a foreground capability in the regs-first pole; also scientifically framed by vendors as a theory-based heuristic, not a fact.
- **"Trip recording is the unit of record"** — rejected. ANGLR centers the trip; FishAngler centers the catch timeline; Fish Rules centers the regulation check. The trip is a common container, not the invariant.
- **"GPS-scoped regulations are definitional"** — rejected. Only the regs-first pole makes them central; other products carry regulations weakly or not at all in fetched copy.
- **"Catch maps with exact positions are definitional"** — rejected. FishAngler gates exact positions behind VIP; privacy norms deliberately obscure positions. The *record* of the catch is invariant; its public positional precision is not.
- **"Connected hardware is definitional"** — rejected. 1/4 in-sample.
- Marketing counters (trips recorded, waypoints logged, species counts) — not promoted to operational facts.

## Boundary Findings

| Neighboring Type | Seam | "Remove what → becomes the other Type" |
|---|---|---|
| **Fisheries Management** (§20, processed) | object world & users: wild stocks × management areas × effort/entitlements for regulators/commercial vs the angler's personal waters/catches. The vendor itself (Fish Rules' company) ships a separate "Fisheries Management" product and a separate Commercial angler app — a vendor-documented three-way split. Citizen-science logging is a voluntary contribution channel into research, not governance machinery. | Give the catch record statutory weight and the water a governing frame with quotas/entitlements → fisheries-management territory. |
| **Hiking / Trail Application** (sibling, processed) | trail = walked route object with wayfinding-along-a-line; fishing = water/spot knowledge + catch record; no "follow the line" loop. | Replace the catch record with a walked-track record and the water layer with a trail network → hiking/trail territory. |
| **Outdoor Recreation Discovery** | discovery is a capability here, not the center; the Type must hold the catch record and water-bound operational knowledge. | Keep only inspiration/content/places, drop the record and operational knowledge → discovery territory. |
| **Tour & Activity Marketplace / charter booking** | transacting guided trips is commerce; this Type supports one's own fishing. Vendor "business solutions" (FishAngler Pages/ads) are advertising surfaces, not booking. | Make the transaction (book a charter/guide) the primary object → marketplace territory. |
| **Generic Social Network** | the follow graph here is organized around waters/species/catches with catch semantics and spot privacy; FishAngler even lacks DM — social exists to share intel, not to converse. | Remove water-binding and catch semantics → generic interest social network. |
| **Weather / Tide utility** | conditions without water-bound fishing knowledge and a catch record = a weather app with fishing framing. | Remove knowledge + record, keep forecasts → weather/tide utility. |
| **Marine/boating navigation** | charts exist for safety of navigation; fishing apps consume depth/structure as *fishing* knowledge. Conceptual seam; not directly evidenced in-sample (no nav product sampled). | Make safe boat operation the primary job → navigation territory. |
| **Workout / Activity Tracking** | ANGLR's "stats" are fishing stats (catches, waypoints, gear), not athletic training load; the catch, not the exercise session, is the unit. | Make the session's athletic performance the record's center → workout tracking. |

## Historical / Market-Sample Check

- Paper-era lineage satisfies the two-leg core without any software: the angler's logbook (species/date/place/lure/weight + photos) = leg 2; the lake map / chart / printed regulation booklet / tide table & solunar almanac = leg 1's knowledge. The modern app merges artifacts that existed separately — the *application* is the merged, interactive form.
- Regional products: US state/federal regulation splits (Fish Rules' coverage statement), North-America-focused data (ANGLR), global species directories (FishAngler) — the two-leg core is region-neutral; regulations and species content are regional *content* inside a stable structure.
- The regs-first pole (Fish Rules) proves the knowledge layer can dominate; the social/log pole (FishAngler/Fishbrain pattern) proves the record layer can dominate; the analytics pole (ANGLR) proves the trip container can be foregrounded. One Type, multiple dominant poles — the pair (water knowledge + catch record) holds across all poles.
- No platform-native or pre-smartphone *application* generation exists for this Type (it is inherently a mobile-GPS-era form); the paper-artifact check stands in for the historical test.

## Uncertainties

- Fishbrain operational specifics unverified (sourcing limitation recorded above). Its inclusion in Representative Products rests on market position + family cross-references, not fetched documentation.
- Fishing Points (conditions-first pole) could not be fetched; the "conditions-first" variant is asserted only as a market shape inferred from the sampled products' conditions layers, not from a fetched conditions-only product.
- Whether regulations data in social-first products (FishAngler/Fishbrain) exists but was simply not surfaced in fetched copy — possible undercount of the regulations layer's prevalence.
- Exact mechanics of "citizen science" data flows (what is shared with whom, consent granularity) not researched beyond Fish Rules' homepage statements.
- Navionics/boating-navigation boundary asserted conceptually; no nav product fetched to test the seam from that side.

## Final Synthesis

The Recreational Fishing Application is the angler's companion organized around two jointly-held structures: **water-bound fishing knowledge** (fishable waters/spots as mappable, knowledge-carrying places) and **the angler's catch record** (structured, species-identified, place- and time-bound catch entries accumulating into a persistent personal log), bound by the plan → fish → log → share/analyze loop in which knowledge informs trips and records enrich knowledge. Around this core, mature products add species identification, location-and-date-scoped regulations, conditions/forecast layers, social intel organized around anglers/waters/species, spot-privacy machinery, trip containers, and tiered monetization; hardware ecosystems, license wallets, citizen science, and printed regulation sets are optional. The Type's most distinctive behavioral norms are **spot secrecy** (granular visibility and position obscuring) and **location-and-date-scoped rules** (regulations change by water and by day). It is separated from fisheries-management by object world and users (personal record vs governance of record), from hiking/trail by the absence of a walked-route object, from discovery products by the operational record, and from weather/social/map utilities by the requirement that both core structures be present.
