# Research Notes — IRT / RTSM (Interactive Response Technology / Randomization and Trial Supply Management)

Research date: 2026-09-10

## Research Goal

Understand what an IRT/RTSM system actually is and how it works: what the system holds, what happens at the moment a trial subject is enrolled, how trial drug supply is managed around those assignments, how blinding is preserved (and broken under control), and where the boundary sits against EDC, CTMS, clinical supply-chain services, and pure randomization tools.

## Initial Boundary (pre-research hypothesis)

- IRT (Interactive Response Technology; historically IVRS — Interactive Voice Response System) and RTSM (Randomization and Trial Supply Management) are two industry names for the same product category.
- Hypothesized core: (a) randomize/allocate subjects to treatment per the protocol design, (b) manage investigational-product supply (depots, sites, kits, shipments) tied to those assignments, (c) preserve blinding with controlled emergency unblinding.
- Nearest neighbors: EDC (data capture), CTMS (trial operations), clinical trial supply chain services (physical logistics/forecasting), pharmacy management (patient-care dispensing), pure randomization services (academic).
- Unknowns entering research: Is supply management definitional or merely common (trials without IP exist)? Is blinding definitional (open-label trials use RTSM too)? What exactly is the "interactive" transaction?

## Research Questions

1. What is "randomization" as a system capability — what is configured, when triggered, what returned?
2. What is "trial supply management" — what objects (kit, lot, depot, site inventory, shipment), what flows?
3. How does blinding work — role-based visibility, code break, emergency unblinding?
4. What is the enrollment-moment transaction (the defining loop)?
5. What study-lifecycle machinery exists — build/UAT, amendments, mid-study change?
6. What interfaces and users — site staff, sponsor/supply managers, depots, patients (DtP)?
7. How do integrations with EDC/CTMS/temperature/depot systems work?
8. Boundary: what removes/keeps this Type distinct; is supply management or blinding part of the minimal core?

## Representative Products

Selected for market representation, different product philosophies, and different customer tiers:

| Product | Vendor | Philosophy / tier |
|---|---|---|
| IRT / RTSM | Suvoda | Standalone IRT specialist; "command and control center" positioning; complexity-first (oncology, CNS, rare disease); rich configurability by permissioned users mid-study |
| Prancer RTSM® | 4G Clinical | Productized RTSM family (Prancer RTSM / Prancer Lite / Prancer Inventory Platform) + separate forecasting product (4C Supply®); "RTSM not IRT" naming philosophy |
| IXRS®3 | Almac Clinical Technologies | Legacy market leader; IVRS/IWRS/IXRS heritage; expert-services + biostatistics list generation; extensive educational content |
| Medidata RTSM | Medidata (Dassault) | Platform-embedded pole: unified with Rave EDC on one platform; "Edit Live Design" mid-study changes; eSA electronic supply accountability |
| IQVIA IRT | IQVIA | CRO-suite-embedded; component-library build approach; Patient Suite integration; 24×7 multilingual support |

Boundary probes (not counted in the core sample): pure randomization SOPs/services (USF, UCL JRO, MCW cancer center SOPs); independent academic literature on RTSM supply methods (PMC).

## Sources

Tier 1 (operational docs) largely unavailable — all sampled systems keep user manuals behind client logins (validated GxP systems). Evidence base is Tier 2 (official product + educational pages) + Tier 3 (independent academic, sponsor SOPs):

