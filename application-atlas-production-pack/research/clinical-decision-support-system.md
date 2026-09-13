# Research Notes — Clinical Decision Support System

## Research Goal

Identify the smallest stable structure that defines the **Clinical Decision Support System (CDSS)** Application Type, and place every other observed feature at the correct abstraction level.

Following `WORKFLOW_v1.1.md §22` and `WRITING_GUIDE_v1.1.md §28`, this document separates:

```text
L0 Defining Invariant
L1 Common Mature Structure
L2 Variant / Optional
L3 Vendor-specific
```

It also separates evidence into layers per `WORKFLOW_v1.1.md §23`:

```text
A Direct Product Observation
B Cross-product Commonality
C Canonical Inference
```

## Initial Boundary

Target:

> Clinical Decision Support System

Nearest confusing Types (from DIRECTORY §22 and adjacent sections):

- Electronic Health Record / EHR — the record system CDS usually lives inside
- CPOE / Clinical Order Management — the order-entry workflow where CDS most often fires
- Electronic Prescribing — the prescribing workflow that consumes medication CDS
- Medical Image Analysis Platform — also patient-specific and advisory, but image-centric
- Population Health Management — also "identify who needs attention", but population-facing
- Care Plan Management — care plans appear both as CDS content and as a managed record system
- Clinical Documentation Platform — documentation guidance is a CDS intervention family
- Patient-facing symptom checkers / triage tools — same machinery, different decision-maker

Working hypothesis:

> A CDSS is software that applies clinical knowledge to a specific patient's situation and delivers the result as advice to a clinician at the moment of a clinical decision. The clinician, not the system, acts on the advice.

The hypothesis is intentionally narrower than "any software used in clinical decisions" and broader than "drug–drug interaction alerts" — the alert is only the most visible intervention family.

## Research Questions

- What is the minimal structure without which a product is no longer recognizable as CDS?
- How does patient context reach the decision logic? (embedded in EHR vs external service vs manual entry)
- At which points in the clinical workflow does CDS fire?
- What forms does the advisory output take? (interruptive alert, passive card, order set, differential list, risk score, registry action list)
- What happens after delivery? (accept / reject / override, reason capture, feedback into tuning)
- Who maintains the knowledge? (content vendors, hospital informatics teams, rule governance)
- How is alert fatigue handled as a structural concern?
- Where are the boundaries vs EHR, CPOE, medical image analysis, population health, and clinical reference content?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| OpenCDS | open-source CDS engine | exposes the engine anatomy explicitly (data in → rules → suggestions out); standards-based |
| Zynx Health (ZynxOrder) | evidence-based CDS content vendor | shows the knowledge content lifecycle (author → customize → deploy into EHR → keep current) |
| Isabel Healthcare (DDx Companion) | diagnostic decision support | shows the standalone/point-of-care pole with EMR integration via API / info-button |
| FDB (First Databank) | medication knowledge + alert management | shows the drug-knowledge substrate and the alert-fatigue governance layer |
| MEDITECH Expanse | EHR-embedded CDS | shows the embedded pole: active vs passive interventions, registries/surveillance, rules repository |

Plus one standards source used for integration machinery (not a product):

- HL7 CDS Hooks — the published hook-based pattern for invoking decision support from within a clinician's workflow

The five products intentionally span: engine / content / diagnostic tool / knowledge base / embedded EHR capability; open-source / vendor / institution; deterministic rules / curated evidence / machine learning.

## Sources

Research date: **2026-09-07**

All sources below were fetched successfully on the research date (Tier 1 official documentation or official product surfaces):

