# Research Notes — Software Architecture Modeling

## Research Goal

Understand what a Software Architecture Modeling application is from real products: what the unit of record is (model vs diagram), what users actually do, how views relate to the model, which capabilities are definitional vs common vs optional, and where the Type's boundaries sit — especially against Diagramming Application, MBSE Platform, and the unprocessed sibling System Design Application.

This pass also discharges the forward flag pre-hung by the MBSE-platform pass ("vs software-architecture-modeling — same modeling technology, software subject vs engineered-system subject").

## Initial Boundary (working hypothesis before research)

- Core use: author and maintain a description of a software system's structure (systems, building blocks, dependencies, deployments) and communicate it to audiences.
- Likely unit of record: a persistent **model** with element identity independent of diagrams; diagrams are views over the model.
- Nearest neighbors: Diagramming Application (03.05), System Design Application (§12 sibling), MBSE Platform (§16), API Design Platform, Database Schema Design Tool, Application Portfolio Management (§14), Digital Whiteboard.
- Unknowns: is "model-based" (vs shape-drawing) actually the market's own distinction? Is a modeling language (C4/UML/ArchiMate) definitional? Are deployment/dynamic views definitional? Is collaboration definitional?

## Research Questions

1. What is the unit of record — model elements with identity, or per-diagram shapes?
2. How do views/diagrams relate to the model (composed selections? rendered? synced?)?
3. What element vocabulary do products use (people/actors, systems, containers/apps, components, stores, external systems, deployment nodes)?
4. How are relationships represented and reused (named, directed, technology-labeled, implied/lower-level)?
5. What abstraction levels exist (context → container → component; layers; viewpoints)?
6. Do products model deployment (environments, nodes, instances) and dynamic behavior (flows/sequences)?
7. What is the authoring loop end-to-end?
8. How is the model kept current (statuses, versions, future-state drafts, sync with code/infra)?
9. How is the model consumed (share links, viewers, exports, docs sites, embeds)?
10. Which capabilities vary by segment (collaboration depth, repository, code engineering, language enforcement)?
11. Where is the diagramming boundary — what separates modeling tools from Visio/draw.io-class tools, per the market's own framing?
12. Where is the MBSE boundary — software structure vs engineered-system subject?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy | Segment | Evidence tier reached |
|---|---|---|---|
| IcePanel | collaborative GUI modeling, C4-native, SaaS | engineering teams (startup→enterprise) | Tier 1 (official docs) |
| Structurizr | "models as code" (DSL + CLI + server), C4 reference implementation | architect-led teams, Git-centric | Tier 1 (official docs + live DSL playground) |
| Visual Paradigm | heavyweight multi-notation modeling suite (UML/SysML/BPMN/ArchiMate/C4) + code engineering + collaboration server | enterprise | Tier 2 (official product/feature pages) |
| Archi | free open-source desktop ArchiMate toolkit, single-user | individual architects, education, cost-sensitive orgs | Tier 2 (official product page + user guide reference) |

Boundary poles observed but not sampled as members: diagrams.net/draw.io, Visio, Lucidchart, Miro (general diagramming); PlantUML/Mermaid (diagram-as-code renderers); Sparx Enterprise Architect (unreachable — see Sources); LeanIX/Ardoq-class EA portfolio tools (adjacent market).

## Sources

- IcePanel product homepage — https://icepanel.io/ (fetched 2026-09-09)
- IcePanel Documentation — Getting started — https://docs.icepanel.io/getting-started.md (fetched 2026-09-09)
- IcePanel Documentation — Modelling — https://docs.icepanel.io/core-features/modelling.md (fetched 2026-09-09)
- IcePanel Documentation — Diagramming — https://docs.icepanel.io/core-features/diagramming.md (fetched 2026-09-09)
- IcePanel Documentation — Linking to reality — https://docs.icepanel.io/integrations/linking-to-reality.md (fetched 2026-09-09)
- Structurizr documentation home — https://structurizr.com/help (fetched 2026-09-09; serves site home with full feature/nav index)
- Structurizr live DSL editor/playground page — https://structurizr.com/dsl (fetched 2026-09-09; exposes workspace grammar: model + views + configuration)
- Visual Paradigm product homepage + feature map — https://www.visual-paradigm.com/ (fetched 2026-09-09)
- Archi product homepage — https://www.archimatetool.com/ (fetched 2026-09-09)

