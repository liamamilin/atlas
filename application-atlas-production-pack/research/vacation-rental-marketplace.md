# Research Notes — Vacation Rental Marketplace

Research date: 2026-09-09. Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1.

## Research Goal

Understand what a Vacation Rental Marketplace actually is as an Application Type: who uses it, what objects exist inside it (listing, host, guest, calendar, rates, booking, trip, review, payout), how the booking transaction flows from discovery to stay, which rules (approval gates, cancellation ladders, payment collection, fee rules) shape behavior, and where its boundary lies against the neighboring Types that have pre-flagged this pass.

Pre-flagged joint-review duties inherited from sibling passes:

1. **hotel-search-booking-platform** (processed 2026-09-08): "vs vacation-rental-marketplace + campground-booking (inventory-character seam, JOINT REVIEW RECOMMENDED — both unprocessed)"; its later note narrows the seam candidate to "property-operated accommodation sold by rate" vs "individually hosted units / owner-mediated stays."
2. **property-listing-platform** (processed 2026-09-09): inventory-character seam held from its side — "short-stay bookable inventory with platform-mediated booking vs housing-market offers with enquiry routing and off-platform completion."
3. **boat-yacht-charter-platform** (processed): "the boundary vs Vacation Rental Marketplace is the sharpest structural seam in this pass — same two-sided time-based rental skeleton, held on vessel-operation semantics; recommend re-confirming when vacation-rental-marketplace is processed."
4. **online-travel-agency-ota** (processed): "Two-sided marketplace where the platform's defining surface is host-side listing management and host-guest marketplace mechanics; the OTA pattern (traveler-first multi-supplier retail) is a subset posture. Remove supplier-retail framing → marketplace."
5. **hostel-booking-platform / campground-booking-platform** (processed): directory splits demand-side lodging booking into inventory-domain siblings (hotel / hostel / vacation rental / campground); loop shared, inventory semantics differ — no alias problem.
6. **listing-marketplace** (processed): "Booking platforms execute reservations as the core transaction; long-term rental listing marketplaces end at inquiry/viewing."

## Initial Boundary

- Hypothesis: a two-sided platform where hosts (owners or their managers) list privately controlled accommodation units for short-stay rental and travelers book specific dated stays, with the platform mediating the transaction.
- Nearest neighbors: Hotel Search/Booking Platform (§26), Property Listing Platform (§17), OTA (§26), Boat/Yacht Charter Platform (§18), Hostel/Campground Booking Platforms (§26), Short-term Rental Management (§17, unprocessed), Travel Review Platform (§26), Metasearch (§02.02).
- Obvious unknowns: how far the supply side extends (individual owners vs professional property managers vs provider-owned portfolios); whether the booking transaction is definitional (given the listings-territory seam); what happens when the same venue also sells hotels or acts as its own provider.

## Research Questions

1. What is the unit of supply? Who may publish it?
2. What does the host side manage (listing, calendar, rates, booking settings, payouts)?
3. What does the guest side do (search, listing evaluation, booking, payment, stay)?
4. What booking modes exist and what states does a booking traverse?
5. How do payment collection, fees, refunds, and payouts work?
6. What trust machinery exists (verification, reviews, damage protection, contracts)?
7. What rules constrain behavior (off-platform fees, disclosure requirements, review eligibility)?
8. What exceptions matter (decline/expire, host cancellation, double booking, damage claims)?
9. What interfaces does each side get?
10. Where are the boundaries vs the flagged neighbors?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies + different customer tiers + different supply postures.

| Product | Supply posture | Positioning | Docs sampled |
|---|---|---|---|
| **Airbnb** | P2P individual hosts (plus co-hosts, professional hosts; also lists hotels) | the standard-bearer consumer marketplace | Tier-1 help center (topic tree + articles) |
| **Homes & Villas by Marriott Bonvoy** | professional property management companies (PMCs) only | hotel-brand curatorial layer over professionally managed premium homes | Tier-1 FAQ (long-form) + site surfaces |
| **Interhome** | provider: own managed portfolio + local partner offices + third-party providers | European holiday-home specialist "since 1965"; self-declared non-intermediary for its own offers | Tier-1 "How the platform works" + review policy |

