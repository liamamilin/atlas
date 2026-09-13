# Research Notes — Salon Management System

Research date: 2026-09-10

## Research Goal

Understand the software category used by hair and beauty salons — businesses whose revenue is built on client appointments for services performed by stylists and other salon professionals — and derive its canonical structure: what objects exist, how the salon visit is booked and delivered (including the color-service time model), how it resolves into money, and where the salon variant sits against the generic appointment-based service business core and the other §29 beauty-industry siblings (barbershop, spa, med spa, massage, nail, tattoo, beauty-professional app, marketplace).

## Initial Boundary

Initial hypothesis (before research):

- The leaf sits in Directory §29 between "Pet Insurance Customer App" and "Barbershop Management", surrounded by industry-specific siblings. Five of those siblings (barbershop-management, massage-practice-management, med-spa-management, nail-salon-management, tattoo-studio-management) have already been processed and each was ratified as an **industry Variant of the generic appointment-business core** (bookable service catalog + identified clients + appointment binding client×service×provider×time + lifecycle + checkout), with the industry difference concentrated in an overlay rather than in object types.
- Three inherited flags must be discharged:
  1. The appointment pass's sibling flag (salon-management-system listed as probable industry Variant).
  2. The med-spa pass's recorded removal test for this leaf: "remove the regulated-treatment layer → that industry's business on the same visit economy."
  3. The beauty-professional-business-app pass's joint-review request: "joint review suggested with Salon Management System when processed" (establishment-first vs professional-first packaging).
- Expected salon overlay candidates (to verify, not assume): hair-service vocabulary (color/highlight/perm/keratin), **color formulas/recipes on client records**, **processing time inside the service time model** (color services where the client waits and the stylist is free), multi-service visits (cut + color in one sitting), stations/rooms as resources, stylist-level pricing and commissions, booth-rent economics, professional product retail with backbar usage.
- Working assumption to test: the salon variant adds no new object types — only vocabulary, time-model elaboration, and emphasis on the same core.

## Research Questions

1. Does the market realize salon software as a separate product family, or as a configuration of multi-vertical beauty platforms? Where is the salon-native pole?
2. What hair-specific service vocabulary and catalog structure do the products carry?
3. How is the color-service time model handled — is "processing time" a first-class concept, and is it bookable by other clients?
4. What does the client record carry that is salon-specific (color formulas/recipes, before/after photos, preferences)?
5. How are multi-service visits (cut + color) and service bundles modeled?
6. How do stylist-level pricing (junior/senior/master), commissions, tips, and payroll work?
7. How do booth-rental and hybrid business models interact with the commission-model machinery?
8. How do walk-in visits interact with the appointment structure?
9. Do any salon-specific structures change the core model, or only decorate it?
10. Historical / regional check: would older, paper-era, or regional salons fit the definition?

## Representative Products

| Product | Segment / philosophy | Customer tier | Why selected |
|---|---|---|---|
| Vagaro | Multi-vertical salon/spa/fitness suite with consumer marketplace | Solo → chains | Tier-1 help center; Hair Salon is a first-class business type with a documented keyword list; gap-processing time documented Tier-1 |
| Boulevard | Salon-native client-experience platform (salon is the lead vertical) | Premium salons/spas, multi-location, franchises | Tier-1 support center; four-block service timing model documented Tier-1; color-formula client notes Tier-1; salon-industry integrations (Vish, Green Circle, OPERA) |
| Zenoti | Enterprise salon/spa/medspa/fitness platform | Single-location → large chains/franchise | Salon management page (Tier-2) with salon-specific economics (commissions, turnover/book preservation, backbar inventory deduction); Tier-1 API docs from the family pass |
| Mangomint | Design-forward salon/spa suite, hair salons the lead vertical | SMB salons, solo → multi-location | Hair-salon page (Tier-2) with booth-rental/hybrid/commission model support, tiered stylist pricing, walk-in machinery |
| GlossGenius | Solo-first, mobile-first, payments-native; no marketplace | Solo stylists, booth renters, small salons | Salon page (Tier-2) with color recipes/before-after photos on client profiles, booth-renter payouts, commissions/tips/hourly payroll |

Notes on sampling: the salon-native pole is covered by Boulevard (salon is its lead industry) and by the hair-salon-first packaging of Mangomint/GlossGenius; the multi-vertical pole by Vagaro/Zenoti. Fresha and Booksy remained unreachable (carried limitation from the 2026-09-06 family pass). Desktop-era salon software (Millennium/Salon Iris class) was not fetched; the historical check is reasoned, not asserted from fetched evidence.

## Sources

Tier 1 (official operational documentation):

