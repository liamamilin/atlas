# Research Notes — Punch List Management

## Research Goal

Understand what a Punch List Management application actually is as an Application Type: what objects it holds, who records and resolves deficiencies, how the correction loop runs from discovery to verified closure, and where its boundary lies against the neighboring construction Types that share the same machinery — Construction Closeout Management, Construction Quality Management, Construction Field Management, Building Commissioning Platform, Construction Project Management, BIM Coordination, RFI Management, and generic task management.

This pass also discharges two standing joint-review flags recorded by earlier passes:

1. **From construction-closeout-management**: "when punch-list-management is processed, define it by the loop-only scope (regional names: punch US / snag UK-UAE / defect AU-SG / deficiency CA) and keep the acceptance/handover machinery on the closeout side."
2. **From construction-quality-management**: "JOINT REVIEW of construction-quality-management ↔ construction-field-management ↔ punch-list-management recommended when punch-list-management is processed" — the deficiency-register machinery is shared across three leaves; this pass must draw the register's own center.

## Initial Boundary

Initial hypothesis: a punch list is the list of remaining/deficient items found when inspecting completed construction work (characteristically near project end / handover), each item recording what is wrong, where, who must fix it, by when, with evidence; the software manages the list as a register and drives each item through assign → correct → verify → close. Nearest confusions: closeout (the phase outcome), quality (the conformance loop), field management (the integrating site layer), Cx (equipment-bound verification), generic task management (same loop shape, different object semantics).

## Research Questions

1. What is the unit of record, and what does an item carry (location, responsible party, evidence, due date, status)?
2. What is the item lifecycle, and who is allowed to close — can the fixing party close its own work?
3. Is the register (the list itself) a managed object — dashboards, filters, aging, reports?
4. Who uses it (GC superintendent/PM, subcontractors, owner, architect), and what rights does each party have?
5. How are items created (walkthrough capture, drawing pins, templates, import) and dispatched?
6. How is the register reported outward (PDF/CSV to owner/architect)?
7. Is the Type end-of-project-only, or is the machinery used across delivery stages?
8. What regional terminology variants exist, and do they name the same object?
9. How is this Type realized inside suites vs standalone apps vs free tiers?
10. Where are the boundaries vs closeout, quality, field management, Cx, PM, BIM coordination, RFI, and generic task management?

## Representative Products

| Product | Pole | Segment | Docs fetched |
|---|---|---|---|
| Procore | Enterprise GC suite; Punch List as a formal project tool with a named workflow | commercial GCs, owners | Tier-1 support (tool landing + workflow FAQ) |
| Fieldwire by Hilti | Field-first task app; punch realized as tasks + lists with two-step verification | GCs, subcontractors, SMB→enterprise | Tier-2 product page + Tier-1 help center |
| Dalux | European AEC platform; punch lists as a named solution under Dalux Field, BIM-anchored issues, free snagging tier | European GCs, owners, subs | Tier-2 solution + product pages |
| PlanRadar | International ticket-on-plan platform; defect management & punch lists across industries | GCs, developers/owners, facility managers, inspectors | Tier-2 product page + Tier-1 help center (ticket lifecycle) |

Attempted, unreachable (abandoned per network rule): **Bluebeam** (markup-based punch philosophy; support article URLs 404 ×2 — recorded as market context only, no claims), **Buildertrend** (403 in the closeout pass; residential pole therefore structural only), **Autodesk Construction Cloud** (JS-only help, per closeout pass).

## Sources