1. Suvoda — IRT product page: https://www.suvoda.com/products/irt (fetched 2026-09-10, full functionality lists, mid-study change posture, reporting, DtP module)
2. Suvoda — RTSM (IRT) page: https://www.suvoda.com/rtsm-irt-clinical-trial (search-verified; agentic AI study build, same functionality lists)
3. 4G Clinical — home: https://www.4gclinical.com/ ; technology: https://www.4gclinical.com/technology (search-verified; Prancer RTSM/Lite/Inventory Platform, 4C Supply, GS1)
4. 4G Clinical — white paper "IRT. IVRS. IXRS. IWRS. RTSM.": https://www.4gclinical.com/hubfs/IRT_IVRS_IxRS_IWRS_RTSM_WP%20%282%29.pdf (search excerpt; history of IVRS→IRT→RTSM naming and function)
5. Almac — "What is IRT and How Does it Impact Clinical Trials?": https://www.almacgroup.com/clinical-technologies/blogs/what-is-irt-and-how-does-it-impact-clinical-trials (fetched; full mechanism: envelope predecessor, enrollment/randomization/kit assignment, depot→site supply loop, chain of custody, reporting)
6. Almac — "What is Randomisation and Trial Supply Management (RTSM)?": https://www.almacgroup.com/clinical-technologies/blogs/what-is-randomisation-and-trial-supply-management-rtsm (search excerpt; R vs TSM naming, list generation/import, UAT, go-live)
7. Almac — supply strategy white paper: https://www.almacgroup.com/knowledge/wp-content/uploads/sites/10/2022/05/41098-ALMAC-CT-Supply-Strategy-White-Paper-WEB-AM6720.pdf (search excerpt; kit-type changes at visits, expiry, weight-based dosing, dose construction from kit combinations, country restrictions, visit projection window)
8. Medidata — "What is RTSM? Randomization & Trial Supply Management 101": https://www.medidata.com/en/life-science-resources/medidata-blog/what-is-rtsm (fetched; core vs advanced functionality, pre-RTSM history, code break section, supply evolution)
9. Medidata — RTSM product page: https://www.medidata.com/en/data-experience/rtsm/ (fetched; Edit Live Design, eSA, Rave unification, DtP with patient receipt confirmation, pooling, multi-dose vial)
10. IQVIA — IRT fact sheet: https://www.iqvia.com/-/media/iqvia/pdfs/library/fact-sheets/2026/iqvia-interactive-response-technology---fact-sheet---final.pdf (search excerpt; consent→randomization exchange, DtP dispensation, temperature excursion, mobile IP accountability, support model)
11. PMC — "Blinding properties of methods for supplying drug kits to investigational sites": https://pmc.ncbi.nlm.nih.gov/articles/PMC5935824 (independent academic; TR/PR supply methods, partial-unblinding risk, site parameters secret, kit interchangeability premise)
12. USF Health SOP "Randomization and Blinding" (neutral definition: "IVRS: Phone or web-based tool used by sites to register the enrollment of patients and to allocate patients to a particular treatment arm") — search excerpt
13. UCL Joint Research Office SOP "Randomisation, Blinding and Code Break" (code break log contents, 24-hour cover, IxRS term, kit-code overages) — search excerpt
14. Octalsoft — IRT page (secondary vendor; corroborates emergency-unblinding mechanics) — search excerpt

**Source-access limitation:** no product's operational user manual is public; vendor metrics (study counts, UAT defect counts, component counts, "years as IRT partner") are marketing claims and were excluded from the final document. Precise operational parameters (resupply thresholds, buffer quantities, check cadences, list lengths, window sizes) are not asserted anywhere. The PMC paper's "e.g., daily" check cadence is an example from cited literature, not asserted as an industry default.

## Product Observations

### Suvoda IRT (evidence layer A — official product page, fetched)

