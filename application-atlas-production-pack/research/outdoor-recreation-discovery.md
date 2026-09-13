# Research Notes — Outdoor Recreation Discovery

## Research Goal

Understand what software sits under the directory leaf "Outdoor Recreation Discovery" (§28 Sports, Fitness & Recreation, between "School / College Athletics Management" and "Hiking / Trail Application"): products whose center of gravity is helping people **find and choose** outdoor recreation opportunities. Identify the objects (opportunity records, map, decision content, community knowledge), the discovery loop, what is definitional vs common vs variant vs vendor-specific, and the boundaries against the eight sibling Types that have already drawn seams to this leaf.

## Initial Boundary

Eight processed sibling passes have already pre-drawn seams TO this leaf. This pass must land on the same side of each seam:

| Sibling pass (date) | Seam as drawn from that side |
|---|---|
| hiking-trail-application (2026-09-08) | "remove field use → Outdoor Recreation Discovery"; discovery products center on content/places/outfitters/inspiration; a trail app holds the trail as an operational object walked with field wayfinding |
| running-application (2026-09-09) | "remove run recording (keep only route discovery) → Outdoor Recreation Discovery"; pure route browsing is not a Running Application |
| cycling-application (2026-09-07) | same pattern: no ride-record loop |
| recreational-fishing-application (2026-09-09) | "describes places and inspiration for many activities; lacks the catch record and the operational water-bound knowledge" |
| ski-resort-recreation-application (2026-09-09) | "finding and choosing destinations vs being the companion at the destination" |
| sports-marketplace (2026-09-09) | "discovery without transaction — discovery content lacks the participation transaction of record" |
| sports-court-booking (2026-09-09) | "discovery-first without slot inventory or reservations" |
| campground-booking-platform (2026-09-06) | that Type is defined by the payment-confirmed booking transaction; discovery is only its frame |

Initial risks: (1) collapsing this Type into "trail discovery" (overfitting to the AllTrails/Komoot shape, which the hiking pass classed as Hiking/Trail); (2) collapsing into generic Directory/Review Platform (§02); (3) letting Recreation.gov's reservation layer drag the Type into booking-platform territory; (4) overfitting to community-content products and making community knowledge definitional.

## Research Questions

1. What is an "opportunity" record in these products — what object types exist (trails, campsites, POIs, facilities, services, permits), and what attributes do they carry?
2. What are the discovery surfaces — map browsing, search/filter, lists, editorial/collections?
3. What is the discovery loop from inspiration to decision, and where does it hand off (navigation, booking, recording)?
4. Where does community knowledge sit (reviews, photos, check-ins, corrections), and is it definitional or common?
5. What content-authority models exist (official agency, community+moderation, editorial, hybrid)?
6. How do products handle the freshness problem (places close/change)?
7. How do products monetize if they don't transact the opportunity itself?
8. What governance rules shape content (paid placement, visited-in-person, illegal places)?
9. Where exactly are the seams to Hiking/Trail, sport trackers, booking platforms, directories, and map/navigation products?

## Representative Products

Selected for market representation, different product philosophies, different content-authority models, different customer tiers:

1. **Recreation.gov** — the official US federal public-lands portal; multi-activity; official-content-led; free government service with a reservation/permit layer on top of a discovery frame.
2. **Komoot** — multi-activity (hiking/cycling/running) route + Highlights discovery with planning and navigation; community content + curated editorial; freemium; EU-origin, global.
3. **iOverlander** — community-crowdsourced place discovery for overlanders (campgrounds + road-trip services); no commerce in the opportunity, no navigation; offline-first; global; subscription-funded.
4. **Campendium** — camping/RV discovery; community structured reviews; map-first; freemium (PRO adds RV navigation/trip tools); US/Canada; part of the Roadtrippers/Roadpass family.
5. **Wikiloc** — community trail-sharing discovery, multi-activity; navigation + live tracking in app; premium; global.
6. **PeakVisor** — mountain discovery led by 3D maps and peak identification; freemium; global.

