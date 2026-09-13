# Research Notes — Pet Health Application

## Research Goal

Understand the consumer/caretaker-facing pet health application as an Application Type: what its defining core is, what mature products commonly add, what varies, and where its boundaries sit against the surrounding pet-application family (veterinary practice management, pet DNA platforms, pet insurance customer apps, adoption/shelter, pet services) and against adjacent human-side Types (health tracking, telehealth).

## Pre-hung Duties (from STATUS.md Boundary Issues)

1. **pet-dna-analysis-platform** (processed 2026-09-09) — JOINT-REVIEW FLAG: shared pet-profile vocabulary; seam claimed to be the laboratory loop (DNA platform's unit of record = lab-derived genetic findings via kit→activation→mail-in→analysis; Pet Health Application's unit of record = the animal's day-to-day health state with no lab). DNA products drift toward health content (fitness plans, games, supplements) — drift surface, not identity. Removal test proposed: remove the lab/sample loop from the DNA platform → health-app territory; a health app with no lab never becomes a DNA platform. Also recorded: consumer DNA platforms sell a veterinarian line whose platform side stays in-type; seam vs Veterinary Practice Management is caretaker-collected + risk-framing vs clinic-collected + clinical diagnosis. → Discharged in Boundary Findings #2.
2. **pet-insurance-customer-app** (processed 2026-09-09) — boundary table entry: "Pet Health Application | sibling, shared pet-profile vocabulary | pet health records, reminders, vet advice without an insurance relationship | remove policy + claims; keep records/reminders → Pet Health Application (Figo's Pet Cloud shows the drift surface)". Also: "1 alone [pet profile/account site] = pet profile/account site = Pet Health Application territory". → Confirmed from this side in Boundary Findings #3.
3. **veterinary-practice-management** (processed 2026-09-09) — Boundary Findings #4: "owner-facing consumer record of the animal's day-to-day health or lab-derived findings vs practice-operated clinical system of record; clinic-collected, clinician-attributed, diagnosis-bearing". → Confirmed from this side in Boundary Findings #1.
4. **pet-adoption-platform** (processed 2026-09-09) — forward flag: "shared pet-profile vocabulary, no placement loop — expected clean". → Confirmed clean in Boundary Findings #5.

## Initial Boundary (hypothesis before research)

- What: a consumer application through which a pet's caretaker (owner/family) maintains and works the animal's health state — profile, records, reminders, provider handoff.
- Who: pet owners / caretakers; sometimes the whole household; sometimes connected to veterinary clinics.
- Confusable neighbors: Veterinary Practice Management (clinic-side), Pet DNA Analysis Platform (lab loop), Pet Insurance Customer App (policy/claims), pet-service business systems (grooming/boarding/training), human health-tracking apps, GPS trackers, pet telehealth.
- Unknowns: whether the reminder/care loop is definitional or merely common; whether clinic-anchored companion apps and device-derived monitors are in-type or separate Types; whether telehealth-first products belong.

## Research Questions

1. What is the unit of record — the animal? the household? the visit?
2. Who enters and owns the health data — caretaker, clinic, device, or a mix?
3. What health-state content does the record carry (measurements, care events, documents, observations)?
4. Is there a proactive care loop (reminders/schedules/alerts), and is it definitional or common?
5. How does the record reach the veterinarian (sharing, clinic sync, consultation)?
6. What capabilities are common but not defining (expenses, booking, community, loyalty, telehealth, wearables)?
7. Where are the hard boundaries vs the sibling pet Types and human-side analogs?

## Representative Products

Selected for market representation, documentation completeness, and distinct product philosophies / customer tiers:

| Product | Pole | Philosophy | Evidence tier reached |
|---|---|---|---|
| 11pets | standalone caretaker-maintained tracker | caretaker owns and enters everything; multi-pet; fine-grained sharing | official site home + features page (Tier 1/2) |
| PetDesk | clinic-anchored companion app | records authored in the clinic's PIMS and synced to the owner app | official help center (Tier 1) + app-store listing + about page |
| Tractive | device-derived monitoring (boundary probe) | GPS-first tracker product with a health-monitoring feature layer | official feature page + FAQ (Tier 1/2) |
| Airvet | telehealth-first (boundary probe) | access to licensed vets on demand; now positioned as an employer benefit | official site root (Tier 2) |

Note: whistle.com (Whistle Health, formerly the leading wearable pet-health tracker) now redirects to Tractive — the standalone wearable-health pole has consolidated into GPS-tracker products. Recorded as a market observation.

## Sources

- 11pets — https://www.11pets.com/en/ (home; fetched 2026-09-10), https://www.11pets.com/en/feature (features; fetched 2026-09-10)
- PetDesk — https://petdesk.zendesk.com/hc/en-us/sections/360009821334-Pet-Records-Reminders-Prescription-Labs (help center section), https://petdesk.zendesk.com/hc/en-us/articles/360052833813-Accessing-or-Editing-Pet-Reminder-Prescription-Records (fetched via search 2026-09-10), Apple App Store listing https://apps.apple.com/us/app/petdesk/id631377773, http://petdesk.com/about-petdesk (search-surfaced)
- Tractive — https://whistle.com/pages/whistle-health (redirects to Tractive), https://tractive.com/en/ (root; fetched 2026-09-10), https://tractive.com/en/fp/health-monitoring-for-dogs-and-cats (fetched 2026-09-10)
- Airvet — https://airvet.com/ (root; fetched 2026-09-10)

## Product A — 11pets (standalone caretaker-maintained tracker)

### Key observations (evidence layer A unless noted)

- Positioning: "the most attentive pet-care platform"; "all-in-one pet care solution"; 50+ features; two versions — "11pets: Pet Care for pet owners" and "11pets: Business for pet-care businesses" (the business product is a separate web app for vets/groomers/shelters/trainers/sitters/boarding — confirms this Type's consumer/caretaker orientation).
- **Pet profiles**: "as many pets as you want"; family members can be added with access to a pet.
- **Preventive care**: deworming and vaccinations held in detail; "the application will maintain an automatic schedule and will remind you when the next action is due"; custom categories for additional treatments.
- **Medical records**: x-rays, analyses, tests, blood work; veterinary treatments, medical conditions, allergies, surgeries; medical incidents monitored with photos and notes; "share the complete medical history with any veterinarian or specialist".
- **Hygiene care**: bathing, teeth brushing, nail clipping, ear cleaning; user-defined schedule with due reminders.
- **Meals**: each meal recorded as a task with type/amount; feeding schedule.
- **Medications**: define medication, dosage, frequency; "the application will automatically notify you for every administration".
- **Vet visits**: reason, date/time, professional, price; vet feedback as notes and photos.
- **Sharing**: "Share all the information of your pet with your veterinarian or your caregiver"; fine-grained data-sharing control — "select which data you want to share, of which pet, with who and for how long"; professionals (e.g., vets) can be invited to input data without being platform members; family members access via their own accounts.
- **Sync**: multi-device sync "especially handy when there are different people caring for the same pet"; data stored on the vendor cloud (online-only).
- **Booking**: electronic appointments with professionals (find professional, see services/availability, book).
- **Behaviour monitoring**: log evolution over time; evaluate on characteristics; timeline with notes and photos.
- **Expenses**: per pet, per category; Excel export.
- **Measurements**: track measurements over time; set normal limits; warnings outside range; charts for trends.
- **Calendar sync**: pet-care schedule reflected to device calendars.
- **Community hub** (newer addition): challenges, points, nominating/voting for vets, groomers, shelters; seeing other pets in the area; feedback before booking — social/discovery layer (drift surface).
- Data ownership framing: "you are the owner of your data at all times".

## Product B — PetDesk (clinic-anchored companion app)

### Key observations

- Positioning (owner side): "Healthy pets, happy humans"; "puts you at the center of your pet's health needs by seamlessly connecting you with the best pet care professionals near you"; Google Play name: "PetDesk - Pet Health Reminders".
- **Record authorship is clinic-side**: "Changes cannot be initiated manually by the mobile app user. Records are created and updated within their practice management software on your provider's end… it will update your profile within 24-48 hours"; "Our PetDesk app would need that record on file at the clinic to sync into your profile." The owner app is a synced window onto the clinic's record plus owner-added lightweight content.
- **Pet Records section**: "History and records for your pet, which include health service reminders, medications, and lab results"; reminder records show "what health services your pet may need, or check when they'll be due"; records shareable by email; records can be shared "with your pet care providers".
- **Appointments**: 24/7 appointment request tool to providers.
- **Reminders / to-dos**: synced reminders plus owner-created custom to-dos, calendar sync.
- **Medication requests**: request refills through the app.
- **Providers**: add and view pet-care professionals (veterinary clinics, grooming, boarding, daycare).
- **Loyalty**: points per dollar spent at provider locations (clinic-marketing capability).
- Vendor framing (about page): veterinary-side client-engagement platform that "connects directly to your PIMS"; the owner app is one surface of a clinic communication product. (The clinic-side product belongs to the veterinary-practice-management/client-communication territory; the owner app is the caretaker-facing face of it.)

## Product C — Tractive (device-derived monitoring; boundary probe)

### Key observations

- Product center is the GPS tracker (location, virtual fences); health monitoring is a feature layer: "Advanced health insights in a comfortable tracker they can wear all day."
- Health monitoring content: activity, sleep, resting heart rate, resting respiratory rate; scratching and barking monitoring (dogs); daily insights; health alerts on significant sustained changes; weekly report with AI summary; breed-based comparison ("compare your pet with others of the same breed").
- Baseline-learning model: tracker establishes the animal's baseline after ~7 days of wear; alerts require regular wear (vendor-stated thresholds — kept in research notes, not promoted).
- Explicit non-medical positioning: "Does Tractive diagnose health conditions? No… medical advice and diagnosis should always be sought from a veterinarian"; "Tractive is not a medical device… leaving medical diagnosis where it belongs — in the hands of veterinarians."
- No caretaker-maintained record of care events, documents, or schedules — the data is sensor-derived and monitoring-shaped, not record-keeping-shaped. The pet profile exists (device-bound), but the longitudinal health record in the record-keeping sense is absent.
- Reading: the device-derived data source is a real variant input for pet-health products, but a GPS-first product whose center is location is a different product Type; its health-monitoring capability is the overlap zone.

## Product D — Airvet (telehealth-first; boundary probe)

### Key observations

- Positioning (current): "Pet benefits reimagined" — an employer-sponsored pet benefit; "24/7 on-demand virtual veterinary care with licensed providers"; online pharmacy; in-person partnerships; family sharing; wellness plans; life-stage care; multiple languages.
- Consumer value framing: consultations that "prevent an unnecessary in-person vet visit"; guidance "anytime".
- No caretaker-maintained longitudinal health record at the center; the record exists to support consultation. The center is access to veterinary professionals.
- Reading: telehealth-centered pet products are a different center of gravity (consultation access); the health record is supporting. Pet telehealth has no directory leaf (the §22 Telehealth Platform leaf is human-care); recorded as a boundary pole, not a taxonomy conflict.

## Cross-product Comparison

| Structure | 11pets | PetDesk | Tractive | Airvet |
|---|---|---|---|---|
| Animal profile of record | yes (multi-pet, family access) | yes (per-pet profiles, clinic-linked) | yes (device-bound pet) | yes (pet family) |
| Caretaker-maintained longitudinal health record | yes — full (measurements, care events, documents, incidents) | partial — clinic-authored records synced; owner adds to-dos/notes only | no — sensor-derived monitoring data only | no — record supports consultation |
| Proactive care loop (reminders/schedules/alerts) | yes — schedules + due reminders + medication notifications + measurement-range warnings | yes — clinic-synced service reminders + custom to-dos | alerts only (behavior/vital trend alerts, no care schedule) | life-stage care framing only |
| Provider handoff | share complete history with any vet; invite vets to input data | records shared with providers; appointment requests; refill requests | "talk to your vet" framing; shareable reports | consultation itself is the handoff |
| Data entry actor | caretaker (+ invited professionals) | clinic (records) + caretaker (to-dos) | device (automatic) | vet/professional |
| Expenses | yes | no | no | no |
| Booking | yes (electronic appointments) | yes (24/7 appointment requests) | no | in-person partnerships |
| Community/social | yes (challenges, voting, local pets) | no | share reports with friends/followers | no |
| Loyalty/commerce | no | loyalty points; medication refills | device + subscription commerce | pharmacy; insurance products |
| Non-medical disclaimer | — | — | explicit ("not a medical device") | — |

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The animal profile of record** — an identified individual animal (not a person) held as a persistent record in the application, carrying caretaker-facing identity (name, species/breed, age/birth date, and commonly a weight baseline); the anchor to which all health content attaches. Remove → a generic journal/notes app or a human health tracker.
2. **The caretaker-maintained longitudinal health record** — dated entries of the animal's health state accumulating over time on the animal's record: measurements (weight, vitals), care events (medications administered, vaccinations, treatments, hygiene, vet visits), observations (behavior, symptoms, incidents with photos/notes), and health documents (vaccination certificates, lab results); entered by the caretaker and/or synced from providers or devices, but held and controlled in the caretaker's application. Remove → a pet profile card / address-book entry; if the clinic holds it instead, it is the veterinary record.
3. **The active care loop** — the record is worked, not just stored: recurring care actions are tracked with due states and surfaced (reminders, schedules, alerts, current-status view), and the record is made usable in care decisions — most commonly by being shareable with a veterinarian or other providers. Remove → a static archive nobody acts on, or a bare reminder app with no health record.

Jointly-held load-bearing tests:

- 1 alone = pet profile card / social pet profile
- 2 without 1 = anonymous health log
- 3 without 1+2 = generic reminder/to-do app
- 1+2 without 3 = records vault (thin pole, still marginally recognizable — see Uncertainties)
- 1+3 without 2 = reminder app with pet names and no health content
- 2+3 without 1 = generic health tracker

### L1 — Common Mature Structure

- Multi-pet household management (several animal profiles under one caretaker account)
- Multi-user household access (family members with their own accounts; shared care)
- Sharing/handoff of the record to veterinarians or other providers (export, email, in-platform sharing, clinic sync)
- Appointment booking / appointment requests with providers
- Calendar sync of the care schedule
- Trend views (charts of measurements/weight; behavior timelines)
- Cloud sync across devices
- Data-ownership/privacy framing (who can see and share what)

### L2 — Variant / Optional Structure

- Data-entry substrate: caretaker-entered (standalone pole) vs clinic-synced (companion pole) vs device-derived (wearable/tracker pole) vs consultation-supported (telehealth pole) — and combinations
- Species breadth (dog/cat-centric vs exotics; regional differences)
- Expense tracking and export
- Community/social layers (challenges, voting, local discovery, sharing reports with followers)
- Telehealth / vet chat access
- Medication refill requests; pharmacy
- Insurance products / wellness plans attached
- AI-derived insights, breed-norm comparisons, weekly reports
- Booking marketplaces / provider directories
- Business-side sibling products (same brand selling an operator-side product to pet-care businesses — separate product, separate Type territory)
- Local-only vs cloud storage; online-only vs offline

### L3 — Vendor-specific (kept out of the final document)

- 11pets: community hub mechanics (challenges, points, nominations), fine-grained share-scoping wording, Excel export, "50+ features" claim, online-only cloud storage, business-version split.
- PetDesk: 24–48h sync window, records editable only in the clinic's PIMS, loyalty points per dollar, "12,000+ practices" claim, "10 million additional years of pet life" vision, two-way texting from clinic dashboard.
- Tractive: baseline-learning windows (7-day baseline, 12h/day wear, 6-week alert horizon — vendor-stated), 42,000+ health alerts in 2024, 650+ breeds, VetMed Vienna / Max-Planck partnerships, AI weekly summaries, scratch/bark monitoring specifics.
- Airvet: employer-benefit positioning, utilization/NPS/ROI claims, LegitScript/SOC 2 seals, enterprise client list.

## Anti-overfitting notes

- **Reminders are NOT definitional in their modern form** — the paper-era analog (vaccination booklet + the owner's own care routine, with recalls living in the vet's postcard system or the owner's calendar) satisfies the record and the "worked record" idea without in-app notification machinery. The invariant is the *worked record* (due states, current status, actionable care), not push notifications.
- **Cloud sync is NOT definitional** — local-only storage satisfies the core.
- **Multi-pet is NOT definitional** — single-animal apps in-type.
- **Sharing with vets is NOT definitional as a mechanism** — the record's use in care decisions is the invariant; sharing is the common realization.
- **Device-derived data is NOT definitional** — caretaker entry is the base substrate; devices are a variant source.
- **Telehealth is NOT definitional** — consultation-centered products are a different center of gravity.
- **Expenses, community, loyalty, booking are NOT definitional** — capability layers.
- **The clinic-anchored companion app is in-type** — the record is still held in the caretaker's application (synced), the caretaker still works the care loop; the authorship substrate differs, not the structure. (PetDesk's owner app satisfies all three legs.)
- **The GPS-first tracker product is NOT this Type** — its center is location; health monitoring is a feature. Boundary, not variant.

## Boundary Findings

1. **vs Veterinary Practice Management (processed sibling; confirmed from this side)** — the practice's operator-side clinical-business system of record (client-and-patient two-level record, clinical encounter loop producing attributed diagnosis-bearing documentation, client-account billing loop) vs the caretaker-facing consumer application (caretaker-held record, no diagnosis authority, no billing loop). Clinic-collected/clinician-attributed vs caretaker-collected/caretaker-controlled. Clinic-anchored companion apps sit on the seam: the clinic authors records, but the caretaker's app holds the consumer-facing record and care loop — in-type. Remove the clinic operation and billing → this Type; move record authorship and diagnosis into the operator's system → Veterinary Practice Management.
2. **vs Pet DNA Analysis Platform (JOINT-REVIEW FLAG DISCHARGED — keep-both RATIFIED)** — confirmed from this side exactly as the DNA pass predicted: the DNA platform's unit of record is lab-derived genetic findings produced by the kit→activation→mail-in→analysis cycle (one production event per test, record maintained thereafter); this Type's unit of record is the animal's ongoing health state (logs, measurements, care events, reminders, vet records) with no lab loop. DNA products drift toward health content (fitness plans, games, supplements) — drift surface, not identity. Removal test holds both ways: remove the lab/sample loop from a DNA platform → health-app territory; a health app with no lab never becomes a DNA platform. The DNA pass's second observation also confirmed: the caretaker-collected + risk-framing vs clinic-collected + clinical-diagnosis seam vs Veterinary Practice Management holds for this Type as well.
3. **vs Pet Insurance Customer App (processed sibling; confirmed from this side)** — the insurance app's defining core is the policy/coverage of record + claim filing anchored to a veterinary bill + the claim-to-money loop; this Type has records, reminders, and provider handoff with no insurance relationship. The insurance pass's "pet profile/account site = Pet Health Application territory" reading is confirmed: a pet profile with health records but no policy/claims is this Type's territory. Figo-style "Pet Cloud" record storage inside an insurance app is the drift surface, not identity.
4. **vs Pet Adoption Platform / Animal Shelter Management (processed siblings; expected clean — confirmed)** — placement/custody lifecycle vs health-state record; shared pet-profile vocabulary only. No placement loop exists in this Type; no health record is the shelter's unit of record.
5. **vs the pet-service business family (grooming/boarding/daycare/training/dog-walking/pet-care-business)** — operator-side service-delivery business systems vs caretaker-side health record. Booking and provider directories appear in this Type as capabilities (11pets electronic appointments; PetDesk provider list), and the veterinarian appears only as a data source/handoff target, never as a clinical workflow — mirroring the veterinary pass's finding for the non-clinical service family.
6. **vs GPS tracker products (Tractive pole)** — location-centered products with a health-monitoring feature layer vs health-centered applications. The device-derived data source is a legitimate variant input for in-type products, but a product whose center is live location (virtual fences, escape alerts) is a different Type. Market observation: the standalone wearable-health pole (Whistle) has consolidated into GPS-tracker brands (whistle.com → Tractive).
7. **vs pet telehealth products (Airvet pole)** — consultation-centered (access to licensed vets on demand, pharmacy, wellness plans) vs record-centered. Telehealth appears in-type as an optional capability; when the consultation is the center and the record merely supports it, the product is telehealth-shaped. No directory leaf exists for pet telehealth; recorded as a taxonomy observation.
8. **vs human health-tracking / wearable fitness applications** — same structural rhyme (subject profile + longitudinal measurements + trends + goals), different subject: the animal, acted for by a human caretaker who is not the patient. The caretaker-proxy relationship and the veterinary handoff are the discriminators.
9. **vs Lost Pet Platform (processed sibling)** — recorded reunion (lost/noticed events, search, sighting network) vs ongoing health state; different unit of record, no shared workflow.
10. **Removal tests**: remove the animal-of-record → human health tracker or generic journal; remove the longitudinal record → pet profile card; remove the care loop → records vault; move record authorship + diagnosis + billing to the clinic side → Veterinary Practice Management; add a lab loop → Pet DNA territory; add policy + claims → Pet Insurance Customer App territory.

## Historical / Market-Sample Check

- **Paper vaccination/health booklet (the "pet passport" generation)**: an identified animal's booklet held by the owner, recording vaccinations, treatments, weight; consulted to decide care; schedule pages in many booklets; handed to the vet at visits. Satisfies the animal-of-record + caretaker-maintained record + worked-record legs at analog level (the reminder machinery lived in the vet's recall postcards and the owner's calendar, not in the artifact). Confirms the core is era-independent and not over-fitted to app-era notification mechanics.
- **Vet-issued reminder/recall systems (postcards, calls)**: the proactive loop existed pre-app, but operated by the clinic — confirms that the *care loop* is the Type's structure while *who operates the reminder machinery* is a variant (clinic-synced reminders as in PetDesk are the modern realization, not a new structure).
- **Kennel-club / breeding record cards**: husbandry records for breeding purposes, not day-to-day health care — correctly outside (different purpose and audience).
- **Human health record booklets / baby books**: same genus, different subject — the animal subject + caretaker-for-animal relationship is the discriminator.
- Check passed: the definition does not over-fit the modern cloud, multi-pet, notification-rich implementation.

## Uncertainties

- The records-vault pole (records without an active care loop): no sampled product sits cleanly there (PetDesk's owner app carries synced reminders; 11pets is loop-rich). Whether a pure records-access app would still be recognized as this Type is held as an open question; the L0's third leg is written as "the record is worked" rather than "in-app push reminders" to keep such a pole marginally in-type.
- Airvet's pet-parent surface was evidenced at root-page depth (employer-benefit positioning); its in-app record/reminder mechanics were not observed. No claims made about its in-app structure.
- PetDesk's non-clinic-linked usage (whether the app is usable without a partnered provider) is not evidenced from the fetched articles; the clinic-anchored reading is held at the strength of the help-center evidence.
- Tractive's vendor-stated thresholds (7-day baseline, 12h/day, 6 weeks) are marketing/support-page claims; recorded here only, not carried into the final document.
- Regional products (EU pet-passport-linked apps, Japanese/Chinese pet apps) unsampled; species breadth beyond dog/cat unverified.
- No authenticated in-app screens were observed for any product; all state/permission descriptions are conceptual.

## Final Synthesis

A Pet Health Application is the caretaker-facing application of record for an individual animal's health: the animal is the unit of record; the caretaker maintains a longitudinal health record on that animal (measurements, care events, observations, documents — entered directly, synced from providers, or derived from devices); and the record is actively worked — recurring care tracked with due states and surfaced as reminders/schedules/alerts, and the record made usable in care decisions, most commonly by being shareable with a veterinarian. Around this core, mature products add multi-pet households, family access, booking, trend charts, calendar sync, and fine-grained sharing; variants add device-derived monitoring, telehealth, expenses, community layers, and insurance attachments. The defining seams: clinic-operated clinical systems (veterinary practice management) hold the diagnosis-bearing record and the money loop; DNA platforms run a lab loop this Type never has; insurance customer apps bind the record to a policy and claims; GPS trackers center location; telehealth products center consultation. The paper vaccination booklet satisfies the core at analog level — the Type is era-independent.
