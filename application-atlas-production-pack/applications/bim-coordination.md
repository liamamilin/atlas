# BIM Coordination

## Overview

A **BIM Coordination** application is the environment in which building models from multiple disciplines are brought together into one federated whole, examined for conflicts and inconsistencies, and driven to a coordinated state through tracked, model-anchored issues.

The defining structure is small:

```text
Models from several disciplines/authors
└── combined into one federated review context (each model keeping its origin)
    └── problems found in the combination (clashes, rule violations, data gaps)
        └── recorded as issues anchored to the model (viewpoint, linked elements)
            └── tracked resolution loop: assign → fix in the authoring tool
                → re-federate → re-check → verify → close, repeated per cycle
```

Everything commonly associated with modern coordination practice — clash-detection engines, standardized issue exchange (BCF), rules-based model checking, cloud platforms, dashboards, AI assistance — makes the work faster or more rigorous, but is not what makes the software a coordination tool. Early desktop federation tools satisfied the defining structure above with nothing more than model combination, clash tests, and tracked markups.

Two boundaries frame the Type. When models are created and edited rather than consumed, the work belongs to BIM Authoring. And when the tracked object is a schedule, a cost, a contractual question, or a site defect rather than a conflict inside the model, the work belongs to Construction Project Management, RFI Management, or Construction Quality Management respectively.

## Users & Context

The operating user is the **BIM coordinator or BIM/VDC manager** — the person responsible for making the disciplines' models fit together. Around them:

- **Discipline engineers and designers** (architecture, structure, MEP) — they receive issues against their models and resolve them in their authoring tools; they also run checks on their own models before submission.
- **Contractors' design and construction teams** — they coordinate constructability, run federated reviews ahead of installation planning, and rely on the coordinated model for sequencing and prefabrication.
- **Subcontractors and detailers** — they check their fabrication models against the design federation.
- **Project and owner representatives** — they consume progress visibility (open issues, resolution trends) rather than operating the checks.

The work is organized around **coordination cycles**: models are submitted at agreed milestones, federated and checked, issues are triaged and assigned in or ahead of coordination meetings, disciplines fix their models, and the cycle repeats until the federation is clean enough for the next stage gate. The context is project-wide and multi-company: the tool is typically the one place where all parties — often using different authoring software — look at the same combined model and the same issue list.

## Core Model

### The defining core

**1. The federated model context.** The software assembles models from multiple sources — different disciplines, different authors, different authoring tools — into one combined review context. Each source model keeps its identity: which discipline it comes from, which version it is, who submitted it. The combination is what makes coordination problems visible at all; many conflicts and gaps do not exist inside any single discipline model and appear only when models are reviewed together.

**2. Model-anchored issues.** A problem found in the federation is recorded as an issue: a persistent, trackable record that is anchored to the model — through a saved viewpoint (camera position, section, visibility state) and, in mature products, through links to the specific model objects involved. An issue carries an assignee, a status, a description, and a discussion thread. Issues are the coordination tool's own system of record: the federation shows where things conflict; the issue register tracks what is being done about it.

**3. The resolution loop.** An issue is not closed when it is filed. It is assigned to the responsible party, communicated out (through notifications, standardized issue exchange, or plugins that surface it inside the authoring tool), fixed by editing the discipline model where the model is actually authored, and then verified: the updated model is re-federated, the check is re-run, and the issue is confirmed resolved before it is closed. The loop runs repeatedly — per coordination cycle, per model submission — for as long as the models evolve.

### Standard capabilities of mature products

Most current coordination products carry the following. They make the workflow efficient and rigorous, but a product can be genuine coordination software without every one of them:

