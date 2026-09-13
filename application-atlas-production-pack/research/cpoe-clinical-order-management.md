# Research Notes — CPOE / Clinical Order Management

Research date: 2026-09-07
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a CPOE (Computerized Provider Order Entry) / Clinical Order Management application really is from real products: its core objects, the order lifecycle, who does what on the ordering side vs the fulfillment side, what order-time decision support means in context, and where its boundaries lie with the EHR, e-prescribing, CDSS, LIS/RIS, and the (lexically colliding) commercial "Order Management System".

## Initial Boundary

Temporary hypothesis before research:

- Core purpose: clinicians electronically record orders (medications, laboratory, diagnostic imaging, procedures, nursing tasks, consults, referrals, etc.) for a specific patient; the system makes those orders available to the care team and fulfilling departments and tracks each order through its lifecycle.
- Primary users: ordering clinicians (physicians, NPs/PAs, residents); secondary: nurses, pharmacists, lab/radiology staff (fulfillment), informatics/administrators (catalog and order-set maintenance).
- Nearest Types: Electronic Health Record (parent container), Electronic Prescribing (specific order class with its own external rails), Clinical Decision Support System (standalone systems vs checks embedded at order time), Laboratory Information System / RIS / Pharmacy Management (receiving systems), Care Plan Management, Referral Management.
- Name collision: "Order Management System / OMS" (§05.07, commerce) is a different domain entirely.
- Unknowns at start: how universal the sign→verify two-step is; how order sets are governed; whether routing to fulfillment is definitional; how statuses are standardized.

## Research Questions

1. What is a clinical "order"? Which order classes exist across products?
2. What objects compose the model: orderable item/catalog, order, order set, order action, prior-order linkage?
3. What is the order lifecycle and who transitions it (ordering side vs fulfillment side)?
4. Is routing/transmission of orders to fulfilling parties definitional or optional?
5. What order-time decision support appears inside the entry flow, and how does it relate to a standalone CDSS Type?
6. What signature/verification workflows exist (ordering-side signature, result sign-off, countersignature)?
7. How are order sets structured and maintained?
8. What interfaces does each side see (composer, chart orders view, fulfillment worklists, results)?
9. Where is the boundary with EHR (module vs standalone), e-prescribing, CDSS, LIS/RIS?
10. Would older / smaller / differently positioned products still fit the definition (historical check)?

## Representative Products

Chosen for market representativeness + documentation availability + different philosophies + different customer tiers:

| Product | Category | Why chosen | Evidence depth reached |
|---|---|---|---|
| OpenMRS | open-source medical records platform, global-health deployments | public REST API documentation defines the Order model precisely | Tier 1 (API docs) |
| OpenEMR | open-source ambulatory EHR/PM, ONC-certified | public wiki documents the procedure-order process end to end; ONC certificate lists CPOE criteria | Tier 1 (wiki + certification listing) |
| MEDITECH Expanse | commercial EHR, large community/rural/acute install base | physician-facing product pages name orders as core process; order sets; department modules | Tier 2 (product pages) |
| Oracle Health (Cerner Millennium heritage) | commercial EHR, co-dominant in US acute care | market-structure anchor; clinical suite positioning | Tier 2 (product page only; detailed docs gated) |

Also used as a primary/regulatory source (not a product): ONC Health IT Certification Program criteria for CPOE (healthit.gov).

Epic (largest US EHR vendor) was intended as a fifth product; epic.com returned HTTP 403 on both access attempts and was abandoned per the source-access rules. Recorded as a limitation.

## Sources

All fetched 2026-09-07.

- OpenMRS REST API documentation — Order / Order type resources: https://rest.openmrs.org/#orders (direct fetch, full text captured)
- OpenEMR Project Wiki — Home (certification + manuals index): https://www.open-emr.org/wiki/index.php/OpenEMR_Wiki_Home_Page
- OpenEMR Project Wiki — Procedure configuration & order process: https://www.open-emr.org/wiki/index.php/Procedure_configuration_%26_order_process
- MEDITECH — Expanse for Physicians: https://ehr.meditech.com/ehr-solutions/expanse-for-physicians
- MEDITECH — Expanse (home / solutions nav): https://ehr.meditech.com/
- Oracle Health — product page: https://www.oracle.com/health/
- ONC Health IT — Certification criterion pages: CPOE–laboratory §170.315(a)(2) (fetched; includes Base EHR clarification naming (a)(1) medications and (a)(3) diagnostic imaging): https://www.healthit.gov/test-method/computerized-provider-order-entry-medications (URL for (a)(1) redirected to the (a)(2) page; (a)(2) content retrieved twice)
- OpenEMR ONC certification criteria table (embedded in wiki home): 170.315(a)(1), (a)(2), (a)(5), (a)(12), (a)(14), etc.

