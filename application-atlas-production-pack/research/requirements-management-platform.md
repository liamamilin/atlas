# Research Notes — Requirements Management Platform

## Research Goal

Understand what a Requirements Management Platform (§12, Software Development & Product Engineering) really is, from real products: what objects exist inside it, what users do with them, how requirements work flows, which states/rules matter, and where the Type's boundaries lie. This pass carries three pre-hung joint-review obligations from earlier passes:

1. **vs Engineering Requirements Management (§16, processed 2026-09-08)** — that pass flagged that the directory carries two leaves but the market may maintain only one product category; candidate outcomes: alias/consolidation, or a segment-variant seam. This pass must discharge that flag.
2. **vs Product Management Platform (§12, processed 2026-09-09)** — that pass flagged "specs = handoff out of the PM platform" as the proposed seam.
3. **vs Product Roadmap Application (§12, processed 2026-09-09)** — that pass left an open item: "no spec/requirement objects surfaced in any sampled roadmap core — plan lines express what/when, not how-exactly".

## Initial Boundary

Working hypothesis at start:

- Core purpose: a system of record for the requirements a product (software, hardware, system, regulated device) must satisfy — capturing, structuring, tracing, reviewing, baselining, and managing change of those requirements across the development lifecycle.
- Primary users: business/systems analysts, requirements engineers, product owners, developers, QA/test engineers, compliance staff.
- Nearest neighbors: Engineering Requirements Management (§16 sibling), Product Management Platform, Product Roadmap Application, Issue Tracker, Engineering Project Management Platform, Software Test Management, MBSE Platform.
- Known unknowns: whether the §12 population differs from the §16 population; how the DevOps-native realization (RM built inside Azure DevOps) relates to the classic standalone form; how lightweight desktop tools fit.

## Research Questions

1. What is the "requirement" as an object (identity, text, attributes, versions)?
2. How are requirements organized (documents, hierarchies, trees, work-item structures)?
3. What is traceability and how is it implemented (link types, direction, coverage, matrices)?
4. How does change management work (history, baselines, impact analysis, suspect links)?
5. How do reviews/approvals work?
6. How do requirements connect to tests, risks, and source code?
7. How do these products integrate with the software-development toolchain (issue trackers, DevOps platforms, modeling tools)?
8. Do the sampled products serve software-only teams, or also systems/hardware/regulated engineering? (the §12/§16 joint-review question)
9. What interfaces do users actually work in?
10. Boundary: vs product management, roadmaps, issue trackers, engineering PM, MBSE, test management.

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers — deliberately disjoint from the §16 pass's sample (IBM DOORS Next, Jama Connect, Polarion, Visure) so this pass's evidence is independent:

| Product | Vendor | Philosophy / tier |
|---|---|---|
| ReqView | Eccam | Lightweight desktop requirements tool with Git/SVN version control; small-to-mid teams; HW/SW and systems engineers; 10+ years on the market |
| Perforce ALM (Helix ALM) Requirements Management module | Perforce Software | Modular ALM suite — requirements, test cases, issues as separate modules; mid-to-large; ISO 26262-certified; medical/defense/automotive customers |
| Modern Requirements4DevOps | Modern Requirements | DevOps-native pole — requirements management built directly inside Azure DevOps; regulated-industry programs (FDA, DO-178C, ISO 26262, ASPICE) |
| codebeamer | PTC (Intland) | Unified ALM platform with requirements management as a dedicated domain; medical, automotive, aviation, pharma |

## Sources

Fetched 2026-09-09 (research date). Evidence layers: A = directly observed on an official source for a specific product; B = cross-product commonality; C = canonical inference.

