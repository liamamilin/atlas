# Boat / Yacht Charter Platform

## Overview

A **Boat / Yacht Charter Platform** is a booking platform that connects people who want to use a boat for a defined period (charterers) with the owners or operators of boats available for charter (the supply side). Its inventory is identified vessels — sailboats, catamarans, motorboats, yachts, and related craft — presented with their type, size, capacity, home base, rates, and options. Its transaction unit is the **charter booking**: a specific vessel reserved for a specific period, from a few hours to several weeks. The platform mediates the commercial transaction between the two sides: it carries the offer, collects and administers the payment, and settles the supplier through the platform rather than privately — when and how funds move varies by product.

The defining core is deliberately small:

```text
Vessel inventory (identified boats held by owners/operators)
  └── Time-bound charter booking (specific vessel × defined period × party)
      └── Mediated transaction (offer → payment → payout, administered by the platform)
```

Everything else commonly associated with these products — skipper and crew add-ons, license checks, security deposits, marina handover checklists, reviews, instant booking — is standard machinery that mature products add on top, not what makes the Type what it is. The definition also covers older and differently shaped implementations: a traditional charter broker matching clients with crewed yachts, or a local charter-fleet operator taking bookings for its own boats, both fit the same core without any of the modern marketplace features.

When the inventory stops being a vessel that is *operated* — no self-operation, no qualification, no operating deposits — the product is drifting toward a different Application Type (most closely Vacation Rental Marketplace or Tour & Activity Marketplace).

## Users & Context

**Charterers** are the demand side: individuals, families, or groups booking a boat for a day trip (swimming, fishing, parties, sightseeing) or a multi-day sailing vacation (island hopping, flotillas, crewed cruises). They range from people with no boating experience (who book a boat *with* a captain) to licensed sailors (who take a *bareboat* charter and operate it themselves).

**Suppliers** are the supply side, in three recognizable forms:

- private boat owners renting out their own vessel when they are not using it;
- professional charter companies operating fleets of charter-ready boats from marine bases;
- charter brokers/agencies that curate and resell professional fleets' capacity with human assistance.

**Platform staff** (support, and in agency models human advisors) assist with matching, quotes, documents, and dispute or damage adjudication.

The work context is travel and leisure planning on the demand side (web and mobile, often months or days before the trip), and small-business operations on the supply side (listing management, calendar, inquiries, payouts). The charter itself happens offline — at a marina or dock — but the platform governs what must be true before anyone steps aboard: qualification, payment, deposit, and a documented handover.

## Core Model

### The defining core

Three structures carry the Type:

- **Vessel listing** — an identified boat as bookable inventory: vessel type and model, size, guest capacity, home base or cruising area, photos, equipment, and rate structure. The listing is held by an owner or operator, who controls its availability and pricing. Without identified bookable vessels there is no charter platform.
- **Charter booking** — a reservation binding one specific vessel to a defined period (hours, days, or a week) and a party size. The booking is the object every other thing attaches to: extras, documents, payment, deposit, handover, review.
- **Mediated transaction** — the platform (or agency) sits between charterer and supplier for the money: the charterer's commitment is created by accepting an offer or quote; payment is collected or scheduled by the platform; the supplier is settled through the platform under the product's payment model. Without this mediation the product is a listings directory, not a charter platform.

### What mature products add

These capabilities are present across the researched sample and expected in practice, but they are not part of the definition:

