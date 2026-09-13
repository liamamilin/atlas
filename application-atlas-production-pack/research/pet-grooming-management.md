# Research Notes — Pet Grooming Management

Research date: 2026-09-09
Slug: pet-grooming-management
Directory leaf: Pet Grooming Management (§29 Home, Family, Personal & Local Services; siblings include Veterinary Practice Management, Pet Boarding Management, Pet Daycare Management, Pet Care Business Management, Pet Training Management, Dog Walking Platform, Pet Sitting Platform, Salon Management System, Appointment-based Service Business Management)

## Research Goal

Understand what "Pet Grooming Management" software actually is as an Application Type: who operates it, what core objects exist inside it, how the grooming cycle (booking → drop-off → groom → pick-up → payment) works, what grooming-specific structure exists (breed/coat/size-based service menus, behavior/handling records, groomer-time capacity), and where its boundary sits against the umbrella sibling (Pet Care Business Management), the structurally rhyming human salon Types (Salon Management System, Appointment-based Service Business Management), the duration-of-care siblings (Pet Boarding / Pet Daycare Management), and generic appointment scheduling.

Prior-pass context carried into this pass (flags to discharge):
- pet-care-business-management (processed 2026-09-09) recorded: "a single-line tool (grooming-only appointment book with client/pet records and billing) fails L0 leg 2's multi-line scope → it belongs to the sibling Type (Pet Grooming Management)" — this pass must discharge that boundary from the grooming side.
- pet-boarding-management (processed 2026-09-09): standing observation that pet-care-business-management is the umbrella over the same product population; grooming named as one bundled line.
- pet-daycare-management (processed 2026-09-09): "pet-grooming-management and pet-training-management remain unprocessed siblings and should discharge the cluster observation at their passes" (one product population, multiple scope cuts).

## Initial Boundary

Working hypothesis before research:

1. Core use: operator-side administration of a pet-grooming business (grooming salons, mobile groomers, grooming desks of pet-care facilities) — appointment book + client/pet records + service menu + billing.
2. Primary users: groomers, front-desk staff, owner-operator; pet owners as self-service clients.
3. Nearest neighbors: Pet Care Business Management (umbrella), Salon Management System / Appointment-based Service Business Management (same appointment-book skeleton, human trade), Pet Boarding / Pet Daycare Management (same trade, different unit of work), generic Appointment Scheduling Application.
4. Likely seam with salon management: the served subject is an animal (breed/coat/size/behavior), services priced by the animal's attributes, owner drops off and is called back for pick-up, mobile-grooming variant.
5. Unknowns: is groomer-time capacity definitional or merely common? Is the service menu's breed/coat/size pricing definitional? Does vaccination gating (documented in boarding) carry to grooming? Is a distinct mobile-grooming structure a variant or a separate Type?

## Research Questions

1. What is the unit of work — how is a grooming appointment represented, and what lifecycle does it traverse?
2. What is the capacity model — how does the appointment book realize groomer time (columns, slots, blocks, pet counts)?
3. What lives on the pet record vs the client record — what grooming-relevant data does the system hold?
4. How is the service menu structured — pricing and duration rules (breed/coat/size), add-ons, packages?
5. How does the appointment resolve into money — checkout, tips, deposits/no-show protection, retail?
6. What happens between drop-off and pick-up — status tracking, ready-for-pickup notification, grooming notes?
7. What client-facing surfaces exist — online booking, portals, recurring appointments?
8. What rules and exceptions matter — double-booking, conflicts, cancellations, no-shows, difficult dogs?
9. What variants exist — mobile grooming, salon, multi-line facilities, deployment generations, region?
10. Where are the boundaries against the neighboring Types (umbrella, salon/appointment-business, boarding/daycare, vet, marketplace scheduling)?

## Representative Products

Selection principles applied: market representation, documentation completeness, different product philosophies (mobile-first modern platform / desktop-lineage suite / mobile-groomer-native booking app), different customer tiers (solo → high-volume), different deployment postures (cloud / installed desktop lineage).

| Product | Positioning | Tier of evidence |
|---|---|---|
| MoeGo | Grooming-first modern platform ("The Intelligent Platform for Pet Businesses"; grooming the founding line, boarding/daycare added later); solo → enterprise/multi-location, mobile + salon | A — official help center (Intercom) fetched at article level |
| DaySmart Pet (123Pet) | Grooming-led business software ("Trusted by over 5,000 groomers"; industries: grooming, daycare, boarding, mobile pet grooming; "since 2005"); solo → high-volume salons; ships an installed Windows desktop release alongside cloud | B — official product/industry pages + official downloads page |
| Groomer.io | Grooming-only software + websites for salons and mobile groomers ("purpose-built for grooming salons and mobile groomers", 10+ years claim) | A− — official help center (HubSpot) article fetched + product pages |
| Gingr (carried evidence) | US multi-line pet-care SaaS; grooming sold as the "Appointments" booking type with specialist (groomer) scheduling | carried from research/pet-care-business-management.md (Tier-1 help-center structure) |
| Revelation Pets (carried evidence) | Budget multi-line SaaS; grooming via "appointment calendars — staff calendars, block availability, manage grooming" | carried from research/pet-care-business-management.md (Tier-2) |