Access limitations:

- Epic (epic.com/software): HTTP 403, twice → abandoned. No Epic-specific claims made.
- Oracle Health operational documentation (PowerOrders/PowerPlans user guides): not publicly reachable from this environment; only the marketing/positioning page was reachable. No Oracle-specific workflow claims made.
- ONC CPOE–medications criterion page ((a)(1)): URL redirected to the (a)(2) laboratory page; the medication-specific capability text was not independently retrieved. Medication-ordering specifics below rely on other sources only.
- VA CPRS documentation (intended as a historical Tier-1 source): va.gov/vdl request timed out once → abandoned.
- Per the evidence rules, no precise operational details (numeric limits, exact status vocabularies, default settings) were filled from model memory where direct evidence was unavailable.

## Product Observations

### OpenMRS — REST API documentation (Tier 1, directly observed)

- "An **Order** represents a request from a provider such as a lab test, procedure, referral, etc." [A]
- "An Order only records an intention, not whether or not the action is carried out. The results of an Order are typically recorded later as Observations." [A] — strong boundary statement: the order record is separate from execution and results.
- Order types: "Common types of orders are prescriptions (drug orders), lab tests, radiology tests, procedures and referrals." [A]
- The Order resource has subtypes (DrugOrder, TestOrder); `orderType` is a configurable classification bound to implementation classes. [A]
- Order fields (directly observed in create/read payloads): `patient`, `encounter` (order placed within a care encounter), `orderer` (provider), `concept` ("the item being requested (e.g., 'serum creatinine')"), `careSetting` (INPATIENT / OUTPATIENT), `urgency` (ROUTINE / STAT / ON_SCHEDULED_DATE), `dateActivated`, `scheduledDate`, `dateStopped`, `instructions`, `previousOrder`. [A]
- Order actions: NEW ("placing a new order"), REVISE ("revising an existing order"), DISCONTINUE ("request an active order to be stopped"), RENEW ("resume a prior order"). [A]
- Orders are listable per patient and per care setting; orders carry full display strings composed from concept + parameters. [A]
- No signature/verification field observed in the Order resource. No routing/fulfillment fields observed (no "send to lab" concept at the API level). [A] — supports treating routing and signature as non-definitional.

### OpenEMR — wiki (Tier 1, directly observed)

- Procedure module catalog has three levels: **Test Group** (e.g., "Gynecology Laboratory Services") → **Procedure Order** (orderable item, e.g., "Cervical Cytology", with an "Order from" location = where tests will be performed) → **Discrete Results** (expected result definitions under the orderable). [A]
- Supporting vocabularies are configurable lists: body sites, specimen types, routes, result statuses, report statuses, units, lateralities. [A]
- Laboratory service locations (internal or external) are defined in an address book as "Lab service" type; external-lab communication exists as a separate "Laboratory Exchange" add-on. [A]
- Order flow (directly observed): place order → "click save and transmit" → order appears under "pending review" → staff update status / add results manually → once "signed off" under pending review, "the status automatically appears under 'patient results' and updates the 'procedure order' for that specific encounter". [A]
- "In order for a test to appear on the 'pending review' tab, the tests ordered must be correctly configured — otherwise it fails silently." [A] — practical coupling between catalog configuration and fulfillment tracking.
- Requisition forms can be generated for the patient's procedures (paper leg of the transmission). Even a referral can be "transmitted". [A]
- Clinical rules / CDR engine exist as a separate decision-support mechanism ("Some tasks, especially recurring or that which could be encapsulated in a rule, are best handled using clinical rules"). [A]
- ONC certification: certified criteria include 170.315(a)(1) (CPOE–medications) and 170.315(a)(2) (CPOE–laboratory), among others; separate e-prescribing module (OpenEMR ePrescribe / WENO exchange) and Pharmacy Dispensary module exist. [A]
- Release history: "Computer Aided Medical Ordering System (CAMOS) module" shipped in v2.8.2, October 2007 — a documented, older ordering module within the same product lineage. [A] — historical anchor.

### MEDITECH Expanse — product pages (Tier 2)

