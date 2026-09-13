# Research Notes — Personal Concierge Platform

## Research Goal

Understand what a Personal Concierge Platform actually is as an Application Type: who is served, what the core objects are (member, request, concierge team), how delegation and fulfillment flow, how the payer structure works, where the software surface sits (member side, operator side, payer side), and how the type differs from its nearest neighbors — Digital Concierge (property guests), Household Staff Management, Local/Home Services Marketplace, on-demand delivery, employee service portals, virtual-assistant services, and AI assistants.

Leaf: Personal Concierge Platform (DIRECTORY.md §29 Home, Family, Personal & Local Services; between Personal Styling Platform and Appointment-based Service Business Management).

## Initial Boundary

- Working hypothesis: a platform through which individuals delegate personal tasks (errands, reservations, travel, events, purchases, arrangements) to a concierge service team that fulfills them on the member's behalf.
- Pre-hung seams from earlier passes:
  - digital-concierge (§26, processed 2026-09-07): "vs Personal Concierge Platform — name collision only: that type serves consumers' personal errands; this type serves guests of a property. No merger."
  - household-staff-management (§29, processed): "delivering errands/services to members vs administering the employment of the people who serve the home."
- Suspected confusions: hotel concierge (property-anchored), gig/task marketplaces (self-serve matching), virtual assistant services (admin-heavy delegation), employee service portals (org-scoped requests), AI assistants (no human execution).

## Research Questions

