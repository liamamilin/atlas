# Research Notes — Scientific Core Facility Management

Research date: 2026-09-09
Slug: scientific-core-facility-management
Directory leaf: Scientific Core Facility Management (Section 22 — Healthcare & Life Sciences)

---

## Research Goal

This pass had two goals:

1. **Primary (taxonomy):** determine whether "Scientific Core Facility Management" (§22 Healthcare & Life Sciences) is a distinct Application Type, or the same market family already documented under the sibling leaf **Research Core Facility Management** (§23 Education, Research & Knowledge Institutions, processed 2026-09-09). The two directory placements — healthcare vs education/research — make this a live alias question.
2. **Secondary (substance):** if the same family, verify from fresh evidence that the sibling's three-leg core holds unchanged on the healthcare/clinical side (hospital cores, medical-school cores), and check whether any healthcare-specific structure (clinical billing, patient samples, clinical regulation) would justify a separate Type.

## Initial Boundary

Initial hypothesis (before research):

- A "scientific core facility" is the same kind of shared instrumentation/service facility as a "research core facility" — the qualifier varies by institution, not by software category.
- The §22 placement suggests hospital/academic-medical-center cores; the §23 placement suggests university cores. The market's products (core facility management software) are known to serve both.
- Expected nearest neighbors (inherited from the sibling pass): LIMS/Research LIMS (sample-centric), Scientific Instrument Management (asset lifecycle), Resource Calendar (booking without economics), Research Animal Facility Management (sibling shared-facility type), LIS (clinical testing), Laboratory Billing / outreach (clinical-side charging).
- Key open question: is there a distinct healthcare-side product population (hospital core facility software with clinical billing/regulatory machinery), or do hospitals buy the same products?

## Research Questions

1. What does the market itself call this category — do vendors maintain separate "scientific" vs "research" core facility product lines?
2. Do hospitals and academic medical centers run core facilities on the same products as universities?
3. Does the three-leg core (rate-bearing catalog / identified-user attribution / usage-to-recharge) hold unchanged for hospital-based cores?
4. Is there any healthcare-specific structure (patient billing, clinical regulation, clinical sample workflows) that is definitional on this side?
5. Where does this Type end against LIS / clinical lab billing on the healthcare side?
6. What is the facility-type breadth (which scientific disciplines run cores on this software)?

## Representative Products

Selected for market representation, documentation quality, different product philosophy, and — for this pass — explicit healthcare-side customer evidence. Three products carry fresh direct evidence in this pass; the sibling pass's four-product sample (same market) is used as corroborating context, not as a substitute for this pass's own observations.

| Product | Vendor | Why selected | Angle |
|---|---|---|---|
| iLab Operations Software | Agilent | Dominant academic/medical-center platform; official help site reachable (Tier 1) | Entity/role/financial model from official glossary |
| BookitLab | Prog4biz | Self-labels "Core Facility Management Software"; uses "scientific core operations" language; hospital customer (Hadassah University Hospital) | Vendor-side lexical bridge "scientific" ↔ core facility management |
| Stratocore PPMS | Stratocore | Category page "Core Facility Software"; hospitals among stated customer base; Emory School of Medicine case study | Healthcare-customer evidence + core-type taxonomy |

NEMO was attempted as a fourth sample (nemosoftware.com); the site returned an empty response (the sibling pass had the same result). Dropped per the network-restriction rule; no claim depends on it.

## Sources

Tier 1 (official operational documentation):

- Agilent iLab Help Site — https://help.ilab.agilent.com/ (root)
  - Key iLab Terms (glossary): https://help.ilab.agilent.com/en_US/99540-getting-started-with-ilab/261285-key-ilab-terms.html

Tier 2 (official product pages):

- BookitLab — https://www.bookitlab.com/ (home) and https://www.bookitlab.com/solution/core-facility-management (page title "Core Facility Management Software")
- Stratocore PPMS — https://www.stratocore.com/ (home) and https://www.stratocore.com/solutions/core-facilities (page title "Core Facility Software")

Access limitations:

- Agilent's marketing product page for iLab was not fetched in this pass (the sibling pass recorded HTTP 403 on 2026-09-09); iLab evidence rests on its official help site, which is the stronger tier for operational structure.
- NEMO unreachable (empty response), dropped after one attempt this pass.
- Two institutional-page probes for "scientific core facility" naming (Helmholtz Munich; Cincinnati Children's core facilities) returned 404 and were dropped per the network rule. Institution-side terminology is therefore evidenced through vendor pages (customer names, testimonials, case studies) rather than institutional pages.

---

## Product A — iLab Operations Software (Agilent)

### Key observations (evidence layer A — official help site, fetched this pass)

**Entity model** (Key iLab Terms glossary):

- Institution → contains Core Facilities / Shared Resources, Labs/Groups, Departments (optional), Centers.
- "Core Facility / Shared Resource: an entity that offers services or access to resources for customers… each Core has an online store-front that customers can use to identify the offerings available and directly order products/services. For core administrators and staff, iLab provides workflows to help deliver services, manage resources, complete billing and generate reports."
- Lab/Group: users supervised by a PI and/or Lab/Group Managers; "typically used as the primary way to organize access to Funds and manage financial approvals for purchases at Core Facilities."
- Fund: "the general term used to describe a way for users to pay for services… a Fund may be known as a 'Grant number', 'Chart Field String', 'Speed Code', 'Account Number', 'Project ID' or any other identifier." Funds are allocated to Labs/Groups and assigned to members by the PI/Lab Manager; users choose from the Funds made available to them when ordering or reserving.
- Service request; Charge ("an individual 'line item' that corresponds to a specific product/service provided by a core"); Resource/Equipment (time-based reservation target — "often represents a piece of equipment, but can also refer to other resources such as specific facility or time with specialists"); Schedule/Calendar; Reservation.
- Financial Approval: "typically a financial approval step needs to be completed before the transaction can be completed" — PI or designated Lab/Group Manager approves explicitly, unless below a configurable Approval Threshold (auto-approved).
- Financial Integration (fund allocation + billing-data upload to internal/external billing systems); ID integration (login with institutional credentials).

**Roles**: Institutional Administrator; PI (manages users, controls financial access/approvals); Lab/Group Manager (PI's delegate); Lab/Group Member; Core Administrator (modifies core workflow, generates billing events and reports); Core Member (staff performing workflow functions); "Core Customer" (role-in-context, not a separate account type).

**Interpretation**: the glossary alone states the full economic spine — storefront catalog, identified lab/group attribution, payment-source selection, financial approval, charges, billing upload. The Fund concept is explicitly name-agnostic ("any other identifier"), which is the structural reason hospital cost centers fit without any model change.

---

## Product B — BookitLab (Prog4biz)

### Key observations (evidence layer A — official product pages, fetched this pass)

**Category self-labeling**: the product page is titled "Core Facility Management Software". The same page describes the system as "built for **scientific core operations**" and its pricing controls as "designed for shared **scientific facilities**"; the home page says "Bookitlab has been used in leading **scientific institutions** around the world since 2007". This is direct vendor-side lexical evidence that the "scientific" qualifier names the same product family the sibling pass documented — not a separate category.

**Module set** (core-facility product page): dynamic scheduling (instruments, rooms, services, staff, "any other bookable resource"); inventory (consumables/reagents/assets, barcode/mobile scanning, "costs captured & chargeback ready"); request management (service/sample/supply/operational requests, configurable approvals, booking- and inventory-aware); controlled access & verified usage (permissions tied to roles and training status; software rules and hardware locks; kiosk, assisted, and supervised usage models; real-time usage for monitoring and billing); billing & chargeback (charges across reservations/usage/services/consumables; chargebacks, invoicing, pricing by user or project); asset management (lifecycle, maintenance, calibration, status); reporting & analytics (utilization, revenue/chargebacks, downtime, service demand).

**Add-ons**: Sample Management ("sample intake, labeling, tracking, pricing, and LIMS-ready workflows"); Interactive Floorplans; Animal Facility Management; Loan Desk; Publications (DOI capture linked to instruments/projects/usage); Multi Language.

**Healthcare-side customers**: Hadassah University Hospital appears in the customer logo wall (twice across pages). Testimonial: "As director of the Interdepartmental Core Facility at the Sackler School of Medicine I really needed a program that would allow me to monitor and control booking, usage and billing of the many devices in our ever growing unit… At present we have over 150 research labs with 500 registered users on line using our facilities." (Bar-Ilan University — a medical-school interdepartmental core facility.)

**Interpretation**: one product, one structure, serving university cores, medical-school cores, a hospital, biotech, and (per the home page's lab-type list) analytical-testing and manufacturing/quality labs. The "scientific" vocabulary is the vendor's own umbrella for the same facility operation.

---

## Product C — Stratocore PPMS

### Key observations (evidence layer A — official product pages, fetched this pass)

**Category self-labeling**: the solutions page is titled "Core Facility Software". The home page states: "Trusted by over 250 organisations – from universities and **hospitals** to biotech and pharmaceutical companies."

**Healthcare-side customers** (vendor-published testimonials/logo wall):

- Cincinnati Children's Hospital Medical Center (testimonial by name)
- Amsterdam UMC — "Associate Professor, Microscopy and Cytometry Core Facility Director (VUmc location), Amsterdam UMC"
- Harvard Medical School (testimonial by name)
- Westmead Institute for Medical Research (Director of Scientific Operations)

**Case study** (Emory University): "Emory University's core research facilities are organized across several academic units, **including the School of Medicine**" — direct evidence that a single deployment spans university and medical-school cores, i.e., the §22 and §23 contexts are one operational population, not two.

**Core-type taxonomy** (solutions page): instrument-based cores vs service-based cores, then genomics, proteomics, metabolomics, flow cytometry, sequencing, vector, light microscopy, electron microscopy, histology, structural biology, NMR, bioinformatics, mass spectrometry, and "other cores" (cryo-preservation, behavioural research, translational support). Each core-type block repeats the same machinery: booking/access/training, request forms/validation/phases/staff assignment, dynamic pricing by user group/project/scenario, automated billing with ERP integration, usage tracking, maintenance/incidents, reporting.

**Feature set** (home page): booking and queuing, priorities/restrictions, user budget codes, dynamic scenario pricing, real-time usage tracking; maintenance & incident management; asset catalogue; service ordering (questionnaires, validation, sample manifests, staff assignment per service line, service phases); automated billing ("unlimited price and subsidy rules; financial permissions for PIs, Groups, Users and Projects; financial account managers/owners; ERP financial system integration; automated financial journals and PDF invoices"); training management; hardware interlock; publication tracking; inventory; API.

**Interpretation**: PPMS's own marketing taxonomy shows the market's facility-type breadth (biomedical-dominant but explicitly open-ended: "other cores… behavioural research or translational support") and its customer breadth (universities, hospitals, biotech, pharma) on one product. No healthcare-specific module appears anywhere in the fetched pages.

---

## Cross-product Comparison

| Dimension | iLab | BookitLab | PPMS | Layer |
|---|---|---|---|---|
| Category self-label | (help site; product = core facility operations) | "Core Facility Management Software"; "scientific core operations"; "shared scientific facilities" | "Core Facility Software" | A |
| Shared instrument/service catalog presented as storefront | "online store-front" per Core | service catalogs module; bookable instruments/rooms/services/staff | "Asset Catalogue… searchable directory" of instruments, services, facilities | A/B |
| Time-based reservation on per-resource schedule | Schedule/Calendar per Resource/Equipment; Reservation = claim on a time slot | visual calendar/timeline; conflict detection | booking/queuing, priorities, instrument hours | A/B |
| Reservation/request attributed to identified user + group + payment source | Lab/Group + Fund chosen at order/reservation | pricing by user or project; chargebacks | user budget codes; financial permissions for PIs/Groups/Users/Projects | A/B |
| Financial approval before work | explicit PI/Lab-Manager approval; configurable auto-approval threshold | approval workflows | financial permissions and approvals | A/B |
| Rates, subsidies, price tiers | pricing per resource; subsidies; center funds | rate structures; pricing by user/project | unlimited price & subsidy rules; dynamic scenario pricing | A/B |
| Charges → funding sources → invoices | Funds ("grant number… or any other identifier"); billing upload | invoices from usage/requests; ERP connectors | automated invoices & journals; ERP integration | A/B |
| Training/qualification gating | required forms; core approval (training modules exist; not fetched in detail this pass) | "tie access permissions to roles and training status"; hardware locks | training management; "access tied to training validation" | A/B |
| Actual-usage capture | Kiosk module (sibling pass, layer A) | kiosk/assisted/supervised usage models; real-time usage | real-time usage tracking; hardware interlock | A/B |
| Service requests as parallel arm | Service request + quote + approval + status | request management with forms/approvals/milestones | service ordering with questionnaires/validation/phases | A/B |
| Maintenance & incidents | schedule banners/unavailable time (sibling pass) | work orders, maintenance, calibration, incidents | maintenance scheduling, incident logging, downtime reporting | A/B |
| Healthcare customers on the same product | (academic medical centers widely reported; not verified this pass) | Hadassah University Hospital; Sackler School of Medicine interdepartmental core | Cincinnati Children's; Amsterdam UMC; Harvard Medical School; Emory case study incl. School of Medicine | A |
| Healthcare-specific module (clinical billing, patient records, CLIA/CAP-type regulatory layer) | not present in fetched pages | not present in fetched pages | not present in fetched pages | A (absence) |
| Sample handling | generic request forms | Sample Management add-on ("LIMS-ready workflows") | sample manifests in service ordering | A/B |
| Facility-type breadth | cores as institutional entities (type-agnostic) | scientific institutions; analytical testing & manufacturing labs also named | instrument/service-based cores + 13 named scientific core types + "other cores" | A/B |

Stable commonalities (layer B, corroborating the sibling pass's four-product sample): storefront catalog; per-resource schedule booking; user+group+payment-source attribution; financial approval; rates/subsidies; charges→funding sources→invoices; training gating; usage capture; service requests; maintenance; reporting; SSO/ERP integration.

**The decisive finding for the taxonomy question**: all three products serve healthcare institutions (hospitals, medical schools) with the same structure they serve universities; none ships a healthcare-specific structural layer; and the vendors' own category language ("Core Facility Management Software", "Core Facility Software", "scientific core operations") treats "scientific" as the umbrella adjective for the same facilities the sibling documented as "research" core facilities.

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures (independently re-derived this pass from iLab's glossary and corroborated at layer B by BookitLab and PPMS; identical in substance to the sibling pass's L0, which is itself evidence that the two leaves resolve to one Type):

1. **The shared facility catalog as the managed, rate-bearing offering.** The facility's shared instruments and services held as managed objects — instruments bookable as time on schedules, services orderable as requests — each carrying description, visibility control, and pricing, presented to the user population as the facility's storefront/catalog.
   Remove → an asset registry or a rate list with no operation.

2. **Identified-user reservation/request with per-user, per-group usage attribution.** Users act as identified members of groups (labs/departments/teams): they reserve instrument time or submit service requests; every reservation/request is attributed to the identified user and their group and carries a payment source; access is commonly gated by qualification.
   Remove → an anonymous/public booking board; the accountability and billing join-key disappear.

3. **The usage-to-recharge loop.** Recorded usage and completed work are priced at facility rates (with internal/external tiers and subsidies), accumulated as charges, and billed on a recurring cycle to funding sources (grants, departmental/hospital accounts, POs), producing invoices/statements and utilization/revenue reporting.
   Remove → a resource calendar / scheduling tool; the facility's economic operation disappears.

Jointly-held load-bearing tests (same as sibling's, re-verified):

- 1 alone = asset registry / rate list
- 2 without 1 = generic booking site
- 3 without 1+2 = billing shell over nothing
- 1+2 without 3 = resource calendar
- 1+3 without 2 = rate card with no attributable usage
- 2+3 without 1 = usage metering with no facility catalog

### L1 — Common Mature Structure

- training/qualification management gating access (records, verification, progressive access; hardware enforcement via locks/interlocks)
- service request workflows (forms/questionnaires, quotes, validation, phases, staff assignment)
- actual-usage capture at the instrument (kiosk, workstation app, card readers, interlocks, walk-up sessions)
- maintenance & incident management (downtime, work orders, scheduling)
- instrument/asset lifecycle records (acquisition → retirement; calibration)
- reporting & analytics (utilization, revenue; BI exports)
- financial integrations (ERP upload, journals, fund provisioning)
- identity integration (SSO with institutional credentials)
- multi-facility institutional deployment
- notifications/messaging to users
- consumables/inventory management

### L2 — Variant / Optional Structure

- external/commercial user commerce (POs, credit card, wire)
- subsidy models (automatic subsidies, centrally-assigned funds, split charges)
- publication/research-output tracking linked to facility usage
- scientific project management (milestones, multi-step validation)
- sample manifests / sample-tracking add-ons ("LIMS-ready" per one vendor)
- animal facility management, loan desk, floorplans, ELN-lite (module-level adjacencies in one product)
- non-biomedical scientific cores (engineering, analytical testing, manufacturing/quality labs) — the same machinery applied outside the life sciences
- deployment: cloud vs self-hosted; licensing posture
- non-institutional operators (pharma internal facilities, biotech, CROs, incubator shared labs)

### L3 — Vendor-specific Structure

(Research Notes only)

- iLab: "Fund" terminology and synonyms; Center Assigned Funds; configurable Approval Threshold; Kiosk module; Agilent ownership; "Core Facility / Shared Resource" naming.
- PPMS: "PPMS" name; Stratobox hardware interlock; Institut Pasteur lineage; "dynamic scenario pricing"; the 13-name core-type marketing taxonomy; Power BI emphasis; vendor-published ROI statistics (not independently verified).
- BookitLab: Prog4biz company; module packaging; "assemblies"/"modes" reservation configuration; Lite ELN; animal facility module; Loan Desk; Interactive Floorplans; vendor-published user/instrument counts (not independently verified).

## Alias Determination (the taxonomy finding)

**Conclusion: "Scientific Core Facility Management" is an ALIAS of "Research Core Facility Management" — one market family, one Application Type, two directory names.**

Evidence:

1. **Vendor category language is singular.** The sampled vendors self-label one category — "Core Facility Management Software" (BookitLab page title), "Core Facility Software" (PPMS page title). No vendor maintains separate "scientific" vs "research" core facility product lines, and no product population was found that serves "scientific core facilities" but not "research core facilities" (or vice versa).
2. **The "scientific" qualifier is the market's own umbrella word for the same facilities.** BookitLab describes its core-facility product as "built for scientific core operations" serving "shared scientific facilities" and "scientific institutions" — the same product the sibling pass documented from its "research" framing.
3. **Healthcare institutions are customers of the same products with the same structure.** PPMS: hospitals in its stated customer base, with named hospital/medical-school testimonials (Cincinnati Children's, Amsterdam UMC, Harvard Medical School) and an Emory case study whose cores span "several academic units, including the School of Medicine". BookitLab: Hadassah University Hospital in its logo wall and a medical-school interdepartmental core facility testimonial. The §22 placement (healthcare) and §23 placement (education/research) therefore describe customer context, not product or structure differences.
4. **The three-leg core holds unchanged on the healthcare side.** The payment-source concept is explicitly name-agnostic (iLab: "Grant number… Account Number, Project ID or any other identifier"), so hospital cost centers and departmental accounts fit without structural change. No healthcare-specific definitional structure was observed: no clinical/patient billing machinery, no clinical-regulatory layer (CLIA/CAP-class) appears in any fetched core-facility product page; sample handling exists only as an optional add-on on both sides.
5. **The sibling pass's independent four-product sample reached the same core** (catalog / attribution / recharge) from the research angle — two independent passes converging on one model is strong alias evidence.

What would have falsified the alias (and was not found): a healthcare-only product family with patient-facing billing or clinical-regulatory machinery as the center; a vendor maintaining distinct "scientific" and "research" product lines; hospital cores running structurally different software (they do not, per the customer evidence above).

## Boundary Findings

Inherited from and re-confirmed against the sibling pass; the healthcare-side seam is new:

**vs LIS (Laboratory Information System) — the healthcare-side seam.** LIS is patient/clinical-specimen testing: orders for patient care, results to clinical record systems, regulated clinical lab operation. A hospital's research core facility is not its clinical lab: the core serves researchers with booking/access/recharge machinery. Test: remove the researcher-catalog/attribution/recharge loop and keep patient-specimen testing → LIS territory. A hospital can run both, on different systems.

**vs Laboratory Billing / outreach charging (clinical side).** Charging for clinical services to patients/insurers/payers is healthcare revenue-cycle machinery, not facility recharge. The recharge loop here bills internal funding sources and external research customers, not payers.

**vs LIMS / Research LIMS.** Sample/assay-centric vs access/usage/economics-centric. Sample manifests and sample-tracking add-ons appear in core-facility products as optional depth; the center stays scheduling+recharge. Test: remove scheduling/recharge and keep sample-assay workflows → LIMS.

**vs Scientific Instrument Management.** Asset registry/maintenance/calibration/lifecycle is one operational ring here; the center is the facility's service operation. Test: remove scheduling/billing/users and keep asset lifecycle → Scientific Instrument Management / CMMS.

**vs Resource Calendar.** Bookings without the rate-bearing catalog, funding-source charging, financial approval, and recharge reporting. Test: remove leg 3 → Resource Calendar.

**vs Research Animal Facility Management.** Sibling shared-facility type: same attribution/recharge family, different managed subject (animal colonies vs instruments/services). One sampled vendor ships animal facility management as a separate module — market evidence they are siblings, not the same type.

**"Remove what to become another type" summary:**

- remove the recharge loop → Resource Calendar
- remove the shared-facility/multi-group context (single lab, no recharge) → single-lab scheduling tooling
- remove scheduling/access and keep samples+assays → LIMS / Research LIMS
- remove scheduling/billing and keep asset lifecycle → Scientific Instrument Management / CMMS
- replace instruments/services with patient specimens and clinical orders → LIS
- replace instruments/services with animal colonies → Research Animal Facility Management

## Historical / Market-Sample Check

- **Paper-era facility (pre-software):** sign-up sheet on the instrument (schedule/reservation), usage logbook (per-user attribution), training before keys were handed out (qualification gate), monthly recharge invoices to grant/cost-center numbers (usage-to-recharge loop). All three legs satisfied without software. ✓ (carried over from the sibling pass's check; unchanged by the healthcare framing — hospital cores ran the same paper practice)
- **Non-university operators:** PPMS explicitly names hospitals, biotech, and pharmaceutical companies in its customer base; BookitLab names scientific institutions across the US, Canada, Australia, Europe, China, and the Middle East, with a hospital and analytical/manufacturing labs among them. The type is not university-specific. ✓
- **Non-biomedical cores:** PPMS's "other cores" (behavioural research, translational support) and BookitLab's analytical-testing/manufacturing-lab positioning; the sibling sample had an engineering-school core testimonial. The machinery is discipline-agnostic. ✓
- **Non-charging facilities:** fully subsidized facilities run the same machinery with charges resolving to zero or to subsidies (iLab documents subsidies as automatic line items). ✓

Conclusion: the L0 survives the historical and market-breadth check; the alias conclusion is stable across eras and customer types.

## Uncertainties

1. **Institution-side pages unreachable.** Two probes for institutional "scientific core facility" pages (Helmholtz Munich, Cincinnati Children's) returned 404 and were dropped. Institution-side naming is therefore evidenced through vendor pages (customer names, testimonials, case studies) rather than institutional pages. This weakens nothing material: the vendor pages themselves carry the "scientific" vocabulary and the hospital customers.
2. **iLab marketing page not fetched this pass** (sibling recorded HTTP 403). iLab evidence rests on its official help site — the stronger tier for operational structure. No market-share or positioning claims are made.
3. **NEMO not sampled** (empty response; sibling had the same result). A fourth product would add breadth; no claim depends on it.
4. **iLab training-module depth** not directly fetched this pass; the training claim is carried by BookitLab/PPMS direct evidence plus iLab's form/approval gating (sibling pass noted the same).
5. **Vendor-published statistics** (PPMS "250+ organisations", BookitLab "130,000+ users") are marketing claims, not independently verified; they are used only as existence/breadth evidence, not as precise facts.
6. **No healthcare-specific regulatory layer observed** — an absence claim from fetched pages, not a proof that no product anywhere offers one; assertion kept calibrated ("not present in fetched pages").

## Final Synthesis

"Scientific Core Facility Management" and "Research Core Facility Management" are two directory names for one Application Type: the operating system of a shared scientific core facility. Its defining core is three jointly-held structures:

1. the facility's shared instrument/service catalog as the managed, rate-bearing offering (the storefront);
2. identified-user reservations and service requests with per-user, per-group usage attribution and a chosen payment source (the accountability layer);
3. the usage-to-recharge loop that prices recorded usage at facility rates and bills it to funding sources, with invoices and utilization/revenue reporting (the economic loop).

Around this core, mature products add a standard ring: training/qualification gating, actual-usage capture, service request workflows, maintenance and incident management, asset lifecycle records, reporting/analytics, and integrations with institutional identity and finance systems.

The type's customer population spans universities, research institutes, hospitals and academic medical centers, medical schools, pharma/biotech, and shared/incubator laboratories — the §22 (healthcare) and §23 (education/research) directory placements cut across one market, not two. The alias is recorded for taxonomy review; this document is written from the scientific-facility lens (healthcare and cross-disciplinary breadth), and the sibling document holds the research-facility lens.
