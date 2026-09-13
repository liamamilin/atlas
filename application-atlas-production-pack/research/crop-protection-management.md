# Research Notes — Crop Protection Management

## Research Goal

Understand what "Crop Protection Management" software actually is in the market: what the managed domain is (protecting crops against pests, diseases and weeds with plant protection products — PPPs — and related interventions), what the defining structures are (product/label governance, the treatment decision, the application record, the safety state, compliance reporting), who operates it (growers, IPM technicians/advisors, custom applicators, ag retailers), and how it differs from neighboring agricultural Types. This pass must also **discharge two joint-review flags** recorded by earlier passes (agronomy-management and crop-management both flagged crop-protection-management as a probable single-domain leaf / module-inside-suite case).

## Initial Boundary

Working hypothesis before research:

- "Crop protection" in production agriculture = managing biological threats to crops (insect pests, mites, diseases, weeds, vertebrate pests) with plant protection products (insecticides, fungicides, herbicides etc.) plus non-chemical interventions (e.g. mating disruption, biologicals).
- Likely core: the crop-protection product (a legally governed input — the label) + the treatment decision (which product, rate, timing) + the application record (a compliance artifact mandated by several regulatory regimes) + the safety state of treated areas (re-entry / pre-harvest intervals).
- Nearest neighbors: Crop Management (the whole crop cycle), Agronomy Management (multi-domain input decisions), Precision Agriculture Platform (variable-rate execution loop), Agricultural IoT Platform (monitoring backbone), plus label/product data services (Greenbook/CDMS pattern) as a data layer.
- Risks: (1) the module reality — spray records ship as one module inside crop-management suites (documented in the crop-management pass); (2) the naming trap — "pest control software" commonly names business-management software for structural pest-control service companies (a different domain, not researched here); (3) "crop protection" also names the PPP manufacturing industry — managing a crop-protection *business* would be ERP-land, not this Type.
- Two prior flags to discharge:
  - research/agronomy-management.md: "vs Nutrient Management / Crop Protection Management / Soil Management / Seed-adjacent siblings (§20): these appear to be single-domain leaves… Risk: superset/capability relationship (each domain leaf may exist as a module inside agronomy suites)."
  - research/crop-management.md: "vs single-domain siblings — Irrigation Management / Crop Protection Management / Nutrient Management / Soil Management (§20): … Probable superset/capability relationship (spray records ship as one module inside a sampled crop product)."

## Research Questions

1. Is there a standalone market for crop-protection-centered software, or only spray-record modules inside farm/crop suites? (The Type-vs-capability question — both prior flags.)
2. What is the unit of record — the treatment/application event, the treated field, the product, or the season's protection program?
3. What does the application record contain across products and regulatory regimes, and who requires it?
4. How does the legal product layer (registration/label: permitted uses, rates, safety intervals) manifest in software?
5. How is the threat context (pests/diseases/weeds) captured and used in the decision (scouting, traps, models, alerts, timing)?
6. What safety-state machinery exists (worker re-entry, pre-harvest intervals) and is it definitional or regime-specific?
7. What roles appear (grower, farm manager, applicator, IPM technician/PCA, compliance staff, ag retailer)?
8. What is clearly NOT this Type (label databases, monitoring dashboards, whole-cycle crop management, structural pest-control business software)?

## Representative Products

| Product | Operating model | Why sampled |
|---|---|---|
| Semios | Specialty-perennial monitoring-and-intervention service (sensor networks, pest/disease models, spray timing, mating disruption; Greenbook label data in group) | The threat-modeling / intervention-execution pole: crop protection as monitored decision + intervention; self-describes as delivering "crop protection" tools |
| Agroptima | European (Spain-origin) farm management whose signature pillar is the legally mandated phytosanitary record (field journal / cuaderno de campo) | The regulatory record-compliance pole: the official treatment register digitized, official-format reports, applicator/product legal attributes |
| Croptracker | North-American specialty-crop record-keeping platform with deep spray-record machinery | The records + safety-state pole: PHI/REI auto-calculation, entry warnings, chemical inventory withdrawal — documented in the crop-management pass; also the module-inside-suite evidence |
| Agworld | Collaborative farm-data platform (agronomist ↔ grower); owner of Greenbook | The recommendation→record pole: recommendations become work orders and automatic spray records; also connects this Type to the label-data layer |

