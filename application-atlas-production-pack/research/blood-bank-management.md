# Research Notes — Blood Bank Management

## Research Goal

Understand what Blood Bank Management software actually is and how it works in real products: what objects exist inside it, how a blood unit moves from donor to patient (or to a care facility), which states and safety gates govern that movement, who uses it, and where its boundary lies against LIS/LIMS, Biobank Management, EHR, and generic inventory systems.

## Initial Boundary

Working hypothesis before research:

- Core purpose: manage blood products (donor-derived blood units and their components) through a regulated lifecycle — donor eligibility, collection, testing, processing/labeling, storage/inventory, compatibility testing, issue to a patient, transfusion record, traceability.
- Primary users: blood center / blood bank staff (technologists, collection staff, quality staff) and hospital transfusion service staff; nurses at the bedside for transfusion confirmation.
- Nearest neighbors: Laboratory Information System / LIS, LIMS, Biobank Management, EHR, Hospital Management System, generic Inventory Management.
- Suspected key distinction: the managed object is a **donor-derived blood unit** (a product with inventory semantics, expiry, and release gates), not a patient specimen and not a research sample.
- Open questions: is donor management part of the Type or only of the blood-establishment variant? Is the hospital transfusion service the same Type? Are EHR-embedded modules a variant?

## Research Questions

1. What are the core objects (donor, donation, unit, component, test, inventory location, request, crossmatch, issue, transfusion)?
2. How does the unit lifecycle flow, and which states/gates are mandatory?
3. How is donor eligibility and deferral handled?
4. How is inventory organized (product type, blood group, status, expiry)?
5. How do compliance and traceability manifest (labeling standards, safety checks, release gates, audit)?
6. How does the system integrate with EHR / LIS / instruments / external donor centers?
7. What variants exist (blood establishment vs hospital transfusion service vs EHR-embedded vs regional regimes)?

## Representative Products

Selected for market representation, documentation quality, different product philosophy, different customer tier, and regional spread:

| Product | Vendor | Pole | Why selected |
|---|---|---|---|
| WellSky Transfusion (formerly SCC Soft Computer SoftBank line) | WellSky | Hospital transfusion service / blood bank LIS | Long-established (40+ years claim), FDA 510(k) cleared, US hospital market leader segment |
| WellSky Blood Centers | WellSky | Blood establishment / community blood center | Claims ~75% of US blood supply tested with it; full donor-to-distribution lifecycle |
| EdgeBlood + Blood Donor On Line + EdgeTrack / EdgeTrack Ward | Inlog (France) | Blood establishment + hospital transfusion (both poles, modular) | European/regional sample; French regulatory context (EFS, hémovigilance); modular product philosophy |
| ISBT 128 (ICCBBA) | ICCBBA (standards body) | Labeling/traceability standard | Defines the unit-identification substrate the software must implement |

Attempted but unreachable (recorded as source-access limitations): Haemonetics SafeTrace Tx (404 ×2), Mak-SYSTEM eProgesa (transport error ×2), Hemasoft (transport error ×2), Medinfo/medinfo.com.au (wrong domain; .com.au transport error), FDA BECS pages (404 ×2), Epic Beaker (403), DuckDuckGo search (timeout). No precise claims are made for these products.

## Sources

- WellSky — Blood Transfusion (blood bank software): https://wellsky.com/blood-bank-software/ (fetched 2026-09-06)
- WellSky — Blood Centers: https://wellsky.com/blood-centers/ (fetched 2026-09-06)
- Inlog — EdgeBlood: https://www.inlog.com/edgeblood/ (fetched 2026-09-06)
- Inlog — Blood Donor On Line: https://www.inlog.com/blood-donor-on-line/ (fetched 2026-09-06)
- Inlog — EdgeTrack et EdgeTrack Ward: https://www.inlog.com/edgetrack-et-edgetrack-ward/ (fetched 2026-09-06)
- ICCBBA — ISBT 128 standard: https://www.iccbba.org/ (fetched 2026-09-06)

Evidence layers: **A** = directly observed on the fetched official page; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + boundary reasoning.

## Product Observations

### WellSky Transfusion (hospital transfusion service pole) — evidence layer A

From https://wellsky.com/blood-bank-software/:

- Positioned as "blood bank software" / "blood bank LIS systems" for hospitals; "trusted for more than 40 years"; FDA 510(k) cleared device.
- **Safety checks**: "more than 60 built-in automated safety checks at critical times throughout the process including 15 at the time of transfusion".
- **Inventory management**: "at-a-glance view of product availability. Color-coded charts … indicate product inventory status and provide a simple way to view the number of products within specific expiration date ranges."
- **Reporting**: built-in reports + "WellSky Transfusion Analytics" for utilization, inventory management, and patient history reports; clinical/financial/operations teams.
- **Dashboards**: "display a wide variety of data … in a single view. Streamlined entry allows you to complete several tasks without extra navigation."
- **Integrations**: "end-to-end communications with electronic health record and laboratory systems, instrumentation, billing applications, remote storage devices, and outside donor centers"; "automate orders and test results, update product status with EMRs".
- Extensions (product-specific modules): Epic integration (co-licensing), Quality and Compliance (document/compliance/accreditation for hospital blood banks, blood centers, testing centers, cell therapy), Transfusion Analytics, **Emergency Issue** ("connects the blood bank to every department … expedite blood bank deliveries … while maintaining patient safety"), **Bacterial Platelet Testing** ("tracks bacterial test results to extend the life of your platelet products … updating the expiration dates and product codes"), **Patient Assure** ("flags and addresses duplicates … trusted view of the patient's complete medical history, including products used prior to transfusion").

### WellSky Blood Centers (blood establishment pole) — evidence layer A

From https://wellsky.com/blood-centers/:

- Scope statement: "From donor recruitment and blood collection, to manufacturing, testing and distribution, you can confidently manage the complete product life cycle within a single FDA 510(k) cleared system." Claims ~75% of the U.S. blood supply tested using WellSky Blood Centers.
- **Recruitment**: donor call lists, scheduling, reminders; assignment of vehicles, equipment, staff; per-drive data collection and productivity reporting (mobile blood drives).
- **Donor management**: "dynamic eligibility calculation, deferral tracking through notification to the donor, and a full CASI (Computer Assisted Self Interview) including health history, physicals, and consent forms"; donor history/eligibility/donations/communications in one view.
- **Manufacturing management**: "extensive controls for all aspects of product manufacturing, including cGMP guides and over 40 safety checks in the labeling process"; Enhanced Manufacturing Manager for exception workflows.
- **Pathogen reduction**: first BECS capturing complete/controlled pathogen-reduction data; compatible with the INTERCEPT system (developed in consultation with Cerus).
- **Inventory management**: "Only transfusable products move to inventory with safety checks at packing to ensure the status of the donor or product has not changed since labeling. Customer defined requirements for product restriction … Easily manage returns, outdates, and product quarantine."
- **Multi-site**: enterprise blood centers, cross-time-zone data sharing, affiliate/merged sites with independent operations.
- **Integration**: open APIs.
- Quality & Compliance (formerly KnowledgeTrak) companion for document/compliance/accreditation.

### Inlog EdgeBlood (blood establishment, modular, French/EU context) — evidence layer A

From https://www.inlog.com/edgeblood/:

- Positioning: "Logiciel médical complet pour la gestion des collectes, donneurs et de la production/distribution des produits sanguins conçu pour les banques de sang et centres de collecte de sang." Manages mobile donation campaigns, regulatory obligations, transfusion safety/traceability; highly configurable modular design.
- Feature list (directly observed): donor recruitment; resource & collection planning; blood collection (prélèvement sanguin); donor screening (dépistage des donneurs); production and labeling; **inventory and quarantine**; quality assurance; delivery/shipping of blood; billing/accounting; **ISBT 128 compliance**; transfusion orders (commandes de transfusions); receipt of blood components; patient screening (red-cell counts, HLA); **electronic crossmatch** (compatibilité croisée électronique); transfusion follow-up; autotransfusion; traceability and reports; configurable popup alerts/notifications; web-based donor questionnaire under development.

### Inlog Blood Donor On Line (donor intake surface) — evidence layer A

From https://www.inlog.com/blood-donor-on-line/:

- Dematerializes the pre-donation questionnaire: donor completes it from home (web/mobile) or on site (fixed or mobile collection) before donating.
- Customizable questionnaire with conditional questions; admin module for building it.
- Donor identified at reception; QR code generated by the questionnaire links donor to EdgeBlood; if not completed, staff activate it on-site (tablet/PC).
- Eligibility verification based on questionnaire answers, performed by center staff.
- Electronic signature module (donor; handwritten signature on tablet); donor and physician both sign.
- **Physician interface**: doctor reviews/modifies the questionnaire during the pre-donation interview; separate admin accesses record donor vitals (constantes) and scan bag barcodes.
- **Donor queue management**: status workflow with tags; supervisor/physician sees donors awaiting the pre-donation interview.
- Multilingual; optional PDF archiving on a secure server or definitive deletion (paperless option).