- **Clash detection** — computing spatial conflicts between elements of different models: hard intersections, clearance violations, and related conflict types; with classification, grouping of related results, and prioritization so that large result sets become workable issue lists.
- **Rules-based model checking** — validation beyond geometry: naming conventions, classification systems, missing or inconsistent element data, and project-defined information requirements. In standards-driven projects this is formalized through information-delivery specifications checked against the models.
- **Issue workflow machinery** — assignment, deadlines, discussion threads, status tracking, and a complete audit trail of every change; some products add configurable approval gates before an issue may be closed, or mandatory fields that must be filled before it can be saved.
- **Authoring-tool integration** — plugins and issue-exchange managers that make the issue list visible and actionable inside the BIM software where the fix happens; clicking an issue in the authoring tool zooms to its position in the model.
- **Open exchange standards** — IFC for model exchange, BCF for issue exchange between different tools and parties, IDS-style specifications for information requirements.
- **Re-verification across model versions** — recognizing previously reported problems in newly submitted model versions, updating their status automatically, and distinguishing genuinely new findings from already-reported ones — including when several coordinators check models concurrently.
- **Progress reporting** — dashboards and reports over open issues, resolution progress, aging, and per-discipline workload, used to run coordination meetings and stage gates.
- **Stakeholder viewers** — browser and mobile access to the federated model and its issues for people who do not operate the checking tools.
- **2D drawings alongside 3D models** — drawings and models reviewed in one environment, with issues placeable on either.

### One core, several realizations

The defining core is stable, but the market realizes it through visibly different philosophies, and understanding them explains most product differences:

```text
Concept:              Where checking happens
Realizations:         a dedicated validation checker fed by exchanged models;
                      a cloud issue hub fed by plugins from many authoring tools;
                      a collaboration hub unifying models, drawings and issues;
                      a lightweight viewer whose comments carry the issue loop

Concept:              Where the clash engine lives
Realizations:         built into the coordination tool;
                      run in companion checking tools and imported;
                      run inside the authoring tools and exchanged as issues

Concept:              Where the platform sits
Realizations:         standalone coordination product;
                      module of a construction platform family;
                      capability embedded in a common data environment
```

No single realization is the definition. What all of them share is the federated context, the model-anchored issue, and the loop that ends only when the updated federation verifies the fix.

## How It Works

A coordination cycle typically moves through the following steps — repeated for each model submission or project milestone:

**1. Collect the discipline models.**
Models arrive from each party — uploaded through plugins from the authoring tools, exchanged as IFC, or pulled from a common data environment. Each arrival is a versioned submission tied to a discipline and a milestone.

**2. Federate.**
The models are combined into one spatially aligned review context. The federation preserves origins: any element can be traced back to its source model, discipline, and version.

**3. Check.**
Clash tests and rule checks run against the federation — spatial conflicts between disciplines, clearance violations, missing openings, inconsistent or missing information, classification and naming problems. Results are grouped and prioritized; not every raw finding becomes an issue.

**4. Triage and create issues.**
The coordinator reviews the findings, discards noise, groups related problems, and raises issues — each anchored to a viewpoint and the involved objects, assigned to the responsible party, with priority and deadline.

**5. Communicate.**
Issues reach the responsible disciplines through notifications, reports for coordination meetings, standardized issue exchange, or plugins that show the issue list inside the authoring tools. The fixes are made in the authoring tools — the coordination tool never edits the building elements themselves.

**6. Re-federate and verify.**
Updated models are submitted; the federation is rebuilt; checks re-run. Previously reported problems are recognized and their status updated — resolved issues are verified against the new federation and closed (sometimes through an approval gate); unresolved ones stay open and age.

**7. Report and gate.**
Dashboards and reports summarize open issues, resolution progress, and per-discipline workload. When the federation reaches the agreed quality level, the milestone is signed off and the coordinated model moves downstream — to construction planning, fabrication, or handover.

### What is core, common, and optional

- **Defining core** — federated multi-source model context; model-anchored issue records; tracked resolution loop with re-verification.
- **Common mature structure** — clash detection, rules-based checking, issue workflow machinery, authoring-tool integration, IFC/BCF/IDS exchange, version re-verification, progress reporting, stakeholder viewers, 2D+3D context.
- **Variant or optional** — governance depth (execution-plan enforcement, information-requirement checking, permit workflows), field/site integration, schedule linkage, information takeoffs, sovereign or air-gapped deployment, AI assistance, CDE and construction-management integrations.

## Interfaces

