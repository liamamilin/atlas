# Research Notes — Campground / RV Park Management

## Research Goal

Understand what operator-side Campground / RV Park Management software actually is as an Application Type: who uses it, what objects exist inside it (site, reservation, stay, account), how the operator's daily work flows through it, and where its boundaries lie with the neighboring Types — especially the already-processed sibling **Campground Booking Platform** (demand side), **Hotel PMS**, **Marina Management**, and the false-friend **Camp Management System**.

## Initial Boundary

- Hypothesis: this is the **operator-side** system of record for running a campground or RV park — the software the park staff work in daily — as opposed to the camper-facing booking platform (sibling leaf, processed 2026-09-06, which explicitly held this boundary: "products without the camper-facing surface are campground management systems").
- Closest confusions: Campground Booking Platform (same objects, other side of the transaction); Hotel PMS (same skeleton — guest/reservation/unit/stay/folio — different unit semantics); Marina Management (same shape over water); HOA/Community Association Management (long-stay/annual sites); Self-storage Management (off-season RV storage); Camp Management System (namesake only — children's program camps; sibling research already recorded "shares nothing structural beyond the word camp").
- The sibling booking-platform research also established: on professional platforms, the booking platform reads real-time availability from the operator's campground management system and writes reservations back into it — i.e., the management system is the **system of record for site inventory**.

## Research Questions

1. What is the core object model: site/space inventory, site types, reservation, stay, account/folio?
2. How does the operator's daily loop work: arrivals, check-in, on-site, departures, check-out, site turnover?
3. What camping-specific semantics exist (hookups, rig size/length limits, vehicle/pet counts, site map)?
4. How are rates structured (seasonal, site-type, extra-person/vehicle, add-ons) and how do charges settle?
5. How do long-term stays work (monthly/seasonal/annual sites, recurring billing, metered utilities)?
6. How does the operator side connect to online booking (booking engine, channel manager, pending-approval)?
7. What does the front desk actually do in the software (walk-ins, grid drag-drop, POS, receipts)?
8. Where are the boundaries with Hotel PMS, Marina Management, booking platforms, and community-association software?

## Representative Products

| Product | Position / philosophy | Evidence layer |
|---|---|---|
| **Campspot** (software.campspot.com) | Modern US/Canada cloud platform for professional private campgrounds, RV resorts, public parks, franchises, multi-park groups (3,500+ parks claimed); revenue-management-forward | A — product pages (root, Management & Operations, Growth & Revenue) + KB structure (support.campspot.com, partially gated) |
| **RMS Cloud** (rmscloud.com) | Global cloud-native hospitality PMS (6,000+ properties, 70+ countries) with a dedicated Campgrounds & RV Parks solution; AU holiday-park heritage; multi-vertical (hotels→campgrounds→marinas) | A — root, campground solution page, Help Center (Zendesk, Tier-1 structure) |
| **Campground Master** (campgroundmaster.com, Cottonwood Software) | Desktop Windows reservation software for campgrounds/RV parks; one-time license, no internet required; full manual online; the "wall chart and paper forms" successor — historical/platform-native check | A — root, features, maps, online reservations, uses pages (all fetched) |
| Newbook ("Storable Newbook") | AU-origin campground/holiday-park management, now under Storable | Context only — root site transport-error ×2 (abandoned); known to the market via RMS's own comparison list |
| ResNexus | Multi-vertical reservation system serving campgrounds among others | Context only — 403 ×1 (abandoned) |

Sample rationale: one modern revenue-forward cloud platform (Campspot), one global multi-vertical PMS with a campground solution (RMS), one desktop-era single-park product with a complete public manual (Campground Master). This spans customer tier (SMB single park → enterprise multi-park), product philosophy (campground-native vs hospitality-platform-with-campground-solution vs desktop utility), and era (2001-era desktop → current cloud), which supports the historical/market-sample check.

## Sources

- Campspot — https://software.campspot.com/ ; https://software.campspot.com/features/management-and-operations/ ; https://software.campspot.com/features/growth-and-revenue/ ; https://support.campspot.com/ (+ /get-started, /campground-setup-page) — fetched 2026-09-06
- RMS Cloud — https://www.rmscloud.com/ ; https://www.rmscloud.com/solutions/campground-management-software ; https://support.rmscloud.com/hc/en-gb — fetched 2026-09-06
- Campground Master — http://www.campgroundmaster.com/ (+ features.html, maps.html, online.html, quickstart.html, uses.html) — fetched 2026-09-06
- Sibling research: research/campground-booking-platform.md, applications/campground-booking-platform.md (boundary context; Campspot operator-side pages already fetched there)
- Failed/blocked: newbook.com.au (transport error ×2 — abandoned), resnexus.com (403 — abandoned), Campspot KB article bodies (gated behind "full access"), CampLife (JS-empty root — not pursued further)

## Product Observations

### Campspot (Layer A unless noted)

Key observations:

- Positioning: "campground management software … streamline operations, grow revenue"; admin login at reservation.campspot.com/admin/login; serves private campgrounds, public parks, enterprise/multi-park groups, franchises (US/Canada).
- Platform modules: Growth and Revenue / Management and Operations / Marketing / Guest Experience / Integrations / Data and Reporting.
- Management & Operations features: **Drag & Drop Grid Functionality** ("instantly extend, shorten, or relocate reservations with a simple click-and-drag"); analytics/reporting (dashboards, reservation activity feed to BI tools, scheduled reports); text messaging (one-way SMS; two-way via SimpleTexting integration); third-party integrations (Mailchimp etc.); **Guest Self Service** (Online Check-in, online Cancellations, Date Changes — "empower guests to manage their own reservation"); **Point-of-Sale Management** ("from firewood to golf-cart rentals, guests can add amenities to their reservations … daily or hourly rentals, or items from your camp store"); housekeeping dashboard; **Auto-Charge Balance Rule**; **recurring guest billing**; user-created business rules; gift card management; cash and accrual accounting.
- Growth & Revenue features: **Dynamic Pricing** ("business rules engine … adjusts rates in real time based on occupancy, demand, and booking lead time"); **Automatic Grid Optimization** ("algorithm shifts reservations in real time to fill up your campground, so you don't have to play Tetris"); **Lock Site** ("optional lock fee gives the guest the option to lock in a specific site for a fee" — implies default assignment is site-type/comparable-site, with exact site as a paid option); **Reservation Add-Ons** (firewood, golf carts, camp store items during booking); **Online Marketplace** (Campspot.com OTA — "bookings flow directly into your existing Campspot inventory with no separate system to reconcile"); Accelerator (partner placements on the park's consumer booking site).
- KB structure (public layer): Get Started (park setup basics), **Campground Setup Page** ("Accounting, Site Setup, Base Pricing, and more"; Properties → Form Lists; **Site Amenities** forms), Integrations ("3rd Party Booking Services"), Campspot Analytics (Performance Planner), Request Forms (Marketplace Updates, Admin Site Update Requests). Most operational articles are gated ("Not seeing all content? … gain full access").
- Vendor figures (L3, not for final doc): 70.3% dynamic-pricing revenue delta, $9.1M/$14M/$22.9M/$43.6M/$89M 2025 figures, 10M marketplace sessions, 3,500+ parks.

### RMS Cloud (Layer A unless noted)

Key observations:

- Positioning: cloud-native PMS "trusted by over 6,000 hotels, motels, holiday parks, campgrounds, and serviced apartments across 70+ countries"; dedicated **Campgrounds and RV Parks** solution page.
- Campground solution page capabilities: **Guest portal** (guests view/manage/pay all reservations and extras; self check-in and check-out; two-way chat; rebooking); **Housekeeping and maintenance** (job lists on a staff portal; cleaning schedules customized by room type and duration of stay; task assignment by skill; audit trail; built-in maintenance hub); **Built-in channel manager** ("handle all your OTA distribution on one platform … decide how your inventory is sold across channels"); **Interactive maps** ("let guests pick their exact spot, check availability, and book confidently"; real-time availability; multi-booking; mobile-optimized); **Meter reads** ("capture and track utility usage (gas, water, electricity) accurately per guest or unit; automate oncharging"); **Embedded payments** (upfront or instalments; flexible payment options at every stage).
- FAQ (Layer A): real-time updates across platforms prevent overbookings; dynamic pricing adjusts rates by demand/occupancy; **automated site assignments based on preferences and availability**; multi-campground centralized control; contactless check-ins.
- Case studies (Layer A, qualitative): Warburton Holiday Park — "digitises annual agreements", manages "over 80 long-stay residents in one platform"; Twin Creeks — marina + hospitality on one platform; BIG4 franchise network; Barwon Coast — interactive maps for site choice; Beachport — "Sadie" AI call handling.
- Help Center (Tier-1 structure): categories — Property Management; Rates & Revenue Management; Booking Engine & Distribution; Guest Experience & Engagement; Reporting & Finance; RMS Pay & Payment Gateways; Modules & Integrations; Security. FAQ highlights: **Smart Search** ("quickly look up existing Guest Profiles"); **Daily Procedures Guide for Hotels, Motels and Parks**; Frequently Used Reports; Keyboard Shortcuts. Billing notices reference **"Active Bookable Areas"** as the inventory/billing unit and per-user licences. Popular articles: Automated Invoicing and Payments, Direct Debit (GoCardless), **Advanced Payment Schedules**.

### Campground Master (Layer A — richest operational detail; historical sample)

Key observations:

- Positioning: "Reservation Software for RV Parks and Campgrounds"; desktop Windows; one-time $795 license, no monthly fees; "No internet access required for the basic functionality"; optional networking/remote access; explicit predecessor framing: "If you're still using a wall chart and paper forms, we can help you make the transition."
- Core operations: "Speed up check-ins and check-outs, completed with a printed receipt in just a few clicks"; "Eliminate booking mistakes — no more lost or duplicate reservations"; secure log-ins with **operator/date/time tracking of all transactions**; waiting lists; "Avoid missing charges for extras like **additional people or vehicles, late departures** … automatically calculated"; custom transaction reports + QuickBooks export; **"1-click Monthly Billing"** and **"Electric Meter batch entry & auto-calculation"**; batch email invoices/notices; "Walk-ins can be handled with just a few clicks"; reports: occupancy grid, **Arrivals list, Departures list, On-Site, Payments Due**.
- **Map model** (maps.html): map = any background image + interactive per-site "indicators" (circles/rectangles/fills); **status colors: Available (white), Reserved (yellow), Occupied (green), Occupied But Due Out Today (light green)**; optional reservation-status coloring showing "group reservations … monthlies, who has not paid in full, guaranteed reservations"; right-click menu; **double-click an open site to make a new reservation**; hot-spots to drill from overview map to zoomed sections. Customer quote: "I love being able to print it out at the end of the day to show next day's availability of sites — we were doing this by hand everyday!!"
- **Online reservations** (online.html): 2-way real-time integration with an external booking engine (Hercules/Leisure Interactive): "availability shown to customers … will always match the availability in Campground Master, eliminating the possibility of double-booking"; online reservations imported automatically, "optionally tagged as 'pending approval' until you review them"; operator "can change or reject online-submitted reservations"; DIY alternatives: web reservation-form data retrieval, **"vacancy grid" web pages** generated from availability, **iCal export/import**.
- **Other uses** (uses.html — boundary evidence): same product reconfigured for motels, boat slips/marinas, mobile-home lots, flea-market booths, storage, kennels. Reveals the campground data model: **"Rig size" field for RVs** (renamed "Boat size" for marinas) with **maximum length restrictions on sites** ("keeps you from booking too large of a boat"); guest info includes "vehicle tags, number of adults, children, pets"; default site attribute is **"Sewer hookup"** (renamable); sites have length/width fields; per-site days-of-week availability; **monthly or annual rentals for sites**; metered electricity/water/gas billing; Payments Due reports; statements/contracts/delinquent notices. Payment-timing note: **"most RV parks put in charges and take payment up front"** vs hotel pay-at-checkout (checkout payment is the option, not the norm). Housekeeping report exists for rooms (departures/arrivals/back-to-back).

## Cross-product Comparison

| Dimension | Campspot | RMS Cloud | Campground Master | Verdict |
|---|---|---|---|---|
| Site/space inventory as system of record | Site Setup in park setup; grid | "Bookable Areas"; interactive maps | Sites with types, attributes, sizes, map indicators | **Core (B)** |
| Camping-specific site semantics | Site amenities forms; add-ons | Site choice by amenities; meter reads | Hookups (sewer default), rig size, length limits, vehicle/pet counts | **Core (B)** |
| Reservation binds guest × site (or site type) × dates | Drag & drop grid | Automated site assignment; maps | Double-click open site → reservation; no duplicates | **Core (B)** |
| Operator-advanced stay lifecycle (check-in/out, on-site) | Online check-in + front desk; housekeeping dashboard | Self check-in/out; front desk ops; housekeeping | Check-ins/outs with receipts; Arrivals/Departures/On-Site lists | **Core (B)** |
| Site states visible (available/reserved/occupied/due-out) | Grid | Real-time availability on maps | Explicit color states incl. "Occupied But Due Out Today" | **Core (B)** (state concept; exact labels product-specific) |
| Stay account: charges accumulate → settlement | Auto-charge balance rule; cash/accrual accounting; gift cards | Embedded payments; payment schedules; invoicing | Receipts, payments due, transaction tracking w/ operator attribution | **Core (B)** |
| Extras beyond the nightly rate | Add-ons (firewood, golf carts, store) | Extras in portal | Extra people/vehicles, late departures auto-calculated; POS | **Core (B)** |
| Site map / drag-drop grid as primary surface | Drag & drop grid | Interactive maps (guest + operator) | Map view with status indicators | **Common (B)** — signature surface, not definitional |
| Guest profiles & history | (implied; KB gated) | Smart Search on guest profiles | "Saves all customer information for easy recall on return visits" | **Common (B)** |
| Rate configuration (seasons, site types, min stays) | Base Pricing in setup; dynamic pricing | Rates & Revenue Management category | Rates by site type/size; day-of-week availability | **Common (B)** |
| Online booking integration | Marketplace bookings flow into inventory; 3rd-party booking services | Built-in channel manager; booking engine | 2-way real-time sync w/ external engine; iCal/vacancy-grid DIY | **Common (B)** |
| Guest self-service | Online check-in, cancellations, date changes | Guest portal (manage/pay/chat/rebook) | — (era) | **Common (B)** |
| POS / camp store | POS management | POS module | POS with barcodes, store inventory | **Common (B)** |
| Housekeeping / site turnover | Housekeeping dashboard | Housekeeping module (schedules by stay duration) | Housekeeping report (rooms) | **Common (B)** — lighter than hotel housekeeping |
| Waiting lists | (not observed) | (not observed) | Waiting lists | **Optional (A, single product)** |
| Long-stay machinery (monthly/annual, recurring billing) | Recurring guest billing; auto-charge | Annual agreements; long-stay residents; payment schedules; direct debit | 1-click Monthly Billing; monthly/annual rentals; statements | **Common (B)** — campground-distinctive emphasis |
| Metered utilities | (not observed) | Meter reads (gas/water/electric) + oncharging | Electric meter batch entry & auto-calculation | **Common (B)** — long-stay-linked |
| Dynamic pricing / revenue management | Dynamic Pricing engine | Revenue management module | — (era) | **Optional/Variant (B)** — modern professional segment |
| Grid optimization algorithms | Automatic Grid Optimization | (not observed) | — | **Vendor-leaning (A, single product)** |
| Lock-site fee / exact-site assignment model | Lock Site (fee for exact site) | Guests pick exact spot on maps | Book specific site from map | **Variant (B)** — assignment model differs by product |
| Multi-park / centralized control | Enterprise/multi-park groups | Multi-property; centralized control | Networking (multi-terminal, one park) | **Common (B)** at enterprise tier |
| Public/agency parks | Public Parks segment | Agency parks (Barwon Coast, Reflections) | — | **Variant (B)** |
| Deployment | Cloud SaaS | Cloud SaaS | Desktop, offline-first, one-time license | **Variant (B)** — era/philosophy |
| Adjacent-property bundling (marina/motel/storage/mobile-home) | — | Marinas (Twin Creeks); hotels/motels | Explicit multi-use reconfiguration | **Variant (B)** |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The operator-side system of record for running a campground/RV park. Four properties; remove any one and the product is no longer a campground management system:

1. **Site/space inventory** — the park modeled as individually identified rentable sites/spaces (RV sites, tent sites, cabins, group areas), each typed and attributed in camping terms (hookups, size/rig fit, amenities). This is what makes the system *of record* for the property.
2. **Reservation** — a guest's dated occupancy claim on a specific site or a site type, held against the inventory; the same site cannot be double-booked.
3. **Operator-advanced stay lifecycle** — the reservation is worked by park staff through arrival/check-in → on-site occupancy → departure/check-out, with site state (available / reserved / occupied / due-out) tracking reality; this operating loop is what distinguishes management from a mere booking engine.
4. **Stay account** — charges accumulate on the guest's stay (site rate by season/type, extras, store items) and are settled by payment, producing receipts/statements.

### L1 — Common Mature Structure

- Site map / drag-drop grid as the primary operating surface (occupancy at a glance, click/drag to book, move, extend)
- Daily operations lists: arrivals, departures, on-site, payments due
- Guest profiles with history (returning guests; party size, vehicles, pets)
- Rate configuration: seasonal rates by site type, extra-person/vehicle fees, minimum stays, day-of-week availability
- Online booking integration: booking engine and/or channel manager with two-way availability sync; optional pending-approval control
- Guest self-service: online check-in, self-service edits/cancellations, portal payments
- POS / camp store: counter sales, add-ons attached to reservations, gift cards
- Housekeeping / site-turnover task tracking (lighter than hotel housekeeping)
- Integrated payments: card processing, deposits, payment schedules
- Reporting/analytics: occupancy, revenue, payments due; dashboards
- Guest communications: email/SMS, batch notices
- Waiting lists (observed in the historical sample; likely common but unverified across the modern sample)
- Multi-park management at enterprise tier

### L2 — Variant / Optional Structure

- **Long-stay machinery** (monthly/seasonal/annual sites): recurring/monthly billing cycles, statements/contracts/delinquency notices, metered utilities with oncharging, annual agreements, long-stay resident management. Emphasis varies by region/segment (AU/NZ holiday parks vs US transient RV resorts).
- **Revenue management**: dynamic pricing engines, grid-optimization algorithms, lock-site fees — modern professional segment.
- **Site-assignment model**: exact-site selection (map pick, or paid lock) vs site-type booking with comparable-site assignment.
- **Customer segment**: private campground/RV resort; public/agency park; franchise networks; multi-park investment groups.
- **Regional shape**: AU/NZ holiday parks (annuals, on-site caravans, long-stay residents) vs North American RV resorts/campgrounds (transient + seasonal) — inferred from sample, kept qualitative.
- **Deployment**: cloud SaaS vs desktop/offline-first with optional networking.
- **Adjacent-property bundling**: marina slips, motel rooms, storage bays, mobile-home lots managed in the same product.
- **Membership/loyalty/gift-card programs**; trust/owner accounting (multi-vertical PMS).

### L3 — Vendor-specific (Research Notes only)

- Campspot: Lock Site fee; Accelerator partner placements; Campspot Marketplace; "The Data Dig"; certification program; CardPointe/Fiserv support; SimpleTexting; revenue/percentage figures; "play Tetris" framing.
- RMS: "Bookable Areas" billing unit; Sadie AI; RMS Pay; GoCardless direct debit; RBA surcharging-ban guide; user-licence billing; trust accounting.
- Campground Master: Hercules/Leisure Interactive 2-way integration; vacancy-grid web pages; iCal import/export; $795 one-time license; QuickBooks export; F1 manual; exact status-color names (Available/Reserved/Occupied/Occupied But Due Out Today).
- Campspot KB gating; Newbook unreachability (see Uncertainties).

## Historical / Market-Sample Check

- **Campground Master** (desktop, 2001–2025, offline-first, one-time license) satisfies the L0 fully: site inventory with map, reservations, check-in/out, folio/settlement, POS, monthly billing, meters. The L0 is therefore not a cloud-era artifact.
- The product's own framing — successor to the **wall chart and paper forms** — shows the L0 digitizes the pre-software campground office (wall map + reservation rack + ledger), not a modern SaaS pattern.
- Regional check: RMS's AU/NZ holiday-park shape (annual agreements, long-stay residents, metered utilities) and Campspot's North American shape (transient + seasonal, dynamic pricing) both fit the same L0; the differences land in L2.
- Multi-use check: the same product reconfigured for motels/marinas/storage still satisfies L0 with renamed vocabulary — confirming L0 is about *rentable-space operations*, with campground semantics carried by the attribute vocabulary (hookups, rigs) and the stay mix. The Type is defined by the campground operation, not by vendor packaging.

## Vendor-specific Findings

See L3 above. Notable: Campspot is the clearest case of a vendor straddling both sides of the sibling boundary (operator software + camper-facing marketplace) — used as boundary evidence, not as a Type property.

## Boundary Findings

1. **vs Campground Booking Platform** (sibling, processed): sharpest seam. The booking platform serves **campers choosing among many operators** (multi-operator catalog, discovery, camper-side booking); the management system serves **the operator running one property** (site inventory of record, desk operations, folio, daily loop). Test: who works in the software day to day. Remove the operator's daily operations and inventory-of-record role → booking engine; add the camper-facing multi-operator surface → booking platform. Vendors straddle (Campspot ships both; bookings flow from its marketplace directly into operator inventory).
2. **vs Hotel PMS**: same skeleton (guest / reservation / unit / stay / folio / unit status). Differences: the unit is a **piece of land/pitch** with camping attributes (hookups, rig length fit) rather than a room; guests bring their own accommodation, so there is no daily room-turnover/housekeeping cycle of hotel intensity; stays skew longer (weekly/monthly/seasonal/annual) and long-stay machinery (monthly billing cycles, metered utilities, annual agreements) is a first-class emphasis; payment timing skews **up-front at check-in** (per Campground Master: "most RV parks put in charges and take payment up front") vs hotel pay-at-checkout norm; camp store/POS is a standard companion. Same genus, different species — Hotel PMS vendors (RMS) serve campgrounds with the same platform, which is exactly why the campground-specific semantics must carry the boundary.
3. **vs Marina Management** (§18): same shape over water (slips as sites, transient docking + long-term leases, size-fit constraints). Campground Master explicitly reuses rig-size/site-type fields for boats; RMS runs marinas on the same platform. Distinct Type because watercraft operations (berthing, haul-out, dockside services) differ; products straddle.
4. **vs HOA / Community Association Management**: parks with annual/seasonal sites and long-stay residents resemble community associations (annual agreements, recurring billing, delinquency). Boundary: the campground Type centers on **transient nightly/weekly stays plus site operations**; long-stay is a variant emphasis, not the center.
5. **vs Self-storage Management**: off-season RV storage bays share the "individually identified space + monthly billing" pattern, but storage has no nightly stay lifecycle, no arrival/departure loop, no per-stay folio.
6. **vs Camp Management System**: namesake only — children's program camps (sessions, bunks, health center) share no structural objects with campground operations (confirmed by sibling research).
7. **vs Hotel Booking Engine / Channel Manager**: distribution capability, not the operator's system of record; campground systems integrate or embed them (RMS built-in channel manager; Campground Master's external-engine integration; Campspot marketplace write-back).
8. **vs Event / Venue Management**: group areas and pavilions exist as bookable spaces, but events are not the structural center.

## Uncertainties

- **Campspot operational detail**: most KB articles are gated; no precise Campspot defaults/rules (cancellation windows, fee amounts, state names) are asserted anywhere in the final document.
- **Newbook**: unreachable (transport error ×2); treated as market context only, no claims.
- **ResNexus**: 403; not used.
- **Site-state vocabulary**: only Campground Master's color states were directly observed; the *concept* of site states is cross-product (grid/maps/real-time availability) but exact labels are product-specific — final doc states states conceptually.
- **Housekeeping depth for sites**: RMS has a full housekeeping module; Campspot mentions a housekeeping dashboard; Campground Master has a housekeeping report (rooms). Depth for open-air sites (vs cabins) is not directly evidenced — kept qualitative.
- **Waiting lists**: observed only in Campground Master — marked single-product/optional.
- **European touring-park shape**: not directly sampled; excluded from claims.
- **Metered utilities**: two products (RMS, Campground Master) — treated as common-but-variant (long-stay-linked), not core.

## Final Synthesis

A Campground / RV Park Management system is the **operator-side system of record for running a campground or RV park**: it holds the park as an inventory of individually identified, camping-typed sites and spaces; binds guest reservations to that inventory (site or site type × date range, no double-booking); advances each stay through an operator-worked lifecycle (check-in → on-site → check-out) reflected in site states; and accumulates each stay's charges on an account that is settled by payment. Around this core, mature products add the machinery of running the property: the site map/grid as the operating surface, arrivals/departures boards, guest profiles, seasonal rate configuration, online-booking integration with two-way availability sync, guest self-service, camp-store POS, housekeeping/site-turnover tasks, reporting, and — distinctively for this Type — long-stay machinery (monthly/seasonal/annual billing, metered utilities, annual agreements). The Type is the supply-side twin of the Campground Booking Platform and the land-based sibling of the Hotel PMS and Marina Management, distinguished by its unit semantics (sites, not rooms or slips), its stay mix (transient through annual), and its up-front, desk-centered operating culture.