Boundary-evidence products (observed via sibling pass, not re-fetched): AllTrails (classed as Hiking/Trail Application by the hiking pass), Hipcamp/Campspot (campground-booking territory).

## Sources

All fetched 2026-09-10 (Layer A unless noted):

- Recreation.gov homepage — https://www.recreation.gov/ (rich, readable)
- Recreation.gov Help Center — https://help.recreation.gov/helpcenter (JS-rendered, unreadable — limitation recorded)
- Komoot homepage — https://www.komoot.com/ (rich)
- Komoot Help Center home — https://support.komoot.com/hc/en-us (category structure readable; specific article fetch 404)
- iOverlander homepage — https://www.ioverlander.com/
- iOverlander Features — https://ioverlander.com/features
- iOverlander General Criteria — https://ioverlander.com/general_criteria
- Campendium homepage — https://www.campendium.com/ (rich)
- Wikiloc homepage — https://www.wikiloc.com/ (rich)
- PeakVisor homepage — https://peakvisor.com/ (rich)

Access limitations:
- **The Dyrt** — HTTP 406 on homepage (1 attempt, abandoned). The largest camping-discovery app is UNOBSERVED this pass; also unobserved by the campground-booking pass ("The Dyrt fetches blocked"). No claims rest on it.
- **AllTrails** — homepage request timed out (1 attempt, abandoned). Its classification as a Hiking/Trail Application rests on the hiking pass's research, not this pass's observation.
- **Recreation.gov Help Center** — JS-rendered shell only; reservation/lottery/permit flow details NOT characterized; no precise operational claims made about them.

## Product Observations

### Recreation.gov (Layer A — homepage)

- Self-description: "your gateway to explore America's outdoor and cultural destinations… a one-stop shop for inspiration and ideation, trip planning, information sharing, and reservations."
- Scale claim: "over 3,600 facilities and 103,000 individual sites."
- Opportunity catalog: facilities and individual sites (camping & day use), tours & tickets, permits (e.g., Christmas tree permits), interagency/site passes, lottery entry — the catalog spans multiple object kinds, not only campsites.
- Discovery surfaces: Explore by State (50-state link grid), Explore Most Popular Locations (named "gateways" — parks, forests, lakes, seashores), activity categories, "What's New on Recreation.gov" (new locations feed).
- Planning aids: "Build a Trip" tool; editorial library ("Find Inspiration & Information" — travel guides, tips, visitor stories); gear & RV rentals.
- Transaction layer: reservations, passes, permits, lotteries, tours & tickets — sits ON the discovery frame; the homepage leads with discovery language ("Find Your Next Adventure", "Explore Destinations & Activities").
- Supply side: "Add Your Facility" (agency onboarding); "Use Our Data" (open data).
- Mobile app exists. Photo contest ("Share Your Best Photo").
- Help center exists but JS-unreadable — reservation mechanics not characterized.

### Komoot (Layer A — homepage + support home)

- Self-description: "Find, plan and share your adventures"; app pitch: "navigate, discover, adventure."
- Scale claims: 45M app-dialog users / "50M+ outdoor explorers", "8M+ routes in over 100 countries", "850M+ photos, tips, and highlights shared by the community."
- Opportunity catalog is TWO-KINDED: **routes/Tours** (sport-specific: hiking, bike touring, MTB, road cycling, running, mountain hikes) and **Highlights** (POI taxonomy: Huts, Mountain Peaks, Waterfalls, Caves, Lakes, Mountain passes, Canyons, Bike Parks, Natural Monuments, Castles).
- Discovery surfaces: per-activity route discovery by region ("top 10 best hikes by region"), "Browse places" by Highlight type, **Collections** ("selected, curated and tested by komoot… include everything from detailed routes to insider info", authored by named community members), region guides (country → region → destination hierarchy, e.g. "hiking in the United Kingdom" → England → Lake District).
- Filters: "Filter by distance, difficulty, or public transport links."
- Planning: sport-specific route planner ("smooth asphalt for your road bike, singletracks for your mountain bike, or peaceful trails for your hikes").
- Navigation: "turn-by-turn voice navigation and offline maps."
- Community: "Share your adventure… photos and suggestions"; Groups; Live Tracking; Experiences; Hazard Assessment.
- Commerce: free account + paid (support category "Billing and Purchases"; voucher/gift redemption); B2B (komoot.business, Connect, Embed routes); Connected Devices (watches, GPS devices, e-bikes).

