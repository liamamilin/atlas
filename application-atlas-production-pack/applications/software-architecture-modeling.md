# Software Architecture Modeling

## Overview

A **Software Architecture Modeling** application is a model-based authoring environment for describing the structure of software systems. It holds a persistent **model** of the system's building blocks and the relationships between them — where each element exists independently of any diagram — and produces **diagrams as views over that model**, so the same underlying description can serve different audiences without copies drifting apart.

The problem it solves is familiar to any team that documents systems with drawing tools: diagrams multiply, each becomes its own source of truth, and they silently disagree. Modeling tools replace "many independent drawings" with "one model, many views" — when an element changes, the change appears everywhere that element is shown. The modeled subject is the software system itself: what it consists of, what it depends on, and, with varying depth, how its pieces are deployed and how interactions between them play out.

The boundary that defines the Type is the model. Tools that only draw shapes — general diagramming and whiteboard applications, however heavily used for architecture sketches — are a different Application Type. So are tools that model something else: engineered multi-discipline systems (MBSE), business processes, API contracts, or database schemas.

## Users & Context

Primary users:

- **Software architects and principal/senior engineers** — author and maintain the model; design reviews; propose future changes
- **Development teams** — consult views to understand the systems they work on; onboarding into unfamiliar architecture

Secondary users:

- **Technical leads and engineering managers** — plan changes, communicate direction, track current vs future design
- **Product managers and business stakeholders** — consume high-level views (typically the context level) without technical detail
- **Enterprise architects** — at the suite end of the market, place system models into wider enterprise contexts (layers, viewpoints, frameworks)

Typical occasions of use: documenting an existing system ("current state"), designing a change ("future state") before implementation, explaining a system to a new joiner or a stakeholder, reviewing a proposed design, and keeping architecture descriptions trustworthy as systems evolve. Work happens in a shared space — a SaaS workspace, a version-controlled code repository, or a desktop project file — depending on the product.

## Core Model

### The defining core

Three structures together make the Type recognizable. Remove any one and the product stops being an architecture modeling tool.

```text
Architecture Model  (source of truth)
├── Elements
│   ├── people / actors who interact with the system
│   ├── software systems (including external ones it depends on)
│   └── building blocks inside a system
│       (deployable units/apps, data stores, components/services)
├── Relationships
│   └── named, directed dependencies between elements
│       ("uses", "reads from and writes to", …)
└── Views / Diagrams
    └── scoped visual renderings of model elements
        for a specific audience or question
```

- **The architecture model is the unit of record.** Elements and relationships are persistent, named, reusable records. They are created once and referenced by many diagrams; each carries identity, description, and often metadata (technology, ownership, tags) that follows the element wherever it appears. In every researched product, an element deleted from one diagram survives in the model and in other diagrams; only an explicit model-level deletion removes it everywhere.
- **Views are composed or rendered over the model.** A diagram is not a free-standing drawing: it is a selection or rendering of model elements, usually scoped to one subject (a system, a building block) and one level of detail. The model is the master — editing an element or relationship updates every view that shows it — while layout, grouping, and visual emphasis belong to the individual view. The same model therefore supports as many views as the team needs: one for executives, one for developers, one per subsystem.
- **The subject is software system structure.** The elements denote architectural things — systems, their deployable units, their data stores, their internal components, the people and external systems at the edges — not arbitrary shapes. The model answers structural questions: what does this system consist of, what does it talk to, what depends on this service, where does this data live.

### Standard capabilities

Mature products across the researched sample commonly add, on top of the core:

