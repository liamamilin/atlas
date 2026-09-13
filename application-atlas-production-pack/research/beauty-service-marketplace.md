# Research Notes — Beauty Service Marketplace

Research date: 2026-09-06

## Research Goal

Understand "Beauty Service Marketplace" as an Application Type: a consumer-facing, two-sided platform where many independent beauty providers (salons, studios, barbers, individual professionals) are listed, discovered, booked, and reviewed by consumers. Determine:

1. what the provider-side listing consists of and how the provider population is formed;
2. what consumer-side discovery looks like (search, filters, deals);
3. what the booking transaction is (availability, confirmation modes, payment posture, cancellation/no-show handling);
4. what trust machinery the platform operates (reviews, vetting, licensing);
5. how the marketplace posture relates to operator-side beauty SaaS (many vendors operate both sides);
6. where the boundaries with neighboring Types lie (Service Marketplace, Local Service Marketplace, Babysitting Marketplace, Salon/Barbershop/Beauty-professional operator Types, Appointment Scheduling, Directory/Review platforms).

## Initial Boundary (hypotheses before research)

- Core hypothesis: the Type is the beauty-domain sibling of other §29 marketplace leaves (Babysitting Marketplace): two-sided skeleton (provider profiles → consumer discovery → booking transaction → trust) structured by beauty services (hair, nails, makeup, barbering, skin).
- Biggest tension: the largest beauty booking companies (Fresha, Booksy, Treatwell, Vagaro, StyleSeat) are simultaneously operator-side business software and consumer-side marketplaces. Which surface defines the Type?
- Distinct from operator Types (Salon Management System, Beauty Professional Business App, Barbershop Management, Spa Management): those run ONE business; the marketplace's primary surface is discovery ACROSS many providers.
- Distinct from directories/review platforms: a directory lists and a review platform critiques; neither executes the booking transaction on-platform.
- Distinct from Appointment Scheduling Application (03.09): generic scheduling has no provider population, no cross-provider discovery, no platform trust layer.

## Research Questions

1. Provider side: what joins a provider to the marketplace (application? self-serve?), and what does a listing contain (services, durations, prices, portfolio, team, reviews)?
2. Consumer side: how does discovery work (location-based search? service categories? filters by time, price, rating; sort by proximity/rating)?
3. Booking: is availability live? Instant confirm vs request-to-book? Prepay vs pay-at-venue vs deposit vs card-on-file? Cancellation policies accepted at booking time? No-show rules?
4. Venue: in-salon vs house call (mobile service) — is service location a first-class choice?
5. Trust: reviews with photos? Verified purchase (appointment-based) reviews? Licensing/background checks? Verification of both sides?
6. Money: does the platform mediate payment, take commission, or is it subscription-SaaS with payment processing? (Evidence limited — major pure marketplaces unreachable.)
7. Variants: browse-listings vs request→offers vs platform-matched discovery; beauty-only vs beauty+wellness+fitness scope; independent vs managed/curated supply; consumer memberships; deals layer.

## Representative Products

Selected for market representation + documentation accessibility + different philosophies + different layers:

1. **Vagaro** — beauty/wellness/fitness business-management platform whose consumer app and website form a booking marketplace over its business customers. Chosen because its consumer-side help center (Tier 1) documents the entire discovery→booking loop operationally.
2. **Mindbody** — large wellness platform ("world's largest fitness & wellness marketplace" per its own site) with beauty as one vertical (hair salon, nail salon, lash salon, barbershop, hair removal). Chosen for the multi-vertical, enterprise-scale posture.
3. **Glamsquad** — managed on-demand beauty marketplace (in-home hair, makeup, nails) where the platform vets pros and matches them to consumer requests. Chosen for the full-stack/concierge philosophy.
4. **Mobile Styles** — on-demand US beauty/health marketplace with a public pro directory plus a request→offers flow. Chosen for the browse-independent-professionals philosophy.

Considered and rejected/unreachable: Fresha, Booksy, Treatwell, Urban Company, Blys, Soothe, The Glam App, YesMadam, StyleSeat (see Sources — accessibility).

## Sources

### Vagaro (Tier 1 — official support/help center)

