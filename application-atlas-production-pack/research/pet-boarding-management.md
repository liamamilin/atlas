# Research Notes — Pet Boarding Management

Date: 2026-09-09
Slug: pet-boarding-management
Directory leaf: Pet Boarding Management (§29 Home, Family, Personal & Local Services)

---

## Research Goal

Understand what "Pet Boarding Management" software actually is as an Application Type: who operates it, what core objects exist inside it, how the boarding cycle (booking → check-in → board → check-out → payment) works, how daily care of boarded animals is organized, and where its boundary sits against the neighboring pet-family Types (Animal Shelter Management, Pet Daycare Management, Veterinary Practice Management, Pet Sitting / Dog Walking, Pet Care Business Management) and against the structurally rhyming Hotel PMS.

## Initial Boundary

Hypothesis before research: this is operator-side software for commercial boarding businesses (boarding kennels, catteries, pet hotels, boarding wings of daycare/grooming businesses). The owner retains custody of the animal; the business sells an overnight (or multi-night) stay in its own accommodation units, plus care during the stay. Closest confusion risks:

- Animal Shelter Management — also tracks animals in kennels, but custody is transferred to the organization and the outcome is placement, not return-to-owner.
- Pet Daycare Management — same facilities, same software population, but same-day care without overnight accommodation consumption.
- Hotel PMS — same reservation→room→stay→folio skeleton, but the guest is a person.
- Pet Sitting Platform — care without a facility inventory (in-home).

Prior-pass anchor: research/animal-shelter-management.md §Boundary Findings item 4 flags this leaf for joint review: "commercial boarding is a paid service where the owner retains custody; sheltering is custody transfer. Both track kennel occupancy, which creates surface similarity; the custody model and outcome set differ. ASM even ships a separate Boarding module chapter — again the vendor separates the structures." This pass must discharge that flag.

## Research Questions

1. What is the unit of work — how is a boarding commitment represented, and what lifecycle does it traverse?
2. What is the accommodation model — how are kennels/runs/rooms/units represented, and how does occupancy work?
3. How do the pet and the client relate — who is the customer, what is stored on the pet record?
4. How does daily care work — feeding, medication, exercise; how are instructions captured and executed?
5. How does the stay resolve into money — rates, duration bases, add-ons, deposits, packages, checkout?
6. What gates exist before a stay — vaccinations, contracts, waivers, assessments?
7. What client-facing surfaces exist — portal, online booking, updates during the stay?
8. What rules and exceptions matter — overbooking, capacity, cancellations, incidents, waitlists?
9. What variants exist — species, service mix, region, deployment, scale?
10. Where are the boundaries against the neighboring Types?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers/geographies:

| Product | Positioning | Tier of evidence |
|---|---|---|
| Gingr | US market-leading multi-service pet-care SaaS (boarding/daycare/grooming/training/dog park; enterprise tier) | A — official help center (Zendesk KB) fetched at article level |
| PetExec | Established US boarding/daycare SaaS (now Gingr/TogetherWork-owned, separately operated) | B — official product pages; docs center is a JS app (not fetchable) |
| Revelation Pets | Budget/simple SaaS aimed at small kennels and catteries (US/UK customer base) | B — official product/feature pages |
| ProPet | Canadian founder-owned all-in-one (boarding/daycare/grooming/training/retail) | B — official product/module pages |
| KennelBooker | UK-origin booking-first platform, 40 countries, licensing-compliance orientation; room-count pricing tiers | B — official product pages incl. boarding page and legacy-migration pages |

Historical/regional anchor (via vendor-documented migration): **KennelSuite** (Plane Software) — Windows desktop kennel software storing data in a password-protected local Microsoft Access database; company ceased trading ~2017/2018. Documented by KennelBooker's official "KennelSuite Alternative" page, which imports KennelSuite's "customer, pet and vet information". This documents the pre-cloud generation's record structure.

