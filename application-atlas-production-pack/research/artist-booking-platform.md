# Research Notes — Artist Booking Platform

Research date: 2026-09-06
Status: leaf processed under v1.1 methodology
Directory location: §27 Media, Entertainment, Creator & Culture (siblings: Talent Agency Management, Casting Platform, Audition Management, Record Label Management, Music Promotion Platform, Event Management/Ticketing siblings under §26)

---

## Research Goal

Understand what an "Artist Booking Platform" actually is as an Application Type: what object it centers on, who its parties are, what lifecycle a booking goes through, and where it begins/ends relative to Talent Agency Management, Casting Platform, Service Marketplace, Event Management, and Appointment Scheduling.

## Initial Boundary

Hypothesis before research: the Type covers software that connects performers (musicians, DJs, comedians, speakers, acts) with parties who want to book them for dated live appearances, and manages that engagement from enquiry/offer to confirmation and settlement.

Risks identified up front:

1. **Ambiguity of "artist"** — could mean musical artists only, or any live performer; could even drift toward appointment booking of individual professionals (e.g., tattoo artists) which would be a different Type.
2. **Two-sided marketplace vs agency workflow** — "booking platform" may denote either a self-serve marketplace or an agency's internal booking system.
3. **Adjacent "Talent Agency Management"** (sibling leaf) — an agency suite also handles bookings; overlap must be resolved.
4. **"Venue Management System"** (§26) — naming collision risk: music-booking tools for venues sometimes market themselves as "venue management software" while managing artist bookings, not venue spaces.

## Research Questions

- RQ1: What is the central object — enquiry, offer, hold, booking, gig?
- RQ2: Who are the parties and roles (artist, buyer, agent, venue, platform)?
- RQ3: What is the booking lifecycle and its states?
- RQ4: How are artists represented (profile, EPK, roster, pricing basis, reviews)?
- RQ5: How are commercial terms handled (quotes, fees, deposits, contracts, settlements, commission)?
- RQ6: How do marketplace vs agency-mediated vs submission-based operating models differ, and what is shared?
- RQ7: Which rules matter (holds, availability conflicts, deposits, cancellation, confidentiality of statuses)?
- RQ8: What are the main interfaces?
- RQ9: Boundary answers vs neighboring Types.

## Representative Products

Selected for different operating models, geographies, and customer levels:

| Product | Model | Segment / Level | Evidence quality |
|---|---|---|---|
| Encore Musicians ("Encore") | Two-sided self-serve marketplace (buyer-initiated enquiry) | Consumer + small events (weddings/functions/corporate), UK | A — official homepage with explicit flow |
| Gigwell | Agency-side booking management suite (agent + talent-buyer products) | Professional music booking agencies, venues, festivals; touring | A — official product pages, deep feature descriptions |
| Sonicbids | Submission-based platform (venue posts dates/slots; artists submit EPK; hold → confirm) | Independent artists + venues/promoters/festivals | B — official site, but mid-reboot; several features announced as "coming" |

Attempted and rejected as representatives:
- **The Bash** (thebash.com) — HTTP 403 on homepage, transport error on help center (2 attempts) → abandoned per source-access rule.
- **GigSalad** (gigsalad.com) — HTTP 403 (1 attempt, then abandoned in favor of Bash alternate paths; both consumer-events marketplaces).
- **Eventric** (eventric.com) — HTTP 403 (1 attempt) → abandoned.
- **AmpSuite** (ampsuite.com) — **Product Mismatch**: the domain now serves Beatport's label-management suite ("Ampsuite" = distribution, royalty accounting, publishing, contracts for record labels). Whatever its historical booking-agency functionality, current official positioning belongs to Record Label Management, not this Type. Dropped as representative.

## Sources

- Encore Musicians — https://encoremusicians.com/ (homepage; enquiry → tailored quotes → booking protection → secure payment flow; performer categories; reviews) — fetched 2026-09-06
- Gigwell — https://www.gigwell.com/ (home), https://www.gigwell.com/productivity (Productivity Suite), https://www.gigwell.com/talent-buyer (Talent Buyer Pro) — fetched 2026-09-06
- Sonicbids — https://www.sonicbids.com/ (home; EPK → submit → get booked; venue-side hold/confirm/open calendar) — fetched 2026-09-06