- Self-definition: "Our advanced patient randomization and trial supply management system. Your clinical trial command and control center." Also markets the same system as "Suvoda RTSM (IRT)" — uses both names for one product.
- Functionality grouped in three: **Trial Logistics** (roles/permissions/blinding management; study and site administration; cohort/stage/phase management; dynamic cohort and dose management; additional and dynamic visit schedule); **Patient Logistics** (subject management; adaptive replacement and randomization; cross-over and re-treatment; open-label extension; dose calculation; subject roll-over; dose modification and interruption); **Drug Logistics** (dispensing management; supply management; accountability/reconciliation/returns-destruction; temperature excursion; controlled substances; variable sourcing; central pharmacy; DtP shipping; supply strategy management).
- Mid-study: "Commonly-needed additions, modifications, and corrections to study, site, drug management, and administrative functions can be made by permissioned users within our system after go-live... reduces change-orders"; modular architecture for larger updates.
- Reporting: pre-set and ad-hoc reports on "subjects, sites, drugs, and depots".
- Users: "from dedicated pros to more occasional site-users, and even home caregivers" — the site-occasional-user design point is explicit.
- Build: "easy-to-assemble building blocks" assembled by services teams.
- Featured modules: temperature excursion (integration with temperature data loggers, monitoring software, depot distribution), direct-to-patient shipping ("supply patients anywhere — at home or in the clinic — while protecting privacy and blinding").

### 4G Clinical Prancer RTSM (layer A — official pages, search-verified)

- "Prancer RTSM® unifies randomization, supply, and forecasting for live study execution, while 4C Supply® supports broader forecasting, scenario modeling, and long-range planning."
- Product family tiers: Prancer RTSM (complex global trials: "complex randomization, adaptive and cohort-based trials, titration strategies, supply oversight, integrated forecasting, operational reporting"); **Prancer Lite** ("streamlined deployment... without the demands of a large, highly complex global build"); **Prancer Inventory Platform** ("dedicated inventory visibility and resupply management... without requiring full randomization deployment") — an inventory-without-randomization pole in the same family.
- 4C Supply®: portfolio-level supply modeling across manufacturing/distribution/long-range planning; integrates with Prancer RTSM, third-party IRTs, and enterprise data.
- GS1-aligned IRT workflows for IP traceability; sustainability framing (reduce waste via configurable resupply).
- White paper (history): 1980s patient-numbered kit labels shipped in full blocks → staggering waste; 1990s first clinical IVR systems "developed in order to randomize patients over the phone, and later, to dispense drug and resupply sites as well. For the first time, all patient kits could be interchangeable for any other equivalent kit." IVRS→IWRS→IxRS→IRT umbrella→RTSM "refers more to the function of the actual system versus the modality of delivery." "Historically IRT was used primarily for randomization and getting drug to the site. Over the years, it became apparent that supply management was just as critical as randomization and the combined action of them together elevates the function of this system. They are synergistic and need to co-exist."

### Almac IXRS®3 (layer A — official educational blog fetched + platform pages)

- "An IRT system is known by many other names such as IVRS, IWRS, IXRS, RTSM but regardless of its name, the system delivers a wide range of features for managing patient enrollment and drug supply activities throughout the clinical trial lifecycle."
- Randomization: "The system allows for complex protocol enrollment and randomisation design and strictly controls sensitive information such as treatment arm and medication treatment assignments to maintain study blinding." Methodologies: "central, subject stratified and/or site stratified randomisation schemes"; at the randomisation visit the IRT assigns the treatment arm per the programmed methodology and "will typically also assign the subject the appropriate medication kit which matches the randomised treatment arm." Minimization as an alternative algorithmic approach; randomisation list generation by vendor biostatisticians or sponsor; list import by vendor data managers; build → test → UAT → QA certification → go-live.
- Pre-IRT method: each list entry sealed in an envelope with sequence number; envelope blocks + matching kits sent to sites; envelope chosen in sequence, matching kit dispensed; slow, simple designs only, human error.
- Supply mechanics: "Individual kits stored at the depot and site are not labeled for particular patients. Instead, kits are assigned to patients when they arrive for their visit. So, shipments to sites only contain enough product to meet patient demand over a certain period, and resupplies are triggered when inventories hit a designated level... The IRT is able to tailor the supply provided to each site since it knows what patients are at each site, their treatment arms, and the visit schedule."
- The closed loop: "As soon as the Sponsor activates a site in the IRT, the system triggers a request to the depot for an initial supply of medication. The depot fills the order and sends the shipment to the site. When an order arrives at the site, staff confirm its receipt in the IRT, and the drugs are made available for assignment to patients. As patients visit the site, they are assigned a medication kit from the site's inventory. All the while, an algorithm within the system is monitoring the inventory at each site. If the inventory reaches a pre-determined low level, the supply engine will generate a request for the depot to send a resupply."
- Chain of custody: "from the time supplies are packaged and released at the depot through to medication assignment as well as drug returns and destruction." Expiry tracking with alerts; global view of supplies at main depot, secondary depot, site level.
- Emergency unblinding: "The IRT commonly includes emergency unblinding functionality. This can be setup so that Principal Investigators are able to unblind patients at their sites in case of an emergency. When an emergency code break by the site occurs, the system immediately notifies the study team. Often times, that patient who was unblinded by the site is then automatically discontinued from the study, preventing further drug assignments by the IRT. The IRT can also provide access to the Medical Safety team who can unblind any patient at any site without impacting their ongoing participation in the study."
- Platform context: IXRS®3 is the IRT platform; companion products (Almac Trial Coordinator, eCOA, eConsent, Visit Management); IRT "boosters" (ART drug accountability & reconciliation tracking; archival investigator access; drug pooling protocols; DCT support package); Almac One™ bundles IRT with clinical supply chain services.

