# Research Notes — Spa Management System

## Research Goal

Determine what "Spa Management System" software actually is, from real products: its core operating model, what (if anything) structurally distinguishes it from the generic appointment-based service business software already documented (appointment-based-service-business-management and the processed §29 siblings), and where its boundaries sit — especially against Med Spa Management (the regulated-treatment sibling) and Salon Management System.

## Initial Boundary

Working hypothesis at start:

- Core use: run a spa business (day spa, resort/hotel spa, combined salon-spa, wellness formats) — booking relaxation/wellness treatments, delivering them in rooms by therapists, and monetizing the client relationship.
- Primary users: front desk/reception, therapists/technicians (massage, facial, body treatments), spa directors/managers.
- Nearest neighbors: appointment-based-service-business-management (generic core), med-spa-management (processed sibling), salon-management-system (processed sibling), massage-practice-management (processed sibling), §26 Hotel PMS (resort-spa integration seam), beauty-service-marketplace (consumer side).
- Prior flags hanging on this leaf:
  - The appointment pass (2026-09-06) flagged spa-management-system as a probable industry Variant of the generic appointment-business core.
  - The med-spa pass (2026-09-08) recorded a removal test for this leaf: "remove the regulated-treatment layer → that industry's business on the same visit economy (spa pole's center = room-and-therapy itinerary vs med-spa center = provider-typed regulated treatments + documentation + compliance)."
  - The salon pass (2026-09-10) predicted the seam: "Spa pole's center = room-and-therapy itinerary; salon pole's center = the stylist's chair and the color service."
  - The massage pass (2026-09-08) listed spa-management-system among unprocessed siblings as a probable industry Variant.
  - The beauty-service-marketplace pass listed spa-management-system among operator-side beauty leaves (no specific action required beyond noting).

## Research Questions

1. What objects does the software manage? (catalog, clients, appointments, rooms, therapists, packages, memberships…)
2. Is the appointment/visit economy (catalog + client + appointment + lifecycle + checkout) present at every market pole, including the most hospitality-embedded one (resort spa)?
3. What is the characteristic spa overlay, and is it definitional or emphasis? (Removal test: remove rooms/itineraries → does the generic appointment-business core remain?)
4. How do treatment rooms and therapists co-schedule? Is room allocation a first-class booking constraint?
5. How are multi-service visits handled (spa journeys: massage + facial + body treatment in one visit; couples treatments with two providers)?
6. What does the resort/hotel spa variant add (PMS integration, room charge, guest recognition, multi-currency)?
7. What state machines and rules matter (bundle ordering/simultaneity, resource double-booking, no-show, deposits)?
8. Historical check: does a paper-era or regional spa satisfy the same definition (avoid overfitting to the current SaaS/AI generation)?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Client tier | Region | Evidence tier reached |
|---|---|---|---|---|
| Vagaro | Generic multi-industry suite serving spas as a first-class business type | Single + small multi-location | US | Tier-1 (support center: Resources, Service Bundle, Multiple Appointments articles) |
| Zenoti | Enterprise all-in-one spa/salon/medspa platform | Multi-location chains, resort/hotel spas, global | US/global | Tier-2 (spa-management-software page with detailed FAQ) |
| Mangomint | Mid-market salon/spa software with a dedicated spa solution | Boutique salons/spas | US | Tier-2 (spa solution page with FAQ) |
| Agilysys Book4Time | Spa-native hospitality pole — built for hotels, resorts, wellness operators | Global hotel groups (Marriott, Hilton, Four Seasons named) | Global | Tier-2 (product page with FAQ) |

Deliberately excluded: Fresha/Booksy (known unreachable from this environment per prior passes); SpaSoft/SpaBooker (legacy spa-native products, not fetched this pass — recorded as an evidence gap, not a claimed difference); Mindbody (wellness/fitness-first positioning, adjacent).

## Sources

All fetched 2026-09-10.

- Vagaro — https://support.vagaro.com/hc/en-us (Tier-1): article 204347960 "Add Resources to Services and Classes", article 204348090 "Create a Service Bundle", article 360038357414 "Book a Service Bundle", article 360010525613 "Schedule Multiple Appointments at Once"
- Zenoti — https://www.zenoti.com/spa-management-software (Tier-2, with FAQ)
- Mangomint — https://www.mangomint.com/solutions/spa-software/ (Tier-2, with FAQ)
- Agilysys Book4Time — https://www.agilysys.com/en/products/book4time/ (Tier-2, with FAQ)

