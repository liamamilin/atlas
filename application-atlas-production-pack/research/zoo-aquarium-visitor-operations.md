# Research Notes — Zoo / Aquarium Visitor Operations

Research date: 2026-09-10

## Predecessor Context (pre-hung flags)

1. **attraction-management-system sibling-leaf cluster flag (§26, processed 2026-09-06):** the AMS pass recorded that "Zoo-Aquarium Visitor Operations" is a probable **segment posture** of the admission-business Type ("museum/zoo/aquarium (timed entry, memberships, donations/fundraising, education, patron CRM depth)" listed as a segment shape at L2) and required each sibling to confirm slice-vs-variant-vs-independent-Type status. This pass must confirm or contest that from fresh zoo/aquarium product evidence.
2. **theme-park-management (§26, processed 2026-09-09):** resolved as SEGMENT POSTURE of AMS (keep-both, own-lens documentation); its pass explicitly noted "zoo-aquarium-visitor-operations remains the open member of the sibling cluster."
3. **family-entertainment-center-management (§26, processed 2026-09-07):** resolved as its OWN Type (play catalog + play entitlements + whole-venue transaction unification) — the precedent for what independence looks like in this cluster.
4. **museum-visitor-experience-platform (§26, processed 2026-09-08):** resolved as INDEPENDENT TYPE (interpretation layer, zero admission machinery) — the precedent for the experience-layer boundary.

## Research Goal

Determine what software serves the visitor business of zoos and aquariums, whether that software has a defining core distinct from the Attraction Management System's admission spine, and what the zoo/aquarium lens specifically adds or emphasizes. Decide: segment posture (like theme park), independent Type (like FEC), or something else.

## Initial Boundary

Working hypothesis before research: zoos/aquariums are living-collection institutions whose visitor business = admission + memberships + education programs + on-site spend; the animal-husbandry side (animal records, husbandry, enrichment) is a different domain entirely. Nearest neighbors: Attraction Management System (admission business), Theme Park Management (sibling lens), Museum Visitor Experience Platform (interpretation layer), Membership/fundraising CRM (nonprofit posture), Parks & Recreation Management (municipal deployments), Animal Collection Management (out of scope by name).

## Research Questions

1. Do zoo/aquarium-serving products implement the AMS admission spine (operator-defined admission products → multi-channel sale → recorded transactions issuing entitlements → entry validation → attendance)?
2. Do zoo products add any structurally distinct pillar that can exist independently of admission (joint-holding test)? Candidates: education program registration, membership economy, animal encounters/tours, donations/fundraising.
3. Is there a zoo/aquarium-specific product family with a different center of gravity?
4. Where does the animal-records domain (collection management) sit relative to "visitor operations"?
5. What deployment/posture variants exist (nonprofit cultural, municipal parks-&-rec, commercial animal parks)?
6. Historical check: would a small regional zoo with paper tickets, hand stamps, and a membership card file still satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

1. **Gateway Ticketing (Galaxy)** — long-established admission-control leader that self-describes as "a point-of-sale leader in the zoo and aquarium industry" (Milwaukee County Zoo announcement); enterprise/legacy tier.
2. **ROLLER** — cloud-first all-in-one venue platform with a dedicated Zoos & Aquariums industry page; modern mid-market tier.
3. **Doubleknot** — SaaS built specifically for "admission- and membership-based cultural attractions" (zoos, aquariums, museums, nature centers); nonprofit/cultural posture with education-first emphasis.
4. **Semnox (Parafait/Tixera)** — multi-vertical international venue platform; zoo evidence via a live zoo deployment (Lembang Park & Zoo) and an Aquariums industry listing.
5. **accesso** — module suite for large destinations with a dedicated Zoos & Aquariums market page and a zoo-specific timed-ticketing learning resource (Columbus Zoo, Australia Zoo, San Diego Zoo webstore, Wild Animal Safari parks).

Supporting artifacts (institution-side, for product semantics): Cincinnati Zoo membership page; San Diego Zoo Wildlife Alliance web store (accesso-powered); ACTIVE Network (parks-&-rec pattern); Tracks Software (animal collection management — boundary evidence).

