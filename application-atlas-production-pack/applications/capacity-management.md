# Capacity Management

## Overview

A **Capacity Management** application is IT-operations software that keeps infrastructure supply ahead of demand. It maintains a picture of the organization's capacity-bearing resources — compute, memory, storage, network bandwidth, and their container/cloud equivalents — tracks how much of each is actually consumed over time, and continuously answers the question the practice exists for: *how much headroom is left, and when will demand reach the limits?*

On top of that assessment, it supports the decisions that follow: adding capacity before it runs out, reclaiming capacity that is provisioned but unused, resizing or rebalancing workloads, and evaluating planned changes (growth, migrations, consolidations) before committing to them. Some products stop at advisory output — dashboards, forecasts, recommendations, reports; others close the loop and execute optimization actions automatically under guardrails.

The boundary is easy to state: a monitoring system tells you what is happening now; a capacity management system tells you what is *about to happen* to your resource supply, and what to do about it. When the forward-looking, supply-vs-demand planning layer is removed, what remains is infrastructure monitoring; when resource limits and headroom are removed and only spend remains, what remains is cloud cost management.

## Users & Context

Primary users:

- **Capacity planners / capacity managers** — the core audience. They review utilization trends and forecasts across the estate, decide when and where to add capacity, and justify procurement with evidence. In many organizations this role sits inside infrastructure or IT operations teams rather than being a separate job title.
- **Infrastructure / platform operations engineers** — use capacity views and recommendations in daily operations: checking cluster headroom, acting on right-sizing suggestions, investigating resources that are running hot or idle.
- **IT operations managers / CIO-level reporting consumers** — receive scheduled capacity reports and dashboards used for budget cycles, procurement approvals, and risk reviews.

Secondary users:

- **Cloud / FinOps teams** — consume the cost side of capacity analysis (cost of recommended changes, cost-and-capacity comparisons) and coordinate on right-sizing and commitment decisions.
- **Application owners** (in some organizations) — consulted about workload growth assumptions and placement decisions.

The work context is periodic and continuous at once: forecast runs and planning reviews happen on a cadence (weekly/monthly/quarterly, or overnight analysis cycles in some products), while utilization tracking, alerting, and — where automation exists — optimization run continuously.

## Core Model

The world of a capacity management application is built from a small set of structures.

### The defining core

```text
Capacity-bearing resource (with limits)
    └── Consumption observed over time
        └── Capacity position (headroom now)
            └── Capacity risk (projected demand vs limits)
                └── Capacity decision (add / reclaim / resize / rebalance / migrate)
```

- **Capacity-bearing resource** — the managed unit of supply: a host, cluster, storage array or volume, network link, virtual machine, container workload, cloud service allocation, or GPU pool. Each carries a notion of *total capacity* and, in most products, a notion of *usable capacity* — what is actually available after reservations, high-availability buffers, or policy-set headroom are subtracted. The distinction matters: a cluster whose raw capacity is fully allocated may still have usable headroom, and vice versa.
- **Consumption over time** — utilization measurements collected from the resources through integrations, collectors, or agents, retained as history. History is the raw material of everything else: without it there are no trends, no forecasts, and no evidence for recommendations.
- **Capacity position** — the current comparison of consumption against limits: how much headroom remains on each resource, expressed in resource units or percentages.
- **Capacity risk** — the forward-looking extension of position: where the demand trend is heading and when it will cross the usable limit. Products express this as projected exhaustion ("time remaining" before resources run out), risk levels derived from conservative vs aggressive projections, or forecast results of the form "these datastores may reach their usage limit within N days."
- **Capacity decision** — the action the assessment exists to inform: procure/add capacity, reclaim or right-size overprovisioned resources, rebalance or move workloads, or accept the risk. The application's output — recommendations, scenario results, reports — is decision support; in automation-oriented products the decision can also be executed by the system itself under policy guardrails.

### Standard capabilities of mature products

These are widespread across the researched market but are not what makes a product a capacity management application:

- **Utilization and capacity dashboards** — estate-wide and per-resource views of usage trends, headroom, and hot spots, often organized by data center, cluster, environment, or service.
- **Capacity alerts** — threshold-based warnings that fire while there is still time to act, typically keyed to a warning window before projected exhaustion rather than at the moment of failure.
- **Forecasting engine** — projects future demand from historical consumption. Implementations vary (trend regression, periodic/seasonal pattern detection, percentile-based projections), and products commonly expose tuning: forecast thresholds, the percentile a projection is based on, or — in some engines — a conservative-vs-aggressive risk posture.
- **Right-sizing and reclaim recommendations** — identification of overprovisioned or idle resources with suggested reductions, and of undersized resources with suggested additions. Recommendations are typically bounded so that a single suggestion cannot radically reshape a resource.
- **Placement guidance** — where a new workload should be deployed so that it fits without unbalancing existing capacity (cluster/array selection based on historical usage patterns).
- **Scenario / what-if planning** — simulation of hypothetical changes: adding or removing workloads, adding or removing capacity, migrating workloads to other platforms or clouds — with results showing whether the plan fits, what remains, and often what it costs.
- **Policies** — the configuration layer that governs how capacity is computed and acted on: which metrics count as demand, what thresholds trigger alerts, how aggressive projections are, and what automation may do.
- **Data acquisition layer** — integrations, management packs, or collectors that pull inventory and utilization from hypervisors, storage arrays, network devices, cloud accounts, or Kubernetes clusters.
- **Reports** — scheduled, shareable snapshots of capacity views for planning and management audiences.
- **Cost dimension** — attaching cost to capacity: cost of idle/overprovisioned resources, cost of recommended changes, cost-and-capacity comparison of migration targets, chargeback context.

### One structure, many implementations

The core model is conceptual; products realize it differently:

```text
Concept:  Capacity-bearing resource with limits
Implementations:  virtualization clusters/hosts/datastores; storage arrays and
                  volumes; network links/ports; Kubernetes nodes and workload
                  requests/limits; cloud service allocations; GPU pools

Concept:  Consumption over time
Implementations:  platform-integrated metric collection; deployed collectors/
                  agents; cloud provider metrics; in-cluster metrics pipelines

Concept:  Capacity risk
Implementations:  projected exhaustion dates ("time remaining"); forecast runs
                  with thresholds and percentiles; recommendation engines that
                  anticipate demand from recent usage patterns

Concept:  Capacity decision
Implementations:  advisory reports/recommendations; approval-gated change
                  suggestions; automated resizing/placement with guardrails
```

A reader who has only seen one implementation — say, a Kubernetes right-sizing tool — should still be able to recognize a classic virtualization capacity planner, or a storage-array capacity forecaster, as the same application type.

## How It Works

The canonical loop runs in six stages. Products differ in which stages they automate and how deeply, but the loop itself is stable.

### 1. Connect and inventory

The application is connected to the environments whose capacity matters — virtualization platforms, storage arrays, network devices, cloud accounts, Kubernetes clusters — through integrations or deployed collectors. It discovers the capacity-bearing resources, builds the inventory, and begins recording utilization. From this point the system holds both sides of the comparison: limits (what exists) and consumption (what is used).

### 2. Assess the current capacity position

For each resource (and aggregates of them), the system compares consumption against usable capacity: how much headroom remains, which resources are running hot, which are overprovisioned or idle. This is the "where are we now" layer, surfaced in capacity dashboards and per-resource capacity views.

### 3. Project demand

The forecasting layer evaluates the consumption history and projects it forward against the limits. Mature implementations distinguish kinds of usage history — one-off spikes, sustained shifts, and recurring/seasonal patterns — and choose projection behavior accordingly, often offering a risk posture (conservative projections plan for the worst case; aggressive ones for the expected case). The output is capacity risk: projected exhaustion dates, saturation warnings, or the demand assumptions behind recommendations.

### 4. Decide

The system turns assessment and projection into decision support:

- **Add capacity** — forecasts and alerts identify resources that will run out; scenario planning can validate how much to add and where.
- **Reclaim / right-size** — recommendations identify idle or overprovisioned resources whose capacity can be recovered, and undersized resources that need more.
- **Rebalance / place** — placement guidance and workload-balancing suggestions distribute demand across available supply.
- **Migrate / consolidate** — scenario comparisons evaluate candidate targets on both capacity fit and cost.

### 5. Act

In advisory products, the decisions leave the application as reports, tickets, or manual changes. In automation-capable products, the system executes approved optimization actions itself — resizing workload allocations, moving workloads, adjusting placements — under guardrails: disruption budgets, quota and policy compliance, validation that the target can absorb the change, and pause windows while the system re-learns after application changes. Some products additionally suspend automation automatically when repeated changes fail to stabilize a workload.

### 6. Report and repeat

Dashboards, alerts, and scheduled reports keep the planning audience informed; the utilization record keeps growing, which sharpens the next forecast. The loop is continuous.

### Core vs common vs optional

