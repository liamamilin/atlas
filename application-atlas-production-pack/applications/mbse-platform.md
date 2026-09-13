# MBSE Platform

## Overview

An **MBSE Platform** (Model-Based Systems Engineering platform) is the engineering system of record for the **system model**: it holds a persistent, structured, language-governed model of the engineered system under development, generates every diagram and view from that model, and lets systems engineers do their work — requirements linkage, architecture definition, behavioral analysis, verification planning, and generation of downstream artifacts — directly on the model.

The defining core is small:

```text
The system model (unit of record)
└── Diagrams and views generated from the model
    └── Editing governed by a defined modeling language
        └── Subject: the engineered system (requirements, structure, behavior, verification)
```

Everything else the market associates with mature MBSE — shared model repositories, simulation, document generation, requirements traceability, toolchain integration, embedded methodology — is standard capability of mature products or a variant, not part of what makes the product an MBSE platform. The Type exists in deliberate contrast to both document-centric systems engineering (specifications in documents and spreadsheets, with hand-maintained diagrams) and general-purpose diagram drawing: in an MBSE platform, the diagrams are not the artifact — the model is.

## Users & Context

Primary users are **systems engineers and system architects** working on the development of complex, multi-discipline engineered products — typical in aerospace, defense, space, automotive, rail, energy, and complex equipment programs. They define what the system must do, how it is structured, how its parts interact, and how the design satisfies its requirements.

Around them sit several secondary roles:

- **specialty engineers** (safety, security, performance, cost) who consume and annotate the model through viewpoints relevant to their concern
- **requirements engineers**, who either work with requirements held inside the model or keep them in a dedicated requirements tool linked to the model
- **verification and validation engineers**, who derive verification cases from model-defined behavior and scenarios
- **subsystem and component teams**, who receive contracts or models transitioned from the system level and co-engineer at their own level
- **stakeholders and reviewers** (customers, program management), who read published views of the model rather than editing it
- **tool administrators**, who run the model repository, permissions, and backups where a shared deployment exists

The working context is a development program in which many stakeholders must stay consistent about what the system is and does. The model serves as the shared engineering reference: when it changes, the views, analyses, and generated documents change with it.

## Core Model

### The Defining Core

```text
The system model (unit of record)
└── Diagrams and views generated from the model
    └── Editing governed by a defined modeling language
        └── Subject: the engineered system
```

Four properties. If any one is removed, the product is no longer recognizable as an MBSE platform:

- **The system model as the unit of record.** A persistent, structured model of the system under development, composed of typed model elements — structural components or blocks, functions or activities, ports and connections, states and modes, requirements, constraints and parameters — organized in containment structures such as packages or trees. Model elements exist independently of any diagram; the model, not a drawing, is what persists and evolves.
- **Diagrams as views over the model.** Every diagram is a generated rendering of underlying model elements. The same elements can be shown in multiple diagram kinds (structure, behavior, interfaces, requirements) and in non-graphical views — trees, tables, matrices, query-driven context views. Editing happens on the model; diagrams follow.
- **Language-governed editing.** Users create, connect, and modify typed elements, and the tool enforces the modeling language's grammar: which element kinds exist, which relationships are allowed between them, and what makes a model well formed. The tool does not accept arbitrary shapes on a canvas.
- **Systems-engineering subject.** The modeled subject is the engineered system as a whole — spanning its requirements, structure, behavior, and commonly its parameters and verification concerns — rather than software alone. The model is the working basis for the system's engineering definition and is handed onward to detailed design, verification, and production.

### What Mature Products Add

Mature products commonly carry most of the following. They make the platform practical for real programs, but they are not what makes the product an MBSE platform:

- **Requirements and traceability** — requirements held as model elements or imported from a dedicated requirements tool, linked to the model elements that satisfy or derive them, with coverage and suspect-link tracking so that unverified work is visible.
- **Model validation** — rule suites that check integrity, completeness, and traceability of the model, often organized into selectable profiles with automated quick fixes.
- **Shared model repository** — server-side storage with parallel editing, locking or merging, branching, versioning, baselines, access control, and audit, so that a team can work on one model.
- **Behavioral execution** — simulation or animation of model fragments (state machines, activities, parametric evaluations) to validate behavior early, plus bridges that hand the model to dedicated simulation tools.
- **Document and report generation** — generation of specification-style documents, web publications, and review packages from the model, so non-modeling stakeholders can read the current truth.
- **Navigation and query** — search, context browsers that answer "what relates to this element", matrices and tables computed from the model.
- **Reuse machinery** — libraries, replicable model fragments, reference architectures shared across projects.
- **Toolchain integration** — connections to requirements tools, simulation tools, PLM/ALM suites, office tools, and code-generation paths, often through standard protocols and APIs.
- **Embedded methodological guidance** — activity browsers or wizards that walk the engineer through the recommended engineering steps, where the product couples to a specific method.
- **Viewpoints and profiles** — mechanisms to extend the language or define concern-specific views (enterprise architectures, safety, security, cost, mass).

