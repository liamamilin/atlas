# Research Notes — Appointment-based Service Business Management

Research date: 2026-09-06

## Research Goal

Understand the software category used by businesses whose revenue model is built on client appointments for services — salons, barbershops, spas, massage and wellness studios, nail salons, medspas and similar appointment-driven service businesses — and derive the canonical structure of such systems: what objects exist, how booking works, how the appointment travels to service delivery and payment, and where the boundaries lie against pure scheduling tools, POS, field-service management and marketplaces.

## Initial Boundary

Initial hypothesis (before research):

- The leaf sits in Directory §29 between "Personal Concierge Platform" and "Local Service Marketplace", surrounded by industry-specific leaves (Salon Management System, Barbershop Management, Spa Management System, Massage Practice Management, Nail Salon Management...). It appears to be the **generic** appointment-based service business management Type, of which those siblings are industry variants.
- Closest neighbors to test against:
  - **Appointment Scheduling Application (03.09)** — the booking/calendar machinery alone.
  - **Retail POS (05.10)** — the money/checkout machinery alone.
  - **Small Business Field Service Management (§29)** — appointment-like scheduling but service is delivered at the customer's location with dispatch/travel/job-quote semantics.
  - **Local Service Marketplace (§29)** — consumer-side discovery vs operator-side management.
  - **Patient Scheduling / Practice Management (§22)** — regulated clinical variant.
- Working assumption: the defining difference from plain scheduling is that this Type runs the *business* around the appointment: identified clients, service history, checkout/money, and staff economics.

## Research Questions

1. What objects make up the system's world? (service, client, staff/provider, appointment, resource, transaction...)
2. How does booking work — staff-side and client self-booking? What makes a slot bookable?
3. What is the appointment lifecycle? Which states exist between booking and completion, and how are cancellation/no-show handled?
4. How does the appointment resolve into money? What does "checkout" mean here (services + retail, redemption of prepaid balances, tips, split payment, refunds)?
5. What does the client record carry (history, notes, formulas/photos, forms, balances)?
6. What staff structures exist (schedules, time off, commissions/payroll, roles)?
7. Which capabilities are common but not defining (marketplaces, memberships, packages, gift cards, reviews, marketing, AI)?
8. Where is the boundary against scheduling-only tools, POS, field service, and marketplaces?
9. Would older / regional / non-marketplace products still fit the definition?

## Representative Products

| Product | Segment / philosophy | Customer tier | Why selected |
|---|---|---|---|
| Vagaro | Salon/spa/fitness suite with consumer marketplace; deep help center | SMB, solo → chains | Best-documented operational flow of the sample |
| Zenoti | Enterprise spa/salon/wellness platform for multi-center organizations | Enterprise / chains | Different tier + vocabulary (guest/center/therapist); API docs expose the full object model |
| GlossGenius | Solo-first, mobile-first "all-in-one" for beauty/wellness; no client app needed | Solo / small teams | Different philosophy (single-operator focus, payments-native) |
| Square Appointments | Booking product inside a general payments/commerce platform | Solo → large salons | Payments-platform philosophy; shows the Type as a scheduling+POS combination |

Notes on sampling: Fresha and Booksy (marketplace-first vendors) were also candidates but their sites were not fetchable from the research environment (see Sources — access limitations). Class-heavy wellness platforms (Mindbody-style) were deliberately not sampled as primary; class structures observed in Vagaro/Square/Zenoti are treated as variant structures.

## Sources

Tier 1 (official operational documentation):

- Vagaro Support (Zendesk help center), fetched 2026-09-06:
  - Home: https://support.vagaro.com/hc/en-us
  - Calendar and Scheduling category: https://support.vagaro.com/hc/en-us/categories/115000066033-Calendar-and-Scheduling
  - Service Appointment Statuses & Colors: https://support.vagaro.com/hc/en-us/articles/28544779074971-Service-Appointment-Statuses-Colors
  - Checkout category: https://support.vagaro.com/hc/en-us/categories/22542821917083-Checkout
  - Customer Management category: https://support.vagaro.com/hc/en-us/categories/200260220-Customer-Management
  - Things You Sell category: https://support.vagaro.com/hc/en-us/categories/1260800189649-Things-You-Sell
