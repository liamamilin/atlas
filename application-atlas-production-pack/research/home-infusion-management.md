# Research Notes — Home Infusion Management

## Research Goal

Understand what "Home Infusion Management" software actually is by studying real products: what a home infusion provider's system of record contains, who uses it, how a therapy moves from referral to revenue, and where the Type's boundaries sit against the many already-processed neighboring healthcare Types (pharmacy management, home health, home care, hospice, DME, dialysis, medication management, RCM).

## Initial Boundary

Initial hypothesis: this is the provider-side system of record for a **home infusion therapy provider** — typically a home infusion pharmacy that delivers IV (and other parenteral) medications to patients at home, coordinating pharmacy production, delivery logistics, infusion nursing, clinical monitoring, and payer billing. Nearest neighbors: pharmacy management system (dispensing), home health EHR (home visit care), DME management (equipment provision), specialty pharmacy (same product family), dialysis center management (facility-based therapy sessions), ambulatory infusion center software (no leaf in directory).

## Research Questions

1. What is the service being managed? (What does a home infusion provider actually do?)
2. What are the core objects: therapy, dose, patient, referral, delivery, nursing visit, claim?
3. How does a therapy move from referral to first dose to course completion to payment?
4. Which legs are definitional vs common vs variant: compounding, nursing, delivery, billing, pumps, engagement?
5. How does this Type differ from pharmacy management systems, home health EHRs, and specialty pharmacy software — which are served by the same products?
6. Do nursing-agency-side and engagement-overlay products belong to the Type or sit beside it?

## Representative Products

Selected for market coverage, different product philosophies, and different positions in the workflow:

| Product | Vendor | Position | Why sampled |
|---|---|---|---|
| CareTend | WellSky | Dedicated home infusion + specialty pharmacy system of record (25+ yrs in market; claims largest installed base) | The full-Type pole: intake→dispense→delivery→clinical→billing in one application |
| Brightree Pharmacy (Home Infusion) | Brightree (ResMed) | Pharmacy business management platform with a home infusion line; sibling of the vendor's DME product | Referral-to-revenue pole; shares platform with DME (boundary evidence vs durable-medical-equipment-management) |
| HDMS | Universal Software Solutions | Home infusion/specialty pharmacy workflow software | Explicit dual-benefit adjudication (pharmacy NCPDP + medical ANSI X12) and delivery-management detail |
| Newleaf | Keycentrix | Next-gen pharmacy management for specialty/infusion/retail/mail-order | Infusion-specific modules (TPN, factor), accreditation-metrics angle |
| AlayaCare (Home Infusion) | AlayaCare | Home infusion software from the nursing-agency / specialty-pharmacy coordination side | The administration-leg pole: scheduling, EVV, point-of-care documentation, pharmacy↔nursing referral network |
| WeInfuse | WeInfuse | Infusion-center-first platform expanded to home infusion & specialty pharmacy | The ambulatory-infusion-center pole that shares the therapy object |
| QliqSOFT / CitusHealth | QliqSOFT / Citus (WellSky-integrated) | Patient-engagement & coordination overlays for home infusion | The overlay pole — explicitly works *alongside* the pharmacy management system; boundary evidence |

Industry-canonical source: NHIA (National Home Infusion Association) — "What is home infusion?" and "Home Infusion 101" curriculum.

## Sources

Research date: 2026-09-10. All evidence Tier-2 official vendor product/solution pages plus one industry-association definitional page and one vendor brochure PDF. No Tier-1 help-center/user-guide articles were reachable this pass (HBS hbsrx.com transport error after one attempt — abandoned per network rule). Assertion strength calibrated accordingly; no precise operational facts (numeric limits, exact stage names, defaults) asserted.

