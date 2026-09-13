# Research Notes — Campground Booking Platform

Research date: 2026-09-06
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Campground Booking Platform actually is as an Application Type: who uses it, what objects exist inside it (campground, site, availability, booking), how the camper-side and operator-side surfaces work, and where its boundaries lie with the neighboring §26 travel Types (Hotel/Vacation Rental/Hostel booking, OTA, Travel Review) and with the §17 operator-side Type (Campground / RV Park Management).

## Initial Boundary (hypothesis before research)

- A camper/traveler-facing platform for discovering and reserving overnight stays at campgrounds and RV parks: tent sites, RV sites (hookup tiers), cabins, glamping structures, group sites.
- Demand-side surface (search → book), in contrast to Campground / RV Park Management (operator-side operations).
- Closest confusions: Vacation Rental Marketplace (private homes vs campground site inventory), Hotel Search / Booking Platform (same demand-side shape, different inventory domain), OTA (cross-vertical vs campground-specific), Directory/Listing (no transacted booking), Campground/RV Park Management (same objects, other side of the transaction).

## Research Questions

1. What are the core objects: campground property, site, site type, availability, booking?
2. How does the search → book loop work, and what filters are camping-specific (hookups, RV length, tent/RV/cabin categories)?
3. How is availability modeled (per-site vs per-site-type; calendar granularity)?
4. What does a booking contain (dates × site/type × party × equipment) and what lifecycle does it have (confirm, modify, cancel, refund)?
5. How do payments and fees work (pay-in-full vs deposit; platform booking fee vs commission; who is merchant of record)?
6. What does the supply side of the platform look like (host/operator portal, calendar sync, PMS integrations) — and where does it stop being "booking platform" and become "campground management system"?
7. What discovery content exists (photos, reviews, maps, editorial, alerts)?
8. How do agency-run public-land platforms differ from private marketplaces?
9. Boundary: remove-tests vs Vacation Rental Marketplace, Hotel Booking, OTA, Directory, operator management.

## Representative Products

| Product | Role in sample | Evidence level reached |
|---|---|---|
| Hipcamp | open private-land + public-land marketplace ("Airbnb-for-camping" philosophy) | A — homepage, campground listing page (Upper Pines), host page (all fetched) |
| Campspot (marketplace side) | professional campground/resort marketplace fed by the vendor's own operator software | A — homepage + full FAQ page (fetched); software.campspot.com fetched for boundary evidence |
| Reserve America (Aspira) | agency-run booking portal for government/public campgrounds | A for site surface (homepage fetched); help center is a JS app (aspiraconnect.service-now.com) — not readable; rest is positioning-level |
| Recreation.gov | government public-lands reservation portal | title-only evidence ("Camping, Cabins, RVs, Permits, Passes & More"); SPA — not usable beyond positioning |
| The Dyrt / Pitchup / KOA | content-first discovery, UK/EU aggregator, franchise-native platform | excluded — fetches blocked (406/timeout, 403 ×2, 403) |

Sample rationale: two poles of supply philosophy (open marketplace of private land vs professional-operator inventory), the agency/government tier, and operator-side boundary evidence via Campspot Software. The content-first and franchise-native poles could not be documented (blocked) — noted in Uncertainties.

## Sources

Fetched successfully (2026-09-06):

- Hipcamp homepage — https://www.hipcamp.com/en-US
- Hipcamp listing page (Upper Pines Campground, Yosemite) — https://www.hipcamp.com/en-US/campground/united-states/california/upper-pines-campground-5pzxcgvl
- Hipcamp host page — https://www.hipcamp.com/en-US/host
- Campspot marketplace homepage — https://www.campspot.com/
- Campspot FAQ — https://www.campspot.com/about/faq
- Campspot Software (operator side) — https://software.campspot.com/
- Reserve America homepage — https://www.reserveamerica.com/

Attempted, failed (per network-restriction rule, abandoned after 1–2 failures):

- Hipcamp camper help center — https://www.hipcamp.com/en-US/help (404), https://help.hipcamp.com (transport error), https://support.hipcamp.com/hc/... (transport error) → Hipcamp evidence is product-page level; no camper-policy claims made for Hipcamp
- The Dyrt — https://thedyrt.com/help (406), https://thedyrt.zendesk.com (timeout) → excluded
- Pitchup — https://www.pitchup.com/help/ (403), https://www.pitchup.com/ (403) → excluded
- KOA — https://koa.com/ (403) → excluded
- Recreation.gov — https://www.recreation.gov/help (SPA shell twice) → positioning-only
- Reserve America help center — https://aspiraconnect.service-now.com/csp (JS shell) → surface evidence only

