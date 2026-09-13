# Research Notes — Animal Research Ethics / IACUC Platform

Research date: 2026-09-06

## Research Goal

Understand what software in the "Animal Research Ethics / IACUC Platform" category actually does: its core objects, the review and oversight workflows it digitizes, its users and interfaces, its rules and lifecycle behavior, and how it differs from adjacent Application Types (IRB platforms, animal facility/colony management, research compliance suites, research administration platforms).

## Initial Boundary

Working hypothesis before research:

- This Type is the system that supports an institutional animal care and use oversight body (in the US context, the IACUC — Institutional Animal Care and Use Committee; other regions use differently named bodies) in managing protocol-based review and continuing oversight of animal use in research/teaching/testing.
- Likely confusion sets:
  - IRB / Research Ethics Management (same workflow shape, different review object: human participants)
  - Research Animal Facility Management (vivarium/colony/census/husbandry/billing — manages the animals, not the authorization)
  - Research Compliance Management (broader multi-committee compliance container)
  - Research Administration / Grant Management (adjacent integration point, e.g., protocol–grant congruency)
- Unknowns going in: exact module boundaries in each product; whether inspections/post-approval monitoring are core or optional; how training/qualifications are modeled; regional variants; whether standalone (non-suite) IACUC products dominate.

## Research Questions

1. What is the central object (protocol? application? license?) and what does it contain?
2. What is the full lifecycle of that object (submission → review → decision → amendments → renewals → closeout)?
3. Who interacts with the system and in which roles (PI, staff, reviewers, administrators, veterinarian)?
4. How is committee review itself supported (meetings, agendas, reviewer assignment, decision recording)?
5. What ongoing-oversight surfaces exist (reportable events, inspections, post-approval monitoring, annual review)?
6. What institution-level outputs exist (reports to USDA/OLAW/AAALAC-type bodies, program descriptions, audit trails)?
7. How do personnel, qualifications, and training attach to the protocol?
8. Where are the boundaries with IRB platforms and with animal facility/colony systems?
9. What varies by regulatory region, institution size, and product packaging (suite module vs standalone)?

## Representative Products

Sampled (direct evidence this pass):

1. **Cayuse — Animal Oversight** (compliance module of the Cayuse research administration suite; higher education, healthcare, life sciences; US origin, marketed internationally)
2. **Kuali — Animal Ethics Review** (compliance module of Kuali Research; higher education; US origin, customers include Canadian institutions)

Sampling rationale: both are current, marketed products with reachable official product pages and (for Kuali) a reachable help center; both sit inside research administration/compliance suites, which matches the dominant packaging in this market; they differ in philosophy (Cayuse: deep pre-built IACUC workflow with versioned review tooling; Kuali: configurable form/workflow platform approach).

Attempted but not reachable (see Source-access Limitation):

- **Huron Research Suite (IACUC)** — domain (huronresearchsuite.com) transport errors, both www and bare.
- **Topaz Technologies (eProtocol/protocol management, acquired by SciShield)** — topaztek.com transport error; SciShield has since merged into **SciSure** (eLabNext + SciShield), whose current site centers on ELN/LIMS/EHS and no longer surfaces an IACUC protocol product at root level.
- **InfoEd Global** — infoed.org transport error.
- **Advarra** — reachable, but its current site navigation shows IRB/IBC/DMC review services and site solutions; no IACUC protocol product surface was found this pass → recorded as Product Mismatch for this Type, and useful only as context for the human-subjects sibling Type.
- **NIH OLAW** — 403 (bot-blocked); **USDA APHIS** — not attempted after other failures.

Sample skew note: both confirmed products are modules of higher-ed research suites. The market reportedly also contains legacy/standalone vendors and institution-built systems, but none could be verified this pass. Cross-product claims below are calibrated accordingly ("the researched sample", "commonly" only where both sampled products agree).

## Sources

Tier 2 (official product pages):

