# Decarbonization Planning Platform

## Overview

A **Decarbonization Planning Platform** is an organization's system for planning and governing the reduction of its own greenhouse gas emissions. It anchors on the organization's measured emissions, organizes a persistent plan for getting from today's footprint to stated reduction ambitions, composes that plan from discrete reduction projects, and tracks delivery against the target trajectory over time.

The defining structure is small:

```text
Emissions evidence (the organization's own measured emissions — baseline and hotspots)
        ↓ anchors
A decarbonization plan — persistent, structured, organized toward a reduction ambition
        ↓ composed of
Discrete reduction levers / projects / initiatives (attributable, costed)
        ↓ tracked through
Recorded implementation progress (planned vs realized, over time)
```

Everything else commonly associated with these products — science-based target validation, marginal abatement cost curves, multi-year scenario simulation, initiative template libraries, AI recommendations — is widespread in current products but is not what makes the product a decarbonization planning platform. Earlier corporate and municipal climate action plans built on emissions inventories, lists of measures, and progress reporting satisfy the same defining loop without any of the modern machinery.

When the forward-looking program disappears and only the measured, auditable inventory of record remains, the product is a carbon accounting platform. When the emissions anchor is replaced by climate hazards, the same loop becomes climate adaptation planning.

## Users & Context

The primary user is the organization's sustainability or climate team, which owns the plan: maintaining the emissions baseline, setting or defending targets, building the project portfolio, and reporting progress.

Around that center:

- **finance** participates because reduction projects are capital decisions — the platform's cost and return machinery exists so sustainability and finance can agree on what to fund next;
- **operations and facility managers** own execution at the site level, where much of the decarbonization actually happens;
- **executives and boards** consume the roadmap, the target trajectory, and the investment case;
- **advisors and consultants** participate in several market realizations, either as platform staff or as external partners guiding target setting and roadmap development;
- **in the municipal variant**, department owners across a city administration carry the measures, with elected officials and the public as the accountability audience.

The work is recurring rather than one-shot: baselines are refreshed each reporting cycle, delivery is updated continuously, and the plan is revised as assumptions change.

## Core Model

### The Defining Core

```text
Emissions evidence (baseline + hotspots)
        ↓ anchors
Decarbonization plan (persistent roadmap toward a stated reduction ambition)
        ↓ composed of
Reduction levers / projects / initiatives
        ↓ tracked through
Implementation progress (planned vs realized)
```

Four properties. If any one is removed, the product is no longer recognizable as this Type:

- **Emissions evidence as the anchor** — the plan is built on the organization's own quantified emissions: a baseline and the hotspots within it. The evidence may be computed in the same product, imported from a carbon accounting system, or assembled with advisors — what matters is that the plan is anchored to the organization's real emissions rather than generic benchmarks. Without this, the product is generic strategy-execution or project-portfolio software.
- **The plan as a persistent structured artifact** — a roadmap or pathway that organizes how the organization moves from the baseline toward its reduction ambition over years. It survives sessions and reporting cycles, is edited as circumstances change, and is the single reference for what the organization has committed to. Without it, the product is hotspot analytics or a target dashboard.
- **Discrete reduction levers as managed records** — the individual projects, initiatives, or measures through which reduction happens (an energy-efficiency retrofit, a fuel switch, a supplier change, a fleet electrification). Each is identifiable and attributable, commonly carries an expected abatement amount and cost, and is drawn from a curated library or authored custom. Without them, the product is target-setting tooling.
- **Recorded implementation progress** — status, ownership, and realized reductions maintained over time, compared against what the plan promised. Reductions are projections until delivered; the platform keeps the difference visible. Without this, the product is a one-shot plan document.

### Capabilities Shared by Mature Products

These are standard in the current market but do not define the Type:

- **Target machinery** — formal reduction targets as the plan's destination: science-based or custom, absolute or intensity-based, near-term and net-zero horizons, consolidated top-down or bottom-up across scopes, regions, and entities. Validation against science-based target frameworks is a common service layer.
- **Financial modeling of levers** — project-level capital and operating cost, investment metrics (return, payback), and cost per tonne abated, so levers can be compared as investments.
- **Abatement-cost prioritization** — ranking levers by cost-effectiveness and impact; the marginal abatement cost curve is the best-known realization.
- **Scenario and pathway modeling** — multi-year simulation of alternative lever mixes against the target, including sensitivity to carbon prices and business forecasts.
- **Lever libraries and templates** — curated catalogs of industry-typical reduction initiatives that organizations adapt to their own operations.
- **Hotspot analysis** — identification of the highest-emission activities that the plan should target first.
- **Multi-level structure** — facility- or site-level plans that roll up into the corporate roadmap; entity and regional consolidation.
- **Progress dashboards** — planned versus realized reductions, forecasts, and alerts against the target trajectory.
- **Cross-functional collaboration** — assignment of levers to owners across sustainability, finance, and operations.
- **Reporting outputs** — transition-plan documents and disclosure-ready progress narratives derived from the plan.

### One Structure, Many Implementations

The core model is written conceptually. Realizations differ on where the emissions anchor comes from, how levers are quantified, and who does the work:

```text
Emissions anchor:      computed in-product, imported from a carbon accounting
                       system, or assembled with advisors
Lever economics:       full investment modeling with abatement-cost curves,
                       lighter cost/benefit comparison, or advisor judgment
Planning philosophy:   abatement-economics-led, target-led, energy-data-led,
                       or plan-led (municipal climate action planning)
```

A reader who encounters only one realization — say, a finance-grade enterprise platform with abatement cost curves — should still be able to recognize a municipal climate action plan tool or an advisor-led target-setting product as the same Type from the core model.

## How It Works

### Anchor the plan in measured emissions

```text
Establish or refresh the emissions baseline
  (in-product calculation, import from carbon accounting, or advisor-supported)
→ identify hotspots: the activities and units that dominate the footprint
→ the plan will be built from this evidence, not from benchmarks
```

### Commit to an ambition

```text
Set or adopt reduction targets
  (science-based or custom; absolute and/or intensity; near-term and net-zero)
→ consolidate targets across scopes, regions, and entities
→ the gap between baseline and target defines what the plan must close
```

### Compose the plan

```text
Identify candidate levers (library templates and/or custom projects)
→ quantify each: expected abatement, cost, timing, dependencies
→ model scenarios: multi-year pathways, carbon-price sensitivity, alternative mixes
→ prioritize: rank by cost-effectiveness and impact against budget
→ sequence the selected levers into the roadmap by year, site, and owner
```

### Execute and track

```text
Assign owners and schedules
→ record status as work proceeds
→ compare planned outcomes with realized emissions reductions and savings
→ forecast whether the target trajectory still holds
```

### Close the loop

```text
Review variance between plan and delivery
→ revise the plan (add, accelerate, or replace levers)
→ report progress to executives, regulators, and stakeholders
→ repeat each planning cycle
```

### Core vs standard vs optional

**Defining core** — without these, not a decarbonization planning platform:

- emissions evidence anchoring the plan
- the persistent plan artifact organized toward a reduction ambition
- discrete managed reduction levers
- recorded implementation progress over time

**Standard capabilities** — present in most mature products:

- target machinery (science-based alignment, target types, consolidation)
- financial modeling and abatement-cost prioritization
- scenario and pathway modeling
- lever libraries and hotspot analysis
- multi-level planning with roll-up
- progress dashboards and collaboration
- transition-plan reporting

**Optional / variant** — depends on segment and realization:

- integrated climate plans carrying adaptation beside mitigation (municipal)
- energy-data-led planning built on utility and meter data
- advisor-coupled delivery (named experts, consultancy services)
- supplier and value-chain engagement programs
- beyond-value-chain contribution (credits, climate financing)
- public transparency pages
- AI assistance

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Baseline / hotspot view

The evidentiary starting point.

- emissions by scope, business unit, site, and activity over time
- primary actions: drill into hotspots, export, hand off to plan building

### Target-setting surface

Where the ambition is defined and defended.

- target types, horizons, scope coverage, consolidation across the organization
- primary actions: create/adjust targets, test against science-based pathways, submit for validation where used

### Lever / project portfolio

The plan's inventory of candidate and committed actions.

- each lever with abatement estimate, cost, timing, owner, status
- primary actions: add from library or custom, quantify, assign, group into the roadmap

### Prioritization view

Where levers are compared as investments.

- cost-effectiveness ranking (abatement cost curve or equivalent), budget views, portfolio totals
- primary actions: compare, select, fund, defer

### Scenario / pathway modeler

Where the plan is stress-tested.

- multi-year simulation of lever mixes against the target; assumption controls (carbon price, business growth)
- primary actions: run scenarios, compare pathways, promote a scenario to the plan

### Roadmap / plan timeline

The plan of record.

- levers placed over years, grouped by site, theme, or owner; revisions retained
- primary actions: sequence, reschedule, revise, publish internally

### Progress dashboard

The delivery view.

- planned vs realized reductions, status of levers, trajectory against target, alerts
- primary actions: update status, review variance, generate reports

### Reporting / export

- transition-plan and disclosure-ready outputs assembled from the same data spine

In the municipal variant, a **public plan page** publishes the plan and its progress to citizens.

## Important Rules / Behaviors

### The plan must reconcile with the inventory

The plan's numbers are anchored to the organization's measured emissions. Mature products keep baseline, footprint, disclosures, and reduction plan on one data spine so the plan cannot drift from the inventory; plans built on generic benchmarks are explicitly rejected by the market's own framing.

### Reductions are projections until delivered

A lever's abatement is a modeled expectation. The platform's tracking discipline is the comparison of planned outcomes with realized reductions once the inventory reflects the work — the gap between the two is a first-class object, not an embarrassment to be hidden.

### Targets constrain the plan

The plan exists to close the gap between baseline and target. Scenario modeling tests whether a lever mix can close it; if delivery slips or assumptions change, the plan is revised — the roadmap is a living artifact, not a one-time document.

### Capital allocation is part of the workflow

Levers carry cost, and choosing among them is an investment decision. The financial machinery (project economics, budget views, abatement-cost ranking) exists so that sustainability, finance, and operations converge on what to fund.

