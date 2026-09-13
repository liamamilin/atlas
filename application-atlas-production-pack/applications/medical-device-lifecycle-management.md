# Medical Device Lifecycle Management

## Overview

A **Medical Device Lifecycle Management** application is the medical-device manufacturer's product-lifecycle system of record: it holds the device itself as a managed subject and maintains the regulated design-control record chain — user needs, design inputs (requirements), design outputs, risk controls, and verification & validation evidence — as linked, traceable, approval-gated records that accumulate into the device's design history or technical documentation, from concept through design transfer and market release to post-market changes.

The problem it exists to solve is specific to the device regulatory regime: regulators and standards bodies (FDA design controls under the Quality Management System Regulation, ISO 13485, ISO 14971 for risk, EU MDR technical documentation, IEC 62304 for device software) require that every device on the market be backed by a complete, current, traceable evidence chain showing what the device was designed to do, how risks were controlled, and how the design was verified. Spreadsheets and disconnected tools break that chain; this class of application keeps it whole as the work happens.

The boundary: when the center of gravity is the quality-event loop (deviations, CAPAs, audits as the quality system's own evidence), the product is a Life Sciences QMS; when it is the requirement of record for arbitrary engineered products, it is Engineering Requirements Management; when it is the product data estate (CAD, BOM, change) without design-control semantics, it is generic PLM; when it is marketed-device vigilance, it is Medical Device Post-market Surveillance. This Type sits at the intersection of those needs but is defined by the device's design-control record chain.

## Users & Context

Primary users are the product-development organization of a medical-device manufacturer:

- **R&D / systems / design engineers** — capture user needs and requirements, define design outputs, link risks, record verification and validation results.
- **Risk managers / quality engineers** — build and maintain the risk management file, keep risk controls tied to the design.
- **Quality assurance (QA)** — run design reviews, control documents and changes, keep the record chain audit-ready.
- **Regulatory affairs (RA)** — assemble submission evidence from the live record chain and track pathway alignment.

Secondary users: program/product managers overseeing the device portfolio; manufacturing and post-market teams consuming transferred designs and feeding field experience back; executives reading portfolio-level status.

The context spans company stages — startups preparing a first submission (template- and guardrail-driven) through global manufacturers managing portfolios of complex, software-enabled devices (audit defensibility at scale). Device classes shape the work: traditional hardware devices, software as a medical device (SaMD) and software in a device (SiMD) with fast iterative release cycles, in vitro diagnostics, and combination products. The regulatory regime (US FDA, EU MDR, or both) shapes the vocabulary of the evidence chain but not its structure.

## Core Model

### The Defining Core

```text
Device Product (lifecycle subject of record)
└── Design-Control Record Chain
    ├── User needs
    ├── Design inputs / requirements
    ├── Design outputs
    ├── Risk controls (risk management file)
    └── Verification & validation evidence
    (linked end-to-end; the links accumulate as the
     device's design history / technical documentation)
└── Controlled change and release over the chain
```

Three structures, jointly held. Remove any one and the product stops being recognizable as this Type:

- **The device product as the lifecycle subject of record** — a persistent, individually identified record of the device (or device family / software product) being developed and maintained, spanning concept → design → market → post-market. Every requirement, risk, test, and document hangs off it. Without it, the software is a requirements project or a document library with nothing device-shaped at the center.
- **The design-control record chain with traceability** — user needs, design inputs, design outputs, risk controls, and V&V evidence held as individually identified, linked records. The links are the point: every requirement traces forward to the verification that proves it and backward to the need and risk that motivated it. The chain, accumulated over the device's life, is the design history record / technical documentation that audits and submissions consume. Without it, the software is a document store or a generic PLM; with only one link class (requirements), it is a requirements tool.
- **Controlled change and release over the chain** — records are versioned, reviewable, and approval-gated with attributed sign-offs; a change is assessed for impact across the chain and propagates with traceability intact, so the released definition of the device's records is never ambiguous. Without it, the software is a static archive.

### Standard Capabilities

Mature products commonly add the following. They make the Type practical; they do not define it.

- **Risk management as a record class** — a risk management file (hazard analysis, risk matrices, risk controls) maintained per device and linked to the requirements and design elements it controls; in the software-device pole, cybersecurity risk is embedded in the same workflows.
- **Design reviews** — recorded review events with participants, decisions, and links into the chain.
- **Evidence generation** — on-demand traceability matrices and design-history / risk-file / technical-documentation exports assembled from live records rather than manual document assembly.
- **Controlled documents** — SOPs, specifications, and other controlled documents with version control and approvals (separable; some products center items and links instead of documents).
- **Design transfer** — the handoff of a released design into production, with changes, approvals, and notifications crossing the design–manufacturing boundary.
- **Submission support** — packaging the chain's evidence for regulatory pathways (510(k)-class US submissions, CE/MDR-class EU documentation).
- **Post-market linkage** — complaints, CAPAs, and post-market data feeding back into the chain as inputs to design changes.
- **Bundled quality-system records** — in some product families, the eQMS record population (CAPAs, complaints, nonconformances, audits, training, suppliers) ships inside the same platform; in others it is absent or a separate product.
- **BOM / parts management** — product structure records alongside the design chain in suite- and PLM-shaped products.
- **Developer-tool integrations** — present in products built for software-enabled devices: synchronization with issue trackers and source-control tools so engineering work stays in its own tools while traceability stays current.

### One Structure, Many Implementations

The core model is conceptual. Products realize it differently:

```text
Concept:   Device product of record
Realized as:  device/product records in a vertical platform,
              projects in a requirements tool, product structures
              in a PLM suite, product lines in a QMS suite

Concept:   Design-control chain
Realized as:  linked item graphs (requirement ↔ risk ↔ test),
              design-control modules with staged phases,
              document-plus-matrix assemblies

Concept:   Design history / technical documentation
Realized as:  exportable file bundles (DHF/DDF/RMF-class),
              generated documentation from live data,
              compiled submission evidence packages
```

A reader who has only seen one pole (for example, a requirements-centered tool) should still be able to recognize the device-native platform and the enterprise-suite realizations from the core model.

## How It Works

### Build the chain as the device is designed

```text
Start a device program / product record
→ capture user needs
→ derive design inputs (requirements)
→ link risks and define risk controls
→ record design outputs
→ run verification and validation, linking evidence to requirements
→ hold design reviews at defined points
```

The work pattern vendors emphasize is linking *while working*: requirements, risks, and tests are connected as they are created, so traceability accumulates as a by-product of development instead of a reconstruction exercise before an audit.

### Keep traceability current

As requirements change, tests evolve, and risks are updated, the links between records are maintained automatically; gaps and suspect links (a changed requirement whose downstream verification is no longer valid) are surfaced visibly, because an incomplete chain is the failure mode this software exists to prevent.

### Review and approve

Design reviews and record approvals happen inside the system with attributed, signed decisions. Approvals gate progression; the record of who approved what, when, is part of the evidence chain.

### Change a released device

```text
Change request
→ impact assessment across the chain
  (affected requirements, risks, tests, documents)
→ recorded approval
→ new versions of affected records
→ transfer to production / notification of affected parties
→ post-market feedback loops back in
```

Changes to a marketed device are the highest-stakes loop: the chain must show what changed, why, how it was verified, and what it affects.

### Generate the evidence

For audits and submissions, the system assembles traceability matrices and the design-history / risk-file / technical-documentation outputs from the live chain. Because the chain is maintained as work happens, generation is a retrieval and formatting act, not a re-assembly project.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Design-control workspace

The primary working surface for engineers.

- requirements and design records as addressable items with attributes (statement, rationale, status, owner)
- link views showing what connects to what; trace graphs exposing missing links
- primary actions: create/link records, flag verifications, comment, edit with version history

### Risk management surface

- risk matrices (severity × probability framings), hazard lists, risk controls
- primary actions: add/assess risks, link controls to requirements and design elements, keep the risk file current

### Review / approval center

- queued reviews with diffs and context; e-signature approval flows
- primary actions: review, comment, approve/reject, sign

### Document library

- controlled documents (SOPs, specs) with versions, effective states, approval trails
- primary actions: author, route for approval, view version history

### Change records

- change requests/orders with impact views across the chain
- primary actions: raise change, assess impact, approve, implement, verify

### Export / report generation

- traceability matrices, design-history and risk-file bundles, audit trails
- primary actions: select scope, generate, download

### Dashboards / admin

- program and portfolio status, traceability completeness, training and event overviews; configuration of record types, workflows, and templates

## Important Rules / Behaviors

### Traceability completeness is the central quality gate

The chain from user need through requirement to verification must be traversable in both directions on demand. Missing or suspect links are surfaced as visible gaps, because they are precisely what an audit or submission review will find.

### Records are versioned and approvals are attributed

Every element is versioned; prior versions remain retrievable; approvals carry the identity of the approver. Silent edits are not part of the model — the evidence chain depends on attributable change.

### Changes propagate with impact analysis

A change to one record (a requirement, a risk control, a document) is assessed for what it affects downstream before approval, and the affected records' traceability is updated or flagged as the change is implemented.

### Evidence is generated from live records

Audit- and submission-ready outputs are assembled from the maintained chain, not hand-built. Products differ in how much generation is automated, but the direction is uniform: the chain is the source of truth.

### The regime shapes the record vocabulary, not the structure

Design controls, risk management files, technical documentation, and software lifecycle records are the regime's names for parts of the same chain. Products align their templates and workflows to the regimes their customers face (US, EU, software devices), but the underlying structure — linked, versioned, approval-gated records over a device subject — is shared.

## Variants

- **Product poles** — device-native platforms (quality + product development + clinical evidence on one platform); requirements/traceability-centered tools with packaged device frameworks; enterprise QMS suites where development is one suite beside quality, manufacturing, and postmarket; enterprise PLM estates serving medtech with generic product-data machinery plus traceability.
- **Device class** — traditional hardware devices; SaMD/SiMD with software release lifecycle machinery and developer-tool integrations; in vitro diagnostics; combination products; research-use-only and laboratory-developed tests.
- **Regulatory regime** — US-centered (FDA pathways, QMSR alignment), EU-centered (MDR/CE technical documentation), or both.
- **Scale and packaging** — startup editions built on templates and guardrails; mid-market implementations; enterprise deployments with portfolio-level governance and validation support.
- **Deployment** — cloud SaaS dominant; on-premises heritage in enterprise PLM.
- **Optional extensions** — clinical evidence modules (device EDC, ePRO, post-market clinical surveys); AI assistance (requirement-verifiability checks, link suggestions); validation tooling for the manufacturer's own computerized systems.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Life Sciences QMS (eQMS) | closest sibling | eQMS centers the quality-event/action loop (deviations, CAPAs, change controls, audits) as the quality system's evidence; this Type centers the device's design-control record chain. The eQMS record population appears here only as a bundled capability in some product families; device-native vendors sell the two as separate products. |
| Engineering Requirements Management | overlapping machinery | that Type centers the requirement of record and its traceability for any engineered product; here requirements are one link class inside the device lifecycle, which adds the device subject, transfer, submission, and post-market legs. Requirements tools with device frameworks straddle by center of gravity. |
| Product Lifecycle Management / PLM | adjacent estate | PLM centers the product data estate (CAD/PDM, BOM, change, manufacturing process) across industries; this Type centers the device-regime record chain. Enterprise PLM serves device makers with accelerators — packaging, not identity. |
| Medical Device Post-market Surveillance | downstream sibling | that Type centers marketed-device vigilance (complaints, adverse events, trend reporting, post-market follow-up); here post-market linkage is the leg feeding changes back into the design chain. |
| Regulatory Information Management / RIM | adjacent | RIM centers the regulatory-affairs system of record (submissions, dossiers, registrations); here submission support is evidence generation from the design chain. |
| CAPA Management | bundled record class | CAPA is one record class inside bundled quality modules here, not the center. |
| Bill of Materials Management | bundled capability | product structure records appear in suite- and PLM-shaped products; the BOM is not this Type's center. |
| Validation Management | distinct function | validating computerized systems and processes is a separate discipline (often a separate product); design V&V here is verification of the device design itself. |
| Manufacturing QMS / eDHR | production-side neighbor | production-floor quality and device history records vs design-phase records; suite vendors sell both beside each other. |

## Representative Products

- **Greenlight Guru** — device-native platform spanning quality management, product development (design controls, risk, software release lifecycle), and clinical evidence; mid-market device companies through enterprise.
- **Jama Connect (Jama Software)** — requirements/traceability-centered engineering platform with a packaged medical-device framework; used by top-tier device manufacturers for requirements, risk, and V&V traceability.
- **MasterControl** — enterprise QMS suite whose device offering spans Development, Quality, Supplier, Manufacturing, and Postmarket suites on one platform.
- **PTC Windchill** — enterprise PLM serving medtech with product-data, change, and traceability machinery.

The core model was checked across all four poles (device-native platform, requirements tool, QMS suite, enterprise PLM) to avoid defining the Type by any single vendor's packaging.

## Sources

Research date: **2026-09-08**

- Greenlight Guru — platform overview and Medical Device Product Development pages: https://www.greenlight.guru/ , https://www.greenlight.guru/product-development-software
- Jama Software — MedTech & Life Sciences solution page: https://www.jamasoftware.com/solutions/medtech/
- MasterControl — Medical Device industry page and Product Development (Development Excellence) page: https://www.mastercontrol.com/industries/medical-device/ , https://www.mastercontrol.com/product-development/
- PTC — Windchill product page (MedTech industry positioning): https://www.ptc.com/en/products/windchill

> Sourcing limitation: official help-center / operational documentation was not reachable for any sampled product; evidence is official product- and solution-page depth. PTC's device-specific solution pages and Arena Solutions' medical-device pages were unreachable (repeated fetch failures), so the enterprise-PLM pole is evidenced at generic-PLM strength and the mid-market cloud PLM+QMS pole is under-sampled. No exact workflow state names, numeric limits, or defaults are asserted in this document; precise vendor claims (marketing statistics, named-customer metrics) are omitted.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
