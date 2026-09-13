# Research Notes — Product Discovery Platform

## Research Goal

Understand the Application Type "Product Discovery Platform" (DIRECTORY §12 Software Development & Product Engineering): what the product team's *discovery* workspace really consists of, how it differs from the planning/delivery side of product management tooling, and where its boundaries run against Customer Feedback Management, Product Roadmap Application, Requirements Management Platform, and research platforms.

Name-collision guard (recorded in STATUS.md by the product-discovery-application pass): "Product Discovery Application" (§05.05, consumer shopping discovery) and "Product Discovery Platform" (§12, this leaf) are unrelated Types sharing near-identical names. This pass confirms the guard from the §12 side.

## Initial Boundary

Working hypothesis before research:

- Core use: helping software product teams continuously gather signals (customer feedback, research, stakeholder input), turn them into candidate ideas/opportunities, prioritize them, and decide what to build next.
- Primary users: product managers, product leaders, product operations; secondary contributors across the org.
- Nearest neighbors: Product Management Platform (§12 sibling, unprocessed), Product Roadmap Application (§12 sibling, unprocessed), Requirements Management Platform (§12 sibling, unprocessed), Customer Feedback Management (§07, processed 2026-09-08), Voice of Customer Platform (§07, processed), Issue Tracker (§12), Market/Consumer Research Platforms (§06).
- Known unknowns: is this leaf a distinct Type or a Variant of Product Management Platform? Do all market products carry a distinct "insight/evidence" object? Is the customer-facing voting portal part of the Type or an adjacent capability?

## Research Questions

1. What is the unit of record — idea? feature? insight? opportunity? How do products name and structure it?
2. How does evidence (feedback, research, sales input) attach to candidates, and is the evidence object first-class?
3. What does prioritization look like concretely (fields, scores, frameworks, views)?
4. What is the decision lifecycle, and where does it end (handoff to delivery tools? roadmap placement? archive)?
5. Who contributes (internal roles, external customers) and through which channels?
6. How do products relate to roadmaps, to delivery trackers, and to strategy objects (OKRs/goals)?
7. Where is the seam vs Customer Feedback Management (feedback item vs idea) and vs Product Management Platform (idea vs planned work)?
8. Historical check: would pre-SaaS and spreadsheet-era discovery practice satisfy the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers/ecosystems:

| Product | Philosophy / position | Tier |
|---|---|---|
| Productboard | Enterprise "product management platform" whose distinctive core is insights → prioritization → roadmaps; fixed product hierarchy | Tier 1 (help center fetched) + Tier 2 |
| ProdPad | Opinionated discovery-led PM tool; "discovery separated from delivery" as an explicit design principle; Now-Next-Later roadmap inventor | Tier 2 (site + feature pages) |
| Jira Product Discovery (Atlassian) | Delivery-suite-native ideas/prioritization front-end to Jira; the most on-name product | Tier 1 (official docs fetched) |
| airfocus (by Lucid) | Modular item/workspace/field/view system with prioritization apps and insights/portal apps; EU/mid-market pole | Tier 1 (help-center structure) + Tier 2 |
| Aha! | Suite pole: discovery (Aha! Discovery = interviews), ideas capture (Aha! Ideas = feedback portal), planning (Aha! Roadmaps) sold as separate products | Tier 2 |

## Sources

Fetched 2026-09-09:

- Productboard — https://www.productboard.com/product/ (Tier 2); https://support.productboard.com/hc/en-us (Tier 1 index); https://support.productboard.com/hc/en-us/articles/27858826222355-Fundamentals-of-Productboard (Tier 1)
- ProdPad — https://www.prodpad.com/ (Tier 2); https://www.prodpad.com/features/ideas/ (Tier 2); https://www.prodpad.com/features/ideas/idea-workflow/ (Tier 2); https://help.prodpad.com/ (Tier 1 index only)
- Jira Product Discovery — https://support.atlassian.com/jira-product-discovery/ (Tier 1 index); https://support.atlassian.com/jira-product-discovery/resources/ (Tier 1 doc tree); https://support.atlassian.com/jira-product-discovery/docs/what-is-jira-product-discovery/ (Tier 1); https://support.atlassian.com/jira-product-discovery/docs/what-are-insights/ (Tier 1)
- airfocus — https://airfocus.com/ (Tier 2); https://help.airfocus.com/ → Lucid help center airfocus category https://help.lucid.co/hc/en-us/categories/14652566349972 (Tier 1 article index)
- Aha! — https://www.aha.io/product (Tier 2; suite structure: Aha! Roadmaps / Discovery / Ideas / Develop)

Not fetched (time/network budget): ProdPad individual help articles, airfocus individual articles, Aha! support KB, Canny/Dovetail boundary poles. The Customer Feedback Management seam is taken from the processed customer-feedback-management pass (STATUS.md 2026-09-08), which documents the boundary from that side.

## Product A — Productboard

### Key observations