- Zenoti API documentation (llms.txt index + pages), fetched 2026-09-06: https://docs.zenoti.com/llms.txt (service booking flow: create booking → slots → reserve → confirm → collect payment; guest/center/service/room/employee/membership/package/gift-card/loyalty objects)

Tier 2 (official product pages):

- GlossGenius homepage/platform pages: https://glossgenius.com/ (platform modules, industries, FAQ), fetched 2026-09-06
- Square Appointments product page: https://squareup.com/us/en/software/appointments (fetched 2026-09-06; feature pages listed: reminders, booking website, cancellation policy, multi-location, waitlist, Square Assistant, Square Go marketplace)

Access limitations:

- Fresha: https://support.fresha.com/hc/en-gb → HTTP 403; https://www.fresha.com/for-business → HTTP 403. Abandoned after 2 attempts; no Fresha evidence used.
- Booksy: https://booksy.com/biz → HTTP 403. Abandoned after 1 attempt; no Booksy evidence used.
- GlossGenius Learning Center (elevio): https://glossgenius.elevio.help/en returned an empty JS shell; GlossGenius assertions therefore rest on its own platform pages (Tier 2), not on help-center articles.

## Product Observations

### Vagaro (evidence layer: A — direct observation of Tier-1 help center)

Object structure observed:

- **Services / Things You Sell**: services (with categories, service menu ordering, prices), service bundles, add-ons (created for services & classes, applied when booking or checking out), classes/workshops, gift cards, memberships, packages (Vagaro documents a "Difference Between a Package and a Membership" article), retail products (inventory with variants, brands, vendors, product bundles), **resources** ("Add Resources to Services and Classes" — rooms/equipment attached to what you sell).
- **Customer Management**: customer profile overview, profile picture, referrer, general tags, customer notes, retention tracking, **appointment history**, class attendance history, purchased products, IOUs, family & friend sharing (including sharing memberships/packages), merge & clean up customers, delete/restore, customer reviews (respond, review standards), blocking a customer from online booking, points balance.
- **Calendar and Scheduling**: calendar configuration, calendar icons and appointment status colors, employee calendars and **resource calendars**, online appointment rules (require acceptance for online booking, auto-assign employees for online bookings, employee booking order, block family & friend bookings, require a membership or package for online appointments, block new customers from booking online), notifications & reminders (with HIPAA-compliant notification option), booking single appointments, repeating appointments, service bundles, rebooking, scheduling multiple appointments at once, rescheduling; personal tasks, blocking holidays, time off; calendar sync (Google Calendar), print appointment ticket, daily plan.
- **Employee Management / Payroll** categories exist as first-class sections.
- **Checkout** category: check out a customer's appointment, check out walk-in customers, save a checkout for later, group customers at checkout, change the price of an item at checkout, **change who's performing a service at checkout**, accept cash/check, split payment at checkout, create and send an invoice at checkout, redeem gift cards / membership visits / package visits at checkout, cards on file, charge a customer's card, enter card payment without Vagaro Merchant Services (BYO processing), refunds (incl. refunding packages and partially redeemed packages, issuing a gift card as a refund), Tap to Phone, discounts and daily deals (with discount approval), tips, receipts, taxes, maximum checkout amount.
- **Appointment statuses & colors** (documented explicitly): Requested (purple) → Accepted (light blue) → Awaiting Confirmation (yellow) → Confirmed (pink) → Show (light green) → Ready to Start (blue) → In Progress (green) → Complete (grey); plus No-Show (red) and Cancel. Cancel and No-Show can carry a fee charged to the customer's card on file; No-Show increments the customer's no-show total in their profile. "Undo a Checked-Out Appointment" exists (checked-out is effectively the terminal/completed state where checkout occurred).
- **Mobile service**: "Notify Customers about Their Mobile Service" — Vagaro supports services performed at the customer's location as an in-product mode.
- Marketplace: consumer Vagaro app + "Find Businesses" — the business is listed in a consumer discovery surface; separate consumer app; "Customers of a Vagaro Professional or Business" category; consumer booking without login per product pages.
- Also: Live Stream services (start service via video), Check-in App, Vagaro Drive, Connect by Vagaro, developer features, E-Prescribe category (vertical extension), HIPAA compliance claim.