- OpenCDS — https://www.opencds.org/ and https://www.opencds.org/pages/resources
- Zynx Health — https://www.zynxhealth.com/ and https://www.zynxhealth.com/solution/zynxorder/
- Isabel Healthcare — https://www.isabelhealthcare.com/ and https://www.isabelhealthcare.com/products/isabel-ddx-companion
- FDB (First Databank) — https://www.fdbhealth.com/ and https://www.fdbhealth.com/solutions/alertspace-drug-alert-management-software
- MEDITECH — https://ehr.meditech.com/ehr-solutions/clinical-decision-support
- HL7 CDS Hooks — https://cds-hooks.hl7.org/ (Implementation Guide v2.0.1)

Failed / not attempted fetches:

- https://www.meditech.com/en/expanse returned Page Not Found (wrong URL guess); corrected to the EHR CDS page above, which succeeded.
- Epic and Oracle Health (Cerner) embedded CDS documentation was **not** fetched (Epic user-web is login-gated; Oracle Health public docs not attempted within budget). Epic and Cerner appear in this research only as market context referenced by other vendors' pages (Isabel: "available in the Cerner App Gallery and Epic clients can have info-button access").

Per `WORKFLOW_v1.1.md §23 Source-access Limitation`:

> 1. record the limitation ✓
> 2. reduce assertion strength for EHR-internal mechanics (e.g., Epic BPA behavior) ✓
> 3. avoid precise workflow/rule claims that depend on inaccessible evidence ✓
> 4. do not compensate from model memory ✓

Vendor marketing pages (Zynx, Isabel, FDB, MEDITECH) are used as Tier-2 official product surfaces: they support product positioning, scope, and named capabilities, but numeric claims on them (order-set counts, accuracy percentages, hours saved) are treated as vendor claims and kept out of the final document.

## Product Observations

### OpenCDS (open-source CDS engine)

- Layer A: the project describes itself as open-source, standards-based clinical decision support tools "that can be widely adopted to enable CDS at scale"; Java-based engine, Apache 2 licensed.
- Layer A: the project's own three-step description of what its software does:
  1. "transform proprietary source data from the EHR into a standard data structure"
  2. "evaluate the data using a set of rules based on the latest researched medical knowledge"
  3. "return appropriate treatment suggestions for an individual patient"
- Layer A: integration options offered to clients: CDS Hooks using HL7 FHIR as the data model for input and output; HL7 DSS using vMR (Virtual Medical Record) as the data model; customizable for other APIs.
- Layer A: rules may be written in Java, Drools, HL7 CQL (listed as future support), or any custom rules language via a developed adapter.
- Layer A: the example project exists specifically to show how to create a KnowledgeModule adapter for a chosen rules engine — knowledge packaged as modules is a first-class engineering unit.
- Layer B observation: the engine's anatomy (normalize patient data → evaluate knowledge → return patient-specific suggestions) is presented as the definition of CDS by a neutral, non-commercial party.

### Zynx Health (evidence-based CDS content vendor)

- Layer A: positioning: helping organizations "align their clinical decision support, strategies, and workflows around the standardization of evidence-based best practices"; operating since 1996; vendor-claimed use in over 1,500 hospitals; KLAS awards in "Clinical Decision Support – Care Plans and Order Sets" (vendor claim).
- Layer A (ZynxOrder): described as a "cloud-based clinical decision support solution that enables you to deploy and customize evidence-based order sets into your EHR."
- Layer A: the published content workflow:
  1. access the content library through the vendor's content management system (AuthorSpace)
  2. work from vendor default order sets or customize
  3. review with stakeholders using collaboration software (ViewSpace) to gain consensus
  4. deploy the order sets into the EHR
  5. keep content current with vendor updates on practice-changing evidence
- Layer A: updates are designed so new recommendations can be applied "without risking the content you've previously customized" — vendor content and local customization are versioned separately.
- Layer A: content grounded in citations of national guideline/performance-measure organizations and journals; a "referential web pages" layer links guidance to sources (vendor claim on counts withheld from final doc).
- Layer A: Knowledge Analyzer — a product that automates updating order-set content inside a partner EHR (MEDITECH); case study cites hours saved per update cycle (vendor claim; withheld from final doc).
- Layer A: sibling content families: evidence-based plans of care (ZynxCare), primary-care guidance, chronic-care management content; professional informatics services.
- Layer B observation: the same "content lifecycle" pattern (library → customize → review → deploy → maintenance updates) is the commercial counterpart to the engine anatomy seen in OpenCDS.

