# Research Notes — Hospital Management System

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Hospital Management System (HMS, also called Hospital Information System / HIS in many markets) actually is as an Application Type: what objects exist inside it, who operates it, how a patient's path through a hospital is administered, how services translate into money, where it stops and the EHR / departmental systems begin, and which parts of the modern feature stack are definitional vs. common vs. optional.

## Initial Boundary

Initial hypothesis (before research):

- HMS = hospital-operated administrative/operational system: patient registration, outpatient visits, admissions/discharge/transfer (ADT), bed/ward occupancy, service/charge capture across departments (lab, pharmacy, radiology), billing/settlement, stores/inventory.
- Nearest neighbors to separate from: EHR (clinical record of record), Practice Management System (physician-office/clinic scale), Healthcare Revenue Cycle Management (claims depth), Bed & Capacity Management / Patient Flow Management (focused leaves), LIS / RIS / PACS / Pharmacy Management System (departmental), ERP (non-patient institutional resources), Patient Portal (patient-facing).
- Market naming suspicion to verify: the standalone "HMS" category is strongest outside the US (South Asia, Middle East, Africa, Europe, open-source/public sector); in the US the same space is absorbed into EHR-suite + Revenue Cycle branding.

## Research Questions

1. What is the operational unit the system is organized around — patient? visit? admission episode?
2. How does registration work, and what does a "patient of record" hold?
3. How does ADT work: admission, bed assignment, transfer, discharge? What state does a bed/ward hold?
4. How do outpatient (OPD) and inpatient (IPD) flows differ, and how does one convert into the other?
5. How are services (lab tests, drugs, procedures, consultations) requested, fulfilled, and captured as charges?
6. How does the bill work: charge accumulation, rate plans, discounts/refunds/cancellations, payer routing, settlement at discharge?
7. What institutional configuration does a hospital set up (locations, departments, wards/beds, staff, price catalogs)?
8. What roles operate the system, and which permissions matter?
9. What is genuinely common vs. regional/optional (insurance/TPA machinery, government scheme integrations, accreditation packaging, multi-location, EMR depth inside the suite)?

## Representative Products

Chosen for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / segment | Evidence quality reached |
|---|---|---|
| Bahmni | Open-source HIS+EMR assembled from open-source components (OpenMRS EMR core, Odoo ERP for billing/inventory, OpenELIS lab), designed for low-resource hospitals; Digital Public Good; hospital-site hosted, offline-capable | A — official wiki (home, Feature Guide, User Guide incl. Registration / In-Patient Management / Bed Management / Billing pages) |
| GNU Health | Free-software HIS/HMIS built on the Tryton ERP framework, public-health philosophy (GNU package, UNIU-IIGH collaboration), serves health centers + hospitals, strong international/public-sector footprint | A — official docs portal, Features page (module table), Health Center user guide |
| MocDoc HMS | Commercial cloud SaaS HMS from India serving hospitals/clinics/labs across South/Southeast Asia, Middle East, Africa; suite (HMS, LIMS, clinic, pharmacy, ART/IVF, ophthalmology, dental); NABH-certified; India-scheme integrations | A for API structure (public API documentation = object-level model); Tier 2 marketing for positioning |
| MEDITECH Expanse | Large Western EHR-suite vendor (market-naming pole only) | Tier 2 — site navigation/positioning only (docs gated / page not found); used solely for market-naming signal, no operational claims |

Attempted and abandoned per network rules: docs.bahmni.org and help.instahealth.com (transport errors), GNU Health wikibooks (timeout — replaced by docs.gnuhealth.org which succeeded), InterSystems TrakCare product page (timeout), NIC eHospital e-hospital portal (transport error), MEDITECH Expanse Portfolio page (404 — root navigation captured instead).

## Sources