Rejected/abandoned samples:
- PetLinx (desktop kennel/cattery software, NZ) — www.petlinx.com and petlinx.com both failed with transport errors (2 attempts); abandoned per network-restriction rule. Legacy desktop generation covered via KennelSuite documentation instead.
- Kennel Connection — referenced as a competitor by Gingr and KennelBooker but not directly fetched; treated as part of the older desktop generation at B-/claim level only.

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- Gingr — https://www.gingrapp.com/ (root), https://www.gingrapp.com/kennel-software (boarding page), https://support.gingrapp.com/hc/en-us (help center home), /sections/25504866326541 (Owners and Animals), /sections/25504838903565 (Facility Management), /sections/25504731245453 (Reservations, Appointments, and Group Classes), /articles/27773305468557 (Areas & Lodging Topic Outline), /articles/31114610626061 (Animals Topic Outline), /articles/28500398225805 (Reservations Topic Outline), /articles/29641449718669 (During the Stay and Departure Topic Outline), /articles/28507854434829 (Feeding Topic Outline), /articles/29645201128077 (Check Out Reservations Topic Outline)
- PetExec — https://www.petexec.net/ (root), https://www.petexec.net/service/boarders (boarding page), https://docs.petexec.net/ (docs center home — JS application, article content not fetchable)
- Revelation Pets — https://www.revelationpets.com/ (root), /kennel-software, /features
- ProPet — https://www.propetware.com/ (root), /boarding-kennel-daycare-software/ (boarding & daycare module)
- KennelBooker — https://www.kennelbooker.com/ (root), /boarding, /kennelsuite-alternative
- Prior-pass cross-reference: research/animal-shelter-management.md (boundary flag to discharge)

Source-access limitations:
- PetExec documentation center (docs.petexec.net) is a JavaScript application; category pages render but article content was not retrievable. PetExec evidence is product-page level (Tier 2). No precise PetExec operational mechanics asserted.
- PetLinx unreachable (2 transport errors). No claims rest on it.
- No numeric limits (deposit percentages, cancellation windows, vaccination validity periods) were researched at Tier-1 depth; none are asserted anywhere.

---

## Product A — Gingr

### Key observations (evidence layer A unless noted)

**Positioning**: "pet business software for boarding kennels / doggy daycare / grooming salons / dog training"; boarding page: "From booking to checkout, the whole boarding stay runs in one system." 5,000+ facilities claim (marketing number, not asserted).

**Accommodation model (Tier 1, Areas & Lodging Topic Outline)**:
- "**Area** is a room or building within a facility that contains Lodgings."
- "**Lodging** is a specific kennel, run, pen, crate, or suite that the animal stays in within the Area… Lodgings are intended to be selected when a reservation type that requires Lodging (example: Boarding) is scheduled. Lodgings are booked at the time that the reservation is scheduled."
- "If your facility is Cage Free (you don't use enclosures like pens, kennels, or crates), you can skip creating lodgings." → cage-free facilities run on capacity alone.
- Capacity Limits section: location capacity limit, lodging capacity limit, capacity by date (set/edit). Boarding page: "automated capacity groups keep reservation types and services from overbooking"; FAQ: "Set up custom capacity rules that the online booking portal will follow to automatically show 'unavailable' to clients once those spots are filled."

**Unit of work (Tier 1, Reservations Topic Outline)**:
- "Within Gingr, every time a pet is checked in and out, this is considered a reservation."
- Reservation machinery: Reservation Types, Reservation Estimates, Reservation Deposits, Belongings, Online Reservations, Waitlist, Additional Services.
- Stay lifecycle sections in the KB: Reservations → Check-In (Quick Check-In, check-in from Expected Today, from Animal Profile, check in a pet without a reservation) → During the Stay and Departure (Report Cards, Check Out, Additional Services).
- Front-desk cockpit (home page mock): "Checked in 11 / Expected 4 / Going home 3", capacity "12 / 20", per-pet schedule with Check in/Check out actions.
- Lodging calendar: "the heart of a boarding operation — one view of what is full, what is open, and what is coming in"; "See which kennels and runs are occupied and which are available, by day."

**Pet & client records (Tier 1, Animals / Owners and Animals)**:
- Animal profile tabs: Details, Immunizations, Incidents, Report Cards, Reservations, Employee Notes, Additional Details.
- Animal machinery: Feeding (schedules, quantities, units, methods, types, statuses; Feeding Report; automated feeding charges), Medication Schedule, Immunization Records, Incidents, Temperament Types, Veterinarian List, Breeds, Animal Icons.
- Owner accounts as a parallel record class ("Owners and Animals").
- FAQ: "You can make vaccination uploads a mandatory step in the online portal. Then, Gingr will automatically block a reservation request if a pet's required vaccinations have expired or are missing." → vaccination gating blocks booking.

**Billing (Tier 1 + product pages)**:
- Check Out section: quick checkout, checkout with package credits, checkout using account balance, cart.
- "Automated pricing: Convert partial days to full stays, apply multi-pet discounts and batch payments automatically."
- Deposits paid online at booking; packages; memberships; convenience fees; integrated payment processing.
- Retail/purchases section exists in KB.

**Client-facing**: online portal (self-register, request stays, buy packages, pay deposits, add services), Pet Parent mobile app (book, pay, update pet records, message), report cards ("notes and photos by email or SMS — or print them out"), PreCheck ("Vaccinations, waivers, and belongings verified the night before"), reservation reminders (email/SMS templates).