- ReqView homepage: https://www.reqview.com/ (Tier 2)
- ReqView Documentation (Tier 1): https://www.reqview.com/doc/welcome/ — full documentation map; and https://www.reqview.com/doc/requirements-traceability-links/ — full article (traceability links, link types, suspect flags, RTM, linked projects). Deepest operational source in this pass.
- Perforce ALM product page: https://www.perforce.com/products/helix-alm (Tier 2)
- Perforce ALM Requirements Management page: https://www.perforce.com/products/helix-requirements-management (Tier 2). Note: https://www.perforce.com/products/helix-alm/helix-rm returned 404 ×1; the correct path is /products/helix-requirements-management. Perforce documentation portal (portal.perforce.com) not fetched — claims held at product-page strength.
- Modern Requirements4DevOps homepage: https://www.modernrequirements.com/ (Tier 2)
- Modern Requirements4DevOps features page: https://www.modernrequirements.com/products/modern-requirements4devops-features/ (Tier 2, detailed capability descriptions; vendor-authored, marketing-leaning — operational claims kept general)
- codebeamer homepage: https://codebeamer.com/ (Tier 2) — core capabilities list, industry solutions, knowledge-base links
- codebeamer Help Center (Tier 1): https://support.ptc.com/help/codebeamer/r3.3/en/codebeamer/user_guide/ug_cb_common_concepts.html — "dedicated support for … requirements management, test management, and task management"; and ug_dashboard.html (dashboards). Note: codebeamer.com wiki (User's Guide) requires login; intland.com/requirements-management/ transport error ×1 — abandoned per network rule; codebeamer claims held at homepage + help-center strength.

## Product Observations

### ReqView (Eccam)

Key observations (evidence layer A; homepage + documentation):

- Self-labeling: "HW/SW Requirements Management Tool on Git"; "Simply Powerful Solution for HW/SW and Systems Engineers". Audience explicitly spans hardware, software, AND systems engineering.
- Purpose framing: "Develop software and hardware products using the V-Model process with formal verifications, end-to-end traceability and full audit trails. Comply with safety-critical and information security standards." Industries named: Medical Devices, Aerospace & Defense, Automotive & Railways, Robotics & Electronics.
- Three-step pitch: Capture Requirements (templates based on ISO/IEC/IEEE 29148:2018, import from Word, "Describe structured requirements by formatted text, tables, images, PDF, or other files") → Manage Requirements and Risks ("Customize requirement attributes according to your work-flow. Link related requirements, verification & validation, and safety risks. Baseline requirements in Git.") → Analyze Requirements Traceability ("Meet safety standards, analyze requirements coverage, risks, and impact of changes. Browse traceability links or generate reports to MS Word, Excel, PDF, or HTML formats.")
- Versioning substrate: "Track requirements in Git as your source code. Benefit from human-readable JSON format. Integrate with Github, Gitlab, ADO or Bitbucket hosted on premise or in cloud." Also SVN and Google Drive collaboration; shared-drive collaboration.
- Documentation map (Tier 1): Requirements Projects (open/save projects, reusable document templates); Edit Documents (structure requirements documents, set attributes, discuss requirements); Custom Attributes; Traceability Links; Filter & Search; Change Management ("track requirements changes using requirements history"); Project Dashboard; Linked Projects ("split projects with a high number of documents and reuse requirements in several products"); Review Documents; imports (Word, Excel, ReqIF); exports (DOCX, XLSX, PDF, HTML, CSV, ReqIF, custom templates); integrations (Jira Cloud, Azure DevOps, Sparx Enterprise Architect); administration (CLI, floating license server).
- Traceability article (Tier 1, full text): "Requirements traceability links represent relationship between requirements and other project artifacts." "You can create directed traceability links between objects from the same document, between objects from different documents in the same project, or from linked projects." "links are usually organized into custom traceability link types" — user-definable link types with name/source/target/suspect properties (JSON-configurable in the Project Traceability dialog); V-model example defines *satisfaction* and *verification* link types. Directional guidance: "We strongly recommend that you link requirements upwards, i.e., from derived to the source information." RTM: "a shared Table View displaying Traceability Columns" — a live traceability matrix view, up to three traceability levels per column wizard. Suspect flags: "find missing links … and track changes in the linked object by filtering suspect flags." Copy semantics: "ignore, duplicate, or inherit traceability links from the copied origin to its new copy" (origin references propagate inherited links). Compliance framing: "Detailed and consistent requirements traceability is essential for understanding the impact of proposed changes to high-level requirements before the changes are propagated downstream. It is also required to ensure compliance with several Automotive, Aerospace, Defense, and Medical industry standards."
- Templates offered: ISO/IEC/IEEE 29148, OWASP ASVS, Volere Process, User Stories, FMEA.
- Customer-review positioning (vendor-published Capterra quotes): "It is very similar to a limited DOORS product but at a fraction of the price" (medical devices VP); "Round trip update from Jira! Possible to work with distributed teams/tiers (document exchange)" (aviation systems engineer).
- MBSE integration: "Connect ReqView with Sparx Systems Enterprise Architect (EA) to benefit from an integrated Model-Based Systems Engineering (MBSE) solution." Jira/ADO integration framed as "Requirements Management for Jira and Azure DevOps — Manage end-to-end requirements traceability. Analyze impact of changes. Comply with safety critical standards for automotive, A&D, and medical devices industries."