Rejected/abandoned samples (per network-restriction rule):
- Groomer's Edge (veteran desktop grooming software) — groomersedge.com returned HTTP 403; abandoned. The desktop-era pole is instead covered by DaySmart's official Windows installer (Version 13) and the paper-era conceptual anchor.
- Pawfinity — pawfinity.com and www.pawfinity.com both returned HTTP 403; abandoned.
- Groomer.io marketing subpages — two URL guesses returned 404; abandoned in favor of the vendor's help center.

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- MoeGo help center home: https://www.moego.pet/help/en
- MoeGo Grooming collection: https://www.moego.pet/help/en/collections/12675311-grooming
- MoeGo Grooming Service collection: https://www.moego.pet/help/en/collections/16033855-grooming-service
- MoeGo article — Setting Up Your Grooming Services: https://www.moego.pet/help/en/articles/11116749-setting-up-your-grooming-services
- MoeGo article — Grooming Appointment - Create New: https://www.moego.pet/help/en/articles/14008185-grooming-appointment-create-new
- DaySmart Pet root: https://www.daysmart.com/pet/
- DaySmart Pet grooming industry page: https://www.daysmart.com/pet/dog-grooming-software/
- DaySmart Pet downloads & drivers (desktop installer): https://www.daysmart.com/pet/support/downloads-drivers/
- Groomer.io root: https://groomer.io/
- Groomer.io help center home: https://help.groomer.io/
- Groomer.io help section — Booking an Appointment: https://help.groomer.io/booking-an-appointment
- Groomer.io help article — Scheduling New Customers - Calendar (BLOCK Scheduling): https://help.groomer.io/schedule-appointments-block
- Groomer.io help section — Payments: https://help.groomer.io/payments
- Groomer.io help section — Getting Started and Onboarding: https://help.groomer.io/getting-started-and-onboarding
- Carried: research/pet-care-business-management.md (Gingr and Revelation Pets grooming-line evidence, MoeGo Client & Pet collection incl. Pet vaccine, MoeGo retail "coming soon")

Source-access limitations:
- Groomer's Edge and Pawfinity unreachable (403 ×1 / ×2 respectively); the veteran desktop pole is not directly sampled.
- DaySmart Pet evidence is Tier-2 (product/industry/marketing pages) plus the official downloads page; no help-center article bodies fetched. Vendor claim numbers (5,000+ groomers, 50+ reports, plan prices, "one to seven days" reminder window, "since 2005") are recorded as vendor claims only and none are asserted in the final document.
- Groomer.io evidence is help-center structure + one fetched article + product pages; "How To" article bodies beyond the block-scheduling article were not fetched.
- MoeGo appointment-detail and calendar article bodies beyond the two fetched were not retrieved; exact appointment state names were not verified at field level.
- The sample is US-centric (all three primary products are US vendors); regional fit of the definition is argued structurally (no region-specific machinery named in the core), not from sampled regional products.

---

## Product A — MoeGo

### Key observations (evidence layer A — help-center article bodies unless noted)

**Positioning**: "The Intelligent Platform for Pet Businesses." By care type: mobile grooming, grooming salon (live); boarding, daycare (live, later additions); retail/training/pet-sitting "coming soon" (carried from pet-care pass). Business sizes: enterprise, franchise, multi-locations. Help-center Grooming collection (39 articles) described as "Schedule and manage grooming appointments, services, and your calendar."

**Service menu (Tier-1, "Setting Up Your Grooming Services")**:
- Grooming services configured with: name, category (editable category list), description (client-visible on online booking/storefront), active/inactive status, image, calendar color code, available business locations, **assigned staff per service** ("When creating an appointment, the assigned staff will automatically appear when that service is selected"), price, tax rate, **duration**, advanced per-location and **per-staff price/duration overrides** ("staff members work at different speeds on the same service").
- **Pet-details applicability**: each service specifies which **pet types & breeds** ("All Types and Breeds" vs "Customize"), which **weight/size ranges**, and which **coat types** it applies to; scheduling and online booking then show only applicable services ("Only Show Applicable Services" filter). Companion articles: Service Price By Coat Type; Service Price By Types & Breeds; Service Price By Pet Size / Weight; Service Price By Age Group (Alpha).
- **Add-ons** as a separate catalog class with default add-on rules (auto-include with a service).
- **Pricing priority FAQ** (verbatim structure): 1. last finished appointment's price & duration (if book again); 2. saved price & duration for pet; 3. saved price & duration for staff; 4. price & duration in service setting. Custom price/duration can be saved per pet.
- Service edits can apply to "all unconfirmed upcoming appointments"; **confirmed appointments retain the price set at booking time** (manual updates required).