The following surfaces are described conceptually; exact names and layouts vary by product.

### Federated 3D viewer

The spatial working surface.

- the combined model — orbit, isolate by discipline or selection, section/cut, measure, inspect element properties and source model
- clash results and issue markers visualized in context
- primary actions: navigate the federation, inspect a finding, create an issue from a selection or viewpoint

### Issue list / board

The register's working surface.

- filterable list of issues by status, assignee, discipline, priority, age, model version
- primary actions: create, assign, reassign, change status, set deadlines, filter and sort, export

### Issue detail

The single issue's surface.

- saved viewpoint, linked model objects, screenshots/markups, description, comment thread, status history, approval state
- primary actions: comment, update status, approve/close, link related issues

### Check setup

How detection is configured.

- clash tests: which model pairs or groups, which conflict types, tolerances, grouping rules; rule sets and requirement specifications for data checking
- primary actions: define/run tests and rule sets, review results, convert findings into issues

### Dashboards / reports

The management surface.

- open-issue counts, resolution progress, aging, per-discipline workload, trend over cycles
- primary actions: review progress in coordination meetings, export reports, drill into issue groups

### Administration

Project-level configuration.

- projects, teams, user groups, roles and permissions, custom/mandatory issue fields, approval workflows, exchange/integration settings
- primary actions: onboard parties, configure workflows, manage access

### Authoring-tool plugin surface

The loop's other end, inside the BIM software.

- the shared issue list visible in the authoring tool; click-to-zoom to the issue's position
- primary actions: read issues against one's own model, update status, push model updates

## Important Rules / Behaviors

### The coordination tool does not edit the model

Fixes happen in the authoring tools. The coordination tool's leverage is the federation, the checks, and the issue loop — its authority ends where element editing begins. This division of labor is what keeps authorship and accountability clear across companies.

### Issues must survive model changes

An issue anchored to a viewpoint and objects has to remain meaningful when the next model version arrives: the same conflict, re-found in new geometry, must be recognized as the same issue — updated, not duplicated. And because several coordinators may check models concurrently, duplicate reporting is a standing hazard; some products add explicit mechanisms that recognize already-reported clashes across checkers and test configurations.

### Not every clash is a problem

Raw clash results include intended connections, tolerable proximities, and false positives from imprecise models. Triage — classifying, grouping, prioritizing, and discarding — is a structural part of the workflow, not an optional refinement; unfiltered clash counts are not a measure of coordination quality.

### Closure is verified, not declared

An issue is closed because the updated federation demonstrates the fix — the check no longer finds the problem — sometimes with a second person's approval before closure. The audit trail of who changed what, when, is part of the deliverable, since coordination records are relied on in disputes and handover.

### Exchange fidelity is a structural risk

Issues and models travel between different tools and companies. An issue that loses its viewpoint or object links on the way to another tool becomes unactionable; a model that loses element identity degrades the checks. Round-trips are verified rather than trusted, and the open exchange standards exist precisely to bound this risk.

### Exceptions the workflow must absorb

- **Late or missing submissions** — a discipline's model does not arrive; the federation is checked without it and the gap itself becomes an issue.
- **Cross-version drift** — a fix in one discipline reopens or creates conflicts in another; the cycle repeats.
- **Non-modeled scope** — parts of the work exist only in drawings or outside the models; coordination falls back on 2D context and recorded assumptions.
- **Disputes about responsibility** — an issue assigned across party boundaries may be rejected or reassigned; the register records the negotiation.

## Variants