**Staff-facing**: run cards ("Set Up Run Cards", "Automatically Print Run Card at Check-In", "Show Employee Notes on Run Cards"), dashboards, calendars, hours of operation with pick-up/drop-off times, forms, status page.

**Vendor-specific (L3)**: Areas→Lodgings two-level hierarchy; PreCheck; evaluation workflow; automated feeding charges; memberships; convenience fees; webcams mentioned in trust framing.

## Product B — PetExec

### Key observations (evidence layer B — product pages only; docs center not fetchable)

**Positioning**: "Operations Software for Boarding Facilities and Boarders. From managing rooms to intake notes, we've got it all."

**Boarding-specific features (boarding page)**:
- "Manage Kennels and Occupancy: Track your stays with ease and avoid overbooking during peak seasons."
- "Occupancy Management: PetExec seamlessly tracks your occupancy and prohibits users from booking if your facility is full. That said, we allow you to double-book if you like!" → capacity enforcement with an operator override.
- "Create a customizable boarding eScorecard to easily track feedings, medicines, and eliminations on any device."
- "Custom Options and Services: You can create options for boarding facility (rooms, suites, etc.) and set your own prices."
- "Collect Deposits: Easily require customers to pay a deposit prior to booking a stay and help curb the issue of customers who reserve a room but never show up."
- "Automatic Daycare Fees: We calculate the number of hours/days a dog is boarded and allow you to add on daycare fees at checkout for any dogs that are boarding with you." → boarding+daycare combination billing.
- "Create and Sell Add-ons: … walks, Kong treats, and so on … add those add-ons to the customer's cart."
- "Manage Waitlist Customers: … automatically tracks customers who are wait listed and those customers who have scheduled their stay without paying their deposit."
- "Boarding Snapshot provides you with a top-level overview" (which dogs require additional services).
- Contract management: "Require customers sign up to three (3) contracts digitally, once they create their account, and restrict their ability to schedule themselves until these contracts are signed."
- Owner portal: self-book, pay deposits, upload files, see vaccination records; automatic email reminders before stays; paperless intake forms; document management (vet notes, vaccination paperwork); transaction/order history.

**Vendor-specific (L3)**: eScorecard; 3-contract gating; automatic daycare fees at checkout; Boarding Snapshot; Packmate program.

## Product C — Revelation Pets

### Key observations (evidence layer B — product/feature pages)

**Positioning**: "Dog Daycare, Cattery, Grooming, and Kennel Software… Designed with small businesses in mind." Separate solution pages: Cattery, Daycare, Grooming, Kennel.

**Dashboard/cockpit**: "The easily accessible dashboard provides a snapshot of your entire day. See arrivals, departures, appointments, and occupancy, all in one place. From the dashboard, you can check dogs in and out with one click, communicate with customers, print boarding cards, and easily search your records."

**Reservations**: "make a reservation or check-in a pet in just seconds. And with split bookings, you can fill up every space"; "simple but powerful waitlists, vaccination alerts, automatic booking reminders, and flexible rates for discounts or upsells."

**Customer portal**: "customers can easily check availability, make one-time or repeating reservations for boarding, make payments, and both access and provide key information such as vaccination records and pet activity."

**Features page**: cloud-based; customer portal (self-register, upload vaccine records, "view their pet during their stay" — camera framing); online booking widget; packages (credit packages with expiration); dashboard (arrivals/departures/appointments/occupancy, print boarding cards); boarding calendar (drag-and-drop bookings); pet updates (email updates with photos during the stay); reports (arrivals/departures, occupancy, bookings, payments, sales by service, **feedings**, birthdays, vaccinations); digital agreements (e-sign); vaccination records (store, track expiration, automatic reminders); customize & upsell ("Charge different rates for sharing pets, apply discounts, upsell products and enable a waitlist"); reservation reminders; appointment calendars (grooming, training, drivers, staff); profiles (client and pet profiles, color-coding, notes, credits).

**Vendor-specific (L3)**: credit packages with expiration periods; Google Calendar/Maps integration; review-request automation.

## Product D — ProPet

### Key observations (evidence layer B — product/module pages)

**Positioning**: "Boarding, Dog Daycare, Training, Grooming, and Retail — all in one place." Modules: Pet and Client Manager, Boarding Kennel Module, Dog Daycare Module, Grooming, Training, Retail, Scheduled Services. Founded by kennel owners, 2014, founder-owned.

