# Pet Health Application

## Overview

A **Pet Health Application** is the caretaker-facing application of record for an individual animal's health. The pet's owner (or another caretaker) holds, in one place, a persistent profile of the animal, a longitudinal record of its health state, and the working loop that turns that record into day-to-day care: what is due, what has been done, and what the veterinarian needs to know.

The defining core is small:

```text
Animal profile of record
└── Caretaker-maintained longitudinal health record
    └── Active care loop (due states, reminders, provider handoff)
```

Everything else commonly associated with these products — multi-pet households, family sharing, appointment booking, expense tracking, wearable-derived data, telehealth access, community features — is widespread in current products but is not what makes the product a pet health application. The paper vaccination booklet held by an owner, consulted before care decisions and handed to the vet, satisfies the same core without any of the modern machinery.

When the center of gravity shifts — to the clinic's own clinical and billing system, to a laboratory test cycle, to an insurance policy and claims, or to live location tracking — the product has drifted toward a different Application Type.

## Users & Context

The primary user is a **pet owner or caretaker** — the person responsible for an animal's day-to-day health. The work is personal and domestic: giving medication on schedule, keeping vaccinations current, watching weight and behavior, preparing for vet visits.

Typical reasons to open the application:

- record something that just happened (a dose given, a symptom noticed, a vet visit, a weight measurement)
- check what care is due (next vaccination, next deworming, next dose, next grooming)
- look up the animal's history before or during a vet visit, and share it
- track a trend (weight, behavior, measurements) over weeks or months

Secondary users include **other household members** who share care of the same animal (many products give each person their own account with access to the pet), and — at one remove — **veterinarians and other care providers**, who receive the record or, in some products, author parts of it. The context is overwhelmingly mobile: the record is kept where the animal is.

## Core Model

### The Defining Core

```text
Animal profile of record
└── Caretaker-maintained longitudinal health record
    └── Active care loop (due states, reminders, provider handoff)
```

Three properties. If any one is removed, the product is no longer recognizable as a pet health application:

- **Animal profile of record** — an identified individual animal (not a person) held as a persistent record: name, species/breed, age or birth date, commonly a weight baseline and photo. Everything else attaches to this record. Without it, the product is a generic journal or a human health tracker.
- **Caretaker-maintained longitudinal health record** — dated entries of the animal's health state accumulating over time: measurements (weight, vitals), care events (medications administered, vaccinations, deworming, treatments, hygiene care, vet visits), observations (behavior, symptoms, incidents with photos and notes), and health documents (vaccination certificates, lab results). Entries are made by the caretaker and/or arrive from providers or devices — but the record is held and controlled in the caretaker's application. Without it, the product is a pet profile card. If the clinic holds the record instead, it is the veterinary record, not this application.
- **Active care loop** — the record is worked, not just stored: recurring care actions are tracked with due states and surfaced (reminders, schedules, alerts, a current-status view), and the record is made usable in care decisions — most commonly by being shareable with a veterinarian or other provider. Without it, the product is a static archive nobody acts on, or a bare reminder app with no health content.

### What Mature Products Commonly Add

These capabilities are near-universal in current products; they make the core practical but do not define the Type:

- **Multi-pet household** — several animal profiles under one caretaker account.
- **Household access** — family members with their own accounts sharing the same animal's record and care duties.
- **Provider handoff** — sharing or exporting the record to a veterinarian or specialist; in some products, inviting a professional to enter data directly.
- **Appointment booking** — requesting or booking visits with providers from inside the application.
- **Trend views** — charts of weight and measurements over time, behavior timelines, normal-range warnings.
- **Calendar sync** — the care schedule reflected into the device's calendars.
- **Sync across devices** — the same record on every household device.

### One Structure, Many Implementations

The core is written conceptually; the same structure is realized differently across the market:

```text
Concept:            who enters the record
Implementations:    caretaker entry (standalone apps),
                    clinic-authored records synced to the owner app,
                    device-derived sensor data,
                    consultation-supported notes

Concept:            the care loop
Implementations:    in-app schedules and dose notifications,
                    clinic-synced service reminders plus owner to-dos,
                    behavior/vital trend alerts,
                    the vet's own recall system (the paper-era form)

Concept:            provider handoff
Implementations:    export/email of records, in-platform sharing,
                    clinic sync, the consultation itself
```

## How It Works

### Set up the animal and the household

```text
Create the animal's profile
→ name, species/breed, age/birth date, weight baseline, photo
→ optionally add family members with access to the same animal
→ optionally connect a provider (clinic) or a device
```

