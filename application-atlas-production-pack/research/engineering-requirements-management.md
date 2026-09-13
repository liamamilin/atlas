# Research Notes — Engineering Requirements Management

## Research Goal

Understand what an Engineering Requirements Management application really is, from real products: what objects exist inside it, what users do with them, how requirements work flows, which states/rules matter, and where the Type's boundaries lie against neighboring Types (MBSE, PLM, issue trackers, test management, product management, and the §12 sibling leaf "Requirements Management Platform").

## Initial Boundary

Working hypothesis at start:

- Core purpose: a system of record for the requirements an engineered product (system, hardware, software, regulated device) must satisfy — capturing, structuring, tracing, reviewing, baselining, and managing change of those requirements across the engineering lifecycle.
- Primary users: systems engineers, requirements engineers, product/program managers, design engineers, test/V&V engineers, quality/regulatory staff.
- Nearest neighbors: Requirements Management Platform (§12 sibling), MBSE Platform, PLM, Issue Tracker, Software Test Management, Engineering Change Management, Product Management Platform.
- Known unknowns: exact object models per product; how review/approval machinery works; how traceability is implemented; reuse/variant machinery; whether §12 and §16 leaves are the same Type.

## Research Questions

1. What is the "requirement" as an object (identity, text, attributes, versions)?
2. How are requirements organized (modules/documents, hierarchy, projects, components)?
3. What is traceability and how is it implemented (link types, coverage views, matrices)?
4. How does change management work (baselines, versions, change proposals, approvals, signatures)?
5. How do requirements connect to tests/V&V and to risk?
6. What collaboration surfaces exist (review cycles, comments, dashboards)?
7. How is reuse across product lines/variants handled?
8. What standards/compliance machinery exists (ISO 26262, DO-178C, IEC 62304, ASPICE, CMMI)?
9. What interfaces do users actually work in?
10. Boundary: vs MBSE, PLM, issue trackers, product management — and §12 vs §16.

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Vendor | Philosophy / tier |
|---|---|---|
| IBM Engineering Requirements Management DOORS Next (and classic DOORS) | IBM | Enterprise systems-engineering incumbent; DOORS lineage "several decades" (vendor-stated); part of Engineering Lifecycle Management suite |
| Jama Connect | Jama Software | Regulated-industry requirements specialist (medical device, automotive); review + traceability center; mid-to-large tier |
| Polarion ALM / Polarion REQUIREMENTS | Siemens | Unified single-repository ALM philosophy — requirements, code, tests, release in one work-item model; large enterprise |
| Visure Requirements | Visure Solutions | Compliance-first requirements ALM for regulated industries; mid-market + enterprise; best-of-breed integrations |

## Sources

Fetched 2026-09-08 (research date). Evidence layers: A = directly observed on an official source for a specific product; B = cross-product commonality; C = canonical inference.

- IBM — Engineering Requirements Management product page: https://www.ibm.com/products/requirements-management (Tier 2)
- IBM — DOORS Next documentation: https://www.ibm.com/docs/en/engineering-requirements-management-doors-next — **HTTP 403, unreachable ×2**; alternate docs URL also 403. IBM training page returned empty (JS-rendered). Limitation recorded; IBM claims kept at product-page strength.
- Jama Software Support Center (Tier 1): https://support.jamasoftware.com/ — Knowledge Base category map, "Use & Troubleshoot Jama Connect" section map, "Items, Item Types & Lifecycle", "Versioning & Baselines", "Reviews & Collaboration", "Traceability & Relationships" section maps; article "Model-Based vs. Document-Centric Project Structures in Jama Connect®" (full text)
- Polarion (Siemens) product pages (Tier 2): https://polarion.com/ (redirects to siemens.com/en-us/products/polarion/) and https://plm.sw.siemens.com/en-US/polarion/requirements/
- Visure Solutions product pages (Tier 2): https://www.visuresolutions.com/ and https://visuresolutions.com/features/requirements-management-software/ ; help center https://visuresolutions.zendesk.com/hc/en-us — **timed out ×1, abandoned**; Visure evidence is product-page level (marketing-leaning), so operational claims kept general.

## Product Observations

### IBM Engineering Requirements Management (DOORS Next / DOORS)

Key observations (evidence layer A unless noted; product-page strength only — docs unreachable):

