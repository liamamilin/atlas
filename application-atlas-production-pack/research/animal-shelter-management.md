# Research Notes — Animal Shelter Management

Research date: 2026-09-06
Slug: animal-shelter-management
Directory location: §29 Home, Family, Personal & Local Services (siblings: Pet Adoption Platform, Veterinary Practice Management, Pet Boarding Management, Pet Care Business Management; cross-section neighbors: Animal Control Management §24, Research Animal Facility Management §22)

---

## Research Goal

Understand what "Animal Shelter Management" software actually is as an Application Type: who operates it, what core objects exist inside it, how the intake→in-care→outcome loop works, how care and adoption workflows are executed, and where its boundary sits against the neighboring Pet Adoption Platform, Animal Control Management, Veterinary Practice Management, and Pet Boarding Types.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: operator-side operational software for organizations that take custody of animals (animal shelters, humane societies, SPCAs, rescue groups, municipal animal services). The center is the individual animal's record and its custody lifecycle: intake into care → daily care while in custody → outcome that ends custody (adoption, return to owner, transfer, euthanasia, death).
- Primary users: shelter staff (front desk/intake, kennel/animal care, veterinary/medical, adoption counselors), shelter managers, volunteers and foster caregivers; municipal variants add animal control/field officers.
- Most likely confusions:
  - Pet Adoption Platform (consumer-facing adoption discovery/listing)
  - Animal Control Management (government field/enforcement operations)
  - Veterinary Practice Management (client-based clinical business)
  - Pet Boarding / Kennel Management (commercial boarding; owner retains custody)
  - Nonprofit CRM / Donor Management (fundraising)
  - Research Animal Facility Management (custody for research, not adoption)
- Unknowns going in: whether the animal record or the kennel is the structural center; whether adoption workflow is definitional or just the most common outcome; how strongly animal-control functions are bundled; how public adoption listing integrates; regional/legal variation (hold periods, statistics regimes).

## Research Questions

1. What is the central record, and what does it contain (identity, species/breed, identifiers, status)?
2. How does an animal enter the system (intake types: stray, owner surrender, transfer, return) and leave it (outcome types)?
3. How is in-care state tracked (location, kennel/unit, foster placement, status flags)?
4. How are care activities recorded and scheduled (vaccinations, treatments, tests, observations, behavior)?
5. How does the adoption workflow work (application/reservation → approval → contract → fee), and what other outcomes exist?
6. What person records exist (adopter, owner, foster, volunteer, transfer partner) and how do they relate to animals?
7. What municipal/animal-control functions appear (licensing, citations, incidents, field dispatch), and are they core or optional?
8. What public-facing surfaces exist (adoption website, third-party listing portals, microchip registration)?
9. What reporting/compliance exists (intake/outcome statistics, standardized measures)?
10. What varies by segment (foster-based rescue vs municipal shelter vs enterprise multi-site)?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Segment | Philosophy | Evidence quality |
|---|---|---|---|
| Animal Shelter Manager (ASM3 / sheltermanager.com) | international; small-to-medium rescues and shelters; open source + hosted | comprehensive shelter operations, configurable, self-hostable | Strong (full official user manual, fetched chapter-by-chapter) |
| PetPoint (24Pet/Pethealth) | North American industry standard; thousands of orgs | cloud shelter operations + industry data network + microchip ecosystem | Medium (official product page; operational docs behind login) |
| Chameleon (24Pet) | municipal animal services / large shelters (Orange County, Las Vegas, Montgomery County) | shelter + field services, deep customization, on-prem-era heritage | Medium (official product page + detailed customer operation testimonials) |
| 24PetShelter (24Pet) | new-generation cloud platform for simplified operations | mobile-first, lightweight intake→adoption core | Medium (official product page with feature lists and roadmap FAQ) |
| RescueGroups.org | US foster-based rescues/nonprofits; free service tier | adoption-portal-first with data management add-on | Medium-strong (official user guide, fetched) |
| ShelterBuddy | independent commercial; shelters, rescues, municipalities, enterprise multi-site | record→in-care services→placement→reporting pipeline | Medium (official product site) |

Note: PetPoint, Chameleon, and 24PetShelter are one vendor family (24Pet/Pethealth) representing three product generations; they are treated as one sample with three generations for cross-product purposes, with ASM, RescueGroups, and ShelterBuddy providing independent-vendor coverage.