## Product Observations

### Product A — Hipcamp (evidence layer A unless noted)

Camper side (homepage + listing page):

- Search inputs: destination, dates, site type, guest count. Also "roadtrip planner" and a "search near me" entry.
- Homepage organizes land as "over 500,000 iconic public lands, well-equipped RV resorts, and private sites" [marketing figure — product-specific, L3]; land sources include aggregated public lands (map layers for national park system, national forests, BLM) and private hosts.
- Listing page anatomy (observed on a public campground listing): breadcrumb location taxonomy (Explore → country → state → park → campground); rating (e.g. "97%") + review count; "240 sites · RV, Tent" [site inventory summary]; photo set; long property description including per-night price ("costs $26 per night"); "What this place offers" amenity list (Campfire allowed, Pets allowed, No showers, Toilets, Potable water, Picnic tables, Sewer hookups, No electric hookups); "Add dates" booking entry; "Available campgrounds nearby"; availability-alert prompt ("Scanning sold-out campgrounds… Get notified the moment … becomes available" — marketing claim, product-specific); reviews annotated with stay context (equipment: "Tent", "18 ft travel trailer", pets, month); "Suggest edits to improve this listing" (community-maintained listing data); filters exposed in URLs (accommodations=tents / rv-motorhomes / vehicles; land-highlight tags like single_private_site, creature_comforts).
- Availability alerts for sold-out campgrounds ("Free availability alerts — Snag sold-out campsites").

Supply side (host page):

- "Become a Host" targets: family farms, nature preserves, RV parks, glamping resorts, established campgrounds; host types include a 100+ property RV resort network (i.e., professional operators) alongside single-site landowners.
- Listing creation free; "We only charge a commission on confirmed bookings. Your rate depends on your property type" (rate not stated on page — do not generalize).
- Host controls: "Control when you host, who you host, and how much to charge"; set availability, pricing, rules; booking management tools; instant messaging with guests and automated messages; review management; pricing tools ("auto-adapt for holidays and weekends"); professional photography program.
- Inventory interoperability: calendar syncing with Airbnb, VRBO, etc. "to avoid double bookings"; PMS integrations listed (Cloudbeds, ResNexus, RMS, Staylist, Newbook, Checkfront, Bedful, RezStream, RoverPass, ReservationKey, Firefly) — "from full-service PMS integrations to simple calendar syncing."
- Standards: campers must have access to a toilet (own or provided — "toilet policy"); Host Standards; camper community standards; local-regulation compliance guidance; included liability/property protection (figures product-specific, L3).

### Product B — Campspot Marketplace (evidence layer A: homepage + FAQ)

Camper side:

- Homepage: search = where / check-in / check-out / guests (adults, children, pets). "3,200+ campgrounds, book instantly" and "over 350K campsites" [product-specific figures]; "Free to use, no membership"; real-time availability; "Find your Campspot — Discover and book the best campgrounds, RV parks, cabins, glamping, and more."
- Ways to stay categories: Cabins & Lodging / RV Sites / Tent Sites (URL categories campsiteCategory=Lodging|RV Sites|Tent Sites).
- Long-term segment: monthly/seasonal ("a month, a season, or more").
- Promo codes and camping deals; Good Sam / Senior / Military discounts "offered on a park by park basis," sometimes via park promo codes entered at checkout.
- Multiple campsites in one transaction ("Add to Cart" and repeat).

Booking mechanics (FAQ, directly observed):

- "You must pay in full at the time of booking."
- "Payment is made directly to the park for your campground reservation. For this reason, refunds and cancellations … are handled by the park you booked with." → platform is not merchant of record for the site fee; a separate "Booking Fee" is charged by the platform ("helps run Campspot's platform"; "will appear as a separate charge from Campspot on your credit card statement"). Booking-fee refund rule: fully refundable if cancelled within 24 hours of booking; after that, refundable only if the campground reservation is fully refundable; not partially refundable. [Campspot-specific policy, L3]
- "Lock your site location" for a fee at some parks: guarantees the exact site chosen from the map; without it "your location may be switched to a comparable site within your selected campground." → two-level site model: exact site vs site-type/comparable assignment. [Campspot-specific fee, but the exact-vs-assigned model is a structural observation]
- Cancellation: "Cancellation policies … vary from park to park"; online self-service cancellation available "on a park-by-park basis"; otherwise contact the park (phone from confirmation email).
- Check-in/check-out times listed on the campground page.
- Camp/User Credit: funds held by the system after cancellations, usable per park policy; park-specific.
- Post-stay: "We also send an email after every stay allowing you to rate and review your experience."
- Account: My Account → Account Details / Payment Methods / Reservations / Saved locations; view upcoming and past trips.
- Optional weather protection add-on (partner product) purchased at booking time; not addable after booking.