Source-access limitations:

- Sparx Systems Enterprise Architect: https://sparxsystems.com/products/ea/ timed out this pass; the MBSE-platform pass (2026-09-09) recorded 403 ×2 on the same domain. Treat Sparx as unreachable; the heavyweight-repository pole is covered indirectly via Visual Paradigm (which itself documents importing Enterprise Architect files). No precise claims about Sparx are made.
- Structurizr subpage URLs (/dsl/basics, /dsl/tutorial, /dsl/example, /as-code) returned 404 despite appearing in the site's own navigation; the reachable layer was the documentation home (which enumerates the full docs tree) and the live /dsl playground (which renders the workspace grammar). Claim strength for Structurizr DSL internals kept at "documented feature exists" level without deep semantics.
- IcePanel plan-gated features (Domains = Growth plan; edit permissions = Growth/Isolation plans; free-plan link limit) recorded as product-specific facts; not generalized.

## Product Observations

### IcePanel (Tier 1 — official docs; evidence layer A unless noted)

Positioning (homepage): "Collaborative diagramming and modelling tool for software architecture"; "Turn scattered diagrams to a single, trusted source of truth"; "Modelling keeps diagrams in sync"; "A view for each audience"; "Model your architecture for humans and agents".

Modelling vs diagramming (docs, Modelling page — A):
- "Modelling (in software architecture) is a way to see the full picture of how your system(s) work. It is view-agnostic and provides more detail than a single diagram."
- Stated benefits of model-based over "just shapes and lines": 1) Reusability (reuse same objects incl. connections and metadata), 2) Syncing diagrams ("when you change the reusable object, it updates in all other places it was referenced"), 3) Deeper insights ("your objects live in a source of truth, you can analyze how they're being used, what objects have specific traits or technologies"), 4) Consistency ("paired with a standard modelling language, such as the C4 model").

C4 model support (docs — A):
- The 4 C's: Level 1 Context, Level 2 Container (IcePanel renames to "App"; "Container is more commonly used for Docker"), Level 3 Component, Level 4 Code ("currently, you can't diagram the fourth level in IcePanel… link your model objects to the code itself (reality)… most IDEs can generate this level of detail on demand" — quoting the C4 author).
- IcePanel model object structure: Organization → Landscape → Domain (Growth plan) → Actor / Group / System → App or Store → Component.

Model object semantics (docs, Modelling + Diagramming pages — A):
- Object details: icon (linked to technology choices), name, connections, history, team edit access, internal/external type, abstraction (Actor/System/Group/App/Store/Component), **status (Live, Future, Deprecated, Removed)**, domain, ownership team, diagrams list, flows list, tags, display description (120-char cap; product-specific), detailed description (Markdown; API-importable), technology choices, custom links.
- Uniqueness rule: "Each model object must have a unique name within its scope" (same parent, or higher in hierarchy within the same Domain).
- "Adding and editing objects in diagrams automatically adds them to your model to be re-used later."
- Editing an object "will update it everywhere it exists. This includes all diagrams, flows, and the model… auto-sync everywhere."
- "Removing model objects from a diagram" (Backspace/Del or context menu) keeps them in the model; **deleting from the model** is a separate, irreversible Model-Objects-Tab action that deletes the object from all diagrams, connections, owned diagrams.
- "Using the delete key in a diagram does not remove objects from your model."
- "You can think of diagrams as a visual representation of a model. You can visualize the same model through different diagrams depending on what you want to communicate."

Connections (docs, Diagramming page — A):
- "Connections are stored in the model as relationships" — reusable across diagrams, synced.
- Connection details: name, team edit permissions, sender, receiver, status (Live/Future/Deprecated/Removed), direction (Outgoing default / No direction / Bidirectional), line shape, label position, diagrams list, flows list, tags, technology, links, detailed description.
- "Lower connections" (a.k.a. implied): connections between child objects surface at parent level and sync with the original.
- "Via Property": attach an intermediate object (e.g. Kafka, RabbitMQ topics/queues) onto a connection; reflected in the Dependencies view.
- Connections table: filterable list of all connections in the landscape.