Source-access limitation: the largest US consumer-events marketplaces (The Bash, GigSalad) and promoter-side Eventric could not be fetched. Generalizations about "marketplace" behavior therefore rest mainly on Encore (UK) plus partial signal from Sonicbids' venue-side flow. Deep help-center / operational documentation (Gigwell knowledge base at help.gigwell.com, Encore help articles) was not fetched; precise operational facts (exact fee percentages, exact hold policies, contract clause specifics) are deliberately not asserted.

---

## Product Observations

### Encore Musicians (marketplace model) — Evidence layer A

Key observations from the official homepage:

- Positioning: "The fastest way to find and book great musicians"; buyers are wedding/private/corporate/function event hosts.
- Supply side: a browsable catalog of **13,450+ performers** organized in categories (wedding bands, string groups, singers, DJs, violinists...) with indicative starting prices ("From £250/£400/£600").
- **Booking flow (as advertised)**: "Tell us about your event → Relevant musicians are instantly alerted → Available performers respond with tailored quotes." So: event enquiry broadcast → availability-gated responses → tailored quotes.
- Trust machinery: "vetted musicians", 33,000+ five-star booking reviews, aggregate rating.
- Money: "Fast Quotes, Secure Payment, No Hidden Fees"; "Every quote you receive from a musician is all-inclusive."
- Protection & cancellation: "Booking protection"; "Free 48hr cancellations" (specific number — keep product-specific).
- Human support: a named "bookings specialist" assists buyers.
- Note: the word "enquiry" is the platform's own term for the buyer-side booking request; "quote" is the artist-side response.

### Gigwell (agency-side suite + talent-buyer product) — Evidence layer A

Key observations from official product pages:

