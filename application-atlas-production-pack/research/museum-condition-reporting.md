# Research Notes — Museum Condition Reporting

Slug: `museum-condition-reporting`
Research date: 2026-09-08
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what "condition reporting" software actually is in the museum/collection-care world: what a condition report is as a record, who produces them, when they are produced, how they attach to objects, how products structure them, and where the Type's boundaries run — especially against Museum Conservation Management (treatment), Museum Collections Management (the container), and the exhibition/loan siblings that consume condition documentation at handover moments.

## Initial Boundary (pre-research hypothesis)

- Core use: documenting the physical condition of collection objects at defined moments, as dated, attributed, object-bound records, retained so change over time is detectable and custody responsibility can be evidenced at handovers.
- Users: conservators, registrars, collections managers, couriers/art handlers, exhibition staff.
- Nearest neighbors: Museum Conservation Management (treatment — the biggest confusion risk), Museum Collections Management (container), Museum Loan Management (trigger + consumer), Exhibition Installation Management / Artwork Exhibition Logistics (consumers at handover), Provenance Research Platform (different content: ownership history, not physical state).
- Prior-pass context: museum-collections-management (processed 2026-09-08) hosts this leaf as one custody-lifecycle event family ("care") and defers the workflow's internal structure to this pass; exhibition-installation-management (processed 2026-09-07) treats condition documentation as "institutional norm, not definitional" for install and defers the standalone discipline here; artwork-exhibition-logistics (processed 2026-09-06) noted Articheck as a dedicated condition/transit documentation point tool.
- Unknowns: do standalone dedicated products exist beyond Articheck; what structure do condition records have at field level; is the trigger structure definitional or common; is the comparable-history leg load-bearing.

## Research Questions

1. What is a condition report as a record — what does it contain, and in what forms (free text, ratings, controlled vocabularies, annotated images, templates)?
2. What triggers condition reports — which custody/handling moments, and is the trigger structure part of the product or institutional practice?
3. How do condition records attach to object identity, and how are prior reports referred to (comparable history)?
4. Who authors condition reports (roles, expertise tiers), and how are they shared with external parties (lenders, couriers, partners)?
5. Where exactly does condition documentation end and conservation treatment documentation begin — in standards, in products, in packaging?
6. Do standalone dedicated condition-reporting products exist, and how do they differ from CMS modules?
7. What outputs does the workflow produce beyond the record (recommendations, treatment priorities, next-check scheduling, report documents)?
8. Historical check: does the paper-era form (condition report cards/forms filed by object number) satisfy the minimal core?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| **Articheck** | dedicated standalone condition-reporting SaaS (galleries, museums, conservators, shippers) | the reachable market's purpose-built pole; different philosophy (condition documentation as the product itself, cross-party sharing) |
| **TMS Collections / TMS Conservation Studio** (Gallery Systems) | enterprise incumbent; condition reporting as CMS module + conservation-suite companion | the dominant museum CMS; Spectrum-compliance list is public via the Collections Trust directory |
| **CatalogIt** | small-institution SaaS CMS + a dedicated Conservator plan | SMB pole; condition tracked on entries; conservator plan makes condition the anchor workflow |
| **eHive** (Vernon Systems) | mid-market cloud CMS with public field-level documentation | the only sampled product with fully public field-level docs — condition record structure verifiable at field level |
| **Spectrum** (Collections Trust) | domain standard (not a product) | the normative statement of the procedure family; used as the structural anchor, as in the sibling passes |

MuseumPlus considered and dropped for this leaf: product page names no condition module, operational docs login-gated (consistent with sibling passes); Axiell / Vernon CMS desktop / Lucidea / PastPerfect unreachable in prior passes — not retried beyond the recorded limits.

## Sources

All fetched 2026-09-08 unless noted.