### Medidata RTSM (layer A — official blog + product page, fetched)

- "An RTSM system efficiently and accurately controls patient randomization; automates investigational product (IP) supply and resupply to depots, sites, and direct-to-patient; and handles drug dosing and dispensation." Core named as "randomization, unblinding, and supply management."
- Advanced capabilities list: variety of randomization schemes; re-randomization; in-built randomization list generator; forecasting; assignment in pre-specified ratios across multiple stratification/balance factors (e.g., sex, age groups, disease severity); cohort enrollment/management (sequential and parallel); patient replacement; complex dosing calculations; supply accountability; DtP with choice of dispensing from site stock or directly from depot; automatic configurable resupply; real-time recruitment/supply monitoring; exports gated by user's blinding status (historical supply/shipments, dose assignments, patient status).
- Pre-RTSM history: kits labeled with patient's randomization ID for full study duration → waste; early RTSM kept near-term site stock and auto-requested IP; "Blinded, uniquely-identified site inventory no longer needed to be pre-allocated to patients because RTSM could signal the study coordinator or pharmacist which kit to dispense at each visit."
- Modern supply: multiple supply plans per site profile; alerts for low depot supply, shipments not received in reasonable time, upcoming expiry; projection of future inventory needs; pooled supplies across studies at depot and site level; serialized (numbered) and bulk (unnumbered) supply tracking; "Supply accountability, returns, and destruction functionality now enable RTSM to provide oversight for the full life-cycle of clinical supplies."
- Blinding: "RTSM's automated code break functionality provides greater security and a superior audit trail as compared to other methods where a lesser level of control is present (code break envelopes, 24-hour manned telephone line, etc.). The system is programmed for the investigator, a designated study leader, and/or global drug safety department user to be able to unblind the patient and to verify dosing accuracy."
- Product page: "connects randomization, patient assignment, and drug logistics in one unified environment"; Edit Live Design = protocol updates after go-live with no downtime (adding new cohorts); RTSM Analytics dashboards across randomization/inventory/shipments; unified electronic supply accountability (eSA) with Rave "eliminates paper logs"; predictive supply logic, depot integration services, DtP (shipments triggered at site, visit, or patient level; patients confirm receipt via myMedidata); multi-dose vial tracking; drug pooling.
- Platform posture: "fully unified with Rave... not a separate integration but part of the same system. This unification eliminates the need for double data entry and reconciliation between randomization and EDC systems."

### IQVIA IRT (layer A — official fact sheet, search excerpt)