- Procore Support — Punch List (project tool user guide): https://support.procore.com/products/online/user-guide/project-level/punch-list (fetched 2026-09-09)
- Procore Support FAQ — "What is the Punch List Workflow?": https://support.procore.com/faq/what-is-the-punch-list-work-flow (fetched 2026-09-09)
- Fieldwire by Hilti — Punch List App product page: https://www.fieldwire.com/punch-list-app/ (fetched 2026-09-09; includes per-locale URL variants)
- Fieldwire Help Center — search "punch list" (141 results; tasks/custom-lists/QR/reports realization): https://help.fieldwire.com/hc/en-us/search?query=punch+list (fetched 2026-09-09)
- Dalux — Punch lists solution page: https://www.dalux.com/solutions/punch-lists/ (fetched 2026-09-09; includes per-locale URL variants)
- Dalux — product grid / Field Basic free snagging tool: https://www.dalux.com/ (fetched 2026-09-09)
- PlanRadar — US product page ("Defect management & punch lists" positioning): https://www.planradar.com/us/ (fetched 2026-09-09)
- PlanRadar HelpCenter — "Set Status & Progress of a Ticket": https://help.planradar.com/hc/en-gb/articles/13195317110685-Set-Status-Progress-of-a-Ticket (fetched 2026-09-09)
- Sibling research (in-repo, Layer B cross-reference): research/construction-closeout-management.md, research/construction-quality-management.md, research/construction-field-management.md, research/building-commissioning-platform.md, research/bim-coordination.md, research/construction-project-management.md, research/daily-log-application.md

## Product A — Procore

### Key observations (Layer A unless noted)

**Tool positioning** (Tier-1): "The Punch List tool is used at the end of a project to keep track of remaining items to complete, assign responsibility, and maintain due dates." Capabilities: create/manage items with drawings/photos attached, assign to users, set due dates with automatic overdue email notifications, assignees view/respond/complete from mobile in the field, track by status (open/closed/pending) with "real-time history of all actions."

**Punch List Workflow** (Tier-1 FAQ, "new Punch List Workflow"):
- Roles: **Punch Item Manager** ("responsible for overseeing a punch list item throughout its entire lifecycle… assigns a punch list item, manages all communication with third-party collaborators, and forwards the item to the responsible party for final approval") and **Final Approver** ("the last responsible party… has the final authority to close an item. In many cases, a punch list item's Creator will also serve as the Final Approver").
- Item statuses: Draft → Initiated → Work Required → Ready for Review → Ready to Close → Closed, with **In Dispute**, **Work Not Accepted**, and **Not Accepted** as negative paths. Closure authority is explicitly split: "The Final Approver, while in Ready to Close"; "A Project level Punch List tool Admin, at any time."
- Assignee responses: Work Required / Ready for Review / Work Not Accepted / Resolved — the resolver's "done" is a response, not a closure.
- Overdue semantics: an item is overdue "if the required work is not completed while the item's status is listed as Work Required or Work Not Accepted."
- **Activity Feed**: "a record of changes for each punch list item, including when the item was created, modified, and closed."

**Item anatomy & tooling** (Tier-1 user guide): templates & template categories (project-level punch item templates); import (incl. assisted import requests) and export (PDF/CSV, log export); bulk actions; email distribution & assignee notifications; search/filter; dashboards; change history per item; recycle bin; configurable fieldsets (fields configurable as required/optional/hidden); custom fields; granular per-tool permissions; private-by-default items; Quick Capture (voice titles, video, QR codes, offline); create items from drawings (pins, color codes) and map views; multi-tiered locations; mobile iOS/Android create/respond/close; distribution groups; "Date Notified" field.

**Roles observed in tutorial titles** (Tier-1): Owner, Superintendent, Subcontractor-as-collaborator, Specialty Contractor-as-client — the multi-party create → respond → close loop is documented per role combination.

**Market definition** (Tier-2 marketing FAQ, from sibling closeout research, corroborated): "Punch lists are lists of discrepancies between what the contract documents call for and what the parties to the contract delivered… come into play near the end of the project so people can fix them before the project's closeout." "It's common for every party in a construction project to use punch lists. The project punch list usually starts with the owner or the owner's design agents. General contractors and construction managers use the owner's punch list to make their own punch lists for the subcontractors." "Contractors usually must clear up the punch list items before they can get paid."

**Suite composition** (structural): Punch List is one project tool inside the suite (beside Submittals, RFIs, Documents, Daily Log, Inspections…). No separate named "closeout" tool — closeout is composed from the punch loop plus document/submittal records.

