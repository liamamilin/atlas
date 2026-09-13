# Engineering Requirements Management

## Overview

An **Engineering Requirements Management** application is the engineering organization's system of record for the requirements a product must satisfy. It captures each requirement as a persistent, individually identified record; organizes requirements into structured specifications; links them traceably to the stakeholder needs above them and the designs, tests, and risks below them; and manages their change through version history, baselines, and controlled review and approval.

The defining structure is small:

```text
Requirement of record
└── Structured specification (hierarchy / document / tree)
    └── Traceability links (upstream needs ↔ requirements ↔ design, tests, risks)
        └── Managed change (version history → baselines → controlled change)
```

Everything else commonly associated with these products — review centers with electronic signatures, test coverage machinery, reuse across product lines, ReqIF and Office interchange, generated specification documents, compliance report packs, AI-assisted requirement quality checks — is widespread in current products but is not what makes the product a requirements management system. Classic requirements tools used for decades in high-compliance programs, and even disciplined spreadsheet-and-document practice before them, exhibit the same four-part core without any of the modern additions.

When the center of gravity shifts away from the requirement record — to formal system models, to the physical product structure, to work items to be executed, or to market-facing prioritization — the product is drifting toward a different Application Type (MBSE Platform, PLM, Issue Tracker, Product Management Platform).

## Users & Context

The primary users are engineering roles on complex product development programs:

- **Systems engineers / requirements engineers** — author and structure the requirement set, define the specification breakdown, maintain traceability, run reviews and baselines
- **Product / program managers** — track scope, status, and coverage across the program; own release-to-requirement assignment
- **Design engineers (software, hardware, electrical, mechanical)** — consume requirements allocated to their discipline, link their design artifacts back to them
- **Test / V&V engineers** — link test cases and verification results to requirements, work coverage gaps
- **Quality / regulatory / safety engineers** — use traceability and baselines as compliance evidence for audits and certification

The typical context is development of complex engineered products — vehicles, aircraft, medical devices, trains, industrial equipment, safety-critical software — usually under functional-safety and quality standards (for example automotive, aerospace, medical-device, and rail regimes), frequently across distributed teams and suppliers. Audits and certification reviews are a standing reason these systems exist: the traceability they maintain is the evidence.

## Core Model

### The Defining Core

**The requirement of record.** A requirement is a persistent, individually identified statement of a capability, condition, or constraint the product must satisfy. Each requirement carries a stable unique identifier that survives edits and reorganizations, a statement (typically rich text), and attributes — commonly rationale, verification method, status, ownership, priority, and allocation to a discipline or release. Every change to a requirement produces a recorded version. Without stable requirement records there is nothing to manage.

**Structured specification.** Requirements are not a loose list. They live inside a project in a structured collection: a hierarchy of requirements, a specification document whose sections and paragraphs are individually addressable, or a tree of folders and modules organized by abstraction level and discipline. The structure expresses the specification's breakdown — stakeholder needs at the top, system requirements below them, subsystem and component requirements further down. Without structure, the product is a flat ticket list rather than an engineering specification.

**Traceability links.** Requirements are connected by explicit, typed, navigable links. Upstream links tie a requirement to the stakeholder need, regulation, or hazard it addresses; downstream links tie it to the requirements derived from it, the design elements that realize it, the test cases that verify it, and — in some products — the risks or source code related to it. Links are directional and typed (derive, satisfy, verify, and similar relationships), and they are the substrate for coverage: whether a requirement has been derived, designed, and verified is computed from the link graph. Without traceability, the product is a document editor.

**Managed change.** The requirement set evolves under control. Every requirement has a version history; the set can be frozen as a baseline — a named snapshot of the specification at a point in time — and changes after a baseline are proposed, analyzed for downstream impact, reviewed, and approved before they take effect. Baselines can be compared (what was added, removed, changed since the last one), and historical states remain inspectable. Without managed change, the product is a static snapshot, and the "management" in the Type name is gone.

