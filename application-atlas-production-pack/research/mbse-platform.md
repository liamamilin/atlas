# Research Notes — MBSE Platform

Research date: 2026-09-09

## Research Goal

Understand what an MBSE (Model-Based Systems Engineering) Platform really is, from real products: what objects exist inside it, what users do with them, how engineering work flows through the model, which states/rules matter, and where the Type's boundaries lie against neighboring Types (diagramming applications, engineering requirements management, system simulation platforms, software architecture modeling, PLM, CAE, digital twin platforms).

## Initial Boundary

Working hypothesis before research:

- An MBSE Platform is the tooling for model-based systems engineering: instead of document-centric systems engineering (Word/Excel specifications + hand-drawn diagrams), the system under development is captured as a structured, formal model that serves as the central engineering artifact.
- Nearest neighbors likely confused with it: Diagramming Application (Visio-class drawing tools), Engineering Requirements Management (requirement records as the system of record), System Simulation Platform (Simulink/Modelica-class behavioral/physical simulation), Software Architecture Modeling (§12), PLM (product data estate), CAE (physics simulation), Digital Twin Platform (operational replica).
- Open questions: is the "platform" aspect (repository, collaboration, integration) definitional, or is the model-centric core enough? Is SysML definitional? Is simulation definitional? Is requirements-in-model definitional?

## Research Questions

1. What is the central artifact — what does "the model" consist of, and where does it live?
2. What is the relationship between diagrams and the model? (This is the suspected seam vs diagramming applications.)
3. What role does the modeling language play (SysML / UML / Arcadia DSL / proprietary languages)? Is a specific language definitional?
4. What do users actually do day-to-day: create elements, draw diagrams, run analyses, generate documents, link requirements?
5. How do requirements, verification, and traceability relate to the model?
6. What does simulation/execution mean in this context, and is it definitional?
7. How do multi-user collaboration, versioning, and governance work on a model?
8. How does the tool connect to the wider engineering toolchain (requirements tools, simulation tools, PLM, code generation)?
9. What is the methodology layer (Arcadia, HarmonyMBE, STRATA) and is it definitional?
10. Boundary: vs diagramming, vs requirements management, vs simulation platforms, vs software architecture modeling, vs PLM.

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

