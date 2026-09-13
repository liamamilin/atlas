# Research Notes — Hazardous Waste Management

Research date: **2026-09-08**
Slug: `hazardous-waste-management` (§21 Environment, Sustainability & Climate)

---

## Research Goal

Explain what Hazardous Waste Management software is, who uses it, what core objects it manages, how waste moves through it from generation to final disposition, what rules govern it, and where its boundary sits against neighboring Application Types — especially the processed sibling Hazardous Materials Management (whose pass flagged a joint review with this leaf), Waste Management Platform and Waste Hauling Management (both unprocessed), Dangerous Goods Transportation Management (processed), and the environmental compliance / EHS family.

## Initial Boundary (hypothesis before research)

- Hypothesis: the generator-side system of record for the waste an organization *produces and ships out* — waste characterization (profiles/codes), on-site accumulation (containers, accumulation areas, time-in-storage), off-site transfer under legally required paperwork (manifest / consignment note), and disposition closure — as opposed to Hazardous Materials Management (materials held *in* the facility) and hauler-side systems (waste collection *businesses*).
- Expected confusion: HazMat sibling (inbound vs outbound), general waste management (sustainability/operations vs regulated compliance), waste hauling (operator business vs generator compliance), DG transport (transport classification vs waste-lifecycle compliance), EHS platforms (module embedding).

## Research Questions

1. What is the central record — "waste profile", "waste stream"? What does it carry?
2. How is at-site waste state modeled (containers, drums, accumulation areas, storage time)?
3. How does the off-site shipment work — what paperwork, who is named, how is it tracked to closure?
4. What determination machinery exists (hazardous vs non-hazardous, waste codes) and can it stand alone?
5. Who are the users (waste generators, waste handlers, EHS managers, contractors)?
6. What regulatory reporting is produced from the records?
7. What is the relationship to chemical/inventory systems (the chemical→waste handoff)?
8. What differs by region/regime (US RCRA vs EU/UK waste framework)?

## Representative Products

Selected for market representativeness, different product philosophies, and different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| Chemical Safety Software (EMS Waste module) | long-standing chemical-lifecycle specialist; lab/university/government generator pole | dedicated "Hazardous Waste Management" product page (Tier 1), deep operational detail |
| Locus Technologies — Locus Waste Management | multi-tenant cloud platform app; cradle-to-grave drum accounting; large + small generators | dedicated waste app page within an EHS platform (Tier 1) |
| Intelex Waste Management | enterprise EHS/ESG suite module; breadth across waste types, RCRA + EU WFD | dedicated waste management page (Tier 1) |
| HazWasteOnline (One Touch Data, UK) | classification-engine specialist; UK/EU/Saudi regulatory environments | the waste-determination depth as a standalone market product — tests whether characterization alone is the Type |

Ecosystem reference (not a commercial sample): **US EPA e-Manifest** system — the government platform receiving the uniform hazardous waste manifest; documents the manifest's role and the user types of the waste-shipment ecosystem.

Probes attempted and abandoned: Quentic (3× 404 across plausible URLs), eraenvironmental.com (domain held by an unrelated stormwater consultancy — the EHS vendor "ERA Environmental Management Solutions" was therefore not reachable under that name), Locus fact-sheet PDF (binary, unreadable). Sphera and Chemwatch were already unreachable in the hazardous-materials-management pass; not retried.

## Sources

- Chemical Safety Software — Hazardous Waste Management: https://chemicalsafety.com/hazardous-waste-management-software/ [fetched 2026-09-08]
- Chemical Safety Software — suite home (module adjacency): https://chemicalsafety.com/ [fetched 2026-09-08]
- Locus Technologies — Waste Management: https://www.locustec.com/applications/waste-management/ [fetched 2026-09-08]
- Intelex — Waste Management Software: https://www.intelex.com/waste-management-software/ [fetched 2026-09-08]
- HazWasteOnline — home (classification software): https://www.hazwasteonline.com/ [fetched 2026-09-08]
- US EPA — The Hazardous Waste Electronic Manifest (e-Manifest) System: https://www.epa.gov/e-manifest [fetched 2026-09-08]

Evidence layers: **A** = directly observed on the fetched official page of one product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + Type-boundary reasoning.

---

## Product Observations

### Chemical Safety Software — EMS Hazardous Waste module (Tier 1, A)

