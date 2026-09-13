# Pet Boarding Management

## Overview

A **Pet Boarding Management** application is the operator-side system of record for a business that boards client-owned animals overnight in its own accommodation — boarding kennels, catteries, pet hotels, and the boarding lines of pet-care facilities. It manages the full service cycle of each stay: the client books a dated reservation, the animal is checked in, housed in a kennel, run, or suite from a limited accommodation inventory, cared for daily according to the owner's instructions, checked out, and billed for the stay.

The defining core is small:

```text
Client-owned pet (custody stays with the owner; the animal goes home)
└── Boarding reservation / stay (dated unit of work: drop-off → board → pick-up)
    └── occupies a place in a capacity-limited accommodation inventory
        └── resolves into per-stay billing (rate × duration + add-ons → payment)
```

Everything else commonly associated with modern boarding software — online booking portals, vaccination gating, report cards with photos, deposits and packages, peak-season pricing — is widespread in current products but is not what makes the product a boarding system. Older desktop-era and paper-era kennel operations ran the same four-part core with a diary, a kennel board, and handwritten run cards.

The custody model is the Type's anchor: the owner retains custody throughout, and the only outcome of a stay is the animal going home. When custody instead transfers to the organization and the outcome is placement, the software is a different Type (Animal Shelter Management).

## Users & Context

Primary users are the staff of the boarding business:

- **front-desk / reception staff** — take bookings, check pets in and out, take payment, answer owner questions
- **care/kennel attendants** — execute daily care: feeding, medication, exercise, cleaning; work from run cards or on-screen care lists
- **manager / owner-operator** — sets prices, capacity, service catalog, and vaccination rules; watches occupancy and revenue

Secondary users:

- **pet owners (clients)** — book stays through a portal or online booking page, upload vaccination records, sign agreements, pay deposits and invoices, and receive updates during the stay

The work environment is a facility with physical accommodation units and a front desk. The software's daily rhythm follows the facility's day: a morning arrivals list, an on-site population during the day, an evening feeding/medication round, and a departures list. Peak periods (holidays, summer) are the operational stress the capacity machinery exists for.

## Core Model

### The Defining Core

**The client-owned pet.** The animal is held as an individual record under an owner/client account. The record carries what care requires: species/breed/age, weight, veterinarian, feeding instructions (food types, amounts, schedules), medication schedules, temperament and behavior flags, and vaccination records. The pet — not the owner — is what the stay is for; multi-pet households book several pets onto one owner account.

**The boarding reservation (stay).** The unit of work. A reservation binds one pet (or a sharing group) to a date span — drop-off to pick-up — and a service type. It is created before arrival (online request, phone, walk-in) and advances through a lifecycle: requested/confirmed → checked in → boarding → checked out. Everything else hangs off it: the assigned accommodation, care instructions for this stay, add-on services, belongings logged at arrival, and the charges that accumulate. In mature products the reservation is the object staff work from all day.

**The accommodation inventory.** The facility's placement structure: kennels, runs, pens, crates, suites, or cattery units, usually organized into rooms, areas, or buildings, each with a capacity. Occupancy is the binding constraint of the business — a full kennel cannot take another dog, which is what makes boarding scheduling different from ordinary appointment booking. Products realize the inventory in two ways: as named units that a reservation is assigned to, or — for cage-free facilities that do not use enclosures — as aggregate capacity limits (per day, per reservation type). Both forms exist in the sample; the invariant is limited placement capacity that stays consume, not enclosures as such.

**Per-stay billing.** The stay resolves into money. Rates are applied over the stay's duration — charged by night, by day, or by 24-hour period depending on the business — plus add-on services (walks, baths, play sessions), fees (late checkout, cancellation), and adjustments (multi-pet or sharing discounts, peak-season rates). Deposits, prepaid packages, and account credit are common pre-payment forms; the balance is invoiced and paid at or after checkout. The system is the authority for what each stay costs.