## Sources

All fetched 2026-09-10 unless noted.

- ROLLER — https://www.roller.software/industries/zoos-management-software (direct fetch)
- Doubleknot — https://www.doubleknot.com/zoo-software (direct fetch); https://www.doubleknot.com/aquarium-software (search-captured page text); https://www.doubleknot.com/education-and-group-sales-software (search-captured); https://www.doubleknot.com/about-doubleknot (search-captured)
- Gateway Ticketing — https://www.gatewayticketing.com/markets/zoos-and-aquariums (direct fetch); https://www.gatewayticketing.com/zoo-ticketing-software (search-captured, verbatim same content); https://www.gatewayticketing.com/ (search-captured); Milwaukee County Zoo announcement http://gatewayticketing.com/resources/gateway-ticketing-systems-and-milwaukee-county-zoo-set-stage-for-smarter-streamlined-guest-access (search-captured)
- Semnox — https://www.semnox.com/ (search-captured); https://www.semnox.com/news/semnox-ticketing-cashless-technology-powers-lembang-park-zoo-reopening (search-captured); https://www.semnox.com/solution/entry-ticketing.html (search-captured); IAAPA marketplace listing https://iaapa.org/partners/marketplace/semnox-solutions (search-captured)
- accesso — https://accesso.com/markets/zoos-aquariums (search-captured); https://accesso.com/learn/accesso-learning-series-enhancing-the-guest-experience-with-timed-ticketing-for-zoos (search-captured); https://accesso.com/news/parks-america-inc-selects-accesso-ticketing-solution (search-captured); San Diego Zoo web store https://tickets.sandiegozoo.org/webstore/shop/ViewItems.aspx?C=sdztp&CG=webstoresdz (search-captured)
- Cincinnati Zoo — https://cincinnatizoo.org/membership (search-captured)
- ACTIVE Network — https://www.activenetwork.com/activenet/features (search-captured); https://www.activenetwork.com/parks (search-captured)
- Tracks Software — https://trackssoftware.com/ and https://trackssoftware.com/features (search-captured); GetApp/SoftwareAdvice listings (search-captured)
- Sibling research (B layer): research/attraction-management-system.md, research/theme-park-management.md, research/family-entertainment-center-management.md, research/museum-visitor-experience-platform.md

## Product Observations

### Gateway Ticketing (Galaxy) — zoo market page + zoo ticketing page + Milwaukee County Zoo announcement

Key observations (Layer A):

- Zoo revenue framing, verbatim: "Ticket sales, educational programs and food sales make up the greatest part of your revenue. By selecting a point-of-sale solution that can unify your income streams, you'll gain better visibility into your operations."
- Galaxy modular offer for zoos, verbatim bullets:
  - "Integrated ticketing and admission control – sell tickets and passes through multiple sales channels and validate those tickets with the simple scan of a barcode (whether printed or on a mobile device)"
  - "Membership creation and management – process new memberships at any point-of-sale system you designate and create full-color membership cards on the spot; manage your members directly through Galaxy **or interface with third-party software such as The Raiser's Edge**"
  - "Efficient scheduling of groups, private tours, advanced bookings and timed events – … managing all reservations through one system that lets you see at a glance the availability of resources throughout your venue"
  - "Increased sales capacity – sell at the front gate or at kiosks, through a call center, online through your own web store, or through third-party distributors via Galaxy Connect"
  - "A unified point-of-sale solution – consolidate your ticketing, food & beverage and retail sales for faster reporting and better customer relationship management"
- Product family (site nav): Galaxy 8 = Sell Tickets On-Site & Online + Admission Control; CRM+ and Reporting+; Membership; Hardware; Food & Beverage and Retail. Pure admission-business module structure.
- Milwaukee County Zoo announcement (2024/2025): zoo "selected Gateway to deliver a mobile-first, integrated solution"; "the Galaxy platform will seamlessly integrate with the Zoological Society of Milwaukee, ensuring real-time data access through operational reporting and fully supporting GiveX gift cards"; zoo deputy director: "Gateway is a point-of-sale leader in the zoo and aquarium industry"; the zoo sought "an all-in-one SaaS Zoo Management System software solution" (InPark wording).
- No animal-records functionality anywhere on the zoo pages.