### Zenoti (evidence layer: A — direct observation of Tier-1 API documentation)

Object structure observed (API reference):

- **Organization → Centers** (multi-center; "Search Guest Across Centers" org setting; center categories, rooms, services, packages, products, memberships).
- **Services**: list per center with categories/sub-categories, variants, add-ons; therapist pricing and **price scaling per therapist** ("therapists who can perform a particular service").
- **Employees / Therapists**: per-center rosters, schedules (retrieve/update per day), attendance (check-in/check-out), blockout times (per employee and per room; recurring blockouts; blockout types such as lunch/training/break), security roles and permissions (e.g., a "Schedule" role permission required to view schedules).
- **Rooms**: per-center rooms with blockout times — resources are bookable objects.
- **Guests** (clients): create/update/merge guests, guest search across centers, guest notes (typed, with alerts; private notes), guest forms (v2 forms with signatures), guest relationships (family/spouse/friend — group bookings made by a "host" guest), saved cards, appointment history per guest, products purchased per guest, gift cards, prepaid cards, coupons, series packages owned/redeemed per guest, memberships per guest (freeze/unfreeze, auto-renewal change/cancel, pending collection), loyalty points (earn/redeem, tiers), password/OTP self-service.
- **Service booking flow** (documented as a 4-step recipe): Create a service booking (guest + item details; therapist preference or therapist-gender preference; group bookings) → Retrieve available slots → Reserve a slot → Confirm the booking ("Invoice id ... generated only when you confirm") → Collect payment for the invoice. Reschedule = re-run the booking flow against the previous booking's invoice id. Service bundles and day packages bookable; couple bookings supported.
- **Money objects**: invoice + invoice items; collect payment for invoice; gift card balance verification; loyalty redemption against an invoice; coupons; product sale flow (choose product → generate invoice → collect payment); membership sale flow; gift card sale flow; prepaid cards.
- **Opportunities**: upsell/sales pipeline objects inside the platform (stages, dispositions, sources, sales stage rules).
- **Classes**: class registrations/booking APIs (fitness side).
- **Webstore / customer mobile app** mentioned as native online-booking channels; "Checkout as guest" dummy-guest flow for online stores.

### GlossGenius (evidence layer: B for structure — vendor's own platform pages, no help-center access)

Platform structure observed (from glossgenius.com):

- **Booking & Scheduling**: Online Booking ("no client logins or app downloads required"), Website Builder, Reserve with Google, Calendar & Scheduling, Waitlist, Resource Management, **No-Show Protection** (card on file).
- **Marketing & CRM**: Client Management, Client Notifications, Client Insights, Client Reviews, Forms & Waivers, Photo Markup.
- **Payments & POS**: Payments (integrated processing, flat advertised rate), Card Readers & Point of Sale, Invoices, Buy Now Pay Later, Instant Payouts, **Memberships & Packages**, Gift Cards, Loans & Financing.
- **Staff & Business**: Payroll, Time Tracking, Staff Management, Reports & Analytics, Goal Setting, Finances, Inventory Management, Free Data Transfer (migration import).
- **EMR module** for medspa/health verticals: Charting, Forms & Waivers, Photo Markup — clinical overlay on the same core.
- Multi-provider teams: "individual staff calendars with personalized access permissions, team-wide sales and performance reporting, employee time tracking, integrated payroll reporting for commissions, tips, and hourly wages" (vendor FAQ).
- Industries targeted: hair/nail/lash/brow/makeup/tanning/tattoo/barber salons; esthetics, massage & spa, acupuncture, chiropractic; medspa (injectables & laser, medical weight loss); physical/behavioral therapy; yoga/pilates/personal training. Business sizes: solopreneur, booth renters, single location, multi-location.
- Positioning: revenue/rebooking-centered ("75% average rebooking rates"), AI "Agents" (Growth/Marketing/Reception answering calls/texts 24/7), automation-driven rebooking.

