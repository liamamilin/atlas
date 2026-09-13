# Promotion Management

## Overview

A **Promotion Management** application is a merchant-side application that treats temporary promotional offers as managed, governed, and measurable business objects. It is where a retailer or seller plans *which* products will be promoted, *how* (the offer mechanic), *when* (a defined validity period), *where* (stores, zones, channels, or customer groups), under whose approval, and at what cost — and then tracks what each promotion actually delivered.

The defining core is small:

```text
Promotion record
└── offer mechanic + product scope + validity period
    └── governed lifecycle (plan → approve → activate → distribute)
        └── tracked performance against the promotion
```

Everything else commonly associated with the category — the promotion calendar, impact simulation, budgets, vendor funding, AI-generated recommendations, coupon codes — is widespread in mature products but is not what makes the application a Promotion Management system. Remove the temporality and it becomes everyday price management; remove the governed lifecycle and measurement and it becomes a discount engine inside a commerce platform; remove the offer and price mechanics and it becomes campaign management.

## Users & Context

Primary users are the commercial teams accountable for promotional outcomes:

- **Pricing analysts and promotion planners** — build promotions, define mechanics and scope, run simulations, prepare events for approval.
- **Category managers / buyers / merchandisers** — own product categories, decide which items go into promotional events, and give final approval (in some products the buyer role formally submits or approves the recommendations).
- **Pricing managers and administrators** — configure strategies, rules, mechanics libraries, and permissions.

Secondary users:

- **Marketing** — aligns promotional events with advertising and communication; the promotion defines the offer, the campaign announces it.
- **Finance** — cares about promotional budgets, margin impact, and post-event ROI.
- **Vendor/supplier partners** (grocery and consumer-goods contexts) — suppliers often fund part of retailers' promotional events; some products expose a shared record where both sides see the committed funds for an event.

The work context is a planning cadence: promotions are planned weeks to seasons ahead on a calendar, executed for a bounded window, and evaluated afterward to improve the next cycle. In B2B settings (pricing-platform deployments), the same work is done by pricing teams managing promotional discounts toward customers rather than shoppers.

## Core Model

### The defining core

**The promotion record.** The central object is a promotion: a defined offer bound to three things.

- **Mechanic** — what the offer actually is: a percentage or amount off, a fixed promotional price or price point, a multi-buy ("buy 3 pay 2"), a gift, a bundle, or a member-targeted discount. Mature products maintain a library of reusable mechanic definitions, each with its own calculation logic.
- **Product scope** — which items the promotion covers, usually selected from the merchandise hierarchy (department → category → style/item) or by rule.
- **Validity period** — an explicit start and end. Temporality is the property that separates a promotion from an everyday price: when the period ends, the promotion is over and the regular price resumes.

Optionally the record also carries a **location or customer scope** (stores, price zones, channels, customer segments) and **commercial parameters** (budget, expected lift, funding source).

**The governed lifecycle.** A promotion is not just configured — it passes through accountable states. Across the researched products the pattern is the same even though the labels differ:

```text
Draft / planned
  → reviewed / approved (named approvers, recorded decisions)
  → scheduled / active (within its validity window)
  → completed
  → evaluated (results attached to the record)
```

Approval is a first-class step, not an afterthought: promotions commit margin, so products record who approved what, keep audit histories, and lock records once approved.

**Tracked performance.** The promotion record persists after the event ends and serves as the anchor for measurement: sales and margin during the window compared against a baseline (what the items would have sold at regular price), expressed as lift, incremental revenue, margin change, or ROI. The evaluation feeds the next planning cycle.

### One structure, many implementations

The core model is conceptual; products realize each piece differently:

