# System Design Application

## Overview

A **System Design Application** is an application for designing the structure of a software system — working out what the system will consist of, what it depends on, how its pieces are arranged and deployed, and how interactions between them flow — and communicating that design to the people who will review, build, and operate the system.

Two things about this category should be stated up front, because they shape everything else in this document:

**"System design application" is a practitioner label, not a vendor category name.** Engineers say "system design" for the activity; no significant product sells itself under this name as a category today. Vendors sell modeling tools, diagramming tools, design-doc workspaces, and cloud design tools — and the label is claimed, in one way or another, by all of them. At least one product that once led its marketing with "system design platform" has since left the category entirely and now sells a debugging agent.

**The market serves the activity through three product shapes with different centers of gravity:**

1. **Governed architecture modeling tools** — the design held as a living model, with diagrams as views over that model. This population is documented as its own Type: **Software Architecture Modeling**.
2. **Design workspaces** — the design held as artifacts: structural diagrams kept together with the written design document, in a workspace built for fast iteration and review.
3. **Cloud-infrastructure design and topology tools** — the design target is cloud infrastructure; products range from design-first surfaces that generate deployable infrastructure code, to tools that automatically diagram what is actually running.

This document describes what these tools share — the design activity and its artifacts — how the shapes differ, and where the boundaries sit. Readers who need the governed-model population in depth should read **Software Architecture Modeling**; readers who need generic drawing should read **Diagramming Application**.

## Users & Context

The primary users are the people who design software systems for a living:

- **Software engineers and tech leads** — draft a design for a new service or feature, write the accompanying design document, take it through review before building.
- **Software and solution architects** — own the structural picture across services; propose changes to existing systems; communicate designs to stakeholders.
- **DevOps, platform, and cloud engineers** — design cloud infrastructure: network topology, environments, resource arrangements; increasingly, design it in a form that generates deployable code.
- **Technology consultants and pre-sales engineers** — produce client-facing architecture diagrams and solution documents quickly and consistently.

The work context is the design loop that engineering organizations run around building software: a proposal or RFC is framed, the structure is drafted, the design is reviewed and argued over, decisions are recorded, and the accepted design is handed off to implementation — after which someone must keep the picture current as the system evolves. Designs are consumed in review meetings, in wikis and documentation portals, and by new joiners trying to understand a system they did not build.

## Core Model

### The shared content basis

Whatever the product shape, the same content basis recurs:

**The system under design.** The subject: a software system (a service, an application, a platform estate) or a cloud infrastructure environment. Everything else in the model describes this subject.

**The structural description.** The heart of the artifact: the system's components or resources and the relationships between them — what talks to what, what depends on what, where things run. Mature tools commonly add views for the deployment arrangement (environments, regions, clusters) and for interaction flows (how a request travels through the structure). In every shape, the description is **editable and maintained** — it is an artifact the team works on, not a one-off picture.

**The design documentation.** The written rationale that travels with the structure: goals and non-goals, constraints, the options considered, the decisions taken and why, rollout plans. In the design-workspace shape this is a first-class artifact — a document in the same file as the diagrams, with the diagrams embedded in it. In the modeling shape it attaches to the model itself (element descriptions, decision records). Cloud-design tools typically carry little or none of it; the generated infrastructure code is the record.

**The design loop.** Draft → review → iterate → baseline and hand off. The loop is what makes this an application category rather than a file format: the tools exist to move a design through argument and revision, and — in some shapes — to keep it current afterward.

### Where the description lives: the three shapes

The shapes differ on exactly one question: **where the structural description is kept, and what it is attached to.**

**The governed model** (Software Architecture Modeling territory). The description is a persistent model: named elements with identity independent of any diagram, and diagrams composed as views over the model. Edit an element once and every view that shows it updates; delete it from one diagram and it survives in the model. The model is the source of truth, and keeping it current as the real system evolves is a designed-in job (statuses, versions, drift checks against code repositories). This is the shape to choose when the architecture description must stay trustworthy for years. Its full working model is documented under **Software Architecture Modeling**.

