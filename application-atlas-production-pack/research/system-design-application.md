# Research Notes — System Design Application

## Research Goal

Resolve what the directory leaf **System Design Application** (§12 Software Development & Product Engineering) corresponds to in the real market, and discharge the forward flag left by the software-architecture-modeling pass (2026-09-09), which proposed the seam "governed persistent model-of-record + views vs design-exploration surface" but could not resolve this sibling's population from its own evidence.

Specifically:

1. Is there a coherent product population that sells itself as "system design" tools, distinct from Software Architecture Modeling and Diagramming Application?
2. If yes — what is its defining core? If no — what is the leaf actually a label for, and which documented Types own its populations?
3. Where do the boundaries sit (modeling vs exploration vs cloud-infrastructure design vs live topology visualization)?

## Initial Boundary

- **Working hypothesis at start**: the leaf is the "design-exploration surface" sibling of Software Architecture Modeling — tools for designing proposed systems without a governed model-of-record (per the SAM pass's proposed seam).
- **Adjacent Types to watch**: Software Architecture Modeling (§12 sibling, processed), Diagramming Application (03.05, processed), Digital Whiteboard (03.05), MBSE Platform (§16), API Design Platform / Database Schema Design Tool (§12 artifact layers), Infrastructure-as-Code Platform (§14), Application Portfolio Management (§14), Internal Developer Portal (§12), observability Types (§14).
- **Known complication**: the phrase "system design" is a practitioner term (the activity of designing a software system's structure), not obviously a vendor category. The research must determine whether a vendor-led category exists at all.

## Research Questions

1. Which products self-identify with "system design" language, and what do they actually do?
2. What is the unit of record in each candidate product — a governed model, a design file (diagrams + docs), a cloud-resource design, or an auto-generated topology?
3. Do the candidate products share a core structure that neither Software Architecture Modeling nor Diagramming Application already owns?
4. Is the population stable, growing, or drifting (products entering/leaving the label)?
5. Historical check: what served "system design" before the current generation, and would older products fit a candidate definition?

## Representative Products

Selected to cover the different product shapes that claim the "system design" label, plus the drift case:

| Product | Shape | Why selected |
|---|---|---|
| **Eraser** | AI diagramming + design-doc workspace | The most explicit active claimant of the "system design" activity label; Tier-1 documentation |
| **IcePanel** | Governed model-of-record modeling (Software Architecture Modeling territory) | Boundary probe: a modeling product that markets its design-process layer in "system design" language |
| **Cloudcraft** | Cloud design + live topology (3D, AWS/Azure) | Design-first cloud pole ("plan new architectures") owned by Datadog; self-labels "diagramming tool" |
| **Hava** | Automated live-cloud topology visualization | Visualization-first pole ("ditch your drawing tools"); continuous sync from cloud accounts |
| **Brainboard** | Cloud design → IaC generation → deploy | Design-first cloud pole with deployable-code output; strongest "design the cloud system" product |
| **Multiplayer** | Former "system design platform", now pivoted | Market-drift evidence: the loudest historical self-labeler has left the category |

Rejected as representatives: Excalidraw/tldraw/Miro (whiteboard family — excluded by the diagramming pass's boundary), PlantUML/Mermaid/Kroki (renderers, no persistent artifact workspace), draw.io/Lucidchart/Visio (already documented under Diagramming Application), Structurizr/Visual Paradigm/Archi (already documented under Software Architecture Modeling), Lucidscale (unreachable — recorded as limitation).

## Sources

Research date: **2026-09-09**. All fetches from the research environment on this date.

| Source | Tier | Status |
|---|---|---|
| Eraser — product site (eraser.io), docs root, "What is Eraser?", Figures doc, Cloud diagrams doc, AI Documents product page, Design Docs use-case page | Tier 1 (official docs + product pages) | Fetched OK |
| IcePanel — product site (icepanel.io) | Tier 2 (product page; sibling pass holds Tier-1 docs evidence) | Fetched OK |
| Cloudcraft — Datadog docs "Cloudcraft (Standalone)" overview (docs.datadoghq.com/cloudcraft/) | Tier 1 (official docs) | Fetched OK (cloudcraft.co root 403; datadoghq.com/products/cloudcraft/ 404) |
| Hava — product site (hava.io) | Tier 2 (product page; user/developer docs linked but not fetched) | Fetched OK |
| Brainboard — product site (brainboard.co) | Tier 2 (product page; docs.brainboard.co linked but not fetched) | Fetched OK |
| Multiplayer — product site (multiplayer.app) + docs root + web-dashboard docs | Tier 1 (official docs) | Fetched OK |
| Lucidscale (lucidscale.com, lucidchart.com/pages/lucidscale) | — | 403 ×2 — abandoned per network rule; no claims made |
| Cloudcraft marketing root (cloudcraft.co) | — | 403; evidence taken from Datadog docs instead |

## Product Observations

### Eraser (Tier 1 — docs + product pages)

**Self-positioning**: "Eraser creates production-ready diagrams in seconds using AI" (docs, "What is Eraser?"). Marketing headline: "AI for diagrams that matter". Use cases listed: Architecture Diagrams, Design Docs, Documentation, Brainstorming, Wireframes, plus a long tail (Kubernetes architecture, API diagrams, auth flows, state diagrams, dependency diagrams, threat modeling, network diagrams, Git diagrams…). The Design Docs use-case page states: "Trusted by Fortune 100 companies with their system design" — an explicit claim on the "system design" activity. Solutions pages target enterprise architects, DevOps, technology consultants, software engineers.

**Structure (from docs)**:

- **File as container**: a file holds **diagrams** (canvas) and **markdown documents** (note editor) together. "Diagrams sit alongside markdown documents in the same file" (What is Eraser?). REST API operates at file/diagram granularity: list/create/get/update/archive files; list/create/get/update/delete diagrams **in a file**; folders organize files. **No element-level model API is documented** — no model tree, no element identity across diagrams, no cross-view sync machinery in the documentation navigation or API surface.
- **Canvas**: insert menu, figures (containers that group canvas elements; figures can be embedded live into the note editor via figure embeds), drag-drop editing (beta).
- **Diagram-as-code**: Eraser DSL for architecture diagrams, flowcharts, ERDs, sequence diagrams, BPMN; "anything AI produces can be read, diffed and edited as text".
- **AI generation**: prompt → diagram; image → diagram; file → diagram (Terraform, database schema, PDF/Word/Excel/PowerPoint/Draw.io/Visio); chat-based refinement; AI presets, rules ("naming & notation rules", "PCI data boundaries"), references ("reference architectures and domain knowledge"), custom styles, templates — all to make generation consistent with the team's conventions.
- **Cloud environments**: connect AWS/Azure/GCP; Eraser scans the environment; cloud diagrams are generated **from the newest scan, not the live account** ("There is no scheduled background scan"); multiple environments can be attached to one prompt; can also ask for a **document** (inventory, workload description) instead of a diagram.
- **Git integration**: connect repositories; codebase diagrams; Eraserbot keeps codebase diagrams current via CI; Git sync (push markdown docs to Git).
- **Collaboration**: folders, sharing, comments, private files, version history, mentions; teams/organizations, SAML SSO, SCIM.
- **Agents**: MCP server (full diagram CRUD from Claude/Cursor/ChatGPT), agent integrations, open-source agent toolkit.
- **Design docs product (AI Documents)**: generate design docs/documentation grounded in company templates and codebase; interactive AI follow-up questions; template-based outlines; use cases: RFCs, PRDs, ADRs, project documentation, compliance docs, team knowledge repository. "Docs + Canvas — Eraser's unique embeds let you drop diagrams directly into your documents."

**Reading**: Eraser's unit of record is the **file** (diagrams + documents); diagrams are per-diagram masters; there is no governed cross-view model. It is a design workspace: fast authoring/generation of structural diagrams plus the written design document, with review/collaboration machinery, and sources-of-truth (Git, cloud scans) used as **generation inputs**, not as a synchronized model.

### IcePanel (Tier 2 own fetch; Tier 1 evidence held by the sibling SAM pass)

**Self-positioning**: "Collaborative diagramming and modelling tool for software architecture". Product pages: "C4 Model — Model your systems for the long term"; "Software architecture diagramming"; "Planning and design — Design for now and for the future".

**"System design" language on the modeling pole**: homepage states "Accelerate your design process — The essentials to keep your **system design** moving forward and up-to-date" and "Design systems like you build them — Draft future ideas, gain feedback and iterate before committing to new/improved technical directions" (fork current-vs-future, feedback/annotation, merge, phases, dynamic views). 

**Reading**: a Software Architecture Modeling product (model + views + C4 levels — the sibling pass's documented core) explicitly markets its **design-process layer** in "system design" vocabulary. The label does not separate modeling tools from the leaf; if anything the modeling pole claims the design process most loudly.

### Cloudcraft (Tier 1 — Datadog docs; marketing root 403)

**Self-positioning** (Datadog docs, "Cloudcraft (Standalone)"): "Cloudcraft is a **diagramming tool** for professionals that manage cloud-based infrastructure systems. Catering to Azure and AWS users, Cloudcraft provides aesthetic, **real-time 3D visualizations** of your cloud environments… enables the secure sharing of professional-quality cloud architecture diagrams". Datadog blog title (linked from docs): "Plan new architectures and track your cloud footprint with Cloudcraft by Datadog".

**Reading**: two postures in one product — design new architectures (proposed designs, with cost/budget framing per the blog title) and visualize live cloud footprint (real-time). Self-labels as **diagramming**, not "system design". Acquired by Datadog (standalone product docs retained).

### Hava (Tier 2 — product site)

**Self-positioning**: "Automated cloud diagrams in minutes… Explore, monitor, track changes in your cloud. **Ditch your drawing tools.**" Connect AWS/GCP/Azure (and Kubernetes) accounts; "within minutes you will have a set of logically laid out infrastructure diagrams grouped by VPCs or resource zones"; resource attributes (security groups, connections, subnets, IPs); cost forecasts; **diagram history** ("continuously polls your cloud config. When a change is detected, your diagrams are updated and the previous version is archived to version history"); alerts on architectural drift; export to Visio/PNG/CSV/JSON; embeddable viewer; CI/CD auto-generation via API/CLI; self-hosted option.

**Reading**: the **live-topology documentation** pole — diagrams are generated from and kept current with the real environment; there is no proposed-design authoring loop. Explicitly anti-drawing-tool positioning. Closest atlas neighbors: Diagramming Application's data-linked generation layer, and infrastructure monitoring/visibility.

### Brainboard (Tier 2 — product site)

**Self-positioning**: "The cloud is your canvas. Design, deploy and manage your cloud infrastructure from end-to-end." "Cloud Infrastructure Management Platform"; "AI driven platform to visually design and manage cloud infrastructure, collaboratively… the only solution that automatically generates IaC code for any cloud provider, with an embedded CI/CD."

**Structure**: multi-cloud collaborative designer (AWS/Azure/GCP/OCI/Scaleway) that "generates Terraform code instantly as you design"; Terraform/OpenTofu module registry as "central & single source of truth"; GitOps workflow; TF-state drift detection with scheduled scans; synchronized architectures across environments (dev/QA/staging/prod); visual CI/CD engine; templating; AI generation ("Just describe what you need, and Brainboard builds the infrastructure for you"); integrations (Infracost cost estimation, Checkov/Tfsec/Terrascan/OPA policy, Slack/Teams, webhooks); RBAC; versioning via Git.

**Reading**: the **design-to-deployment** pole — the design artifact is a cloud-resource architecture whose output is deployable code. Self-labels "cloud infrastructure management", not "system design". The design loop extends past documentation into provisioning — beyond this leaf's documentation boundary, into Infrastructure-as-Code territory.

### Multiplayer (Tier 1 — product site + docs) — MARKET DRIFT

**Current state**: "The debugging agent for developers. We connect your favorite coding agent to prod to fix application bugs automatically." Docs: quickstart (session recorder SDKs, debugging-agent TUI), web dashboard (agents/issues/recordings), MCP server, VS Code extension. **No system-design surface remains anywhere in the current product or documentation** — the web dashboard holds debugging sessions, issues, and recordings only.

**Historical note**: Multiplayer previously marketed itself as a "system design platform" (system designer with components/revisions/environments, session capture, mock APIs). That positioning is gone from all fetched surfaces. The loudest historical self-labeler of "system design platform" has left the category — strong evidence that "system design" is not a stable vendor category name.

## Cross-product Comparison

| Dimension | Eraser | IcePanel (SAM) | Cloudcraft | Hava | Brainboard | Multiplayer (legacy) |
|---|---|---|---|---|---|---|
| Self-label | "AI for diagrams"; claims "system design" activity | "diagramming and modelling tool for software architecture"; claims "system design" for its design process | "diagramming tool" for cloud infrastructure | "automated cloud diagrams" | "cloud infrastructure management platform" | (was) "system design platform" |
| Unit of record | file (diagrams + markdown docs) | governed model (elements + relationships) with views | diagram (design or live-linked) | auto-generated topology + version history | cloud-resource architecture + generated IaC | (was) system design with revisions/environments |
| Element identity across views | not documented (file/diagram granularity in API) | yes (model-level; delete-in-diagram ≠ delete-from-model) | no evidence | no (regenerated from live state) | partial (modules/templates reusable; IaC is the record) | (was) revisions |
| Design loop (propose → review → iterate) | yes (chat/canvas iteration, comments, version history, share) | yes (fork future state, feedback, merge, phases) | partial (plan new architectures) | no (documents what exists) | yes (design → code → deploy) | (was) yes |
| Design documentation layer | yes (markdown docs + figure embeds; RFC/PRD/ADR outlines) | yes (element descriptions, decisions) | no evidence | no | no (code is the record) | (was) partial |
| Source of truth | external (Git repos, cloud scans) used as generation inputs | the model itself (+ repo-link drift checks) | live cloud (real-time) | live cloud (continuous polling) | the design/IaC (+ drift detection vs cloud) | (was) the design + captured sessions |
| Output | diagrams + docs (export, publish, Git push) | views, docs sites, exports | diagrams (share/export) | diagrams (export/embed) | deployable Terraform + pipelines | (was) designs + mock APIs |
| Subject | software systems (broad: also flowcharts, wireframes, BPMN…) | software system structure | cloud infrastructure (AWS/Azure) | cloud infrastructure (AWS/Azure/GCP/K8s) | cloud infrastructure (multi-cloud) | (was) distributed software systems |

**Reading of the comparison**: the shared denominator across all label-claimants is thin — a maintained, editable **structural description of a system** (components/resources + relationships). Everything else that defines a product shape varies: where the description lives (governed model / design file / cloud resources / live topology), whether a design loop exists (propose-review-iterate) or a documentation loop (keep current with reality), whether a written design-document layer exists, and what the output is (views / docs / deployable code).

## Abstraction Levels

### L0 — Defining Invariant (of the activity space the leaf labels)

The smallest structure shared by everything the "system design" label is applied to:

```text
A maintained, editable structural description of a system
(what it consists of + how the pieces relate)
```

That is all. It is deliberately minimal because the research shows nothing else survives across the label's population:

- The **design loop** (propose → review → iterate) is absent in the live-topology pole (Hava documents what exists; it does not design).
- The **design-documentation layer** (written rationale beside the diagrams) is absent in the cloud poles (Brainboard, Cloudcraft, Hava).
- The **governed model-of-record** exists only in the modeling pole.
- The **software-system subject** is abandoned by the cloud poles (infrastructure resources, not software building blocks).

**Consequence**: this L0 does not distinguish the leaf from Diagramming Application (an architecture diagram is also "a maintained, editable structural description") or from Software Architecture Modeling (a model is a superset of it). **The leaf has no defining core of its own that its neighboring Types do not already own.** This is the central research finding — see Boundary Findings.

### L1 — Common Mature Structure (within the exploration-workspace shape)

For the shape closest to the leaf's own center (design workspaces, evidenced by Eraser at Tier 1; Multiplayer legacy corroborates the shape historically):

- diagrams + written design documents held together in one workspace (embeds of diagrams inside documents)
- fast authoring paths: canvas editing + diagram-as-code + AI generation from prompts/images/files
- generation grounded in team conventions (templates, rules, references, styles)
- sources-of-truth as generation inputs: Git repositories (codebase diagrams, CI-updated), cloud account scans
- collaboration/review machinery: comments, mentions, sharing, version history, folders
- export/publish surfaces (images, embeds, Git push, Confluence/Notion integration)
- agent access (MCP server; diagram CRUD from coding agents)

### L2 — Variant / Optional Structure

- **Authoring substrate**: canvas-first vs diagram-as-code-first vs AI-first (all three in one product in-sample)
- **Generation sources**: none / Git / cloud scans / uploaded files (Terraform, schemas, documents)
- **Cloud-source depth**: on-demand scan → generate (Eraser) vs continuous polling with version history and drift alerts (Hava) vs real-time (Cloudcraft)
- **Output depth**: diagrams + docs only (Eraser) vs deployable IaC + pipelines (Brainboard)
- **Subject breadth**: software systems only vs general diagram types (flowcharts, BPMN, wireframes) alongside
- **Deployment**: SaaS vs self-hosted (Hava, Brainboard options)
- **Diagram notation scope**: architecture-shaped vs full diagramming breadth

### L3 — Vendor-specific Structure (research notes only)

- Eraser: Eraserbot (CI codebase-diagram keeper), DiagramGPT free tool, designDocs.dev resource site, "Microsites" (interactive drill-down maps with C4 context/container/component zoom), usage-based AI-credit pricing, whiteboard-interview use case.
- IcePanel: The IcePanel Loop, viewer licenses for stakeholders, academy/e-book content (sibling pass holds detail).
- Cloudcraft: 3D isometric visualization style, AWS Marketplace distribution, "Cloudcraft in Datadog" integration mode.
- Hava: AWS Control Tower integration, Confluence embedding, "diagram history that audits itself" framing.
- Brainboard: one-click IaC migration, self-serve internal service catalog, cron-scheduled drift scans, design-embedded policy/security scanning (Checkov/Tfsec/Terrascan/OPA).
- Multiplayer: session recorder SDKs per stack, debugging-agent TUI, issue deduplication/scoring — all post-pivot, outside this leaf.

## Vendor-specific / Rejected Findings

- **"System design platform" as a category name** — REJECTED as a stable category. The one product that led with it (Multiplayer) has pivoted entirely away (Tier-1 evidence). No fetched product leads with "system design application/tool" as its category today.
- **"System design = architecture modeling"** — REJECTED as an alias equation. The label is claimed on both sides of the model-of-record seam (IcePanel's design-process marketing vs Eraser's workspace), and also by cloud tools that are neither. An alias resolution would be false.
- **"System design = AI diagramming"** — REJECTED. Eraser's canvas core is diagramming-grade (per-diagram masters, file/diagram granularity); AI generation is an era-current capability layer, not a defining structure (consistent with the diagramming pass's treatment of AI as optional).
- **"Cloud design tools are system design applications"** — REJECTED as an equation; HELD as adjacent label-sharers. They self-label cloud architecture/design/visualization; their subject is infrastructure resources; their strongest products extend into IaC deployment (Brainboard) or live-state documentation (Hava). Recorded as a cluster with no dedicated atlas leaf — flagged for taxonomy review.
- **Eraser "Microsites" drill-downs as model semantics** — NOT asserted. The docs describe interactive drill-down maps, but no element-identity/cross-view-sync machinery is documented; held as presentation-layer linking until evidence says otherwise.

## Boundary Findings

### vs Software Architecture Modeling (§12 sibling) — SAM pass's forward flag DISCHARGED from this side

The SAM pass proposed the seam "governed persistent model-of-record + views vs design-exploration surface" and could not resolve this leaf's population. **Confirmed from this side, with two refinements:**

1. **The seam is real and structural**: what separates the modeling pole from the exploration-workspace pole is the governed model-of-record — element identity independent of diagrams, cross-view sync, model-level operations. Eraser's documented structure (file → diagrams + docs; API at file/diagram granularity; no model machinery) sits on the exploration side; IcePanel/Structurizr/VP/Archi sit on the model side. The cross-view consistency test proposed by the SAM pass ("delete an element from one diagram — does it survive elsewhere?") cleanly separates them.
2. **The population on the exploration side is thin and drifting**: one active Tier-1-documented product (Eraser); the historical second product (Multiplayer) has pivoted out of the category entirely. The seam holds, but the leaf cannot be documented as a thriving independent Type on this population alone.
3. **The label cannot be the discriminator**: both poles claim "system design" language (IcePanel: "keep your system design moving forward"; Eraser: "companies with their system design"). The structure (model-of-record vs design artifacts), not the vocabulary, carries the boundary.

**Resolution recorded**: keep-both (SAM and this leaf) is defensible only if this leaf is documented as the label/activity-space node; if the taxonomy prefers population-clean Types, this leaf collapses into SAM + Diagramming Application with a disambiguation note. Recorded in STATUS.md Boundary Issues for taxonomy review — no directory change made unilaterally.

### vs Diagramming Application (03.05)

The exploration-workspace shape's canvas is diagramming-grade: per-diagram masters, shapes + connectors, broad diagram-type support (Eraser documents flowcharts, BPMN, ERD, sequence, wireframes — the diagramming pass's own territory). What scopes the workspace shape beyond generic diagramming is the **pairing and the loop**: structural diagrams of systems held together with design documentation, with review/iteration machinery aimed at the design activity. A diagramming tool used to draw one architecture diagram remains Diagramming Application (per that pass's own holding); a workspace organized around the system-design activity (docs + diagrams + review + generation from code/cloud) is what this leaf's remaining population looks like. The seam is center-of-gravity, not exclusive capability — consistent with how sibling passes treat bundled neighbors.

### vs Digital Whiteboard (03.05)

Freeform ideation surfaces lack the structural artifact discipline (notation vocabulary, connector semantics, persistent design documents). The diagramming pass already polices this boundary; nothing in this pass's evidence moves it.

### vs MBSE Platform (§16)

"System design" in the systems-engineering sense (requirements, behavior, parametrics, verification over multi-discipline engineered systems) is MBSE territory — discharged by the SAM pass's joint review. This leaf's subject, where it has one, is software/cloud systems, not engineered multi-discipline systems.

### vs API Design Platform / Database Schema Design Tool (§12)

Artifact-layer design tools (interface contracts; data layer) are downstream artifact design, not whole-system design. Eraser can *draw* ERDs and API diagrams (diagramming-grade), but does not manage schemas or contracts — no seam conflict.

### vs Infrastructure-as-Code Platform (§14)

Brainboard's design→Terraform→CI/CD loop crosses into IaC territory: the design artifact's output is deployable code and the drift detection runs against real infrastructure. Held as the cloud-design cluster's extension beyond this leaf; if the taxonomy ever gives the cloud-design cluster its own leaf, the IaC seam must be drawn there (design-first visual surface vs code/pipeline-centric platform).

### vs Application Portfolio Management (§14) / CMDB (§14)

Inventories of deployed applications/assets as lifecycle factsheets or operational records vs designed/intended structure. Hava's live topology is closest to the operational-record side (auto-generated from reality); still visualization-shaped, not portfolio-shaped. No seam conflict.

### vs observability Types (§14)

Multiplayer's pivot destination (session capture, debugging agent) is observability/debugging territory, not this leaf. The pivot itself is recorded as market drift, not as a boundary overlap.

### "去掉什么就变成另一个 Type" 判据 (removal tests)

- From the exploration-workspace shape, remove the **design-document pairing and the design loop** → a diagramming tool with architecture stencils (Diagramming Application).
- From the modeling pole, remove the **governed model-of-record** → the exploration workspace (this leaf's remaining population) — the SAM seam.
- From the cloud-design cluster, remove the **cloud-resource subject and IaC/live linkage** → generic diagramming; remove the **design/proposed-state authoring** → live topology documentation (Hava pole).
- From the whole label space, remove the **system subject** → whiteboard/generic drawing.

## Uncertainties

1. **Population depth of the exploration-workspace shape**: only one active product documented at Tier 1 (Eraser). Other possible members (e.g., generic doc tools with embedded diagramming, Notion/Confluence-class) were not sampled — the shape's true market depth is unknown. Assertions about the shape are calibrated to "the researched sample suggests".
2. **Lucidscale unreachable** (403 ×2) — the Lucid-family cloud-visualization pole is undocumented here; the cloud-design cluster's breadth is inferred from Hava + Cloudcraft + Brainboard only.
3. **Cloudcraft's design-mode mechanics** (blueprint authoring, cost estimation flow) rest on the Datadog docs overview + blog title; the marketing root was 403 and the getting-started page was not fetched. No precise Cloudcraft operational claims are made.
4. **Hava and Brainboard** evidenced at product-page strength (Tier 2); their docs were linked but not fetched. Feature claims are held at "documented feature exists" strength; no numeric limits, sync intervals (beyond Hava's own "syncs daily, or in real-time via API" marketing phrasing), or plan-gating details asserted.
5. **Multiplayer's legacy system-design product** is evidenced only by its absence in current surfaces plus the pivot framing on the current site; the legacy feature set is described from the pivot-era positioning visible in the current site's framing and is not asserted in detail.
6. **Eraser "Microsites"** internals (whether drill-downs imply any element linkage beyond presentation) undocumented — held as presentation-layer.
7. Whether a **dedicated cloud-infrastructure design/visualization leaf** should exist in the directory is a taxonomy question, not resolvable by this pass alone — flagged, not decided.

## Historical / Market-Sample Check

Would older, regional, platform-native, or differently positioned products still fit a "system design application" definition — and is the leaf's population an era artifact?

- **Older practice (pre-dedicated-tooling)**: system design was served by *generic* tools — whiteboards, Visio-class diagramming for the structure, Word/wiki documents for the rationale, design reviews in person. No dedicated product population existed; the activity predates every candidate product. This **confirms** the label-node finding: there was never a distinct "system design application" category to which older products belong.
- **The UML-suite generation** (Rational Rose lineage): marketed for designing systems, but it is the modeling pole's own lineage — claimed by Software Architecture Modeling (the sibling pass documents suite products' import compatibility with that generation). Fits the *activity*, belongs to the *modeling shape*.
- **The "system design platform" generation** (Multiplayer-era, ~2023–2024): the one moment a vendor-led category name existed; it did not hold — the leading product pivoted to debugging (Tier-1 evidence of the pivot). A definition built on that generation would already be stale.
- **Regional/platform-native check**: nothing in the evidence suggests regional variants of a system-design tool population; the cloud-design cluster is global and provider-driven.

Conclusion: the historical check does not rescue a distinct Type — it strengthens the label-node resolution. The activity is long-lived; the dedicated-product population is thin, recent, and unstable.

## Final Synthesis

**"System Design Application" is a practitioner label, not a vendor category.** It names the activity — designing the structure of a software system and communicating that design to the people who build, review, and operate it — and the market serves that activity through three product shapes with different centers of gravity:

1. **Governed model-of-record modeling** (IcePanel, Structurizr, Visual Paradigm, Archi) — the design as a living model with views; owns the "keep the design current as the system evolves" job. Already documented as **Software Architecture Modeling**; that pass's proposed seam (model-of-record vs design-exploration surface) is **confirmed from this side**.
2. **Design-exploration workspaces** (Eraser active; Multiplayer legacy, pivoted away) — the design as diagrams + written design documents in one workspace, with fast authoring (canvas / diagram-as-code / AI), review machinery, and code/cloud sources used as generation inputs. This is the leaf's own remaining population — real but thin (one active Tier-1-documented product).
3. **Cloud-infrastructure design & topology** (Brainboard, Cloudcraft, Hava, Lucidscale) — the design target is cloud infrastructure; spans design-first-with-deployable-output (Brainboard), design+live visualization (Cloudcraft), and automated live-topology documentation (Hava). Self-labels cloud architecture/design/visualization; has no dedicated atlas leaf — flagged for taxonomy review.

The leaf is therefore documented as the **system-design activity space**: the shared content basis (a maintained structural description of a system, worked through a design loop and communicated outward), the three realizations, and the seams to the Types that own each population. The taxonomy question (umbrella node vs collapse into SAM + Diagramming vs new cloud-design leaf) is recorded in STATUS.md Boundary Issues for review — no directory change made.
