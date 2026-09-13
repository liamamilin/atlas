# Research Notes — Travel Itinerary Planner

Directory leaf: Travel Itinerary Planner (§26 Travel, Hospitality, Food Service & Events)
Slug: travel-itinerary-planner
Research date: 2026-09-09
Methodology: WORKFLOW_v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

---

## Research Goal

Understand, from real products, what a traveler-facing trip-planning application is: what its primary record is, what objects live inside it, how the planning loop works, and where it ends against the neighboring traveler-side and operator-side travel Types.

## Pre-hung Flag (from destination-discovery-application pass, 2026-09-07)

The destination-discovery-application pass recorded a joint-review flag naming this leaf as the heaviest seam in the travel family, and recommended: adopt the **primary-record test** — remove the trip/itinerary machinery → a destination catalog still stands (discovery); remove the destination catalog and only a trip workspace remains (planner); treat discovery-layer-inside-planner as **layered packaging**, not a duplicate leaf. A secondary note: travel-review-platform (§26, unprocessed) realizes destination pages as aggregation context over review records — the same test applies from that side. This pass formally adopts the test and discharges the flag (see Boundary Findings).

## Initial Boundary (hypothesis before research)

- Core use: a traveler assembles the parts of one prospective journey (places to go, things to do, stays, transport, reservations, notes) into an organized plan.
- Users: leisure travelers, group-trip organizers, business travelers who need their bookings in one place.
- Nearest neighbors: Destination Discovery Application (explore/catalog), booking Types (OTA / Flight / Hotel / Package / Tour & Activity), Travel Review Platform, operator-side systems (Travel Agency Management System, Tour Operator Management System, DMC Platform), Corporate Travel Management Platform, Calendar Application, Event Agenda Management, Mobility-as-a-Service, Hiking Trail Application, Flight Planning Application.
- Likely boundary: the **trip/itinerary is the primary record** for the planner; catalogs, priced inventory, reviews, and business money records belong to neighbors.
- Unknowns: is day-by-day structure definitional or just dominant? Is the discovery layer definitional? Is auto-import of bookings definitional? Is collaboration definitional? Where does the route-first road-trip style sit?

## Research Questions

1. What is the unit of record — the trip? What does a trip contain?
2. What are itinerary items and what kinds exist (place, activity, lodging, transport, reservation, note)?
3. How are items arranged — day-by-day, route, both? Is day-grain definitional?
4. Where do items come from — discovery layer, import of confirmation emails, hand entry, booking inside the plan?
5. What happens during the trip (offline use, alerts, changes)? After the trip (archive, reuse)?
6. Collaboration: who shares, with what roles?
7. What does the planner NOT do — no selling, no operator money record, no policy wrapper?
8. What is era-current (AI drafting, flight-status feeds) vs structural?

## Representative Products (4 sampled)

Selection rationale: market representativeness + documentation reachability + different product philosophies + different customer tiers/geographies.

| Product | Philosophy pole | Tier / geography | Access |
|---|---|---|---|
| TripIt (SAP Concur) | bookings-first organizer: itinerary assembled from confirmation emails; business-travel anchored; no meaningful discovery layer | frequent/business travelers, global | Homepage + How-it-works fetched 2026-09-09 (evidence layer A) |
| Wanderlog | planner-first builder: itinerary + map in one view; collaboration, budget, guides marketplace | leisure/group travelers, consumer free+paid | Homepage, plan-a-trip page, guides page fetched 2026-09-09 (A) |
| Tripomatic | planner-first with curated place database + navigation; Explore→Plan→Go loop; print/PDF export; multilingual (12 languages, EU-based) | leisure travelers incl. EU/Central-Europe | travel.sygic.com now serves Tripomatic; homepage fetched 2026-09-09 (A). Note: Sygic Travel and Tripomatic are the same lineage — domain observed serving the Tripomatic product |
| Roadtrippers | route-first road-trip planner: start→destination stops along a driving route; POI discovery ("Extraordinary Places"), RV specialization, magazine/forum | US road-trip / RV community, freemium | Homepage fetched 2026-09-09 (A) |