### Square Appointments (evidence layer: B for structure — vendor's own product page)

Capabilities observed:

- Booking site (free tier), bookable 24/7; embed on website, links from Google/Instagram, QR code booking.
- Staff: "unlimited staff schedules", team members bookable at any location; staff working hours and services-per-staff assignment; double-booking prevention described as availability-driven.
- **Resources**: "Assign rooms, stations, or chairs to services so they get booked when clients make appointments."
- Payments: all major types, digital wallets, gift cards, Tap to Pay; "Keep cards on file for no-show protection" — hold appointments, manage prepayments, charge cancellation fees; sell prepaid packages ("secure cash upfront").
- Reminders: automated email/SMS confirmations, reminders, easy rescheduling; Square Assistant (AI-generated appointment messages); waitlist that "automatically fills cancellation openings".
- Client profiles: "transaction history, texts, and emails", "preferences, birthdays, documents, images, and files"; forms and contracts collected during booking; built-in customer directory with CSV import.
- Products & services "in the same transaction" with inventory tracking; loyalty, marketing, invoices, gift cards, websites, banking/payroll as sibling Square products.
- **Square Go marketplace**: "Get discovered and booked by clients" — a consumer discovery app.
- Multi-location scheduling; classes ("single sessions or recurring classes"); pricing tiers gated by features (cancellation policy & no-show fees, multi-staff booking, waitlist, resource management at higher tiers).

## Cross-product Comparison