### Isabel Healthcare (diagnostic decision support)

- Layer A (root): the tool "can convert a patient's signs and symptoms into a list of relevant diseases or triage advice"; machine-learning based; used in over 90 countries and 14 languages (vendor claims).
- Layer A (DDx Companion, the clinician-facing product):
  - input: patient demographics plus presenting clinical features — chosen from a large autocomplete phrase list or entered as free text; may include lab / imaging results, co-morbidities, and other risk factors
  - computation: "specialized algorithms to present only results relevant to the patient's age, sex and region"; results ranked by relevance match against a database of typical and atypical disease presentations
  - output: ranked differential list with a colored likelihood bar; "red flags" highlight 'don't miss' diseases; sortable by specialty; a "Drugs" feature lists medications that could cause the symptoms
  - next steps: partnered evidence-based knowledge (DynaMed / DynaMedex, BMJ Best Practice) for further signs to check, first-line tests, treatment protocols
  - accuracy claims exist but are vendor claims (withheld from final doc)
- Layer A: workflow integration: manual use, or integration with an EMR via the company's API so clinical features are extracted automatically; availability via a major EHR vendor's app gallery (Cerner) and info-button access for another (Epic).
- Layer A: sibling products: a patient-facing self-triage tool for institutions/health platforms, and a clinical educator tool for training; API made available since 2010.
- Layer B observation: diagnostic CDS shares the same anatomy — patient context (demographics + features) + knowledge (trained disease-presentation database) + advisory output (ranked differential) + clinician decision ("reassurance in decision making", "safety net").

### FDB (First Databank) (medication knowledge + alert management)

- Layer A (root): drug databases positioned as the substrate that "empower[s] EHR decision support with clinically-relevant drug data"; applications listed across EHR, CPOE, ePrescribing, drug utilization review, eMAR, dispensing; smart-pump drug library content; pharmacogenomic CDS ("evidence-based drug-gene guidance within the workflow").
- Layer A: a knowledge module family explicitly organized as clinical modules — drug–drug interaction and drug–allergy modules are named as the knowledge behind medication alerts.
- Layer A (AlertSpace): "the breakthrough solution for medication alert fatigue":
  - problem statement: "the high volume of medication alerts for drug-drug interactions, drug-allergy reactions and more, overwhelms clinicians, renders some alerts ineffective"
  - machinery: customize allergen groups, medications, and ingredient names used to profile patient allergens; edit, turn off, track, and audit customizations; compare against the alerts most commonly customized by the product's user community
  - goal: "reduce alert fatigue and improve clinician acceptance of computerized provider order entry (CPOE)"
- Layer A: CDS Analytics — "insights into the effectiveness of an organization's CDS" (measurement layer).
- Layer A: Targeted Medication Warnings — patient-specific medication guidance positioned to reduce alert volume (vendor-claimed percentage withheld from final doc).
- Layer B observation: the knowledge base itself is not the CDS; the CDS emerges when the knowledge is evaluated against a patient's medication list / allergen profile inside an ordering workflow. The alert-management and analytics layers treat CDS output as a governed, tunable operational system.

### MEDITECH Expanse (EHR-embedded CDS)