- Orders named as a core "data in" physician process: "The 'data in' challenge includes processes like documentation, orders, notes, problems, and more." [A for existence in this product; marketing-level depth]
- "Expanse includes a library of intuitive widgets and shortcuts, **customizable order sets**, and streamlined workflows — so physicians can practice their way." [A for existence; structure undocumented]
- Expanse Now mobile app: physicians "remotely manage routine tasks from their smartphones". [A for existence]
- Vendor ships the fulfillment side as separate solution areas: Expanse for Nurses, Expanse Pharmacy, Expanse Pathology; Clinical Decision Support is a dedicated solutions area; evidence-based toolkits exist. [A for existence]
- Care settings span acute, ED, ambulatory, critical care, therapies, etc. [A for positioning]

### Oracle Health — product page (Tier 2, positioning only)

- Clinical suite exists as the physician-facing EHR core ("Transform your EHR... Easily document and access critical information"); no order-entry specifics publicly reachable. [A for positioning; no workflow claims]

### ONC Health IT Certification Program (regulatory source, Tier 1)

- Criteria §170.315(a)(1) CPOE–medications, (a)(2) CPOE–laboratory, (a)(3) CPOE–diagnostic imaging exist; "To meet the Base electronic health record (EHR) definition, providers must possess technology that has been certified to at least one of the following" [A]
- (a)(2) regulation text: "Enable a user to record, change, and access laboratory orders" + optional "Include a 'reason for order' field." [A]
- Clarification: "This provision does not focus on the transmission of laboratory orders, only on the ability of a user to record, change, and access the laboratory order." [A] — transmission/routing is explicitly out of scope of the criterion → not definitional for the Type.
- CPOE criteria carry attached privacy/security criteria (§170.315(d)) and safety-enhanced design (g)(3). [A]

## Cross-product Comparison

| Dimension | OpenMRS | OpenEMR | MEDITECH Expanse | Oracle Health | Verdict |
|---|---|---|---|---|---|
| Order = provider request for a patient | yes ("request from a provider") | yes (procedure orders tied to patient + encounter) | yes (orders as core physician process) | assumed by category; not directly observed | **Core** |
| Orderable item from a catalog vocabulary | concept ("the item being requested") | 3-level configurable procedure catalog | undocumented (customizable order sets imply catalog) | undocumented | **Core** (form varies) |
| Per-order actions: new / revise / discontinue / renew | explicit (NEW/REVISE/DISCONTINUE/RENEW) | revise/discontinue implicit in module (orders changeable per ONC "record, change") | undocumented | undocumented | **Core** (lifecycle management) |
| Priority/timing semantics | ROUTINE / STAT / ON_SCHEDULED_DATE + dates | undocumented | undocumented | undocumented | Common (single-product direct; conservative treatment) |
| Care-setting distinction (inpatient/outpatient) | explicit field | ambulatory only (single setting) | acute/ED/ambulatory positioning | acute positioning | Common structure |
| Transmission/routing to fulfilling party | not modeled at API level | "save and transmit" to internal/external lab location; requisitions | department modules exist | undocumented | **Common, not definitional** (ONC explicitly excludes transmission) |
| Fulfillment-side status tracking | explicitly out (results later as Observations) | pending review → status → signed off → patient results | nurse/pharmacy/pathology modules | undocumented | Common (linkage to execution is the practical point) |
| Results linked back to orders | results recorded as Observations | signed-off results update the procedure order + patient results | pathology/lab modules | undocumented | Common |
| Order-time decision support | not in order resource (CDR/rules as separate mechanism) | clinical rules engine (separate) | dedicated CDS solutions area | undocumented | Common capability, **not definitional** |
| Order sets / bundles | no | no | yes ("customizable order sets") | undocumented | Common in hospital EHRs (single-product direct evidence → keep qualified) |
| Signature/verification | not observed at API level | sign-off on result review (fulfillment side) | undocumented | undocumented | Ordering-side signature: widely expected, weakly evidenced → qualified wording |
| Charge capture linkage | no | fee sheet is a separate billing mechanism (not observed linked) | revenue cycle is separate suite | separate suite | Optional/adjacent |
| Mobile ordering | no | Android apps exist (general) | Expanse Now | undocumented | Optional |
| Standalone vs EHR-embedded | module of a platform | module of an EHR | module of an EHR | module of a suite | **Realization pattern: embedded is dominant** |

## Abstraction

### L0 — Defining Invariant (deliberately minimal)

An application of this Type is recognizable if and only if all of the following hold:

1. **Patient-specific order record** — an identified clinician records an order bound to one identified patient (and typically to a care encounter/context).
2. **Identified orderable item with execution parameters** — each order names a specific item from an orderable vocabulary (medication, test, procedure, referral…) plus the parameters needed to act on it. The vocabulary may be small and locally configured; free-text-only "orders" inside a note do not constitute this Type.
3. **Shared accessibility within the care process** — the order is not a private note: it is recorded in a system where other authorized participants (nurses, departments, covering clinicians) can access it and act on it. This is what makes it order entry + management rather than documentation.
4. **Managed order lifecycle** — orders can be added, changed, superseded, and stopped over time, and the per-patient order history persists (active vs past orders remain distinguishable).

Remove #1/#2 → not clinical ordering (generic task management). Remove #3 → personal to-do list / documentation. Remove #4 → a fixed list that cannot reflect care reality; "order management" in the leaf name fails.

Deliberately NOT in L0: decision support, order sets, priority vocabularies, signature workflow, routing/transmission, charge capture, results handling, mobile, cloud. Historical check below confirms older/smaller products satisfy L0 without them.

### L1 — Common Mature Structure

- Configurable order catalog governance (order types/classes, grouped catalogs, catalog maintenance)
- Priority & timing semantics (routine/urgent/scheduled/as-needed patterns; effective dates)
- Order sets / bundles for conditions or pathways
- Order-time decision support (duplicate checks, interaction/allergy warnings, guidance) surfaced inside the entry flow
- Status tracking with fulfillment acknowledgment (pending / in process / completed / cancelled — conceptual; labels vary)
- Results linkage back to orders; patient results view
- Transmission to fulfilling departments/external organizations (with paper requisitions as a fallback leg)
- Signature/verification workflow (ordering-side signature; result sign-off; secondary sign-off for supervised clinicians)
- Clinician personalization (favorites, templates, quick orders) and a chart-level orders summary (active orders first)
- Fulfillment-side worklists derived from orders
- Audit trails and role-scoped access (required in US-certified implementations via attached privacy/security criteria)
- Mobile access to routine order tasks

### L2 — Variant / Optional Structure

- Setting packaging: inpatient vs ambulatory vs ED emphasis; care-setting tagging
- Breadth of orderable classes: US certification anchors on medications/laboratory/diagnostic imaging; products extend to nursing orders, consults, dietary, supplies, blood products, referrals (class inventory is local)
- Structured vs free-text depth of order details
- Realization: EHR-embedded module (dominant) vs standalone ordering surface
- Governance of orders placed on another clinician's behalf (verbal/telephone orders, countersignature) — jurisdiction- and product-dependent
- Integration rails: HL7 order/result messaging, FHIR resources, CDS Hooks; handoff to a dedicated e-prescribing rail for medication orders
- Charge capture coupling to orders
- AI assistance (draft orders, ambient-note linkage)
- Regional adoption context (US certification/incentive framework shaped the modern feature set)

### L3 — Vendor-specific (kept out of the final document)

- OpenMRS: REST `order` resource field names; DrugOrder/TestOrder subtypes; concept-driven orderables
- OpenEMR: "Procedure" module naming; Test Group / Procedure Order / Discrete Results ladder; "pending review" tab mechanics; CAMOS (2007) module; WENO e-prescribing exchange
- MEDITECH: Expanse Now app; evidence-based toolkits; Expanse Pharmacy/Pathology module split
- Cerner/Oracle Health: PowerOrders/PowerPlans naming (known, NOT verified in this pass — excluded from evidence)
- Epic: Order Composer / Best Practice Advisories naming (known, NOT verified — 403; excluded from evidence)

## Vendor-specific Findings

See L3 above. Additionally: OpenEMR's silent-failure coupling ("test must be correctly configured - otherwise it fails silently" for pending-review appearance) is a product-specific implementation quirk, not a Type behavior. MEDITECH's "customizable order sets" phrasing is the only direct order-set evidence in the sample → order sets stay at L1 with qualified wording in the final document.

## Boundary Findings

