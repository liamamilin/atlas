# Research Notes — Livestock Management

Research date: 2026-09-09
Leaf: Livestock Management (DIRECTORY §20 Agriculture, Food & Natural Resources)
Slug: livestock-management

## Research Goal

Understand what the generic livestock-management Application Type is, from real products: what its system of record holds, what users do with it, how the production cycle flows through it, and where it ends relative to the specialty livestock leaves (dairy, poultry, swine), the feed discipline, and the whole-farm platform.

## Initial Boundary Hypothesis

- Core use: manage a terrestrial livestock population (beef cattle, sheep, goats, multi-species) as records — identity, breeding, health, performance, movements, purchases/sales — and convert those records into management decisions.
- Users: ranchers / livestock producers, herd managers, farm hands, consultants/vets.
- Nearest neighbors (from sibling passes already processed):
  - **Dairy Farm Management** (processed 2026-09-07): its defining rhythm is the individual lactation/milking cycle; the pass explicitly recorded "remove the lactation/milking production cycle → generic Livestock Management", and described livestock as managing beef/sheep "by growth/breeding cycles, often at group level". Uniform ships a separate beef ("suckling herd") product — same vendor, different products.
  - **Feed Management** (processed 2026-09-08): the feed (rations, supply, feeding loop) is the subject there; "products whose unit of record is the individually identified animal belong to herd/livestock management".
  - **Farm Management Platform** (processed 2026-09-08): whole-operation scope (land + crops + livestock + money); "2 alone = the Crop/Livestock Management capability slices" — livestock management is what remains when whole-operation scope is removed.
  - **Aquaculture Management** (processed): structurally closest cousin but water-environment + per-unit populations; livestock is terrestrial.
  - Dairy pass naming-drift note: assign Types by center of gravity (animals + events + cycles), not vendor category labels; herd system of record and sensor/parlor data layer are separable roles.
- Expected L0 shape: animal population as unit of record + dated event stream + records→decisions loop. Individual identity suspected NOT definitional (beef/sheep often managed at mob/group level).

## Research Questions

1. What is the unit of record — the individual animal, the mob/group/flock, or both? At what granularity is identity held?
2. What event/record vocabulary does the system carry (breeding, calving/lambing, weaning, treatments, weights, movements, purchases/sales/deaths)?
3. How does the production cycle flow through the system (breeding → pregnancy → birth → weaning → growth → sale/cull)?
4. How do records become decisions (reports, performance measures, worksheets, work lists)?
5. Where do hardware (EID readers, scales) and land (paddocks/pastures) sit — core or layer?
6. Where is the boundary with dairy, poultry/swine, feed, whole-farm platforms, and breed-association registries?
7. Would older/regional products (paper herd books, desktop herd software) still fit the definition?

## Representative Products

| Product | Pole | Customer tier / geography | Evidence strength |
|---|---|---|---|
| AgriWebb | livestock-led; mob-level AND individual-animal platforms (sheep & beef) | Large pastoral + mid ranches; AU/UK/global | A — official help center (full collection trees fetched) |
| CattleMax | individual-animal-centric cattle records (cow-calf, commercial + registered) | US/Canada ranches, small→large; since 1999 | A — official product pages + help center root |
| Herdwatch | mobile-first multi-species (cattle + sheep), calving-book origin | US/IE/UK ranchers, 20k+ producers | B — official product pages (help center not fetched) |
| Farmbrite | whole-farm suite with a livestock module (slice pole) | Small diversified farms worldwide, multi-species | B — official product + FAQ pages (docs site unreachable this pass) |

Selection rationale: two record-granularity poles (group-first AgriWebb Mob vs individual-first CattleMax), one mobile-first multi-species pole (Herdwatch), one whole-farm slice pole (Farmbrite). Covers beef cattle + sheep (the core of generic livestock), different product philosophies, different customer tiers, different geographies. VAS checked for a feedlot pole — vendor site is dairy+feed only; no beef product; pole dropped (see Uncertainties).

## Sources