Also attempted: TripCase (Sabre) — site unreachable (redirects to a Sabre 404; product appears retired); Tripadvisor Trips (planning layer inside a review giant) — tripadvisor.com blocked (403), recorded as unverified instance, used only with qualified wording.

## Sources

- TripIt — https://www.tripit.com/web ; https://www.tripit.com/web/free/how-it-works (fetched 2026-09-09)
- Wanderlog — https://www.wanderlog.com/ ; https://wanderlog.com/plan-a-trip ; https://wanderlog.com/guides (fetched 2026-09-09)
- Tripomatic — https://travel.sygic.com/ (serves Tripomatic product) (fetched 2026-09-09)
- Roadtrippers — https://roadtrippers.com/ (fetched 2026-09-09)
- Prior pass context: research/destination-discovery-application.md (boundary flag), applications/corporate-travel-management-platform.md, applications/travel-agency-management-system.md, applications/tour-operator-management-system.md, applications/destination-management-company-platform.md (operator-side seams, cross-referenced)
- Unreachable: tripadvisorsupport.com / tripadvisor.com/Trips (403); help.wanderlog.com (timeout); tripcase.com (retired). Per evidence rules, no precise operational claims are made from these.

Source-access limitation: all four sampled products were reached only at their public product/marketing pages; deep help-center articles were not reachable for TripIt (freshdesk portal not opened), Wanderlog (help subdomain timeout), Tripomatic (support portal not opened), Roadtrippers (support portal not opened). Claims below are therefore held at the strength of directly observed product pages (layer A) and cross-product commonality (layer B); no numeric limits, plan-tier details, or default settings from help centers are asserted in the final document.

---

## Product Observations

### TripIt (evidence layer A — directly observed)

- Positioning: "Organize your travel itinerary automatically"; "You handle the booking, TripIt builds your itinerary."
- Core loop: forward booking confirmation emails to a product address → the system "automatically adds it to your trip" and builds "a comprehensive itinerary for every trip"; works "no matter where you book".
- The trip is the container: "a comprehensive itinerary for every trip"; multiple trips held in one place.
- Output is a consultable plan: "Access your trip details on the go"; send plans to calendar or to anyone chosen; apps across phone/watch/desktop.
- Paid tier (Pro) adds real-time flight alerts and travel reminders/guidance (gate/delay information framed in testimonials) — an era-current monitoring layer on top of the itinerary, not the itinerary itself.
- No place-discovery/explore layer observed on the product pages — planning input is the user's own bookings. This is the strongest witness that a discovery layer is NOT definitional.
- Blog/travel-guides content exists but as editorial marketing, not a planning object layer.

### Wanderlog (evidence layer A)

- Positioning: "One app for all your travel planning needs. Create detailed itineraries, explore user-shared guides, and manage your bookings seamlessly."
- Itinerary builder: "save all your reservations, flights, and attractions in one place. See your plans laid out on a color-coded map, organized by day or by category." → day-organization AND category-organization both exist; map is a first-class view.
- Route: "See your itinerary laid out on a map with distance and time between places. The optimize route feature helps to save on gas and time." → inter-item geometry is computed and user-visible.
- Discovery layer inside the planner: "Our guides use traveler reviews from Tripadvisor and Google to rank activities, restaurants"; "you can search for a location and there are recommended things to do… quickly add it to a list"; auto-populates place cards with "a featured pic and description from the web"; place detail pages and per-city/park explore pages exist (footer: explore cities and countries, places to visit by destination, etc.).
- Reservation import: "Forward your confirmation emails to Wanderlog and we'll auto-populate your itinerary with dates and times for flights, reservations, and more." Same mechanism as TripIt, inside a builder-first product.
- Collaboration: "Invite your trip mates and plan your upcoming trip together in real-time"; expense splitting with "tripmates"; a reviewer: "the free version let both of us access the itinerary, add information."
- Budget: "Set and manage your budget, track expenses, split bills, converts currency."
- Other standard features: packing checklists, flight status, offline access ("Download your trip plan… even without an internet connection"), lodging booking with price comparison, AI assistant, browser extension, export route to Google Maps.
- Guides marketplace: user-created itineraries published as guides (likes/views counters; browse by destination) — the planner's trip format doubles as shareable content; copying others' trips as a starting point is a supported pattern ("look at trips that others have planned for inspiration").
- Idea-staging: "Super useful app to plan a trip and create a bucket list of places to visit" → items can exist in a trip before being scheduled (unscheduled pool).

