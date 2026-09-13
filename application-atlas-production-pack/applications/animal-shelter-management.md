# Animal Shelter Management

## Overview

An **Animal Shelter Management** application is operator-facing software for organizations that take custody of animals — animal shelters, humane societies, SPCAs, rescue groups, and municipal animal services. Its job is to track each individual animal from the moment it enters the organization's custody, through daily care while in custody, to the outcome that ends custody (adoption, return to owner, transfer to another organization, or death).

The defining structure is small:

```text
Animal Record (individually identified animal)
└── Custody Lifecycle
    ├── Intake (animal enters the organization's custody)
    ├── In Care (custody state with a trackable placement)
    └── Outcome (event that ends custody)
├── Care & Custody Events (dated records attached to the animal)
└── Associated Person Records (the people on the other side of custody events)
```

Everything else commonly associated with shelter software — kennel boards, medical books, adoption applications, foster programs, public adoption listings, microchip registration, licensing, donations — is widespread in mature products but is not what makes the product shelter management. A foster-based rescue with no facility, a municipal impound operation with no public listings, and a large open-adoption shelter all satisfy the same core.

When the dominant surface shifts to consumer-facing discovery of adoptable pets, the product is drifting toward a different Application Type (Pet Adoption Platform). When it shifts to field enforcement (complaints, citations, dispatch), that is the Animal Control overlay — bundled by many products, but a distinct structure.

## Users & Context

The primary users are the staff of an organization that holds animals in custody:

- **Intake / front-desk staff** — receive strays, owner surrenders, returns, and transfers; create or reopen animal records; identify the people involved.
- **Animal care / kennel staff** — move animals between locations and units, log daily observations, carry out feeding and cleaning routines.
- **Veterinary / medical staff** — examine animals, record and schedule vaccinations, tests, treatments, and spay/neuter surgery.
- **Adoption counselors / coordinators** — process adoption applications, meet adopters, complete contracts and fees.
- **Foster coordinators and foster caregivers** — place animals into volunteer homes and track them there.
- **Shelter managers** — oversee occupancy, capacity, statistics, compliance, and reporting.

Secondary users: volunteers (often as restricted system users), transfer-partner organizations, and — in municipal deployments — animal control/field officers. The work environment is facility-based for shelters (kennels, runs, catteries) and home-based for foster-centric rescues; both track the same thing: which animal is in custody, where it is, and what has been done to and for it.

## Core Model

### The Defining Core

Four structures. If any one is removed, the product is no longer recognizable as shelter management:

- **Animal record** — every animal the organization takes in is an individually identified record: name and/or shelter code, species, breed, age, sex, and identifiers such as microchip number. The record persists for the animal's lifetime, including after its outcome, and is the anchor for everything else.
- **Custody lifecycle** — the record moves through **intake** (the animal enters custody, with a reason such as stray, owner surrender, transfer-in, or returned adoption), an **in-care** state (the animal is in custody at a trackable placement — a kennel/unit, a room, a foster home, or an offsite location), and an **outcome** (the event that ends custody: adoption, return to owner, transfer out, release, escape, death, or euthanasia). The lifecycle is the workflow spine of the whole application.
- **Care & custody events** — dated, attributed events attach to the animal while it is in custody: vaccinations, tests, medical treatments, observations and behavior notes, location changes, holds, costs. These events are what staff perform daily and what the organization must be able to account for.
- **Associated person records** — every custody transition has a person on the other side (or a recorded unknown, as with anonymous stray intakes): the finder or surrendering owner at intake, the foster caregiver during placement, the adopter at adoption, the receiving organization at transfer, the reclaiming owner at return. People are also staff, volunteers, and licensing/citation subjects in municipal deployments.

### Capabilities Shared by Mature Products

A typical modern product carries most of these. They are not what makes the product shelter management, but they make it operable:

- **In-care cockpit** — a location/unit board showing every animal currently in custody, grouped by kennel, room, or foster placement, with occupancy and availability visible at a glance.
- **Medical suite** — vaccination, test, and treatment records with due/given dates; outstanding-treatment views; reusable medical templates or profiles applied at intake.
- **Status and flag system** — adoptable, not for adoption, hold (e.g., stray hold awaiting reclaim), quarantine, cruelty case, reserved. Flags control what staff may do with the animal and whether it may be publicly listed.
- **Adoption workflow** — application/reservation capture (multiple applications per animal are normal), coordinator assignment, approval, contract/document generation with electronic signing, fee collection, and receipting.
- **Foster program** — foster homes as placements with capacity, foster books, and return-from-foster handling.
- **Person database** — one record per person with role flags (adopter, foster, volunteer, staff, transfer partner), contact history, and duplicate merging.
- **Public adoption output** — the organization's own adoptable-pet pages and/or automated feeds to third-party adoption portals, driven by the animal's status flags.
- **Photo/media management** — per-animal photos and documents, with a preferred public image.
- **Statistics and reporting** — intake/outcome counts, lengths of stay, occupancy; in the US, standardized aggregation (Asilomar-style categories, national statistics services).
- **Payments** — adoption fees, donations, vouchers; receipts.
- **Role-based permissions** — staff, volunteers, and coordinators see and do different things.
- **Reminders and alerts** — vaccinations due, treatments outstanding, holds expiring, follow-ups pending.

### One Structure, Many Implementations

The core model is conceptual. Products realize it differently:

```text
Concept:          Animal identity
Implementations:  shelter code, animal name, microchip number, tag

Concept:          Placement while in care
Implementations:  kennel/unit inventory (facility shelters), foster home network (rescues), room/location (small operations)

Concept:          Outcome
Implementations:  adoption movement, return-to-owner, transfer, release, death/euthanasia record

Concept:          Adoption application
Implementations:  reservation records, online application forms, portal applications

Concept:          Public listing
Implementations:  self-hosted adoption pages, feeds to national/regional adoption portals
```

A reader who has only seen one implementation (e.g., a cloud SaaS with a kennel board) should still be able to recognize a foster-based rescue system or a municipal impound system from the core model.

## How It Works

### Intake: an animal enters custody

```text
Animal arrives (stray / owner surrender / return / transfer-in)
→ create or reopen the animal record
→ record entry reason, date, and the person who brought the animal (if any)
→ assign an initial placement (unit, room, or foster home)
→ apply intake care package (vaccinations, tests, treatments due)
→ set initial status flags (e.g., hold, not yet available)
```

Returning animals may reopen their existing record rather than creating a duplicate; some products keep an entry history so each stay is recorded separately.

### In care: the daily loop

```text
Staff open the in-care board (by location/unit or foster)
→ move animals as space and health require
→ record daily observations (appetite, behavior, weight)
→ complete due medical items (vaccinations, treatments, tests)
→ update status flags as the animal becomes available
→ publish the animal to the adoption page / portals once eligible
```

The medical side runs on due dates: items fall due, staff complete them, and the system reminds about what is outstanding. Holds and quarantine flags keep an animal invisible to public listing until cleared.

### Outcome: custody ends

```text
Adoption path:
application/reservation received
→ coordinator reviews adopter (and any adoption history warnings)
→ approval, meet-and-greet
→ contract generated and signed, fee collected, receipt issued
→ adoption outcome recorded; animal leaves custody
→ post-adoption: microchip registration to the adopter (where used)

Other outcomes:
return to owner (reclaim) · transfer to another organization · release · escape · death/euthanasia (recorded on the animal record itself)
```

Every way an animal leaves custody is recorded as an outcome event against the animal and the person involved. Death is the exception among outcomes: it is recorded directly on the animal record rather than as a movement, because it can only happen once. A returned adoption re-enters the in-care state and the cycle repeats.

### The custody rule that shapes everything