- Bahmni Wiki — Bahmni Home: https://bahmni.atlassian.net/wiki/spaces/BAH/overview (fetched 2026-09-08)
- Bahmni Wiki — Feature Guide: https://bahmni.atlassian.net/wiki/spaces/BAH/pages/32604183/Feature+Guide (fetched 2026-09-08)
- Bahmni Wiki — User Guide: https://bahmni.atlassian.net/wiki/spaces/BAH/pages/32014338/User+Guide (fetched 2026-09-08)
- Bahmni Wiki — Registration: https://bahmni.atlassian.net/wiki/spaces/BAH/pages/32014347/Registration (fetched 2026-09-08)
- Bahmni Wiki — In-Patient Management: https://bahmni.atlassian.net/wiki/spaces/BAH/pages/32014373/In-Patient+Management (fetched 2026-09-08)
- Bahmni Wiki — Bed Management: https://bahmni.atlassian.net/wiki/spaces/BAH/pages/707559542/Bed+Management (fetched 2026-09-08)
- Bahmni Wiki — Billing and Accounting: https://bahmni.atlassian.net/wiki/spaces/BAH/pages/32014379/Billing+and+Accounting (fetched 2026-09-08)
- GNU Health Documentation Portal: https://www.gnuhealth.org/docs/ (fetched 2026-09-08)
- GNU Health HIS — Features: https://docs.gnuhealth.org/his/features.html (fetched 2026-09-08)
- GNU Health HIS — Health Center user guide: https://docs.gnuhealth.org/his/userguide/healthcenter/index.html (fetched 2026-09-08)
- MocDoc — homepage: https://www.mocdoc.com/ (fetched 2026-09-08)
- MocDoc — HMS product page: https://www.mocdoc.com/hospital-management-system (fetched 2026-09-08)
- MocDoc — API Documentation: https://www.mocdoc.com/api/docs (fetched 2026-09-08)
- MEDITECH — site navigation (market-naming signal only): https://ehr.meditech.com/ (fetched 2026-09-08)

Evidence layers used below: A = directly observed in one product's official documentation; B = cross-product commonality in the sample; C = canonical inference from comparison + Type-boundary reasoning.

## Product A — Bahmni

### Key observations (layer A)

- Self-description: "an easy to use, complete, open source Hospital Information System (HIS) and Electronic Medical Record (EMR) that aims to meet the needs of low resource environments by leveraging a tapestry of existing open source products"; an OpenMRS distribution. Pitch: "Manage patient information across registration, point of care, investigations, and billing."
- Infrastructure posture: "Hosted and operated at the hospital site, requiring no dependence on Internet" (infrastructure-appropriate); Bahmni Connect provides an offline-capable client; tablet/laptop operation.
- Module map (Feature Guide): Patient Registration; Treatment Programs; Clinical Services (consultation, observations, diagnoses, allergies, disposition, ordering lab/radiology, prescribing, order sets, dispensing); Appointment Scheduling (services & specialities, calendar/list/weekly views); Operation Theatre Scheduling (surgical blocks, surgeries in block); Laboratory Management (dashboard, result validation, report printing, referring tests out); Radiology and PACS integration; Pharmacy Management; Patient Document Management; In-Patient Management (IPD); Bed Management; Patient Billing and Accounting; Stock/Inventory Management (lots/batches, quantity adjustments); Reporting; Administrator's Page (import/export, order-set authoring, Ward Management Admin Console, audit logs of patient data access); Login/2FA; Teleconsultation; IPD dashboards (Care View, medication administration tasks).
- Registration page: "Patient Registration provides the ability to start a patient file at a hospital. Most hospitals have a front desk where patients have to register before starting medical interactions such as consultation, lab tests, admission, procedures etc." Used by "the person at the Registration desk"; capture of name, photograph, address and hospital-specific attributes by non-clinical staff; search existing patients / add new; per-implementation configuration "can vary drastically."
- In-Patient Management page (nurse-facing): patient queue page shows "patients to be admitted, patients who are already admitted and patients who are ready to be discharged"; ward list; patient movement page supports "transfer patient from one bed to other or one ward to other or discharge a patient"; on admit, a popup can "close the OPD visit and open a new IPD visit"; bed assignment from a ward bed grid; beds already assigned shown in a distinct color, but a bed can still be double-assigned, explicitly "enabled to assign bed to new born baby with mother."
- Bed Management page (replaced the old ADT/IPD module from release 0.91): "the ability to admit, discharge and transfer a patient. A patient can be assigned to a selected bed. The bed details can also be viewed including tags." Ward layout or list views; Bed Types and Ward Layout configured in an admin console; configurable patient queues.
- Billing and Accounting page: "a doctor can prescribe drugs/medicines or place orders for patient to undergo some tests for a patient from the clinical module... The patient then proceeds to the Pharmacy or to a Billing Counter to make the payment." Sub-workflows: Manage Orders; Print Bill and Prescription; Manual Billing — Creating Quotation in Odoo; Refunding the Invoice. Billing/inventory ride on Odoo (OpenERP) — an ERP provides the ledger.
- GNU-Health-equivalent context: Bahmni is deliberately modular — hospitals can adopt parts ("Choose parts of Bahmni and integrate with existing systems").