- Positioning: "End-to-End Booking Management Platform" / "Booking Agency Software for Agents, Artists, DJs and more"; serves agents, artists, venues/talent buyers as distinct roles with dedicated products (Productivity Suite, Artist Essentials, Talent Buyer Pro, Tour IQ, Ticket Counts Pro).
- **Roster & representation**: agents create an agency-branded booking page + **EPK (electronic press kit)** per artist; embeddable on agency website/social; "Talent buyers can now review artist assets and submit a booking request from one location."
- **Workflow phrase (vendor's own)**: "From inquiry to performance" — and on the buyer side: "Streamline your venue's artist booking process **from offer generation to settlement**."
- **Contracts**: contract builder with templates ("customize and send contracts, artist riders and travel docs in minutes"), e-signature integration ("legally binding signature"); "85% contracts signed within 24h" (vendor stat — L3).
- **Money**: FlexPay online payments — card/PayPal/bank wire; "The minute a contract is signed, Gigwell automatically sends your client a direct payment link"; automated **deposit reminders**; deposits + payments tracked; vendor stat "53% gig deposits paid within 24h" (L3).
- **Holds calendar (buyer side)**: "Smart Holds Calendar — Effortlessly track multiple holds, confirmed shows, on-sale dates, and announcements"; "keeping sensitive statuses private and easily publish to Google Calendar when you're ready to share"; color-coded entries.
- **Offer sheet (buyer side)**: branded offer sheet with "customizable terms and conditions", tracked receipt/opens/forwards.
- **Artist advancing & logistics**: manage "artist advancing", travel docs, itinerary builder; artist mobile app with itinerary, contracts/deal docs, offline support, chat with agent; scheduling-conflict alerts when artists block dates or connect personal calendars.
- **Task automation**: "Actions like signing a contract trigger sequential tasks—from Marketing creating collateral to Logistics arranging artist pickups."
- **Settlements (buyer side)**: "Show Settlements — track settlements, review past show performance."
- **Discovery**: Tour IQ — venue/festival database with capacity, genre booked, distance, **radius clauses**; venue profiles with buyer contacts and announced-show calendars (powered by SeatGeek — L3 detail).
- **Ticket tracking**: Ticket Counts Pro — automated ticket count collection, market pace reports (relevant to deal-based bookings, L3).
- Contacts/CRM: centralized contacts with tags, Gmail sync.
- Reporting: real-time analytics on bookings/revenue; agency performance.
- Pricing tiers exist (Artist $49 / Agency $99 monthly-annual; L3, not for final doc).

### Sonicbids (submission-based model) — Evidence layer B (mid-reboot caveat)

Key observations from the official homepage:

- Positioning: "Get booked for more gigs"; 200,000+ artists, 1,500+ venues; artist flow summarized as "1 Build your EPK → 2 Submit → 3 Get booked."
- **EPK-centric artist profile**: tour history, ticket counts, live performance video, downloadable stage plots; "Live Stats & Booking Metrics — followers, past ticket counts, venue-level performance data."
- **Submission**: "Apply by slot, by night, or as general interest. Accept offers directly, update your calendar, and manage bookings without the usual back-and-forth."
- **Venue-side booking calendar (their own vocabulary)**: "Event-Level Booking with **Hold, Confirm & Open Status** — Manage full nights, not just artist blocks. Easily mark slots as open, on hold, or confirmed across your calendar."
- Submissions inbox + artist roster integration: "View who submitted for each date and instantly book from your preferred artist list or past performers."
- Run-of-show: door times, soundcheck windows, staff assignments, tech rider links.
- Artist performance insights: "Track real gigs, payouts, fan engagement, and show history" (implies payout handling; depth unverifiable).
- Announced-but-rolling-out features ("Smarter Booking Tools — data-driven matching... Streamlined contracts and availability"; dashboards; sponsorships) — treat announced features as weaker evidence than shipped ones.
- Reboot caveat: site states "Sonicbids is back online, starting with brand-new EPKs... Submissions, dashboards, and partner tools rolling out next." Historical Sonicbids (pre-reboot gig-subscription marketplace) could not be verified.

---

## Cross-product Comparison

| Dimension | Encore (marketplace) | Gigwell (agency suite) | Sonicbids (submissions) |
|---|---|---|---|
| Bookable artist representation | Performer profile in public catalog, category, starting price, reviews, vetting | Roster entry with agency-branded booking page + EPK | EPK profile (media, tour history, ticket counts, stage plots) |
| Who initiates | Buyer (event enquiry) | Buyer submits booking request; agent generates offer sheets; agent also hunts venues (Tour IQ) | Artist submits for posted dates/slots; venue books |
| Central object | Enquiry → quote (booking) | Offer / booking (per artist × date), holds | Submission → slot booking (hold → confirm) |
| Dated occasion | Yes — the user's event | Yes — gig dates, tours, festival slots | Yes — event nights / slots |
| Availability handling | "Available performers respond" (availability gates quotes) | Holds calendar, conflict alerts via calendar sync | Hold / confirm / open slot statuses; artist calendar updates |
| Negotiation | Tailored quotes (all-inclusive) | Offer sheets with customizable terms; contract negotiation | Offers accepted directly; "without back-and-forth" ambition |
| Contracting | Booking confirmation + "booking protection" (contract formalities not verified) | Contract builder + e-sign + riders + travel docs | Streamlined contracts announced (rolling out) |
| Money | Secure online payment for accepted quote | Deposits + payments automation (FlexPay); show settlements (buyer side) | Payouts referenced in artist insights (depth unverified) |
| Performance logistics | — (support specialist assists) | Advancing, itinerary, travel docs, mobile app, task workflows | Run-of-show notes, soundcheck, staffing, riders |
| Post-booking tracking | Reviews after booking | Settlements, reporting, ticket counts | Performance insights, payout/show history |
| Discovery machinery | Category browse + enquiry broadcast | Tour IQ venue/festival database, radius clauses | Submissions inbox, preferred-artist roster |

Convergent vocabulary across all three (evidence layer B/C): **artist profile → booking request/offer for a dated occasion → negotiation → confirmation → (performance) → settlement/review**. The "hold" as a pre-confirmation placeholder for a date appears explicitly in Gigwell (Smart Holds Calendar) and Sonicbids (Hold/Confirm/Open); in Encore's flow availability gates responses, and holds are implicit in the enquiry-response model.

---

## Canonical Model

### Level 0 — Defining Invariant

The smallest structure without which the product stops being an Artist Booking Platform:

```text
Artist / Act (bookable profile: what they perform)
└── Booking / Offer
    = artist × dated performance occasion × recorded commercial terms
    └── Confirmation lifecycle
        (request/enquiry/offer/hold → negotiation → confirmed → performed or cancelled)
```

Four properties:

1. **Bookable artist profile** — a representation of a performer/act as a bookable entity (what they do, media, pricing basis). Without it there is nothing to book.
2. **Dated performance occasion** — the booking is anchored to a specific date (event, gig, slot), not to an ongoing service relationship or generic service order.
3. **Booking/offer object with recorded commercial terms** — a request or offer binding an artist to an occasion with terms (at minimum a fee/compensation basis) that both sides can see and act on.
4. **Confirmation lifecycle** — the object moves through visible states from initial request/offer/hold to a confirmed engagement (and to performed / cancelled outcomes). Without a tracked lifecycle it is a directory or a contact list, not a booking platform.

Historical check: a pre-internet booking agency operating rosters + offer letters + contracts + date holds by phone/fax satisfies this structure — the four properties are substrate-independent. The digital products add machinery (calendars, e-sign, payment rails), not new defining structure. Solo performers and non-music performers (comedy, speakers, variety) also fit; nothing in L0 requires music or an agency.

### Level 1 — Common Mature Structure

Present in most mature products, not definitional:

- **EPK / media kit** — photos, audio/video, tech specs; the artist profile's commercial face.
- **Availability / booking calendar with holds** — hold (non-binding placeholder) → confirm; conflict detection when artists sync external calendars.
- **Contracts & e-signature** — offer sheets, artist contracts, riders, travel docs; contract signing as the binding event.
- **Deposits & payments** — deposit collection (often automated reminders), balance settlement, payment links; on the buyer side, show settlements.
- **Messaging/negotiation thread** attached to the booking.
- **Trust & track record** — reviews, vetting, ticket counts, past-show data.
- **Roster management** — preferred artists, past performers, agency rosters.
- **Reporting** — bookings, revenue, settlement performance.

### Level 2 — Variant / Optional Structure

Depends on operating model, segment, region:

- **Operating model**: open self-serve marketplace (buyer-enquiry) vs agency-mediated workflow vs submission-based venue-first platform vs artist-side self-booking tools.
- **Who initiates**: buyer enquiry, artist submission, or agent-generated offer.
- **Fee basis**: flat guarantee with deposit+balance vs door-deal/percentage splits settled after the show; ticket-count tracking attaches to deal-based bookings.
- **Touring support depth**: radius clauses, venue databases, itinerary/travel docs, advancing — heavy touring/agency segment.
- **Public discovery vs private roster**: public catalog with search vs gated agency booking pages.
- **White-label/branding**: agency-branded booking pages and offer documents.
- **Confidentiality posture**: private holds/on-sale dates until public announcement.
- **Marketplace protection features**: bounded free cancellation windows, booking protection (product-specific mechanics vary).

### Level 3 — Vendor-specific Detail (Research Notes only)

- Gigwell: Tour IQ venue database (SeatGeek-powered announced-show calendars), FlexPay payment portal, Ticket Counts Pro market-pace reports, Eco-Rider marketing, specific pricing tiers ($49 Artist / $99 Agency, annual billing), "85% contracts signed in 24h / 53% deposits paid in 24h" marketing stats.
- Encore: "Free 48hr cancellations", all-inclusive quotes promise, tree-planting/carbon-offset positioning, named human bookings specialist.
- Sonicbids: Sounds on Tap NYC series, brand-sponsorship marketplace ambitions, reboot roadmap items.

---

## Vendor-specific Findings

- Gigwell is the only sampled product that explicitly supports the **full professional touring chain** (advancing, itinerary, radius clauses, settlements, ticket counts). These are L1/L2 structures of the broader Type, concentrated in the agency segment.
- Encore's human-in-the-loop support ("bookings specialist") is product-specific positioning.
- Sonicbids' sponsorship marketplace is unrelated to the booking core (L3).

## Boundary Findings

1. **vs Talent Agency Management (sibling leaf, §27)**: the closest and most dangerous boundary. Agency-side booking suites (Gigwell-style: roster, offers, contracts, settlements) overlap heavily with what a talent agency management system must do for the bookings portion of its work. Structural test: an Artist Booking Platform centers the **booking transaction** (artist × date × terms × lifecycle) between artist-side and buyer-side parties; Talent Agency Management centers the **artist's career/agency operations** across revenue types (casting, commercials, appearances, recording deals) with contracts/commissions/finances as the spine. A booking platform can exist with no career-management object at all (Encore). Probable partial-overlap gradient; **flagged for joint review** when Talent Agency Management is processed.
2. **vs Casting Platform (§27)**: casting selects performers for production roles via audition/submission mechanics (film/TV/commercial); artist booking engages a performer for a **live dated appearance** via offer/hold/confirm. Different lifecycle vocabulary (audition → callback vs hold → confirm) and different occasion semantics. Distinct Types.
3. **vs Service Marketplace (§05.02)**: structurally similar (supply profile + demand request + transaction + reviews). The distinguishing structure is the performance-specific booking lifecycle: dated occasion, holds, contract/offer terms, deposits, settlement — none of which is generic marketplace machinery. Treated as a domain-specific Type rather than a marketplace Variant; observation recorded, no taxonomy change proposed.
4. **vs Appointment Scheduling / Appointment-based Service Business Management (§03.09)**: appointments are short, catalog-priced service slots booked against staff schedules; artist bookings are negotiated event engagements with fees, contracts, holds and (often) settlements. Distinct.
5. **vs Event Management Platform / Event Ticketing Platform (§26)**: those organize the event and sell to the audience; the Artist Booking Platform contracts the talent appearing at the event. An event's talent lineup is the booking platform's output, not its input. Distinct.
6. **vs Venue Management System (§26)**: terminology collision observed — Gigwell markets its talent-buyer product as "Venue Management Software", but its object is **artist bookings for the venue**, not physical space/event operations. When Venue Management System is processed, beware search-based mis-linking. Observation recorded.
7. **vs Music Promotion Platform / Record Label Management (§27)**: promotion markets artists to audiences/industries; label management handles recordings/royalties. Neither centers the booking transaction. Distinct. (AmpSuite's migration into label tooling — see Product Mismatch above — incidentally confirms the market separates these.)

## Uncertainties

- **Whether payment execution is definitional**: Encore and Gigwell both run money through the platform; Sonicbids references payouts but its reboot state makes depth unverifiable. Kept payment machinery at L1, with only "recorded terms" at L0.
- **Contract formalities in marketplaces**: Encore's "booking protection" implies contractual coverage, but the contract-generation mechanics were not verifiable from the fetched page; contract tooling kept at L1 with "common" strength.
- **US consumer-events marketplaces** (The Bash, GigSalad) unreachable; marketplace generalizations rest mainly on one product (Encore) plus partial signal from Sonicbids. Claims about marketplace behavior are worded accordingly.
- **Hold semantics**: "multiple holds per date" is explicit in Gigwell and Sonicbids; whether it is universal practice (industry folklore says yes) is asserted only as "common", not definitional.
- Sonicbids historical model (pre-reboot subscription-based gig application) not verified.

## Final Synthesis

The Artist Booking Platform is the software layer for the live-performance booking transaction. Its defining core is a bookable artist profile, a booking/offer anchored to a dated performance occasion with recorded terms, and a tracked lifecycle that carries that offer to a confirmed engagement. Mature products add the machinery that makes bookings practical in each segment: EPKs, holds calendars, contracts with e-signature, deposits and payments, advancing/itinerary (touring), and post-show settlements/reviews. The market realizes the same core in three operating models — buyer-enquiry marketplace, agency-mediated suite, and venue-first submissions — which differ in who initiates and how much professional machinery surrounds the transaction, not in the core structure itself.