**Appointment creation (Tier-1, "Grooming Appointment - Create New")**:
- Created from + Quick Actions, from the Grooming Calendar (click an **available time slot under a staff member**), from a client profile, or via **Book Again** (copies a previous appointment).
- Creation flow: select client (search/dropdown/quick-add) → **select one or more pets** (multi-pet families: "Each pet can have its own service and assigned staff") → select services + optional add-ons (at least one service required; appointments "cannot be created with add-ons only") → **staff auto-assigned by priority: last appointment groomer (book again) → preferred groomer → first available groomer in the staff list** (manual override; per-service and multi-staff assignment supported) → date & start time; **duration and price editable per appointment** → "Book Now" → optional confirmation message (send now / schedule later / not this time); client agreement sent alongside if required.
- **Conflict machinery**: overlapping appointments or staff-off-schedule produce a yellow warning message (schedule overrides are visible, not silent).
- **New-pet quick-create required fields: name, gender, pet type, breed, weight, coat type**; optional: spayed/neutered status, birthday, **behavior notes**, pet codes, pet photo.
- Appointment-level machinery (collection titles): Alert Note, Ticket Comments, Client & Pet Notes, **Update History**, Repeat Appointment (recurring), Edit Appointment, Waitlist, Smart Scheduling (recommended slots), **Book-by-slot Mode: By Pet Number** (capacity realized as pet-count slots), Multi-staff & Multi-pets, Print Appointment.
- Calendar View collection: calendar configuration, print appointment, calendar views. Mobile Grooming collection: Map View, Route Optimization, Service Areas, Vans Management, Advanced Settings.

**Context from help-center structure (layer A at collection level)**: Client & Pet collection (47 articles — client/pet profiles, pet vaccine, leads, intake forms, digital agreements, pet parent portal, report cards); Online Booking (29); Payments (44 — invoices, refunds, MoeGo Pay); Staff Management (22 — "staff schedule, payroll, staff profile"); Business Management (availability rules); Marketing; Insights (revenue, payroll, performance); Advanced Tools (workflow automation, loyalty, integrations).

## Product B — DaySmart Pet (123Pet)

### Key observations (evidence layer B — product/industry pages + official downloads page)

**Positioning**: "Pet Business Software for Groomers, Kennels, and More"; grooming industry page: "DaySmart Dog Grooming Software: A Cut Above the Rest" — "whether you run a brick-and-mortar or mobile pet grooming business"; "Trusted by over 5,000 groomers"; "Since 2005, DaySmart Pet has been helping dog grooming and pet care businesses of all sizes". Business tiers: solo groomers / growing grooming shops / high-volume salons. Footer brands the mobile app "123Pet Groom Software". (Vendor claims only.)

**Scheduling**: "**Digital Appointment Book**" viewable "by day, week, or employee"; drag-and-drop rearrangement; accepted online bookings auto-added, cancellations removed; "**making it impossible for your dog grooming business to double-book**"; **recurring appointments** ("Schedule repeat clients… enter details once"); automated text/email appointment reminders with client reply-to-confirm shown in the appointment book; "24/7 Online Booking… gives you control over scheduling" (staff-approval framing); digital forms "sent via text or email mean faster check-ins".

**Client & pet records**: "Client & Pet Profiles give you instant access to preferences and histories"; "Keep client and pet details, photos, and preferences organized"; mobile app to "track **grooming, personality, and medical information**"; "**Track vaccination statuses.** Receive alerts when they are nearing expiration… and notify pet guardians when pets are due for vaccines."

**Money**: seamless checkouts (chip/swipe/tap, Apple/Google Pay); "**No-Show Protection** lets you collect deposits and securely store card info to cover cancellation fees"; invoices; card-on-file for "deposits, no-shows, and late cancellations"; Clover Mini/Flex devices; gift cards; **payroll processing** ("salary by the hour or commission settings… business payroll based on sales commissions, time clock information"); loyalty programs/rewards "displayed at checkout"; pricing tiers Basic→Premium Growth (vendor claim). Inventory management at Deluxe tier; integrations (QuickBooks, Glammatic websites, Beresford gift cards).

**Mobile grooming**: "Easily map your daily route and get directions… turn-by-turn directions, traffic conditions, and estimated travel times"; "everyone can also track pick-up and drop-off times"; accept payments on the go (mobile card readers); mobile app for appointments on the road. FAQ: "DaySmart Pet was built specifically for mobile grooming businesses. It combines scheduling, route planning, client communication, and payments in one platform."