- Positioning: "capture, trace, analyze and manage changes to requirements while maintaining compliance with regulations and standards" (DOORS Next); classic DOORS described as used "for several decades" in "complex, high-compliance systems engineering programs".
- Data organization: "Specify a data model, organize your data with structured folders, modules and hierarchy, and use advanced filtering, views and tags."
- Traceability: "Link artifacts for alignment and use a graphical explorer to visualize project relationships"; classic DOORS: "customizable requirements views with multi-level traceability".
- Change/versioning: "Track requirements across the lifecycle with versioning, baselines and supplier exchanges"; classic DOORS: "electronic signatures, baselines".
- Configuration & variants: "Manage global configurations, reuse components, track changes and handle multiple development streams."
- Compliance use cases: ASPICE, ISO 26262, DO178C.
- AI automations: quality scores against industry standards, wording recommendations, conversational queries (era-current).
- Classic DOORS: "structured requirements specification modules, round-trip data import and export".
- Packaging note: DOORS Next (web-based) and DOORS (classic client) are two products under one brand; both are requirements management.

### Jama Connect

Key observations (evidence layer A; support-center KB, strongest source in sample):

- Object model: **Items** with configurable **item types**, **fields/picklists/categories**, **workflows** with lifecycle states, **locks** (user-locked and system-locked items), deletion as "made inactive" (soft delete with retrieval).
- Organization: **Explorer tree** per project; two documented structure philosophies — "Model-Based Product Structure" (organized by abstraction level / engineering discipline / V-model) vs "Document-Centric Structure" (Explorer tree mirrors a table of contents; medical-device framework can simulate a Design History File with Introduction/Scope/References sections). Hybrid supported; documents generated via **Advanced Filters** + report templates rather than the tree alone.
- Versioning & baselines: baselines as snapshots; **Baseline Diff Report** (added/removed/updated items); "version vs current" comparison; trace matrix exportable from a baseline; assigning requirements to a system release/version; reuse with "source project hierarchy in destination project".
- Traceability: **Traceability Views (Trace View / Coverage / Relationships)**; relationships between items; Explorer tree navigation.
- Review: **Review Center** — review lifecycle & status, review participation & permissions, e-signature & approvals, comments, review content & traceability, review reports & exports.
- Test: dedicated Test Management section; "Verification vs. Validation in Jama Connect" article exists (title-level evidence only).
- Interchange: imports/exports for Word, Excel, **ReqIF**.
- Administration: item types/fields configuration, permissions, project templates ("template project" article).

### Polarion ALM / Polarion REQUIREMENTS

Key observations (evidence layer A; product pages):

- Unified repository philosophy: "a single, unified solution for requirements, coding, testing and release"; "Manage extra large enterprise data, hundreds of projects and millions of requirements, all in one unified repository".
- **LiveDocs**: "online structured specification documents … every single paragraph uniquely identifiable and traceable" — the document is a live container whose paragraphs are requirement-grade work items.
- Work items: "system requirements specifications, verification procedures, project plans and tasks—everything is simply stored in version control repositories, so every modification produces a version history record."
- Workflows: "workflows that enforce how and when they move from state to state based on definable rules, with full audit trails, electronic signature and security."
- E-signature gate: "Invite and require stakeholders to electronically sign the specification documents as reviewed or approved before they can be released to production."
- Traceability: "traceability that is easily implemented and guaranteed via automatic change control of every requirement."
- Time machine: "browse, search and report any historical state of your project just like you do the current state."
- Reuse/branching: "Derived Documents" for shared regulatory requirements distributed across projects; "Branch specification documents to effectively manage commonalities between your products"; distribute changes from master to branched documents on demand.
- Interchange: "Built-in ReqIF enables lossless requirements and test case specifications exchange with customers and suppliers"; rule-based Import Wizard from Word/Excel.
- Test: "Build test cases in parallel with requirements in our unified solution."
- Integrations: Simulink, Azure DevOps, HP QC, Jira connectors; open APIs; extensions platform.
- Reporting: real-time online reports, WYSIWYG report designer, cross-project reports, dashboards ("My Polarion").
- Deployment: on-premise (Polarion ALM) or cloud (Polarion X).

### Visure Requirements

Key observations (evidence layer A; product pages — marketing-leaning, kept general):