- WellSky — CareTend Home Infusion Software: https://wellsky.com/home-infusion-software/ (fetched)
- WellSky — CareTend brochure "Get to know CareTend": https://info.wellsky.com/rs/596-FKF-634/images/WS-HC071-CareTend_Brochure%5BWEB%5D.pdf (via search highlights)
- WellSky — CareTend Specialty Pharmacy: https://wellsky.com/specialty-pharmacy/ (via search highlights)
- Brightree — Home Infusion Pharmacy: https://www.brightree.com/home-infusion-pharmacy/ (fetched)
- Brightree — Pharmacy: https://www.brightree.com/pharmacy/ (via search highlights)
- Universal Software Solutions — HDMS Infusion Pharmacy Software: https://universalss.com/infusion-pharmacy-software/ (via search highlights)
- Keycentrix — Newleaf: https://keycentrix.com/newleaf/ (via search highlights)
- AlayaCare — Home Infusion Software: https://alayacare.com/home-infusion-software/ (via search highlights)
- WeInfuse — Infusion Center Software: https://weinfuse.com/infusion-center-software/ (via search highlights)
- QliqSOFT — Home Infusion: https://www.qliqsoft.com/industries/home-infusion/ (via search highlights)
- NHIA — What is home infusion?: https://nhia.org/about-home-infusion/ (fetched)
- NHIA — Home Infusion 101: https://nhia.org/education-ce/open-access-education/home-infusion-101/ (fetched)
- NHIA — 2025 Products & Services Guide: https://nhia.org/wp-content/uploads/2024/09/2025-Products-and-Services-Guide.pdf (via search highlights)

## Product Observations

### WellSky CareTend (evidence layer A)

- Positioning: "home infusion and specialty pharmacy organizations"; also supports ambulatory infusion centers (AIC), DME/HME, and nursing workflows. "Over 25 years of experience in home infusion technology."
- Stated end-to-end scope (brochure): "intake and scheduling • dispense and fulfillment • delivery and shipping • clinical practice • decision support • billing and collection."
- Clinical tools: "medication profiles, care plans, customizable patient assessments, progress notes, lab tracking, scheduling, and automated patient follow up."
- Fulfillment: "task-based work lists designed specifically for infusion pharmacies… from intake to billing."
- Billing: "bill for compounded IV drugs, TPN and Factor products"; metrics named: revenue adjustments, bad debt reserve, DSO, A/R aging, COGS.
- Inventory: "real-time perpetual inventory of all your drugs, supplies, and equipment"; barcode automation of ordering/receiving/warehousing/withdrawal.
- Delivery: WellSky Delivery Manager integration — route optimization, real-time truck tracking, e-signature, proof of delivery (GPS + photo), courier integration (FedEx/USPS/UPS).
- Intake network: Surescripts e-prescribing integration; CoverMyMeds prior-auth automation; controlled-substance/PDMP state reporting.
- Engagement: engagement manager powered by Citus Health — secure messages, patient education, e-signatures, digital delivery tickets, satisfaction surveys.
- Resource Manager (companion): staff/patient scheduling, assessments, care planning, EVV-style data tracking for home infusion & infusion centers.
- Interoperability: REST APIs, CommonWell network enrollment.

### Brightree Pharmacy — Home Infusion (evidence layer A)