- AgriWebb Help Center root — https://help.agriwebb.com/en/ (fetched 2026-09-09)
- AgriWebb Mob Management collection — https://help.agriwebb.com/en/collections/804704-mob-management (fetched)
- AgriWebb Individual Animal Management collection — https://help.agriwebb.com/en/collections/1971527-individual-animal-management-iam (fetched)
- CattleMax product site — https://www.cattlemax.com/ , https://www.cattlemax.com/cattle-records (fetched)
- CattleMax Help root — https://help.cattlemax.com/ (fetched)
- Herdwatch site — https://herdwatch.com/ , https://herdwatch.com/solutions/cattle-management-software/ (fetched)
- Farmbrite site — https://www.farmbrite.com/ , https://www.farmbrite.com/livestock (fetched)
- VAS site — https://www.vas.com/ (fetched; dairy+feed only — used to rule out a beef/feedlot pole)
- Sibling research notes: research/dairy-farm-management.md, research/feed-management.md, research/farm-management-platform.md (boundary seams)

Source-access limitations: docs.farmbrite.com returned a transport error this pass (reachable in the 2026-09-08 FMP pass); Farmbrite claims rest on official product/FAQ pages (Tier 2). Herdwatch help center not fetched; Herdwatch claims rest on official product pages (Tier 2). No feedlot-specific vendor documentation fetched; feedlot machinery claims avoided.

## Product Observations

### AgriWebb (evidence layer A — help center)

Two platforms for the same livestock world, sold as separate editions:

- **Mob Management** (group-level): livestock held as mobs with counts. Record types directly observed: creating records; movement records (between paddocks); draft & split; merge; livestock transfers between farms; recount record ("easily adjust livestock numbers"); weight records; assumed daily gain (ADG) projection; body condition score; purchase records; sale records (with market performance details); death records; treatments (vaccinations); feed records; tagging records; wool harvest records (shearing/crutching); worm test records (WEC/FEC); fertility records: joining (drag & drop), pregnancy scanning, marking (lamb/calf), weaning, castrate & spay; ageing up livestock; enterprises and management groups; management tags; mob activity & history summary.
- **Individual Animal Management (IAM)** (individual-level, EIDs/VIDs): livestock list; animal details & history per animal; live sessions in the yards (crush-side processing of a group of animals with templates, drafting); records: movement, observation, weight, ADG, feed, tagging, treatment, TB test, joining & natural service, artificial insemination, pregnancy scanning, birth (incl. bulk birth), weaning, death, sale, purchase, transfers, wool harvest, worm test, BCS, castrate & spay, embryo-transfer workaround; hardware: supported EID readers and scale heads (Gallagher, Tru-Test, Te Pari, FarmXL), Bluetooth/WiFi connection, live-session hardware configurations; show livestock on the farm map; bulk CSV update.
- Other collections: paddock records & grazing management; livestock/feed/chemical inventory (treatments, vaccines, semen, embryo, feed, fertiliser, spray; cost of production); reports & data-driven decisions; farm calendar & team management; sustainability program hub; marketplace/integrations.

### CattleMax (evidence layer A — product pages + help root)

- Positioning: "North America's most widely used cattle software"; cloud-based; ranch records in one place; commercial + registered cattle editions.
- Cattle records: cattle inventory via **groups** ("sort animals based on specific criteria… accurate and up-to-date inventory"); herd health (vaccinations, antibiotics, treatments — "whether you have 10 animals or 5000"); breeding & pregnancy (heat cycles, AI, pregnancy checks, natural service, embryo transfers, production status, calving history); calving entry on mobile in the pasture; group-based weaning (weights → Average Daily Gain and performance numbers); reports and **worksheets** (printed worksheets for working cattle when cell service unavailable).
- Ranch records (beyond cattle): pasture management, equipment maintenance, financial records, rainfall tracking, calendar & tasks, customer management.
- Integrations: EID readers, weigh scales, **breed association interfaces** (import pedigrees and EPDs; register calves from calving records — "no double entry"); industry partners (Tru-Test, Gallagher, Zoetis, Neogen…).
- Help center structure: Animal Records & Data; Herd Management; Reporting & Analytics; Equipment & Scales Integration; Breed Interfaces (US/Canada/AU/NZ breed societies).

### Herdwatch (evidence layer B — product pages)