### Multi-level consistency

Site- and entity-level plans must roll up to the corporate roadmap without contradiction; consolidation works top-down and bottom-up, and dependencies between levers are representable.

### Within value chain, by default

The defining scope is the organization's own emissions and its value chain. Offsets and beyond-value-chain financing are adjacent capabilities — some products carry them as separate modules, but the planning core is about reducing the organization's own emissions.

## Variants

- **Abatement-economics-led enterprise platforms** — finance-grade project modeling, abatement cost curves, carbon-price scenarios; typical of heavy industry and capital-intensive sectors.
- **Carbon-accounting suite modules** — planning delivered as the forward-looking module of a measurement platform, sharing the same emissions data spine.
- **Target-led, advisor-coupled platforms** — science-based target development and validation services at the center, with scenario analysis in the platform and expert staff carrying the planning work.
- **Energy-data-led enterprise suites** — planning built on utility-bill and interval-meter analytics with program tracking; decarbonization realized as energy management plus initiative portfolios.
- **Municipal climate action planning** — plan-first products for cities: a measures database (mitigation, often alongside adaptation), prioritization by cost and co-benefit, progress tracking, and public transparency pages; frequently grouped across municipalities in regional programs.
- **Consultancy-coupled SaaS** — the platform sold with expert services (roadmap development, target setting) as part of the delivery model.

A variant remains a variant unless it changes the core objects or workflow; the municipal pole keeps the same loop and differs in audience, content breadth, and public accountability.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Carbon Accounting Platform | complementary halves, commonly one suite | accounting's defining loop ends at a measured, auditable inventory of record; this Type starts from that inventory and governs the forward reduction program. Remove the plan, levers, and tracking → carbon accounting. |
| Climate Adaptation Planning | structural sibling | the same planning loop anchored on climate hazards and adaptive capacity instead of emissions and reduction levers. One product can carry both domains in a single climate plan (observed in municipal platforms). Replace the emissions anchor with a hazard anchor → adaptation planning. |
| Climate Risk Management | adjacent | keeps a risk process alive over an exposure population (assessments, prioritization, disclosure); this Type governs a reduction program over emission sources. |
| Climate Scenario Analysis | upstream machinery | projects alternative futures for comparison; holds no managed plan or levers. This Type consumes scenario-class machinery as one capability. |
| Energy & Carbon Management | adjacent | centers organization-wide energy and carbon data operations; this Type centers the strategic reduction program. Enterprise suites blend the two; the managed plan/program object is the seam. |
| Building Energy Management | adjacent | building-scoped operational energy control; no organization-wide reduction program. |
| Sustainability / ESG Management Platform | broader | manages wider environmental, social, and governance data and disclosure; the emissions-reduction program is one topic among many. |
| Carbon Credit Management | adjacent | credits are beyond-value-chain instruments with registries and retirement; this Type governs within-value-chain abatement. |
| Strategic Plan Execution / Government Performance Management | generic machinery carrier | the same plan→actions→tracking loop without emissions content; the emissions anchor is the Type boundary. |
| Product Carbon Footprint / LCA | adjacent | unit of account is the product, not the organization's reduction program. |

The boundary with the Carbon Accounting Platform is the most important one, because the two are usually sold together: measurement is the backward-looking system of record; planning is the forward-looking program that consumes it. The boundary with Climate Adaptation Planning is the subtlest: identical loop, different anchor — and some products legitimately carry both.

## Representative Products

- SINAI Technologies (Reduce module — abatement-economics-led enterprise planning)
- Persefoni (Net-Zero Navigator — planning module on a carbon accounting ledger)
- Sweep (Decarbonization Strategy — targets, initiatives, scenarios, and budget modeling on one data spine)
- Normative (target-setting-led, advisor-coupled platform)
- Futureproofed (integrated climate action planning for cities; carbon management for business)
- IBM Envizi (energy-data-led decarbonization module family in an enterprise ESG suite)

The core model was checked against pre-SBTi practice and the municipal climate-plan tradition to avoid over-fitting to the current finance-grade enterprise pattern.

## Sources

Research date: **2026-09-07**

Primary vendor surfaces (official product pages):

- SINAI — https://www.sinai.com/ , https://www.sinai.com/platform/reduce
- Persefoni — https://www.persefoni.com/business/decarbonization-management
- Sweep — https://www.sweep.net/ , https://www.sweep.net/decarbonization-strategy
- Normative — https://normative.io/ , https://normative.io/platform/sbti/
- Futureproofed — https://www.futureproofed.com/products/business (Cities-platform observations from the same-date climate-adaptation-planning research)
- IBM Envizi — https://www.ibm.com/products/envizi/decarbonization

> Sourcing limitation: live help-center / user-manual documentation was not reachable for any sampled product; all findings rest on official product pages. Operational details (exact lever states, approval flows, numeric limits, vendor-published statistics) are intentionally not stated in this document. A dedicated municipal transition-planning product attempted for the sample was unreachable; the municipal variant rests on one sampled product. Claims are calibrated accordingly.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