```text
Concept:   Offer mechanic
Implementations:  percentage-off rules, price-point ladders, condition types with
                  calculation logic, event types (temporary price reduction, ad, display),
                  multi-buy mechanics, gift/bundle values, coupon codes

Concept:   Scope
Implementations:  merchandise hierarchy selection, store/price-zone assignment,
                  customer or segment eligibility, channel scoping

Concept:   Governance
Implementations:  approval workflows with approvers and watchers, role-based privileges,
                  status locks, activity/audit logs, bilateral committed/accepted
                  states shared with funding vendors

Concept:   Distribution
Implementations:  export to a price execution system, generated price records synced to
                  ERP/CRM/CPQ/eCommerce, flighting to stores and digital channels

Concept:   Performance
Implementations:  forecast-vs-actual comparison, base vs incremental decomposition,
                  ROI and margin-change analytics, predicted-vs-actual agents
```

### What mature products add

Beyond the core, mature products commonly carry:

- **Promotion calendar** — the planning surface: active, upcoming, and historical promotions laid out over weeks or seasons.
- **Impact simulation** — expected volume lift, margin impact, and cross effects (cannibalization of related items) estimated *before* the promotion is committed.
- **Budgets** — promotional spend limits, sometimes with separate promotion and markdown budgets and allocation schemes.
- **Bulk operations** — mass updates, bulk approvals, copy/relaunch of recurring events.
- **Overlap rules** — what happens when two promotions touch the same item (stacking modes, exclusivity groups such as "at most one item of this group may be promoted per week").
- **Optimization engines** — in some products, the system does not just record human plans but *generates* recommended promotions (which items, what depth, which weeks) from demand models, which humans then review.

## How It Works

The typical loop runs from plan to proof:

```text
Plan the event
  → choose items, mechanic, dates, scope, budget
  → simulate / forecast the impact
  → submit for approval
  → activate and distribute to execution surfaces
  → the promotion runs inside its window
  → track performance while live
  → evaluate after it ends
  → feed the next planning cycle
```

**Plan.** A planner creates a promotion and fills in its definition: items (often picked from a category), the mechanic (from the library or custom), start and end dates, and where it applies. In calendar-led products this happens directly on the promotion calendar; in optimization-led products the planner instead defines a scope (season, department, zone, week), objectives (e.g., maximize revenue or gross margin), and business rules (minimum and maximum discount, minimum time between promotions on the same item, no-touch windows, exclusivity groups), and the system proposes item-level promotions that the planner reviews.

**Simulate.** Before commitment, the product estimates what the event will do: predicted lift versus the regular-price baseline, margin impact, and often cannibalization — sales shifted from untreated items onto promoted ones. Simulation is where promotion management earns its keep over a spreadsheet: the estimate is attached to the record and later compared with reality.

**Approve.** The promotion (or a batch of them) is routed through an approval workflow. Approvers can be named per step; watchers can observe; every action is logged. Once approved, the record typically locks against casual edits.

**Distribute.** An approved promotion must reach the surfaces where it actually applies. Products publish promotional prices to price execution systems (which in turn drive store POS price files), generate price records synced into ERP/CRM/CPQ/eCommerce systems, or "flight" the event to stores and digital channels. Timing matters: distribution usually needs lead time before the start date.

**Run and track.** During the window, the promotion is active: the mechanic applies at the register or in the cart. Some products track execution against the forecast while the event is still running, so underperforming events can be flagged in-season rather than discovered afterward.

**Evaluate.** After the window closes, the record is completed with actuals: sales, margin, lift versus baseline, budget consumed, and (where applicable) vendor funds claimed. Winners and under-performers are identified; the analysis seeds the next quarter's plan.

**The optimization variant.** In optimization-led products the loop is slightly different: scheduled batch runs generate recommended promotions across thousands of items; analysts review, accept, reject, or override each recommendation; approved recommendations flow to the price execution system exactly as human-authored ones would. The governance and measurement layers are identical — only the origin of the plan differs.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Promotion calendar

The planning overview.

- promotions laid out by week/period, with event types and statuses
- typical information: event name, items/categories, mechanic, dates, status, budget or funding
- primary actions: create event, move/reschedule, open detail, filter by status or category