There is no business setup, no service catalog, no billing configuration. The account exists to serve the animal's record.

### Keep the record current

The ongoing interaction loop is entry and accumulation:

```text
Something happens (dose given, symptom seen, visit completed, weight measured)
→ record it as a dated entry on the animal's profile
→ optionally attach photos, notes, or documents
→ the entry joins the animal's history
```

In standalone products the caretaker enters everything. In clinic-anchored products the clinic's system authors the formal record (services, medications, lab results) and it syncs into the owner's app, while the caretaker adds lightweight content (to-dos, notes) and requests actions (refills, appointments). In device-based products the data arrives automatically from the sensor. Most products combine sources.

### Work the care loop

The record drives what happens next:

```text
Recurring care defined (vaccination schedule, medication course, hygiene routine)
→ the application tracks due states
→ reminders surface what is due or overdue
→ the caretaker acts and records completion
→ the next cycle is scheduled
```

The same loop covers one-off attention: measurements outside a normal range, behavior changes, and — in device-based products — sustained changes in activity, sleep, or vitals surfaced as alerts. The loop is what distinguishes a health *application* from a health *archive*.

### Use the record in care decisions

```text
Before or during a vet visit
→ open the animal's history
→ share or show the record (export, email, in-platform share, or clinic sync)
→ the vet works from the complete picture
→ findings come back as new entries
```

### Core vs Common vs Optional

**Defining core** — without these, not a pet health application:

- animal profile of record
- caretaker-maintained longitudinal health record
- active care loop (due states + provider handoff)

**Common mature structure** — present in most modern products:

- multi-pet household, family access
- provider handoff mechanisms, appointment booking
- trend views, calendar sync, device sync

**Variant / optional** — depends on product philosophy and market:

- data-entry substrate (caretaker / clinic-synced / device / consultation)
- expense tracking, community and social layers, telehealth access, medication refill requests, insurance attachments, AI-derived insights and breed comparisons

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Pet list / household home

The entry surface: the user's animals at a glance.

- animal cards with photo, name, age; due-item indicators
- primary actions: open a pet, add a pet, see what's due today

### Animal profile

The record's anchor surface for one animal.

- identity (species/breed, age, weight baseline), current status (medications, conditions, allergies)
- primary actions: edit profile, jump to any record section, share the record

### Health record sections

The longitudinal record, usually organized by kind of content.

- measurements (weight, vitals) with trend charts and normal-range limits
- care events (medications, vaccinations, treatments, hygiene, vet visits) as dated, attributable entries
- documents (vaccination certificates, lab results, x-rays) as attachable, shareable files
- primary actions: add an entry, attach a document, filter history, share

### Care schedule / reminders

The proactive surface.

- upcoming and overdue care items across the household's animals
- primary actions: mark done, reschedule, create a custom care item, sync to calendar

### Sharing / provider connection

The handoff surface.

- share scope (which data, which pet, with whom, for how long in the most granular products), export, provider connections
- primary actions: share history with a vet, request an appointment, request a refill (where offered)

### Settings / privacy

- household members and their access, data-ownership and sharing controls, connected providers and devices

## Important Rules / Behaviors

### The caretaker holds the record

The record lives in the caretaker's application and under the caretaker's control — this is the structural difference from the veterinary record, which the clinic owns and operates. In clinic-anchored products the clinic authors the formal record and the owner app mirrors it; the caretaker's control shows up as sharing scope and to-do authorship rather than record editing.

### No diagnosis authority

These applications record and organize health information; they do not diagnose. Device-based products state this explicitly ("not a medical device; seek veterinary advice"), and the recurring pattern across the Type is: the application surfaces changes and due care, the veterinarian interprets. The record's job is to make the vet's interpretation better informed.

### The care loop is stateful

Care items carry due states (done / due / overdue). Completing one cycle generates the next. In clinic-anchored products the reminder state can be maintained on the clinic side and synced — which means the caretaker may not be able to clear a clinic-set reminder locally; the correction happens at the source.

### Sharing is scoped

Where sharing exists, it is typically selective: which data, of which animal, with whom, and for how long. The record is personal data about a dependant animal, and mature products treat its circulation as a controlled act rather than an all-or-nothing export.

### Multi-source entries must coexist

The same animal's record may hold caretaker entries, clinic-synced records, and device-derived data. Products differ in how they attribute and reconcile these sources; the caretaker-facing record remains the single place where the animal's health picture is assembled.