### ROLLER — Zoos & Aquariums industry page

Key observations (Layer A):

- Positioning: "ROLLER's all-in-one aquarium and zoo management software" — same platform as its FEC/theme-park/museum pages (one platform, industry pages are lenses).
- Four zoo-specific pillars marketed:
  1. Memberships: "Turn visitors into members of your pack. Create a custom-designed membership program and season passes that can be redeemed both online and at the counter. Easily upsell visitors to a membership upon arrival, or after their visit, and capture their payment details for automated monthly or yearly billing."
  2. Group bookings and tours: "manage admissions at scale for large groups. With online ticketing, robust capacity management, and intuitive check-in via POS or mobile."
  3. Animal encounters: "Session-based animal encounters and tours are a big part of your business. Our aquarium & zoo software simplifies the online booking experience making it easy for visitors to add upsells while the back-end capacity management process eliminates over-booking."
  4. F&B/retail POS: "maximize visitor spend."
- Customer story: Oakvale Wildlife Park "increased animal encounter sales by 300%" after moving encounters online ("Going from the previous reservations system to ROLLER, our wildlife encounters were up 300% in the first six months").
- Digital waivers module offered in the zoo context.
- ROLLER's own FAQ definition of the category, verbatim: "Zoo and aquarium software is a tool tailored to assist operators in efficiently managing and enhancing the operations of zoological parks, aquariums and other wildlife facilities. This software offers a range of features such as online ticketing, membership management, scheduling, educational program coordination, retail and concessions management, and reporting."
- Feature list on the zoo page = the generic ROLLER feature set (POS, online ticketing, memberships, party bookings, gift cards, SSK, waivers, guest feedback, F&B, reporting, payments, HQ, CRM, API, access control, capacity management). No animal-records functionality.

### Doubleknot — zoo software + aquarium software pages

Key observations (Layer A):

- Positioning: "With Doubleknot, your zoo can manage every aspect of ticketing, sales, memberships, event and educational program planning, and supporter interactions in a single, integrated platform." Serves "admission- and membership-based organizations including museums, zoos, aquariums, nature centers, botanical and public gardens, science and technology centers… and scout councils" (300+ orgs, North America).
- Core zoo features (six modules):
  1. Ticketing & Admissions: "timed-entry ticketing to manage your zoo's capacity on peak days"; "tiered pricing for members, children, seniors, and other visitor segments"; mobile tickets.
  2. Membership & Fundraising: "flexible membership tiers, payment options, and renewal timelines"; "Monitor fundraising campaign participation, donor engagement, and revenue generation"; add-on Communications Suite for member/donor journeys.
  3. Education & Group Sales: "book a range of group activities like field trips, camps, workshops, and birthday parties"; "color-coded administrative calendars"; "individualized group pricing and booking incentives."
  4. Event Registration: custom signup forms, QR check-in codes, attendance limits/waitlists.
  5. POS: payments; "upsell options with ticket purchases for donations, special attractions, and merchandise."
  6. CRM: "Store all visitor interaction and transaction information in a unified database"; supporter profiles; external CRM integrations.
- **Boundary statement, verbatim (FAQ):** "Note that Doubleknot is *not* a platform for managing zoo animal records."
- Doubleknot's category definition, verbatim: "Zoo software describes technology used by animal-focused cultural organizations to manage operations and revenue generation. Key functionalities of zoo software include ticketing, membership management, fundraising, event registration, educational program planning, point-of-sale (POS) processing, and supporter data management."
- Deployment: cloud, tablets for cashiers, smartphones scanning QR codes at check-in.
- Education & Group Sales module page: group visits/field trips/tours/parties/rentals with capacity, scheduling, billing, check-in; "issue and scan a single group ticket, update headcount and collect any balance due."

### Semnox (Parafait/Tixera) — zoo deployment + industry listing