- **Defining core**: capacity-bearing resources with limits; consumption observed over time; demand-vs-capacity assessment including forward-looking risk; decision support for capacity actions.
- **Standard capabilities**: dashboards, alerts, forecasting engines, right-sizing/reclaim recommendations, placement guidance, scenario planning, policies, data acquisition, reports, cost dimension.
- **Optional / variant**: automated execution of optimization actions; migration cost comparison; chargeback; GPU/AI-specific capacity; physical-data-center adjacency.

## Interfaces

The surfaces below are described conceptually; names and layouts vary by product.

### Capacity overview / dashboard

The estate-level entry surface.

- Typical information: capacity position and risk across data centers, clusters, arrays, or environments; consumption trends; resources approaching limits; reclamation opportunities.
- Primary actions: drill into a resource, open forecasts or recommendations, configure views.

### Resource capacity detail

The per-resource view (a cluster, array, host, or workload).

- Typical information: usage history and trend lines, total vs usable capacity, current headroom, projected exhaustion or risk indicators, per-dimension breakdowns (CPU, memory, storage, network).
- Primary actions: inspect forecasts, accept or export recommendations, configure thresholds for this resource.

### Recommendations / reclaim views

The action-oriented surface.

- Typical information: lists of overprovisioned, idle, or undersized resources with suggested changes and (often) associated savings.
- Primary actions: review evidence, apply a recommendation (manually or via automation), dismiss or defer.

### Scenario / what-if workspace

The planning surface.

- Typical information: scenario definitions (workloads or capacity to add/remove, migration targets), fit/no-fit results, projected remaining capacity and time, cost estimates where supported.
- Primary actions: create and run scenarios, compare targets, save or share results.

### Policy / configuration

The governance surface.

- Typical information: which metrics define demand, risk posture, thresholds, automation scope and constraints, data-source connections.
- Primary actions: edit policies, manage integrations, set alert rules.

### Reports

- Typical information: scheduled snapshots of capacity views for planning audiences.
- Primary actions: schedule, generate, distribute.

### Automation status (automation-capable products)

- Typical information: which resources are under automation, recent changes applied, change history with before/after utilization context, paused or excluded workloads.
- Primary actions: enable/disable automation per scope, review and audit changes.

## Important Rules / Behaviors

- **Usable capacity is not total capacity.** Reservations, high-availability buffers, and policy-set headroom reduce what is actually available. Capacity conclusions that ignore this distinction are wrong in both directions — and products make the usable-capacity definition explicit precisely because it drives every risk number.
- **"Well balanced" and "about to run out" are different verdicts.** A resource can be optimally balanced across its members and still be close to exhaustion; optimization health and exhaustion risk are separate measures, and mature products surface both rather than conflating them.
- **How demand is counted changes the answer.** Consumption-based assessment (what workloads actually use) and commitment-based assessment (what workloads are allocated, including overcommit ratios) produce different headroom and risk figures. Products typically default to one model and allow the other; the choice is a policy decision, not a technical detail.
- **Not all peaks matter equally.** Some forecasting engines distinguish momentary spikes (which do not justify new capacity) from sustained shifts and recurring seasonal patterns (which do). A forecast that treats every spike as demand would chronically overprovision.
- **Forecasts are only as good as their history.** Products require a minimum span of utilization history before projections are trusted, and may restrict or gradually ramp automated actions for resources with thin history.
- **Recommendations are bounded.** Right-sizing suggestions are typically capped relative to current allocations so that a single recommendation cannot radically reshape a resource — a deliberate conservatism that users can rely on.
- **Alerts lead exhaustion.** Capacity warnings are keyed to warning windows before projected limits are crossed, because the corrective actions (procurement, migration) take time.
- **Automation is guarded.** Where products execute optimization actions, they do so under disruption budgets, quota and policy compliance, target-capacity validation, and learning pauses after application changes; some also suspend automation automatically, with a cooldown, when repeated changes fail to stabilize a workload.

## Variants

Common forms of the type. A variant remains a variant unless it changes the core users, objects, or loop so much that the model above no longer applies.

- **By product form**
  - feature area of an infrastructure operations platform (capacity optimization inside a broader monitoring/ops suite)
  - standalone capacity analytics suite focused on deep resource coverage (storage arrays, network, OS)
  - SaaS optimization service for cloud/container estates
  - in-cluster controllers that optimize capacity where the workloads run
- **By scope**
  - virtualization/data-center capacity (clusters, hosts, datastores)
  - storage capacity (arrays, volumes, dedup/compression effects)
  - network capacity (links, ports, bandwidth)
  - Kubernetes/container capacity (workload requests, node pools)
  - cloud capacity (service allocations, accounts, regions)
  - GPU/AI infrastructure capacity
- **By posture**
  - advisory (forecasts, recommendations, reports; humans act)
  - continuous optimization (system applies changes under guardrails)