### Tripomatic (evidence layer A)

- Positioning: "Explore. Plan. Go. Discover places to visit, plan your day-by-day trip itinerary, and navigate easily."
- Three-phase loop stated by the vendor: **Explore** (browse destinations and find inspiring places) → **Plan** (build your itinerary with smart routing and drag-and-drop) → **Go** (navigate on the go, even offline).
- Day-by-day is the organizing unit: "Organize your trip into days with drag-and-drop scheduling and smart time estimates."
- Place database: "Millions of Places — Explore top attractions and hidden gems with detailed information, opening hours, and local tips."
- Routing: "Get optimized routes across walking, public transit, car, bike, and hiking trails."
- Cost estimation: "automatically tracks the costs of activities in your trip for each traveler. You can also add extra expenses or adjust any costs manually."
- Tours & tickets booking inside the plan ("Book tours, skip-the-line tickets, and activities directly in your plan") — commerce as an attachment to the plan.
- Collaboration with roles: "share your trip with others and choose whether they can edit it or view it only."
- Export/print: "Export to PDF, GPX, or KML and access your plan offline on any device"; FAQ: "You can download your trip itinerary as a PDF and print it."
- Trip lifecycle: "All your trips are saved in your account. You can revisit them, duplicate them, or use them as a starting point for a new trip."
- Notes: "add notes to each day, place, or route in your trip."
- Road trips / multi-day multi-stop supported ("add as many destinations as you need and organize them into a day-by-day itinerary… plan your driving time and decide how many days to spend at each location").
- Explicit self-positioning vs map apps (FAQ): "Google Maps is great for navigation. Tripomatic is built for trip planning. It helps you decide where to go, what to see, and how to structure your days."
- AI itinerary generation is offered as a feature layer ("Let AI craft your perfect itinerary based on your interests, pace, and travel style") — era-current.

### Roadtrippers (evidence layer A)

- Positioning: "A road trip planner that plans your trip for you"; the planner is reachable as a map surface ("Explore the map", maps.roadtrippers.com).
- Trip creation is route-anchored: Starting Point → Destination fields; "Plan on your own — Explore and discover stops by yourself".
- Autopilot (AI): "creates your itinerary based on what we've learned from over 42 million trips" — generative itinerary as an era-current layer.
- Items are **stops** along the route; discovery is a POI database: "5 million points of interest", curated "Extraordinary Places" layer, trip guides, magazine content, famous-route guides.
- Plan-gated structure (plan tiers): "Saved trips: 1 / 3 / 5 / ∞; Stops per trip: 3 / 20 / 50 / 150; Trip export; Trip collaboration; Navigation; Offline maps; Live traffic; RV GPS; Overnight RV parking" — the trip/stop structure is the priced unit; numeric caps are plan-specific (research notes only, not canonical).
- Collaboration: "Plan, discover, and collaborate" (collaborator UI shown).
- Vehicle context: vehicle profiles (car/RV/motorcycle) with fuel cost estimates; RV GPS; campground search/booking for RVers — domain specialization layered on the trip/stops model.
- Sync: "Anything you plan or save automagically syncs with the apps" — web planner + mobile companion.
- Community: forum, user-submitted POI finds ("See what roadtrippers are finding").

### TripCase (not sampled — unreachable)

tripcase.com resolves into a Sabre corporate 404; the product site appears retired. Not used as evidence. Recorded as Source-access limitation.

---

## Cross-product Comparison