1. **IBM Engineering Rhapsody** (heritage enterprise pole; UML/SysML modeling + simulation + code generation; part of IBM Engineering Lifecycle Management) — evidence: Tier 2 product page only (IBM docs site returned 403).
2. **CATIA Magic / No Magic (MagicDraw / Cameo Systems Modeler / Magic Systems of Systems Architect)** (dominant SysML modeling tool pole, now Dassault Systèmes) — evidence: Tier 1 public documentation (docs.nomagic.com).
3. **Eclipse Capella** (open-source, methodology-driven pole; implements Thales's Arcadia method) — evidence: Tier 1 features/add-ons pages + Tier 2 product/method pages.
4. **GENESYS (Vitech, now Zuken)** (pure-play MBSE platform pole; own language CSDL + own methodology STRATA) — evidence: Tier 1 public help site (genesys-help.vitechcorp.com).
5. **Gaphor** (open-source minimal pole; lightweight UML/SysML modeling application) — evidence: Tier 2 homepage; used mainly for the minimal-feature / historical check.

Market context recorded during research: Vitech has been absorbed into Zuken (vitechcorp.com now redirects; "GENESYS continues as Zuken's Model-Based Systems Engineering platform"). Dassault acquired No Magic (MagicDraw/Cameo → CATIA Magic). IBM renamed Rational Rhapsody → IBM Engineering (Systems Design) Rhapsody and added a cloud-native SysML v2 product (Rhapsody Systems Engineering). The market consolidates around a handful of modeling-tool families plus an ecosystem of connectors.

## Sources

Fetched 2026-09-09:

- No Magic / CATIA Magic documentation home — https://docs.nomagic.com/ (Tier 1)
- No Magic Modeling Tools documentation — https://docs.nomagic.com/MT/ (Tier 1)
- No Magic SysML v1 modeling — https://docs.nomagic.com/MT/latest/magic-systems-of-systems-architect---cameo-enterprise-architecture/sysml-v1-modeling-303989657.html (Tier 1)
- Magic Collaboration Studio / Teamwork Cloud — https://docs.nomagic.com/MCS/ (Tier 1)
- GENESYS Help home — https://genesys-help.vitechcorp.com/genesys-help (Tier 1)
- GENESYS "Three Pillars of MBSE: An Overview" — https://genesys-help.vitechcorp.com/genesys-help/three-pillars-of-mbse-an-overview (Tier 1)
- Eclipse Capella home — https://www.eclipse.org/capella/ (Tier 2)
- Eclipse Capella Features — https://www.eclipse.org/capella/features.html (Tier 1/2)
- Eclipse Capella Arcadia — https://www.eclipse.org/capella/arcadia.html (Tier 2)
- Eclipse Capella Add-Ons — https://www.eclipse.org/capella/addons.html (Tier 1/2)
- IBM Engineering Rhapsody product page — https://www.ibm.com/products/systems-design-rhapsody (Tier 2)
- Gaphor home — https://gaphor.org/ (Tier 2)

Unreachable / limitations:

- IBM product documentation (ibm.com/docs/en/rhapsody) — 403. Rhapsody evidence is product-page strength only; no precise Rhapsody operational claims asserted.
- Sparx Systems (sparxsystems.com user guide and product page) — 403 twice. The independent mid-market modeling-tool pole is under-sampled; Gaphor partially covers the independent/lightweight pole.
- Vitech/Zuken GENESYS product marketing pages reachable but marketing-grade; the help site was used as the primary GENESYS source.

## Product Observations

### IBM Engineering Rhapsody (evidence layer A, Tier 2 product page only)

- Positioned as "Design, visualize, and manage complex systems and software"; "a proven solution for modeling and systems design activities".
- "Continuous validation through rapid simulation, prototyping and execution."
- "A rigorous SysML and HarmonyMBE–based systems engineering environment that connects stakeholder needs to architecture, behavior, and implementation"; "rich UML support" for software teams in "a single, consistent model".
- Product editions: Rhapsody Developer (embedded/real-time software engineering, "full application generation of production-ready code for C, C++, Java, and Ada", "animated statecharts and live debugging"), Rhapsody Designer (systems engineers + "prototype, simulate and execute designs"), Rhapsody Systems Engineering ("cloud native, web based solution built on SysML V2").
- Traceability: "end-to-end traceability by linking requirements, architecture, implementation, and verification"; "suspect link tracking"; "automated documentation"; "deep integration across the IBM Engineering Lifecycle Management products".
- Industry packages: AUTOSAR, UAF/DoDAF, FMI/FMU co-simulation; safety kits aligned to ISO 26262, DO-178C, IEC 61508.
- AI: "MBSE use case discovery" — identifies use cases/actors in natural-language requirements and creates corresponding model elements and use-case diagrams with traceability links.
- Note: docs site 403 — no precise operational details (menu-level behavior, exact simulation semantics) asserted anywhere.

### CATIA Magic / No Magic — MagicDraw / Cameo (evidence layer A, Tier 1)

Documentation portfolio structure (docs.nomagic.com) reveals the product family's shape:

- **Modeling tools** (Magic Systems of Systems Architect / Cameo Enterprise Architecture, Magic Cyber Systems Engineer / Cameo Systems Modeler, Magic Software Architect / MagicDraw): SysML v1 modeling, UAF 1.3 modeling, BPMN modeling, data-related modeling, general modeling features.
- SysML v1 modeling guide sections: creating projects; organizing your model; **requirements management**; item flow management; **modeling structure with Blocks**; **behavior-to-structure synchronization**; contextual relationships; **modeling parametric constraints**; functional analysis; **views and viewpoints**; **generating report documents**; working with model elements; **SysML v1 validation**; diagram descriptions; elements; style; **importing/exporting to external simulation models**.
- SysML v1 diagrams: Block Definition, Internal Block, Package, Parametric, Requirements, Activity, Use Case.
- **Server-side collaboration** (Magic Collaboration Studio / Teamwork Cloud): "a compound product for collaborative model development and storage... model governance (merging, branching, access control), analysis, and integration with third-party tools"; Teamwork Cloud = "a model repository that enables parallel modeling, model storage, and version control with strict yet flexible access control"; Teamwork Cloud Admin = web admin for users, projects, RBAC, LDAP; Cameo Collaborator = web-based model presentation for stakeholders with commenting and web editing.
- **Simulation** (Magic Model Analyst / Cameo Simulation Toolkit) as a separate documentation product; **SysML v2** plugin + evaluation + simulation plugins; MagicLab (view SysML v2 models in a browser).
- **Cameo DataHub**: "modeling tool integrations with third-party applications".
- Other plugins: safety/reliability analyzer (ISO 26262), systems cybersecurity designer, product line engineering/variability, UPDM 2, UML profiling and DSL engine ("customizing domain-specific profiles"), validation rules reference.
- Language-element reference: "SysML v1/UAF/UML Model Element Descriptions" — the tool's world is the language's element vocabulary.

### Eclipse Capella (evidence layer A/B, Tier 1 features + Tier 2 pages)

- Self-description: "a powerful and extensible MBSE software tool that leverages a field-proven language and method to successfully design the architecture of complex systems"; "the modeling tool implementing the Arcadia methodology"; "industrial-grade MBSE Workbench".
- Diagram kinds (features page): Operational Architecture, Capabilities, Dataflows, Architecture ("allocation of Functions onto Components"), Trees (function/component breakdowns), Sequence (functional/exchange/interface scenarios), Modes & States ("UML-inspired state machines"), Classes & Interfaces (bit-precise data structures).
- **Diagram synchronization**: "Synchronization/unsynchronization of diagrams: gives a fine level of control on the elements which are systematically displayed or not" — diagrams are renderings of model elements with controlled sync; "Automated contextual diagrams: content is automatically updated according to preselected elements and predefined semantic rules"; filters and layers.
- **Model validation**: "Capella organizes model validation rules in several categories: Integrity, design, completeness, traceability... Architects can define validation profiles... quick fixes provide quick and automated solutions."
- **Semantic browser**: "instantaneously provides the context of model elements through meaningful queries... the preferred way to navigate in models and diagrams and to quickly analyse the relationships between model elements."
- **Computed links**: "Capella automatically computes graphical simplifications. The information exchanges between lower-level functions are automatically displayed on higher-level functions" — abstraction-level consistency maintained by the tool.
- **Semantic delete with preview**: "instant impact analysis of deletions."
- **Reuse**: Replicable Elements (REC/RPL) — "definition of an element / set of elements which can be reused in multiple contexts / configurations / models"; libraries shared between projects.
- **System/Subsystem transition**: "the contract and model of the subsystems are computed from the system" — multi-level engineering.
- **Multi-viewpoint**: demonstration viewpoints (Mass, Cost, Latency); Kitalpha API for viewpoint development; trade-off comparison views.
- **HTML output**: "Publishing and sharing HTML versions of models helps make models THE reference of all engineering activities."
- **Methodological guidance**: activity browser provides "methodological access to all key activities" — the method is embedded in the tool.
- Arcadia method page: Arcadia is "a tooled method devoted to systems & architecture engineering"; phases Operational Analysis → System Need Analysis → Logical Architecture → Physical Architecture → EPBS (component contracts); "A domain-specific language (DSL) was preferred in order to ease appropriation by all stakeholders, usually not familiar with general-purpose, generic languages such as UML or SysML"; viewpoint-driven per ISO/IEC 42010; "A Capella model is built for each Arcadia engineering phase. All of these models are articulated through model transformation, and related by justification links; they are processed as a whole for impact analysis"; recursive application at each level of system breakdown; iterative lifecycles (top-down, bottom-up, middle-out).
- Add-ons ecosystem (evidence of the integration surface): Requirements Viewpoint (ReqIF import + link model elements to requirements); Team for Capella (shared server, automatic locking, change propagation); M2Doc (Word generation from models) and XHTML docgen; Simulink connector (export functional chains); Ansys ModelCenter connector (analysis/trade studies); SCADE Architect importer; SysML Bridge (Capella ↔ SysML transformation); TASTE plugin (export to AADL/ASN.1 toolchain, executable code for embedded targets); Atica4Capella (safety analysis FHA/FMEA from system models); DARC (cybersecurity assets/threats viewpoint); PVMT (custom properties); pure::variants connector (product-line variability); MapleMBSE (Excel-based editing interface to the model); Obeo Publication (publish models, connect to Polarion/DOORS Next/Jama Connect/Codebeamer/Jira/Confluence, OSLC); System Modeling Workbench for Teamcenter (Siemens PLM integration); Obeo Cloud (hosted collaboration); Obeo AI (LLM/agents via MCP and APIs); Python4Capella (scripting).

### GENESYS / Vitech → Zuken (evidence layer A, Tier 1 help site)

- Help-site self-description: "GENESYS is the premier tool supporting model-based systems engineering (MBSE) and product design that includes capabilities to model in six c[ore languages...]" (truncated in fetch).
- **Three Pillars of MBSE** (help article citing Delligatti, *SysML Distilled*):
  - **Language**: "a (semi)-formal language that defines the kinds of elements you're allowed to put into a model, the allowed relationships between them, and the set of notations you can use to display the elements and relationships on diagrams. The language defines the grammar: a set of rules that determines whether a given model is well formed."
  - **Methodology**: "A documented set of design tasks and organizational structure that ensures that everyone on the team is building the system model consistently and working towards a common end point."
  - **Tool**: "A software package that incorporates one or more modeling languages into a **structured, relational database of entities and relationships** and supports the generation of diagrams and other visualizations of the data to the user. **It is not simply a drawing tool – the entities and relationships on a diagram are part of an underlying model.** The tools may also support simulations, provide consistency and integrity checking, and provide various ways of ingesting and egesting data."
  - Vitech's pillar solutions: Language = CSDL (Comprehensive Systems Design Language; also supports SysML v1.6, UAF, DoDAF); Tool = GENESYS; Methodology = STRATA. "CSDL forms a critical foundation for GENESYS. The language concepts, parsed into the SE pillars defined in STRATA and combined with completeness and integrity checkers, provides a holistic capability for developing comprehensive system architectures."
- **Project Explorer**: containment tab, classes tab, packages, property sheet, model assistant, related projects, cross-project relationships.
- **Schema**: the tool's data model is itself an editable artifact — Schema Classes / Facilities / Relations; commands: New Class, New Attribute, New Relation, Check Schema Consistency, Migrate Schema, Enable/Disable Versioning. (Vendor-specific depth: user-extensible schema.)
- **Views**: "Entity-Centric Views" — a large diagram family generated from model entities: N2, Interface N2, Interface Block, IDEF0, FFBD/EFFBD, Activity, Flow IBD, Parametric, Package, State Transition, Use Case, Spider, Physical Block, Sequence, BDD, Constraint BDD, Requirements, Physical N2, Class, Hierarchy; plus "Independent Views": View Lists, **Table Views**, **Matrix Views** (non-graphical renderings of the same data).
- **Diagram framework**: multiple views of a diagram, presentation layer ("Delivering Substance with Style"), rule sets applied to diagrams, elision, behavior constructs.
- **Model checking**: "Auto-Checking with Model Diagnostics", Entity Completeness Checks, Entity Design Integrity Checks (per-schema-version variants).
- **Simulator**: "Virtual Prototyping and Design Validation with the Simulator" — run/step/stop, timeline, transcripts, random streams/distributions, animation.
- **Connectors**: DOORS (import/export), Excel, ModelCenter, PowerPoint, Simulink Exporter, Constraint Solver; OSLC admin; REST API; "GENESYS Adapter for SBE Digital Thread"; Document Parser (project startup from documents, human-in-the-loop).
- **Repository governance**: connect to repository; entity lock/unlock; entity/attribute/parameter permissions; versioning; baselines; audit logs; sessions administration; users/groups/security.
- **Reports/scripts/viewpoints**: report definitions, scripts, customized viewpoints of the data model, RDF generation, masks, filters, sort blocks.

### Gaphor (evidence layer A, Tier 2 homepage — minimal pole)

- "Gaphor is a UML, SysML, RAAML, and C4 modeling application... Gaphor implements a fully-compliant UML 2 data model, so **it is much more than a picture drawing tool**."
- "UML is a graphical modeling language, so all information you put in the model is visible in the diagrams... No hidden panels and property pages. Just diagrams!"
- Tree view of all model elements; extensible via plugins ("Plug-in a code generator or export your diagrams for documentation"); standards-compliant (UML, SysML, RAAML OMG standards; C4).
- No server repository, no simulation, no validation suite, no methodology layer advertised — yet it is unambiguously a modeling application. This anchors the minimal pole: model-backed + diagram-views + language compliance is enough to be in-Type; everything else is common/optional.

## Cross-product Comparison

| Dimension | Rhapsody | CATIA Magic / Cameo | Capella | GENESYS | Gaphor |
|---|---|---|---|---|---|
| Central artifact | system/software model (UML/SysML) | model (SysML/UAF/UML/BPMN) | model per Arcadia phase (Arcadia DSL) | model in relational DB of entities/relations (CSDL; SysML/UAF/DoDAF supported) | model (UML 2 data model; SysML/RAAML/C4) |
| Diagrams vs model | diagrams render the model; animated statecharts | diagrams + behavior-to-structure synchronization | diagrams synchronized to model; automated contextual diagrams; computed links | "not simply a drawing tool"; entity-centric views generated from entities | "much more than a picture drawing tool"; model visible in diagrams |
| Language governance | SysML/UML compliance; profiles (AUTOSAR, UAF) | language specs + validation rules; DSL engine | Arcadia language; validation rules with quick fixes | language grammar (well-formedness); schema consistency checks | OMG standards compliance |
| Model validation | (not confirmed — docs unreachable) | SysML v1 validation rules | validation rule categories + profiles | Model Diagnostics, completeness + design-integrity checks | — |
| Requirements | links to requirements; AI use-case discovery from NL requirements | requirements management in-model | Requirements Viewpoint (ReqIF) / Basic Requirements viewpoint | requirements as entity class; DOORS connector; derived requirements; verification entities | Requirements diagrams (SysML) |
| Simulation/execution | rapid simulation, prototyping, execution; FMI/FMU co-sim | Cameo Simulation Toolkit; SysML v2 evaluation/simulation; external sim import/export | core tool: no built-in sim; add-ons (DESS, ModelCenter, Simulink export) | Simulator (virtual prototyping, timeline, transcripts) | — |
| Collaboration | shared models, governed reviews (ELM integration) | Teamwork Cloud repository: parallel modeling, version control, merging/branching, RBAC | Team for Capella add-on (shared server, locking); Obeo Cloud | repository with lock/unlock, permissions, versioning, baselines, audit | — |
| Non-graphical views | — | — | semantic browser (query-based context) | table views, matrix views, view lists, property sheets | tree view |
| Document generation | automated documentation | generating report documents | M2Doc (Word), XHTML docgen, HTML publication | reports, PowerPoint export | diagram export |
| Integration | IBM ELM; DOORS-class requirements; code gen C/C++/Java/Ada | DataHub; Cameo Collaborator; SysML v2; safety/cyber plugins | ReqIF, Simulink, ModelCenter, SCADE, TASTE, Polarion/DOORS Next/Jama/Jira, Teamcenter, pure::variants | DOORS, Excel, ModelCenter, Simulink, PowerPoint, OSLC, REST, digital-thread adapter | code-generator plugins, export |
| Methodology | HarmonyMBE | (method-agnostic; profiles) | Arcadia embedded (activity browser) | STRATA embedded | — |
| Deployment | desktop + cloud-native web (Rhapsody SE) | desktop client + server (Teamwork Cloud) + web reviewer | desktop workbench (+ hosted cloud option) | client + repository server + admin tools | desktop app |
| Customer tier | large enterprise / regulated | large enterprise + mid | open-source + industrial (aerospace/energy/transport) | pure-play MBSE programs (defense/aerospace) | individual / small teams |

Reading of the comparison:

- The **model as the central structured artifact** and **diagrams as views over it** are present in all five products, stated in near-identical terms by the vendors themselves ("not simply a drawing tool", "much more than a picture drawing tool", "behavior-to-structure synchronization", "diagrams synchronized to model"). This is the strongest cross-product signal (evidence layer B).
- **Language governance** (typed elements, allowed relationships, well-formedness) is present in all five; rich validation suites are present in four of five (Gaphor lacks one) — common-mature, not definitional.
- **Requirements handling** varies: in-model requirement elements (GENESYS, Cameo, Gaphor/SysML), add-on viewpoints (Capella), or external-tool linkage (Rhapsody→ELM/DOORS, GENESYS→DOORS). Requirements-in-model is NOT definitional; requirements traceability to the model is the common mature pattern.
- **Simulation/execution** varies from absent (Gaphor, Capella core) to first-class (GENESYS Simulator, Cameo Simulation Toolkit, Rhapsody). NOT definitional.
- **Multi-user repository** varies from absent (Gaphor, Capella core without add-on) to product-defining suite components (Teamwork Cloud, GENESYS repository, Rhapsody Model Manager). NOT definitional — but very common in mature deployments.
- **Methodology coupling** varies: embedded method (Arcadia in Capella, STRATA in GENESYS, HarmonyMBE in Rhapsody) vs method-agnostic tool (MagicDraw core, Gaphor). NOT definitional.
- **Language substrate** varies: SysML v1, SysML v2, UML, Arcadia DSL, CSDL, custom profiles. No single language is definitional; "a defined modeling language with formal semantics" is.

## Canonical Model

### L0 — Defining Invariant (minimal)

An MBSE Platform is recognizable as such when it holds, jointly:

1. **The system model as the unit of record** — a persistent, structured model of the engineered system under development, composed of typed model elements (structural components/blocks, functions/activities, ports and connections, states, requirements, constraints/parameters) held in a defined modeling language with formal semantics. Model elements exist independent of any diagram.
2. **Diagrams as views over the model** — diagrams are generated renderings of the underlying elements, not freehand drawings; the model is the single source of truth; the same elements can be rendered in multiple diagram types and in non-graphical views (trees, tables, matrices, queries).
3. **Language-governed editing** — users create, connect, and modify typed elements; the tool enforces the language's grammar (allowed element kinds and relationships, well-formedness) rather than accepting arbitrary shapes.
4. **Systems-engineering subject** — the modeled subject is the engineered system (spanning requirements, structure, behavior, and commonly parametrics/verification concerns) rather than software alone; the model serves as the working basis for the system's engineering definition.

Jointly-held is load-bearing:

- 1 alone = an element database with no engineering surface.
- 2 without 1 = a diagramming application (shapes on pages).
- 3 without 1+2 = a language specification/validator, not a tool.
- 4 without 1–3 = document-centric systems engineering (the pre-MBSE state this Type replaced).
- 1+2 without 3 = drawing tool with shape semantics (diagramming pole).
- 1+2+3 without 4 = a general UML/software modeling tool (Software Architecture Modeling territory).

### L1 — Common Mature Structure

- Requirements in the model or linked to it, with traceability links (satisfy/derive/verify) between requirements and model elements; coverage/suspect-link machinery.
- Model validation suites (integrity, completeness, traceability rule categories, with quick fixes / diagnostics).
- Multi-user model repository: server-side storage, parallel editing with locking/merging/branching, version control, access control, audit.
- Behavioral execution/simulation of model fragments (state machines, activities, parametric evaluation) and co-simulation/export bridges to dedicated simulation tools.
- Document/report generation from the model (Word/HTML publication) — "make the model the reference of all engineering activities".
- Model navigation and query surfaces (semantic browsers, search, matrices, tables).
- Reuse machinery (libraries, replicable elements, model segments, reference architectures).
- Toolchain integration: requirements tools (DOORS/DOORS Next/Jama/Polarion), simulation tools (Simulink, ModelCenter), PLM (Teamcenter), ALM, office tools; OSLC/REST APIs.
- Embedded methodological guidance (activity browsers, wizards) for the coupled or recommended method.
- Viewpoint/profile machinery (UAF/UPDM, custom profiles, DSL engines, viewpoint APIs).

### L2 — Variant / Optional Structure

- Language substrate: SysML v1 vs SysML v2 vs UML vs domain-specific language (Arcadia) vs proprietary language (CSDL) vs custom profiles.
- Methodology posture: methodology-agnostic tool vs embedded proprietary method (Arcadia, STRATA, HarmonyMBE).
- Deployment: single-user desktop workbench ↔ client-server repository ↔ cloud-native web (and web-based stakeholder reviewers).
- Industry/regulatory packages: AUTOSAR, UAF/DoDAF/UPDM, safety kits (ISO 26262, DO-178C, IEC 61508), cybersecurity viewpoints, ecodesign/LCA viewpoints.
- Code generation depth: none → export bridges → full production code generation (C/C++/Java/Ada).
- Specialty analysis add-ons: safety (FHA/FMEA), reliability, cybersecurity, trade studies/optimization, product-line variability.
- AI assistance (use-case discovery from natural-language requirements; LLM/agent access to models).
- Stakeholder publication surfaces (web reviewers with commenting, HTML publication servers).

### L3 — Vendor-specific Structure (research notes only)

- GENESYS: user-editable schema (Classes/Facilities/Relations), CSDL language, STRATA methodology, Sidekick review client, model obfuscator, PUID wizard.
- CATIA Magic / No Magic: Cameo product-family naming, MagicLab browser viewer, DataHub integration engine, Teamwork Cloud on Cassandra, Magic Concept Modeller, Virtual Twin of the Organization plugin.
- IBM: HarmonyMBE method, Engineering Lifecycle Management suite integration, Rhapsody SE cloud-native SysML v2 product, TÜV-certified safety kits.
- Capella: REC/RPL replicable elements, Kitalpha viewpoint API, Capella Studio, semantic browser specifics, Obeo commercial ecosystem.
- Zuken: E3.GENESYS connector (model-based wire-harness design), ITAR-compliant support posture.

## Vendor-specific Findings

- The GENESYS "Three Pillars" framing (Language/Methodology/Tool) is a vendor-adopted pedagogy (from Delligatti's *SysML Distilled*), but its tool definition — "structured, relational database of entities and relationships... not simply a drawing tool" — matches what every other sampled vendor independently builds. Treated as strong corroborating evidence for L0, not as vendor-specific structure.
- GENESYS's editable schema is the deepest exposure of the "model as database" idea; other products expose the language as fixed (SysML/UML) with profile/DSL extension instead. Two realization strategies of the same concept.
- Capella's computed links and semantic browser are the most developed "complexity management" surfaces; GENESYS reaches similar ends via elision, filters, and matrix views.
- Rhapsody is the only sampled product advertising full production code generation as a core edition capability (embedded/real-time pole).

## Boundary Findings

1. **vs Diagramming Application** (§03.05, processed 2026-09-07). Diagramming: page-oriented diagram document; shapes as discrete semantic objects from notation stencils; the diagram IS the artifact. MBSE: typed model elements with formal semantics; diagrams are generated views; the model is the artifact. The vendors' own language draws this line ("not simply a drawing tool", "much more than a picture drawing tool"). Remove the model → diagramming application. Seam held from this side; consistent with the diagramming pass's "shapes as discrete semantic objects" core.
2. **vs Engineering Requirements Management** (§16, processed 2026-09-08 — DISCHARGES that pass's "model-first vs record-first" flag from this side). ERM: the requirement record (textual statement + attributes + traceability + baselines) is the system of record; models are integration targets. MBSE: the system model is the system of record; requirements are one element class inside the model (or external records linked to model elements). Complementary Types; the seam is the center of gravity of the record world. Confirmed by both sides' integration evidence (ERM tools integrate with modeling tools; MBSE tools integrate with DOORS-class tools).
3. **vs System Simulation Platform** (§16, unprocessed — FLAG for joint review). Simulation platforms (Simulink/Modelica-class) model behavioral/physical dynamics of a design for analysis; MBSE platforms model the system's architecture (requirements/structure/behavior/interfaces) as the engineering definition of record. MBSE tools execute model fragments for validation and export to simulation tools (Simulink exporters, FMI/FMU, ModelCenter bridges) — the export bridge is the seam made visible. Proposed seam: architecture-of-record vs dynamics-analysis-of-design.
4. **vs Software Architecture Modeling** (§12, unprocessed — FLAG). Same modeling technology (UML-class languages, model-backed diagrams), different subject: software structure vs the engineered multi-discipline system. The sampled MBSE products all carry software-modeling capability too (Rhapsody Developer is explicitly a software pole) — the Type boundary is the center of gravity, not exclusive capability. Flag for joint review when that leaf is processed.
5. **vs PLM** (§16, unprocessed — FLAG, consistent with medical-device-lifecycle-management pass's pre-hung seam). PLM: the product data estate (CAD/PDM/BOM/change/documents). MBSE: the system model. Integration exists (System Modeling Workbench for Teamcenter; Obeo Publication) but the record worlds differ. Flag for joint review when the PLM leaf is processed.
6. **vs CAE / Engineering Simulation** (§16, processed 2026-09-06). That pass already holds the seam: "CAE computes physical responses; MBSE manages system models, requirements, and architecture." Consistent from this side.
7. **vs Digital Twin Platform** (§16, processed 2026-09-07). Twin: persistent digital object standing for a specific physical counterpart in operation. MBSE: development-time model of a system being designed. Some vendors use "virtual twin" vocabulary (No Magic plugin naming) — packaging vocabulary, not the same record world.
8. **Leaf-name observation**: the market says "MBSE tool", "MBSE platform", "modeling tool", "MBSE workbench" interchangeably; "platform" in vendor usage correlates with the repository/collaboration/integration layer being first-class (GENESYS, Rhapsody+ELM, Magic+Teamwork Cloud), but single-user workbenches (Capella core, Gaphor) are unambiguously in-Type. The defining core is model-centric systems engineering; the platform layer is common-mature. No directory change recommended; leaf stands.

## Uncertainties

- IBM Rhapsody evidence is Tier 2 only (docs 403). No precise Rhapsody operational claims asserted; its L0 fit is inferred from the product page's own descriptions (model, simulation, traceability, SysML/UML) — high confidence but not Tier 1.
- Sparx Enterprise Architect unreachable (403 ×2) — the large independent mid-market user base is under-sampled; Gaphor partially covers the independent/lightweight pole but is not a full substitute.
- Exact simulation semantics per product (what exactly executes, with what fidelity) not researched; simulation treated only as presence/absence + role.
- SysML v2 tooling is early (plugin-generation at No Magic, cloud-native at IBM); the L0 was checked to be language-version-agnostic, but v2-era workflow shifts (textual notation, client-server APIs) are not yet fully observable from the sampled documentation.
- Market-share/adoption figures not researched (not needed for the Type definition).

## Final Synthesis

An MBSE Platform is the engineering system of record for the **system model**: a persistent, structured, language-governed model of the engineered system under development, from which all diagrams and views are generated and on which systems-engineering work — requirements linkage, architecture definition, behavioral analysis, verification planning, downstream artifact generation — is performed directly. The defining core is deliberately small: model-as-record, diagrams-as-views, language-governed editing, systems-engineering subject. Everything the market associates with mature MBSE — repositories and governance, simulation, document generation, requirements traceability, toolchain integration, embedded methodology, industry packages — is common mature structure or variant structure, not definition. The Type's historical anchor is the replacement of document-centric systems engineering; its boundary anchors are the diagramming tool (no model), the requirements tool (record-first), the simulation platform (dynamics-analysis), and the software modeling tool (software subject).