- Requirements management: "Capture, organize, and manage requirements at every level of abstraction. Full history, attributes, and ownership tracking across the entire product lifecycle."
- Authoring: "authoring, reading, and editing items in a single view without losing visual context in the overall document. Achieve a balance between atomic requirements management and traceability, all while maintaining a familiar document-style approach."
- Traceability: "Live traceability matrix from stakeholder need to test result, covering requirements, risks, source code, and defects"; "explore upstream and downstream relationships, anticipate change impact, monitor cross-project relationships … visualize relationship rules across projects."
- Change & impact: "Understand the full downstream impact of every change before you approve it. Automated propagation across linked items with a complete audit trail: who changed what, when, and who signed off."
- Baselines & reuse: "Compare changes in requirements … snapshot project states, build reusable requirements catalogs, and develop product variants or new versions"; "development stream baselines or requirement catalogs."
- Test & V&V: "Test cases, test runs, and V&V evidence linked directly to requirements. Coverage reports and verification matrices generated automatically."
- Risk: "Integrate FMEA and risk analysis directly with your requirements. Bidirectional links to hazards and controls"; PHA and FMEA techniques; open risks traced to requirements.
- Compliance: "Standards-aligned workflows for DO-178C, ISO 26262, IEC 62304, EN 50128"; "Audit evidence packages generate directly from your live traceability data"; industry packs (aerospace, automotive, rail, medical, energy, semiconductors).
- Cybersecurity: TARA outputs linked to security requirements; ISO/SAE 21434, IEC 62443, CRA.
- Interchange: ReqIF, IBM DOORS, MS Word/Excel (two-way sync).
- Quality analysis: "Automatically analyze the quality of requirements while writing them" (ambiguity detection; INCOSE-guideline scoring via AI assistant).
- AI (Vivia): requirements generation, ambiguity detection, quality scoring, test-case generation, human-in-the-loop approval before entering a baseline (era-current).
- Tool suite packaging: Requirements ALM Platform + Contributor/Reviewer license tier + Report Manager + Quality Analyzer + Automated Checklists + Tool Qualification Package (aviation tool-qualification context).
- Deployment: cloud or on-premise incl. air-gapped.

## Cross-product Comparison

| Aspect | IBM DOORS Next | Jama Connect | Polarion | Visure |
|---|---|---|---|---|
| Requirement object | artifacts in modules (data-model-driven) | items with item types, fields, workflows, locks | work items; LiveDocs paragraphs uniquely identifiable | items with attributes, history, ownership |
| Organization | data model + folders + modules + hierarchy | Explorer tree; model-based vs document-centric structures | LiveDocs specification documents + work items in one repository | document-style view over atomic items; configurable data model |
| Traceability | link artifacts; graphical explorer; multi-level views | relationships; trace view / coverage | links; "automatic change control of every requirement" | live traceability matrix; upstream/downstream; relationship rules |
| Versioning/change | versioning, baselines, supplier exchanges | baselines, baseline diff, version-vs-current, release assignment | version history per modification; time machine; change requests | versions, baselines, impact analysis, audit trail |
| Review/approval | e-signatures (classic DOORS) | Review Center: lifecycle, permissions, e-signatures, comments | workflow-enforced states + e-signature before release | review + sign-off audit trail |
| Test/V&V linkage | via ELM suite | test management section | test cases in parallel, unified | test & V&V management, coverage reports |
| Risk linkage | not observed on page | not observed | not observed | FMEA/PHA integrated (product-specific emphasis) |
| Reuse/variants | global configurations, reuse components, development streams | reuse with source hierarchy | derived documents, branching, product lines | requirement catalogs, variants, stream baselines |
| Compliance | ASPICE, ISO 26262, DO178C | QMS/audit documents, DHF (medical) | audit/SPICE positioning | standards packs (DO-178C, 26262, 62304, EN 50128, 21434) |
| Interchange | round-trip import/export | Word, Excel, ReqIF | ReqIF built-in; Word/Excel import | ReqIF, DOORS, Word/Excel sync |
| Deployment | enterprise (ELM suite) | cloud + self-hosted Kubernetes | on-prem + cloud | cloud + on-prem/air-gapped |
| AI | quality scores, conversational queries | (not sampled) | (not sampled) | generation, ambiguity detection, test-case generation |

## Canonical Abstraction

### L0 — Defining Invariant

Four jointly-held structures. Removing any one stops the product from being recognizable as Engineering Requirements Management:

1. **The requirement of record** — a persistent, individually identified (stable unique ID), versioned statement of a capability, condition, or constraint the engineered product must satisfy, carrying attributes (statement text, rationale, verification method, status, ownership). Remove → there is nothing to manage; the product becomes a document editor or a generic work-item tracker.
2. **Structured organization of the requirement set** — requirements held in a structured collection within a project: a hierarchy, a specification document, or a tree of folders/modules. Remove → flat ticket list; the specification character disappears (issue-tracker shape).
3. **Traceability links** — explicit, typed, navigable links between requirements (upstream/downstream, derive/refine/satisfy/verify) and to related artifacts (stakeholder needs, design, tests, risks). Remove → a requirements document processor; "management" collapses to authoring.
4. **Managed change over the lifecycle** — version history per requirement, baselines (frozen snapshots of the requirement set), and controlled change (impact analysis, review/approval before changes take effect). Remove → a static snapshot; the "management" in the Type name is gone.

Jointly-held is load-bearing:
- 1+2 without 3 = requirements document authoring (Word with numbering)
- 1+3 without 2 = a flat link database, not an engineering specification
- 2+3 without 1 = structure with no stable records
- 1+4 without 3 = a versioned document store, not traceability-driven engineering
- 3+4 without 1 = change machinery with nothing to change

### L1 — Common Mature Structure

Present across the sample (4/4 unless noted) but not definitional:

- Review/approval machinery: structured review cycles with comments, reviewer roles, and electronic signatures (Jama Review Center; Polarion e-sign before release; IBM DOORS e-signatures; Visure sign-off audit trail)
- Test/V&V linkage: test cases/runs linked to requirements; coverage views; verification matrices
- Reuse & variant machinery: reusable requirement components/catalogs, branching, product-line development streams
- Interchange: ReqIF (industry standard exchange with customers/suppliers), Word/Excel import-export round trips
- Document generation & reporting: specification documents, traceability matrices, compliance/audit reports generated from the live record
- Dashboards/analytics: coverage status, progress, quality metrics
- Permissions/roles: who can see/edit/approve what; contributor/reviewer license tiers (Visure names it; all sample products have role differentiation)
- Integrations: issue trackers (Jira), MBSE/modeling tools (Simulink, Enterprise Architect, Cameo), test tools (VectorCAST, HP QC), code platforms (GitLab/Azure DevOps)
- Requirements quality analysis: rule-based or AI-assisted checks for ambiguity/testability (era-current form: AI)

### L2 — Variant / Optional Structure

- Risk/FMEA integration as a first-class module (Visure emphasis; regulated-industry variant)
- Cybersecurity requirements engineering (TARA, ISO/SAE 21434) (Visure; era/industry variant)
- Standards packs per industry (DO-178C/DO-254 aviation, ISO 26262/ASPICE automotive, IEC 62304/ISO 14971 medical, EN 50128 rail)
- Tool qualification packaging (Visure Tool Qualification Package — aviation DO-330 context)
- Deployment posture: cloud vs on-premise vs air-gapped (all sample products offer a regulated-friendly on-prem option)
- Source-code traceability (Visure, Polarion)
- Supplier exchange workflows (IBM "supplier exchanges"; Polarion ReqIF with customers/suppliers)
- MBSE integration depth (model synchronization vs link-only)
- AI assistance depth (generation, conversational query) — era-current

### L3 — Vendor-specific Structure

(kept out of the final document)

- IBM: global configurations; DOORS Next vs classic DOORS dual packaging; ELM suite composition; graphical sketching; glossary of terms
- Jama: Review Center as named surface; baseline diff report; DHF-simulating medical-device framework; "made inactive" deletion semantics; set item type with set keys
- Polarion: LiveDocs (paragraph-level identity inside live documents); Derived Documents; time machine; unified work-item model spanning code/tests
- Visure: Vivia AI assistant; Contributor/Reviewer license tier; Report Manager / Quality Analyzer / Automated Checklists / Tool Qualification Package add-ons; MCP-server AI integration

## Historical / Market-Sample Check

- Classic DOORS (vendor-stated "several decades" of use in high-compliance programs) already exhibits the four L0 structures: structured specification modules, links/multi-level traceability, baselines, electronic signatures — with no cloud, no AI, no ReqIF. The core holds without modern implementations.
- Pre-tool practice (requirements registers in spreadsheets/word processors with IDs, attributes, hand-maintained traceability matrices, and change logs) satisfies a thin version of the core — the market itself pitches these products as the replacement for "version chaos in Word or Excel" (Visure) and "keeping multiple Word/Excel documents up to date" (customer quote). This confirms the L0 is era-independent: the tool industrializes identity, structure, traceability, and change control that existed as manual practice.
- Conclusion: no L0 element depends on the current dominant implementation (cloud, AI, ReqIF, ALM unification).