| Structure | TripIt | Wanderlog | Tripomatic | Roadtrippers | Assessment |
|---|---|---|---|---|---|
| Trip as persistent container (named, held across time, revisitable/duplicable) | Y ("every trip", account-held) | Y (trips list, saved) | Y ("all your trips are saved… revisit, duplicate") | Y ("saved trips" as the priced unit) | **All 4 — defining** |
| Itinerary items anchored to places (attractions/food/lodging/transport) | reservations + travel events | attractions, restaurants, lodging, flights | places, activities, lodging, routes | stops (POIs) along a route | **All 4 — defining** |
| Reservations/bookings held inside the plan | Y (core mechanism: email forward) | Y (email forward + manual + in-plan booking) | Y (tours/tickets in plan) | weak/absent on homepage (campground booking for RV) | **3/4 strong, 1 partial — common, not definitional** |
| Day-by-day arrangement | day-ordered itinerary (auto from bookings) | "organized by day or by category" | "organize your trip into days" (drag-drop) | route-first; days secondary | **All 4 (day-grain varies) — defining as time-structure, day-grain as dominant realization** |
| Route/map arrangement with computed distance/time | map view secondary | Y (optimize route, distance/time) | Y (smart routing, multi-mode) | Y (route is the spine) | **All 4 — common-to-defining; spatial arrangement present throughout** |
| Discovery/explore layer (place DB, recommendations, guides) | absent | Y (Tripadvisor/Google-sourced recs, guides marketplace, explore pages) | Y (curated place DB, destination browse) | Y (5M POIs, Extraordinary Places, trip guides) | **3/4 — common, NOT definitional (TripIt witness)** |
| Collaboration/sharing | Y (share plans, calendar) | Y (real-time co-editing, expense split) | Y (edit vs view-only) | Y (collaboration feature) | **All 4 — common** |
| Export/print/offline | apps + calendar | offline download, export to Google Maps | PDF/GPX/KML + offline | offline maps + trip export (plan-gated) | **All 4 — common** |
| Budget/expense tracking | not observed | Y (+ split, currency) | Y (+ manual adjustments) | fuel-cost estimate via vehicle profile | **3/4 — common at leisure pole** |
| Travel-status alerts (flight status/delays) | Y (Pro tier) | Y (flight status feature) | not observed | live traffic (plan-gated) | **2/4 — optional/plan-gated** |
| AI itinerary generation | not observed | Y (AI assistant) | Y (AI planner) | Y (Autopilot) | **3/4 — era-current layer, NOT definitional** |
| Community/content layer (guides, magazine, forum) | editorial blog only | Y (guides marketplace) | place content, destination lists | Y (magazine, forum, route guides) | **2-3/4 — variant layer** |
| Booking transaction inside the product | no (bookings made elsewhere) | lodging price comparison/booking | tours & tickets in plan | campground booking (RV) | **2-3/4, shallow — commerce is an attachment, not the record** |

## Canonical Model

### L0 — Defining Invariant (minimal; all three jointly held)

1. **The trip as the unit of record.** A persistent, identified container for one prospective travel undertaking — a journey bound to destinations and (typically) dates, held across the whole planning horizon, revisitable and reusable. Remove → a place catalog (discovery territory) or a generic list/calendar.
2. **Travel items bound to the trip.** The trip's content: things to see and do, places to stay, transport between stops, reservations, and notes — each anchored to a place, optionally to a time. Items enter by discovery, import of confirmations, hand entry, or booking. Remove → an empty container.
3. **Arrangement into a followable plan.** Items are organized along the journey's time/space structure — a day-by-day sequence and/or an ordered route on a map — presented as a plan the traveler can read, follow, and consult while traveling. Remove → a save-list / idea board / bookmark collection.

Jointly-held is load-bearing:
- 1 alone = a trip folder/calendar shell with nothing in it
- 2 alone = a save-list / destination-discovery shortlist / bookmark manager
- 3 alone = a schedule with nothing planned
- 1+2 without 3 = a trip stash of unordered ideas ("bucket list" state)
- 1+3 without 2 = an empty itinerary template
- 2+3 without 1 = a floating day plan / route list with no trip context (generic planner territory)

### L1 — Common Mature Structure (present across the sample, not definitional)