An animal can only be in one placement at a time. Products model leaving and returning as paired halves of one custody event: sending an animal to a foster home, a retailer, or an adopter ends the current in-care state, and only a return (or a completed outcome) can start a new one. This single rule drives the movement screens, the occupancy board, and the statistics.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### In-care board (shelter view)

The operational home screen.

- every animal currently in custody, grouped by location/unit or foster home
- occupancy and available space; status emblems (hold, quarantine, reserved)
- primary actions: move an animal, open its record, filter by status

### Animal record

The center of the application; a tabbed document per animal.

- identity and description; entry information (reason, date, person); health and identification; current placement and status flags
- care history: vaccinations, tests, treatments, observations, logs, costs, media
- custody history: every placement and outcome, past and current
- primary actions: edit details, add care events, change placement, record an outcome

### Movement / outcome screens

Guided screens for each custody transition.

- pick the animal, pick the person or organization, validate eligibility (e.g., animal not on hold), set dates
- primary actions: adopt, foster, transfer, return, reclaim

### Medical books

Worklists of outstanding care across all animals.

- due vaccinations, tests, and treatments with animal, date, and status
- primary actions: mark given/completed, schedule next, print worklists

### Person records

One record per person the organization touches.

- contact details, role flags (adopter, foster, volunteer, staff), animals linked to this person, payments, documents
- primary actions: find linked animals, record payment, merge duplicates

### Adoption / application screens

The pipeline from application to completed adoption.

- open applications per animal, adopter details, coordinator assignment, approval state
- primary actions: create application, approve, generate contract, collect fee, complete adoption

### Publishing / listing management

Controls what the public sees.

- which animals are listed (status-driven), where (own pages, third-party portals), with which photo and description
- primary actions: include/exclude an animal, choose destination, refresh feeds

### Reports and dashboards

- intake/outcome counts, lengths of stay, occupancy, medical compliance, financial totals
- primary actions: run, filter, export

## Important Rules / Behaviors

### One active placement per animal

An animal cannot be in two placements at once. A new placement requires the previous one to be returned/ended first; products typically enforce or automate this (e.g., fostering an already-fostered animal returns it first).

### Outcomes end custody; death is recorded on the record

Every departure from custody is an outcome event. Death/euthanasia is recorded directly on the animal record (with date and reason) rather than as a movement, and deceased animals drop out of in-care views and public listing while remaining in history and statistics.

### Status flags gate public visibility and actions

Hold, quarantine, cruelty-case, and not-for-adoption flags suppress public listing and can restrict movements. A held animal awaiting reclaim is treated differently from an adoptable one — including for downstream registrations (e.g., microchip registration to a new owner does not apply while a reclaim hold is active).

### Care events drive reminders

Vaccinations, tests, and treatments carry due dates; the system surfaces what is outstanding per animal and across the shelter. Completing one item may generate the next in a series.

### People accumulate history and warnings

A person's history with the organization (previous adoptions, returns, surrendered animals, citations) is visible on their record and can warn staff during adoption decisions. Duplicate person records are merged rather than deleted, preserving linked history.

### Statistics are derived from intake and outcome events

Intake/outcome reporting (including standardized US aggregation) is computed from the custody events themselves — which is why entry dates, outcome types, and return handling are recorded consistently.

### Custody events are historical records

Movements, care events, and outcomes are retained for the animal's lifetime; they are the audit trail for the organization's care of the animal and the basis for compliance and grant reporting.

## Variants

