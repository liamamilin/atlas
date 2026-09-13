# Research Notes — Research Animal Facility Management

Research date: 2026-09-09

## Research Goal

Understand what a Research Animal Facility Management application actually is, from real products: what objects exist inside it (animals, cages, colonies, protocols), how the daily operational loop works (census, husbandry, breeding, health), how research governance (approved protocols) binds to the animal population, how facilities recover costs, and where the Type's boundaries lie against the IACUC/ethics platform, Biobank Management, LIMS, Scientific Core Facility Management, Livestock Management, and Animal Shelter Management.

## Initial Boundary (pre-research hypothesis)

- Core purpose: operational system of record for a research animal facility (vivarium) and the colonies it hosts — animal records, housing/cage locations, breeding/colony management, protocol linkage, census, health/veterinary records, ordering, per-diem billing.
- Primary users: animal caretakers/technicians, vivarium managers, veterinarians, principal investigators and lab members, compliance staff, billing staff.
- Likely confusions:
  - Animal Research Ethics / IACUC Platform (protocol review workflow vs animal operations) — already documented in the atlas; it explicitly defers animal operations to this Type.
  - Biobank Management (preserved specimens vs living animals) — already documented; lists this Type as adjacent.
  - LIMS / Research LIMS (assay/test-centric vs animal-care-centric).
  - Scientific Core Facility Management (service/instrument billing vs husbandry operations; both may bill PIs).
  - Livestock Management (agricultural production vs research context).
  - Animal Shelter Management (custody transfer/adoption vs research custody under protocols).
- Unknowns to resolve: is the central object the animal, the cage, or the colony? Is protocol linkage definitional or common? Is billing definitional? Is breeding machinery definitional or rodent-dominant? Does the lab-level "colony management" pole belong to this Type or is it a separate Type? How do aquatic facilities differ?

## Research Questions

1. What is the central managed object — the individual animal, the cage, or the colony/line?
2. How is housing modeled (rooms, racks, cages, tanks; occupancy; capacity)?
3. How do animals enter (ordering, birth, transfer) and leave (euthanasia, transfer out, export)?
4. What life-cycle states do animals carry, and what drives state changes?
5. How are approved protocols linked to animals, and is usage tracked against approved numbers?
6. What breeding/colony machinery exists (matings, litters, weaning, pedigrees, lines/strains)?
7. What health/veterinary structures exist?
8. How does billing work (per-diem rates, cost accumulation, export/invoicing)?
9. What roles exist and how is data segregated (facility staff vs researchers vs vets)?
10. What variants exist (institutional vivarium vs lab-level colony management vs aquatic vs transgenic)?

## Representative Products

| Product | Vendor | Why selected | Tier of evidence obtained |
|---|---|---|---|
| SoftMouse.NET | Iseehear Inc. (Toronto, Canada) | Leading lab-level colony-management SaaS; free/premium tiers; official online manual (FAQ) reachable — deep operational evidence for the researcher/colony pole | Homepage + official online manual (FAQ) + module pages (official) |
| PyRAT | Scionics Computer Innovation GmbH (Dresden, Germany) | Self-described leading animal facility management software in Europe, stable since 2003; institutional vivarium pole; EU regulatory framing (directive 2010/63/EU) | Product page + Aquatic product page + Add-ons page (official) |
| PyRAT Aquatic | Scionics | Aquatic (fish/zebrafish) facility variant — tests species-specific realization of the same Type | Product page (official) |
| JCMS (JAX Colony Management System) | The Jackson Laboratory (US) | Historical open-source colony management system (MS Access + MySQL + web + mobile); tests whether the Type holds for an older, non-SaaS, lab-level generation | jax.org product page + GitHub repository README (official; positioning/structure level) |

Sample structure: lab-level SaaS colony pole (SoftMouse.NET) vs institutional European facility pole (PyRAT) vs aquatic variant (PyRAT Aquatic) vs historical open-source lab pole (JCMS). Customer tiers: single labs (SoftMouse FREE), institutions/cores (SoftMouse PREMIUM/Institution, PyRAT campus license), breeding cores, biotech.

## Sources

All fetched 2026-09-09.