- "IQVIA's Randomization and Trial Supply Management (RTSM) solution to maintain trial integrity and ensure sites are always ready for the next patient visit."
- "Real-time data exchange from informed consent to randomization and data collection"; turnkey integrations with clinical technologies; part of IQVIA Patient Suite (SSO, workflow automation).
- DtP "dispensation and confirmation options support hybrid studies"; drug supply optimization ("reduce IP waste, shipping expenses, and site burden"); mobile IP ("drug accountability through intelligent data collection on mobile devices"); temperature excursion management ("monitors kit-level temperature to verify product viability"); material forecasting dashboard.
- Build/service model: "IRT technical staff configures the IRT solution based on protocol requirements, and the validation team executes study level testing"; dedicated project manager handles amendment requests; "safeguard against unblinding... through expert RTSM configuration and analysis"; white-glove multilingual 24×7 support (live chat or toll-free call) — the call-center channel heritage.

### Independent / neutral sources (layers B/C)

- USF SOP: "Interactive Voice Response System (IVRS): Phone or web-based tool used by sites to register the enrollment of patients and to allocate patients to a particular treatment arm." Confirms the site-side transaction pattern from the sponsor-process side.
- UCL JRO SOP: IxRS term (interactive voice/web response system); kit codes may need sequential setup with overage quantities; 24-hour cover for code breaks; code break log contents (participant trial ID, reason, date, requester, breaker, sponsor informed); test the emergency number; unblinding user accounts for investigator/delegate (emergency) and pharmacovigilance (safety reporting).
- PMC (academic): drug kits "enable investigators to administer study drug to subjects in a blinded manner without the assistance of an unblinded pharmacist"; TR (trigger-resupply: trigger level + resupply level per kit type per site) and PR (prediction for return visits) methods "implemented in many RTSM systems"; resupply checks "frequently, e.g. daily"; buffer/prediction stocks not differentiated at dispensing; partial unblinding possible from inventory patterns; "a site's parameters should be kept secret from the site"; efficiency objectives (minimize total kits, shipment frequency, initial kits, site inventory).
- Octalsoft (secondary vendor): emergency unblinding configured so PIs can unblind at their sites; system alerts research team on code breach; site-unblinded patient often auto-removed preventing further drug assignment; medical safety team can unblind without affecting participation.

## Cross-product Comparison

| Aspect | Suvoda | 4G Clinical | Almac | Medidata | IQVIA |
|---|---|---|---|---|---|
| Names used for the category | IRT and RTSM for one product | RTSM (deliberately) | IRT (IXRS®3) and RTSM | RTSM (also IRT) | IRT and RTSM |
| Randomization | adaptive replacement and randomization; cohort/stage/phase; dynamic dose | complex randomization; adaptive/cohort designs (Prancer) | programmed methodology (central/stratified schemes; minimization possible); list import | simple→highly complex strategies; stratification/balance factors; schemes; re-randomization; in-built list generator | configuration-based; trial integrity framing |
| Enrollment transaction | subject management → randomization | patient allocation | at randomisation visit: arm + "typically also" medication kit assigned | patient assignment | site registers → allocation |
| Blinding machinery | roles/permissions/blinding management; DtP "protecting privacy and blinding" | blinded execution; GS1 traceability | strictly controls treatment-arm/medication-assignment info; emergency unblinding (PI + medical safety) | automated code break; blinding-gated exports | safeguard against unblinding |
| Supply chain | dispensing; supply; accountability/reconciliation/returns/destruction; temperature; controlled substances; central pharmacy; DtP; supply strategy | supply + forecasting unified; configurable resupply; inventory-only product pole | depot/site inventory; shipments + receipt confirmation; resupply triggers; expiry alerts; chain of custody to destruction | automated IP supply/resupply depots/sites/DtP; multi-dose vial; pooling; eSA paper-log elimination | supply optimization; forecasting dashboard; temperature excursion; mobile accountability |
| Mid-study change | permissioned users after go-live; modular adds | "change without study disruption" | amendment processes in white papers | Edit Live Design: no downtime, no change orders | amendment requests via project manager |
| Build model | building blocks + services team | configuration flexibility aligned to complexity | vendor biostatistics + data managers + UAT + QA certification | professional services; unified platform build | vendor technical staff + validation team; component library |
| Reporting | pre-set/ad-hoc: subjects, sites, drugs, depots | reporting + supply data surfaces | real-time data, metrics, alerts | RTSM Analytics; blinding-gated exports | material forecasting dashboard; mobile IP |
| Platform posture | one clinical-trial platform (8 products incl. eCOA/eConsent) | single RTSM framework + separate forecasting product | clinical-technologies suite + supply-chain services (Almac One) | unified with Rave EDC — no separate integration | part of Patient Suite |
| Channel heritage | web (modality-neutral) | web | IVRS/IWRS/IXRS heritage → IXRS³ | IRT-partner heritage | 24×7 phone/chat support heritage |

