# Research Notes — Product Test Management

Research date: 2026-09-09

## Research Goal

Establish what "Product Test Management" is as an Application Type in directory §16 (Engineering, Manufacturing & Industrial): what objects exist inside it, who uses it, how the testing loop works, what rules and states matter, and where its boundaries lie against neighboring Types — Software Test Management (§12), Industrial Laboratory Management (§16, processed), Inspection & Metrology Software (§16, processed), Engineering Requirements Management (§16, processed), PLM (§16, processed), Manufacturing QMS / Reliability Management / SPC (§16, unprocessed), Test Automation Platform (§12, unprocessed), Validation Management (§22, unprocessed).

The directory places this leaf in the engineering/manufacturing section, not in §12 (Software Development), so the working hypothesis is that this is the test management of **physical/engineered products during development** (design verification / product validation), not software QA.

## Initial Boundary (hypothesis before research)

- Core guess: the system of record for planning, defining, executing, and tracking tests of a product under development — test plans, test cases/procedures, test executions against specific units, results and verdicts, defects raised from failures, and coverage/sign-off against requirements.
- Likely users: test engineers, development engineers, V&V engineers, quality engineers, program managers.
- Likely confusion points:
  - Software Test Management (§12) — same object family (test cases, runs), different subject and ecosystem.
  - Industrial Laboratory Management (§16, processed) — routine QC of production materials vs engineering verification of products under development. That pass left a forward flag: "vs Product Test Management — engineering/DV/PV verification testing vs routine QC of production materials."
  - Inspection & Metrology Software (§16, processed) — that pass drew the seam: "product tests exercise *function and performance*; this Type verifies *geometry* against declared nominal."
  - Engineering Requirements Management (§16, processed) — the requirement record and its verification-method links vs the test definition/execution/verdict side.
  - PLM (§16, processed) — product record/BOM/change vs the test lifecycle; test modules observed as packaging.
  - Test-lab / DAQ execution software (Simcenter Testlab-class, NI TestStand-class) — execution engines and measurement systems, expected adjacent.

## Research Questions

1. What objects exist (test plan, test case/procedure, test run, test item/unit under test, results, defects)?
2. How do tests relate to requirements — is requirement linkage definitional or a common implementation?
3. How is execution recorded for physical tests (manual entry, offline logging, instrument/automation integration)?
4. What lifecycle/states do tests and runs have, and what roles gate them?
5. What happens to failed tests (defects, re-test, change actions)?
6. What are the deliverables (coverage reports, test reports, sign-off evidence)?
7. Is this a distinct market category, a module of PLM/ALM, or a variant of Software Test Management?
8. Would older/regional/paper-era product test practice still fit the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

1. **Jama Connect** (Jama Software) — requirements-centric engineering management platform; test management positioned as "requirements-based test management" for regulated multidisciplinary products (medical devices, automotive, aerospace, electronics). Customer tier: mid-market to enterprise regulated programs. *Best documentation access: official user guide (Tier 1) + product pages (Tier 2).*
2. **Polarion QA** (Siemens) — ALM-integrated test management ("Polarion QA"), used by enterprise QA departments in automotive and other compliance-heavy product development. Tier: enterprise. *Tier 2 product pages reachable; deep help docs not fetched.*
3. **Codebeamer** (PTC) — ALM platform with "QA and Test Management" as a named core capability; industry solutions for automotive, medical, aviation, pharma. Tier: mid-market to enterprise suppliers. *Tier 2 only; help-center test-management pages unreachable (see Sources).*
4. **Greenlight Guru** — medical-device eQMS whose design-control module manages verification and validation testing as part of the design history file. Tier: medical device companies (start-up to enterprise). *Tier 2 product pages reachable.*

Checked but not sampled: **Siemens Teamcenter** (PLM suite; product page surfaces no dedicated test-management module and deep docs were not reachable — recorded as a sourcing limitation, not a finding); **NI TestStand / Simcenter Testlab-class** execution software (adjacent pole; public doc URLs not located within budget — boundary note only, low assertion strength).

## Sources