## Product B — GNU Health

### Key observations (layer A)

- Self-description: "Welcome to the Hospital Management Information System (HIS) of GNU Health." Main areas:
  1. Demographics and Community: individuals, domiciliary units, families, socioeconomics.
  2. Patient Management: "Health encounters and evaluations, hospitalizations, clinical history and other information that makes up the electronic medical records (EMR)."
  3. **Health Center**: "Finances & billing, stock & pharmacy, staff, suppliers, beds, operating rooms and other relevant tasks to manage the health center" — operated by "administrative personnel and accountants."
  4. Laboratory and Medical Imaging: "complementary orders such as lab tests, medical and diagnostic imaging requests and workflows."
  5. Health Information System: statistics/reporting on collected data for health authorities.
- Module table highlights:
  - `health` (core): demographics, patients, evaluations, health centers, appointments, vaccinations, medicaments, conditions, health professionals.
  - `health_accounting`: "Billing, Chart of Accounts, General Ledger, Invoice handling, journals" — full ERP accounting inside the HIS.
  - `health_inpatient`: "Patient hospitalization management and history, including: Patient Registration, Bed management, Hospitalization, Nursing Plan, Discharge Plan, Reporting." (a package — the inpatient capability is installable, i.e., modular)
  - `health_insurance`: "Manages insurances, policies, plans and discounts based on products and/or categories."
  - `health_services`: "Functionality to group orders and services related to a patient evaluation, prescription or hospitalization. It also allows invoicing specific items/lines from the service document." Extensions: `health_services_lab`, `health_services_imaging`.
  - `health_stock`: stock moves "in different objects, products and contexts within the health institution operation... medicaments, vaccines, ambulatory care, hospitalization roundings and prescriptions moves."
  - `health_surgery`: surgery management incl. "Operating Room Scheduler."
  - `health_nursing`: roundings, procedures, ambulatory care sessions (outpatient + inpatient).
  - `health_lab`, `health_imaging` + Orthanc PACS integration; `health_ems` (ambulance); pediatrics/gyneco/ICU etc. (clinical-specialty depth).
- Foundation: Tryton (ERP framework) — the docs reference the Tryton framework directly; GNU Health is an ERP vertical for health.
- Health Center user guide sections: Financial Accounting; Analytic Accounting; Products and Services Management (products, categories, **invoicing patients**); Purchase Administration; Access Management (groups, users).

## Product C — MocDoc HMS

### Key observations (layer A for API object model; Tier 2 for positioning)