- Positioning: "home infusion pharmacy solution… from billing and compliance documentation to clinical oversight… a single, easily managed home infusion pharmacy platform."
- Named capabilities: **Clinical oversight** ("integrated clinician decision support, including standard practices and multidisciplinary care plan creation, outcomes tracking"); **Compounding support** ("Dispense Infusion therapy medications and parenteral nutrition (TPN) prescriptions, print supporting documentation like labels"); **Billing and compliance documentation** ("more accurate and consistent billing with automation… proactive monitoring").
- Workflow framing: "a comprehensive system from referral all the way to revenue in one platform"; "tailored workflows for folks who do intake, for pharmacists"; "pharmacist experience" role view with worklists; document management; electronic patient communications; "automated overnight claim submission."
- Customer evidence: CarePro Home Health & Home Infusion — IV therapy to patients 200 miles away across four states.
- Platform context: same vendor platform serves HME/DME and O&P (suite adjacency — matches the DME pass's recorded note).

### Universal Software Solutions HDMS (evidence layer A)

- Therapy scope: "Factor, TPN, Chemo, IVIG, Antibiotics, and more"; controlled substances with customized reporting.
- Inventory: multi-location (warehouse, supply closet, locations, mobile inventory vehicles), purchase orders, transfers, adjustments.
- Billing: "a unified system that adjudicates both pharmacy and medical benefits… test adjudications and eligibility checks with automatic reversals… bill either the NCPDP or ANSI X12 Professional type transactions, depending on the patient's benefit type"; authorization management; denial and appeals management; collection manager.
- Delivery: "Work Order Insight" — order status, delivery carriers (FedEx, UPS, USPS, dropship), PV2 checks, order verification, delivery confirmation.
- Companion products (WorkLogix workflow, Stowpoint) for HME/DME and infusion pharmacy operations.

### Keycentrix Newleaf (evidence layer A)

- Positioning: pharmacy management for "specialty, infusion, retail, or mail-order."
- Infusion-specific pain points named by the vendor: "Home infusion reimbursement is limited by policy and accreditation requirements… maintains compliant documentation, streamlines claims, and tracks accreditation metrics"; "Infusion billing is highly complex — interface with R2 Health automates code generation, applies payer-specific rules, and validates claim data"; "Infusion pharmacies have complex workflows — custom workflows tailored to infusion pharmacies including TPN and factor infusion modules along with features like OTC Kitting."

### AlayaCare Home Infusion (evidence layer A)

- Serves: "Specialty Pharmacies, Nursing Agencies, Mobile IV."
- "Integrates with pharmacy management solutions, includes robust medication management, clinical documentation capabilities and handles referral management between you and infusion nursing agencies."
- Nursing-agency side: mobile app with point-of-care documentation and configurable forms; back-office dashboards; "intelligent scheduling and referral marketplace for efficient in-home and clinic/ambulatory infusions"; "GPS and time-stamped visit verification."
- Nursing referral network: "send, receive, and track visit referrals across multiple organizations."
- Inventory: "via integration" (not native) — confirms the nursing-side pole does not carry the production leg natively.
- FAQ confirms: automated scheduling (centralized or field-created, with automations, schedule/route optimization); inventory via integration.

### WeInfuse (evidence layer A)

- Infusion-center-first: chair-driven appointment scheduling, buy-and-bill and specialty inventory ("order, check in, manage… in-out system"), nurse-built treatment notes capturing "clinical and inventory information."
- "Our pharmacy solution includes all the same patient management, patient intake, and financial tools that exist in WeInfuse, plus home infusion and specialty pharmacy workflows."
- Powers 850+ infusion centers; expanded to home infusion and specialty pharmacy.

### QliqSOFT / CitusHealth — engagement overlays (evidence layer A)

- QliqSOFT self-description: "Home infusion is a coordination sport, pharmacy, nursing, courier, prescriber, payer, and patient all have to land on the same day."
- Functions: referral relay in one thread (intake, benefits investigation, prior auth, pharmacy, nursing, delivery), consents/AOB e-signature, patient group chats per patient, pre-refill scored assessments, delivery-visit sync confirmation, after-hours AI voice agents with on-call routing, time-stamped documentation synced back to the EMR.
- Explicit positioning: "Works alongside your pharmacy management system" — an overlay, not the system of record.
- Regulatory context cited (US): Medicare HIT supplier obligations (professional services 7 days/week, 24 hours/day per plan of care), payment contingent on documentation, accreditation (Joint Commission, ACHC, CHAP), prior auth.
- CitusHealth (NHIA guide): "complete end-to-end solution specifically designed to help infusion providers and pharmacies accelerate speed to therapy"; schedule coordination, real-time nursing notes, plan-of-care updates. Now integrated into CareTend as its engagement manager.

### NHIA — industry-canonical definition (evidence layer A, industry association)

- Service definition: "Home infusion involves the administration of a medication through a needle or catheter in a setting other than a hospital or other medical facility."
- Provider definition: "An infusion therapy provider is a state-licensed, independently accredited and qualified pharmacy that specializes in provision of medically necessary infusion therapies to patients in their homes or other alternate-sites. The infusion therapy always originates with a prescription order from a qualified physician… A clinical team of pharmacists and nurses, along with other support staff coordinates care for the patient that includes—but is not limited to—verifying insurance coverage, designing a therapy plan based on the therapy and patient needs, sterile medication preparation and delivery, arranging nursing services, drug administration education and support, clinical monitoring of labs and response to therapy, 24/7 support, and coordination with the prescribing physician."
- Nursing model: "infusion nursing services are either provided directly by the infusion pharmacy by employed nurses, or through a collaboration with an affiliated nursing agency."
- Pumps: "generally reserved for specific situations such as continuous or extended infusions… or when administering drugs three or more times per day" — therapy-dependent, not universal.
- Reimbursement: "nearly all commercial health plans treat home infusion therapy as a medical service, reimbursed under their medical benefit (rather than the prescription drug benefit) and paid for using a per diem for clinical services, supplies, and equipment with separate payments for the drugs and nursing visits." Medicare fee-for-service is "the only major health plan… that does not offer comprehensive coverage."
- Accreditation: voluntary but required by most commercial insurers (Joint Commission, ACHC, CHAP, HQAA, NABP, URAC, The Compliance Team).
- Settings: home + ambulatory infusion centers/suites; "Home infusion providers are unique in that they can coordinate care wherever the patient may be."
- Therapy range: antibiotic, antifungal, antiviral, chemotherapy, hydration, pain management, parenteral nutrition; blood factors, corticosteroids, erythropoietin, infliximab, inotropic medications, growth hormones, immunoglobulin, natalizumab.
- "Home Infusion 101" curriculum units: The Patient Journey / Pharmacy Responsibilities / Sterile Compounding / Nursing Services / Reimbursement Methodologies / Revenue Cycle Management — the industry's own decomposition of the discipline.

## Cross-product Comparison

| Structure | CareTend | Brightree | HDMS | Newleaf | AlayaCare | WeInfuse | QliqSOFT/Citus |
|---|---|---|---|---|---|---|---|
| Referral/intake + benefits/auth | ✓ (intake; CoverMyMeds; Surescripts) | ✓ ("referral… get patients on service") | ✓ (authorization mgmt) | ✓ (claims/validates) | ✓ (referral mgmt, network) | ✓ (patient intake) | ✓ (referral relay) |
| Therapy/prescription of record (course) | ✓ (prescription mgmt, refills) | ✓ (infusion/TPN prescriptions) | ✓ (therapy types) | ✓ (TPN/factor modules) | partial (medication mgmt) | ✓ | ✓ (thread context) |
| Dose production & dispense (task workflow) | ✓ (task-based work lists) | ✓ (pharmacist worklists, compounding) | ✓ (fill workflow) | ✓ (custom infusion workflows) | via integration | ✓ (pharmacy workflow) | — |
| Sterile compounding emphasis | ✓ (compounded drugs) | ✓ (compounding support, labels) | implicit | ✓ (TPN/factor) | — | — | — |
| Delivery/shipping to home | ✓ (Delivery Manager, POD) | ✓ (mobile delivery) | ✓ (Work Order Insight, carriers) | ✓ (shipment scheduling) | ✓ (scheduling/routing) | — | ✓ (delivery-visit sync) |
| Nursing coordination & documentation | ✓ (scheduling, Resource Manager, EVV-style) | ✓ (clinical oversight, care plans) | — (not surfaced) | — (not surfaced) | ✓ (core: POC docs, EVV, marketplace) | ✓ (treatment notes) | ✓ (nursing notes, on-call) |
| Clinical monitoring (labs, assessments, follow-up) | ✓ (lab tracking, assessments, follow-up) | ✓ (outcomes tracking) | — | — | ✓ (outcomes reporting) | ✓ (treatment notes) | ✓ (assessments) |
| Inventory (drugs/supplies/equipment) | ✓ (perpetual, barcode) | ✓ (inventory module) | ✓ (multi-location, vehicles) | ✓ | via integration | ✓ (buy-and-bill) | — |
| Billing/collections | ✓ (compounded IV, TPN, Factor; AR metrics) | ✓ (referral→revenue, overnight claims) | ✓ (dual-benefit NCPDP+X12, denials) | ✓ (R2 Health interface) | ✓ (agency billing) | ✓ (financial tools) | — |
| Patient engagement surfaces | ✓ (Citus engagement manager) | ✓ (digital experience) | — | ✓ (outreach logging) | ✓ | ✓ (reminders) | ✓ (core purpose) |
| Analytics/reporting | ✓ (DSO, AR aging, COGS) | ✓ (data & analytics) | ✓ (custom reports) | ✓ (accreditation metrics) | ✓ (outcomes) | ✓ | — |

Reading: the four full-system poles (CareTend, Brightree, HDMS, Newleaf) hold the same spine — referral/intake → therapy of record → dose production → home delivery → administration/clinical → billing. AlayaCare (nursing pole) and WeInfuse (infusion-center pole) hold subsets; QliqSOFT/Citus hold only the coordination/engagement layer and explicitly position alongside the system of record.

## Canonical Model

### L0 — Defining Invariant (four jointly-held structures)

1. **The home infusion therapy of record** — a physician-ordered parenteral medication therapy for an identified patient, designed as a plan (drug, dose, schedule, duration, route/device) to be administered outside a facility — in the patient's home, or in the provider's infusion suite as an alternate site. The anchor object to which intake, production, delivery, nursing, monitoring, and billing all attach. *(Remove → generic pharmacy dispensing or a referral/benefits tool.)*
2. **Dose preparation & dispense** — the provider's pharmacy prepares (commonly by sterile compounding) and dispenses each dose of the therapy, advanced through a task-based fulfillment workflow with pharmacist verification. *(Remove → nursing-only coordination or home health; the drug-production signature disappears.)*
3. **Home delivery & administration coordination** — the provider coordinates getting each dose into the patient's hands (courier/shipment of drugs, supplies, and delivery devices) and getting it administered (employed or contracted infusion nurses for first-dose teaching and ongoing care, or a trained patient/caregiver self-administering), with delivery and visit synchronized. *(Remove → retail/mail-order/specialty pharmacy.)*
4. **The therapy-to-revenue loop** — the delivered therapy is billed to payers — commonly under the medical benefit with a per-diem for services/supplies/equipment plus separate drug and nursing-visit payments, or under the pharmacy benefit — with benefits verification, authorization, claims, and collection tracked against the therapy. *(Remove → clinical coordination with no business loop.)*

Jointly-held load-bearing:
- 1 alone = prescription/patient record
- 2 without 1 = compounding batch log with no patient therapy
- 3 without 1+2 = courier logistics
- 4 without 1–3 = generic pharmacy billing
- 1+2 without 3 = facility pharmacy dispensing for pickup (specialty-pharmacy-shaped)
- 1+3 without 2 = nursing agency coordinating administration of drugs it does not produce
- 2+3 without 1 = anonymous production/delivery
- 1+4 without 2+3 = benefits/authorization case management

### L1 — Common Mature Structure

- Referral intake funnel with benefits investigation and prior authorization (all sampled products)
- Task-based dispense/fulfillment worklists with role views (pharmacist experience)
- Clinical chart: medication profile, care plan, assessments, progress notes, lab tracking, automated follow-up
- Nursing visit scheduling + point-of-care (mobile) documentation; EVV-style verification in US implementations
- Delivery/shipping management: route planning, courier integration, proof of delivery, delivery-visit sync
- Perpetual inventory of drugs, supplies, and equipment with barcode; lot/expiry and controlled-substance handling
- Dual-benefit claims adjudication (pharmacy NCPDP and/or medical ANSI X12 professional), denial/appeal handling, AR metrics (DSO, AR aging, COGS, bad debt)
- Patient engagement: secure messaging, education, e-signature, delivery tickets, surveys
- Analytics/reporting; accreditation-metrics and compliance documentation
- E-prescribing intake, PA automation, PDMP reporting, interoperability APIs

### L2 — Variant / Optional

- Sterile compounding depth (batch compounding, IV workflow systems) — therapy-dependent; some therapies dispensed as manufactured products
- Infusion pump/equipment fleet management — therapy-dependent (NHIA: pumps reserved for specific situations)
- Nursing model: employed nurses vs contracted nursing agency vs patient/caregiver self-administration after teaching
- Site extension: ambulatory infusion suite/AIC services supplementing home delivery
- Therapy specialization: anti-infective, nutrition support/TPN, factor/bleeding disorders, IVIG/immunology, oncology, hydration, pain, inotropic therapy
- Business model: independent local/regional/national pharmacy, hospital-affiliated, specialty-pharmacy-attached
- Regime: US commercial per-diem medical-benefit model vs Medicare's partial coverage vs non-US OPAT-style services (not sampled)
- Consumer-pay mobile IV/wellness infusion (AlayaCare "Mobile IV" segment)
- Packaging: standalone system of record vs overlay products (engagement, delivery, RCM services) sold alongside it

### L3 — Vendor-specific (Research Notes only)

- WellSky: Delivery Manager, Resource Manager, Revenue Cycle Services (outsourced billing with named performance targets), Citus-powered engagement manager, CommonWell enrollment
- Brightree: "pharmacist experience" role view, R2 Health-class claim interfaces (Newleaf), overnight claim submission branding
- QliqSOFT: Quincy AI assessments/voice agents, on-call routing engine
- Universal: WorkLogix/Stowpoint companions, PV2 checks
- NHIA per-diem definition and coding standard as industry artifacts

## Historical / Market-Sample Check

Pre-software home infusion (1980s–90s US, and non-US OPAT-style services): a licensed infusion pharmacy received a physician's prescription, verified insurance, designed a therapy plan, sterile-prepared doses, couriered them with supplies and (where needed) pumps to the home, arranged employed or affiliated nurses for first-dose teaching and ongoing care, reviewed labs, supported patients 24/7 by phone, and billed per diem plus drug/nursing charges. All four L0 legs existed on paper, phone, and fax. Modern machinery (e-prescribing, EVV, engagement apps, route optimization, AI triage, dual-benefit e-adjudication) is implementation, not definition. **Historical check passed.**

## Vendor-specific Findings

See L3 above. Notable: WellSky claims market leadership ("proven partner to more home infusion and specialty pharmacy organizations than any other software provider"; "more than 10,000 people use WellSky's home infusion technologies daily") — marketing claims, not structural evidence. Brightree/WellSky both package DME + pharmacy + home infusion on one platform family, confirming the DME pass's "suite adjacency" note from the other side.

## Boundary Findings

1. **vs Pharmacy Management System (processed)**: PMS core = prescription → drug catalog → patient medication profile → fill pipeline for dispense of packaged drug products at the pharmacy. HIM binds a *course of parenteral therapy at home* with production, home delivery, administration coordination, and course-level (per-diem/dual-benefit) billing. HBS-class pharmacy systems literally serve home infusion pharmacies — the PMS machinery is embedded; the defining objects (therapy course, dose schedule, delivery, nursing, dual-benefit billing) exceed it. Remove delivery + administration + course-billing → PMS territory.
2. **vs Home Health EHR/Management (processed)**: home health = skilled nursing/therapy visits under an authorizing plan of care; no drug production, no dose dispense. HIM's nursing-visit machinery resembles home health's, but the therapy-of-record + production + delivery legs are the difference. Remove legs 2+3 → home health territory.
3. **vs Home Care Agency Management (processed)**: non-skilled personal/support care; no clinical therapy, no drug production. Clear.
4. **vs Durable Medical Equipment Management (processed)**: DME = equipment as the billable product (rental/sale + custody movement); HIM = the drug therapy as the anchor, equipment (pumps, supplies) subordinate to the dose. The DME pass recorded "pharmacy/home-infusion suite adjacency"; this pass confirms from the infusion side (Brightree/WellSky platform families serve both). Pumps straddle: in HIM the pump is delivery equipment for a dose; in DME the unit is the product.
5. **vs Dialysis Center Management (processed)**: dialysis = prescribed treatment sessions executed at a station (or home dialysis with patient-side capture); the dose object is a dialysis treatment, not a dispensed/compounded drug product with a supply chain. Home-therapy dialysis programs were recorded as variants in that pass. Keep both.
6. **vs Medication Management Platform (processed)**: MMP = one care organization's internal medication-use process (stock estate + regimen-driven execution + accountable event record) across its points of care. HIM = one provider's therapy-delivery *business* to patients' homes, with delivery logistics and payer money path. Overlap in "regimen drives dispense," different center of gravity.
7. **vs Healthcare Revenue Cycle Management (processed)**: HIM's billing leg is therapy-specific (per-diem, dual-benefit, authorization-gated) and embedded in the delivery workflow; RCM is the generic provider money pipeline. Same seam as the DME/SNF passes: embedded money path vs standalone RCM.
8. **vs Clinical Communication Platform (processed)**: QliqSOFT/Citus are coordination/engagement overlays that work *alongside* the pharmacy management system — not the system of record. Different Type.
9. **vs Remote Patient Monitoring (processed)**: RPM anchors on device-originated physiological data streams; HIM may include monitoring (labs, assessments) but anchors on the therapy and its doses. Clear.
10. **vs Electronic Prescribing (processed)**: e-Rx feeds the intake leg (Surescripts integration in CareTend). Clear.
11. **Taxonomy gaps (no directory leaves)**: **specialty pharmacy management** and **ambulatory infusion center management** are served by the same product family (CareTend, Brightree, Newleaf, HDMS, WeInfuse all serve infusion + specialty + AIC markets) but have no leaves in the directory. The distinguishing object for HIM is the parenteral therapy course with home delivery/administration coordination; specialty pharmacy dispenses high-touch drugs (usually manufactured products, shipped, with patient-support programs, no administration coordination); AIC is chair-based on-site administration. Recorded in STATUS Boundary Issues; no unilateral directory change.
12. **Nursing-agency-side tools** (AlayaCare's nursing-agency segment): they hold the administration leg only (drugs produced elsewhere). Graded as administration-leg participants in the home infusion workflow rather than the full Type; the canonical Type binds all four legs in one system of record. Flagged as a boundary question worth revisiting if a nursing-agency-infusion leaf ever exists.

## Uncertainties

- No Tier-1 help-center/user-guide articles fetched; all product evidence is Tier-2 marketing/product pages + one brochure. Exact workflow stage names, numeric limits, defaults, and compounding-module depth inside the products are unverified and intentionally not asserted in the final document.
- Compounding workflow depth (batch records, IV workflow system integration) not directly observed in any sampled product's documentation — kept conceptual ("preparation, commonly sterile compounding").
- Non-US home infusion software market not sampled (sample is US-dominated); the canonical model is written regime-neutral, but regime machinery (Medicare HIT benefit, EVV, accreditation bodies) is documented as US-realization only.
- Whether a standalone nursing-agency infusion tool should ever be formalized as its own Type — recorded as a boundary question, not resolved by directory change.

## Final Synthesis

Home Infusion Management is the home infusion provider's system of record: the application in which a licensed infusion pharmacy runs its therapy-delivery business — from referral intake and benefits verification, through the therapy plan of record, dose preparation and dispense, home delivery and nursing coordination, clinical monitoring, to per-diem/dual-benefit billing and collection. The defining core is the four jointly-held legs (therapy of record + dose production + home delivery/administration coordination + therapy-to-revenue loop). Everything else — compounding depth, pumps, EVV, engagement apps, AI triage, accreditation machinery — is common mature structure or variant. The Type sits between pharmacy management (dispense transaction), home health (home visits without drug production), and specialty pharmacy (same product family, different anchor object), and is the canonical system-of-record leaf for the home-and-alternate-site infusion market.