### iOverlander (Layer A — homepage + features + general criteria)

- Self-description: "a website and mobile app to help overlanders find their next destination. All of our places and reviews are created by travelers like you."
- Scale claims: "250,000 Places in 190 countries", "1M+ Check-ins and reviews", "over 5,000 place corrections every month."
- Opportunity catalog: "Campsites are just the beginning — Mechanics, restaurants, hotels, propane, water, wifi, shopping, laundry, showers, doctors, tourist attractions, border crossings, warnings, checkpoints, insurance, storage, shipping, consulates, banks, and more." The record is a PLACE serving the journey, not only a recreation site.
- Discovery surfaces: "Browse the map", "Browse by country", amenity filters ("Need a campsite with wifi? A mechanic that sells parts? A hotel with hot showers?"), map styles (street + topographic with hill shading, contour lines, building footprints), "Wild camps" (free/informal places), tent-friendly filters.
- Personal: favorites ("Favorite it. Don't forget it."), check-in history ("Track your adventures… manage the places you've added, updated or checked into").
- Offline: "No signal? No problem." — offline maps + place downloads; subscription tiers (Pro/Unlimited) sell offline maps, additional downloads, ad-free, in-app translation.
- Philosophy (features page): "**No star ratings** — One traveler's paradise is another's worst nightmare. Stars won't tell you which is which, so forget the stars—read the details." "**Unbiased Listings** — We'll never allow owners of places to buy top spots… overlanders should do the choosing, not advertisers."
- Governance (General Criteria): places must be of interest to the majority of at least one overlander type; must presently exist (valid ≥4 weeks); must not violate laws/wishes of locals or damage environment (no illegal wild camps, no fee-dodging routes); must contain relevant quality information; **must be physically visited by the contributor**; no preferential treatment for financial gain; owners may add their own place only if identified as owners; no wifi passwords; no bribery encouragement; duplicates flagged via "Report a problem"; multiple categories at one location = separate points (with a GPS-decimal convention to avoid overlap); moderation by experienced overlanders who "write the criteria that determines what places we accept."
- No booking anywhere; no turn-by-turn navigation — the map is for browsing, not following a route.

### Campendium (Layer A — homepage)

- Self-description: "RV Trip Planner and Camping Discovery Map"; "Your RV deserves a smarter co-pilot"; "Not sure where to go? Explore our Map."
- Discovery surfaces: map-first (maps.campendium.com) with category layers: Public Land, RV Parks, Overnight RV Parking, Dump Stations, Fuel & Charging, Rest Stops, Bars & Restaurants, Sights & Attractions, The Great Outdoors, Hotels & Unique Stays, Activities & Experiences, Shopping, Sports & Wellness; dedicated free-camping/dispersed/boondocking discovery; "Featured Campgrounds" / "Campers Choice".
- Community knowledge: recent reviews carry structured fields — ratings for Access, Cleanliness, Location, Noise, Site Quality, plus Days Stayed, Nightly Rate, Site Number, RV Type, RV Length, and per-carrier Cell Coverage Rating; community photos; "would stay here again" flag; "Add a Campground" contribution form; "6,000,000+ People Love Campendium" claim.
- PRO subscription: RV-Safe Navigation ("routes based on your height, weight, and propane status"), Trip Planner ("RV trip planning starts with camping"), Autopilot ("Powered by 42 million real trips"), Overnight RV Parking (15,000+ locations), CAMPalerts ("text the minute a sold-out site opens up"), Offline Maps (marked "Coming Soon").
- Ecosystem: Roadtrippers/Roadpass account family; blog; RV University; member deals; Amazon associate disclosure.
- No on-platform booking — reviewers describe booking externally; Campendium's own surface is discovery + tools.

### Wikiloc (Layer A — homepage)