**Stable across all five (B-layer):** randomization of enrolled subjects per a protocol-held design; kit assignment coupled to the allocation; blinded site inventory that is not patient-pre-labeled; depot→site shipments with receipt confirmation; automated resupply logic; accountability through returns/destruction; blinding governance with controlled emergency unblinding; mid-study change machinery; reporting/oversight for sponsor and supply teams; EDC-adjacent integration; specialist build/service teams.

## Canonical Model

### Level 0 — Defining Invariant (three jointly-held structures)

1. **The study's allocation design held by the system.** The trial's randomization scheme — list/schedule or algorithm, with stratification/balance factors, cohorts, and stages — is configured into the system per study before go-live and versioned across amendments. The system, not the site, holds the mapping from allocation sequence to treatment. Remove → a statistics tool or a data-entry form; there is nothing for the system to apply.
2. **The enrollment-moment interactive assignment.** A site-side transaction — registering a subject's enrollment/randomization request — prompts the system to compute and return that subject's treatment allocation in real time, recorded persistently on the subject's record, typically coupled with the kit to dispense. This is the "interactive response" in the name. Remove → batch list generation; not a trial-conduct system.
3. **The trial-supply chain bound to assignments.** The system tracks the trial's investigational product as identified (blinded) units — kits — across depots and site inventories; moves them through managed shipments with receipt confirmation; assigns/dispenses kits to subjects against their assignments; and keeps accountability through returns and destruction. Remove → either a pure randomization tool (1+2 without 3) or warehouse software (3 alone).

Jointly-held load-bearing analysis:

- 1 alone = randomization list generator / statistical service
- 2 without 1 = incoherent (no design to assign from)
- 3 without 1+2 = clinical depot / inventory software
- 1+2 without 3 = pure randomization system (real but thinner sibling — the academic/sequential-envelope lineage)
- 1+3 without 2 = the pre-IRT envelope/kit-block method (the ancestor, not the Type)
- 2+3 without 1 = impossible (assignment requires the held design)

### Level 1 — Common Mature Structure

- Blinding governance as the characteristic machinery of the dominant case: role-based visibility of the treatment mapping, blinded site inventory, automated emergency code break with audit trail and study-team notification, blinding-gated data exports. (Present in all sampled products; relaxed in open-label deployments — see L2.)
- Automated resupply logic: trigger levels and/or prediction from visit schedules; initial supply on site activation; receipt confirmation; expiry management and alerts.
- Visit-schedule-driven dispensing: kit-type changes at visits, dose titration/calculation/modification/interruption, multi-dispensation trials.
- Cohort/stage/phase machinery; adaptive patterns (replacement, re-randomization, crossover, roll-over, open-label extension).
- Mid-study change: amendments applied to a live study (vendor-specific mechanisms differ — change orders vs permissioned self-service vs in-platform live editing).
- Reporting/analytics: enrollment, inventory, shipments, expiry, depots; blinding-gated exports; alerts.
- Direct-to-patient shipping and confirmation; central pharmacy; temperature excursion management; controlled-substance handling; supply pooling.
- Integrations: EDC (enrollment/eligibility facts in, randomization number/kit out; platform-embedded products eliminate double entry), CTMS (supply rollups), temperature loggers/monitoring software, depot distribution systems.
- Study build/UAT lifecycle with vendor professional services; 24/7 multilingual helpdesk heritage.
- Kit interchangeability: kits not labeled for particular patients; assigned at dispensing time.

