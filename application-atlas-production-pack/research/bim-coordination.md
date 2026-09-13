# Research Notes — BIM Coordination

## Research Goal

Understand, from real products, what the software category that coordinates Building Information Models across disciplines actually consists of: what the central managed artifact is (federated model? issue? check result?), what the core workflow is (federation → detection → issue → resolution → re-verification), how issues travel between tools and parties, and where the boundary lies with neighboring Types (BIM Authoring, Construction Project Management, RFI Management, Construction Quality Management, generic BIM viewers).

This pass is the downstream counterpart of the same-day BIM Authoring pass, which explicitly assigned the "federate models authored elsewhere to detect/resolve cross-discipline conflicts and manage issues" work to this Type and recorded the removal test: remove authoring → BIM Coordination; add authoring → BIM Authoring.

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: combining discipline models into one federated review context, finding conflicts and model problems, and driving them to resolution through tracked issues.
- Primary users: BIM/VDC managers and coordinators, discipline engineers, contractors' design teams.
- Nearest neighbors: BIM Authoring (17 — upstream), Construction Project Management, RFI Management, Submittal Management, Construction Quality Management / Punch List, Construction Reality Capture, Digital Twin, generic BIM viewers.
- Unknowns: whether clash detection is definitional or just the canonical mechanism; whether the issue register or the federation is the true center; whether "model checking" (rules/data validation) belongs here or is a separate Type; how issues survive model version changes.

## Research Questions

1. What is the central persistent artifact — the federated model, the issue register, or the check results?
2. What exactly is a "clash" in products, and what other problem kinds do coordination tools find (rule violations, data gaps, classification errors)?
3. How do models arrive (IFC, native formats, plugins, live links), and how is federation performed?
4. What is the issue lifecycle: creation, assignment, status, approval, closure — and how do issues reference the model (viewpoints, element links)?
5. How do issues travel between the coordination tool and authoring tools (BCF, plugins, APIs)?
6. What happens when new model versions arrive — how are issues re-verified, updated, or closed?
7. Who uses the tool and in what meeting/cycle rhythm (coordination meetings, milestones)?
8. What governance machinery exists (BIM execution plans, information requirements/IDS, audit trails)?
9. What distinguishes this Type from BIM Authoring, Construction Project Management, RFI Management, quality/punch-list tools, and plain BIM viewers?

## Representative Products

Selection rationale: market representativeness + different product philosophies + different customer tiers + documentation accessibility. Autodesk Navisworks — the classic desktop federation/clash tool and historical category anchor — was intended as a sample but remained unreachable (403, consistent with the same-day BIM Authoring and Architecture passes); it is retained for market anchoring only, with no claims.

| Product | Philosophy / tier | Evidence tier reached |
|---|---|---|
| Solibri (Nemetschek) | validation-first model checker: federation review, rule-based checking, clash detection, issue management, governance | Tier 2 (official homepage + dedicated BIM Coordination solution page) |
| BIMcollab (KUBUS/Nemetschek) | issue-centric cloud platform built on open standards (IFC/BCF/IDS); model checking in companion desktop app (Zoom); BCF Manager plugins | Tier 2 (official platform, Nexus, issue-management, Zoom clash-management pages) |
| Revizto | collaboration hub: unified 2D/3D environment, collaborative clash automation, integrated issue management, dashboards | Tier 2 (official homepage/product pages) |
| Dalux BIM Viewer | free viewer-centric coordination: plugin-based federation, comments with responsible person + audit trail, clash import from Solibri/Navisworks | Tier 2 (official product page) |
| Trimble Connect | CDE-embedded collaboration: comments on files/tasks/3D models, versioned data packages, connected issue workflows | Tier 2 (official product page; coordination detail thin) |
| buildingSMART International | standards body — IFC/BCF/IDS definitions used for concept/boundary evidence | Tier 1 (carried over from same-day BIM Authoring pass) |

## Sources

Fetched 2026-09-06 (this pass):