These four are jointly held. A versioned document with numbered requirements but no links is requirements authoring, not management. A flat list of linked items with no specification structure loses the engineering character. Change machinery with no requirement records has nothing to change.

### One Structure, Many Implementations

The core model is conceptual. Mature products realize each concept differently:

```text
Concept:   Requirement of record
Implementations:  data-model-driven artifacts in modules;
                  items with configurable types and fields;
                  uniquely identifiable paragraphs inside live specification documents

Concept:   Structured specification
Implementations:  folder/module trees; document-style outlines mirroring a
                  table of contents; product-structure trees organized by
                  abstraction level and discipline (V-model style)

Concept:   Traceability link
Implementations:  typed relationship records between items; link types with
                  rules about which directions are legal; cross-project links

Concept:   Baseline
Implementations:  named snapshots with diff reports; development-stream
                  baselines; version comparison against current
```

A reader who has only seen one implementation should still be able to recognize the others from the core model.

### Standard Capabilities

Mature products commonly add the following. They make the Type practical, but a product lacking one can still be recognized as requirements management:

- **Review and approval** — structured review cycles over requirement content: reviewers are invited, comment on specific requirements, and approve or reject; electronic signatures record who approved what, and in regulated settings signatures gate release
- **Test and V&V linkage** — test cases and test runs linked to requirements; coverage views and verification matrices showing which requirements lack verification
- **Reuse and variants** — reusable requirement components or catalogs, branching of specifications for product lines, and distribution of shared requirement updates across projects
- **Interchange** — import and export with Word and Excel (the legacy habitat of requirements), and ReqIF exchange with customers and suppliers
- **Document generation and reporting** — specification documents, traceability matrices, and compliance/audit reports generated from the live record rather than maintained by hand
- **Dashboards and analytics** — coverage status, requirement quality metrics, progress across projects
- **Permissions and roles** — who can see, edit, approve, and baseline what; contributor/reviewer participation for occasional stakeholders
- **Integrations** — issue trackers, modeling and simulation tools, test tools, and code platforms, so downstream artifacts can be linked into the traceability graph
- **Requirement quality analysis** — rule-based or AI-assisted checks for ambiguity, inconsistency, and testability while writing

## How It Works

The typical working loop of an engineering program:

### 1. Establish the project and its data model

Before requirements are written, the project's structure is configured: which requirement types exist (stakeholder need, system requirement, subsystem requirement, test case…), which attributes each carries, which workflow states they move through, and who may do what. Some organizations mirror a document layout; others organize by product structure and abstraction level; hybrids are common. This configuration is itself maintained as the program evolves.

### 2. Capture requirements

Requirements enter as records: authored directly in the structured editor, imported from existing Word or Excel specifications, exchanged via ReqIF with customers and suppliers, or generated with AI assistance and then human-reviewed. Import from documents is a first-class path because most organizations arrive with their requirements living in documents.

### 3. Organize and attribute

Each requirement is placed in the specification structure, given its attributes (rationale, verification method, status, allocation), and connected into the hierarchy. The requirement's identity is fixed at creation; reorganizing the tree does not change what the requirement is.

### 4. Build traceability

Users link requirements to their upstream sources and downstream realizations: need → system requirement → subsystem requirement → design element → test case. Traceability views and coverage matrices render the link graph, exposing gaps — requirements with no source, no design, or no test.

### 5. Review and approve

Requirement content is circulated for review: reviewers see the proposed content in context, comment against specific requirements, and approve or reject. Completed reviews are recorded, and in regulated settings signatories electronically sign the specification as reviewed or approved.

### 6. Baseline and manage change

At milestones the requirement set is baselined. Subsequent changes are proposed against the baseline; the system surfaces the downstream impact of each proposed change (which derived requirements, designs, and tests are affected); approved changes propagate to linked artifacts and are recorded in each requirement's history. Baselines can be diffed to show exactly what moved between milestones.

