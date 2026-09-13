# Research Notes — Product Management Platform

## Research Goal

Understand what a Product Management Platform actually is as an Application Type: what its world is made of, what its users do in it, how work flows through it, and where its boundaries sit against the neighboring §12 leaves (Product Discovery Platform, Product Roadmap Application, Requirements Management Platform) and the delivery-side leaves (Issue Tracker, Agile/Engineering Project Management).

This pass also carries a **joint-review obligation** recorded by the product-discovery-platform pass (2026-09-09): the discovery/PM-platform seam must be reviewed from this side, and the seam with the still-unprocessed product-roadmap-application must be positioned.

## Initial Boundary

Initial hypothesis (to be tested, not asserted):

- A Product Management Platform is the product organization's system of record for **planning and coordinating committed product work**: features as records, organized under products, scheduled into releases/timeframes, expressed as roadmaps, tracked from proposal to launch, and coordinated with delivery teams.
- Nearest neighbors: Product Discovery Platform (decides *what's worth building*), Product Roadmap Application (the roadmap artifact itself), Requirements Management Platform (specifies *how exactly*), Issue Tracker / Agile PM (delivery-side work items), Project Management Application (generic bounded undertakings), Customer Feedback Management (voice of customer).
- Known risk: vendors self-label loosely — Productboard calls itself a "product management platform" while centering feedback-driven discovery; ProdPad calls itself "product management software" while centering outcome-based roadmaps. The Type must be defined by structure, not by vendor self-labels.

## Research Questions

1. What is the unit of record — feature? initiative? idea? roadmap bar?
2. What container organizes the units (product, workspace, portfolio)?
3. How do units get committed to time (releases, timeframes, Now-Next-Later)?
4. Is the roadmap a record or a view? What exactly does it express?
5. What is the status lifecycle of a planned item, and where does delivery status come from?
6. How does the platform connect to delivery tools (Jira-class trackers)? Is the link structural?
7. What planning machinery exists (prioritization, scorecards, dependencies, capacity)?
8. What input surfaces exist (feedback, ideas, research) and are they definitional or optional?
9. What communication surfaces exist (shareable roadmaps, portals, presentations)?
10. Where exactly is the seam vs Product Discovery Platform, Product Roadmap Application, Requirements Management, and the delivery-side Types?

## Representative Products

Selected for market representativeness, documentation quality, and distinct product philosophies / customer tiers:

| Product | Philosophy / position | Customer tier | Evidence tier |
|---|---|---|---|
| Productboard | feedback-connected feature planning; self-labels "product management platform" | mid-market → enterprise | Tier 1 (help center articles fetched) |
| Aha! Roadmaps | suite product (Roadmaps / Discovery / Ideas / Knowledge / Develop sold separately); strategy-first | mid-market → enterprise | Tier 1 (getting-started article fetched) |
| ProdPad | opinionated standalone; outcome/initiative-based roadmaps; "discovery separated from delivery" as stated principle; Lucid-owned | SMB → mid-market | Tier 1 (help center index + initiatives article fetched) |
| ProductPlan | roadmap-first communication tool, expanded into "Product Intelligence Platform" | SMB → enterprise | Tier 2 (official marketing site fetched; support hub exists, articles not fetched) |

Rejected/deferred samples:

- **Craft.io** — WebFetch transport error twice; abandoned per source-access rule. Not sampled; no claims rest on it.
- **Jira Product Discovery (Atlassian)** — already deeply sampled by the product-discovery-platform pass as the suite-native discovery pole; reused here only as boundary evidence, not re-fetched.
- **airfocus** — already sampled by the discovery pass; modular workspace/field architecture noted there; not re-fetched.

## Sources

Fetched 2026-09-09:

- Productboard Support — "Fundamentals of Productboard" (key data structures, hierarchy, boards, data model): https://support.productboard.com/hc/en-us/articles/27858826222355-Fundamentals-of-Productboard
- Productboard Support — "Quick start guide: Roadmaps" (roadmap board types, roadmap-centered entity types, sharing): https://support.productboard.com/hc/en-us/articles/29983922254739-Quick-start-guide-New-roadmaps
- Productboard Support — "Getting started with Productboard's Jira Integration" (push/link features, release push, status automation): https://support.productboard.com/hc/en-us/articles/11535151728275-Getting-started-with-Productboard-s-Jira-Integration
- Productboard Support — knowledge base index (category structure: Customer Insights, Strategic Planning, Prioritization and Roadmapping, Product Operations, Integrations): https://support.productboard.com/hc/en-us/
- Aha! Support — "Get started with your new account" (Aha! Roadmaps: workspace hierarchy, strategy records, features board, parking lots, releases, Gantt, scorecards, roadmaps, reports, presentations): https://support.aha.io/aha-roadmaps/getting-started/introduction/get-started-with-aha~7444678287096948177
- Aha! Support — knowledge base index (product split: Roadmaps / Discovery / Ideas / Whiteboards / Develop / Teamwork / Knowledge): https://support.aha.io/
- ProdPad Help — "Using ProdPad" category index (Products, Roadmaps, Ideas, Feedback, Personas, Designs, Collaboration sections): https://help.prodpad.com/category/69-using-prodpad
- ProdPad Help — "Initiatives" (roadmap cards as initiatives, grouping ideas/stories, objectives link, candidate/completed states): https://prodpad.helpscoutdocs.com/article/531-initiatives
- ProductPlan — official site (platform positioning: Strategic Roadmaps, Prioritization, Ideas, Portfolio, Jira/Azure DevOps integrations, comparison table): https://www.productplan.com/

Prior-pass evidence reused (fetched 2026-09-09 by product-discovery-platform pass):

- research/product-discovery-platform.md — JPD positioning, ProdPad "discovery separated from delivery" principle, Aha! suite split, Productboard "Features aren't feedback" / "Subfeatures aren't bugs" help-center statements.

Source-access limitations:

- Craft.io unreachable (2 transport errors) — not sampled.
- ProductPlan help-center articles not fetched; its internal record model is described at existence level from official marketing pages only.
- ProdPad individual articles beyond the index and the Initiatives article not fetched; ideas/feedback mechanics recorded at existence level.
- Aha! record-workflow state names not enumerated (they are customer-customizable anyway); no canonical state vocabulary claimed anywhere.

## Product A — Productboard

### Key observations (evidence layer A unless noted)

- **Product hierarchy is the backbone**: "Your product hierarchy is a nested list of entities… It's the backbone of your workspace, and you can't use Productboard without it." Entity types in descending order: **Products → Components → Features → Subfeatures**. Products/components are structural (no status); features/subfeatures carry status.
- **Feature defined by the vendor**: "Features represent a piece of plannable, completable work on the order of an epic"; subfeatures are smaller, "something like a user story."
- **Status lifecycle on features**: colored status per feature/subfeature, clickable to change; admin-customizable status list (plan-dependent).
- **Release as a data field**: hierarchy data includes "feature status, release, or formula score" — release is an attribute a feature carries.
- **Boards are views, not records**: "A board is a set of tools and filters… Creating, duplicating, or deleting a board has no effect on the data it displays." Board types: Insights (feedback), Grids (prioritization), Timelines and Columns (roadmaps).
- **Roadmap = view over the same data**: roadmaps (timelines/columns) are "specialized for communicating plans to internal audiences"; can center on Objectives, Initiatives, Products/components/features, or Releases ("milestones, launch phases, or abstract time measurements like Now-Next-Later"). "The data you see on roadmaps are the same data you see on other boards… usually better to edit and organize your data on grid boards, then use roadmaps for visualization and alignment."
- **Audience-specific roadmaps**: guidance to build per-audience roadmaps (executives high-level, engineers granular); roadmaps inherit teamspace access controls; portals (not roadmaps) are the external-communication surface.
- **Delivery link is structural**: Jira integration — push features/subfeatures into Jira as new issues or link to existing ones; push releases into Jira (sync to fix versions); field mapping; **status automation: Productboard feature status updates automatically from Jira issue status** — "track from Productboard what is happening across your delivery teams." Vendor framing: "connect your product discovery and product delivery processes in one seamless workflow."
- **Vendor-drawn boundaries**: "Features aren't feedback" (insights are for feedback; features are completable work); "Subfeatures aren't bugs… You're better off doing that in a project management tool like Jira."
- **Input side**: Insights boards for collecting/reviewing feedback; portals for collecting feedback at scale; feedback links to features.
- **Governance**: teamspaces (open/private) with member roles (makers/contributors/viewers); custom roles governing field access; data is universal and deletion is destructive ("no undo button").
- **AI**: Spark AI agent (chat + skills) — 2026-era addition, not structural.

## Product B — Aha! Roadmaps

### Key observations

- **Suite split confirms the Type's seams**: Aha! sells Roadmaps, Discovery, Ideas, Whiteboards, Develop, Teamwork, Knowledge as separate products. Roadmaps is the planning product; Discovery/Ideas are the idea-side products; Develop/Teamwork are delivery-side; Knowledge is documentation. (Layer A for the split; supports the discovery/PM seam.)
- **Workspace hierarchy**: account → workspace lines → workspaces; settings inherit down; terminology customizable per line.
- **Strategy layer**: vision, models, positioning, personas, competitor profiles, **goals** (time-bound, measurable), **initiatives** ("large, strategic themes of work"); work links to initiatives; initiatives link to goals.
- **Features board**: create **parking lots** ("define your backlog — important work you have not yet committed to"); create a **release** — vendor definition: "a container for work organized around a specific date"; create/import **features**, then add them to a parking lot or a release.
- **Gantt**: release phases, milestones, dependencies between records or phases.
- **Prioritization**: product value scorecard (metrics + equation, customizable), sort releases by score, prioritization page with custom stack ranking, assign features to users.
- **Roadmaps as saved views**: starter roadmap, strategy roadmap (visualizing initiatives); saved views; roadmaps update in real time as records change.
- **Reporting/communication**: pivot tables (e.g., "Feature status"), dashboards, presentations built from saved views for stakeholders.
- **Delivery link**: integrations with Jira, Azure DevOps, Rally — import records or sync; 30+ integrations.
- **Record workflows customizable**; custom fields/layouts per workspace.
- **AI**: Elle assistant (draft strategy records, refine backlog, release plans, feature scoring, roadmap alignment analysis) — 2026-era, not structural.

## Product C — ProdPad

### Key observations

- **Product container**: Products (with portfolios for multi-product management; private products supported); product-level **Objectives and Key Results** and **Canvas** (lean canvas).
- **Roadmap built on Initiatives, not releases**: "A roadmap card is an initiative to be undertaken, expressed as a problem to solve… framed as a hypothesis or opportunity." Initiatives "group a set of ideas and stories together so you can understand what and why you are working on things and will link back to a set of objectives." Initiative states include **candidate** and **completed**; target dates optional; ARR linkable; roadmap update log; publish roadmap for sharing.
- **Ideas as the working unit below initiatives**: ideas list, idea prioritization, idea scoping, idea automations; ideas promoted into initiatives; user stories generated (AI-assisted in 2026).
- **Feedback as a module**: customer feedback with contacts/companies, signals/theme analysis, feedback portal — a first-class module but distinct from ideas and initiatives.
- **Designs**: attach designs with annotations to items.
- **Collaboration**: discussions, real-time collaboration, revision history, conflict resolution.
- **Philosophy (from prior pass, Tier 1)**: "discovery separated from delivery" is a stated design principle; specs/user stories are the handoff to development tools (Jira integration pushes stories).
- **Time posture**: Now/Next/Later columns and target dates rather than date-boxed releases (existence level from category index + initiative article).

## Product D — ProductPlan

### Key observations (Tier 2 — official marketing; existence level)

- **Self-positioning**: "product management software that combines strategic roadmapping with AI-powered customer and market intelligence"; "The Product Intelligence Platform."
- **Roadmap is the center**: "Visual timeline roadmaps your whole company can read without training"; audience-specific views for leadership, engineering, external stakeholders; live sharing via secure links "no slide decks required."
- **Records behind the roadmap**: bars/items with dates; "23M+ initiatives planned," "14M roadmap items shipped" — items carry progress to shipped.
- **Delivery link**: "Real-time Jira and Azure DevOps integrations"; "Parent/child relationships maintained across initiatives, epics, and stories in Jira, ADO, and ProductPlan in real-time"; unassigned-work drawer for dragging tracker items onto the roadmap.
- **Prioritization**: customizable scoring frameworks; connect customer feedback to feature scoring; backlog management connected to strategic goals.
- **Portfolio**: portfolio view across multiple products and teams (native, per its comparison table).
- **Ideas/research**: ideas capture & management; AI-moderated research surveys (Product Intelligence) — 2026-era expansion.
- **Comparison table** (vendor-claimed, use with caution): positions itself as faster-to-first-roadmap vs Aha!/Productboard; claims competitors are "built for large orgs" — marketing, not evidence.

## Cross-product Comparison

| Structure | Productboard | Aha! Roadmaps | ProdPad | ProductPlan |
|---|---|---|---|---|
| Unit of record | Feature (+Subfeature) | Feature | Idea → grouped under Initiative | Roadmap item/bar |
| Product container | Product hierarchy (Products→Components) | Workspace hierarchy | Products (+portfolios) | Roadmaps/portfolios |
| Time commitment | Release (field; Now-Next-Later as abstract release) | Release ("container for work organized around a specific date") + phases/milestones | Initiative target dates; Now/Next/Later | Timeline bars with date ranges |
| Strategy grouping | Objectives, Initiatives | Goals, Initiatives | Objectives/OKRs | Goals connected to items (claimed) |
| Roadmap | Timeline/columns boards = views over same data | Saved roadmap views + Gantt | Roadmap of initiative cards; publishable | The center; visual timeline |
| Prioritization | Grids, formula score | Value scorecard, stack ranking | Idea prioritization | Scoring frameworks |
| Status lifecycle | Feature status (customizable) | Customizable record workflow | Candidate → active → completed initiatives | Progress on items to "shipped" |
| Delivery link | Jira push/link + status automation | Jira/Azure/Rally sync | Jira story push | Jira/ADO real-time parent/child sync |
| Input/evidence | Insights (feedback) | Ideas portal (separate product) | Feedback module | Ideas + AI research |
| Communication | Portals, shared boards | Presentations, dashboards | Published roadmap | Share links, audience views |
| Specs/docs | Details sidebar; docs | Aha! Knowledge (separate product) | Specs/user stories | Not center |

**Cross-product commonalities (Layer B):**

1. All four hold **planned product work as persistent records** (feature / item / idea-under-initiative) with owner, priority, and status.
2. All four organize records **under a product/workspace container** and support multi-product portfolios.
3. All four commit records into **time-bound structure** (release, timeframe, target date, timeline bar) — the roadmap expresses this commitment.
4. In all four, **the roadmap is a view/communication surface over records**, not the record itself (Productboard states it explicitly; Aha! saved views update in real time; ProdPad roadmap cards are initiatives; ProductPlan bars are items).
5. All four carry a **status lifecycle from proposal to shipped/launched** (customizable vocabularies; ProdPad's candidate→completed; ProductPlan's "items shipped").
6. All four integrate with **delivery trackers** (Jira-class) and keep plan status current from delivery progress (Productboard status automation is the most explicit).
7. All four provide **prioritization machinery** (scores, rankings) — but manual ordering also works; machinery is not the invariant.
8. All four provide **stakeholder communication surfaces** (share links, portals, presentations, published roadmaps).
9. All four ship **AI assistance** in 2026 — era feature, not structural (historical check confirms).
10. Input surfaces (feedback/ideas/research) exist in all four but with **wildly different weight** — from Productboard's insight-centric design to Aha! selling Ideas as a separate product. Not definitional.

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The feature as the unit of record** — a persistent, individually addressable record of one planned piece of product work (a capability or change to be built), carrying description, owner, priority, and status, and belonging to the product. Remove → issue-tracker work item, idea card, or feedback item — the object is no longer "planned product capability."
2. **The product plan of record** — features organized under the product and committed into time-bound structure (releases, timeframes, target dates) forming the single plan that roadmap views express. Remove → flat backlog list, or a roadmap picture with no records behind it.
3. **The plan-to-delivery coordination loop** — features advance through a managed status lifecycle from proposal to shipped/launched; the product team maintains the plan against delivery progress (commonly synced from delivery tools) and communicates the plan to stakeholders. Remove → a one-shot planning document; the "management" is gone.

Jointly-held load-bearing:

- 1 alone = issue tracker / feature-request list
- 2 without 1 = empty release calendar / roadmap picture
- 3 without 1+2 = status spreadsheet over nothing
- 1+2 without 3 = static plan document
- 1+3 without 2 = status tracker without a plan (drifts to issue tracker)
- 2+3 without 1 = roadmap artifact without records

### L1 — Common Mature Structure

- product/workspace hierarchy (products → components → features; workspace lines; portfolios)
- grouping above the unit: initiatives / objectives / goals linking work to strategy
- roadmap views (timeline, columns, Gantt) as saved, audience-specific views over the same records
- release/phase/milestone structure with dependencies
- prioritization machinery (scorecards, custom fields, stack ranking)
- delivery-tool integration (push/link features ↔ tracker issues; status sync back into the plan)
- backlog/parking-lot state for uncommitted candidates
- stakeholder communication surfaces (shareable roadmaps, portals, presentations, dashboards)
- roles/permissions (makers/contributors/viewers; workspace-level access control)
- reporting/analytics (status reports, progress dashboards)

### L2 — Variant / Optional Structure

- feedback/ideas capture inside the platform (weight varies from center to separate product)
- spec/PRD/user-story authoring (ProdPad pole; Aha! sells Knowledge separately)
- strategy artifact authoring (vision/personas/competitor models — Aha! pole)
- OKR/objective management depth
- external customer portals
- AI assistance (all sampled, 2026)
- release notes / launch management
- design attachment (ProdPad)
- deployment posture: SaaS-dominant; no self-host pole sampled (uncertainty noted)

### L3 — Vendor-specific (research notes only)

- Productboard: teamspaces, Spark AI, no-undo data model, plan-gated integration counts, "Features aren't feedback" phrasing.
- Aha!: Elle assistant, presentations-from-views, workspace-line terminology customization, suite split (Roadmaps/Discovery/Ideas/Knowledge/Develop).
- ProdPad: Canvas, Signals/theme analysis, CoPilot PM, MCP integration, ARR-on-initiatives.
- ProductPlan: Product Intelligence (AI-moderated surveys), comparison-table marketing claims, "23M+ initiatives" counters.

## Vendor-specific Findings

See L3. Additionally: vendor self-labels are unreliable for typing — Productboard ("product management platform") and ProdPad ("product management software") both self-label as PM platforms while structurally weighting discovery and outcome-roadmaps respectively. ProductPlan's comparison-table claims are marketing and were not used as evidence for any canonical structure.

## Rejected Findings

- **"The roadmap is the unit of record."** Rejected: in every sampled product the roadmap is a view/communication surface over records (Productboard states this explicitly; Aha! saved views; ProdPad cards are initiatives; ProductPlan bars are items). The record is the feature/initiative.
- **"Product Management Platform = feedback/ideas capture."** Rejected: input surfaces vary from center (Productboard insights) to separate product (Aha! Ideas) to module (ProdPad feedback). The invariant is the committed-work plan, not the input pipe.
- **"Releases are definitional."** Rejected as a *named* structure: ProdPad runs on initiative target dates and Now/Next/Later without date-boxed releases; Productboard supports abstract releases (Now-Next-Later). The invariant is time-bound commitment, not the release object.
- **"Scorecards/prioritization frameworks are definitional."** Rejected: manual ordering suffices; machinery is common mature structure.
- **"Specs/PRDs are definitional."** Rejected: Aha! sells Knowledge separately; Productboard keeps specs in a details sidebar; the spec is a handoff artifact, not the plan.
- **"AI assistance is definitional."** Rejected: all sampled products ship AI (2026), but the paper-era practice satisfies the core without it.
- **"Suite-native delivery tracking is part of the Type."** Rejected: vendor-drawn boundaries explicitly push bugs/task delivery to trackers (Productboard → Jira); the PM platform holds the plan and syncs status, it does not replace the tracker.

## Boundary Findings

- **vs Product Discovery Platform (§12 sibling, processed 2026-09-09) — JOINT REVIEW DISCHARGED from this side.** Same market population, different center of gravity. Discovery = the *what's worth building* decision workspace: idea/opportunity-centric, evidence-driven, ending in a recorded build/don't-build decision. PM platform = the *committed-work plan of record*: feature-centric, plan/release-centric, ending in shipped. Market evidence: Aha! sells Roadmaps and Discovery as separate products (confirmed from this side's fetch of the Aha! product split); ProdPad states "discovery separated from delivery" as a design principle; JPD positions itself as the ideas front-end to Jira delivery. Counter-evidence: vendors self-label loosely (Productboard "product management platform"; ProdPad "product management software") and products legitimately span both — the seam is the center of gravity, not a hard wall. **Conclusion: keep both leaves; seam = decision workspace vs delivery-planning system of record.** Consistent with the discovery pass's conclusion; no conflict.
- **vs Product Roadmap Application (§12 sibling, UNPROCESSED).** The roadmap is a communication/planning artifact; in PM platforms it is a view over feature records + time commitments, not the record. ProductPlan is the roadmap-first pole and still holds items with status/progress and tracker sync — evidence that even the roadmap-first product carries the PM-platform core. **Joint review with product-roadmap-application remains OPEN until that leaf is processed** — recorded in STATUS.md.
- **vs Requirements Management Platform (§12 sibling, UNPROCESSED).** Requirements specify the *how exactly* for committed work; the PM platform plans the *what/when*. ProdPad's flow marks spec-out/user-stories as the handoff to development. Seam noted for that pass.
- **vs Issue Tracker / Agile PM / Engineering PM (§12, processed).** Delivery-side work items (stories/bugs/tasks, sprints, velocity) vs product-side plan (features/releases/roadmap). Vendor-drawn: Productboard "Subfeatures aren't bugs… better off in Jira"; status automation flows tracker→plan, making the direction of authority explicit (delivery executes; the plan coordinates). Products interlock via push/link/sync.
- **vs Project Management Application (§03.07, processed).** Generic bounded undertaking (any project) vs product capability planning under a product container with roadmap/release semantics.
- **vs Customer Feedback Management (§07, processed 2026-09-08).** Feedback item (customer voice, attributed, aggregated) ≠ planned feature (committed work). Feedback is one evidence input; the CFM pass already recorded "feedback item ≠ planned work item" vs this leaf — consistent from this side.
- **"去掉什么就变成另一个 Type" 判据：** remove the feature unit (keep only ideas under decision) → Product Discovery Platform; remove the plan-of-record/time commitments (keep only status-tracked work items) → Issue Tracker / Agile PM; remove the delivery-coordination loop (keep only the communication artifact) → Product Roadmap Application territory; remove the product context (keep generic projects) → Project Management Application; move the center to precise specifications → Requirements Management Platform; keep only attributed customer voice → Customer Feedback Management.

## Historical / Market-Sample Check

- **Paper-era product plan**: a feature list with target-release columns, owner, status, and a launch checklist satisfies all three L0 structures with no software, scorecards, portals, or AI.
- **Spreadsheet-era (2000s) practice**: Excel roadmap + PRD documents + release plan + status meetings satisfies the same structures; the roadmap spreadsheet was a view over a feature list, exactly as modern roadmaps are views over records.
- **Early-agile-era**: product backlog + release plan + roadmap slide deck satisfies (backlog = uncommitted candidates; release plan = time commitment; status maintained against delivery).
- **Poles all fit**: roadmap-first (ProductPlan), outcome-first (ProdPad), feedback-first (Productboard), strategy-first suite (Aha!) — none require era-specific machinery in the core.
- Conclusion: the definition is era-robust; nothing in L0 names cloud, AI, scorecards, portals, or any specific framework. The §24 check passes.

## Uncertainties

- Craft.io could not be fetched; the sample lacks a spec-centric standalone pole. The spec/PRD layer is therefore held at L2 with existence-level evidence (ProdPad) and the requirements seam is noted for the unprocessed sibling pass.
- ProductPlan evidence is Tier 2 (official marketing); its internal record model (items, bars, portfolios) is described at existence level only. No precise operational claims rest on it.
- ProdPad ideas/feedback mechanics recorded at existence level (category index + one article); promotion mechanics (idea → initiative) observed but not step-verified.
- Aha! record-workflow state names not enumerated (customer-customizable); no canonical status vocabulary is claimed anywhere in this pass.
- Self-hosted / on-prem PM platforms were not sampled; deployment posture held as uncertainty, not asserted either way.
- The exact boundary vs Product Roadmap Application cannot be finalized while that leaf is unprocessed; this pass records its side and flags the open joint review.

## Final Synthesis

A Product Management Platform is the product organization's **plan-of-record system for committed product work**. Its world is made of **features** — persistent records of planned product capabilities, owned, prioritized, and status-carrying — organized **under products** and committed into **time-bound structure** (releases, timeframes, target dates) that forms the single plan the roadmap expresses; and a **plan-to-delivery coordination loop** in which features advance from proposal through committed plan to shipped/launched, with delivery progress (commonly synced from trackers like Jira) flowing back into the plan and the plan being communicated outward to stakeholders through shareable roadmap views. Mature products add product/workspace hierarchies and portfolios, initiative/objective groupings linking work to strategy, prioritization machinery, dependencies, audience-specific roadmap views, portals and presentations, roles and access control, and reporting. Input surfaces (feedback, ideas, research) are common but weighted very differently across products — from center to separate product — and are not what makes the Type. The Type sits between the discovery workspace (which decides what's worth building, ending in a decision) and the delivery tracker (which executes the work, story by story): its center is the committed plan that connects the two.