**The design workspace.** The description lives in **design artifacts**: a file (or folder of files) that holds structural diagrams together with the written design document. Each diagram is its own master — there is no model layer above the diagrams. What the shape adds over plain drawing is the pairing and the loop: diagrams embedded inside the design document; fast authoring paths (direct canvas editing, text-based diagram languages, and AI generation from a prompt, an image, or an existing file); generation grounded in the team's own conventions (templates, naming and notation rules, reference architectures); sources of truth such as code repositories and cloud accounts used as **inputs that a diagram can be generated from**; and review machinery — comments, mentions, sharing, version history — wrapped around the artifact.

**The cloud design and topology surface.** The description is written in **cloud resources**: the vocabulary is the provider's own building blocks (networks, subnets, clusters, managed services), not abstract components. Two postures share this vocabulary. The design-first posture treats the canvas as the place to compose a proposed infrastructure architecture — commonly with the property that the design **generates deployable infrastructure code**, and sometimes with cost and policy checks attached to the design itself. The topology-documentation posture treats the diagram as a **rendering of what actually exists**: connect a cloud account, and the tool generates and continuously refreshes the diagram from the live environment, keeping version history so changes over time can be compared.

### Standard capabilities of the design-workspace shape

The workspace shape is the leaf's own center of gravity. Its evidenced capabilities — documented at full depth by one active product, with the pivoted second product corroborating the shape — are:

- **Diagrams and documents in one artifact** — live diagram embeds inside the written design document, so the picture and the rationale cannot drift apart.
- **Multiple authoring paths** — direct canvas editing; a text-based diagram language (so a diagram can be read, diffed, and edited as code); and AI generation from prompts, images, or files such as infrastructure definitions and database schemas.
- **Convention-grounded generation** — templates, rules, reference libraries, and style presets that make generated diagrams match the team's notation instead of a generic look.
- **Sources of truth as generation inputs** — code repositories (diagrams generated from the codebase, kept current by CI) and cloud accounts (diagrams generated from a scan of the environment).
- **Review and collaboration machinery** — comments, mentions, sharing and permissions, version history, folders for organizing the design corpus.
- **Publishing and export** — images, embeds, links, exports to interchange formats, and push into Git or documentation tools.
- **Agent access** — an interface that lets coding agents create, read, and update diagrams as part of their work.

## How It Works

The canonical working loop, described across the shapes:

```text
Frame the design
  → draft the structure
  → iterate
  → review and decide
  → hand off — and keep current (in the shapes that do)
```

**1. Frame the design.** The work starts in the written layer: context, goals and non-goals, constraints. In the workspace shape this is the design document itself — in the researched sample it is outlined from templates or drafted with AI, shaped around familiar engineering forms (proposals, RFCs, decision records). In the modeling shape the framing attaches to the model as descriptions and decision records.

**2. Draft the structure.** The structural description is produced. Three authoring paths coexist in current products: placing and connecting components on a canvas; writing the structure in a diagram language and letting the tool lay it out; and describing the system in plain language (or pointing the tool at a codebase, a cloud account, or an uploaded file) and letting generation produce the first draft. In the cloud-design shape, drafting means composing the architecture from the provider's real resources — with infrastructure code generated as you design.

**3. Iterate.** The draft is reshaped: refine by hand on the canvas, keep chatting with the generator, edit the diagram-as-code text, or — in the modeling shape — fork the current design into a proposed future state and change the copy. Speed of iteration is the shape's defining value: the tooling is optimized for getting a revisable structure on the table in minutes.

**4. Review and decide.** The design artifact is shared — a link, an embed in a wiki, a review session. Reviewers comment on diagrams and documents, propose changes, and the design is argued into acceptance. Version history preserves the loop's record: what was proposed, what changed, what was decided.

**5. Hand off — and keep current.** The accepted design is handed to implementation: exported into documentation, pushed into a repository, or — in the cloud-design shape — deployed as generated infrastructure code. What happens next separates the shapes. The governed-model shape treats keeping the description current as a first-class job (statuses, versions, drift checks against code). The workspace shape treats currency as a re-generation act: a diagram produced from a codebase or a cloud scan is a snapshot, refreshed by re-running the generation (manually or through CI). The topology-documentation shape automates currency entirely — the diagram is regenerated from the live environment whenever it changes, with the previous version archived for comparison.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Canvas diagram editor