**Regional terminology** (Tier-2, per-locale URLs, from sibling research): punch list (US), deficiency list (CA), snag list (UK, UAE), defect list (AU, SG), Mangellisten (DE), lista de repasos (ES).

## Product B — Fieldwire by Hilti

### Key observations (Layer A for page content; positioning Tier-2)

**Product placement**: Punch list is one of four "Field management" surfaces (task management, scheduling, punch list, inspection) beside a "Project management" group (RFIs, submittals, change orders, budget, document management, specifications).

**Punch process** (Tier-2): "complete a punch list walkthrough in minutes while attaching all the pertinent details about each deficiency. Any contractor deficiency reported… can include a location on the blueprints plus photos, checklists, categories, hashtags, and due dates." Dispatch "to the various contractors from your iPhone, iPad, or Android device without ever needing to go back to the office." Skilled contractors "can also attach manpower, cost estimates and notes."

**Two-step verification** (Tier-2): "Every item reported in the mobile app will have to go through a two-step verification system. This allows you to move fast while guaranteeing that every deficiency was inspected for accurate completion." "Only Fieldwire Admins have the ability to verify the true completion of deficiencies. For example, on an architectural punch list, the general contractor would only be able to mark construction punchlist items as complete, while an architect could verify them."

**Walkthrough efficiency** (Tier-2): "Create a template for common deficiencies with attached checklists and duplicate them across locations that need a QA/QC review." Comments/photos "trigger a new notification."

**Reporting** (Tier-2): "Generate a polished PDF report in seconds by simply exporting all tasks in a given category or status. Then, send that report out to the project team, the project owner, or the architect." Automatic recurring reports; customer quote: "Fieldwire creates a punch list that gets delivered weekly to the trades via reports."

**Closeout framing** (Tier-2): "reach closeout faster with nothing falling through the cracks"; "Punch lists are a staple part of closing out your projects" (help center).

**Realization architecture** (Tier-1 help center): punch is realized through the **task** object plus **custom lists** ("for inspections and the punch list process"), **tags** ("tasks, plans, or photos with a specific trade, location, punch list, or anything else"), **QR codes** per task ("provide users in the field instant access to a task or punch list"), and **reports**. Third-party punch imports "import as Notes pinned directly on drawings." There is no separate punch object — the punch list is a configured view over tasks.

**Regional terminology** (Tier-2, per-locale URLs): punch list (US), snag-list-app (UK/IE/AU), réserves (FR), Mangellisten (DE), lista-de-defectos (ES), opleverlijst-app (NL), anmärkningslista (SV), applicazione-per-gli-elenchi-difformità (IT), aplikacja-do-listy-usterek (PL), aplikace-pro-seznam-vad-a-nedodělky (CS).

**Scale evidence** (Tier-2 customer story): a hospital project "tracked 15,000 punch items"; a real-estate owner uses the punch app for residential unit inspections.

## Product C — Dalux

### Key observations (Layer A for page content; positioning Tier-2)

**Named solution**: "Punch lists — Less deficiencies. More quality." sits under Dalux Field (on-site management) as a solution, beside Quality Control & Assurance and Health & Safety. Sibling product **Field Basic** is positioned as "Easy-to-use snagging tool with drawings and BIM. Invite all project members for free" — "a free mobile app to use for defect management on site. Upload your drawings or BIM models, invite your subcontractors."

**Issue loop** (Tier-2): "Upload drawings and pin the issue directly on the correct location. It makes it easy for other project participants to locate it." "Register all issues in one place and make sure nothing is overlooked. Send to the responsible person to rectify, and follow the progress on the phone." "Distribute the issues to the people responsible to rectify. It is easy to assign and send all information needed to finish and report ready."

**Register & analytics** (Tier-2): "Track progress, identify bottlenecks and make sure nothing is missed… gathering all issues in one place and get the complete overview." "Create a protocol with all issues directly from the system."

**BIM anchoring** (Tier-2): integrated BIM Viewer; issues usable against drawings and BIM models; measurements on drawings/models; "No more outdated drawings — access the most recent drawings and BIM models instantly on site."