- **By cadence**
  - periodic planning (scheduled forecast runs, overnight analysis, quarterly reviews)
  - continuous recalculation (always-current projections and recommendations)
- **By business alignment**
  - pure capacity view
  - cost-and-capacity view (savings estimates, migration cost comparison, chargeback context)

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Infrastructure Monitoring / Metrics Monitoring | closest neighbor; data feeder | observes current state and detects incidents; no supply-vs-demand projection or capacity planning. Capacity tools consume monitoring-style data and are often bundled inside the same platform |
| Cloud Cost Management / FinOps | adjacent, overlapping | centers on spend (billing, commitments, unit economics); capacity management centers on resource limits, headroom, and exhaustion. Right-sizing and commitment planning are shared ground |
| Data Center Infrastructure Management (DCIM) | adjacent, physical layer | manages physical facility capacity (power, cooling, space, racks); capacity management handles logical IT resource capacity |
| AIOps Platform | adjacent | correlates events and anomalies to reduce noise and speed diagnosis; capacity management does deterministic demand-vs-supply projection. ML appears in both, for different purposes |
| Kubernetes Management Platform / Virtualization Management / Server Management | adjacent, lifecycle-focused | manage configuration and lifecycle of resources; capacity management plans supply vs demand over time. Management platforms may bundle capacity views |
| Load Testing Platform | methodological opposite | generates synthetic demand at a point in time to probe limits; capacity management observes real demand over time and projects it |
| IT Service Management (ITSM) | process governance | may govern the capacity practice (reviews, change approval); does not perform the analytics |
| Bed & Capacity Management (healthcare) | name collision only | manages hospital bed capacity — a different domain and a different Application Type despite the shared term |

The sharpest boundary is with infrastructure monitoring: the test is whether the system projects demand against limits and supports capacity decisions. Remove that, and the product is a monitor; remove current-state observation, and capacity management has nothing to work with.

## Representative Products

- **VMware Aria Operations** — capacity optimization as a feature area of a virtualization operations platform; capacity engine with time-remaining/capacity-remaining outputs, reclaim, workload optimization, and what-if scenario planning (including migration comparisons). Documentation now published under Broadcom TechDocs; the capability line continues in VMware Cloud Foundation operations.
- **Virtana Infrastructure Observability** — hybrid-infrastructure capacity analytics with deep storage/compute/network coverage; named capacity analytics (forecast, deployment advisor, capacity auditor) plus cross-domain cost-and-capacity dashboards.
- **Cast AI** — Kubernetes cloud optimization; continuous automated right-sizing of workload resources under scaling policies with safety machinery (disruption budgets, quota compliance, confidence gating).
- **Kubex (Densify)** — autonomous resource optimization for Kubernetes and AI/GPU infrastructure; historical-usage analytics, recommendations, and guardrail-based automation.

The classic standalone capacity-suite category (e.g., ServiceNow Capacity Optimization, BMC TrueSight Capacity Optimization) could not be documented from public sources during research; the type definition above does not depend on any single vendor's implementation.

## Sources

Research date: **2026-09-06**

- Broadcom TechDocs — VMware Aria Operations 8.18 Configuration Guide, "Optimizing Capacity and Improving Performance" chapter (concepts, capacity engine and forecasting, demand/allocation models, viewing/assessing capacity, what-if planning): https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-operations/8-18.html
- Virtana Docs — Infrastructure Observability User Guide, "Predictive Capacity Management Analytics" (Capacity Forecast, VM Deployment Advisor, Capacity Auditor) and Virtana Platform capacity-forecasting workflow: https://docs.virtana.com/
- Cast AI documentation — platform overview and Workload Autoscaler (recommendations, scaling policies, apply modes, safety mechanisms): https://docs.cast.ai/
- Kubex (Densify) documentation — platform overview, data collection, automation engine: https://docs.kubex.ai/ , https://docs.densify.com/
- Virtana product pages (positioning): https://www.virtana.com/
- Flexera/Spot documentation (FinOps boundary context only): https://docs.spot.io/

> Sourcing limitation: official documentation for several classic capacity-management vendors could not be reached from the research environment on 2026-09-06 (ServiceNow docs JavaScript-gated after product-page timeouts; BMC docs returned access errors; IBM docs returned access errors). The type definition rests on the four reachable representatives; no vendor-specific defaults, numeric limits, or thresholds from unreachable products are asserted anywhere in this document. Precise product-specific figures observed in reachable documentation (projection windows, caps, cycle times, minimum history spans) were deliberately kept out of this document and remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample breadth check are recorded in the paired Research Notes.
