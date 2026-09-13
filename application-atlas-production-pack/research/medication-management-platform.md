# Research Notes — Medication Management Platform

## Research Goal

Understand what a **Medication Management Platform** actually is as an Application Type, from real products' official documentation — in particular:

- What does "medication management" mean in the healthcare software market — the care organization's medication-use process, or the consumer's personal medication routine? The phrase is used by both markets.
- What is the managed object on the provider side: the medication stock, the medication order, the administration event, or the whole chain?
- How does the "closed-loop" medication process (order → verify → dispense → administer → reconcile → monitor) map onto software structures, and which parts does this Type own vs. its neighbors (EHR, CPOE, e-prescribing, pharmacy management system, nursing information system)?
- Is the EHR-embedded module the only form, or does a standalone market exist (automation vendors)?
- Would older, non-automated medication practice (paper MAR, unit-dose carts, narcotic ledgers) still fit the definition?

## Initial Boundary

Leaf: `Medication Management Platform` (§22 Healthcare & Life Sciences), listed between Pharmacy Management System and Electronic Prescribing.

Hypothesis at start: the Type centers on the **medication-use process inside a care organization** — the chain from stock through verification, dispensing, and administration to the patient — rather than on any single document or transaction. Two ambiguities to resolve:

1. **Consumer-pole ambiguity**: consumer "medication management" apps (pill reminders, adherence trackers) self-describe with the same phrase. Different users, objects, and workflows — likely a different Type sharing a name.
2. **EHR-embedding ambiguity**: prior passes flagged that medication ordering/management appears as an L1 capability of the EHR (research/electronic-health-record-ehr.md boundary flag) and requested a cross-check of the e-prescribing × MMP seam (research/electronic-prescribing.md). The Pharmacy Management System pass already graded this leaf "broader lifecycle — reconciliation, administration, and monitoring across care settings" vs. the PMS's "pharmacy's dispensing operations" (applications/pharmacy-management-system.md Related Types table).

Directory neighbors: Electronic Health Record / EHR, Practice Management System, CPOE / Clinical Order Management, Electronic Prescribing, Pharmacy Management System, Nursing Information System, Clinical Decision Support System, Care Plan Management, Long-term Care EHR, Home Infusion Management, Durable Medical Equipment Management (all §22 unless noted).

## Research Questions

1. What does the market's dominant vendor framing of "medication management" cover — which care settings, which roles, which objects?
2. What is the supply side: how is the organization's medication stock held, counted, located, and consumed?
3. What is the clinical side: how do medication orders/regimens drive preparation, dispensing, and administration?
4. What is the record side: which events are documented, with what attribution and accountability (especially controlled substances)?
5. Where does medication reconciliation (admission/discharge/transfer) sit?
6. What verification machinery exists (pharmacist review, barcode/identity checks, interaction/dose checking) — definitional or standard?
7. What are the boundaries vs EHR, PMS, e-prescribing, CPOE, NIS, CDSS, generic inventory?
8. Is there a standalone market outside the EHR? What do automation vendors actually sell?
9. What is the consumer pole, and is it the same Type?
10. Would the paper-era form satisfy the definition?

## Representative Products

Selected for market representation + different product philosophies + different customer tiers + coverage of both phrase-readings:

| Product | Pole | Posture | Customer tier |
|---|---|---|---|
| **Omnicell** (OmniSphere, XT cabinets, XR2, Central Pharmacy Manager, Diversion Management, Medication Adherence) | medication automation + enterprise software platform | "Unifying Medication Management Across the Enterprise" — robotics + smart devices + software + services across inpatient and outpatient settings | enterprise health systems; retail/LTC/correctional pharmacies |
| **Swisslog Healthcare** | medication automation + transport + software | "Medication management means more than just handling drugs" — pharmacy automation + physical transport + software/analytics | hospitals and healthcare facilities (EU-rooted, global) |
| **MEDITECH Expanse Pharmacy** | EHR-embedded pharmacist module | pharmacist's verification/dispensing/med-rec/rounds workflow inside the Expanse EHR, with PGx CDS and smart-pump integration | mid-size hospitals/health systems |
| **Medisafe** | consumer pole + pharma engagement platform | consumer medication app (reminders, intake logging, caregiver tools) now positioned as "patient engagement engine for pharma portfolios" | patients; pharma brand teams; providers |
| **MyTherapy** (smartpatient) | consumer pole, pure | free personal medication reminder + intake diary + health tracking + doctor report sharing | consumers (global, 13 languages) |