- **Self-positioning (Tier 2):** "The leading product management platform built for scale… understand what customers need, prioritize what to build next, and align everyone around the roadmap." Use cases: customer feedback analysis/insights, roadmapping, customer engagement ("validate ideas & planned features, and share what's been launched"), product specification, strategic planning. [A for the product's own claims; positioning only]
- **Core data structures (Tier 1, Fundamentals article):**
  - One **product hierarchy** per workspace: **Products → Components → Features → Subfeatures**. Features = "a piece of plannable, completable work on the order of an epic"; subfeatures ≈ user stories. Features/subfeatures carry **statuses** (customizable on some plans); products/components are structural.
  - **"Features aren't feedback."** Features represent functional ideas that can be worked on and completed; feedback is tracked as **insights**, which are used "for connecting feedback to feature ideas."
  - **"Subfeatures aren't bugs."** Bug tracking belongs in a project management tool like Jira — an explicit boundary statement against issue trackers.
  - **Boards** are saved sets of tools/filters over the data: **Insights boards** (collect/review feedback), **Grids** (strategic planning and prioritization), **Timelines/columns boards** (roadmaps). Creating/deleting a board has no effect on data; boards are views.
  - **Data is universal**: entities and data fields deleted anywhere disappear workspace-wide; **no undo**; archive recommended. Deleting a board is cheap; deleting entities/data is dangerous.
  - **Spaces/teamspaces** organize folders and boards (Product, GTM, Leadership); default teamspace "Organization"; **member roles** gate board creation and editing ("makers" must join a teamspace to edit its boards).
- **Surfaces (Tier 1 index + Tier 2):** insights boards, prioritization grids, roadmap timelines/columns, customer feedback **portals** ("flexible, interactive interfaces you can share with colleagues or customers to validate…"), access-control/roles, Jira integration, app-store review ingestion, AI agent (Spark).
- **Evidence layer:** hierarchy/insights/board model = A (direct, Tier 1). Portal mechanics, AI behavior, integration details = B/A-mixed (vendor docs index + marketing).

## Product B — ProdPad

### Key observations

- **Self-positioning (Tier 2):** "Product management software that turns strategy into outcomes. Your roadmap, your ideas, your customer feedback, and your objectives belong in one connected system." Built by the co-founders of Mind the Product; inventor of the **Now-Next-Later roadmap**.
- **Six design principles (Tier 2, quoted):** outcomes over outputs; **evidence over opinions**; **discovery separated from delivery**; connected systems; time horizons instead of timelines; product management as a discipline. — Direct vendor articulation of the discovery/delivery seam.
- **Idea management (Tier 2):** ideas are the backlog unit: "Collect, validate, prioritize, implement and measure, all from one place."
  - **Idea workflow:** ideas move through phases "**discovery, delivery, and launch**"; preset filters separate ideas needing attention; workflow is configurable ("set whatever stages you need") and syncs with development tools (Jira, Azure DevOps, GitHub, Trello, Pivotal Tracker…).
  - **Idea Canvas:** "Validate your ideas with built-in questions and guidance… Expand and enrich with a business case, customer feedback, user stories and designs, until you have a fully-formed product spec that's ready to push to development."
  - **Prioritization:** "impact and effort scores… view your entire idea backlog in our unique priority chart."
  - **Feedback linking:** feedback captured from Slack, Salesforce, email, customer portals; AI "Signals" surface themes; related feedback auto-links to ideas; duplicate-idea similarity matching.
  - **Contributors:** "Invite unlimited free contributors" — stakeholders/team members/customers can submit ideas.
- **Strategy layer (Tier 2):** Objectives/OKRs, initiatives linked to ideas; lean roadmaps organized by Now/Next/Later horizons; portfolio management; reporting.
- **Evidence layer:** all observations = A for the vendor's own descriptions (official site), but mechanics (exact workflow states, canvas fields) not verified in help-center articles → treat operational specifics as existence-level.

## Product C — Jira Product Discovery (Atlassian)

### Key observations

- **Self-definition (Tier 1):** "a dedicated tool for product teams to **capture and prioritize ideas**, connect business and tech teams, and align everyone… It makes it easy for product managers to capture and share the ***why*** behind the work." "Built in Jira so you can bridge the gap between your business and tech teams connecting product ideas to the dev work in Jira."
- **Structure (Tier 1 doc tree + articles):**
  - **Spaces** = discovery containers with **space roles** and access management; **workflows** configurable per space; automation templates.
  - **Ideas** = the central record: multiple **idea types with hierarchies** configurable; description templates; comments; **merge ideas**; **archive and restore**; created from the create-button, list/board views, Jira Service Management portal, Slack/Teams, Chrome extension.
  - **Insights** (Tier 1 article): "derived from various sources, including snippets from customer interviews, research links related to user behavior, support cases, sales opportunities, product analytics dashboards, or messages from stakeholders via… Slack or Teams." Insights "help articulate the rationale behind prioritizing specific ideas." Attributes: description, optional link (Zendesk/JSM/Salesforce objects), **rating**, labels; fields can aggregate insight impact ("how many support tickets mention this idea?").
  - **Fields** (global + per-space, custom fields, **custom formulas**) drive evaluation; **views**: list, board, **matrix** (prioritization), timeline, tree; **roadmaps** as curated views with permissions; view publishing/commenting/export.
  - **Delivery tab:** "**Convert Jira Product Discovery ideas into Jira epics** and link ideas to Jira work items and track progress"; delivery-progress field with date autofill — the handoff is a first-class surface.
- **Evidence layer:** A (direct, Tier 1) for structure and insights; the "what is JPD" framing is the vendor's own.

## Product D — airfocus (by Lucid)

### Key observations

- **Self-positioning (Tier 2):** "The Product Intelligence Platform for teams that have to make the right decisions, fast… Strategy, signal, and insight in one connected system." Modules named on the site: **Objectives & OKRs, Roadmaps, Prioritization, Feedback & Insights, Portal**. Signals "traceable back to the source."
- **Help-center structure (Tier 1 index, now hosted under Lucid):**
  - **Workspaces** (with workspace groups, multi-workspace templates) connected via **item types and hierarchy**; **portfolios** centralize items from multiple workspaces.
  - **Items** = the generic record; item activity log; **item links** (relationship mapping); Docs (rich text).
  - **Fields**: single/multi-select, t-shirt sizing, time period, **status**, people, text — the evaluation vocabulary is user-configurable.
  - **Views**: list, timeline, chart, **dashboard**, document.
  - **Apps**: **Priority Ratings** ("determine your next project"), Capacity Planning, **Portal** ("share airfocus items with the customizable Portal app"), Item Mirror, **Insights** ("collect feedback with the Insights app") + **Insights agent** (AI).
  - **Integrations**: Jira, Azure DevOps, Zendesk, Microsoft Planner, webhooks, MCP server.
  - Roles/permissions article; EU data residency; SAML/SCIM.
- **Evidence layer:** A for the module/article structure (official help index); individual article contents not read → mechanics at existence level.

## Product E — Aha! (suite pole)

### Key observations

- **Suite structure (Tier 2):** Aha! sells separate products: **Aha! Roadmaps** ("link strategy to plans" — strategy, prioritization, releases, roadmaps, reports), **Aha! Discovery** ("manage customer interviews"), **Aha! Ideas** ("capture customer feedback" — "crowdsource ideas from customers and employees via a custom-branded portal… promote the best ones directly to your roadmap… send automatic status updates"), Aha! Whiteboards, Aha! Develop (agile delivery), plus knowledge/teamwork products.
- **Aha! Roadmaps capabilities (Tier 2):** set strategy (goals/initiatives, personas, competitor insights), capture ideas, score features ("objective scoring metrics"), prioritize, plan releases (Gantt, dependencies, capacity), report (75+ pre-built reports), whiteboard concepts, AI assistant (Elle); integrations send planned work to engineering (Jira, Azure DevOps, Aha! Develop).
- **Interpretive value:** the suite vendor's own packaging separates **research/interviews (Discovery)**, **feedback capture (Ideas)**, and **planning (Roadmaps)** — market evidence that "discovery" as a named concern centers on understanding needs and deciding, distinct from planning/delivery. [A for the packaging; B for the interpretation]

## Cross-product Comparison

| Dimension | Productboard | ProdPad | Jira Product Discovery | airfocus | Aha! |
|---|---|---|---|---|---|
| Unit of record | Feature/Subfeature in a fixed product hierarchy (Products→Components→Features→Subfeatures) | Idea (backlog unit, Idea Canvas) | Idea (configurable types + hierarchies) | Item (generic, in workspaces, item types/hierarchy configurable) | Feature/initiative (Roadmaps); idea (Ideas product) |
| Evidence object | Insight ("features aren't feedback") | Feedback linked to ideas; Signals themes | Insight (interviews/research/tickets/opportunities; rating, labels, source links) | Insights app + agent (feedback, traceable to source) | Ideas portal entries; personas/insight notes (Discovery = interviews) |
| Evaluation machinery | Grids, formula scores, custom fields | Impact/effort scores, priority chart | Custom fields + formulas, matrix view | Priority Ratings app, custom fields, chart views | Feature scores (value vs effort class), prioritization view |
| Decision lifecycle | Feature statuses; releases | Idea workflow: discovery → delivery → launch (configurable stages) | Space workflows; promote to Jira epic; archive/restore | Status fields; workspace workflows | Promote ideas to roadmap; release plans |
| Delivery handoff | Jira integration | Two-way sync with dev tools | Delivery tab: link/convert to Jira work items, delivery progress | Jira/Azure DevOps integrations | Send to engineering via Jira/Azure DevOps/Aha! Develop |
| Roadmap surface | Timeline/columns boards | Now-Next-Later lean roadmap | Roadmaps as curated views | Timeline view; roadmaps sharing | Roadmaps product (the suite's center) |
| Strategy linkage | Objectives | Objectives/OKRs, initiatives | Atlassian Goals integration | Objectives & OKRs module | Goals/initiatives |
| Contribution channels | Integrations (support/CRM/app-store), portals | Free contributors, Slack/Salesforce/email/portals | Slack/Teams, JSM portal, Chrome extension, Salesforce | Insights app, Portal app, Zendesk | Branded ideas portal, Salesforce/Zendesk add-ons |
| Org container | Teamspaces + member roles (makers/contributors) | Products/portfolios; contributor licenses | Spaces + space roles | Workspaces + roles/permissions | Workspaces per product |
| Duplicate handling | (insights tagging/merging — not verified this pass) | AI similarity dedupe | Merge ideas | Item Mirror (sync, not dedupe) | (not verified) |
| Customer-facing loop | Portals to validate ideas & planned features | Roadmap embedding, portals | JSM portal (idea intake) | Portal app | Ideas portal with status updates |
| AI | Spark agent | CoPilot, Signals | Atlassian Intelligence | Insights agent, AI features | Elle |

**Cross-product commonalities (evidence layer B):** every sampled product holds a population of candidate-work records (idea/feature/item); every product provides comparative evaluation (fields/scores/frameworks + at least one matrix/chart/board view); every product carries a decision lifecycle that ends in promotion toward delivery tooling or a roadmap, with archive/decline as a first-class outcome; every product attaches customer/stakeholder evidence to candidates; every product separates an internal decision workspace from customer/stakeholder-facing surfaces; every product links to delivery trackers.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The idea/opportunity as the unit of record.** A persistent, individually addressable record of a *candidate for future product work* — a problem to solve, an opportunity, a proposed capability — carrying a description and decision attributes (owner, status, evaluation values). It is not a task, not a bug, not a customer remark. *(Remove → issue tracker / task list / feedback inbox.)*
2. **Comparative evaluation machinery over the idea population.** Shared decision attributes (fields, scores, framework values) plus views (lists, boards, matrices, charts) that let the team compare ideas against each other and against strategy, producing a relative ordering. *(Remove → idea archive/suggestion box with no decision support.)*
3. **The decision lifecycle ending in a build/don't-build outcome.** Ideas move through managed workflow states from capture through evaluation to a recorded decision: promoted into planning/delivery (handed to development tools or placed on a roadmap) or declined/archived. *(Remove → static idea list; the "deciding what to build" function is gone.)*

Jointly-held is load-bearing:
- 1 alone = idea list / suggestion box
- 2 without 1 = empty scoring machinery / generic spreadsheet
- 3 without 1+2 = workflow tool with nothing to decide
- 1+2 without 3 = evaluation without decisions (analysis, not discovery)
- 2+3 without 1 = process over nothing

### L1 — Common mature structure (evidence layer B)

- **Evidence/insight attachment** — insights/feedback/research records linked to ideas, commonly with source links, ratings, labels, and aggregation into idea-level signals. (All 5 sampled; realized very differently — dedicated insight objects vs feedback linking vs research modules.)
- **Roadmap/plan views over decided ideas** — timeline, Now-Next-Later, columns; communication artifacts, not the record itself.
- **Delivery-tool handoff** — link/convert/push ideas into Jira-class trackers; delivery progress read back.
- **Contribution channels** — portals, Slack/Teams capture, browser extensions, support/CRM integrations, free contributor seats.
- **Strategy linkage** — objectives/OKRs/initiatives/goals that ideas attach to.
- **Workspace organization + roles** — spaces/workspaces/teamspaces; maker/contributor/viewer distinctions.
- **Duplicate handling** — merge, similarity dedupe.
- **Stakeholder communication** — shareable/publishable views, comments, notifications, status updates.
- **AI assistance** — theme surfacing, triage, drafting (2026 market; not definitional).

### L2 — Variant / optional structure

- Customer-facing validation portals with voting (heavy overlap with Customer Feedback Management; present in some products as a major surface, absent/light in others).
- Hierarchy philosophy: fixed product hierarchy (Productboard) vs configurable item types (JPD, airfocus) vs flat ideas.
- Prioritization framework specifics (RICE-class, value/effort, impact/effort, custom formulas).
- Suite membership vs standalone; depth of delivery-suite coupling (native same-vendor vs third-party integrations).
- Research-module depth (interview management, research repositories — Aha! Discovery pole; Dovetail-class tools adjacent).
- Portfolio/multi-product rollups, capacity planning.
- Deployment/compliance posture (EU residency, SAML/SCIM, enterprise controls).

### L3 — Vendor-specific (kept out of the final document)

- Productboard: fixed Products/Components/Features/Subfeatures hierarchy; teamspaces; "no undo" data doctrine; Spark agent; makers/contributors role names.
- ProdPad: Now-Next-Later branding; Idea Canvas; CoPilot; Signals; six principles; free contributor licenses.
- Jira Product Discovery: spaces/space roles; delivery tab with Jira epic conversion and delivery-progress autofill; JSM portal intake; Atlassian Goals; Chrome extension; insight ratings + aggregation fields.
- airfocus: workspaces/items/fields/views/apps architecture; Priority Ratings, Capacity Planning, Item Mirror, Portal, Insights apps; Lucid ownership; EU residency emphasis.
- Aha!: suite split (Roadmaps/Discovery/Ideas/Develop/Whiteboards); Elle assistant; branded ideas portal with automatic status updates.

## Vendor-specific Findings

See L3. Additionally: ProdPad's "six principles" page is the clearest vendor articulation of the Type's philosophy (evidence over opinions; discovery separated from delivery) — used as boundary evidence, not as canonical structure. Productboard's "Features aren't feedback" and "Subfeatures aren't bugs" help-center statements are explicit vendor-drawn boundaries (vs feedback tools and vs issue trackers) — high-value boundary evidence.

## Rejected Findings

- **"Product Discovery Platform = public feedback voting portal."** Rejected: voting portals are one capture/validation surface (and belong substantially to Customer Feedback Management); the sampled centers are internal decision workspaces (JPD, airfocus, ProdPad centers; Productboard portals are auxiliary).
- **"Roadmaps are the unit of record."** Rejected: in every sampled product the roadmap is a view/communication surface over decided candidates, not the record; the record is the idea/candidate.
- **"Discovery = customer interviews."** Rejected: interview management is one module (Aha! Discovery pole); the Type's center is the idea-decision workspace.
- **"Must be coupled to a specific delivery suite."** Rejected: only JPD is suite-native; others integrate across tools.
- **"AI assistance is definitional."** Rejected: all sampled products ship AI (2026), but the historical check shows the Type predates it.
- **"Customer attribution is definitional"** (the discriminator Customer Feedback Management uses). Rejected for this Type: internal ideas are first-class discovery input (JPD "collect feedback from internal stakeholders"; ProdPad internal contributors); the discriminator vs CFM runs the other way (see Boundary Findings).

## Boundary Findings

- **vs Product Management Platform (§12 sibling, unprocessed).** Same population, different center of gravity. Discovery = the *why/what's worth building* decision workspace: idea-centric, evidence-driven, ending in a decision. PM platform = planning/coordination of *committed* work: feature/release/roadmap-centric. Market evidence: Aha! sells Discovery/Ideas and Roadmaps as separate products; ProdPad states "discovery separated from delivery" as a design principle; JPD positions itself as the ideas/prioritization front-end to Jira delivery. Counter-evidence: vendors self-label loosely (Productboard calls itself a "product management platform"; ProdPad calls itself "product management software") and products legitimately span both. **Conclusion: keep both leaves; the seam is the center of gravity (decision workspace vs delivery-planning system of record). Recommend joint review when product-management-platform is processed.**
- **vs Product Roadmap Application (§12 sibling, unprocessed).** The roadmap is a communication/planning artifact; in discovery platforms it is one view over the decided idea population. A roadmap application's unit of record is the plan/roadmap itself.
- **vs Requirements Management Platform (§12 sibling, unprocessed).** Requirements specify the *how exactly* for committed work; discovery decides the *what/why* before commitment. ProdPad's own flow marks spec-out as the end of discovery ("a fully-formed product spec that's ready to push to development").
- **vs Customer Feedback Management (§07, processed 2026-09-08).** CFM's unit of record is the *customer feedback item* (attributed to customers, aggregated into demand signals, tracked toward product decisions). This Type's unit of record is the *idea/opportunity being decided*; feedback is one evidence input among several (research, sales, analytics, stakeholder input). The CFM pass recorded "feedback item ≠ planned work item" vs Product Management Platform; from this side the seam is "feedback item ≠ idea under decision." Products straddle (Productboard portals, Aha! Ideas, ProdPad feedback module). Echo/discharge: consistent with the CFM pass's boundary; no conflict.
- **vs Voice of Customer Platform (§07, processed).** VoC fields instruments to the organization's own customers and scores experience metrics; discovery platforms do not field surveys as their center.
- **vs Issue Tracker / delivery tools (§12).** Explicit vendor boundaries: Productboard "Subfeatures aren't bugs… better off in Jira"; JPD converts ideas *into* Jira epics — delivery work lives in the tracker, candidates live here.
- **vs Market Research Platform / Consumer Research Platform (§06).** Those field studies to samples of consumers with panels; discovery platforms organize the product team's own continuous evidence and decisions. Interview management appears only as a module (Aha! Discovery).
- **vs Product Discovery Application (§05.05, consumer shopping discovery).** Name collision only; unrelated users, objects, and workflows. Guard confirmed from this side.
- **"去掉什么就变成另一个 Type" 判据：** remove the idea/opportunity unit (keep only attributed customer feedback) → Customer Feedback Management; remove the decision lifecycle (keep capture + evidence) → research repository / feedback archive; remove the product-decision context → internal idea management (no leaf); move the center to committed work + releases → Product Management Platform / Product Roadmap Application; move the center to precise specifications → Requirements Management Platform.

## Historical / Market-Sample Check

- The spreadsheet-era practice — a feature-request/idea list with value-and-effort columns, a prioritization matrix, a "decided" column, and a handoff memo to engineering — satisfies all three L0 structures with no SaaS, AI, portals, or integrations. 
- Early-agile-era product backlogs (prioritized candidate lists feeding release planning) satisfy the same structures.
- Suite-native (JPD), standalone-opinionated (ProdPad), modular (airfocus), enterprise-hierarchy (Productboard), and suite-split (Aha!) realizations all fit the L0 without era-specific machinery.
- Conclusion: the definition is era-robust; nothing in L0 names cloud, AI, voting, or any specific framework.

## Uncertainties

- ProdPad and Aha! help-center articles were not individually fetched; workflow-state names, canvas fields, and portal mechanics are existence-level only. No precise operational claims made in the final document.
- airfocus individual help articles not read (help center migrated to Lucid); the item/workspace/field/view/app model rests on the official article index (Tier 1 structure, Tier 1 article titles).
- Productboard insight mechanics (auto-linking, AI summarization) observed via marketing pages and help index, not step-by-step articles.
- Duplicate-handling evidence is uneven across the sample (verified at JPD/ProdPad; unverified at Productboard/Aha!) — kept as common-with-gaps, not definitional.
- Canny/Dovetail-class boundary poles not fetched this pass; the CFM seam relies on the processed CFM pass plus vendor doc trees. If a research-repository leaf is ever added, re-examine the Dovetail/EnjoyHQ pole.
- The market's self-labeling ("product management platform") overlaps this leaf and the unprocessed product-management-platform leaf; the center-of-gravity seam is well-evidenced but the leaf pair should be reviewed together when the sibling is processed.

## Final Synthesis

A Product Discovery Platform is the product organization's **decision workspace for what to build next**. Its world is made of **candidate ideas/opportunities** held as records; **evidence** (customer feedback, research, sales and support signals, stakeholder input) attached to them; **shared evaluation machinery** (fields, scores, frameworks, comparative views) that turns judgment into an ordered, debatable portfolio; and a **decision lifecycle** that moves each idea from capture through evaluation to a recorded build/don't-build outcome, with promotion into planning/delivery tooling (or a roadmap) as the exit and archive/decline as a first-class alternative. Mature products add evidence objects, roadmap views, delivery handoffs, contribution channels, strategy linkage, roles, duplicate handling, and AI assistance. The Type sits between voice-of-customer tooling (which captures and aggregates what customers say) and product management/delivery tooling (which plans and tracks what is committed): its center is the decision that connects the two.