- Vagaro Support (Zendesk help center), fetched 2026-09-10:
  - "Set Your Business Type": https://support.vagaro.com/hc/en-us/articles/360048745274-Set-Your-Business-Type — Hair Salon keyword list (salon, highlight, blowdry, blow dry, straightening, thermal press, foil, perm, bang trim, haircut, balyage, fantasy color, blowout, keratin, relaxer, color correction, permanent hair color, permanent color, hair cut, style); hair-adjacent business types Extensions (tape ins, weave, sew in, hand tied), Braids (cornrow, box braids), Locs, Textured Hair (silk press, flexi rod), Hair Replacement (wig, transplant); business type auto-derived from service-name keywords and drives marketplace categorization
  - "Manage Customer Notes": https://support.vagaro.com/hc/en-us/articles/360007906613-Manage-Customer-Notes — four note types: General, Allergy, and **Formula Notes** (informational, "an employee should be aware of when booking an appointment for a customer"); Popup notes (appear when booking and at Checkout, up to two); notes visible as icons on calendar appointments; internal-only (support comment confirms only business owner/employees see them); exportable to Excel; filterable by note type and business location
  - "Manage Gap Processing Time During a Service": https://support.vagaro.com/hc/en-us/articles/360010299394-Manage-Gap-Processing-Time-During-a-Service — "Adding gap processing time, or gap time, allows service providers to take additional appointments during a client's downtime, maximizing their daily bookings"; example: "in a hair color service, the 45 minutes a client spends under a dryer is considered gap time, during which the provider can take another appointment"; duration model = Initial Duration + Gap (processing) + Finish Duration; set per service per provider in the Service/Class Menu; editable per appointment on the Calendar; operator calendar shows available slots inside the appointment; "customer-facing calendars, including the Vagaro app and third-party apps, do not display details about gap time"; booking during gap time works like normal booking with a popup alert if the new service is longer than the gap; Booking Percentage report measures gap-time effectiveness; "available for all Vagaro businesses"
  - Booking articles (search results): appointment time "including gap processing time, cleanup time, and any add-ons" (Rebook an Appointment; Book a Single Appointment for a Customer; Schedule Repeating Appointments; Schedule Multiple Appointments at Once; Book a Service Bundle)
  - "Copy Service Prices to Another Employee" (search result): per-employee service prices/durations with "Gap (Processing) Initial Duration"
  - "Vagaro Features Included in Your Base Subscription" (search result): "Collection: Set up and manage renters and contractors" (booth-rent collection)
- Boulevard Support Center (Intercom), fetched 2026-09-10:
  - "Client Notes": https://support.boulevard.io/en/articles/5941455-client-notes — "Client Notes are commonly used for: **Color formulas**, Client preferences, Medications, Allergies, Photos, Documents and files, Progress notes"; date-stamped, file/photo attachments (photos visible in client's photo gallery); internal-only; permission-gated ("View Client Notes", "Create and Modify Client Notes"); "Non-clinical businesses have an Allergies section"
  - "Service Timing Options": https://support.boulevard.io/en/articles/5941395-service-timing-options — four independent time blocks: **Duration** (client with professional; professional cannot be booked), **Processing Time** ("client is unavailable but the professional is available. This option is mostly used with hair color processing when the client is waiting for the color to process and the colorist is available to work on other clients. **Processing Time is bookable time.**" — online self-booking during processing allowed unless Double Booking is disabled, and only if the desired service fits within the allotted processing time), **Finishing Time** (client back with the same professional — "mostly used with blow-drys or treatments immediately after the client has been processed"; not bookable), **Transition Time** (after the service — "break time, cleanup time, documentation time, or any reason why the professional would want some time or a 'cushion'"; not bookable); "To maximize profits, Boulevard by default allows staff members to be booked during processing time"; Double Booking toggle per service
  - "Advanced Service Customization" (search result): services customizable by role type or person — custom Pricing, Duration, Processing Time, Finishing Time, Transition Time, Book-ability online
  - "Service Records Report" (search result): report fields include service name, category, active status, pricing, duration, processing time, transition time, finishing time
  - "Granular permission groups" (search result): permissions over "duration, processing time, finishing time, transition time, commission, deposit settings"; time cards for payroll validation
  - "Boulevard Integrations": https://support.boulevard.io/en/articles/7880786-boulevard-integrations — **Vish**: "track color notes and formulas and also pushing appointments back to the color bar"; intelligent weighing scale "capture[s] the details of every color mixed as ingredients are weighed, then reweighing the bowl after service formulas are adjusted to eliminate any waste"; "Ticket information such as product changes, add-ons, and additional color charges are sent directly to the front desk ensuring every color bill is correct"; "**Formula details sent to client profile**"; "Consistent color mixed every time"; dashboard shows "every team member's color usage, cost, and waste by service"; **Green Circle Salons**: salon-industry environmental program — "Create custom environmental service fees for individual services… automatically applied to each order… full transparency into fees directly within receipts"; **OPERA PMS**: hotel-guest room charges from an on-site salon/spa
  - Industries nav: For Salons (lead), For Barbers, For Spas, For Medspas, For Massages, For Nails