Shelterluv (major modern US SaaS) was targeted but www.shelterluv.com returns 403 to automated fetch (2 attempts) and its help center is a JavaScript application with no extractable content — abandoned per source-access rules and recorded as a sourcing limitation.

## Sources

Tier 1 (official operational documentation):

- Animal Shelter Manager 3 official user manual (in-repo Sphinx source, fetched via GitHub):
  - Animals — https://github.com/sheltermanager/asm3/blob/master/doc/manual/animals.rst
  - Movements — https://github.com/sheltermanager/asm3/blob/master/doc/manual/movements.rst
  - People — https://github.com/sheltermanager/asm3/blob/master/doc/manual/people.rst
  - Animal Control — https://github.com/sheltermanager/asm3/blob/master/doc/manual/animalcontrol.rst
  - Publishing — https://github.com/sheltermanager/asm3/blob/master/doc/manual/publishing.rst
  - Manual chapter index (module map) — https://github.com/sheltermanager/asm3/tree/master/doc/manual
- RescueGroups.org official user guide:
  - Getting Started with RescueGroups.org — https://userguide.rescuegroups.org/
  - Data Management Guide — https://userguide.rescuegroups.org/display/DMG/Data+Management+Guide
  - Getting started with Data Management — https://userguide.rescuegroups.org/display/DMG/Getting+started+with+Data+Management

Tier 2 (official product pages):

- 24Pet (PetPoint) — https://www.24pet.com/products/petpoint — fetched 2026-09-06
- 24Pet (Chameleon) — https://www.24pet.com/products/chameleon — fetched 2026-09-06
- 24PetShelter — https://www.24pet.com/products/24petshelter — fetched 2026-09-06
- 24Pet root (vendor/network context) — https://www.petpoint.com/ (redirects into 24pet.com) — fetched 2026-09-06
- ShelterBuddy — https://www.shelterbuddy.com/ — fetched 2026-09-06
- ASM3 repository (project facts, GPL, hosted service sheltermanager.com) — https://github.com/sheltermanager/asm3

Failed / limited sources:

- Shelterluv: https://www.shelterluv.com/ and /features → 403 (twice); https://help.shelterluv.com/ → JS app ("Pylon"), no extractable content → abandoned. Shelterluv is therefore NOT used as a sample; market-share claims about it are not made anywhere in this research.
- PetPoint operational help (sms.petpoint.com login required) → not accessible; PetPoint evidence limited to product-page level.
- sheltermanager.com marketing site requires JavaScript → not extractable; ASM evidence taken from the official manual and repository instead (stronger sources anyway).

---

## Product Observations

### Animal Shelter Manager / ASM3 / sheltermanager.com (evidence layer A unless noted)

Open-source (GPLv3) shelter management application with a hosted commercial instance (sheltermanager.com); used internationally (US/UK/AU locale features visible in manual).

Manual module map (chapter titles = direct evidence of module existence): Animals, Movements, People, Animal Control, Lost and Found, Waiting List, Online Forms, Documents, Diary, Rota (staff scheduling), Stock Control, Accounts, Boarding, Clinic, Events, Mail Merge, Reports, Publishing, Website, Mobile, Searching, Configuration.

Key operational findings:

- **Shelter View (in-care cockpit)**: overview of all animals currently on the shelter, broken down by internal location; drag-and-drop animals between locations; units = pens/cages/kennels/runs; unoccupied units highlighted as available; units can be reserved or sponsored; special modes show animals in foster homes (foster is a "virtual location"); a "status" mode separates adoptable animals from not-for-adoption, reserved, quarantined, held, cruelty-case animals.
- **Animal record**: the central object. Banner + tabbed sections: Details (species, breed(s) + crossbreed flag, name, age, shelter code, location; flags: Non-Shelter Animal, courtesy listing, not for adoption, Hold, Quarantine), Entry (how the animal entered: original owner, person who brought in, date brought in, entry reason; Asilomar categories in US locale), Entry History (repeat intakes via "New Entry" generating a new shelter code), Health & Identification (microchip, special needs), Death (deceased date marks the animal dead; "died off shelter" excluded from figures), Diet, Costs (daily boarding cost accrual + cost types + donations allocated to the animal), Vaccination (required/given/expires dates), Test, Medical (regimens/profiles generating sequential treatment records; Medical Book of outstanding treatments), Media (photos/documents, watermarking, web-preferred image, publish exclusion), Diary, Transport, Movements, Log (free-typed log types: weights, bite reports, owner emails, complaints).
- **Movements (custody transactions)**: "each movement record represents a leaving and returning transaction"; only one active unreturned movement at a time; every way an animal leaves the shelter requires a movement record — the only exception is death (handled on the death tab). Move menu actions validate animal and person, auto-return from foster, cancel open reservations. Movement kinds observed: adoption, foster, transfer, retailer (pet-shop channel), trial adoption ("foster-to-adopt"), reclaimed/escaped/stolen/released returns handled via return books. Movement books: Reservation, Foster, Retailer, Trial adoption, plus return books for recent adoptions/transfers/other movements.
- **Reservations = adoption applications**: ASM explicitly notes it calls reservations what some shelters call "adoption applications"; multiple open reservations per animal allowed; one becomes the adoption and the others are cancelled; reservations can be created without an animal (option) for pre-approval of adopters.
- **Adoption workflow support**: adoption coordinator staff flag; animals assigned a coordinator; online forms (adoption applications) can be emailed to the coordinator; document templates with merge keys; on-screen/electronic document signing; adoption fee and costs tracked; payments per person (adoption fees, donations, sponsorship; recurring payments; vouchers in UK locale).
- **People**: "any person or organisation who has any contact with the shelter — staff member, volunteer, care officer, animal adopter/fosterer". Classification flags (adopter, fosterer, volunteer, homechecker with coverage areas, retailer, adoption coordinator, membership, gift aid UK). "Looking For" panel: adopter criteria matched against animals by a daily report. Person tabs for License, Investigation, Citations, Equipment Loans (all part of the animal-control module and removable). Person merge for duplicates; links tab shows every record the person touches.
- **Animal control module (optional, explicitly removable)**: "Disable animal control functionality from menus and screens" option. Incidents (call → dispatch → follow-up; pickup location as jurisdiction; up to 3 suspects; citations and fines with due/paid dates; victim), alerts for unpaid fines/undispatched calls/incomplete incidents/traps due back, map of active incidents, equipment (trap) loans with deposits, animal licensing (license records on animal and person; licensed animals are typically non-shelter animal records).
- **Lost and Found / Waiting List / Boarding / Clinic modules exist** as separate manual chapters (module existence observed from chapter index; details not fetched).
- **Publishing (public adoption output)**: publishes adoptable animals to third-party portals (PetFinder, Adopt-a-Pet, RescueGroups.org, PetRescue AU, Savour-Life AU, Maddie's Pet Assistant, Petco Love/petcolove, PetFBI) and generates the shelter's own website (templated HTML pages, thumbnails, RSS, adopted/deceased pages); animal selection rules (exclude too-young animals, exclude animals over a reservation threshold, exclude not-for-adoption/hold/quarantine flags, courtesy listings included); microchip registry updates after adoption/reclaim (AVID PETtrac, Anibase, AKC Reunite, BuddyID, FoundAnimals, HomeAgain, PetLink, SmartTag, 24Petwatch), with held-awaiting-reclaim animals excluded until the hold is removed; statistics publisher to Shelter Animals Count (US national intake/outcome aggregation).
- **Bonded animals & litters**: bonding links up to 2 companion animals (joint adoption warnings, merged listings); litters tracked with mother, species, count, auto-expiry.
- **Template animals**: default vaccination/medical/diet/cost packages cloned onto new intakes (per type or species, with baby variants).
- **Daily observations**: structured per-animal log entries (e.g., appetite/behavior fields) written in bulk from a location-filtered list.
- **Roles/users**: system users with permissions; daily batch routines recalculate ages/time-on-shelter and run publishing.

### PetPoint (24Pet) (evidence layer A for product-page claims; operational detail not accessible)

Positioning: "cloud-based shelter software… streamline workflows and deliver superior care and outcome for every pet." Partners include large US shelters (Louisiana SPCA, Wisconsin Humane Society, City of Lubbock — a municipal customer).

- Key features (product page): pet inventory management; instant access to the 24Petwatch microchip registry; automated transfer of pet records; streamlined search; customizable reporting; dedicated support.
- Network features: PetPlace — "automatic publishing feature and our pet adoption search engine" (public listing of adoptable pets); 24Petwatch — consent-to-contact collected at adoption, lost-pet database; industry data — aggregated animal-welfare statistics.
- Enterprise tier (customer quote): scheduled reports, scheduled intakes/outcomes, mobile inventory.
- Login surface exists at sms.petpoint.com (operational docs behind authentication — not accessible).

### Chameleon (24Pet) (evidence layer A for product-page claims; customer testimonials treated as vendor-published operational evidence)

Positioning: "shelter management software" for "the most complex operations"; customers are predominantly municipal animal services (Orange County Animal Services FL, The Animal Foundation Las Vegas, Montgomery County Animal Services TX, Corpus Christi Animal Care Services, CACC).

- Key features (product page): animal tracking; unlimited custom reporting; dashboard integration; data mapping; WebChameleon and WebLicensing (web access + online licensing); ScanIt (barcode data entry) and Quick Kennel (kennel checks); onboarding/training.
- Customer-confirmed operations (vendor-published testimonials): issuing citations; entering behavior notes; scheduling spay/neuter surgery; emailing rescue partners; visual kennel feature showing available kennel space; customizable fields; veterinary team tracking medical care and medications; length-of-stay filters; microchip lookup linking owners; automated emailing of medical records (PostMaster); daily snapshot reports; adopter review reports; public "411" available-animal reports; 20-year usage span (Orange County) — long-lived municipal deployments.
- Explicit dual scope: "fully supports BOTH your Shelter and Field Services" (Montgomery County).

### 24PetShelter (24Pet) (evidence layer A for product-page claims)

New-generation cloud platform ("mobile-first, intuitive, and light"); positioned as successor architecture to PetPoint/Chameleon (which stop receiving new feature development but continue in support).

- Current features: animal profiles (photos/videos, tags, key details); manage animal locations within the shelter; guided intake workflows; outcome tracking (adoption + other outcomes); standardized medical templates; memo/note tracking; stats dashboard for key shelter metrics; organizational account setup with role-based permissions; digital adoption workflows; mobile checkout with receipt generation; microchip registration to the 24Petwatch registry.
- Roadmap (FAQ): over-the-counter transactions, external tender support, multi-animal outcomes, additional contract types, advanced user permissions, foster parent management, online pet listings, kennel cards.
- Pricing model: no subscription for core; per-adoption fee via digital checkout; free microchip per eligible adoption.

### RescueGroups.org (evidence layer A for user-guide claims)

Free/low-cost service suite for US nonprofit rescues; the suite separates a consumer-facing "Pet Adoption Portal" service from a "Data Management" service — structurally important for the boundary with Pet Adoption Platform.

- Data Management service = Pet Adoption Portal plus: more animal fields; track adoptions; track returns; track contacts; track donations; inventory loaners; animal journals (medical tracking and reminders); reports.
- Getting-started flow: review organization contact info → add animals → enable exports (animal exports to adoption services) → add volunteers (user logins with roles/permissions).
- Related guide topics: managing animal status; about animal adoptions; handling returned animals; templates when adding animals; managing animal files; managing information about colonies (community cat colonies); events; donations; inventory; contacts.
- Volunteers are account users with role-based permissions; contacts are a first-class data table.

### ShelterBuddy (evidence layer A for product-site claims)

Independent commercial vendor; segments: animal shelters, rescues (foster care), municipalities & animal control ("manage records, ensure compliance, and coordinate field officers"), enterprise shelters (multi-location, custom API, advanced reporting). Scale claims: 200+ shelters, 1M+ animals/year.

- Described pipeline ("How ShelterBuddy Works"): animal record creation and intake notes → medical, licensing, and other treatments & services applied to the animal while in care → services that help the animal find a home and keep documentation clear → records and reporting (fundraising, compliance, community relations).
- Headline: "Track intakes, outcomes, in-care pets, licenses, donations, and much more."
- Plans: Express (core), Pro (municipalities/large shelters), Gold (advanced reporting/documentation/API).
- Integration partners displayed: Shelter Animals Count, PetRescue, Petfinder, Adopt-a-Pet, Doobert, Lost… (listing/transport/logistics partners).

---

## Cross-product Comparison

| Dimension | ASM | PetPoint | Chameleon | 24PetShelter | RescueGroups | ShelterBuddy |
|---|---|---|---|---|---|---|
| Central animal record with identity (name/code, species/breed, microchip) | ✓ (shelter code, microchip, breeds) | ✓ ("pet inventory") | ✓ (animal tracking) | ✓ (animal profiles, tags) | ✓ (animals table) | ✓ (animal record creation) |
| Intake capture (entry reason, brought-in person/date) | ✓ (Entry tab, entry history) | ✓ (scheduled intakes) | ✓ (intake via field/shelter) | ✓ (guided intake workflows) | ✓ (add animals; status) | ✓ (intake notes) |
| Outcome capture ending custody | ✓ (movements + death tab) | ✓ (scheduled outcomes) | ✓ | ✓ (outcome tracking: adoption + other) | ✓ (adoptions, returns) | ✓ (outcomes) |
| In-care placement tracking (location/unit/kennel) | ✓ (shelter view, units, drag-drop) | ✓ (kennel management) | ✓ (visual kennel, Quick Kennel) | ✓ (locations; kennel cards on roadmap) | — (foster-based; not observed) | ✓ (physical environment setup) |
| Foster program | ✓ (foster movements, foster book, capacity) | not observed | ✓ (rescue placements via communications) | roadmap (foster parent management) | ✓ (foster-based rescues are the core audience) | ✓ (rescue segment: foster care) |
| Medical/vaccination/treatment records with due tracking | ✓ (vaccination/test/medical books, regimens) | ✓ (medical care) | ✓ (vet team, medications, surgery scheduling) | ✓ (standardized medical templates) | ✓ (animal journals, reminders) | ✓ (medical treatments while in care) |
| Behavior/observation notes | ✓ (daily observations, log types, behavior flags) | not observed | ✓ (behavior notes) | ✓ (memo/note tracking) | not observed | not observed |
| Holds / legal status flags | ✓ (Hold, Quarantine, cruelty case, not-for-adoption) | not observed | not observed (custom fields) | not observed | not observed | not observed (compliance mentioned) |
| Adoption application/reservation handling | ✓ (reservations = applications; coordinator) | not observed (PetPlace publishing only) | ✓ (adopter review report) | ✓ (digital adoption workflows) | ✓ (track adoptions; portal) | ✓ (placement services, documentation) |
| Adoption contract/document generation & signing | ✓ (document templates, e-signing) | not observed | not observed | ✓ (contract types on roadmap; receipts) | not observed | ✓ (documentation) |
| Fees/payments (adoption fees, donations) | ✓ (payments, vouchers, funding) | ✓ (mobile checkout per 24PetShelter) | not observed | ✓ (digital checkout, receipts) | ✓ (donations) | ✓ (donations) |
| Public adoption listing output | ✓ (own site + PetFinder/Adopt-a-Pet/etc.) | ✓ (PetPlace publishing + search engine) | ✓ (public available-animal reports) | roadmap (online pet listings) | ✓ (Pet Adoption Portal + exports) | ✓ (Petfinder/Adopt-a-Pet partners) |
| Microchip registration to registries | ✓ (many registries) | ✓ (24Petwatch) | ✓ (microchip lookup) | ✓ (24Petwatch) | not observed | not observed |
| Person database (adopters/owners/fosters/volunteers) | ✓ (people module, flags, merge) | not observed | ✓ (owner linking) | not observed | ✓ (contacts, volunteers as users) | ✓ (volunteers/staff counts) |
| Volunteer management | ✓ (flags, rota) | not observed | not observed | not observed | ✓ (user logins, roles) | ✓ (5,000+ volunteers claim) |
| Animal control: incidents/citations/field | ✓ (optional module, removable) | not observed | ✓ (citations, field services) | not observed | not observed | ✓ (municipality segment: field officers) |
| Licensing (pet licenses) | ✓ (in animal-control module) | not observed | ✓ (WebLicensing) | not observed (licensing module fees mentioned) | not observed | ✓ (licenses) |
| Lost & found matching | ✓ (module + publishers) | not observed | not observed | not observed | not observed | not observed (partner "Lost…") |
| Waiting list | ✓ (module) | not observed | not observed | not observed | not observed | not observed |
| Standardized statistics reporting | ✓ (Asilomar categories; Shelter Animals Count publisher) | ✓ (industry data) | ✓ (custom reports/dashboards) | ✓ (stats dashboard) | not observed | ✓ (Shelter Animals Count partner) |
| Multi-site/enterprise | ✓ (multi-database) | ✓ (Enterprise level) | ✓ (large municipal) | not observed | not observed | ✓ (enterprise multi-location + API) |
| Deployment | self-hosted OSS + hosted | cloud SaaS | on-prem heritage + web modules | cloud SaaS (mobile-first) | cloud service (free tier) | cloud SaaS (tiered) |

Reading of the matrix:

- Present in all six samples (or five of six, with the sixth being a foster-based rescue where the concept transfers): animal record, intake, outcome, care records, person records, adoption workflow support, public listing output. These are the Type's stable structure.
- Present in most but shaped by segment: kennel/unit inventory (facility-based products), foster program (rescue-weighted), licensing/citations (municipal-weighted), microchip registration (North America-weighted).
- Present in one or two: lost & found matching, waiting list, retailer channel, colonies (community cats), trap loans — optional structures.

## Canonical Model (L0–L3)

### L0 — Defining Invariant

An Animal Shelter Management application is operated by an organization that takes custody of animals, and is built on four inseparable structures:

```text
Animal Record (individually identified animal)
└── Custody Lifecycle
    ├── Intake (animal enters the organization's custody)
    ├── In Care (custody state with a trackable placement)
    └── Outcome (event that ends custody)
├── Care & Custody Events (dated records attached to the animal while in care)
└── Associated Person Records (the people on the other side of custody events)
```

1. **Animal record** — every animal in the organization's care or history is an individually identified record (name/shelter code, species, breed, age/sex, identifiers such as microchip). Without it there is nothing to manage.
2. **Custody lifecycle** — the record moves through intake → in care → outcome. The outcome ends custody (adoption, return to owner, transfer to another organization, death/euthanasia). Without the lifecycle the product is a listing site or a medical records system, not shelter management.
3. **Care & custody events** — dated, attributed events attach to the animal while it is in care (vaccinations, treatments, tests, observations, holds, location changes). Without them the organization cannot operate or account for the animal's stay.
4. **Associated person records** — each custody transition has a person (or a recorded unknown): the surrendering/finding owner at intake, the adopter at adoption, the foster caregiver during placement, the receiving organization at transfer. Without people the custody events have no counterparty.

Historical/market-sample check (§24-style): the sampled products span ~20+ years of deployments (Chameleon municipal installs, PetPoint since at least 2008, ASM since the early 2000s) and three regions (US, UK, AU locale features in ASM). All fit the four-element core. Foster-based rescues without facilities satisfy it (placement = foster home). Older open-source shelter systems (ASM lineage) satisfy it. The core therefore does not over-fit the current cloud-SaaS market.

Deliberately NOT in L0 (tested and demoted):

- **Adoption workflow specifics** — adoption is the most common outcome but not the defining one; return-to-owner, transfer, and death are equal citizens in the outcome set (ASM treats death as the only non-movement outcome; RescueGroups tracks "returns" as a first-class concept).
- **Kennel/unit inventory** — universal in facility-based products but absent in foster-based rescues (RescueGroups sample); the invariant is "trackable placement", not cages.
- **Medical module depth** — care events are invariant; regimens/books/templates are mature implementations.
- **Public adoption listings** — an output function (publishing/exports) in every sampled product, not the system's center; a shelter-management product without listings still exists (municipal impound-only operations).
- **Payments/fees** — common but not universal (free-adoption orgs; RescueGroups' donations-first framing).
- **Animal control functions** — explicitly optional/removable in ASM; absent in rescue-focused samples.
- **Microchip registration** — region-weighted (North America) common structure, not definitional.

### L1 — Common Mature Structure

Present across most sampled products; expected by the market but not definitional:

- In-care cockpit: location/unit board of current animals (Shelter View; visual kennel; kennel cards on roadmap)
- Medical suite: vaccination/test/treatment records with due/given dates, outstanding-treatment books, medical templates/profiles
- Status/flag system: adoptable, not-for-adoption, hold, quarantine, cruelty case, reserved
- Adoption workflow: application/reservation capture, coordinator assignment, approval, contract/document generation, fee collection, receipts
- Foster program: foster homes as placements with capacity, foster books/management
- Person database with role flags (adopter, foster, volunteer, staff, transfer partner) and duplicate merging
- Public adoption output: own adoption page/website + push to third-party portals (Petfinder, Adopt-a-Pet, regional portals)
- Photo/media management per animal (web-preferred image, watermarking)
- Intake/outcome statistics and dashboards; standardized aggregation feeds (Shelter Animals Count; Asilomar categories in US products)
- Payments: adoption fees, donations, vouchers; receipts
- Role-based user permissions; volunteers as restricted users
- Document templates with merge fields; electronic signing
- Tasks/reminders/alerts (vaccinations due, holds expiring, follow-ups)
- Microchip registration to lost-pet registries (North America)

### L2 — Variant / Optional Structure

Depends on segment, geography, deployment, or business model:

- Municipal/animal-control overlay: field incidents (call→dispatch→follow-up), citations and fines, trap/equipment loans, pet licensing, jurisdiction/pickup locations (ASM optional module; Chameleon and ShelterBuddy municipal editions)
- Facility depth: kennel/unit inventory with reservations/sponsorship, boarding cost accrual (facility shelters) vs foster-network-as-placement (rescues)
- Lost & found matching (found-stray ↔ lost-report matching; regional services)
- Waiting lists (surrender queues)
- Community cat colonies / TNR support (RescueGroups colonies)
- Retailer/pet-shop channel movements (ASM; UK-style retail adoption)
- Bonded-animal and litter handling
- Regional regimes: US (Asilomar categories, Shelter Animals Count, stray holds), UK (gift aid, neuter vouchers, petslocated), AU (PetRescue/Savour-Life publishers, breeder ID fields)
- Deployment: cloud SaaS vs self-hosted open source vs on-prem heritage; pricing models (subscription vs per-adoption vs free tier)
- Scale: single-site rescue vs enterprise multi-site with APIs and advanced reporting
- Species scope: companion animals (dogs/cats) vs exotics, equine, livestock (sanctuaries)
- Ecosystem coupling: microchip registry + lost-pet network + national statistics (24Pet/PetPoint model)

### L3 — Vendor-specific Structure

- ASM: template animals cloned onto intake; retailer movements; unit sponsorship; "Looking For" adopter matching; funded payments; specific publisher integrations (petfbi, petslocated)
- 24Pet family: PetPlace adoption search engine; consent-to-contact collection at adoption; ScanIt/Quick Kennel/PostMaster; WebLicensing; per-adoption pricing with bundled microchip; 24Petwatch registry coupling
- RescueGroups: free-tier service suite bundling voicemail/fax/email marketing around the core; colonies module
- ShelterBuddy: Express/Pro/Gold tiering; Adōpets fundraising tie-in

## Vendor-specific Findings

See L3 above. The most consequential vendor pattern is the 24Pet ecosystem model (shelter software + microchip registry + adoption search engine + national statistics), which bundles several adjacent services around the shelter core; it must not be generalized into the Type definition.

## Rejected Findings

- "Shelter management = kennel management": rejected — foster-based rescues (RescueGroups sample) satisfy the Type with no kennel inventory; placement is the invariant, cages are an implementation.
- "Shelter management = adoption processing": rejected — outcomes include return-to-owner, transfer, euthanasia, death; adoption is one outcome among several (ASM movement model; 24PetShelter "adoption + other outcomes").
- "Shelter management includes animal control field operations": rejected as definitional — ASM ships it as an explicitly removable module; rescue-focused samples lack it entirely. It is a segment overlay.
- "Shelter management = veterinary records": rejected — care records attach to animals in custody; there is no client/appointment/billing-for-services structure as the primary object (contrast Veterinary Practice Management).
- "Public adoption listings are the product": rejected — listings are an output/publishing function in every sample; the consumer-facing listing surface is a different Type (Pet Adoption Platform).
- "Fundraising/donor management is part of the Type": rejected as definitional — donations appear as payment records and reporting feeds; donor CRM depth is a separate Type.

## Boundary Findings

1. **vs Pet Adoption Platform (§29 sibling)** — the sharpest boundary. The shelter system is operator-facing and centers on custody; the adoption platform is consumer-facing and centers on discovery/listing. Evidence: RescueGroups ships "Pet Adoption Portal" and "Data Management" as two separate services; ASM's publishing menu is an output function; PetPoint's PetPlace is a companion feature; 24PetShelter lists "online pet listings" as roadmap (i.e., a shelter product can exist without listings). Structural test: remove the custody lifecycle → an adoption platform remains (listings + adopter applications); remove public discovery → shelter management remains (impound/transfer-only operations still function). Flag for joint review when Pet Adoption Platform is processed.
2. **vs Animal Control Management (§24)** — government field/enforcement operations (complaint intake, dispatch, citations, licensing) vs custody operations. Evidence: ASM ships animal control as an optional module that can be disabled without affecting the shelter core; Chameleon and ShelterBuddy sell municipal editions where both are bundled; Montgomery County testimonial: "fully supports BOTH your Shelter and Field Services". The two Types share the animal record and the impound→shelter handoff; products merge them, but the structures are distinct. Flag for joint review when Animal Control Management is processed.
3. **vs Veterinary Practice Management (§29)** — client-based clinical business (owners book appointments, pay for services; patients are outpatients) vs custody-based care (animals are in the organization's custody; care is part of the stay). Evidence: shelter medical modules track in-care animals with due-date regimens; ASM additionally ships a separate Clinic module chapter (for shelters running public clinics) — the vendor itself separates the two structures. Flag for joint review when Veterinary Practice Management is processed.
4. **vs Pet Boarding / Kennel Management (§29)** — commercial boarding is a paid service where the owner retains custody; sheltering is custody transfer. Both track kennel occupancy, which creates surface similarity; the custody model and outcome set differ. ASM even ships a separate Boarding module chapter — again the vendor separates the structures.
5. **vs Nonprofit CRM / Donor Management (§25)** — donations/payments exist inside shelter products as records and reporting feeds, but donor cultivation, campaigns, and gift processing are not the shelter core. Adjacent, frequently bundled.
6. **vs Research Animal Facility Management (§22)** — custody of animals for research protocols vs custody for welfare/placement outcomes; different lifecycle ends, different compliance regimes. Same "animal record + custody" pattern, different Type.
7. **Internal taxonomy observation** — the leaf sits in §29 (consumer/pet services) while its closest operational neighbor Animal Control Management sits in §24 (government). The Type itself is nonprofit/municipal operator software; its placement reflects the pet-services framing of the directory. Recorded as an observation; no taxonomy change proposed.

## Uncertainties

- PetPoint operational detail (exact intake/outcome editors, kennel board behavior) is behind authenticated support portals; PetPoint evidence is product-page level. Its structural role (industry-standard NA platform) is well corroborated by vendor-published customer testimonials and the 24Pet network pages.
- Shelterluv could not be fetched at all (403 + JS help center). It is a major modern US vendor; its absence means the sample under-represents the newest SaaS generation's UX conventions. Nothing in the synthesis depends on Shelterluv-specific behavior, but UI-level claims are kept generic.
- Hold-period specifics (stray hold durations, quarantine rules) are jurisdiction-dependent; no product documentation in the sample states numeric hold periods, so none are asserted.
- The exact set of outcome types varies by product and jurisdiction (e.g., "released to wild" for TNR, "escaped", "stolen"); the synthesis describes the outcome concept and observed examples without asserting a universal taxonomy.
- Chameleon's current architecture (post-24Pet acquisition) is described by vendor pages only; its on-prem heritage is inferred from customer testimonials ("20 years", on-prem-era features) and the vendor's own FAQ describing PetPoint/Chameleon as "older architecture".
- RescueGroups' management depth (medical journals, status model) is documented at guide-index level; article-level detail was not fetched.

## Final Synthesis

Animal Shelter Management is operator-facing custody software for organizations that take animals into their care. Its world model is: an individually identified **animal record**, moving through a **custody lifecycle** (intake → in care at a trackable placement → outcome that ends custody), accumulating **care and custody events** (medical, observational, locational, legal), and connected at every transition to **person records** (surrenderer/finder, adopter, foster, transfer partner, owner). Around this core, mature products add: an in-care cockpit (location/kennel board), a medical suite with due-date tracking, status/hold flags, an adoption workflow (application → approval → contract → fee), foster programs, a person database with role flags, public adoption output (own pages + portal feeds), statistics, payments, and role-based permissions. Municipal deployments overlay animal-control structures (incidents, citations, licensing, field dispatch); rescue deployments replace kennels with foster networks. The Type's boundaries are sharpest against Pet Adoption Platform (consumer-facing listing surface fed by, but distinct from, the custody system), Animal Control Management (field/enforcement overlay, not the core), and Veterinary Practice Management (client-based clinical business, not custody-based care).