## Vendor-specific Findings

See L3 above. Additional notes:

- Polarion's unified work-item model is a philosophy difference, not a Type difference: requirements, test cases, and tasks share one object infrastructure, but the requirement-specific structures (LiveDocs identity, traceability, baselines) remain.
- Jama's model-based vs document-centric structure choice is a documented customer decision point, not a product split — both shapes realize the same L0.
- Visure's risk/FMEA and cybersecurity modules are deeper than sample peers, but this is emphasis, not a different Type.

## Boundary Findings

1. **vs Requirements Management Platform (§12 sibling, unprocessed)**: The directory lists both "Requirements Management Platform" (§12 Software Development) and "Engineering Requirements Management" (§16 Engineering/Manufacturing). Research shows the market does NOT maintain two product categories: the same products (Jama, Polarion, Visure, DOORS) serve software-only and systems/hardware engineering; all four explicitly cover software requirements alongside systems requirements. The §12/§16 split appears to be industry-positioning of one Type, not two Types. **Flagged for joint review** when the §12 leaf is processed; candidate outcomes: alias/consolidation, or a segment-variant seam (software-team pole vs systems-engineering pole). This pass documents the Type once, with the software-development pole named in Variants.
2. **vs MBSE Platform**: MBSE centers on formal system models (SysML-style); requirements may live as model elements. ERM centers on requirement records with textual statements, attributes, and traceability. Adjacent, complementary; integration (Simulink/Enterprise Architect/Cameo connectors) is the seam. MBSE platforms may embed requirements modules — overlap noted, boundary held on center of gravity (model-first vs record-first).
3. **vs PLM**: PLM's center of gravity is the physical product record (BOM, CAD, documents, engineering change). Requirements may be linked from PLM but are not its core object. Consistent with the bill-of-materials-management pass's boundary criterion (center of gravity).
4. **vs Issue Tracker / Bug Tracking System**: work items to be executed (plan/execute lifecycle, flat lists) vs statements of what to build (hierarchical specification, traceability, baselines). Polarion blurs the seam by unifying both in one work-item model — but even there, requirements carry LiveDocs identity + traceability + baselines that defects/tickets do not.
5. **vs Software Test Management**: test cases/runs/verdicts vs requirements; linked bidirectionally (coverage) but different centers. Test management appears as a module inside several ERM products (Jama, Visure, Polarion) — module bundling, not Type merger.
6. **vs Engineering Change Management (§16 sibling)**: ECM is the change-process machinery for engineering artifacts (ECOs, effectivity); ERM holds the requirement record and its change history. ERM's change management is requirement-set-scoped (baselines, change requests against requirements); deep cross-artifact change orchestration belongs to ECM/PLM.
7. **vs Product Management Platform / Product Roadmap**: market-facing prioritization (backlogs, roadmaps, customer demand) vs engineering specification of record (verifiable statements, compliance evidence). Vocabulary overlap ("requirements") but different objects, users, and rules.

## Uncertainties

- IBM DOORS Next operational detail (artifact/module terminology, exact link types, configuration mechanics) could not be verified — docs 403 ×2; claims kept at product-page strength.
- Visure help center unreachable (timeout); Visure evidence is product-page level and marketing-leaning; operational claims kept general.
- Exact state vocabularies (requirement statuses, review states) vary by product and were not asserted.
- Whether the §12 leaf, when processed, will confirm the alias/variant reading — flagged, not decided.
- Jama's Verification-vs-Validation article was seen at title level only; V&V semantics not asserted in detail.
- AI capabilities are era-current and evolving; treated as L2 throughout.

## Final Synthesis

Engineering Requirements Management is the engineering side's system of record for what the product must satisfy. Its defining core is exactly four jointly-held structures: the requirement of record (persistent, uniquely identified, versioned, attributed statement), the structured organization of the requirement set (hierarchy/specification-document/tree within a project), traceability links (typed, navigable, bidirectional, extending to needs/design/tests/risks), and managed change (version history, baselines, controlled change with impact analysis and approval). Everything else — review centers with e-signatures, test linkage, reuse/variant machinery, ReqIF/Office interchange, document generation, dashboards, standards packs, risk integration, AI quality analysis — is common mature structure or variant capability, not definition. The Type is era-independent (classic DOORS and even spreadsheet-era practice satisfy the core) and industry-independent (the same products serve software, systems, hardware, and regulated-device engineering), which is precisely why the §12/§16 directory split needs a joint-review flag rather than a hard Type boundary.