- Self-description: "Trails of the World — a place to discover the best outdoor trails for hiking, cycling and many other activities."
- Scale claims: 21,748,875 members; 82,626,486 outdoor trails; 149,667,564 photos.
- The community IS the supply: "Upload your trail"; members share GPS tracks + photos.
- Discovery surfaces: Explore trails by country (country → region → city hierarchy), World Map, "Explore by Photos", All Activities & Countries, **Official Trails** (organization-published), Wikiloc Planet.
- App: Outdoor Navigation, free offline maps, Live Tracking, "Search by Passing Area"; web route planner.
- Device hand-off: "Send trails to your GPS effortlessly" (GPS device partners).
- Commerce: Premium subscription; donor program; 1% for the Planet member.

### PeakVisor (Layer A — homepage)

- Self-description: "3D Maps & Peaks Identification… explore mountains"; "Find your mountain, lake, or a perfect place among the peaks."
- Discovery surfaces: 3D map exploration; peaks identification (real-time AR + photo import labeling every peak in view); trails with 3D route visualization ("By visualizing hiking trails in the realistic 3D maps you can immediately understand where the route will take you"); worldwide mountain-range/park browsing; "world mountain lifts" (real-time open/closed lift and slope status); sun/moon trail positioning tools.
- Community: "Mountain Pulse — find other PeakVisor users who have checked-in in the same or neighboring region… See where else these peak baggers have hiked and climbed, and be inspired."
- Offline: "Download your area before you set off, then explore maps, peaks and routes with no signal at all."
- Commerce: PRO subscription (incl. lifetime gift); editorial news layer.

## Cross-product Comparison

| Structure | Recreation.gov | Komoot | iOverlander | Campendium | Wikiloc | PeakVisor |
|---|---|---|---|---|---|---|
| Opportunity record kinds | facilities, sites, tours/tickets, permits, passes | routes (Tours) + POI Highlights | places: campgrounds + journey services | campgrounds + road-trip POI categories | trails (community GPS tracks) | peaks, trails, ranges, lifts |
| Map-anchored browsing | state/location browse + maps | map + region guides | map browse + country browse | map-first with category layers | world map + by-photos | 3D map exploration |
| Search/filter | state × activity | activity × distance/difficulty/transit | amenity filters | category layers | activity × country × passing-area | region/range |
| Decision content | official descriptions + articles | route details + community tips | descriptions + check-ins (no stars) | structured reviews + photos | trail stats + photos | peak/trail data + editorial |
| Community knowledge | minimal (photo contest) | tips/photos/highlights | check-ins + corrections (core) | structured reviews (core) | uploaded trails/photos (core) | check-ins (Mountain Pulse) |
| Contribution | agency facility onboarding | share highlights | add places / check-ins / corrections | add campground / review | upload trails | check-in |
| Personal organization | trip builder | saved tours | favorites + history | account | account | account |
| Offline support | mobile app | offline maps | offline maps + downloads | PRO (coming soon) | offline maps | offline areas |
| Navigation | — | turn-by-turn voice | — (browse only) | RV-safe nav (PRO) | outdoor navigation | 3D map navigation |
| Activity recording | — | live tracking | — | — | live tracking | — |
| Opportunity transaction | reservations/permits/passes/lotteries | — | — | — | — | — |
| Commerce model | free government service + service fees | freemium | freemium subscription | freemium (PRO) | freemium (Premium) | freemium (PRO) |
| Content authority | official agencies | community + curated editorial | community + moderator criteria | community reviews + editorial | community | in-house data + community |

Reading of the table:

- **Universal (6/6)**: a persistent catalog of outdoor-opportunity records; map-anchored browsing; a per-record decision surface; mobile app; account/personal layer.
- **Near-universal (5/6)**: search/filter by activity or category; offline support; freemium subscription commerce.
- **Strong pattern, not universal**: community contribution layer (5/6 — Recreation.gov is agency-led); hand-off features (navigation 4/6, recording 2/6, transaction 1/6).
- **Anti-overfit checks**: no-star vs star ratings (iOverlander vs Campendium) — rating philosophy is variant; official vs community authority — variant; single-domain vs multi-activity breadth — variant; transaction presence — variant (Recreation.gov yes, others no).

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