- SoftMouse.NET homepage — https://www.softmouse.net/
- SoftMouse.NET FAQ (official online manual) — http://www.softmousefaq.com/ (topic index; individual pages: Mouse States Explained, Track No. of Animals Used)
- SoftMouse.NET Per Diem module page — https://www.softmouse.net/softmouse-best-animal-per-diem-expense-management.jsp (navigation-level only; substantive per-diem detail taken from the FAQ)
- SoftMouse.NET colony features page — https://www.softmouse.net/mouse-colony-software-features.jsp (navigation-level only)
- PyRAT product page — https://www.scionics.com/pyrat
- PyRAT Aquatic product page — https://www.scionics.com/pyrat_aquatic
- PyRAT Add-ons page — https://www.scionics.com/pyrat_add_ons
- Scionics company page — https://www.scionics.com/
- JCMS page (The Jackson Laboratory) — https://www.jax.org/jcms
- JCMS GitHub repository — https://github.com/jaxcs/JCMS-root

Source-access limitation: several major US institutional vivarium vendors were unreachable from the research environment after repeated attempts — Topaz Technologies (topaztek.com, 2 failures), eSirius (esirius.com / esiriusweb.com, 2 failures), Mosaic Vivarium (mosaicvivarium.com, 2 failures). Instem's former animal-facility product line is no longer visible as a distinct product on its current site (folded into study management). LabKey's animal-management solution page returned 404; LabWare is a general LIMS with no visible animal-facility product. AniLog (anilog.co.uk) was fetched but is animal-welfare-sector software (shelters/boarding/veterinary) — used as a boundary data point only, not a sample. MausDB (sourceforge, mdc-berlin.de) returned 404. Consequently the US institutional vivarium pole (Topaz/eSirius/Mosaic class: deep per-diem billing, USDA/IACUC reporting) is under-sampled; billing and compliance findings rest on PyRAT (EU framing) plus SoftMouse.NET's per-diem module, and US-specific regulatory machinery is NOT asserted in the final document. JCMS evidence is positioning/structure level only (jax.org description + GitHub README); its protocol-tracking support is unverified.

## Product Observations

### SoftMouse.NET (Iseehear) — evidence layer: A (official homepage + official online manual)

- Positioning: "Rodent Colony Management Database & Software"; "the only fit-for-purpose Animal Data Platform built for in vivo research groups of all sizes"; "Your Digital Vivarium, Breeding & Colony Management Partner"; tracks "mice, rats, breeding, pedigrees, cages, litters, complex genotypes, mouselines, transgenic animals". Serves laboratories, institutions ("maintain complete records of colony use and ensure protocol compliance"), breeding cores, biotech, animal facilities.
- Object model (from the official FAQ manual): Mouse records, Cage records, Mating records, Litter records, Mouselines/Strains, Protocols, Experiments, Studies, Requests, Orders, Per Diems, Samples.
- Mouse life-cycle states (FAQ "Mouse States Explained"): state changes automatically — created with a litter → "Pup"; weaned → "Weanling"; reaching maturity date (auto-calculated from mouseline preferences; default 42 days, editable) → "Stock"; put into a Mating record → "Mating" (only Weanlings and Stock can enter matings); ended (e.g., sacrificed) → "Ended". Deactivation and deletion of mouse records exist; ended mice can be reactivated (error correction).
- Cages: create cages; move mice into new or existing cages (with/without filters); end a whole cage; add location and cage capacities. Cage cards: customizable, printed to paper/card stock/labels, multiple per sheet, QR codes on cards scannable, browser-specific print configuration.
- Breeding schemas: create matings; harems in one or two records; male rotations; retire and remate males; add an active male breeder to multiple matings; pending matings; plug-date tracking; pregnant females with pregnancy dates; disband matings; end old breeders.
- Litters: create litters; add pups; foster a litter; edit parents; embryonic litters; distinguish alive vs ended pups; mother selection in harem matings; generation auto-population; end litters.
- Weaning: tag, sex, genotype and wean one or multiple litters at a time; wean before the set wean date; exclude unneeded pups; list of unweaned pups; configurable default wean/mature/tail-tag ages.
- Tag & ID: physical tags, ear marks with alternate IDs, RapID tag scanning (RFID), tag automation.
- Genotype: gene/allele dropdown lists per standard nomenclature; genotypes on unweaned pups; find mice to be genotyped; single/bulk genotype editing; filter by genotype; Transnetyx integration (link account, create orders, upload/import results, well plates, API refresh token).
- Mouselines/Strains: create/edit mouselines; strains; transfer a mouseline; mouseline–gene, mouseline–strain, mouseline–protocol associations; color coding.
- Lineage & history: The Mouse Record, The Mating Record, The Litter Record, The Cage Record; family/pedigree tree (up to 10 generations, expandable); find all pups from one breeder; add parents to existing mice.
- Protocols: create protocols; automate protocol assignment; manually assign protocols to mice (or cages); track number of animals used — "# Mice Approved" (entered on the protocol) plus increases via amendments vs "# Mice Used" (animals assigned) plus "Start Count From" (historical animals logged elsewhere); Protocol List shows # Approved, # Used, # Left; print protocol on the cage card; search mice in a specific protocol; archive/restore/delete protocols; attach files; add amendments; protocol permissions (create/edit/view/assign) grantable per group.
- Experiments & Studies: create experiments, modify mice in experiments, time points; Studies module with study groups, tasks, workflows, schedules, thresholds, auto-calculated values, super study administrators.
- Per Diems (FAQ): set up per diem rates; assign a per diem to a cage; visualize colony costs; export colony costs for billing purposes. Account customization includes "Owner – Billing Code Associations".
- Requests: create requests with or without colony records; mark done; visibility rules; view completed requests.
- Orders: regular (one-time) orders, standing orders, multi-orders; order states; confirm, pre-receive, receive.
- Samples: add samples to protocols; tube labels; takedown schemas; scan and collect samples; emergency kits; find animals scheduled for takedown; study group of an animal.
- Filter & report: quick filters, sticky filters, saved filters; total mouse count per cage type; total cage count per cage type; pup count per mouseline; mice born or weaned; ended mice; count of mice alive on a given day; count of active cages on a given day; count of active matings on a given day; export data.
- Accounts & sharing: group accounts; centralized vs decentralized account strategies; view-only rights; admins; transfer mice between owners; general access with overriding permissions; edit/view-only/create-and-transfer access; field-level edit permissions; access to inactive-user data.
- Compliance & audit: audit trail with date/time stamps per change (Activity History Log); customizable access permissions; encrypted passwords; housing-density limits ("ensure that the housing density limit for mice is never exceeded"); file attachments on animal records as digital paper trail.
- Alerts: email reminders for wean dates, plug dates, breeder replacement dates, custom events; calendar events binding records.
- Deployment: cloud SaaS; FOREVER FREE tier (single users, core relational tracking) vs PREMIUM; data import tools (from spreadsheets, JCMS, gMouse, MouseHouse, FileMaker Pro).