### One Structure, Many Implementations

The core model is written in conceptual terms. Products realize each concept differently:

```text
Concept:            Modeling language
Implementations:    SysML (v1 or v2), UML, domain-specific languages defined by a
                    methodology, proprietary systems design languages, custom profiles

Concept:            Model storage
Implementations:    single-user workbench file, shared repository server,
                    cloud-hosted model service

Concept:            Behavioral analysis
Implementations:    built-in simulators and animators, export bridges to dedicated
                    simulation tools, or none (analysis delegated entirely to external tools)

Concept:            Requirements handling
Implementations:    requirements as native model elements, requirements viewpoints
                    loaded as add-ons, or external requirements tools linked to the model
```

A reader who encounters only one implementation — for example only SysML-based tools — should still be able to recognize products built on a different language or a different storage model from the core structure above.

## How It Works

### Set up the model

```text
Create a project
→ start from a template, a method's skeleton, or an imported baseline
→ organize the containment structure (packages, packages per discipline or level)
→ optionally import requirements or parse legacy documents into first model content
```

### Build the architecture iteratively

```text
Create typed elements (components, functions, actors, states, data)
→ connect them through ports and defined relationships
→ allocate functions to components
→ refine across abstraction levels (need → logical → physical, or the method's equivalent)
→ diagrams of the affected kinds update with the model
→ repeat as understanding deepens
```

The loop is model-first: the engineer manipulates elements and relationships; diagrams are regenerated views used for reading, communication, and review. Tools help manage scale by computing higher-level renderings from lower-level detail and by keeping multiple abstraction levels consistent.

### Link requirements and verification

```text
Import or create requirements
→ link them to the model elements that satisfy, derive, or verify them
→ coverage views show unlinked requirements and unverified elements
→ changes mark affected links suspect for re-check
```

### Analyze and validate

```text
Run validation rules (integrity, completeness, traceability)
→ fix reported issues, often with automated quick fixes
→ execute behavioral fragments or hand the model to simulation tools
→ evaluate parametric constraints and compare candidate architectures
```

### Publish and hand off

```text
Generate documents, reports, or web publications from the model
→ reviewers read and comment on published views
→ export model content to simulation tools, code-generation paths,
  or the product data management environment
→ transition contracts or models to subsystem teams
```

### Collaborate and govern

```text
Work against a shared repository (where deployed)
→ elements lock while being edited; changes merge and version
→ baselines freeze reviewed states of the model
→ permissions and audit trail govern who changed what
```

### Core vs standard vs optional

- **Defining core** — model as record; diagrams as views; language-governed editing; systems-engineering subject.
- **Standard capabilities of mature products** — requirements traceability, validation suites, shared repositories, behavioral execution, document generation, navigation/query, reuse, integration, methodology guidance, viewpoints.
- **Variant / optional** — language substrate, methodology coupling, deployment shape, industry packages, code generation depth, specialty analysis extensions, AI assistance.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Model explorer / containment tree

The structural entry surface.

- shows the model's elements organized by containment (packages, hierarchies)
- primary actions: create elements, reorganize, open element details or diagrams

### Diagram editors

The visual working surfaces, one per diagram kind.

- structure diagrams (components and their parts), behavior diagrams (activities, state machines, sequences), interface and parametric diagrams, requirements diagrams
- primary actions: add or connect the underlying elements, arrange and filter the rendering, navigate from a shape to its element and back

### Element inspector / property sheet

The detail surface for a single model element.

- shows the element's attributes, relationships, and owned content
- primary actions: edit attributes, manage relationships and links

### Validation and diagnostics panel

- lists rule violations by category with locations in the model
- primary actions: inspect, jump to the offending element, apply quick fixes

### Query and navigation surfaces

- context browsers that show everything related to a selected element; matrices and tables computed from the model; search
- primary actions: navigate relationships, check coverage, spot missing links

### Simulation / animation console

- runs behavioral fragments with controls (run, step, stop), timelines, and transcripts where provided
- primary actions: execute, observe, record results

### Publication and review surfaces

- generated documents or web views of the model for non-modeling stakeholders, sometimes with commenting
- primary actions: publish, browse, comment

### Repository and administration surfaces

- project/user administration, permissions, sessions, version and baseline management where a shared deployment exists

## Important Rules / Behaviors

### The model is the source of truth

Removing an element from a diagram is not the same as deleting it from the model; diagrams can be re-synchronized or regenerated from the elements. Conversely, editing an element updates every view in which it appears. Products differ in how tightly a given diagram is synchronized, but the model-first direction is the defining behavior.

### Well-formedness is enforced

The tool constrains what can be created and connected according to the modeling language. Invalid structures are prevented at creation time or reported by validation; the user cannot silently accumulate arbitrary drawings.

### Traceability makes gaps visible

Because requirements, model elements, and verification artifacts are linked, unlinked requirements and unverified elements are computable states, not opinions. Changes can mark downstream links suspect until re-examined.

### Changes propagate across views and levels