**Domain standard (Tier 1):**
- Collections Trust — Spectrum procedures list: https://collectionstrust.org.uk/spectrum/procedures/
- Spectrum — Condition checking and technical assessment (procedure page): https://collectionstrust.org.uk/spectrum/procedures/condition-checking-spectrum-5-0/
- Spectrum — Condition checking and technical assessment, the standard (minimum requirements): https://collectionstrust.org.uk/resource/condition-checking-and-technical-assessment-the-spectrum-standard/
- Spectrum — Condition checking and technical assessment, suggested procedure: https://collectionstrust.org.uk/resource/condition-checking-and-technical-assessment-suggested-procedure/

**Articheck (Tier 1/2):**
- https://www.articheck.com/ (homepage: positioning, testimonials, FAQ)
- https://www.articheck.com/risk-management/art-condition-reports/ (Condition Reporting product page: features)

**Gallery Systems (Tier 2):**
- https://www.gallerysystems.com/solutions/collections-management/ (TMS Collections)
- https://www.gallerysystems.com/solutions/conservation-documentation/ (TMS Conservation Studio)
- Collections Trust software directory entry "TMS Collections and eMuseum": https://collectionstrust.org.uk/software/tms/ (Spectrum procedures supported; suite composition)

**CatalogIt (Tier 1/2):**
- https://www.catalogit.app/ (homepage: condition tracked on entries; plan structure)
- https://www.catalogit.app/products/conservator (Conservator plan: condition/conservation tracking features)
- https://support.catalogit.app/en_US/museum-features and /en_US/museum-features/generating-forms (forms list; condition as object-record data verified in loan workflow)

**eHive (Tier 1 — field-level operational docs):**
- https://help.ehive.com/ (help home)
- https://help.ehive.com/conservation-fields.htm (Conservation tab: Condition / Risk & handling / Proposed treatment / Completed treatment field groups)
- https://help.ehive.com/field-help/object/condition-keyword.htm (overall-condition picklist)
- https://help.ehive.com/field-help/object/condition-notes.htm (damage vocabulary; Te Papa template source)

**Unreachable / limited (recorded per source-access rules):**
- Zetcom MuseumPlus: product page fetched (no condition module named); public docs site covers only the Web Service API; operational docs login-gated. eHive main site returned an empty response once (help site reachable); help.ehive.com/field-help/conservation-fields.htm 404'd once before the correct path was fetched.
- Gallery Systems detailed help (community.gallerysystems.com) login-gated (consistent with sibling passes).
- CollectiveAccess not sampled this pass (manual only partially reachable in prior passes; condition machinery likely user-configured — unverified, recorded as uncertainty).

## Product Observations

### Spectrum — Condition checking and technical assessment (standard; evidence layer A for the domain's normative structure)

- Procedure definition: "Documenting the make-up and condition of objects, and noting any resulting recommendations."
- Scope: "There are many situations where you might do this, so you will often use this procedure together with others." Checks may include technical assessments (scientific tests on material samples). "Condition checks also inform recommendations for treating, storing and using objects. Over time, the resulting records provide an audit trail of changes to objects."
- It is a **further procedure** (not one of the 9 primary procedures), listed separately from "Collections care and conservation" — the standard itself splits assessment from treatment.
- Minimum requirements (the standard): monitor and record condition per policy schedule ("build up information over time"); staff know when a check is needed as part of another procedure; **check condition at points of risk (e.g. before and after moving objects)** — "well-documented evidence should any problem arise over alleged damage"; schedule checks after significant change to use or environment; **all condition checks documented and accessible via the relevant object numbers**; **record the date, name of the condition checker and the reason for checking** ("you can audit condition checks"); staff know what to do when they have concerns.
- Suggested procedure (workflow): (1) **Requesting** — "usually prompted by another Spectrum procedure"; sample-check when many objects involved. (2) **Preparation** — good light; materials/equipment; quarantine area if infested/hazardous; movement handled under Location and movement control. (3) **Carrying out** — policy defines who is authorized and when professional conservators are needed; **refer to previous condition checks** and hazard notes/handling recommendations; **photographs highly desirable (may be required by lenders, insurers or indemnifiers)**; sketches/diagrams for areas of loss or damage. (4) **Recording the check event** — object number(s); condition check reference number; date; checker name (standard form); method (standard term source); reason (standard term source); note. (5) **Recording the result** — may live on an entry record, catalogue record, or a separate record; may be duplicated as an **'object passport'** to travel with the object; depth varies by procedure — "a brief comment (e.g. fair, cracked lid) when an object enters" vs "a full technical assessment carried out by a conservator… The condition of the object should be recorded **before any treatment takes place**." Result fields: completeness; condition (term + date + note); technical assessment; conservation treatment priority; environmental condition note; hazard; **next condition check/assessment date**; object requirement information (display / environmental / handling / packing / special / storage recommendations); recall date after conservation. (6) **Responding** — update object records with recommendations; **if condition gives cause for concern or differs from previous checks → conservator (Collections care and conservation)**; otherwise return to the prompting procedure.
- Note 1 — three levels of checking: (a) condition check by potentially any staff member/volunteer (arrivals, loans, potential acquisitions); (b) condition report by staff with conservation skills or a professional conservator (objects going on loan; before treatments involving tools or chemicals); (c) full condition report by a professional conservator before major conservation treatment.

