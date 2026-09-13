# Product Discovery Platform

## Overview

A **Product Discovery Platform** is a product team's decision workspace for determining what to build next. It holds candidate product ideas and opportunities as persistent records, attaches customer and stakeholder evidence to them, provides shared machinery for comparing and prioritizing the candidates, and moves each one through a decision lifecycle that ends in a recorded outcome: promoted into planning and delivery, or declined and archived.

The problems it solves are specific: feedback and ideas arrive scattered across support tickets, sales calls, research notes, and meetings; every idea looks urgent and the loudest voice wins; and the reasoning behind what gets built lives in slide decks and private spreadsheets nobody trusts. A discovery platform gives the team one place where candidates accumulate, evidence gathers behind them, priorities are argued with visible criteria, and decisions are made and communicated.

Its boundary: a discovery platform manages the *why* and the *what's worth building* — the period before work is committed. It is not where committed work is specified, scheduled, and tracked (product management and delivery tools), and it is not where customer feedback is merely collected and aggregated (feedback management systems), though it connects to both.

## Users & Context

Primary users:

- **Product managers** — run the loop daily: capture ideas and insights, enrich candidates, evaluate and compare, prepare decisions, hand off what is chosen.
- **Product leaders / heads of product** — steer the portfolio: review priorities against objectives, arbitrate competing bets, communicate plans upward and outward.
- **Product operations** — standardize the process: configure workflows, fields, and views so every team decides the same way.

Secondary users:

- **Contributors across the organization** — engineers, designers, sales, support, and executives who submit ideas, add evidence, and comment. Many products deliberately make contributing cheap or free, because discovery depends on input from people who don't live in the tool.
- **Stakeholders and customers** — view published roadmaps and, in some products, submit and follow ideas through customer-facing portals.

Typical context: software product organizations practicing continuous discovery — regularly talking to customers, feeding what they learn into a visible pipeline of candidate work, and deciding in the open rather than by escalation.

## Core Model

The defining core is small — three structures that only work together:

```text
Evidence (insights, feedback, research, sales & support signals)
      │ attached to
      ▼
Idea / Opportunity  ── evaluated with ──▶  Evaluation fields, scores & views
 (the unit of record)                          (comparative prioritization)
      │
      ▼
Decision lifecycle  ──▶  Build: hand off to planning/delivery
      │                  Don't build: decline / archive (a first-class outcome)
```

- **The idea / opportunity as the unit of record.** A persistent, individually addressable record of a *candidate for future product work* — a problem to solve, an opportunity to seize, a capability to add. It carries a description and decision attributes: owner, status, evaluation values, links to strategy. It is deliberately not a task, not a bug, and not a customer remark — vendors draw these lines explicitly ("features aren't feedback"; bugs belong in the issue tracker). One product may hold many idea types with hierarchies; another may fix a strict product → component → feature → subfeature hierarchy; a third keeps a flat idea list. The candidate record itself is the constant.
- **Evidence attached to ideas.** Customer feedback, interview snippets, research findings, support cases, sales opportunities, analytics observations, and stakeholder messages are captured as evidence records — commonly called insights — and linked to the ideas they bear on, often with a source link, a rating of significance, and labels. Evidence is what turns a wish list into an argued case: it articulates *why* an idea deserves priority, and it can aggregate (how many customers, which accounts, which revenue segment).
- **Comparative evaluation machinery.** Ideas are described by shared, configurable fields — value, effort, impact, confidence, reach, custom formulas — and surfaced through views built for comparison: prioritization matrices (value against effort), scored lists, boards grouped by status or theme. The machinery exists to make relative ordering debatable: two people can dispute a score, not a hunch.
- **The decision lifecycle.** Ideas move through managed workflow states — captured, under evaluation, validated, decided — configurable per team. The lifecycle ends in a recorded outcome: promotion into planning and delivery (typically by linking or converting the idea into work items in a development tracker, and/or placing it on a roadmap) or an explicit decline/archive. Declining is a first-class outcome, not a failure: a visible "not now, because…" is part of the system's value.
- **Strategy linkage.** Ideas commonly attach to objectives, OKRs, initiatives, or goals, so prioritization is argued against declared direction rather than in a vacuum.

**Standard capabilities** that mature products add around this core (expected in the market, but not what makes the Type):

- roadmap views over decided ideas (timelines, horizon-based Now/Next/Later columns) as communication surfaces
- delivery handoff: link or convert ideas into work items in development trackers, with delivery progress read back
- contribution channels: customer/stakeholder portals, chat-app capture, browser extensions, support and CRM integrations
- duplicate handling: merging related ideas, similarity-based dedupe
- workspace organization and roles: spaces/workspaces/teamspaces; maker/contributor/viewer distinctions
- stakeholder communication: shareable or publishable views, comments, notifications, status updates to contributors
- AI assistance: surfacing themes across feedback, suggesting links, drafting summaries (common in current products; not definitional)