### Level 2 — Variant / Optional Structure

- Interaction modality: phone/IVR heritage → web → mobile → (emerging) AI-assisted build/assistants. The "I" in IRT names the modality; RTSM names the function. Modality is not definitional.
- Randomization methodology: fixed-list schemes vs algorithmic (minimization); in-built list generators vs sponsor/vendor-generated lists.
- Blinding posture: double-blind (archetype), single-blind, open-label (machinery reused without concealment).
- Deployment/packaging: standalone specialist vendor; embedded in EDC platform (Medidata-Rave unification); embedded in CRO suite (IQVIA); IRT + supply-chain-services bundling (Almac One).
- Reduced deployments: randomization-only for trials without IP supply; inventory-only companion deployments (4G Prancer Inventory Platform).
- Trial-type adaptations: oncology/CNS/rare-disease complexity (Suvoda positioning), vaccine/large-simplex, gene therapy (Almac white paper), device trials.
- Decentralized-trial posture: DtP shipping, patient receipt confirmation, home-caregiver users.
- Customer tier: global top-20 pharma enterprise programs vs emerging-biotech streamlined builds (Prancer Lite).

### Level 3 — Vendor-specific (research notes only; excluded from final document)

- Suvoda: Sofia AI assistant; agentic AI study build ("kickoff to UAT in as little as two weeks" claim); building-block architecture; marketing metrics (1400+ trials, 0.9 UAT defects).
- 4G Clinical: Prancer/Prancer Lite/Prancer Inventory Platform/4C Supply product naming; GS1 workflow alignment; sustainability framing.
- Almac: IXRS®3 platform name; IRT "boosters" (ART accountability tracking, archival investigator access, drug pooling protocols, DCT support package); Almac Trial Coordinator; biostatistics-led list generation service; Almac One bundling.
- Medidata: Edit Live Design; eSA (electronic supply accountability); myMedidata patient receipt confirmation; Rave unification claims; "3,000+ studies over 11 years" claim.
- IQVIA: Quantam Interactive rapid build/prototyping; SAVE (Supply Automation Value Engine); "140+ pre-validated components" claim; Patient Suite integration.

## Boundary Findings

- **vs EDC (closest sibling).** EDC captures clinical data about subjects (forms, visits, validation, the regulated record); IRT/RTSM decides treatment allocation and manages IP. The enrollment event is shared turf: eligibility/enrollment facts flow in from (or are entered alongside) EDC, and allocation/kit data flow out. Packaging varies from full integration (interfaces) to unification on one platform (Medidata: "not a separate integration") — a packaging seam, not a Type merge: even unified, RTSM remains a distinct product with its own build, roles, and blinding model. Removing allocation+supply from a unified product leaves EDC; removing capture leaves IRT/RTSM. Both leaves stand; ratified against the processed EDC document, which lists "randomization/trial supply" among suite modules.
- **vs CTMS.** CTMS manages trial operations (sites, milestones, monitoring, budgets) and shows supply rollups via integration; it does not randomize subjects or manage kits. The processed CTMS document's seam ("CTMS may show supply rollups but does not randomize or manage kits") is confirmed from this side: every sampled IRT/RTSM product's center of gravity is the assignment transaction and the kit chain of custody, which no sampled CTMS holds. Keep-both ratified.
- **vs clinical trial supply chain services / forecasting planning tools.** Physical distribution (depot storage, packaging/labeling, distribution, returns) and pre-trial forecasting/scenario modeling are adjacent services/products. Evidence: 4G itself ships 4C Supply® (forecasting/planning) as a separate product from Prancer RTSM (live execution); Almac separates Clinical Services (supply chain) from Clinical Technologies (IRT). The IRT/RTSM Type is the trial-conduct system of record for assignment + accountability, not the logistics operator's system.
- **vs pharmacy management systems.** Patient-care pharmacy dispensing vs blinded trial-IP dispensing under a protocol's allocation design. The overlap ("central pharmacy" as an IRT module) is a module, not the Type.
- **vs pure randomization services/tools (the 1+2-without-3 pole).** Randomization-only systems (common in academic and non-IP trials, sometimes inside EDC products) hold the design and produce assignments but carry no trial-supply chain. The market's IRT/RTSM category is the combined system; randomization-only is recorded as a reduced variant / thinner sibling rather than this leaf. No separate directory leaf exists; noted as a boundary note, not a taxonomy change.
- **"去掉什么就变成另一个 Type" judgments:** remove the allocation design → inventory/warehouse software; remove the supply chain → randomization service; remove the interactive site-side transaction → batch list generation (the envelope era); remove EDC-style clinical data capture → this Type stands (it never had it).