- Support center home: https://support.vagaro.com/hc/en-us — fetched 2026-09-06 (A)
- Consumer category "Customers of a Vagaro Professional or Business": https://support.vagaro.com/hc/en-us/categories/115000379474-Customers-of-a-Vagaro-Professional-or-Business — fetched (A). Sections: Appointments, Getting Started, Gift Cards, Making Purchases, Memberships and Packages, Reviews, Managing Your Account, More.
- "Find a Vagaro Business - for Customers of a Vagaro Business": https://support.vagaro.com/hc/en-us/articles/360006273733-Find-a-Vagaro-Business-for-Customers-of-a-Vagaro-Business — fetched (A)
- "Book a Service Appointment - for Customers of a Vagaro Business": https://support.vagaro.com/hc/en-us/articles/115003521813-Book-a-Service-Appointment-for-Customers-of-a-Vagaro-Business — fetched (A)
- "Book a Mobile Service (House Call) - for Customers of a Vagaro Business": https://support.vagaro.com/hc/en-us/articles/360055718674-Book-a-Mobile-Service-House-Call-for-Customers-of-a-Vagaro-Business — fetched (A)

### Mindbody (Tier 2 — official site)

- https://www.mindbodyonline.com/ — fetched 2026-09-06 (A). Business-type navigation includes Beauty vertical (barbershop, hair removal, hair salon, lash salon, nail salon); consumer app positioning ("Discover local fitness, beauty & wellness services on the Mindbody app"); "Explore" consumer marketplace with a Beauty section (explore/beauty/search/locations); operator pitch "Get discovered by 3M+ active users", "world's largest fitness & wellness marketplace".
- https://www.mindbodyonline.com/explore/beauty/search/locations — JS-only shell, not usable (abandoned after 1 attempt).

### Glamsquad (Tier 2 — official site)

- https://glamsquad.com/ — fetched (A): in-home hair/makeup/nails; booking steps (address → services → date/time → account → matched pro); pro vetting claims (licensed, background checked, experience requirements); Become a Pro at apply.glamsquad.com; membership; weddings/events/group services.
- https://glamsquad.com/how-it-works — fetched (A): 4-step flow; "Match with top-tier beauty pros" (vetted, certified); same-day availability; prep instructions per service; cancellation policy with detailed windows/fees; in-app communication window with the pro; "no physical salon locations".
- https://glamsquad.com/faq — fetched (A): FAQ category index (Appointments, Billing, Gratuity, Memberships, Payment, Promotions, Refunds, Reservations, Service Packages, Gift Certificates, Group Reservations…).

### Mobile Styles (Tier 2 — official site)

- https://mobilestyles.com/ — fetched (A): on-demand health & beauty; categories (Barbering, Coloring, Haircut, Makeup, Nail, Waxing, Massage); "Pick the place and time / Choose your PRO / Enjoy"; directory of professionals; Become a PRO (application, free membership, weekly payments, own schedule); gift cards; referrals.
- https://mobilestyles.com/how-it-works — fetched (A): download → register (client and PRO registrations) → book a service (100+ services; "receive multiple offers by verified PROs in your area") → find a PRO ("5,000 vetted and licensed PROs" directory) → pro arrives; verification ("certifies each PRO and Client using phone verification and ID scan"); active/licensed in 38 states (marketing stat, not used in final doc).
- https://mobilestyles.com/professionals (directory page) — linked from fetched pages but not itself fetched; directory existence is A-evidenced via fetched pages, directory page details are not.

### Unreachable sources (abandoned per network-failure rules; no claims made about these vendors)

- Fresha: fresha.com/for-business (403), support.fresha.com (403) — 2 attempts. (Also unreachable in the earlier barbershop-management pass.)
- Booksy: booksy.com (403), booksy.biz (empty response) — 2 attempts. (Unreachable in barbershop pass too.)
- Treatwell: treatwell.co.uk (403), get.treatwell.co.uk (transport error) — 2 attempts.
- Urban Company: urbancompany.com (403), help.urbancompany.com (transport error) — 2 attempts.
- Blys: getblys.com (403), www.getblys.com (403) — 2 attempts. (blys.co is an unrelated designer portfolio — wrong domain.)
- Soothe: soothe.com (403) — 1 attempt.
- The Glam App: theglamapp.com (transport error) — 1 attempt.
- YesMadam: yesmadam.com (JS-only shell) — 1 attempt.
- Mindbody consumer "Explore Beauty" page: JS-only shell — 1 attempt.
- StyleSeat: unreachable in earlier passes (JS shell + 404); not re-attempted here.

