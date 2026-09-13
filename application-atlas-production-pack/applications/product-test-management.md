# Product Test Management

## Overview

A **Product Test Management** application is the product-development organization's system of record for the tests that verify and validate a product under development. It holds each test as a persistent, identified definition — what to do and what outcome counts as passing — records each execution of a test against a specific unit or configuration together with its results and verdict, and organizes the whole testing effort into plans whose progress, coverage, and outcomes are tracked and reported as evidence for design reviews, audits, and regulatory submissions.

The defining core is small:

```text
Test of record
  (persistent identified test definition:
   procedure / steps + acceptance basis — what result counts as passing)
└── Execution record (run)
    (a recorded execution of that test against a specific test item —
     unit, prototype, build, configuration — with observed results
     and a verdict)
└── Managed testing effort
    (tests organized into plans / campaigns / cycles,
     execution tracked to completion, progress and outcomes
     surfaced as status, coverage, and reports)
```

Everything else commonly associated with these products — requirement linkage and coverage matrices, defect tracking from failed tests, review and electronic sign-off, test-case libraries and reuse, dashboards, integration with test automation and measurement tools — is widespread in current products but is not what makes the product a test management system. Disciplined paper-era practice — a written test plan, numbered test procedures, filled-in test logs, and signed test reports — exhibits the same three-part core with none of the modern machinery.

When the subject shifts to routine testing of production materials against specifications, the product is drifting toward a different Application Type (Industrial Laboratory Management); when it shifts to verifying part geometry against a nominal model, that is Inspection & Metrology; when it shifts to holding the requirement statements themselves, that is Engineering Requirements Management.

## Users & Context

Primary users are the engineering roles on a product-development program:

- **test engineers / V&V engineers** — author test cases and procedures, plan test campaigns, execute or supervise execution, record results and verdicts
- **development engineers** — see which of their requirements have been verified, respond to defects raised from failed tests, re-test after fixes
- **test technicians / lab personnel** — carry out the physical execution on benches, rigs, test cells, or field trials, and log what happened
- **quality / regulatory engineers** — review and approve test plans and results, own the evidence trail for audits and submissions
- **program / project managers** — track testing progress and coverage across the program, identify roadblocks, report readiness

The typical context is development of engineered products — vehicles, medical devices, aircraft, industrial equipment, electronics — usually multidisciplinary (mechanical, electrical, software) and frequently under functional-safety and quality regimes (automotive, medical-device, aerospace). Testing happens away from the desk as often as at it: prototype builds, durability rigs, environmental chambers, vehicle test drives, bench setups. This physical reality shapes the software: results must be recordable offline and imported later, and the same procedure must be reusable across many test items and conditions. Audits and design reviews are a standing reason these systems exist: the recorded tests are the objective evidence that the product was verified.

## Core Model

### The Defining Core

**The test of record.** A test is a persistent, individually identified definition: the procedure or steps to perform, and the acceptance basis — the expected outcomes or criteria against which results will be judged. The test belongs to the program, not to any single execution; it is written once and executed many times, often across different units, variants, or configurations. Without stable test definitions there is nothing to manage — only ad-hoc experimentation.

**The execution record (run).** A run is a recorded execution of a test against a specific test item — which unit, prototype, build, or configuration was exercised, under what conditions — capturing the observed results (measurements, observations, step outcomes) and a verdict: pass, fail, or an equivalent state. The run is where testing becomes evidence: it binds what was supposed to be verified to what actually happened, on a specific, identified subject. Mature products keep this binding explicit — the run is automatically associated with its originating test, its place in the plan, and the item it exercised.

**The managed testing effort.** Individual tests and runs are organized into a planned structure — test plans, campaigns, cycles — that expresses the strategy: what needs to be tested, in what order, together with what, by when. The system tracks execution against that structure (what is done, what is pending, what failed) and surfaces progress and outcomes as status, coverage, and reports. This is what the "management" in the Type name delivers: not just a log of what happened, but a tracked effort that can be steered, reviewed, and reported.