- **Abstraction levels with zoom** — the model is navigated at several levels of detail (typically: who uses the system and what surrounds it → the deployable units inside a system → the components inside a unit). Navigation mirrors the zoom: clicking into an element opens its next-level view. Specific level schemes vary — the C4 model's context/container/component levels, UML's package and component granularity, or ArchiMate's layers and viewpoints — but the level-and-zoom shape is common.
- **Typed elements and relationships** — building blocks usually carry a type (person, system, app/container, store, component) and relationships carry direction, a label, and often a technology or protocol. Some products enforce connection validity against a modeling language; others treat types as organizational aids.
- **Deployment modeling** — environments, deployment nodes (servers, clusters, cloud services), and instances of software placed on them, commonly with a dedicated deployment view. Depth varies considerably between products, from first-class objects to metadata overlays on the static model.
- **Dynamic views** — ordered interaction flows (a user journey, a request path) stepped over the static structure, complementing the "what exists" model with "how it behaves in this scenario".
- **Element documentation and metadata** — descriptions attached to elements and relationships; technology choices; tags that group elements by theme (deployment tier, risk, cost, team) and can be highlighted or filtered in views.
- **Evolution machinery** — element statuses distinguishing current, future/planned, deprecated, and removed; versioned snapshots or branches of the model; draft "future state" designs that can be proposed, reviewed, and merged; history/timeline of change.
- **Dependency analysis** — incoming and outgoing dependencies of any element across the whole model, and usually a filterable table of all relationships.
- **Model navigation and search** — a tree or browser of all model objects, cross-model search, and navigators that show an element's surroundings.
- **Sharing and publishing** — read-only viewers, share links or embeds, and exports to images, documents, documentation sites, or interchange formats.
- **Collaboration** — multi-user editing, comments on elements or diagrams, review and approval flows, ownership and permissions (absent at the single-user end of the market).
- **Notation and styling** — standard element shapes and icons (including cloud-provider iconography), themes, and consistent visual language across all views.

### One structure, many implementations

The core is conceptual; products realize it differently:

```text
Concept:      Model as source of truth
Realizations: GUI-canvas objects in a cloud workspace
              a textual model written in a DSL, kept in version control
              a desktop project file holding a standards-language repository

Concept:      Views over the model
Realizations: hand-composed diagram canvases selecting model elements
              declared view specifications rendered by the tool
              viewpoints that filter a standards-language model

Concept:      Modeling language
Realizations: C4 model · UML · ArchiMate · ad-hoc team vocabularies
              (enforced grammars, advisory palettes, or free-form)
```

No single realization is the Type. A tool without a canvas can be architecture modeling (models-as-code); a tool without a formal language can be architecture modeling (ad-hoc vocabularies with true model semantics). What none of the Type's members lack is the model-with-views separation and the software-structure subject.

## How It Works

The canonical working loop:

```text
Establish a model container
  → author structure (add elements, connect with named relationships)
  → compose views for audiences
  → enrich elements (descriptions, technology, tags, ownership)
  → communicate (share, publish, export)
  → evolve (change the model; propose future state; keep the record current)
```

**1. Establish the model container.** Work begins in a container that scopes the model — a workspace or landscape for an organization's systems, a project or repository for one team's estate. Products differ in whether the container is cloud-hosted, a Git-tracked text file, or a local project file; the container always holds the model and its views together.

**2. Author structure.** Users add elements — the systems under discussion, the people who use them, the external systems they depend on — and connect them with named relationships. Authoring typically happens directly in a diagram: placing an object on a canvas or declaring it in a DSL both create a model element that can be reused elsewhere. Relationships are model objects in their own right, so a connection defined once can be surfaced in any view that shows both endpoints; many products also derive parent-level relationships from child-level ones automatically.

**3. Compose views.** For each audience or question, the author creates a diagram scoped to a subject and level: a context view for everyone, a unit-level view for engineers, a component view for a team. Elements are pulled in from the model (or added fresh, which also enters the model), arranged, and labeled. Mature products encourage many focused views rather than one exhaustive diagram, since the model guarantees the views stay mutually consistent.

**4. Enrich.** Elements receive descriptions, technology choices, tags, ownership, and links (to repositories, runbooks, or tickets). Enrichment attaches to the model element, so it follows the element into every view and can drive filtering, highlighting, and analysis.

**5. Communicate.** The views are consumed where the audience is: interactive read-only links or embedded views for browsers, exported images for documents, generated documentation sites, published pages in wiki or collaboration tools. Consumers usually navigate — zooming between levels, stepping through flows — rather than reading static pictures.

**6. Evolve.** The system changes; the model must follow. Authors edit elements (edits propagate to all views), draft future-state designs alongside the current one, mark elements deprecated or planned, snapshot versions, and — where the product supports it — link model objects to code repositories so the tool can signal when reality and model have drifted. Because a stale model is the Type's central failure mode, keeping-the-record-current mechanisms (statuses, versions, drift checks, accuracy reminders) are a distinctive part of the working loop, not an afterthought.

### Core vs common vs optional

**Defining core** — without these, not architecture modeling:

- persistent model of elements + relationships with identity independent of diagrams
- views/diagrams composed or rendered over the model, with model edits syncing across views
- software-system structure as the modeled subject