### PyRAT (Scionics) — evidence layer: A (official product pages)

- Positioning: "PyRAT – The Leading Animal Facility Management Software"; web-based; "leading animal colony management software in Europe"; stable since 2003; SaaS or self-hosted campus license; 11 languages; ISO 9001:2015-certified QMS. Key benefits: compliance ("tracks communications and authorizations"), streamlined billing and cost accounting, role-based access, automatic alerts, workflow automation.
- Animal Management: location management with graphical rack display; occupancy report; complete animal history; cage card/cage label printing in individual layouts; platform for shared animals; health records.
- Compliance: real-time centralized information; audit trail; full history tracking; authorization management according to directive 2010/63/EU; severity assessment for genetically modified lines; training and competences; SOP management; SSO integration (add-on).
- Breeding: extended line/strain management; generation tracking; animal and line/strain pedigree graphs.
- Genotyping: wellplate management; genotyping stickers for Eppendorf tubes; import of genotyping results (Transnetyx XML, CSV).
- Statistics: real-time reporting (weaning and breeding information, animal and cage usage); generation of the European statistical report according to directives 2012/707/EU and 2014/11/EU.
- Ordering: special services ordering; suppliers and supplier catalogs; internal and external animal orders.
- Experiments: authorization tracking; scoresheets; procedures; document uploads; comment system.
- Budgeting and invoices: retrieve budgeting information for animal housing, orders, procedures, or any kind of service; individual invoice layouts.
- Task management: work request system between scientists, caretakers, and managers; full history of requests and completed tasks.
- Usability: getting-started documents; single/multiple animal or cage data handling; user-configurable views and filters.
- Integration: configurable emails/notifications; API; interfaces to Tecniplast DVC and other systems.

### PyRAT Aquatic (Scionics) — evidence layer: A (official product page)