### Standard Capabilities of Mature Products

These are widespread across current products but do not define the Type:

- **Owner portal / online booking** — clients self-register, request stays, upload vaccination records, sign agreements, pay deposits, and buy packages
- **Vaccination records with expiry tracking** — the most characteristic eligibility gate of the Type; enforcement strictness varies (see Rules)
- **Care instruction capture** — feeding schedules, medication schedules, temperament flags, veterinarian, dietary and medical notes on the pet record
- **Daily care execution** — run cards / kennel cards / scorecards (printed at check-in or on-screen) listing each boarded pet's feeding, medication, and exercise instructions; staff log feedings, medications, walks, and toilet breaks against the stay
- **Check-in / check-out cockpit** — a daily view of arrivals, departures, on-site pets, and occupancy; one-click check-in/out; belongings logged at arrival
- **Add-on services** — attachable at booking or during the stay, billed with the stay
- **Deposits, packages, account credit, waitlists** — the commercial machinery around scarce peak capacity
- **Confirmations and reminders** — email/SMS before arrival
- **Agreements and waivers** — digital signing, sometimes gating self-service booking
- **Pricing rules** — peak/holiday rates, sharing and multi-pet discounts, late-checkout and cancellation fees
- **Owner communication during the stay** — report cards, photos, updates
- **Reports** — occupancy, arrivals/departures, sales, feedings, vaccinations due
- **Retail / product sales** — food, toys, sundries, often with POS hardware (bundle-dependent)

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  accommodation inventory
Realizations:  named kennels/runs/suites in rooms or areas · aggregate capacity limits (cage-free) · room-count tiers

Concept:  the stay's charge
Realizations:  per-night rate · per-day rate · 24-hour-period rate · package credits · account balance