- place-discovery/explore layer (database, recommendations, guides) — 3/4
- reservation capture: email-forward auto-import, manual entry, in-plan booking — 3/4 strong
- map view with computed distance/time and route optimization — 4/4
- collaboration with roles (edit vs view; co-planning; expense split) — 4/4
- offline access + export/print (PDF, GPS formats, calendar, hand-off to navigation apps) — 4/4
- budget/expense tracking — 3/4
- trip duplication/reuse and shared itineraries as content — 2-3/4
- cross-device sync — 4/4 (era-standard)

### L2 — Variant / Optional Structure

- identity of the pole: bookings-first organizer (business-travel anchored, no discovery) vs planner-first builder (leisure, discovery-rich) vs route-first road trip (driving spine, vehicle/RV specialization)
- day-grain emphasis: day-by-day as primary spine (Tripomatic, Wanderlog) vs day-secondary route-first (Roadtrippers) vs auto-ordered from bookings (TripIt)
- travel-status monitoring (flight alerts, live traffic) — often plan-gated
- commerce attachment (tours/tickets in plan, lodging price comparison) — shallow, product-dependent
- community/content layer (guides marketplace, magazine, forum) — product-dependent
- region/language posture (12-language EU product vs US-centric RV ecosystem)
- AI itinerary drafting — era-current, all poles adopting
- dateless idea-trips (bucket lists) as an immature state of the same container

### L3 — Vendor-specific (research notes only)

- TripIt's plans@tripit.com forwarding address and "Supported Booking Sites" registry; Pro tier packaging (alerts, travel guidance)
- Roadtrippers' Autopilot brand, "Extraordinary Places" curation, saved-trips/stops numeric plan caps (1/3/5/∞ trips; 3/20/50/150 stops), Roadpass ecosystem, roadside-assistance bundle
- Wanderlog's "tripmates" expense splitting, browser extension, blog embeddable maps
- Tripomatic's GPX/KML export set, OpenStreetMap/Wikimedia place-data sourcing, B2B arm
- Sygic↔Tripomatic brand history (travel.sygic.com now serves Tripomatic)

## Rejected Findings (anti-overfit)

- **Discovery layer is NOT definitional** — TripIt runs the whole Type with no meaningful discovery layer. Held as layered packaging when present (3/4).
- **Reservation auto-import is NOT definitional** — modern-common (email-forward at TripIt/Wanderlog), but hand-built plans are first-class (Tripomatic/Roadtrippers poles).
- **Day-by-day grain is NOT strictly definitional** — route-first planning (Roadtrippers) organizes along a driving spine with days secondary; the invariant is temporal/spatial arrangement, day-grain is the dominant realization.
- **Collaboration is NOT definitional** — universal in-sample but the Type works solo; paper-era itineraries were single-author.
- **AI drafting is NOT definitional** — era-current layer (would fail the historical check by construction).
- **Numeric limits / plan caps / export format lists** — plan- and product-specific, kept out of the canonical document.
- **"Itinerary planner = travel agent tool"** — rejected: agent-side itinerary assembly is the DMC/Tour-Operator/Travel-Agency territory (operator money record); this Type is the traveler's own trip.

## Boundary Findings