- Self-labels "Livestock Management Software"; three solutions in one app: Cattle, Sheep, Pasture. 20,000+ producers; 2.3m cattle, 3.5m calf births, 1.7m sheep in app.
- Cattle solution: digital calving book (record calves, sires, dams, birth weights; offline; cow families → replacement and culling decisions); health records (pulls and treatments, protocols, medicine inventory); herd management ("manage cows individually or in groups"; weaning weights, feed purchases, pasture moves, sales); breeding (heats, breeding dates, repeats, pregnancy results; calving window, open cows); reporting (calving summaries, breeding results, weight gain trends, sales history; "which cows are making you money").
- Platform traits: phone/tablet/desktop; offline with sync; multiple users on the same herd; Bluetooth EID reader and scale-head integration; free herd-data upload by the vendor team; breed association exports; free digital calving book tier.
- IE/UK sites carry the compliance angle (farm compliance and regulation searches; remedies recording in those markets).

### Farmbrite (evidence layer B — product + FAQ pages)

- Whole-farm suite; "Livestock Management" is one capability beside task management, crop planning, accounting, mapping, climate, commerce, reporting.
- Livestock module: animal records with wellness (treatment schedules, plans, tasks, reminders, **withdrawals**); productivity & yield (growth, feed conversion, measurements); breeding & genealogy (select animals for breeding factors, pedigree reports to vets/breed associations/buyers); grazing insights (grazing days auto-calculation, rotations, paddocks, animal movements, hay production).
- Multi-species: cattle/cow-calf, sheep, goats, pigs, poultry, horses, bees, specialty; "track your herd or flock as one production group where you don't need to track each animal's data, as well as with basic and smart groups"; individual + group records; RFID scanning; team/vet/accountant collaboration with roles; offline recording; plans sized by active animal count.
- FAQ workflow: add animals (manual or import with species-specific fields) → record daily events (measurements, health checks, breedings, births, treatments, feeds, yields, movements) → review/compare performance vs expectations → adjust breeding strategies, grazing rotations, health protocols.

### VAS (boundary check only)

- Vendor site is dairy (DairyComp) + feed (FeedComp, WeighComp) only; no beef/feedlot product on the current site. Confirms the dairy pass's finding that dairy vendors ship separate beef products — beef belongs to this leaf's territory, not dairy's.

## Cross-product Comparison