- **Validation-first checker** — a desktop checking environment centered on rule-based validation and clash detection, feeding issues to the parties; typical where model quality assurance is formalized (enterprise and public-mandate contexts).
- **Issue-centric cloud hub** — a cloud platform whose center is the shared issue register, connected to many authoring tools through plugins and open exchange; typical for multi-company projects with heterogeneous software.
- **Collaboration hub** — a broader platform unifying models, drawings, issues, and analytics for all project roles, including field teams and owners.
- **Viewer-plus-comments entry tier** — a free or lightweight federated viewer whose comment machinery (responsible person, status, audit trail) carries a lightweight coordination loop; typical as an adoption on-ramp or small-project tool.
- **CDE-embedded coordination** — coordination capability living inside a common data environment alongside document management, rather than as a standalone product.
- **Governance-heavy coordination** — the same Type tuned by regional/public-client requirements: information-delivery specifications, permit workflows, audit-ready validation.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| BIM Authoring | upstream sibling | authors the data-rich element models; coordination consumes models authored elsewhere to find and resolve cross-discipline conflicts — it does not create or edit elements. In-authoring clash checks are a convenience layer, not this Type |
| Construction Project Management | adjacent | centers on schedule, cost, procurement, contracts; coordination centers on the model and its conflicts. Integration exists; the tracked object differs |
| RFI Management | adjacent | formal contractual questions between parties about design intent; coordination issues are model problems with technical resolution, not contractual correspondence |
| Construction Quality Management / Punch List | adjacent, later stage | site-stage defects against constructed work; coordination issues are design-stage conflicts between models. Products often split these into separate modules |
| Construction Reality Capture Platform | data source | captures and processes scans; scans may enter coordination as context, which does not merge the Types |
| Digital Twin Platform / Facility Management | downstream | operates the asset over its life; coordination may hand over validated models toward it |
| Generic BIM Viewer | capability sibling | a viewer without a persistent issue register and resolution loop is not coordination; viewing alone is not enough |

The most consequential boundary is with **BIM Authoring**: the two Types share the model as their material, and authoring suites increasingly embed review surfaces. The structural test is what the software owns — the authoring tool owns the elements and their data; the coordination tool owns the federation, the checks, and the issues that drive the models to a coordinated state.

## Representative Products

- **Solibri** — validation-first model checker: federated review, rule-based checking, clash detection, and issue management under an explicit "BIM coordination" umbrella
- **BIMcollab** — issue-centric cloud platform built on IFC/BCF/IDS, with companion model-checking and clash-management tools and authoring-tool plugins
- **Revizto** — collaboration hub unifying 2D drawings, 3D models, clash automation, and issue management for all project roles
- **Dalux BIM Viewer** — free federated viewer whose comment machinery (responsible person, audit trail, clash import) carries a lightweight coordination loop
- **Trimble Connect** — coordination and issue workflows embedded in a cloud common data environment
- Autodesk **Navisworks** — the classic desktop federation/clash tool and historical category anchor, listed for market completeness (its documentation could not be reviewed in this research pass; see Sources)

## Sources

Research date: **2026-09-06**

- Solibri — homepage and BIM Coordination solution page: https://www.solibri.com/ , https://www.solibri.com/solutions/building-lifecycle/bim-coordination
- BIMcollab — platform, BIM Coordination (Nexus), issue management, and clash management pages: https://www.bimcollab.com/en/ , https://www.bimcollab.com/en/products/bimcollab-nexus/ , https://www.bimcollab.com/en/products/bimcollab-nexus/issue-management/ , https://www.bimcollab.com/en/products/bimcollab-zoom/clash-management
- Revizto — homepage and product pages: https://revizto.com/en/
- Dalux — BIM Viewer product page: https://www.dalux.com/products/bim-viewer/
- Trimble — Trimble Connect product page: https://connect.trimble.com/en/products/clash-detection
- buildingSMART International — openBIM overview (IFC / BCF / IDS definitions): https://www.buildingsmart.org/about/openbim/

> Sourcing limitation: Autodesk's domains for Navisworks returned 403 on 2026-09-06 (consistent with the same-day BIM Authoring and Architecture Design Application passes) and were abandoned per source-access rules; Navisworks is therefore not characterized in this document, and no claims are made about it. No Tier-1 operational help documentation was fetched for any sampled product in this pass — product evidence rests on official product and solution pages plus the buildingSMART standards pages. Accordingly, no precise operational details (exact issue-status vocabularies, exact clash-test configuration, exact format-version support, numeric limits) are asserted in this document; such detail as was recorded remains in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical / market-sample breadth check are recorded in the paired Research Notes.