- **Discovery and search** — find boats by destination or marine base, dates, boat type, size, capacity, and price; common filters include "license-free" boats, fishing charters, and luxury/crewed charters.
- **Inquiry → offer → confirmation lifecycle** — the charterer requests a quote or sends a booking inquiry; the supplier (or platform) responds with a priced offer including chosen extras; acceptance creates the binding booking. Some products also offer instant reservation at the listed price.
- **Extras as priced add-ons** — skipper, crew (cook, hostess, deckhand), fuel, provisioning, watersports equipment, safety gear, pets, insurance. The base rate rarely covers everything; the offer itemizes what is included.
- **Skipper/crew as the alternative to self-operation** — the single most characteristic option in the model: either the charterer operates the boat (bareboat) or a bookable professional operates it for them.
- **Qualification gating** — for bareboat charters, the platform or supplier requires proof of competence: a boating license or certificate appropriate to the cruising area, sometimes a radio certificate; week-long charters may also require a crew list submitted in advance. Renters' stated experience and past reviews can figure in the supplier's acceptance decision.
- **Security deposit / damage settlement** — a reserved amount (pre-authorization, hold, or cash at handover) backs potential damage or cleaning costs, with a defined claim path: damage reported and documented, repair cost assessed, deducted from the deposit or charged up to the reserved amount, with platform adjudication if the parties disagree.
- **Insurance products** — hull/liability coverage held by the owner (charter boats are insured by their owners as a baseline), plus optional renter-facing products such as cancellation insurance or deposit protection.
- **Handover (check-in / check-out)** — a formal joint inspection of the boat at the base: documents (passport, license, deposit) presented at the operator's office, a condition checklist walked through and confirmed, defects reported immediately; the same procedure in reverse at return, ending with deposit release if all is well.
- **Cancellation and refund ladder** — refund depth tied to how far before the trip the cancellation happens; weather is a recognized contingency in the domain even where specific policies vary.
- **Two-sided reputation** — reviews of boats/owners and, in owner-renter marketplaces, reviews of renters, feeding acceptance and ranking decisions.
- **Messaging** — in-platform communication between charterer and supplier (or with an advisor) to customize the trip before booking.
- **Supplier console** — listing creation, availability calendar, pricing management, inquiry inbox, and payout/earnings tracking.
- **Booking documents** — booking confirmation, and in agency models a charter contract signed by customer and agency; operators at the base may have their own paperwork.

### One structure, many implementations

The core is conceptual; products realize it differently:

```text
Concept:  Vessel inventory supply
          → private owners (peer-to-peer) / professional fleets / curated broker partners

Concept:  Booking commitment
          → instant reservation at listed price / offer acceptance / advisor-prepared quote

Concept:  Payment administration
          → card charged at acceptance with funds held until trip completion
          / bank-transfer installments (deposit + balance before departure)
          / invoice issued at the base

Concept:  Qualification
          → platform-published local rules / agency-verified certificates / checked at handover
```

A reader who has only seen one implementation — say, an app for renting a pontoon by the hour — should still be able to recognize a European crewed-yacht charter agency as the same Type from the core model.

## How It Works

The charter lifecycle runs from discovery to post-trip settlement:

```text
Discover
→ inquire / request quote (or instant book)
→ receive offer (base rate + extras + deposit terms)
→ accept → booking confirmed
→ pay (charged / installments scheduled)
→ prepare (documents, license, crew list, provisioning)
→ handover at the base (check-in: documents + deposit + condition checklist)
→ the charter period
→ return (check-out: condition check → deposit settlement)
→ payout to supplier + reviews (+ damage claims if any)
```

**Discover.** The charterer searches by destination or base, dates, boat type, capacity, and budget. Two trip shapes dominate: day trips (often captained, priced by the hour or day) and multi-day charters (priced per week in many sailing destinations, where boats commonly turn over on a fixed weekly rhythm).

**Inquire and offer.** The charterer sends an inquiry or quote request, often exchanging messages to customize the trip. The supplier or platform returns a priced offer: base charter rate, chosen extras (skipper, crew, provisioning, equipment), insurance options, deposit terms, and platform fees. Accepting the offer creates the binding booking. In marketplace products the charterer may instead book instantly at the listed price; in agency products an advisor assembles the offer.

**Pay.** Payment mechanics vary by posture, but the money moves through the platform rather than settling privately. Observed patterns include charging the charterer's card in full at acceptance and holding the funds until the trip is completed (a marketplace posture), and staging installments — a first payment at confirmation, the balance a fixed period before departure (an agency posture). Payout timing to the supplier likewise varies by product. Off-platform payment is prohibited in marketplace postures because it forfeits the platform's protections.

**Prepare.** For a bareboat charter the charterer assembles qualification documents (license or certificate, sometimes a radio certificate) and, for week charters, a crew list; the agency or operator may verify these before departure. Skippered charters shift this burden to the booked crew.