- Positioning: "Smarter Fish Colony Management"; built on PyRAT with "specialized logic and reporting for tank-based operations".
- Tanks: graphical rack display; stock and experiment/project tanks; health records; full tank history; tank label printing; document uploads.
- Crossings: record crossings; print labels for Petri dishes; crossing list with performance measuring; tank genotyping and pedigree; repeated crossings.
- Age levels: larva, juvenile, adult.
- Statistics: real-time stock information; survival rate per age level; average death rate; death report.
- Experiments: authorization tracking; procedures; document uploads; comment system.
- Compliance: authorization management and tracking; SOP management.
- Task management: same work-request system as PyRAT.

### PyRAT Add-ons (Scionics) — evidence layer: A (official product page)

- PyRAT Transgenic: cryopreservation database (graphical tank representation; embryo and sperm freezing); revitalization (embryo/sperm revitalization; rederivation of a line/strain through embryo transfer); transfer reports including offspring; integration with PyRAT (ordering of donors, plug-check, sampling procedures, genotyping, cage cards).
- PyRAT Pharmacy: drug registers (central and per-work-group; responsible users; registers assigned to rooms in the location system); drug information (CSV import; elimination protocols); drug packages (import, transfers between registers, elimination, splitting, expiry notifications); internal drug orders with status/history; use of drugs in animals via procedures, linked to licenses and competencies.
- PyRAT Integration: electronic cage card data exchange; vendor-specific cage systems (Tecniplast DVC); billing modules for cost recovery; multi-authorization solutions (Azure AD, SAML2, LDAP) for facilities shared between multiple organizations; robust API; ELN integrations (e.g., RSpace); custom integrations.

### JCMS (The Jackson Laboratory) — evidence layer: A positioning/structure only

- jax.org: "The JAX Colony Management System (JCMS) was a free multi-user relational database system for managing research mouse colonies." Supported by NIGMS, HHMI, and JAX; no longer developed, unsupported.
- GitHub README: source open-sourced 2015 (GPL v3). Structure: MS Access interface (jcms.mdb) + MySQL backend; JCMSWeb (JBoss web tier, integration/middle/web tiers); Android mobile app (iOS incomplete); CageCardsV1 (cage-card source); JCMS Pedigree Tree (jpt) for the Access backend; Access-to-MySQL converter (JMyC).
- Observation: confirms the colony-management generation (multi-user relational database for mouse colonies, cage cards, pedigree trees, web + mobile surfaces) predates current SaaS products. Protocol-tracking support not verifiable from fetched material — recorded as uncertainty.

### AniLog (boundary data point only) — evidence layer: A (official homepage)

- "Animal Welfare Management Software" for the animal welfare sector: veterinary module, boarding module, pet adoption; microchip registration integrations (Chipworks, Identibase, PetLog, PETtrac), pet insurance, postcode lookup.
- Observation: same generic shape (animal records + facilities + movements) but a completely different managed context — ownership/adoption/welfare, not research use under authorizations. Useful as the contrast case for the boundary against Animal Shelter Management; NOT a sample of this Type.

## Cross-product Comparison