**Desktop generation (official evidence)**: Downloads & Drivers page ships "**DaySmart Pet Version 13**" as a Windows installer (123PetSetupV13.exe) plus an updater — an installed desktop release line coexisting with the cloud product; compatibility page claims "Windows, Mac, iOS, and Android". Documents the desktop-era deployment pole with a current vendor's own artifacts.

## Product C — Groomer.io

### Key observations (evidence layer A− — help-center structure + one article body; product pages layer B)

**Positioning**: "Pet Grooming Software + websites" — "Software and websites purpose-built for grooming salons and mobile groomers"; "Trusted by 3,000+ mobile and storefront groomers" (vendor claim); "Trusted by groomers for over 10 years"; pricing "per storefront or van" (vendor claim).

**Salon features (root page)**: "Manage appointments, clients, and staff"; "**Automated pick-up calls and SMS**"; "**Track appointment working status**"; "**Automated comeback reminders**"; "**Multi-groomer Blocks & Slots scheduling**". Mobile features: "Optimize routes, share enroute updates… Automated enroute call and SMS; Smart mapping and scheduling; ETA and departure reminders; On-the-go client messaging and payments."

**Booking machinery (help center)**:
- Booking an Appointment section: two named scheduling styles — **BLOCK scheduling** and **BULK scheduling** — across calendar and home screens, for new and existing customers, plus "How to book an appointment for Mobile Groomers from the Map Screen".
- Block-scheduling article flow (Tier-1): calendar → day → + → "Create New Customer" (name, then "enter all pets separated by commas") → "**Assign this dog a breed**" → "Add Service" (service(s) for the appointment) → "Tap on the appointment time **under your desired groomer** (you can also drag and drop)" → confirm → "Add Phone" for "schedule confirmations, appointment reminders, and **ready-for-pick-up calls and texts**" → send the schedule confirmation text.
- Online Scheduling section: "set up Online Booking, Request, and how to Customize your page" (instant booking vs request modes).
- Getting Started section: "set up your facility, employees, schedules, and services".
- Payments section: Online Pay (pay ahead — "How can mobile groomers utilize Online Pay?"), Square and Square Terminal connections, "**DePAWsits (Deposits)**".
- Other sections: Client Management, Marketing, Payroll & Reporting (solution pages in root nav).

## Carried evidence — the multi-line population (umbrella context)

From research/pet-care-business-management.md (Gingr Tier-1, Revelation Pets Tier-2, ProPet Tier-2, MoeGo Tier-1 structure):