Sourcing limitation: Tier-1 help-center evidence was reached for Vagaro only; Zenoti, Mangomint and Book4Time claims rest on their official product pages (Tier-2). Marketing numbers (benchmark percentages, "no-shows reduced by up to 40%", rating claims) are NOT carried into the final document. Prior-pass Tier-1 knowledge reused from the family file where noted (Vagaro/Zenoti API-doc observations from the appointment and massage passes).

## Product A — Vagaro (generic suite pole, Tier-1)

### Key observations (evidence: A = direct from fetched help-center articles)

- **Resources as bookable constraints (Tier-1, article 204347960):** "A Resource is a room, space, furniture, or tool required to perform a service. Because of its limited quantity, resources must be shared between team members. Examples include a massage room, a chair, a studio, and different types of equipment. Vagaro automatically selects the first available resource for each booking, and you can change the assigned resource if needed." Resources attach to services on the Service/Class Menu and auto-assign at booking; assignable per appointment on the Calendar.
- **Multi-service same-day visits (Tier-1, article 360010525613):** "you are not limited to scheduling one service at a time. You can book multiple services together, as long as they are scheduled for the same day." Up to six services at once on the calendar flow; up to ten services/classes in the multiple-appointment flow.
- **Service bundles (Tier-1, article 204348090):** "A service bundle allows you to group up to six services and sell them together, typically at a discounted price, like a couples massage or haircut and beard trim." Bundle semantics are explicitly configurable: "Services Must be Performed in Order" (prevent reordering) and "Services can be performed at the same time" with three modes — No / Optional / Required ("must be booked and performed at the same time by two different service providers"). Bundles are categorized as services in the service menu and sellable online.
- **Couples/simultaneous two-provider delivery (Tier-1, articles 204347960 + 360038357414):** "Multiple appointments and service bundles can be booked to be performed at the same time, such as a couple's massage performed by two service providers, or back-to-back, such as one person getting a massage followed by the person's friend." All bundle services must be scheduled for the same day.
- **Bundle vs package distinction (Tier-1, vendor comment):** "A bundle is made up of multiple services that the customer books at once at a special price, whereas a package is a group of pre-paid services that the customer can redeem over time."
- **Resource double-booking protection (Tier-1, vendor comment):** "Add-ons must always be scheduled with a service or class to avoid the risk of double-booking the resource… If you include a service for a resource, the entire duration of the service, including the add-on, will also be scheduled."
- Family machinery present throughout (from the appointment pass's Tier-1 evidence, reused): appointment statuses, checkout with tips/IOUs, packages/memberships/gift cards, retail, Forms and SOAP Notes (activatable feature area), payroll, marketing, consumer listing page.

## Product B — Zenoti (enterprise pole, Tier-2)

### Key observations (evidence: A on the fetched page, Tier-2 strength)

- Positioning: "Spa Management Software: Run Every Part of Your Spa from One Platform"; "Whether you run a spa, a salon, or a combined salon and spa, Zenoti runs booking, POS, memberships, staff, and marketing from one platform."
- **Zenoti's own category definition (quotable):** "Spa management software is an all-in-one platform that handles appointment scheduling, point of sale, client management, memberships, staff scheduling, inventory, marketing automation, and reporting for spa businesses."
- **Room + therapist co-scheduling (FAQ, quotable):** "Zenoti's scheduling system manages both therapist availability and treatment room allocation in the same booking flow. When a client books a treatment, the system assigns a therapist and a room simultaneously, preventing double-booking of either. For multi-room spas and resort properties, this is a critical capability that standalone booking tools typically lack."
- **Resort/hotel spa variant (FAQ + body text):** "Resort spa operations connect the spa to the broader property. Hotel guests should book treatments through the hotel's flow, charge services to their room, and have their profile recognized at the spa. Zenoti integrates with major property management systems, supports multi-currency billing for international guests, and manages treatment room inventory across large multi-room facilities."
- **Day spa variant:** "appointment-driven, repeat-client businesses… 24/7 online booking… membership programs that drive visit frequency, and CRM-triggered marketing."
- **Wellness formats (float spa, foot spa):** float spas — "single-occupancy tanks, timed sessions, mandatory cleaning buffers between floats… online booking that shows real tank availability"; foot spas — "chair/station scheduling, quick checkout, and packages for regulars."
- **Access & Amenity Control feature:** "Manage digital check-ins, facility access, and amenity usage without separate systems."
- **Combined salon+spa:** "shared client profiles, one POS checkout, and consolidated reporting across every service type."
- Family machinery: online booking, kiosk/POS, memberships & packages, gift cards, loyalty, marketing automation, inventory, payroll & tipping, multi-location, AI workforce (receptionist, concierge, scribe, marketer).

## Product C — Mangomint (mid-market salon+spa pole, Tier-2)

### Key observations (evidence: A on the fetched page, Tier-2 strength)

- Positioning: "Best Spa Software for Booking, Scheduling & Payments"; "Built for top-performing spas"; spas are one named solution among ~12 industries on the same platform.
- **Multi-service single appointment with automatic resource/provider scheduling (FAQ, quotable):** "Mangomint allows clients to book multiple services in a single appointment seamlessly. Whether a client wants a massage followed by a facial or a body treatment with a sauna session, the system automatically schedules each service with the appropriate provider and resources. This ensures a smooth experience for both clients and staff while preventing scheduling conflicts."
- **Treatment rooms/equipment as resources (FAQ, quotable):** "You can assign specific treatment rooms or equipment to services with our Resources feature to track usage and make sure you're never double booked."
- Family machinery: login-free online booking, reminders, memberships & packages, recurring appointments, automated flows, retail inventory, gift cards, forms & charting, multi-location, POS.
- Vocabulary: "therapists" for staff; "clients" for customers.

## Product D — Agilysys Book4Time (spa-native hospitality pole, Tier-2)

### Key observations (evidence: A on the fetched page, Tier-2 strength)

- Positioning: "The Leading Spa Software for Hotels & Resorts… a cloud-based spa management software platform built for hotels, resorts, and wellness operators." Named customers: Marriott, Hilton, Accor, Hyatt, Four Seasons.
- **Room + technician co-scheduling:** "Optimize technician availability, treatment room assignments, and service capacity across single or multi-location operations."
- **Hospitality integration (the resort variant's machinery):** "integrated with the Agilysys PMS hotel property management system and InfoGenesis hospitality POS system"; "spas can support seamless guest recognition and room-charge workflows"; multi-currency, multi-language, multi-property.
- **Dynamic yield management (product-distinctive):** "Apply hotel-style revenue optimization to spa services by adjusting pricing based on demand, therapist availability, and time of day… Customize pricing rules based on day of week, time of day, occupancy levels, therapist availability, and lead time."
- Family machinery: scheduling, payments (native Book4Time Pay: deposits, memberships, gift cards), memberships & packages, retail, inventory with product usage tracking, commissions/payroll automation, analytics, branded online booking.
- Vocabulary: "technicians", "guests", "treatment rooms", "spa outlets".

## Cross-product Comparison

| Structure / capability | Vagaro | Zenoti | Mangomint | Book4Time | Evidence layer |
|---|---|---|---|---|---|
| Bookable service catalog (duration+price) | ✓ (Tier-1) | ✓ | ✓ | ✓ | B |
| Identified client/guest records with history | ✓ | ✓ | ✓ | ✓ (guest recognition) | B |
| Appointment binding client×service×provider×time | ✓ (Tier-1) | ✓ | ✓ | ✓ | B |
| Visit lifecycle through delivery; cancel/no-show handling | ✓ | ✓ | ✓ | ✓ | B |
| Checkout resolving visit into recorded payment | ✓ (Tier-1) | ✓ | ✓ | ✓ (native pay) | B |
| Treatment rooms/spaces as bookable resources | ✓ (Tier-1, "massage room") | ✓ (FAQ: room+therapist simultaneous) | ✓ (FAQ: rooms/equipment) | ✓ (room assignments) | B |
| Multi-service same-day visit / bundle / itinerary | ✓ (Tier-1, bundles up to 6, same-day rule) | ✓ (implied by combined flows) | ✓ (FAQ: multi-service single appointment) | ✓ (packages; upsells) | B |
| Couples / simultaneous two-provider delivery | ✓ (Tier-1, explicit) | — (not observed) | — (not observed) | — (not observed) | A (product-specific at Tier-1; couples massage is the vendors' own canonical example) |
| Bundle ordering/simultaneity rules (in-order / same-time No-Optional-Required) | ✓ (Tier-1) | — | — | — | A (product-specific) |
| Resort/hotel PMS integration, room charge, guest recognition | — | ✓ (FAQ) | — | ✓ (core positioning) | B (2/4) |
| Dynamic yield/dynamic pricing | — | ✓ (dynamic pricing module) | — | ✓ (core positioning) | B (2/4) |
| Memberships / packages / prepaid series / gift cards | ✓ | ✓ | ✓ | ✓ | B |
| Retail + inventory (product usage tracking) | ✓ | ✓ | ✓ | ✓ (usage tracking) | B |
| Staff schedules, commissions, (payroll) | ✓ | ✓ (payroll) | ✓ | ✓ (payroll) | B |
| Multi-location / multi-property | ✓ | ✓ | ✓ | ✓ (multi-property core) | B |
| Amenity/facility access control | — | ✓ (single-product) | — | — | A (product-specific) |
| Float-tank turnover/cleaning buffers | — | ✓ (single-product FAQ) | — | — | A (product-specific) |
| Marketing/loyalty/reviews | ✓ | ✓ | ✓ | ✓ | B |

Reading: the visit economy is unanimous (B-layer) at every pole including the most hospitality-embedded one. The spa overlay is also common, but its depth varies: room+therapist co-scheduling and multi-service itineraries appear across the sample (B), while couples-simultaneity rules, yield management, amenity access, and float mechanics are product-specific or variant-level.

## Canonical Model (four abstraction levels)

### L0 — Defining Invariant

Same jointly-held core the family passes already established (appointment-business core), realized for the spa trade:

1. **Bookable treatment catalog** — services with duration and price (massage, facial, body treatments, hydro/thermal sessions; catalog typed by therapy, not by hair service or regulated treatment).
2. **Identified client/guest records** — persistent per-person records carrying visit history and preferences.
3. **Appointment** — binding client × treatment × provider (therapist/technician) × time; treatment rooms/spaces as common resource constraints.
4. **Visit lifecycle through service delivery** — with cancellation and no-show as named outcomes (deposits/no-show protection common but not invariant).
5. **Checkout resolving the visit into recorded payment** — the visit becomes revenue in the same system (retail, gift cards, packages sharing the checkout).

Remove any leg → not this Type (remove catalog/appointment → generic CRM; remove checkout → scheduler; remove appointment → retail POS).

### L1 — Common Mature Structure

Present across the sample (evidence layer B), expected of mature products but not defining:

- Self-booking portal + reminders + waitlist + deposits/no-show protection
- Treatment rooms/spaces/equipment as bookable resources alongside provider availability, with double-booking prevention
- Multi-service same-day visits (spa journeys) sold as bundles/packages and scheduled across providers and rooms
- Memberships, packages/prepaid series, gift cards
- Retail product sales with inventory and product-usage tracking, in the same checkout
- Staff scheduling, commissions, tips, (in some suites payroll)
- Marketing automation, campaigns, loyalty, reviews, gift-card referral loops
- Multi-location management and reporting; role-based permissions
- Client intake/preference capture (lighter than the med-spa clinical layer)

### L2 — Variant / Optional Structure

- **Resort/hotel spa packaging** — PMS integration, room charge to the hotel folio, property-level guest recognition, multi-currency/multi-language, multi-property oversight (Zenoti FAQ, Book4Time core)
- **Dynamic yield management** — hotel-style demand-based pricing on treatments/rooms (Book4Time core; Zenoti dynamic-pricing module)
- **Couples/simultaneous two-provider delivery** with explicit bundle ordering/simultaneity rules (Vagaro Tier-1; the vendors' own canonical bundle example)
- **Wellness formats** — float spas (tank turnover, cleaning buffers, single-occupancy), foot spas/reflexology (station scheduling, walk-in emphasis), infrared/sauna/cryo studios (Zenoti)
- **Amenity/facility access control** — digital check-ins, locker/amenity usage (Zenoti, single-product)
- **Combined salon+spa operation** — one platform, shared client profiles, one checkout (Zenoti, Mangomint)
- Marketplace posture, AI reception/agents, mobile services — family-level variants inherited from the generic pass

### L3 — Vendor-specific (research notes only)

- Vagaro: resource auto-assignment ("first available"), up-to-10 multiple-appointment booking, bundle Show Online/Bundle Only/Bundle & Price display options, appointment-type retention tracking (request/new/return), Live Stream services, Check-in App, IOUs
- Zenoti: AI Workforce family (Receptionist, Concierge, Scribe, Lead Manager, Marketer, Dispute Manager, Retention Manager, Employee Scheduler, Inventory Manager); myZen tip card; benchmark-report claims; "no-shows reduced by up to 40%" marketing claim (not carried)
- Mangomint: Express Booking™, Virtual Waiting Room, flat pricing ($120/mo + $10/user marketing claim, not carried), 4.9-star rating claims (not carried)
- Book4Time: RevStream Analytics (ISPA award), Book4Time Pay, Agilysys PMS/InfoGenesis/Analyze integration family, guestsense.ai

## Vendor-specific Findings

- Vagaro's Tier-1 bundle semantics are the cleanest natural experiment for the spa itinerary: a bundle is explicitly a same-day multi-service sale with configurable ordering and simultaneity ("Required: …performed at the same time by two different service providers" — the couples-massage case), distinct from a prepaid package redeemed over time. This shows the multi-service visit is a first-class scheduling object, not just marketing bundling.
- Zenoti's FAQ states the room+therapist simultaneous-assignment capability as the differentiator "that standalone booking tools typically lack" — vendor framing, but consistent with Mangomint's and Book4Time's resource features (B-layer).
- Book4Time is the only sampled product whose entire identity is hospitality-embedded (PMS room charge, guest recognition, yield management modeled on hotels/airlines) — the resort-spa packaging pole.
- Mangomint's FAQ frames multi-service booking as client-facing self-service ("clients can book multiple services in a single appointment"), while Vagaro's Tier-1 docs frame it as staff-side calendar composition; both realize the same structure.

## Boundary Findings

1. **vs appointment-based-service-business-management (generic, §29)** — keep-both, industry-variant resolution per barbershop/massage/med-spa/nail/tattoo/salon precedent. The L0 is identical; the spa differences concentrate in the overlay (room-and-therapist co-scheduling emphasis, multi-service same-day itineraries, couples/simultaneous delivery, resort/hospitality packaging). Removal test passed in BOTH directions: (a) generic platforms (Vagaro) serve spas with the same core machinery plus resources; (b) no sampled product lacks the visit economy, not even the hospitality-embedded pole. ⇒ This pass DISCHARGES the appointment pass's sibling flag for spa-management-system.
2. **vs med-spa-management (§29 sibling)** — the med-spa pass's recorded removal test CONFIRMED from this side: remove the regulated-treatment layer (medical intake/consents, provider-facing charts, compliance posture, unit-usage economics) and the treatments revert to relaxation/wellness therapies delivered in rooms by therapists → this Type on the same visit economy. The spa sample carries no clinical-documentation layer: no sampled spa page leads with charting, consent workflows, or regulated-data posture (those exist in the platforms as the medspa overlay machinery). The med-spa center is provider-typed regulated treatments + documentation + compliance; the spa center is the room-and-therapy itinerary. Same L0 family; keep-both RATIFIED.
3. **vs salon-management-system (§29 sibling)** — the salon pass's predicted seam CONFIRMED: the spa pole's center is the room-and-therapy itinerary (rooms as scarce shared resources, multi-service journeys through different rooms/therapists); the salon pole's center is the stylist's chair and the color service (processing-time subdivision, formulas). Both overlays ride the same core; platforms cross-serve both (Zenoti, Mangomint combined salon+spa pages).
4. **vs massage-practice-management (§29 sibling)** — massage is a single-therapy practice variant (clinical-documentation overlay optional); spa is the multi-therapy establishment variant where the room/itinerary structure is foregrounded. Same core; keep-both per that pass's precedent.
5. **vs Hotel PMS (§26)** — the resort-spa variant integrates WITH the PMS (room charge, guest recognition) but the spa system's own records of record are treatments/rooms/therapists/visits, not guest stays/room inventory/folios. Book4Time is itself positioned as a spa module inside a hospitality suite — the seam is the object world, not the brand. When stay/folio/room-inventory management dominates, the product is a PMS.
6. **vs beauty-service-marketplace (§29)** — consumer-side discovery across providers vs operator-side management of one business (established family seam; Vagaro bundles both sides, Book4Time does not).
7. **vs appointment-scheduling-application (§03.09)** — remove the client ledger and checkout → only a scheduler remains. Here the booking runs a business and resolves into money.
8. **vs retail POS (§05.10)** — remove booking/durations/room-therapist binding → only counter retail remains; retail shares the checkout, not the center.

**Escalation (Variant Problem, per workflow):** the researched evidence confirms this leaf shares its operational core with Appointment-based Service Business Management and the §29 industry family. Its defensible distinction is the spa industry overlay (room-and-therapy itinerary emphasis, multi-service journeys, couples/simultaneous delivery, resort/hospitality packaging). Documented as an industry Variant with keep-both per the family precedent; recorded in STATUS.md rather than rewriting the taxonomy.

**Removal tests (for the final doc):** remove the client ledger and checkout → an appointment scheduler remains; remove the booking and calendar → a point of sale remains; remove the room/itinerary overlay → the generic appointment-business Type remains; remove the regulated-treatment layer from the med-spa sibling → this Type remains; remove the stay/folio object world from the resort variant → the spa system remains (the PMS keeps it).

## Historical / Market-Sample Check

- **Paper-era spa (conceptual, passed):** a day spa before this software category — appointment book with room columns; client cards with treatment history and preferences; printed treatment menus; package/gift-card stubs; product retail shelf; cash drawer; therapist tip-out envelopes. Satisfies the L0 at analog level AND shows the room-and-itinerary overlay predates the software — the paper appointment book already scheduled rooms alongside therapists. The software-era additions (AI reception, yield management, amenity apps) are correctly NOT in the core.
- **Regional check:** the sample is US/global-hospitality weighted; European and Asian spa traditions (thermal baths, onsen, hammam) differ in business model but reduce to the same visit economy when run as appointment businesses. Not separately evidenced this pass; recorded as an uncertainty rather than a claim.
- **Era check:** the definition names no AI, no cloud, no dynamic pricing, no PMS integration, no specific therapy type in L0.

## Uncertainties

- No Tier-1 help-center evidence for Zenoti, Mangomint, Book4Time this pass; their structural claims rest on official product pages (Tier-2). Structure-level assertions only; no operational minutiae asserted from them.
- Couples/simultaneous two-provider delivery is Tier-1-verified only in Vagaro; held at variant level in the final document despite being the vendors' own canonical bundle example.
- The legacy spa-native desktop pole (SpaSoft-class products) was not fetched; the resort pole (Book4Time) and generic poles carry the sample. The spa-native standalone pole is an evidence gap, not a claimed structural difference.
- Amenity access control and float-tank mechanics are single-product observations (Zenoti); held at product-specific level.
- Whether any resort spa product models the treatment itinerary against the guest's stay (e.g., spa credit consumed from a stay package) is unverified from official docs; room-charge and guest recognition are verified, deeper package-coupling is not.
- Zenoti help center (help.zenoti.com) not fetched this pass; its room+therapist claim rests on the product page FAQ.

## Final Synthesis

Spa Management System software is the spa industry's expression of the appointment-business core: a bookable treatment catalog, identified client records, the appointment binding client×treatment×therapist×time, the visit lifecycle through delivery, and checkout into recorded payment — with a characteristic (not definitional) spa overlay: treatment rooms and spaces scheduled as first-class resources alongside therapists, multi-service same-day visits (spa journeys) sold as bundles and scheduled across rooms and providers, couples/simultaneous delivery as a named booking pattern, and — in the resort/hotel variant — integration with the property's PMS for room charge and guest recognition. The market realizes one Type across a packaging gradient — from generic multi-industry suites, to mid-market salon+spa platforms, to enterprise spa chains, to hospitality-embedded resort systems — and the visit economy remains the operating spine at every point on that gradient.