Views & navigation (docs — A):
- Diagrams created with a **type and a parent object** (3 levels of connected diagrams per C4; Level 4 replaced by linking to reality).
- Zoom navigation: 🔎 icon on an object drills into its child diagram; numeric indicator of nested objects; blank child diagram created on demand.
- Custom landing diagram: per-diagram zoom targets so different views land on different child diagrams.
- Best practice (docs): "breaking complex diagrams into multiple diagrams that exist in parallel. Each diagram should communicate a specific message or architectural story and be tailored to a particular audience."

Storytelling layers (docs + homepage — A):
- **Flows**: "show how your system works in multiple scenarios or user journeys on the same view" — ordered steps over objects/connections with descriptions, Back/Next stepping (homepage: "Message flows — step through how data moves on top of existing diagrams").
- **Tags / perspective tags**: tag groups (e.g., deployment information, risk, cost) overlaid on diagrams; hide/focus/pin; "show multiple perspectives of your diagrams without duplicating them".
- **Drafts / current vs future**: homepage — "Fork your model to design your future and track where key architectural decisions are being made"; feedback/annotation; "Merge designs into your model once you've gained approval"; Phases ("phased release designs").
- **Dynamic views** (homepage): "View your model from different perspectives by overlaying details instead of hundreds of diagrams."

Collaboration & sharing (docs — A):
- Invite teammates as editors or viewers ("viewers… unlimited and free on all plans"); read-only **share links** and embeds (audience lands exactly where the creator was — position, selected object, Flow, Tags).
- **Versions**: "create versions of your landscapes to track changes and use the timeline to visualize how your architecture has evolved."

Reality linkage (docs, Linking to reality — A):
- Link model objects to source-control reality (GitHub, GitLab, Bitbucket, Azure DevOps): repos, branches, folders, files. "When those links move, change names or get deleted, we'll notify you that the object may need to be updated." Expired/missing links reduce an **Accuracy Score** "as a reminder to update the link or remove that object from your model."
- "We never request, store or copy your source code" — metadata (file tree, sizes, commit SHAs) only; periodic re-checks (30 min–1 h; product-specific).
- Dependency analysis: per-object Dependencies view (incoming/outgoing, direct + lower).

External validation of the market taxonomy (homepage testimonial — A, quoted attribution):
- The C4 model's creator lists the tool landscape as: "C4-PlantUML (diagrams as code) · diagrams.net (traditional diagramming) · IcePanel (browser-based modelling tool) · Structurizr (models as code)" — the market's own Modelling-vs-Diagramming vs Diagrams-as-code vs Models-as-code taxonomy.

### Structurizr (Tier 1 — official docs home + live DSL playground; layer A)

Positioning (docs home — A): "Structurizr is a 'models as code' tool designed for the C4 model - you write Structurizr DSL to create **multiple software architecture diagrams from a single model**." Created by the C4 model's author; "the reference implementation" for C4 compliance. "The as code approach is version control friendly, supporting traditional Git collaboration workflows."

Workspace grammar (live /dsl playground — A): a workspace contains
- `model` — `person`, `softwareSystem` (with `container`, incl. database-schema containers), `deploymentEnvironment` containing `deploymentNode` / `infrastructureNode` / `softwareSystemInstance` / `containerInstance` / `instanceOf`, plus `element`, and relationships `->` (and relationship removal `-/>`).
- `views` — `systemLandscape`, `systemContext`, `container`, `component`, `filtered`, `dynamic`, `deployment`, `custom`, `image`, `styles` (element/relationship styles, light/dark), `themes`, `terminology`.
- `configuration` — `visibility`, `scope`, `users`.