Key observations (Layer A):

- Lembang Park & Zoo (Bandung, Indonesia) case study: "The operations at Lembang Park and Zoo have been completely powered by the Parafait Amusement Park Management System since December 2019. The Park uses the Ticketing and Access control solution via the barcoded wristbands and Semnox Readers and turnstiles. Single band can be used by guests to enjoy a whole range of activities inside the park including paying for food and other facilities. The park is able to continuously expand its offerings with new attractions, arcade games and membership cards supported by the integrated solution."
- A zoo runs on the same amusement-park platform: ticketing + access control (wristbands/turnstiles) + cashless + F&B + membership cards; the venue mixes animal experiences with amusement rides/arcade.
- Semnox industries list includes Aquariums (alongside theme parks, water parks, museums, FECs, trampoline parks, VR/AR centers, restaurants).
- Entry Ticketing & Access Control solution page: multi-channel sale (online B2B/B2C, kiosks, on-site POS), time-based entry criteria, season passes and multiple-entry packages, RFID/barcode/wristband credentials, turnstile hardware, OTA integration.
- No animal-records functionality in any reachable material.

### accesso — Zoos & Aquariums market page + timed-ticketing resource + zoo deployments

Key observations (Layer A):

- Market page framing: "As visitors encounter a world of fascinating creatures, we help you gather insights to turn them into long-term members and donors." Connected suite across "ticketing, eCommerce, retail, F&B, mobile apps, analytics and distribution."
- Zoo-specific upsell framing: "From behind-the-scenes tours to animal-encounter photos and meal vouchers, our zoo ticketing software delivers the perfect extras during online checkout and at the park."
- Timed Ticketing for Zoos (learning article): "Timed Ticketing allows you to sell tickets for different time-slots throughout the day. Timed Ticketing has many applications and can be used for daily tickets as well as animal encounters." Features: real-time slot visibility, create/manage capacities, thresholds, dynamic pricing (peak/non-peak), "Share the same capacity with General Admission and Member reservations," distribute capacities by location.
- "Sell anything online: … from memberships to parking, admission tickets to camp sessions – even meal deals and souvenirs." — camp sessions sold as products in the ticketing system.
- Zoo deployments: Columbus Zoo and Aquarium ("nearly 15 years… multiple parks, ticketing structures, and in park revenue options"), Australia Zoo, Parks! America's Wild Animal Safari parks (Passport across "multiple admission, pass and group reservation options… front gate point of sale… group sales features, season pass processing and access control options… self-service kiosks or mobile points of sale"), San Diego Zoo web store (Passport-class webstore: 1-Day Pass Any Day / Value Days tiers, 1-Day Pass PLUS with 4D theater, multi-park 3-for-1 pass, validity windows "within one year from date of purchase," per-age pricing).

### Supporting artifacts

**Cincinnati Zoo membership page (institution-side, Layer A):** membership tiers (Individual/Dual/Family) with "year-round unlimited admission plus parking"; member benefits include "Discounted Admission to over 100 reciprocal zoos and aquariums," "Discounts on Zoo education classes, camps and lectures," free admission to a seasonal festival; exclusions: "Memberships are not applicable for admission or rides during school field trips or ticketed events"; non-refundable/non-transferable; virtual membership tier with animal cams but no admission. This documents zoo membership product semantics from the zoo's own side: annual validity, member recognition, reciprocal-network benefits, education discounts, event exclusions.

**San Diego Zoo web store (accesso-powered, Layer A):** zoo admission product structure — dated/undated variants (Any Day vs Value Days), bundled experiences (4D theater), multi-venue passes (Zoo + Safari Park + SeaWorld), validity windows, age-band pricing, "A valid entrance ticket is required for Zoo entrance for each visitor 3 years of age and older."

**ACTIVE Network / ACTIVENet (parks-&-rec pattern, Layer A):** recreation management with activity/program registration, membership management ("unlimited number of membership types, passes, and rates… issue multiple cards for family memberships"), access control ("Instantly verify memberships with access cards, control access with either staffed or self-serve entry points"), facility rentals, POS, childcare management. This is the municipal package whose membership + program-registration + access-control pattern can serve a city-owned zoo; no zoo-specific claims asserted (see Uncertainties).