### Inlog EdgeTrack / EdgeTrack Ward (hospital transfusion pole, French context) — evidence layer A

From https://www.inlog.com/edgetrack-et-edgetrack-ward/:

- Positioning: "solution logicielle complète pour la gestion de la transfusion et des produits sanguins au sein des établissements de soins" — transfusion management inside care facilities; traceability "de la prescription à la délivrance" (from prescription to delivery).
- "Parfaite compatibilité avec l'EFS": communicates with the distributing blood establishment (Établissement Français du Sang) via AFNOR communication standards.
- **Hémovigilance**: complete solution for hemovigilance, traceability, and management of blood depots (dépôts attributeurs, relais d'urgence — attributed depots, emergency relays).
- EdgeTrack features: depot management; EFS communication; complete transfusion record (dossier transfusionnel) with exhaustive archiving; post-transfusion information management (follow-up exams); transfusion traceability (record and confirm transfusions, incident entry).
- EdgeTrack Ward (bedside) features: consult the patient's transfusion record; assisted prescription of PSL (produits sanguins labiles) and analyses; prescription of PSL + immuno-hematology (IH) exams; **pre-transfusion checks** (risk information, patient consent collection); **returns of untransfused PSL**; transfusion incident management; confirmation and return of transfusion; pre/post-transfusion information; surveillance management; connected PSL prescription.

### ICCBBA / ISBT 128 (standard substrate) — evidence layer A

From https://www.iccbba.org/:

- "ISBT 128 is the global standard for the terminology, identification, coding and labeling of medical products of human origin (including blood, cell, tissue, milk, and organ products). Used on six continents."
- Provides "international consistency to support the transfer, traceability and transfusion/transplantation of blood, cells, tissues and organs."
- Label data can be carried by Code 128 bar codes, 2-D data matrix symbols, or RFID tags.
- ICCBBA manages product codes, reference tables, and a check-character calculation for ISBT 128 data structures.

## Cross-product Comparison

| Aspect | WellSky Transfusion | WellSky Blood Centers | Inlog EdgeBlood | Inlog EdgeTrack/Ward |
|---|---|---|---|---|
| Primary pole | hospital transfusion service | blood establishment | blood establishment (+ hospital features) | hospital transfusion (depot + ward) |
| Donor registry / eligibility / deferral | via outside donor centers (integration) | yes (dynamic eligibility, deferral + donor notification, CASI) | yes (recruitment, screening) | — |
| Collection / drives | — | yes (mobile drives, vehicles/staff assignment) | yes (mobile campaigns, planning) | — |
| Testing | instrument integration; orders/results with EMR | testing stage in lifecycle | donor screening; patient screening (IH) | IH exam prescription |
| Manufacturing / labeling | — | cGMP guides, 40+ labeling safety checks, pathogen reduction | production & labeling, ISBT 128 | — |
| Inventory | availability view, expiry ranges, color-coded | only transfusable units enter inventory; returns/outdates/quarantine | inventory & quarantine | depot management (attributed depots, emergency relays) |
| Request → issue | safety checks incl. at transfusion; emergency issue | customer product restriction; packing checks | transfusion orders; electronic crossmatch; receipt of components | prescription → delivery; pre-transfusion checks |
| Bedside / transfusion record | Patient Assure (patient history incl. prior products) | — | transfusion follow-up | ward confirmation, surveillance, incidents, returns |
| Traceability | patient history reports | complete product life cycle | traceability & reports | complete transfusion record; hemovigilance |
| Compliance posture | FDA 510(k) cleared | FDA 510(k) BECS, cGMP | ISBT 128, regulatory obligations | EFS/AFNOR compatibility |
| Integrations | EHR, lab, instruments, billing, remote storage, donor centers | open APIs | secure exchange with care facilities | EFS communication |

### Stable commonalities (evidence layer B)

Across the sample, every product — regardless of pole — provides:

1. **Individually identified blood units** carrying product identity (product code, ABO/Rh group, expiration) — ISBT 128 or equivalent labeling.
2. **A status-gated lifecycle**: units are held in states and may not move to usable/issued status until required checks pass (quarantine → release; packing checks; transfusion-time checks).
3. **A unit inventory** queryable by product type, blood group, status, and expiration range.
4. **Request-driven allocation/issue**: units are matched/reserved and issued against a specific request (patient order at a transfusion service; hospital/customer order at a blood center), with a recorded handoff.
5. **Traceability**: a recorded chain from donation/source through every state change to final disposition (transfused, returned, outdated, discarded), plus incident recording.
6. **Regulated-device posture**: FDA 510(k) cleared (US products), cGMP controls, ISBT 128 labeling, national-system compatibility (EFS/AFNOR in France).
7. **Integration with the surrounding clinical IT**: EHR orders/results, lab instruments, billing, remote storage monitoring, external donor centers / care facilities.

### Pole-dependent structures (present on one side of the market)

- Donor registry, eligibility/deferral, CASI, collection/drive logistics, manufacturing/labeling, distribution shipping → **blood establishment side**.
- Patient ABO/Rh typing, antibody screening, crossmatch (incl. electronic), reservation, issue to patient, bedside confirmation, transfusion record, returns → **hospital transfusion service side**.
- Products exist on both sides (WellSky splits Transfusion vs Blood Centers; Inlog splits EdgeBlood vs EdgeTrack/Ward) — strong evidence that these are two deployments of one Type, not two Types.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The smallest structure without which the software is not a blood bank management system:

```text
Individually identified blood product unit
  (unique unit identity + product code + blood group + expiration)
└── Status-gated lifecycle
    (units held in states; safety gates control movement to available/issued;
     quarantine / expired / discarded states exist)
└── Unit inventory
    (queryable stock by product type, blood group, status, expiry)
└── Request-driven allocation & issue
    (units matched/reserved and issued against a specific request,
     with a recorded handoff)
└── Traceability chain
    (donation/source → every state change → final disposition)
```

Justification (§24 historical check applied): older standalone blood bank systems, regional products (Inlog, Hemasoft-class), and hospital LIS-embedded modules all exhibit these five properties; a paper-based blood bank's ledger has the same structure. Donor management, collection, testing machinery, and manufacturing are NOT in L0 because hospital transfusion services — unambiguously blood bank software — perform none of them (they receive units from donor centers), yet remain the Type.

### L1 — Common Mature Structure

- Donor registry with eligibility calculation, deferral tracking (with donor notification), health-history questionnaire (CASI), consent, physician review (blood-establishment deployments)
- Donation/collection recording; mobile drive scheduling and resource assignment
- Infectious-disease/serology testing results attached to units; testing gates release
- Component manufacturing/separation and labeling under cGMP-style controls with labeling safety checks
- Patient ABO/Rh typing and antibody screening; compatibility testing (serologic and electronic crossmatch); unit reservation for a patient
- Issue-time safety checks; emergency-issue path that expedites while preserving checks
- Bedside transfusion confirmation, surveillance, and the patient transfusion record; returns of untransfused units
- Expiry management: outdates, wastage, expiry-range views; platelet bacterial-testing result entry that updates expiry
- Dashboards and reports: inventory, utilization, patient history, traceability
- Integration: EHR orders/results, lab instruments, billing, remote storage monitors, external donor centers / care facilities
- Multi-site / affiliate support; open APIs
- Quality & compliance document management (documents, accreditation, CAPA-style processes)

### L2 — Variant / Optional Structure

- Deployment pole: standalone blood establishment vs hospital transfusion service vs combined national/regional system
- Packaging: standalone product vs LIS-embedded module vs EHR-coexisting (Epic co-licensing/integration observed)
- Regional regulatory regime: FDA 510(k)/cGMP (US) vs EU/national blood service interfaces (EFS/AFNOR, hémovigilance in France)
- Pathogen-reduction data capture; bacterial platelet testing
- Autotransfusion; HLA/platelet support
- Billing/accounting integration
- Donor self-service (online/mobile pre-donation questionnaire, QR check-in, e-signature)
- Paperless options (PDF archiving vs data deletion), multilingual support
- Analytics modules (utilization, patient blood management)
- Hospital donor programs (hospital-based collection) as a mid-form between the two poles

### L3 — Vendor-specific (kept out of the final document)

- WellSky: exact counts ("60+ safety checks, 15 at transfusion"; "40+ labeling safety checks"; "75% of US blood supply tested"); module names Patient Assure, Emergency Issue, Bacterial Platelet Testing, Transfusion Analytics, Quality & Compliance (ex-KnowledgeTrak), Enhanced Manufacturing Manager; INTERCEPT/Cerus partnership claim.
- Inlog: product names EdgeBlood / Blood Donor On Line / EdgeTrack / EdgeTrack Ward; DAD (délivrance à distance) interface; dépôts attributeurs / relais d'urgence vocabulary; EFS/AFNOR compatibility; Héma-Québec, CHU Besançon, AP-HM, CHU La Réunion references.

## Vendor-specific Findings

- WellSky's safety-check counts and market-share claims are vendor marketing figures — recorded, not generalized.
- Inlog's EFS/AFNOR compatibility is specific to the French national blood system context; other countries use different national interfaces.
- WellSky's Epic co-licensing is a commercial arrangement; it evidences EHR coexistence as a variant, not an Epic feature set.

## Boundary Findings

| Neighbor | Relationship | Distinction | "Remove X and it becomes the other Type" test |
|---|---|---|---|
| Laboratory Information System / LIS | adjacent; often the host or sibling | LIS manages patient specimens through order→collection→analysis→result→report; blood bank manages donor-derived products with inventory, expiry, release gates, and issue | Remove unit inventory/expiry/issue and keep patient test reporting → generic LIS. Remove patient-test reporting and keep units → still a blood bank |
| LIMS | adjacent | LIMS manages industrial/research sample workflows; no transfusion issue, no blood-group compatibility, no donor eligibility | Same test as LIS |
| Biobank Management | adjacent; same "stored specimen" surface | Biobank stores research specimens (ISO 20387 context); no clinical release gates, no crossmatch, no patient issue; donor consent is research consent | Remove clinical issue/compatibility and transfusion traceability → biobank. Vendor evidence: Inlog sells EdgeCell (biobanks) as a separate product line from EdgeBlood |
| EHR | adjacent; integration partner | EHR holds the patient chart and issues orders; blood bank holds the unit inventory and executes the issue workflow | The unit inventory and release/issue machinery never lives in the EHR core; coexistence observed (WellSky–Epic) |
| Hospital Management System | broader | HMS spans admission, billing, departments; blood bank is a departmental system of record for units | — |
| Generic Inventory Management | capability overlap | Generic inventory lacks regulated status gates, blood-group compatibility semantics, patient-linked issue, and unit traceability | Remove status gates + compatibility + patient linkage → generic inventory |
| Organ Transplant Management | analogous pattern | Same chain-of-custody + matching + traceability pattern, but organs are not manufactured/stocked units with expiry; different objects and rules | — |
| Donor Testing Services / blood testing labs | adjacent | Testing is one gate inside the lifecycle; a standalone testing lab has no inventory/issue | Remove inventory/issue → testing service, not blood bank management |

## Uncertainties

- EHR-embedded blood bank modules (e.g., transfusion functionality inside an EHR vendor's lab module) could not be directly documented (Epic 403; no accessible official docs). The researched sample evidences EHR **coexistence/integration** (WellSky–Epic co-licensing; EMR order/result exchange) rather than embedding. Final document uses qualified wording.
- Exact audit-trail mechanics (per-user attribution of every state change) are implied by the regulated posture (FDA 510(k), cGMP) but were not directly observed as feature text on the fetched pages; the final document states the regulated posture and traceability, not precise audit mechanics.
- Plasma-collection centers (plasma-derived industry) likely use related but distinct systems; no evidence gathered — excluded from the final document.
- SafeTrace Tx, eProgesa, Hemasoft could not be reached; the sample's breadth (2 vendors × both poles × 2 regions + 1 standard body) is judged sufficient, but US-hospital-pole detail rests on WellSky alone.

## Final Synthesis

Blood Bank Management software is the regulated operational system of record for blood products. Its defining core is deliberately small: individually identified blood units; a status-gated lifecycle (quarantine → release → issue → disposition); a unit inventory organized by product, blood group, status, and expiry; request-driven allocation/issue with a recorded handoff; and an end-to-end traceability chain. Everything else — donor management, collection, testing, manufacturing/labeling, crossmatch machinery, bedside confirmation, analytics, billing — is mature but pole- or deployment-dependent structure. The Type has two stable poles (blood establishment vs hospital transfusion service) that share the same core model; products and product lines exist on both poles, and several vendors sell both. The strongest boundary is against LIS (patient specimens vs blood units) and Biobank Management (research storage vs clinical release-and-issue).