1. What is the core object model — member, request, team, fulfillment?
2. Is the fulfilling team first-party (provider's own staff) or a marketplace of independents?
3. How is member access established (membership, employer program, brand program, residency)?
4. How open-ended is the service scope — fixed catalog or "anything legal"?
5. What does the software actually contain on the member side, operator side, payer side?
6. Who pays, and how does the payer relationship shape the structure?
7. Where are the boundaries vs Digital Concierge, marketplaces, household staff management, VA services, AI assistants?
8. Historical check: do pre-digital concierge programs (workplace desks, membership clubs, building concierges) satisfy the definition? Does the AI era break it?

## Representative Products

Selection rationale: market-leading or category-standard self-labeled concierge services with distinct product philosophies and customer tiers, all with reachable official product pages.

1. **Circles** (Sodexo group) — employer-paid corporate concierge / workplace hospitality; on-site + digital 24/7; enterprise tier; proprietary platform (HOS/COS/Analytics).
2. **Best Upon Request** — benefit-provider pole across employers, healthcare employers, hospitals, commercial real estate; on-site + mobile + virtual; proprietary CyberButler® software + member app + portal.
3. **John Paul** (Accor subsidiary) — B2B2C premium concierge powering brands' client programs (banks, insurers, hotels, luxury) + direct "Elite" annual subscription for individuals; global 24/7.
4. **Quintessentially** — luxury private/corporate membership club; lifestyle-manager relationship; member-exclusive portal; explicitly human-first (no AI).
5. **AskSunday** — D2C subscription "dedicated assistant" service; portal-based request forms, progress tracking, task history; admin-heavy pole used deliberately as boundary evidence (virtual-assistant vs concierge center of gravity).

Rejected candidates: Hello Alfred (alfred.com now resolves to an unrelated sheet-music publisher; consumer service not verifiable — dropped after one attempt).

## Sources

Research date: 2026-09-09. All fetched live.

- Circles: https://www.circles.com/ , /how-we-can-help/support-your-employees , /about/personal-assistant-services , /about/digital-concierge , /who-we-are/technology
- Best Upon Request: https://www.bestuponrequest.com/ , /employee-concierge-services/ , /program-costs/
- John Paul: https://www.johnpaul.com/ , /fr/expertises/service-de-conciergerie-premium , /fr/expertises/solution-elite-pour-les-particuliers
- Quintessentially: https://quintessentially.com/ , /single/what-is-concierge-service
- AskSunday: https://asksunday.com/ , /how-it-works

Source-access limitation: all fetched surfaces are public marketing/product pages. Member portals (my.circles.com, members.quintessentially.com, asksunday.com/portal, BEST customer portal) are login-walled; no member-facing help centers were reachable for John Paul or Quintessentially. Therefore no precise operational claims (SLAs, response-time promises, pricing figures, app feature inventories) are asserted anywhere. Vendor performance claims (e.g., "3+ hours saved per request", "800,000 active subscriptions") are recorded here as vendor claims only.

## Product A — Circles [A — product pages]

### Key observations

- Positioning: "Workplace Hospitality & Employee Services"; pillars: Employee & Guest Services, Corporate Concierge, Community Engagement. Payer = employer; served = employees (and workplace guests).
- **On-site concierge**: "combines traditional concierge services with proactive workplace support"; anticipates on-site needs (desk setups, room bookings, IT troubleshooting); "team of local area experts" for errand running, travel planning, local recommendations.
- **Digital concierge**: "convenient, mobile-first platform for all their lifestyle requests"; team of concierge experts available 24/7; expertise in "home services, leisure and events, and holiday and travel"; access "through phone, email and our app", "24/7, 365 days a year".
- **Members portal**: "Log in to Circles members portal and place all your requests. Our team is one click away." (my.circles.com)
- **Personal assistant services**: "team of dedicated personal assistants… specialists in the concierge profession"; domains: home solutions, corporate events, travel arrangements, celebrations (birthdays, weddings); "some excelling in travel arrangements, while others are experts at securing reservations at the finest restaurants or obtaining elusive tickets"; "even the most unconventional requests".
- **Errand running services**: returns, dry cleaning, last-minute errands; "our errand runners tackle a variety of everyday tasks".
- **Technology page** (direct software evidence): proprietary platform in three layers —
  - **HOS (Hospitality operating system)**: "the service delivery engine… helps our teams manage requests, follow clear service standards, capture preferences and gather real-time feedback"; tracks visitor flow, facility needs, safety checks, amenity usage, event participation.
  - **COS (Concierge operating system)**: "the member engagement layer… a single destination to get help, make requests, access exclusive promotions and discounts and connect to the services and support they need, anytime and anywhere… supports both everyday needs and complex, multi-step requests".
  - **Analytics**: insights layer across the ecosystem.
- Vendor claims (L3): "3+ hours saved per request", "800,000 active subscriptions on Circles OS", "1M annual consumer interactions", NPS figures.
- Service categories named: travel planning (flights, hotels, transportation), event coordination, restaurant reservations, entertainment recommendations, home services, family needs, errands, gifting/celebrations.

## Product B — Best Upon Request [A — product pages]

### Key observations

- Positioning: "Through on-site, mobile and virtual concierge solutions…" — three delivery modes named on the homepage.
- Audiences/programs: For Employers (Employee Concierge, Maternity Concierge), For Healthcare Employers (employee/physician concierge), For Hospitals (Patient Concierge, Maternity Unit, Emergency Department), For Commercial Real Estate (Commercial Building Concierge). Same machinery, different served populations and contexts.
- **Payer rule (explicit)**: "BEST's programs are paid by the corporation or hospital – there is no service fee for the employees or patients we serve." Client quote: "subsidize the concierge program so that our team members pay zero cost for the service."
- Program structure: "Our customer success team creates, markets and manages your tailored concierge program" — customized program, dedicated concierge support, continuous marketing to maximize utilization, monthly and annual reporting with program stats.
- Service examples: on-campus errand running (dry cleaning, vehicle servicing, lunch delivery via local vendors), convenience services (stamps, cards, tickets), travel and event planning (including currency exchange), off-campus errand running (shopping, prescription pick-up, returns, post office, courier), information research (gifts, mechanics, deals), home-based help (concierge waits at the member's home for a repair/delivery).
- **Platforms (direct software evidence)**: "Proprietary and PCI-compliant CyberButler® concierge software and point-of-sale system"; award-winning mobile app (BestURequest); "Customer portal with dedicated concierge details, newsletter, vendor discounts and more"; "Additional multi-channel access: email, two-way text messaging, toll-free phone"; "24/7/365 multi-channel access"; "Request a service in seconds with our concierge app."
- Team: "Highly-Trained Professional Concierge", "In-Depth Hiring, Coaching, & Training", "Risk Mitigation & Service Recovery", "Real-Time Reporting", "Secure Point-of-Sale & Mobile App".
- Pricing variables (program-side): hours of service, number of employees, number/distance of buildings, patient beds, service mix priority, urban vs suburban.

## Product C — John Paul (Accor) [A — product pages]

### Key observations

- Positioning: premium concierge for enterprises to offer their own clients ("vos clients d'exception") — B2B2C: banks, insurers, automotive, luxury, hotels (client logos: Visa, Hyundai, Burberry, Accor…).
- Concierge service: "disponible 24/7 via une multitude de canaux"; request range "du plus simple (réservations d'hôtels, restaurants, vacances) au plus audacieux (accès exclusifs, loges VIP et jets privés)"; dedicated ticketing team for concert/opera/show seats "parfois déjà complets"; travel and exceptional stays; on-site concierge deployment at events; corporate concierge (North America only).
- Team: "+280 concierges d'elite issus du voyage, du luxe, de l'hospitality"; concierge managers with teams handling "les demandes variées de nos Membres"; "confidentialité absolue" as a stated service value.
- **Elite solution for individuals** (D2C pole): annual subscription ("abonnement annuel") connecting the individual to Elite concierges who "prendront en compte toutes vos requêtes" — family vacation organization, surprise gift shopping, dinner reservations; 24/7 premium access; "Gain de temps & Prix négociés".
- Adjacent expertise lines (L3): relational marketing, loyalty programs, premium clienteling, events agency, "IA & Innovations digitales".
- Terminology: served individuals are "Membres"; brand programs embed the concierge as the brand's own service.

## Product D — Quintessentially [A — product pages]

### Key observations

- Positioning: "the ultimate destination for discerning individuals and businesses seeking industry-leading concierge services worldwide… our lifestyle managers do it all with unparalleled personalisation"; 25 years.
- Membership structure: Private membership (individuals) + Corporate membership (brands/businesses for their audiences and staff). Member-exclusive portal (login-walled).
- Service catalog: Travel ("award-winning in-house travel agency"), Restaurants & nightlife ("relationships with the world's best chefs"), Lifestyle services ("everything practical and banal"), Private events, Exclusive access, Real estate/Estates, Art advisory, Education, Weddings.
- **Vendor-articulated type definition** ("What is a concierge service?" article):
  - "A concierge is an individual or organisation that provides personalised services, handling their client's every need – no matter how big or small. A concierge is typically available 24/7…"
  - Hotel vs lifestyle concierge: "the former enhances a guest's experience during their hotel stay, while the latter elevates every aspect of their clients' lives – whether at home, at work, or abroad." ← direct vendor articulation of the Digital Concierge boundary.
  - Types: "travel bookings, restaurant reservations, event planning, calendar scheduling, household management, and medical appointments".
  - AI concierge: "the virtual version of a personal assistant… may not provide the same personalised, high-touch service as a human".
  - Luxury lifestyle management: "combines traditional concierge with access you can't get anywhere else… sourcing limited-edition luxury items, securing sold-out tickets, and arranging VIP access."
  - Lifestyle manager: "go beyond the traditional level of support, making the impossible possible."
- Human-first posture: "Nor do we use AI; we pride ourselves on authentic one-to-one contact."
- Member testimonial evidence of the standing relationship: "I'm extremely relaxed with my lifestyle manager because I know that anything I need will be looked after. He is on top of all my requests."

## Product E — AskSunday [A — product pages] (boundary pole)

### Key observations

- Positioning: "Professional Virtual Assistant Services for Businesses & Entrepreneurs – Trusted Since 2007"; also self-labels "personal assistant service".
- Dedicated Assistant model: one assigned assistant per member; Primary/Secondary DA system for coverage; accessible by email, IM and phone; 24h/5days availability; billing by time in 5-minute increments with remaining plan time visible in the portal.
- Flow: sign up → enter personal details in secure portal → welcome manager call → assistant assigned → phone introductions → "Email or call your assistant directly to offload your tasks" → give a timeframe → assistant executes → outputs delivered.
- Portal: "Request Task Assistance—with easy and streamlined request forms… Track Progress & History—of current and previous tasks… Access Customer Support—via online chat."
- Scope: data entry/analysis, research, travel planning, social media, content writing, graphic design, outbound calling, email management, scheduling, ecommerce support; "As long as it is legal and ethical, we will do almost everything for you"; "For Individuals: Outsource web research, holiday planning, gifting, e-commerce purchases and more."
- Assessment: the delegated-task + portal + first-party-team structure is identical to the concierge sample; the center of gravity is remote administrative/knowledge work rather than personal-life arrangement and physical-world errands. Treated as the admin-heavy variant pole of the same delegated-personal-service space, and as boundary evidence vs virtual-assistant services.

## Cross-product Comparison

| Structure | Circles | Best Upon Request | John Paul | Quintessentially | AskSunday | Evidence |
|---|---|---|---|---|---|---|
| Enrolled served individual (membership/program eligibility) | ✓ employer program, members portal | ✓ employer/hospital/CRE programs | ✓ brand programs + Elite annual subscription | ✓ private/corporate membership | ✓ subscription plans | B (5/5) |
| Delegated personal request as unit of work | ✓ "place all your requests" | ✓ "Request a service in seconds" | ✓ "toutes vos requêtes" | ✓ "on top of all my requests" | ✓ request forms + task history | B (5/5) |
| Open-ended personal-life scope (not a fixed catalog) | ✓ "even the most unconventional requests" | ✓ errands/research/home help/travel/events | ✓ "du plus simple… au plus audacieux" | ✓ "every need – no matter how big or small" | ✓ "almost everything… legal and ethical" | B (5/5) |
| First-party concierge team executing on the member's behalf | ✓ "our team of concierge experts", errand runners | ✓ "Highly-Trained Professional Concierge", hiring/training | ✓ "+280 concierges d'elite" | ✓ "lifestyle managers", "in-house specialists" | ✓ "assigns one of our assistants" | B (5/5) |
| Member-visible request tracking (portal/app) | ✓ members portal + COS | ✓ app + customer portal | not directly evidenced (marketing site) | portal exists; tracking not directly evidenced | ✓ "Track Progress & History" | A in 3/5; B- for the rest |
| Personal context / preferences | ✓ HOS "capture preferences" | ✓ customized programs; dedicated concierge details | ✓ "personnalisation" | ✓ standing lifestyle-manager relationship | ✓ "get to know your… working style" | B (5/5, depth varies) |
| Multi-channel intake (app/portal + phone + email [+ text/on-site]) | ✓ phone/email/app + on-site | ✓ app/email/two-way text/toll-free + on-site | ✓ "24/7 via une multitude de canaux" | ✓ one-to-one contact + portal | ✓ email/IM/phone + portal | B (5/5) |
| 24/7 or extended availability | ✓ 24/7 digital | ✓ 24/7/365 | ✓ 24/7 | "typically available 24/7" (own definition) | 24h/5days | B — common, not definitional |
| On-site (physical) delivery mode | ✓ on-site concierge | ✓ on-site programs | ✓ corporate concierge (NA), event presence | ✗ (remote) | ✗ (remote) | Variant |
| Payer ≠ user (institution-paid, member free) | ✓ (employer-paid positioning) | ✓ explicit: "no service fee for the employees or patients" | ✓ brand-funded programs (B2B2C) | ✗ member-paid | ✗ member-paid | Variant (both poles in-sample) |
| Reporting/analytics to payer | ✓ Analytics layer, ROI calculator | ✓ monthly/annual reporting, real-time reporting | not evidenced | not evidenced | n/a (D2C) | Common in B2B-paid pole |
| Vendor/partner network orchestrated by the concierge | ✓ local area experts | ✓ "work with local vendors", curated discounts | ✓ relationships/access | ✓ in-house travel agency, chef relationships | implied | B |
| Human-first vs AI posture | digital platform + human team | proprietary software + human team | human + "IA & Innovations" line | explicit no-AI | human | Variant |

## Canonical Model

### L0 — Defining Invariant (minimal)

A Personal Concierge Platform is a service platform through which an enrolled individual delegates open-ended personal tasks to the provider's own concierge team, which fulfills them on the member's behalf, each request handled as a tracked unit of service.

Three jointly-held structures:

1. **The enrolled member with personal context** — an identified individual whose access exists through an eligibility relationship with the provider (employer program, membership subscription, brand program, residency), and around whom personal preferences and service history accumulate. Remove → anonymous pay-per-task counter or open gig marketplace.
2. **The delegated personal request as the unit of work** — open-ended personal-life tasks (errands, reservations, travel, events, purchases, research, home help) submitted by the member and carried to completion by the service; scope bounded by legality/ethics and program rules, not by a fixed product catalog. Remove → booking engine (fixed catalog), help desk (org-scoped), or a to-do tracker (no fulfillment).
3. **The provider's first-party concierge team executing on the member's behalf** — human staff who act in the member's stead in the outside world: booking, buying, arranging, coordinating vendors, physically running errands. Remove → self-serve marketplace (member picks and manages providers directly), AI chatbot (answers but does not execute), or advisory-only recommendation service.

Jointly-held is load-bearing:
- 1 alone = a membership club with no service machinery
- 2 without 3 = a task tracker / to-do app
- 3 without 1+2 = a staffing agency
- 1+2 without 3 = a self-service portal with no one to delegate to
- 2+3 without 1 = drop-in task service drifting toward gig-marketplace territory
- Remove "personal-life scope" → employee/IT service portal territory (org-scoped requests)
- Remove "on the member's behalf" → recommendation/advisory content

### L1 — Common Mature Structure

- Multi-channel intake: member app/portal plus phone, email, text/IM; on-site desk where the program is workplace/hospitality-embedded
- Member-visible request tracking and history (portal/app)
- Preference capture and personalization (service standards, member profiles)
- Recurring request categories: travel, dining/reservations, events, errands, home services, research, gifting, celebrations
- Orchestrated vendor/partner network the concierge executes through
- Extended/24-7 availability
- Payer-facing reporting/analytics and utilization marketing (in institution-paid variants)
- Perks layer: negotiated prices, curated discounts, exclusive access

### L2 — Variant / Optional Structure

- Payer model: employer/institution-paid benefit (member pays nothing) ↔ member-paid subscription ↔ brand-embedded B2B2C (the brand funds concierge for its own customers)
- Delivery mode: on-site + virtual hybrid ↔ purely remote
- Service depth: everyday errands/work-life ↔ luxury lifestyle management (exclusive access, sold-out tickets, VIP)
- Dedicated assistant/lifestyle-manager relationship ↔ pooled team
- Human-first ↔ AI-augmented posture (one sampled vendor explicitly refuses AI; others run digital layers; "AI concierge" exists as an adjacent automated form)
- Domain extensions: patient concierge (hospitals), maternity concierge, physician concierge, residential/CRE building concierge
- Billing mechanics: program fees priced on population/coverage, time-based member billing, annual memberships

### L3 — Vendor-specific (research notes only)

- Circles: HOS/COS/Analytics naming; "3+ hours saved per request"; "800,000 active subscriptions"; ROI calculator; Sodexo group.
- Best Upon Request: CyberButler® software; BestURequest app; PCI-compliant POS; 35+ years; program-pricing variable list.
- John Paul: Accor ownership; Elite program naming; ticketing team; "+280 concierges d'elite"; "Prix négociés".
- Quintessentially: Noted editorial; Foundation; Estates/Art/Education advisory lines; "Nor do we use AI" posture.
- AskSunday: Primary/Secondary DA system; 5-minute billing increments; TRYFREE25 coupon; LiveChat support.

## Vendor-specific Findings

See L3 above. None of these entered the canonical model.

## Boundary Findings

1. **vs Digital Concierge (§26, processed)** — pre-hung seam, confirmed and sharpened from this side. Digital Concierge is property-operated and stay-anchored (guest of a hotel/venue; requests scoped to the stay and the property's services). Personal Concierge is provider-operated and life-wide (the member's life across home, work, travel). Quintessentially's own definitional article articulates exactly this distinction ("the former enhances a guest's experience during their hotel stay, while the latter elevates every aspect of their clients' lives"). No merger. Note: concierge providers also operate inside hospitals and commercial buildings (BEST) — eligibility there is residency/employment/patient status, still life- or visit-scoped personal service, not property-stay service delivery machinery.
2. **vs Household Staff Management (§29, processed)** — pre-hung seam confirmed: this type delivers services to members through the provider's own team; that type administers the employment of domestic staff who serve the household. A concierge platform's concierges are the provider's employees, not the client's.
3. **vs Local Service Marketplace / Home Services Marketplace (§29)** — marketplaces match a consumer to independent third-party pros whom the consumer selects and manages; the concierge platform's own team takes the request and executes (possibly through vendors) as the member's delegate. Self-serve selection vs delegated arrangement is the seam.
4. **vs On-demand Delivery Platform (§18)** — courier/delivery logistics with a fixed transaction shape vs open-ended personal delegation that may include but is not centered on delivery.
5. **vs Employee Service Portal / Enterprise Request Management (§10)** — those handle organization-scoped requests (IT, HR, facilities) for employees acting in their work role; the personal concierge handles the employee's personal-life tasks. Circles' on-site concierge explicitly mixes both surfaces (room bookings, IT troubleshooting are workplace services; errands are personal) — the personal-life delegation is what belongs to this Type.
6. **vs Virtual/Personal Assistant services (AskSunday pole)** — same delegated-task machinery (first-party team, portal, subscription); center of gravity differs: remote administrative/knowledge work vs personal-life arrangement and physical-world execution. The directory has no separate virtual-assistant-service leaf; this Type holds the delegated-personal-service space, with the admin-heavy pole documented as a variant. Flagged as a mild taxonomy observation, not a directory error.
7. **vs Enterprise AI Assistant (§13, processed)** — workforce-facing digital assistance (answers, drafting, knowledge) vs human-executed delegation into the physical world. An "AI concierge" that only answers is adjacent; AI layers inside a human concierge team are a capability.
8. **vs Appointment-based Service Business Management (§29, processed)** — that Type is back-office management SaaS for service businesses serving their own clients; this Type is the service platform of the concierge business itself. Different seat.
9. **vs Travel Itinerary Planner / OTA (§26)** — travel is one request category here; the center is all-domain personal delegation.

## Uncertainties

- Internal operator tooling depth for John Paul and Quintessentially is not directly evidenced (marketing-grade public surfaces; member portals login-walled). Their inclusion of request tracking/preference machinery is inferred from the service model, not observed. Assertion strength kept at "common" for member-visible tracking.
- Whether a drop-in, pay-per-request concierge without any enrollment relationship exists as a stable product form — not found in the sample; if it exists, it sits at the marketplace boundary. The canonical model holds enrollment as definitional based on 5/5 sample evidence.
- The exact split between concierge-performed work and vendor-performed work inside a single request (e.g., errand runner vs contracted local vendor) varies by product and is not precisely documented in public sources.
- Market size/segment shares not researched (not needed for the type definition).

## Historical / Market-Sample Check

- 1990s-era workplace concierge program (employer contract, staffed on-site desk, paper or simple electronic request log, employer-paid, employees submit errands) — satisfies all three L0 structures with no app, no AI, no 24/7 promise, no subscription billing. ✓
- Pre-digital private-membership concierge clubs (membership card, phone/letter requests, club staff fulfilling) — satisfies. ✓
- Residential building concierge desk serving residents (eligibility = residency; personal errands; building staff) — satisfies; matches BEST's commercial-building program shape. ✓
- Hotel concierge desk — fails the life-wide scope leg (stay-anchored, property-operated) → Digital Concierge territory; the sampled vendors themselves draw this line. ✓ (boundary, not counterexample)
- AI-era: a pure AI concierge/chatbot fails the first-party-human-execution leg → adjacent automated form; AI-assisted human teams still satisfy. ✓
- Conclusion: the definition is not overfit to the current mobile-app/AI implementation.

## Final Synthesis

A Personal Concierge Platform is the operating platform of a delegated personal-service business: an enrolled population of individuals (employees, members, patients, residents, a brand's customers) submits open-ended personal requests; the provider's own concierge team takes each request and executes it in the real world on the member's behalf — booking, buying, arranging, coordinating vendors, running errands — with the request tracked to completion and the member's preferences accumulating over time. The software surface has three seats: the member's intake/tracking surface (app/portal plus human channels), the concierge team's request-management surface, and the payer's reporting surface. What the type is NOT: a property-stay service desk (Digital Concierge), a self-serve marketplace of independent pros, an employment-administration system for domestic staff, an org-scoped employee request portal, or an AI answer engine. The payer may be the member (subscriptions, luxury memberships) or an institution (employers, hospitals, brands) — both poles realize the same core.