**Participation** (Tier-2): "No Restriction on the number of user invites — Invite all project participants / the whole project"; "Unlimited number of issues."

**Quality-vs-punch seam from the vendor's own users** (Tier-2 testimonials): UBA Bouw quality manager: "we can use inspection- and control plans to register what goes right, while deviations are registered and monitored by a task" — the vendor's own ecosystem distinguishes planned conformance records from deviation/punch tasks. Betonmast: "follow up on Tasks to ensure quality."

**Regional terminology** (Tier-2, per-locale URLs): punch lists (US/CA/IE/UK/NO "punchlister"), Mängellisten (DE/AT), mangellister (DA), opleverlijsten (NL-BE/NL), listes de contrôle (FR), snag-list (IT/CH-IT), listas de incidencias (ES/PT-PT/PE), liste de defecte (RO), hiánylista (HU), seznamy nedostatků (CS), listy kontrolne (PL), zoznamy úloh (SK), seznami pomanjkljivosti (SL), tehtävälista (FI), loogiloendid (ET), kontrolinių darbų sąrašas (LT), списъци с незавършени работи (BG).

## Product D — PlanRadar

### Key observations (Layer A for help center; Tier-2 for positioning)

**Positioning** (Tier-2): "Construction & Building Condition Assessment Platform — field management, simplified"; for general contractors: "Build it right, first time" with capability tiles **"Defect management & punch lists"**, daily logs, inspections/checklists/safety audits, **handovers**, evidence collection & claims management. Multi-industry (construction, real estate, fire & life safety, facility management, property management). "Unlimited free subcontractors and watchers."

**Ticket object model** (Tier-1, from sibling closeout research + fresh fetch): the core object is the **ticket**, created against a project with form-defined fields; positioned on plans/BIM models; assignee & receivers; due date & extension date; attachments incl. photos, voice recordings, 360° panoramas; journal (activity history); QR codes / NFC tags / GPS to link & open tickets.

**Status lifecycle** (Tier-1, fresh fetch 2026-09-09): Open (default) → In Progress → Resolved ("resolved by a subcontractor and needs to be reviewed and closed by an in-house user") → Closed ("work is done"), plus Feedback ("assignee requires feedback to continue") and Rejected ("used when there is a reason that the ticket cannot be resolved"). **"Subcontractors cannot set tickets to Closed."** Separate 0–100% progress field; status colors map to ticket pins; ticket progress rolls up into schedule phases.

**Pre-digital practice attestation** (Tier-2 FAQ, from sibling research): "Many companies still manage highly complicated projects using only Microsoft Excel or even paper forms and snagging lists." — direct vendor confirmation of the paper/Excel antecedent.

## Cross-product Comparison

| Dimension | Procore | Fieldwire | Dalux | PlanRadar |
|---|---|---|---|---|
| Unit of record | punch list item (dedicated tool) | task (punch = configured lists/categories/tags) | issue/task in Field | ticket (form-defined) |
| Item content | description, assignee(s), due date, drawings/photos, location, comments, custom fields | location on blueprints, photos, checklists, categories, hashtags, due dates, cost estimates | description pinned on drawing/BIM, photos, responsible party | form fields, plan/BIM position, photos/voice/360°, assignee, due/extension date |
| Location anchoring | drawing pins + color codes, map view, multi-tiered locations | blueprint location | drawing pin + BIM model | plan/BIM position, QR/NFC/GPS |
| Lifecycle shape | Draft→Initiated→Work Required→Ready for Review→Ready to Close→Closed (+In Dispute/Work Not Accepted/Not Accepted) | task status + two-step verification (Admin verifies) | create → send to responsible → rectify → report ready | Open→In Progress→Resolved→Closed (+Feedback/Rejected) |
| Verified-closure gate | Final Approver closes; resolver's "Resolved" is not closure; Admin can force-close | only Admins verify true completion (GC marks complete, architect verifies) | responsible party rectifies; progress followed by issuer | subcontractors cannot set Closed; in-house reviews & closes |
| Register surfaces | log list, dashboard, search/filter, column display, CSV/PDF export | task list filtered by category/status, PDF reports | issue list, analytics/progress overview, protocol report | ticket list, statistics/boards, PDF reports |
| Dispatch & notification | email distribution, assignee notifications, overdue emails | dispatch to contractors from mobile, comment/photo notifications | send to responsible person, follow on phone | assignee & receivers, due/extension dates |
| Templates/import | punch item templates + categories, import (incl. assisted), Excel | deficiency templates with checklists, duplicated across locations; third-party punch import as pinned notes | — (not directly observed) | form templates |
| External participation | collaborator model, granular permissions, private-by-default items | assign to subcontractors; clients log in to view status | unlimited invited participants | unlimited free subcontractors/watchers |
| Audit trail | activity feed / change history | task activity | issue history (implied by follow-progress) | journal |
| Phase framing | "end of a project" | "staple part of closing out"; also QA/QC walkthroughs mid-project | "ensure a finished building" | defect management across build; handovers; reused in operations |
| Regional naming | punch/deficiency/snag/defect | punch/snag/réserves/Mängellisten/opleverlijst/anmärkningslista… | punch/Mängellisten/snag/opleverlijsten/listas de incidencias… | snag/defect (per-locale sites) |