1. **vs Destination Discovery Application (pre-hung flag DISCHARGED)** — the primary-record test is adopted and held both ways with fresh evidence: Wanderlog's explore/guides layer, Tripomatic's place database, and Roadtrippers' POI/Extraordinary-Places layer all exist *inside* planner-first products whose primary record is the trip (removal test: strip the trip machinery → a destination catalog still stands on the same place data; strip the catalog → only a trip workspace remains). TripIt is the converse witness: a full planner with no discovery layer. Discovery-inside-planner = layered packaging; the two leaves both stand. Secondary seam to travel-review-platform (unprocessed): same test applies from that side (destination pages there are aggregation context over review records); one major review platform's embedded trip-planning layer could not be verified this pass (403) — recorded as unverified instance only.
2. **vs booking Types (OTA / Flight / Hotel / Vacation Rental / Package / Tour & Activity)** — those Types center on priced inventory and the transaction; the planner holds bookings as *items* and arranges them. In-sample commerce is shallow (ticket/lodging attachments) and never the record. When search→price→book is the center, the product is a booking Type.
3. **vs operator-side systems (Travel Agency Management System / Tour Operator Management System / DMC Platform)** — their itinerary is a *product/quote for sale*: supplier terms, margins, client money records, bookings operated on behalf of a client. This Type has no supplier terms, no business money record; the traveler plans their own trip.
4. **vs Corporate Travel Management Platform** — the corporate platform wraps the trip in a company program (policy, approval, expense, duty of care); the itinerary there is a managed trip record. This Type has no program and no policy wrapper. (TripIt's business-traveler anchor shows affinity, not identity — TripIt organizes the traveler's plans; it does not run a corporate travel program.)
5. **vs Calendar Application** — a calendar holds generic time events without place-anchored travel semantics, route geometry, or a trip container; the planner's items are travel-shaped and trip-bound. Planners push to calendars (hand-off seam), not vice versa.
6. **vs Event Agenda Management** — sessions at a bounded event, venue-bound, attendee-facing; not a journey across places.
7. **vs To-do List Application (and sibling consumer planners, e.g. the processed Home Improvement Planner)** — the consumer-planner family pattern: a bounded real-world effort as the record. The subject differs — a trip (journey across places/dates) vs tasks or a home project; the planner's items are place-anchored and route-connected.
8. **vs Hiking Trail Application** — trail-level objects with field navigation on foot; the itinerary planner is trip-level, multi-place, journey-grain.
9. **vs Flight Planning Application** — aviation computation and regulatory filing; the travel planner has no aviation world model.
10. **vs Mobility-as-a-Service Platform** — urban door-to-door mobility consumed as individual trips/services; different grain from the multi-day journey plan.
11. **vs Map/Navigation applications** — navigation routes to a known target; the planner decides and structures what the targets are (Tripomatic's own FAQ framing corroborates).

## Historical / Market-Sample Check

- Paper-era realization: a traveler's (or travel-agent-issued) printed day-by-day itinerary — trip title/dates, per-day ordered list of places, times, reservations, transport, notes — satisfies all three L0 structures with no digital machinery. Class-level lineage evidence only (no archived source fetched this pass; kept low-strength).
- Group-trip itinerary booklets (the printed "trip notebook" tradition accompanying organized group tours, incl. the Japanese 旅のしおり custom) realize the same structure — container + items + day arrangement — for a non-commercial organizer. Class-level, low-strength.
- Early-2000s email-forwarding itinerary builders (the TripIt/TripCase generation) realize the organizer pole without maps-first UI, AI, or collaboration as shipped at launch.
- The definition therefore holds for older/regional/analogue realizations; no era-current capability (maps, sync, discovery DB, email import, AI) is load-bearing in L0.

## Uncertainties

1. Tripadvisor-class embedded planning (planning layer inside a review platform) — unverified this pass (403); held structurally, qualified wording in the final document.
2. Deep help-center behavior (exact import parsing, attachment semantics, notification defaults) — not reachable; no precise operational claims made.
3. Whether a significant market of pure "auto-aggregator" organizers exists beyond the sampled organizer pole (TripCase appears retired; Google Trips discontinued 2019 — market memory, not evidence; not asserted in final doc).
4. Roadtrippers' trip/stop model as a variant vs its own Type: held as Variant — the trip+items+arrangement core is intact; the route spine is a realization. A future pass on a "road trip planner" leaf (none exists in the directory) would apply the same primary-record test.
5. Regional planner ecosystems (e.g., Japan/China super-app trip features) not sampled; held as possible variants only.

## Final Synthesis

A **Travel Itinerary Planner** is a traveler-facing application whose defining core is the **trip as the unit of record** — a persistent container for one prospective journey — filled with **travel items anchored to places** (things to do, stays, transport, reservations, notes) and **arranged into a followable plan** (day-by-day sequence and/or mapped route). Everything else the sampled products carry — discovery layers, booking import, collaboration, budgets, offline packs, alerts, AI drafting — is standard mature capability layered on that core, not what makes the product a trip planner. The Type sits between discovery (which ends in a shortlist) and booking (which ends in a transaction): the planner's loop ends in a plan that is carried and lived.