Attempted and abandoned: **BD Pyxis** (bd.com — 403 on two URL patterns; the other major automation vendor, absent from this sample), **Epic Willow** (epic.com — 403; EHR-embedded pole covered by MEDITECH instead), **Swisslog hospital-pharmacy deep page** (404; root + medication-management hub used instead).

## Sources

Research date: **2026-09-10**. All official vendor pages (Tier 2 — product/solution/marketing pages). No help-center or user-guide article was reached in this pass.

- Omnicell — home: https://www.omnicell.com/ ; OmniSphere cloud platform: https://www.omnicell.com/omnisphere/ ; Points of Care: https://www.omnicell.com/points-of-care/ ; Central Pharmacy: https://www.omnicell.com/central-pharmacy/ ; Diversion Management: https://www.omnicell.com/points-of-care/diversion-management/ ; Medication Adherence: https://www.omnicell.com/medication-adherence/
- Swisslog Healthcare — root (medication-management hub): https://www.swisslog-healthcare.com/ (nav: /en-cn/medication-management, central-pharmacy, transport-automation, outpatient-pharmacy, correctional-facilities, consolidated-service-center)
- MEDITECH — Expanse Pharmacy: https://ehr.meditech.com/ehr-solutions/expanse-pharmacy
- Medisafe — home: https://www.medisafe.com/ ; platform: https://www.medisafe.com/platform
- MyTherapy — home: https://www.mytherapyapp.com/

Unreachable: bd.com (403 ×2 — Pyxis MedStation / medication-management capability pages), epic.com (403 — Willow pharmacy page), swisslog-healthcare.com deep care-area page (404 ×1, root used).