These three are jointly held. A library of procedures with no recorded executions is documentation, not testing. A pile of results with no test definitions is a lab notebook. A schedule with nothing executed behind it is a plan on paper. Records without the planned structure are a log, not a managed effort.

### Standard Capabilities

Mature products commonly add the following. They make the Type practical and are strongly expected in the market, but a product lacking one can still be recognized as test management:

- **Requirement linkage and coverage** — tests linked to the requirements (or design inputs, user needs) they verify; coverage views and verification matrices exposing which requirements have no test or no passing result. This is the dominant modern organizing structure — vendors themselves position the capability as requirements-based test management — but the defining core does not require formal requirement records; plans keyed to design targets and standards satisfy the same loop.
- **Defect loop** — when a run fails, a tracked defect or issue is raised and linked back through the run to the test and the requirement; fixes are re-tested through new runs.
- **Review, approval, and electronic signature** — test plans and completed results are reviewed and approved; signatures and audit trails turn the record into defensible evidence.
- **Test-item context** — which unit, prototype, build, or variant was tested; parameterized test items that let one procedure be executed repeatedly across many configurations.
- **Reports and dashboards** — progress by plan or cycle, coverage status, results summaries, defect status — for design reviews, management, and auditors.
- **Reuse** — test-case libraries, templates, and cross-project reuse for features shared across product lines.
- **Execution-tool integration** — results imported from specialized test automation or measurement tools; offline logging round-trips (export a test list, execute and record away from the desk, import the results).
- **Roles and permissions** — who may author, execute, review, approve, and configure.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Test of record
Realized as:  test cases with steps and expected results;
              verification activities inside design-control structures;
              test procedures referenced from a plan

Concept:   Execution record
Realized as:  test runs created per executed case;
              individual test records linked under a requirement;
              recorded verification results as objective evidence

Concept:   Managed effort
Realized as:  test plans containing groups and cycles;
              structured testing cycles across projects;
              design-control phases with tracked verification activities

Concept:   Acceptance basis
Realized as:  expected results per step; pass/fail criteria;
              acceptance criteria derived from requirements
