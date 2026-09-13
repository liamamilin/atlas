# Pet Care Business Management

## Overview

A **Pet Care Business Management** application is the operator-side system of record for a pet-care company — the software a pet-care facility runs its entire business in: client and pet records, booking across all of the business's service lines (typically daycare, boarding, grooming, and training), staff coordination, and billing.

It solves a specific problem: a pet-care business sells several different kinds of services through one front desk, to the same clients, often in a single visit (a dog dropped off for a week of boarding may also get a groom, attend daycare, and its owner buys food at pickup). Without a shared system, each service line keeps its own calendar, its own client list, and its own till, and nothing reconciles. This Type exists precisely at whole-business scope: one client account, one schedule, and one money loop spanning every service line.

The defining core is small:

```text
Client account with pets
└── Multi-service-line booking on one shared schedule
    └── Cross-line billing resolving on the client account
```

Everything else commonly associated with these products — online booking, customer portals, report cards, vaccination reminders, payroll, retail, marketing — is widespread in current products but not part of what makes the Type. Older desktop-era kennel software held the same client, pet, booking, and billing records with none of it.

## Users & Context

Primary users, all inside the business:

- **Front-desk / reception staff** — create and modify bookings, check pets in and out, answer "is there room next weekend", take payment, close invoices. This role touches every service line in a single shift.
- **Service providers** — groomers, trainers, daycare attendants, kennel staff. They work from the schedule they are assigned and record what happened during service (a completed groom, a feeding, a medication given, a report card).
- **Owner / manager** — configures the service catalog and pricing rules, manages staff schedules and permissions, watches occupancy and revenue reports.

Secondary participants:

- **Pet parents (clients)** — through a self-service surface (online booking page, portal, or mobile app) they request bookings, sign agreements, upload vaccination records, pay, and receive updates. They never operate the system of record.
- **Accountants / bookkeepers** — reached indirectly through accounting exports and end-of-period reports.

The work environment is a facility front desk plus the floor: a persistent "today" view of who is arriving, who is leaving, who is in the building, and how full the facility is, used continuously through the day.

## Core Model

### The Defining Core

Three structures, held jointly:

**1. The client account with pets.** Every customer is an identified owner account holding one or more animal sub-records. The pet record carries the care data the business needs before and during service — vaccination status, medications, feeding instructions, temperament notes, veterinarian contact — and the account accumulates the relationship: past and upcoming bookings across every service line, notes, prepaid value (packages, credits, deposits), and communication history. The pet is a first-class record, not a text field on a contact: it is the thing that gets booked, checked in, cared for, and billed. Without the animals and their care semantics, this is just a CRM.

**2. Multi-service-line booking on one shared schedule.** The business's services are booked as dated commitments for specific pets. Different lines take different shapes, and mature products model them distinctly:

```text
Daycare      → a day's attendance, counted against a capacity limit
Boarding     → a dated stay (drop-off → board → pick-up), occupying lodging
Grooming     → an appointment at a time, with a specific groomer
Training     → a series of pre-scheduled class sessions, enrolled per pet
```

What makes the Type is that these live in **one** scheduling surface and hang off **one** client account. A single visit can mix lines — a boarding stay that includes a grooming appointment, a daycare day with a training class. Remove the multi-line scope and what remains is a single-line system: the territory of the sibling Types (boarding management, daycare management, grooming management, training management).

**3. Cross-line billing resolving on the client account.** Charges from every line — stay charges, appointment services, class enrollment, add-on services during a stay, retail items — accumulate on the client's account and resolve into invoices and payments. Prepaid forms are part of the same loop: packages and credit bundles are sold, held on the account, and deducted as services are used; deposits are taken at booking; store credit and gift certificates redeem at checkout. Without this, the system is a schedule board with no money in it.

The three stand or fall together:

```text
client/pet records alone                          → a client/pet CRM
booking without client records                    → an anonymous booking calendar
billing without records and bookings              → an invoicing shell
records + booking without consolidated billing    → a schedule board
```