- Family machinery (statuses, checkout, packages/memberships, resources, marketplace) reuses Tier-1 Vagaro help-center and Zenoti API-doc evidence recorded in the same research program on 2026-09-06 (research/appointment-based-service-business-management.md)

Tier 2 (official product pages):

- Zenoti salon management page, fetched 2026-09-10: https://www.zenoti.com/salon-management-software — "built for every kind of salon — hair, nail, beauty, and tanning salons — from single-location small businesses to multi-location groups"; turnover narrative: "When a provider leaves, guests often follow. Without systems to re-book guests or preserve histories, revenue walks out the door. And when staff lack tools to build a book or track earnings, they're more likely to leave too"; "salon staff commissions and payouts"; "Show staff what they earn in real time and give instant tip access via the myZen card"; "Flexible commission structures"; guest profile: "services completed, products used, stylist who performed the work, and spend for that visit" / "service history, product preferences, stylist notes, skin or hair type records, and visit frequency"; "product usage deducts from salon inventory management in real time — no manual entry"; inventory: "real-time stock levels, automatic deduction when products are used in services, low-stock alerts, and auto-reorder"; appointment book: cloud, real-time, "double-bookings are prevented automatically"; "the salon POS system checkout ticket pre-fills from the appointment record automatically"; walk-ins: "manage walk-ins, appointments, and last-minute changes"; tanning: "bed and room scheduling"; platform pages: Integrated Payroll & Tipping, Photo Manager, Employee Performance Management, Dynamic Pricing, Premium Provider Pricing, Forms & Charting. (Vendor marketing figures — benchmark percentages, pricing tiers — recorded here only, not used in the final document.)
- Mangomint hair-salon page, fetched 2026-09-10: https://www.mangomint.com/solutions/hair-salon-software/ — Hair Salons lead business type (solutions span 12 verticals); login-free online booking embedded on the salon's website ("no third-party marketplaces here!"); Express Booking™ (booking completed via a text link); Virtual Waiting Room for walk-ins ("texting a link to collect a card-on-file to notifying clients when their stylist is ready"); booth rental: "works seamlessly in booth rental, hybrid, and commission-based hair salons… direct booking links, automatic payment routing, customizable client management settings"; commission salons: "custom staff commissions (both service- and product-based) and salaries/wages for each staff member… built-in Payroll feature"; tiered pricing: "service customizations allow you to set tiered pricing based on stylist experience, seniority, or specialized skills… junior, senior, or master stylist pricing"; add-ons with variable pricing; multi-location; migration transfers "clients, products, and gift cards, and in many cases… notes, services, transaction and appointment history". (Pricing figures recorded here only.)
- GlossGenius salon page, fetched 2026-09-10: https://glossgenius.com/customers/salon-software — "all-in-one software designed to help salon owners and booth renters"; industries: Hair Salon (lead), Nail, Lash, Brow, Makeup, Tanning, Tattoo, Barber; by size: Multi-Location, Single Location, Solopreneur, Booth Rentals; "Organize key client details — like **before & after images, color recipes, and birthdays** — with Client Profiles"; booth renters: "Pay booth renters directly with simple payouts to separate accounts"; "free same-business-day transfers and instant payouts"; payroll: "Automate payroll and seamlessly handle commissions, tips, and hourly pay"; inventory: "automated quantity updates, barcode scanning, and restocking through GeniusShop"; booking website with portfolio gallery and service images; "deposit, cancellation, and card-on-file policies built into booking"; "Rebooking Reminders built into checkout"; Resource Management feature; EMR/charting as a separate medspa overlay. (Processing-rate marketing figures recorded here only.)

Access limitations:

- Zenoti help center (help.zenoti.com): HTTP 403 on search (1 attempt, abandoned per network rules). Zenoti evidence rests on its official product pages (Tier-2) plus Tier-1 API-doc evidence reused from the family pass.
- Mangomint help center: not reachable in prior passes (404 on tried paths, carried limitation); Mangomint evidence rests on its official product pages.
- GlossGenius Learning Center: JS shell (carried from the 2026-09-06 pass); GlossGenius evidence rests on its own product pages.
- Fresha/Booksy: unreachable (carried from the 2026-09-06 pass).
- Vagaro marketing site: 403 (carried); Vagaro evidence rests on its Tier-1 help center.
- Search engines: not needed this pass; product discovery inherited from the family program.

## Product Observations

### Vagaro (evidence layer: A — Tier-1 help center)