1. **vs EHR**: CPOE is almost always realized as a module inside an EHR/chart (all three commercial-and-platform sampled products; ONC treats CPOE criteria as part of the Base EHR definition). It remains a legitimate separate Type because its users, objects, lifecycle, and interfaces are distinct and independently named/regulatable. Rule of thumb: the EHR owns the chart; the order-management capability owns the request-for-action record and its lifecycle. Removing the order record + lifecycle from an EHR yields documentation/results systems; removing the chart from CPOE leaves an unusable fragment — that asymmetry is the boundary.
2. **vs Electronic Prescribing**: medication orders inside this Type can hand off to dedicated e-prescribing rails (OpenEMR ships both an order module and a separate ePrescribe module). The seam: prescribing = medication-specific ordering with external pharmacy transmission/benefit interactions; CPOE = the general order record across all classes with internal fulfillment routing. If the product only orders medications through an external prescribing network, it is e-prescribing, not this Type.
3. **vs Clinical Decision Support System**: CDS in this Type appears as checks embedded in the order flow (and the open-source sample keeps the rules engine as a separate mechanism). A CDSS Type centers on evaluation/advice over data; here advice is a moment inside ordering. Remove decision support and this Type remains fully intact (OpenMRS order model has no CDS fields) → CDS is capability, not core.
4. **vs LIS / RIS / Pharmacy Management / Nursing Information System**: these are fulfillment-side systems — they receive orders, execute, and return results/status. OpenMRS states it directly ("An Order only records an intention...; results... recorded later as Observations"); OpenEMR shows the receiving loop (pending review → results → sign-off). The Type boundary is the ordering side of that hand-off.
5. **vs commerce "Order Management System / OMS" (§05.07)**: lexical collision only — goods orders, inventory, fulfillment logistics. No shared model beyond the word "order". No taxonomy action.
6. **"What to remove" test**: remove the per-patient clinical intent + care-team accessibility (keep scheduling) → Patient Scheduling. Keep only the medication class + external pharmacy transmission → Electronic Prescribing. Keep the fulfillment/execution side → LIS/RIS/Pharmacy systems. Keep the plan (not discrete orders) → Care Plan Management. Each removal collapses into a neighboring Type, confirming the four-part L0.

## Historical / Market-Sample Check

- Directly evidenced older sample: OpenEMR's CAMOS "Computer Aided Medical Ordering System" module (2007, per release history) and the 2011–2014-era procedure-order documentation still describe catalog + order + transmit + review — the L0 fits a decade-old open-source module with none of today's CDS/order-sets/mobile.
- OpenMRS (designed for resource-constrained global-health settings) satisfies L0 with a small concept catalog, no signature machinery at API level, and no routing model — the definition does not over-fit to US hospital EHRs.
- Pre-digital paper ordering practice (order sheets, verbal orders) is the conceptual ancestor; L0 is written so that an early-generation electronic order-entry system (catalog + per-patient order + shared access + change/discontinue) qualifies without requiring CDS, structured medications, or transmission. Precise verification of 1970s–80s systems (HELP, Regenstrief, VA/CPRS) was not possible in this pass (VA source timed out); this is recorded as an uncertainty, and the definition was kept minimal precisely to avoid over-fitting to the modern US market.

## Uncertainties

1. Ordering-side signature/verification and verbal/telephone-order countersignature: standard industry expectations, but only fulfillment-side sign-off is directly evidenced in the sample. Final document uses qualified wording only.
2. Order sets: single-product direct evidence (MEDITECH). Treated as common mature structure, not definitional.
3. Priority vocabularies: directly observed only in OpenMRS (ROUTINE/STAT/ON_SCHEDULED_DATE). Final document describes the pattern without asserting universal values.
4. Charge capture coupling and inventory decrementing: not evidenced in sample; excluded from the final document.
5. Epic and Oracle Health operational documentation unavailable; their inclusion is market-structural, with zero workflow claims.
6. Exact status vocabularies vary by product; the final document presents conceptual states only.

## Final Synthesis

A CPOE / Clinical Order Management application is the clinician-side system for recording requests for clinical action — medications, laboratory tests, diagnostic imaging, procedures, nursing tasks, consults, referrals — as patient-specific orders drawn from an orderable catalog, made accessible to the care team and fulfilling departments, and managed through a lifecycle of creation, revision, renewal, discontinuation, and persistent per-patient order history. Its defining core is small: identified orderer + patient + orderable item with parameters; shared accessibility; managed lifecycle. Decision support, order sets, priority vocabularies, signature workflows, transmission, results linkage, and mobile access are common mature structures that make the Type safe and efficient but do not define it. It is overwhelmingly realized as a module of an EHR, with fulfillment-side systems (LIS/RIS/pharmacy) as the receiving counterpart, e-prescribing as the medication-transmission rail, and standalone CDSS as adjacent advice machinery.