### Promotion editor (record detail)

Where a single promotion is defined and managed.

- header with dates, scope, status, and ownership; line items for the covered products; mechanic parameters per item or group
- attachments, notes, activity/audit history, and the approval workflow with its steps and approvers
- primary actions: add items, set mechanic parameters, save draft, submit for approval, copy/revise

### Simulation / forecast view

The pre-commitment estimate.

- predicted lift, margin impact, cannibalization/cross effects, often decomposed into baseline sales versus promotion-driven sales
- primary actions: compare scenarios, adjust parameters, commit or discard

### Approval inbox / workflow

The governance surface.

- pending promotions awaiting decision, with history of prior decisions
- primary actions: approve, reject, request changes, add approver or watcher

### Performance / analytics dashboard

The evaluation surface.

- ROI, incremental versus base sales, margin change, period-over-period comparisons; per-event drill-down
- primary actions: filter by event/category/period, export, compare planned versus actual

### Administration

Configuration of the mechanic library, rules and strategies, budgets, roles and permissions, and integration mappings to execution systems.

## Important Rules / Behaviors

**Temporality governs everything.** A promotion exists inside its window. Products enforce start and end dates, and some add guardrails around them — for example minimum spacing between promotions on the same item, "no-touch" periods after an item launches or before it exits, and caps on how many promotions an item may receive per season. The regular price is the reference the promotion deviates from and returns to.

**Promotions and markdowns are different levers.** A promotion is a temporary reduction intended to drive sales during an event; a markdown is a permanent reduction for clearance or end-of-life. Products that handle both keep them as distinct objects with distinct rule sets — and coordinate them, so a clearance markdown does not undercut a planned promotion (or vice versa).

**Approval is recorded and locking.** Promotions commit real margin, so the lifecycle includes explicit approval with named accountability. Once reviewed or approved, records commonly lock: further edits require a new revision or a re-approval, and the audit trail preserves who did what.

**Overlap must be resolved deterministically.** When several promotions could apply to the same item, mature products make the resolution explicit — for example exclusivity groups ("at most one from this group") or stacking rules. Leaving this implicit produces unintended compounded discounts.

**Budgets constrain plans.** Promotional spend is budgeted; some products enforce budget limits during planning and allocate budgets across categories or periods.

**Distribution is scheduled ahead of the window.** An approved promotion must reach stores and channels before its start date; products schedule the exports or syncs accordingly.

**Evaluation compares against a baseline.** The meaningful question is not "how much did we sell" but "how much more did we sell than we would have at regular price". Products decompose results into baseline versus promotion-driven sales, and some also account for returns and cannibalization of non-promoted items.

**Vendor-funded events carry shared state.** Where suppliers fund promotions (common in grocery), the event may be bound to a committed fund balance that both the retailer and the supplier can see, with the event's status mirrored on both sides (committed / accepted) and reconciliation against claims afterward.

## Variants