### Articheck (dedicated standalone; evidence layer A)

- Positioning: "Easy to use condition reports and complete visibility of art in situ, transit, and storage — help our customers avoid disputes, reduce liability, and protect artwork." Risk-management framing: "Proof of due care & diligence — establish a legally verifiable audit trail for your objects."
- Condition Reporting product page: "Create, store, and reference detailed multimedia condition reports, allowing you to document condition history and move art securely while minimising risk."
- Features: **Guided templates** ("Choose your template – from painting to paper, basic to detailed"; optional sections such as Packing Requirements and Treatment Proposals); **Annotations** ("Annotate images with industry-standard symbols, attach detail images and notes directly to annotations"); **Notes & comments**; **Condition history**; **Video reporting**; **Secure sharing** ("Share a report as read-only, give editing and sharing capabilities, or revoke access at any time" — "for example when collaborating with partners on loans or travelling exhibitions").
- Transit: Transit Hub product line; transit checks (vehicle unloading, airside) — condition documentation attached to shipment moments.
- Audience breadth: solutions pages for Galleries, Museums, Conservators, Shippers; testimonials from registrars, collections managers, conservation managers (e.g. MOTAT: "Even a basic condition report, done thoroughly, takes up a great deal of time and we wanted something that would help automate the process of reporting"), conservators (CCA), galleries, art services.
- Platform: iOS app + web app; templates in nine languages; closed system with 2FA; sharing is purposeful and permission-scoped.
- Founder background: conservation (Tate, St Paul's Cathedral) — "the need for a digital solution to streamline condition reporting and manage risk."

### TMS Collections / TMS Conservation Studio (enterprise module pole; evidence layer A at product/directory level, no screen-level claims)

- Collections Trust directory entry: TMS Collections is Spectrum 5 compliant; the listed supported **Spectrum procedures include "Condition checking and technical assessment" and "Collections care and conservation" as separate lines** (alongside the primary procedures). 11 interrelated modules; suite companions: TMS Conservation Studio (conservation documentation), TMS Media Studio, Audit Manager, eMuseum.
- TMS Conservation Studio product page: "museum conservation documentation software" for conservators; "Design custom reports for fast **condition, damage, and treatment reporting**"; tablet photographing with "annotation tools" to "note areas of damage or concern"; "linking records for outgoing objects to their upcoming exhibitions or loans"; "immediate record syncing with TMS Collections"; "granular security settings to safeguard your conservation data until it's ready for sharing."
- Frick Collection conservator quote: the TMS ↔ Conservation Studio link mattered because "we didn't want to have to go into a separate system to access object data."
- Interpretation (calibrated): condition reporting appears both inside the CMS (as a supported procedure/module family) and inside the conservation documentation companion (condition + damage + treatment reports); the assessment/treatment split is a workflow split, not strictly a product split. Screen-level behavior of TMS condition reports is login-gated — no screen-level claims made.

### CatalogIt (SMB SaaS pole; evidence layer A)

- Homepage: "Securely track and update entries — including value, location, and **condition** — adding to their stories in real time." Museum demo description includes "updating condition and maintenance status."
- Museum plan bullet: "Accession, exhibition, loan, and location documentation" (condition not headlined there; it lives on the entry).
- **Conservator plan** (same core sold to conservators): "Document an objects' condition in detail, meticulously capture its conservation process, all while tracking each step for complete accountability." Key features: "Track condition and conservation over time — capture condition details over time — before, during and after treatments — **use repeating fields to show every stage of the process**"; "Generate condition and conservation reports for clients and your own records — attach images and documents"; "Deliver condition summaries and conservation plans to clients"; "Monitor the movement of objects between clients and the conservation lab — track precise locations."
- Help center (forms article): forms list covers Deed of Gift, Loan In/Out Agreements, Temporary Custody Agreements/Return Receipts — no condition-report form in that list; but the loan workflow instructs "Verify object data (**condition**, insurance values, medium) is up-to-date" — condition is entry-level data consumed by loan documentation.
- Interpretation (calibrated): condition documentation is entry-attached and history-bearing (repeating fields), report-generating, and client-facing in the conservator posture; no screen-level claims beyond the documented feature text.

### eHive (mid-market cloud pole; evidence layer A — field-level operational docs)

- Object cataloguing page has a **Conservation tab**: "record information about an object's condition, risk, handling, proposed treatment, and completed treatment."
- **Condition field group**: Condition date; Condition keyword ("records the object's overall condition" — pick list; five recommended keywords: Excellent / Good / Fair / Poor / Very poor, each with a one-line definition); Condition notes ("records details about an object's condition **on a certain date**"; damage/deterioration vocabulary list — abrasions, flaking, mould active, insect damage, torn, warped… — **sourced from Te Papa Tongarewa's Condition Reporting Forms Template**; "If an object requires treatment… record this in the conservation treatment field"); Condition part (part reference/aspect — which part of the object); Condition person.
- **Risk and handling group**: risk assessment (+ by/date/notes/factor), handling details.
- **Proposed treatment group** and **Completed treatment group**: separate field sets (description/date/keyword/notes/part/person; priority for proposed).
- Fields are private (not public-facing) and searchable (e.g. `condition_keyword: poor`).
- Interpretation (calibrated): the condition record = date + person + overall rating + structured notes + part reference; treatment is a separate field family on the same tab — the assessment/treatment boundary visible at field level inside one product. The vocabulary's paper-template provenance (Te Papa) documents the paper-form lineage feeding digital fields.

## Cross-product Comparison

| Dimension | Spectrum (standard) | Articheck | TMS / Conservation Studio | CatalogIt | eHive |
|---|---|---|---|---|---|
| Condition record bound to object identity | object number required; accessible via object numbers | reports per artwork entity | condition reports on object records (module family); Conservation Studio syncs to TMS object data | condition on entries (object records) | condition fields on object records (Conservation tab) |
| Dated + attributed | date + checker + reason required | report authorship; audit trail | report records (screen-level n/a) | condition history over time | Condition date + Condition person |
| Structured condition content | condition term + note; method; completeness; hazard | guided templates by material; annotations with symbols; notes | condition/damage reports; annotation tools | condition details; repeating fields | keyword picklist + notes vocabulary + part reference |
| Photographic/sketch documentation | "highly desirable", may be required by lenders/insurers | multimedia reports; image annotation; video | photograph + annotate on tablet | attach photos/documents | (media attachable to records; not condition-specific in fetched docs) |
| Retained comparable history | "audit trail of changes"; "refer to previous condition checks"; escalation on difference | "Condition history" feature | history on record (screen-level n/a) | repeating fields show every stage | fields accumulate per check date (searchable) |
| Trigger structure | prompted by other procedures; risk points (before/after moving); scheduled; post-change | in situ / transit / storage moments; Transit Hub checks | outgoing objects linked to exhibitions/loans | movement between clients/lab tracked; loan workflow verifies condition | (trigger machinery not in fetched field docs) |
| Recommendations output | display/env/handling/packing/storage recommendations; treatment priority; next check date | optional Packing Requirements / Treatment Proposals sections | treatment reporting | conservation plans; condition summaries to clients | handling details; proposed treatment fields |
| Depth tiering | check → condition report → full condition report (3 named levels) | "basic to detailed" templates | custom reports | one-click vs customized reports | single field-group depth |
| Sharing beyond the institution | lenders/insurers/indemnifiers may require records; object passport | purposeful permission-scoped sharing; read-only/edit/revoke | granular security "until ready for sharing" | reports delivered to clients | private fields (not public) |
| Packaging | medium-agnostic (paper allowed) | dedicated standalone product | CMS module + conservation companion product | CMS feature + Conservator plan posture | CMS field group |

**Cross-product commonalities (evidence layer B):** the object-bound, dated, attributed condition record; structured condition content (rating/keywords + damage description + damage location); photographic documentation; retained per-object history that later reports are read against; report generation as a shareable deliverable; the assessment/treatment separation; consumption by loan/exhibition/movement workflows.

**Product-specific (evidence layer A, single-product):** Articheck's transit-check/shipment layer and permission-scoped cross-party sharing; eHive's five-keyword rating picklist and Te Papa-sourced vocabulary; CatalogIt's repeating-field realization and Conservator-plan client posture; TMS's two-product split (CMS module + Conservation Studio); Spectrum's object-passport duplication and three-level expertise tiering.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The condition record as a dated, attributed assessment of an identified object.** A persistent record bound to the object's identity (object number/accession number or equivalent), recording the object's physical state at a point in time, who assessed it, and when (with the reason for checking as the standard's required audit field). Remove → object descriptions or a check log, not condition documentation.
2. **Structured condition content describing physical state.** The observed state expressed in some structured form — overall rating/keywords, damage and deterioration descriptions, damage location on the object (part references, annotated images) — plus photographic/sketch documentation. Form varies widely (free text ↔ controlled vocabularies ↔ annotated images ↔ material-specific templates); structured descriptive content is the constant. Remove → a bare "checked on" log with no state content.
3. **The retained comparable history.** Condition records accumulate per object and are retained so earlier states remain referable and change is detectable — the standard's "audit trail of changes to objects," its instruction to "refer to previous condition checks," and its escalation rule triggered when condition "differs from that recorded in previous condition checks." Remove → a mutable current-condition field; the discipline's evidentiary and change-detection purpose collapses.

Jointly-held is load-bearing: 1 alone = check log; 2 alone = descriptive cataloguing; 3 alone = an archive of unanchored documents; 1+2 without 3 = overwriting snapshot (loses the audit trail and change detection); 1+3 without 2 = check log archive; 2+3 without 1 = unanchored document collection.

### L1 — Common Mature Structure

- **Event-anchored checking**: reports prompted by custody/handling moments — before/after movement, loan release/return, exhibition install/deinstall, object entry — plus scheduled/periodic checks and post-change checks; next-check scheduling (recall date) as forward planning.
- **Depth tiering**: quick check (any trained staff) → condition report (conservation-skilled staff) → full technical assessment (professional conservator, pre-treatment baseline).
- **Templates and vocabularies**: material/object-type templates; controlled condition terms and rating scales; damage vocabularies inherited from institutional paper templates.
- **Photographic documentation with damage-location annotation** (images, detail images, sketches; video in current-era products).
- **Recommendations output**: handling/packing/display/storage/environment recommendations, treatment priority, hazard notes — the assessment feeding care decisions.
- **Concern escalation to conservation** when condition gives cause for concern or differs from prior records.
- **Report generation as deliverable documents** for internal files and external parties.
- **Access control over sensitive condition data**; sharing with external parties (lenders, couriers, partners) under permissions.

### L2 — Variant / Optional Structure

- **Packaging**: module/field-group of a collection management system (TMS, CatalogIt, eHive) vs dedicated standalone product (Articheck) vs conservation-suite component (TMS Conservation Studio). The standalone pole maintains its own lightweight object/artwork identity layer.
- **Technical assessment depth**: scientific tests, material sampling, destructive analysis (policy-gated per the standard).
- **Transit/shipment integration**: condition checks bound to shipment legs; transit hubs (Articheck).
- **Cross-party collaboration networks**: permission-scoped sharing across institutions, galleries, shippers; client-facing conservator postures (CatalogIt Conservator plan).
- **Object passport duplication** (a portable copy of condition/hazard information traveling with the object) — standard-suggested, not observed as product machinery in the sample.
- **Multi-language templates, mobile-first capture, video reporting** — era machinery.
- **Who authors**: institution-policy-dependent (any staff/volunteer vs conservator), realized as permission tiers.

### L3 — Vendor-specific (kept here, not in the final document)

- Articheck: "up to 75% faster" claim; nine template languages; 2FA closed system; AWS/128-bit/OAuth2 security specifics; Transit Hub branding; free-trial mechanics; named-client testimonials.
- eHive: field IDs (condition_keyword, condition_notes…); 200-char/1000-char limits; the five recommended keywords and their definitions; the Te Papa-sourced damage vocabulary; private-field visibility; search syntax examples.
- TMS: 11-module composition; Conservation Studio syncing and granular security; Frick quote; directory-entry licensing/training details.
- CatalogIt: plan structure and pricing (Museum/Personal/Organization/Conservator; entry counts); repeating-field implementation; HUB publishing; forms template authoring (.docx upload, Admin/Owner-only).
- Spectrum: condition check reference numbers; standard term sources; object passport; the three-level Note 1 tiering; quarantine-area guidance.

## Vendor-specific vs Type Findings (explicit)

- The **assessment/treatment separation** is Type-level: it holds in the standard (two procedures), at field level (eHive), and in product packaging (TMS's two products; CatalogIt's condition vs conservation-process tracking). Not vendor-specific.
- **Templates/annotation/vocabularies** are common machinery, not definitional — the standard is medium-agnostic and paper-satisfiable.
- **Transit/shipment condition checks** are common practice (standard's risk-point checks; Articheck's Transit Hub) but the shipment-integration machinery is product-specific.
- **Cross-party permission-scoped sharing** is Articheck-verified at that depth; the underlying behavior (reports shared with lenders/partners) is standard-and-practice level.
- **Standalone packaging exists** (Articheck) — this distinguishes the leaf from the exhibition cluster, where no standalone product was found; it does not make standalone packaging definitional (most market volume is module-packaged).

## Rejected Findings

- "Condition reporting = conservation management" — REJECTED: the standard splits them into two procedures; eHive splits them into field groups; TMS ships two products. Condition documents state; conservation documents interventions (proposed/completed treatment). They interlock (pre-treatment baseline condition report) but are distinct workflows.
- "Condition reporting is just a field on the object record" — REJECTED as a definition: the minimal realization is field-shaped (eHive), but the discipline includes the event record (date/checker/reason), the accumulated history, and the report-as-deliverable; a single mutable field fails leg 3.
- "Condition reports are produced only by conservators" — REJECTED: the standard's three levels explicitly include checks by any staff member/volunteer; products serve registrars, collections managers, couriers, gallery staff.
- "Condition reporting requires a CMS" — REJECTED: Articheck realizes the workflow standalone with its own artwork-entity layer.
- "Condition reporting is museum-only" — REJECTED: the same structure serves galleries, shippers, conservators in private practice, and collectors (Articheck solutions pages; CatalogIt plans); the museum is the directory's framing, not the structure's limit.
- "Damage and loss records = condition reports" — REJECTED: damage/loss documents incidents and claims (a separate Spectrum procedure); condition checks document state, including pre-existing damage. A check may surface damage that spawns an incident record, but the record classes differ.

## Boundary Findings

**1. vs Museum Conservation Management (§27 sibling, unprocessed) — the primary boundary.** Condition reporting documents physical state (assessment); conservation management documents and governs interventions (examinations, treatment proposals, treatment records, treatment programs). Evidence: Spectrum lists "Condition checking and technical assessment" and "Collections care and conservation" as separate procedures, with the escalation rule connecting them (concern → conservator); eHive separates Condition fields from Proposed/Completed treatment fields on the same tab; TMS separates condition reporting (CMS) from treatment documentation (Conservation Studio) while noting condition reports are also written pre-treatment ("the condition of the object should be recorded before any treatment takes place" — the interlock point). Removal tests: remove treatment records → condition reporting stands alone (Articheck ships treatment proposals only as an optional section); remove condition assessments → treatment management stands (though conservators commonly write the pre-treatment baseline). **Verdict: distinct sibling Types with a documented interlock; this document is the counterparty the conservation pass should treat as such.**

**2. vs Museum Collections Management (§27 container, processed 2026-09-08).** That pass hosts this leaf as one custody-lifecycle event family ("care") and defers the workflow's internal structure here. Confirmed from this side: condition records attach to the object records the container owns; the container's location/movement machinery handles the physical moves that prompt checks (Spectrum's own cross-reference). Removal tests: strip condition reporting from a CMS → the register, location picture, and other event families stand (care leg weakened); strip the object register → module-packaged condition reporting has nothing to attach to — but the standalone pole (Articheck) maintains its own minimal artwork-entity layer, so the workflow survives packaging independence. **Verdict: keep-both with containment framing, consistent with the accession/cataloging and exhibition-cluster precedents.**

**3. vs Museum Loan Management (§27 sibling, unprocessed).** Loans *require* condition documentation at release and return (standard's loans procedures; Articheck's loan-collaboration sharing; CatalogIt's loan workflow verifying condition data). The loan owns the agreement/transaction lifecycle; condition owns the assessment discipline. Removal tests: remove condition reports → loan management stands with a liability gap at handovers; remove loans → condition reporting remains (transit, storage surveys, treatment baselines, intake). **Verdict: distinct; loan pass should treat this document as counterparty.**

**4. vs Exhibition Installation Management (processed 2026-09-07) and Artwork Exhibition Logistics (processed 2026-09-06).** Both consume condition documentation at handover moments; both passes explicitly deferred the standalone discipline here ("condition documentation as a standalone discipline at any moment; installation consumes it at handover points but is not constituted by it"; handover documentation is L1 for logistics). Ratified from this side: condition reporting exists at any moment (storage surveys, treatment baselines, intake) without any display occasion or movement chain. **Verdict: boundaries hold as pre-agreed; no new flags.**

**5. vs Museum Object Movement Management (§27 sibling, unprocessed).** Movement owns the location picture and move transactions; condition owns the state assessment. Spectrum's own procedure cross-reference shows the seam: "If you need to move objects to check them, go to Location and movement control." Removal tests both directions hold. **Verdict: distinct; movement pass should treat this document as counterparty.**

**6. vs Provenance Research Platform (§27 sibling, unprocessed).** Provenance documents the history of ownership/origin (who held it, how it traveled); condition documents physical state. Both attach to object records; content classes differ. **Verdict: expected clean; noted for that pass.**

**7. vs Building Condition Assessment (§17 leaf) and generic inspection tools.** Same assessment-documentation shape, different object world: buildings/facilities vs collection objects under custody, with object-number binding, conservation vocabularies, and custody-moment triggers. **Verdict: distinct Types; the shared "condition report" name is vocabulary overlap, not Type identity.**

**8. Packaging reality.** Unlike the exhibition cluster (no standalone product found), this leaf has a reachable dedicated standalone product (Articheck) alongside module-packaged realizations (TMS, CatalogIt, eHive) and a conservation-suite component (Conservation Studio). The Type therefore stands on its own workflow structure, not on suite packaging. No directory change proposed.

## Historical / Market-Sample Check

Paper-era form of the same discipline: a condition report card/form per object — object number, date, checker, description of damage and deterioration (often from a standard vocabulary list), sketches or photographs — filed by object number in the object's file; loan condition reports prepared in duplicate to travel with the object; hazard/handling notes and "object passport" tags; pre- and post-treatment condition baselines in the conservation file. All satisfy the three legs: object-bound dated attributed assessment (card + number + date + checker), structured condition content (vocabulary + sketch/photo), retained comparable history (the file of prior cards consulted before the next report). The digital lineage is directly documented: eHive's condition-notes vocabulary is sourced from Te Papa Tongarewa's **Condition Reporting Forms Template** (paper-form practice feeding product fields), and Spectrum explicitly allows paper-based systems. The definition therefore names no software surface, no cloud, no templates machinery, no annotation tools, no sharing infrastructure — older, regional, paper-based, and small-museum realizations all fit. Modern machinery (multimedia reports, video, permission-scoped sharing networks, transit hubs, mobile capture) is era layering, held outside the core.

## Uncertainties

- Screen-level operational behavior for TMS Collections condition reports and MuseumPlus is login-gated (consistent with sibling passes); their evidence is directory/product-page level. No screen-level claims made for them.
- MuseumPlus: product page names no condition module; public docs cover only the Web Service API. MuseumPlus's condition machinery is unverified this pass — recorded, not asserted.
- Axiell Collections, Vernon CMS (desktop), Lucidea, PastPerfect unreachable in prior passes — not retried beyond recorded limits; the small-museum desktop pole is unverified this pass (eHive partially covers the Vernon-family structure at field level).
- CollectiveAccess not sampled (manual only partially reachable in prior passes); whether its condition machinery is built-in or user-configured is unverified.
- Whether other dedicated standalone condition-reporting products exist beyond Articheck could not be exhaustively excluded; Articheck is the clearly reachable dedicated product (also noted by the artwork-exhibition-logistics pass).
- The exact division of condition-report labor between TMS Collections and TMS Conservation Studio (both document condition) is not fully documented publicly; the assessment/treatment boundary claim rests on the standard, eHive's field structure, and product positioning, not on TMS screen evidence.
- Terminology varies ("condition check", "condition report", "condition assessment", "technical assessment"); the standard itself uses all of these with a three-level depth distinction. The final document uses "condition report/record" as the umbrella and notes the tiering.

## Final Synthesis

Museum Condition Reporting is the collection-care discipline of **documenting the physical condition of collection objects as dated, attributed, object-bound records with structured condition content, retained as a comparable per-object history** — the audit trail of changes to objects that the domain standard names explicitly. The workflow is triggered by the custody moments where state matters (before/after movement, loan release/return, exhibition handovers, intake, treatment baselines) and by scheduled surveys; it produces recommendations (handling, packing, display, storage, treatment priority) and escalates concerns to conservation. The Type is deliberately distinct from conservation treatment management (assessment vs intervention — split at standard, field, and product levels), from the collections container (one care-event family hosted on its object records), and from the loan/exhibition/movement siblings (which trigger and consume condition documentation but are not constituted by it). The market realizes the Type as CMS modules and field groups (TMS, CatalogIt, eHive), a conservation-suite component (Conservation Studio), and a dedicated standalone product (Articheck) — the only §27 museum-workflow sibling with a reachable standalone pole. The paper-era condition card filed by object number satisfies the defining core, so the definition names no software surface or era machinery.