Three jointly-held structures, held by a product whose center of gravity is the find-and-choose loop:

1. **The opportunity catalog of record** — persistent, individually addressable records of outdoor recreation opportunities: a place or thing-to-do outdoors (campsite, trail, peak, hut, put-in, facility/site, permit, journey service point). Each record carries outdoor-recreation-relevant attributes: where (location), what (activity/category), how demanding / how suitable (difficulty, effort, vehicle/rig fit), when (season, availability), practicalities (access, fees, amenities, rules). The record outlives any single trip. *Remove → a generic map/search/directory.*
2. **Map-anchored discovery browsing** — the catalog is presented and browsed spatially: the map is a primary working surface (browse around a place, along a route, within a region), paired with search/filter across place × activity × attributes. Technology-neutral: the paper ancestor is the guidebook's regional map sheet with numbered entries. *Remove → a text directory / editorial list.*
3. **The decision surface per opportunity** — each record renders as a detail view whose job is to inform the go/no-go choice: what it is, how to do it, what it requires/costs, and — where the product's content model provides it — what others experienced (photos, reports, ratings) and current conditions. *Remove → bare map pins / a POI layer, a map feature rather than a discovery application.*

Jointly-held load-bearing: 1 alone = a listings database; 2 alone = a generic map; 3 alone = an editorial article; 1+2 without 3 = pins without decision content; 1+3 without 2 = the paper guidebook (historical floor); 2+3 without 1 = ephemeral map content with no persistent catalog.