**One structure, many implementations:**

```text
Concept:   Candidate for future work      Implementations: idea, feature, opportunity, item
Concept:   Evidence                       Implementations: insight objects, linked feedback, research notes
Concept:   Comparative evaluation         Implementations: scoring fields + formulas, matrix views, priority charts
Concept:   Decision outcome               Implementations: workflow statuses, conversion to delivery tickets, roadmap placement
Concept:   Strategy linkage               Implementations: objectives/OKRs, initiatives, goals
```

## How It Works

The defining loop is continuous and runs in cycles:

```text
Capture
→ an idea or opportunity is recorded (from a teammate, a portal, a chat message,
  a support ticket, a sales call, a research session)
→ evidence is attached (linked feedback, interview notes, source records, ratings)
→ enrich & evaluate
→ the idea is described, scored against shared criteria, compared with peers in
  matrix/list/board views, and argued over in comments
→ decide
→ the team promotes it (status change; place on a roadmap; convert/link to work
  items in the development tracker) or declines/archives it with the reasoning kept
→ hand off & close the loop
→ delivery happens in the development tool; progress and launch flow back as status;
  contributors and customers are updated
```

Two structural separations run through everything:

- **Discovery is separated from delivery.** The platform holds candidates and decisions; actual work items, sprints, and bugs live in the development tracker. The handoff — link, convert, push — is a first-class operation, and delivery progress is read back so the idea's record shows what happened.
- **The internal workspace is separated from external surfaces.** Inside, the team argues with raw evidence and candid scores. Outside, curated views and portals show stakeholders and customers what is planned, what shipped, and what became of their suggestions — without exposing internal deliberation.

A typical adoption path: define the workspace (products, idea types, workflow states, evaluation fields), connect feedback sources, invite contributors, then run the loop and publish views for stakeholders.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Idea list / backlog board

The primary working surface: the population of candidates with their statuses, owners, and scores.

- typical information: title, status, owner, scores, linked evidence count, product/area
- primary actions: create idea, filter/group, move status, open detail

### Idea detail (canvas / spec)

The record for one candidate.

- typical information: description, problem statement, linked evidence and insights, scores, comments, attachments, linked strategy, delivery links
- primary actions: edit, attach evidence, score, comment, change status, convert/link to delivery work, merge duplicates, archive

### Prioritization view (matrix / scored list)

The comparison surface where relative order is decided.

- typical information: ideas plotted or ranked by evaluation fields (value vs effort, custom formulas)
- primary actions: adjust scores, compare, select for promotion, reorder

### Roadmap view

The communication surface over decided ideas.

- typical information: promoted ideas arranged by time horizon or plan, status, target period
- primary actions: curate what appears, share/publish, export

### Evidence / insights surfaces

Where feedback and research accumulate and link to ideas.

- typical information: captured feedback items, sources, ratings, themes
- primary actions: capture from integrations/channels, link to ideas, tag, aggregate

### Portal (customer/stakeholder-facing)

The external surface for validation and engagement.

- typical information: candidate or planned ideas chosen for sharing, status labels, sometimes voting/submission
- primary actions: submit an idea, vote/comment, follow status updates

### Administration / settings

Workflow states, idea types, fields and formulas, roles and permissions, integrations, portal branding.

## Important Rules / Behaviors

- **Candidates are not delivery work.** The platform's records describe and decide; they do not schedule or track engineering execution. The boundary is enforced by the handoff: work begins when an idea becomes a work item in the delivery tool. Bugs and tasks belong in the tracker, not here.
- **Views don't change the record.** Lists, boards, matrices, and roadmaps are saved perspectives over one shared dataset; rearranging a view doesn't move the underlying ideas, and deleting a view destroys nothing but the view.
- **Evidence feeds decisions, visibly.** Scores and priorities are expected to trace to attached evidence; the strongest products make the trail inspectable (which customers or accounts, which sources, how many).
- **Merging is the answer to duplicates.** Related ideas about the same need are consolidated — commonly with the contributors and evidence preserved — so demand signals don't fragment.
- **Decline and archive are managed outcomes.** Rejected ideas are archived with their reasoning rather than deleted; products commonly treat archive as the safe alternative to deletion, since records are shared state for the whole workspace.
- **Roles gate the workspace.** A small set of people curates and decides; a wider set contributes ideas, evidence, and comments; stakeholders view published surfaces. Contributor access is often intentionally cheap so the funnel stays wide.
- **Internal deliberation stays internal.** Customer-facing portals expose only what the team chooses to share; internal scores, debates, and evidence remain behind the line.