- **Hair Salon is a first-class business type**, auto-derived from service-name keywords against a documented list (highlight, blowdry, foil, perm, bang trim, haircut, balyage, fantasy color, blowout, keratin, relaxer, color correction, permanent hair color…). The hair vertical is further subdivided into adjacent business types: Extensions, Braids, Locs, Textured Hair, Hair Replacement. Business type drives marketplace categorization.
- **Formula Notes are a first-class note category** on the customer profile (General / Allergy / Formula), described as informational notes "an employee should be aware of when booking an appointment for a customer". Popup notes (max two) surface at booking and checkout. Notes are internal-only, visible as icons on calendar appointments, exportable, filterable by type and location.
- **Gap processing time is a first-class service-time concept**: Initial Duration + Gap (processing) + Finish Duration. The gap is "reserved for taking additional appointments"; the canonical example is a hair color service (client under a dryer while the stylist takes another client). Gap time is configured per service per provider, editable per appointment, visible as bookable slots inside the appointment on the operator calendar, and hidden from customer-facing calendars. A Booking Percentage report measures how effectively gap time is used. Appointment time = service time + gap processing time + cleanup time + add-ons.
- Per-employee service prices and durations (with per-employee gap-processing configuration) are copyable between employees.
- Booth-rent collection: base subscription includes "set up and manage renters and contractors".
- SOAP Notes/Forms exist as a separate clinical-grade documentation layer (the medspa/massage overlay machinery, present in the same platform).
- Family machinery (statuses/colors, checkout, packages/memberships, resources, marketplace) documented Tier-1 in the 2026-09-06 pass.

### Boulevard (evidence layer: A — Tier-1 support center)

