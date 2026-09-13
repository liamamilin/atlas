# Research Notes — Nail Salon Management

Research date: 2026-09-08

## Research Goal

Understand the software category used by nail salons — businesses whose revenue is built on manicure, pedicure, and nail-enhancement services performed by nail technicians — and derive its canonical structure: what objects exist, how the nail visit is booked and delivered, how it resolves into money, and where the nail variant sits against the generic appointment-based service business core and the other §29 beauty-industry siblings (salon, barbershop, spa, med spa, massage).

## Initial Boundary

Initial hypothesis (before research):

- The leaf sits in Directory §29 between "Massage Practice Management" and "Beauty Professional Business App", surrounded by industry-specific siblings. Three of those siblings (barbershop-management, massage-practice-management, med-spa-management) have already been processed and each was ratified as an **industry Variant of the generic appointment-business core** (bookable service catalog + identified clients + appointment binding client×service×provider×time + lifecycle + checkout), with the industry difference concentrated in an overlay rather than in object types.
- The med-spa pass recorded a removal test for this leaf: "remove the regulated-treatment layer → that industry's business on the same visit economy."
- Expected nail overlay candidates (to verify, not assume): nail service semantics (manicure/pedicure/gel/acrylic), color/shape preference records, nail-art-driven booking (design photos, complexity pricing), two-technician services (mani+pedi in parallel), walk-in and group-visit culture, per-technician pricing levels.
- Working assumption to test: the nail variant adds no new object types — only vocabulary, emphasis, and configuration of the same core.

## Research Questions

1. Does the market realize nail-salon software as a separate product family, or as a configuration of multi-vertical salon platforms?
2. What nail-specific service vocabulary and catalog structure do the products carry?
3. What does the client record carry that is nail-specific (shapes, colors, formulas, photos)?
4. How does nail art affect booking and pricing (design photos, complexity-based pricing, technician skill levels)?
5. How are two-technician services (e.g., simultaneous mani + pedi) and group visits modeled?
6. How do walk-in visits — culturally strong in nail salons — interact with the appointment structure?
7. How does payment attribution to individual technicians and per-technician pricing work?
8. Do any nail-specific structures change the core model, or only decorate it?
9. Historical / regional check: would older, walk-in-dominated, or regional nail businesses fit the definition?

## Representative Products

| Product | Segment / philosophy | Customer tier | Why selected |
|---|---|---|---|
| Mangomint | Design-forward salon/spa suite with a dedicated nail-salon solutions page | SMB salons, solo → multi-location | Richest nail-specific feature evidence of the sample (art photos, 2-technician services, tiered tech pricing, walk-in room) |
| GlossGenius | Solo-first, mobile-first platform; no client app needed; strong nail-technician user base | Solo techs, booth renters, small salons | Nail page positions walk-ins→regulars and nail-specific client notes (shapes, color combos) |
| Vagaro | Multi-vertical salon/spa/fitness suite with consumer marketplace | Solo → chains | Tier-1 help center documents Nail Salon as a first-class business type with nail catalog vocabulary; core machinery Tier-1 from the same research program |
| Boulevard | Client-experience platform for appointment-based self-care businesses | Premium salons/spas, multi-location, franchises | Nail-salon vertical page + Tier-1 support center; nail franchise customer (multi-location pole) |

Notes on sampling: no nail-native standalone product could be researched. NailsMedia (nail-specific) is an unreleased "Launching Soon" site; Nailbook (Japan, nail-specific) returned HTTP 403; Fresha/Booksy were already unreachable in the 2026-09-06 pass. The market reality that nail salons are served almost entirely by multi-vertical salon platforms is itself recorded as a research finding, and the nail-native pole is recorded as an evidence gap.

## Sources

Tier 1 (official operational documentation):