- Jama Connect Help — "Testing" (user guide, Tier 1): https://help.jamasoftware.com/ah/en/getting-to-know-jama-connect-features/testing.html
- Jama Connect Help — test objects and workflow pages surfaced via support-center search (test cases, test plans, test cycles, test runs, test-run item, test-case status): https://help.jamasoftware.com/ah/en/test/... , https://support.jamasoftware.com/hc/en-us/search?query=test+plan+test+case+test+run
- Jama Software — Test Management solution page (Tier 2): https://www.jamasoftware.com/solutions/test-management/
- Jama Software — Automotive solution page (Tier 2): https://www.jamasoftware.com/solutions/automotive/
- Siemens — Polarion product page (Tier 2): https://www.siemens.com/en-us/products/polarion/
- Siemens — Polarion QA product page (Tier 2): https://www.siemens.com/en-us/products/polarion/qa/
- PTC — Codebeamer site home and Help Center welcome (Tier 2): https://codebeamer.com/ , https://support.ptc.com/help/codebeamer/r3.3/en/codebeamer/codebeamer_welcome.html
- Greenlight Guru — Design Control Software page and platform home (Tier 2): https://www.greenlight.guru/design-control-software , https://www.greenlight.guru/
- Siemens — Teamcenter product page (checked; no test module surfaced): https://www.siemens.com/en-us/products/teamcenter/

**Source-access limitations:**

- Codebeamer's help-center test-management section could not be located (two URL attempts returned 404; the wiki root rendered only the login/home page). Codebeamer evidence is therefore Tier 2 (positioning and capability naming) and is used at reduced strength.
- Siemens deep documentation (docs.sw.siemens.com / support portal) was not reachable within budget; Polarion evidence is Tier 2 product-page level. Teamcenter's public product page does not surface a test-management module; no claim about PLM-embedded test modules is made from it.
- NI / Simcenter test-execution software pages were not located within budget; the execution-layer boundary is stated at low assertion strength.
- No numeric limits, default settings, or exhaustive state lists are asserted anywhere below.

## Product A — Jama Connect

### Key observations (evidence layer A unless noted)

From the official user guide "Testing" page (Tier 1):

- Positioning: "use Jama Connect test capabilities to guide your teams through the testing process, so you can validate and verify your products and systems."
- Object model, in the product's own terms:
  - **Test case** — lives within a project; "contains the steps a tester or script uses to validate and verify associated requirements"; can be organized into a separate test-suite project or alongside requirements; can be associated with one or multiple test plans.
  - **Test plan** — lives within a project; "contains a description of the strategy and objective for testing a system or subsystem"; can include test cases from the same or different projects.
  - **Test group** — optional organization of test cases into collections within a plan.
  - **Test cycle** — lives within a plan; "a container to organize a specific set of cases that are executed together. When a case is associated with a cycle, a corresponding test run is created in that cycle."
  - **Test run** — lives within a cycle; "the record of results for an executed test case."
  - **Defect** — lives within a project; "a record of an error or defect that was discovered while executing a test run. When a defect is logged during test execution, it is traced to the originating test run to upstream test cases and requirements through the relationship configuration."