- **Client Notes name color formulas first** in the documented use list ("Color formulas, Client preferences, Medications, Allergies, Photos, Documents and files, Progress notes"). Notes are date-stamped, carry file/photo attachments (photos land in the client's photo gallery), are internal-only, and are permission-gated (separate "View" and "Create and Modify" permissions). "Non-clinical businesses have an Allergies section" — the clinical/non-clinical split mirrors the med-spa pass's two-document-class finding.
- **The service time model has four named blocks**: Duration (client present, not bookable), Processing Time (client waiting, **professional bookable** — "mostly used with hair color processing… the colorist is available to work on other clients"), Finishing Time (client back with the same professional — blow-dry/treatment after processing), Transition Time (professional's cushion after the service — break/cleanup/documentation). Processing Time is bookable by online self-booking unless the per-service Double Booking toggle is disabled, and only if the desired service fits within the allotted processing time. Default posture: bookable during processing ("to maximize profits").
- Services are customizable by role type or person: pricing, duration, processing/finishing/transition time, online book-ability. Service records report on all four time blocks. Granular permission groups gate who may view/change timing, commission, and deposit settings.
- **Color-service economics arrive through the Vish integration**: color notes and formulas tracked, appointments pushed "back to the color bar", an intelligent weighing scale captures every color mixed and reweighs the bowl to eliminate waste, color charges flow to the front-desk ticket ("every color bill is correct"), formula details land on the client profile, and a dashboard shows per-team-member color usage/cost/waste with inventory replenishment.
- **Salon-industry environmental fees** via Green Circle Salons: custom environmental service fees per service, auto-applied, visible on receipts.
- **Hotel-salon room charges** via OPERA PMS: on-site salon/spa services charged to the hotel guest's room.
- Industries nav: For Salons is the lead vertical (before Barbers/Spas/Medspas/Massages/Nails).

### Zenoti (evidence layer: A for API object model [family pass], B for page posture — mixed Tiers)

- Salon management page positions the platform "built for every kind of salon — hair, nail, beauty, and tanning salons", single-location to multi-location groups.
- **The stylist-book/turnover narrative is the salon-specific framing**: "When a provider leaves, guests often follow. Without systems to re-book guests or preserve histories, revenue walks out the door. And when staff lack tools to build a book or track earnings, they're more likely to leave too."
- **Salon economics**: "salon staff commissions and payouts"; "Show staff what they earn in real time and give instant tip access via the myZen card"; "Flexible commission structures"; real-time tip and commission tracking; Integrated Payroll & Tipping platform page.
- **Guest profile as the salon's memory**: every visit updates the profile with "services completed, products used, stylist who performed the work, and spend for that visit"; the CRM FAQ lists "service history, product preferences, stylist notes, skin or hair type records, and visit frequency".
- **Backbar usage deduction**: "product usage deducts from salon inventory management in real time — no manual entry"; inventory FAQ: "automatic deduction when products are used in services, low-stock alerts, and auto-reorder".
- Appointment book: cloud, real-time, double-bookings prevented automatically; checkout ticket pre-fills from the appointment record; walk-ins managed beside appointments; tanning salons get "bed and room scheduling".
- Homepage word cloud includes "Formulas" among platform data types (marketing-level corroboration of formula-keeping).
- Tier-1 API object model (guest/center/appointment/invoice) reused from the family pass.

### Mangomint (evidence layer: B — Tier-2 product page)

- Hair Salons are the lead business type; the platform spans 12 beauty/wellness verticals.
- **Business-model breadth is explicit**: booth rental, hybrid, and commission-based salons all supported — booth rental via "direct booking links, automatic payment routing, customizable client management settings"; commission salons via "custom staff commissions (both service- and product-based) and salaries/wages… built-in Payroll".
- **Tiered stylist pricing**: "service customizations allow you to set tiered pricing based on stylist experience, seniority, or specialized skills… junior, senior, or master stylist pricing"; add-ons carry variable pricing.
- **Walk-in machinery**: Virtual Waiting Room + Express Booking™ (text-link booking, card-on-file collection, "notifying clients when their stylist is ready").
- Login-free online booking embedded on the salon's own website; explicit anti-marketplace posture ("no third-party marketplaces here!").
- Multi-location; migration carries clients, products, gift cards, notes, services, transaction and appointment history.

### GlossGenius (evidence layer: B — Tier-2 product page)

- "Salon software… designed to help salon owners and booth renters"; Hair Salon leads the industries list; size segments include Solopreneur and Booth Rentals.
- **Client profiles carry salon-specific content**: "before & after images, color recipes, and birthdays".
- **Booth-renter economics**: "Pay booth renters directly with simple payouts to separate accounts"; same-business-day transfers and instant payouts.
- **Payroll**: "commissions, tips, and hourly pay" automated.
- Inventory/retail: automated quantity updates, barcode scanning, restocking (GeniusShop).
- Booking website with portfolio gallery and service images; deposit/cancellation/card-on-file built into booking; rebooking reminders built into checkout; Resource Management feature; EMR/charting exists as a separate medspa overlay (not salon core).

## Cross-product Comparison

| Structure / capability | Vagaro | Boulevard | Zenoti | Mangomint | GlossGenius | Evidence layer |
|---|---|---|---|---|---|---|
| Bookable service catalog (duration + price, categories/add-ons/bundles) | ✔ (Tier-1) | ✔ (Tier-1) | ✔ (Tier-1 API) | ✔ (Tier-2) | ✔ (Tier-2) | B |
| Identified client records with history/notes/preferences | ✔ (Tier-1) | ✔ (Tier-1) | ✔ (Tier-1 API + Tier-2) | ✔ (Tier-2) | ✔ (Tier-2) | B |
| Appointment binding client × service × stylist × time | ✔ (Tier-1) | ✔ (Tier-1) | ✔ (Tier-1 API + Tier-2) | ✔ (Tier-2) | ✔ (Tier-2) | B |
| Visit lifecycle with cancel/no-show as named outcomes | ✔ (Tier-1, family) | ✔ (Tier-1, family) | ✔ (Tier-1 API) | ✔ (Tier-2) | ✔ (Tier-2) | B |
| Checkout resolving the visit into recorded money (tips, retail, prepaid) | ✔ (Tier-1, family) | ✔ (Tier-1, family) | ✔ (Tier-1 API + Tier-2) | ✔ (Tier-2) | ✔ (Tier-2) | B |
| Hair-service vocabulary as catalog content | ✔ (keyword list, Tier-1) | ✔ (salon lead vertical) | ✔ (hair/nail/beauty/tanning) | ✔ (hair lead vertical) | ✔ (hair lead industry) | B |
| **Processing-time model (bookable gap inside the service)** | ✔ (Initial/Gap/Finish, Tier-1) | ✔ (Duration/Processing/Finishing/Transition, Tier-1) | not observed this pass | not observed this pass | not observed this pass | B (2 products, both Tier-1) |
| **Color formulas/recipes on the client record** | ✔ (Formula Notes category, Tier-1) | ✔ (Client Notes use list + Vish push, Tier-1) | ✔ ("Formulas" in platform data, Tier-2 marketing) | not observed | ✔ ("color recipes", Tier-2) | B (3 products) |
| Multi-service visits / bundles (cut + color in one sitting) | ✔ (Tier-1) | ✔ (Tier-1, family) | ✔ (Tier-2) | ✔ (Tier-2) | ✔ (Tier-2) | B |
| Stylist-level pricing (junior/senior/master tiers) | ✔ (per-employee prices, Tier-1) | ✔ (customization by role/person, Tier-1) | ✔ (Premium Provider Pricing, Tier-2) | ✔ (tiered pricing, Tier-2) | not observed explicitly | B |
| Commissions / tips / payroll | ✔ (payroll; family Tier-1) | ✔ (commission permissions, Tier-1) | ✔ (Tier-2) | ✔ (Tier-2) | ✔ (Tier-2) | B |
| Booth-rent / renter economics | ✔ (renters & contractors collection, Tier-1) | not observed this pass | not observed this pass | ✔ (booth rental mode, Tier-2) | ✔ (booth-renter payouts, Tier-2) | B |
| Retail + inventory with service-usage deduction | ✔ (family Tier-1) | ✔ (Vish replenishment, Tier-1) | ✔ (Tier-2) | ✔ (Tier-2) | ✔ (Tier-2) | B |
| Walk-in handling beside appointments | ✔ (family Tier-1) | ✔ (Tier-1, family) | ✔ (Tier-2) | ✔ (Virtual Waiting Room, Tier-2) | ✔ (Tier-2) | B |
| Marketplace posture | bundled marketplace | own-site overlay + Reserve with Google | social booking (Google/IG/FB) | anti-marketplace (explicit) | anti-marketplace (explicit) | L2 variant spectrum |
| Hotel room charges (hotel-salon variant) | — | ✔ (OPERA, Tier-1) | — | — | — | vendor/integration-specific |
| Environmental service fees (salon-industry program) | — | ✔ (Green Circle, Tier-1) | — | — | — | vendor/integration-specific |
| Color-bar weighing/waste machinery | — | ✔ (Vish, Tier-1) | — | — | — | vendor/integration-specific |

Reading: the visit economy is unanimous at every pole. The salon differences concentrate in three places — (1) hair-service vocabulary filling the same catalog object, (2) the **subdivided service time model** (processing time as bookable provider capacity inside an appointment), and (3) **formula/formula-adjacent content on the client record** — plus a strong emphasis layer on stylist-level economics (tiered pricing, commissions, booth rent) and professional-product retail. None of these adds a new object type to the core.

## Canonical Model

### L0 — Defining Invariant (identical to the family core)

The salon's visit-economy operating system, whose defining core is exactly five jointly-held structures:

1. **Bookable hair-service catalog** — services with durations and prices, organized in categories, with add-ons and bundles; hair-service vocabulary (cuts, color, highlights, perms, keratin, treatments) fills the catalog without changing its structure. Remove → a POS with a client CRM.
2. **Identified client records** — persistent per-person records the salon remembers across visits. Remove → anonymous retail.
3. **The appointment as the central binding object** — client × service × stylist × time on the salon calendar; stylist availability makes slots bookable; stations/rooms as common resource constraints. Remove → an appointment-scheduling application.
4. **The visit lifecycle to service delivery** — booked → confirmed → arrived → in service → complete, with cancellation/no-show as named outcomes backed by policy machinery. Remove → a calendar with no delivery semantics.
5. **Checkout resolving the visit into recorded money** — tips, retail, package/gift-card redemption, per-stylist attribution of earnings. Remove → a scheduler.

Binding: the salon's own hair/beauty service business (remove the binding → the generic appointment-business core; the industry siblings are the other bindings).

Jointly-held load-bearing (family tests): 1 alone = menu/price list; 2 alone = CRM; 3 without 1+2 = anonymous booking calendar; 4 without 1–3 = status board; 5 without 1–4 = a payment terminal; 1+2 without 3 = a client list with a menu; any three without the rest = fragments, not a salon operating system.

### L1 — Common Mature Structure

- Online client self-booking (booking page/link; login-free forms in current products)
- Automated confirmations and reminders; cancellation/no-show policies with fees, deposits, cards on file
- Staff schedules, time off, per-stylist service assignment; stations/rooms as bookable resources
- Client visit history, notes, preferences — **with color formulas/recipes and before/after photos as the salon-characteristic content**
- **The subdivided service time model**: processing time inside a service during which the client waits and the stylist is bookable by other clients (documented Tier-1 in two products; machinery is platform-generic, semantics are salon-shaped)
- Multi-service visits and bundles composed at booking (cut + color in one sitting)
- Add-ons and service customizations; tiered pricing by stylist level (junior/senior/master)
- Packages, memberships, gift cards with redemption at checkout
- Retail product sales with inventory; **backbar/professional-product usage deducted by services**
- Commissions (service- and product-based), tips, payroll; per-stylist earnings attribution
- Walk-in handling beside the appointment book (waiting-room/express machinery)
- Reporting (revenue, utilization, retention, no-shows, gap-time effectiveness)
- Multi-location management

### L2 — Variant / Optional Structure

- Acquisition posture: bundled consumer marketplace (Vagaro) ↔ own-site-only with external channels (Mangomint, GlossGenius explicit anti-marketplace; Boulevard overlay + Reserve with Google)
- Business-model packaging: commission-based ↔ booth-rental ↔ hybrid (rent tracking, renter payouts to separate accounts, direct booking links for renters)
- Hotel-salon room charges (OPERA-class PMS integration)
- Salon-industry environmental service fees (Green Circle-class program)
- Mobile/outcall services; tanning-bed/room scheduling; classes
- Clinical-grade documentation overlays (SOAP notes/forms — the medspa/massage machinery, present in the same platforms but not salon core)
- AI assistance (receptionist, marketing, rebooking); payments-stack packaging; pricing model

### L3 — Vendor-specific (research notes only)

- Vagaro: business-type keyword derivation (including the hair-adjacent types Extensions/Braids/Locs/Textured Hair/Hair Replacement); popup notes (max two); "Gap (Processing)" vocabulary; Booking Percentage report; PayPro hardware; renters-and-contractors collection in base subscription
- Boulevard: four-block timing vocabulary (Duration/Processing/Finishing/Transition); Double Booking toggle; Vish color-bar integration (weighing, waste, per-team-member color cost); Green Circle environmental fees; OPERA room charges; plan names (Essentials/Premier/Prestige/Enterprise); Duo hardware
- Zenoti: myZen card; AI Workforce agent branding; Premium Provider Pricing; benchmark-report marketing figures
- Mangomint: Express Booking™; Virtual Waiting Room; $120/month + $10/user pricing figure
- GlossGenius: flat 2.6% processing-rate marketing; GeniusShop; plan names/prices

## Rejected Findings (considered, not promoted)

- **"Processing time is definitional for the salon Type"** — rejected. Removal test passes: a salon management system without processing-time support is still clearly a salon management system (many salons do little color work; the machinery is absent/unobserved in three of five sampled products). Held at L1 with salon-characteristic emphasis.
- **"Color formulas require a dedicated formula object"** — rejected. Every observed realization is client-record content: a note category (Vagaro), client notes (Boulevard), profile content (GlossGenius). Dedicated formula machinery (weighing, waste, per-mix tracking) arrives through a third-party integration (Vish), not the core.
- **"The marketplace is part of the Type"** — rejected. Two of five sampled products are explicitly anti-marketplace; posture is an L2 acquisition variant (family finding, reconfirmed).
- **"Booth rent is definitional"** — rejected. The commission model is the dominant packaging; booth rent is a business-model variant with product support in three of five products.
- **"Salon = hair only"** — rejected. Products serve "salon" broadly (hair, nail, beauty, tanning); the directory carves the other verticals into sibling leaves. This leaf is the hair-centered salon variant whose products cross-serve the siblings.
- **"Tiered stylist pricing is definitional"** — rejected. Widespread (4/5 products with direct or implied evidence) but an elaboration of per-provider pricing, which the family core already carries.

## Boundary Findings

| Neighbor | Test | Result |
|---|---|---|
| Appointment-based Service Business Management (generic, §29) | Remove the hair-service overlay (color/processing/formulas/stylist economics emphasis) | The generic appointment-business core remains intact. **No machinery separates the two; the separation is industry overlay.** Keep-both per family precedent. This pass DISCHARGES the appointment pass's sibling flag. |
| Med-spa Management (§29 sibling) | The med-spa pass's recorded test: "remove the regulated-treatment layer → that industry's business on the same visit economy" | CONFIRMED from this side: the salon sample carries **no regulated-treatment/clinical-documentation layer at all** (formula notes are trade content, not clinical charts; SOAP notes exist in the platforms as the medspa/massage overlay, not salon core). The salon is the visit economy with hair-service semantics. |
| Barbershop Management (§29 sibling) | Compare overlays | Same core; salon overlay = color formulas, processing time, multi-service color visits, chemical-service retail; barber overlay = individual-barber identity, booth rent foregrounded, tips, client-side checkout. Removal test either way changes overlays only. Platforms cross-serve both. |
| Nail Salon Management (§29 sibling) | Compare overlays | Same core; nail overlay = nail vocabulary, shapes/colors, art-informed booking, two-technician parallel visits; salon overlay = hair vocabulary, formulas, processing time. |
| Spa Management System (§29 sibling, unprocessed) | Predicted seam (per med-spa pass) | Spa pole's center = room-and-therapy itinerary; salon pole's center = the stylist's chair and the color service. Left to that leaf's own pass. |
| Beauty Professional Business App (§29 sibling) | Joint review requested by that pass: compare account unit and emphasis | **DISCHARGED from this side.** Salon management is establishment-first: the salon is the account (team roster, stations, commissions, shop identity, multi-location). The beauty-professional app is professional-first: the individual professional's own book/brand/income is the account. They converge when a solo stylist uses salon software (the pro is modeled as a one-person business — GlossGenius serves both packagings). Same core, opposite packaging emphasis; keep-both. |
| Beauty Service Marketplace (§29 sibling) | Whose surface is primary | Marketplace = consumer discovery across many businesses; salon management = running one business. Some vendors bundle both sides (Vagaro); others refuse (Mangomint, GlossGenius). |
| Appointment Scheduling Application (§03.09) | Remove client ledger + checkout | Only a scheduler remains. Here the booking runs a business and resolves into money. |
| Retail Point of Sale (§05.10) | Remove booking/durations/stylist binding | Only counter retail remains; here the sale originates from a scheduled service (retail shares the checkout, not the center). |
| Pet Grooming Management (§29 sibling) | Subject of the visit | There the served subject is an animal under an owner account with a drop-off→groom→pick-up loop; here a person sits in the chair through the visit. Ratifies that pass's seam from this side. |

**Escalation (Variant Problem, per workflow):** the researched evidence confirms this leaf shares its operational core with Appointment-based Service Business Management and the §29 industry family. Its defensible distinction is the hair-salon industry overlay (vocabulary, processing-time semantics, formula content, stylist-economics emphasis). Documented as an industry Variant with keep-both per the barbershop/massage/med-spa/nail/tattoo precedent; recorded in STATUS.md rather than rewriting the taxonomy.

**Removal tests (for the final doc):** remove the client ledger and checkout → an appointment scheduler remains; remove the booking and calendar → a point of sale remains; remove the hair-service overlay → the generic appointment-business Type remains; remove the regulated-treatment layer from the med-spa sibling → this Type remains.

## Historical / Market-Sample Check (§24-style)

Would older, simpler, or differently positioned products still fit the L0?

- **Paper-era salon** (front-desk appointment book, client formula cards, retail shelf, cash drawer): fits — all five L0 structures present without software; formula-keeping on paper cards predates software, so the formula overlay is era-neutral trade practice, not a software-generation artifact. ✓
- **Desktop-era salon software** (1990s–2000s Windows-class salon systems): fits the same core on desktop; not fetched this pass (reasoned from the family's desktop-era checks, not asserted as fetched evidence). ✓
- **Regional salons outside the US** (different tipping/commission norms, no booth-rent culture): fit — commissions/tips/booth-rent are L1/L2, not L0. ✓
- **Single-service salons** (blow-dry bars, braid shops, extension studios — Vagaro's own business-type list names them): fit — the catalog carries their vocabulary; processing time is optional. ✓
- **Marketplace-era and anti-marketplace products**: both fit — posture is L2. ✓

The L0 therefore avoids freezing the current marketplace-era, AI-assisted, payments-native generation into the definition.

## Uncertainties

1. **Processing-time support in Zenoti/Mangomint/GlossGenius is unobserved** (Zenoti help center 403; the others' evidence is product-page level). The subdivided time model is evidenced in 2/5 products (both Tier-1) and is held at "common in salon-serving products", not universal.
2. **Formula-keeping depth** (per-service formula history, versioning, product-level formula linkage) is unobserved in operational docs; held at "client-record content" strength.
3. **The salon-native standalone pole** (desktop-era Millennium/Salon Iris class; Squire is barber-side) was not sampled; the salon-native reading rests on Boulevard's salon-first positioning plus the hair-first packaging of Mangomint/GlossGenius. Consistent with the nail pass's market-structure finding (multi-vertical platforms realize the vertical), but the standalone-pole gap is recorded, not claimed as absence.
4. **Booth-rent machinery depth** (rent invoicing, vacancy listings) observed at product-page level only (Mangomint, GlossGenius); Vagaro's renters-and-contractors collection is a base-subscription mention.
5. **Fresha/Booksy** remain unreachable (carried) — no marketplace-first vendor evidence this pass.

## Final Synthesis

Salon Management System is the **hair-salon industry Variant of the appointment-based service business core**: an application whose account is the salon and whose defining core is the family visit economy — bookable hair-service catalog (durations and prices), identified client records, the appointment binding client × service × stylist × time, the visit lifecycle through delivery with cancellation/no-show as named outcomes, and checkout resolving the visit into recorded money with tips, retail, and per-stylist attribution. The industry's contribution is overlay, not architecture: hair-service vocabulary filling the catalog (Tier-1 keyword-documented), the **subdivided service time model** in which processing time is bookable provider capacity inside a color service (Tier-1 in two products — the salon's most distinctive machinery), **color formulas/recipes and before/after photos as client-record content** (three products), and a strong emphasis layer on stylist-level economics — tiered pricing by seniority, service- and product-based commissions, tips, payroll, and booth-rent/hybrid business models — plus professional-product retail with backbar usage deducted from inventory. Around that core, products diverge on acquisition posture (bundled marketplace vs explicit anti-marketplace), business-model packaging (commission vs booth-rent vs hybrid), and adjacent overlays (hotel room charges, environmental fees, clinical documentation for medspa-adjacent use). Sharpest boundaries: against the generic appointment-business core (same structure, different industry expression — kept as a separate leaf per family precedent), against the barber/nail/spa siblings (overlay content differs), against the beauty-professional app (establishment-first vs professional-first packaging — joint review discharged from this side), and against the marketplace (whose surface is consumer discovery, not one business's operations).