- **Retail promotion management (grocery/mass shape)** — calendar of temporary price reductions, advertisements, and display events; strong vendor-funding and trade-spend dimension; weekly cadence.
- **Optimization-led promotion management** — the system generates recommended promotions from demand models and business rules; humans review and approve; common in enterprise retail pricing suites.
- **B2B pricing-suite promotions** — promotions as agreement-like documents with condition types and approval workflows, generating price records published into ERP/CPQ/eCommerce; customer-segment eligibility replaces store scope.
- **Targeted / member promotions** — offers aimed at specific customer segments or loyalty members rather than everyone; redemption becomes the success metric.
- **E-commerce-native promotions** — coupon codes and cart-level discounts managed by commerce teams; when planning, governance, and measurement are thin, this collapses into the commerce platform's discount engine rather than a full Promotion Management application.
- **Markdown-adjacent deployments** — promotion and markdown handled by one engine with separate rule sets; markdown optimization is documented as its own Application Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Retail Pricing Management | sibling, tightly coupled | owns the everyday/base price; promotion management owns temporary, event-driven deviations from it — the base price is the reference the promotion returns to |
| Markdown Optimization Application | sibling lever | markdown is a permanent reduction for clearance/end-of-life; promotion is temporary and reverts |
| Marketing Campaign Management Platform | adjacent, upstream communicator | campaigns announce and communicate; promotion management defines the offer terms, their price mechanics, and their measured price impact |
| Loyalty Program Management | adjacent | loyalty owns the member program (points, tiers, benefits); promotion management may issue member-targeted offers without running the program |
| E-commerce Platform (discount engine) | downstream executor | cart/discount engines evaluate offer conditions at checkout; they have no planning calendar, forecast, funding, approval, or post-event evaluation — promotion management feeds them |
| Trade Promotion Management (CPG-side) | mirror-image Type | the manufacturer plans and funds promotions *through* retailers; this Type is the seller running its own promotional events; bilateral products expose the same deal record to both sides |
| Deal Discovery Platform | consumer-side counterpart | aggregates existing deals for shoppers; promotion management creates the deals |

The sharpest boundary is with Retail Pricing Management: both live in pricing organizations and often share one demand model, but the promotion's defining property — a bounded, planned, measured deviation from the regular price — is exactly what the pricing application does not own.

## Representative Products

- **Oracle Retail Lifecycle Pricing Optimization Cloud Service** — enterprise retailer-side suite; optimization-run-centric promotion, markdown, regular-price, and targeted-offer recommendations with review/approval workflow and export to price execution systems.
- **Pricefx (Agreements & Promotions)** — B2B pricing platform; promotion as agreement document with condition types, approval workflow, generated price records, simulation and ROI analytics.
- **DemandTec (Revenue Optimization · Promotions)** — retailer-side, forecast-led promotion planning on a promo calendar, with a bilateral trade layer binding events to committed vendor funds.
- **Revionics (Promotions)** — retailer-side AI promotions planning and performance measurement within a lifecycle pricing suite (base price / promotions / markdown).

The definition was checked against older and simpler shapes (merchandising-system deal records, spreadsheet-and-calendar planning, temporary price files driven to POS) to avoid over-fitting it to the current AI-optimization era.

## Sources

Research date: **2026-09-06**

- Oracle Retail Lifecycle Pricing Optimization Cloud Service User Guide, Release 26.2.301.0 — https://docs.oracle.com/en/industries/retail/retail-lifecycle-pricing-optimization-cloud/26.2.301.0/ (user guide chapters: Lifecycle Pricing Optimization; LPO Workflow and User Roles; Promotion/Markdown What-If Run)
- Oracle Retail Help Center — Retail portfolio index — https://docs.oracle.com/en/industries/retail/
- Pricefx Knowledge Base — Agreements & Promotions — https://knowledge.pricefx.com/pricefx-unity-documentation/pricefx-capabilities/agreements-promotions (incl. Agreement & Promotion Documents and Detail pages)
- Pricefx — Promotions product page — https://www.pricefx.com/platform/promotions/
- DemandTec — Promotions — https://www.demandtec.com/promotions ; platform overview — https://www.demandtec.com/
- Revionics — Promotions — https://www.revionics.com/solutions/promotions
- commercetools API documentation — Cart Discounts (boundary evidence) — https://docs.commercetools.com/api/projects/cartDiscounts

> Sourcing limitations: SAP Promotion Management for Retail (help portal renders as a JavaScript shell) and Blue Yonder pricing pages (repeated 404s) could not be reached; assertions about enterprise promotion structure therefore rest on the four sampled products. DemandTec and Revionics evidence comes from official product pages rather than operational documentation, so no field-level or status-level details were taken from them. Vendor-cited market figures (e.g., shares of trade promotions that break even, share of events funded by suppliers) are recorded as vendor claims in the Research Notes and are not stated as facts in this document.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