**Handover.** At the marine base, the charterer presents documents and the deposit, walks the boat through a condition checklist with the operator's staff, and confirms the state of the vessel. This is the transition from "paid booking" to "vessel in the charterer's (or skipper's) hands".

**The charter and the return.** During the charter period the boat is operated — by the charterer (bareboat) or the booked crew. At return, the check-out inspection mirrors the check-in; if all is well the deposit is released in full. Damage found at return triggers the claim path: documentation, assessment, deduction from the deposit or charge up to the reserved amount, with the platform adjudicating disputes. If a skipper was booked, responsibility for operation-related damage follows the skipper in some supplier arrangements.

**Settle.** The platform settles the supplier according to its payment model (in the observed marketplace posture, shortly after trip completion), the charterer reviews the boat and the owner/captain, and the owner may review the renter.

## Interfaces

### Search / discovery surface

The charterer's entry point.

- typical information: destination or base, date range, boat type, capacity, price; charter-type categories (license-free, fishing, luxury/crewed)
- primary actions: search, filter, save/favorite, open a listing

### Vessel listing detail

The unit of supply.

- typical information: photos, vessel type/model/size, capacity, base location, equipment, rate structure (hour/day/week), extras and their prices, deposit and insurance terms, owner/operator profile and reviews, availability
- primary actions: message the owner, request a quote, book instantly (where offered), choose extras

### Booking / checkout surface

Where the offer becomes a commitment.

- typical information: itemized price (base + extras + fees + deposit terms), payment schedule, cancellation policy, required documents
- primary actions: accept offer / confirm booking, pay, sign charter contract (agency models)

### Booking management (charterer side)

- typical information: upcoming and past charters, payment status, documents due (license, crew list), messages
- primary actions: message supplier, modify or cancel, access booking documents

### Supplier console (owner / operator side)

- typical information: listings and their performance, availability calendar, pricing, incoming inquiries and offers, renter profiles and reviews, earnings and payouts
- primary actions: create/edit listing, set availability and prices, respond to inquiries, send offers, accept or decline requests, track payouts

### Advisor / agency surface (agency posture)

Where a human intermediary works the same objects.

- typical information: client requests, curated fleet options, quotes in preparation, charter contracts, payment schedules
- primary actions: prepare and send quotes, confirm bookings, collect documents, coordinate with base operators

## Important Rules / Behaviors

- **Self-operation is gated.** A bareboat charter is conditional on demonstrated competence — a recognized license or certificate for the cruising area, sometimes a radio certificate, and a crew list for longer charters. The universal alternative is booking a skipper. License-free rental, where it exists, is typically confined to smaller, low-power craft; the exact requirements depend on local law, and platforms surface rather than replace those rules.
- **The platform administers the money.** Payments are collected, held, staged, and settled through the platform's payment machinery rather than privately between the parties. Some products hold charged funds until the trip completes before paying the supplier; others stage installments against departure dates or pay out per booking. The common invariant is administration and protection, not a single payout schedule.
- **The deposit backs the operation.** A reserved amount stands behind potential damage or cleaning costs. Claims follow a documented path — report, evidence, assessment, deduction — and the platform adjudicates when the parties disagree. Where a skipper is booked, responsibility for operation-related damage may shift to the skipper.
- **Handover is a formal state transition.** The condition checklist at check-in and check-out is what makes deposit settlement possible; defects must be reported at handover, not discovered later.
- **Cancellation is priced by proximity.** Refund depth decreases as departure approaches, per the published policy ladder; exact percentages and windows are product-specific.
- **Reputation gates access.** In owner-renter marketplaces, owners choose which requests to accept, informed by the renter's stated experience and reviews; renters choose by ratings. Acceptance of a request is a supplier decision, not an automatic outcome.
- **Off-platform payment is prohibited** in marketplace postures; transacting outside the platform forfeits its payment protection, support, and dispute mechanisms (some products allow crew gratuities outside the platform as an exception).

## Variants

- **Peer-to-peer marketplace** — private owners list their own boats; platform earns service fees from both sides; offer-based or instant booking; strongest two-sided reputation machinery.
- **Professional-fleet marketplace** — charter companies list fleets; same discovery/booking machinery, more standardized weekly cadence and base operations.
- **Charter broker / agency** — curated professional supply, quote-driven booking with human advisors, charter contracts, staged payments, travel-agency financial guarantees; often the widest product lines (crewed yachts, cabin cruises, flotillas, sailing courses, river/barge cruises).
- **Day-trip / experience posture** — hourly or daily captained trips (fishing, sunset, party boats) dominate the catalog; the bareboat machinery recedes; this posture shades toward Tour & Activity Marketplace.
- **Weekly-vacation posture** — sailing-vacation markets with fixed weekly turnover, base handovers, and qualification checks; the classic yacht-charter shape.
- **Craft-scope variants** — platforms range from small craft (kayaks, jet skis, pontoons) through sailing yachts and catamarans to crewed motor yachts and gulets; some add houseboats and barges on inland waters.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Vacation Rental Marketplace | closest structural sibling | same two-sided time-based rental skeleton, but inventory is accommodation; remove the vessel-operation semantics (qualification, operating deposits, handover, weather) and this Type collapses into it |
| Vehicle Rental Platform | adjacent | also rents an operated vehicle by time, but typically operator-fleet and counter-shaped rather than marketplace/broker-shaped; no skipper/crew alternative; no weekly vacation cadence |
| Tour & Activity Marketplace | adjacent (overlapping posture) | captained day trips are sold by both; the presence of self-operated (bareboat) vessel use with qualification and deposits is what keeps a platform in this Type |
| Marina Management | different operator, different object | manages berths, dockage, and marina operations for the marina operator; a charter platform sells time-use of vessels to the public; marinas host charter bases but the systems do not merge |
| Cruise Operations Platform | different transaction shape | runs scheduled voyages selling cabins per passenger on a line-operated vessel; charter platforms sell a whole vessel's time to one party (cabin cruises on chartered yachts are the boundary case, sold as charter products) |
| Online Travel Agency / OTA | broader distributor | distributes flights, hotels, and verticals; charter platforms are vertical specialists owning the marine transaction semantics |
| Boat club / membership access model | different access model | membership entitlement to a fleet rather than per-charter mediated transactions; would be a separate Type rather than a variant (not verified against a live product in this research pass) |

## Representative Products

- **GetMyBoat** — global peer-to-peer boating marketplace; day trips through yacht charters; offer-based booking with platform-held payment.
- **Click&Boat** — European peer-to-peer yacht-charter marketplace; private owners plus a professional-fleet path; quote and instant reservation; license/skipper filtering.
- **GlobeSailor** — charter agency with curated professional partners; advisor-mediated quotes; crewed yachts, cabin cruises, flotillas, and courses.
- **Boatico** — charter agency over professional operators' fleets; weekly charter cadence; documented handover, deposit, and installment-payment mechanics.

The definition was checked against older and differently shaped implementations — traditional charter brokers and single-operator charter fleets — which fit the same core without marketplace features, to avoid defining the Type by today's dominant marketplace pattern.

## Sources

Research date: **2026-09-06**

- GetMyBoat — homepage, How It Works, For Owners: https://www.getmyboat.com , https://www.getmyboat.com/how-it-works/ , https://www.getmyboat.com/for-owners/
- Click&Boat — homepage (including FAQ), Rent out your boat: https://www.clickandboat.com/en/ , https://www.clickandboat.com/en/rent-out-your-boat
- GlobeSailor — homepage: https://www.globesailor.fr/
- Boatico — homepage, FAQs: https://boatico.com/ , https://boatico.com/information/faqs/

> Sourcing limitation: dedicated help centers for several sampled products were unreachable from the research environment (Click&Boat's help center transport error; Sailo, Boatbookings, Borrow a Boat, 12knots, and Dream Yacht Charter returned access-denied responses). Observations for those products were not used. Product-specific figures (fee percentages, claim windows, offer-validity periods, cancellation percentages) are recorded only in the Research Notes and are intentionally not stated here. Claims about qualification rules, deposits, and handover are stated qualitatively because exact requirements vary by jurisdiction and supplier.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