**Boarding & daycare module page**:
- Dashboard: "simple but informative check-in/check-out process"; "Access notes, reservation summary, customer and pet profiles, **buddy and enemy list**, colour codes and more pet information."
- Admin-only notes and admin-only rates (bookable by staff, not by clients online).
- Manage bookings: "Easily mark bookings as **pending** to manage confirmations that are waiting lists, deposits, assessments etc."; change request and cancellation management; recurring daycare schedules; "open reservations" (accumulate then charge); "Customizable digital and printable **kennel cards**"; internal messaging; customer account credit; reservation-process logs.
- On-site pet management: "Daily reports including: Feeding, medication, and vaccinations management reports"; scheduled services (baths, walks); quick search; online access to documents, agreements, vaccination records.
- Kennel cards (booking sheets): customizable, printable, size options.
- Prepaid packages (bulk, expiring, bundles).
- Feature pages (nav): Kennel View, Vaccination Manager, Availability Calendar, Smart Pricing Engine, Report Cards, Companion Mobile App, Online Booking, Text Messaging.
- Home page: "Smart Medications — The right meds. The right pet. Every single time."

**Vendor-specific (L3)**: buddy/enemy list; open-reservation billing; kennel-card size options; Smart Pricing Engine branding.

## Product E — KennelBooker

### Key observations (evidence layer B — product pages; boarding page is detailed)

**Positioning**: "Software that fills your diary while you're with the dogs"; "The complete booking platform for boarding, cattery, board & train, daycare, grooming, dog-walking, training and house-sitting businesses." Services list: Boarding, Daycare, Grooming, Training, Board & Train, Dog Walking, Drop-in Visits, House Sitting, Evening Care, Universal Bookings, Cremation. "Trusted by pet businesses in 40 countries." UK-origin (AAL compliance), multi-currency pricing.

**Boarding page — pricing machinery**:
- "Charge by number of nights, days or 24-hour periods"; late checkout fees; cancellation fees; "Add up to two peak rates — mid-season and high-season. KennelBooker automatically applies the correct rate to every day of a booking"; percentage or fixed discounts; custom pricing algorithms (pets sharing runs, duration of stay); manual pricing always available.

**Boarding page — accommodation & occupancy**:
- "No room available? KennelBooker automatically checks if the booking can be **split across multiple runs** — so you capture more revenue instead of turning customers away."
- "Create runs/rooms for particular pet types"; "Allow certain pet types to share rooms (e.g. hamsters/rabbits)"; "Set pet capacity limits (e.g. 50-pet limit)"; "Set minimum and maximum booking durations"; "Prevent un-neutered pets attending."
- Calendar view with color coding "So you never double-book a run again."
- Pricing tiers by room count (10/30/60/100 rooms; "Group Rooms" feature counts concurrent bookings).

**Boarding page — check-in/checkout & care**:
- "Your entire day — one screen. See who is arriving, who is on-site, and who is leaving."
- "Check in pets with one click and **log their belongings** as they arrive."
- "Run cards ready in seconds. Print run cards for every pet at check-in, or batch print them all in one go. Contact details, pet info, **feeding instructions and medical notes** — everything your team needs before they open a run."
- "Activity recording: Record **feeding, medication, exercise and toilet breaks** against every pet's stay."
- "Automatic alerts for missing or expired vaccinations — before they become a problem"; FAQ: "Customers upload vaccination certificates to their own profiles, and you get automatic alerts at booking and check-in when a vaccination is missing or expired." → alert-and-verify gating (staff verify at check-in), contrasted with Gingr's block-at-booking.
- Digital waivers signed online; booking/vet waivers printed.
- Waitlist ("When a cancellation comes in, the system shows you which wait-listed bookings you can now accommodate"); wallet funds/credit; record payments with transaction reference; Stripe terminals for in-person (booking updated to 'paid'); document upload (customer and pet accounts); SMS reminders 24h before; postcards/mini-updates with pictures emailed during the stay.
- "Dietary & Medical Info: Individual pet records… Your KennelBooker daily overview page will highlight pets with any specific dietary or medical conditions."
- Customized questionnaires (customer or pet specific).
- Booking details screen: "quickly see if vaccines are in date or have expired, the price being charged, any additional services/charges."

**Compliance**: "Sail through your licensing inspection… UK Animal Activities Licensing Regulations 2018 (AAL)… EU GDPR… PCI DSS."

**Legacy generation (official migration page, "KennelSuite Alternative")**:
- "KennelSuite is no longer supported and the company behind it has ceased trading" (Plane Software, ~2017/2018).
- "KennelSuite stores your data in a password-protected Microsoft Access database on your computer."
- "Windows desktop only"; no online booking, no automatic emails/reminders/invoices, no online payments, no off-site backups (comparison table).
- "We will unlock your old database and import your data free of charge… import your **customer, pet and vet information** into KennelBooker."
- → Documents that the pre-cloud generation held the same record classes (customers, pets, vet info, bookings) on desktop; the cloud generation adds portal/payments/automation on top of the same core.