**Tracks Software (boundary evidence, Layer A):** self-described collection management for zoos & aquariums — animal records, health, husbandry, inventory, training, enrichment, welfare, diet planning, water quality, lab tests, permits, enclosure management, education-program/ambassador-animal scheduling. Its own features page contains no admissions/ticketing/membership/POS functionality (third-party listings that mention "Ticketing" are not corroborated by the vendor's own feature list). Per-module licensing for facilities that "do not use Tracks to manage their inventory records." This is the animal-side domain, adjacent to but distinct from visitor operations.

## Cross-product Comparison

| # | Finding | Gateway | ROLLER | Doubleknot | Semnox | accesso | Strength |
|---|---|---|---|---|---|---|---|
| 1 | Operator-defined admission products (tickets/passes with pricing tiers and validity) | ✓ tickets & passes, multi-channel | ✓ online ticketing | ✓ timed-entry ticketing, tiered pricing | ✓ entry ticketing, season/multi-entry packages | ✓ admission products incl. Any-Day/Value-Day tiers (SDZ webstore) | B — cross-product |
| 2 | Multi-channel sale (gate POS, online, kiosk, call center, resellers) | ✓ gate/kiosk/call center/web store/Galaxy Connect | ✓ online + counter + kiosk | ✓ in-person + online | ✓ online B2B/B2C, kiosks, on-site POS | ✓ online + front gate + kiosks/mobile POS | B — cross-product |
| 3 | Recorded transaction issuing entitlements validated at entry (scan/barcode/QR/wristband) | ✓ barcode scan validation | ✓ check-in via POS/mobile; access control partner | ✓ mobile tickets; QR check-in scanning | ✓ barcoded wristbands + readers/turnstiles | ✓ digital tickets scanned from phone; access control options | B — cross-product |
| 4 | Memberships as a first-class product (tiers, renewal, member recognition, cards) | ✓ membership creation/management, cards on the spot | ✓ memberships & season passes, auto-billing | ✓ membership tiers, renewal timelines | ✓ membership cards | ✓ memberships; member reservations share capacity | B — cross-product |
| 5 | Education / group sales operations (field trips, camps, groups) | ✓ "educational programs" in revenue framing; group/tour scheduling with resources | ✓ group bookings at scale; FAQ names "educational program coordination" | ✓ dedicated Education & Group Sales module (field trips, camps, workshops) | not evidenced in reachable zoo material | ✓ camp sessions sold as products; group reservation options | B — cross-product (depth varies; Doubleknot deepest) |
| 6 | Session-based animal encounters / behind-the-scenes tours as bookable capacity-managed products | ✓ private tours & advanced bookings scheduling | ✓ "session-based animal encounters and tours… a big part of your business" | ◐ special attractions as POS upsells; group tours | not evidenced | ✓ behind-the-scenes tours; encounters; timed ticketing "used for daily tickets as well as animal encounters" | B — cross-product |
| 7 | Timed entry / capacity management for peak days | ✓ timed events scheduling | ✓ capacity management | ✓ timed-entry ticketing for peak-day capacity | ✓ time-based entry criteria | ✓ Timed Ticketing with shared GA/member capacity | B — cross-product |
| 8 | Unified on-site spend (F&B + retail on the same system) | ✓ unified POS: ticketing + F&B + retail | ✓ F&B/retail POS | ✓ POS with upsells; online store add-on | ✓ single wristband pays for food/facilities | ✓ retail + F&B one system | B — cross-product |
| 9 | Donations / fundraising / supporter CRM | ◐ interfaces with Raiser's Edge (external) | not headlined | ✓ Membership & Fundraising module; add-on donation requests with tickets | not evidenced | ✓ "turn them into long-term members and donors" | Segment variant (nonprofit posture) |
| 10 | Membership/fundraising split with external systems | ✓ Raiser's Edge interface; Zoological Society integration | not evidenced | ✓ external CRM integrations offered | not evidenced | not evidenced | Variant posture |
| 11 | Waivers | not evidenced | ✓ digital waivers module | not evidenced | ✓ (digital waiver marketing, sibling evidence) | not evidenced | Optional |
| 12 | Cashless credential / stored value | not evidenced in zoo page | not headlined on zoo page | not evidenced | ✓ single wristband pays across park | not evidenced | Optional |
| 13 | Animal records / husbandry / collection management | ✗ absent | ✗ absent | ✗ explicitly excluded ("not a platform for managing zoo animal records") | ✗ absent | ✗ absent | Boundary constant — out of scope in 5/5 |
| 14 | Ride/arcade play economy | ✗ absent | ✗ absent | ✗ absent | ◐ Lembang zoo runs arcade/amusement on the same platform | ✗ absent | Coexistence capability, not zoo-defining |

Legend: ✓ observed; ◐ partially observed; ✗ absent in reachable material; "not evidenced" = not found in reachable sources (absence of evidence, not evidence of absence).

## Abstraction Levels

### L0 — Defining Invariant (minimal)

Zoo / Aquarium Visitor Operations is the operator-side system for a zoo's or aquarium's visitor business in which:

1. **Operator-defined admission products** — the institution defines what grants entry (dated/undated day tickets, memberships/annual passes, group tickets) as catalog products carrying price and validity rules.
2. **Sale → transaction → issued admission entitlements** — purchases through the system's channels are recorded as transactions that issue redeemable admission entitlements.
3. **Entry validation producing attendance** — entitlements are validated at the institution's entry (scan of barcode/QR/wristband), and that redemption is the attendance record.
4. **On-site spending recorded against the same operation** — food, retail, and extras sold inside the institution flow into the same reporting spine.

This is exactly the Attraction Management System's defining core. Nothing zoo-specific is required to recognize the Type.

Historical/market-sample check: a small regional zoo selling paper tickets at a gate booth, stamping hands or tearing stubs, keeping a membership card file, and running a snack stand satisfies all four properties with no modern machinery — memberships with reciprocal-network lists and education bookings by phone/paper are pre-software practice. Conversely, remove entry validation and it collapses into generic e-commerce; remove admission products and there is no visitor business to run. The core holds.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not required for recognition:

- **Membership economy** — tiers, renewal timelines, automated billing, member recognition at entry (cards/photos/QR), member pricing, member reservations sharing capacity with general admission.
- **Group sales & education operations** — school groups, field trips, camps, workshops, private tours: group booking with per-group pricing, resource/scheduling calendars, group tickets/check-in, headcount updates, deposits/balances.
- **Session-based animal encounters & behind-the-scenes tours** — bookable, capacity-managed session products upsold at checkout and sold online.
- **Timed entry / capacity management** — time-slot ticketing for peak days; capacities shared across channels and member/GA reservation types.
- **Unified F&B and retail POS** on the same system, per-location reporting.
- **Guest/constituent CRM** — visitor, member, and donor records in one database; visit/purchase history; segments.
- **Promotions and pricing rules** — tiered/segmented pricing, peak/off-peak, discount codes.
- **Kiosks and mobile POS**; **digital tickets** (mobile/QR); **reporting** on attendance, revenue by center, membership.
- **Staff roles/permissions** and gate hardware integration (turnstiles, handhelds, readers).

### L2 — Variant / Optional Structure

- **Nonprofit/conservation posture** — donations requested at multiple touchpoints, fundraising campaigns, supporter/donor analytics, communications suites; deepest in cultural-nonprofit products (Doubleknot), present as positioning in accesso, externalized in Gateway (Raiser's Edge interface).
- **Membership/fundraising split** — some institutions run membership in a dedicated nonprofit CRM/fundraising system (e.g., a zoological society's separate membership operation) with the admission system interfacing for recognition and reporting.
- **Municipal deployment posture** — city-owned zoos may run admissions/memberships/education through parks-&-recreation management systems (membership types + program registration + access control pattern).
- **Cashless credential / stored value** — wristbands/cards paying across entry, food, and activities (documented in a zoo deployment; optional).
- **Waivers** — for encounters/interactive activities (optional module).
- **Ride/arcade coexistence** — zoos that add amusement rides or arcades run the play economy on the same or adjacent systems (FEC territory).
- **Multi-park/multi-venue operations** — zoo + safari park + affiliated venues on one platform; cross-venue passes.
- **Dynamic pricing** (peak/non-peak), **OTA/reseller distribution**, **regional fiscal packs** — as in the generic admission business.

### L3 — Vendor-specific (kept out of the final document)

- Gateway: Galaxy 8 module naming; Galaxy Connect reseller channel; GiveX gift cards; Zoological Society of Milwaukee integration; Raiser's Edge trademark note.
- ROLLER: "members of your pack" campaign framing; Oakvale Wildlife Park +300% encounter-sales claim; Venue Manager/HQ naming (sibling evidence).
- Doubleknot: color-coded administrative calendars; Communications Suite add-on; scout-council vertical; 95% retention claim.
- Semnox: Lembang Park & Zoo deployment specifics (10,000-guest capacity figure, December 2019 go-live); Parafait vs Tixera product-line split.
- accesso: Passport naming; Timed Ticketing deminar specifics (thresholds by duration/interval); Columbus Zoo 15-year partnership; SDZWA webstore product names and prices.

## Vendor-specific Findings

See L3. None of these carry to the canonical model.

## Rejected Findings

1. **"Zoo software = animal management software"** — REJECTED as the leaf's subject. The market's own category definitions (ROLLER FAQ, Doubleknot FAQ) describe the visitor/revenue business; Doubleknot explicitly excludes animal records; Gateway/ROLLER/Semnox/accesso zoo materials contain no animal-records functionality. Animal collection management (Tracks, Species360 ZIMS) is a separate product family and a separate domain.
2. **"Education programs are a defining pillar"** — REJECTED as definitional. Education/group sales is emphasized in the segment (Gateway revenue framing, Doubleknot module, accesso camp sessions, ROLLER FAQ) but is absent from some zoo pages (ROLLER's zoo page headlines memberships/groups/encounters/F&B, not education), and education/camp registration exists as its own software family independent of zoos (parks-&-rec, class-registration products). It fails the joint-holding test for definitional status; it is a segment-emphasized capability.
3. **"Memberships make zoo visitor ops a different Type"** — REJECTED. Memberships with validity rules, renewal, and recognition are already inside the AMS defining core; the zoo lens changes their *prominence* (dominant product, reciprocal networks, society splits), not their structure.
4. **"Timed entry is definitional for zoos"** — REJECTED. Open-dated tickets and membership-based entry without reservations are documented (SDZ Any-Day passes; Cincinnati membership terms); timed entry is capacity machinery, present across the whole admission business.
5. **"Donations are definitional"** — REJECTED. Nonprofit-posture variant only; commercial-posture zoo products (ROLLER, Gateway zoo pages) do not headline donations.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove/add to flip the Type) |
|---|---|---|
| Attraction Management System | same Type, generic lens | The defining core is identical; AMS documents the admission business across all attraction segments, this page documents the zoo/aquarium segment: membership-centric economy, education & group sales, animal encounters as session products, nonprofit posture. Remove the lens and the AMS document stands alone. |
| Theme Park Management | sibling segment lens | Same admission core; the theme-park lens adds ride-level control points and ride queues (downstream of admission); the zoo lens adds membership/education/encounters emphasis. Neither lens changes the core. |
| Family Entertainment Center Management | sibling, independent Type | FEC's core is the internal play economy (chargeable play catalog + validated play entitlements), which exists without dated admission (walk in, load a card). A zoo's visitor business cannot exist without admission. Where a zoo adds rides/arcades, the FEC economy coexists as an adjacent capability. |
| Museum Visitor Experience Platform | adjacent, complementary | The interpretation layer (guides, tours content, wayfinding) of a visit, not the commercial visitor business. A zoo app with animal info/maps is that Type's pattern applied to zoos. |
| Animal Collection Management (Tracks, Species360 ZIMS) | adjacent domain, out of scope | Animal records, health, husbandry, enrichment, water quality — the living-collection side of the institution. Doubleknot states the exclusion verbatim; no sampled visitor-ops product contains it. Remove admission from Tracks and it remains collection management; remove animals from zoo visitor ops and it remains the admission business. |
| Membership Management System / Nonprofit CRM / Fundraising CRM | adjacent, sometimes split | Some zoos run membership/fundraising in dedicated nonprofit systems with the admission system interfacing (Gateway ↔ Raiser's Edge; Galaxy ↔ Zoological Society). The admission system's membership module and the dedicated CRM overlap; the split is a deployment posture, not a Type boundary. |
| Parks & Recreation Management | adjacent, municipal posture | Municipal zoos may run the same spine (memberships + program registration + access control) inside a recreation-management package. Same structures, different package context. |
| Event Ticketing Platform | adjacent, coexistence | Zoos run separately ticketed special events (evening festivals, ticketed events excluded from memberships); those occasions can use event-ticketing machinery. Admission to the place vs admission to a dated performance. |
| Tour Operator Management System | distant | Behind-the-scenes tours here are session products inside the admission system (time slots + capacity), not multi-day itineraries with guides/departures. |
| Cashless Venue Platform | slice | The stored-value payment slice of on-site spending (wristband economies). |
| Digital Waiver Management | slice | Waiver capture for encounters/activities, embedded as an optional module. |

Taxonomy resolution: the AMS pass's "Zoo = segment posture" hypothesis is **CONFIRMED** with fresh evidence. The leaf is retained and documented from its own lens (same keep-both pattern as theme-park-management). No directory change made from this side.

## Uncertainties

- No vendor help-center/user-manual pages were reachable from the research environment; all observations are official product-page level (plus one institution-side membership page and one live webstore). Precise operational details — capacity mechanics, re-entry rules, validity-window configuration, membership proration, group-deposit rules — are deliberately not asserted.
- ACTIVE Network serving zoos specifically: the parks-&-rec pattern is documented, but no sampled municipal-zoo deployment was directly verified; kept as a posture variant, not a product claim.
- Tracks' third-party listings mention "Ticketing" among features; the vendor's own features page does not corroborate it. Treated as uncorroborated; the boundary conclusion does not depend on it.
- Education-module depth varies widely (Doubleknot dedicated module vs ROLLER FAQ mention); the exact boundary between "group sales" and "education program registration" inside products is not documented precisely enough to assert a common structure beyond group booking + calendars + per-group pricing.
- Regional zoo markets outside North America/Indonesia (e.g., Europe's zoo software landscape) were not sampled; DigiTickets/Regiondo-class attraction platforms likely serve zoos there (sibling evidence), but no zoo-specific page was fetched.

## Final Synthesis

Zoos and aquariums run their visitor business on the same admission-business software as every other visitor attraction: operator-defined admission products, multi-channel sale, recorded transactions issuing entitlements, validation at entry producing the attendance record, and on-site spending on the same reporting spine. Four independent vendors' zoo materials (Gateway, ROLLER, Doubleknot, Semnox) plus accesso's zoo vertical all land inside that core; none adds a structurally new pillar that can exist without it. What the zoo/aquarium lens changes is emphasis and posture, not structure: the membership economy dominates (annual memberships as the primary product, renewal engines, member recognition, reciprocal networks, sometimes split with a zoological society's own CRM); education and group sales are a major operational surface (field trips, camps, school groups with resource scheduling); animal encounters and behind-the-scenes tours are sold as capacity-managed session products; timed entry manages peak-day capacity; and the nonprofit posture adds donations and supporter CRM. The sharpest boundary is with the animal side of the institution: animal records and husbandry live in collection-management systems (Tracks, ZIMS) that no visitor-operations product contains — Doubleknot excludes them verbatim. The leaf is therefore a segment posture of the Attraction Management System Type, documented from its own lens, with the animal-collection domain explicitly outside it.