### Perforce ALM (Helix ALM) — Requirements Management module

Key observations (evidence layer A; product pages):

- Suite structure: "With dedicated modules for requirements, test case, and issue management, Perforce ALM offers a full suite of ALM software… Take advantage of the complete suite, or start with one module and grow into the solution at your own pace." Requirements management is a purchasable module that also stands alone: "You can use the module on its own, or as part of the ALM suite. You can even use it alongside Jira."
- Positioning: "Easily track requirements throughout the development lifecycle for automatic, continuous traceability"; "capture and review requirements, understand the impact of changes, and always know which requirements have been met and which ones are outstanding."
- Anti-spreadsheet framing: "Using spreadsheets to manage requirements is inefficient and can't give you the traceability you need."
- Centralize: "everyone can work on the most recent, up-to-date requirements. You'll be able to organize (and reorganize) their hierarchy in real-time."
- Decompose: "decompose marketing requirements into product requirements, system specifications, and functional requirements. Import existing requirements in any number of formats." (abstraction-level decomposition named explicitly)
- Reuse: "you can reuse requirements. You'll save time when writing requirements and ensure consistency across your project."
- Track and trace: "you'll be able to link requirements to: Other requirements. Test cases and test results. Source code. And more." "the ALM requirements management module automatically creates a requirements traceability matrix for you."
- Impact analysis: "Impact analysis helps you understand the impact of requirement change on related requirements (and test cases)… When a requirement changes, you'll know exactly which items need to be reviewed."
- Collaborate/review: "requirements reviews… Stakeholders can comment in real-time. You can even export requirements documents to Microsoft Word for customers or stakeholders who don't have ALM." "You will know who has reviewed requirements and who you are waiting on. Keep communication flowing and gain approval faster."
- Baselines: "You can also compare historical data with baselines. You'll be able to prove compliance in record time." (traceability-matrix tab)
- Risk: "you can create requirements based on risk. You can also do risk analysis, including FMEA and impact analyses."
- Workflows: "let the workflow engine handle states, events, transitions, assignment rules, escalation rules, triggers, and more."
- Test linkage: "create test cases based on requirements. Generate test runs based on those test cases. And trace test results back to requirements." Failed test runs "automatically create an issue."
- Issue-tracker boundary (vendor's own words): "Are you tracking bugs and managing tasks in Jira? … you can keep using Jira (and get more out of it) by adding a requirements management tool. (Because, let's face it, using Jira for requirements doesn't work.)" — "link requirements to Jira issues — and vice versa… know which requirements have outstanding issues at all times."
- Compliance: "ISO 26262 certified to meet the most stringent functional safety requirements"; customer logos span medical devices (Biomerieux, Vyaire), defense (US DoD), consumer (Sennheiser, Leica). Customer story: traceability matrix + documentation "to fulfill regulatory compliance needs, demonstrate that all requirements have been met, and prepare for audits"; "More ways to link requirements, test cases, and other items to show dependencies"; "Automatic traceability matrix for an immutable single source of truth"; "Built-in traceability reports to compare historical data with baselines."
- Integrations: Jira, Jenkins, P4 (Helix Core), Slack, Word, Excel, IBM, GitHub, Visual Studio, OpsHub; REST API.

### Modern Requirements4DevOps

Key observations (evidence layer A; homepage + features page — vendor-authored, marketing-leaning, operational claims kept general):

- Self-labeling: "End-to-end requirements management in Azure DevOps"; "the only requirements management solution built directly within Azure DevOps Server/Services and TFS"; features page: "Modern Requirements4DevOps is the requirements management platform built natively for Azure DevOps… Lives inside ADO. Works the way your team already does." — the DevOps-native realization: no separate URL or login; inherits the ADO permission model.
- Compliance positioning: "Built for FDA, ISO, DO-178C, IEC, ASPICE programs from day one"; standards named across pages: FDA 21 CFR Part 11, ISO 13485, IEC 62304, DO-178C, ISO 26262, ASPICE, MIL-STD-882E, DO-254, IEC 61508, NERC CIP, DORA, GAMP 5. Industry solutions: MedTech, Healthcare, Defence, Banking & Finance, Systems Engineering ("ISO 26262, ASPICE, and functional-safety traceability from the V-model to verification"), Energy & Utility, Railways.
- Authoring: **Smart Docs** — "Instead of managing work items one by one in ADO, Smart Docs lets you create, organize, and edit them inside a document-style interface, complete with hierarchy, indentation, and configurable column layouts. Build from scratch or from reusable templates." Document lifecycle: "compare against a saved version, clone across projects, capture as a Baseline, or send for review, all without leaving the document."
- Reporting: **Smart Report** — "Generate Word, PDF, or HTML reports from your live ADO data using customizable templates. Audit-ready output… Live data binding. Reports always reflect the current state of your work items."
- Document management: personal/shared workspaces, check-out/check-in version control, multi-version Word compare.
- Legacy bridge: **Word Import** — "Bring existing Word documents into ADO as structured work items. Map headings to hierarchy, preserve formatting, and round-trip back to Word via Smart Report."
- Test linkage: **Test Hub Reporting** — "Compliance-ready test reports linked to Azure Test Plans. Surface coverage, execution outcomes, and traceability in one report ready for audit."
- Review: **Review Management** — "Create a review request from any Smart Doc or work item set. Assign reviewers and approvers, set a due date, send… Reviewers comment per item and click Mark as Reviewed. Approvers can Approve, Reject, or act on the full set… A comment is required on any rejection, creating an automatic, traceable audit trail… E-signatures. Capture electronic sign-off with reauthentication where required." Distinct reviewer/approver roles; personal "Reviews Assigned To Me" queue; threaded comments.
- Traceability: **Trace Analysis** — "Build matrices between any two sets of ADO work items. Three views (Grid, List, Heatmap) plus an Analytics tab for gap analysis and state distribution… Choose an Intersection Matrix to map two work item types against each other, or a Horizontal Matrix to expand a hierarchy of linked items. Edit links inline without leaving the matrix." Coverage example: per-requirement test counts and coverage percentages; "Heatmap visualization. Color-coded coverage density. Spot gaps instantly."
- Baselines: **Baseline** — "Capture an immutable snapshot of work items at any milestone. Once captured, a baseline cannot be edited. Compare against current state or against another baseline, copy across projects, merge two baselines, or generate a Word-format Difference Report."
- Variants: **Variant Management** — "Manage product, region, or customer-specific configurations from a single requirement set. Capture variants, compare any two side by side with color-coded highlighting of added, removed, and updated work items. Share variants across projects, lock at milestones, and roll back to any prior state." **Parameterized Requirements** — "Write a requirement once, parameterize it, and reuse across product configurations."
- Change impact: **360° Impact Assessment** — "Evaluate how a proposed change affects existing work items across the project." **Suspect Link** flagging (blog-listed feature).
- AI capabilities (era-current, 12 named): Elicitation, Chat, Analysis ("Evaluate requirements against 6C's, INVEST, and MoSCoW quality frameworks"), Impact Assessment, Diagram Generation, Mockup, Pseudocode & Test Scripts, Convert ("Express requirements as user stories, use cases, or Gherkin scenarios"), Dynamic Prompt, SOP/Document Generator, Transform, Q&A Assistant.
- Requirement identity: **Custom ID** — "how to make your requirement IDs more descriptive and distinctive".

### codebeamer (PTC / Intland)

Key observations (evidence layer A; homepage + help center — positioning strength, operational detail limited):

- Positioning: "Welcome to codebeamer, the integrated Application Lifecycle Management platform from PTC"; "Develop better software, faster."
- Core capabilities list: "Application Lifecycle Management, Requirements Management, Software Development, QA and Test Management, IT Operations / DevOps, Demand Management, Risk Management, Variants Management" — requirements management named as a first-class capability of the ALM platform.
- Help center (Tier 1): "Codebeamer provides dedicated support for various problem domains, such as requirements management, test management, and task management. In addition to specialized support for these specific domains, Codebeamer includes a common set of features applicable across each of these domains." — requirements management is a dedicated domain sharing a common work-item infrastructure with tests and tasks (the unified-ALM philosophy, same family as Polarion per the §16 pass).
- Dashboards (Tier 1): wiki-plugin dashboards at project/team/personal scope; widgets for statistics, activity streams, open-vs-resolved issues.
- Industry solutions: Medical, Automotive, Aviation, Pharmaceutical — regulated-engineering positioning.
- Knowledge base exists (User's Guide, Admin Guide, Developer's Guide) but the wiki requires login; deeper operational detail not fetched.

## Cross-product Comparison

| Aspect | ReqView | Perforce ALM RM | Modern Requirements4DevOps | codebeamer |
|---|---|---|---|---|
| Requirement object | document objects (sections/requirements) with custom attributes, IDs | requirements as tracked items with hierarchy | ADO work items surfaced in document-style Smart Docs | dedicated requirements domain over common work-item infrastructure |
| Organization | requirements documents in projects; sections; linked projects | hierarchy, organize/reorganize in real time | Smart Docs hierarchy + ADO project structure | project/tracker structure |
| Traceability | directed links, custom link types (satisfaction/verification), suspect flags, live RTM table view | links to requirements/test cases/test results/source code; automatic traceability matrix | Trace Analysis matrices (intersection/horizontal), Grid/List/Heatmap, gap analytics, inline link editing | traceability within ALM (capability-level evidence) |
| Change management | requirements history (Change Management doc); Git/SVN versioning; baselines in Git | manage changes; impact analysis; baselines comparison | immutable Baselines, Difference Report, 360° Impact Assessment, suspect links | versioned work items (common-infrastructure evidence) |
| Review/approval | Review Documents (review/print/export) | requirements reviews with approvals, who-has-reviewed visibility | Review Management: reviewers/approvers, mandatory rejection comments, e-signatures | (not sampled at detail) |
| Test/V&V linkage | verification links; tests as linked artifacts | test cases created from requirements; test runs; results traced back | Test Hub Reporting linked to Azure Test Plans; coverage | QA and Test Management domain |
| Risk linkage | risks as linked artifacts; FMEA template | requirements based on risk; FMEA analysis | risk management in MedTech/Defence solutions | Risk Management capability |
| Reuse/variants | linked projects; copy with ignore/duplicate/inherit links | reuse requirements across projects | Variant Management; Parameterized Requirements | Variants Management capability |
| Interchange | Word/Excel/ReqIF import; DOCX/XLSX/PDF/HTML/CSV/ReqIF export | Word export for stakeholders; import "in any number of formats" | Word Import (heading→hierarchy) + Smart Report round-trip | (not sampled) |
| Dev-toolchain integration | Jira Cloud, Azure DevOps, GitHub/GitLab/Bitbucket (via Git), Sparx EA | Jira (bidirectional links), Jenkins, P4, REST API | native inside Azure DevOps; inherits ADO permissions | ALM spans dev/test/ops |
| Deployment | desktop app + Git/SVN/shared drive/Google Drive | suite, on-prem/cloud | inside Azure DevOps Server/Services | self-hosted/cloud (codebeamer.com runs its own instance) |
| Audience span | HW/SW and systems engineers; medical/aerospace/automotive/rail | medical/defense/automotive/consumer; ISO 26262 | MedTech/defence/systems engineering/banking/energy/rail | medical/automotive/aviation/pharma |
| AI | AI-assisted import (service); INCOSE/EARS quality rules (contact-gated) | (not sampled) | 12 AI capabilities (elicitation, analysis, conversion, generation) | (not sampled) |

## Canonical Abstraction

### L0 — Defining Invariant

Four jointly-held structures, independently derived in this pass and identical to the §16 pass's independent derivation:

1. **The requirement of record** — a persistent, individually identified (stable unique ID), versioned statement of a capability, condition, or constraint the product must satisfy, carrying attributes (statement text, rationale, verification method, status, ownership; custom attributes configurable per process — ReqView Custom Attributes, MR4DevOps Custom ID). Remove → there is nothing to manage; the product becomes a document editor or a generic work-item tracker.
2. **Structured specification** — requirements held in a structured collection within a project: a hierarchy, a specification document, or a tree (ReqView requirements documents with sections; Perforce hierarchy "organize (and reorganize) in real-time"; MR4DevOps Smart Docs "document-style interface, complete with hierarchy"; decomposition across abstraction levels — Perforce "decompose marketing requirements into product requirements, system specifications, and functional requirements"). Remove → flat ticket list; the specification character disappears.
3. **Traceability links** — explicit, typed, directional, navigable links between requirements and to related artifacts (upstream needs, downstream design/tests/risks/source code), with coverage computed from the link graph (ReqView custom link types + suspect flags + live RTM; Perforce automatic traceability matrix; MR4DevOps Trace Analysis matrices + gap analytics). Remove → a requirements document processor; "management" collapses to authoring.
4. **Managed change** — version history per requirement, baselines as frozen snapshots, and controlled change with impact analysis (ReqView change management + Git baselines; Perforce baselines + impact analysis; MR4DevOps immutable Baselines + Difference Report + 360° Impact Assessment + suspect links). Remove → a static snapshot; the "management" in the Type name is gone.

Jointly-held is load-bearing:
- 1+2 without 3 = requirements document authoring (Word with numbering)
- 1+3 without 2 = a flat link database, not a specification
- 2+3 without 1 = structure with no stable records
- 3+4 without 1 = change machinery with nothing to change
- 1+4 without 3 = a versioned document store, not traceability-driven engineering

### L1 — Common Mature Structure

Present across the sample (and corroborated by the §16 pass's sample) but not definitional:

- Review/approval machinery: reviews with comments, reviewer/approver roles, approvals, e-signatures (Perforce reviews + approvals; MR4DevOps Review Management with e-signatures and mandatory rejection comments; ReqView Review Documents; §16 pass: Jama Review Center, Polarion e-signature gate, DOORS e-signatures)
- Test/V&V linkage: test cases linked to requirements, coverage views/matrices (Perforce test cases from requirements + results traced back; MR4DevOps Test Hub + coverage heatmaps; ReqView verification links; §16 pass 4/4)
- Reuse and variants: reusable requirements, linked/reused projects, variant configurations, parameterized requirements (ReqView linked projects + inherited links; Perforce reuse; MR4DevOps Variant Management + Parameterized Requirements)
- Interchange: Word/Excel import-export round trips (the legacy habitat), ReqIF exchange (ReqView both directions; MR4DevOps Word Import + report round-trip; Perforce Word export + multi-format import; §16 pass 4/4)
- Document generation and reporting: specification documents, traceability matrices, audit-ready reports generated from the live record (MR4DevOps Smart Report; ReqView exports; Perforce traceability matrix + reports)
- Dev-toolchain integrations: issue trackers (Jira), DevOps platforms (Azure DevOps), code platforms, CI (Jenkins), modeling tools (Sparx EA) — links flow both directions
- Dashboards/analytics: coverage status, gap analysis, progress (codebeamer dashboards Tier-1; MR4DevOps Trace Analysis analytics; ReqView project dashboard)
- Permissions/roles: who can see/edit/review/approve what (MR4DevOps inherits ADO permission model; reviewer/approver roles)
- Workflow engines: states, transitions, assignment/escalation rules (Perforce workflow engine; §16 pass: Jama workflows, Polarion workflow-enforced states)

### L2 — Variant / Optional Structure

- Risk/FMEA integration as first-class content (Perforce FMEA; ReqView FMEA template; §16 pass: Visure)
- Industry standards packs and compliance framing (MR4DevOps FDA/ISO/DO-178C/ASPICE/MIL-STD; ReqView ISO 29148/OWASP ASVS templates; §16 pass: Visure standards packs)
- Variant/configuration management depth (MR4DevOps Variant Management; §16 pass: IBM global configurations, Polarion branching)
- Deployment posture: desktop+Git self-hosted (ReqView), modular suite (Perforce), DevOps-platform-native (MR4DevOps), unified ALM (codebeamer); cloud vs on-prem vs air-gapped (§16 pass)
- Version-control substrate: Git/SVN as the versioning layer (ReqView) vs built-in versioning (others)
- Source-code traceability (Perforce; §16 pass: Visure, Polarion)
- AI assistance (MR4DevOps 12 capabilities; §16 pass: Visure Vivia, IBM AI) — era-current
- MBSE integration depth (ReqView↔EA export/import; §16 pass: Simulink/Cameo connectors)

### L3 — Vendor-specific Structure

(kept out of the final document)

- ReqView: JSON open file format; Traceability Column Wizard; origin/inherited-links copy semantics; floating license server; CLI for automated exports; Google Drive sharing
- Perforce: module-based suite economics ("start with one module"); automatic issue creation from failed test runs; Helix ALM brand lineage (TestTrack)
- Modern Requirements4DevOps: Smart Docs/Smart Report/Trace Analysis as named modules; AI Credits metering; Copilot4DevOps/Compliance4DevOps/Agents4DevOps companion products; AI Sync Bridge
- codebeamer: wiki-plugin dashboards; tracker concept; umbrella projects

## Historical / Market-Sample Check

- ReqView (vendor-stated "10+ years on the market", © 2013–2026) is a desktop + Git tool with no cloud-native machinery — it satisfies all four L0 legs. The lightweight desktop pole holds.
- The DevOps-native pole (MR4DevOps) satisfies the same four legs on top of Azure DevOps work items — the substrate (standalone repository vs DevOps platform) is not definitional.
- Perforce's own anti-spreadsheet framing ("Using spreadsheets to manage requirements is inefficient and can't give you the traceability you need") and the §16 pass's equivalent findings (Visure "version chaos in Word or Excel") confirm the market positions these tools as the industrialization of pre-tool document-and-spreadsheet practice — which satisfies a thin version of the same core (IDs, attributes, hand-maintained traceability matrices, change logs).
- The §16 pass already verified the classic DOORS generation (modules/links/baselines/e-signatures, no cloud/AI/ReqIF). Combined: no L0 element depends on the current dominant implementation.
- Conclusion: historical check passed; the core is era-independent and substrate-independent.

## Vendor-specific Findings

See L3. Additional notes:

- Perforce's "using Jira for requirements doesn't work" is vendor positioning, but it is direct market evidence for the issue-tracker boundary: the vendor sells RM as the complement to the issue tracker, with bidirectional links — not as a replacement of the tracker's own work-item role.
- MR4DevOps's "built directly within Azure DevOps" is a realization posture, not a different Type: the same four legs (Smart Docs structure, Trace Analysis links, Baselines, Review Management) are present; the substrate differs.
- codebeamer's unified work-item infrastructure (requirements/tests/tasks share common features) matches the §16 pass's Polarion finding — a philosophy difference within one Type, not a Type split.

## Boundary Findings

1. **vs Engineering Requirements Management (§16 sibling) — ALIAS RATIFIED.** This pass's independent sample (ReqView, Perforce ALM RM, MR4DevOps, codebeamer) reaches the identical four-leg core that the §16 pass derived from a disjoint sample (DOORS Next, Jama, Polarion, Visure). Every product in this pass's sample explicitly serves software AND systems/hardware/regulated engineering (ReqView "HW/SW and Systems Engineers"; Perforce ISO 26262 + medical/defense; MR4DevOps Systems Engineering/MedTech/Defence solutions; codebeamer medical/automotive/aviation/pharma). No product population answers to "requirements management platform" but not to "engineering requirements management", or vice versa. The §12/§16 split is industry positioning of one Type, not two Types. Resolution: the two leaves are one Application Type under two names; both documents stand cross-referenced (this one from the software-development angle, the sibling from the engineering-program angle); consolidation recommended at a taxonomy pass. (Precedent: questionnaire-application ≡ survey-platform.)
2. **vs Product Management Platform (§12, processed) — keep-both RATIFIED, seam = object + center of gravity.** The PM platform holds feature records for committed product work planned into releases (what/when, market-facing); this Type holds requirement records as the specification of record (how exactly, verifiable, traceable, baselined). The PM pass's "specs = handoff out of the PM platform" is exactly the seam: when a spec becomes managed requirement records with traceability and baselines, it has entered this Type. Vocabulary overlap ("requirements" in PM tools = prioritized feature demand) is not the requirement record.
3. **vs Product Roadmap Application (§12, processed) — keep-both CONFIRMED from this side.** The roadmap pass's open item ("no spec/requirement objects surfaced in any sampled roadmap core — plan lines express what/when, not how-exactly") is confirmed: this Type's defining objects (requirement records, typed links, baselines) never appear in roadmap cores. The how-exactly lives here.
4. **vs Issue Tracker (§12, processed) — consistent with that pass's removal test.** Issue trackers hold flat work-item populations with plan/execute lifecycles; this Type holds structured specifications with typed traceability and baselines. Perforce's own positioning ("using Jira for requirements doesn't work"; link requirements to Jira issues and vice versa) documents the complementarity from the market side. Requirements tracked as plain tickets lose the specification structure, typed links, and baselines — the §16 pass's "flat ticket list, issue-tracker shape" removal test.
5. **vs Engineering Project Management Platform (§12, processed) — seam RATIFIED from this side.** That pass's table entry ("formal requirement objects with baselines and regulated traceability; engineering PM work items are the lighter delivery-side counterpart") matches this pass's evidence; delivery-side work management and requirement specification remain distinct centers.
6. **vs MBSE Platform (§16, processed) — complementary pairing CONFIRMED from this side.** ReqView's EA integration ("export requirements to EA and import design models to ReqView… integrated MBSE solution") documents the record-first ↔ model-first seam from the RM side; consistent with the mbse-platform pass's ratification.
7. **vs Software Test Management (§12) — module bundling, not Type merger.** Test management appears as a module/domain inside several sampled products (Perforce test module, MR4DevOps Test Hub, codebeamer QA domain) — same pattern the §16 pass observed (Jama, Visure, Polarion).
8. **vs Medical Device Lifecycle Management (§22, processed) — consistent.** That pass held "a requirements tool covers one link class only"; this Type is exactly that requirements layer, which the device Type links into its design-control chain.

## Uncertainties

- codebeamer operational detail (tracker/requirements object mechanics, link types, baseline machinery) not verified — wiki requires login, intland.com transport error; claims held at homepage + help-center strength.
- Perforce documentation portal not fetched; Perforce claims held at product-page strength (positioning, capability areas, named features).
- MR4DevOps evidence is vendor-authored feature marketing (detailed but promotional); operational claims kept general; no third-party operational verification.
- Exact state vocabularies (requirement statuses, review states) vary by product and were not asserted.
- ReqView's review machinery depth (approval gates, e-signatures) not verified at article level — Review Documents page seen at map level only; held as common-mature at low strength.
- AI capabilities are era-current and evolving; treated as L2 throughout.

## Final Synthesis

Requirements Management Platform (§12) is the same Application Type as Engineering Requirements Management (§16): the development organization's system of record for the requirements a product must satisfy. Its defining core is exactly four jointly-held structures — the requirement of record (persistent, uniquely identified, versioned, attributed statement), the structured specification (hierarchy/document/tree within a project), traceability links (typed, directional, navigable, extending to needs/design/tests/risks/source code, with coverage computed from the link graph), and managed change (version history, baselines, controlled change with impact analysis). Everything else — review/approval with e-signatures, test linkage and coverage, reuse/variant machinery, Word/Excel/ReqIF interchange, document generation, dashboards, standards packs, risk integration, AI assistance — is common mature structure or variant capability. The Type is era-independent (desktop+Git pole, classic-tool generation, and pre-tool spreadsheet practice all satisfy the core), substrate-independent (standalone repository, modular ALM suite, DevOps-platform-native, and unified ALM all realize it), and industry-independent (the same products serve software, hardware, systems, and regulated-device engineering) — which is precisely why the §12/§16 directory split resolves as one Type under two names.