- Typical workflow (five steps, product's own framing):
  1. **Create coverage** — create test cases to validate upstream requirements; create relationships between test cases and requirements; use the Trace View to check for coverage gaps.
  2. **Devise a plan** — create a test plan describing which requirements need to be tested and the strategy; associate test cases; optionally group them.
  3. **Execute the plan** — create one or multiple test cycles; associate all or a subset of cases; a test run is created per associated case; execute the runs.
  4. **Monitor progress** — filters, dashboards, and trace views for requirement coverage, per-cycle testing progress, and high-priority defects.
  5. **Review and report results** — send the entire test plan or a single cycle to review; generate reports ("Test Details Grouped by Test Cycle", "Test Details Grouped by Test Case").
- From the support KB (Tier 1): "Test Plans have no status. Test Case Status is a field determined by the lowest status of the most recent Test Run" — i.e., case status is *derived from execution*, not manually declared. The test-run item page documents that a run is automatically associated with its originating test case, test cycle, test group, and test plan ("these associations contextualize" the run).
- From the Test Management solution page (Tier 2): "define, organize, and execute requirements-based test plans and test cases"; "perform manual testing, and integrate with trusted test execution and automation solutions"; "trace failed tests to new and existing defects"; "customize reports for proof of regulatory compliance"; "reuse validated requirements... when testing consistent features across products"; dashboards to "monitor test progress and requirements to identify roadblocks"; customer quote (Össur, a physical medical-device maker) about tracking time spent on test cases and estimating remaining testing time.
- From the Automotive solution page (Tier 2): "Pre-built workflows connect requirements, risks, tests and validation in one traceable digital thread"; "built-in traceability and compliance reporting simplify audits and demonstrate verification across every requirement"; standards named: ISO 26262, ASPICE, ISO/SAE 21434; sub-industries include EV hardware, ADAS, automotive semiconductors; dSPACE (automotive engineering supplier) is a customer.

### Interpretation

Jama realizes the Type as a **requirements-anchored verification loop**: tests exist to verify requirements; execution produces runs; run outcomes roll up (derived status) to cases and coverage; failures become defects traced back through runs to requirements; plans/cycles structure the effort; reviews and reports produce the compliance evidence. Physical products (medical devices, vehicles) are first-class subjects; execution is commonly manual with automation-tool integration for results.

## Product B — Polarion QA (Siemens)

### Key observations (Tier 2)

- Positioning: "Design, coordinate and track all your test management activities in a single, collaborative QA environment... centralizing every testing activity in one repository with multi-directional traceability."
- Enterprise framing: "Enterprise QA departments can run unlimited number of projects adhering to very structured testing cycles, combined with a diverse ecosystem of both automated and manual testing activities, while keeping everything in sync and fully traceable."
- Test construction: "Create test cases and easily link them to their corresponding work items such as requirements, change requests, other test cases and more."
- **Parameterized test items**: "Parameterize your test steps to separate a test specification and test items configuration so you can execute the same procedure several times to fully cover your complex test conditions." — direct evidence that the *item under test* (which unit/variant/configuration) is a first-class dimension separate from the test procedure.
- Execution: "Execute test cases with online test execution panel or offline by exporting to MS Excel and importing test results back" — an offline round-trip for logging results, characteristic of physical/bench testing away from the desk.
- Automation: "Leverage automated test cases as a 'first-class citizen.' Integrate with third-party test automation tools via Open API... be import-ready for any test results in xUnit file format."
- Failure handling: "Track issues automatically on any test failure, no matter if test is manual or automated, performed in Polarion or in a third-party tool"; "Automatically create bug reports and tasks for developers based on test failures."
- Traceability depth: "Build traceability from requirements, not just to test cases but individual test records."
- Governance: workflows that "enforce how and when they move from state to state based on definable rules, with full audit trails, electronic signature and security"; "Accurately and consistently automate verification and verification tasks with electronic signatures"; compliance-based templates; FMEA risk templates.
- Analysis: "Analyze the quality of the requirements by measuring the number of issues and change requests linked to requirements."

### Interpretation

Polarion realizes the same loop inside an ALM platform: test cases as linked work items, execution as test records (online or offline), failures auto-raised as issues, traceability from requirements down to individual test records, e-signature governance. The parameterized test-item configuration is the clearest cross-product evidence that "what was tested" is structurally distinct from "what was done".

## Product C — Codebeamer (PTC)

### Key observations (Tier 2, reduced strength)

- The vendor's own site names **"QA and Test Management"** as one of the platform's core capabilities, alongside Requirements Management, Software Development, Risk Management, and Variants Management.
- The Help Center welcome describes Codebeamer as "an advanced ALM solution that enables organizations to manage the entire software and product development lifecycle, from requirements to release, within a single integrated platform."
- Industry-specific solutions named: medical, automotive, aviation, pharmaceutical — i.e., regulated physical-product development programs.
- Detailed test-management mechanics (test case/run/plan objects, execution recording) could not be verified from official documentation (see Source-access limitations). No specific object model is claimed for this product.

### Interpretation

Codebeamer confirms the market pattern — test management as a named core capability of an ALM platform serving regulated product development — but contributes no object-level evidence in this pass.

## Product D — Greenlight Guru

### Key observations (Tier 2)

- Positioning: medical-device platform; the Product Development module "connect[s] design, risk, and AI-powered traceability as you build"; "Link needs, requirements, and verification to design controls."
- Design-control page: "Document, track, and trace all aspects of your design control process"; "Our multi-level traceability matrix is the most powerful and flexible way for you to manage your complex medical device products, link documents, conduct project reviews, and generate a design history file."
- Verification/testing as part of design controls: "Collaborate with your R&D team on verification and validation testing" (product-team benefit); the traceability matrix "automatically links user needs to design inputs, outputs, verification, and validation activities."
- Governance/evidence: "Provide auditors and inspectors with the signatures and objective evidence they require — on-demand"; design reviews tracked "with Part 11 compliant workflows"; "auto-generating, auto-updating DDF" for 21 CFR 820.30 / ISO 13485 compliance.
- Multi-component products: "manage interrelated hardware, firmware, and software elements while maintaining full traceability across systems" (SaMD and multi-component devices).

### Interpretation

Greenlight Guru realizes the Type from the **quality-system/design-control** side: verification and validation testing are managed as traceable design-control activities whose recorded outcomes are the objective evidence regulators audit. The test objects are less prominent than the traceability matrix, but the loop (requirement/design input → verification activity → recorded result → evidence) is the same shape. This is the medical-device regime variant of the Type.

## Cross-product Comparison

| Dimension | Jama Connect | Polarion QA | Codebeamer | Greenlight Guru |
|---|---|---|---|---|
| Host substrate | requirements/engineering management platform | ALM platform (QA module) | ALM platform | medical-device eQMS (design-control module) |
| Test definition object | Test case (steps for tester or script) | Test case (linked work item; parameterized steps) | named capability; detail unverified | verification/validation activities within design controls |
| Plan/campaign container | Test plan → test group → test cycle | "structured testing cycles"; projects | named capability; detail unverified | design-control structure / traceability matrix |
| Execution record | Test run ("record of results for an executed test case"), auto-associated to case/cycle/group/plan | test records; online execution panel or offline Excel round-trip | named capability; detail unverified | recorded verification activities as objective evidence |
| Unit-under-test dimension | run contextualized by associations | parameterized test items (spec vs item configuration) | — | design outputs / configurations linked |
| Requirement linkage | relationships test case ↔ requirement; Trace View coverage gaps | traceability from requirements to test cases and individual test records | requirements management core capability | user needs → design inputs → outputs → verification/validation matrix |
| Failure handling | defect logged during run, traced to run → cases → requirements | issues auto-tracked on any failure; bug reports/tasks auto-created | — | (quality events handled in the QMS side) |
| Status model | case status derived from most recent run status; plans have no status | workflow states with definable rules | — | review/approval workflows |
| Review / sign-off | send plan or cycle to review; reports | e-signatures for verification tasks; audit trails | — | Part 11 e-signature design reviews; auditor-facing evidence |
| Execution posture | manual testing + automation integrations | manual + automated first-class; xUnit import; third-party tools | — | R&D collaboration on V&V testing |
| Deliverables | compliance reports; dashboards; trace views | reports, dashboards, audit trail | — | design history file; traceability matrix; audit-ready evidence |
| Industry regimes | medical devices, automotive (ISO 26262/ASPICE/21434), aerospace, electronics | automotive and compliance-heavy product development | automotive, medical, aviation, pharma | medical devices (FDA 820.30, ISO 13485, ISO 14971) |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The test of record** — a persistent, identified definition of a test: what to do (procedure/steps) and the basis for judgment (expected outcomes / acceptance criteria). Remove → ad-hoc experimentation or a procedure/SOP library with no testing memory.
2. **The execution record (run)** — a recorded execution of a test against a specific test item (unit, prototype, build, configuration) in a specific context, capturing the observed results and a verdict (pass/fail or equivalent) evaluated against the test's acceptance basis. Remove → a procedure library, or a results spreadsheet with no linkage to what was supposed to be verified.
3. **The managed testing effort** — tests organized into a planned structure (plans/campaigns/cycles) whose execution is tracked to completion, with progress and outcomes surfaced (status, coverage, reports) so the testing effort can be managed and its evidence delivered. Remove → a test log (record-keeping without management), or a schedule with nothing executed.

Jointly-held load-bearing: 1 alone = procedure library; 2 without 1 = lab notebook/results log; 3 without 1+2 = test schedule with nothing behind it; 1+2 without 3 = test log, not management; 1+3 without 2 = planning tool with no execution; 2+3 without 1 = ad-hoc runs with no reusable definitions.

### L1 — Common Mature Structure

- **Requirement linkage and coverage** — tests linked to the requirements (or design inputs/user needs) they verify; coverage views exposing unverified requirements; verification matrices. *Dominant modern organizing structure — the market's own vocabulary is "requirements-based test management" — but not definitional: paper-era test plans keyed to design targets and standards satisfy the Type without formal requirement records.*
- **Defect/issue loop** — failures raise tracked defects/issues linked back to the run, the test, and the requirement; re-test after fix.
- **Review, approval, and e-signature** — test plans and results reviewed/approved; signatures as audit evidence.
- **Test-item context** — which unit/prototype/build/variant/configuration was tested; parameterized test items letting one procedure cover many conditions.
- **Reports and dashboards** — progress, coverage, and results reports for design reviews, audits, and regulatory submissions.
- **Reuse** — test-case libraries, templates, cross-project/product-line reuse.
- **Execution-tool integration** — results imported from specialized test/automation tools; offline logging round-trips (e.g., spreadsheet export/import).
- **Roles and permissions** — tester, test lead, reviewer/approver; who may execute, sign, configure.

### L2 — Variant / Optional Structure

- **Industry regime** — automotive (DVP&R practice, ISO 26262/ASPICE evidence), medical device (design controls, DHF, FDA 21 CFR 820.30 / Part 11), aerospace/defense, general industrial. The core holds across all; the vocabulary and evidence obligations differ.
- **Verification vs validation emphasis** (DV/PV) — same machinery, different intent and audience.
- **Host substrate** — standalone requirements/ALM module vs eQMS design-control module vs PLM-embedded module (PLM-embedded evidence not directly observed in this pass).
- **Execution posture** — manual-first with offline logging vs automation-integrated with results import.
- **Measurement depth** — from pass/fail checklists to captured measurement data; deep measurement/acquisition usually lives in adjacent test-lab/DAQ software.
- **Deployment** — cloud SaaS vs on-premises.

### L3 — Vendor-specific (Research Notes only)

- Jama: Test Cycle/Test Group naming; case status derived from "lowest status of the most recent Test Run"; Live Traceability branding; test-suite projects separate from requirements projects.
- Polarion: LiveDocs specification documents; Time Machine historical browsing; HP Quality Center connector; xUnit import; FMEA templates; 100+ QA-centric integrations claim.
- Greenlight Guru: auto-generating design history file (DDF); AI suggestions/predictive verifiability checks; Jira integration for software teams; SaMD-specific design workflow.
- Codebeamer: tracker-based item model (not verified in this pass).

## Vendor-specific Findings

See L3. None promoted to the canonical model.

## Boundary Findings

1. **vs Software Test Management (§12, unprocessed)** — the two leaves share the generic test-management shape (test definitions, runs, verdicts, plans). The seam this pass draws: the §16 leaf is the **product/engineering-program instance** — verification of engineered products (hardware + embedded software) against product requirements, with regulatory/design-review sign-off as the deliverable; the §12 leaf is expected to be the **software-team instance** — the application build/release cycle, automation frameworks, CI. The market itself sells one test-management capability across both (Jama, Polarion, Codebeamer serve software and hardware programs with the same objects), so these are sibling domain instances of one family, analogous to the LIMS/industrial-lab precedent. Forward flag for the software-test-management pass; recommend joint review.
2. **vs Industrial Laboratory Management (§16, processed)** — DISCHARGES that pass's forward flag. Seam: engineering verification testing of products under development (tests anchored to requirements/design intent; deliverable = coverage/sign-off evidence) vs routine QC testing of production materials (samples anchored to production lots; deliverable = lot disposition/CoA). The industrial-lab pass's characterization ("engineering/DV/PV verification testing vs routine QC") is confirmed by this pass's evidence.
3. **vs Inspection & Metrology Software (§16, processed)** — consistent with that pass's own seam: product tests exercise function and performance; metrology verifies geometry against declared nominal.
4. **vs Engineering Requirements Management (§16, processed)** — the requirements Type holds the requirement record, its structure, and its traceability/coverage machinery; this Type holds the test definition, execution, and verdict. The verification-method/test-case link is the seam; requirements platforms bundle both sides as packaging, but the center of gravity differs (requirement record vs test execution).
5. **vs PLM (§16, processed)** — PLM holds the product record, structure, and change; test management may attach to the product record as a module, but the test lifecycle is this Type's center. PLM-embedded test modules were not directly observed (sourcing limitation); the seam is drawn from the PLM pass's own packaging observation.
6. **vs Manufacturing QMS (§16, unprocessed)** — expected seam: the plant's quality system of record (documents, deviations, CAPA, audits) vs development-phase verification testing. Forward flag.
7. **vs Reliability Management (§16, unprocessed)** — expected seam: reliability engineering (durability prediction, failure analysis) vs the test management that plans and records durability tests as one test category. Forward flag.
8. **vs Test Automation Platform (§12, unprocessed)** — expected seam: automation frameworks author/execute automated tests; test management plans, tracks, records, and proves. Integration (results import) is the observed bridge. Forward flag.
9. **vs Validation Management (§22, unprocessed)** — expected seam: process/equipment/computerized-system validation (IQ/OQ/PQ) vs product design verification/validation. Forward flag.
10. **vs test-lab / DAQ execution software (Simcenter Testlab-class, NI TestStand-class)** — execution engines and measurement systems for physical tests; expected adjacent (they execute and acquire; this Type plans, tracks, and proves). Evidence not reachable in this pass; low assertion strength, recorded as a boundary note only.

## Uncertainties

- The PLM-embedded pole (Teamcenter/ENOVIA-class test modules) could not be verified from public sources; the "host substrate" variant list includes it on market-structure reasoning, not direct evidence.
- Codebeamer's object-level test mechanics are unverified; it is used only as Tier-2 confirmation of the market pattern.
- The exact relationship between this Type and Software Test Management (one family with two instances vs two Types) deserves joint review when the §12 leaf is processed.
- Whether deep physical-measurement capture (test-cell/DAQ data) should be treated as part of this Type or firmly adjacent could not be settled from reachable sources; this pass treats it as adjacent with integration.
- Automotive DVP&R as a named artifact was not directly observed on the fetched pages (the automotive page names standards and workflows, not the artifact); DVP&R is therefore mentioned only as industry practice context, not as a product feature claim.

## Final Synthesis

Product Test Management is the product-development organization's system of record for the tests that verify and validate a product under development. Its defining core is three jointly-held structures: the **test of record** (a persistent identified test definition — procedure plus acceptance basis), the **execution record** (a run of that test against a specific test item, capturing results and a verdict), and the **managed testing effort** (tests organized into plans/campaigns whose execution is tracked and reported). Around that core, mature products add requirement linkage with coverage views, a defect loop from failures, review/sign-off with e-signatures, test-item context, reports and dashboards, reuse, and integration with execution tooling. The market realizes the Type as requirements/ALM platforms' test management (Jama Connect, Polarion QA, Codebeamer), medical-device design-control modules (Greenlight Guru), and — per market structure, not directly observed — PLM-embedded test modules. The Type is distinct from routine production QC (Industrial Laboratory Management), geometry verification (Inspection & Metrology), the requirement record itself (Engineering Requirements Management), and the software-team instance of test management (§12 sibling, joint review recommended).