Docs-tree evidence (nav index of docs home — A at "documented feature" strength):
- Workspaces: DSL vs JSON file types; **scope** (landscape vs software system); recommendations; enterprise usage; inspections (model quality checks).
- DSL: identifiers, archetypes, **implied relationships**, expressions, includes, workspace extension, **Markdown/AsciiDoc documentation sections**, **Architecture Decision Records (ADRs)**, scripts, plugins (PlantUML/Mermaid).
- Server: workspace sharing, **workspace versions**, **workspace branches**, role-based access, diagram viewer vs diagram editor, notation customization, themes, perspectives, iframe/image embeds, diagram review; CLI commands: push, pull, lock, unlock, **merge**, **validate**, **inspect**, list, generate.
- Export: PlantUML, C4-PlantUML, Mermaid, WebSequenceDiagrams, **static site** (documentation site), PNG/SVG.
- Deployment variants: cloud service, on-premises server, (Lite/EOL noted).

Reading: the model (elements + relationships, including deployment instances) is authored once in DSL; views are declared specifications over that model; diagrams are rendered from views. Implied relationships and expressions are model-level derivation machinery. Documentation and ADRs attach to the model. This is the code-native realization of the same model/view separation IcePanel implements in a GUI.

### Visual Paradigm (Tier 2 — official product/feature pages; layer A at page-strength, suite breadth)

Positioning (homepage — A): "The comprehensive platform for Visual Modeling, Code Engineering, Agile Management, and Enterprise Architecture." Desktop + VP Online ("Unified Platform" hub; "100+ apps").

Modeling surface (feature map — A):
- Full UML editor set (class, sequence, use case, activity, state machine, **component**, **deployment**, package, composite structure, …); SysML (requirement, block definition, internal block, parametric); BPMN 2.0; ERD (conceptual/logical/physical transformation); **ArchiMate 3.x with viewpoints**; **C4 editors (System Context, Container, Component, System Landscape, Dynamic, Deployment)**; DFD; TOGAF ADM guide-through; Zachman; DoDAF/NAF/MODAF.
- Model management: sub-diagrams, **model refactoring**, **Model Transitor** (model versions), Logical View, Master and Auxiliary View, **Compare Diagram with Visual Diff**, **Dependency Analysis diagram + Matrix**, diagram layers, advanced search, model extractor, ETL table extraction, Doc. Composer / Project Publisher (documentation generation), glossary.
- Team collaboration server: concurrent editing, revision history (browse/compare/revert), **commit/update, conflict resolution, branching and tagging**, comments/annotation on diagram elements, change-request management; integrations (Confluence export, Jira, IDE round-trip).
- Code engineering: code generation, **reverse code to class/sequence diagram**, round-trip engineering; DB engineering (generate DB from ERD and reverse); REST API designer.
- Import: Enterprise Architect, Rational Rose, Rational System Architect, Rational Rhapsody, Archi (ArchiMate), XMI, Visio, PowerDesigner, ERwin — direct documentary evidence of the UML/EA-suite lineage this Type inherits.
- AI diagram generation (text-to-diagram, C4-PlantUML studio) — era-current add-on layer.

Reading: a suite realizing the same model/view separation across many notations, with repository-level machinery (refactor, diff, transitor, dependency matrix) that presupposes model elements with identity beyond any diagram. C4 appears as one notation family among many; the suite also reaches into requirements/BPMN/ERD — broader than the software-architecture core.

### Archi (Tier 2 — official product page; layer A at page-strength, single-user free pole)

Positioning (homepage — A): "The Open Source modelling toolkit for creating ArchiMate models and sketches. Used by Enterprise Architects everywhere… a low cost to entry solution… within a TOGAF or other Enterprise Architecture framework."