**Vendor-specific (L3)**: AAL 2018 compliance pack; PawCheck / AI Vaccination Checker; group rooms; two-peak-rate model; room-count pricing tiers; postcards; multi-currency; "Switch From" competitive set (KennelSuite, Kennel Connection, Gingr, PetExec, RevelationPets).

---

## Cross-product Comparison

| Structure / capability | Gingr (A) | PetExec (B) | Revelation Pets (B) | ProPet (B) | KennelBooker (B) | Assessment |
|---|---|---|---|---|---|---|
| Client (owner) account + pet records under it | Owners and Animals | owner portal accounts | client + pet profiles | Pet and Client Manager | customer + pet records | **Defining (5/5)** |
| Pet record carries care data (feeding/medication/behavior/vet) | feeding schedules, medication, temperament, vet list, incidents | eScorecard feedings/medicines/eliminations; vet notes | feedings reports; medical/dietary notes | feeding/medication reports; buddy/enemy; smart medications | feeding instructions, medical notes, dietary/medical highlighting, vet info (imported from legacy) | **Defining (5/5)** |
| Boarding reservation as dated unit of work (drop-off→pick-up) | "every time a pet is checked in and out, this is considered a reservation" | stays, deposits prior to booking | one-time or repeating reservations | bookings with pending state | bookings with min/max durations | **Defining (5/5)** |
| Accommodation inventory / capacity that stays occupy | Areas→Lodgings (kennel/run/pen/crate/suite); capacity groups & limits; cage-free skips lodgings | rooms/suites options; occupancy management; overbooking guard | occupancy; split bookings | kennel view; kennel cards | runs/rooms by pet type; room-count tiers; pet capacity limits; split bookings | **Defining (5/5)** — realized as named units OR aggregate capacity (cage-free) |
| Check-in / check-out workflow + daily cockpit | Expected Today / checked in / going home; quick check-in/out | implied (stays tracked) | arrivals/departures/occupancy dashboard; one-click check in/out | check-in/check-out dashboard | arriving/on-site/leaving; one-click check-in | **Defining (5/5)** |
| Per-stay billing resolving into payment | checkout cart, packages, account balance, deposits | deposits, transaction history | invoices, payments, credit packages | invoicing, packages, account credit | rates × nights/days/24h, peak rates, fees, deposits, wallet, terminals | **Defining (5/5)** |
| Vaccination records with expiry + gating | blocks booking if expired/missing (FAQ) | vaccination records online; reminders | store, track expiry, reminders, alerts | Vaccination Manager | alerts at booking and check-in; staff verify | **Common** (5/5 present; gating strictness varies: block vs alert) |
| Daily care execution capture (run cards / scorecards / logs) | run cards, feeding report, automated feeding charges | eScorecard | boarding cards; feedings reports | kennel cards; daily feeding/med reports | run cards; activity recording (feeding/medication/exercise/toilet) | **Common** (5/5; form varies: printed card vs on-screen log) |
| Add-on services attached to the stay | additional services | add-ons (walks, treats) | upsells | scheduled services (baths, walks) | additional services (walks, baths, nail clipping) | **Common** (5/5) |
| Online booking / owner portal | portal + mobile app | owner portal | online booker + portal | online booking | branded booking portal | **Common** (5/5) |
| Deposits / packages / account credit | deposits, packages, memberships | deposits, packages | credit packages | packages, credit | deposits, wallet funds | **Common** (5/5; mix varies) |
| Waitlist | waitlist topic | waitlist tracking | waitlists | pending bookings (waitlists, deposits, assessments) | waitlist with cancellation matching | **Common** (5/5) |
| Reminders / confirmations (email/SMS) | email/SMS templates | automatic reminders | automatic reminders | reminders, triggers | confirmations + 24h SMS | **Common** (5/5) |
| Waivers / contracts / agreements | PreCheck incl. waivers; forms | up to 3 digital contracts gate self-scheduling | digital agreements | agreements | digital waivers; booking/vet waivers | **Common** (5/5; depth varies) |
| Report cards / photo updates to owner | report cards (email/SMS/print) | (not surfaced on fetched pages) | pet updates with photos | report cards | postcards/mini-updates | **Common** (4/5 observed) |
| Peak/seasonal & multi-pet pricing rules | multi-pet discounts, partial→full days | custom prices per room type | rates for sharing pets, discounts | Smart Pricing Engine | peak rates, sharing discounts, late checkout/cancellation fees | **Common** (5/5; depth varies) |
| Retail / product sales | retail section in KB | (not surfaced) | upsell products | Retail module | product sales with POS hardware | **Optional** (bundle-dependent) |
| Grooming / training / daycare lines beside boarding | all four + dog park | daycare, grooming, training | daycare, grooming | daycare, grooming, training, retail | daycare, grooming, training, board&train, walking, homestay, cremation | **Optional** (service-mix variant) |
| Incident reports | incidents tab + topic | "pet incidents managed" (claim) | (not surfaced) | (not surfaced) | (not surfaced) | **Optional** (2/5 observed) |
| Cameras / live view | webcams (trust framing) | (not surfaced) | "view their pet during their stay" | pet photography (not live) | (not surfaced) | **Optional** (2/5) |
| Regulatory compliance pack | (not surfaced) | (not surfaced) | (not surfaced) | (not surfaced) | AAL 2018 / GDPR / PCI DSS | **Optional / regional variant** (1/5) |
| Multi-location / enterprise | enterprise page | multi-building facilities claim | (not surfaced) | (not surfaced) | enterprise & multi-location page | **Optional / scale variant** |
| Belongings logging at check-in | Belongings topic | (not surfaced) | (not surfaced) | (not surfaced) | log belongings at arrival | **Common-leaning** (2/5 observed; likely under-documented elsewhere) |