- **Municipal animal services shelter** — impound-centered intake (strays, seizures), legal holds, pet licensing, citations, and often an integrated field/enforcement side (incidents, dispatch). The custody core is unchanged; the overlay adds government structures.
- **Private nonprofit shelter (humane society / SPCA)** — open-adoption focused, with strong adoption workflow, public listing, volunteer and foster programs, and donation/fundraising ties.
- **Foster-based rescue** — no facility; the foster network is the placement structure. Kennel boards are replaced by foster-home capacity views; everything else in the core model applies.
- **Sanctuary / long-term care** — custody without the adoption outcome as the primary goal; care and lifecycle records dominate.
- **Enterprise / multi-site** — multiple locations and chapters with consolidated reporting, APIs, and advanced permissions.
- **Regional regimes** — hold periods, licensing, and statistics differ by jurisdiction (e.g., US standardized intake/outcome aggregation and stray holds; UK voucher and gift-aid features; AU national adoption portals and breeder-registration fields). The core model is region-neutral; these are overlays.
- **Deployment and business model** — cloud SaaS (subscription or per-adoption pricing), self-hosted open source, and legacy on-prem installations all exist; the structure is the same.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Pet Adoption Platform | adjacent, consumer-facing | discovery/listing of adoptable pets for the public; no custody lifecycle — the shelter system is the operator system that feeds it |
| Animal Control Management | adjacent, government overlay | field/enforcement operations (complaints, dispatch, citations, licensing); frequently bundled with shelter management in municipal products, but the shelter core stands alone without it |
| Veterinary Practice Management | adjacent | client-based clinical business (appointments, services, billing for owners); shelter care is custody-based, not client-scheduled |
| Pet Boarding / Kennel Management | adjacent | commercial boarding where the owner retains custody and pays for a service; sheltering transfers custody and ends in outcomes |
| Nonprofit CRM / Donor Management | adjacent, often bundled | donor cultivation, campaigns, and gift processing; shelter products record donations as payments but fundraising is not the core |
| Research Animal Facility Management | related pattern, different Type | custody of animals for research protocols with protocol/compliance lifecycles, not welfare/placement outcomes |
| Kennel / Pet Daycare Management | adjacent | paid short-term care with owner custody retained; no intake/outcome custody lifecycle |

The boundary with **Pet Adoption Platform** is the most important one: the same adoptable-animal data appears in both, but on one side it is an operator's custody record and on the other a consumer's listing. The boundary with **Animal Control Management** is the most frequently blurred in the market, because municipal vendors bundle both; the structural test is field enforcement versus custody operations.

## Representative Products

- **Animal Shelter Manager (ASM3 / sheltermanager.com)** — open source and hosted; international; small-to-medium shelters and rescues
- **PetPoint (24Pet)** — long-standing North American industry-standard platform with a large shelter network
- **Chameleon (24Pet)** — municipal/large-shelter platform combining shelter and field services
- **24PetShelter (24Pet)** — new-generation mobile-first cloud platform
- **RescueGroups.org** — free-tier service suite widely used by foster-based US rescues
- **ShelterBuddy** — independent commercial platform for shelters, rescues, municipalities, and enterprise multi-site operations

The core model was checked across product generations spanning two decades (legacy municipal installations, open-source lineage, and current cloud platforms) and across regions (US, UK, AU locale features) to avoid over-fitting to the current cloud-SaaS pattern.

## Sources

Research date: **2026-09-06**

Primary official sources:

- Animal Shelter Manager 3 — official user manual (Animals, Movements, People, Animal Control, Publishing chapters) — https://github.com/sheltermanager/asm3/tree/master/doc/manual
- RescueGroups.org — official user guide (Getting Started; Data Management Guide) — https://userguide.rescuegroups.org/
- 24Pet — PetPoint product page — https://www.24pet.com/products/petpoint
- 24Pet — Chameleon product page — https://www.24pet.com/products/chameleon
- 24Pet — 24PetShelter product page (features and roadmap FAQ) — https://www.24pet.com/products/24petshelter
- ShelterBuddy — product site — https://www.shelterbuddy.com/

> Sourcing limitation: Shelterluv, a major vendor in this market, could not be accessed from the research environment (site returned access errors; its help center is a JavaScript application with no extractable content), and PetPoint's operational help is behind authenticated login. Claims in this document are therefore calibrated to the accessible official documentation: detailed operational mechanics come from the ASM manual and the RescueGroups guide; the remaining products contribute positioning-level and feature-level evidence. Precise numeric limits, hold durations, and jurisdiction-specific rules are intentionally not stated, as no accessible source supports that precision.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