Modeling surface (product page — A):
- ArchiMate 3.2 support; "Easily and intuitively create all ArchiMate elements and relations"; **magic connector** "to create the correct connections between ArchiMate concepts" (language-governed connection validity); user-defined properties; custom color schemes.
- **Views and Viewpoints**: "create a new ArchiMate View and set its Viewpoint to the one that is suitable for the target audience and stakeholders. Add concepts that are aligned to the given Viewpoint to create a unique perspective on your model."
- **Model Tree** (the model repository), **Navigator**, **Visualiser** ("displays the selected model element and all of its relationships with other model elements in a radial-tree graphic… Selecting an element or relationship in the Model Tree, the Navigator or in a Diagram View will update the selection") — a model-first navigation surface.
- **Hints View** (in-tool description of elements/relationships/viewpoints).
- **Sketch View** ("Brainstorm your ideas with elements written on 'stickies'… 'soft' models… before transforming them to ArchiMate views") and **Canvas Modelling Toolkit** (re-usable canvas templates as a pre-design tool).
- Cross-platform desktop (Java/Eclipse RCP). Vendor-claimed download volume (~6,000/month) recorded as vendor claim only.

Reading: the single-user, file-based, standards-language pole. Model Tree + views + viewpoints confirm the model/view separation without any server or collaboration machinery — proving collaboration and SaaS delivery are not definitional. Archi's subject leans enterprise architecture (business + application + technology layers), showing the Type's edge where EA-tooling overlaps; the application/technology layers are the software-structure-relevant part.

## Cross-product Comparison

| Dimension | IcePanel | Structurizr | Visual Paradigm | Archi | Verdict |
|---|---|---|---|---|---|
| Unit of record | Model objects w/ identity (Landscape→System→App→Component); delete-in-diagram ≠ delete-in-model (A) | Workspace model in DSL; elements + relationships + deployment instances (A) | Project repository w/ model refactoring/diff/matrix (A) | Model Tree of ArchiMate elements (A) | **Defining core** (all four) |
| Views vs model | "Diagrams are a visual representation of a model"; multiple diagrams per level; view-local layout (A) | Views declared in DSL, diagrams rendered; multiple view kinds from one model (A) | Sub-diagrams, master/auxiliary views, visual diff over model (A) | Views + viewpoints over model; Visualiser from model tree (A) | **Defining core** |
| Subject | Software systems & their architecture (A) | Software systems (C4) (A) | Software + EA + process breadth; software architecture central among notations (A) | EA breadth; application/technology layers cover software structure (A) | **Defining core** (subject = system structure; breadth varies) |
| Abstraction levels / zoom | C4 levels 1–3 + zoom navigation (A) | Landscape/context/container/component views (A) | Packages/components; ArchiMate layers/viewpoints (A) | ArchiMate layers + viewpoints (A) | Common mature (universal in sample; level count varies) |
| Typed element vocabulary | Actor/System/App/Store/Component + status (A) | person/softwareSystem/container/instances (A) | UML/ArchiMate/C4 metaclasses (A) | ArchiMate elements (A) | Common mature (grammar strictness varies; market boundary is model-vs-shapes, not grammar) |
| Relationship semantics | Named, directed, status, technology, Via-property (A) | Named relationships + implied relationships (A) | Typed UML/ArchiMate relations + dependency matrix (A) | Magic connector enforces ArchiMate relations (A) | Common mature (realization varies) |
| Deployment modeling | Deployment info via tag groups (homepage A); no dedicated deployment-view doc observed | First-class: deployment environments/nodes/instances + deployment views (A) | Deployment diagram editor (A) | Technology layer elements (A, page-strength) | Common (realization depth varies; not observed as definitional anywhere) |
| Dynamic/behavioral views | Flows over static diagrams (A) | Dynamic views (A) | Sequence diagrams (A) | Not observed | Common (not definitional — absent in one sample) |
| Future state / statuses | Live/Future/Deprecated/Removed statuses; drafts fork/merge; phases (A) | Workspace branches + versions (A) | Revision history, Model Transitor, visual diff (A) | Not observed | Common (realization varies strongly) |
| Collaboration | Multi-user editing, viewers, comments, ownership, share links (A) | Server sharing, role-based access, branches, diagram review (A) | Concurrent editing, commit/merge, change requests (A) | Single-user desktop (A) | Common, NOT definitional (Archi pole) |
| Publishing/consumption | Share links, embeds, viewers (A) | Static documentation site, exports, iframe embeds (A) | Project Publisher, Doc. Composer, Confluence export (A) | Model file sharing (implied; not directly observed) | Common (form varies) |
| Authoring substrate | GUI canvas, SaaS (A) | DSL-as-code + CLI + server (A) | Desktop + cloud suite (A) | Desktop file-based (A) | Variant axis |
| Modeling language | C4 (enforced hierarchy) (A) | C4 (reference implementation) (A) | UML/SysML/ArchiMate/BPMN/C4 (A) | ArchiMate 3.2 (A) | Variant axis — language NOT definitional |
| Keep-in-sync-with-reality | Link to repos + Accuracy Score drift notifications (A) | Validate/inspect CLI; as-code Git workflows (A) | Reverse-engineering from code; round-trip (A) | Not observed | Common/optional (depth varies) |
| AI generation | — (not observed on fetched pages) | AI + MCP section in docs (DSL generation, landscape generation) (A, nav-index strength) | AI diagram generation suite-wide (A) | — | Era-current, optional |

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