## Canonical Model

### L0 — Defining Invariant

Four jointly-held structures. If any one is removed, the product stops being recognizable as pet boarding management:

1. **The client-owned pet as the boarded subject** — an animal record held under an owner/client account. Custody stays with the owner throughout; the animal arrives, is cared for, and returns home. Remove → custody-transfer territory (shelter / animal control).
2. **The boarding reservation/stay as the unit of work** — a dated, bounded service commitment (drop-off date/time → pick-up date/time) created before or at arrival, to which accommodation, care instructions, add-on services, and charges attach, and which advances through check-in → board → check-out. Remove → a client/pet contact list with nothing to manage.
3. **The capacity-limited accommodation inventory the stay occupies** — the facility's placement structure (kennels, runs, pens, crates, suites, cattery units) or, in cage-free realizations, aggregate capacity groups/limits; occupancy is the binding constraint and the overbooking guard. Remove → generic appointment scheduling.
4. **Per-stay billing** — the stay resolves into money: rates applied over the stay's duration (night/day/24-hour bases observed), plus add-on services and fees, invoiced and paid at or after checkout (deposits/packages/credit as common pre-payment forms). Remove → a free roster (which is shelter-like, not a service business).

Jointly-held load-bearing tests:
- 1 alone = client/pet CRM
- 2 without 1 = anonymous booking
- 3 without 2 = a facility map with nothing consuming it
- 4 without 1–3 = an invoicing shell
- 1+2 without 3 = sitting-style booking (no facility inventory) — Pet Sitting territory
- 1+2+3 without 4 = free kenneling — shelter-like, not a paid service business

### L1 — Common Mature Structure

Present across the sample (mostly 5/5 or 4/5) but not required to recognize the Type:

- online booking / owner portal (self-service requests, deposits, records)
- vaccination records with expiry tracking and gating (block-at-booking vs alert-and-verify-at-check-in both documented)
- care instructions on the pet record: feeding schedules, medication schedules, temperament/behavior flags, veterinarian
- daily care execution capture: run cards / kennel cards / scorecards (printed or on-screen), feeding/medication/exercise logs
- check-in/check-out workflow with a daily cockpit (arrivals, departures, on-site, occupancy)
- add-on services attached to the stay (walks, baths, one-on-one time)
- deposits, packages, account credit/wallet
- waitlists (with cancellation matching)
- confirmations/reminders (email/SMS)
- waivers/contracts/agreements with digital signing
- pricing rules: peak/seasonal rates, multi-pet/sharing discounts, late-checkout and cancellation fees, partial-day conversion
- report cards / photo updates to owners during the stay
- reports (occupancy, sales, feedings, vaccinations, arrivals/departures)
- belongings logging at check-in
- retail/product sales (bundle-dependent)

### L2 — Variant / Optional Structure

- Species scope: dog kennel vs cattery vs mixed; small-animal room sharing (rabbits/hamsters)
- Service mix: boarding-only vs boarding+daycare+grooming+training+retail; board & train; homestay/house-sitting lines sold beside boarding
- Enclosure-based vs cage-free operation (cage-free runs on aggregate capacity)
- Regulatory regime: UK Animal Activities Licensing 2018; US state/county kennel licensing; GDPR
- Deployment: cloud SaaS vs legacy Windows desktop (KennelSuite generation)
- Scale: single facility vs multi-location/multi-building
- Cameras/live view; memberships; convenience fees; review automation
- Payment posture: deposits required vs optional; package economies vs pay-per-stay
- Pricing bases: per night vs per day vs 24-hour periods

