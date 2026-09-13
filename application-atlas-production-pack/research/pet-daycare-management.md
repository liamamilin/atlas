# Research Notes — Pet Daycare Management

Date: 2026-09-09
Slug: pet-daycare-management
Directory leaf: Pet Daycare Management (§29 Home, Family, Personal & Local Services)

---

## Research Goal

Understand what "Pet Daycare Management" software actually is as an Application Type: who operates it, what core objects exist inside it, how the daycare day (drop-off → care → pick-up → payment) works, how recurring attendance and walk-ins are handled, how group play is organized, and where its boundary sits against the neighboring pet-family Types — above all **Pet Boarding Management** (whose pass left a joint-review flag for this leaf), Pet Care Business Management (umbrella), Dog Walking / Pet Sitting Platforms, Animal Shelter Management — and against the naming-collision neighbor Daycare / Preschool Management (children).

## Initial Boundary

Hypothesis before research: this is operator-side software for businesses that provide same-day care for client-owned animals in a facility (dog daycare, doggy daycare, pet daycare; often alongside boarding/grooming/training). The owner retains custody; the animal arrives in the morning (or for a scheduled day), spends the day in supervised group or individual care, and goes home the same day. Closest confusion risks:

- Pet Boarding Management — same facilities, same software population, same care semantics, but the overnight stay consuming accommodation capacity is the boarding unit of work; daycare is same-day attendance.
- Pet Care Business Management — the umbrella leaf over the same product population at whole-business scope.
- Daycare / Preschool Management (§29 children's segment) — the word "daycare" collides; the subject (children vs animals), structures (enrollment/classrooms/ratios vs attendance/playgroups), and regulatory context differ.
- Dog Walking Platform / Pet Sitting Platform — care without a facility (outing or in-home), typically marketplace-shaped.
- Animal Shelter Management — custody transfer, no per-attendance billing.

Prior-pass anchors to discharge:
- research/pet-boarding-management.md §Boundary Findings #2: "same software population … different unit of work: daycare is same-day care (day passes, recurring schedules, open reservations) without overnight accommodation consumption … Flag for joint review when the daycare leaf is processed; provisional seam: the overnight stay consuming placement capacity."
- STATUS.md pet-boarding entry: "NEW FLAG for unprocessed pet-daycare-management … joint review recommended when that leaf processes."
- STATUS.md pet-care-business-management entry: taxonomy observation that the §29 pet cluster repeats the trade-leaf family pattern; the daycare leaf is one of the scope cuts.

## Research Questions

1. What is the unit of work — how is a day of attendance represented (day pass, reservation, recurring schedule, walk-in)?
2. What is the capacity model — aggregate daily headcount, per-date limits, capacity groups, play areas/rooms?
3. How do the pet and client relate — who is the customer, what care data lives on the pet record?
4. How does the daily loop work — check-in, group assignment, activities, feeding/medication, report card, check-out?
5. How does attendance resolve into money — day/half-day/hourly rates, packages of days, memberships, late pick-up fees, credits?
6. What gates exist before attendance — vaccinations, temperament evaluations/assessments, waivers?
7. What client-facing surfaces exist — portal, online booking, updates during the day?
8. What rules and exceptions matter — overbooking, late pick-up, walk-ins, behavior removal, waitlists?
9. What variants exist — daycare-only vs multi-line, group-play vs room-based, membership vs per-day, scale?
10. Where are the boundaries — vs boarding (discharge the flag), vs the umbrella, vs the children's daycare Type, vs walking/sitting, vs shelter?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers — the same product population the boarding and umbrella passes sampled, now observed through the daycare lens:

| Product | Positioning | Tier of evidence |
|---|---|---|
| Gingr | US market-leading multi-service pet-care SaaS; dedicated daycare segment page + deep Zendesk help center | A — daycare product page + help-center articles fetched at article level |
| MoeGo | Mobile-first platform (grooming + boarding & daycare); Intercom help center with a full Boarding & Daycare collection incl. Playgroup | A — help-center articles fetched at article level |
| KennelBooker | UK-origin booking-first platform, 40 countries; dedicated doggy-daycare page with daycare-specific mechanics | B — official daycare product page |
| Revelation Pets | Budget/simple SaaS aimed at small businesses; dedicated dog-daycare solution page | B — official daycare product page |
| ProPet | Canadian founder-owned all-in-one; daycare module (shares the boarding module page) | B — carried from the pet-boarding pass (module page fetched there) |

Supplementary (carried, not re-fetched): **PetExec** — boarding/daycare SaaS; boarding-pass product-page evidence includes daycare-fee cross-charging. Its daycare page returned 404 this pass; docs center JS-unreachable (limitation carried from the boarding pass).

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- Gingr — https://www.gingrapp.com/dog-daycare-software (daycare product page); help center: https://support.gingrapp.com/hc/en-us/articles/27923415247117 (Capacity Limit Permissions & Settings Reference), /articles/28500398225805 (Reservations Topic Outline), /articles/39265789329037 (Understanding the Evaluation Results Icon Reference)
- MoeGo — help center: https://www.moego.pet/help/en/collections/12675402-boarding-daycare (collection), /articles/14106724 (Boarding & Daycare Overview), /articles/11731114 (Set Up Daycare Service), /articles/15338486 (Playgroup Overview), /articles/12729636 (Daycare Quick Check-in)
- KennelBooker — https://www.kennelbooker.com/daycare (redirects to /daycare-software; daycare product page)
- Revelation Pets — https://www.revelationpets.com/dog-daycare-software (daycare solution page)
- ProPet — carried from research/pet-boarding-management.md (https://www.propetware.com/boarding-kennel-daycare-software/ fetched there; this pass's /dog-daycare-software/ URL redirects to the site home)
- Prior-pass cross-references: research/pet-boarding-management.md (joint-review flag), research/pet-care-business-management.md (umbrella lens; MoeGo collection structure), research/dog-walking-platform.md (daycare as a marketplace daytime service), STATUS.md boundary entries

Source-access limitations:
- PetExec daycare page 404 (1 attempt; abandoned per network rule). PetExec evidence stays at boarding-pass product-page level; no PetExec daycare mechanics asserted beyond the boarding page's "Automatic Daycare Fees" feature.
- ProPet's daycare module has no dedicated page (nav points the "Dog Daycare Module" link at the combined boarding-and-daycare module URL); ProPet daycare observations are from that combined page (fetched in the boarding pass).
- Revelation Pets and KennelBooker evidence is product-page depth (Tier 2); no help-center articles fetched for them this pass.
- No numeric limits (capacity defaults, fee amounts, package sizes, evaluation counts) were researched at Tier-1 depth; vendor-quoted examples (e.g., KennelBooker's "10 days for $200") are quoted as the vendor's own illustrations, not asserted as market defaults.

---

## Product A — Gingr

### Key observations (evidence layer A unless noted)

**Positioning (daycare page, Tier 2)**: "Dog daycare software built for a busy play floor." "From the morning rush to the last pickup, the whole daycare day runs in one system." Features: check-in/check-out ("One screen shows who is expected, who is already in, and who is going home today"), online booking ("Pet parents book their own daycare days from the app… Your capacity limits are built in, so the play floor never overbooks"), payments ("Sell daycare passes in bundles, take payment at pickup"; screenshot: "a daycare full-day package sold as credits"), PreCheck ("Paperwork, vaccinations and belongings are confirmed before the leash hits the lobby"), two-way messaging attached to the pet profile, report cards ("Notes on how the day went — behavior, demeanor and any health flags; Photos and video from the play floor; Sent by email or text, one pet at a time or the whole day's roster at once").

**Daycare-specific details (daycare page)**:
- Custom icons on the check-in screen flag "an expired vaccination, a favorite playgroup, a pet who eats alone" → playgroup and feeding flags surface at the front desk.
- "Daycare Full Day reservation" appears as a reservation type in the booking screenshot.
- Capacity Management: "Create automated capacity groups for reservation types and services."
- Automated Pricing: "Convert half-day appointments to full-day, apply multi-pet discounts and automatically batch payments."
- Memberships: "stack benefits… automate renewals… discounts that apply automatically and across your locations."
- Late pickup fees FAQ: "automatically apply a late fee if a dog is not checked out by closing time or the end of their scheduled block."
- **Daycare-only FAQ**: "Does Gingr work for a daycare that doesn't do boarding? Yes. Gingr runs daycare-only operations every day: check-in and check-out, daycare passes, report cards and payments all work without any boarding setup at all." → the daycare core stands alone in the vendor's own words.

**Capacity machinery (help center, Tier 1 — Capacity Limit Permissions & Settings Reference)**:
- Location capacity limit = "the maximum number of animals allowed at the facility at one time."
- Related how-tos: Set Location Capacity Limit, Set Lodging Capacity Limit, Set/Edit Capacity Limit by Date, Create Capacity Groups, Set Animal Icon Capacity, Enable Availability Calendar.
- Permission "Can Override Capacity": staff with the permission may override when booking into an 'at capacity' error.
- Setting "Allow Requests Over Capacity": customers may request over-capacity reservations for staff rejection, or receive an error — operator's choice.

**Reservations (help center, Tier 1 — Reservations Topic Outline)**:
- "Within Gingr, every time a pet is checked in and out, this is considered a reservation." Reservations created on the New Reservation page and via Quick Check In.
- Machinery: Reservation Types, Reservation Estimates, Reservation Deposits, Belongings, Online Reservations, Waitlist, Additional Services.

**Evaluation gate (help center, Tier 1 — Understanding the Evaluation Results Icon)**:
- Color-coded evaluation status: gray (never evaluated), green (passed all required categories), orange (partial), red (completed but passed none).
- Evaluation Workflow topics: Configure Evaluation Types, Managing Evaluation Results in the Pet Profile, Booking an Evaluation in the Customer Portal, pass email/SMS templates.
- Customer portal: "Requires Evaluation" badge on booking categories; "If a booking is attempted without a passed evaluation, the system redirects the customer to book the evaluation first."
- Multi-location options for saving evaluation results (per location / all locations).

**Carried from the boarding pass (Tier 1)**: animal profile tabs (Details, Immunizations, Incidents, Report Cards, Reservations, Employee Notes, Additional Details); feeding schedules/automated feeding charges; medication schedules; temperament types; veterinarian list; vaccination gating blocks online booking when expired/missing; run cards; Areas→Lodgings; cage-free facilities skip lodgings.

**Vendor-specific (L3)**: PreCheck; evaluation-results icon color logic; animal icon capacity; memberships module; capacity-override permission model; report-card roster-wide send.

## Product B — MoeGo

### Key observations (evidence layer A — Intercom help center)

**Boarding & Daycare Overview (Tier 1)**:
- "MoeGo's Boarding & Daycare module gives pet care facilities a complete system for managing overnight stays and daily attendances."
- "Whether you run a standalone boarding kennel, a daycare drop-in business, or a full-service facility that combines grooming with overnight stays, the Boarding & Daycare module is built around your daily operations." → daycare-only ("daycare drop-in business") is a named deployment.
- Setup articles: Set Up Boarding Services, Set Up Daycare Services ("service menu, set pricing, and define pet eligibility"), Set Up Lodging, Set Up Feeding & Medication Settings, Set Up Evaluation Service ("evaluation appointments to assess new pets before they're eligible for boarding or daycare services").
- Appointment articles: create boarding/daycare appointment ("Manually book a boarding stay or daycare attendance, assign lodging, and add optional grooming services"), Daycare quick check-in ("Check in walk-in daycare clients without going through the full booking flow"), Evaluation Management ("Create evaluation appointments, record pass/fail results, and view a pet's evaluation history"), apply feeding & medication.
- Views: Lodging View (occupancy, drag-and-drop), Lodging Capacity ("how room/kennel and area capacity are calculated and how overbooking rules work"), Checkout Cut-off Time.
- Pricing rules: nightly rates, length-of-stay discounts, custom fees ("late pick-up, early drop-off, or cleaning charges to boarding and daycare appointments").
- Online booking: "arrival and pickup windows, booking lead times, capacity limits, and waitlist settings."
- Client communication: auto messages for boarding & daycare.

**Set Up Daycare Service (Tier 1)**:
- Daycare services organized in categories; service fields: name, category, description, status, image, color code.
- Lodgings toggle: a daycare service may be limited to specific lodging types (combined-module realization).
- Businesses: multi-location offering toggle.
- Price, tax, override by business location.
- **Max stay duration**: "Receive notifications if the stay exceeds the set duration."
- **Service Auto Rollover**: "automatically roll over to another service after checking in for a certain period of time… Example: This service will turn into a Full Day service if a pet stays 30 minutes past the max duration of 4 hours." → the half-day→full-day conversion mechanism, vendor-documented.
- Pet eligibility: type & breed, weight ranges, pet codes (eligible/blocked).
- **Evaluation requirement**: "an evaluation must be added to this appointment before staff can schedule this daycare service"; online-booking variant: "clients will be prompted to schedule an evaluation before they can book the actual daycare service online."

**Playgroup Overview (Tier 1)**:
- "Boarding and daycare facilities group dogs by size, temperament, energy level, or service type to keep play sessions safe and manageable."
- Before-state: "most facilities tracked this on whiteboards or from memory — group assignments didn't carry between days, vaccine flags required opening individual profiles."
- Capabilities: create named groups with a color and a daily pet capacity; assign pets in advance (from the evaluation appointment or the pet profile); batch-assign ungrouped pets on arrival; monitor groups daily (capacity, vaccine flags, in-house status); reassign by drag in Day View; print group lists for handlers.
- "Playgroup information is visible to your internal team only. It is never shown to pet owners."
- Plan-gated: "available to Boarding & Daycare businesses on Growth and Ultimate plans" (vendor packaging detail).

**Daycare Quick Check-in (Tier 1)**: "For walk-in clients… select the service type and pet, enabling you to check in pets for daycare services only quickly."

**Vendor-specific (L3)**: Service Auto Rollover; pet codes; playgroup plan gating; max-stay notifications; weekly summary.

## Product C — KennelBooker

### Key observations (evidence layer B — daycare product page)

**Positioning**: "Doggy daycare software built for busy daycare businesses. Manage walk-ins, recurring bookings, daycare packages, and online payments — all in one place."

**Durations & capacity**: "Book any duration — full day, half day, or hourly. Your daycare, your rules. Set a daily dog limit and KennelBooker blocks out availability automatically when you're full. No overbooking. No stress."

**Grouping**: "Assign pets to play areas or rooms — your choice. Group pets into specific play areas or use your boarding rooms for daycare overflow. Full flexibility to run your space exactly the way that works for you."

**Walk-ins**: "Walk-ins checked in instantly. Search for a pet, add the booking, done. The quick check-in screen is built for busy morning rushes — add multiple bookings in seconds even when the queue is out the door."

**Recurring**: "Customer comes every Mon, Wed and Fri? Add all their bookings for the next 3 years in a single step. Availability is checked automatically for every date… Book 3 months of daycare in one go — one click saves them all. The customer gets one confirmation email with every date listed."

**Money**: "Sell daycare packages: Offer bundles like '10 days for $200' and collect payment immediately"; "Credits sit on the customer account and are automatically applied at checkout"; credit balance ledger on the customer's history page; "Require up-front payment for online daycare bookings — customers with a positive credit balance won't be asked to pay."

**Gates**: "Vaccination reminders: Get alerted in real time when customers book in without valid or in-date vaccinations"; "Evaluation checks: Require evaluations for pets before they are allowed to book in for daycare"; "Waivers signed before they even arrive — customers sign your daycare waivers when they register online."

**Other**: auto-confirm online bookings "while space permits — and block certain customers or dogs from booking online if required"; SMS reminders 24h before; tags on bookings/customers/pets; email & SMS automation (acknowledgments, confirmations, receipts, check-out messages); FAQ: every plan includes daycare alongside boarding, grooming, training, dog walking, homestay.

**Carried from the boarding pass**: daily overview (arriving/on-site/leaving), run cards with feeding/medical notes, activity recording (feeding/medication/exercise/toilet breaks), AAL 2018 compliance orientation, wallet funds.

**Vendor-specific (L3)**: 3-year recurring booking horizon; credit balance ledger; PawCheck/AI vaccination checker; room-count pricing tiers.

## Product D — Revelation Pets

### Key observations (evidence layer B — daycare solution page)

**Positioning**: "Simplify, Organize, and Modernize Your Dog Daycare… powerful yet intuitive software that can streamline tedious processes like booking, check-in."

**Day at a glance**: dashboard "Your Day at a Glance" — one-click overview.

**Reservations**: "Create and Manage Dog Daycare Reservations in Seconds… create a new booking in seconds, schedule repeat appointments, and edit and update bookings right from the calendar." Google Calendar/Maps integration; staff availability through the calendar.

**Portal**: online customer portal — book reservations, make payments; "it's simple to generate activity reports so clients can check in on their pets during the day"; portal supports "vaccine information, medical and dietary notes, terms and conditions."

**Money**: "Intuitive Payments with Dog Daycare Packages… one-time reservations or to purchase packages and keep track of credits"; "Daycare Credit Packs: Maintain customer loyalty and improve cash flow by selling a range of dog daycare credit packages. Credits are applied to reservations with just a couple of clicks."

**Reports**: arrivals and departures, bookings, customer history, payment, vaccination records, birthdays; QuickBooks/Xero export.

**Carried from the boarding pass (features page)**: dashboard with arrivals/departures/appointments/occupancy and one-click check in/out; boarding calendar drag-and-drop; vaccination records with expiry tracking and reminders; waitlists; rates for sharing pets; pet updates (email updates with photos during the stay); feedings reports; digital agreements.

**Vendor-specific (L3)**: credit packages with expiration; Google Calendar/Maps; review-request automation.

## Product E — ProPet

### Key observations (evidence layer B — carried from the pet-boarding pass; combined boarding & daycare module page)

- Modules include a named "Dog Daycare Module" (nav), but its page is the combined boarding-and-daycare module page — the vendor treats them as one module surface.
- Dashboard: "simple but informative check-in/check-out process"; notes, reservation summary, customer and pet profiles, **buddy and enemy list**, colour codes.
- Bookings: "Easily mark bookings as pending to manage confirmations that are waiting lists, deposits, assessments etc."; change request and cancellation management; **recurring daycare schedules**; **"open reservations" (accumulate then charge)**; customizable digital and printable kennel cards; internal messaging; customer account credit; reservation-process logs.
- On-site pet management: daily reports (feeding, medication, vaccinations); scheduled services (baths, walks); quick search.
- Prepaid packages (bulk, expiring, bundles); feature pages: Kennel View, Vaccination Manager, Availability Calendar, Smart Pricing Engine, Report Cards, Companion Mobile App, Online Booking, Text Messaging; Smart Medications.

**Vendor-specific (L3)**: buddy/enemy list; open-reservation billing; kennel-card options; Smart Pricing Engine branding.

## Product F — PetExec (supplementary, carried)

- Boarding page (boarding pass): "Automatic Daycare Fees: We calculate the number of hours/days a dog is boarded and allow you to add on daycare fees at checkout for any dogs that are boarding with you." → daycare as a cross-line charge on boarding stays.
- Daycare page 404 this pass; docs center JS-unreachable. No further PetExec daycare mechanics asserted.

---

## Cross-product Comparison

| Structure / capability | Gingr (A) | MoeGo (A) | KennelBooker (B) | Revelation Pets (B) | ProPet (B, carried) | Assessment |
|---|---|---|---|---|---|---|
| Client (owner) account + pet records with care data | ✔ (carried Tier 1) | ✔ (Tier 1) | ✔ | ✔ | ✔ | **Defining (5/5)** |
| Daycare attendance as the unit of work (check-in → care day → check-out, same day) | "every check-in/out = reservation"; "Daycare Full Day reservation" | "daily attendances"; daycare appointment; daycare quick check-in | bookings by full/half/hourly day | daycare reservations; repeat appointments | recurring daycare schedules; open reservations | **Defining (5/5)** |
| Capacity-limited daily attendance | location capacity = "max animals at facility at one time"; capacity by date; capacity groups; override permission | capacity limits in online booking; playgroup daily pet capacity | "daily dog limit… blocks out availability… No overbooking" | occupancy (dashboard) | capacity machinery (kennel view; carried) | **Defining (5/5)** — Revelation/ProPet documented more thinly |
| Per-attendance billing | passes in bundles, payment at pickup, half→full conversion, late fees | service price; auto rollover to full day; late pick-up/early drop-off fees | full/half/hourly rates; packages; credits; up-front online payment | daycare credit packs; payments | open reservations accumulate then charge; packages | **Defining (5/5)** |
| Walk-in / quick check-in | Quick Check-In (carried Tier 1) | Daycare Quick Check-in (Tier 1) | "walk-ins checked in instantly" | one-click check in (carried) | dashboard check-in | **Common** (5/5) |
| Recurring schedules | memberships imply recurring patterns; recurring reservations not directly observed | not observed | 3-year recurring, one confirmation | "schedule repeat appointments" | "recurring daycare schedules" | **Common** (3/5 direct + memberships) |
| Playgroups / play areas | "favorite playgroup" icon | full Playgroup machinery (named groups, daily capacity, drag reassign, handler lists) | "play areas or rooms… boarding rooms for daycare overflow" | not surfaced | buddy/enemy list (behavior grouping) | **Common** (4/5) |
| Evaluation / temperament gate | evaluation workflow, icon, portal redirect (Tier 1) | evaluation service, pass/fail, required-before-scheduling (Tier 1) | "Evaluation checks… before they are allowed to book in" | not surfaced | assessments in pending bookings | **Common** (4/5) |
| Vaccination records + expiry gating | blocks booking (carried); expired-vaccination icon | vaccine flags in playgroup view | real-time alerts at booking | records, expiry, reminders | Vaccination Manager | **Common** (5/5) |
| Daily care execution (feeding/medication) | feeding/medication machinery; "pet who eats alone" icon | feeding & medication in appointment; task management | activity recording (carried) | feedings reports (carried) | daily feeding/med reports | **Common** (5/5) |
| Report cards / owner updates | report cards with photos/video; roster-wide send | auto messages; client communication | SMS check-out messages | activity reports; pet updates with photos | report cards | **Common** (5/5) |
| Packages / credits / memberships | passes, memberships | not surfaced on fetched pages | packages, credits, ledger | credit packs | prepaid packages | **Common** (4/5 + memberships) |
| Late pick-up / early drop-off fees | late-fee FAQ | Late Pick-Up / Early Drop-Off Fee rule (Tier 1) | late checkout fees (boarding page) | not surfaced | Smart Pricing Engine (depth unspecified) | **Common** (3/5) |
| Half-day / full-day / hourly durations | half→full conversion | max stay + auto rollover (Tier 1) | full/half/hourly | not surfaced | not surfaced | **Common** (3/5) |
| Waitlist | waitlist topic (Tier 1) | waitlist settings in online booking | auto-confirm while space permits (no waitlist surfaced) | waitlists (carried) | pending bookings incl. waitlists | **Common** (4/5) |
| Waivers / agreements | PreCheck incl. waivers | not surfaced | waivers at registration | digital agreements (carried) | agreements | **Common** (4/5) |
| Online booking / owner portal | portal + mobile app | online booking collection | online bookings + accounts | portal + booking | online booking | **Common** (5/5) |
| Boarding / grooming / training lines beside daycare | all four + dog park | boarding + grooming | all + walking/homestay/cremation | kennel/grooming/cattery | all + retail | **Optional** (service-mix variant) |
| Webcams / live view | not surfaced this pass | — | — | "view pet during stay" (carried) | — | **Optional** (1/5 this pass) |
| Daycare-only deployment supported | ✔ vendor FAQ | ✔ "daycare drop-in business" named | ✔ (daycare page standalone) | ✔ (daycare solution page) | ✔ (module configurable per service mix) | **Variant axis** (5/5) |

## Canonical Model

### L0 — Defining Invariant

Four jointly-held structures. If any one is removed, the product stops being recognizable as pet daycare management:

1. **The client-owned pet as the cared-for subject** — an animal record held under an owner/client account, carrying the care data the day requires (vaccination status, feeding/medication instructions, temperament/behavior flags, veterinarian). Custody stays with the owner; the animal arrives and goes home the same day. Remove → custody-transfer territory (shelter / animal control).
2. **The daycare attendance as the unit of work** — a same-day service commitment (drop-off → care day → pick-up within the business day) for a specific pet, created before arrival (booking, recurring schedule) or on arrival (walk-in), to which group assignment, care instructions, add-on services, and charges attach, and which advances check-in → in-care → check-out. Remove → a client/pet contact list with nothing to manage.
3. **Capacity-limited daily attendance** — the facility's limit on how many animals can be in care at once (location-level headcount, per-date limits, per-reservation-type capacity groups, play-area/room capacities), the binding constraint and the overbooking guard. Remove → generic appointment scheduling / an unbounded roster.
4. **Per-attendance billing** — the attendance resolves into money: day/half-day/hourly rates, packages of days, memberships, late pick-up fees, and add-on services, paid at pick-up or prepaid through credits/packages. Remove → a free drop-in roster, which is not a service business.

Jointly-held load-bearing tests:
- 1 alone = client/pet CRM
- 2 without 1 = anonymous day booking
- 3 without 2 = a headcount board
- 4 without 1–3 = an invoicing shell
- 1+2 without 3 = an unbounded roster (no overbooking guard)
- 1+2+3 without 4 = free drop-in playgroup

### L1 — Common Mature Structure

Present across the sample (mostly 4/5–5/5) but not required to recognize the Type:

- walk-in / quick check-in (the morning-rush flow)
- recurring attendance schedules (weekly patterns booked far ahead)
- playgroups / play areas (named groups, often with their own capacity; assigned by size/temperament/energy)
- temperament evaluation/assessment gate before first attendance (pass/fail recorded; booking gated or prompted)
- vaccination records with expiry tracking and gating (block vs alert-and-verify varies)
- daily care execution capture (feeding/medication logs, task lists)
- report cards / photo updates to owners during or at the end of the day
- packages of days, credits, memberships
- late pick-up / early drop-off fees; half-day/full-day (sometimes hourly) rate tiers
- waitlists
- waivers/agreements signed online
- online booking / owner portal
- confirmations and reminders (email/SMS)

### L2 — Variant / Optional Structure

- Service mix: daycare-only vs daycare + boarding + grooming + training + retail (the most common modern shape is multi-line; daycare-only is explicitly supported)
- Group-play (cage-free, playgroup-organized) vs room-based operations; boarding rooms reused as daycare overflow
- Species scope: dog-dominant; cat/small-animal daycare exists in-market
- Commercial model: pay-per-day vs packages of days vs monthly memberships
- Drop-in vs scheduled vs recurring attendance patterns
- Scale: single site vs multi-location (evaluation results sharing across locations is a multi-location concern)
- Regulatory context: licensing regimes (e.g., UK animal-activities licensing) add record-keeping expectations
- Webcams/live view; dog park / dog bar adjacent segment (walk-in membership venues)

### L3 — Vendor-specific Structure

- Gingr: PreCheck; evaluation-results icon color logic; animal icon capacity; memberships module; capacity-override permission; roster-wide report-card send
- MoeGo: Service Auto Rollover (half-day→full-day); pet codes; playgroup plan gating (Growth/Ultimate); max-stay notifications; weekly summary
- KennelBooker: 3-year recurring booking horizon; credit balance ledger; PawCheck/AI vaccination checker; room-count pricing tiers
- Revelation Pets: credit packages with expiration; Google Calendar/Maps integration; review-request automation
- ProPet: buddy/enemy list; open-reservation billing; kennel-card options; Smart Pricing Engine branding
- PetExec: automatic daycare fees charged on boarding stays (cross-line billing)

## Vendor-specific Findings

See L3. Market-structure observation: the sample is the same competitive set as the boarding pass (KennelBooker's "Switch From" list names Gingr, PetExec, RevelationPets; Gingr's "vs" pages name MoeGo, Goose, Paw Partner, RunLoyal) — one product population in which daycare is a first-class segment. Vendor page architecture varies: Gingr, Revelation Pets, and KennelBooker maintain dedicated daycare pages; ProPet and MoeGo present daycare inside a combined boarding-and-daycare module. Both architectures serve the same population.

## Rejected Findings

- "Daycare management = a booking calendar": rejected — capacity limits, care execution, and per-attendance billing are load-bearing in every sampled product.
- "Playgroups are definitional": rejected — Revelation Pets (a daycare-focused product) surfaces no group machinery; MoeGo's own before-state description ("whiteboards or from memory") shows group tracking predates software machinery. Group assignment is common and characteristic, not invariant.
- "Temperament evaluations are definitional": rejected — not surfaced at Revelation Pets; present at 4/5. Characteristic of daycare (group play screening) but not invariant.
- "Recurring schedules are definitional": rejected — walk-in daycare is a first-class flow (MoeGo Daycare Quick Check-in; KennelBooker walk-ins; Gingr Quick Check-In). Recurring is common, not required.
- "Daycare management includes boarding": rejected — Gingr's own FAQ: daycare-only operations run "without any boarding setup at all"; MoeGo names the "daycare drop-in business" as a standalone deployment.
- "Pet daycare management = childcare management for pets": rejected — the children's daycare Type (§29) is built on enrollment, classrooms, ratios, guardians, and learning records; pet daycare is built on attendance, capacity, vaccinations, and day rates. The shared word "daycare" is a naming collision, not a shared structure.
- "Daycare capacity = kennel inventory": rejected — daycare capacity is headcount-at-once (location/date/group limits); it can be realized through play areas or rooms, but the invariant is the daily attendance limit, not overnight units.

## Boundary Findings

1. **vs Pet Boarding Management (§29 sibling; DISCHARGES the pet-boarding pass's joint-review flag)** — keep-both RATIFIED. Same software population (all sampled products serve both lines), same client/pet records, same care semantics, same vaccination gates — but different unit of work and capacity model: daycare = same-day attendance consuming daily attendance capacity (headcount at the facility at once; day/half-day/hourly billing); boarding = overnight/multi-night stay consuming accommodation capacity (kennels/runs/suites per night; rate × duration billing). The seam is the overnight stay. Vendor corroboration: Gingr, Revelation Pets, and KennelBooker maintain separate boarding and daycare pages; Gingr's FAQ states daycare-only operation works "without any boarding setup at all"; MoeGo names "overnight stays and daily attendances" as the two booking shapes of one module; ProPet combines them in one module page. Cross-links are common and documented: PetExec auto-charges daycare fees on boarding stays; KennelBooker uses boarding rooms as daycare overflow; MoeGo daycare services can be limited to lodging types. Structural test both ways: remove the overnight span and accommodation consumption → daycare management; add the overnight stay consuming accommodation units → boarding management. Neither core contains the other; both documents stand.
2. **vs Pet Care Business Management (§29 sibling, umbrella leaf)** — the umbrella Type is the same product population at whole-business scope (multi-line booking, cross-line accounts, cross-line billing). Daycare Management is the daycare-specific core within it. Family pattern consistent with the §29 trade-leaf observation. Test: remove the multi-line scope → this leaf; add sibling lines to the daycare core → the umbrella.
3. **vs Daycare / Preschool Management (§29 children's segment) and Childcare Management System** — naming collision only. Children's daycare: enrolled children under guardians, classrooms and ratios, licensing, learning records, tuition. Pet daycare: client-owned animals, attendance capacity, vaccinations, day rates, playgroups. No shared defining structure beyond "scheduled care with attendance." Both Types stand; the shared word should not suggest a relationship.
4. **vs Dog Walking Platform / Pet Sitting Platform (§29 siblings)** — walking = the outing as service unit, consumer-side marketplace of independent walkers; sitting = custody care in the pet's home or caregiver's home; daycare = facility-based same-day group care, operator-side system of record. KennelBooker ships Dog Walking as a separate service line beside daycare — vendor-documented separation. Dog-walking research independently treats daycare as a distinct daytime service in marketplace search wizards.
5. **vs Animal Shelter Management (§29 sibling)** — custody transfer vs owner-retained custody; shelter outcomes are placements, daycare outcomes are always return-to-owner-same-day; shelter has no per-attendance billing. Consistent with the custody boundary ratified in the boarding pass.
6. **vs Veterinary Practice Management (§29 sibling, unprocessed)** — clinical business vs care service; the veterinarian appears as a data field on the pet record, never as clinical workflow.
7. **vs Appointment Scheduling Application (§03.09)** — daycare scheduling is capacity-of-day scheduling (headcount limits, per-date capacity, capacity groups) with a care-execution layer and per-attendance billing; generic appointment scheduling is staff-calendar scheduling without those.
8. **vs Dog Park / Dog Bar software (Gingr segment)** — adjacent walk-in membership venue segment; observed only as a Gingr navigation segment this pass, held as market context, not a boundary resolution.

## Historical / Market-Sample Check

- **Paper-era dog daycare** (conceptual): a daily roster with a maximum headcount, a check-in sheet, play groups sorted by temperament on a whiteboard, handwritten feeding/medication notes, day rates collected at pick-up — satisfies all four L0 legs with no software-era machinery. (MoeGo's own before-state description — "whiteboards or from memory… group assignments didn't carry between days" — documents exactly this practice.)
- **Recurring schedules**: software makes multi-year recurring booking easy (KennelBooker 3-year horizon), but the standing weekly attendance pattern is a paper-era concept (standing booking cards); recurring is Common, not definitional.
- **Regional**: UK daycare under AAL 2018 licensing orientation (KennelBooker); multi-currency; non-US regimes fit without US-specific machinery in the core.
- Conclusion: the L0 definition is era-, region-, and deployment-neutral. Online booking, portals, evaluation icons, auto-rollover, and report-card automation are era machinery and stay out of the core.

## Uncertainties

- Revelation Pets capacity machinery is documented only as "occupancy" on feature pages; ProPet's capacity documentation is via the combined module (Kennel View). The capacity invariant is held at 5/5 but with thinner documentation for these two products.
- Recurring schedules observed directly at 3/5 (KennelBooker, Revelation Pets, ProPet) plus Gingr memberships; not observed at MoeGo on fetched pages. Held Common.
- Playgroup machinery observed at 3/5 directly (MoeGo Tier 1, Gingr icon, KennelBooker play areas) plus ProPet's buddy/enemy list as adjacent behavior-grouping; not surfaced at Revelation Pets. Held Common.
- Evaluation gates observed at 4/5 (Gingr and MoeGo Tier 1; KennelBooker and ProPet Tier 2); not surfaced at Revelation Pets. Held Common with a daycare-characteristic note.
- Exact reservation/attendance state vocabularies vary (Gingr: expected/checked-in/checked-out; MoeGo: pet status on home page; ProPet: pending; KennelBooker: booking → paid). No universal state taxonomy asserted.
- No numeric rules (capacity defaults, fee amounts, package sizes, evaluation validity) asserted; vendor-quoted examples kept as quotes.
- PetExec daycare mechanics beyond the boarding-page cross-charge remain unverified (404 + JS docs).
- Cat/small-animal daycare exists in-market (testimonial mention "caring for our dogs and cats"; MoeGo pet-type eligibility includes cat) but no dedicated small-animal daycare product was sampled; species scope held as a variant axis on thin evidence.

## Final Synthesis

Pet Daycare Management is the operator-side service system of record for businesses that provide same-day care for client-owned animals in a facility. Its world model: a **client-owned pet** (custody retained; the animal goes home the same day) books — or walks in for — a **daycare attendance**, the same-day unit of work that advances drop-off → care day → pick-up; the attendance consumes one of the facility's **limited daily attendance slots** (location headcount, per-date limits, capacity groups, play-area/room capacities — the overbooking guard); and the attendance resolves into **per-attendance billing** (day/half-day/hourly rates, packages of days, memberships, late pick-up fees, add-ons → payment at pick-up or prepaid credits). Around this core, mature products add: walk-in quick check-in, recurring attendance schedules, playgroup organization with per-group capacity, temperament evaluation gates, vaccination records with expiry gating, daily care execution capture (feeding/medication), report cards and photo updates, packages/credits/memberships, waitlists, waivers, online booking/portal, and reminders. The Type's sharpest boundary is against Pet Boarding Management (same-day attendance vs the overnight stay consuming accommodation capacity — the joint-review flag discharged, keep-both ratified), against Pet Care Business Management (the umbrella scope over the same population), and against the children's Daycare/Preschool Management Type (a naming collision, not a shared structure).