| Structure | Vagaro | Zenoti | GlossGenius | Square Appointments | Evidence layer |
|---|---|---|---|---|---|
| Bookable service catalog (services with duration/price; categories; add-ons) | ✔ (services, bundles, add-ons) | ✔ (services, variants, add-ons, categories) | ✔ (services) | ✔ (services) | B |
| Identified client records ("customer"/"guest"/"client") | ✔ customer profiles | ✔ guests (merge, relationships, notes, forms) | ✔ client management | ✔ customer profiles/directory | B |
| Appointment binds client + service + provider + time slot on business calendar | ✔ | ✔ (booking → slot → confirm) | ✔ | ✔ | B |
| Provider/staff as schedulable entity with availability | ✔ employee calendars | ✔ employee schedules + blockouts | ✔ staff calendars | ✔ staff schedules | B |
| Appointment lifecycle: request/accept → confirm → arrival → in service → complete | ✔ (documented status set) | ✔ (booking → reserve → confirm; appointment book states) | ✔ (calendar; check-in implied) | ✔ (confirmed instantly; reminders/waitlist) | B (states fully documented only in Vagaro) |
| No-show / cancellation handling with fees & card on file | ✔ (no-show & cancel + fee; no-show count on profile) | ◐ (cards on file; policies org-configurable — not directly observed in API docs) | ✔ (No-Show Protection) | ✔ (no-show protection, cancellation fees, prepayments) | B |
| Checkout resolving appointment into payment (service ticket → payment) | ✔ (Check Out a Customer's Appointment) | ✔ (invoice generated at confirm → collect payment) | ✔ (payments & POS) | ✔ (payments connected to booking) | B |
| Checkout of walk-ins / retail products alongside services | ✔ (walk-ins; products+services same checkout) | ✔ (product sale flow; retail) | ✔ (POS + inventory) | ✔ (products & services in same transaction) | B |
| Redemption of prepaid value at checkout (packages/memberships/gift cards) | ✔ (redeem package/membership visits, gift cards) | ✔ (series packages, gift card balance, loyalty, prepaid) | ✔ (memberships & packages, gift cards) | ✔ (prepaid packages, gift cards) | B |
| Resources (rooms/chairs/stations/equipment) as bookable constraints | ✔ (resource calendars) | ✔ (rooms + room blockouts) | ✔ (resource management) | ✔ (rooms/stations/chairs) | B |
| Online client self-booking surface | ✔ (consumer app + web) | ✔ (Webstore, mobile app) | ✔ (booking site; no client app needed) | ✔ (booking site, QR, social) | B |
| Automated confirmations / reminders | ✔ | ✔ (notification flows) | ✔ (client notifications) | ✔ (email/SMS; AI assistant) | B |
| Client visit history / notes on profile | ✔ (appointment history, notes, tags) | ✔ (appointment history, notes) | ✔ (client insights, photo markup) | ✔ (transaction history, preferences, notes) | B |
| Client forms / intake (incl. clinical overlay) | ◐ (HIPAA-compliant notifications; Forms & SOAP Notes category) | ✔ (guest forms v2) | ✔ (forms & waivers; EMR/charting) | ✔ (forms & contracts at booking) | B |
| Packages / prepaid series | ✔ | ✔ (series & day packages) | ✔ | ✔ | B |
| Memberships (recurring) | ✔ | ✔ (freeze/unfreeze, renewal) | ✔ | ◐ (loyalty is separate product) | B |
| Gift cards | ✔ | ✔ | ✔ | ✔ | B |
| Staff commissions / payroll | ✔ (payroll category) | ✔ (payroll info API) | ✔ (payroll reporting: commissions, tips, hourly) | ◐ (Shifts/Payroll as sibling products) | B |
| Reviews / reputation | ✔ (review management) | ◐ (not observed in API docs) | ✔ (client reviews) | ◐ (via marketplace/Google integration pages) | B |
| Waitlist | ✔ (implied by scheduling docs) | — (not observed) | ✔ | ✔ | B |
| Consumer marketplace / discovery | ✔ (consumer app) | — (own-brand webstore) | — (explicitly no marketplace posture) | ✔ (Square Go) | B — optional |
| Class / group sessions | ✔ (classes & workshops; attendee mgmt) | ✔ (classes API) | ◐ (fitness vertical pages) | ✔ (class bookings) | B — optional |
| Mobile (at-client-location) services | ✔ (mobile service notifications) | — (not observed) | — | — | product-specific (Vagaro) |
| Upsell pipeline (opportunities) inside the platform | — | ✔ (opportunities, sales stage rules) | ◐ (growth agent positioning) | — | product-specific (Zenoti) |
| Multi-center / multi-location | ✔ | ✔ (centers; org-level settings) | ✔ (multi-location pages) | ✔ (multi-location scheduling) | B |
| AI assistant / automated reception | ◐ (Vagaro university/videos) | ◐ (Zenoti AI on marketing pages, not in API docs) | ✔ (Agents/Reception 24/7) | ✔ (Square Assistant) | B — emerging, varies |

Legend: ✔ directly observed for that product; ◐ observed indirectly or partially; — not observed in fetched sources.

## Canonical Model

### Level 0 — Defining Invariant

The smallest structure without which the product stops being an appointment-based service business management application:

1. **Business-defined bookable service catalog** — services the business offers, each with its own duration and price, organized in a menu (with categories and add-ons as the standard elaboration).
2. **Identified client records** — the business's clientele as persistent, individually identified records (not anonymous transactions).
3. **The appointment as the central binding object** — an appointment binds a client, a service from the catalog, and the staff member who will perform it, into a time slot on the business's calendar. Provider availability is what makes a slot bookable.
4. **Appointment lifecycle to service delivery** — the appointment moves from booking (optionally requested/confirmed) through arrival and service performance to completion, with cancellation and no-show as named alternative outcomes.
5. **Checkout that resolves the appointment into recorded money** — the completed appointment becomes a chargeable visit recorded against the client (service ticket → payment; walk-in and retail items share the same checkout surface).

Justification tests:

- Remove the service catalog + appointment binding → the product is generic POS.
- Remove checkout + client ledger → the product is an appointment scheduling application (Directory 03.09), not business management.
- Remove the client record / service-delivery context → retail checkout.
- Historical check: 2000s-era salon management systems (appointment book + client cards + checkout + commissions) satisfy all five; marketplace-era and solo-mobile-era products satisfy all five; a pure booking widget (calendar + reminders, no client ledger, no checkout) does not. So the definition does not overfit the current marketplace generation.

### Level 1 — Common Mature Structure

Present across the researched sample (evidence layer B), expected of mature products but not defining:

- Online client self-booking site/page (and often a client-facing app), with booking rules (approval requirement, who can book, auto-assignment of staff).
- Automated confirmations and reminders (email/SMS), appointment notifications to staff.
- Cancellation / no-show policies: fees, deposits, cards on file, no-show tracking per client.
- Staff management: schedules/working hours, time off/blockouts, per-staff service assignment; often commissions and payroll reporting; role-based permissions.
- Client relationship data: visit/appointment history, notes, preferences, tags; family/group linking; merge/duplicate handling.
- Resources (rooms, chairs, stations, equipment) as additional bookable constraints.
- Add-ons and service bundles within the catalog.
- Prepaid value: packages/series, memberships, gift cards — sold, tracked per client, redeemed at checkout.
- Retail product sales with inventory, in the same checkout as services; walk-in support.
- Discounts, taxes, tips, receipts, split payment, refunds.
- Reporting dashboards (revenue, utilization, rebooking, client retention; cancellation/no-show reports).
- Reviews/reputation and re-engagement marketing as adjacent growth loops.

### Level 2 — Variant / Optional Structure

Depends on segment, geography, business model:

- **Consumer marketplace posture** — business listed in the vendor's consumer discovery app (marketplace-first vendors built whole models on this; other products intentionally have no marketplace, e.g. GlossGenius "no client logins or app downloads").
- **Industry overlays** — salon formulas/photos, medspa charting/EMR & consent forms, clinical/regulatory modes (HIPAA-compliant messaging), spa room/equipment emphasis.
- **Class/group sessions** — workshops, classes, attendee rosters alongside 1:1 appointments (fitness-adjacent businesses).
- **Mobile (at-client-location) services** — the same appointment structure performed off-site (observed in Vagaro).
- **Multi-location / enterprise scale** — centers, cross-center guest search, org-level settings, corporate reporting.
- **Payments posture** — native integrated processing vs bring-your-own processor; hardware readers; tap-to-pay.
- **Pricing model of the software itself** — subscription tiers vs subscription-free-with-processing-fees vs marketplace commission.
- **AI automation** — AI reception/assistants, automated rebooking, marketing agents.
- **Client identity surface** — client app + login vs link-based booking without accounts.

### Level 3 — Vendor-specific (research notes only)

- Vagaro: appointment status color scheme (purple requested / light blue accepted / yellow awaiting confirmation / pink confirmed / light green show / blue ready-to-start / green in progress / grey complete / red no-show); Live Stream services; Check-in App; Vagaro Drive; Connect by Vagaro; IOUs at checkout; PayPro front-desk hardware; E-Prescribe category (vertical extension).
- Zenoti: "guest/center/therapist" vocabulary; host-guest group booking with family relationships; therapist-gender preference in booking; price scaling per therapist; opportunities with sales-stage rules; Aveda birthday-gift integration; org setting "Search Guest Across Centers"; dummy-guest "checkout as guest" for webstores.
- GlossGenius: flat processing rate advertising (2.6%), Genius Agents (Growth/Marketing/Reception), GeniusShop, White Glove migration service, EMR/charting module.
- Square: ecosystem bundling (Banking, Loans, Afterpay/BNPL, Loyalty, Marketing as separate Square products), Square Assistant, Square Go marketplace, tier-gated features (waitlist, resource management, cancellation policy at higher tiers).

## Boundary Findings

1. **vs Appointment Scheduling Application (03.09)** — shares the entire booking machinery (catalog of bookable slots, availability, confirmations). The structural test is the business-operations layer: this Type carries identified client ledger + service-delivery lifecycle + checkout/payment + staff economics. Remove checkout and the client ledger → appointment scheduling application. Removal test documented against all four sampled products (none lacks either side).
2. **vs Retail POS (05.10)** — shares the checkout spine (items → payment). Here the sale is generated by a scheduled appointment for a service delivered by staff at an appointed time, and the catalog carries durations/providers. Remove the appointment/calendar → generic POS.
3. **vs Small Business Field Service Management (§29 sibling)** — both schedule work for customers, but the default delivery locus differs: this Type is client-comes-to-the-business (chair, room, station at a fixed location) with client checkout on completion; field service is provider-travels-to-customer with dispatch, travel, job sites, quotes/estimates. Vagaro's "mobile service" mode is an off-site variant inside this Type, not a full dispatch structure. Boundary is a gradient; products with heavy quoting/dispatch/routing belong to field service.
4. **vs Local Service Marketplace (§29) / Service Marketplace (05.02)** — marketplace is consumer-side discovery/booking across businesses; this Type is operator-side management of one business. Marketplace posture is an L2 variant here (some products bundle both, e.g. Vagaro consumer app, Square Go; others deliberately do not).
5. **vs Salon/Spa/Barbershop/Massage/Nail leaves (§29 siblings)** — these are industry variants of this same Type: same core model with industry-specific overlays (formulas, rooms, charting). This generic leaf is the shared core; the industry leaves should be treated as Variants unless their research reveals structurally different objects. Flagged for joint review.
6. **vs Patient Scheduling / Practice Management System (§22)** — regulated clinical care: scheduling exists, but the appointment is an encounter inside a clinical record system with provider licensure, insurance and documentation semantics. Some appointment-business vendors add medspa/EMR overlays (GlossGenius EMR, Zenoti forms) without becoming clinical systems.
7. **vs Membership Management (§25) / class-registration Types (§23/§29)** — memberships and classes appear here as client-value structures inside an appointment business; when recurring group sessions (not appointments) become the primary unit, the product drifts toward class/registration-oriented Types. All four sampled products support classes as a secondary structure.

## Uncertainties

- No marketplace-first vendor (Fresha, Booksy) documentation could be fetched; marketplace-posture observations rest on Vagaro/Square consumer surfaces and on GlossGenius's explicit no-marketplace positioning. Claim strength for marketplace variants is correspondingly reduced.
- GlossGenius and Square Appointments evidence is Tier-2 (vendor product pages), not help-center articles; operational details (exact states, refund rules, deposit mechanics) are asserted only at structure level for those two products.
- Whether "cancellation/no-show fee" is universal or plan-gated: observed as a first-class capability in Vagaro and Square (Square gates it to paid tiers per pricing page); Zenoti supports cards on file but fee policy details were not directly observed. Final document states the policy layer as common, not universal.
- Class support breadth: documented in Vagaro, Zenoti (API), Square; GlossGenius only via fitness vertical pages — treated as optional/variant.
- Appointment states: only Vagaro documents a full status set; the canonical lifecycle is written conceptually, exact state names vary by product.

## Final Synthesis

The Type is best understood as **a business operating system organized around the appointment**. Its world contains: a catalog of bookable services (durations, prices, add-ons), a bookable staff roster with availability, optionally bookable resources, an identified client population, and the appointment as the central object binding client × service × provider × time. The appointment carries a lifecycle from booking through confirmation and arrival to completion (or cancellation/no-show), and terminates in checkout — a payment-bearing visit recorded against the client, into which retail and prepaid-value redemption fold. Around this core, mature products add the self-booking surface, automated reminders, no-show protection, client history/notes, packages/memberships/gift cards, staff commissions/payroll, and reporting. Marketplace exposure, industry overlays (salon/medspa/clinical), classes, multi-location scale, and AI automation are variants, not defining structure. The two sharpest boundaries: toward scheduling-only tools (remove the client ledger and checkout) and toward POS (remove the appointment).