Boundary evidence (software.campspot.com — operator side):

- Campspot Software: "campground management software" — Growth and Revenue (dynamic pricing engine, add-ons), Management and Operations ("front desk to housekeeping to the camp store"), Marketing (email, two-way texting), Guest Experience ("intuitive booking experience"), Integrations, Data and Reporting; serves "3,500 public and private parks" incl. enterprise/multi-park groups; marketplace described as "the largest campground-specific OTA."
- → The vendor operates both sides: operator PMS (management system) and camper marketplace (booking platform). The marketplace's real-time inventory comes from parks running the software.

### Product C — Reserve America / Aspira (surface evidence A; operations positioning-only)

- Homepage: "Camping & Campground Reservations Online"; Discover menu = Articles / Destinations (campground directory) / Hunting & Fishing; heavy editorial content (camping guides per state, recipes, trip ideas); "BOOK YOUR OUTDOOR ADVENTURE".
- Structure indicates an agency-model booking portal (public campgrounds operated by government agencies) with a content/discovery layer on top; actual booking flows are JS-driven and were not readable.
- Help center is a ServiceNow consumer service portal (JS shell) — not readable.
- Affiliate disclosure on homepage ("will receive a commission if you make a purchase using these links") — indicates affiliate/commercial layer distinct from the booking function.

### Recreation.gov (positioning-only)

- Title: "Recreation.gov - Camping, Cabins, RVs, Permits, Passes & More" — confirms scope beyond campgrounds (permits, passes, tours). No further claims; SPA not readable.

## Cross-product Comparison

| Dimension | Hipcamp | Campspot Marketplace | Reserve America |
|---|---|---|---|
| Primary surface | camper search/discovery + rich listing pages | camper search + booking engine on park inventory | agency booking portal + directory + editorial content |
| Supply model | open listing: private landowners + farms + campgrounds + RV resorts + aggregated public lands | professional campgrounds/resorts, largely running the vendor's own operator software | government/agency-operated public campgrounds |
| Inventory unit | listing = property with sites; types: tent / RV / vehicle / lodging / glamping | park with site-level availability; categories: Lodging / RV Sites / Tent Sites | campground with site types (positioning-level) |
| Site selection | property/site-level browsing; "Add dates" | exact site optional via paid "lock", otherwise comparable site assigned | not observed |
| Booking transaction | instant book; "Hipcamp handles all payments" (host page) | instant book; pay in full; booking fee separate from park payment | online reservation (payment at booking assumed; not verified) |
| Merchant of record | platform (commission on confirmed bookings; host payouts via "trusted payment system") | park for stay cost; platform for booking fee | agency/platform (not verified) |
| Cancellation / refund | host-defined rules + standards; specifics not verified (help center blocked) | park-defined policies; online cancellation park-by-park; booking-fee window (product-specific) | agency policy (not verified) |
| Reviews | star/percent ratings + review text with stay context (equipment, month) | post-stay review email; ratings on parks | not observed |
| Discovery extras | map layers (public lands), availability alerts, roadtrip planner, curated collections, community listing edits | long-term/monthly segment, promo codes, weather add-on, app | editorial articles, destination directory, hunting/fishing cross-sell |
| Account surfaces | camper account + host console | My Account (reservations, saved, payment methods) | sign-in (not readable) |

Stable across all observed products (B-layer cross-product commonality):

1. A searchable catalog of campground properties from many operators, entered via place + dates + stay type.
2. Property listings carrying site/space inventory with camping-specific semantics (site types; hookups/electric/sewer/water; pets; campfire; toilets/showers; RV compatibility).
3. Date-based availability for nightly stays; availability is the search constraint.
4. An online booking transaction binding camper × site (or site type) × date range, confirmed by payment.
5. A camper-side record of the reservation (confirmation email at minimum; account with trips where documented).
6. Cancellation/modification governed by operator-defined policy, surfaced through the platform.
7. Reviews/ratings tied to actual stays.
8. A supply-side surface where operators/hosts maintain listing, availability, and pricing (depth varies from "free listing + sync" to full console).