**Sourcing limitation (applies to all products):** evidence is Tier-2 official product/solution pages. No operational help-center documentation was fetched. Assertions are therefore kept at the structure/workflow level; precise operational facts (numeric limits, timing windows, default settings, per-plan capabilities, device models' exact behaviors) are NOT asserted in the final document. Vendor performance metrics (e.g., "54% nursing time saved", "99% savings") are recorded here as claims only.

Internal corroboration from prior processed passes (atlas evidence, not external): applications/pharmacy-management-system.md (Related Types seam), applications/electronic-health-record-ehr.md (medication record as chart L1), applications/long-term-care-ehr.md (MAR machinery inside resident record), applications/nursing-information-system.md (bedside medication administration as nursing documentation), research/electronic-prescribing.md (seam cross-check request), applications/clinical-decision-support-system.md (medication checking as CDS family).

## Product Observations

### Omnicell — Evidence layer: A

Positioning: "Pharmacy Management | Medication Management". Portfolio organized by care setting: Inpatient (IV Room, Central Pharmacy, Points of Care) and Outpatient (Specialty Pharmacy, Retail Pharmacy, Medication Adherence). Four capability blocks: Robotics ("Removing human interaction from medication management processes"), Smart Devices ("closing gaps in safety and inventory visibility"), Software ("greater visibility to medication inventory… data insights to optimize the pharmacy supply chain to reduce medication waste"), Services.

- **OmniSphere** (cloud platform): "designed to be the brain that powers a body of proven medication management automation, providing scalability, one source of truth, interoperability with EHRs, and advanced intelligence to unify Omnicell devices and power a connected enterprise." "A more intuitive, efficient, and collaborative medication management experience for **both pharmacy and nursing teams**." "Enterprise-wide visibility and actionable insights."
- **Points of Care**: "the bedside exchange of medication from nurse to patient is critical… countbacks, restocks, reconciliation, and other manual tasks force nurses to spend more time managing medications." XT Automated Dispensing Cabinets "guide clinicians directly to the drugs needed, minimizing labor-intensive steps of counting and tracking medications." Cloud software "generates dashboards to quickly identify inventory and potential drug diversion issues… operational and user-level data across multiple sites… real-time advanced analytics, data visualizations, and powerful reporting and benchmarking."
- **Central Pharmacy**: "the medication dispensing hub of every hospital." XR2 robotic central pharmacy system; Pharmacy Carousel (vertical storage/retrieval); **Central Pharmacy Manager** software — "real-time visibility to every dose and corresponding expiration date managed in XR2… streamlines medication distribution from wholesaler receipt"; **XT Controlled Substance Manager** — "simplifies controlled substance distribution"; MedVision — "web-enabled software… workflows and inventory management tools"; blister packagers/medication packagers; **Enterprise Medication Manager** brochure: "One Platform to Manage medications Throughout the Care Continuum."
- **Diversion Management**: "comprehensive tracking of controlled substances and staff access across care locations, technologies, and workflows"; "centralized monitoring of controlled substance administration… single, enterprise view of possible diversion risk across units, roles, and care settings"; "embedded documentation, audit trails, and investigation workflows… regulatory readiness."
- **Medication Adherence** (outpatient pole): adherence **packaging** — single-dose blister cards, MultiMed 30-day time-pass blister cards, Guided Packing software, unit-dose printing, label applicators, deblistering, MTS fillers/sealers ("Designed to streamline packaging for Correctional and Long Term Care Pharmacies"), AccuFlex/E3 single-dose automation.

Observation: Omnicell's "medication management" = the organization's entire medication supply-and-use chain: stock in (wholesaler receipt) → central pharmacy estate (robotic storage, dose-level + expiry visibility) → dispensing (carousel, robots, cabinets) → points of care (nurse exchange, countback, restock) → accountability (controlled substances, diversion surveillance) → analytics (inventory optimization, benchmarking) — unified by a cloud platform interoperable with the EHR, serving pharmacy AND nursing. The patient's regimen appears implicitly (dispensing is for patients; reconciliation named at points of care); the supply estate and event accountability are explicit.

### Swisslog Healthcare — Evidence layer: A

Positioning (site hub): "Medication Management: Transport, Software & Automation." "Medication management means more than just handling drugs. Your aspiration is to ensure seamless supply through pharmacy and transport automation as well as overarching software solutions… integrated solutions." "Our approach combines physical transport with pharmacy automation - enabled by software and analytics."

- Solution areas: **Consolidated Service Center**, **Central Pharmacy**, **Hospital Transport** (automation), **Outpatient Pharmacy**, **Correctional facilities**; products: Pharmacy Automation, medical refrigerators/freezers (Tenutō), Transport Automation, Software.
- Framing: the hospital's medication flow as a physical + digital logistics chain — items move through automated storage, compounding, and transport (e.g., pneumatic tube class) under software control with analytics.

Observation: same center as Omnicell (the facility's medication supply chain), different emphasis: physical transport and logistics automation foregrounded; software/analytics as the enabling layer. Confirms that "medication management" in the automation market = supply chain + dispensing + accountability, not the clinical chart.

### MEDITECH Expanse Pharmacy — Evidence layer: A

Positioning: "Evolve with the new era of pharmacy. Pharmacists today are responsible for so much more than just the verification and dispensing of medications. They're tasked with everything from **medication reconciliation at admission and discharge**, to bedside rounds and provider consults."

- **Pharmacist work surfaces**: "The patient chart, Rx Audit, and Intervention documentation are all just a click away so pharmacists can easily access and review medication lists when completing patient rounds." "From compounding and administering IV drugs to checking interaction history, pharmacists can quickly access important information about ordered medications."
- **Order work**: "greater control over medication orders, order sets, and dose calculations… optimizing the order/edit process."
- **Safety/precision**: integrated pharmacogenomic conflict checking and clinical decision support; Surveillance + Patient Registries "automatically identify patients in need of intervention regardless if they're inpatient or outpatient."
- **Integration**: "bidirectional integration with IV Workflow Management Systems and IV Smart Pumps streamlines accurate patient information and reduces calls between pharmacists, technicians, and nursing staff." Real-time shared chart across the care team.
- **Analytics**: customizable pharmacy dashboards (Business and Clinical Analytics).

Observation: the EHR-embedded pole centers the **pharmacist's clinical workflow** over medication orders — verification, dose calculation, IV compounding, interaction checking, med reconciliation, interventions — with the chart shared in real time and outward integration to IV workflow systems and smart pumps. Inventory/automation machinery is not foregrounded on this page (it lives in the surrounding Expanse suite and integrations). This is the same medication-use process seen from the clinical end rather than the supply end.

### Medisafe — Evidence layer: A (consumer pole + pharma engagement)

Positioning (current): "The patient engagement engine for pharma portfolios… Behavior-driven digital engagement that helps pharmaceutical brands activate patients, improve outcomes, and scale support across therapies and markets." Platform = Maestro (enterprise orchestration: journey builder, campaigns, analytics), **Digital Drug Companion** (branded therapy-specific patient experiences: "Personalized medication reminders and scheduling… Caregiver coordination and family support tools… Progress tracking"), JITI predictive engine ("Predictive non-adherence risk scoring… just-in-time intervention triggers").

- **For Patients**: "Simple, intuitive medication management across all prescriptions; personalized reminders that adapt to individual routines; educational content tailored to each therapy and condition; caregiver tools for family members."
- **For Providers**: "Monitor patient adherence between visits with real-time behavioral signals; receive alerts when patients are at risk of discontinuation."
- Scale claims: 13M+ patients supported, 25+ pharma partners, 150+ countries (vendor claims).

Observation: the consumer pole's structure = the **individual's personal medication regimen** (list + dose schedule), reminders, intake logging, adherence analytics, caregiver sharing — monetized today primarily toward pharma engagement programs. No stock estate, no organizational medication process, no dispensing/administration accountability. Structurally a personal-health application.

### MyTherapy (smartpatient) — Evidence layer: A (consumer pole, pure)

Positioning: "Reliable medication reminders for you… MyTherapy is your personal, digital health companion. Reliable medication reminders and consistent documentation of your intakes."

- "Reliable reminders for your tablets, pills and other medications as well as measurements, doctor's appointments or symptom checks."
- "MyTherapy automatically documents every intake, whether taken or skipped… add notes to each instance… your personal treatment overview… anytime, anywhere."
- "Always remain in control over your medication supply… remind you well in advance when it's time for a refill or to get a new prescription."
- Symptom/measurements/mood tracking; "generate a health report and medication plan for your doctor… share your medication plan, intake diary and more with your doctor at the push of a button" (one-time code).
- Business model: free for users; "we cooperate with partners such as pharmaceutical companies and healthcare institutes to whom medication adherence information is vital."

Observation: the pure consumer form: personal med list → dose reminders → taken/skipped logging → refill reminders → shareable report. Confirms the consumer pole's structure is personal-regimen management, sharing nothing of the organizational stock/verification/accountability machinery.

## Cross-product Comparison

| Dimension | Omnicell | Swisslog | MEDITECH Expanse Pharmacy | Medisafe | MyTherapy |
|---|---|---|---|---|---|
| Primary user | pharmacy + nursing teams | pharmacy/logistics staff | pharmacists (with care-team chart access) | patients/caregivers (+ pharma programs) | patients/caregivers |
| Medication stock estate | explicit, central (dose-level visibility, expiry, cabinets, robots, carousel) | explicit, central (automation + transport + refrigerators) | not foregrounded (lives in suite/integrations) | none | none |
| Patient regimen as demand | implicit (dispensing for patients; reconciliation named) | implicit (supply for patients) | explicit (orders, verification, dose calculation, med rec) | explicit (personal med list + schedule) | explicit (personal med list + schedule) |
| Event record & accountability | explicit (dispensing/administration events, controlled substances, diversion surveillance, audit trails) | explicit (automated movement under software control) | explicit (Rx Audit, intervention documentation, shared chart) | personal intake log only | personal intake log only |
| Verification machinery | guided cabinet workflows, controlled-substance manager | automation-enforced handling | pharmacist verification, interaction/PGx checking, dose calculation | interaction info (consumer-grade) | none foregrounded |
| Integration with EHR | "interoperability with EHRs" (one source of truth) | software layer over automation | native (is the EHR) | none claimed on fetched pages | doctor report sharing only |
| Analytics | inventory optimization, diversion detection, benchmarking | software + analytics over the chain | pharmacy dashboards, surveillance/registries | adherence analytics for pharma | personal history |
| Care settings | inpatient (IV room, central pharmacy, points of care) + outpatient (specialty, retail, adherence) | central pharmacy, transport, outpatient, correctional | hospital pharmacy department | consumer + pharma programs | consumer |
| Packaging | EHR-integrated automation platform | automation + transport + software | EHR-embedded module | consumer app + pharma SaaS | consumer app |

**Reading**: the three provider-side products describe one continuous object — the care organization's medication-use process — from two ends: the supply end (Omnicell, Swisslog: stock, automation, transport, accountability) and the clinical end (MEDITECH: orders, verification, preparation, reconciliation). The two consumer products describe a different object entirely — the individual's personal regimen routine — with no stock estate, no organizational process, and no professional accountability. Same phrase, different Types.

## Canonical Abstraction

### L0 — Defining Invariant (provider-side Type)

The care organization's **medication-use system of record**. Three jointly-held structures:

1. **The medication stock estate of record** — the organization's medications held as counted, located, expiry-tracked stock across its locations (central pharmacy, automated cabinets, refrigerators, ward stock), consumed by dispensing/administration and restored by recorded receipt. Remove → generic inventory management.
2. **The patient's active medication regimen as the executable demand** — medication orders for identified patients (arriving from prescribers/CPOE/e-prescribing), clinically verified, that drive preparation, dispensing, and administration, and are reconciled at care transitions. Remove → stock logistics with no patient semantics.
3. **The verified medication event record with accountability** — each dispensing, administration, transfer, and waste event documented against regimen and stock with who/what/when attribution; controlled substances under heightened accountability (documented handling, investigation-ready audit trails). Remove → logistics with no clinical/legal record.

**Binding**: one care organization's own medication-use process across its points of care, with pharmacy and nursing on the same medication spine. Remove the organizational binding → retail dispensing (Pharmacy Management System territory) or a personal regimen (consumer app territory).

**Jointly-held load-bearing**:
- 1 alone = inventory system
- 2 alone = order management / e-prescribing territory
- 3 without 1+2 = free-floating charting
- 1+2 without 3 = supply logistics with no administration record
- 1+3 without 2 = stock accountability with no regimen driver
- 2+3 without 1 = eMAR/charting with no supply estate

**Historical / market-sample check (§24)**: the paper-era hospital satisfies all three legs — pharmacy stockroom + unit-dose cart + narcotic ledger (stock estate); paper medication orders verified and compounded by pharmacists (regimen as demand); paper MAR + narcotic sign-out ledger (event record with accountability). UK-style ward stock + CD cupboard registers fit equally. Automation, barcode verification, cloud, and AI are era machinery, not definitional. ✓

### L1 — Common Mature Structure

- automated dispensing cabinets at points of care (guided selection, countback/restock support)
- pharmacist verification/clinical review of orders before dispensing (interaction, allergy, dose checking)
- barcode/identity verification at dispensing and administration
- IV compounding / IV workflow documentation; smart-pump integration
- inventory analytics: optimization, shortage visibility, expiry management, benchmarking
- diversion surveillance beyond basic controlled-substance logs (analytics + case management)
- EHR integration (orders in, administration documentation back, one shared patient picture)
- adherence packaging (unit-dose, multi-dose blister/pouch, med carts)
- dashboards/reporting for pharmacy operations

### L2 — Variant / Optional Structure

- care-setting scope: acute inpatient / outpatient retail / specialty / long-term care / correctional
- packaging: EHR-embedded module vs automation-vendor platform vs hybrid estate
- robotics/transport automation depth (robots, carousels, pneumatic transport)
- outpatient adherence programs (patient outreach, persistence analytics — the pharma-facing pole)
- regional regime machinery (controlled-substance regulations, unit-dose norms, reimbursement)
- delivery: cloud platform vs on-premises server
- consumer-pole products (personal regimen apps) — a different Type sharing the phrase, not a variant of this one

### L3 — Vendor-specific Structure (Research Notes only)

OmniSphere, CarePlus, Titan XT, XR2, Central Pharmacy Manager, MedVision, XT Controlled Substance Manager, Enterprise Medication Manager, Guided Packing, MTS/AccuFlex/E3 (Omnicell); Tenutō, TranspoNet-class transport (Swisslog); Rx Audit, Expanse Care Compass, Surveillance, BCA dashboards (MEDITECH); Maestro, Digital Drug Companion, JITI (Medisafe). Vendor metrics (54% nursing time saved; 99% repackaging savings; 13M+ patients; adherence-lift percentages) are claims recorded here only.

## Vendor-specific Findings

- Omnicell's "Medication Adherence" pole is **adherence packaging** (blister/pouch automation for retail/LTC/correctional pharmacies) — supply-side, not a consumer app; distinct from Medisafe's adherence (consumer behavior) despite the shared word.
- Medisafe's current positioning has pivoted to pharma patient-engagement (Maestro/JITI); the consumer medication app remains its base. Its provider-facing "For Providers" surface (adherence signals between visits) is engagement analytics, not medication-use operations.
- Swisslog foregrounds **physical transport automation** (hospital logistics) as part of medication management — a framing Omnicell expresses through robotics but does not lead with.
- MEDITECH leads with **pharmacogenomic CDS** as a differentiator — an L1/L2 capability, not definitional.

## Rejected Findings

- "Medication management = pharmacy inventory automation" — rejected as the definition: the EHR-embedded pole carries the clinical half (verification, med rec, interventions) with little automation machinery; the supply estate alone is just inventory.
- "Medication management = the EHR's medication record" — rejected: the record is the EHR's; this Type owns the **process** (stock → verify → prepare → dispense → administer → account), which the EHR does not.
- "Medication management = consumer pill reminders" — rejected as a different Type: different users (patient vs pharmacy/nursing staff), different objects (personal regimen vs organizational stock estate), different workflows (self-administration logging vs verified dispensing/administration). Documented as a boundary finding, not a variant.
- "Barcode verification / five-rights checking is definitional" — rejected: the paper-era form (visual checks + signatures) satisfies the Type; barcode machinery is the dominant modern implementation of the verification seam, not the invariant.
- "Diversion analytics is definitional" — rejected: controlled-substance accountability is the old, definitional layer (narcotic ledgers); analytics over it is L1.

## Boundary Findings

| Neighboring Type | Seam | Remove-what test |
|---|---|---|
| Electronic Health Record / EHR | EHR holds the patient's medication **record** (med list, orders) inside the chart; MMP owns the medication-use **process** (stock, verification, preparation, dispensing, administration, accountability). EHR-embedded pharmacy modules instantiate the MMP function inside the EHR. | Take away the stock estate and event accountability, leaving the chart → EHR. Take away the chart, keeping the process → MMP. |
| Pharmacy Management System | PMS = the dispensing pharmacy's business system of record (prescription as unit of work, fill pipeline, patient medication profile, retail operations). MMP = the care organization's medication-use process across settings. In hospitals the PMS function is typically absorbed into the MMP/EHR pharmacy module; in retail they are distinct businesses. | Confirms the PMS pass's grading from this side. Remove the multi-setting process, keep the dispensing business → PMS. |
| Electronic Prescribing | e-prescribing = prescriber-side composition + transmission to an external dispensing pharmacy over a network. MMP = the receiving organization's internal execution (stock → verify → dispense → administer). | Confirms "frequent coexistence, distinct centers" from this side; discharges the e-prescribing pass's cross-check request. Remove the internal execution, keep transmission → e-prescribing. |
| CPOE / Clinical Order Management | CPOE records the intention (the order); MMP executes it (verification, preparation, dispensing, administration) and records execution. | Remove execution, keep ordering → CPOE. |
| Nursing Information System | NIS = nurse-facing care-delivery system; medication administration is one documented activity within nursing care. MMP = medication-centered spine across roles; the MAR is shared territory (nursing documents care; MMP owns medication verification/accountability machinery). | Remove the medication spine (stock, controlled-substance accountability), keep nursing care documentation → NIS. |
| Clinical Decision Support System | Medication safety checking (interaction/allergy/dosing/PGx) is CDS capability embedded in the MMP workflow, not the MMP center. | Remove the process, keep the advice engine → CDSS. |
| Inventory Management System (§10) | Generic stock control vs a medication estate bound to clinical consumption (regimen-driven dispensing, administration decrements, controlled-substance accountability, expiry as a safety property). | Remove clinical consumption semantics → generic inventory. |
| Long-term Care EHR | LTC EHR holds the MAR inside the resident's standing record; MMP's LTC realization is the medication process serving it (pouch packaging, med carts, pharmacy-generated MARs). | Remove the medication process, keep the resident record → LTC EHR. |
| Consumer medication reminder / adherence app (Medisafe, MyTherapy) | Different Type: personal regimen + reminders + self-logged intakes; no stock estate, no organizational process, no professional verification/accountability. | Remove the organization and its stock/verification/accountability → consumer app. Flagged for taxonomy (see below). |
| Home Infusion Management | Home infusion = the infusion-therapy service line (patient, pump, nursing visits, supplies); MMP's IV room/compounding is the facility-side preparation step of the medication process. | Remove the facility medication process, keep the home therapy program → Home Infusion Management. |

## Uncertainties

- **BD Pyxis unreachable** (403 ×2): the second major automation vendor is absent from the direct sample. The automation pole rests on Omnicell + Swisslog; BD's Pyxis MedStation class is corroborated only by market familiarity, not fetched evidence. Assertions about the automation pole are therefore anchored to two products, not three.
- **Epic Willow unreachable** (403): the largest EHR pharmacy module is not directly evidenced; the EHR-embedded pole rests on MEDITECH alone. The claim "EHR pharmacy modules instantiate this Type inside the EHR" is single-product direct evidence + prior-pass context (EHR pass lists medication management as an EHR L1 capability), kept at moderate strength.
- **No help-center documentation reached**: all evidence is Tier-2 product/solution pages. Workflow details below the page level (exact cabinet interaction sequences, exact verification-queue mechanics, exact reconciliation screens) are inferred at the structure level only and not asserted as precise facts.
- **Inventory depth in EHR pharmacy modules**: MEDITECH's page does not foreground stock management; whether every EHR-embedded realization carries the full stock estate could not be confirmed from fetched evidence. The L0 keeps the stock estate as definitional based on the automation pole + the hospital-pharmacy function generally; if a pure-clinical EHR module without any stock semantics existed, it would look like pharmacist order-management (CPOE-adjacent) rather than a full MMP — noted as a residual edge case.
- **Consumer-pole taxonomy disposition**: whether the directory should eventually carry a separate leaf for consumer medication reminder/adherence apps (or treat them under a consumer-health family) is a taxonomy decision above this pass; flagged in STATUS.md.

## Final Synthesis

The market uses "medication management" for two different things. The consumer pole (Medisafe, MyTherapy) means the individual's personal medication routine — a personal-health application. The provider pole — the one this §22 leaf names — means the care organization's medication-use process, and it is a coherent, independently sold Application Type with two dominant packagings: the **automation-vendor platform** (Omnicell, Swisslog: the stock estate, dispensing automation, transport, controlled-substance accountability, analytics, EHR interoperability) and the **EHR-embedded pharmacy module** (MEDITECH Expanse Pharmacy: verification, preparation, reconciliation, interventions over the shared chart). Both packagings describe the same three-part structure: a counted medication stock estate, the patient's active regimen as the executable demand, and a verified event record with accountability — bound to one organization's medication-use process across its points of care, serving pharmacy and nursing on one spine.

The Type stands independently of the EHR (answering the EHR pass's joint-review flag): the EHR holds the medication record; this Type runs the medication process. The seams vs PMS (dispensing business vs organization-wide process), e-prescribing (external transmission vs internal execution), CPOE (intention vs execution), and NIS (nursing care record vs medication spine) are all confirmed from this side. The paper-era hospital (stockroom + cart + paper MAR + narcotic ledger) satisfies the definition, so automation/barcode/cloud/AI are documented as mature machinery, not invariants.