**Consequence (Source-access Limitation):** the best-known beauty-native booking marketplaces (Fresha, Booksy, Treatwell) and the largest full-stack managed marketplace (Urban Company) could not be observed operationally. All marketplace-structure claims in the final document therefore rest on the four reachable products; claims are worded at cross-product-commonality strength, and market-model claims (commissions, provider fees, payout schedules) are NOT asserted. Numbers, windows, and fees from reachable products are kept in these notes (or stated with product attribution) and stay out of the canonical document.

## Product A — Vagaro (Tier 1, consumer-side help center)

### Key observations (evidence layer A unless noted)

**Positioning** — "Vagaro is a business management software platform that helps wellness, beauty, and fitness businesses manage their business and allows their customers to schedule online." The consumer side ("Customers of a Vagaro Professional or Business") is a first-class surface: web + consumer app ("for customers"), separate from the operator app ("for businesses").

**Discovery (consumer)**
- Search by business name, location, or service ("Search for the business, location, or service"), on web and app.
- No account needed to search; an account is required to book.
- Location settings drive "businesses closest to you and their business hours in your time zone".
- Category browse under the search bar: **Beauty**, **Wellness**, **Fitness**, then specific business types.
- Filters: **Anytime → day and time** you want to book; **Type of Service**: in-person, house call, or live stream services.
- Result-list controls: **Sort** by **Nearest** (default) or **Highest Rated**; **Map** view of locations; **Filter** to reduce results.
- Bookmarked businesses (save/list); share a business or deal; view a business's working hours.
- **Daily Deals on the Marketplace** — a dedicated deals surface.

**Listing page (business)**
- "Vagaro Listing Page" with **Services** tab: all services the business offers, expandable categories; add-ons per service; Mobile Service icon on eligible services.