| Structure | AgriWebb | CattleMax | Herdwatch | Farmbrite | Assessment |
|---|---|---|---|---|---|
| Livestock population as persistent records | ✔ (mobs w/ counts; IAM animals) | ✔ (individual animals + saved groups) | ✔ (individual cows; groups) | ✔ (individuals + production groups/smart groups) | Core (all, both granularities) |
| Individual animal identity | ✔ (IAM edition, EID/VID) | ✔ (individual IDs, EID readers) | ✔ (individual cattle IDs) | ✔ (individual records; RFID) | Common pole — NOT definitional (mob/group pole exists without it) |
| Group/mob/flock as managed unit with counts | ✔ (Mob Management edition) | ✔ (groups as criteria-based sets) | ✔ ("individually or in groups") | ✔ (production groups, no per-animal data needed) | Common pole — NOT definitional |
| Dated event records bound to animals/groups | ✔ (movement/weight/treatment/joining/birth/sale/death…) | ✔ (health, breeding, calving, weaning records) | ✔ (calving, treatments, breeding, weights, sales) | ✔ (measurements, health, breedings, births, treatments, feeds, movements) | Core (all) |
| Breeding → pregnancy → birth → weaning cycle machinery | ✔ (joining, AI, scanning, birth, weaning, marking) | ✔ (heat, AI, preg checks, calving, weaning) | ✔ (heats, serves, repeats, calving book) | ✔ (breeding, births, genealogy) | Common mature (feedlot-style ops may not breed) |
| Health/treatment records (+ medicine inventory, withdrawals) | ✔ (treatments; chemical/vaccine inventory) | ✔ (vaccinations, antibiotics) | ✔ (treatments, medicine inventory) | ✔ (treatment schedules, withdrawals) | Common mature |
| Weight/performance recording (weights, ADG, BCS) | ✔ (weight, ADG projection, BCS) | ✔ (weaning weights → ADG) | ✔ (weights, ADG, growth) | ✔ (measurements, growth, feed conversion) | Common mature |
| Purchase/sale/death records | ✔ (purchase, sale w/ market performance, death) | ✔ (sales & purchases) | ✔ (sales & purchases) | ✔ (sales; yields) | Common mature |
| Movement between land units (paddocks/pastures) | ✔ (movement records; farm map) | ✔ (pasture management) | ✔ (pasture moves; pasture solution) | ✔ (movements, rotations) | Common mature (location context) |
| Records → decisions (reports, performance, worksheets) | ✔ (reports collection; activity history) | ✔ (reports & worksheets) | ✔ (reports; "which cows are making you money") | ✔ (100+ reports; compare vs expectations) | Core (all) |
| EID/RFID + scale hardware integration | ✔ (readers, scale heads, live sessions) | ✔ (EID readers, scales) | ✔ (Bluetooth EID, scale heads) | ✔ (RFID scanners) | Common mature |
| Breed association / pedigree interfaces | — (not observed in fetched pages) | ✔ (pedigrees, EPDs, registration) | ✔ (breed association exports) | ✔ (pedigree reports) | Common (registered-herd pole) |
| Mobile/offline capture at the animal | ✔ (mobile app, yards) | ✔ (mobile, worksheets offline) | ✔ (offline-first) | ✔ (offline, voice-to-text) | Common mature |
| Wool harvest (sheep-specific) | ✔ (shearing/crutching) | — | — (sheep solution exists; detail unfetched) | — | Variant (species-dependent) |
| Compliance/regulatory reporting | ✔ (sustainability hub; AU/UK context) | — | ✔ (IE/UK compliance angle) | ✔ (compliance reporting claim) | Variant (regional) |
| Grazing/pasture planning depth | ✔ (paddock records & grazing collection) | ✔ (pasture management) | ✔ (pasture solution) | ✔ (grazing insights) | Optional layer |
| Feed/ration machinery | ✔ (feed records, feed inventory) | — (feed purchases only) | ✔ (feed purchases) | ✔ (feeds, feed conversion) | Optional layer (→ Feed Management) |
| Whole-farm embedding (crops, accounting, commerce) | — (livestock-led) | ✔ (ranch financials, equipment) | — (pasture only) | ✔ (full suite) | Variant (packaging) |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures:

1. **The livestock population as the managed unit of record.** The system holds the animals being raised as persistent records — as individually identified animals, and/or as groups/mobs/flocks carrying counts — organized by species, age class, and breeding status. Remove → an animal address book or static herd register; or the subject stops being animals at all (crop/field tool).
2. **The dated event/record stream bound to that population.** Every management action and observation is captured as a dated, attributed record attached to the animals/groups it concerns: breeding and reproduction events, births, weaning, health treatments, weights/condition observations, movements, purchases, sales, deaths. Remove → a bare head-count ledger; the "management" content is gone.
3. **The records → decisions loop.** The accumulated records are continuously converted into management output — performance measures (growth, reproduction, sale outcomes), reports, and work lists/worksheets — that drive which animals to breed, treat, move, cull, or sell. Remove → a passive archive (herd book), not a management system.

Jointly-held is load-bearing:
- 1 alone = animal address book / static herd register
- 2 without 1 = free-floating event log
- 3 without 1+2 = generic reporting tool
- 1+2 without 3 = herd book/archive (the "management" gone)
- 2+3 without 1 = task/reporting tool with no animal population

Anti-overfitting: **individual animal identity is NOT definitional** — AgriWebb's Mob Management edition and Farmbrite's production-group mode manage livestock at group/count level without per-animal records, and both are unambiguously livestock management. The invariant is the population held as records *at some granularity*; individual identity (EID-driven) and group/count management are the two market poles. Likewise **no specific event type is definitional by itself** (a finishing operation may never breed; a stud operation may never purchase) — the invariant is that the system carries the event vocabulary of the livestock cycle and records events against the population.

### L1 — Common Mature Structure