**Cross-product commonality (Layer B):**

- All four implement a **resolution/verification split**: the party that fixes an item cannot unilaterally close it (Procore Final Approver; Fieldwire Admin-only verification; PlanRadar in-house-only closure; Dalux issuer follows the responsible party's rectification). This is the strongest cross-product rule in the sample.
- All four anchor items to **locations on the built work** (drawing pins, blueprint locations, plan/BIM positions, location hierarchies).
- All four carry **due dates with notification/overdue machinery** and **per-item attributable history**.
- All four maintain the **register as a managed, reportable object** (list + filters + dashboards + PDF/CSV reports sent to owner/architect/team).
- All four are **multi-party**: external subcontractors participate (respond/rectify) with limited rights; the accepting side (owner/architect/GC) creates and verifies.
- All four support **templates/reusable item structures** and **mobile field capture** (depth varies).

**Where the products diverge (poles):**

- **Formal-workflow pole** (Procore): a dedicated tool with named roles, an expanded status model, dispute paths, and granular permissions — the most codified accountability structure.
- **Task-view pole** (Fieldwire): no dedicated punch object; the punch list is a configured view over a general task object (lists, categories, tags), with verification as a permission gate.
- **BIM-anchored European pole** (Dalux): issues pinned on drawings and BIM models, packaged as a named solution with a free snagging tier (Field Basic) and unlimited participants.
- **Ticket-platform pole** (PlanRadar): form-defined tickets reused across industries (construction, fire safety, facility management), with the same machinery serving defect lists, inspections, and post-handover operations.

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **The deficiency item as the unit of record** — an individually identified record of a discrepancy between what the contract documents call for and what the completed work delivered, found by inspecting built work; the item carries its location on the work, a responsible party, and its status. (Remove → a generic task list.)
2. **The correction loop with verified closure** — the item is assigned to a responsible party who corrects it and reports completion; closure requires a verifying party distinct from the fixer — the fixer's "done" is a response, not a closure. (Remove → a to-do list; the accountability structure dies.)
3. **The register as the managed, reportable object** — items accumulate in one tracked list whose state (open/closed, aging, by location/trade/responsible party) is visible, filterable, and communicable outward (reports to the parties who must fix and accept the work); the register's burn-down toward zero is the managed outcome. (Remove → scattered issue comments with no list memory.)

Jointly-held load-bearing: (1 alone = a defect log with no accountability loop; 2 without 1 = an approval workflow over nothing; 3 without 1+2 = a report template; 1+2 without 3 = per-item tracking with no managed list; 1+3 without 2 = a defect tracker whose closure nobody verifies).

Historical check (§24): the pre-digital practice — a paper punch/snag list walked with the owner or architect, items noted by room with responsible trades, corrected by the trades, re-walked and checked off by the architect or GC (verifier ≠ fixer), the list copied and handed to the parties — satisfies all three invariants with no software. PlanRadar's own FAQ attests the living antecedent: "Many companies still manage highly complicated projects using only Microsoft Excel or even paper forms and snagging lists." Nothing in L0 assumes cloud, mobile, photos, BIM, or templates. The check passes.

### L1 — Common Mature Structure

Present across the sampled mature products but not definitional:

- **Location anchoring machinery** — drawing/plan pins with color codes, multi-tiered location hierarchies, map views, QR/NFC/GPS links (Layer B).
- **Photo/visual evidence** attached to items, feeding project photo stores (Layer B).
- **Due dates, overdue notifications, date-notified tracking, extension dates** (Layer B).
- **Templates & template categories** for recurring deficiency types; **import** (Excel/CSV, assisted, third-party punch import) and **export** (PDF/CSV) (Layer B).
- **Mobile field capture** incl. offline and quick-capture input (voice, video, QR) (Layer B; depth varies).
- **Dashboards/analytics** — open/closed counts, aging, bottlenecks, by-trade/by-location breakdowns (Layer B).
- **Attributable audit history** per item (activity feed / journal / change history) (Layer B).
- **Multi-party participation with limited external rights** — free/low-cost subcontractor accounts, collaborator models, private-by-default items (Layer B).
- **Granular permissions** over who can create, assign, respond, verify, close, configure (Layer B).
- **Custom fields / configurable fieldsets** (Layer B).
- **Status color coding** mapped onto drawing pins (Layer B).
- **Progress percentage** on items, rolling up into schedule phases (Layer B; single-product-strong → common with variation).

### L2 — Variant / Optional Structure

- **Regional terminology** — punch list (US), snag list (UK/IE/AE), defect list (AU/SG), deficiency list (CA), réserves (FR), Mängellisten (DE/AT), opleverlijst (NL), anmärkningslista (SV), lista de defectos (ES), and further local names — the same object under different names (Layer A across per-locale URLs).
- **Packaging shape** — dedicated tool inside an enterprise suite (Procore), configured view over a general task object (Fieldwire), named solution inside a European AEC platform with a free snagging tier (Dalux), form-defined tickets on a multi-industry platform (PlanRadar) (Layer B).
- **Phase orientation** — characteristically end-of-project/handover, but the same machinery is used mid-project (QA/QC walkthroughs, trade-to-trade handovers, "issues found at all stages of project delivery" per the quality-specialist evidence in sibling research) and post-handover (warranty/defects-liability, facility management reuse) (Layer B/C).
- **BIM/3D anchoring** — issues pinned on BIM models vs 2D drawings only (Layer B).
- **Cost/schedule impact tracking on items** (Layer B; single-product-dominant → optional).
- **Payment linkage** — punch completion gating payment (one vendor's FAQ framing; contractual practice) (Layer C).
- **Dispute paths on items** (Layer B; product-dependent).
- **Reality-capture integration** (360° capture feeding items) (Layer B).
- **AI assistance** (era-current, optional).
- **Residential/SMB dedicated shapes** — expected variant; sample evidence weak (Buildertrend family unreachable) — treat as unverified for feature specifics.

### L3 — Vendor-specific Structure

(Research notes only — not for the final document.)

- Procore: Punch Item Manager / Final Approver role names; status vocabulary (Draft, Initiated, In Dispute, Work Required, Work Not Accepted, Ready for Review, Ready to Close, Not Accepted, Closed); assignee-response vocabulary; Quick Capture (voice titles, video, QR, offline); recycle bin; configurable fieldsets (required/optional/hidden); permissions matrix (None/Read Only/Standard/Admin); distribution groups vs lists; "Date Notified" field; GH Phipps default punch list TYPE community artifact; per-locale marketing URL slugs.
- Fieldwire: punch realized as tasks + custom lists + hashtags + QR codes; two-step verification with Admin-only verify; tier-gated availability (pricing tiers); Track3D/Opusense/Teleworker integrations; per-locale URL slugs; customer-scale claims (15,000 items on one project).
- Dalux: Field Basic free tier; TwinBIM/AR; protocol reports; unlimited-users/unlimited-issues framing; localized solution slugs across ~28 locales; "Quality Assurance Act" (Norwegian) compliance framing by a customer.
- PlanRadar: ticket/form architecture (status & progress as form fields); status set (Open/In Progress/Resolved/Feedback/Rejected/Closed); "Subcontractors cannot set tickets to Closed"; extension dates; NFC tags; SiteView 360°; progress rollup into schedule phases; unlimited free subcontractors/watchers; multi-industry reuse (fire safety, facility management).

## Vendor-specific Findings

- Procore's "new Punch List Workflow" (Punch Item Manager + Final Approver + expanded statuses) is an explicit product evolution toward accountability/transparency — a vendor refinement of the L0 verification rule, not an industry-standard status model. The vendor explicitly notes the tool "can still be used in the same way you always have."
- Fieldwire implements punch with **no dedicated object** — the punch list is a configured view over tasks (lists/categories/tags) with verification as a permission gate. This is the clearest evidence that the Type's essence is the register + loop, not a specific data model.
- Dalux packages punch as a named solution beside Quality Control & Assurance and sells a free snagging tier (Field Basic) — evidence that the punch register is market-viable as a standalone free product, and that vendors themselves separate planned quality records from deviation/punch tasks (UBA Bouw testimonial).
- PlanRadar implements deficiency machinery as generic form-defined tickets and reuses it across industries and into building operations — the machinery is substrate, the punch use case is configuration.

## Rejected Findings

- **"Punch list = end-of-project only"** — rejected as definitional: the machinery is documented in use at all delivery stages (quality-specialist evidence: "document issues found at all stages of project delivery"; Fieldwire QA/QC walkthrough templates mid-project). Phase orientation is characteristic context, not invariant.
- **"The punch item is the same object as an RFI or a BIM coordination issue"** — rejected (consistent with the BIM-coordination pass): different anchors (contractual question vs model conflict vs site defect), different stages, different parties.
- **"Two named roles (manager + approver) are canonical"** — rejected: Procore-specific role names; the invariant is the verification split, not the role names.
- **"A specific status vocabulary is canonical"** — rejected: each product ships its own status set; the invariant is the loop shape (assigned → corrected → verified → closed).
- **"Payment gating is definitional"** — rejected: one vendor's FAQ framing; contractual practice varies.
- **"Photos/BIM/mobile are definitional"** — rejected: the paper/Excel antecedent satisfies the core without any of them.
- **"Free subcontractor access is definitional"** — rejected: business-model variant (Procore uses a collaborator/permission model instead).
- **"Punch list management = closeout management"** — rejected: the closeout pass held the seam; the punch Type is the loop-only scope (see Boundary Findings).

## Boundary Findings

| Type | Relationship | Distinction ("remove X → becomes Y") |
|---|---|---|
| Construction Closeout Management | nearest superset (phase outcome) | Punch = the deficiency loop to verified closure. Add the phase outcome — deliverable fulfillment (O&M, warranties, as-builts), recorded owner acceptance/turnover, retained owner-controlled record — and it becomes Closeout Management. Remove the loop and keep deliverables/acceptance → Closeout territory. In GC suites the punch tool is a *component*; closeout is the phase outcome composed around it. (Held seam from the closeout pass — RATIFIED from this side.) |
| Construction Quality Management | sibling sharing the deficiency register | Quality = the conformance loop: planned inspection regimes (ITPs, checklists against specifications, hold points), non-conformance disposition, acceptance machinery, spanning the whole delivery. Punch = the register-centric deficiency loop without a planned regime. Quality tools commonly host punch machinery (one platform ships quality tools and a punch tool side by side; a quality specialist labels its register "deficiency/work-to-complete punchlist") — bundling, not type fusion. Keep only the handover defect register → Punch List Management. (Held seam from the quality pass — joint review DISCHARGED from this side.) |
| Construction Field Management | sibling (integrating layer) | Field = the integrating site-execution layer (day record + general field work items). Punch = one register and its workflow. Keep only the punch register → this leaf; add the day record and the other registers → Field Management. (Held seam from the field pass.) |
| Building Commissioning Platform | sibling (verification evidence) | Cx = verification loop bound to equipment/system records and test outcomes; punch = deficiency list not bound to equipment/test structure. Remove tests/equipment and keep the deficiency list → Punch List Management. (Held seam from the Cx pass.) |
| Construction Project Management | container | PM owns schedule/cost/contracts/change across the lifecycle; punch is a point register inside the project container. Widen to the full lifecycle → Construction Project Management. (Consistent with the PM pass's umbrella note.) |
| BIM Coordination | adjacent issue loop | Coordination issues = design-stage conflicts between federated models; punch items = site-stage defects against constructed work. Dalux literally splits these across products (BIM Viewer comments vs Field snagging). (Held from the BIM-coordination pass.) |
| RFI Management | adjacent question loop | RFI = a contractual question routed to the design team; punch = a defect to be corrected by a responsible party. Different anchor and resolution. |
| Task Management (generic) | same loop shape, different object | A generic task is any work to do; a punch item is a deficiency in completed work measured against contract requirements, closed only on verification. Remove the deficiency semantics and the verification gate → generic task management. |
| Daily Log Application | complementary register | The day record ("what happened") vs the work-item register ("what must change"). (Consistent with the daily-log pass.) |
| Property Inspection Application | adjacent (standing portfolio) | Project-delivery register inside a project container vs recurring inspections over a standing property portfolio. |
| Government Inspection Management | adjacent (regulatory program) | Ongoing regulatory program over a standing subject inventory vs project-delivery deficiency register. |

## Uncertainties

- **Residential/SMB dedicated punch products** (Buildertrend family): unreachable (403 in the closeout pass; not retried per network rule); the residential variant shape is asserted only structurally, with no feature-level claims in the final document.
- **Markup-based punch** (Bluebeam Revu punch symbols on PDF drawings): support documentation unreachable (404 ×2); the "punch as drawing markup" philosophy is recorded as market context only, with no product claims.
- **Payment-gate strength**: "punch cleared before payment" is documented from one vendor's FAQ; the final document hedges accordingly.
- **Location-anchoring necessity**: every sampled product anchors items to locations, and the paper antecedent does too (room names); whether a market-viable product could carry the register without location anchoring is untested — location is therefore held as an item attribute (part of L0 #1's anatomy) rather than a standalone invariant.
- **Progress-percentage machinery**: documented as a first-class field at PlanRadar; treated as common-with-variation rather than definitional.

## Final Synthesis

Punch List Management is the register-centric deficiency-loop Type of construction delivery. Its defining core binds three things: the deficiency item as the unit of record (an individually identified discrepancy between what the contract documents call for and what the completed work delivered, carrying its location on the work, a responsible party, and status); the correction loop with verified closure (the responsible party corrects and reports; a distinct verifying party closes — the fixer's "done" is a response, not closure); and the register as the managed, reportable object (one tracked list whose open/closed state, aging, and per-trade/per-location breakdown are visible and communicated outward to the parties who must fix and accept the work, with the register's burn-down toward zero as the managed outcome). Mature products add drawing/plan/BIM pinning, photo evidence, due-date and overdue machinery, templates and import/export, mobile and offline capture, dashboards, attributable audit history, granular multi-party permissions, and configurable fields. The market realizes the Type in four shapes — a formal workflow tool inside an enterprise suite, a configured view over a general task object, a named solution inside a European BIM-anchored platform with a free snagging tier, and form-defined tickets on a multi-industry platform — under regional names that all denote the same object (punch / snag / defect / deficiency / réserves / Mängellisten / opleverlijst). The Type's boundaries are held by subtraction: add the phase outcome (deliverables, acceptance, turnover record) → Construction Closeout Management; add planned inspection regimes and non-conformance disposition → Construction Quality Management; add the day record and the other field registers → Construction Field Management; bind the loop to equipment and tests → Building Commissioning Platform; remove the deficiency semantics and verification gate → generic task management.