**Booking transaction (consumer)**
- Three per-business booking modes surfaced as button variants: **Book Now** (book directly onto the business's calendar), **Request** (business requires acceptance before scheduling), **Add to Cart** (prepay for appointments before booking).
- Choose employee + date + timeslot from a live scheduler; browse weeks; up to six services in one booking ("Add Service"); waitlist if no slot fits (business-permitted).
- Finalization: booking for someone else (**Who Are You Booking For** — family, friend, pet); notes/requests to the business; **review and accept the business's cancellation policy (if applicable)**; **some businesses may require a deposit or card on file** before scheduling.
- **Mobile service (house call)**: service-location choice — At the Business's Location / At My Location (profile address) / Different Location; same book modes, deposit/card rules.
- Post-booking: view upcoming/past appointments, add to calendar, rebook, join waitlists.

**Money (consumer)**
- Pay with saved card; promo codes; gift cards (buy/redeem); buy memberships and packages from a business; request refunds FROM the business (refund is business-side, not marketplace-side); Affirm financing offered on some purchases.

**Trust**
- Reviews: write a review, manage reviews you posted, add photos to a review. (Verified-appointment linkage not stated in fetched articles.)
- Sort by Highest Rated in search.

**Provider side (from the same help center's operator categories — A)**
- Operator console categories: Calendar and Scheduling, Things You Sell, Customer Management, Employee Management, Checkout, Credit Card Processing, Marketing Your Business, Payroll, Reports, Business Settings — i.e., the marketplace consumer surface sits on top of full operator software operated by the same vendor.
- Businesses join via signup/trial (self-serve).

## Product B — Mindbody (Tier 2, official site)

### Key observations (A for wording on fetched pages; operational detail not observed)

**Positioning** — business management software for fitness, wellness, and beauty; consumer side is "the world's largest fitness & wellness marketplace"; businesses "get discovered by 3M+ active users" on the Mindbody app; "Discover local fitness, beauty & wellness services on the Mindbody app" (Explore). 40,000+ businesses; beauty business types listed: Barbershop, Hair removal, Hair salon, Lash salon, Nail salon. (Marketing stats — recorded here, not used in the final document.)

**Structure**
- Two-sided: operator software (payments, scheduling, staff, marketing, reporting; branded apps; ClassPass integration) + consumer marketplace app with a Beauty browse section (explore/beauty — URL structure observed; page content not fetched).
- Beauty is one vertical inside a multi-vertical wellness marketplace — the marketplace aggregates class-based fitness AND appointment-based beauty/wellness businesses.

**Not observed** — consumer booking mechanics, payment posture, review mechanics on the consumer surface (JS shell). No operational claims about Mindbody's consumer flow are made anywhere.

## Product C — Glamsquad (Tier 2, official site)

### Key observations (A)

**Positioning** — "We bring beauty to you. In-home hair, makeup and nail services." No physical salon locations; services performed at the address the consumer provides (home, hotel, office, venue).

**Discovery model — platform-matched, not browse-listings**
- Booking flow: input address → choose services → choose date/time → create account → "Match with top-tier beauty pros" ("paired with a vetted, certified pro who specializes in exactly what you need"). The platform assigns the pro; consumers may request a specific pro with assistance from the support team ("request a specific Beauty Professional, just reach out").
- Same-day service available.

**Supply side**
- "Become a Beauty Pro" via application (apply.glamsquad.com); pros described as "fully licensed hair and nail artists", "background checked", with experience requirements (7 years average — marketing stat, recorded here only).
- Bridal-certified pros; concierge team for group/wedding bookings.

**Booking lifecycle**
- Cancellation policy: windows and fees vary by day of week, market, and special events; rescheduling treated as cancellation; members never pay cancellation fees; changes <4h may incur fees; readiness rule — pro waits 15–20 minutes, then full charge.
- In-app **Communication Tab** with the pro opens ~1 hour before the appointment and stays open until completion.
- Modification: cancel/adjust time self-serve; add service/guest/switch type via support.

**Money**
- Card-charged appointments (cancellation fees, full charges); payment, billing, refunds, gratuities, promotions, gift certificates, service packages FAQ categories; consumer **Membership** program.

**Trust**
- Vetting-first (licensed/background-checked/certified) rather than browse-and-compare reviews; star-rated testimonials appear on the marketing site.

## Product D — Mobile Styles (Tier 2, official site)

### Key observations (A)

**Positioning** — "On-demand professional health and beauty services"; connects clients with "local health and beauty professionals" who travel to the client ("Your PRO will arrive"). US, licensed in 38 states (marketing stat, recorded here only).

**Discovery — directory + offers (two mechanisms on one platform)**
- **Directory**: public "Service and PRO directory" browsable by category (Barbering, Coloring, Haircut, Makeup, Nail, Waxing; Massage listed among services); "Explore over 5,000 vetted and licensed PROs" (marketing stat).
- **Offers**: "Search over 100+ salon-grade beauty services and receive multiple offers by verified PROs in your area" — request→offers flow alongside the directory.

**Booking flow (site narrative)** — Pick the place and time → Choose your PRO → PRO arrives and delivers the service.

**Verification/trust**
- "MOBILESTYLES certifies each PRO and Client using phone verification and ID scan"; pros are "vetted and licensed"; review culture: "Submit before and after pictures of your service" for social features ("Just Completed, What People Are Saying").

**Supply side**
- PRO registration/application; free membership for pros; **weekly payments** to pros; pros set their own schedule; social featuring of pro work.

**Money (consumer)**
- Gift cards (send), referrals, special offers/discounts; payment mechanics not documented on fetched pages — not asserted.

## Cross-product Comparison

| Dimension | Vagaro | Mindbody | Glamsquad | Mobile Styles | Evidence |
|---|---|---|---|---|---|
| Provider population | businesses (beauty/wellness/fitness) on operator SaaS (A) | businesses incl. beauty vertical (A, wording) | individual beauty pros, applied + vetted (A) | independent pros, registered + verified (A) | B: marketplace aggregates many providers on one consumer surface |
| Consumer discovery | search by business/location/service + category browse + filters (time, service type) + sort nearest/highest-rated + map + deals (A) | consumer app marketplace, beauty section (A wording; mechanics not observed) | platform-matched after address+service+time (A) | public pro directory by category + request→multiple offers (A) | B with model variance: browse vs match vs offers |
| Bookable unit | service from a business's service menu w/ categories + add-ons (A) | not observed | service(s) at consumer's address (A) | service (100+) from a pro (A) | B: provider-structured beauty service offering is the booked unit |
| Confirmation modes | Book Now (instant) / Request (provider accepts) / Add to Cart (prepay), per business (A) | not observed | platform matches/pro assigned (A) | offers→choose pro (A) | B: instant-vs-request-vs-matched variance; mechanism is per-provider/platform |
| Venue model | at business / at my location / different location, per service (A) | not observed | house-call native (A) | house-call native (A) | B: venue is a first-class booking parameter |
| Payment posture | prepay optional per business; deposit/card-on-file possible; refunds from business (A) | not observed | card-charged; fees/windows; membership waives fees (A) | in-app implied; not documented (not asserted) | B: payment posture varies (prepay / at-venue / deposit); not universal |
| Cancellation | business's own policy accepted at booking (A) | not observed | platform policy, detailed windows/fees (A) | not documented | B: cancellation policy surfaced and accepted at booking |
| Trust layer | reviews + photos + Highest Rated sort (A) | not observed | vetting (licensed/background-checked/certified) (A) | reviews/before-after + ID verification of both sides (A) | B: platform-operated trust (reviews and/or vetting) — universal in sample |
| Consumer account | required to book; bookmarks; booking history; family/friends; rebook (A) | account required (app) | account creation in booking flow (A) | registration required (A) | B: consumer account + history |
| Provider onboarding | self-serve signup to operator platform (A) | operator signup (A wording) | application → vetting (A) | PRO application; free membership; weekly payouts (A) | B: provider side joins via application/signup |
| Deals/promotions | Daily Deals surface; promo codes; gift cards (A) | not observed | promotions, gift certificates, packages (A) | offers, discounts, referrals, gift cards (A) | B: promotion layer is standard |
| Scope | beauty + wellness + fitness (A) | fitness + wellness + beauty (A) | beauty only (hair/makeup/nails) (A) | beauty + health/wellness services (A) | B: vertical scope varies; beauty is the constant |
| Marketplace-vs-SaaS posture | SaaS-first, marketplace on top (A) | SaaS-first, marketplace on top (A wording) | demand-first managed marketplace (A) | demand-first marketplace w/ directory (A) | A: posture is the major philosophical axis |

## Canonical Abstraction

### Level 0 — Defining Invariant

A Beauty Service Marketplace is recognizable as this Type when all of the following hold:

1. **Platform-operated provider population** — many independent beauty providers (businesses or individual professionals) exist on the platform as listings/profiles the platform operates. Remove this → single-business booking page (operator-side scheduling), not a marketplace.
2. **Cross-provider consumer discovery** — consumers browse/search/filter/sort ACROSS the provider population (by service, location, time, price/rating). Remove this → each provider is just a separate booking site; the marketplace's defining surface disappears.
3. **On-platform booking transaction** — the platform records a binding booking (consumer × beauty-service offering × provider × time) and manages its lifecycle (confirmation, modification, cancellation, completion). Remove this → a directory/review platform, not a marketplace.
4. **Beauty-service structuring** — the booked unit is a beauty service offering (hair, nails, makeup, barbering, skin/lash/wax services) presented with provider-defined parameters (category, duration, price where applicable). Remove this → generic service marketplace.

Deliberately NOT in L0 (tested): in-app payment at booking (many bookings settle at the venue), ratings/reviews specifically (vetting-based trust satisfies the same need), mobile app surface, commission model, house-call delivery, consumer memberships, deals.

### Level 1 — Common Mature Structure

- **Trust layer** operated by the platform: ratings/reviews attached to providers (review + photos + management, rating-informed sorting) and/or vetting/verification (licensing, background checks, ID verification). Universal in the sample, but the form varies (browse-reviews vs vetting-first).
- **Live availability and scheduling tooling**: real-time timeslot selection against provider calendars; date/time filters in discovery.
- **Listing page as the point of sale**: provider profile with service menu (categories, durations, prices), add-ons, portfolio/photos, policies.
- **Consumer account**: booking history, saved/bookmarked providers, rebooking, booking for others, notifications/reminders.
- **Cancellation and no-show machinery**: policies surfaced and accepted at booking; deposits/card-on-file requirements as enforcement instruments.
- **Provider-side console** (often the same vendor's operator software): listing management, calendar, request acceptance, customer records, checkout.
- **Promotion layer**: deals/discounts, promo codes, gift cards, packages.
- **Mobile app as the primary consumer surface**; web as companion.
- **Dual-surface posture**: the marketplace usually coexists with operator-side business software, sometimes from the same vendor.

### Level 2 — Variant / Optional Structure

- **Discovery philosophy**: browse-listings (directory-style, consumer picks provider) ↔ request→offers (consumer posts need, pros bid) ↔ platform-matched (concierge assigns pro).
- **Provider unit**: businesses/salons vs individual professionals vs both.
- **Venue model**: in-salon/in-studio vs house-call (at consumer's location) vs both; service-location choice at booking.
- **Vertical scope**: beauty-only vs beauty+wellness+fitness multi-vertical.
- **Supply curation**: open self-serve listings vs vetted/curated/managed supply (licensing/background checks as entry conditions).
- **Payment/commercial posture**: pay-at-venue vs prepay vs deposits vs platform-mediated payouts; commission vs subscription vs free-tier economics for providers (economics NOT verified across the sample — see Source-access Limitation).
- **Consumer monetization extras**: memberships (fee waivers, perks), packages, points/loyalty.
- **Immediacy**: advance booking vs same-day on-demand emphasis.
- **Regional/market models**: European connect marketplaces and South Asian full-stack managed marketplaces are known market forms; NOT operationally verified in this pass (vendors unreachable) — recorded as market knowledge only, no claims.
- **Adjacent booking types on the same platform**: classes/live-stream sessions (multi-vertical wellness), retail product purchase.

### Level 3 — Vendor-specific (research notes only)

- Vagaro: Book Now/Request/Add-to-Cart button semantics; "book up to six services at once"; family/friend/**pet** booking targets; live-stream service type; QR codes; waitlists; Daily Deals; Affirm financing; operator suite breadth (payroll, reports, e-prescribe for some verticals).
- Glamsquad: cancellation windows varying by weekday/market/special events; $25 fee band Fri–Sun 4–12h; The Hamptons 24h window; 15–20 minute readiness rule then full charge; Communication Tab opens ~1h before appointment; bridal certification; Group Glam concierge; ambassador program.
- Mobile Styles: phone verification + ID scan for BOTH sides; weekly pro payouts; free PRO membership; "Just Completed" social featuring; 38-state licensing claim.
- Mindbody: 3M+ active users / 40k+ businesses / 600M bookings per year claims; ClassPass integration; branded-app product; Mindbody Capital.

## Vendor-specific Findings → Rejected Findings

- **Rejected: "Beauty Service Marketplace = booking software with a commission."** Vagaro/Mindbody show marketplaces operating on a SaaS posture where consumers settle with the business and the platform does not necessarily mediate every payment. Commercial mediation is a business-model variant, not defining.
- **Rejected: "Reviews are the defining trust mechanism."** Glamsquad is vetting-first with no browse-compare review culture on fetched surfaces; Mobile Styles adds ID verification. The abstract concept is a platform-operated trust layer; reviews are its most common implementation.
- **Rejected: "Marketplaces are consumer-paid."** In the sample, consumers usually pay nothing to the platform directly; fees (where they exist) attach to cancellations or provider economics. No fee-structure claims are made (evidence insufficient).
- **Rejected: "House call is the defining mode."** Two of four sampled products are house-call-native, but Vagaro treats venue as a per-service parameter. Venue model is a variant dimension.
- **Rejected: "Beauty Service Marketplace is just Local Service Marketplace with a narrower catalog."** The beauty domain structurally shapes the object (provider-defined service menus with duration/price, portfolio imagery, licensing/vetting norms, gratuity culture, before/after review photos). Held as a sibling Type with domain structuring, consistent with the Babysitting Marketplace precedent.

## Boundary Findings

| Neighbor | Test | Result |
|---|---|---|
| **Service Marketplace (05.02) / Local Service Marketplace (§29)** | strip beauty-service structuring (service menus, licensing/vetting norms, beauty categories) → generic service marketplace | distinct sibling; boundary = domain structuring |
| **Babysitting Marketplace (§29, processed)** | same two-sided skeleton; different domain objects (caregivers/children/safety) | sibling Types, not variants — consistent with that leaf's research |
| **Salon Management System / Beauty Professional Business App / Barbershop Management / Spa Management (§29 operator leaves)** | whose surface is primary: strip the multi-provider consumer discovery from a bundled product → operator SaaS remains (still recognizable); strip operator tools → consumer marketplace remains | distinct Types; the same vendor may operate both surfaces; posture gradient documented (Vagaro/Mindbody SaaS-first; Glamsquad/Mobile Styles demand-first) |
| **Appointment Scheduling Application (03.09)** | remove provider population + cross-provider discovery + platform trust → single-organization scheduling tool | distinct; scheduling mechanics are shared machinery, not the Type |
| **Directory Application (02.11) / Listings Platform / Review Platform (02.10)** | remove the on-platform booking transaction → directory/review platform | the booking transaction is the Type line |
| **Online Marketplace (05.02) / Retail POS (05.10)** | marketplace sells appointments at future times with fulfillment by humans; POS executes in-person goods transactions | distinct objects and flows |
| **Food Delivery Marketplace (26) / OTA (26)** | same two-sided booking-marketplace family, different domain objects and fulfillment semantics | analogous structure; different Types |
| **Personal Styling Platform (§29, unprocessed)** | styling advice/recommendation vs executing beauty-service bookings | expected distinct; left to that leaf's pass |
| **Virtual Beauty Try-on Application (§29 sibling)** | consumer AR surface over appearance; no provider population, no bookings, no money flow | different world; no overlap |

## Uncertainties

1. **Commercial economics unverified**: commission rates, booking fees, provider subscription pricing, payout schedules of beauty-native marketplaces (Fresha/Booksy/Treatwell/Urban Company) could not be observed. No such claims appear in the final document.
2. **Pure-marketplace discovery mechanics** (deals-first browsing, ranking algorithms, paid placement) unverified; the sample's discovery evidence comes from SaaS-first and on-demand products.
3. **Review authenticity mechanics** (verified-appointment review gating) not observed for any sampled product — Vagaro documents review creation but not its eligibility rule.
4. **Mindbody consumer flow** unobserved (JS shell); Mindbody contributes positioning/vertical evidence only.
5. **Full-stack managed model** (Urban Company-style: platform-employed/managed supply) known as a market form but not operationally verified; recorded as a possible L2 variant with low confidence.
6. Whether "Beauty Service Marketplace" should eventually merge into a general "Service Marketplace" Type with domain variants is a taxonomy-owner question; this pass documents it as a domain sibling per the Babysitting Marketplace precedent.

## Final Synthesis

A Beauty Service Marketplace is a consumer-facing, two-sided application that aggregates many independent beauty providers — salons, studios, and individual professionals — onto one platform-operated surface, structures them through provider-defined beauty service offerings, lets consumers discover across the whole population (by service, location, time, and reputation), executes the booking transaction on the platform (binding consumer × service × provider × time, with confirmation, modification, and cancellation lifecycle), and operates a trust layer (reviews and/or vetting) over the provider population.

Around that core, mature products converge on: live availability, listing pages as points of sale, consumer accounts with history and rebooking, cancellation/deposit enforcement, provider consoles, promotion layers (deals, gift cards, packages), and mobile-app-first delivery. The market divides most visibly on: discovery philosophy (browse vs offers vs platform-matching), provider unit (business vs individual), venue model (in-salon vs house call), vertical scope (beauty-only vs beauty+wellness+fitness), supply curation (open vs vetted/managed), and commercial posture (marketplace-mediated vs SaaS-hosted with payment processing).

The Type is the consumer-side counterpart of the beauty operator Types: when a product's primary surface is running one business, it is operator software; when its primary surface is discovery across many providers, it is this Type — even when one vendor ships both.