- Cayuse — Animal Oversight product page: https://www.cayuse.com/compliance-management/animal-oversight/ (fetched 2026-09-06)
- Cayuse — corporate site / suite structure (Compliance Management, Vivarium Management, International pages): https://www.cayuse.com/
- Kuali — Animal Ethics Review product page: https://www.kuali.co/products/animal-ethics-review (fetched 2026-09-06)
- Kuali — Research suite overview (Help Center article "What is Kuali Research?"): https://kuali.zendesk.com/hc/en-us/articles/27090467314075-What-is-Kuali-Research (fetched 2026-09-06)

Tier 1 (operational documentation, partial):

- Kuali Help Center — Research category and Research Knowledge Base: https://kuali.zendesk.com/hc/en-us/categories/23343502783771 (generic, product-family level; no animal-specific operational articles surfaced)

Domain context (official accreditor — grounds the oversight structure the products digitize):

- AAALAC International — site structure, accreditation process, Program Description, adverse-event reporting expectations, global directory of accredited programs: https://www.aaalac.org/ (fetched 2026-09-06)

Source-access Limitation: vendor support portals requiring sign-in (Cayuse Support: https://support.cayuse.com — login wall) and unreachable vendors (see above) mean no step-by-step operational manuals were observed. All precise operational facts (exact form sections, exact review pathway names, voting mechanics, renewal cadences, numeric limits) are therefore either unobserved or are reported only as they appear verbatim on the reachable pages. No such detail was filled in from model memory.

## Product A — Cayuse (Animal Oversight)

### Key observations (Evidence Layer A — directly observed on official pages)

- Positioning: "streamlined IACUC protocol oversight"; part of Cayuse Compliance Management alongside Human Ethics, Hazard Safety, Outside Interests (COI), and Risk & Compliance; separate sister line "Vivarium Management" (Vivarium Operations, Schedules, Vet Care) for animal care/orders/inventory/billing.
- Protocol lifecycle: "Electronically prepare, submit, and route studies for IACUC committee approval"; "full lifecycle of IACUC protocols"; homepage dashboards "displaying all critical workflow information"; "Know protocol status at all times".
- Review tooling: "instantaneous access to the latest version, change history, in-line comments, and side-by-side version comparisons"; "View tracked changes and reviewer comments within the protocol form".
- Renewals: "Automatic notifications for annual and De Novo renewals".
- Meetings: "Agenda and committee meeting management".
- Training: "Automatically track training requirements at the personnel, species, and activity level"; "Configurable training requirements for activities, species, procedures, and hazardous agents"; "Transparency into personnel qualifications during protocol authorship".
- Reporting: "reports needed for the AAALAC program description, USDA site visits, and PHS Assurance"; "Filter-driven USDA and AAALAC reports".
- Integrations: "Integrate with Hazard Safety for cross-committee approvals and Vivarium Operations and Vet Care for centralized animal research data sharing"; Cayuse Platform unifies task management and user data across apps; Report Connector exists at platform level.
- Workflow: "Workflows for compliance and protocols" (configurable); "100% paperless".
- Regional posture: International page states configurable workflows/forms "can accommodate region-specific ethics, grants, and compliance processes".
- Evidence of use: university IACUC coordinator testimonial (time reduction in reviews); La Jolla Institute testimonial about animal orders taking "less than an hour" via Cayuse (order placement surfaced through the platform/integration).

## Product B — Kuali (Animal Ethics Review)

### Key observations (Evidence Layer A — directly observed on official pages)

- Positioning: "Animal Ethics Review" product within Kuali Research suite; siblings: Sponsored Programs, Internal Opportunities, Conflict Management, Export Control, Human Ethics Review, Biosafety Review, GrantRisk.
- Suite-level definition (Help Center, verbatim): "Oversee the ethical treatment and use of animals in research through collection and review of protocols, including information about animal care, housing, handling, and experimental procedures, to ensure appropriate animal welfare and minimize pain and distress."
- In-the-box units: Protocol/Application Submissions; Annual Review/Closeout ("Manage the annual protocol review and closeout processes"); Meetings ("Manage IACUC committee meetings and meeting agendas"); Reportable Events ("Collect information related to adverse events that occur during the course of a study"); Reviews/Checklists ("Create a checklist to aid reviewers"); Facility Inspections ("Track and report on animal facility inspection data").
- Workflow: "Handle renewals, amendments, and reportable events all in one, integrated interface"; "Tame the triage, VVR, and review process with flexible, powerful workflow that matches your process, and convenient committee management tools" (VVR acronym not expanded on the page; left unexpanded here).
- Guided authorship: "easy-to-follow navigation, built-in help, and conditional visibility that keeps the focus on capturing the right data".
- Extensibility: form builder & workflow designer ("Flexible, easy-to-use form builder and powerful workflow designer"); add-on examples listed by the vendor: Animal ordering, animal transfer, occupational health/animal handling, new species request, congruency review, training verification, researcher help request, facilities review form; "pre-approved procedures library".
- Administration: "Sophisticated Group and Role Management"; dashboards and reporting; "Shared configuration makes it easy to keep track of sponsor, training & person data"; "Deep integration with other parts of the Kuali suite enables visibility into related proposals, awards, disclosures and other protocols"; modern APIs; institutional branding; SaaS continuous delivery.

## Cross-product Comparison

| Dimension | Cayuse Animal Oversight | Kuali Animal Ethics Review | Read |
|---|---|---|---|
| Central object | IACUC protocol ("studies") | IACUC protocol ("protocols/applications") | Common |
| Authored by investigator into structured form | Yes ("prepare, submit and route") | Yes ("collection of protocols"; guided forms) | Common |
| Committee review workflow with recorded outcomes | Yes (route for committee approval) | Yes (triage → VVR → review; flexible workflow) | Common |
| Review tooling detail | Version comparison, tracked changes, in-line comments | Reviewer checklists, workflow designer | Common (mechanism differs) |
| Committee/meeting management | Agendas + meetings | Meetings + agendas | Common |
| Amendments / modifications | Within full lifecycle | Explicit ("renewals, amendments, reportable events") | Common |
| Recurring review / renewal | Automatic notifications (annual, De Novo) | Annual review / closeout | Common |
| Reportable events / adverse events | "Workflows for compliance and protocols" (not itemized on page) | Explicit "Reportable Events" unit | Common (explicitness differs) |
| Facility inspections | Not on product page | Explicit "Facility Inspections" unit | Product-specific-leaning; treat as Common-Optional |
| Personnel / training tracking | Deep (personnel, species, activity, procedures, hazardous agents) | Present (training verification add-on; shared person data) | Common |
| Regulator/accreditor reporting | USDA / AAALAC / PHS reports | Dashboards/reporting (generic) | Common (depth differs) |
| Status dashboards | Homepage dashboards | Document dashboard, status views | Common |
| Vivarium / animal ordering integration | Vivarium Operations & Vet Care integration | Add-on (animal ordering, animal transfer) | Common (packaging differs) |
| Cross-committee coupling | Hazard Safety cross-committee approvals | Sibling Biosafety Review product; congruency review add-on | Common |
| Suite embedding | Suite module (Compliance Management) | Suite module (Kuali Research) | Common in sample |
| Deployment | Cloud (SaaS) | Cloud SaaS, continuous delivery | Common in sample |
| Form configurability | Configurable workflows | Form builder + workflow designer | Common |

## Canonical Model

### L0 — Defining Invariant (deliberately small)

1. **Protocol record** — an investigator-authored, institution-owned structured record describing a proposed/ongoing use of animals (species, procedures, personnel, welfare measures).
2. **Committee review process** — the institutional animal care and use oversight body (IACUC or regional equivalent) reviews the protocol through a structured, recorded workflow.
3. **Recorded decision + approval status** — the system records review outcomes and maintains the protocol's approval status, which functions as the institution's authorization for the described animal work.
4. **Ongoing oversight of the approved protocol** — the approved protocol remains a living record: changes are reviewed before implementation, review recurs, and reportable events can be attached.

If (1)–(3) are removed, the product is not this Type. If (4) is removed, the product degrades to a one-shot electronic form system rather than an oversight platform — and every sampled product, the accreditor's expectations (adverse-event notification, site visits), and the historical paper-era IACUC process all include recurring oversight, so it belongs in the invariant.

Historical/market-sample check: paper-era IACUC files, in-house databases, and older products (e.g., legacy compliance suites from the 2000s) all fit this minimal structure; regionally, differently named bodies (AWERB-type in the UK, animal ethics committees elsewhere — visible as "region-specific ethics processes" on Cayuse's international page and via AAALAC's global accredited-program directory) still fit. Therefore "IACUC" as a US-specific label stays out of the invariant; the invariant is phrased as protocol + oversight committee + recorded approval + living oversight.

### L1 — Common Mature Structure (both sampled products agree unless noted)

- Institution-configurable protocol forms capturing animal care, housing, handling, and experimental procedures; welfare and pain/distress minimization content (Kuali verbatim; Cayuse via configurable workflows/forms).
- Review machinery: triage/routing, reviewer assignment, reviewer checklists (Kuali), version comparison and in-line comments/tracked changes (Cayuse), clarification correspondence.
- Committee and meeting management: agendas, meeting support.
- Amendments/modifications processed through the same review loop.
- Recurring review/renewal (annual review / closeout; automatic renewal notifications).
- Reportable events / adverse event capture attached to protocols.
- Facility inspections tracking (explicit in Kuali; not observed on Cayuse product page — keep as Common-Optional).
- Personnel and training tracking, incl. qualification checks during authorship; configurable per activity/species/procedure/hazardous agent (Cayuse deepest).
- Status dashboards for PI and administrators.
- Institutional reporting surfaces (regulator/site-visit/accreditation reports; audit-ready records).
- Role-based access control (explicit in Kuali; implied by workflow structure in Cayuse).
- Suite integration points: human ethics sibling, hazard/biosafety cross-committee approvals, congruency review against sponsored projects, vivarium/animal-ordering adjacency.

### L2 — Variant / Optional Structure

- Packaging: suite module (dominant in sample) vs standalone product vs institution-built system.
- Regulatory regime packaging: US-heavy artifacts (USDA, PHS Assurance, AAALAC program description) vs region-configurable forms/workflows.
- Animal-operations coupling depth: none / data-sharing integration / full vivarium operations & ordering in the same vendor family (Kuali add-ons vs Cayuse integrated sister line).
- Breadth of committee families supported in the same product family (IRB, IBC, COI, export control).
- Configuration philosophy: pre-built deep workflows vs form/workflow designers.
- Pre-approved procedures libraries; conditional form visibility; guided authorship aids.
- Internationalization/multi-site program structures.

### L3 — Vendor-specific Structure (kept out of final document)

- Cayuse: module names (Animal Oversight, Hazard Safety, Vivarium Operations, Vet Care), "De Novo renewals" terminology, Report Connector, testimonials (Idaho State University, La Jolla Institute for Immunology), "200% faster" marketing claim.
- Kuali: "triage, VVR, and review" phrasing (VVR unexpanded), add-on catalog items, Kuali Build form/workflow designer lineage, GrantRisk, customer names (University of Maryland, UC San Diego, etc.), institutional branding feature.
- SciSure/SciShield corporate merger context (eLabNext + SciShield → SciSure; LabFolder acquisition), Topaz heritage — uncertain whether a Topaz-heritage IACUC protocol product remains marketed.

## Vendor-specific Findings

See L3 above. Additional product-specific observations that must not generalize:

- Only Cayuse's page explicitly names regulator/accreditation report artifacts (AAALAC program description, USDA site visits, PHS Assurance).
- Only Kuali's page explicitly itemizes facility inspections and reportable events as named product units.
- Only Cayuse's page documents training requirements at the species/activity/procedure/hazardous-agent granularity.
- Kuali's page documents the add-on pattern (animal ordering/transfer as extensions), while Cayuse documents vivarium integration into a separate vendor product line.

## Boundary Findings

- **IRB / Research Ethics Management** (sibling Type): identical platform shape (protocol → committee review → decision → amendments → renewals → reportable events), different review object (human participants vs animal use) and different regulatory regime. Vendor evidence: both sampled vendors ship Human Ethics as a sibling product built on the same machinery. Boundary test: swap the review object and the regulatory artifacts; if the system's forms, checklists, and reports are about human-subjects protections, it is the IRB Type, not this one.
- **Research Animal Facility Management** (vivarium/colony/census): manages the animals themselves — housing, census, husbandry schedules, vet care, orders, per-diem billing (Cayuse's separate Vivarium Management line). This Type manages the *authorization and oversight* of animal use. Boundary test: remove the committee review/decision loop and you are left with facility/colony management; that is the "去掉什么就变成另一个 Type" discriminator. The two Types integrate (protocol→ordering, approved-protocol as prerequisite for housing/procurement) but are structurally distinct.
- **Research Compliance Management** (broader Type): multi-committee compliance containers (Kuali Research; Cayuse Compliance Management) typically include this Type as one module. Relationship: container vs member.
- **Research Administration / Grant Management**: adjacent; integration point is protocol–grant congruency review (Kuali add-on explicitly named "congruency review"; Kuali help notes visibility into related proposals/awards from protocol context). Not the same Type: no committee review of animal use.
- **Accreditation / Certification Management**: AAALAC-type accreditation is an institution-level program-review cycle (Program Description, site visits) that this Type *supports with reports and evidence*, but the accreditation record is not the central object of this Type.
- **CTMS**: clinical trial management for human-subject trials; different object and regime (Advarra check confirmed CTMS/IRB services orientation, no IACUC product surface).

## Uncertainties

1. Operational depth (exact protocol section taxonomies, review pathway names, voting/quorum mechanics, renewal cadences, electronic-signature handling) — not observed; support portals were login-gated. Final document must avoid precise operational claims.
2. Market breadth: only two products verified this pass; both are higher-ed suite modules. The existence and shape of standalone IACUC products, central-IACUC service models, and legacy systems are plausible (and partially visible as unreachable domains) but unverified. Claims calibrated to "the researched sample".
3. Whether facility inspections and post-approval monitoring are universally bundled (explicit only in Kuali's page within the sample) — kept as Common-Optional.
4. Regional products (UK AWERB software, EU/Canada/Australia committee systems) were not sampled; the international claim rests on vendor statements (Cayuse international page) and the accreditor's global directory.
5. The SciShield/Topaz situation (whether a Topaz-heritage protocol product continues inside SciSure) — unresolved.

## Final Synthesis

The Application Type is best modeled as: **a protocol-centric institutional oversight system**. One central object — the animal-use protocol — carries the entire workflow: authored by the investigator, reviewed by the institutional oversight committee through configurable review machinery, decided and recorded, then kept under recurring oversight (modifications, renewals, reportable events, inspections) for as long as the animal work continues. Around this loop, mature products add personnel/qualification tracking, committee/meeting management, status dashboards, regulator/accreditation reporting, and integrations to the human-ethics sibling, hazard/biosafety committees, sponsored-projects records, and the vivarium/animal operations stack.

The Type's identity is neither "a form tool" nor "an animal husbandry system": the defining discriminator is the committee review loop that converts a described intention into an institutional authorization, and then continuously polices the gap between what was approved and what is being done.
