# Research Notes — Monitoring & Evaluation Platform

Research date: 2026-09-08
Leaf: Monitoring & Evaluation Platform (DIRECTORY.md §25 Nonprofit, Membership & Religious Organizations, line 1797)
Slug: monitoring-evaluation-platform

---

## Research Goal

Understand what a Monitoring & Evaluation (M&E) Platform actually is as a software category: what objects exist inside it, what its users do with them, how program data flows from field collection to donor reporting, which structures are definitional vs merely common, and where its boundaries run against survey/data-collection tools, case management, BI/reporting platforms, grant management, and the sibling leaf "Social Impact Measurement".

## Initial Boundary (pre-research hypothesis)

- Core use: track the results of development/humanitarian/social programs against planned targets (logframe / results framework), and produce accountability reports for donors and funders.
- Likely users: M&E officers/managers, program managers, field staff and implementing partners, donor-facing reporting teams.
- Nearest neighbors: Social Impact Measurement (sibling leaf), Survey Platform / data collection tools (KoboToolbox), Nonprofit Case Management, Nonprofit Grant Management, BI/Dashboard Platform, Government Performance Management, Project Management.
- Boundary guesses to verify: (1) collection-only tools are NOT M&E platforms even though every M&E stack uses one; (2) "evaluation" studies themselves are not executed inside the platform; (3) case-level service tracking is a different Type even though M&E platforms may aggregate case data.
- Unknowns: which object is the system's center of gravity (indicator? form? database? project?); how data quality/approval works; whether targets/baselines are definitional; how multi-partner and multi-level aggregation is modeled.

## Research Questions

1. What is the core object structure — is the results framework/logframe a first-class system object or just an import format?
2. What does an "indicator" record carry (definition, unit, type, baseline, targets, disaggregations, data source, methodology metadata)?
3. How do indicator actuals get into the system (direct entry, computed from collected records, import, formula) and how is periodicity modeled (reporting periods, cycles, incremental vs cumulative)?
4. How does data quality control work (validation, submission, approval, return, locking, audit trail)?
5. Who uses the system and how are roles split (M&E staff, program staff, field/partner data entry, donors)?
6. How does reporting to oversight parties actually happen (progress-to-target, dashboards, exports, standards like IATI)?
7. How do platforms handle multi-project / multi-partner / multi-level aggregation (project → program → organization)?
8. Where is the line vs pure data collection tools, case management, and BI?
9. Historical check: does a paper-era M&E setup (logframe document + indicator spreadsheet + quarterly donor report) satisfy the definition?

## Representative Products

Selection rationale: dedicated M&E platforms (not generic BI or survey tools), each with reachable official documentation, different construction philosophies and customer tiers.

| Product | Construction philosophy | Customer tier | Notes |
|---|---|---|---|
| ActivityInfo | no-code relational database (Database → Folder → Form → Record → Field); M&E realized through database templates | UN agencies, INGOs, country programs | web + self-managed server; strong Tier-1 docs |
| DevResults | framework-first enterprise M&E (Results Frameworks, Indicators, Projects, Reporting Periods) | large development contractors, US Gov agencies (FedRAMP-authorized) | deepest KB articles fetched |
| TolaData | impact-workflow suite: results framework + data tables + collection integrations + dashboards | INGOs, GIZ-type agencies, alliances | positions "results framework, theory of change, or outcomes model" |
| LogAlto | logframe-centric M&E system (project portfolio + logframe + indicator tracking + forms) | INGOs / nonprofits, mid-size | explicit "every M&E system should have at least indicators tracking and data collection" |
| KoboToolbox (boundary sample) | data collection, management, visualization platform | humanitarian field data collection | used to test the collection-vs-M&E boundary |

## Sources

Tier 1 (official operational documentation):

- DevResults Knowledge Base — root: https://help.devresults.com/help
  - Define an Indicator: https://help.devresults.com/help/define-an-indicator (accessed 2026-09-08)
  - Results Frameworks: https://help.devresults.com/help/results-frameworks (accessed 2026-09-08)
  - Define a Results Framework: https://help.devresults.com/help/define-a-results-framework (accessed 2026-09-08)
  - Data Submission & Approval Process: https://help.devresults.com/help/data-submission-approval-process (accessed 2026-09-08)
  - Targets: https://help.devresults.com/help/targets (accessed 2026-09-08)