### Standard Capabilities of Mature Products

These are common across the researched sample and expected by the market, but they are additions to the core, not the definition:

- **Staff management** — staff user accounts with roles and permissions; specialist schedules for groomers and trainers; deeper products add time clocks, commissions, and payroll.
- **Service-delivery records** — what happened during the service: report cards with photos and activity notes sent to owners, feeding and medication task logs, playgroup or group assignments, add-on services recorded against a stay.
- **Vaccination machinery** — vaccine records stored on the pet, expiration tracked, reminders sent automatically; eligibility for service commonly gated on vaccine currency (some products block booking, others alert and verify at check-in).
- **Client self-service** — an online booking page (requests often confirmed by staff before they hit the calendar), a customer portal or mobile app for booking, forms, payment, and updates; digital intake forms and signed agreements.
- **Communications** — automated booking confirmations and reminders by email/SMS, two-way texting, review requests, marketing campaigns.
- **Pricing machinery** — pricing rules that adjust the bill: peak-date charges, late pick-up / early drop-off fees, extended-stay thresholds, discounts and promotions.
- **Retail / POS** — product sales with inventory, sold at the front desk or added to a visit's bill. Present in most products; notably absent from at least one current platform's live feature set, which confirms it is optional.
- **Reporting** — occupancy, arrivals/departures, revenue, sales by service, staff performance; accounting exports (QuickBooks/Xero) and integrated payment processing.
- **Multi-location support** — several facilities under one account, per-location settings, cross-location views; an enterprise/franchise tier capability.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  client account with pets
Realized as:  owner + animal records, client & pet profiles, pet and client manager

Concept:  multi-line booking
Realized as:  reservations + appointments + group classes (three booking types),
              per-line modules sharing one calendar, one appointment book across industries

Concept:  cross-line billing
Realized as:  a cart/invoice aggregating stay + appointment + retail charges,
              account-level credits and packages deducted at checkout
```

A reader who has only seen one product should still be able to recognize any other from the core.

## How It Works

### Configure the business

```text
Define service lines and the service catalog (services, durations, rates)
→ set pricing rules (peak dates, late fees, discounts)
→ set up resources (lodging/areas and capacity limits where boarding/daycare exist;
   specialist working hours where appointments exist)
→ set hours of operation and pick-up/drop-off windows
→ add staff accounts and permissions
→ configure intake forms, agreements, and vaccine requirements
```

### Book

```text
Front desk creates a booking (or client self-books online)
→ select client and pet, service line, dates/time, resources
→ system checks capacity/lodging availability and vaccine currency
→ deposit taken where required; confirmation sent
→ online requests typically land as pending until staff confirm
```

### Check in

```text
Pet arrives (scheduled or walk-in — walk-ins can be checked in without a booking)
→ verify vaccinations, forms, belongings, medications
→ check-in logged; per-pet care card/instructions available to floor staff
```

### During service

```text
Staff log care as it happens: feeding, medication, walks, play groups, activity notes
→ photos and report cards sent to the owner before pickup
→ additional services added to the visit as they are delivered
```

### Check out and settle

```text
Check-out logged
→ all charges from the visit — stay, appointments, classes, add-ons, retail —
  assemble on the client's invoice