## Canonical Model

### L0 — Defining Invariant (deliberately small)

```text
Camper-facing platform over a multi-operator catalog of campground properties
└── each property listing carries bookable site/space inventory
    with camping-specific semantics and date-based availability
    └── camper-initiated booking transaction
        (site or site type × date range × party)
        confirmed online by payment
        └── persistent reservation record for the camper,
            conveyed to the operator
```

Three invariants:

1. **Searchable multi-operator campground catalog** — the demand-side discovery surface. Remove it and the product collapses into a single-property booking engine (the Hotel Booking Engine analog), not a platform.
2. **Bookable site/space inventory with camping semantics and date availability** — the unit of supply is a site/space at a campground property (tent site, RV site with hookup tier, cabin/glamping structure, group site), bookable per night/date. Remove it and the product is a directory or review site.
3. **Payment-confirmed online booking transaction with a persistent reservation record** — remove the transacted booking and it becomes a Directory/Listing or Travel Review Type.

Not in L0 (verified as common or variant, not defining): reviews, alerts, maps, editorial, fee mechanics, lock fees, insurance, apps, long-term stays, public-land aggregates.

Historical / market-sample check (§24 reasoning): early online campground reservation systems (Reserve America lineage, ~1990s onward) already exhibit all three invariants (searchable park catalog, dated site inventory, paid reservation) — the L0 holds for the older, agency-run generation, not just modern marketplaces. Phone/mail-era campground directories (Woodall's/Trailer Life lineage) do NOT satisfy invariant 3 — they belong to Directory/Listing, which is exactly the boundary. Older/regional variants used request-based or phone-finalized flows in places; the canonical constant is the online transacted reservation, which is what distinguishes "booking platform" from "directory" in the directory taxonomy itself.

### L1 — Common Mature Structure

- Camper accounts with trip history (upcoming/past reservations) and saved/favorite places.
- Reviews and ratings anchored to completed stays, often annotated with stay context (equipment, party).
- Media-rich listings: photos, amenities list, location maps, descriptive content.
- Camping-specific filters: stay type (tent / RV / cabin-lodging / glamping), hookups (electric/water/sewer), RV size/equipment compatibility, pets, campfires, waterfront/terrain attributes.
- Availability alerts / sold-out watch.
- Cancellation and modification flows with operator-defined policies surfaced at booking.
- Platform fee layer (booking fee or commission) distinct from the operator's rate.
- Discounts/promo codes (often park-by-park).
- Mobile apps.
- Long-term/monthly/seasonal stays as a distinct search/booking segment.
- Supply-side portal: listing management, availability/pricing control, guest messaging, calendar sync to external channels; PMS integrations for professional operators.
- Optional protection products (weather guarantees, insurance).

### L2 — Variant / Optional Structure

- Supply philosophy: open marketplace (any landowner can list) vs curated professional-operator inventory vs agency/government-run catalog vs single-brand/franchise network.
- Commercial model: commission on confirmed bookings (platform merchant-of-record role) vs park-direct payment + separate platform booking fee vs agency-collected public fees.
- Site-selection model: exact-site choice (sometimes with paid lock) vs site-type booking with operator assignment to a comparable site.
- Discovery posture: content/editorial-led vs map-led vs deal-led.
- Inventory breadth: campground-only vs aggregated public lands vs mixed lodging.
- Region: the researched sample is US/Canada-centric; UK/European aggregator and request-based models exist (not documented — blocked) — kept qualitative.
- Adjacent mechanics on public-land platforms (permits, passes, tours, lotteries) — signaled by Recreation.gov title only; not verified; treated as adjacent-Type mechanics, not part of this Type.

### L3 — Vendor-specific (stays here, not in final doc)

- Hipcamp: "500,000+ listings" and "18 million campers in 2025" figures; $1M liability / $10K property protection figures; "scanning sold-out campgrounds every 15 seconds"; land-highlight tags; community "suggest edits"; professional photography program; toilet policy; commission rate by property type; host standards documents.
- Campspot: "3,200+ campgrounds / 350K sites" figures; 24-hour booking-fee refund rule; lock fee; Camp/User Credit mechanics; Sensible Weather partnership; Good Sam/Senior/Military promo-code handling; payment goes directly to parks (agency-of-nothing model: platform fee vs park fee separation).
- Reserve America / Aspira: ServiceNow-based help portal; hunting & fishing cross-sell; affiliate disclosure.
- Recreation.gov: permits/passes/tours scope (title-only).
- Campspot Software (sibling product): dynamic pricing engine, front desk/housekeeping/camp-store operations, marketing tools — these belong to Campground / RV Park Management, not to the booking platform.

## Boundary Findings

| Neighboring Type | Relationship | Remove-test / distinction |
|---|---|---|
| Campground / RV Park Management (§17) | sharpest seam; same objects (site, reservation), opposite side | Remove multi-camper discovery + multi-operator search and keep front-desk/housekeeping/revenue/camp-store operations → management system. Keep camper-side discovery/booking, drop operator operations → booking platform. Vendors straddle: Campspot sells both ("software" vs "marketplace" sites); marketplace inventory comes from the operator side. |
| Vacation Rental Marketplace | adjacent; same demand-side shape | Inventory unit differs: site/space at a campground property with nightly site availability and equipment semantics vs an entire private home. Glamping structures are the overlap zone. |
| Hotel Search / Booking Platform | structural sibling (demand-side lodging booking) | Same loop, different inventory domain and semantics (rooms vs sites/hookups/equipment). The directory partitions these by inventory domain; consistent design, not a duplicate. |
| Online Travel Agency (OTA) | adjacent, broader | OTA aggregates across lodging (and travel) verticals; this Type is campground-specific supply. Campspot self-describes as "largest campground-specific OTA" — the word "OTA" is used for the channel, the specialization is the Type line. |
| Directory / Listings Platform; Travel Review Platform | boundary by absence | Remove the transacted booking (and date availability) → directory/review product (phone/mail-era campground directories, review-first discovery). This is the historical edge of the Type. |
| Tour & Activity Marketplace | adjacent | Unit is an experience/activity, not an overnight site stay. |
| Hostel Booking Platform | structural sibling | Same demand-side shape, hostel-bed inventory domain. |
| Hotel Booking Engine | adjacent | Single-property booking surface; no multi-operator discovery. |

Taxonomy observation (not an error): the directory splits demand-side lodging booking into inventory-domain siblings (hotel / hostel / vacation rental / campground). Research supports this partition: the loop is shared, the inventory semantics and operator ecosystem differ. No alias/variant problem found for this leaf.

## Uncertainties

1. Hipcamp camper-side policies (refunds, cancellations, fees from the camper perspective) could not be verified — help center blocked. Only host-side facts observed. No camper-policy claims are made in the final document.
2. The Dyrt (content-first discovery pole), Pitchup (UK/EU aggregator), KOA (franchise-native) all blocked — the sample's geographic and philosophical breadth is narrower than ideal. Claims about regional/request-based models are kept qualitative or omitted.
3. Recreation.gov and Reserve America booking internals (payment, cancellation, lotteries) not readable — public-land tier documented at surface level only; no operational claims.
4. Exact fee percentages, refund windows, minimum-stay rules are product-specific or unverified; final document states fee and policy structures qualitatively, with one product-specific exception (Campspot booking-fee window) kept in these notes only.
5. "Payment-confirmed booking" as an invariant: all observed products transact payment at booking; some regional/older products may finalize by request/phone. If such a product is a "booking platform," the invariant would soften to "reservation transaction confirmed online." Sample evidence does not settle this; final doc uses "payment-confirmed" as the common mature form and notes the boundary via the directory line.

## Final Synthesis

A Campground Booking Platform is the demand-side sibling of the campground industry's operator systems: a camper-facing platform that aggregates many operators' campground properties into a searchable catalog, models each property's sites/spaces as dated, camping-specific inventory, and completes the camper's stay as a payment-confirmed online booking that both the camper (trip record) and the operator (reservation) can act on. Around that core, mature products add the camping-specific discovery layer (filters for hookups/equipment/stay types, maps, reviews from real stays, availability alerts), the policy layer (operator-defined cancellation, platform fees, discounts), and a supply-side portal that connects the platform to operator reality (listing management, calendar sync, PMS integrations). The Type's edges are exact: without booking it is a directory/review surface; without multi-operator discovery it is a booking engine; without site/equipment semantics it is a generic lodging OTA; without the camper surface it is Campground / RV Park Management.