- Positioning: "No.1 Cloud Hospital Management System (HMS Software)"; "streamlines operations from patient registration to discharge"; suite spans Hospital Management Software, Laboratory Management Software, Pharmacy Management Software, Clinic/Polyclinic, ART/IVF, ophthalmology, dental, environmental LIMS. Customers span India, Fiji, Maldives, Nigeria, Oman/Muscat, Rwanda, Trinidad — South/Southeast Asia, Middle East, Africa.
- Regulatory/accreditation packaging (marketing): NABH Advanced certification for EMR & HMS; compliance pages for NABH self-assessment, NABH CMS; integration pages for ABDM and PMJAY (India government health schemes), NPHIES (Saudi), Aasandha (Maldives), POS, VMS (VAT), machine interfacing.
- Public API documentation — resource tree (= the platform's object model):
  - **Master Data**: Locations; Users; Providers ("billing providers... including insurance companies, corporate organizations, TPAs, and other payer organizations"); Doctors; Referrals; Investigations (lab tests/profiles); Packages; **Rateplan List / Rateplan Details ("applicable services and charges")**; Products; Stores.
  - **Patient Management**: Register Patient (returns a `phid` — patient ID; scoped by `entitykey` + `entitylocation`), Update Patient, Get Patient Info, Patient Timeline ("complete clinical timeline of a patient, including OP bills, IP bills, pharmacy bills, laboratory orders, visit notes, and other clinical activities").
  - **Appointment & Visit**: Book Appointment, Update Appointment Status, Calendar, O/P Visits, Checked In.
  - **Billing**: OP Bill Creation, Pharmacy Bill Creation.
  - **Inpatient (IP)**: I/P Admissions, I/P Discharges, I/P Room Transfers.
  - **Laboratory**: Create Lab Order, Lab Orders, Lab Results.
  - **Inventory**: Current Stock (batchwise).
  - Tele Consultation (doctors, slots, booking, block slot).
  - **MIS reports**: appointment reports; billing reports (bills, bills detailed, edited bills, OP/IP cancelled bills, OP/IP discounted bills, refund bills); pharmacy billing reports (stock sale, discounted/cancelled/returns); purchase reports (PR, PO, GRN, GReturn); inventory reports (Indent, GDN).
  - **Webhooks**: registration; appointment confirmation / reschedule / cancellation / no-show / check-in / check-out; OP bill creation / updation / cancellation.
- Operational API constraints (L3 detail): one-day-per-call retrieval model, minimum 3-second request interval, HMAC-SHA256 request signing over TLS.
- Feature blocks (marketing): Appointment Management; EMR; Billing and Analytics ("billing processes from patient registration to final invoicing"); Multi-Location Management ("centralize operations and data across multiple locations"); Security & Compliance (role-based access, HIPAA/NABH claims); Reporting and Analytics. Customer quote mentions "ward request, docket entry" as salient features.

## Product D — Market-naming signals (layer A/Tier 2, non-operational)

- MEDITECH (major US/Western EHR vendor) presents its hospital offering as "EHR Solutions" with care settings: Acute Care, Ambulatory, Critical Care, Emergency Department, Labor and Delivery, Mental Health, Oncology, Post Acute, Practice Management, Surgical Services, Therapies, Virtual Care — plus separate solution tiles for Pharmacy, Pathology, Revenue Cycle, Analytics, Patient Connect. I.e., in the Western enterprise market the HMS functionality is packaged inside an EHR-suite brand plus a Revenue Cycle line, not sold as a standalone "Hospital Management System."
- MocDoc, Bahmni, and GNU Health (South Asia / international / open-source poles) all self-identify as HMS/HIS. Conclusion: "HMS" as a named product category is strongest in non-US markets and the public/open-source sector; the underlying functional space is universal, the packaging differs by market. (Layer B observation on naming, not on structure.)

## Cross-product Comparison

| Structure | Bahmni | GNU Health | MocDoc | Evidence |
|---|---|---|---|---|
| Patient of record created at registration/front desk by non-clinical staff | Registration module (search/create, photo, address, hospital-specific attributes) | core `health` demographics/patients | Register Patient API returns `phid` | B |
| Institutional structure of record (locations/departments/wards; stores) | Location widget; wards + bed layouts in Ward Management Admin Console | health centers; Health Center area (beds, operating rooms, staff, suppliers) | `entitykey` + `entitylocation`; Locations, Stores, Doctors masters | B |
| Visit/encounter as unit of service consumption, OP vs IP distinction | OPD visit closed and IPD visit opened on admit | ambulatory encounters vs hospitalization (`health_inpatient`) | O/P Visits, I/P Admissions as separate API groups; Patient Timeline lists OP bills and IP bills | B |
| ADT: admit → bed assignment → transfer (bed/ward) → discharge | In-Patient Management + Bed Management (queues: to admit / admitted / to discharge) | `health_inpatient`: bed management, hospitalization, discharge plan | I/P Admissions, I/P Room Transfers, I/P Discharges as first-class operations | B |
| Departmental order fulfillment (lab; pharmacy; imaging) | Laboratory dashboard/validation; Pharmacy medication orders; Radiology+PACS | `health_lab`, `health_imaging`+Orthanc, stock moves for prescriptions | Create Lab Order / Lab Orders / Lab Results; Pharmacy Bill Creation; investigations masters | B |
| Service→charge→bill→settlement loop | Billing Counter; orders become payable; Odoo invoices; refunds | `health_services` groups orders/services from evaluation/prescription/hospitalization → invoicing lines; `health_accounting` GL | OP Bill / Pharmacy Bill creation; rate plans (services & charges); billing reports incl. cancelled/discounted/refund | B |
| Price/rate configuration | bill printing & Odoo quotations (pricing present; config UI not directly observed) | Products & Services management; discounts | Rateplans explicit master with "applicable services and charges" | B (weakest in Bahmni docs) |
| Payer/insurance machinery | not documented as first-class in fetched pages (cash-billing counter focus) | `health_insurance` (insurances, policies, plans, discounts) | Providers master = insurance companies, corporates, TPAs; insurance billing page | A/B mixed — common but not universal |
| Inventory/stores/purchase machinery | Inventory module (lots/batches, adjustments) | `health_stock`; Purchase Administration | Products/Stores masters; stock; purchase reports (PR/PO/GRN/GReturn); indent/GDN | B |
| OT / theatre scheduling | Operation Theatre Scheduling (surgical blocks) | `health_surgery` Operating Room Scheduler | not observed in API surface | A (2/3) |
| Appointments/OPD scheduling | Appointment Scheduling (services & specialities, calendar) | `health` appointments + calendars | Book Appointment, calendar, check-in/out webhooks | B |
| Role-based operation & audit | 2FA; audit logs of patient data access; admin roles | Access Management (groups, users) | Users master; role-based access (marketing) | B |
| Reporting/MIS | Reporting module | `health_reporting` (demographics, epidemiology) | MIS report tree (appointment/billing/pharmacy/purchase/inventory) | B |
| Multi-location/facility group operation | single-site hosted posture (Connect offline) | Federation to distributed health institutions; "participating health institutions" | Multi-Location Management explicit; entity/location model | C-leaning; common, not universal |
| EMR/clinical depth inside the same product | explicit: HIS + EMR (OpenMRS) | explicit: Patient Management = EMR area | EMR is one feature block of the suite | B |
| ERP underneath the administrative layer | Odoo/OpenERP | Tryton | n/a (SaaS; ledger not named) | A/B: two of three literally ERP-framework-based |

### Canonical abstraction (layer C)

Three jointly-held structures define the Type; every sampled product realizes all three, and each leg fails a "remove it" test:

1. **The hospital as administered institution of record** — a configured multi-department institution (locations, departments, wards and beds where inpatient care exists, staff, priceable service catalog) whose daily operations the system runs. Remove it → generic scheduling/billing/invoicing tools with no institutional subject.
2. **The patient of record and the visit/encounter as the unit of service consumption** — patients are registered at the hospital (front desk, non-clinical data) and move through visits/encounters (outpatient visit; inpatient admission episode) to which all service activity attaches. Remove it → an ERP/inventory/HR system that happens to serve a hospital (no patient).
3. **The service-to-money loop** — services delivered under the encounter (consultations, tests, drugs, procedures, bed days) are captured as charges and settled through bills/invoices and payments, with discounts/refunds/cancellations and payer routing where present. Remove it → patient-flow/registration tooling with no business loop (the recognized thin "patient administration system" pole).

The inpatient admission/ADT/bed machinery is the characteristic *workflow* of legs 1+2 for inpatient care — near-universal in hospital-targeted deployments (A in all three samples) — but it is realized as an installable module even inside sampled HMS products (GNU Health `health_inpatient` is a package; Bahmni Bed Management replaced a prior ADT module; MocDoc exposes it as a distinct API group). It is therefore held as standard mature structure just below the defining line, with the hospital's ward/bed structure belonging to leg 1. The joint-held logic: 1 alone = ERP; 2 alone = registration app; 3 alone = invoicing; 1+2 without 3 = patient administration thin pole; 2+3 without 1 = clinic/practice management scale; 1+3 without 2 = invoicing with nothing patient-anchored.

## Abstraction Hierarchy

### L0 — Defining Invariant

1. The hospital's institutional service structure of record (locations/departments/wards+beds/staff/priceable service catalog) operated by the hospital itself.
2. The registered patient of record and the visit/encounter (outpatient visit, inpatient admission episode) as the operational unit to which service activity attaches.
3. The service-to-money translation: charges captured under the encounter → bills/invoices → payment/settlement (cash and/or payer).

Historical/market-sample check (per §24): the paper-era hospital satisfies the core without any software — front-desk registration ledger (leg 2), bed board + ward structure (leg 1), cash bill book + stores ledger (leg 3). Early computerized HIS (1960s–70s "ADT + billing" systems) satisfy it. EMR depth, insurance/TPA machinery, government-scheme integrations, accreditation packaging, cloud/mobile/AI are era- or market-current and excluded. The definition survives older/regional/platform-native products (Layer C reasoning; no additional historical fetches were used — this check is structural, anchored on the paper-era analog of the same three legs).

### L1 — Common Mature Structure

- ADT/bed-ward operations: to-admit/admitted/to-discharge queues, bed assignment from ward layouts, bed/ward transfer, discharge (A in all three).
- Departmental order fulfillment surfaces: lab worklists/result validation, pharmacy dispensing, radiology order flows (B).
- Appointment/OPD scheduling with calendar/list views and check-in (B).
- OT/theatre scheduling with blocks (A in 2/3).
- Rate/price configuration (service price catalogs, rate plans, discounts) (B).
- Refunds, cancellations, discounted-bill handling in billing (A in MocDoc report tree + Bahmni refund workflow; B).
- Inventory/stores/purchase machinery (lots/batches, stock moves, PO/GRN-class documents) (B).
- Role-based access by function + audit logs of record access (B).
- Reporting/MIS (B).
- EMR/clinical capability inside the same product (B — strongest in the open-source poles; present as a module/feature block in the SaaS pole).

### L2 — Variant / Optional Structure

- Payer/insurance depth (insurers, TPAs, corporate payers, claim routing) — strong in South Asia/Middle East market and GNU Health; not first-class in Bahmni's fetched documentation → common variant, not definitional.
- Government health-scheme integrations (ABDM/PMJAY in India, NPHIES in Saudi, Aasandha in Maldives) — regional.
- Accreditation/compliance packaging (NABH certification marketing, HIPAA claims) — regional/segment.
- Multi-location/facility-group operation — segment-dependent (chains); single-site deployments equally valid.
- Offline-first / low-infrastructure deployment (Bahmni Connect; hospital-site hosting) — segment (low-resource environments).
- Teleconsultation (Bahmni, MocDoc) — era-current optional.
- Lab machine interfacing, PACS integration — optional integrations.
- Suite packaging: standalone HMS vs clinic/pharmacy/lab sibling products from the same vendor vs everything absorbed into an EHR suite (US pattern).
- Deployment: cloud SaaS vs on-premise/self-hosted vs open-source self-assembly.

### L3 — Vendor-specific (Research Notes only)

- Bahmni: OpenMRS + Odoo/OpenERP + OpenELIS assembly; Bahmni Lite edition; Bahmni Connect offline app; per-implementation configuration variability explicitly documented ("screens and workflows are not constant across all installations"); double bed assignment for newborn-with-mother; surgical blocks terminology.
- GNU Health: Tryton framework; Federation/Thalamus message server; domiciliary units & socioeconomics; contact tracing, injury surveillance, NTD packages (Chagas, dengue); WHO essential medicines; ICD-9/10/11 & ICPM coding packages; crypto/signing of medical documents; Ansible deployment.
- MocDoc: HMAC-SHA1/256 signed API with one-day-per-call retrieval and 3-second minimum interval; ART/IVF module; ophthalmology/dental variants; PR/PO/GRN/GReturn/Indent/GDN purchase-inventory vocabulary; WhatsApp report delivery mention in a customer quote; entity/location scoping of all API calls.

## Vendor-specific Findings

See L3 above. None of these are promoted into the canonical model. Note especially: two of three sampled products literally ride on ERP frameworks (Odoo, Tryton) for their ledger/billing/inventory layers — this supports the boundary reasoning vs ERP (the HMS *uses* ERP machinery; the patient-anchored encounter/charge machinery is what makes it an HMS), but "built on an ERP" is not itself a definitional property (MocDoc is a SaaS platform without a named ERP foundation).

## Boundary Findings

| Neighboring Type | Boundary judgment | "Remove what → becomes the other" |
|---|---|---|
| Electronic Health Record / EHR | Different record of record. EHR: the patient's clinical state (documentation, orders, results, decision support) is the record of record. HMS: the hospital's operations (registration, movement, beds, charges, bills) is the record of record. The two are frequently bundled in one product (Bahmni self-describes as HIS+EMR; GNU Health's Patient Management area is an EMR; US EHR suites absorb hospital operations) — the distinction is the center of gravity, not the vendor packaging. | Remove clinical-documentation depth, keep operations → HMS. Remove operations, keep the clinical record → EHR. |
| Practice Management System | Scale/institution type. Practice management serves a physician office/clinic: appointments + billing for practitioners, no wards/beds/ADT, no multi-department institutional structure. The market itself separates them (MocDoc sells Clinic Management as a distinct product). | Remove the institutional multi-department structure and inpatient operations, shrink to practitioner-side appointments+billing → Practice Management. |
| Healthcare Revenue Cycle Management | Depth of the money leg. HMS carries front-end charge capture and the billing counter inside the hospital; RCM specializes the back end (coding, claims, remittances, denials) as its own system of record. | Deepen claims/coding/denial machinery and detach from bed/ward operations → RCM. |
| Bed & Capacity Management / Patient Flow Management | Focused leaves. In an HMS the bed board and queues are one surface among many; these Types center capacity/flow prediction and coordination as the primary object. | Extract the bed/flow machinery as the primary subject → those Types. |
| LIS / RIS / PACS / Pharmacy Management System | Departmental clinical/operational systems. The HMS coordinates, orders into, and bills for them; the department's internal depth (analyzers, imaging archives, dispensing) is their territory. | Keep only one department's depth → that departmental Type. |
| Patient Registration & Intake / Patient Scheduling | Capability slices (front desk, scheduling) that exist inside the HMS and as standalone thin products. | Keep only registration or only scheduling → those Types. |
| Patient Portal / Telehealth Platform | Patient-facing vs staff-facing. HMS is operated by hospital staff; the patient-facing surfaces (portal, telehealth) are adjacent Types. | Flip to patient-facing primary user → Patient Portal / Telehealth. |
| ERP | Non-patient institutional resources. HMS's administrative layer is ERP-like (accounting, inventory, purchase — two samples literally on ERP frameworks); the registered patient + encounter + charge loop is what makes it an HMS. | Remove patients/encounters → ERP (or a hospital's generic back office). |

Market-naming asymmetry (recorded, not a taxonomy defect): in the US enterprise market the HMS functional space is sold under EHR-suite + Revenue Cycle branding; the standalone "HMS/HIS" product category is strongest in South Asia, Middle East, Africa, Europe, and the open-source/public-health sector. Products sampled here self-identify as HMS/HIS (Bahmni, GNU Health, MocDoc).

## Uncertainties

- Western enterprise pole (Epic/Oracle Health/MEDITECH/TrakCare/Dedalus) has no operational documentation in this pass; the claim that the same three-leg core exists there rests on market-naming signals (MEDITECH's care-setting/revenue-cycle structure) plus general category knowledge, not A-layer evidence. Assertions about enterprise HIS remain deliberately weak in the final document.
- Insurance/claims depth inside HMS varies widely; Bahmni's fetched pages show a cash-billing-counter posture, while GNU Health and MocDoc carry payer machinery. The final document therefore phrases payer handling as common-but-not-universal.
- Whether OPD-only deployments should still count as HMS is genuinely contested in the market (vendors sell clinic management separately, yet HMS products serve OPD-heavy facilities). The definition resolves this via the institutional-structure leg (a hospital's wards/services exist even if a given deployment uses few of them); a truly ward-less single-practice deployment is Practice Management territory. Recorded as a judgment call, not an observed fact.
- Per-product workflow minutiae (exact check-in states, exact bed-state taxonomies, exact cancellation windows) were not researched to A-layer precision and are absent from the final document by design.

## Final Synthesis

A Hospital Management System is the hospital's own operational system of record: it holds the hospital as an administered institution (locations, departments, wards and beds, staff, priceable services), registers patients and moves them through visits and inpatient admission episodes, coordinates service delivery across the hospital's own departments (consultations, laboratory, pharmacy, radiology, operating theatres), and translates the services each encounter consumes into charges, bills, and payments. ADT/bed-ward management is its most characteristic workflow; departmental clinical depth (EHR, LIS, RIS, PACS, pharmacy internals) belongs to neighboring Types, which the HMS orders into and bills. The category is named and sold as "HMS/HIS" principally in South Asian, Middle Eastern, African, European, and open-source/public-sector markets, while US enterprise vendors package the same space inside EHR suites plus revenue-cycle lines; the functional core is the same. The defining core is small and survives the paper-era analog of the same three legs (registration ledger, bed board, cash bill book).