```

A reader who has only seen one implementation should still be able to recognize the others from the core.

## How It Works

The typical working loop of a product-development program:

### 1. Define the tests and their basis

Test cases or procedures are authored — steps to perform, expected outcomes, equipment and conditions — and linked to what they verify: requirements, design inputs, or the plan's stated objectives. Coverage views show where the product's requirements have no test yet.

### 2. Plan the effort

A test plan states the strategy and objective for testing a system or subsystem and collects the relevant tests. Tests may be organized into groups, and the plan is commonly reviewed and approved before execution begins.

### 3. Execute in cycles

Execution is organized into cycles or campaigns — a defined set of tests executed together, often against a specific build or batch of prototypes. Each executed test produces its run within that cycle; the tester performs the procedure (at the bench, rig, cell, or field) and records results and a verdict — live in the application, or offline with results imported afterward. The run carries its context automatically: which test, which cycle, which item.

### 4. Handle failures

A failed run raises a tracked defect, linked back through the run to the test and the requirement it was verifying. The defect is fixed, and the fix is proven by a new run. Requirement quality can be assessed from the issues accumulated against each requirement.

### 5. Track, review, and report

Progress is monitored against the plan: which runs are done, which cases remain, where coverage is thin, which defects are open. Completed plans or cycles are sent for review; results are reported — per cycle, per case, per requirement — and, in regulated settings, signed. The accumulated record is the evidence produced at design reviews, audits, and submissions.

### Capability tiers

**Defining core** — test of record with acceptance basis; execution records with verdicts against identified test items; a managed, tracked, reported testing effort.

**Standard in mature products** — requirement linkage and coverage; defect loop; review/approval with e-signatures; test-item context and parameterization; reports and dashboards; reuse; execution-tool integration; roles.

**Optional / variant** — industry-specific evidence frameworks (design-control files, safety-case evidence); deep measurement-data capture (usually delegated to adjacent test-lab software); AI assistance for test generation and review; PLM- or QMS-embedded packaging.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Test plan / campaign view

The management surface for the effort: the plan's objective, its tests organized into groups and cycles, execution status per cycle, coverage against requirements. Primary actions: create plans and cycles, associate tests, check progress, send for review.

### Test case editor

Where a test is defined: steps, expected results, preconditions, equipment, linked requirements. Primary actions: author and version the test, link it to what it verifies, add it to plans.

### Execution / run surface

Where a tester works: the procedure's steps with expected results alongside, fields for observed results and measurements, the verdict control, and the run's context (test, cycle, item). Primary actions: step through the procedure, record results, set the verdict, log a defect from a failure. Offline variants export the run list and import results after field or bench execution.

### Coverage / traceability view

The verification picture: requirements (or design inputs) mapped to their tests and results, with gaps — unverified requirements, failing tests — made visible. Primary actions: inspect coverage, navigate from requirement to test to run and back.

### Defect / issue view

Tracked problems raised from failed runs, with their linkage to the run, test, and requirement, their status, and their resolution. Primary actions: raise, assign, resolve, re-test.

### Reports and dashboards

Progress, coverage, and results reporting for managers, reviewers, and auditors; commonly exportable as the formal evidence document.

### Administration

Test-case and defect type configuration, workflows and states, roles and permissions, templates, integrations.

## Important Rules / Behaviors

- **The verdict is judged against the test's acceptance basis.** A run's pass/fail is not the tester's opinion; it is the observed result compared with the expected outcomes defined in the test. Changing the basis is a change to the test, not to the run.
- **Execution status derives from runs, not declarations.** Whether a test "passes" is computed from its recorded runs — most recently and, in some products, by aggregation across runs — rather than asserted by hand. Plans themselves may carry no status of their own; their state is the state of what they contain.
- **Runs are bound to their context.** A run records which test, which cycle or campaign, and which item it exercised; this binding is what makes the record evidence rather than a note.
- **Failures become tracked objects.** A failed run raises a defect that is linked back through the run to the test and the requirement; the loop closes only when a subsequent run proves the fix.
- **Review and signature gate the evidence.** Plans and results become deliverable evidence through review and, in regulated settings, electronic signature; the audit trail of who did and approved what is part of the record.
- **The record is retained.** Tests, runs, verdicts, and signatures are kept as the program's verification history — the material that audits, design reviews, and regulatory submissions draw on.

## Variants

- **Industry regime** — automotive programs (verification organized around plan-and-report practice, evidence shaped by functional-safety and process standards), medical device (verification and validation managed as design-control activities feeding the design history file, with regulator-facing signatures), aerospace and defense, general industrial equipment. The core holds across all; the vocabulary and evidence obligations differ.
- **Verification vs validation emphasis** — the same machinery serves design verification (does the design meet the requirements) and product validation (does the product serve its users); programs typically run both through the same structures.
- **Host substrate** — a module of a requirements/ALM platform (the dominant pattern in the researched sample), a design-control module inside a quality management system, or — per market structure — a module embedded in a PLM suite beside the product record.
- **Execution posture** — manual-first with offline logging (bench, rig, field) vs automation-integrated with results imported from test automation and measurement tools; most mature products support both.
- **Measurement depth** — from pass/fail checklists to captured measurement data; deep data acquisition and analysis usually live in adjacent test-lab software that this Type integrates with rather than replaces.
- **Deployment** — cloud SaaS vs on-premises, reflecting the program's compliance and IT posture.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Software Test Management | sibling instance of the same family | the software-team instance: the application build/release cycle and automation frameworks are the center; here the center is the engineered product's verification against product requirements, with design-review and regulatory sign-off |
| Industrial Laboratory Management | adjacent, different phase | routine QC testing of production materials against specifications, samples anchored to production lots, deliverable = lot disposition and certificates; here tests anchor to requirements and design intent, deliverable = verification evidence |
| Inspection & Metrology Software | adjacent, different object | verifies part geometry against a declared nominal; here tests exercise function and performance |
| Engineering Requirements Management | upstream complement | holds the requirement record, its structure, and its traceability; this Type holds the test definition, execution, and verdict — the "verify" side of the same traceability graph |
| Product Lifecycle Management (PLM) | broader product record | PLM holds the product definition, structure, and change; test management may attach to the product record as a module, but the test lifecycle is the center here |
| Manufacturing QMS | complementary quality layer | owns the plant's quality system (documents, deviations, CAPA, audits) for production; this Type owns development-phase verification testing |
| Reliability Management | adjacent engineering discipline | reliability engineering predicts and analyzes durability and failure; the durability tests themselves are planned and recorded here as one test category |
| Test Automation Platform | execution complement | automation frameworks author and execute automated tests; this Type plans, tracks, records, and proves — results flow in as integration |
| Validation Management | adjacent, different subject | validation of processes, equipment, and computerized systems (installation/operational/performance qualification); here the subject is the product design itself |

The boundary with Software Test Management is the most important one, because the market sells one test-management capability across both worlds and the object vocabulary (test case, run, plan) is shared. The structural difference is the subject and the ecosystem of judgment: product test management verifies an engineered product against product requirements with design-review and regulatory evidence, while software test management serves the software build and release cycle. The two leaves are best understood as sibling instances of one test-management family.

## Representative Products

- Jama Connect (requirements-based test management for regulated multidisciplinary products; medical devices, automotive, aerospace)
- Polarion QA (Siemens; ALM-integrated test management for compliance-heavy product development)
- Codebeamer (PTC; ALM platform with QA and test management for automotive, medical, and other regulated programs)
- Greenlight Guru (medical-device design-control platform managing verification and validation testing as traceable design-control evidence)

The core was also checked against the paper-era ancestor of the practice (written test plans, numbered procedures, filled-in test logs, signed reports) to avoid over-fitting the definition to modern ALM implementations.

## Sources

Research date: **2026-09-09**

- Jama Connect Help — "Testing" (user guide): https://help.jamasoftware.com/ah/en/getting-to-know-jama-connect-features/testing.html
- Jama Software — Test Management solution page: https://www.jamasoftware.com/solutions/test-management/
- Jama Software — Automotive solution page: https://www.jamasoftware.com/solutions/automotive/
- Jama Software Support Center — test-management knowledge base and help search: https://support.jamasoftware.com/hc/en-us/search?query=test+plan+test+case+test+run
- Siemens — Polarion product page: https://www.siemens.com/en-us/products/polarion/
- Siemens — Polarion QA product page: https://www.siemens.com/en-us/products/polarion/qa/
- PTC — Codebeamer site and Help Center welcome: https://codebeamer.com/ , https://support.ptc.com/help/codebeamer/r3.3/en/codebeamer/codebeamer_welcome.html
- Greenlight Guru — Design Control Software page and platform home: https://www.greenlight.guru/design-control-software , https://www.greenlight.guru/
- Siemens — Teamcenter product page (checked for a test-management module; none surfaced): https://www.siemens.com/en-us/products/teamcenter/

> Sourcing limitation: operator-manual-grade documentation was reachable in depth only for Jama Connect. Polarion evidence is product-page level; Codebeamer's test-management help section could not be located (its site confirms the capability's existence and positioning only); PLM-embedded test modules and test-execution software (test-lab/DAQ and test-sequencer products) were not verifiable from public sources within the research budget. Accordingly, no numeric limits, default settings, or exhaustive state lists are stated in this document, claims about those unobserved poles are kept at market-structure strength, and cross-product generalizations are limited to what the reachable sources support.

Detailed evidence, product-by-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