A change to a model element appears in all its views; tools that manage multiple abstraction levels compute higher-level renderings from lower-level detail and offer impact analysis before deletions or changes.

### Concurrent editing is governed

Where a shared repository exists, concurrent work is managed through locking, merging, or branching with version history and audit trails; the exact mechanism varies by product.

### Method structure (where embedded)

Products coupled to a methodology structure the work into named engineering activities and phases; the method guides what to model next, but the underlying model-first loop is the same.

## Variants

Common variants of the Type:

- **SysML-based general-purpose platforms** — the dominant pattern; the model is expressed in SysML (v1 today, v2 emerging), usually with UML heritage and profile mechanisms (e.g. CATIA Magic/Cameo, IBM Rhapsody)
- **Methodology-coupled platforms** — the tool implements a specific engineering method and its own language, with the method embedded as guidance (e.g. Eclipse Capella with Arcadia; GENESYS with its design language and method)
- **Pure-play MBSE platforms** — products whose entire identity is MBSE, typically with a repository-centric, multi-user posture and their own language/method stack
- **Enterprise-lifecycle-embedded platforms** — modeling tools deeply integrated into a vendor's wider engineering lifecycle suite (requirements, ALM, change)
- **Lightweight / open-source modeling workbenches** — single-user tools with standards-compliant models and diagram views but without repository, simulation, or validation machinery (e.g. Gaphor); they satisfy the defining core and serve learning, small projects, and documentation
- **Industry-package variants** — the same core with regulatory/industry overlays: automotive architectures, defense enterprise frameworks, functional-safety kits, cybersecurity viewpoints

A variant remains a **Variant** unless it changes the core structure — for example, a tool that only renders diagrams without a governed model has left the Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Diagramming Application | the diagram document is the artifact and shapes carry stencil semantics; an MBSE platform's diagrams are generated views of a governed model — remove the model and an MBSE platform degenerates into a diagramming tool |
| Engineering Requirements Management | requirement records (statements, attributes, baselines) are the system of record; models are integration targets; in MBSE the system model is the record and requirements are one element class or a linked external set — complementary, model-first vs record-first |
| System Simulation Platform | models the behavioral/physical dynamics of a design for analysis; an MBSE platform holds the system's architecture of record and hands behavior analysis to simulation tools through bridges |
| Software Architecture Modeling | same modeling technology, different subject: software structure vs the multi-discipline engineered system; MBSE products usually also model software, but the systems-engineering scope is the Type's center |
| Product Lifecycle Management / PLM | manages the product data estate (CAD, BOM, change, documents); the MBSE platform holds the system model and integrates with PLM rather than replacing it |
| CAE / Engineering Simulation | computes physical responses of a design scenario; unrelated record world, adjacent discipline |
| Digital Twin Platform | a persistent digital counterpart of a specific physical asset in operation; the MBSE model is a development-time engineering definition, not an operational replica |
| Engineering Document Management | manages documents as records; MBSE exists to replace document-centric specification with a governed model, though it generates documents from the model |

The most important boundary is with **Diagramming Application**, because both produce diagrams. The structural difference is whether the diagram is the artifact (drawing) or a view of a governed model (MBSE). The most important complementary relationship is with **Engineering Requirements Management**: the two Types coexist in the same programs, joined by traceability integrations.

## Representative Products

- IBM Engineering Rhapsody (heritage enterprise pole; UML/SysML modeling with simulation, code generation, and lifecycle-suite integration)
- CATIA Magic / No Magic — MagicDraw / Cameo Systems Modeler family (dominant SysML modeling tool family with server-side collaboration and simulation companions)
- Eclipse Capella (open-source workbench implementing the Arcadia method, with a large connector ecosystem)
- GENESYS, originally Vitech, now Zuken (pure-play MBSE platform with its own design language and method)
- Gaphor (open-source lightweight modeling application; anchors the minimal end of the Type)

The defining core was checked against the lightweight pole (Gaphor) and against the pre-MBSE document-centric practice to avoid defining the Type by today's repository-and-simulation-heavy implementations.

## Sources

Research date: **2026-09-09**

Primary sources:

- CATIA Magic / No Magic documentation (modeling tools, SysML v1 modeling, Magic Collaboration Studio / Teamwork Cloud) — https://docs.nomagic.com/
- GENESYS Help (Three Pillars of MBSE, Project Explorer, Views, Tools, Command Reference) — https://genesys-help.vitechcorp.com/genesys-help
- Eclipse Capella (home, features, Arcadia, add-ons) — https://www.eclipse.org/capella/
- IBM Engineering Rhapsody product page — https://www.ibm.com/products/systems-design-rhapsody
- Gaphor — https://gaphor.org/

> Sourcing limitation: IBM's product documentation site and Sparx Systems' site were not reachable from the research environment (HTTP 403). Rhapsody evidence is therefore product-page strength only, and the independent mid-market modeling-tool pole (Sparx Enterprise Architect) is under-sampled; the lightweight open-source pole (Gaphor) partially covers it. Precise operational details (exact rule sets, simulation semantics, numeric limits, edition boundaries) are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
