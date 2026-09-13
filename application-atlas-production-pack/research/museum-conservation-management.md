# Research Notes — Museum Conservation Management

## Research Goal

Understand what "Museum Conservation Management" software actually is and how it works: the system museums (and conservators serving them) use to manage and document conservation work — examinations, treatment proposals, authorizations, treatments, preventive care — on collection objects. Produce a vendor-neutral canonical model, hold the boundary against the already-processed siblings (especially museum-condition-reporting, whose pass left explicit counterpart guidance for this leaf), and check the definition against the domain standard and older/paper-based practice.

## Initial Boundary

Working hypothesis at start:

- This is the museum conservator's work-management system of record: it manages **care and treatment work** done to objects, not just descriptions of objects.
- Closest sibling: **Museum Condition Reporting** (documents physical state, not treatment). Prior pass explicitly routed the seam here: split at standard level (two separate Spectrum procedures), field level (condition group vs proposed/completed treatment groups on one tab in eHive), packaging level (TMS's two products), with the pre-treatment baseline condition report as the standing interlock. This pass adopts or adjusts that seam from its side.
- Container sibling: **Museum Collections Management** — hosts condition & conservation as one custody-lifecycle event family on the object record; this leaf owns the workflow's internal structure (keep-both-with-containment precedent from the accession-cataloging and condition passes).
- Name-collision neighbor: **Conservation Management** (§21) — nature/landscape/species conservation. Entirely different domain; not a boundary risk in practice but worth an explicit note.
- Also adjacent: Museum Object Movement Management (objects move to/from conservation), Museum Loan Management (loans prompt treatment), CMMS (industrial maintenance work orders — family resemblance, different subject world).

## Research Questions

1. What is the unit of record — is there a "conservation work record" distinct from the object record and from condition records?
2. What lifecycle does conservation work pass through? (examination → proposal → authorization → treatment → outcome → follow-up?)
3. What does a treatment record contain (method, materials, dates, result, report, images)?
4. How does the workflow interlock with condition checking, movement, loans, exhibitions?
5. How is conservation work planned and scheduled (priorities, recall dates, periodic care)?
6. Who uses it — in-house conservators, external contractors, registrars, curators?
7. How is the workflow packaged (field groups vs module vs standalone studio vs private-practice tool)?
8. Does the definition survive the paper-era realization (§24 historical check)?

## Representative Products

Selected for market representativeness, documentation reachability, different product philosophies, and different customer tiers:

| Product | Vendor | Philosophy / tier | Why sampled |
|---|---|---|---|
| TMS Conservation Studio | Gallery Systems | Dedicated conservation-documentation studio, conservator-facing, enterprise | The dedicated pole; the other half of the TMS two-product packaging used in the sibling's seam |
| MuseumPlus | zetcom | Enterprise museum suite with Conservation as a core module | The suite-module pole; Spectrum 5 compliant per the Collections Trust directory |
| eHive | Vernon Systems | Mid-market SaaS collection system; conservation as field groups on the object record | The light pole; only sample with public field-level documentation |
| CatalogIt Conservator | It Unlimited | Small-tier SaaS for conservators in private practice | The private-practice pole: many clients, many projects, deliverables |
| Spectrum (Collections Trust) | — | Domain standard (not a product) | The UK museum collections-management standard used internationally; defines the "Collections care and conservation" procedure; medium-agnostic |

Considered and not sampled: Axiell Collections (unreachable in all prior sibling passes; not retried per network rules), Vernon CMS desktop (unreachable in prior passes), PastPerfect (unreachable in prior passes), Articheck (sampled by the condition-reporting sibling as its standalone pole — boundary anchor only here).

## Sources

Tier 1 (official operational / standard documentation):

- Collections Trust — Spectrum 5.1, "Collections care and conservation" procedure page — https://collectionstrust.org.uk/spectrum/procedures/collections-care-and-conservation-spectrum-5-0/
- Collections Trust — "Collections care and conservation – the Spectrum standard" (policy questions + minimum requirements) — https://collectionstrust.org.uk/resource/collections-care-and-conservation-the-spectrum-standard/
- Collections Trust — "Collections care and conservation – suggested procedure" (step-by-step + guidance notes) — https://collectionstrust.org.uk/resource/collections-care-and-conservation-suggested-procedure/
- eHive Help Center — "Conservation fields for object records" — https://help.ehive.com/conservation-fields.htm

Tier 2 (official product pages / vendor-validated directory listings):

- Collections Trust software directory — MuseumPlus entry (module list, Spectrum procedure list, compliance) — https://collectionstrust.org.uk/software/museumplus/
- Collections Trust software directory — eHive entry (Spectrum procedure list) — https://collectionstrust.org.uk/software/ehive/
- Gallery Systems — Conservation Documentation (TMS Conservation Studio) product page — https://www.gallerysystems.com/solutions/conservation-documentation/
- zetcom — MuseumPlus product page — https://www.zetcom.com/en/museumplus-en/
- CatalogIt — Conservator plan page — https://catalogit.app/products/conservator

Tier 3 (vendor editorial, used for framing only):

- Gallery Systems blog — "Operational Excellence for Conservation Teams: Rethinking How Museums Manage Conservation Work" — https://www.gallerysystems.com/conservation-management-for-museums-operational-excellence/

Research date: 2026-09-08.

## Product / Standard Observations

### Spectrum 5.1 — "Collections care and conservation" (domain standard; evidence layer A for the practice, not for any product)

Procedure definition (verbatim scope): "Managing and documenting any conservation work on particular objects, such as treatments to slow decay, repair damage or improve appearance."

Scope notes: conservation interventions usually result from condition checks; often prompted by other procedures (e.g., managing a loan request); treatments often informed by scientific analysis and technical assessments; conservation records "should form a seamless part of your collections documentation, even if the work itself is carried out by external specialists away from your museum." Spectrum is explicitly not software and allows paper-based systems.

Minimum requirements (the standard) — four, each with stated rationale:

1. "Appropriate authorisation is given for any decision to change an object's standard of care or carry out any conservation treatment." — "No conservation work happens without the knowledge of those responsible for the objects."
2. "You record the details of all collections care measures and conservation treatment (including dates and who performed the work) and can access these via relevant object numbers." — "You have a full conservation history of your objects, and can find this information easily when you need it. If a problem later arises, you can check other objects that might also be affected."
3. "You update objects' catalogue records with any new information gained as a result of conservation." — "New insights about how objects were made are not just kept in conservation files that might not be generally accessible."
4. "You schedule, where necessary, any further conservation treatment, call-back condition checks or periodic care activities." — "You can plan your conservation activity and ensure that objects are available when needed."

Suggested procedure (steps):

- **Agreeing conservation work**: scope from prior condition assessments/recommendations, or the conservator performs a condition check with treatment recommendations on first receiving objects; reach **written agreement** (owner consent when objects are not yours, e.g. proposed treatment on a borrowed loan; formal external agreement containing assessment + recommendations, timetable, conservator details, authority, terms, transport/handling/security/insurance/access arrangements); file it and note its document location in the relevant object records.
- **Provide the conservator object information**: object number (or entry/loan number for items not owned), description, materials, location, technical descriptions and condition assessments, **previous conservation history**, recommended treatment, reason for conservation, requester, request date, completion date, hazards/risk assessments.
- **Record information about the work before it is carried out**: object number(s); a **Conservation reference number** (standard format); conservator name/contact; **Conservation authoriser** + **Conservation authorisation date**; **Conservation method** (standard term source).
- **Carrying out**: move objects via Location and movement control (or Object exit first, for work at an external conservator); carry out the agreed work.
- **Recording conservation work**: as soon as possible record **Treatment begin date** and **Treatment end date** and the **Treatment report**, containing: type of work (conservation treatment, preventive measures, condition report, loan condition report); the action carried out (location, procedure, method, **materials used**, duration, **result**); reference numbers of reports/photographs/drawings/X-radiographs/other images; new or revised handling/packing/storage/display recommendations; packing/support instructions; updates to the care and maintenance plan; **call-back date (Recall date)** for follow-up or evaluation; details of any new or reproduction parts fitted.
- **Add relevant information from the conservation record to the documentation system**: external contractor returns a copy of everything recorded; file it and note document location in object records; transfer key information (hazard notes, handling recommendations) to the object records so it is immediately available; in-house work can go directly into the collection management system.
- **Check objects on agreed recall dates**: examine on recall dates and record condition (longer-term success check).
- Guidance note 1 — levels of recording vary by event type: disaster recovery, emergency minor treatment, mass/bulk treatment, preventive conservation measures, housekeeping activities (e.g., dusting objects on open display); emergency records completed in full when conditions allow.
- Guidance note 2 — record evidence that might be lost during treatment (e.g., sampling prior to treatment; heat treatment of metals; removal of soil from archaeological objects).

### eHive (Vernon Systems) — evidence layer A (field-level official help) + Tier 2 directory

- Help Center, "Conservation fields for object records": "You can record information about an object's condition, risk, handling, **proposed treatment**, and **completed treatment** on the **Conservation tab** of the object cataloguing page."
- Four field groups on one tab:
  - **Condition**: condition date, condition keyword, condition notes, condition part (part reference/aspect), condition person.
  - **Risk and handling**: risk assessed by, risk assessment, risk assessment date, risk assessment notes, risk factor, handling details.
  - **Proposed treatment**: **conservation priority**, proposed treatment description, proposed treatment date, proposed treatment keyword, proposed treatment notes, proposed treatment part reference, proposed treatment person.
  - **Completed treatment**: completed treatment date, completed treatment keyword, completed treatment notes, completed treatment part reference, completed treatment person.
- Field-level evidence for: object-record anchoring; attribution (person/date on every group); the **proposed vs completed treatment split on the same record**; **conservation priority** as a recorded rating; part references (where on the object).
- Collections Trust directory entry: Spectrum procedures supported include "Condition checking and technical assessment" and "**Collections care and conservation**" (listed as non-primary; the primary procedures are the custody spine). Directory also confirms positioning (web-based collection cataloguing, SMB pricing) and that detailed help is public.

### TMS Conservation Studio (Gallery Systems) — evidence layer A for product claims at feature level (official product page) + Tier 3 editorial

- Product page: "Developed for museum conservators by conservators, TMS Conservation Studio is an easy-to-understand **museum conservation documentation software** that consolidates and supports every aspect of day-to-day activities."
- Documented capabilities: real-time tablet-friendly documentation; "design custom reports for fast **condition, damage, and treatment** reporting"; integrated Thesaurus Manager (vocabulary control); photograph objects and "note areas of damage or concern using annotation tools"; customizable data input fields; "immediate record syncing with TMS Collections"; "linking records for outgoing objects to their upcoming exhibitions or loans"; "keep all your conservation documentation in a single searchable location"; granular security "to safeguard your conservation data until it's ready for sharing."
- Frick Collection conservator testimonial (product page): the link between the collection system and Conservation Studio mattered because they "didn't want to have to go into a separate system to access object data."
- Vendor editorial (Tier 3, framing only): museums "still rely on a patchwork of tools such as paper reports and spreadsheets to track conservation work"; conservators' activities include assessing for exhibitions/loans, condition surveys, documenting treatments and scientific analysis, "tracking long-term conservation histories for objects"; shifts described: centralized digital documentation; structured documentation with configurable templates ("condition reports, treatment proposals, and surveys"); integration with collections management ("conservation reporting, **project tracking**, and media documentation within the same ecosystem"); per-component treatment tracking for composite/multi-part objects; before/during/after treatment images with annotation; cross-department sharing (curators review reports when planning exhibitions; registrars rely on conservation documentation for loan agreements); web/mobile access from lab, storage, gallery.

### MuseumPlus (zetcom) — evidence layer A at module/positioning level (vendor-validated directory entry) + Tier 2 product page

- Collections Trust directory entry (vendor-supplied): standard module list includes **Conservation** (listed among core modules, appears twice in the vendor's own list — alongside Objects/Collections, Location Management, Exhibitions, Registrar, Contracts, Transport, Values and Transaction History, etc.). Spectrum 5 compliant. Spectrum procedures supported include "Condition checking and technical assessment" and "**Collections care and conservation**".
- Directory entry also documents: add-on connectors to third-party products including **Articheck** (the standalone condition-reporting product sampled by the sibling pass) — packaging-level evidence that condition documentation can be externalized and integrated.
- Product page: modules listed are Collection Management, Customer Service, Digital Assets, Contracts, Exhibition Management + "additional modules"; no conservation-specific detail is publicly documented. Operational documentation is login-gated — the internal structure of the Conservation module (fields, workflow states) is NOT observable this pass.

### CatalogIt Conservator (It Unlimited) — evidence layer A at feature level (official plan page)

- Positioning: a plan of a small-institution/collector collection app aimed at **conservators in private practice**.
- "Track Condition and Conservation": "Document and update condition and conservation history. Capture every step of the conservation process — **before, during, and after treatment** — attaching photos and documents along the way. Track the movement of objects between clients and the conservation lab."
- "Manage Your Projects": "Stay on top of **multiple conservation projects** at once with intuitive workflow features... organizing records by project, tracking condition details and the conservation process, and delivering summaries to clients."
- Key features: "Track condition and conservation over time... before-, during- and after treatments. Use **repeating fields** to show every stage of the process"; "Monitor the movement of objects between clients and the conservation lab — track precise locations"; "Generate condition and conservation reports for clients and your own records"; "**Deliver condition summaries and conservation plans to clients**"; project profiles/folders/tags; collaborators with user permissions; insurance reporting.
- This is the private-practice realization: many clients × many objects × many projects, client-facing deliverables, and object movement into/out of the conservation lab — same work record structure, different institutional posture (the conservator holds the record rather than the museum).

## Cross-product Comparison

| Structure | Spectrum (standard) | eHive | TMS Conservation Studio | MuseumPlus | CatalogIt Conservator |
|---|---|---|---|---|---|
| Object-number anchoring of conservation records | minimum req. 2 ("access these via relevant object numbers") | conservation tab on the object cataloguing record | record syncing with the collection system; object data alongside conservation data | Conservation module within an object-centric suite; Spectrum-supported | conservation history on entries |
| Attribution (who/when) on work records | minimum req. 2 (dates + who performed); authoriser + authorisation date; treatment begin/end dates | person + date fields on every conservation group | reports carry author/date (report generation) | module presence + Spectrum support only (docs gated) | reports for clients and own records |
| Proposed-then-completed structure | procedure: record before carried out (ref no., authoriser, method) → treatment report after (begin/end, result) | **separate proposed-treatment and completed-treatment field groups** + conservation priority | condition/damage/**treatment** reporting; vendor editorial names "treatment proposals" | module presence only | conservation **plans** delivered to clients; before/during/after stages via repeating fields |
| Method / materials / result recorded | treatment report: location, procedure, method, materials used, duration, result | treatment keyword/notes/description | customizable fields; vocabulary control (Thesaurus Manager) | module presence only | materials/techniques documented on entries |
| Accumulated care history per object | minimum req. 2 ("full conservation history") | fields accumulate on the object record | "track long-term conservation histories"; single searchable location | module presence only | "condition and conservation history"; repeating fields per stage |
| Write-back to object record | minimum req. 3 (update catalogue records) | hazard/handling group on the object record | sync with collection system | module presence only | movement/insurance info on entries |
| Planned follow-up | minimum req. 4 (recall dates, further treatment, periodic care) | conservation priority (indicative) | editorial: project tracking | module presence only | multiple concurrent projects |
| Condition interlock | interventions usually result from condition checks; assessment forms basis of agreement | condition + risk groups adjacent to treatment groups on the same tab | condition/damage/treatment reports in one studio | both Spectrum procedures supported | condition tracked alongside conservation |
| Preventive care / housekeeping in scope | explicit (preventive measures, housekeeping as event types) | not documented | not documented at page level | module presence only | not documented |

Reading of the comparison:

- The **proposed-vs-completed split** appears at standard level (procedure stages), field level (eHive), feature level (TMS treatment reports vs proposals), and practice level (CatalogIt plans → treatment stages). Cross-product commonality, layer B.
- **Object-number anchoring** is the standard's own requirement and is how every sampled product binds conservation information (field group on object record, sync with object data, or entry-level history). Layer B.
- **Authorization** is standard-level (minimum requirement 1 + authoriser fields in the suggested procedure) but not observable as named machinery in eHive/CatalogIt — held as standard requirement + common practice, not field-level canonical.
- **Recall-date scheduling** is standard-level; no sampled product page documents scheduling machinery explicitly. Not asserted as product structure.
- **Priority rating** appears in eHive (field) and Spectrum (treatment priority recommendations); TMS/CatalogIt not explicit. Layer B-lite (standard + one product) — keep as common capability.
- Packaging varies on a spectrum: field groups on the object record (eHive) ↔ core module of a suite (MuseumPlus) ↔ dedicated studio synced to the collection system (TMS Conservation Studio) ↔ private-practice project posture (CatalogIt Conservator). No packaging is definitional.

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

Museum Conservation Management is the museum's conservation-work system of record. Three structures, jointly held:

1. **The object-bound conservation work record.** Every item of care or treatment work — proposed or performed — is held as a record bound to the identified collection object (findable through the object number), attributed (who performs/authorizes, when), and carrying the reason for the work. Remove → descriptive cataloguing with conservation notes (documentation of objects, not of work) or a generic task board.
2. **The proposal-to-outcome progression of care work.** Work exists as a proposal before it exists as an intervention: scope, priority, and reason recorded and agreed/authorized under the institution's policy (owner consent when the object is not owned), then executed and recorded as completed work with its method, materials, dates, and result, with the treatment report as the record's deliverable. Remove → a bare log of care actions with no managed intent, or the condition-reporting sibling (assessment without intervention).
3. **The accumulated care history that feeds back.** Conservation records accumulate per object and stay referable (the full conservation history); key outcomes are written back to the object record (handling/packing/storage/display recommendations, hazards, new information about how the object was made); and further care is planned (recall dates, further treatment, periodic care). Remove → episodic treatment paperwork; institutional memory and the "management" collapse.

Jointly-held load-bearing: 1+2 without 3 = per-episode paperwork with no institutional memory or planned follow-up; 1+3 without 2 = a dated care log (the container's event layer without the workflow); 2+3 without 1 = generic work/approval machinery detached from objects.

### L1 — Common Mature Structure (not definitional)

- Pre-treatment baseline condition report (the standing interlock with condition reporting; the standard makes assessments/recommendations the basis of the proposal).
- Conservation priority ratings driving what gets treated.
- Treatment report as a generated/formatted document deliverable (for the file, for owners, for clients).
- Before/during/after treatment photography and image annotation of damage/treatment areas.
- Controlled terminology for methods/materials (standard term sources, thesauri).
- Per-component treatment tracking for composite/multi-part objects.
- Hazard notes and handling recommendations written back to object records.
- External-conservator contracting support (agreement contents, transport/handling/security/insurance/access arrangements, document-location references filed on object records).
- Consolidated searchable conservation documentation across the institution.
- Work/project tracking across many concurrent treatments; deliverables to external parties (owners, clients, insurers).

### L2 — Variant / Optional Structure

- Packaging: field groups on the object record (light SaaS) ↔ suite module ↔ dedicated studio synced to the collection system ↔ private-practice posture (the conservator holds the records and serves multiple clients).
- Scope of "care": interventive treatment vs preventive conservation measures vs housekeeping programs vs emergency/disaster treatment vs mass/bulk treatment (the standard names all as event types with differing recording depth).
- In-house vs external (contracted) conservators; owner-consent flows for borrowed objects.
- Integration with standalone condition-reporting products via connectors.
- Scientific/technical analysis records alongside treatment records (standard notes analysis informs treatment; product-level structure unverified).

### L3 — Vendor-specific (research notes only)

- TMS Conservation Studio: brochure-level modules, tablet annotation workflow, Thesaurus Manager, "immediate record syncing with TMS Collections," granular security until ready for sharing, outgoing-object links to exhibitions/loans, "Operational Excellence" editorial framing.
- MuseumPlus: Conservation appearing twice in the vendor's own module list; Groovy-script workflow integration; Articheck/Ortelia/PicturePark connectors; CT-directory pricing/user counts (£90/user/month SaaS etc. — not reproduced in the final document).
- eHive: exact field names (Condition keyword, Risk factor, Proposed treatment part reference, ...), Silver-plan permissions gating, communities/API features.
- CatalogIt: project profiles/folders/tags, HUB web publishing, insurance reporting, migration tooling, storage-tier pricing.

## Vendor-specific Findings

- TMS positions conservation documentation as a **separate product** from its collection system (two-product packaging) with record syncing — the strongest packaging evidence for the documentation-suite pole.
- MuseumPlus embeds conservation as a **core module** of the suite (single-system pole).
- eHive implements the workflow as **field groups** on the object record (lightest pole) — proof the Type does not require a dedicated module.
- CatalogIt implements the workflow as a **practice-management posture** (projects, clients, deliverables) — proof the Type does not require museum-side institutional embedding.
- Only eHive exposes field-level semantics publicly; only TMS exposes a dedicated conservation product page; only CatalogIt exposes the private-practice framing. No single vendor's structure is generalized.

## Boundary Findings

- **vs Museum Condition Reporting** (load-bearing; adopted from the sibling's counterpart guidance): condition reporting documents **state** (dated, attributed, reason-coded assessment of the object's physical condition, retained as comparable history); conservation management manages **intervention** (proposed and performed care/treatment work, its authorization, execution, outcome, and follow-up). The seam holds at three observed levels: standard (Spectrum 5.1 keeps "Condition checking and technical assessment" and "Collections care and conservation" as two separate procedures), field (eHive: condition group vs proposed/completed treatment groups on one Conservation tab), packaging (TMS ships two products; MuseumPlus lists both Spectrum procedures; a standalone condition product connects into a conservation-capable suite via a connector). Standing interlocks: the pre-treatment baseline condition report; condition findings and treatment priority feed proposals; recall dates call back to condition checks; a condition finding that differs from the prior record escalates to conservation. Remove the intervention/proposal structure from this leaf and it collapses into its sibling; remove the assessment structure from the sibling and it collapses into this leaf.
- **vs Museum Collections Management** (container): the collection system of record hosts condition & conservation as one custody-lifecycle event family on the object record; this leaf owns the workflow's internal structure (proposal → treatment → outcome → follow-up). Keep-both-with-containment, consistent with the accession-cataloging and condition passes.
- **vs Museum Object Movement Management**: objects move to/from conservation through location and movement control (and object exit for external conservators); this leaf records the work, not the location. Spectrum's own procedure cross-references both.
- **vs Museum Loan Management**: loans prompt treatment (e.g., borrowed objects requiring consent for treatment) and condition documentation; the loan owns the transaction, this leaf owns the work.
- **vs CMMS / Equipment Maintenance**: family resemblance (work orders, schedules, maintenance history) but a different subject world — unique, irreplaceable collection objects rather than serviceable equipment; documentation-first practice where the treatment report permanently records new knowledge about the object (minimum requirement 3) and materials/methods are recorded under controlled vocabulary for future conservation; no failure/preventive-maintenance asset machinery as core.
- **vs Conservation Management (§21)**: name-collision neighbor — protection of natural areas/species; no collection objects, no treatment records. Explicitly different Type.
- **vs Cultural Heritage Asset Management**: place-based heritage registry (monuments/buildings/sites) vs object-level treatment workflow. Different unit of record.
- **vs Building Condition Assessment**: assessment-documentation shape applied to buildings; no treatment workflow, no collection-object identity.

### §24 Historical / Market-Sample Check

Paper-era conservation studio: examination notes and recommendations from a condition card; a written treatment proposal agreed with the curator or owner; an authoriser's signature; a treatment card/report filed by object number carrying a reference number, method, materials, dates, and result; before/after photographs and sketches; recall notes in the diary or location book; new information passed to the catalogue cards. This satisfies all three L0 legs. Spectrum itself is medium-agnostic ("Spectrum is not software (and can be used with paper-based systems)"). The definition names no software surface, cloud delivery, templates, annotation tools, tablets, sync, or thesauri — all are era machinery or standard capabilities. Historical check passed.

## Uncertainties

- MuseumPlus operational documentation is login-gated; the internal structure of its Conservation module (fields, states) is not observable. Held at module-existence + Spectrum-procedure-support level only. (Consistent with sibling passes.)
- TMS Conservation Studio operational help is login-gated; evidence is feature-level from the product page plus vendor editorial. No screen-level claims made.
- Whether recall-date/periodic-care scheduling exists as first-class machinery in products (vs only in the standard) is unverified at product level; kept at standard level.
- Time/cost tracking of conservation work: not evidenced in the reachable sample; not asserted.
- Preventive-care programs (integrated pest management, environmental monitoring) as in-product workflows: in scope per the standard's event types, but no in-sample product evidence; held as variant/conceptual.
- Axiell Collections, Vernon CMS desktop, PastPerfect unreachable (consistent with all prior sibling passes; not retried per network rules). Mid-market coverage rests on eHive's public documentation.
- The private-practice pole is evidenced by one product (CatalogIt Conservator) plus the standard's external-conservator procedure; variants of that posture (shared labs, regional conservation centers) not separately sampled.

## Final Synthesis

Museum Conservation Management is the conservation-work system of record: it holds every proposed and performed item of care or treatment as a record bound to the identified object, moves that work through proposal → agreement/authorization → treatment → recorded outcome, and retains the object's full conservation history while feeding outcomes back to the object record and scheduling further care. Its defining core is the work record, the proposal-to-outcome progression, and the accumulating, feedback-giving care history — jointly held. Everything else (templates, photography depth, thesauri, priority ratings, external contracting, packaging form) is standard capability or variant. The load-bearing boundary is with Museum Condition Reporting (state assessment vs treatment intervention), adopted from the sibling's counterpart guidance and confirmed at standard, field, and packaging levels. Historical check passed at paper level.