→ pricing rules applied; packages/credits/store credit deducted
→ payment taken; receipt issued; records filed to the account
→ accounting export / end-of-day reconciliation
```

### Run the back office

```text
Staff schedules and (in deeper products) payroll and commissions
→ occupancy, revenue, and service-mix reports
→ reminder and marketing cycles; review requests
→ vaccine-expiry and rebooking prompts to lapsed clients
```

The interaction loop that defines daily use is the front-desk cycle: **today's view → book → check in → care → check out → settle**, repeated across every service line from one login.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Today / dashboard

The operational home screen.

- typical information: arrivals, departures, expected, currently in-care counts, capacity/occupancy, today's schedule across all lines, pending online bookings, messages
- primary actions: check in, check out, create a booking, sell retail, send updates

### Booking calendars

The scheduling surface, with per-line views over one dataset.

- a stay/boarding calendar (often drag-and-drop, showing occupancy), an appointment book organized by day/week/staff member, class rosters
- primary actions: create/move/cancel bookings, block availability, view pet records from the calendar

### Client and pet profiles

The record-of-record surfaces.

- client: contact details, pets, booking history, invoices, credits/packages, notes
- pet: care data (vaccinations, medications, temperament, veterinarian), photos, booking history
- primary actions: edit, book, take payment, add notes, message

### Lodging / capacity view (where boarding or daycare exists)

A floor-level board of units/areas and their occupants or a capacity counter.

- typical information: which pet is where, vacancy, date-by-date capacity
- primary actions: assign/move pets between units, split assignments across stays

### Point of sale / invoice

The money surface.

- typical information: open line items from all of a visit's services plus retail, discounts, prepaid value
- primary actions: add items, apply credits/packages, take payment, print/receipt, export

### Task management (in care-heavy operations)

A worklist of care tasks (feeding, medication, walks) assigned to staff with completion logging.

### Reports and settings

- reports: occupancy, revenue, sales by service, staff performance, vaccine status, arrivals/departures
- settings: services and pricing rules, staff and permissions, locations, taxes, forms, integrations

### Client-facing surfaces

- online booking page (branded, embedded on the business's website)
- customer portal / mobile app: book, pay, sign forms, upload vaccine records, receive report cards and updates, message the business

## Important Rules / Behaviors

### Capacity is a binding constraint

Daycare attendance and boarding stays consume limited capacity (aggregate limits or individual lodging units), often set per date. Bookings beyond capacity are refused or waitlisted. This is the overbooking guard of the whole Type.

### Vaccine currency gates service

A pet whose vaccinations are expired or unrecorded is commonly blocked from booking or flagged for verification at check-in. The enforcement style varies by product (hard block vs alert-and-verify); the gate itself is structural because the business carries legal and safety exposure.

### Online bookings are requests until confirmed

Self-service bookings commonly land as pending and enter the calendar only after staff approval, keeping control of capacity and eligibility with the business.

### One account, many charges

Charges from different service lines and retail accumulate on a single client account and settle together. A visit that mixes lines produces one bill, not one bill per line. Prepaid value (packages, credits, deposits) lives on the account and deducts at checkout.

### Pricing rules adjust the bill automatically

Peak-date charges, late pick-up / early drop-off fees, and extended-stay thresholds are computed by rule, not typed by hand; estimates can be generated before service to verify what a booking will cost.

### Walk-ins and exceptions

Pets can be checked in without a prior booking; stays can be extended or cut short; assignments can be split across units; services can be added mid-stay. The system of record absorbs the messiness of live animal care rather than assuming clean plans.

### Custody stays with the owner

Animals enter by client booking and return home; the outcome of every service is return-to-owner. There are no placement or transfer outcomes here — that is the shelter/adoption territory next door.

## Variants

Common shapes of the same Type:

- **Pet resort / multi-line facility** — boarding + daycare + grooming + training (+ retail) under one roof; the fullest expression of the Type.
- **Daycare-first facility** — capacity-driven daily attendance with boarding as a secondary line.
- **Grooming-led business** — appointment-book-centric; may extend into daycare (a common growth path); mobile-grooming variants add van/route scheduling.
- **Kennel / cattery** — boarding-centric, sometimes species-specific (cattery vocabulary in UK/EU markets).
- **Training facility** — class-series enrollment as the dominant line.
- **Scale variants** — solo operator → single facility → multi-location/franchise/enterprise with cross-location reporting and restricted staff views.
- **Deployment variants** — cloud SaaS is the current norm; installed desktop systems held the same core in earlier generations and still exist in the market's history.

A variant remains a variant unless it changes the core: a single-line deployment of one of these products is better understood through its sibling Type; a consumer marketplace for pet services is a different Type entirely.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Pet Boarding Management | single-line sibling | the boarding-specific core (stay + lodging inventory + per-stay billing) viewed alone; this Type adds the other lines and the cross-line account/billing |
| Pet Daycare Management | single-line sibling | same-day capacity care as the core; here daycare is one line among several |
| Pet Grooming Management | single-line sibling | the appointment-book core for grooming; here grooming is one line among several |
| Pet Training Management | single-line sibling | class-series enrollment as the core; here training is one line among several |
| Salon Management System | structural analog (human clients) | same skeleton (appointment book, staff, POS) but clients are people and there are no animal records, care data, lodging, or vaccine gates |
| Appointment-based Service Business Management | generic skeleton | the shared appointment-business pattern without pet-care trade semantics |
| Veterinary Practice Management | adjacent (both hold client+patient records and bill) | vet is clinical care (medical records, diagnoses, prescriptions); this Type is non-clinical service with business administration at the center; a "veterinarian" field here is a contact, not clinical functionality |
| Dog Walking Platform / Pet Sitting Platform | consumer-side neighbors | two-sided matching of strangers (provider profiles, owner discovery) vs operator-side administration of a business's own clients and staff |
| Pet Adoption Platform / Animal Shelter Management | custody-boundary neighbor | intake and placement outcomes (custody transfers) vs paid service with return-to-owner outcomes |
| Retail POS | module relationship | retail exists here as one charge type on the service account, not the core transaction |

The most important boundary is the one against the single-line siblings: this leaf and its siblings describe the same product population at different scope cuts. The test is scope, not features — remove the multi-line whole-business scope and the remaining core is a sibling Type; add sibling lines to a single-line core and the whole-business Type reappears.

## Representative Products

- **Gingr** — cloud multi-line suite (boarding, daycare, grooming, training, dog park) with deep front-desk workflow; SMB to enterprise/multi-location (US)
- **ProPet Software** — modular cloud suite (boarding, daycare, grooming, training, retail); founder-owned, kennel-operator origins (Canada)
- **Revelation Pets** — deliberately simple multi-line pet-care software for small businesses (kennel, daycare, cattery, grooming)
- **DaySmart Pet (123Pet)** — grooming-led pet business software serving grooming, daycare, boarding, and mobile grooming; solo to high-volume salons (US)
- **MoeGo** — mobile-first platform for grooming, boarding, and daycare; solo to franchise/enterprise

The definition was checked against the desktop-era multi-line kennel generation (carried evidence via current vendors' official data-migration documentation) to avoid over-fitting to today's cloud/portal pattern.

## Sources

Research date: **2026-09-09**

- Gingr — https://www.gingrapp.com/ ; Help Center: https://support.gingrapp.com/hc/en-us (sections: Owners and Animals; Reservations, Appointments, and Group Classes; During the Stay and Departure; Retail, Purchases, and Order Management; Staff & Specialist Account Management; Facility Management; Prices and Pricing Rules)
- ProPet Software — https://www.propetware.com/ (module and feature pages)
- Revelation Pets — https://www.revelationpets.com/ ; https://www.revelationpets.com/features ; https://www.revelationpets.com/faq
- DaySmart Pet (123Pet) — https://www.daysmart.com/pet/ ; https://www.daysmart.com/pet/solution/operations/ ; https://www.daysmart.com/pet/solution/scheduling-software/
- MoeGo — https://www.moego.pet/ ; Help Center: https://www.moego.pet/help/en (collections: Boarding & Daycare; Client & Pet)

> Sourcing limitations: ProPet's primary domain (www.propetsoftware.com) was unreachable; the same vendor was reached at propetware.com, so its evidence is product-page depth rather than help-center depth. PetExec and PetLinx could not be reached (limitation carried from the earlier pet-boarding research pass). Revelation Pets and DaySmart Pet evidence is feature-page depth. Precise numeric limits, default settings, and internal state names are intentionally not stated in this document; detailed observations are recorded in the paired Research Notes.