Concept:  care instructions
Realizations:  printed run/kennel cards · on-screen scorecards · daily care reports · activity logs
```

A reader who has only seen one implementation should still recognize the others from the core model.

## How It Works

### Book a stay

```text
Owner requests dates (portal / phone / walk-in)
→ system checks capacity for those nights
→ reservation created (confirmed, or held pending deposit/assessment)
→ deposit or package payment commonly taken
→ confirmation and pre-arrival reminders sent
```

Capacity is checked against the accommodation inventory for every night of the span. When no unit is free, the request is refused or waitlisted; some products can split a booking across multiple runs to fit peak demand.

### Check in

```text
Pet arrives
→ staff verify eligibility (vaccinations current, agreements signed)
→ belongings logged
→ accommodation unit assigned
→ run card / kennel card produced with this pet's care instructions
→ reservation state: boarding
```

Check-in is the moment the facility takes the animal into its care for the span. Products differ on how hard the vaccination gate bites (see Rules), but all keep the vaccination state visible at this moment.

### Board (the daily loop)

```text
Each day: feed / medicate / exercise / clean per the pet's instructions
→ staff record feedings, medications, walks, toilet breaks against the stay
→ add-on services performed and charged
→ updates (notes, photos) sent to the owner
→ incidents, if any, documented
```

This loop is the operational heart that distinguishes boarding from pure booking software: the system's daily reports tell staff which pet gets what, when.

### Check out and settle

```text
Owner arrives
→ stay closed; charges totaled (rate × duration + add-ons + fees − discounts)
→ package credits or account balance applied, or invoice presented
→ payment taken (card on file, terminal, online)
→ receipt issued; animal returned to owner
```

The outcome of every stay is the same: the animal goes home and the stay becomes a paid transaction on the client's account history.

### Core vs Common vs Optional

**Defining core** — without these, not boarding management:

- client-owned pet record with care data
- boarding reservation/stay as the dated unit of work
- capacity-limited accommodation inventory the stay occupies
- per-stay billing resolving into payment

**Standard capabilities** — present in most modern products:

- owner portal / online booking
- vaccination records with expiry gating
- care execution capture (run cards, activity logs)
- check-in/check-out cockpit
- add-on services, deposits, packages, credit, waitlists
- reminders, agreements/waivers, pricing rules
- owner updates (report cards/photos), reports, retail

**Optional / variant** — depends on business shape:

- grooming, daycare, training, retail lines beside boarding
- cameras / live view of pets
- incident-report modules
- regulatory compliance packs (licensing regimes)
- multi-location management

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Daily dashboard / cockpit

The operator's home surface: today's arrivals, departures, on-site pets, and occupancy at a glance. Primary actions: check a pet in or out, search records, print boarding/run cards, message customers.

### Boarding calendar / lodging calendar

The capacity surface: days across the accommodation inventory, showing which units are occupied, which are open, and what is arriving. Primary actions: create or move reservations, read occupancy, spot peak pressure. This is where overbooking is prevented.

### Reservation detail

The stay's record: pet, owner, dates, assigned unit, service type, status, care notes for the stay, add-on services, belongings, charges, payment state. Primary actions: edit dates, assign accommodation, add services, check in, check out, take payment.

### Pet profile

The care record: details, vaccinations with expiry dates, feeding and medication schedules, temperament flags, veterinarian, incident history, stay history, photos. Primary actions: update care instructions, record vaccinations, view history.

### Client/owner account

The commercial record: contact details, pets, agreements, packages and credit balance, stay and payment history. Primary actions: book, pay, view invoices.

### Owner portal / booking page

The client-facing surface: live availability, stay requests, vaccination uploads, agreement signing, deposits and payments, and (in some products) updates and photos during the stay.

### Run card / kennel card

The care-execution surface, printed or on-screen: the individual boarded pet's feeding instructions, medications, and notes — everything an attendant needs before opening a run.

## Important Rules / Behaviors

### Occupancy is a hard constraint

A stay cannot be confirmed beyond the accommodation inventory's capacity for its nights. Products enforce this automatically (online booking shows "unavailable" when full) and typically allow staff overrides such as double-booking or split bookings across runs — the override is a deliberate operator decision, not a default.

### Vaccination eligibility gates the stay

Boarding is the Application Type where vaccination state is a first-class operational rule: records carry expiry dates, the system flags missing or expired vaccinations, and enforcement strictness varies by product — some block an online booking request outright until records are current; others admit the booking but alert staff to verify at check-in. Some facilities also exclude entire categories of animal (for example, un-neutered pets) by policy.

### The reservation spans check-in to check-out

The stay is one continuous unit of work: charges accrue against it, care is logged against it, and closing it (check-out) is what triggers final billing. A pet checked in without a prior reservation is a normal exception — staff create the reservation on the spot.

### Care instructions come from the owner, execution is the facility's

The pet cannot self-describe. Feeding, medication, and handling instructions are captured from the owner onto the pet record and become the staff's daily work list. Medication administration in particular is treated as a safety-relevant act — products emphasize giving the right medication to the right pet.

### Money rules shape bookings

Deposits (commonly required to hold peak-season dates), cancellation fees, late-checkout fees, and package credits all modify the basic rate × duration calculation. Waitlists release capacity when cancellations arrive.

### Custody never transfers

Unlike shelter software, nothing in the boarding model ends with a placement outcome. The stay ends; the animal returns to the owner. This single rule separates the Type from its closest structural neighbor.

## Variants

- **Boarding-only kennel / cattery** — the classic single-line business; species-specific (dog kennel, cattery) or mixed, with unit types per species
- **Combined pet-care facility** — boarding plus daycare, grooming, training, and retail in one system; the most common modern shape; boarding and daycare share the calendar, and in some products daycare charges can be added to a boarding stay's bill
- **Cage-free operation** — no enclosures; capacity limits replace named units
- **Luxury pet hotel** — suites, add-on menus, heavy owner-communication (photos, updates)
- **Board & train** — boarding combined with a training program
- **Regional regulatory shapes** — licensing regimes (for example UK animal-activity licensing) add record-keeping and inspection-reporting expectations; US county/state kennel licensing similar
- **Deployment generations** — cloud SaaS today; a prior Windows-desktop generation (local database, no online booking) ran the same core and its data still migrates into current products
- **Scale** — single site vs multi-location/multi-building operators

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Animal Shelter Management | closest operational neighbor | shelter = custody transfer (intake by surrender/stray, outcomes are placements); boarding = owner-retained custody, outcome is always return-to-owner, money flows as per-stay billing. Shelter vendors themselves ship boarding as a separate module |
| Pet Daycare Management | sibling in the same product population | daycare = same-day care without overnight accommodation consumption; boarding = the overnight stay that occupies a unit. Products bundle both; the overnight stay is the seam |
| Veterinary Practice Management | adjacent | clinical business (appointments, procedures, medical records); boarding products store the veterinarian as a data field, never the clinical workflow |
| Pet Sitting Platform / Dog Walking Platform | adjacent | care without a facility accommodation inventory (in the pet's home or caregiver's home); some products sell sitting/walking as separate service lines beside boarding |
| Hotel PMS | structural rhyme | same reservation → room/unit → stay → folio skeleton, but the guest is an animal: care execution (feeding/medication/exercise) replaces housekeeping, the owner supplies the "guest requirements", and eligibility is vaccination/behavior-based |
| Pet Care Business Management | umbrella sibling | the same product population viewed at whole-business scope (boarding + daycare + grooming + training + retail); boarding management is the boarding-specific core within it |
| Appointment Scheduling Application | generic neighbor | staff-calendar scheduling without accommodation inventory, care execution, or per-stay rate × duration billing |

## Representative Products

- **Gingr** — US market-leading multi-service pet-care SaaS; boarding, daycare, grooming, training, dog park; enterprise tier
- **PetExec** — established US boarding/daycare SaaS (now part of the Gingr/TogetherWork family, operated separately)
- **Revelation Pets** — budget-friendly SaaS aimed at small kennels and catteries
- **ProPet** — Canadian founder-owned all-in-one (boarding, daycare, grooming, training, retail)
- **KennelBooker** — UK-origin booking-first platform with international reach and a licensing-compliance orientation

The core model was checked against the legacy desktop generation (documented through current vendors' official migration programs for ceased-trading desktop kennel software) and against paper-era kennel practice, to avoid defining the Type by today's cloud/portal implementation.

## Sources

Research date: **2026-09-09**

- Gingr — https://www.gingrapp.com/ , https://www.gingrapp.com/kennel-software , help center: https://support.gingrapp.com/hc/en-us (Owners and Animals; Facility Management — Areas & Lodging, Capacity Limits, Run Cards; Reservations; Check-In; During the Stay and Departure; Feeding; Check Out)
- PetExec — https://www.petexec.net/ , https://www.petexec.net/service/boarders , https://docs.petexec.net/
- Revelation Pets — https://www.revelationpets.com/ , https://www.revelationpets.com/kennel-software , https://www.revelationpets.com/features
- ProPet — https://www.propetware.com/ , https://www.propetware.com/boarding-kennel-daycare-software/
- KennelBooker — https://www.kennelbooker.com/ , https://www.kennelbooker.com/boarding , https://www.kennelbooker.com/kennelsuite-alternative

> Sourcing limitations: PetExec's documentation center is a JavaScript application whose article content could not be fetched; PetExec observations are product-page level. A desktop-generation vendor (PetLinx) was unreachable after repeated attempts; the legacy generation is instead documented through KennelBooker's official migration pages for ceased-trading desktop kennel software. Precise operational numbers (deposit percentages, cancellation windows, vaccination validity defaults, capacity defaults) were not researched at documentation depth and are intentionally not stated. Detailed evidence, product-by-product observations, and the cross-product comparison matrix are recorded in the paired Research Notes.