- Vagaro Support (Zendesk help center), fetched 2026-09-08:
  - "Set Your Business Type": https://support.vagaro.com/hc/en-us/articles/360048745274-Set-Your-Business-Type (Nail Salon keyword list: manicure, pedicure, acrylic, shellac, gel, nail polish, toes, nails, color change nails, color change toes)
  - Search results for "two providers" — "Add Resources to Services and Classes" (services performed by two providers at the same time, e.g. couple's massage), "Create a Service Bundle", "Book Multiple Services" (each service by one or different providers)
  - Help-center search interface: https://support.vagaro.com/hc/en-us/search?query=nail (6 results; business-type article is the nail-specific anchor)
- Boulevard Support Center (Intercom), fetched 2026-09-08:
  - Search: https://support.boulevard.io/en/search?q=two+providers — "Enabling and Disabling Online Booking" (provider-level price display on the self-booking overlay: "if multiple providers share the same price it lists those providers alphabetically"; sorted by price highest to lowest), "Professional App" (providers manage appointments, client info, chart and check out on the go)
  - Search "duo" — Boulevard Duo is a card reader/app (hardware), not a dual-provider service; recorded to prevent mislabeling
- Generic appointment-business machinery (statuses, checkout, packages/memberships, resources, marketplace) reuses Tier-1 Vagaro help-center and Zenoti API evidence recorded in the same research program on 2026-09-06 (research/appointment-based-service-business-management.md)

Tier 2 (official product pages):

- Mangomint nail-salon solutions page, fetched 2026-09-08: https://www.mangomint.com/solutions/nail-salon-software/ (key features for nail salons: login-free online booking; add-ons and service customizations; book via SMS & collect card-on-file; nail art inspiration photo upload; group bookings; embedded two-way texting; support for 2 technician-services; pay via SMS; payroll calculation and processing; FAQ: tiered pricing by tech experience/seniority/specialized skills; Virtual Waiting Room + Express Booking for walk-ins; per-artist payment direction; inventory for nail products)
- GlossGenius nail-salon page, fetched 2026-09-08: https://glossgenius.com/customers/nail-salon-software (headline "Turn walk-ins into regulars"; "preferred nail shapes, color combos, and birthdays" tracked in client notes and history; deposits/cancellation/card-on-file built into booking; rebooking prompts built into checkout; booth renters; BNPL for pricier services) + platform homepage https://glossgenius.com/ (industries list includes Nail Salon; feature modules)
- Boulevard nail-salon page, fetched 2026-09-08: https://www.joinblvd.com/nail-salon-software (nail salon vertical; solutions nav spans salon/spa/barber/massage/medspa) + customer story Freecoat Nails: https://www.joinblvd.com/customer-stories/freecoat-nails (5-location nail franchise; legacy software "couldn't handle group bookings"; no-show reduction, gift cards, gratuities — vendor-published outcome figures recorded here only, not used in the final document)

Access limitations:

- NailsMedia (nail-specific candidate): https://www.nailsmedia.com/ is an unreleased "Launching Soon" page — no product evidence available. Abandoned after 1 fetch.
- Nailbook (Japan, nail-specific): https://nailbook.jp/ → HTTP 403. Abandoned after 1 attempt.
- Vagaro marketing site (https://www.vagaro.com/nail-salon-software) → HTTP 403; Vagaro evidence rests on its Tier-1 help center instead.
- GlossGenius Learning Center: JS shell (already recorded in the 2026-09-06 pass) — GlossGenius assertions rest on its own product pages.
- Mangomint help center: help.mangomint.com not reachable (404 on tried paths) — Mangomint assertions rest on its official product page.
- Search engines: DuckDuckGo timed out (1 attempt), Bing returned geo-sanitized irrelevant results (1 attempt), Mojeek HTTP 403 (1 attempt). Nail-native product discovery therefore rests on prior knowledge; the nail-native pole is an evidence gap, not a claimed absence.

## Product Observations

### Vagaro (evidence layer: A for the business-type structure — Tier-1 help center)

- **Nail Salon is a first-class business type** on the platform. Business type is derived automatically from service names against a keyword list; the Nail Salon entry reads: "manicure, pedicure, acrylic, shellac, gel, nail polish, toes, nails, color change nails, color change toes". This is direct documentation that (a) nail salons are a supported vertical and (b) the platform models the nail service catalog through standard service objects whose names carry nail vocabulary. The business type drives marketplace categorization ("Find Businesses").
- **Multi-provider services are documented** (Tier-1): "Add Resources to Services and Classes" describes services performed by two providers at the same time (couple's massage example) and back-to-back services; "Create a Service Bundle" and "Book Multiple Services" document booking several services with one or different providers in one flow. The machinery that a nail salon would use for a simultaneous mani+pedi by two technicians exists in the core booking model, though Vagaro's own example is spa-framed.
- Everything else observed at Tier-1 in the 2026-09-06 pass applies unchanged to nail businesses (same platform serves them): service catalog with categories/add-ons/bundles, customer profiles with appointment history/notes/tags/no-show counts, appointment statuses (Requested → Accepted → Awaiting Confirmation → Confirmed → Show → Ready to Start → In Progress → Complete; No-Show and Cancel with fees), checkout with split payment/tips/package-redemption/retail, resource calendars (stations/chairs), employee management and payroll, consumer marketplace with client reviews.

### Mangomint (evidence layer: A for feature existence on its own page — Tier-2 product page, vendor FAQ)

The nail-salon solutions page lists "Key features for nail salons":

- Login-free online booking
- Add-ons and service customizations
- Book via SMS & collect card-on-file
- **Nail art inspiration photo upload** — clients attach design photos when booking; the FAQ states the platform "help[s] ensure clients book the correct appointment and are matched with the best artist" for "advanced services and custom nail art"
- Group bookings
- Embedded two-way texting
- **Support for 2 technician-services** — a single client visit can involve two technicians (mani + pedi in parallel is the nail-salon usage)
- Pay via SMS (client-side checkout and tipping from their phones; payments "direct[ed] to the right artist")
- Payroll calculation and processing

The FAQ adds nail-specific pricing: "flexible pricing options based on service complexity or time required. You can also set tiered pricing based on your nail techs' experience, seniority, or specialized skills."

Walk-ins: "Virtual Waiting Room" and "Express Booking™" let the salon manage walk-ins "from texting a link to collect a card-on-file to notifying clients when their nail tech is ready." Inventory: "track nail products… real-time inventory management."

### GlossGenius (evidence layer: A for feature existence on its own page — Tier-2 product page)

- Headline posture for nails: "**Turn walk-ins into regulars**" — walk-in conversion is the positioned growth loop for nail salons; the software "designed to help nail salon owners and booth renters grow."
- Nail-specific client records: "Track important details — like **preferred nail shapes, color combos, and birthdays** — with client notes and history." This is the nail-industry expression of the preference/formula record the family uses (hair color formulas in salons, treatment notes in massage).
- Retention machinery: automated rebooking prompts built into checkout; deposits, cancellation and card-on-file policies built into booking; review management linked to Google Profile or the booking website.
- Payments: flat-rate processing positioning; BNPL "for pricier services" (nail page frames expensive service financing); Instant Payouts and "pay booth renters fast" — booth-rent economics present in the nail segment.
- User base composition on the nail page: individual nail technicians with large social followings (portfolio-driven client acquisition; Instagram handles with follower counts displayed).
- Marketplace-posture argument (marketing): "doesn't jeopardize retention by showing clients your competitors" — i.e., GlossGenius has no consumer marketplace while Vagaro does; recorded as packaging variance within the Type.

### Boulevard (evidence layer: A for support-center items, B for page posture — mixed Tiers)

- Nail Salon is one of six named industry solutions (salon, spa, barber, massage, medspa, nail); the nail page positions "seamless scheduling to marketing and payments" for nail salons (page body largely JS-rendered; posture-level evidence only).
- Tier-1 support center: the self-booking overlay lists providers with per-provider prices ("if multiple providers share the same price it lists those providers alphabetically… listed first by price highest to lowest") — the same service carries different prices per provider, the mechanism behind technician-level pricing. The Professional App gives providers appointment management, client information, charting, and checkout on mobile.
- Customer story (Freecoat Nails, 5-location nail franchise): the prior system "couldn't handle group bookings, automated reminders, or consistent customer support"; Boulevard adoption associated (vendor-reported) with increased service/gift-card/gratuity sales and reduced no-shows. Group bookings and no-show machinery are the operationally salient nail needs in this account. Outcome percentages are vendor-published and excluded from the final document.
- Boulevard "Duo" is a card reader/client-facing checkout app (gratuity collection, gift cards) — hardware, not a dual-provider service feature; recorded to avoid misreading.

## Cross-product Comparison

| Structure | Vagaro | Mangomint | GlossGenius | Boulevard | Evidence layer |
|---|---|---|---|---|---|
| Bookable service catalog carrying nail vocabulary (manicure/pedicure/gel/acrylic/color change) | ✔ (Nail Salon business-type keywords, Tier-1) | ✔ (services + service customizations; add-ons) | ✔ (nail services; booking website) | ✔ (scheduling; nail vertical) | B |
| Identified client records with nail-specific preferences (shapes, colors) | ✔ (notes/tags; no nail wording observed) | ◐ (not observed on the fetched page) | ✔ ("preferred nail shapes, color combos" on client records) | ◐ (client profiles; forms) | A(GG) + B(wrapper) — nail wording single-product |
| Appointment binding client × service × technician × time | ✔ (Tier-1, 2026-09-06 pass) | ✔ | ✔ | ✔ | B |
| Appointment lifecycle with cancellation/no-show as named outcomes | ✔ (Tier-1 status set; no-show counts on profile) | ✔ (card-on-file; reminders) | ✔ (deposits/cancellation/card-on-file "built into booking") | ✔ (case-study emphasis) | B |
| Checkout resolving the visit into recorded money, with tips | ✔ (Tier-1: tips, split payment, packages) | ✔ (pay via SMS, client-side tip, per-artist direction) | ✔ (POS, rebooking prompts at checkout) | ✔ (Tier-1: Duo checkout + gratuity) | B |
| Two-technician service (one visit, two providers) | ✔ machinery (Tier-1 multi-provider services/bundles; spa example) | ✔ nail-framed ("2 technician-services") | ◐ (not observed) | ◐ (not observed) | B (machinery), nail expression single-product |
| Nail art as booking input (design photo upload, artist matching) | — | ✔ | ◐ (portfolio/social positioning; no upload feature observed) | — | A single-product (Mangomint) |
| Tiered pricing by technician level / service complexity | ◐ (employee-side price differences not directly observed) | ✔ (FAQ: tech experience/seniority/specialized skills; complexity pricing) | ◐ (not directly observed) | ✔ mechanism (per-provider price display on booking overlay, Tier-1) | B |
| Walk-in handling (waiting list/queue → visit) | ◐ (walk-in checkout documented Tier-1) | ✔ (Virtual Waiting Room; Express Booking; "nail tech is ready") | ✔ posture ("turn walk-ins into regulars") | ◐ (not observed on nail page) | B |
| Group bookings (parties/multiple simultaneous clients) | ✔ (Tier-1: group checkout; multi-appointment scheduling) | ✔ (nail key feature) | ◐ (not observed) | ✔ need cited in nail case study | B |
| Per-technician payment attribution (tips/commissions) | ✔ (payroll category, Tier-1) | ✔ ("directing payments to the right artist"; payroll) | ✔ (payroll reporting: commissions, tips, hourly) | ✔ (Tier-1 professional app checkout; gratuity) | B |
| Booth-renter / solo-tech packaging | ◐ (solo supported) | ◐ (not observed) | ✔ (booth renters named on nail page) | ◐ | B |
| Retail/inventory for nail products | ✔ (Tier-1 product variants incl. nail polish example) | ✔ (nail products inventory) | ✔ (inventory & retail) | ✔ | B |
| Multi-location / franchise | ✔ | ✔ (FAQ: multi-location nail salons) | ✔ (multi-location pages) | ✔ (nail franchise customer) | B |
| Bundled consumer marketplace | ✔ (consumer app; business-type categorization) | — (no marketplace posture) | — (explicitly positions against marketplaces) | — | B — optional |
| Forms / health-adjacent documentation emphasis | ◐ (forms exist platform-wide) | ◐ (Forms & Charting module exists) | ◐ (Forms & Waivers exists) | ✔ (Forms & Charts exists) | B — generic family machinery, NOT nail-specific; no nail documentation emphasis observed |

Legend: ✔ directly observed; ◐ observed indirectly or partially; — not observed in fetched sources.

## Canonical Model

### Level 0 — Defining Invariant

Identical to the ratified family core (appointment-based service business management; barbershop/massage/med-spa joint reviews). The smallest structure without which the product stops being a nail salon management application:

1. **Bookable service catalog** — the salon's menu of nail services, each with duration and price (categories and add-ons as the standard elaboration). Nail vocabulary (manicure, pedicure, gel, acrylic, color change…) fills the catalog; it does not change its structure.
2. **Identified client records** — persistent individually identified clientele; the salon remembers the person across visits.
3. **The appointment as the central binding object** — client × service × technician × time on the salon's calendar; technician availability makes a slot bookable; stations/tables/pedicure chairs constrain it as resources.
4. **Lifecycle to service delivery** — booked → confirmed → arrived → in service → complete, with cancellation and no-show as named outcomes.
5. **Checkout resolving the visit into recorded money** — the completed service becomes a chargeable visit recorded against the client, with retail and prepaid value redeeming in the same checkout.

Justification tests:

- Remove the appointment/calendar → retail POS with client CRM.
- Remove checkout and the client ledger → appointment scheduling application.
- Remove the service-delivery context → generic POS.
- Historical check: a paper-era nail salon (appointment book + client index cards recording polish color/nail shape + register + per-tech commission sheet) satisfies all five; a walk-in-dominated salon where the "appointment" is created at the counter on arrival also satisfies all five (the visit still binds client × service × technician × time and still ends in checkout). The definition does not depend on online booking, marketplaces, or any nail-art machinery.

### Level 1 — Common Mature Structure

Present across the researched sample (evidence layer B), expected of mature products, not defining:

- Online self-booking (login-free in current products) with deposit/card-on-file and cancellation policies.
- Automated confirmations/reminders; two-way texting; waitlist/waiting-room for walk-ins and cancellations.
- No-show protection (cards on file, fees, client blocking).
- Client history and preference notes (the nail-industry content: shapes, colors, formulas, birthdays).
- Add-ons and service bundles in the catalog.
- Per-provider service pricing; per-technician payment attribution, tips, commissions, payroll.
- Two-technician (multi-provider) services and group bookings.
- Retail product sales and inventory in the same checkout.
- Packages, memberships, gift cards.
- Reviews/reputation and rebooking/retention automation; reporting.
- Multi-location support.

### Level 2 — Variant / Optional Structure

- **Bundled consumer marketplace** — the business listed in the vendor's consumer app with automatic business-type categorization (Vagaro-style) vs. deliberately marketplace-free postures (GlossGenius/Mangomint). Packaging variable, both directions documented.
- **Nail-art-studio configuration** — design-photo intake at booking, artist matching by specialization, complexity-based pricing, premium/level pricing ladders (single-product-strength evidence; likely to spread but recorded at current strength).
- **Walk-in-heavy vs appointment-led operating styles** — same core; the walk-in pole leans on waiting rooms, express booking, and counter-created appointments; the appointment-led pole leans on online booking and deposits.
- **Group/party visits** — multiple simultaneous clients (group checkout machinery Tier-1; group bookings cited as a nail requirement in the franchise case study).
- **Booth-renter economics** — independent technicians paying station rent inside a larger salon; payout tools (GlossGenius nail page).
- **Scale** — solo tech → single salon → multi-location franchise (Boulevard nail franchise customer).
- **Regional forms** — nail-only studios and design-led nail salons in other markets (Japan's Nailbook-class products unreachable — evidence gap, structure assumed to be the same core, not asserted).

### Level 3 — Vendor-specific (research notes only)

- Vagaro: business type auto-derived from service-name keywords (the full multi-industry keyword table incl. the Nail Salon list); appointment status color scheme; consumer marketplace "Find Businesses"; PayPro hardware.
- Mangomint: "Express Booking™", "Virtual Waiting Room" (brand names for the walk-in flow); nail art inspiration photo upload as a named feature; 2 technician-services as a named capability.
- GlossGenius: flat 2.6% processing-rate marketing; GeniusShop restocking; "Genius" AI agents; social-follower display of nail-tech users; competitive comparison table naming rivals.
- Boulevard: "Duo" card reader/client checkout app (hardware, incl. gratuity collection); Beau AI receptionist; per-provider price-sorted booking overlay.

## Boundary Findings

1. **vs Appointment-based Service Business Management (generic §29 leaf)** — same defining core; nail-salon management is the nail-industry Variant. Joint review per the barbershop/massage/med-spa precedent: keep-both ratified; the generic leaf holds the shared core, the industry leaf holds the industry expression. Removal test (from the med-spa pass) discharged: remove the regulated-treatment layer → the nail business runs on the same visit economy; no new object types found in research.
2. **vs Salon Management System (hair)** — same core; the overlay differs: hair salons carry color formulas/processing records; nail salons carry nail shapes/colors/design references. Nail overlay is thinner (no chemical-formula documentation culture observed in the researched sample). Distinction is emphasis, not structure; siblings cross-serve (platforms sell to both).
3. **vs Barbershop Management** — same core; barbershop overlay is individual-barber-as-brand, booth rent, walk-in/queue culture; nail shares the walk-in and booth-rent aspects but adds enhancement-service semantics (gel/acrylic) and the two-technician visit.
4. **vs Med Spa / Massage** — those siblings carry clinical/documentation overlays (consent, charting); no nail documentation emphasis observed in the researched sample — the nail client record carries preferences, not treatment notes. This absence is part of the variant's shape.
5. **vs Beauty Professional Business App** — the professional-centric packaging (the tech is the account) vs. this Type's establishment-centric record; nail techs with personal followings sit on the seam, and solo-tech packaging converges with it (same convergence noted by the massage and med-spa passes).
6. **vs Beauty Service Marketplace / Service Marketplace** — consumer-side discovery across providers vs. operator-side management of one salon; marketplace exposure is an optional bundled posture here (Vagaro) and deliberately absent in others.
7. **vs Retail POS** — shares the payment spine; remove the appointment spine and the technician/service-delivery context and only a POS remains. Nail retail (polish/tools) is a small appendage of the visit checkout, not the center.
8. **vs Appointment Scheduling Application (03.09)** — shares slot machinery; the client ledger + checkout + technician economics are the discriminator (unchanged from the generic pass).

## Uncertainties

- **Nail-native products could not be researched** (NailsMedia unreleased; Nailbook 403; search engines unusable). The researched sample therefore shows the variant as realized by multi-vertical platforms. Claims about nail-native software (if structurally different products exist) are NOT made; the nail-native pole is an evidence gap.
- Nail-specific client-content (shapes/colors) is directly evidenced in one product (GlossGenius, Tier-2). The wrapper claim (client records carry preferences) is Tier-1 across the family; the nail wording is single-product. Held at that strength.
- Two-technician services: machinery Tier-1 (Vagaro multi-provider services; Boulevard per-provider booking), nail-framed expression Tier-2 single-product (Mangomint "2 technician-services"). Held common-with-nail-expression, not universal.
- Walk-in emphasis: positioned as the nail headline by two products (Mangomint, GlossGenius) but the machinery (waiting list, walk-in checkout) is family-generic; whether walk-in handling is more salient for nails than for barbershops cannot be established from official docs (same gap the barbershop pass recorded). Held as emphasis, not structure.
- Nail art photo upload / artist matching: single-product Tier-2. Held variant, not common.
- Freecoat case-study percentages are vendor-published marketing figures; recorded, not propagated.
- Regional nail software (Japan etc.) unverified; no regional structural claims made.

## Final Synthesis

Nail Salon Management is the nail-industry Variant of the appointment-based service business core: bookable nail-service catalog (manicure/pedicure/enhancements with durations and prices), identified clients with preference records (nail shapes, colors), the appointment binding client × service × technician × time on the salon calendar, a lifecycle from booking through delivery with cancellation/no-show as named outcomes, and checkout that resolves the visit into recorded money with tips and per-technician attribution. The industry's contribution is overlay, not architecture: nail service vocabulary in the catalog (Tier-1 documented), preference-type client content, nail-art-informed booking (design photos, complexity- and seniority-based pricing, two-technician parallel services), and a walk-in-and-group visit culture that the products serve with waiting rooms, express booking, and group checkout. No researched product adds a new object type to the core; the market realizes the Type almost entirely through multi-vertical salon platforms configured for nails, with nail-native software an unresearchable gap this pass. Sharpest boundaries: against the generic core (same structure, different industry expression — kept as a separate leaf per family precedent), against salon/barbershop siblings (overlay content differs), and against med-spa/massage (no documentation layer here).