- ActivityInfo Documentation — root: https://www.activityinfo.org/support/docs/index.html
  - Understanding ActivityInfo's data model: https://www.activityinfo.org/support/docs/database/understanding-activityinfo-s-data-model.html (accessed 2026-09-08)
- TolaData — results framework & indicators page: https://www.toladata.com/results-framework-and-indicators/ (accessed 2026-09-08)
- LogAlto — indicator tracking feature page: https://www.logalto.com/en/monitoring-and-evaluation-tool/indicator-tracking-software/ (accessed 2026-09-08)

Tier 2 (official product/positioning pages):

- ActivityInfo root: https://www.activityinfo.org/ ; M&E use-case page: https://www.activityinfo.org/about/monitoring-and-evaluation.html
- DevResults root: https://www.devresults.com/
- TolaData root: https://www.toladata.com/
- LogAlto root: https://www.logalto.com/
- KoboToolbox root: https://www.kobotoolbox.org/

Tier 3 (vendor blog used for boundary evidence only):

- ActivityInfo blog, "Considering alternatives — Should I use KoboToolbox or ActivityInfo": https://www.activityinfo.org/blog/posts/2024-01-02-should-i-use-kobotoolbox-or-ActivityInfo.html (not fetched in full; existence + title observed on the M&E page listing)

Source-access limitations:

- LogAlto Help Center (help.logalto.com) not fetched individually; evidence for LogAlto comes from its official feature pages (Tier 1.5). Claims about LogAlto internals are calibrated accordingly.
- TolaData knowledge base articles not fetched individually; evidence from official product pages.
- DevResults "Reporting Periods" and "Projects" articles not fetched (obliquely evidenced through other fetched articles); periodicity and project-container claims are therefore stated at the strength of what the fetched articles show.
- No pricing/plan details are used for structural claims.

---

## Product observations

### ActivityInfo (evidence: A — directly observed)

From the official documentation and product pages:

- Self-describes as "information management software for the social sector" with use-case pages for Monitoring & Evaluation, Case Management, Humanitarian coordination, Grant management, Impact measurement, Cash & Voucher Assistance, Conservation, Disaster & Climate Risk. (The vendor itself treats M&E as one deployment of a general social-sector information platform.)
- Data model (official "Understanding ActivityInfo's data model"): ActivityInfo "first and foremost is a relational database". Hierarchy: Database (overall container/workspace) → Folders (organize forms) → Forms (bring data in; a set of records sharing the same fields) → Records (a single discrete entity) → Fields (attributes). Field types span structured to unstructured.
- Key fields uniquely identify records to prevent duplicates and enable connections between forms. Two relationship field types: reference fields (one-to-many between forms, e.g. lists of geographic areas or facilities) and sub-form fields (parent-child; documented examples: "collecting indicator results on a monthly basis", household members within a household survey).
- Roles: users are invited to a database and assigned roles, "a collection of specific permissions" (adding/editing, designing forms, managing users, managing reports).
- M&E use-case page claims: track indicators "from project outputs to strategic impact"; centralize results from existing systems; evaluate at "any level of your results framework"; support "results-based management or any other framework"; validate with validation and relevance rules; "lock changes once results have been reported to the donor"; offline field data collection with tablet/mobile sync; calculate indicators "directly from beneficiary-level data"; web and mobile surveys aligned with program data.
- Documentation structure confirms the operational surface: Database design, Form design (with data quality rules and validation), Permission design (role-based access), Report design (dashboards and reports), Data management, Mobile data collection, Formulas, User management, integrations (Power BI, Tableau, R, QGIS, ArcGIS, Power Automate, API, AI assistants via MCP), migration from XLSForms.
- Templates include a "Global M&E database template for indicator tracking" ("Track indicators across tens or hundreds of projects globally in one database").
- Documentation explicitly contains a tutorial "Build a simple M&E system based on primary data" — i.e., the vendor treats M&E as something you *build* in the database, not a fixed schema shipped by the product.

### DevResults (evidence: A — directly observed)

From the Knowledge Base articles:

- Positioning: "M&E software for global development"; capabilities Map / Monitor / Collaborate / Manage; customers are development implementers (US Gov agencies, INGOs, contractors); FedRAMP-authorized since 2021.
- Results Frameworks: "DevResults uses Results Frameworks to organize indicators into hierarchies of results. Some organizations use other terms for a results framework, like 'logframe'." A framework is a hierarchy of results with Code-based nesting (result 1.1 under 1), Short Name, and "Desired Result" full text "as it might appear in a logframe, PMP, etc." A site can hold multiple results frameworks (e.g., a Main Framework and a Foreign Assistance Framework); frameworks can be deactivated/archived. Result Type classification (output/outcome/impact/other) exists primarily for IATI publishing. Deleting a result only removes assignments; indicators and data remain.
- Indicators: created under Program Info > Indicators with a required unique Code and a Name ("# trainees certified" style, not vague phrases). Definition carries:
  - Data Source: "Enter indicator results directly" (report an aggregated actual once per reporting period) | "Populate from a data table" (report individual records; the system aggregates) | "Calculate from a formula" (from other indicators).
  - Characteristics: Indicator Type (sum/average/yes-no), number format, decimal places, Default Reporting Cycle, Unit ("the thing your indicator is counting or measuring"), and "Periods, Targets are": Incremental (target is for that period only) vs Cumulative (target is total to date).
  - Disaggregations: optional non-geographic disaggregations from a master list, combinable "in parallel or cross"; a Geographic Disaggregation is required per indicator ("If the indicator is not disaggregated geographically, select the largest geographic place") and links data to maps.
  - Assignment: Classification section "must" assign the indicator to at least one results-framework section; sectors and tags optional; multi-project indicators have "Results are reported separately for each project" and are assigned to projects.
  - Narrative definition sections: Definition, Justification, Data Acquisition, Data Quality, Data Analysis/Review/Reporting — i.e., the indicator record doubles as the indicator reference sheet / PMP metadata.
  - Editing constraints: with existing data, changing data source, indicator type, disaggregations, or geographic disaggregation deletes data; the importer warns which indicators would be impacted.