- Gingr separates booking into **Reservations** ("owners check in and check out their pet" — boarding/daycare) vs **Appointments** ("services that a customer can book for a specific time with a **specific specialist**" — the vendor's own grooming example), with **Specialist Scheduling** ("specialists = groomers/trainers with schedules").
- Revelation Pets: "Appointment Calendars — use staff calendars and block availability, and manage grooming, training, and van drivers."
- DaySmart Pet industries page lists grooming, daycare, boarding, mobile — grooming-led but multi-line capable.
- MoeGo retail "coming soon" while grooming/boarding/daycare live — proves retail non-definitional at family level; grooming is MoeGo's founding line (its help-center Grooming collection predates the Boarding & Daycare addition in product framing).

Reading: in the multi-line population, the grooming line is realized exactly as this Type's core (appointment book against specialist time + service menu + client/pet records + billing). The multi-line suite adds cross-line account/schedule/billing machinery on top — the umbrella Type's contribution, not the grooming line's.

## Cross-product Comparison

| Structure / capability | MoeGo (A) | DaySmart/123Pet (B) | Groomer.io (A−) | Gingr/Revelation (carried) | Assessment |
|---|---|---|---|---|---|
| Client account + pet records under it | client + pet profiles; quick-add pet during booking | client & pet profiles (photos, preferences, histories) | customer + pets created inline | Owners/Animals + Animals; client/pet profiles | **Defining (all sampled)** |
| Pet record carries grooming-relevant data | required: type, breed, weight, **coat type**; optional: behavior notes, spayed/neutered, birthday, photo | grooming, personality & medical info; vaccination statuses with expiry alerts | breed assignment at creation; (depth beyond article not fetched) | animal records with care data (umbrella population) | **Defining** |
| Grooming appointment as dated, time-bounded unit of work | full appointment machinery (create/edit/repeat/book again/waitlist) | digital appointment book, drag-and-drop | block/bulk scheduling flows | Appointments (specialist × time × service) | **Defining (all sampled)** |
| Services + add-ons from a configured service menu | service catalog with categories, add-ons, default add-on rules | service catalog (implied by appointment book + POS); inventory at higher tier | "Add Service" per appointment | services with prices (umbrella population) | **Defining** |
| Price & duration resolved from the menu, commonly by breed/coat/size; overridable per appointment/pet/staff | explicit four-level priority chain; price-by-coat/breed/size articles | (pricing rules not surfaced at fetched depth) | (not surfaced) | estimates for appointments | **Defining at MoeGo (Tier-1); directionally supported elsewhere — held common-realization, concept-level invariant is menu-resolved price+duration** |
| Groomer-time capacity the appointment consumes | slot under a staff member; conflict warnings; book-by-slot (pet counts); per-staff duration | appointment book "by employee"; "impossible… to double-book" | time "under your desired groomer"; multi-groomer Blocks & Slots | Specialist Scheduling; staff calendars | **Defining (all sampled)** |
| Appointment lifecycle through delivery (drop-off → groom → ready) | appointment detail machinery; print appointment; status surfaces in calendar | digital forms for "faster check-ins"; mobile app tracks grooming info | "track appointment working status"; ready-for-pick-up calls/texts | (umbrella population: check-in/out machinery) | **Defining (loop present in all sampled; exact state names unverified)** |
| Per-appointment billing resolving into payment | Payments collection (invoices, refunds, MoeGo Pay) | checkouts, invoices, Clover devices | Square/terminal + Online Pay | POS/cart, packages, store credit | **Defining (all sampled)** |
| Deposits / card-on-file / no-show protection | (payments depth not fetched) | explicit: deposits + stored cards cover no-shows/late cancellations | DePAWsits deposits; Online Pay pay-ahead | deposits (umbrella population) | **Common (3/4 observed; not asserted as universal)** |
| Online booking / client self-service | Online Booking collection (29 articles) | 24/7 online booking (approval framing) | online booking + request modes | online booking (umbrella population) | **Common (all sampled current products; desktop/paper poles lack it)** |
| Recurring / standing appointments + rebooking | Repeat Appointment; Book Again | recurring appointments ("schedule repeat clients") | automated comeback reminders | (not verified for grooming line) | **Common (3/4 observed)** |
| Reminders & confirmations (email/SMS) | confirmation message at booking; Communication collection | automated text/email reminders, reply-to-confirm | schedule confirmations, appointment reminders | reminders (umbrella population) | **Common (all sampled)** |
| Pick-up moment communication | (communication machinery present; automation unverified) | pick-up/drop-off time tracking (mobile) | automated pick-up calls and SMS; ready-for-pick-up texts | report cards/photos (umbrella population) | **Common as a workflow moment; automated ready-for-pickup messaging single-source (Groomer.io) — qualified** |
| Client intake forms / agreements | Client Form collection; agreement sent with booking | digital forms via text/email (faster check-ins) | (not surfaced) | forms/waivers (umbrella population) | **Common (2/4 observed)** |
| Vaccination records with expiry awareness | Pet vaccine article (Client & Pet collection, carried) | explicit: track vaccination statuses + expiry alerts + guardian notification | (not surfaced) | vaccination machinery (umbrella population, incl. blocking) | **Common (2/4 observed; blocking NOT evidenced in grooming-focused sample — contrast boarding)** |
| Waitlist | Waitlist article | (not surfaced) | (not surfaced) | waitlist (umbrella population) | **Optional (1/4 primary observed)** |
| Staff scheduling depth (commissions/payroll) | Staff Management collection (schedule, payroll, profile); Insights payroll reports | payroll by hour/commission, time clocks, sliding-scale commissions at top tier | Payroll & Reporting solution page | Specialist Scheduling + Employee Mgmt add-on (umbrella) | **Common; depth varies (full payroll → staff calendars)** |
| Retail / product sales | "coming soon" (carried) | POS, inventory (Deluxe tier), gift cards | (not surfaced) | retail modules (umbrella population) | **Optional (absence documented at MoeGo)** |
| Marketing / reviews / loyalty | Marketing collection; loyalty in Advanced Tools | email/SMS marketing, reputation management, review requests, loyalty at checkout | Marketing section | marketing (umbrella population) | **Optional/advanced** |
| Mobile-grooming machinery | Map View, Route Optimization, Service Areas, Vans Management collections | route mapping, turn-by-turn, ETA, on-go payments, pick-up/drop-off tracking | map-screen booking, enroute calls/SMS, ETA & departure reminders, per-van pricing | van drivers (Revelation, carried) | **Variant structure of the Type (segment-level, not separate Type)** |
| Deployment | cloud SaaS + iOS/Android + web | cloud + installed Windows desktop (v13 installer) + mobile apps | cloud (web app claim) + mobile | cloud SaaS | **Deployment variant; desktop lineage officially documented at DaySmart** |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (four jointly-held structures)

1. **The client-owned pet as the groomed subject.** An animal record held under an owner/client account, carrying what grooming work requires: species/type, breed, size/weight, coat type, temperament/behavior and handling notes, commonly vaccination status, and the pet's own service history and saved pricing. Custody stays with the owner; the service is walk-in/walk-out (drop-off, groom, pick-up — or a van visit), never custody transfer. Remove → a generic client CRM or a human-salon client list; the animal semantics collapse.
2. **The grooming appointment as the unit of work.** A dated, time-bounded service commitment binding specific pet(s) to service(s) and add-ons drawn from the business's configured service menu, with price and duration resolved from menu rules (in current products commonly by breed/coat/size, with per-appointment, per-pet and per-staff overrides) and client/staff/alert notes attached; it advances through a delivery lifecycle — booked → arrived/drop-off → in-groom → completed → picked up. Remove → a client/pet contact list with nothing to manage.
3. **Capacity-limited groomer time the appointment consumes.** Appointments are scheduled against the working time of identified groomer(s) — calendar columns/slots per staff member, blocks & slots, pet-count slot modes — so one groomer's time cannot silently host overlapping appointments; conflicts are flagged or double-booking prevented, and the solo/mobile pole schedules against the operator's own day (route). Remove → a waitlist or roster with no schedule; overbooking becomes unbounded.
4. **Per-appointment billing.** The completed appointment resolves into money: menu-priced services + add-ons (plus retail where offered) + fees − discounts → checkout/payment, with tips customary in the trade and deposits/card-on-file/no-show protection as common commercial machinery. Remove → a free appointment calendar, not a service business.

Jointly-held load-bearing tests:
- 1 alone = client/pet CRM
- 2 without 1 = anonymous booking
- 3 without 2 = staff calendar
- 4 without 1–3 = invoicing shell
- 1+2 without 3 = unbounded overbooking — not an appointment book
- 1+2+3 without 4 = free grooming — not a business
- 2+3 without 1 = generic appointment scheduling (human salon skeleton)

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Online booking page / client self-service (sometimes staff-approval-gated; instant-book vs request modes documented)
- Recurring/standing appointments and rebooking shortcuts (book again, repeat appointment, automated comeback reminders)
- Automated confirmations and reminders (email/SMS, reply-to-confirm)
- Appointment status/working-status tracking between drop-off and pick-up; print appointment/ticket
- Ready-for-pick-up communication (automated calls/texts documented at one product; the moment itself universal in the trade)
- Client intake forms and service agreements (digital signing, sent at booking or check-in)
- Vaccination records with expiry awareness (alerts documented; enforcement strictness unverified in this sample — contrast boarding where blocking is documented)
- Deposits, stored cards, no-show/late-cancellation fees; prepaid/pay-ahead options
- Waitlists (single-product observation in the primary sample)
- Staff management: schedules, per-staff price/duration, roles; commissions/time clocks/payroll at the deeper end
- Reports/analytics (revenue, performance, payroll); accounting integrations
- Marketing machinery: campaigns, two-way texting, review requests, loyalty (peripheral to the core loop)
- Mobile apps for staff/client communication
- Retail/POS (present in some products, absent from one sampled product's live feature set)

### L2 — Variant / Optional Structure

- **Business shape**: grooming salon/storefront vs mobile-grooming operation (route/map machinery, service areas, vans, ETA/enroute notifications, in-van payment — a large market segment on the same core) vs the grooming desk of a multi-line pet-care facility
- **Capacity realization**: per-groomer time columns vs shop-level slot counts (pet-number slots) vs block/bulk booking styles
- **Scale**: solo groomer → multi-groomer shop → multi-location/franchise
- **Service mix**: grooming-only vs grooming + daycare/boarding/training/retail lines (the latter = Pet Care Business Management scope)
- **Deployment**: cloud SaaS (current norm) vs installed desktop lineage (officially documented via a current vendor's Windows release) vs mobile-first app
- **Species scope**: dog-dominant with cat/small-animal options (pet types configurable)
- **Region**: no region-specific machinery in the core; the sampled vendors are US-centric (limitation noted)

### L3 — Vendor-specific Structure (Research Notes only)

- MoeGo: Smart Scheduling; Book-by-slot Mode (by pet number); Alert Note; Ticket Comments; Update History; the four-level price/duration priority chain (book-again price > per-pet saved > per-staff saved > service setting); per-staff duration ("staff members work at different speeds"); default add-on rules; "Grooming Report" (marketing claim); van management; leads pipeline
- Groomer.io: "DePAWsits" deposit branding; enroute automated calls; BLOCK vs BULK scheduling styles; Blocks & Slots terminology; per-van pricing; comeback reminders
- DaySmart Pet (123Pet): plan tiers with named capabilities (Basic $29 → Premium Growth — vendor claims); Clover hardware; Glammatic website / Beresford gift-card integrations; reputation management; "50+ reports" claim; "123Pet Groom" mobile-app branding; Windows Version 13 installer; "since 2005" history claim
- Gingr (carried): Reservations-vs-Appointments booking-type split; Specialist Scheduling; PreCheck; Employee Management add-on
- Revelation Pets (carried): staff calendars/block availability; van-driver calendars

## Rejected Findings (anti-overfit)

- **"Grooming management = online booking"** — rejected: online booking is universal in the current cloud sample but the desktop lineage (DaySmart v13) and the paper-era pole ran the same core without it.
- **"Breed/coat/size-based pricing is definitional"** — rejected as a specific mechanism: the invariant is that price and duration resolve from the business's service menu and are overridable; breed/coat/size applicability rules are the dominant current realization (Tier-1 at one product), not provably universal.
- **"Named per-groomer assignment is definitional"** — rejected in the strong form: the invariant is capacity-limited groomer time; the solo/mobile pole schedules against the operator's own time, and shop-level slot counts (pet-number slots) are a documented alternative realization.
- **"Vaccination blocking is definitional"** — rejected for this Type: expiry alerts are documented; no grooming-focused sample product documents hard booking blocks (contrast the boarding sibling where blocking is documented). Held variant/unverified.
- **"Mobile grooming is a separate Type"** — rejected: route/map/van machinery is business-shape packaging around the same appointment core (MoeGo and DaySmart ship both shapes in one product; Groomer.io prices "per storefront or van").
- **"Recurring packages/loyalty are definitional"** — rejected: loyalty/review machinery is peripheral marketing tooling; prepaid package evidence in the grooming-focused sample is thin (pay-ahead deposits documented instead).
- **"Add-ons require a base service"** — held product-specific (MoeGo: appointments cannot be created with add-ons only); not generalized.
- **Precise numbers/defaults NOT stated in the final document** — reminder windows, plan prices, deposit amounts, slot counts, capacity defaults are vendor claims or unverified; none asserted.

## Historical / Market-Sample Check

- **Paper-era grooming shop** (conceptual): appointment book with time columns per groomer, a breed-based price list on the wall, client index cards (breed, coat, temperament, clipper/sensitivities notes, vaccination note), phone reminder calls, cash/check presented at pick-up — satisfies all four defining structures with no software-era machinery.
- **Desktop generation** (documented): DaySmart ships an installed Windows release (Version 13) as a current, officially maintained artifact of the desktop lineage the vendor traces to 2005; compatibility claims span Windows/Mac/iOS/Android. The record classes (clients, pets, appointment book, services, billing) are the same as the cloud product.
- **Regional**: the sample is US-centric; the definition names no region-specific machinery (no US forms, no licensing packs), so regional/regime-specific grooming software fits structurally. Held as structural inference (limitation recorded), not sampled fact.
- **Mobile pole**: a single-groomer van with a route sheet — the day's route is the capacity; clients are pets on the route; money collected on the van — satisfies all four structures.
- Conclusion: the defining core is era-, deployment-, and business-shape-neutral. Online booking, portals, route optimization, automated notifications, and cloud delivery are era/market machinery and stay out of the core.

## Boundary Findings

1. **vs Pet Care Business Management (§29 sibling, umbrella leaf) — DISCHARGES the umbrella pass's boundary flag from the grooming side.** Keep-both RATIFIED: the seam is the scope cut. This Type documents the single-line core — client/pet records + grooming appointment book against groomer time + per-appointment billing — which the umbrella pass itself identified as the sibling-side of the seam ("a single-line tool… belongs to the sibling Type"). The sampled single-line pole (Groomer.io, grooming-only) and the grooming-first poles (MoeGo's founding line; DaySmart's grooming industry page) hold this core without multi-line machinery; the multi-line population (Gingr, ProPet, Revelation Pets) realizes the grooming line exactly as this Type's core inside the umbrella's shared multi-line schedule/account/billing system. Test both ways: remove the multi-line whole-business scope → this Type; add sibling service lines on one shared schedule and account → Pet Care Business Management. Single-line deployments of multi-line products sit on this side of the seam (consistent with the umbrella pass's own ruling).
2. **vs Salon Management System / Appointment-based Service Business Management** — structurally rhyming skeleton (appointment book + staff + client records + POS + online booking). The distinction is the trade semantics: the served subject is an animal under an owner account (breed/coat/size/behavior data drives service applicability and pricing), the owner drops off and is called back (pick-up loop, not a seated visit), and the mobile-grooming variant (route capacity, in-van service) has no human-salon analog. Remove the animals and drop-off/pick-up loop → salon/appointment-business management; the generic appointment Type lacks the client/pet records of record, menu-priced trade services, and the trade's money rules.
3. **vs Pet Boarding Management / Pet Daycare Management (§29 siblings)** — same software population (the multi-line vendors bundle all three), different unit of work and capacity model: grooming = a time-bounded appointment consuming groomer time, resolved same-day with walk-out billing; boarding = an overnight/multi-night stay consuming accommodation units; daycare = same-day attendance consuming daily headcount. Vendor-confirmed separation: Gingr's own booking-type split (Reservations vs Appointments) and Revelation Pets' separate appointment calendars for grooming. Cross-links exist (grooming add-ons during boarding stays in the umbrella population) without dissolving the seam.
4. **vs Veterinary Practice Management (§29 sibling)** — cosmetic service vs clinical care. Vaccination status appears as eligibility/alert data on the pet record, never as the clinical workflow; grooming products hold no medical records, diagnoses, or prescriptions. Mobile-grooming "medical information" fields (DaySmart) are handling notes (allergies, sensitivities), not clinical records.
5. **vs Dog Walking Platform / Pet Sitting Platform (§29 siblings)** — operator-side system of record for a business's own clients vs consumer-side two-sided marketplace of strangers; care is delivered at the salon/van on booked appointment time vs in/at the pet's home over a care duration. Multi-line vendors sell walking/sitting as separate service lines beside grooming (carried: KennelBooker's service list), vendor-documented separation.
6. **vs Appointment Scheduling Application (§03.09)** — generic scheduling is calendar-first with no client/pet records of record, no service-menu pricing machinery, and no money loop. The grooming appointment book is one realization of generic scheduling embedded in a trade system; the Type is defined by the trade system, not the calendar.
7. **vs Retail POS (§05.10)** — product sales are an optional module (absent from one sampled product's live feature set); the core transaction is a booked service, not a product sale.

Taxonomy observation for the §29 pet cluster (discharges the pet-daycare pass's cluster note from this side): the cluster pattern holds — one product population, multiple scope cuts (single-line grooming / boarding / daycare leaves + whole-business umbrella). The remaining unprocessed sibling, pet-training-management, should discharge the same observation at its pass.

## Uncertainties

- Exact appointment state vocabularies (booked/arrived/in-groom/ready) were not verified at field level for any product; the delivery loop is evidenced (status tracking, ready-for-pickup, print appointment) but no universal state names are asserted.
- Ready-for-pickup *automation* (calls/texts) is documented at Groomer.io only — single-source, held qualified; the pick-up moment itself is universal in the trade.
- Vaccination gating strictness in grooming (alert vs block) is unverified in the grooming-focused sample; only alerts are documented.
- Price-resolution breadth: the four-level priority chain is MoeGo Tier-1; the concept (menu-resolved price/duration with overrides) is the invariant, but other products' pricing-rule depth was not fetched.
- Tip handling and commission mechanics were not verified beyond DaySmart's commission/payroll claims.
- Waitlist, packages, and loyalty in the grooming-focused sample rest on thin or single-product evidence; all held qualified.
- Groomer's Edge and Pawfinity unreachable (403); the veteran desktop pole is not directly sampled — the desktop lineage rests on DaySmart's official Windows installer.
- Market-size and count claims (3,000+ groomers, 5,000+ groomers, 39-article collection, 10+ years) are vendor marketing numbers, recorded as claims only.

## Final Synthesis

Pet Grooming Management is the grooming business's operator-side system of record. Its defining core is four jointly-held structures: (1) the client-owned pet — an animal record under an owner account carrying the data grooming work runs on (type/breed/size/coat, behavior and handling notes, vaccination status, per-pet history and pricing); (2) the grooming appointment — a dated, time-bounded commitment binding pets to services and add-ons from the business's configured service menu, price and duration resolved from menu rules and overridable, advancing booked → drop-off → in-groom → completed → picked up; (3) capacity-limited groomer time — the appointment consumes a slot in an identified groomer's working day (columns, blocks & slots, or pet-count slots; the route on the mobile pole), with conflicts flagged or double-booking prevented; (4) per-appointment billing — the completed appointment resolves into payment with the trade's commercial furniture (tips, deposits/card-on-file, no-show protection). Around that core, mature products add online booking, recurring appointments and comeback automation, reminders, status tracking and ready-for-pickup communication, intake forms and agreements, vaccination awareness, staff management with commissions/payroll, reports, marketing, and retail — none definitional. The Type's sharpest boundaries: the umbrella sibling (multi-line whole-business scope vs the single-line core — ratified from both sides), the human salon Types (same appointment-book skeleton, but the subject is an animal and the visit is a drop-off/pick-up loop), the boarding/daycare siblings (hours-long appointment consuming specialist time vs days-long stay/attendance consuming facility capacity), and generic appointment scheduling (no trade records, no money loop). Mobile grooming is a business-shape variant — route machinery around the same appointment core — not a separate Type.