The primary authoring surface in every shape: an unbounded drawing area where components (or cloud resources) are placed, connected, grouped, and labeled. In workspace-shape products the canvas sits beside a text editor for the design document; diagrams can be embedded live into the document.

### Document editor

The written-design surface of the workspace shape: a markdown-grade editor holding the design document, with live diagram embeds, tables, and links. Generation can target the document as well as the diagram (an outline, an inventory, a description of how a workload is wired).

### Model browser (governed-model shape)

The inventory surface of modeling products: all elements and relationships regardless of which diagrams show them, with types, statuses, and ownership. Documented fully under Software Architecture Modeling.

### Cloud connection and resource surfaces

The cloud shapes' entry surfaces: connecting a cloud account or subscription, scanning or continuously syncing the environment, and a palette of the provider's real resources for composing designs. The topology posture adds history and comparison surfaces (diagram versions, change alerts).

### Review and share surfaces

Sharing and permission dialogs, comment threads anchored on diagrams and documents, presentation or walkthrough modes, and export/publish targets (images, embeds, links, Git, documentation tools).

### Version history

The design loop's record in every shape that has a loop: snapshots of the artifact over time, with restore and — in the topology posture — automatic archiving of every regenerated version.

## Important Rules / Behaviors

**Each diagram is its own master in the workspace shape.** Editing a component in one diagram does not change any other diagram, and there is no model layer whose edits propagate across views. This is the structural line between the workspace shape and governed modeling: the moment a team needs element identity and cross-view consistency, it has outgrown the workspace shape and wants Software Architecture Modeling.

**Sources of truth are inputs, not synchronized state.** In the workspace shape, a diagram generated from a codebase or a cloud environment reflects the moment of generation. Cloud-generated diagrams in the researched sample are drawn from the **most recent scan**, not the live account — refreshing requires an explicit re-scan (or a CI job that regenerates on change). Treating a generated diagram as automatically current is the shape's characteristic failure mode.

**Design and live state are different postures.** A design artifact describes what is proposed; a topology diagram describes what exists. Products that serve both keep the two distinct — a proposed architecture is authored and revised; a live topology is generated and refreshed. The design loop and the keep-current loop are different loops, and the shapes specialize accordingly.

**The written rationale is first-class where the shape carries it.** In the workspace shape, the design document — not the diagram — is the artifact of record for review: goals, constraints, decisions, and rollout live in prose beside the embedded pictures. Cloud-design shapes typically invert this: the generated infrastructure code is the record, and the diagram is its view.

**Version history is the loop's memory.** Whether snapshots are taken on save (workspace shape), on merge (modeling shape), or on every detected environment change (topology posture), the retained history of the artifact is what makes design decisions traceable.

## Variants

The label's population, by shape and pole:

- **Governed architecture modeling** — the design as a living model with views; the "keep it current for years" pole. Documented as Software Architecture Modeling (collaborative SaaS modelers, models-as-code toolchains, multi-notation suites, single-user language tools).
- **Design workspaces** — diagrams + design documents with fast authoring and review; the "propose and align quickly" pole. Current products are AI-first (generation from prompts, images, files, codebases, cloud scans) with diagram-as-code and canvas editing beneath.
- **Cloud design-first** — compose proposed cloud architectures from real provider resources, generating deployable infrastructure code, commonly with cost estimation and policy checks at design time and Git-based deployment pipelines.
- **Cloud topology documentation** — connect cloud accounts and auto-generate continuously refreshed diagrams of what is running, with version history, change alerts, cost overlays, and export/embed surfaces.
- **Design + live hybrids** — products that hold both postures: author proposed architectures and also visualize the live footprint.