- Individual animal identity with electronic tags (EID/RFID) and tag lifecycle (add/replace/remove records)
- Groups/mobs/flocks as managed units: draft/split, merge, recount, transfers between farms
- Breeding & reproduction machinery: heat/joining records, AI/natural service, pregnancy scanning, birth/calving/lambing records, weaning
- Health machinery: treatment records, medicine/vaccine inventory, withdrawal tracking
- Performance recording: weights, average daily gain (incl. projected/assumed gain), body condition scoring
- Inventory transactions with commercial detail: purchases, sales (with market performance), deaths
- Movement records against the operation's land units (paddocks/pastures); livestock shown on the farm map
- Reports and worksheets; performance analysis (conception/calving rates, pounds weaned, sale outcomes)
- Hardware integration: EID readers, scale heads (Bluetooth/WiFi), chute-side capture
- Mobile/offline capture at the animal (pasture, yards/chute); multi-user access; vendor-assisted herd import
- Breed association interfaces for registered herds (pedigree/EPD import, registration export)

### L2 — Variant / Optional Structure

- Species scope: cattle-only vs cattle+sheep vs multi-species (goats, pigs, poultry, horses, bees, specialty)
- Record-granularity packaging: mob-level vs individual-level as separate editions of one product
- Registered/pedigree pole (EPDs, pedigree reporting, registration workflows) vs commercial pole
- Regional compliance machinery (IE/UK remedies recording, national database links, AU/NZ programs)
- Species-specific events (wool harvest/shearing, marking, castration/spay)
- Grazing/pasture planning depth (rotational planning, grazing-day calculation, hay)
- Feed layer depth (feed records/inventory → full ration discipline belongs to Feed Management)
- Whole-farm embedding (crops, accounting, commerce, tasks in one suite) vs livestock-led standalone
- Sustainability/program overlays; sensor/IoT data ingestion
- Deployment: cloud web+mobile vs desktop; offline-first vs connected

### L3 — Vendor-specific (Research Notes only)

- AgriWebb: Live Sessions (template-driven chute-side processing), Enterprises & Management Groups, OptiWeigh bulk weight upload, Pastoral muster preparation, Sustainability Program Hub, Marketplace
- CattleMax: TagMax app, printed weaning/breeding worksheets, breed-interface editions (US/Canada/AU/NZ societies), ranch-side extras (rainfall, equipment maintenance, customer management)
- Herdwatch: free digital calving book tier, vendor-done herd upload, VetDrive acquisition (veterinary practice software — separate category), IE/UK compliance editions
- Farmbrite: smart groups (rule-based auto-grouping), voice-to-text entry, plan tiers sized by active-animal count, Zapier/API integrations

## Vendor-specific Findings

See L3. Additionally: Herdwatch and CattleMax both market "rancher-based support" and vendor-performed data migration — onboarding services, not structural. CattleMax's comparison pages (vs paper records, vs spreadsheets, vs breed association software) confirm the competitive frame of this Type: replacing paper herd books and spreadsheets, and coexisting with association registries.

## Boundary Findings