- Solibri — homepage: https://www.solibri.com/
- Solibri — BIM Coordination solution page: https://www.solibri.com/solutions/building-lifecycle/bim-coordination
- BIMcollab — homepage: https://www.bimcollab.com/en/
- BIMcollab — BIM Coordination (Nexus) product page: https://www.bimcollab.com/en/products/bimcollab-nexus/
- BIMcollab — Issue management page: https://www.bimcollab.com/en/products/bimcollab-nexus/issue-management/
- BIMcollab — Clash management / Smart Issues page: https://www.bimcollab.com/en/products/bimcollab-zoom/clash-management
- Revizto — homepage: https://revizto.com/en/
- Dalux — BIM Viewer product page: https://www.dalux.com/products/bim-viewer/ (fetched via /products/bim/ redirect)
- Trimble — Trimble Connect product page: https://connect.trimble.com/en/products/clash-detection (redirects to the Trimble Connect overview; coordination detail thin)

Carried over from same-day BIM Authoring pass (2026-09-06, evidence re-usable):

- buildingSMART International — openBIM overview (IFC / IDS / BCF definitions): https://www.buildingsmart.org/about/openbim/

Unreachable / abandoned:

- Autodesk Navisworks: autodesk.com returned 403 (attempted 2026-09-06; same result in the BIM Authoring and Architecture passes). Abandoned per source-access rules. **No operational or feature claims about Navisworks are made anywhere in this research or in the final document.**
- Dalux /products/bim-coordination/ returned 404; the BIM Viewer page was used instead (Dalux's coordination capability is presented through the BIM Viewer + comments + clash import).
- No Tier-1 operational help documentation was fetched for any sampled product in this pass (help centers exist — help.solibri.com, helpcenter.bimcollab.com, help.revizto.com, support.dalux.com — but were not fetched; product evidence rests on official product/solution pages).

Implication: all cross-product claims below rest on five reachable products (official product/solution pages) plus the standards body. The final document therefore avoids operational precision (exact status vocabularies, exact tolerance mechanics, exact format-version support, numeric limits).

## Product Observations

### Solibri (evidence layer A — official homepage + BIM Coordination solution page)

- Self-description of the stage: "BIM coordination is the stage where discipline models are combined into federated project models and reviewed together."
- Users named: architects, structural engineers, MEP designers, contractors, BIM managers.
- Purpose: "verify that systems fit together, installation space is available, and model information is consistent across disciplines."
- Problem kinds found: "Clearance issues, system conflicts, missing openings, incorrect positioning, and inconsistent model information often only appear when models are combined and reviewed in context." Also: "Geometric conflicts, Information inconsistencies, Classification misalignment, Compliance gaps."
- Clash detection framing: "Clash detection is one of the most recognized parts of BIM coordination because it turns federated model review into actionable issue identification." And: "Effective clash detection is not only about finding intersections. Teams must classify clashes, prioritize critical issues, group related problems, and track issue resolution across coordination cycles."
- FAQ boundary statement: "Clash detection is part of BIM coordination. BIM coordination includes federated model review, clash detection, issue management, and model validation workflows."
- Governance layer: "validating model information to ensure models meet project standards, naming conventions, classification systems, and information requirements defined in BIM execution plans or Information Delivery Specifications"; connects to IDS workflows, digital building permits, data validation.
- Lifecycle framing: coordination connects design models with construction-ready models; coordinated models then support installation planning, scheduling, prefabrication.
- Product tiers: Starter (model review, basic validation) → Essential (clash detection, everyday coordination) → Advanced (rule-based validation, coordination governance) → Premium (enterprise) → Security+ (air-gapped/restricted environments).
- Marketing statistics (not used as structural evidence): "2.1 billion model issues" resolved by users in 2025, "over 1 billion clashes".

### BIMcollab (evidence layer A — official platform/Nexus/issue-management/Zoom pages)

- Platform structure: BIM Coordination (Nexus: issue management, IDS, BCF Managers) + Model Checking (Zoom: clash management, smart properties, smart views, lists) + Document Management (Twin).
- Boundary statement: "BIM coordination entails far more than just clash management. It's about clear requirements, efficient communication, and establishing a single source of truth for all project data."
- Standards posture: "Built on the widely accepted IFC, BCF, and IDS open standards by buildingSMART… centralizing BIM requirements, model coordination, issue management, information takeoffs, and progress intelligence in the cloud."
- Issue anchoring: "Issues are linked to positions and objects in your model and accessible via web browsers or directly from your BIM software. Imagine clicking an issue in your own BIM tool and being zoomed to its position right away."
- Issue workflow machinery: custom and mandatory fields; teams and user groups ("define to whom one can assign issues to, or who can see your confidential issues"); project/area owners; "define who needs to approve issues before they can be closed"; deadlines; comments and viewpoints; email notifications; daily/weekly activity digests.
- Audit and reporting: "complete and transparent audit trail"; issue reports and activity lists in PDF/XLS; Power BI connection; progress graphs.
- Federation: streaming WebViewer "opens and federates even the largest IFC models in seconds, right in your browser"; plugins/BCF Managers into BIM software; direct integrations with Autodesk Docs and Trimble Connect.
- Smart Issues (clash management): "know the clashes or conflicts they represent, to which objects they belong and why and when they are reported or solved"; "prevent the overhead caused by redundant clash-reporting, even by other team members doing concurrent model checking"; clash status "reported, ignored or new"; "When you receive new model versions, Smart Issues can be automatically checked, updated, and closed with a single command."
- Requirements checking: define project BIM requirements with IDS; "automatically check models for compliance with BIMcollab Zoom, catching issues early."
- Customer evidence: AECOM managing "100.000 issues and clashes" across teams in various BIM software; Zaha Hadid on creating/discussing/documenting issues; Tyréns BIM coordinator on stakeholder usability.
- Security posture: ISO 27001, GDPR, data hosted in the Netherlands.

### Revizto (evidence layer A — official homepage/product pages)

- Positioning: "One platform for project coordination"; "The leading 2D/3D platform to deliver complex projects."
- Unified 2D/3D environment: "All drawings and models in one view" — 2D/3D overlay, split view, advanced search, AR/VR/QR, appearance profiler.
- Collaborative clash automation: "Multiple Clash Types, Dynamic Groupings, Interactive Visual Analysis, Advanced Automations."
- Integrated issue management: "Create, track, and manage issues in 2D or 3D. From any device. Synced to its exact spatial location" — 2D/3D markups, location data, stamp & issue workflows, issue automations.
- Connected project intelligence: interactive dashboards & reports, model data extraction, issue API.
- Audience by role: BIM/VDC managers ("Automate coordination and drive model accuracy"), engineers ("Deliver constructible, clash-free designs"), field teams, project managers, owners ("Real-time visibility across the entire project").
- Customer evidence: Bouygues UK regional BIM manager — "consolidating issue management into a single location. This includes design team meeting actions, clash detection, design queries and coordination issues – from builders work to fire stopping." Stantec hyperscale data centers; KiwiRail rail-corridor coordination; Rosendin electrical detailing.
- Integrations: 100+ plugins/formats/partners/CDE integrations (Revit, Navisworks, Rhino, SharePoint, Procore, OpenSpace, FARO…); API; MCP server.

### Dalux BIM Viewer (evidence layer A — official product page)

- Positioning: free BIM viewer — "Combine all discipline models and drawings, and share it with your team on desktop or mobile."
- Federation via plugins: "the only free tool that comes with plugins to Revit, Navisworks, Tekla, ArchiCAD, and more. Quick and easy to upload and federate your BIM models"; "Upload native BIM and drawings together"; "Automatic federation."
- Viewing machinery: native BIM + IFC + drawings; 2D/3D side by side; sections/cuts; measure; filter by model or element properties; save views; element properties.
- Communication: "Import clashes from Solibri or Navisworks for a better way of working. All comments have a responsible person and an audit trail. Quickly raise, respond, track, and close-out any comments the project team may have." Solibri live connector; comments in plugins; clash-test import from Navisworks.
- Escalation path: comments/tasks mature into the paid Dalux Field (on-site quality/safety) and Dalux Box (document/model management) products — coordination sits at the free/entry end of a construction platform family.

### Trimble Connect (evidence layer A — official product page; thin)

- Positioning: "cloud-based common data environment (CDE) and collaboration solution, designed for geospatial and construction professionals."
- Collaboration machinery: "Add comments to files, tasks, and 3D models, share versioned data packages for review, classify information with tags, and establish connected issue management workflows across Trimble and external applications."
- Observation: coordination capability exists inside a CDE/data-hub product rather than as a standalone checker; clash detection is part of the platform's feature set but was not detailed on the fetched page. Treated as a secondary observation (CDE-embedded coordination posture).

### buildingSMART International (evidence layer A — carried over from BIM Authoring pass)

- IFC: standardized digital descriptions of the built asset (model exchange).
- BCF: "Standard communication protocol for efficient issue management and coordination on BIM projects."
- IDS: "Standard for defining and checking information requirements in a computer interpretable form to ensure data quality."
- Relevance: BCF exists precisely because issue exchange between different tools/parties is a distinct coordination need; IDS extends coordination from geometry to information requirements.

## Cross-product Comparison

| Dimension | Solibri | BIMcollab | Revizto | Dalux BIM Viewer | Trimble Connect |
|---|---|---|---|---|---|
| Central artifact | federated model + rule-check results + issues | cloud issue register linked to model objects | unified 2D/3D project space with issues synced to spatial location | federated model view + comments | CDE files/models + comments/tasks |
| Federation | multi-discipline federated review (stated) | streaming WebViewer federates IFC models in browser; plugins | models + drawings ingested into one environment (280TB claim) | plugins upload + "automatic federation" | versioned data packages in CDE |
| Clash detection | yes — "most recognized part"; classify/prioritize/group | yes — Zoom clash management; Smart Issues dedupe | yes — "Collaborative Clash Automation", multiple clash types, dynamic groupings | no native engine — imports clash tests from Solibri/Navisworks | present in platform (not detailed on fetched page) |
| Beyond-clash checking | rule-based validation: data, classification, compliance gaps; IDS/BEP governance | IDS requirement checking via Zoom; smart views/lists | model data extraction; issue automations | — | — |
| Issue anchoring | issues from checks, tracked across coordination cycles | issues linked to positions and objects; click-to-zoom in own BIM tool | issues synced to exact spatial location, 2D or 3D | comments with responsible person + audit trail | comments on files/tasks/3D models |
| Resolution loop | "track issue resolution across coordination cycles"; verify before construction | assign → deadline → comments → approval before close; auto re-check on new model versions (Smart Issues) | issue workflows + automations; status visible in dashboards | raise → respond → track → close-out | connected issue workflows across applications |
| Exchange standards | IDS workflows; integrations with CDEs/issue platforms | IFC + BCF + IDS explicitly; BCF Managers/plugins | 100+ integrations; API; issue API | IFC + native; Solibri live connector; Navisworks clash import | integrations with Trimble + external apps |
| Reporting | governance/validation reporting | progress graphs, PDF/XLS reports, Power BI | interactive dashboards & reports, issue API | comment status tracking via web | — |
| Audience | BIM managers, engineers, contractors; enterprise tiers | BIM coordinators/managers; design + construction teams | BIM/VDC managers, engineers, GCs, subs, owners | whole project team (free entry) | construction + geospatial teams |
| Deployment | desktop tiers + Security+ air-gapped | cloud (NL-hosted, ISO 27001) | cloud + enterprise security/sovereignty | cloud free tier + platform family | cloud CDE |

## Canonical Abstraction (L0–L3)

### L0 — Defining Invariant

The smallest structure without which the product is no longer recognizable as BIM coordination:

1. **Federated multi-source model context** — the software assembles models from multiple disciplines/authors into one combined review context, preserving each model's origin (which discipline, which version). Coordination problems are, by definition, problems between models; without federation the product is a single-model viewer or an authoring tool.
2. **Model-anchored issue records** — a persistent register of problems found in the combined model (spatial conflicts, rule violations, missing or inconsistent information), each located against the model (viewpoint and/or linked elements) and carrying an assignee and a status. Without the register, the product is a viewer.
3. **Tracked resolution loop across model versions** — issues are communicated to the responsible parties, fixes are made in the authoring tools, updated models are re-federated and re-checked, and issues are verified resolved before closure; the cycle repeats as models evolve. Without the loop, the product is a static clash report.

Removal tests:

- Remove (1) → single-model review inside an authoring tool (BIM Authoring's convenience checks) or a generic viewer. Not coordination.
- Remove (2) → a measurement/viewing tool. Not coordination.
- Remove (3) → a one-shot clash report. Not coordination.

Historical / market-sample check (§24): early-2000s desktop federation tools (the Navisworks lineage) combined discipline models, ran clash tests, and tracked markups/issues to resolution — satisfying all three invariants without BCF, without cloud hosting, without rules engines, and without IDS. Solibri's early rule-checking model fits the same invariants with rules instead of clashes as the primary detector. Conversely, an authoring tool's built-in clash check fails (1) (single model), a plain IFC viewer fails (2) and (3), and a static clash-report spreadsheet fails (1) and (3) — all correctly excluded. The invariant does not encode BCF exchange, cloud platforms, rules libraries, IDS, dashboards, or AI; those are maturity layers.

### L1 — Common Mature Structure

Present across essentially all reachable products (evidence layers A/B):

- **Clash detection** — computing spatial conflicts between elements of different discipline models (hard intersections, clearance violations); with classification, grouping, and prioritization of results (Solibri, BIMcollab Zoom, Revizto; Dalux imports clash tests from the others — the capability is universal even where the engine is not).
- **Issue workflow machinery** — assignment to a responsible party, deadlines, comments/discussion, status tracking, and (in some products) approval before closure; audit trail of every change (BIMcollab, Dalux, Revizto, Solibri).
- **Model anchoring of issues** — viewpoints, screenshots/markups, and links to the specific model objects involved; click-to-zoom from an issue into the model (BIMcollab, Revizto, Dalux).
- **Authoring-tool integration** — plugins/BCF Managers that surface issues inside the BIM software where the fix happens (BIMcollab BCF Managers, Dalux plugins, Revizto plugins, Solibri integrations).
- **Open exchange standards** — IFC for models, BCF for issues, IDS for information requirements (BIMcollab explicitly; buildingSMART definitions; Solibri IDS workflows).
- **Re-verification on new model versions** — re-running checks against updated federations and updating issue status accordingly, including automatic recognition of already-reported clashes (BIMcollab Smart Issues; Solibri "coordination cycles").
- **Progress reporting** — dashboards/graphs/reports over issue counts, status, aging, per-discipline workload (BIMcollab, Revizto, Solibri).
- **Multi-user, multi-party access** — web/mobile viewers so non-specialist stakeholders can view the federation and issues (BIMcollab WebViewer, Dalux, Revizto).
- **2D drawings alongside 3D models** (Revizto unified 2D/3D; Dalux native BIM + drawings).

### L2 — Variant / Optional Structure

Depends on segment, region, deployment, governance regime:

- **Platform philosophy** — desktop validation checker (Solibri), cloud issue hub (BIMcollab), collaboration hub (Revizto), free viewer + comments (Dalux), CDE-embedded (Trimble Connect), classic desktop federation/clash (the Navisworks lineage — market anchor).
- **Governance depth** — BIM execution plan enforcement, information-requirement checking (IDS), classification/naming validation, digital-building-permit support, audit-ready validation (Solibri, BIMcollab).
- **Beyond-geometry checking breadth** — accessibility, fire stopping, point-cloud checking, compliance rulesets (Solibri solution pages); region/code-dependent.
- **Field integration** — site tasks/snagging connected to model issues (Dalux Field; Revizto field teams); coordination-to-construction handoff.
- **4D/schedule linkage, information takeoffs** (BIMcollab information takeoffs; Revizto project intelligence).
- **Security/deployment posture** — sovereign/regional hosting, ISO 27001/GDPR posture, air-gapped deployment (Solibri Security+, BIMcollab NL hosting, Revizto data sovereignty).
- **AI/automation** — AI-powered checking assistant (Solibri), issue automations (Revizto), automated clash grouping.
- **Ecosystem integrations** — CDEs (Autodesk Docs, SharePoint, Trimble Connect), construction management (Procore), reality capture (FARO, OpenSpace).

### L3 — Vendor-specific

- BIMcollab: Smart Issues (clash-aware issue objects with automatic re-check), BCF Managers, MQA, Zoom Smart Views/Lists, approval-before-close as a configurable feature, NL hosting.
- Solibri: tiered offerings (Starter→Security+), rule-based validation libraries, Autorun, WebChecker, AI-powered assistant, "2.1 billion issues" marketing statistics.
- Revizto: unified 2D/3D environment, stamp & issue workflows, MCP server, issue API, ROI calculator.
- Dalux: free BIM Viewer tier, Solibri live connector, Navisworks clash-test import, Field/Box/FM platform family.
- Trimble Connect: data packages, tags, Trimble Construction One bundling.
- Autodesk Navisworks: unverified — nothing recorded (unreachable in three same-day passes).

## Vendor-specific Findings

(see L3; none promoted into the canonical core. Notably: Smart Issues-style automatic clash-to-issue deduplication is single-product in the reachable sample; approval-before-close is presented as a distinctive configurable feature by one product; free-viewer entry tier is one product's go-to-market.)

## Rejected Findings

- **"BIM Coordination = clash detection"** — rejected as definition. Evidence: Solibri's own FAQ ("Clash detection is part of BIM coordination"); BIMcollab ("far more than just clash management"); issue management and model validation are co-equal centers. Clash detection is the canonical detector, not the definition.
- **"BIM Coordination requires a built-in clash engine"** — rejected: Dalux coordinates with imported clash tests from other tools; BIMcollab's issue hub can operate on issues raised in authoring tools. The engine is common (L1), not definitional.
- **"BCF exchange is definitional"** — rejected: pre-BCF desktop tools coordinated via proprietary markups/reports; BCF is the current standard realization (L1), not the invariant.
- **"Coordination happens only in a dedicated tool"** — rejected: coordination surfaces exist inside CDEs (Trimble Connect) and construction platforms (Dalux family); the posture varies (L2).
- **"Model checking / validation is a separate Type"** — rejected for now: in the reachable market, rule-based checking is embedded in coordination products (Solibri's whole solution page sits under "BIM Coordination"; BIMcollab ships IDS checking inside the coordination platform). Recorded as a boundary uncertainty rather than a taxonomy split.
- **"Coordination issues are the same object as RFIs or punch-list items"** — rejected: different anchor (model conflict vs contractual question vs site defect), different stage, different parties; products may integrate them, which does not merge the Types.
- **"Owners/architects are the primary users"** — rejected: the operating user is the BIM/VDC coordinator or manager; discipline engineers and contractors participate; owners consume visibility (Revizto role pages; Solibri user list).

## Boundary Findings

- **vs BIM Authoring (17) — the upstream sibling, examined jointly with the same-day BIM Authoring pass.** Coordination federates models *authored elsewhere* to detect/resolve cross-discipline conflicts and manage issues; it does not create or edit building elements. Removal test: remove authoring → BIM Coordination; add authoring → BIM Authoring. In-authoring clash checks (ALLPLAN, Archicad — recorded in the BIM Authoring pass) are a convenience layer, not this Type, because they lack the federated multi-source context. The boundary is soft at the edges: authoring suites embed review/checking surfaces, and coordination tools can display model data richly — but the system-of-record question separates them (the authoring tool owns the elements; the coordination tool owns the issues and the federation).
- **vs Construction Project Management (17)** — PM centers on schedule, cost, procurement, and contracts; coordination centers on the model and its conflicts. Issue records here are model-anchored (viewpoint/elements), not schedule/cost-anchored. Integration exists (Revizto↔Procore), which does not merge the Types.
- **vs RFI Management (17)** — RFIs are formal contractual questions between parties about design intent, with contractual response obligations; coordination issues are model problems tracked against the model with technical resolution. Some platforms carry both object kinds; the anchor and lifecycle differ.
- **vs Construction Quality Management / Punch List (17)** — quality/punch items are site-stage defects against constructed work; coordination issues are design-stage conflicts between models. Dalux literally splits these across products (BIM Viewer comments vs Field snagging), which is a clean market-structure confirmation.
- **vs Construction Reality Capture Platform (17)** — capture/registration of scans is that Type; scans may enter coordination as context (point-cloud checking in Solibri), which does not merge them.
- **vs generic BIM Viewer** — a viewer without a persistent issue register and resolution loop is not coordination. Dalux BIM Viewer sits exactly on this line: viewing alone would be a viewer; the comments-with-responsible-person-and-audit-trail machinery is what makes it coordination-capable.
- **vs Digital Twin Platform / FM** — operation-stage information products; coordination may hand over validated models toward them (Solibri lifecycle framing), which does not merge them.
- Removal tests ("去掉什么就变成另一个 Type"): remove federation (single model) → authoring-tool review or viewer; remove the issue register → viewer; remove the resolution loop → static clash report; move the anchor from model conflicts to schedule/cost → Construction Project Management; move the anchor to contractual questions → RFI Management; move the stage to site defects → Construction Quality Management; add element authoring → BIM Authoring.

## Uncertainties

- **Autodesk Navisworks uncharacterized** — the historical category anchor was unreachable (403) in three same-day passes. The final document contains no Navisworks claims; it is listed as a market anchor only. High prior that it fits the canonical model (the market's coordination vocabulary — federation, clash tests, viewpoints — is largely built around it), but that is inference, not evidence.
- **No Tier-1 operational docs fetched in this pass** — product evidence rests on official product/solution pages (Tier 2). Operational mechanics (exact issue-status vocabularies, exact clash-test configuration, exact BCF round-trip behavior, version-matching internals) were not verified; the final document stays at capability level.
- **Trimble Connect coordination depth** — the fetched page describes collaboration/issue machinery but not clash detection in detail; its coordination posture is recorded as CDE-embedded with thin evidence.
- **Model-checking Type question** — whether rules-based model validation deserves its own Type (separate from coordination) remains open; in the current market it is embedded in coordination products, so this pass keeps it inside the Type and flags it for future review if standalone validation platforms emerge.
- **Issue-status vocabularies** — products differ (BIMcollab shows "reported, ignored or new" for clash status; approval gates before close); no industry-uniform status set is asserted.

## Final Synthesis

BIM Coordination is the practice — and the software supporting it — of combining discipline models into a federated whole and driving the combined model to a conflict-free, information-consistent state through tracked issues: the software assembles models from multiple authors into one review context that preserves each model's origin; it finds problems in the combination (spatial clashes being the canonical kind, with rule violations, data gaps, and classification errors alongside); it records each problem as an issue anchored to the model (viewpoint, linked elements) with an assignee, status, and audit trail; issues travel to the responsible parties — increasingly through standardized exchange (BCF) and authoring-tool plugins — where the fixes are made in the authoring tools, not the coordination tool; updated models are re-federated and re-checked, and issues are verified resolved before closure, in repeating coordination cycles. Mature products add clash-detection engines with grouping/prioritization, rules-based model checking against project standards and information requirements (IDS/BEP), progress dashboards, web/mobile stakeholder viewers, 2D-drawing context, and deep authoring-tool/CDE integrations. Philosophies span validation-first checkers, issue-centric cloud hubs, collaboration hubs, free viewer-plus-comments entry tiers, and CDE-embedded coordination. The Type's hardest boundary is BIM Authoring (coordination consumes models; it does not author elements); its other boundaries — Construction Project Management, RFI Management, quality/punch-list tools, plain viewers — are held by the anchor of the tracked object (model conflict vs schedule/cost vs contractual question vs site defect vs nothing).