**Standard capabilities** — present across the researched market:

- multiple abstraction levels with zoom navigation
- typed element/relationship vocabularies
- deployment modeling (depth varies)
- dynamic/interaction views
- element documentation, metadata, tags
- statuses, versions, and current-vs-future design
- dependency analysis and cross-model search
- sharing, publishing, export surfaces
- collaboration machinery (except at the single-user pole)
- notation/styling control

**Optional / variant** — depends on segment and product philosophy:

- authoring substrate: canvas vs DSL-as-code (both in-type)
- modeling language: C4, UML, ArchiMate, ad-hoc
- repository linkage and drift detection; reverse-engineering from code
- architecture decision records and composed documentation
- inter-tool interchange (XMI-class), model diff/merge
- AI generation of models or diagrams
- sketch/ideation modes; suite breadth (process, data, requirements in one tool)

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Model browser / model tree

The model-level inventory.

- lists all elements (and often all relationships) regardless of which diagrams show them
- typical information: name, type, status, ownership, descriptions, which views contain it
- primary actions: create, edit, delete (model-level), search, open in a view

### Canvas diagram editor

The primary authoring surface in GUI-based products.

- renders model elements as positioned shapes with typed visuals; connections as labeled edges
- primary actions: add new or existing elements, connect, arrange, annotate, create child views by drilling into an element

### DSL / code editor

The primary authoring surface in models-as-code products.

- the model and its views declared as versionable text
- primary actions: declare elements and relationships, define views, validate, render, push/pull through version control

### Object inspector / detail panel

The per-element surface.

- shows everything the model knows about one element or relationship: type, status, description, technology, tags, connections, containing views, change history
- primary actions: edit details, manage links, view dependencies

### Level / zoom navigation

The cross-view navigation surface.

- indicates where the user is in the model hierarchy and which views exist at each level
- primary actions: zoom into an element's child view, move up a level, switch between sibling views

### Flow / dynamic view player

The behavioral storytelling surface.

- presents an ordered scenario as steps over the existing diagram
- primary actions: step forward/back, read step descriptions, switch scenarios

### Dependencies view

The analysis surface.

- shows incoming and outgoing dependencies for a chosen element, often including transitive/derived ones
- primary actions: filter, navigate to dependents

### Sharing / publishing surface

- read-only links or embedded views for non-editing audiences; export and publish targets for documents and docs sites

## Important Rules / Behaviors

**The model is the master; diagrams are views.** The single most consequential behavior. Removing an element from a diagram changes only that view; deleting the element is a separate model-level act that propagates everywhere. Conversely, editing an element anywhere edits it everywhere. Products make this distinction explicit because the alternative — per-diagram masters — is precisely what the Type exists to fix.

**Element identity is scoped and unique.** Elements are uniquely identified within a scope (commonly within their parent or container). Renaming or restructuring respects identity: the element persists across views and versions.

**Relationships are first-class model objects.** A relationship outlives any diagram that shows it, can be reused across views, and commonly derives parent-level ("implied") connections from child-level ones, keeping high-level views consistent with detailed ones without duplication.

**View layout is view-local.** Positions, groupings, colors-for-emphasis, and hidden elements belong to the view. Two views of the same element may look different while describing the same model fact — a feature, not an inconsistency, because semantics live in the model.

**Element status expresses lifecycle.** Current/live, future/planned, deprecated, and removed states (labels vary by product) let the model describe where the architecture is heading, not only where it is; views can include or exclude non-current elements.

**Language rules where a language is enforced.** Products built on a modeling language may restrict which connections are legal between which element types, or auto-derive conforming connections. Where no language is enforced, consistency is a team discipline rather than a tool constraint.

**Keeping the record current is a designed behavior.** Beyond manual editing, products add drift signals: version histories, review-and-merge for proposed changes, and — where supported — links into code repositories whose breakage or movement flags the model object as possibly stale. Architecture documentation that silently rots is the Type's acknowledged failure mode; the tooling treats currency as a property to be maintained, not assumed.

## Variants

The market realizes the Type in four stable shapes:

- **Collaborative SaaS canvas modelers** — cloud workspace, live multi-user editing, interactive share links; C4-style levels typical; aimed at engineering teams making architecture a team practice.
- **Models-as-code toolchains** — the model authored as text in a DSL, stored in version control, rendered to diagrams and documentation sites by CLI or server; Git review workflows replace in-tool approval; favored by architect-led, code-centric teams.
- **Multi-notation desktop suites** — a broad modeling platform carrying UML, ArchiMate, BPMN, ERD, and C4 side by side, with repository machinery (refactoring, diff, traceability), code engineering, and optional collaboration servers; the enterprise-suite pole, historically continuous with the UML-tool generation.
- **Single-user standards-language tools** — free or low-cost desktop editors for one modeling language (commonly ArchiMate), file-based, no server; the individual-architect and education pole.

Two further patterns sit adjacent rather than inside the Type: general diagramming tools used for architecture drawings (no model), and diagram-as-code renderers that produce one diagram per script (no persistent multi-view model) — though the latter are common export targets of genuine modeling tools.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Diagramming Application | primary boundary | shapes on a canvas, each diagram its own master; no persistent model, no cross-view sync, no structural query — even when used with architecture stencils |
| Digital Whiteboard | adjacent | freeform collaborative ideation; no element identity or model semantics |
| MBSE Platform | same technology, different subject | models a multi-discipline engineered system with requirements, behavior, parametrics, and verification machinery; software architecture modeling keeps the subject to software structure |
| System Design Application | adjacent sibling | design-exploration surface for proposed systems rather than a governed model of record (boundary needs its own research pass) |
| API Design Platform | downstream artifact layer | designs interface contracts, not whole-system structure |
| Database Schema Design Tool | downstream artifact layer | designs the data layer only |
| Application Portfolio Management | adjacent market | holds inventories of applications as lifecycle factsheets for portfolio decisions; does not author structural models of system internals |
| Developer Documentation Portal | consumption surface | publishes documentation; architecture models feed it (some tools export documentation sites directly) |
| CMDB / IT asset registries | different subject | records deployed operational assets as they are; architecture models describe designed and intended structure, including future state that does not yet exist |

The boundary with **Diagramming Application** is the load-bearing one, because general drawing tools are ubiquitous for architecture work. The structural test: if a team deletes an element from one diagram, does it disappear from the others? In diagramming, yes — each drawing is a master. In architecture modeling, no — the model outlives the view. The boundary with **MBSE Platform** is the subject: the same model-plus-views technology aimed at engineered multi-discipline systems with requirements and verification machinery is a different Type, even though suite products may straddle both by packaging.

## Representative Products

- **IcePanel** — collaborative SaaS modeling built on the C4 model; canvas authoring, zoomable levels, flows, tags, future-state drafts, repo-link drift detection
- **Structurizr** — "models as code" reference implementation of the C4 model; DSL + CLI + server, one model rendered to many views, Git-centric workflows
- **Visual Paradigm** — multi-notation modeling suite (UML, SysML, ArchiMate, BPMN, C4) with code engineering, repository machinery, and team collaboration
- **Archi** — free open-source desktop ArchiMate modeling toolkit; model tree, views and viewpoints, single-user

The core was checked against the market's older and differently positioned poles (the UML-suite generation, evidenced by suite products' own import compatibility with Rational Rose / Enterprise Architect files; and the single-user free pole) to avoid defining the Type by today's cloud-canvas implementation.

## Sources

Research date: **2026-09-09**

- IcePanel — product site: https://icepanel.io/ ; documentation (Getting started, Modelling, Diagramming, Linking to reality): https://docs.icepanel.io/
- Structurizr — documentation home and feature index: https://structurizr.com/help ; live DSL workspace grammar: https://structurizr.com/dsl
- Visual Paradigm — product site and feature map: https://www.visual-paradigm.com/
- Archi — product site: https://www.archimatetool.com/

> Sourcing limitation: Sparx Systems Enterprise Architect (the classic heavyweight repository-modeling pole) was unreachable from the research environment (request timeout; repeated failures also recorded in a same-day sibling pass). Its fit is supported only by category lineage and other vendors' documented import compatibility; no Sparx-specific claims are made in this document. Some Structurizr documentation subpages were unavailable (404) despite appearing in the site's navigation; its evidence is held at "documented feature exists" strength. Plan-gated product details (e.g., which tiers unlock specific features) are intentionally not asserted. Precise numeric limits and product-specific defaults are recorded in the paired Research Notes, not here.

Detailed product-by-product observations, the cross-product comparison matrix, abstraction decisions, and boundary analysis are recorded in the paired Research Notes.