## Variants

- **Standalone caretaker-maintained tracker** — the caretaker enters everything; richest record-keeping (measurements, care events, documents, expenses); fine-grained sharing with vets and caregivers.
- **Clinic-anchored companion app** — the record is authored in the veterinary clinic's practice system and synced to the owner's app; reminders arrive from the clinic; the caretaker adds to-dos and requests appointments and refills.
- **Device-derived monitoring** — a wearable or collar device captures activity, sleep, and vitals continuously; the application learns the animal's baseline and alerts on sustained changes; explicitly positioned as early-warning, not diagnosis. Often bundled with GPS location tracking, in which case the product's center is location, not health.
- **Telehealth-supported** — on-demand access to licensed veterinarians inside the application; the record supports the consultation. When the consultation is the center, the product is telehealth-shaped rather than record-shaped.
- **Species and market variants** — dog/cat-centric mainstream products; regional forms tied to statutory pet documents (e.g., pet-passport regimes); exotic-animal and multi-species breadth in some products.
- **Household scale** — single-animal apps and multi-pet household managers; the latter is the common modern shape but not the definition.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Veterinary Practice Management | operator-side mirror | the clinic's own clinical-business system of record: client-and-patient records, diagnosis-bearing clinical documentation, client billing. This Type is the caretaker's consumer record with no diagnosis authority and no billing loop |
| Pet DNA Analysis Platform | sibling, shared pet vocabulary | the DNA platform's unit of record is lab-derived genetic findings produced by a kit→lab cycle; this Type tracks the animal's ongoing health state and never runs a lab loop |
| Pet Insurance Customer App | sibling, shared pet vocabulary | binds the pet to a policy of record and a claim-to-money loop anchored to veterinary bills; this Type has records and reminders with no insurance relationship |
| Pet Adoption Platform / Animal Shelter Management | sibling, shared pet vocabulary | placement and custody lifecycles; no ongoing health record at the center |
| Pet-service business systems (grooming, boarding, daycare, training, dog-walking) | adjacent | operator-side service-delivery business systems; this Type is caretaker-side; booking appears here only as a capability |
| Lost Pet Platform | sibling | recorded reunions of lost animals; different unit of record and workflow |
| GPS tracker products | adjacent market | location-centered products (live tracking, escape alerts) that may carry a health-monitoring feature; the center is location, not the health record |
| Pet telehealth products | adjacent market | consultation-centered access to veterinarians; the record supports the consultation rather than the reverse |
| Human health-tracking applications | structural rhyme | same profile + longitudinal-record + trends shape, but the subject is the user's own body; here a human caretaker acts for an animal patient |

The hardest boundary is with **Veterinary Practice Management**, because clinic-anchored companion apps sit directly on the seam: the clinic authors the records, but the caretaker's application holds the consumer-facing record and the care loop. The structural test is who operates the system of record and who holds the diagnosis and billing authority.

## Representative Products

- **11pets** — standalone caretaker-maintained pet care platform (multi-pet, records, schedules, sharing)
- **PetDesk** — clinic-anchored pet-owner companion app synced from the clinic's practice system
- **Tractive** — GPS-first tracker product whose health-monitoring layer illustrates the device-derived pole
- **Airvet** — telehealth-first pet care product (now positioned as an employer benefit), illustrating the consultation pole

The core model was checked against the paper vaccination booklet (the pre-app analog) to avoid over-fitting the definition to the modern cloud, notification-rich implementation.

## Sources

Research date: **2026-09-10**

- 11pets — official site home and features pages: https://www.11pets.com/en/ , https://www.11pets.com/en/feature
- PetDesk — official help center (Pet Records — reminders, prescription & labs; Accessing or Editing Pet Reminder & Prescription Records): https://petdesk.zendesk.com/hc/en-us/sections/360009821334 , https://petdesk.zendesk.com/hc/en-us/articles/360052833813 ; app-store listing and about page
- Tractive — official health-monitoring feature page and FAQ: https://tractive.com/en/fp/health-monitoring-for-dogs-and-cats ; root site https://tractive.com/en/ (whistle.com now redirects to Tractive)
- Airvet — official site root: https://airvet.com/

> Sourcing limitation: no authenticated in-app screens were observed for any product; all state, permission, and workflow descriptions are conceptual. Vendor-stated numeric thresholds and usage statistics were recorded in the Research Notes only and are deliberately absent from this document. Airvet was evidenced at product-page depth only.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical market-sample check are recorded in the paired Research Notes.