**Historical / market-sample check (passed)**: paper-era ancestors — regional hiking/waterway guidebooks with fold-out maps, printed campground directories (Woodall's-class RV directories), agency park brochures/maps — satisfy all three legs with no community layer, no offline machinery, no subscriptions, no apps. A government park-finder website (catalog + map + official descriptions, no community, no transaction) also satisfies the core. Therefore none of: community content, offline downloads, subscriptions, apps, ratings, multi-activity breadth, transaction layers are definitional.

**Posture (Type identity, not a 4th structure)**: the product's center of gravity is the find-and-choose loop. Field wayfinding, activity recording, and opportunity transactions may appear as layers or extensions — when one of them becomes the center, the product belongs to a sibling Type. This is the discriminator all eight sibling passes applied from their side.

### L1 — Common Mature Structure

- Search & filter by activity, geography, and outdoor attributes (difficulty, length, amenities, suitability, cell coverage)
- Curated/editorial layer: collections, guides, "best of", inspiration articles (Komoot Collections, Recreation.gov article library, Campendium blog)
- Community knowledge layer: reviews, photos, tips, check-ins, condition/correction reports (5/6 products)
- Personal organization: favorites, saved lists, trip builders, contribution history
- Offline support: offline maps and place/route downloads
- Mobile app as the primary surface (web as companion or portal)
- Freemium subscription commerce (pay for tools/coverage, not for the opportunity)
- User contribution machinery: add places, upload tracks, write reviews, report problems
- Content governance: moderation, published criteria, anti-paid-placement rules
- Hand-off integrations: send to GPS device, external navigation, booking links

### L2 — Variant / Optional Structure

- Activity breadth: multi-activity (Komoot, Wikiloc, Recreation.gov, PeakVisor) vs single-domain (Campendium, iOverlander — camping/overland)
- Content authority: official agency (Recreation.gov) vs community+moderation (iOverlander, Wikiloc, Campendium) vs curated editorial (Komoot Collections) vs in-house data (PeakVisor)
- Transaction layer: none (iOverlander, Wikiloc, Campendium, Komoot, PeakVisor) vs on-platform reservation/permit/lottery (Recreation.gov) vs partner booking hand-off (unverified this pass — The Dyrt unobserved)
- Navigation depth: none (iOverlander, Recreation.gov) → offline map browsing → full turn-by-turn incl. vehicle-constrained routing (Campendium RV-safe, Komoot voice)
- Recording: none → live tracking (Wikiloc, Komoot)
- Rating philosophy: structured star ratings (Campendium) vs deliberately no stars, read-the-details (iOverlander)
- Map technology: street/topo layers (iOverlander) vs 3D (PeakVisor) vs standard web maps
- Regional scope: global (iOverlander, Wikiloc, Komoot, PeakVisor) vs national public-lands (Recreation.gov) vs regional
- Supply-side openness: agency onboarding (Recreation.gov "Add Your Facility"), owner-identified self-listing (iOverlander owner rules), open community contribution
- B2B/partnership surfaces (Komoot B2B/embed, Recreation.gov open data)

### L3 — Vendor-specific (research notes only)

- Komoot: 45M/50M user claims, 8M+ routes, 850M+ highlights, named-author Collections, region-guide hierarchy, Groups, Live Tracking, Experiences, Hazard Assessment, voucher/gift, komoot.business/Connect/Embed, e-bike integrations
- iOverlander: 250K places/190 countries, 5K corrections/month, 1M+ check-ins, moderator stats ("collective century on the road, 30,000 hours"), no-star philosophy, wifi-password prohibition, bribery-content prohibition, illegal-place prohibition, duplicate GPS-decimal-shift convention (4th decimal ≈10m, 5th ≈1m), multiple-categories-as-separate-points rule, owner-identification rule, Ranger/Owner/Traveler FAQ split, Quick Start Guide PDFs, in-app translation (Unlimited)
- Campendium: 6M+ user claim, structured review schema (Access/Cleanliness/Location/Noise/Site Quality + Days Stayed/Nightly Rate/Site Number/RV Type/RV Length/per-carrier Cell Coverage), CAMPalerts sold-out alerts, Autopilot "42 million real trips", 15,000+ overnight-parking locations, Roadtrippers/Roadpass family, Amazon associate, RV University
- Recreation.gov: 3,600 facilities/103,000 sites, "gateway" facility pages, state link grid, lottery system, Christmas-tree permits, interagency passes, gear/RV rentals, Build a Trip, Share the Experience photo contest, "Use Our Data" open data
- PeakVisor: AR peak identification, photo-import labeling, sun/moon trails, Mountain Pulse, world mountain lifts status, lifetime PRO gift
- Wikiloc: 21.7M members/82.6M trails/149.7M photos, "Search by Passing Area", Official Trails (orgs), GPS-device partners, donor program, 1% for the Planet

## Rejected Findings

- **"Discovery products never transact"** — REJECTED. Recreation.gov transacts heavily (reservations, permits, lotteries) while remaining a discovery portal at its center. The seam to booking Types is center-of-gravity, not presence/absence.
- **"Discovery = trail discovery"** — REJECTED. Opportunity records include journey services (iOverlander mechanics/border crossings/consulates), facilities and permits (Recreation.gov), POIs (Komoot Highlights), road-trip categories (Campendium). Trails are one record kind among several.
- **"Community content is definitional"** — REJECTED. Recreation.gov is official-content-led with minimal community; the paper guidebook ancestor is editorial. Community knowledge is common-mature, not defining.
- **"Offline support is definitional"** — REJECTED. Web-first products (Recreation.gov) operate without it; it is common-mature.
- **"Multi-activity breadth is definitional"** — REJECTED. Single-domain poles (Campendium, iOverlander) are in-sample and fully in-type.
- **"Star ratings are definitional"** — REJECTED. iOverlander's no-star philosophy is explicit and successful.
- **"This Type is just a Directory Application (§02.11) with a map"** — REJECTED as a collapse, family resemblance noted: the outdoor domain binding (difficulty/season/conditions/suitability attributes, outdoors job-to-be-done), map-anchored browsing as the working surface, and the plan-an-outing loop distinguish it from generic directories.
- **"AllTrails belongs here"** — REJECTED for this pass. The hiking pass observed trail-database products as Hiking/Trail Applications (trail as operational object + field wayfinding). AllTrails was unobservable this pass (timeout); no independent claim is made.

## Boundary Findings

- **vs Hiking / Trail Application (closest sibling)** — the sharpest seam. The trail app holds the trail as an operational object and supports walking it (field wayfinding, offline, recording). Here the center is the catalog and the choice; wayfinding is absent (iOverlander, Recreation.gov) or an extension (Komoot, Campendium PRO, Wikiloc). Remove field use from a trail app → this Type; add field wayfinding as the center → Hiking/Trail. Komoot sits on this seam (planner-first); classified by the hiking pass as a trail app, used here as the planner-first boundary pole.
- **vs Running / Cycling / Workout Tracking Applications** — the record loop. Here there is no activity record as the unit of work (live tracking in Wikiloc/Komoot is an extension, not the center). Remove the record loop from a sport app → this Type.
- **vs Campground Booking Platform / Tour & Activity Marketplace / Sports Marketplace** — the transaction of record. Here discovery is the center; a transaction layer may exist on top (Recreation.gov) but the booking is not what defines the product. When the payment-confirmed booking becomes the center → booking/marketplace Types.
- **vs Ski Resort Recreation Application** — finding/choosing destinations vs being the guest's companion at the destination (live operating state, mountain day frame).
- **vs Recreational Fishing Application** — places/inspiration vs the catch record + operational water-bound knowledge (species, regs, conditions).
- **vs Directory Application / Review Platform (§02)** — generic directories list businesses for general purposes; this Type is domain-bound to outdoor recreation with outdoor attributes (difficulty, season, conditions, suitability) and a map-anchored, plan-an-outing loop. Family resemblance acknowledged; not a collapse.
- **vs Map / Navigation Application** — generic routing/wayfinding vs catalog + decision content. Here navigation is absent or an extension.
- **vs Destination Discovery Application (§26 Travel)** — travel destinations broadly (cities, stays, attractions) vs outdoor recreation opportunities specifically.
- **vs Parks & Recreation Administration (§24)** — end-user discovery vs operator-side administration of programs/facilities.

**"去掉什么就变成另一个 Type" 判据**: remove the outdoor-recreation domain binding → generic directory/review; remove the map-anchored browsing → text guidebook/directory (below the Type); remove the decision content → bare POI map layer; add field wayfinding as the center → Hiking/Trail; add the record loop as the center → sport tracker; add the booking transaction as the center → campground booking / marketplace; add the operator side → parks administration.

## Uncertainties

- **The Dyrt unobserved** (HTTP 406): the largest camping-discovery app and its partner-booking model are unverified; the "partner booking hand-off" variant is therefore NOT asserted in the final document.
- **AllTrails unobserved** (timeout): its Type membership rests on the hiking pass's research.
- **Recreation.gov operational mechanics** (reservation flow, lottery rules, payment) uncharacterized — help center JS-unreadable; no precise claims made.
- **Komoot free/paid boundary** (which regions/maps cost) not verified — no precise claims.
- **Outfitter/guide listings** as a record kind: observed only as Recreation.gov tours/tickets; generalization to a broader "outfitter listing" pattern not supported by this sample.
- **PeakVisor trail data provenance** (in-house vs community) not fully determined.
- Whether a "no-map discovery" product exists in the wild (pure editorial) — none found in sample; if one exists it would sit below the Type per the L0 test.

## Final Synthesis

The Outdoor Recreation Discovery application is the **find-and-choose layer of outdoor recreation**: an end-user product organized around a persistent, map-anchored catalog of outdoor opportunities — each record addressable, attribute-rich (where, what, how hard, when, what it takes), and rendered as a decision surface — whose job is to take a person from "where should I go / what should I do outdoors?" to a chosen, prepared outing. Around this core, mature products add search/filter machinery, curated editorial, community knowledge (reviews, photos, check-ins, corrections) with governance, personal organization (favorites, trips), offline support, and freemium tool subscriptions. The market organizes into poles by content authority (official agency / community-moderated / curated editorial / in-house data), activity breadth (multi-activity vs single-domain), and the depth of extension layers (navigation, recording, transaction) — extensions that, when promoted to the center, move the product into a sibling Type (Hiking/Trail, sport trackers, booking platforms). The discovery core itself is widely shared as a *layer* inside those sibling products; this Type is the family of products where discovery IS the center.