Boundary checks (not core samples): Greenbook (label database — the data layer), EPA WPS + Spain's RD 1311/2012 (regulatory substrate grounding what the record and safety state legally are), Agvance dispatch (prior pass — third-party application in ag retail), Bushel Farm / crop-management suites (the superset side of the module reality).

## Sources

All fetches dated **2026-09-07** unless marked as cross-pass reuse (fetched 2026-09-06/07 in the agronomy-management and crop-management passes).

This pass:

- Agroptima:
  - https://www.agroptima.com/en/ (positioning; traceability; phytosanitary & fertilizer reports; SIGPAC codes; product registration numbers; task planning/digital work orders; ISAGRI S.L. footer)
  - https://www.agroptima.com/en/digital-field-journal (Field Journal page — the Spanish field notebook: RD 1311/2012; mandatory since 1 Jan 2013; 12-section official model; treatment register content "Date, parcel identification number, pest, disease or weed… Product, machine or treatment equipment, dosage, quantity"; product registration number per entry; batch number for third-party transactions; treated-seed register; IPM technician validation signature for crops under advisement; third-party applicator regime: Register of Plant Protection Transactions, Treatment Contracts, ROPO registration; 3-year minimum retention; MAPAMA-format Excel export; CAP cross-compliance)
  - https://www.agroptima.com/en/features (Jobs/Fields/Products/Workers/Machinery/Working-time modules; automatic stock-movements registration; crop calendar; search historical data; phytosanitary & fertilizer use reports; per-worker roles incl. app-only recording role and restricted cost access; offline app)
- Semios:
  - https://semios.com/solutions/disease-management/ (disease models: Alternaria, almond rust, fire blight, powdery mildew, walnut blight; risk thresholds + alerts; spray-timing optimization; "reduce the risk of fungicide resistance"; in-canopy sensor data; leaf-wetness/risk index; per-acre risk heatmaps; historical susceptibility; forecast; About: "tools for farm management, crop protection, water, frost, and automation"; footer "Labels & SDS" → greenbook.net)
- EPA (US regulatory substrate):
  - https://www.epa.gov/pesticide-worker-safety (occupational pesticide safety hub; WPS; Restricted Use Pesticide Products; applicator certification)
  - https://www.epa.gov/pesticide-worker-safety/agricultural-worker-protection-standard-wps (WPS: employers must implement restricted-entry intervals (REIs); notify workers about applications and treated areas; provide central access to "Pesticide applications on the establishment" + SDS; commercial-handler information exchange; designated-representative access enumerates the application record fields: product name, EPA registration number, active ingredients, crop/site treated, location/description of treated area, date(s)/times application started and ended, duration of the labeling-specified REI; Application Exclusion Zone; certified crop-advisor exemption)
- Greenbook (label-data layer, boundary check):
  - https://www.greenbook.net/ ("Crop protection label data — Your complete crop protection reference"; filters: active ingredient, manufacturer, pest, crops, state; "35+ years… trusted crop inputs reference guide for farmers, ranchers, agronomists, retailers and crop advisers"; "transforms product labelling into indexed, actionable data"; disclaimer: "does not replace the official manufacturer issued label"; owned by Agworld Inc; group logos Agworld + Semios)

Cross-pass reuse (documented with evidence in the named research notes; the underlying pages were fetched on those passes):

- Croptracker (via research/crop-management.md): https://www.croptracker.com/ , https://www.croptracker.com/product/farm-management-software.html , https://www.croptracker.com/why-use-crop-management-software.html — spray records ("Record chemical and fertilizer applications…"; chemical inventory "automatic withdrawals"; "auto-calculate your tank mix, chemical amounts, and PHI and REI times"; "Alert workers of safe re-entry and pre-harvest intervals…"; "receive notifications when the PHI and REI intervals end, and be warned if you try to schedule a production practice in an area that is not yet safe for entry"; traceability from planting through sprays; GlobalGAP/FSMA; schedules + templates; season-over-season; efficacy and cost analysis)
- Semios (via research/crop-management.md): https://semios.com/ , https://semios.com/solutions/reporting-tools/ ("Semios Crop Management Platform"; threshold alerts; historical records; weekly reports), https://semios.com/solutions/insect-pest-management/ (automated camera traps; pest-pressure alerts with thresholds; site-specific pest models; degree-day modelling and forecast to "accurately time sprays"; variable-rate mating disruption)
- Agworld (via research/agronomy-management.md): https://www.agworld.com/ (recommendations → "compliant digital records" one click; audit-ready standardized data; multi-year field records), https://www.agworld.com/products/activity-management/ (recs → work orders → activities → "automatically convert them into detailed spray or fertilizer records"; offline mobile)
- Agvance (via research/agronomy-management.md, third-party application context): https://agvance.net/products/agronomy/dispatch (jobs list, applicator assignment/status)