## Variants

- **Standalone discovery workspace** — the whole product is the decision loop (ideas, evidence, prioritization, handoff), delivery left to third-party trackers.
- **Delivery-suite-native discovery** — the same loop built inside a development suite, with native conversion to that suite's work items and tighter coupling end-to-end.
- **Suite module** — discovery sold as one product in a vendor's suite, alongside separate products for research/interviews, feedback capture, and roadmap planning.
- **Feedback-portal-heavy** — customer-facing idea boards and voting dominate the surface; the internal decision loop is thinner (heavy overlap with customer feedback management).
- **Prioritization-framework-heavy** — configurable items and scoring machinery dominate; evidence capture is an add-on app rather than the center.
- **Enterprise portfolio** — multi-product hierarchies, portfolios, capacity views, and governance for large product organizations.
- **Research-adjacent** — interview management and research repositories bundled beside the idea loop.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Product Management Platform | closest sibling | same population, different center of gravity: the PM platform plans and coordinates *committed* work (features, releases, roadmaps as the record); the discovery platform decides *what's worth committing* (candidates and evidence as the record). Vendors span both and self-label loosely, so the seam is the center of gravity, not the branding |
| Product Roadmap Application | adjacent | the roadmap itself is the unit of record and the product; here a roadmap is one view over decided ideas |
| Requirements Management Platform | downstream | specifies the *how exactly* of committed work; discovery ends where specification begins |
| Customer Feedback Management | upstream, heavily adjacent | its unit of record is the attributed customer feedback item aggregated into demand signals; here feedback is one evidence input to a decision about an idea. Products legitimately straddle (portal + decision workspace) |
| Voice of Customer Platform | upstream | fields survey instruments and scores experience metrics; discovery platforms don't run measurement programs |
| Issue Tracker / delivery tools | downstream, explicitly distinct | holds tasks and bugs; vendors state the boundary directly (bugs belong there; ideas convert into its work items) |
| Market / Consumer Research Platform | adjacent discipline | fields studies to samples of consumers with panels; discovery platforms organize the team's own continuous evidence and decisions |
| Product Discovery Application (shopping) | name only | despite the near-identical name, that Type is consumer shopping discovery (product feeds, deals, personalized browsing) — unrelated users, objects, and workflows |

## Representative Products

- **Productboard** — enterprise insights → prioritization → roadmap platform; fixed product hierarchy; portals for validation
- **ProdPad** — opinionated discovery-led tool; idea workflow with discovery/delivery/launch phases; Now-Next-Later roadmaps
- **Jira Product Discovery** — delivery-suite-native ideas and prioritization front-end to Jira
- **airfocus (by Lucid)** — modular workspaces/items/fields/views with prioritization, insights, and portal apps
- **Aha!** — suite pole: Discovery (interviews), Ideas (feedback portal), and Roadmaps (planning) sold as separate products, illustrating the market's own discovery/planning split

## Sources

Research date: **2026-09-09**

- Productboard — product overview https://www.productboard.com/product/ ; Help Center https://support.productboard.com/hc/en-us ; "Fundamentals of Productboard" https://support.productboard.com/hc/en-us/articles/27858826222355-Fundamentals-of-Productboard
- ProdPad — https://www.prodpad.com/ ; Idea Management https://www.prodpad.com/features/ideas/ ; Idea Workflow https://www.prodpad.com/features/ideas/idea-workflow/ ; Help Center index https://help.prodpad.com
- Jira Product Discovery — support https://support.atlassian.com/jira-product-discovery/ ; "What is Jira Product Discovery?" https://support.atlassian.com/jira-product-discovery/docs/what-is-jira-product-discovery/ ; "What are insights?" https://support.atlassian.com/jira-product-discovery/docs/what-are-insights/
- airfocus — https://airfocus.com/ ; help center (Lucid) airfocus category https://help.lucid.co/hc/en-us/categories/14652566349972
- Aha! — https://www.aha.io/product (suite structure: Aha! Roadmaps / Discovery / Ideas)

> Sourcing limitation: official help-center articles were read in depth for Productboard and Jira Product Discovery; ProdPad, airfocus, and Aha! rest on official product pages and help-center/doc-tree structure (existence-level evidence). Operational specifics — exact workflow-state names, scoring formulas, portal mechanics, plan limits — are intentionally not stated. Detailed observations and evidence calibration are recorded in the paired Research Notes.