Considered and rejected/unreachable: Vrbo (help center 429×2, root 429 — Expedia family wall, same pattern as hotel pass's Booking.com note), The Plum Guide (FAQ 403), 9flats (403), Tujia (not attempted after three misses in the P2P space — sample already carries a P2P pole with deep docs).

## Sources

- Airbnb Help Center root: https://www.airbnb.com/help (topic tree) — 2026-09-09
- Airbnb, "How to book a home: Instant Book and reservation requests": https://www.airbnb.com/help/article/85 — 2026-09-09
- Airbnb, "How Instant Book works" (host): https://www.airbnb.com/help/article/1510 — 2026-09-09
- Airbnb, "Understanding your reservation status": https://www.airbnb.com/help/article/363 — 2026-09-09
- Airbnb, "Reservation status" topic: https://www.airbnb.com/help/topic/1596 — 2026-09-09
- Airbnb, "Booking places to stay" topic: https://www.airbnb.com/help/topic/1341 — 2026-09-09
- Airbnb, "Cancellations" topic: https://www.airbnb.com/help/topic/1367 — 2026-09-09
- Airbnb, "Pricing and fees" topic: https://www.airbnb.com/help/topic/1355 — 2026-09-09
- Airbnb, "All topics" (guest view): https://www.airbnb.com/help/all-topics — 2026-09-09
- Airbnb host landing: https://www.airbnb.com/host/homes — 2026-09-09
- Homes & Villas by Marriott Bonvoy, "About & FAQs": https://homes-and-villas.marriott.com/en/about-us-faq — 2026-09-09
- Homes & Villas by Marriott Bonvoy, site root: https://homes-and-villas.marriott.com/en — 2026-09-09
- Interhome, "How the platform works": https://www.interhome.com/how-the-platform-works/ — 2026-09-09
- Interhome, site root: https://www.interhome.com — 2026-09-09
- Sibling research notes consulted for boundary consistency: research/hotel-search-booking-platform.md, research/property-listing-platform.md, research/boat-yacht-charter-platform.md, research/online-travel-agency-ota.md, research/hostel-booking-platform.md, research/campground-booking-platform.md, research/listing-marketplace.md, research/travel-package-booking-platform.md, research/travel-itinerary-planner.md, research/destination-discovery-application.md

Sourcing limitations (recorded per the evidence rules):

- Vrbo, The Plum Guide, 9flats unreachable (429/403). Vrbo's request-to-book and subscription-history traditions are therefore NOT asserted from product docs; no claims depend on them.
- Airbnb article-level status lists ("Understanding your reservation status") render section headers behind JS — the status *grouping* (pre-trip / during-trip / post-trip / canceled-declined-expired) is directly observed; the full enumerated status vocabulary is not. All status claims below use the observed grouping + the article snippets that did render.
- Interhome's B2C site is delivered on HomeToGo infrastructure (cdn.hometogo.net assets observed); no claims are built on this.

---

## Product Observations

### Airbnb

All observations Tier-1 (official help center) unless noted. Evidence layer A.

**Positioning / supply model**
- Consumer-facing root surfaces a "Where / When / Who" search bar over "Homes"; hosting entry point is "Airbnb your home" / "Become a host." (site root / host landing)
- Help-center role tabs: Guest / Home host / Experience host / Service host / Travel admin — the home-stay venue is one lane of a wider platform that also sells Experiences, Services, and (per booking help) hotel stays. [A]
- Guest help tree groups: Searching and booking; Your reservations as a guest (status/changes/cancellations/checking in/out/issues); Payments and pricing; Account (incl. Identity verification); Reviews; Safety. [A]
- Host-side surfaces observed: Listings / Listing editor / Booking settings / calendar / Today tab / Earnings (where completed reservations are found); Superhost status program with response-rate requirements. [A]
- Co-hosts exist (find a co-host; co-host management). [A]

**Booking flow (article 85)**
- Two booking modes on homes: **Instant Book** ("Confirm and pay") and **reservation request** ("Request to book": add payment info, review policies and terms, message host, submit). [A]
- Hosts "typically respond within 24 hours" to requests; if declined or no response in 24h, no charge and guest is free to book elsewhere. Charge happens on host acceptance (India-ruble exception noted by the article: charged at request, full refund on decline/expire). [A]
- Pre-booking conversation lane: guests can contact/message hosts before booking; hosts may send a **special offer**, an **invitation to book**, or a **pre-approval** that lets the guest auto-book the inquired dates. [A]
- Identity verification may be requested during booking ("helps us ensure the safety of our community"); "reservation screening" and listing availability are named as reasons a reservation may not complete. [A]
- Booking requirements article: basic info about the guest is needed to book. [A]
- Some hosts require a **rental agreement**; the requirement and terms must be disclosed prior to booking. [A]
- Guest profile shown to hosts pre-booking is limited; profile photo is not shared until after booking. [A]
- Related booking surfaces: booking for someone else; group reservations with invited guests; split stays (two listings for one longer stay); 28+ nights long-stay lane. [A]

**Instant Book (host article 1510)**
- Instant Book = guests "that meet a host's requirements" book immediately without host approval; hosts set guest requirements (e.g., requiring positive reviews from other hosts). [A]
- Instant Book applies to all available dates on the host's calendar; it can be switched per listing under Booking settings. [A]
- Exceptions: bookings within 48 hours of check-in needing arrival outside the check-in window become Request-to-Book for the host to accept. [A]
- Instant Book positively affects response rate and search placement; tied to Superhost criteria. [A]

**Calendar / inventory management**
- Host calendar article (447) is the calendar's home; calendar sync to another website is supported (article 99) and **double bookings** may occur when synced — resolution is to cancel one of the reservations. [A]
- Trip changes: guests may request changes; Instant Book guests may extend nights with instant confirmation; otherwise trip-change requests flow between guest and host. [A]

**Pricing / fees (topic 1355)**
- Service fee "charged when a booking is confirmed." [A]
- Host-set custom prices override default/minimum for specific dates or periods (holidays, weekends, longer reservations). [A]
- Cleaning fee: one-time, set by the host. [A]
- Crossed-out prices shown only for true discounts ("at least 10% lower than usual" — precise threshold kept in notes). [A]
- **Hosts may not collect any additional fees or charges outside the platform unless expressly authorized.** [A]

**Payments / cancellations (topics 1354/1356/1367)**
- Guest charged on host acceptance; no charge on decline/expire (see above). Payment-plan (installment) options exist (Klarna article). [A]
- Cancellation policies are **set by the host and vary by listing** (article 4025/4052 title text). [A]
- Guest cancels from Trips; pending un-accepted requests can be withdrawn via the message thread. [A]
- **Host-initiated cancellations**: full refund, or rebooking assistance at comparable pricing. Hosts must cancel themselves (never ask the guest to cancel). [A]
- **Major Disruptive Events Policy** for large-scale events preventing completion. [A]
- Paid **extended cancellation** option: pay the platform to extend the free-cancellation window up to 24h before check-in. [A]
- Service-fee refundability criteria exist for home stays. [A]
- Refunds/reimbursements machinery ("Guest refunds and reimbursements" topic; AirCover for guests: "If there's a serious issue with your Airbnb home that your host can't resolve, we're here to help"; AirCover for Hosts on the hosting side). [A]

**Reservation status (article 363 + topic 1596)**
- Statuses grouped as: pre-trip / during-trip / post-trip / canceled-declined-or-expired. [A — grouping observed; enumerated list behind JS]
- "Pending" status: host must respond to a request, or identity verification is in progress. [A]
- Guests find reservation status in Messages or Trips; hosts check it in Today tab, messages, or calendar. [A]

**Reviews**
- Review topics for both sides: "Review basics for everyone," "Reviewing your host," "Understanding reviews as a host," "After a review is submitted." Two-sided review architecture (guest reviews host/home; host reviews guest). [A]

### Homes & Villas by Marriott Bonvoy

All observations Tier-1 (official About & FAQs page). Evidence layer A.

**Positioning / supply model**
- "Private Homes With The Assurances Of Marriott"; launched 2019; "focus only on the premium and luxury tier of rental homes"; "Marriott works with select property management companies to ensure that every home listed can be serviced at a standard expected of Marriott Bonvoy." [A]
- **Professionally Managed Homes Only**: individual homeowners cannot list directly — "Individual homeowners will need to sign up with one of our property management companies." PMCs verify each home meets standards (quality, safety, design, service); each home is evaluated "either in person or digitally" before listing. [A]
- PMCs are reviewed/selected by Marriott "based on their expertise, compliance with local regulations and service standards"; a partner-contact funnel exists for PMCs. [A]
- Site surfaces: Destinations, Collections ("Curated Collections"), Saved Homes, My Trips (/lookup-reservations), Help. [A]

**Booking modes**
- "The majority of homes listed on our site can be booked instantly. In some instances, your reservation may be 'inquire to book', or a 'non-instant book.'" [A]
- **Non-instant Book**: "you can submit a reservation and payment on our site, and the relevant property manager will confirm the booking with you within 24 hours." [A]
- **Inquire to Book**: "Contact Property Manager" button; guest submits requested dates and travel-plan details; "the property management company will reach out to the homeowner on your behalf and come back to you with availability and pricing." [A]
- Advance-booking floors: ≥2 days before check-in for card bookings, ≥3 for points bookings. [A]

**Payments / pricing**
- Acceptable payments: major credit cards and Marriott Bonvoy points; no gift cards or Free Night Certificates. [A]
- Deposit schedule: full amount at booking, or split "into two payments" depending on the home's policy — 50% at booking + 50% at 14/30/60/90 days before arrival; bookings inside the window are charged 100%; 90-day-policy first half is non-refundable. (Product-specific policy tables — details kept here, not in the Type document.) [A]
- Failed second-deposit collection triggers a 72-hour cure link, else reservation cancels. [A]
- Cash & Points and points payment mechanics; 100% deducted at reservation for points/cash+points. [A]
- **Security deposits**: some homes require one; collected either at booking (itemized separately; "automatically refunded 7 days after departure if there are no claims of damages" — precise number kept in notes) or collected directly by the PMC post-confirmation, who is then responsible for collection and return. [A]
- Ancillary charges (pet fee, cart passes, pool fees, grocery pre-stock, extra housekeeping) are **handled by the property management company after reservation confirmation**. [A]
- "Due Upon Arrival" fees (commonly resort or HOA fees) collected directly by the PMC at arrival. [A]
- Some homes require a **rental agreement** (sent by the PMC after booking, sometimes with return deadlines to keep the reservation) or a **liability waiver** (recreational amenities). [A]
- Government-occupant taxes due at arrival are indicated on the listing. [A]

**Cancellation**
- Per-home cancellation policy displayed on the listing and confirmation email; policies "very different than hotel cancellation policies"; "Refunds are not granted if requested past the established cancellation window." 14/30/60/90-day policy ladders with a 48-hour post-booking full-refund grace; hotel-elite same-day-cancellation benefits explicitly do not apply. [A]
- Reservations canceled via the Lookup Reservation function; PMC assists. [A]

**Stay operations / support**
- Stay support runs through the PMC: questions, broken/missing items, arrival changes, special requests — contact details come "in your pre-arrival communications"; "24/7 local support team" guaranteed per listing standard. [A]
- Every home guaranteed: 24/7 support, high-speed Wi-Fi, TV, kitchen essentials, premium linens/towels, bathroom amenities, hair dryer, smoke and CO detectors where fuel-burning appliances present, professional cleaning pre/post stay. [A]
- House rules "different for each home," communicated pre-arrival by the PMC, printed in the home. [A]
- Check-in/out times vary by home; disclosed on the listing page. [A]
- Damage during stay: report to PMC; PMC assesses after every stay and works with the guest. [A]
- Receipt/folio via My Trips (reservation lookup by number + last name); platform "sits on its own website" — not visible in Marriott.com/Bonvoy app; loyalty points awarded/deducted offline. [A]

**Reviews / trust**
- No guest-facing review corpus at research time: "we do not have reviews from our guests at this time… You will receive a survey after your stay" (FAQ also references introducing reviews later). [A]
- Trust rests on PMC vetting + brand standards + guaranteed minimums rather than a two-sided review system. [A]
- Add-on protection products sold at checkout: Allianz travel insurance; WeatherPromise (weather-contingent automatic payout). [A]

### Interhome

All observations Tier-1 (official "How the platform works" + root). Evidence layer A.

**Positioning / supply model**
- Root: "European specialist in the rental of holiday homes and apartments" "since 1965"; search by dates + guests; destination/region browsing. Vendor-stated portfolio counts kept in notes only. [A]
- **"Our role": "Interhome operates as a provider of vacation rentals… Interhome manages and provides the accommodation itself, from reservation to check-in, cleaning, and guest support."** Booking = direct contract with Interhome (or the relevant local office); Interhome handles "booking confirmation, payment processing, key handover, and local customer service during your trip." [A]
- Third-party layer: "In some cases, Interhome also offers vacation rentals of third-party providers" — for those, "rental contracts are entered into directly with the provider and/or the owner of the property," Interhome passes on information and payment obligation, complaints/cancellations go to the provider. [A]
- **"Since Interhome is not an intermediary marketplace for the Interhome offers, the ranking of offers is not influenced by commissions from third-party providers, unless third-party offers are listed."** [A]
- Owner side: "Rent out your property" funnel and a logged-in **Owner Portal**; marketing copy: "your property is protected, your guests are supported, and your income is optimised." [A]

**Offer management / ranking**
- Offers are "either part of our managed portfolio or supplied by our trusted providers"; every accommodation "reviewed and quality-checked"; unavailable properties (renovations, owner restrictions) removed from search. [A]
- Own-offer data "maintained directly by Interhome or by our local partners via secure internal systems"; third-party offers arrive via APIs/static feeds, updated "at least once a day." [A]
- Ranking by relevance (location, dates, guests, amenities), popularity/quality (property standards, guest satisfaction, historical booking data), price and availability. [A]

**Reviews policy**
- Reviewers "must be able to provide satisfactory evidence of having booked and spent holidays" in the property; identity/email validation required; **owners and property managers may not review their own properties**; reviews are one-sided (guest → property/service); reviews don't replace formal complaints. [A]

---

## Cross-product Comparison

| Aspect | Airbnb | Homes & Villas by Marriott Bonvoy | Interhome | Layer |
|---|---|---|---|---|
| Unit of supply | host-listed home/room listing (also hotels, a drift surface) | home/villa listed by a PMC | managed holiday homes + third-party provider offers | A×3, realization varies |
| Supply-side actor | individual owner or host (co-hosts possible) | property management company | provider + local offices + third-party providers | A×3 — posture is the variant axis |
| Listing content | photos, amenities, house rules, booking settings, calendar | listing page w/ rate card, check-in times, house rules | offer w/ quality-vetted data maintained in internal systems | A×3 |
| Availability management | host calendar; external sync; double-booking cancel-one | PMC inventory feeds the platform; advance-booking floors | internal/partner systems; 3rd-party feeds ≥daily | A×3 |
| Priced dated stays | host-set nightly + custom/seasonal dates + cleaning fee | nightly rate + taxes/fees rate card | per-stay/per-night price indications | A×3 |
| Guest search | destination + dates + occupancy (+ filters, incl. Instant-Book filter) | destination + dates + occupancy filters; AI-assisted search | dates + guests; destination/region browsing | A×3 |
| Booking modes | Instant Book vs Request-to-Book (24h response; charge on accept; no charge on decline/expire) + pre-approval/special offer/invitation lanes | instant (majority) vs Non-instant (pay now, PMC confirms ≤24h) vs Inquire-to-Book (availability+pricing returned) | provider booking (direct contract); third-party offers forwarded to provider | A×3 — approval gate is variant, mediated transaction is invariant |
| Payment | platform collects; installments exist | platform collects (card/points/cash+points; deposit schedule; 72h cure) | payment processing by the provider | A×3 |
| Cancellation | host-set policy ladder; host-cancel → full refund/rebook; disruptive-events policy; paid extended window | per-home 14/30/60/90-day ladders; 48h grace; no refund past window | own terms; third-party complaints routed to provider | A×3 |
| Booking-state grouping | pre-trip / during-trip / post-trip / canceled-declined-expired; pending = host response or verification | submit → (PMC confirm ≤24h) → confirmed; lookup via reservation number | booking confirmation by provider | A×2 + A (weaker for Interhome) |
| Fees rule | no off-platform fee collection | ancillary fees disclosed pre-booking; PMC-charged after confirmation | provider-set offers | A×2 (Airbnb explicit rule; H&V disclosure practice) |
| Messaging / contact lane | in-app messaging before/during/after booking | "Contact Property Manager" + pre-arrival comms | local offices, key handover by staff, on-site service | A×3 — realization varies widely |
| Stay-time operations | check-in instructions, house rules, trip changes, issues surface | PMC 24/7 support, house rules communicated, damage reported to PMC | key collection arranged by staff, on-site service | A×3 |
| Trust machinery | identity verification, reservation screening, limited pre-booking profile, rental agreements | PMC vetting, brand standards, rental agreements, liability waivers | quality checks, verified-stay reviews, owner self-review ban | A×3 — architecture varies |
| Reviews | two-sided (guest↔host), booking-anchored | none at research time; post-stay surveys | one-sided verified-stay with identity validation | A×3 — posture varies; NOT definitional |
| Damage money | AirCover for Hosts (named in help tree) | security deposits (platform- or PMC-collected) w/ claims refund | (not sampled in detail) | A×2 — partial; kept cautious |
| Host earnings | Earnings surface; completed reservations there | PMC settles with homeowner off-platform | owner portal; "income optimised" | A×3 — settlement locus variant |
| Loyalty / add-ons | gift cards/credits; experiences/services/car/rides add-ons | Bonvoy points/Elite credits; Allianz insurance; WeatherPromise | travel extras; local-office service | A×3 — single-product layers |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a Vacation Rental Marketplace:

1. **Host-published stay-unit listings as the supply of record.** Accommodation units (entire homes/apartments; sometimes rooms within homes) are individually listed under their own identity — photos, amenities, house rules, calendar — by the party that controls them (an owner or an appointed manager/caretaker). The inventory is privately held and unit-granular, not property-operated room blocks. Remove → property-operated accommodation retail (hotel booking) or a property catalog.
2. **A pooled two-sided venue around dated-stay search.** Guest side: search the pooled listing population by destination + dates + occupancy and compare priced offers. Host side: listing management (content, calendar, rates, booking settings) inside the same platform. Remove → a single-property booking engine (no pooled venue) or a directory/catalog (no transactable inventory).
3. **A platform-executed dated-stay booking transaction.** Reserving specific dates of a specific unit happens through the platform: the platform takes the reservation (immediately, or with host/manager approval as a variant gate), collects payment, issues confirmation as a distinct state, and administers changes and cancellation against the listing's policy. Remove → enquiry-routed housing offers with off-platform completion (property-listing territory) or pure comparison/search (metasearch territory).

Jointly-held load-bearing checks:
- 1 alone = a property/unit catalog.
- 2 without 3 = a short-stay listings venue (property-listing-platform territory; see Boundary Findings).
- 3 without 1+2 = booking machinery over someone else's inventory (booking engine).
- 1+2 without 3 = listings marketplace where interest ends at inquiry.
- 1+3 without 2 = direct-booking machinery without the pooled market.
- 2+3 without 1 = generic accommodation retail (hotel-booking territory).

### L1 — Common Mature Structure

Very common in mature products; not required for recognition:

- **Availability calendar per listing** with dated pricing (seasonal/custom pricing) and calendar-sync capability; double-booking detection/resolution where external sync exists.
- **A booking-state machine** visible to both sides — request/pending (with host/manager response deadline), confirmed, changes, declined/expired, canceled — grouped across pre-trip, during-trip, post-trip.
- **Host/manager-set cancellation policy ladders** enforced and refunded through the platform; host-initiated cancellation remediated (full refund or rebooking help).
- **Platform-collected payment** with refund on decline/expiration; fee layers (service fee on confirmation; cleaning fees; ancillary fees disclosed pre-booking).
- **Guest trip-management surface** (trips/reservation lookup, receipts/folios) and **host earnings visibility**.
- **Listing-detail surfaces** with photos, amenities, house rules, check-in/check-out windows.
- **A guest↔supply contact lane** (in-app messaging or managed contact with the manager/provider) operating before, during, and after booking.
- **Stay-anchored reviews** — architecture varies (two-sided P2P; one-sided verified-stay; absent-at-brand-pole) — so held as common structure with variant postures, not definitional.
- **Identity/reservation screening and disclosure machinery** (identity verification requests, disclosed rental agreements, disclosed fees).
- **House rules + check-in coordination** as named, user-visible artifacts.

### L2 — Variant / Optional Structure

- **Supply posture** — the dominant variant axis: P2P individual hosts; professional property management companies (homeowners cannot list directly); provider-owned/managed portfolio (venue and supply vertically integrated, self-declared "not an intermediary marketplace" for own offers); mixed provider+third-party layers.
- **Booking-mode mix** — instant vs approval-gated vs inquiry-first; per-listing and per-product choices.
- **Business model** — per-booking commission/service fee; brand/curator layer over managers; provider margin; subscription-for-supply models exist in the wider market (not directly verified this pass — weak wording).
- **Trust architecture** — platform verification + two-sided reviews; manager vetting + brand standards; curated selection + verified-stay one-sided reviews.
- **Settlement locus** — platform payout to hosts vs manager/provider-borne settlement (security deposits and ancillary charges collected post-confirmation by the manager).
- **Stay-length lanes** (e.g., long-stay 28+ night lane), group reservations, booking-for-someone-else, split stays.
- **Property-type breadth** — whole homes, apartments, villas, chalets, rooms; hotels on the same venue (overlap zone with hotel booking).
- **Loyalty integration, travel insurance, weather guarantees, concierge add-ons, co-host networks, Superhost-class status programs.**
- **Identity substrate** — email/platform account, loyalty-program account; no evidence that phone-number identity is definitional (and no reason to think so).

### L3 — Vendor-specific (research notes only)

Airbnb: AirCover (guest/host) naming; Superhost program (90% response-rate figure — notes only); Split Stays; "Airbnb-friendly apartments"; experiences/services/car/rides/airport-pickup/grocery/luggage-storage add-ons; Klarna installments; India-ruble charge-at-request refund flow (up to 15 days — notes only); crossed-out-price ≥10% true-discount rule (notes only); Cuba/Japan-specific booking regimes; Airbnb.org; co-host marketplace; ResortPass/Bounce partnerships; "book up to 2 years ahead" (notes only).
Homes & Villas: Bonvoy Cash & Points mechanics (min 1,000 points — notes only); Elite Night Credit promos; 14/30/60/90-day named policy ladders + 48h grace (notes only); 72h failed-deposit cure window; 7-day post-departure deposit auto-refund; WeatherPromise; Allianz travel insurance; reservation-number prefixes M/H; Lookup Reservation by number+last name+check-in date+email; guaranteed in-home minimums list; FAQ claim of "new offering" despite 2019 launch (vendor copy, recorded as-is).
Interhome: local offices / key-collection-by-staff model; "at least once a day" third-party feed refresh; 18+ reviewer age rule; HHD review-policy legalese; member-of-Swiss-Tourism-Federation badges; HomeToGo-powered delivery stack (observed, unused for claims).

## Vendor-specific Findings

- The marketplace-vs-provider self-description split is itself evidence: the P2P pole builds its identity on host-side listing management; the provider pole explicitly denies being an intermediary for its own offers. The Type-level abstraction must therefore be written so that the *venue + listing + mediated dated-stay booking* is the core while the *contractual counterparty* (host, manager, provider) and the *fee vocabulary* (service fee vs provider margin) are variant realizations.
- Two-sided review symmetry is NOT invariant: the P2P pole reviews both sides, the provider pole reviews properties (verified-stay, one-sided), the brand pole has no review corpus at all. Review architecture tracks supply posture.
- Approval gating is NOT invariant either: instant booking dominates one pole's majority practice ("majority of homes… booked instantly") while another pole's identity was built on request-to-book traditions; both ship both modes plus inquiry lanes.

## Boundary Findings

1. **vs Hotel Search / Booking Platform (§26) — DISCHARGES the hotel pass's joint-review flag.** Seam: **inventory character + supply-side actor.** Hotel booking aggregates property-operated accommodation (rooms/units in properties run by an operator, sold by rate, multi-seller retail); a vacation rental marketplace's defining surface is the host-published, individually controlled unit listing with its own calendar and rules, and the booking is a stay in *someone's* home, not a room product. Supporting evidence: the brand-pole FAQ explicitly contrasts "Booking a Home vs Booking a Hotel" (cancellation policies differ; hotel amenities/service absent); the P2P pole lists hotels on the same venue — the overlap zone — but hotel inventory there rides on the marketplace loop rather than defining it. Remove the host-listed whole-unit supply and host-side venue machinery → hotel booking; remove property-operation from hotel retail → this Type. Keep-both.
2. **vs Property Listing Platform (§17) — DISCHARGES the listings pass's held seam.** Seam: **transaction character.** Housing-offer venues route interest (enquiry/lead/viewing) and complete off-platform with a market-state lifecycle (sold/let-agreed); the vacation rental marketplace executes the dated-stay booking as the core transaction (date hold + payment + confirmation + cancellation administration) inside the platform. The historical check agrees: pre-booking-machinery vacation-rental listing sites are ancestors of the listings Type, not of this one — the mediation is what makes the venue a *marketplace* (consistent with the listing-marketplace pass's booking-vs-inquiry seam). Keep-both.
3. **vs Boat / Yacht Charter Platform (§18) — RE-CONFIRMS the charter pass's seam from this side.** Same two-sided time-based rental skeleton (listed asset, calendar, deposits, cancellation ladders, owner consoles). Differentiator: vessel-operation semantics (license/skipper qualification, operating deposits, dock handover, weather contingency). Remove vessel-operation semantics from a charter venue → it collapses into this Type; add accommodation-stay semantics to a charter venue → it becomes one. Keep-both.
4. **vs Online Travel Agency (§26) — consistent with the OTA pass's held seam.** Center of gravity: this Type's defining surface is host-side listing management and host-guest marketplace mechanics; traveler-first multi-supplier retail (shopping cart over many suppliers' products) is the OTA. The provider-pole product in-sample shows a venue that retails its own portfolio — a supplier-retail posture one seam over; the third-party layer in the same product shows the OTA posture appearing *inside* the venue. Keep-both; note the posture continuum as an anti-overfit caution, not an alias.
5. **vs Hostel / Campground Booking Platforms (§26)** — inventory-domain siblings confirmed: the demand-side loop is shared; the inventory semantics differ (bed-level shared rooms; campground sites/spaces vs whole private units with host-set house rules). Consistent with both sibling passes' partition observation. Keep-both.
6. **vs Short-term Rental Management (§17, unprocessed — forward note).** This leaf is the demand-side venue + host-side storefront; the §17 sibling (pre-flagged by the hotel-PMS pass) is the operator-side system of record for unit portfolios (owner settlements, cleaning/lockbox ops, direct-booking sites). Expected seam, held for that pass: operating a distributed unit portfolio vs operating a marketplace venue.
7. **vs Travel Review Platform (§26)** — stay-anchored reviews exist here as a trust layer bound to real bookings inside the transaction venue; the review corpus is not the Type's record. Consistent with the travel-review pass.
8. **vs Metasearch / Vertical Search (§02.02)** — searching others' inventory and handing off vs operating the booking transaction; the inquiry lane inside this Type still ends in a platform-executed transaction where booking machinery exists.

## Uncertainties

- **Vrbo/Plum Guide/9flats unreachable** — the request-to-book "origin tradition" and curated-vetting pole are described here only via in-sample evidence (Airbnb's approval modes; the brand pole's vetting) and sibling-pass records. No Vrbo-specific claims are made.
- **Airbnb's enumerated reservation-status vocabulary** sits behind JS; only the status grouping and specific states (pending, decline/expire-no-charge) are asserted.
- **Subscription-for-supply business models** (commonly attributed to one unreachable vendor family) — asserted at market-knowledge strength only, kept out of the Type document.
- **Host-payout timing/cadence mechanics** not directly documented in-sample (Earnings surface observed; payout schedules not fetched) — kept generic.
- **Damage-deposit machinery at the P2P pole** observed only via help-tree surface names, not article depth — kept cautious.
- Whether the wide add-on ecosystems (experiences/services/rides, weather guarantees) will re-shape the Type's boundary is era-current; monitored as drift, not definitional.

## Final Synthesis

A Vacation Rental Marketplace is a two-sided booking venue whose unit of supply is the individually controlled accommodation unit, listed on the platform by the party that controls it, with the platform executing the dated-stay booking transaction — reservation of specific dates, payment collection, confirmation, and cancellation administration — across a pooled, searchable listing population. Everything else commonly seen (identity verification, two-sided reviews, instant-booking defaults, service-fee economics, loyalty add-ons) is common mature structure or variant posture shaped by the supply side, which ranges from individual owners through professional property managers to vertically integrated providers. The Type holds its identity against hotel booking (property-operated retail), property listings (enquiry-routed offers), charter platforms (vessel-operation semantics), and OTAs (retail center of gravity) by the joint hold of host-published unit listings + pooled dated-stay search + platform-executed booking.