A market-drift note: dedicated products once marketed as "system design platforms" have not held the position — the most prominent has pivoted entirely to runtime debugging. The activity persists; the category name did not stabilize around a product family.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Software Architecture Modeling | sibling Type owning the governed-model population | model-of-record with element identity and cross-view sync vs design artifacts (per-diagram masters + documents); the structural test: delete an element from one diagram — does it survive elsewhere? |
| Diagramming Application | adjacent; owns generic drawing | shapes + connectors for any diagram type, each diagram its own master; the workspace shape is diagramming-grade at the canvas but is organized around the system-design activity (design docs, generation from code/cloud, review loop) |
| Digital Whiteboard | adjacent | freeform ideation surface; no notation discipline, no persistent design artifact |
| MBSE Platform | same verb, different subject | "system design" over multi-discipline engineered systems with requirements/behavior/verification machinery; this leaf's subject is software and cloud systems |
| API Design Platform | downstream artifact layer | designs interface contracts, not whole-system structure |
| Database Schema Design Tool | downstream artifact layer | designs the data layer only; drawing an ERD in a design workspace is a picture, not a managed schema |
| Infrastructure-as-Code Platform | downstream of the cloud-design pole | the cloud-design surface generates IaC; the IaC platform owns code, state, and pipelines. Design-first visual surfaces that stop at generated code stay on this leaf's cloud pole |
| Application Portfolio Management | different job | inventories of deployed applications as lifecycle factsheets for portfolio decisions; no design authoring |
| Internal Developer Portal / Developer Documentation Portal | consumption surface | publishes architecture knowledge; design tools produce what those portals serve |
| Observability / debugging tools | drift destination | the pivoted "system design platform" products moved here (runtime session capture, debugging agents) — a different Type |

The load-bearing boundary is with **Software Architecture Modeling**: both populations design software systems, both claim the "system design" vocabulary, and the difference is purely structural — whether the design is a governed model whose edits propagate across views, or a set of design artifacts worked through a review loop. The secondary boundary is with **Diagramming Application**: the workspace shape's canvas is diagramming-grade, and a diagramming tool used occasionally for architecture drawings stays a diagramming tool; the workspace shape is distinguished by the design-document pairing, generation from sources of truth, and the review-centered loop.

## Representative Products

- **Eraser** — the design-workspace pole: AI diagram generation, diagram-as-code, design documents with embedded diagrams, codebase and cloud-scan generation, review/collaboration machinery, agent access.
- **IcePanel** — the governed-model pole (documented under Software Architecture Modeling); included here as the boundary anchor, since it markets its design-process layer in "system design" language.
- **Cloudcraft** — cloud design + live topology: 3D cloud architecture diagrams for AWS/Azure, planning new architectures and visualizing the live footprint.
- **Hava** — cloud topology documentation: automated diagrams generated and continuously refreshed from connected cloud accounts, with version history and drift alerts.
- **Brainboard** — cloud design-first: multi-cloud visual designer that generates deployable Terraform, with drift detection and embedded pipelines.
- **Multiplayer** — recorded as market drift: formerly marketed as a "system design platform"; now a debugging agent with no design surface remaining.

## Sources

Research date: **2026-09-09**

- Eraser — product site: https://www.eraser.io/ ; documentation ("What is Eraser?", Figures, Cloud diagrams): https://docs.eraser.io/ ; AI Documents product page and Design Docs use-case page: https://www.eraser.io/product/ai-documents , https://www.eraser.io/use-case/design-docs
- IcePanel — product site: https://icepanel.io/ (deeper documentation evidence held in the Software Architecture Modeling record: https://docs.icepanel.io/)
- Cloudcraft — Datadog documentation, "Cloudcraft (Standalone)": https://docs.datadoghq.com/cloudcraft/
- Hava — product site: https://www.hava.io/
- Brainboard — product site: https://www.brainboard.co/
- Multiplayer — product site and documentation: https://www.multiplayer.app/ , https://www.multiplayer.app/docs/

> Sourcing limitations: Lucidscale (the Lucid-family cloud-visualization product) was unreachable (403) and is not claimed anywhere in this document. Cloudcraft's marketing root was unreachable (403); its evidence comes from the Datadog documentation overview. Hava and Brainboard are evidenced at product-page strength; their deeper documentation was not fetched, so no precise operational details (sync intervals, limits, plan gating) are asserted for them. The design-workspace shape's market depth is calibrated to the researched sample: one active product documents it at full depth, and the historical second product has pivoted out of the category. Detailed product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