- Targets: "Targets define goals per indicator, per reporting period, and (optionally) per project. When targets are entered... the system automatically includes progress-to-target analyses and visualizations." Global targets vs project targets (need not sum-match); incremental vs cumulative styles ("mathematically equivalent... a matter of preference").
- Data submission & approval: "a built-in submission and approval process for each reporting period, for each project". Statuses per project per reporting period: No Data → In Progress (data being entered) → Submitted (by a user with the "Submit Indicator Results" role, e.g. partner manager) → (Returned, with a request for edits/clarifications, then re-submitted) → Approved (by users with "Approve Indicator Results" permission, e.g. manager/owner). After submission only approvers/Owners may edit; after approval only Owners; Owners can reset a reporting period (deletes that period's direct-entry data; discussion record remains). Status changes and comments accumulate in a per-project-per-period Discussion tab (audit trail). Narratives can be added at any time, including after approval.
- KB sections also evidence (not individually fetched): Data Tables, Forms, Logic Checks, Diagnostics Tools, Custom Queries, Checklists, IATI, Bulk Import, Geographies, Baselines, Narrative Questions, Enterprise publishing — consistent with the observed object set.

### TolaData (evidence: A for the results-framework page; B-graded for suite breadth)

From official pages:

- Positioning: "end-to-end solution for portfolio and project impact management"; workflow "Plan → Collect → Manage → Collaborate → Visualize".
- Results framework: "A results framework is a visual representation of the flow of changes that you intend to deliver... usually displayed in a box-and-arrow tree diagram with different levels". Levels as commonly named by organizations: Goal/Impact, Outcome/Intermediate results, Output, Activities/Input; "Every organization has its own way of defining project levels". Cause-and-effect must hold level to level ("IF [activity A] happens THEN [output A] will happen").
- Indicator plan: "Indicators are specific markers that measure the achievement of inputs, outputs, outcomes and impact... Each level of the results framework has specific indicators assigned to them."
- Data collection: built-in form builder or connections to "Excel, Google Drive, KoboToolbox, SurveyCTO, and more"; "whether it's survey responses, program data, or case-level records, everything flows into one place" (data tables).
- Aggregation: "aggregate results across projects, teams, or regions" (Portfolio Aggregation feature page).
- Collaboration: "manage workflows, route approvals, assign tasks" (approvals evidenced at page level).
- Visualization: configurable dashboards shared "with partners, funders, and stakeholders in real time"; Power BI / Tableau / Superset connectors.
- Standards: IATI compliance feature page exists.
- (AI features are roadmap/marketing — not used for structural claims.)

### LogAlto (evidence: A for feature-page claims; help-center articles not individually fetched)

From official pages:

- Positioning: "Collaborative Web-Based Software for Monitoring and Evaluation of International Development Projects"; "M&E system for NGOs and nonprofits"; fit for INGOs implementing projects in different countries with various partners and multiple donors.
- Explicit industry-structure statement: "Every monitoring and evaluation system should have at least indicators tracking and data collection features."
- Feature set: Project portfolio, Logical framework (logframe software), Indicator tracking, Forms and surveys, Data visualization, Dashboards, Mobile application.
- Indicator tracking (feature page):
  - Indicator form: "Code, description, baseline and target(s), type, etc." plus configurable additional fields ("risks, assumptions, data collection method"); configuration modifiable after launch.
  - Indicator types: quantitative, qualitative, numerator/denominator, percentage.
  - Data entry page is "the heart of the indicator tracking software": see progress of each indicator, "enter actual values or update targets", access past entries and charts. Actuals entered "either as cumulative overall values or the progress that was made during that period" (the same incremental/cumulative duality DevResults documents).
  - History and comments on past data entries.
  - Disaggregation: "Any good indicator tracking software would be incomplete without the ability to disaggregate" — values, baselines, and targets disaggregable on any categories (gender, region, crop types, age group); multiple disaggregation methods combined or parallel; disaggregated data can be aggregated back to the overall value.
  - Linking indicators to collection forms: indicators "can be linked to a form" and updated from records added to it, "reduc[ing] the risk of calculation errors" — the compute-from-records pattern.
  - Import/export: Excel import for logframes ("especially if you already have a logframe in Excel format") and migration from other indicator tracking software.
  - Analytics: aggregate by disaggregation category, by project fields ("project type, sector, donor, location, cross-cutting issues"), by geography, and by organizational unit (division, country office).
- Advantages page: track project indicators independently and "aggregate selected indicators into the programme results framework"; manage lessons learned and success stories; cross-cutting issues (gender, environment).

### KoboToolbox (boundary sample; evidence: A — directly observed, used for boundary only)

- Self-description: "A data collection, management, and visualization platform used globally to accelerate positive social change." Core feature blocks: form development, data collection & analysis, project & team management, data protection.
- Markets an "M&E" vertical ("Optimize data collection and reporting practices to align with your M&E plan", "Track indicators") — but the product's center of gravity is the survey form and field collection; no results-framework object, no target/baseline semantics, no submission/approval-of-indicator-results machinery appears in its public positioning.
- The market treats it as the collection layer that M&E platforms integrate with: TolaData advertises KoboToolbox/SurveyCTO integrations; DevResults KB has an "Import Data From KoboToolbox" article; ActivityInfo publishes a comparison blog and an XLSForm migration guide.
- Conclusion: KoboToolbox-class tools sit one layer below the M&E platform. (Supports the boundary finding below.)

---

## Cross-product Comparison

| Structure | ActivityInfo | DevResults | TolaData | LogAlto | Evidence |
|---|---|---|---|---|---|
| Results framework / logframe as first-class object | realized via database templates + results-framework use case (build-your-own) | first-class: multiple frameworks, code-hierarchies, deactivate/archive | first-class: levels (goal/impact, outcome, output, activities) with cause-effect | first-class: logframe module + Excel import | B (3 explicit; 1 build-your-own) |
| Indicator as defined record with code + measurement metadata | as form/record patterns + indicator templates | full definition page (code, name, type, unit, source, disaggregations, PMP-style narrative metadata) | indicator plan per framework level | indicator form (code, description, baseline, targets, type, configurable fields) | B |
| Baseline / target semantics | templates; claims track outputs→impact | explicit: global vs project targets; incremental vs cumulative; auto progress-to-target | part of indicator plan | explicit: baseline and target(s) in indicator form; targets updatable | B (3 explicit) |
| Reporting periods / periodic actuals | sub-form example: "collecting indicator results on a monthly basis" | "once per reporting period"; per-project per-period submission status machine | implicit in workflow (plan→collect→manage→visualize) | actuals per period, cumulative or per-period | B (2 explicit) |
| Multiple data sources: direct entry / from records / import / formula | all (forms, imports, formulas) | all three named data sources | built-in forms + external integrations + data tables | direct entry, form-linked calculation, Excel import | B |
| Disaggregation (incl. geographic) | reference fields to geographic lists; maps | optional + one required geographic disaggregation; parallel or cross | claimed in dashboards/aggregation | values, baselines, targets disaggregable; combined or parallel | B |
| Data quality workflow (validation/approval/lock/audit) | validation + relevance rules; lock after donor reporting; permissions | full status machine No Data→In Progress→Submitted→Returned→Approved + role gates + discussion audit trail | "route approvals" (lighter evidence) | history + comments (lighter evidence) | gradient: strongest in DevResults, present in ActivityInfo, thinner in TolaData/LogAlto public docs |
| Aggregation across projects/programs/org levels | "project to global level"; hundreds of projects template | multi-framework + multi-project reporting | portfolio aggregation feature | project → programme results framework → org units | B |
| Donor/oversight reporting surface | report designer, dashboards, integrations | reporting tools, IATI export, enterprise publishing | dashboards shared with funders, IATI | dashboards, reports; lessons learned | B |
| Collection substrate bundled vs integrated | bundled (web+mobile+offline) | bundled (data tables) + KoboToolbox import | both (built-in forms + integrations) | bundled (forms/surveys/mobile) | variant: bundled vs integrated |
| Evaluation studies executed in-product | not claimed | not claimed | not claimed | lessons learned/success stories only | A (absence) — the "E" is served by evidence organization, not by in-product study execution |

## Canonical Model (working synthesis, pre-L0)

```text
Program / Project portfolio (the funded work being monitored)
└── Results framework (planned results hierarchy: goal/impact → outcome → output)
    └── Indicator (measurement definition: code, definition, unit, type,
        baseline, targets, disaggregations, data source/method, attribution)
        └── Indicator actuals per reporting period
            ← fed by: direct entry / collected records / imports / formulas
            ← quality-controlled: validation → submission → approval → lock → audit trail
            → aggregated: by period, geography, project, disaggregation category, org unit
            → reported: progress-to-target views, dashboards, donor reports
```

## Abstraction Hierarchy

### L0 — Defining Invariant (candidate)

Three jointly-held structures, plus the domain binding:

1. **The planned-results structure of record.** The program's intended results held as structured, persistent records organized as a results hierarchy (results framework / logframe class), with measurable indicators attached to the results. Remove it → a survey/data-collection tool or a project tracker; the "E" and the "results" semantics disappear.
2. **Indicator actuals recorded over time against that plan.** Measured values for the indicators, accumulated per reporting period (and commonly per project/geography/disaggregation), forming the monitoring record. Remove it → a planning document (logframe-on-paper alone) with nothing monitored.
3. **The accountability reporting loop.** The accumulated record is aggregated and surfaced as progress-vs-plan views and outputs directed at oversight parties (donors, funders, governing management) — the purpose for which the record is maintained. Remove it → an analyst's private data store/spreadsheet; the platform's reason to exist disappears.

Domain binding: the subject is social/development program results (humanitarian, development, nonprofit, public-interest programs) operating under funder/oversight accountability. Remove the binding → generic BI/reporting or government performance machinery.

Jointly-held analysis:
- 1 alone = logframe/documentation tool (or a diagram of intent).
- 2 without 1 = disconnected data store / data-collection territory.
- 3 without 1+2 = reporting shell / BI dashboard.
- 1+2 without 3 = a monitored indicator spreadsheet — the analog pre-history's intermediate stage, not yet the institutionalized Type.
- Historical check: paper-era M&E — a logframe document in the project proposal + an indicator tracking spreadsheet with quarterly actuals + quarterly progress reports to the donor — satisfies all three legs (the spreadsheet holds the plan's reference values; periodic actuals are recorded; reports go to the funder). A results framework with no data fails leg 2; raw field data with no framework fails leg 1; both with no reporting loop fail leg 3. The definition names no mobile forms, cloud, dashboards, IATI, or specific framework vocabularies (goal/outcome/output naming varies by organization — TolaData states this explicitly).

### L1 — Common Mature Structure (evidence: B)

- Program/project as the anchoring container, with indicator-project assignment and per-project reporting; portfolio/program-level aggregation above projects.
- Indicator reference metadata as a managed record: code, definition, justification, data acquisition, data quality notes, methodology (the PMP / indicator reference sheet heritage).
- Baselines and targets on indicators (global and project-level; incremental and cumulative styles — the two styles documented by two products independently).
- Disaggregation as a first-class concept (categories like sex/age; combined or parallel), including disaggregated baselines/targets (LogAlto) and a required geographic disaggregation (DevResults).
- Multiple actuals data sources: direct aggregated entry, computation from collected records, imports, formula indicators.
- Validation rules and quality workflow (submission → approval → lock; discussion/audit trail).
- Dashboards, charting, progress-to-target visualization; report export; Excel interop both directions.
- Role-based access separating data entry (often partners/field staff) from review/approval and from design/administration.
- Geographic dimension: locations/geographies as reference data linking records and indicator data to maps.

### L2 — Variant / Optional Structure

- Construction philosophy: fixed M&E schema (DevResults, LogAlto) vs build-your-own database (ActivityInfo) vs workflow suite (TolaData).
- Collection substrate: bundled mobile/offline collection vs integration with external collection tools (KoboToolbox, SurveyCTO, Excel/Sheets).
- Standards posture: IATI export/publishing (DevResults, TolaData), donor-specific frameworks (PMP-style; foreign-assistance frameworks in DevResults).
- Scale posture: single-project deployments vs enterprise multi-country sites with publishing layers.
- Beneficiary/case-level data: some platforms support person-level records and case management as an adjacent use (ActivityInfo has a dedicated case-management use case; DevResults/TolaData ingest case-level records) — held as variant, not core.
- Deployment: cloud SaaS vs self-managed server (ActivityInfo); government-security postures (FedRAMP for DevResults).
- Language/multilingual databases (ActivityInfo multilingual documentation; LogAlto EN/FR/ES).
- Learning-side features: lessons learned, success stories, qualitative inventories, narrative responses.
- AI assistance (TolaData roadmap; ActivityInfo MCP integration) — emerging, not structural.

### L3 — Vendor-specific (stays in Research Notes)

- DevResults: five-status naming (No Data / In Progress / Submitted / Returned / Approved); "Submit Indicator Results" / "Approve Indicator Results" role names; MultiMatrix reporting tool; Visio-based framework visualization recipe; "Results are reported separately for each project" toggle.
- ActivityInfo: Database→Folder→Form→Record→Field hierarchy; CUID record identifiers; sub-form vs reference field duality; ISO 27001 marketing; specific integration catalog (R package, ArcGIS, MCP).
- TolaData: named module pages (Portfolio Aggregation, Standards & Compliance); AI roadmap items; corporate history (GFA → Athena Infonomics).
- LogAlto: "3-4 weeks to be up and running" deployment claim; plan tiers; Devalto Technologies parentage; numerator/denominator indicator type as a named type.
- KoboToolbox: XLSForm ecosystem, 35,000+ organizations claim — boundary sample only.

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical document; the five-status lifecycle vocabulary is generalized to "submission → approval → lock with an audit trail" in the final document.

## Rejected Findings

1. **"An M&E platform is a data collection tool."** Rejected. Collection-only tools (KoboToolbox-class) lack the planned-results structure, target/baseline semantics, and the accountability reporting loop; M&E platforms treat collection as a feeding layer (all four sampled platforms either bundle collection or integrate with collection tools). The market itself separates the two (vendor comparison content on all sides).
2. **"Evaluations are conducted in the platform."** Rejected as a structural claim. No sampled product claims to execute evaluation studies; the platforms organize evidence, indicators, and records that evaluations draw on, and optionally hold lessons-learned content. The "E" in M&E is served indirectly.
3. **"Disaggregation is definitional."** Rejected from L0 (held L1). LogAlto asserts no good indicator tracker is complete without it, but the paper-era pre-history satisfies the Type without structured disaggregation.
4. **"Mobile/offline field collection is definitional."** Rejected from L0. It is the current dominant implementation of the collection substrate, not the Type.
5. **"Specific result-level vocabulary (goal/outcome/output/impact) is definitional."** Rejected. TolaData explicitly states organizations define their own levels; DevResults maps level names to IATI types only for publishing; logframe vocabulary varies.
6. **"M&E platform = nonprofit CRM with reporting."** Rejected. No sampled platform centers constituent/donor relationship records; funding parties appear as attribution/reporting context, not as CRM objects.

## Boundary Findings

1. **vs Survey Platform / Online Form Builder / data collection tools (KoboToolbox-class).** Collection tools center the form and the field-collection workflow; they have no results framework object, no indicator-target semantics, no per-period submission/approval machinery for indicator results. Seam test: remove the results framework + indicator actuals + reporting loop → a collection tool remains; remove form design as the center → M&E platform remains. Confirmed from both directions (KoboToolbox positioning; ActivityInfo's own comparison article; DevResults/TolaData integration pages treating Kobo as an input).
2. **vs Social Impact Measurement (§25 sibling leaf, unprocessed).** Both live in the same sector. Working distinction pending that pass: M&E Platform = the machinery-first system of record (framework + indicator data + quality workflow + reporting infrastructure) that operationalizes monitoring; Social Impact Measurement = the measurement-practice orientation (methodology, outcome/impact framing, learning). M&E platforms market "impact measurement" as a use case (ActivityInfo has a dedicated page), so the seam is center-of-gravity, not feature presence — JOINT REVIEW RECOMMENDED when that leaf is processed.
3. **vs Nonprofit Case Management / Beneficiary Management.** Case management centers person-level service episodes; M&E platforms aggregate case-level data into indicators (ActivityInfo explicitly calculates indicators from beneficiary-level data) but the managed object of record is the indicator, not the person's case. Remove indicator semantics → case management remains.
4. **vs Nonprofit Grant Management.** Grant management centers the money (awards, compliance, financial reporting to funders); M&E platforms center the results. Donors appear in M&E platforms as reporting recipients/attribution, not as financial records. (ActivityInfo ships a separate grant-management use case — vendor confirms the seam.)
5. **vs BI Platform / Dashboard Platform / Reporting Platform.** BI is domain-agnostic analysis over arbitrary data; M&E platforms carry program results semantics (frameworks, indicators, targets, reporting periods, disaggregation standards, submission workflows) as built-in furniture. Remove the program semantics → BI.
6. **vs Government Performance Management (§24).** The machinery overlaps (indicators, targets, periodic reporting); the institutional context differs (donor-funded programs with implementing partners vs government bodies' own performance regimes). Held as adjacent machinery-first sibling; recorded for that pass.
7. **vs Project Management / Nonprofit Program Management.** Project management centers execution (schedules, tasks, budgets); M&E centers measured results against planned results. M&E platforms hold activities as attribution context and reporting units, not as schedulable work.
8. **Internal seam — collection substrate.** Bundled collection (ActivityInfo/LogAlto mobile forms) vs integrated external collection (TolaData's Kobo/SurveyCTO connectors, DevResults' Kobo import) is a packaging variant, not a Type boundary.

## Uncertainties

- TolaData and LogAlto evidence rests on official product/feature pages rather than fetched help-center articles; their data-quality workflows may be deeper (or shallower) than the pages show. Claims about them are kept at feature-page strength.
- DevResults Reporting Periods and Projects articles were not individually fetched; periodicity and project-container semantics are inferred from articles that reference them (indicator definition, targets, submission process). Confidence high but indirect.
- The boundary vs Social Impact Measurement is held as a working distinction; it cannot be finalized until that leaf is researched.
- Regional players (e.g., francophone-sector M&E tools, national HMIS like DHIS2 used for program M&E) were not sampled; DHIS2 in particular is a health-MIS Type whose M&E usage is an overlap zone not researched here.
- Evaluation-side workflows (evaluation management, TOR tracking) were not found in any sampled product; absence is evidence-based but the negative claim is limited to the sample.

## Final Synthesis

A Monitoring & Evaluation Platform is the program-results system of record for organizations that implement funded social/development/humanitarian programs. Its defining core is three jointly-held structures: (1) the program's planned results held as a structured framework of record with measurable indicators attached; (2) indicator actuals accumulated per reporting period against that plan's reference values; (3) the accountability loop that aggregates and reports progress-vs-plan to oversight parties. Around that core, mature products add the program/project container with per-project attribution and multi-level aggregation, indicator reference metadata (baselines, targets, disaggregations, methodology), a multi-source actuals pipeline (direct entry, computed from collected records, imports, formulas), a quality workflow (validation → submission → approval → lock, with audit trail), role separation between field/partner entry and review, and progress/donor reporting surfaces. Construction philosophy ranges from fixed M&E schemas to build-your-own relational databases; the collection substrate is either bundled or integrated; standards and security postures vary. The Type is bounded below by data-collection tools, sideways by case management, grant management, and BI, and shares machinery with government performance management and the sibling Social Impact Measurement leaf.