| Dimension | SoftMouse.NET | PyRAT | PyRAT Aquatic | JCMS | Verdict |
|---|---|---|---|---|---|
| Individually identified animals as managed records | Yes (mouse records with states) | Yes (complete animal history) | Yes (per-tank colonies; tank history) | Yes (mouse colony database) | Core (B: all sampled) |
| Housing location model with occupancy | Yes (locations, cage capacities, move mice between cages) | Yes (location management, graphical rack display, occupancy report) | Yes (tanks on racks, graphical rack display) | Yes (cages; cage records) | Core (B) |
| Census / counts computable at any date | Yes (mice alive on a given day, active cages on a given day, born/weaned/ended counts) | Yes (occupancy report, real-time animal and cage usage) | Yes (real-time stock, survival/death statistics) | (not verified) | Core (B) |
| Recorded dispositions ending custody | Yes (end mouse / end cage / end litter; ended states) | Yes (full history; death statistics at Aquatic) | Yes (death report) | (not verified) | Core (B) |
| Research-use linkage (protocol/authorization/experiment) | Yes (protocols with # approved / # used / # left, amendments, assignment to mice or cages; experiments; studies) | Yes (authorization management per directive 2010/63/EU; experiments with authorization tracking, procedures, scoresheets) | Yes (authorization tracking; stock vs experiment/project tanks) | Unverified | Core (B: 3 of 3 verifiable) |
| Breeding machinery (matings/litters/weaning) | Yes (matings, harems, plug dates, litters, fostering, weaning workflows) | Yes (breeding module; generation tracking) | Yes (crossings, repeated crossings, performance measuring) | Yes (matings/litters implied by colony database; pedigree tree) | Common mature (B) — dominant in rodent/aquatic facilities; not tested at non-breeding poles |
| Lines/strains & pedigrees | Yes (mouselines, strains, family tree up to 10 generations) | Yes (extended line/strain management, pedigree graphs) | Yes (tank genotyping and pedigree, line/strain pedigree) | Yes (pedigree tree tool) | Common mature (B) |
| Genotyping machinery | Yes (gene/allele nomenclature, Transnetyx integration, well plates) | Yes (wellplates, tube stickers, result import) | Yes (tank genotyping) | (not verified) | Common mature (B), rodent/aquatic-dominant |
| Cage cards / labels | Yes (customizable cards, QR codes, print configuration) | Yes (cage card/label printing, individual layouts) | Yes (tank labels, Petri-dish labels) | Yes (CageCardsV1 source) | Common mature (B) |
| Health / veterinary records | Not observed in fetched evidence | Yes (health records) | Yes (health records) | (not verified) | Common at facility pole (A: PyRAT only) — kept qualified |
| Ordering (animals/supplies/services) | Yes (orders module: one-time, standing, multi-order; receive/pre-receive) | Yes (internal and external animal orders, suppliers, catalogs, special services) | (not observed) | (not verified) | Common mature (B) |
| Billing / per-diem / cost recovery | Yes (per-diem rates assigned to cages, cost visualization, export for billing, owner–billing-code associations) | Yes (budgeting and invoices for housing/orders/procedures/services; billing modules as integration add-ons) | (not observed) | No (free academic tool) | Common at institutional pole (B), absent at lab pole → variant |
| Protocol compliance machinery (training, SOPs, severity) | Partial (protocol permissions, amendments, files) | Yes (training and competences, SOP management, severity assessment for GM lines) | Yes (SOP management) | (not verified) | Common at facility pole (B) |
| Work requests / task management | Yes (requests with/without colony records) | Yes (work request system, full history) | Yes (same system) | (not verified) | Common mature (B) |
| Roles, ownership & data segregation | Yes (group accounts, owner-based data, transfers between owners, field-level permissions) | Yes (role-based access; shared-facility multi-authorization add-on) | Yes (same) | Yes (multi-user) | Common mature (B) |
| Audit trail / activity history | Yes (date/time-stamped audit trail, activity history log) | Yes (audit trail, full history tracking) | Yes (same) | (not verified) | Common mature (B) |
| Notifications/alerts | Yes (wean dates, plug dates, breeder replacement, custom events) | Yes (automatic alerts, configurable emails) | Yes (automated notifications) | (not verified) | Common mature (B) |
| Regulatory statistical reports | Not observed | Yes (EU statistical reports per 2012/707/EU and 2014/11/EU) | (not observed) | (not verified) | Variant (regime-specific) |
| Graphical rack/tank display | Not observed (locations/capacities yes) | Yes | Yes | (not verified) | Common at facility pole (A: PyRAT only) — kept qualified |
| Species scope | Mice, rats | Rodents and terrestrial facility animals | Fish (tank-based) | Mice | Variant axis |
| Deployment | Cloud SaaS, free/premium tiers | SaaS or self-hosted campus license | SaaS or self-hosted | Self-installed (Access/MySQL/JBoss) | Variant axis |

## Canonical Model (abstraction levels)

### L0 — Defining Invariant (deliberately minimal)

Four jointly-held structures:

1. **The animal as the managed unit of care** — individually identified animals (or colony units) held in the facility's custody, carrying species/strain/line identity, genotype where relevant, and a life-stage state. Remove → no managed object; the Type collapses.
2. **Housing location with tracked occupancy** — the facility's physical housing structure (rooms, racks, cages; tanks for aquatic) is modeled with capacity, and every animal's current location is recorded. Remove → an animal list with no physical operation; the facility cannot be run from it.
3. **The census-and-disposition loop** — the population is kept continuously current through recorded life events: arrivals (birth, order receipt, transfer in), movements between locations, breeding events, health/procedure events, and dispositions (euthanasia, transfer out, export, death); counts (census, occupancy) are computable from these records for any date. Remove → a static registry; the "management" disappears.
4. **Research-use linkage** — animals are held and used under a governing research authorization (an approved animal-use protocol or study), and the system tracks usage against it (assignment of animals to protocols/studies/experiments, with approved-vs-used accounting observed in two sampled products and authorization management per EU directive 2010/63/EU in a third). Remove → generic animal husbandry/breeding inventory — Livestock-Management-shaped, not a research animal facility.

Jointly-held load-bearing: 1 alone = a name list; 1+2 without 3 = a housing map with no history; 1+3 without 2 = movements without places; 2+3 without 1 = a cage log with no animals; 1+2+3 without 4 = livestock/husbandry inventory; 4 without 1–3 = a protocol compliance tracker (IACUC-platform territory).

Anti-overfit notes on L0:
- Breeding machinery is NOT in L0: non-breeding facilities (purchased-animal operations, large-animal holdings) are plausible and the aquatic product separates stock tanks from experiment tanks; breeding is common-mature, rodent/aquatic-dominant.
- Billing is NOT in L0: the lab-level pole (JCMS; SoftMouse FREE tier) operates with no billing.
- Health records are NOT in L0: no dedicated health module observed at the colony pole.
- Genotyping is NOT in L0: species-specific machinery.
- Cage cards are NOT in L0: they are the physical interface realization; one sampled vendor ships electronic cage-card data exchange as an add-on, showing the printed card is replaceable.

### L1 — Common Mature Structure

- Breeding & colony machinery: mating setup (pairs, harems, male rotations), plug-date tracking, litters (birth, fostering, parents), weaning workflows (tag/sex/genotype/wean, due-date alerts), breeder retirement/remating, pending matings, pregnant females.
- Lines/strains & pedigrees: line/strain registry with gene/strain/protocol associations, generation tracking, family/pedigree trees across generations.
- Genotyping machinery: gene/allele nomenclature lists, genotyping queues ("find mice to be genotyped"), well-plate management, tube/plate labels, import of results from external genotyping services.
- Cage cards & labels: customizable card/label printing (paper, card stock, stickers), QR/barcodes, scan-based identification (RFID tags observed at one product).
- Protocol/authorization compliance machinery: approved-number accounting with amendments, protocol assignment to animals or cages, protocol-on-cage-card printing, training/competence tracking, SOP management, severity assessment (GM lines), protocol permissions.
- Health & veterinary records (facility-oriented products): per-animal health records, treatments; drug/medication management via pharmacy add-on linked to procedures and licenses.
- Ordering & transfers: vendor orders with receipt states (confirm, pre-receive, receive), standing and multi-orders, internal and external animal orders, supplier catalogs, special services ordering, transfers of animals between owners/groups.
- Billing / cost recovery (institutional facilities): per-diem rates assigned to cages, cost accumulation per owner, cost visualization, export for billing or invoicing with individual layouts, budgeting information for housing/orders/procedures/services.
- Statistics & reporting: census at any date (alive animals, active cages, active matings), born/weaned/ended counts, occupancy reports, breeding productivity, pup counts per line, data export; regime-specific statistical reports (EU directives 2012/707/EU and 2014/11/EU at one vendor).
- Work requests / task management: request system between scientists, caretakers, and managers, with full request history.
- Roles, ownership & permissions: group accounts (centralized vs decentralized strategies), owner-based data segregation, transfers between owners, view/edit/create/assign/field-level permissions, view-only accounts.
- Audit trail & notifications: date/time-stamped, user-attributed change history; email alerts for due events (weaning, plug dates, breeder replacement, expiries).
- Location visualization: graphical rack/tank displays with occupancy (facility pole).
- Integration surface: APIs, ELN integrations, genotyping-service integrations, housing-hardware interfaces (e.g., Tecniplast DVC), electronic cage-card exchange, SSO/multi-authorization (Azure AD, SAML2, LDAP).

### L2 — Variant / Optional Structure

- Species realization: rodent (cages, matings, litters, weaning, tail-tag/ear-mark IDs) vs aquatic (tanks, crossings, Petri-dish labels, larva/juvenile/adult age levels, survival-rate statistics) vs large animals (unverified in sample).
- Operational scope: institutional vivarium management (census, compliance, billing, health, ordering — the facility operator's system) vs lab-level colony management (breeding, genotyping, lines — the research group's system; lighter on billing/compliance).
- Transgenic machinery: cryopreservation databases (embryo/sperm freezing with graphical tank maps), revitalization, rederivation via embryo transfer, donor ordering, plug-checks.
- Pharmacy/medication management: drug registers, package transfers/elimination/splitting, expiry notifications, internal drug orders, use via procedures linked to licenses and competencies.
- Regulatory regime: EU (directive 2010/63/EU authorizations; statistical reports 2012/707/EU, 2014/11/EU) vs US (IACUC/USDA machinery — not directly observed in this pass) vs institutional-local configurations.
- Deployment & packaging: cloud SaaS with free/premium tiers; self-hosted campus licenses; add-on packaging (transgenic, pharmacy, integration); open-source self-installed (historical).
- Study/experiment depth: experiment membership with time points; study groups, tasks, workflows, schedules, thresholds, auto-calculated values.
- Hardware integrations: ventuated-cage monitoring systems (Tecniplast DVC), RFID ear tags, electronic cage-card exchange.
- Multilingual/multi-site/multi-organization operation (shared facilities with multi-authorization).

### L3 — Vendor-specific (research notes only)

- SoftMouse.NET: FOREVER FREE vs PREMIUM tier ladder; default wean/mature/tail-tag ages configurable per mouseline (42-day maturity default); RapID RFID tag scanning; SIDs (sequential IDs); takedown schemas and emergency kits in the Samples module; browser-specific cage-card print configuration; mouseline/mouse color coding; Transnetyx API refresh-token mechanics; data-import tooling targeting JCMS/gMouse/MouseHouse/FileMaker/spreadsheets; schema.org pricing metadata.
- PyRAT: add-on packaging (Transgenic, Pharmacy, Integration); Tecniplast DVC interface; RSpace ELN integration; named multi-authorization stack (Azure AD, SAML2, LDAP); ISO 9001:2015-certified QMS; 11 UI languages; EU directive-specific statistical reports; private demo installations; mascots/branding.
- JCMS: MS Access interface + MySQL backend + JBoss web tier; Android app (iOS unreleased); jpt pedigree-tree tool; JMyC Access-to-MySQL converter; NIGMS/HHMI funding; GPL v3; discontinued/unsupported status.

## Rejected Findings (not promoted to canonical)

- "Colony management is a separate Application Type": rejected. The colony pole shares the same object structure (identified animals, housing occupancy, census loop, research-use linkage) and differs in operational scope and depth. Held as a variant pole of one Type (parallel to the team-lab inventory variant in Biobank Management).
- "Per-diem billing is definitional": rejected — absent at the lab pole (JCMS free academic tool; SoftMouse FREE tier). Institutional cost recovery is common-mature, not defining.
- "Breeding machinery is definitional": rejected — non-breeding facilities are plausible; the aquatic product's stock-vs-experiment tank split shows animals held without breeding. Rodent/aquatic-dominant common structure.
- "Genotyping is definitional": rejected — species-specific machinery; large-animal facilities unverified.
- "Cage cards are definitional": rejected — physical realization of the identification interface; electronic cage-card exchange exists as an add-on.
- "Health records are definitional": rejected — no dedicated health module observed at the colony pole; facility-pole products carry them. Common, not defining.
- "USDA/IACUC reporting is definitional": rejected — regime-specific; only EU statistical reporting directly observed. US machinery not asserted anywhere in the final document.
- "The cage is the central object": rejected — cages/tanks are housing containers; the animal (individually identified, state-carrying) is the managed unit; cage records exist to hold animals and carry per-diem rates.
- "Vivarium software = LIMS for animals": rejected — LIMS is assay/test-centric; this Type is custody/care/census-centric. Kept as boundary discussion.

## Boundary Findings

- **vs Animal Research Ethics / IACUC Platform**: the IACUC platform's central object is the protocol under committee review (submission → review → recorded decision → ongoing oversight). This Type's central object is the animal in care; the protocol appears as a usage-tracking reference (approved numbers, assignment, amendments). The IACUC pass itself recorded the seam: "remove the committee review loop and this Type becomes facility management". Test: if the workflow is review-and-decide on a protocol document, it is the IACUC platform; if the workflow is keeping a living animal population current under an approved authorization, it is this Type. Integration is common (approved protocol as prerequisite for obtaining/holding animals).
- **vs Biobank Management**: biobank manages preserved specimen inventory (custody-centric, years-decade preservation, consent governance); this Type manages living animal populations (census-centric, breeding dynamics, welfare/housing). Test: material that reproduces itself and must be housed daily vs material that is preserved and inert.
- **vs LIMS / Research LIMS**: LIMS is test/assay-centric (samples flow through processing to results). This Type is care/census-centric; procedures and scoresheets exist but no assay-result pipeline is the center.
- **vs Scientific Core Facility Management / Research Core Facility Management**: both may bill PIs, but the core-facility Type manages bookable services/instruments and service requests; this Type manages animals and husbandry operations. Per-diem billing is this Type's cost-recovery realization, not a service catalog.
- **vs Electronic Lab Notebook / Scientific Data Management**: ELN documents experiments; this Type operates the animal population that experiments consume. Experiment membership exists here as animal-to-study linkage, not as protocol documentation.
- **vs Livestock Management (agriculture)**: production economics (herds, yields, feed, market) vs research governance (authorized protocols, strains/lines, experiments). Remove the research-use linkage and this Type drifts toward livestock-shaped husbandry inventory — that removal test is the boundary.
- **vs Animal Shelter Management**: shelter = custody transfer/adoption context (intake → adoption/euthanasia, welfare outcomes, adopter-facing); research facility = custody retained by the institution under research authorizations, animals consumed by studies. AniLog's welfare-sector framing (veterinary/boarding/adoption modules, microchip/insurance integrations) documents the contrast.
- **vs Practice Management System (veterinary)**: clinical patient-and-owner care (appointments, encounters, claims) vs colony/husbandry operations. A vivarium's veterinary function is internal health management, not a client-facing practice.
- **vs preclinical Study Management (e.g., GLP study suites)**: study-management systems center the study lifecycle (planning, data capture, reporting); animal facility systems center the animal population. Pharma facilities may couple both; the coupling is integration, not identity.
- **Historical/market-sample check**: the paper-era vivarium (handwritten cage cards carrying protocol numbers, census books, breeding logs, health sheets, per-diem ledgers) satisfies all four L0 legs with no software. JCMS (2000s–2015, Access/MySQL, open source, free academic tool) satisfies the colony-pole reading (animals, cages, pedigrees, cage cards, multi-user) with no billing; its protocol support is unverified (uncertainty recorded). PyRAT (European, since 2003, EU directive framing) and SoftMouse.NET (North American SaaS) fit fully. The L0 survives the historical/regional/business-model check; the US institutional pole is under-sampled (see Uncertainties).

## Uncertainties

- US institutional vivarium vendors (Topaz Technologies, eSirius, Mosaic Vivarium) unreachable — the deepest per-diem billing and USDA/USDA-class reporting machinery is inferred only from PyRAT's budgeting/invoicing plus SoftMouse's per-diem module; US-specific compliance artifacts (USDA annual reports, IACUC-style protocol limits enforcement) are NOT asserted.
- JCMS protocol-tracking support unverified (positioning/structure-level evidence only).
- Exact per-diem computation semantics (daily snapshot vs event-driven; cage-day vs animal-day bases) not documented in fetched sources — final document describes the mechanism conceptually.
- Health-module depth at SoftMouse.NET unverified (no health module surfaced in the fetched manual index); health records kept as facility-pole common structure with single-product direct evidence.
- Large-animal / NHP facilities (primate centers) not sampled; their fit is asserted only at the conceptual level.
- Whether protocol assignment is enforced (blocking over-assignment) or advisory in general is unknown; SoftMouse documents accounting, not blocking. Final document avoids claiming enforcement.

## Final Synthesis

A Research Animal Facility Management application is the operational system of record for a facility that keeps laboratory animals for research. Its defining structure is four-part: individually identified animals held in the facility's care (with species/strain/line identity, genotype, and life-stage state); a housing-location model with tracked occupancy (rooms/racks/cages, tanks for aquatics); a census-and-disposition loop that keeps the population continuously current through recorded arrivals, movements, breeding, health, and disposition events, making counts computable for any date; and a research-use linkage that tracks animals against the approved protocols/studies under which they are held and used. Around this core, mature products add the machinery that makes the facility operable: breeding and colony management (matings, litters, weaning, pedigrees, lines/strains), genotyping workflows, cage-card/label printing, protocol-compliance machinery (approved-vs-used accounting, amendments, training, SOPs), health records, ordering and transfers, per-diem cost recovery, statistics and regulatory reports, work requests, role-based ownership and permissions, audit trails, and integrations (genotyping services, ELNs, housing hardware, SSO). The Type spans two operational poles — the institutional vivarium system (census, compliance, billing, health) and the lab-level colony system (breeding, genotyping, lines) — plus species realizations (rodent cages vs aquatic tanks). Its neighbors are separated by the central object: the protocol under review (IACUC platform), the preserved specimen (biobank), the assay (LIMS), the bookable service (core facility), the production herd (livestock), or the adoptable animal (shelter).