- Layer A: "MEDITECH's wide range of clinical decision support interventions include active formats that engage clinicians while ordering or documenting, and passive formats that require clinicians to take action, such as linked references" — the vendor's own active/passive taxonomy.
- Layer A: evidence-based content is "embedded in Expanse to give your organization immediate EHR benefits"; third-party knowledge vendors (IMO, Zynx Health, FDB, National Decision Support Company, Elsevier, NCCN) have their content "embedded in Expanse's clinical workflows" — the EHR vendor explicitly positions knowledge vendors as the content layer of its CDS.
- Layer A: Patient Registries and Surveillance work "in tandem to identify patients who may need your attention":
  - preloaded content includes "standard displays, rules, and algorithms" for common conditions, hospital-acquired infections, and quality measures; organizations may use as-is, tailor, or create their own
  - condition registries (diabetes, COPD, hypertension…), health-maintenance registries, event registries (recent ED visit, pre-visit planning)
  - Surveillance: identifies at-risk patients, monitors care, guides the care team; actionable status boards; quality measures; conditions (VAP, sepsis); action lists "including orders, documentation, and notifications"; quality watchlists
- Layer A: a "clinical rules database" — a repository of "approved, multidisciplinary rules for common workflows and issues" that "reduces obstacles to decision support".
- Layer A: monitoring tools for alerts and clinical standardization "minimize alert fatigue, track care variations, and fine-tune quality improvement programs"; documentation templates addressed to specialties; EHR Excellence Toolkits bundle content with workflows for priorities (CAUTI, diabetes, opioid stewardship).
- Layer B observation: inside a full EHR, CDS appears as a capability distributed across ordering, documentation, surveillance, and quality functions — with the same ingredients (knowledge content, rules, delivery into workflow, alert monitoring) organized around the EHR's own objects.

### HL7 CDS Hooks (standard — integration machinery)

- Layer A: the specification "describes a 'hook'-based pattern for invoking decision support from within a clinician's workflow"; synchronous, workflow-triggered CDS calls returning information and suggestions.
- Layer A: roles: the **CDS Client** (an EHR or other clinical system) calls external **CDS Services** at defined workflow points (**hooks**); services return **Cards**.
- Layer A: published hooks name the canonical decision points: patient-view, order-select, order-sign, encounter-start, encounter-discharge, allergyintolerance-create, medication-refill, problem-list-item-create, appointment-book.
- Layer A: Card anatomy: summary text, optional detail, urgency indicator (info / warning / critical), source attribution, optional suggestions the user may accept or reject, optional links, optional override reasons presented to the clinician when dismissing; services may propose auto-applied actions but "the CDS Client decides whether to auto-apply".
- Layer A: a **Feedback API** through which services "learn the outcomes of their recommendations": suggestion accepted, card ignored, guidance overridden (with or without coded override reason).
- Layer A: **prefetch**: the service declares the FHIR data it needs (e.g., latest A1c, active conditions) and the client supplies it; the specification advises services to respond quickly (on the order of 500 ms) to fit the interactive workflow.
- Layer B observation: the standard institutionalizes the whole interaction loop — context in, cards out, accept/reject/override, feedback back — as the contract between an EHR and an external CDS service.

## Cross-product Comparison