### L3 — Vendor-specific Structure

- Gingr: Areas→Lodgings two-level hierarchy; PreCheck; evaluation workflow; automated feeding charges; memberships; convenience fees; webcams
- PetExec: eScorecard; 3-contract self-scheduling gate; automatic daycare fees at checkout; Boarding Snapshot
- ProPet: buddy/enemy list; open-reservation billing; kennel-card size options; Smart Pricing Engine branding
- KennelBooker: AAL 2018 compliance pack; PawCheck/AI vaccination checker; group rooms; two-peak-rate model; room-count pricing tiers; postcards; multi-currency
- Revelation Pets: credit packages with expiration; Google Calendar/Maps integration; review-request automation

## Vendor-specific Findings

See L3. The most consequential market-structure observation: the sample's vendors form a tight competitive set that explicitly names each other (Gingr's "vs" pages: MoeGo, Goose, Paw Partner, RunLoyal, Kennel Connection; KennelBooker's "Switch From": KennelSuite, Kennel Connection, Gingr, PetExec, RevelationPets). This confirms a single product population (one Type), not several.

## Rejected Findings

- "Boarding management = kennel/cage management": rejected — Gingr documents cage-free facilities that skip lodgings and run on capacity alone; the invariant is capacity-limited placement, not enclosures.
- "Boarding management = online booking": rejected — the KennelSuite generation (documented via KennelBooker's migration page) had no online booking, no portal, no online payments, yet held the same customer/pet/vet/booking records. Online booking is era machinery.
- "Boarding management includes daycare/grooming/training": rejected as definitional — every sampled product bundles them, but each sells them as separable service lines (KennelBooker even sells homestay/cremation lines); the boarding core stands alone.
- "Vaccination gating always blocks booking": rejected — Gingr blocks at booking; KennelBooker alerts at booking and check-in with staff verification. The invariant is vaccination records with expiry awareness; enforcement strictness is a variant.
- "Boarding management = hotel PMS for pets": rejected as a definition — the reservation→room→stay→folio skeleton rhymes, but the daily work (feeding/medication/exercise execution, care instructions supplied by the owner, vaccination gating, behavior compatibility) has no hotel analog, and the guest cannot self-describe. Recorded as a structural rhyme, not an identity.
- "Report cards/cameras are the product": rejected — owner communication is common but absent from the legacy generation and optional in the sample.

## Boundary Findings

1. **vs Animal Shelter Management (§29 sibling; DISCHARGES the joint-review flag from the animal-shelter pass)** — confirmed with this pass's evidence. Shelter = custody transfer: animals enter by surrender/stray intake, outcomes are placement-type (adoption, transfer, return-to-owner, euthanasia), funding is donations/adoption fees. Boarding = owner-retained custody: animals enter by client booking, the stay is a paid service with a defined end, the outcome is always return-to-owner, and money flows as per-stay billing. Vendor-confirmed separation: ASM ships Boarding as a separate optional module chapter beside its shelter core (prior-pass Tier-1 evidence); no boarding product in this sample models custody transfer or adoption outcomes. Structural test holds both ways: remove the paid-service booking cycle and add custody transfer → shelter management; remove custody transfer and add client billing over booked stays → boarding management. The shared surface (kennel occupancy) is real but non-defining on both sides.
2. **vs Pet Daycare Management (§29 sibling, unprocessed)** — same software population (Gingr, PetExec, Revelation Pets, ProPet, KennelBooker all serve both), different unit of work: daycare is same-day care (day passes, recurring schedules, open reservations) without overnight accommodation consumption; boarding is the overnight/multi-night stay that consumes accommodation capacity. The two coexist in one product and cross-link (PetExec auto-charges daycare fees for boarded dogs; KennelBooker runs both on one calendar). Flag for joint review when the daycare leaf is processed; provisional seam: the overnight stay consuming placement capacity.
3. **vs Veterinary Practice Management (§29 sibling, unprocessed)** — clinical business (appointments, procedures, medical records, clinical billing) vs hospitality/care service. Boarding products reference veterinarians as a data field on the pet record (Gingr vet list; KennelBooker imports "vet information"), never as the clinical workflow. Vet-run boarding exists in the market but the boarding function there is the same structure documented here.
4. **vs Pet Sitting Platform / Dog Walking Platform (§29 siblings, unprocessed)** — sitting/walking = care without a facility accommodation inventory (in the pet's home or the caregiver's home), typically marketplace- or mobile-worker-shaped. KennelBooker ships Homestay, House Sitting, Dog Walking, Drop-in Visits as separate service types beside Boarding — vendor-documented separation within one product. Structural test: remove the facility accommodation inventory → sitting territory.
5. **vs Hotel PMS (§17)** — the reservation→room/unit→stay→folio skeleton is the same shape, and this is the closest cross-section rhyme. Differences that make it a different Type: the guest is an animal that cannot self-describe (the owner supplies care instructions and pre-authorizes care); the daily operational work is care execution (feeding/medication/exercise/toilet) rather than housekeeping of guest-facing rooms; eligibility gating is vaccination/health/behavior-based, not identity/payment-based; the business commonly stacks daycare/grooming/retail lines; the "folio" resolves per pet per stay with sharing/multi-pet economics. Held as adjacent-with-shared-skeleton.
6. **vs Pet Care Business Management (§29 sibling, umbrella leaf)** — the umbrella Type is the same product population viewed at whole-business scope (boarding+daycare+grooming+training+retail in one suite). Boarding Management is the boarding-specific core within it. Family observation, consistent with the §29 trade-leaf family pattern recorded in the pest-control pass.
7. **vs Appointment Scheduling Application (§03.09)** — generic appointment booking lacks the accommodation inventory, the care-execution layer, and per-stay rate×duration billing. Boarding scheduling is capacity-of-units scheduling, not calendar-of-staff scheduling.

## Historical / Market-Sample Check

- **Paper-era kennel** (conceptual): booking diary + kennel board + handwritten run cards with feeding/medication notes + bill presented at checkout — satisfies all four L0 legs with no software-era machinery.
- **Legacy desktop generation** (documented): KennelSuite — Windows desktop, local password-protected Access database, customer/pet/vet records, bookings; no online booking, no automatic communications, no online payments (KennelBooker official comparison). Satisfies all four legs; ceased trading ~2017/2018, its record structure still imports into current products.
- **Regional**: UK catteries and AAL-2018 licensing (Revelation Pets cattery edition; KennelBooker compliance pack); Australian operators (customer testimonials); multi-currency (KennelBooker: EUR/GBP/USD/AUD/CAD/NZD/ZAR/CHF/MYR). Non-US regimes fit without US-specific machinery in the core.
- Conclusion: the L0 definition is era-, region-, and deployment-neutral. Online booking, portals, vaccination uploads, report cards, and cloud delivery are all era machinery and stay out of the core.

## Uncertainties

- PetLinx (desktop kennel/cattery vendor) unreachable — the direct sample is cloud-heavy; the legacy desktop pole is covered only through KennelBooker's official migration documentation, not by fetching a legacy vendor's own materials.
- PetExec operational mechanics (exact reservation states, scorecard fields) are behind a JS docs application; PetExec claims are product-page level.
- Exact reservation state vocabularies vary and were not exhaustively researched (Gingr: expected/checked-in/checked-out; ProPet: pending; KennelBooker: booking → paid). No universal state taxonomy is asserted.
- Numeric rules (deposit percentages, cancellation windows, vaccination validity defaults, capacity defaults) were not researched at Tier-1 depth; none are asserted.
- Belongings logging is observed at only 2/5 products (Gingr, KennelBooker) but both treat it as a check-in step; classified Common-leaning with a note that other products may under-document it.
- Incident reporting observed at 2/5 (Gingr Tier-1; PetExec claim-level); held Optional.

## Final Synthesis

Pet Boarding Management is the operator-side service system of record for businesses that board client-owned animals overnight in their own accommodation. Its world model: a **client-owned pet** (custody retained by the owner; the animal goes home) books a **boarding reservation/stay** — the dated unit of work that advances drop-off → board → pick-up; the stay occupies a place in a **capacity-limited accommodation inventory** (kennels/runs/suites/cattery units, or aggregate capacity in cage-free operations), which is the binding constraint against overbooking; and the stay resolves into **per-stay billing** (rate × duration + add-ons + fees → invoice/payment, with deposits/packages/credit as common pre-payment forms). Around this core, mature products add: an owner-facing booking portal, vaccination records with expiry gating, care instructions (feeding/medication/behavior) captured on the pet record and executed daily through run cards/kennel cards/scorecards and activity logs, a check-in/check-out cockpit, add-on services, deposits/packages/waitlists/reminders/waivers, owner communications (report cards, photos), pricing rules (peak rates, sharing discounts, fees), reports, and retail. The Type's sharpest boundary is against Animal Shelter Management (custody transfer vs owner-retained custody — a boundary the leading shelter vendor itself maintains by shipping Boarding as a separate module), against Pet Daycare Management (same-day vs overnight accommodation consumption), and structurally against Hotel PMS (same booking skeleton, but the guest is an animal whose care — not room service — is the daily work).