- **vs Dairy Farm Management**: dairy's defining rhythm is the individual lactation/milking cycle with milk production attributed to lactations. Remove the lactation/milking cycle → this Type. Corroborated: VAS (dairy vendor) ships no beef product; the dairy pass recorded Uniform shipping a separate beef product. Dairy is the individual-identity pole taken further (per-lactation production); generic livestock manages growth/breeding cycles, often at group level.
- **vs Poultry Farm Management / Swine Management** (leaves unprocessed): those industries run batch/flock production (all-in/all-out, per-unit populations); the dairy pass and aquaculture pass both characterize them as population/batch-based. This Type's center of gravity is beef cattle/sheep/multi-species with long-lived breeding animals. **Flag for joint review** when those leaves are processed: the seam is production-system shape (long-lived individual/breeding herds vs short-cycle batch flocks), not species lists.
- **vs Feed Management**: the ration, feed supply and feeding loop are the subject there; animals appear as groups being fed. Here the animal population is the subject; feeding appears as a layer (feed records, feed purchases, feed inventory). Test holds both directions (feed pass recorded the mirror image).
- **vs Farm Management Platform**: whole-operation scope (land + crops + livestock + money + work) vs animal-population scope. Remove whole-operation scope from FMP → the livestock slice = this Type. Farmbrite straddles at packaging level (whole-farm suite with a livestock module) — center-of-gravity test applies (per the dairy pass naming-drift note).
- **vs Agricultural IoT Platform**: sensor/telemetry fleet vs animal/event system of record. EID readers and scales are capture hardware for records here, not a device-fleet management product.
- **vs Aquaculture Management**: terrestrial animals vs water-environment rearing units; aquaculture manages per-unit populations (pools/cages) with water parameters; livestock manages long-lived terrestrial herds/mobs.
- **vs breed association registries / genetics databases**: the association's registry is a data partner (pedigree/EPD import, registration export), not the farm's management system. CattleMax's own comparison page frames breed association software as a different product.
- **vs veterinary practice management**: vets are collaborators (shared access, pedigree reports to vets); the clinic-side system of record is a different category (Herdwatch's VetDrive acquisition is a veterinary practice product, kept separate).
- **vs Auction Management System**: sales appear here as events with market performance; the auctioneer's lot/bidder/settlement machinery is a separate Type (processed 2026-09-06).
- **"去掉什么就变成另一个 Type" 判据**: remove the animal population (keep fields/crops) → Farm Management Platform; remove the records→decisions loop → herd book/registry archive; remove event history → head-count ledger; remove the livestock population as subject (keep rations) → Feed Management; add the lactation/milking production cycle as the defining rhythm → Dairy Farm Management; move to water-environment per-unit rearing → Aquaculture Management.

## Historical / Market-Sample Check (§24)

- Paper-era practice: a herd book (breeding females with tags, ages, pedigrees), a calving/lambing book, a treatment log, weaning-weight sheets, and an annual culling/selling decision — satisfies all three L0 structures with no cloud, mobile, EID, or AI. The definition holds for the pre-digital lineage.
- Older desktop herd software (1990s–2000s generation, e.g. the lineage CattleMax grew from in 1999) satisfies: animal records, event history, reports — no cloud/mobile/hardware in the core.
- Regional products (AU/NZ pastoral mob management, IE/UK compliance-first apps, US cow-calf record keepers) all satisfy without naming any specific regime, tag standard, or geography in the core.
- Group-level management (mobs with counts) is not a modern regression — it is the traditional pastoral form; individual EID management is the newer pole. Both fit; neither is definitional.

## Uncertainties

- Herdwatch's help center was not fetched; its record taxonomy is documented from official product pages (Tier 2). Claims about Herdwatch kept at product-page strength; no precise operational details asserted.
- docs.farmbrite.com unreachable this pass (transport error; reachable 2026-09-08 in the FMP pass). Farmbrite claims rest on official product/FAQ pages (Tier 2).
- No feedlot/finishing-specific vendor documentation fetched (VAS has no beef product; no feedlot vendor sampled). Feedlot-style operations are covered only via the group/count pole (AgriWebb mobs, Farmbrite production groups) and the feed-management pass. No feedlot-specific machinery (pen-level performance, close-outs) is claimed for this Type.
- Poultry/swine leaves unprocessed; the batch-vs-breeding-herd seam is stated from sibling-pass evidence and Farmbrite's multi-species positioning, pending joint review.
- Breed-association interface depth varies (CattleMax strongest evidence); treated as common-mature for the registered pole, not universal.

## Final Synthesis

Livestock Management is the livestock producer's animal-population system of record and daily management console. Its defining core is three jointly-held structures: the livestock population held as persistent records (individual animals and/or groups/mobs/flocks with counts); the dated event stream bound to that population (breeding, births, weaning, health treatments, weights/condition, movements, purchases/sales/deaths); and the loop that converts accumulated records into management output — performance measures, reports, worksheets, work lists — driving which animals to breed, treat, move, cull, or sell. Individual electronic identity, the breeding-cycle machinery, hardware integration, pasture context, compliance, and feed layers are common mature or variant structures, not the definition. The Type is the generic residue beside its specialties: dairy (lactation cycle), poultry/swine (batch flocks), aquaculture (water units) — and the animal-side slice of the whole-farm platform.