| Finding | OpenCDS | Zynx | Isabel | FDB | MEDITECH | CDS Hooks | Level |
|---|---|---|---|---|---|---|---|
| advice computed for an identified individual patient | yes ("for an individual patient") | yes (order sets deployed for a patient's care moments) | yes (age/sex/region-filtered) | yes (patient's med list / allergen profile) | yes (per-patient action lists) | yes (patientId context) | L0 |
| clinical knowledge / evaluation machinery applied to context | rules engine, knowledge modules | curated evidence-based content library | trained disease-presentation database + algorithms | drug knowledge modules (DDI/allergy/PGx) | rules + algorithms + evidence content | service-side, unspecified | L0 |
| output delivered as advice at a clinical decision point | treatment suggestions returned to calling system | order sets / care plans surfaced in EHR at point of care | ranked differential at the diagnostic moment | alerts at ordering/dispensing points | active (ordering/documenting) + passive formats | cards at workflow hooks | L0 |
| clinician retains the decision (system advises, does not act) | yes (suggestions returned) | yes | yes ("reassurance", "safety net") | yes (acceptance of alerts is the goal) | yes | yes (accept/reject/override; auto-apply only at client's discretion) | L0 |
| delivery embedded in EHR workflow | via CDS Hooks / HL7 DSS integration | deployed into the EHR | via API / info-button / app gallery | inside EHR/CPOE/ePrescribing | native in Expanse | EHR is the calling client | L1 |
| interruptive vs non-interruptive presentation | out of engine scope | point-of-care deployment formats | tool surface | alerts | active vs passive formats | card indicator (info/warning/critical) | L1 |
| accept / reject / override with reason capture | out of engine scope | — (content, not runtime) | clinician judgment out-of-band | clinician acceptance of alerts | alert monitoring | overrideReasons + feedback API | L1 |
| alert fatigue as managed operational concern | — | — | — | named product focus | named monitoring tools | feedback loop supports tuning | L1 |
| knowledge content lifecycle (author → customize → review → deploy → update) | knowledge modules as code | core of the product (AuthorSpace/ViewSpace, updates preserving customizations) | vendor-maintained, versioned training | vendor-updated drug knowledge | use-as-is / tailor / create own; approved rules repository | service versioning left to implementers | L1 |
| evidence sourcing / guideline linkage | "latest researched medical knowledge" | guideline + journal citations | publisher partnerships (DynaMed, BMJ) | drug knowledge curation | evidence-based toolkits | source attribution on cards | L1 |
| CDS effectiveness analytics | — | update/analytics tooling | validation studies page | CDS Analytics product | track care variations, fine-tune QI programs | feedback events | L1 |
| ML/model-driven logic | rules-first (CQL planned) | curated evidence | ML since inception (vendor) | rules + patient-specific guidance | rules + algorithms (sepsis etc.) | agnostic | L2 |
| population-level surveillance feeding per-patient action | — | — | — | — | registries + surveillance | — | L2 |
| patient-facing sibling (triage/symptom) | — | — | self-triage product | consumer applications line | patient-facing modules exist in EHR suite | — | L2 |
| stand-alone point-of-care app form | no (engine) | no (content) | yes (web/app + trial) | no (knowledge substrate) | no (embedded) | n/a (standard) | L2 |

## Canonical Model

### L0 — Defining Invariant

```text
Patient-Specific Clinical Context
  └── Clinical Knowledge Evaluated Against That Context
      └── Person-Specific Advisory Output, Delivered at a Clinical Decision Point
          └── Clinician Retains the Decision (accept / reject / override)
```

Four properties. If any one is removed, the product stops being recognizable as a CDSS:

- **Patient-specific clinical context** — the computation is about an identified individual patient (their demographics, problems, medications, results, entered features). Remove it and the product becomes generic clinical reference content (different Type).
- **Clinical knowledge applied through decision logic** — rules, curated evidence, trained models, or scores that convert context into advice. Remove it and the product is data display — a function of the EHR, not decision support.
- **Advisory output at a decision point** — the result is delivered where a clinical decision happens (ordering, documenting, diagnosing, reviewing). Remove the decision-point binding and the product drifts to reporting/analytics.
- **Clinician retains the decision** — the system's output enters care only through a human's acceptance; overriding is a supported, instrumented path. Remove this and the system is an autonomous execution system, which CDS by definition is not.

Historical / market-sample check (`WORKFLOW_v1.1.md §24`): older CDS (hospital pharmacy checking systems, Arden-syntax rule modules, early diagnostic tools) and non-US or institution-built CDS all satisfy this minimal core — none of them require cloud delivery, standards-based integration, ML, or vendor content libraries. The modern embedded-EHR delivery is a dominant implementation, not the definition.

### L1 — Common Mature Structure

- **Workflow integration as the dominant delivery**: CDS lives at the EHR's decision moments — order entry, order signing, chart view, documentation, results review — either natively (embedded) or through standardized integration (CDS Hooks; info-buttons; app galleries).
- **Interruptive and non-interruptive presentation**: active formats that engage the clinician mid-task vs passive formats (linked references, informational panels); urgency indicators to rank severity.
- **Override and feedback machinery**: reason-coded override capture; feedback events (suggestion accepted / card ignored / guidance overridden) feeding tuning.
- **Alert-fatigue management as a structural concern**: monitoring of alert volume/acceptance, alert customization (edit/turn off/track/audit), community benchmarking, patient-specificity improvements to reduce low-value alerts.
- **Knowledge content lifecycle**: authored/vendor content → local customization → clinical review/consensus → deployment into the EHR → continuing vendor updates that preserve local customizations; knowledge packaged as units (modules, libraries, rule sets).
- **Clinical governance of content**: approved-rules repositories, multidisciplinary review, stakeholder consensus tooling.
- **Intervention families seen across the sample**: medication checking (DDI, allergy, dosing), order sets/protocols, care plans, diagnostic differentials, surveillance/risks with action lists, documentation guidance/templates, preventive-care reminders/registries, linked references.
- **Evidence traceability**: guidance linked to cited sources (guidelines, journals, publisher content); source attribution on advice.
- **Effectiveness analytics**: measurement of CDS impact and acceptance.

### L2 — Variant / Optional Structure

- **Delivery posture**: embedded EHR capability ↔ external engine integrated via standards ↔ knowledge-content vendor feeding EHRs ↔ standalone point-of-care tool (web/app) with optional EMR hookup.
- **Knowledge substrate**: deterministic rules / curated evidence content / machine-learned models / pharmacogenomic data — frequently mixed within one product.
- **Clinical domain scope**: medication, diagnostic, guideline/order-set, infection/sepsis surveillance, documentation, preventive care.
- **Audience**: clinician-facing (definitional); patient-facing siblings (self-triage, consumer medication guidance) as separate product lines.
- **Population→individual bridging**: registries/surveillance that identify at-risk patients and generate per-patient action lists straddle population health and point-of-care CDS.
- **Delivery/deployment**: cloud SaaS vs engine embedded in hospital infrastructure; open-source vs commercial.
- **Regulatory posture varies by jurisdiction and function**; specifics were not researched and are not asserted.

### L3 — Vendor-specific (research notes only)

- Zynx: AuthorSpace, ViewSpace, ZynxInside (MEDITECH-exclusive embedding), Knowledge Analyzer, ZEE; KLAS-award positioning; hospital counts and order-set counts.
- FDB: AlertSpace community benchmarking, MedKnowledge Explorer, OrderKnowledge (medication order strings), Infusion Knowledge, MedProof MCP (AI/agentic integration layer), Vela e-prescribing network; alert-reduction percentages.
- Isabel: 25,000+ autocomplete phrases claim, accuracy claims, "under 90 seconds" claim, availability of Epic info-button and Cerner App Gallery; the 11-question self-triage claim.
- MEDITECH: Surveillance and Patient Registries module structure, EHR Excellence Toolkits (CAUTI/diabetes/opioid stewardship), documentation-template counts.
- OpenCDS: vMR/DSS data model, Drools/Java rule languages, KnowledgeModule adapter pattern, Bitbucket/Confluence infrastructure.
- Epic / Oracle Health (Cerner) embedded CDS mechanics: not directly observed; only third-party references to info-button and app-gallery integration exist.

## Vendor-specific Findings

Summarized above under L3; none are promoted into the final document. Notably:

- Alert-customization mechanics (who may edit what, how changes are tracked) differ sharply: FDB packages alert governance as a community-benchmarked product; MEDITECH ships monitoring tools inside the EHR; CDS Hooks leaves governance to implementers. Only the *existence* of alert governance is common.
- Content-update mechanics differ: Zynx sells automated update tooling that preserves local customizations; OpenCDS treats knowledge as code; Isabel retrains/validates continuously. The common invariant is that clinical knowledge must keep changing while local adaptations survive.

## Boundary Findings

- **vs EHR**: the EHR is the record system of record; CDS is the advice layer operating on that record. Remove the advice machinery (rules, models, suggestions) and a product remains an EHR; remove the record and a product remains a CDS (Isabel works from entered features alone). In the market the two are entangled — MEDITECH ships CDS natively while licensing third-party content (Zynx, FDB, IMO, Elsevier, NCCN) into its workflows — but the *functions* are distinct and separately sold, which justifies the separate Type.
- **vs CPOE / Electronic Prescribing**: order entry and prescribing are workflow applications that *consume* CDS at their decision points; FDB's own positioning (improve "clinician acceptance of CPOE") shows CDS as a layer serving order entry, not the same object. Remove CDS evaluation from CPOE and order capture still works.
- **vs clinical reference content** (e.g., the publisher knowledge Isabel partners with — DynaMed, BMJ Best Practice): reference is generic and not bound to a patient; CDS binds knowledge to an identified patient and a decision moment. The same knowledge base feeds both; the binding is what makes it CDS.
- **vs Medical Image Analysis Platform**: image analysis computes findings/measurements from image data (modality-specific); CDS applies clinical knowledge to a patient's overall context to advise on decisions. An image-analysis finding can *input* to CDS. Different source object and different function.
- **vs Population Health Management**: population health manages cohorts; CDS advises a clinician about an identified patient at a care moment. MEDITECH's registries/surveillance straddle the seam (population identification → per-patient action lists at the point of care); the per-patient advisory delivery is the CDS half.
- **vs Care Plan Management**: care plans can be (a) CDS content delivered as evidence-based guidance at the point of care (ZynxCare) or (b) the managed per-patient record object of a care-planning system. Same noun, different object.
- **vs patient-facing symptom checkers / triage**: when the recipient of the advice is the patient (Isabel Self-Triage), the decision-maker and liability surface change; the machinery is shared, but the Type boundary is the clinician as the advised decision-maker.
- **What would turn this Type into another**: remove patient-specificity → clinical reference; remove decision-point delivery → analytics/reporting; remove clinician-in-the-loop → autonomous clinical execution (not a current Atlas leaf); remove the advisory character and keep only record-keeping → EHR.

## Uncertainties

- Actual adoption distribution between embedded-EHR CDS and standards-integrated external services (CDS Hooks is STU; OpenCDS supports it; MEDITECH embeds content natively). No adoption claims are made.
- Override-rate figures, alert-volume figures, accuracy percentages: only vendor claims encountered; none asserted.
- Internal mechanics of Epic / Oracle Health CDS (the two largest EHRs): not directly observed; anything EHR-internal is written at the level of the sample's evidence only.
- Regulatory classification of CDS functions (device vs non-device) by jurisdiction: not researched; excluded from both documents.
- Whether FDB "CDS Analytics" is a standalone product or a module: product-specific detail; kept out of the final document.

## Final Synthesis

A Clinical Decision Support System is best understood as an **advice engine wired into clinical work**: it takes an identified patient's situation, applies curated clinical knowledge or learned models to it, and returns person-specific advice at the moment a clinician is about to decide — an alert at order signing, an order set in the ordering flow, a differential during diagnosis, an action list on a surveillance board. The clinician accepts, rejects, or overrides, and those responses feed the continuous governance of the content: alert tuning, evidence updates, local customization.

The market delivers this one function through four commercially distinct postures — as an embedded EHR capability, as an external standards-integrated engine, as licensed evidence-based content deployed into EHRs, and as standalone point-of-care tools — all sharing the same core anatomy. The defining structure is deliberately small: patient context, knowledge evaluation, advisory delivery at a decision point, clinician-as-decider.