### 7. Verify

Test cases are authored and linked to the requirements they verify; test runs record results against those links. Coverage views show which requirements are verified, which are not, and where verification failed — the gap list that drives V&V work.

### 8. Report and audit

Because the record is live, specification documents, traceability matrices, and compliance evidence are generated on demand — for design reviews, audits, and certification submissions — rather than assembled by hand before each review.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Specification editor / requirement list

The primary authoring surface: requirements presented either as a document-style outline (sections and paragraphs with requirement context preserved) or as a tree-plus-table of items with editable attributes.

- typical information: requirement ID, statement, attributes, hierarchy position, status, links
- primary actions: create/edit requirement, reorder, set attributes, link, comment

### Traceability view / coverage matrix

The relationship surface: upstream and downstream links rendered as an expandable trace, and coverage matrices showing requirements against their verification evidence.

- typical information: link types and directions, coverage status, missing links
- primary actions: create/remove links, filter by type or status, export the matrix

### Review center

The collaboration surface for requirement reviews: review cycles with invited participants, per-requirement comments, approve/reject decisions, and signature records.

- typical information: review status, participants, outstanding comments, electronic signatures
- primary actions: start a review, comment, approve/reject, sign

### Baseline and version comparison

The change-control surface: create baselines, diff a baseline against the current set or another baseline (added / removed / changed requirements), and inspect a requirement's version history.

- primary actions: create baseline, compare versions, restore or roll forward context

### Dashboards and reports

Program-level visibility: coverage and verification status, requirement quality metrics, progress by discipline or release; report and document generation for audits.

### Administration

Configuration of the data model (requirement types, fields, workflows), project structure, permissions, and integrations. In practice this is where an implementation lives or dies, and mature products treat it as a first-class surface.

## Important Rules / Behaviors

- **Identity is stable.** A requirement's unique ID persists across edits, moves, and renumbering; traceability depends on it. Deletion is typically controlled — some products deactivate rather than destroy, so history and links survive.
- **Baselines freeze.** After a baseline, the recorded set is immutable as a snapshot; further change happens as new, controlled versions. Comparisons are always against a named baseline.
- **Links are typed and directional.** Coverage is computed from the link graph, so an unlinked requirement is visibly unverified — the system makes gaps a first-class object, not an accident.
- **Workflow states and locks restrict editing.** Requirements under review, approved, or baselined are commonly locked or state-restricted; who may change what in which state is configurable and audited.
- **Signatures gate release.** In regulated settings, an approved-and-signed state is a precondition for releasing a specification to production; the signature record (who, what, when) is part of the audit trail.
- **Documents are outputs, not the record.** The specification document is generated from the requirement records. Editing the document outside the system breaks the record, which is why round-trip import/export and two-way Office sync exist.
- **Impact precedes approval.** Change proposals are evaluated by their downstream impact on derived requirements, designs, and tests before approval; propagation of approved changes is recorded per artifact.

## Variants