A Software Architecture Modeling application is a model-based authoring environment whose defining core is exactly three jointly-held structures:

1. **The architecture model as the unit of record** — a persistent, growing set of named elements (the system's building blocks, the actors and external systems it interacts with) and named relationships between them, held as reusable records with identity **independent of any single diagram**. Remove → a diagramming application (shapes are masters), or an element catalog with no architectural surface.
2. **Views over the model** — diagrams/views are composed or rendered *from* model elements as the audience-facing surface; the model is the source of truth, edits to elements propagate across views, and the same model supports multiple views. Remove → shape drawing where every diagram is its own master, or a dead registry nobody renders.
3. **The software-structure subject** — the modeled thing is a software system's structure: what it consists of, what it depends on, and (varying depth) how it is deployed and how interactions play out. Remove → general diagramming/concept mapping, business-process modeling, or MBSE territory (engineered-system subject).

Jointly-held load-bearing checks:
- 1 alone = element/asset catalog (CMDB-ish inventory, no view loop)
- 2 without 1 = diagramming tool (each diagram master)
- 3 without 1+2 = whiteboard sketching of systems
- 1+3 without 2 = model database with no consumable surface
- 1+2 without 3 = generic structured concept-mapping tool

### L1 — Common Mature Structure (evidence layer B: cross-product)

- **Multiple abstraction levels / zoom** (C4 levels; ArchiMate layers/viewpoints; UML package/component granularity) with level-scoped diagrams
- **Typed building-block vocabulary** (people/actors, systems, deployable units, data stores, components/services, external systems) and **typed/labeled relationships** (direction, technology/protocol labels)
- **Deployment modeling** (environments, deployment nodes, instances) — depth varies from first-class (Structurizr/VP) to tag overlays (IcePanel)
- **Dynamic/interaction views** (flows over static structure; sequence-style views)
- **Element documentation** — descriptions, technology choices, custom properties/metadata attached to elements
- **Status lifecycle & evolution machinery** — live/current vs future/planned vs deprecated/removed; versions, history, drafts/branches
- **Dependency analysis** — incoming/outgoing dependencies of an element across the whole model
- **Model navigation & search** — model trees, navigators, object browsers, cross-model search
- **Sharing/consumption surfaces** — read-only viewers, share links/embeds, exports (images, docs sites, other formats)
- **Collaboration machinery** — comments/annotation, ownership/permissions, review flows (absent at the single-user pole)
- **Notation/styling control** — themes, element styles, standard shapes/icons (incl. cloud-provider iconography)

### L2 — Variant / Optional Structure

- **Authoring substrate**: GUI canvas (SaaS or desktop) ↔ DSL/models-as-code with CLI/Git workflows; both realize the same core
- **Modeling language**: C4, UML, ArchiMate, BPMN adjacency, ad-hoc vocabularies; language may be enforced (magic connectors, DSL grammar, C4 hierarchy) or advisory
- **Reality linkage**: reverse-engineering from code, repo linking with drift/accuracy signals, infra/cloud imports — optional depth
- **Documentation composition**: markdown docs sections, ADRs, generated documentation sites/documents
- **Enterprise repository features**: model diff/merge, XMI/inter-tool import-export, model transfer across versions
- **AI generation** of models/diagrams from text — era-current
- **Sketch/ideation modes** inside modeling tools (pre-model stickies/canvases)
- **Suite breadth** (BPMN/ERD/requirements/wireframes in the same tool) — suite-pole packaging
- **Delivery**: SaaS, self-hosted server, desktop files

### L3 — Vendor-specific (research notes only)

- IcePanel: Landscape/Domain hierarchy (Domain = Growth plan), Accuracy Score, displayed-description 120-char cap, 12 connection points per object, free-plan 10-object repo-link limit, Via Property naming, "The IcePanel Loop" branding, plan-gated edit permissions (Growth/Isolation)
- Structurizr: workspace lock/unlock CLI, client-side encryption of cloud workspaces, DSL archetype/implied-relationship semantics details, Lite/on-premises/cloud editions (Lite EOL), EOL-status pages
- Visual Paradigm: Model Transitor, PostMania annotation tooling, ORM/Hibernate tooling, DoDAF/NAF/MODAF toolsets, VPasCode branding, edition ladder
- Archi: jArchi scripting (plug-in ecosystem), co-Archi collaboration plug-in (not fetched; do not claim), Sketch/Canvas toolkits as branded features

## Vendor-specific / Rejected Findings

Rejected as definitional (considered and deliberately excluded from L0):

- **C4 model** — NOT definitional. Two samples are C4-native, one offers C4 among many notations, one is ArchiMate; the UML-suite generation predates C4 (VP documents importing Rational Rose / Enterprise Architect files). Language is a variant axis.
- **Diagram auto-generation** — NOT definitional. IcePanel diagrams are hand-composed selections of model elements; Structurizr views are declared and rendered; "views over the model" is the invariant, not "generated from code-level truth".
- **SaaS/collaboration** — NOT definitional (Archi single-user pole; Structurizr on-prem/self-host).
- **GUI canvas** — NOT definitional (Structurizr DSL pole).
- **Deployment views as first-class objects** — common, realization varies; not definitional.
- **Strict language-governed editing** — common in the sample but the market's own modelling-vs-diagramming boundary is model-vs-shapes, not grammar-vs-no-grammar; a tool with an ad-hoc element vocabulary but true model semantics would still be in-type. Held at L1.
- **Version control/Git built-in** — realization-dependent (as-code poles make it natural; GUI poles ship versions/timelines); "evolution machinery" is the common concept.
- **Cloud-service import, cost/risk tag overlays, AI generation, code generation/round-trip engineering** — optional/advanced.

## Boundary Findings

1. **vs Diagramming Application (03.05) — the primary boundary.** The market itself states the distinction: IcePanel's docs define modelling by reuse/sync/source-of-truth vs "just shapes and lines"; the C4 model's creator's own tool taxonomy separates "traditional diagramming" (diagrams.net) from "modelling tool" (IcePanel) and "models as code" (Structurizr). Operational test: delete an element from one diagram — in a modeling tool it persists in the model and other diagrams; in a diagramming tool each drawing is a master. Second test: "what depends on X?" answerable across the whole model implies model identity. General diagramming tools (Visio/Lucidchart/draw.io/Miro) are used for architecture drawings constantly — usage overlap is real, but they are a different Type; modeling tools' compare pages (IcePanel vs Visio/Lucidchart/draw.io/Miro) confirm the vendors position against that boundary themselves.
2. **vs MBSE Platform (§16) — DISCHARGED from this side, keep-both RATIFIED.** Same modeling technology (model + views + language-governed editing), different subject: software system structure vs multi-discipline engineered system with requirements/behavior/parametrics/verification machinery. Center-of-gravity seam, consistent with the MBSE pass's own observation that its sample carries software-modeling capability (Rhapsody Developer as explicit software pole). Suite products (VP with SysML) straddle by packaging, not by identity.
3. **vs System Design Application (§12 sibling, unprocessed) — FORWARD FLAG.** Likely adjacent: informal/exploratory design-space work (whiteboard-style system design, infra design) vs a governed model of record. This pass's evidence cannot resolve the sibling's actual market population; needs its own pass. Proposed seam: purpose-built persistent model + views vs design-exploration surface.
4. **vs Diagram-as-code renderers (PlantUML/Mermaid).** Single-diagram text renderings without a persistent multi-view model; heavily used *for* architecture diagrams but they are rendering targets — modeling tools export to them (Structurizr export list, A). Held boundary-adjacent, not in-type; the "models as code" pole (Structurizr DSL) is the in-type version of code authorship because the DSL declares model elements once and derives multiple views.
5. **vs Application Portfolio Management / EA portfolio tools (LeanIX/Ardoq-class).** Those hold inventories of applications as lifecycle factsheets for portfolio decisions; this Type authors structural models of system internals and dependencies. Adjacent markets that often coexist; no directory collision.
6. **vs API Design Platform / Database Schema Design Tool.** Single-artifact-layer design (interface contracts; data schemas) vs whole-system structure. Distinct.
7. **vs Developer Documentation Portal.** Publishing/consumption surface; architecture models feed documentation (static-site export in-sample) but the portal is downstream.
8. **vs CMDB / IT asset registries.** Operational deployed-asset records vs designed/intended structure (including future state that doesn't exist yet). Distinct subjects.

Historical / market-sample check (per §24):
- UML-suite generation (Rational Rose-class, 1990s–2000s): model + diagrams-as-views + typed elements — fits the L0 core with UML as the language. Direct lineage evidence: Visual Paradigm's own import list includes Rational Rose, Enterprise Architect, Rational System Architect/Rhapsody (A).
- Drawing-only practice (Visio with UML stencils): fails leg 1 — that practice is exactly what modeling tools position against; correctly excluded as Diagramming.
- Single-user free tool (Archi) and code-first tool (Structurizr) both fit without SaaS/collaboration/AI.
- The definition does not depend on C4, on GUI canvases, on cloud delivery, or on any status-name set. Historical check passed.

## Uncertainties

- Sparx EA (the classic heavyweight repository-modeling pole) unreachable this pass; its fit is inferred from category lineage and VP's import compatibility rather than direct evidence. No Sparx-specific claims made.
- Structurizr deep DSL semantics (implied-relationship rules, expression language details) documented at nav-index strength only; subpage URLs 404'd. No precise DSL semantics claimed.
- IcePanel's deployment modeling: only tag-group evidence fetched; no dedicated deployment-view doc observed. Depth deliberately not characterized.
- Archi's model file format and sharing mechanics (`.archimate` files) not directly verified from fetched pages; not claimed in the final document.
- Market-share/adoption figures intentionally not asserted (Archi's download claim recorded as vendor claim only).
- Where the Diagramming Application pass will draw its own edge (does a "diagramming application with C4 stencils" get claimed by that leaf?) is unresolved from this side — recorded as a cross-pass note rather than a unilateral boundary ruling.

## Final Synthesis

Software Architecture Modeling is the model-based authoring Type for software system structure. Its members share one defining shape: a persistent model of named building blocks and their relationships, held with identity independent of any diagram; diagrams exist as views composed or rendered over that model for specific audiences, with edits to the model syncing across views; and the subject is what a software system consists of, what it depends on, and how it is arranged and (with varying depth) deployed.

Everything else is layered on top: abstraction levels and zoom, typed vocabularies and languages (C4/UML/ArchiMate/ad-hoc), deployment and dynamic views, documentation and decision records, statuses/versions/future-state design, dependency analysis, collaboration and review, sharing/publishing, reality-linkage and reverse engineering, AI generation. The market realizes the Type in four stable shapes — collaborative SaaS canvas modelers, models-as-code toolchains, multi-notation desktop suites, and single-user standards-language tools — plus a large penumbra of general diagramming tools used for architecture drawings that lack the model and are therefore a different Type.

The Type is distinct from MBSE (engineered-system subject), from diagramming (no model identity), from diagram-as-code renderers (no persistent multi-view model), from portfolio/EA management (inventory vs structure authoring), and from artifact-layer design tools (API/DB).
