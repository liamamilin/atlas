# Research Notes — Animal Control Management

Research date: 2026-09-06
Slug: animal-control-management
Directory location: §24 Government, Public Sector & Civic (siblings: Code Enforcement Management, Government Licensing Management, 311 / Citizen Service Request Platform, Police Records Management System; cross-section neighbor: Animal Shelter Management §29)

Joint-review obligation: research/animal-shelter-management.md flagged "animal-shelter-management vs animal-control-management" for joint review when this leaf is processed. This file discharges that flag (see Boundary Findings #1).

---

## Research Goal

Understand what "Animal Control Management" software actually is as an Application Type: who operates it, what the central operational object is, how the complaint→dispatch→field-response→enforcement loop works, how impoundment hands animals into shelter custody, how pet licensing and compliance fit in, and where the boundary sits against Animal Shelter Management, 311/Citizen Service Request, Code Enforcement, and Government Licensing Types.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: government/authority-facing field-operations software for animal-related service requests: public complaints and officer-initiated calls about animals, dispatch of animal control officers (ACOs), enforcement actions (warnings, citations, fines, quarantine), impoundment/capture of animals, pet licensing and identification compliance, and the records (animal, person, location) that support them.
- Primary users: animal control officers / field officers, dispatchers or front-desk call takers, agency supervisors, licensing/clerical staff; in some jurisdictions the unit sits inside a police department or a contracted humane society.
- Most likely confusions:
  - Animal Shelter Management (custody/care operations; products frequently bundle both)
  - 311 / Citizen Service Request Platform (generic non-emergency request intake; animal complaints are one catalog item)
  - Code Enforcement Management (same complaint→inspection→violation→citation pattern, but property/ordinance objects)
  - Government Licensing Management (pet licensing as an instance of generic licensing)
  - Police Records Management / CAD (animal control is often police-adjacent)
- Unknowns going in: whether the incident or the animal is the structural center; whether licensing is definitional or adjacent; whether dispatch mechanics are definitional or just common; how bite cases/quarantine are structured; whether dangerous-dog designations are a standard structure; how field mobility is delivered.

## Research Questions

1. What is the central operational object — the complaint/incident/call, the animal, or the case?
2. What is the intake loop: who reports, how is the call captured, triaged, dispatched?
3. What happens in the field: capture/impound, warnings/citations, education, quarantine?
4. How do animals flow into custody (impound → shelter) and how does that handoff work?
5. What enforcement structures exist: citations, fines, warnings, court referrals, dangerous-dog designations?
6. Is pet licensing part of this Type, and how does licensing compliance connect to enforcement?
7. What person records exist (complainant, owner, suspect, victim) and how do they relate to incidents?
8. How do dispatch/scheduling/jurisdiction work (zones, pickup locations, follow-ups)?
9. What public-facing surfaces exist (online complaint reporting, license renewal, citation payment)?
10. What varies by operating model (municipal department vs contracted humane society vs police-affiliated unit) and by packaging (suite module vs standalone vs gov-platform module vs licensing network)?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Segment | Philosophy | Evidence quality |
|---|---|---|---|
| Animal Shelter Manager 3 — Animal Control module (sheltermanager.com) | international; small-to-medium agencies; open source + hosted | animal control as a separable module of an animal-services suite | Strong (full official user manual chapter, fetched) |
| Shelter Pro Software | US county/municipal animal services; product lineage since 1994 | dedicated animal control module with law-enforcement framing; modules can stand alone | Strong (official module pages: Animal Control, Animal Identification, Traps, Portal) |
| Chameleon (24Pet) | municipal animal services / large shelters (Orange County FL, The Animal Foundation Las Vegas, Montgomery County TX) | shelter + field services in one customizable municipal suite | Medium (official product page + vendor-published customer operation testimonials) |
| ShelterBuddy | municipalities & animal control segment; shelters, rescues, enterprise | records + compliance + field-officer coordination | Medium (official product site) |
| DocuPet | licensing/reunification network for government agencies across North America | pet licensing as a turnkey outsourced service + national registry | Medium (official partnerships site) |
| GovPilot | generic local-government platform (NJ-centric municipal clerks) | animal services as clerks-department licensing modules + concern reporting | Medium (official module pages; "animal control software" URL resolves to the Dog/Cat License module) |

Note: ASM3 and ShelterPro both ship animal control as a module explicitly separable from shelter management — this vendor-side separability is the cleanest available evidence for the Type boundary. Chameleon and ShelterBuddy represent the municipal bundling pole. DocuPet and GovPilot represent the licensing pole implemented outside dedicated animal-services software.

Failed / limited sources:

- PetData (petdata.com, www.petdata.com): 403 on both attempts → abandoned per source-access rules; the licensing-outsourcing pole is covered by DocuPet instead.
- No dedicated standalone animal-control product with public operational docs was found beyond the module-based ones; the module-based samples are the market's dominant packaging for this Type.

## Sources

Tier 1 (official operational documentation):

- ASM3 official user manual — Animal Control chapter — https://raw.githubusercontent.com/sheltermanager/asm3/master/doc/manual/animalcontrol.rst (fetched 2026-09-06)

Tier 2 (official product pages):

- Shelter Pro — Animal Control Module — https://www.shelterpro.com/animalcontrolmodule/ (fetched 2026-09-06)
- Shelter Pro — Animal Identification Module — https://www.shelterpro.com/animalidentificationmodule/ (fetched 2026-09-06)
- Shelter Pro — Traps Module — https://www.shelterpro.com/trapsmodule/ (fetched 2026-09-06)
- Shelter Pro — home (module map, portal models) — https://www.shelterpro.com/ (fetched 2026-09-06)
- Chameleon (24Pet) — https://www.24pet.com/products/chameleon (fetched 2026-09-06)
- ShelterBuddy — https://www.shelterbuddy.com/ (fetched 2026-09-06)
- DocuPet partnerships — https://partnerships.docupet.com/ (fetched 2026-09-06)
- GovPilot — Dog or Cat License module — https://www.govpilot.com/animal-control-software (redirects to the Dog/Cat License clerks module; fetched 2026-09-06)

Prior-research reuse (same date, same environment):

- research/animal-shelter-management.md (ASM3 manual chapters, 24Pet family pages, ShelterBuddy) — used for the custody-side of the boundary and for cross-referencing module separability.

---

## Product Observations

### Animal Shelter Manager 3 — Animal Control module (evidence layer A)

Open-source (GPLv3) animal-services suite; the Animal Control chapter documents the module's full structure:

- **Incidents are the central object**: "ASM allows you to track animal control incidents. Animal control incidents store information about the initial telephone call, dispatch of officers, the owner/animal being cited, citations, fines and any victim." Incidents are findable via a dedicated find-incident screen and the main search with an `ac:` prefix.
- **Incident detail**: logs the type of incident, the call information, the victim, notes and completion.
- **Dispatch**: covers the address an officer was sent to, who was dispatched, and when they responded; a minimap is shown for the location; a follow-up date/time can be set for reporting, with a home-page alert when due.
- **Pickup locations as jurisdiction**: a pickup location can be chosen from system-configured locations and used "as a jurisdiction for incidents and animals entering the shelter."
- **Suspect/Animal and Citation**: up to 3 suspects per incident, with basic information about the animal(s) causing the incident; optionally linked to an animal record if the animal is taken into the shelter, or to a "non-shelter animal" record for more detail. The citation tab holds citations relating to the incident and fines levied; fines have due and paid dates; overdue fines appear on reports and as home-page alerts.
- **Alerts**: unpaid fines; calls not yet dispatched; calls without a completion date and code; incidents due for follow-up today; traps due for return.
- **Map of active incidents**: plots currently active incidents for route planning and trend spotting.
- **Equipment loans**: traps or equipment loaned to people with deposit amounts; loans have due and return dates; overdue loans highlighted with home-screen alerts; an equipment-loan tab appears on person records.
- **Licensing**: license records appear on both animal and person records; number, type, fee, issue and expiry dates; payments tracked on the animal/person payment tabs. "It is very common for licensed animals to not be shelter animals" — such animals are recorded as "Non-Shelter Animal" records with the current owner set, or (at licensing volume) as comment-only entries without an animal record. Licensing screen has filters for licenses issued/expiring over a period; license numbers searchable with an `li:` prefix.
- Module separability: the shelter research confirmed the animal-control module can be disabled entirely ("Disable animal control functionality from menus and screens") without affecting the shelter core.

### Shelter Pro Software (evidence layer A for module-page claims)

Commercial animal-services application (© 1994–2024), self-hosted or cloud; module map: Animal Control, Shelter Management, Animal Identification, Donations, Traps, Accounting, plus a public Portal with three commercial models (non-transactional / transactional / transactional with online payments).

- **Animal Control Module**: "designed for your agency's law enforcement activities, including the dispatch and field work of Animal Control Officers." Major features: "Incident records (Complaints, Service Calls, Dispatch, etc.)", "Citation records (Citations, Tickets, Warnings, etc.)", "Bite Case records". "An officer can link related records to create a comprehensive and sensible reporting of all elements of any given animal control related occurrence. Or, the Animal Control Module can be used independently as a stand-alone function."
- **Animal Control essentials**: comprehensive ACO narratives and reporting; stray/found pets online real-time (via Portal); evidence photos; remote/field access via virtualization technologies; document imaging; address mapping and geocoding; spell check; customizable note templates; extensive reporting and forms generation.
- **Animal Identification Module (separate module)**: "Licensing / Registration records", "Vaccination / Rabies records", "Microchip records", "Registration records"; tracks "current, expired, or missing status on all forms of identification" and "overall ownership compliance"; "auto generate citations / notices for non-compliance"; online citation payments / dismissals via Portal; online license/registration via Portal; owner and animal profile information; license/registration history; bar coding. Can also be used stand-alone.
- **Traps Module (separate module)**: trap rentals/checkouts with documentation, trap returns; with the Accounting Module: rental fees, deposits, deposit refunds on return; renter signs (or e-signs) a usage agreement.
- **Integration framing**: "the highest value is realized when all the modules are utilized to form an integrated animal control / shelter management / pet licensing system."

### Chameleon (24Pet) (evidence layer A for product-page claims; testimonials treated as vendor-published operational evidence)

Municipal animal-services suite; customers are predominantly municipal animal services (Orange County Animal Services FL — 20 years of use; The Animal Foundation Las Vegas; Montgomery County Animal Services TX; Corpus Christi Animal Care Services; CACC).

- Product-page features: animal tracking; unlimited custom reporting; dashboard integration; data mapping; WebChameleon and WebLicensing ("Manage shelter and field operations from any device with an internet connection and achieve seamless online licensing"); ScanIt (barcode data entry) and Quick Kennel; onboarding/training.
- Customer-confirmed field/enforcement operations (Orange County testimonial): "Our team includes enforcement operations, kennel management, clinic and communications… We utilize Chameleon for issuing citations, entering behavior notes, scheduling for spay/neuter surgery, emailing rescue partners…"
- Dual-scope confirmation (Montgomery County): "a POWERFUL yet CUSTOMIZABLE software suite that fully supports BOTH your Shelter and Field Services."
- Owner identification: Microchip Lookup "allowed us to more quickly, accurately look up and link owners for microchipped animals brought to our Shelter."

### ShelterBuddy (evidence layer A for product-site claims)

Independent commercial vendor; explicit segment: "Municipality & Animal Control — Manage records, ensure compliance, and coordinate field officers." Headline: "Track intakes, outcomes, in-care pets, licenses, donations, and much more." Plans: Express (core), Pro ("Tools for municipalities, large shelters, and advanced situations"), Gold (advanced reporting/documentation/API). Pipeline description: animal record creation and intake notes → medical, licensing, and other treatments & services applied while in care → placement services → records and reporting (fundraising, compliance, community relations).

### DocuPet (evidence layer A for partnerships-site claims)

Licensing/reunification network ("the first nationwide pet registration network"), serving "hundreds of agencies and 4M+ pet owners"; "over 300 communities" as partners; since 2014 providing "comprehensive pet licensing services for municipalities across North America."

- Government/agency offer: "turnkey pet licensing solutions, customized communications, robust reporting, payment management, marketing support"; customizable "to meet the requirements of any licensing or microchip registration mandate."
- Registry/reunification: pet profiles with photos/medical details; owners manage info, select tags, make license payments; "Administrator partners can add and manage records too with a suite of tools designed just for them"; HomeSafe tags with unique ID codes; Lost Pet Alerts; Petco Love Lost integration; public tag-code lookup ("Found a pet with a DocuPet tag? Enter the tag code below to view the profile of this pet"); cross-jurisdictional pet profile database for shelter-network partners ("enabling instant owner identification, decreasing shelter stays").
- Professional framing (NACA — National Animal Care and Control Association): "DocuPet plays an important role in supporting agencies by strengthening pet registration and reunification, which ultimately helps officers do their jobs more effectively."
- Customer base includes county animal care & control agencies (Pinal County, Kern County, Washoe County Regional Animal Services, County of San Diego, Toronto Animal Services, State of Delaware Office of Animal Welfare).

### GovPilot (evidence layer A for module-page claims)

Generic local-government management platform. Its "animal control software" URL resolves to the **Dog or Cat License** module of the Clerks department — the vendor's own framing of animal services at the municipal-platform layer:

- Dog License and Cat License modules: pet owners apply for and renew annual licenses online; issuing departments manage and track renewal statuses; automatic renewal reminders; "Both modules create a database of registered pet owners, including contact information, which can be useful for animal control officers in the event that a pet goes missing"; payment collection included. (A separate "Pet License" module also exists.)
- Adjacent modules in the same platform: "Report-a-Concern" (311-style concern reporting) and "Code Enforcement Software" — i.e., the platform covers complaint intake and generic enforcement as separate products, without animal-specific field-ops semantics.

---

## Cross-product Comparison

| Dimension | ASM3 AC module | ShelterPro | Chameleon | ShelterBuddy | DocuPet | GovPilot |
|---|---|---|---|---|---|---|
| Incident/call record as central object (complaint/service call with call info) | ✓ (incidents: call, type, victim, notes, completion) | ✓ ("Incident records (Complaints, Service Calls, Dispatch)") | ✓ (enforcement operations; citations) | ✓ ("coordinate field officers"; records) | — (not observed) | — (Report-a-Concern is generic, not animal-specific) |
| Dispatch/field response recorded on the incident (officer, address, response, follow-up) | ✓ (dispatch screen: address, officer, response time, follow-up date + alert) | ✓ ("dispatch and field work of Animal Control Officers") | ✓ (field operations from any device) | ✓ (field-officer coordination) | — | — |
| Citations/warnings/fines with tracked lifecycle | ✓ (citations + fines with due/paid dates; overdue alerts) | ✓ ("Citation records (Citations, Tickets, Warnings)") | ✓ (issuing citations) | not observed (compliance mentioned) | — | — (generic fee/fine processing exists platform-wide) |
| Bite case records | not observed | ✓ ("Bite Case records") | not observed | not observed | — | — |
| Animal + person parties linked to the incident | ✓ (up to 3 suspects; animal link optional; victim) | ✓ (officer links related records) | ✓ (owner linking via microchip) | ✓ (records) | ✓ (pet + owner profiles) | ✓ (registered pet-owner database "useful for animal control officers") |
| Impound handoff into shelter custody | ✓ (incident animal link "if the animal is taken into the shelter") | ✓ (integrated with Shelter Management Module) | ✓ (shelter + field in one suite) | ✓ (intakes/outcomes) | — (reunification aims to avoid shelter entry) | — |
| Pet licensing/registration records with expiry/renewal | ✓ (license records on animal+person; issue/expiry; filters) | ✓ (separate ID module: licensing/registration, current/expired/missing) | ✓ (WebLicensing) | ✓ (licenses) | ✓ (core business) | ✓ (core module) |
| Licensing compliance → enforcement linkage | not observed (separate structures) | ✓ ("auto generate citations / notices for non-compliance"; online citation payments/dismissals) | not observed | not observed ("ensure compliance") | — (compliance framed as increased registrations) | — (renewal reminders only) |
| Jurisdiction/location structure | ✓ (pickup locations as jurisdiction) | ✓ (address mapping and geocoding) | ✓ (data mapping) | not observed | ✓ (cross-jurisdiction network) | ✓ (municipality-scoped) |
| Map of active incidents / geospatial | ✓ (map of active incidents; minimap on dispatch) | ✓ (address mapping and geocoding) | not observed | not observed | — | ✓ (GIS Map module platform-wide) |
| Trap/equipment loans | ✓ (equipment loans with deposits, due/return dates, alerts) | ✓ (separate Traps Module: rentals/checkouts, returns, deposits, agreements) | not observed | not observed | — | — |
| Alerts/reminders on operational exceptions | ✓ (unpaid fines, undispatched calls, incomplete incidents, follow-ups due, traps due) | not observed (portal notices for non-compliance) | not observed | not observed | ✓ (renewal reminders; lost pet alerts) | ✓ (renewal reminders) |
| Public-facing surfaces | not observed in AC chapter | ✓ (Portal: stray/found pets, online licensing, citation payments/dismissals) | ✓ (WebLicensing online licensing) | not observed | ✓ (owner portal, tag lookup, lost-pet service) | ✓ (online license application/renewal) |
| Owner-identification support in the field | ✓ (license lookup by number) | ✓ (ID module: microchip records; compliance status) | ✓ (Microchip Lookup) | not observed | ✓ (tag-code lookup; cross-jurisdiction profiles) | ✓ (registered-owner database) |
| Reporting/forms | ✓ (reports; follow-up reporting) | ✓ (extensive reporting and forms generation; ACO narratives) | ✓ (unlimited custom reporting) | ✓ (reporting) | ✓ (robust reporting) | ✓ (platform reporting) |
| Packaging | module of an animal-services suite (removable) | module of a suite; each module can run stand-alone | municipal suite (shelter + field) | suite with municipal plan | standalone licensing network/service | generic gov platform modules |

Reading of the matrix:

- Present in every dedicated animal-services sample (ASM, ShelterPro, Chameleon, ShelterBuddy): incident/call record, officer field response, citations/enforcement, animal+person parties, licensing records. These are the Type's stable structure.
- Present in most but placed differently: licensing (inside the AC module in ASM; a separate integrated module in ShelterPro; a web module in Chameleon; the whole product in DocuPet/GovPilot) and trap/equipment loans (inside AC in ASM; separate module in ShelterPro). Placement varies; existence is common.
- Present in one or two: bite case records (named only in ShelterPro), map of active incidents (ASM; geocoding in ShelterPro), public portals (ShelterPro, Chameleon, DocuPet, GovPilot), compliance→citation automation (ShelterPro).

## Canonical Model (L0–L3)

### L0 — Defining Invariant

An Animal Control Management application is operated by a government authority (or an organization exercising delegated authority) and is built on four inseparable structures:

```text
Animal-related Incident Record (public complaint or officer-initiated call, with location)
└── Officer Field Response Loop
    ├── Dispatch/assignment of an officer
    ├── Field response (on-site action)
    └── Resolution recorded on the incident
├── Animal & Person Parties (animal(s) involved; owner/suspect; complainant; victim)
└── Recorded Enforcement / Impound Actions
    ├── citations / warnings / fines against a person
    └── capture & impoundment of an animal (handoff into custody)
```

1. **Animal-related incident record** — every unit of work is an incident: a complaint, service call, or officer-initiated event about an animal, with call information, location, and a recorded resolution. Without it there is nothing to manage.
2. **Officer field response loop** — the incident moves through dispatch/assignment → field response → recorded completion (with follow-up where needed). Without the field-response loop the product is a request-intake system, not animal control.
3. **Animal & person parties** — each incident names the animal(s) involved and the people on the other side (owner/suspect, complainant, victim), linked to durable animal and person records. Without parties, enforcement and reunification have no counterparties.
4. **Recorded enforcement / impound actions** — the authority's actions are recorded against the incident: citations/warnings with fines (tracked to payment), and capture/impoundment of animals (with handoff into shelter custody). Without enforcement/impound capability the product is a 311 catalog item, not animal control.

Historical/market-sample check (§24-style): the sampled products span ~30 years of deployments (ShelterPro © 1994; ASM open-source lineage from the early 2000s; Chameleon with 20-year municipal installs). All fit the four-element core. The core is incident+response+parties+enforcement — not any modern SaaS pattern (no cloud, portal, or mobile assumption is definitional; ShelterPro delivers field access "via common virtualization technologies", i.e., the loop predates native mobile apps).

Deliberately NOT in L0 (tested and demoted):

- **Pet licensing** — extremely common (5 of 6 samples) but structurally adjacent: ShelterPro ships it as a separate module; GovPilot and DocuPet implement licensing with no field-ops structure at all; ASM's manual treats licensing as a parallel record structure. Licensing is the Type's most common companion, not its definition.
- **Dispatch scheduling mechanics** (zones, shift rosters, priority queues) — the sampled products record dispatch on the incident; none of the fetched documentation shows roster/zone scheduling machinery. The loop (assign → respond → resolve) is invariant; scheduling depth is not.
- **Bite cases / quarantine** — named as a record type in one sample (ShelterPro "Bite Case records"; "Vaccination / Rabies records"); important in practice but not evidenced as a universal structure.
- **Trap/equipment loans** — present in two samples with different placements (inside AC in ASM; separate module in ShelterPro); optional structure.
- **Maps/geospatial** — present in several samples at different depths (minimap, active-incident map, geocoding, platform GIS); an implementation surface, not the definition.
- **Public portals** (online complaints, license renewal, citation payment) — common in current products; absent from older deployments; variant.
- **Shelter custody operations** — the receiving side of impoundment belongs to Animal Shelter Management; the handoff link is part of this Type, the kennel/adoption machinery is not.

### L1 — Common Mature Structure

Present across most sampled products; expected by the market but not definitional:

- Citation/fine lifecycle with due/paid dates and overdue surfacing (alerts, reports, online payment)
- Pet licensing/registration records: number, type, fee, issue/expiry dates, renewal tracking; license history
- Identification compliance tracking: current/expired/missing status across license, vaccination/rabies, microchip; non-compliance notices/citations
- Owner identification support: license-number lookup, microchip lookup, registered-owner databases, cross-jurisdiction profiles
- Jurisdiction/location structures (pickup locations; address mapping/geocoding)
- Alerts/reminders on operational exceptions (undispatched calls, unpaid fines, follow-ups due, expiring items)
- Reporting and forms generation (ACO narratives, citation forms, compliance reports)
- Evidence documentation (photos, document imaging, notes templates)
- Public-facing surfaces: online license application/renewal, stray/found reporting, citation payment
- Integration with shelter custody (incident → animal record taken into shelter)
- Role-based access for officers vs clerical/licensing staff (implied by suite packaging; explicit role detail not fetched)

### L2 — Variant / Optional Structure

Depends on operating model, geography, packaging, or scope:

- Packaging: module of an animal-services suite (ASM, ShelterPro, Chameleon, ShelterBuddy) vs standalone licensing network (DocuPet) vs generic gov-platform modules (GovPilot)
- Operator type: municipal animal services; county animal care & control; contracted humane society/SPCA; police-department-affiliated unit (police affiliation inferred from the field's law-enforcement framing; not directly evidenced in fetched docs)
- Licensing regime: mandatory dog/cat licensing jurisdictions (most North American samples) vs jurisdictions without licensing (licensing structures then absent or vestigial)
- Species scope: domestic pets vs including wildlife calls (not directly evidenced; kept as uncertainty)
- Bite case / rabies quarantine workflows (named record types observed; workflow depth not observed)
- Dangerous-dog designations and court referral workflows (not observed in fetched docs; unverified)
- Public portal depth: read-only listings vs transactional (payments, dismissals)
- Field mobility delivery: virtualized remote access (ShelterPro) vs web-from-any-device (Chameleon) vs native mobile (not observed)
- Regional regimes: North America-weighted licensing/microchip ecosystem; UK/AU variants implied by ASM locale features but not detailed in the AC chapter

### L3 — Vendor-specific Structure

- ASM3: pickup locations as jurisdiction; up to 3 suspects per incident; `ac:`/`li:` search prefixes; trap-loan deposits via payments tab; "non-shelter animal" records for licensed animals; home-page alert bundle
- ShelterPro: module split (AC / ID / Traps / Accounting / Donations); Portal commercial models (non-transactional / transactional / with payments); auto-generated non-compliance citations; online citation dismissals; Pet Detect partner
- Chameleon: WebChameleon/WebLicensing/ScanIt/Quick Kennel/PostMaster; 24Pet network coupling (PetPlace, 24Petwatch, industry data)
- ShelterBuddy: Express/Pro/Gold tiering; Adōpets fundraising tie-in
- DocuPet: HomeSafe tags; national registry; public tag-code lookup; cross-jurisdiction profiles; marketing services for agencies
- GovPilot: Dog/Cat/Pet License as Clerks modules; Report-a-Concern; GovAlert; GIS Map module

## Vendor-specific Findings

See L3. The most consequential vendor pattern is the **suite-module packaging** (animal control as a module of an animal-services suite) — it is the market's dominant shape but must not be read as the Type definition, because the same structures appear in standalone and platform-module shapes. The second is the **licensing-network model** (DocuPet), which outsources licensing as a service; it demonstrates that licensing can be fully industrialized outside any field-ops software.

## Rejected Findings

- "Animal control = shelter management": rejected — both ASM and ShelterPro ship animal control and shelter management as separately purchasable/removable modules; Chameleon's municipal customers use both but the structures (field/enforcement vs custody/care) are distinct.
- "Animal control = pet licensing": rejected — ShelterPro separates licensing into its own module; GovPilot implements licensing with no field-ops semantics; DocuPet runs licensing as a standalone network. Licensing is adjacent and integrated, not definitional.
- "Animal control = generic code enforcement": rejected — the enforcement-case pattern is shared (complaint → response → violation → citation), but the objects differ: animal records, impoundment, bite cases, identification compliance, and reunification have no equivalent in property/ordinance enforcement. GovPilot ships them as separate products.
- "Animal control = 311 / citizen request": rejected — 311 intake is generic; it has no officer dispatch semantics, citations, licensing compliance, or impound. GovPilot's Report-a-Concern coexists with (not replaces) animal-specific structures.
- "Dispatch scheduling (zones/shifts) is the core": rejected as definitional — sampled products record dispatch on the incident; no roster/zone machinery was evidenced. The response loop is invariant; scheduling depth is an implementation.
- "Wildlife control is a defining scope": unverified — no fetched documentation details wildlife handling; species scope varies by jurisdiction. Kept as uncertainty.

## Boundary Findings

1. **vs Animal Shelter Management (§29) — joint review discharged.** The two Types share the animal record and the impound handoff, and municipal products frequently bundle them ("fully supports BOTH your Shelter and Field Services" — Chameleon customer). But the structures are distinct and vendor-separable: ASM ships animal control as an explicitly removable module; ShelterPro sells Animal Control and Shelter Management as separate modules, each usable stand-alone. Structural test: remove field/enforcement (incidents, dispatch, citations) → shelter management remains; remove custody/care (kennels, adoptions, foster) → animal control remains (impound-and-transfer operations still function, with custody handed to an external shelter). Conclusion: two related but distinct Types; the boundary is the operational center (field/enforcement loop vs custody lifecycle), not the shared animal record. No taxonomy change proposed; the directory's split (§24 vs §29) reflects the government-authority vs animal-welfare-operator framing and is defensible.
2. **vs 311 / Citizen Service Request Platform (§24 sibling)** — 311 platforms intake generic non-emergency requests; animal complaints appear as catalog items. Evidence: GovPilot ships Report-a-Concern as a separate module from its animal licensing modules; no 311 product in evidence carries citations, licensing compliance, or impound. Test: remove animal-specific enforcement/licensing semantics → a 311 platform.
3. **vs Code Enforcement Management (§24 sibling)** — same enforcement-case grammar (complaint → field visit → violation → citation → fine), different objects (property/ordinance vs animal/person/impound/licensing). GovPilot ships both as separate products. The shared grammar explains why generic gov platforms can host either; the object model is the boundary.
4. **vs Government Licensing Management (§24 sibling)** — pet licensing is an instance of government licensing; generic platforms implement it as clerks modules (GovPilot) and specialists run it as networks (DocuPet). Licensing without the field/enforcement loop is licensing management, not animal control. The compliance→citation linkage (ShelterPro) is where the two Types touch.
5. **vs Police Records Management / CAD (§24 siblings)** — animal control is often organizationally adjacent to police, and citations are ordinance enforcement rather than criminal cases. The relationship (integration, shared CAD dispatch) was not directly observed in the fetched documentation; recorded as an uncertainty rather than a boundary claim.
6. **vs Public-health rabies programs** — bite cases and rabies records touch public health; the sample shows record types (bite cases, vaccination/rabies records) but no public-health case-management depth. Adjacent, not the same Type.

## Uncertainties

- Dangerous-dog/vicious-animal designation workflows, quarantine order tracking, and court referral flows are standard practice in the profession but were not evidenced in the fetched documentation; no precise claims are made.
- The relationship between animal control software and police CAD/RMS (shared dispatch, record exchange) was not observed; kept generic.
- Wildlife handling scope varies by jurisdiction; no fetched documentation details it.
- PetData (a major licensing-outsourcing vendor) was inaccessible (403 ×2); the licensing pole is covered by DocuPet and GovPilot instead, but the pole may be under-represented.
- Role/permission models inside dedicated AC products were not documented in fetched sources; role statements are kept generic.
- Native mobile field apps: only web/virtualization delivery was evidenced; the current state of native mobile ACO apps is unverified.

## Final Synthesis

Animal Control Management is authority-facing field-operations software for animal-related enforcement and service response. Its world model is: an **animal-related incident record** (public complaint or officer-initiated call, with location and call information) moving through an **officer field response loop** (dispatch → response → recorded resolution, with follow-ups), naming **animal and person parties** (the animal(s) involved, owner/suspect, complainant, victim) linked to durable records, and accumulating **recorded enforcement and impound actions** (citations/warnings with fines tracked to payment; capture and impoundment of animals with handoff into shelter custody). Around this core, mature products add: citation/fine lifecycle management, pet licensing and identification-compliance records (current/expired/missing) with non-compliance notices, owner-identification support (license/microchip/registered-owner lookup), jurisdiction and geospatial structures, exception alerts, reporting/forms, evidence documentation, and public portals (online licensing, stray/found reporting, citation payment). Trap/equipment loans and bite-case records are common optional structures. The Type's boundaries are sharpest against Animal Shelter Management (custody/care operations — the two share the animal record and the impound handoff but are vendor-separable structures), 311/Citizen Service Request (generic intake without enforcement semantics), Code Enforcement (same enforcement grammar, different objects), and Government Licensing (pet licensing as an adjacent, sometimes separately industrialized, structure).