- **Regulated-industry pole** — deep standards alignment (automotive, aerospace, medical-device, rail regimes), risk analysis (e.g. FMEA-style) integrated with requirements, cybersecurity requirements engineering, and certification-evidence generation as first-class outputs; on-premise or air-gapped deployment common
- **Unified ALM pole** — requirements live in one repository and one work-item model together with tests, tasks, and code links; the requirement-specific structures (identity, traceability, baselines) remain, but the product spans the whole engineering lifecycle
- **Requirements-specialist pole** — requirements, review, and traceability as the focused product, integrating outward to modeling, test, and issue tools rather than absorbing them
- **Document-centric vs model-based organization** — the same core organized as export-shaped documents (mirroring a table of contents or a regulatory file) or as product-structure trees organized by abstraction level; organizations frequently migrate from the former to the latter
- **Software-team pole** — lighter-weight requirements practice inside software development, closer to backlog and issue-tracker workflows (see Related Application Types)
- **Supplier-exchange posture** — requirements exchanged with customers and suppliers via ReqIF or round-trip document export, with the tool as the interchange authority

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Requirements Management Platform (software development) | same family, adjacent positioning | the market does not maintain two product categories — the same products serve software and systems engineering; the two names reflect industry positioning more than a structural difference |
| MBSE Platform | adjacent, complementary | MBSE centers on formal system models; requirements here are records with statements, attributes, and traceability; integration links the two |
| Product Lifecycle Management / PLM | adjacent | PLM's center of gravity is the physical product record (BOM, CAD, documents, change); requirements may be linked from it but are not its core object |
| Issue Tracker | adjacent, frequently confused | issue trackers hold work items to be executed with plan/execute lifecycles; requirements are specification records with hierarchy, traceability, and baselines; some ALM products unify both object kinds in one platform |
| Bug Tracking System | adjacent | defect records about observed failures vs requirement records about what to build; linked (defect traced to requirement) but different centers |
| Software Test Management | adjacent, often bundled | test cases, runs, and verdicts vs requirements; linked bidirectionally for coverage; test management appears as a module inside several requirements products |
| Engineering Change Management | adjacent | cross-artifact change machinery (change orders, effectivity) vs requirement-set-scoped change (baselines, change proposals against requirements) |
| Product Management Platform | vocabulary overlap only | market-facing prioritization (backlogs, roadmaps, demand) vs engineering specification of record (verifiable statements, compliance evidence) |
| Engineering Document Management | adjacent | documents as managed records vs requirements as managed records; document management stores the specification file, requirements management structures what it says |

## Representative Products

- **IBM Engineering Requirements Management (DOORS Next / DOORS)** — enterprise systems-engineering incumbent; DOORS lineage used for decades in high-compliance programs; modules, multi-level traceability, baselines, electronic signatures; part of a broader engineering lifecycle suite
- **Jama Connect** — regulated-industry requirements specialist (medical device, automotive); items with configurable types and workflows, review center with e-signatures, baselines with diff reports, model-based and document-centric structure options
- **Polarion ALM (Siemens)** — unified-repository ALM philosophy; live specification documents with paragraph-level requirement identity, workflow-enforced states with e-signatures, branching and derived documents for product lines
- **Visure Requirements** — compliance-first requirements ALM for regulated industries; live traceability matrix through tests, risks, and source code; standards packs; requirement catalogs and baselines; cloud or air-gapped on-premise deployment

The defining core was checked against the classic-tool generation (DOORS's decades-long, pre-cloud, pre-AI form) and against pre-tool document-and-spreadsheet practice to avoid defining the Type by the current cloud/AI implementation.

## Sources

Research date: **2026-09-08**

- IBM — Engineering Requirements Management product page: https://www.ibm.com/products/requirements-management
- Jama Software Support Center (Knowledge Base): https://support.jamasoftware.com/ — including "Items, Item Types & Lifecycle", "Versioning & Baselines", "Reviews & Collaboration", "Traceability & Relationships" section maps and the article "Model-Based vs. Document-Centric Project Structures in Jama Connect"
- Polarion (Siemens) — product pages: https://www.siemens.com/en-us/products/polarion/ and https://plm.sw.siemens.com/en-US/polarion/requirements/
- Visure Solutions — product pages: https://www.visuresolutions.com/ and https://visuresolutions.com/features/requirements-management-software/

> Sourcing limitation: IBM's product documentation returned HTTP 403 on two attempts and the IBM training page rendered empty; Visure's help center timed out. Claims about those two products are therefore held at official-product-page strength (positioning, capability areas, named features), and precise operational details (exact state names, numeric limits, default settings) are intentionally not asserted. Jama's support-center documentation was reachable at article level and carries the deepest operational evidence in this pass. Detailed observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