## Historical / Market-Sample Check (per Workflow §24)

- Pre-IRT method (sealed envelopes + patient-labeled kit blocks): the ancestor. It fails L0 leg 2 (no interactive system) and partially leg 3 (kits pre-allocated to sequence, not assigned from dynamic inventory). Correctly treated as what this Type replaced.
- First-generation 1990s IVRS: phone randomization; dispensing/resupply added "later" (4G white paper). Randomization-only IVRS = the 1+2-without-3 reduced pole; the historical center of the category once supply was added satisfies all three legs. The L0 holds across the phone era (modality-independent), the web era, and the platform era — modality is confirmed non-definitional.
- Open-label trials: use the same systems for allocation and supply without concealment — confirms blinding governance belongs to L1 (characteristic machinery of the dominant blinded case), not the invariant.
- Regional/scale variance (small academic trials with randomization-only, huge global programs with pooled depots): both reduce to the same three structures at different maturity. Check passed.

## Uncertainties

1. Exact resupply algorithm mechanics (trigger vs prediction parameterization, buffer construction) are documented by the academic literature generically (TR/PR) and by vendor white papers qualitatively; per-product parameterization could not be verified (no public manuals). Final document therefore describes resupply conceptually.
2. The precise trigger event naming (screening vs enrollment vs randomization visit) varies by protocol and product; sources agree the transaction happens at/near the randomization visit. Kept general.
3. Whether "unblinding auto-discontinues the patient" is universal — stated by two vendors (Almac, Octalsoft) with "often times" hedging; kept hedged.
4. Emergency code break roles vary (investigator / designated study leader / drug safety); the pattern (permissioned roles + notification + audit trail) is stable; exact role lists are product- and protocol-specific.
5. IQVIA and 4G evidence rests on fact-sheet/product-page text (search-verified) rather than deep documentation; no precise claims made from them.
6. Direct-to-patient mechanics (dispense-from-depot vs site stock choice) confirmed only for Medidata and Suvoda at description level; kept as a variant with generic wording.

## Final Synthesis

The leaf names one product category under two labels: IRT names the interaction heritage (a site interacts with the system — by phone historically, by web/mobile now), RTSM names the function (randomization + trial supply management). The Type is the clinical trial's treatment-allocation and drug-supply system of record: it holds the study's allocation design; it performs the enrollment-moment assignment transaction; it runs the blinded kit chain from depot to subject with automated resupply and full accountability; it governs who may see treatment assignments and provides controlled emergency unblinding. It is adjacent-but-distinct from EDC (capture), CTMS (operations), supply-chain services (physical logistics/forecasting), and pure randomization services (no supply chain). The defining core is the three jointly-held structures above; everything else in modern products — resupply algorithms, forecasting, DtP, temperature, pooling, analytics, AI build — is mature accretion on that core.