Failed / abandoned (network-restriction rule, 1–2 attempts each):

- https://www.agrian.com/ and https://agrian.com/ — 403 on both attempts (Agrian is known as a crop-protection label/recommendation/records platform; it could not be used as evidence. The agronomy pass recorded the same 403.)
- https://aglogiccompany.com/ and https://www.aglogiccompany.com/ — transport errors on both attempts
- https://www.cdms.net/ — 403 (second label-database check abandoned; Greenbook covers the pattern)
- https://www.croptracker.com/spray-records.html — 404 (spray-record evidence reused from the crop-management pass instead)
- https://www.agroptima.com/en/farm-management-software/phytosanitary-software/ — 404

Evidence-layer legend below: **A** = directly observed on an official page of one product; **B** = observed across multiple sampled products; **R** = grounded in an official regulatory source (EPA / RD 1311/2012 as documented by a product's official pages).

Source-access limitation: no Tier-1 help centers were reached for any sampled product in this pass; Agroptima's Field Journal guide is a Tier-2 page with Tier-1-quality regulatory documentation. All product-mechanics evidence is Tier-2 official pages (this pass + two prior passes). Precise operational numbers are asserted only where the sources state them.

## Product A — Semios (pest/disease monitoring-and-intervention pole)

### Key observations

- Self-description (About): Semios "brings together leading brands and expert field services to deliver tools for farm management, **crop protection**, water, frost, and automation" (A) — crop protection named as one of its tool families.
- Disease management: "disease models tailored to your orchard… built using data collected from in-canopy sensors"; named models (Alternaria, almond rust, fire blight, powdery mildew, walnut blight); "optimize spray timing… for optimum treatment results"; "reduce the risk of fungicide resistance"; risk thresholds → outbreak alerts on phone/computer; leaf-wetness and risk-index reporting (rain vs dew); per-acre infection-risk heatmaps; historical susceptibility by block; next-week disease-risk forecast (A).
- Insect pest management (cross-pass, documented): automated camera traps with daily catch summaries and hot-spot prioritization; threshold-based pest-pressure alerts; site-specific pest models; pest-degree-day modelling and forecast to time sprays; variable-rate mating disruption (pheromone intervention, certified for organic and conventional production) (A).
- Sprays are the recurring action verb across both pest and disease pages ("time and target sprays"; "improve application timing"; "accurately time sprays") — the decision output is timing and targeting of crop-protection interventions (A).
- Historical record: "Track and view historical data"; weekly reports covering weather, pest, disease, water, crop development; shareable external reports (cross-pass A).
- Label data: footer links "Labels & SDS" to greenbook.net/semiosbio-technologies-inc — the group operates the Greenbook crop-protection label database (A).
- Not visible on public pages: application/treatment records as first-class objects, product-rate record fields, inventory. The record half of the loop is not publicly documented for this product (limitation, kept weak).

## Product B — Agroptima (EU regulatory record-compliance pole)

### Key observations

- Positioning: farm management software to "record your agricultural operations, get instant traceability and know your costs and yields"; traceability compliance — "Phytosanitary and fertilizer reports, Global GAP, Ecological"; official codes (SIGPAC field codes) and "registration number of phytosanitary products" in reports (A).
- Field Journal page documents the Spanish **cuaderno de campo** (farm treatment register) that the product digitizes (A):
  - Legally mandatory for all professional farmers since 1 Jan 2013 under Royal Decree 1311/2012 on the sustainable use of plant protection products; checkable at any time for CAP cross-compliance; minimum 3-year retention; paper or electronic.
  - Official model has 12 sections, including: registration of phytosanitary actions in plots; treatments on crops under advisement (with boxes for an **Integrated Pest Management technician's validation signature**); treated-seed use; postharvest treatments; storage-facility and transport treatments; product analysis; marketed-harvest record; fertilization record.
  - Treatment register content: "**Date, parcel identification number, pest, disease or weed… Product, machine or treatment equipment, dosage, quantity**" — plus the applicator's card number and machinery identification in the general part.
  - The **product registration number** (authorization number, stable across batches) is required in every entry; batch numbers are required for those transacting PPPs or applying to third parties.
  - Third-party treatment companies: keep a Register of Plant Protection Transactions; a Treatment Contract with the farmer; registration in ROPO (official register of producers/operators of plant-protection equipment).
  - Complementary legal documents: advisory documentation (advised crops), equipment inspection certificates, purchase invoices, residue analyses, waste delivery notes.
- Product surface (A): note activities from the mobile app ("apply phytosanitary, harvest, etc.") in seconds, offline-capable with sync; multi-device/multi-worker ("one user per worker… access to record activities in which he intervenes", app-only role, restricted access to costs); Modules: Jobs, Fields, Products, Workers, Machinery, Working time; **automatic stock-movements registration** (inventory moves as activities are recorded); crop calendar; search over historical data; map-based field drawing/grouping (5 satellite image types); "Phytosanitary and Fertilizers use reports" — downloadable in official MAPAMA format; cost/profitability analytics (Pro); task planning and digital work orders.
- Inference (C): the product's spine for this Type is **the legally specified treatment record**, digitized at capture, from which official reports, traceability, and cost analytics are derived.

## Product C — Croptracker (records + safety-state pole; also the module evidence)

### Key observations (documented in the crop-management pass; reused as evidence here)

- Spray records: "Record chemical and fertilizer applications and analyze input usage, efficacy and costs over time"; chemical inventory with "**automatic withdrawals**" on application (A).
- Safety-state machinery: "**auto-calculate your tank mix, chemical amounts, and PHI and REI times**"; "Alert workers of safe re-entry and pre-harvest intervals before they enter an area"; "receive notifications when the PHI and REI intervals end, and be warned if you try to schedule a production practice in an area that is not yet safe for entry" (A) — the treated area carries a computed safety state that gates subsequent work scheduling.
- Application planning: schedules with a template library; crew/task assignment; traceability chain "from planting through sprays, harvesting, packing and shipping"; GAP/GlobalGAP/FSMA audit reporting; season-over-season verification of best management practices (A).
- Module reality: spray records ship as **one module** of a broader crop-management platform (the superset pattern the crop-management pass flagged) (A).

## Product D — Agworld (recommendation→record pole; label-data owner)

### Key observations (documented in the agronomy pass; reused as evidence here)

- The recommendation loop: agronomist creates recommendations "with products, rates, timing and other instructions specified"; "one click of a button these recommendations become compliant digital records"; records are "structured and standardized", "audit-ready", multi-year (A).
- Execution: recommendations "converted directly into work orders and field activities"; when completed, "Agworld can automatically convert them into detailed **spray** or fertilizer records" (A) — crop-protection recommendations and spray records are first-class.
- Label data ownership: Greenbook ("Crop protection label data") is operated by Agworld Inc — the same group as Semios (A). The label database is a separate reference surface: "indexed, actionable data" from product labelling (active ingredient, manufacturer, pest, crops, state filters), with the explicit disclaimer that it "does not replace the official manufacturer issued label" (A).
- Inference (C): the platform demonstrates the full chain **threat → recommendation (label-constrained product choice) → work order → application → spray record → audit-ready history**, plus the label-data layer that feeds product decisions.

## Regulatory substrate (grounding for the record and safety state)

- **US — EPA Agricultural Worker Protection Standard (WPS)** (R):
  - Employers must "implement restricted-entry intervals (REIs)" and "notify workers about applications and pesticide-treated areas"; keep workers out during applications (Application Exclusion Zone).
  - Employers must provide central, ongoing access to "Pesticide applications on the establishment" and Safety Data Sheets; commercial handler employers and establishment operators must **exchange application information**.
  - The legally accessible application-information set enumerates the record fields: pesticide product name, **EPA registration number**, active ingredients, crop/site treated, location/description of the treated area, **date(s) and times the application started and ended**, duration of the labeling-specified REI.
  - Restricted Use Pesticides (RUP) require certified applicators; certified crop advisors are exempt from certain WPS provisions.
- **EU (Spain) — RD 1311/2012 sustainable use of PPPs** (R, as documented by Agroptima): mandatory treatment register (see Product B), IPM advisory validation for certain crops, third-party applicator registers, 3-year retention, CAP cross-compliance.
- Jointly (R): **the treatment record and the safety interval are legal artifacts, not software conventions.** The software Type exists substantially to produce, govern, and expose these artifacts.

## Cross-product Comparison

| Structure | Semios | Agroptima | Croptracker | Agworld | Evidence |
|---|---|---|---|---|---|
| Field/plot/block registry with crop context | ✔ blocks/orchards | ✔ fields/plots (SIGPAC codes) | ✔ blocks/rows | ✔ fields under farms | B |
| Threat context (pests/diseases/weeds) captured | ✔ core (traps, models, risk) | ✔ per-treatment target ("pest, disease or weed" field) | not visible | ✔ scouting notes/photos | B (3/4) |
| PPP product catalog with registration identity | via Greenbook linkage | ✔ registration number required per entry | ✔ chemical inventory | ✔ products in recommendations | B |
| Label/legal constraints as governing reference | ✔ Greenbook (Labels & SDS) | ✔ registration number; official legal model | ✔ PHI/REI from label data | ✔ "compliant" records + owns label data | B |
| Crop-protection decision artifact (product × rate × timing) | ✔ spray timing/targeting (model-driven) | ✔ work orders / planned tasks | ✔ schedules + tank mix | ✔ recommendations | B |
| Treatment/application record (dated, plot-anchored, attributed) | not visible publicly | ✔ core (the digitized legal register) | ✔ core | ✔ automatic spray records | B (3/4) |
| Safety-state machinery (REI/PHI gating work) | not visible | not visible (legal duty documented) | ✔ auto-calc + entry warnings + interval-end notifications | not visible | A (single product) + R |
| Application planning → work orders/tasks | partial (timing tools) | ✔ task planning, digital work orders | ✔ schedules/templates | ✔ recs → work orders | B |
| Chemical/input inventory with withdrawal on use | ✖ | ✔ automatic stock movements | ✔ automatic withdrawals | not visible | B (2/4) |
| Official/compliance reporting & audits | ✔ shareable external reports | ✔ core (official MAPAMA format; GlobalGAP; CAP) | ✔ GAP/GlobalGAP/FSMA | ✔ audit-ready standardized data | B |
| Label/SDS reference-data linkage | ✔ Greenbook | ✔ product registration numbers | implied (PHI/REI need label data) | ✔ owns Greenbook | B |
| Efficacy/cost analysis of applications | not visible | ✔ costs per field/crop | ✔ "efficacy and costs over time" | ✔ planned vs actual | B (3/4) |
| Offline mobile capture | ✖ (alerts out) | ✔ core | not visible | ✔ offline app | B (2/4) |
| Multi-season retention of protection history | ✔ historical data | ✔ legal 3-yr minimum; cloud retention | ✔ season over season | ✔ multi-year records | B |
| Non-chemical interventions (mating disruption/IPM) | ✔ variable-rate mating disruption | IPM validation regime documented | ✖ | ✖ | A (single) + R |
| Third-party/custom application regime | ✖ | ✔ ROPO, treatment contracts, transactions register | ✖ | contractors assignment | A + prior pass (Agvance) |
| Sensor/model monitoring depth | ✔ core | ✖ | ✖ | ✖ | A (single) |

## Canonical Model

```text
Field / plot / block with its crop (the protected unit)
├── Threat context  (what endangers the crop: scouting, traps, models,
│     risk alerts, historical susceptibility — recorded or monitored)
├── The governed product layer  (crop-protection products as identified,
│     registration-bearing inputs whose legal usage constraints — permitted
│     uses, rates, safety intervals — anchor every decision and record)
├── The crop-protection specification  (product × rate × timing × method for a
│     field/crop — a forward plan/work order or a recorded treatment)
├── The treatment/application record  (dated, plot-anchored, attributed —
│     operator and equipment, product with registration number, dose/quantity —
│     the compliance artifact of record)
└── Compliance state & outputs  (safety intervals live on the treated area and
      gate re-entry/harvest work; official reports, audits, buyer requirements;
      the retained multi-season protection record feeding the next decision)
```

### L0 — Defining Invariant

1. **The crop-protection specification** — an identified crop-protection product at a rate and timing on an identified field/crop, the "what to protect with" content of the system (forward plan/work order or recorded treatment; in minimal realizations the two materialize together in one entry). Remove → a generic operation log or task list.
2. **The governed product/label layer** — crop-protection products exist in the system as identified, registration-bearing inputs whose legal usage constraints (permitted uses, rates, safety intervals) are the standing reference for decisions and records. Remove → generic input-application tracking, indistinguishable from nutrient or seed records.
3. **The treatment record as retained compliance evidence** — dated, plot-anchored, attributed (operator, equipment), product-identified, kept across seasons for inspection, official reporting, and traceability. Remove → a recommendation surface or a monitoring/alerting dashboard.

Historical check: the pre-digital pattern — the printed label as the physical legal document, the farmer's product choice, and the paper treatment register/spray log (legally mandated in several regimes, kept for inspection) — satisfies all three. Early desktop spray-record programs also fit. The definition therefore does not depend on cloud, mobile, sensors, models, GIS, or auto-calculation.

### L1 — Common Mature Structure

- Field/plot/block registry with crop context (substrate shared with crop management)
- Threat context capture: scouting observations, pest/trap counts, disease/pest risk models, weather-driven risk, historical susceptibility; target pest/disease/weed recorded per treatment (legally required in some regimes)
- Product catalog of PPPs (and often fertilizers/seed beside them) with registration numbers, active ingredients, permitted uses
- Application planning: work orders/tasks, timing windows, tank-mix calculation, schedule/template libraries
- Application records with offline mobile capture and sync
- Worker-safety interval machinery: re-entry (REI) and pre-harvest (PHI) intervals computed from label data, entry warnings, interval-end notifications, gating of scheduled work on treated areas (documented in one sampled product; grounded as a legal duty in the researched regimes — treat as common-but-not-universal)
- Chemical/input inventory with automatic withdrawal on application
- Official-format compliance reporting: regulator register exports, certification audits (GlobalGAP, GAP/FSMA-class), buyer/traceability reports
- Label/SDS reference linkage (label databases as the data layer)
- Efficacy/cost analysis per application and season-over-season comparison
- Multi-season retention of protection history (3-year legal minimum in the documented EU regime; often longer in products)
- Roles: grower/farm manager, field worker/applicator (record capture), agronomist/IPM advisor (decision/validation), compliance/quality roles; scoped visibility

### L2 — Variant / Optional Structure

- Regulatory regime: EU treatment-register regime (mandated field journal, official formats) vs US WPS/state record regime vs voluntary certification regimes (GlobalGAP, GAP audits, organic, residue/MRL requirements from buyers)
- Segment: specialty perennial (per-block models, traps, mating disruption) vs broadacre vs greenhouse/nursery (explicitly inside US WPS scope) vs postharvest/storage treatments
- Operating side: grower self-recording vs advisor/IPM-technician validation (some crops legally require professional validation) vs ag-retail/custom-applicator operation (third-party application registers, treatment contracts, applicator registries) vs monitoring-service provider
- Decision depth: record-first vs model/alert-first (sensor networks, degree-days, disease models, forecasts) vs recommendation-first (advisor-authored, approval loops)
- Execution capture: manual mobile entry vs machine/as-applied data; variable-rate application as one output form
- Non-chemical interventions in scope: mating disruption, biologicals, IPM program records
- Resistance management as an explicit concern (timing optimization to reduce resistance risk)
- Downstream residue/MRL compliance (buyer/export-driven) — adjacent, weakly evidenced in this pass
- Deployment: standalone protection tooling vs module inside farm/crop-management suites (the common packaging reality)

### L3 — Vendor-specific (Research Notes only)

- Semios: named disease models (Alternaria, almond rust, fire blight, powdery mildew, walnut blight); per-acre infection-risk heatmaps; automated camera traps; site-specific vs regional models; variable-rate mating disruption with organic-certified pheromones; professional field-services installation; "Semios Crop Management Platform" self-naming; Greenbook "Labels & SDS" footer linkage.
- Agroptima: the 12-section Spanish field-journal model; MAPAMA-format Excel export; SIGPAC codes; ROPO/transactions-register support; applicator card number; 3-year retention framing; 5 satellite image types; app-only worker role with restricted cost access; "Agroptima Costs" Pro analytics; ISAGRI S.L. ownership.
- Croptracker: PHI/REI auto-calculation with interval-end notifications and unsafe-scheduling warnings; tank-mix auto-calculation; chemical inventory auto-withdrawal; Traceability Lot Codes / Critical Tracking Events (FSMA vocabulary); piece-rate payroll machinery (out of this Type); computer-vision add-ons (out of this Type).
- Agworld: one-click recommendation→spray-record conversion; Greenbook ownership (label database as separate reference surface with "does not replace the official label" disclaimer); audit-ready standardized data claim.
- Greenbook: filter dimensions (active ingredient, manufacturer, pest, crops, state); 35+ years history; Agworld Inc ownership.
- EPA WPS specifics retained in research notes only: AEZ radius values (25/100 ft by droplet size), 15-day response window for designated-representative requests, two-year record access span, central-posting mechanics.
- Spain RD 1311/2012 specifics retained here only: 1 Jan 2013 mandate date, 12-section model enumeration, CAP cross-compliance linkage.

## Vendor-specific Findings

None of the L3 items entered the canonical model. The clearest cases: the **12-section field-journal model is Spanish regulation, not a universal structure** (the US enumerates a different, shorter information set); **PHI/REI automation is documented in one sampled product** (regulatory in origin, product-specific in implementation — it stays out of the core and is presented as common-but-not-universal); **sensor/model machinery is Semios-specific in depth** and belongs to the monitoring variant; **the label database is a data-layer product**, not this Type.

## Boundary Findings

1. **vs Crop Management (§20 sibling; joint-review flag DISCHARGED from this side)**: crop management centers the whole crop-cycle loop (plan → execute → record → monitor → harvest across all operation classes); crop protection management centers **one operation class** — protection — with its own regulatory record, product/label governance, and safety state. The module reality is confirmed: Croptracker ships spray records as one module inside a crop-management platform (documented in both passes). But standalone crop-protection-centered software demonstrably exists and is marketed on its own (Agroptima's phytosanitary record machinery is its signature pillar; Semios sells pest/disease management solutions as its own line; label-data services exist specifically for this domain). Structural test: remove planting/irrigation/fertilization/harvest machinery → crop protection management remains (specification + product governance + record + safety state + compliance intact); remove the protection machinery → crop management remains. **Type stands as an independent single-domain Type; keep both; no taxonomy change.**
2. **vs Agronomy Management (§20 sibling; joint-review flag DISCHARGED from this side)**: agronomy management centers the multi-domain input-decision practice (field test data → professional recommendation → execution record); crop protection management centers the protection operation loop with the **treatment record + label compliance** as the artifact. Overlap is real — PPP recommendations are part of agronomy practice, and the agronomy pass noted Agrian (403, unreachable) as its own label-compliance evidence gap. Structural test: remove the label/application-record compliance machinery → agronomy management remains (recommendations + test data); remove the professional multi-domain recommendation practice → crop protection management remains. **Type stands; keep both; no taxonomy change.**
3. **vs label-data services (Greenbook/CDMS pattern)**: label databases transform product labelling into searchable, indexed data (active ingredient, pest, crops, state) and explicitly disclaim replacing the official label. They hold no decisions, no records, no safety states, no compliance outputs. They are the **data layer** this Type consumes (Semios links it; Agworld owns it; PHI/REI machinery presupposes label data). Not the same Type; a capability/companion relationship.
4. **vs pest/disease monitoring (Agricultural IoT Platform pattern)**: monitoring and alerting without the product decision, the treatment record, and the safety state is the sensing pattern. Semios is the boundary-crossing pole: its pest/disease model/alert/spray-timing/mating-disruption machinery is protection decision-making, but its application-record depth is not publicly documented, and its irrigation/frost/climate solutions are pure monitoring. Center-of-gravity test: the treatment record and governed product layer vs the device fleet and data stream.
5. **vs Precision Agriculture Platform (§20 sibling)**: the variable-rate execution loop (prescription → machine → as-applied verification) with machine data as first-class is precision-ag; variable-rate *application of protection products* (e.g., Semios's variable-rate mating disruption) is one output form within this Type. Gradient; consistent with prior passes' flags.
6. **vs Food Safety / Traceability Types**: the treatment record is an *input* to downstream traceability and residue compliance (Agroptima documents residue analyses and marketed-harvest records as companion documents; Croptracker links sprays into its traceability chain). The downstream chain is another Type; this Type produces the field-side protection record.
7. **vs Farm Management Platform (§20 sibling)**: farm management centers whole-farm business operations; protection management centers one technical domain. Spray/phytosanitary records appear inside farm products as modules (Agroptima is itself labeled "farm management software" — vocabulary does not define the Type; its protection machinery is what places it substantially in this domain).
8. **Naming traps (recorded, not taxonomy changes)**: (a) "pest control software" in common market usage names business-management software for structural/commercial pest-control service companies (customer accounts, routes, billing) — a different industry domain entirely, not researched here; (b) "crop protection" also names the PPP manufacturing industry — software for managing a crop-protection *business* would be ERP-class, not this Type; (c) phrasing like "phytosanitary", "plant health", "spray records", "treatment records", "crop protection" is regionally variable for the same structure.
9. **Remaining single-domain siblings (Nutrient Management / Soil Management / Irrigation Management — unprocessed)**: the prior flags extend to them unchanged; this pass adds no new evidence about them. Joint review when those leaves are processed.

## Uncertainties

1. No Tier-1 help centers reached for any sampled product; all product-mechanics evidence is Tier-2 official pages (plus two prior passes' Tier-2 evidence). Record schemas and workflow states are asserted only at the level the pages state.
2. **Agrian was unreachable (403 on both attempts, this pass and the agronomy pass)** — the most explicitly crop-protection-branded platform (labels + recommendations + records) is therefore evidenced only indirectly (Greenbook for the label layer; Agworld/Croptracker for record machinery). Assertion strength for the "compliance-platform pole" is correspondingly reduced.
3. Semios's application-record depth (whether treatment records are kept as first-class objects) is not visible on public pages; its placement in this Type rests on its protection-decision machinery and self-description. Kept weak.
4. Worker-safety interval machinery (PHI/REI automation) is documented in exactly one sampled product; it is grounded as a legal duty (US WPS, EU regime) but its software commonality is unverified. Presented as common-but-not-universal.
5. US state-level pesticide application record requirements (beyond WPS information access) were not researched; the US regulatory picture is WPS-grounded only.
6. Residue/MRL compliance machinery (buyer/export-driven) was not directly evidenced; kept as an adjacent uncertainty.
7. The third-party/custom-application pole (ag retail) is evidenced through Agroptima's legal-regime documentation and the agronomy pass's Agvance dispatch observations; a dedicated ag-retail application product (AgLogic) was unreachable.

## Final Synthesis

Crop Protection Management is the software of the **crop-protection domain**: its world is the protected crop on identified fields, threatened by pests, diseases and weeds; the **governed layer of crop-protection products**, each carrying legal usage constraints (registered uses, rates, safety intervals) that anchor every decision; the **crop-protection specification** — which product, at what rate, at what time, by what method — whether planned forward as work orders or captured as treatments; the **treatment/application record** — dated, plot-anchored, attributed, product-identified — as the retained compliance artifact that multiple regulatory regimes legally require; and the **compliance state and outputs** — safety intervals live on treated areas gating re-entry and harvest work, official reports, certification audits, buyer traceability, and a multi-season protection history feeding the next decision. Threat monitoring, models and alerts, safety-interval automation, inventory withdrawal, label lookup, efficacy/cost analysis, and offline mobile capture are standard capabilities whose depth varies by segment and regime. The Type is genuinely domain-centered and standalone-marketable (discharging the two prior flags), while also commonly appearing as the spray/phytosanitary module inside crop- and farm-management products. Remove the governed product layer and the treatment record and what remains is monitoring or generic field logging — other Types.