- Positioning: "track waste from generation through to certificate of destruction"; "all of the phases of hazardous waste management in compliance with RCRA guidelines for generation, pickup, consolidation, treatment, manifesting, disposal, and reporting." (A)
- Feature roll: Pickup Requests; Waste Profiles; Storage Time Tracking; Accumulation Areas; Lab Packing; Drum Tracking; Waste Labeling; Bill of Lading; Biennial Report; Print Manifests; e-Manifests. (A)
- Accumulation areas: "Define and manage satellite, 90-Day, and Part B accumulation areas" (SAA and WAA vocabulary). (A — vendor's own text names the regime-specific classes)
- Workflow detail: waste generators at the lab initiate an electronic waste disposal request on web/tablet/phone; waste handlers notified by email and generate "pickup request sheets (PRS)"; pickup performed by scanning the container barcode, which "automatically adjust[s] both the chemical inventory quantities as well as accumulation area quantities". (A)
- Profiles: "Manage and store waste profile data. Easily migrate profile data from legacy systems"; waste items "link … to approved waste profiles"; automated alerts "when a waste needs to be disposed" (storage-time driven). (A)
- Paperwork: "EMS Waste generated all required paperwork … including drum labels, waste manifests, LDR's, ERG's, SDS, analysis and related documentation." Biennial Report auto-created. e-Manifest ready. (A)
- Extra waste classes: biohazardous, radioactive, mixed waste tools; onsite waste treatment and recycling toolset. (A)
- Case studies: US DOE facility (drums per waste type set up at labs; generators drop lab packs, record in software, request drum pickup/replacement; dashboard monitors their SAAs); three large research universities (PIs and chemists request pickup of hazardous, biological and radioactive waste; handlers scan barcodes on tablets). (A)
- Suite adjacency: EMS Waste "works in conjunction with the EMS Chemical Inventory module to support your company's chemical storage, use, distribution, treatment, recycling, and waste disposal." Separate modules exist for SDS, GHS labeling, regulatory reporting (Tier II, DHS, Biennial, IFC, VOC, HMBP). (A)

### Locus Technologies — Locus Waste Management (Tier 1, A)

- Positioning: "waste management software for cradle to grave data … tracks cradle-to-grave data about hazardous and non-hazardous waste to ensure every drum is accounted for and to simplify compliance with regulatory requirements." Scales "to meet the needs of large and small generators." (A)
- Container/contents record: "manages every salient detail about waste containers and contents so that everything can be tracked, searched, sorted, and reported on"; single or multiple facilities; "global waste profiles and compliance standings." (A)
- Shipping: "Uniform Hazardous Waste Manifest templates and label templates for warnings, toxicity levels, etc. The software automates the creation of e-Manifest-ready forms and the required drum and lab packing labels." (A)
- Mobile: scan barcodes/QR/RFID at the source "to update waste status and automatically sync." (A)
- Workflow/roles: workflow module maps business processes across stakeholders; "the robust permission model segregates functional capabilities; waste generators can have simplified workflows, while waste administrators can take control of all the forms." (A)
- Dashboards: "container status, waste type generation by facility, accumulation times, and disposal methods or facilities." (A)
- Reporting: "multiple preconfigured regulatory reporting formats such as Biennial and TRI reports and exports"; benefits list includes Biennial and SARA 313/TRI reporting. (A)
- Chemical linkage: "Almost every chemical that enters a manufacturing plant eventually becomes a waste product… Track chemicals arriving at a site, where they are being stored, and when the waste leaves the site"; chemical-inventory app named as adjacent. Lab data/lab reports included. (A)

### Intelex — Waste Management (Tier 1, A)

- Positioning: "track waste creation and storage, ensure proper disposal, comply with complex regulations and minimize the possibility of fines"; compliance for "US EPA/RCRA and EU Waste Framework Directive 2008/98/EC from a single application"; manages "any type of waste from generation to inventory to its final, legal disposal from one central application." (A)
- Onsite containers: "Track the location, storage area, container type, waste profile and net weight of all waste containers… automatic notifications, such as when stored waste is approaching the regulatory limit or when a disposal is required to be sent to an accumulation point." (A)
- Offsite disposal: "Track key offsite disposal details including quantity, receiving facility, transporter, date shipped, costs, manifests and whether it left the country. Transactions can generate a hard-copy waste manifest or an EPA compliant e-Manifest." (A)
- Onsite disposal: waste type, quantity, dates, location recorded centrally. (A)
- Waste profiles: "Easily create profiles for common waste types that include physical properties, potential hazards, applicable regulations, acceptable disposal facilities, waste codes, shipping names, and more." (A)
- Hauler economics: "Monitor information related to each hauler including waste type, quantity and cost of trip. Alter pick-up frequency to eliminate costs associated with unused disposal capacity." (A)
- Roles/analytics: role-based access; real-time lifecycle data by location, region, operation or waste type; ESG framing (waste reduction among ESG metrics). FAQ: used by industrial/manufacturing companies and municipal/government agencies; "EHS managers and supervisors … schedule and strategize waste transportation, storage and disposal." (A)

### HazWasteOnline (One Touch Data, UK) (Tier 1, A)

- Positioning: "Hazardous Waste Classification Software … EU, UK & Saudi Arabia regulatory environments"; "Classify any waste, any number of samples to the latest technical guidance and legislation." (A)
- Workflow: get waste chemistry analysis data from the lab → import and classify → produce a classification report. Import of the lab's `.hwol` files; third-party PDF classification reports importable via smartphone. (A)
- Content: 4,000+ substances or user-created; "Mirror entries List of Waste codes"; WAC (Waste Acceptance Criteria) assessment for landfill-destined waste; PAH double-ratio plots; statistical editions. (A)
- Audience: "waste producers, consultants, regulators, carriers and waste receivers"; partners are consultancies, testing labs, contractors, a regulator (SEPA), infrastructure owners. Classification training courses. (A)
- Framing: "lets the user focus on what is in the waste and not how to do the calculations or keep up with the changing data"; "simple, accurate and auditable tool for the classification of potentially hazardous waste materials, including contaminated soils, filter cakes, sludge residues, ashes, liquids and waste products." (A)
- **Notably absent**: no container/accumulation tracking, no manifests, no pickups — classification only. (A, by absence)

### US EPA e-Manifest (ecosystem reference, A)

- "e-Manifest facilitates the electronic transmission of the uniform manifest form, which accompanies shipments of hazardous waste." (A)
- Registered users; user fees; error-correction process; fact sheets by user type; developer API (public GitHub); state adoption/authorization map; March 2026 proposal to phase out paper manifests entirely. (A)

---

## Cross-product Comparison

| Structure | Chemical Safety | Locus | Intelex | HazWasteOnline | EPA (ecosystem) | Layer |
|---|---|---|---|---|---|---|
| Waste profile / characterization record (identity + codes + handling/disposition approval) | ✔ waste profiles, approved-profile linkage | ✔ global waste profiles | ✔ waste profiles (properties, hazards, regulations, waste codes, shipping names, acceptable facilities) | ✔ the entire product (classification report, LoW codes) | manifest carries waste descriptions | B |
| At-site waste state: containers/durms, locations, quantities | ✔ drums, accumulation areas, barcode-adjusted quantities | ✔ "every drum accounted for", container status | ✔ containers w/ location, storage area, type, profile, net weight | ✘ | — | B |
| Accumulation time / storage-time surveillance & alerts | ✔ storage time tracking, disposal-due alerts, 90-Day/SAA/Part B areas | ✔ accumulation times on dashboard | ✔ notifications approaching regulatory limit | ✘ | — | B |
| Pickup / internal movement workflow with generator-vs-handler roles | ✔ pickup requests, PRS, handlers notified | ✔ workflows, generator vs administrator permissions | ✔ (implied by workflow/roles; notifications) | ✘ | — | B |
| Off-site transfer paperwork (manifest / e-Manifest / BOL) | ✔ manifests, e-Manifest, bill of lading, LDR paperwork | ✔ Uniform HW Manifest templates, e-Manifest-ready forms | ✔ hard-copy manifest or EPA e-Manifest per transaction | ✘ | uniform manifest accompanies shipments | B |
| Transporter / receiving-facility records on the shipment | ✔ (manifest content; BOL) | ✔ disposal methods or facilities dashboard | ✔ receiving facility, transporter, date shipped, costs, left-country flag | ✘ | user types: generators/transporters/receiving facilities | B |
| Disposition closure (treatment/disposal recorded back; "certificate of destruction") | ✔ "through to certificate of destruction" | ✔ disposal methods/facilities | ✔ "final, legal disposal" | ✘ | manifest completion | B |
| Regulated reporting from waste records (Biennial class) | ✔ Biennial report | ✔ Biennial, TRI/SARA 313 | ✔ compliance framing (RCRA/WFD) | ✘ | — | B |
| Determination engine w/ maintained substance/code data + lab-data import | (via profiles/analysis docs) | ✔ lab data/reports included | (regulation lists in profiles) | ✔ core: substances, LoW codes, lab import | — | B |
| Container labeling (drum labels/tags, barcodes) | ✔ drum labels & waste tags w/ barcodes | ✔ label templates, drum labels | ✘ (not shown) | ✘ | — | A→B |
| Consolidation / lab packing | ✔ | ✔ lab packing labels | ✘ | ✘ | — | A |
| Hauler/transport cost tracking | ✘ (not shown) | ✘ (not shown) | ✔ cost of trip, pick-up frequency | ✘ | — | A (product-specific in sample) |
| Biowaste / radioactive / mixed waste classes | ✔ | ✘ (not shown) | ✘ | ✘ | — | A (product-specific) |
| Onsite treatment/recycling tracking | ✔ | ✘ (not shown) | ✔ onsite disposal tracking | ✘ | — | A→B |
| Multi-facility enterprise roll-up & ESG analytics | ✘ (suite-level) | ✔ multi-facility, global views | ✔ by location/region/operation; ESG framing | ✘ | — | B |
| Chemical-inventory ↔ waste linkage | ✔ barcode pickup adjusts chemical inventory | ✔ chemical inventory app adjacency; "chemicals… become waste" | ✘ (not shown) | ✘ | — | B |

Reading of the table:
- The first seven rows travel together in every full-structure product (3 of 4) — the jointly-held core.
- HazWasteOnline realizes only the characterization row and is still a viable, marketed product — proof that characterization depth is separable as a tool, i.e. **not sufficient** to be the Type, while remaining an important depth-variant of one core leg.
- Intelex carries the least hazardous-specific depth in the sample but the same structural spine, plus the clearest general-waste breadth ("any type of waste") — documents the straddle with the unprocessed Waste Management Platform leaf.

## Abstraction Hierarchy

### L0 — Defining Invariant (candidate; deliberately small)

The system of record for waste a regulated organization generates and ships out, carrying three jointly-held structures:

1. **The regulated waste stream of record** — a persistent identified record per waste the organization generates/holds (waste profile / waste stream), carrying its regulatory characterization: what it is, its hazardous/non-hazardous determination and waste codes in the applicable control regime, and its approved handling/disposition pathways. *Remove → a generic waste log or material inventory; nothing "regulated" remains.*
2. **The tracked at-site accumulation state** — waste held between generation and removal in identified containers/accumulation areas, with quantities, locations, and time-in-storage visible and watched. *Remove → a profile database or shipment paperwork bureau with no operational state of the waste.*
3. **The documented off-site transfer-and-disposition loop** — each removal of waste proceeds through the legally required transfer record (manifest / consignment-note class document naming transporter and receiving facility) and is tracked to recorded final disposition/closure. *Remove → container logistics or inventory with no compliance closure; the "hazardous" regime collapses into ordinary stock movement.*

Jointly-held load-bearing:
- 1 alone = classification/profile tool (the sampled classification-only pole) or a waste profile database.
- 2 + 3 without 1 = barcode drum logistics with no regulated identity — generic container/asset tracking.
- 1 + 3 without 2 = paperwork generation with no operational picture of what is accumulating where.
- 1 + 2 without 3 = accumulation inventory that never legally ships — the defining obligation (documented, accountable disposal) unmet.

Subject binding: the managed object is **waste under a waste-control regime**. Products commonly carry non-hazardous streams on the same machinery (sampled vendors say so explicitly); "hazardous" is the paradigm case and the regime's driver, not a filter that every record must pass. The regime vocabulary (RCRA, List of Waste, Waste Framework Directive, manifest, consignment note) is the implementation layer — the invariant is *characterization + controlled accumulation + documented transfer*, not any one jurisdiction's instrument.

### L1 — Common Mature Structure (standard capabilities, not defining)

- Container labeling: drum labels, waste tags with barcodes, warning/toxicity label templates.
- Barcode/QR/RFID scanning and mobile apps for container-level status updates at the point of work.
- Pickup-request workflow: waste generators request removal, handlers/administrators process and route; role separation between generators, handlers, administrators.
- Storage-time tracking with alerts when disposal is due or limits are approached.
- Consolidation and lab-packing support.
- e-Manifest-class electronic integration with the government manifest system (sampled US-facing products all advertise e-Manifest readiness).
- Receiving-facility / transporter master records attached to shipments; hauler trip costs.
- Regulated reporting outputs (Biennial-report class, TRI/SARA class in the US sample).
- Determination support with maintained substance/waste-code data and laboratory data import.
- Multi-facility roll-ups, dashboards (container status, generation by facility, accumulation times, disposal routes), audit-ready records.
- Chemical-inventory linkage — the chemical→waste handoff (pickup scanning decrements chemical inventory; "chemicals entering the plant become waste").

### L2 — Variant / Optional Structure

- Regional regime depth: US RCRA generator machinery (satellite/90-day/Part B accumulation vocabulary, LDR notices, Biennial Report, e-Manifest) vs European tradition (List of Waste codes, Waste Framework Directive, landfill Waste Acceptance Criteria, consignment-note/duty-of-care practice in the UK; Saudi environment cited by the classification pole).
- Breadth of waste classes: hazardous-only focus vs hazardous + non-hazardous + universal classes (biohazardous, radioactive, mixed waste in one sampled product).
- Classification-only specialist products (the characterization leg as a standalone tool, sold to producers, consultants, regulators, carriers and receivers).
- Suite posture: standalone specialist suite vs platform app vs enterprise EHS/ESG module.
- Segment poles: university/laboratory campuses (PI-initiated pickup requests), government/DOE facilities, industrial manufacturing, municipalities.
- ESG/analytics extensions (waste reduction metrics, cost-per-trip optimization, waste-pattern insights).
- Onsite treatment/recycling tracking.
- Receiving-side (TSDF) posture: the manifest ecosystem's user types include receiving facilities; some vendors serve that side or pair it with expert services — recorded as adjacency/variant, not this leaf's center.

### L3 — Vendor-specific (research notes only)

- Chemical Safety: "EMS Waste" module branding; pickup request sheets (PRS); CAS scientific-data integration announcement; iOS/Android/Windows app IDs; DOE/university case-study specifics.
- Locus: user-count and renewal-rate marketing figures; SOC reports/uptime claims; named app ecosystem (chemical inventory, incident management, wastewater apps); fact-sheet PDF (unfetchable).
- Intelex: Datamaran regulatory-content partnership; ESG application cross-sell blocks; customer testimonials; free-trial funnel.
- HazWasteOnline: `.hwol` file format and acronym system; edition names/pricing; training-course cadence and partner-logo wall; GIS/statistics in Expert edition (marked "in development" for GIS).

## Rejected Findings (not promoted to core)

- **"Hazardous-only scope"** — rejected as definitional: sampled products explicitly manage non-hazardous waste alongside hazardous (Locus, Intelex), and the classification pole's product is precisely *determining* which it is. The invariant is the regulated-waste machinery, not a hazardous-only filter.
- **"Manifest is the defining object"** — rejected in US-specific form: the manifest is one jurisdiction's realization of the transfer-document structure; the UK consignment-note tradition and e-Manifest evolution show the *documented transfer record* is the invariant, the manifest its dominant implementation. Also EPA's own move toward a fully electronic system shows the paper form is not timeless.
- **"90-day / accumulation time limits as core"** — rejected in numeric form: regime-specific (vendor text carries the numbers); the invariant is *surveilled time-in-storage against applicable limits*, numbers vary by regime and generator class.
- **"Waste hauling/dispatch"** — rejected: routing trucks is the hauler-side Type (see boundary findings); generator-side products record shipments, they do not operate fleets.
- **"ESG/sustainability analytics"** — rejected: analytics layer, not the compliance spine.
- **"Lab-packing, biowaste/radioactive classes, onsite recycling"** — held as capabilities/variants: strong in one product each.

## Historical / Market-Sample Check

Paper-era generator practice satisfies the candidate L0: a waste-stream file per waste (characterization sheets, analyses, waste codes = leg 1); accumulation-area logbooks tracking drums, dates when accumulation started, weekly container checks, and storage durations against limits (leg 2); multi-copy uniform hazardous waste manifests (or UK consignment notes) traveling with each shipment, copies returning from the receiving facility as proof of disposal, filed with LDR notifications and biennial-report worksheets (leg 3). Older regional regimes (UK hazardous-waste consignment notes; EU List of Waste coding) fit the same three-leg structure with different paperwork. Pre-cloud 1990s waste-tracking databases for generators and TSDFs satisfy it in software form. Definition therefore names no manifest form, no e-Manifest, no RCRA, no specific time limits — only the three structures. The modern e-Manifest integration, mobile scanning, and ESG analytics are era machinery.

## Boundary Findings

| Neighboring Type | Seam | Removal test |
|---|---|---|
| **Hazardous Materials Management** (processed; flagged joint review — **discharged here**) | inbound/at-site *held materials* (SDS identity record + holdings inventory + right-to-know/screening action layer) vs the *outbound regulated waste stream* (profiles, accumulation, transfer documentation, disposition). The same physical drum can be both a hazmat holding (while in use) and a waste container (once determined waste and awaiting shipment). | Remove the waste-transfer/accumulation machinery and keep SDS-identity + holdings + hazard screening → still Hazardous Materials Management. Remove the SDS/holding/right-to-know layer and keep waste profiles + accumulation + manifests → still this Type. |
| **Waste Management Platform** (§21, unprocessed — flag for that pass) | general waste streams/quantities/diversion/costs as sustainability & operations data vs the regulated-waste compliance spine. Sampled products straddle: Intelex markets "waste management software" with RCRA/WFD machinery inside; Locus covers hazardous + non-hazardous. | Remove profiles/determination, accumulation-limit surveillance, and transfer documentation → generic waste tracking/reporting (that sibling). Add them → this Type. |
| **Waste Hauling Management** (§21 unprocessed) / **Junk Removal / Waste Hauling Management** (§29, processed) | hauler-side *business operations* (customers, routes, truck crews, container assets, billing) vs generator-side *compliance record* of the waste itself. The hauling pass itself held compliance manifests as standard-not-definitional on the hauler side. | Remove the waste-regulatory machinery and keep service-account economics → hauling territory; keep the compliance loop → this Type. |
| **Dangerous Goods Transportation Management** (§18, processed) | DG transport: per-consignment transport classification/packaging for *any* dangerous goods vs this Type: waste-lifecycle compliance; waste manifests *contain* transport elements (shipping names, transporter) but the center is the waste's characterization→accumulation→disposition accountability, not carriage execution. | DG pass held "facility-side chemical management" outside its Type from the other side; symmetric here. |
| **Environmental Compliance Management** (processed) | obligation/permit register + conformance loop vs the waste object machinery; waste reporting (biennial-class) *feeds* compliance status. | The waste record with accumulation/manifest machinery does not exist in the obligation register. |
| **Environmental Laboratory Management** (processed) | the lab analyzes waste/leachate samples (matrix "waste" documented there); the classification pole *imports* lab data — the lab is the characterization instrument, not the waste system of record. | Remove lab workflows → this Type intact. |
| **EHS / HSE Platform** (processed) | umbrella register spanning domains (waste named among its environmental records) vs single-regime depth on the waste object; waste software commonly ships as a platform app/module. | Same embedding pattern the hazmat pass documented for chemicals. |
| **Contaminated Site Management / Environmental Remediation** | legacy in-ground contamination vs generated waste streams; contaminated *soil* becomes waste once excavated and classified (the classification pole lists contaminated soils) — a feed-in, not an overlap of records. | |
| **Recycling Operations Management** (§21, unprocessed) | material-recovery operations vs regulated disposal loop; onsite recycling appears in this sample only as a capability. Flag recorded for that pass. | |

## Uncertainties

- European full-structure suite products (Quentic waste module, Sphera waste line) could not be fetched; the EU/UK tradition is evidenced here only through the classification pole (LoW codes, WAC, UK/EU/SA guidance) and Intelex's WFD reference. The *manifest-vs-consignment-note* equivalence at product level is therefore held at inference strength (C), not A-layer product observation.
- Receiving-side (TSDF) waste software was not sampled; the receiving facility's own system (waste acceptance, profiles at receipt, scale/ticket closure) is inferred from the manifest user-type structure and Locus's TSDF-expertise positioning — recorded as adjacency, not asserted as this Type's center.
- Cost/hauler management was observed in one product only — held product-specific in sample.
- The precise set of reports per jurisdiction (beyond Biennial/TRI named by two US products) varies by state/country; no exhaustive claim made.

## Final Synthesis

A Hazardous Waste Management application is the waste-generating organization's compliance system of record for the waste it produces and ships out. Its world is: waste streams as characterized records (what is it, how is it classified, where may it legally go); waste as physical, accumulating state at the facility (containers in defined accumulation areas, quantities, time-in-storage under surveillance); and waste leaving only through documented, accountable transfer (manifest/consignment-class paperwork naming transporter and receiver, tracked to recorded disposition). Around that spine the market adds container labeling and scanning, pickup workflows with role separation, determination engines fed by laboratory data, e-Manifest integration, regulated reporting, hauler economics, and ESG analytics. The Type is the outbound twin of hazardous-materials management and the compliance-side complement of waste hauling: same drum, different regime, different record.
