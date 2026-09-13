# Research Notes — Capacity Management

Slug: capacity-management
Research date: 2026-09-06
Directory location: §14 IT, Cloud & Infrastructure (C. Digital Technology Systems)

## Research Goal

Understand what "Capacity Management" software is in the IT/cloud infrastructure context: what objects it models, how utilization data enters, how demand-vs-capacity assessment and forecasting work, what planning/optimization outputs exist, who uses it, and where its boundaries lie against monitoring, FinOps, DCIM, AIOps, and management platforms.

## Initial Boundary

- Assumed: this leaf is the IT-operations capacity management practice (long-standing ITIL-associated discipline) realized as software — tracking IT resource consumption against limits, projecting future demand, and planning/optimizing capacity.
- NOT the healthcare "Bed & Capacity Management" leaf (§22, already processed as bed-capacity-management) — same word, different domain.
- Nearest neighbors: Infrastructure Monitoring, Metrics Monitoring, Cloud Cost Management / FinOps, DCIM, AIOps Platform, ITOM, Kubernetes Management Platform, Load Testing Platform.
- Initial unknowns: exact object models per product; whether forecasting is definitional or merely common; how much automation is standard; how cost enters; whether the classic standalone capacity-suite pole is still separable from ops platforms.

## Research Questions

1. What are the core objects (resources, clusters, services, clouds, plans)?
2. How does utilization data enter the system (integrations, collectors, agents)?
3. How are capacity limits defined (discovered, configured, policy-set)? What is "usable" capacity?
4. How is forecasting exposed (time-to-exhaustion, ranges, risk levels, models)?
5. What do recommendations look like (right-size, reclaim, place, add capacity)?
6. What does scenario/what-if planning do?
7. How are capacity alerts and policies defined?
8. Who uses it and on which interfaces?
9. Where does cost enter, and where is the FinOps boundary?
10. Advisory vs automated: how much execution is standard?
11. What scope variants exist (virtualization, storage, network, K8s, cloud, GPU)?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, different customer layers:

1. **VMware Aria Operations 8.18** (Broadcom TechDocs) — ops-platform pole; capacity optimization as a feature area of a virtualization operations platform; enterprise virtualization. Note: product is being folded into VMware Cloud Foundation (VCF) Operations; 8.18 is the last standalone docs generation.
2. **Virtana Infrastructure Observability (IO)** (docs.virtana.com) — hybrid-infrastructure capacity analytics pole; deep storage/compute/network integrations; classic capacity analytics (forecast, deployment advisor, auditor) inside an observability platform.
3. **Cast AI** (docs.cast.ai) — Kubernetes cloud optimization pole; continuous automated right-sizing/autoscaling with cost framing.
4. **Kubex (Densify)** (docs.kubex.ai) — autonomous resource optimization pole (Densify's current product line); K8s + AI/GPU infrastructure; recommendations + guardrail-based automation.

Attempted but unreachable (recorded, not retried beyond limits):
- ServiceNow Capacity Optimization — servicenow.com product page timed out ×2; docs.servicenow.com JS-gated ("Loading application..."). No claims made.
- BMC TrueSight Capacity Optimization — docs.bmc.com 403. No claims made.
- IBM Turbonomic — ibm.com/docs 403. No claims made.
- ScienceLogic — docs.sciencelogic.com returned empty. No claims made.
- Spot by NetApp (docs.spot.io, now Flexera docs) — reachable but positioned as cost/commitment optimization (Ocean/Elastigroup/Eco); used as FinOps boundary context only, not a representative.
- Wikipedia "Capacity management" — timed out ×1; no ITIL-specific structural claims asserted anywhere.

## Sources

Tier-1 (fetched successfully, 2026-09-06):

- Broadcom TechDocs — VMware Aria Operations 8.18 Configuration Guide:
  - Optimizing Capacity and Improving Performance (chapter)
  - Capacity Optimization Concepts
  - How Does Capacity Optimization Work
  - How Does VMware Aria Operations Calculate and Forecast Capacity
  - Allocation and Demand Model in Workload Optimization
  - How to View and Assess Capacity (+ sub-pages listed)
  - How to Plan for Capacity Changes (+ What-If sub-pages listed)
  - Configuration Guide TOC (policies, data sources, dashboards, reports, cost, alerts)
  - URLs under https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-operations/8-18/
- Virtana Docs:
  - IO User Guide → Analytics → Predictive Capacity Management Analytics (+ Capacity Forecast page)
  - IO User Guide TOC (per-integration Capacity Forecast / Capacity Auditor; Health, Utilization, Capacity, and Performance concepts)
  - Virtana Platform workflows TOC ("Planning for the future: Capacity forecasting and resource optimization")
  - Global View dashboards TOC (On-Premises Compute Cost and Capacity; Storage Array Cost and Capacity Summary)
  - URLs under https://docs.virtana.com/en/
- Cast AI docs:
  - https://docs.cast.ai/ (platform overview)
  - https://docs.cast.ai/docs/workload-autoscaling-overview.md (Workload Autoscaler)
  - https://docs.cast.ai/llms.txt (section index)
- Kubex (Densify) docs:
  - https://docs.densify.com/ → Kubex Overview
  - https://docs.kubex.ai/docs-kubex/Content/Kubex/Data_Collection_Overview
  - https://docs.kubex.ai/docs-kubex/Content/Kubex/Automation_Overview

Tier-2 (positioning only):

- https://www.virtana.com/ (platform positioning; capacity forecasting listed under Infrastructure Observability)
- https://docs.spot.io/ (Flexera/Spot product family — FinOps boundary context)

## Product A — VMware Aria Operations 8.18

### Key observations (evidence layer A unless noted)

- Capacity Optimization is a named key feature area: "efficiently utilizing and managing resources within a virtualized infrastructure... maintain optimal performance and maximize utilization while ensuring capacity remains within acceptable limits."
- Four integrated functions: **Overview, Reclaim, Workload Optimization, What-If Scenarios**.
- Explicit audience framing: "Capacity planners must assess whether physical capacity is sufficient to meet current or forecasted demand."
- **Capacity engine**: inputs = Demand and Usable Capacity metrics; outputs = **Time Remaining** (days until projected utilization crosses the usable-capacity threshold), **Capacity Remaining**, **Recommended Size**, **Recommended Total Capacity**.
- Usable capacity = total capacity excluding HA settings.
- Projection window 1 year; engine consumes data points every 5 minutes (product-specific numbers).
- **Risk levels**: conservative (upper-bound projection) vs aggressive (mean of upper/lower bounds) — configured in policy.
- **Utilization peaks** classified: momentary (ignored), sustained (decaying impact), periodic (cyclical patterns, overlapping cycles detected).
- **Projection models**: linear (linear regression, ARMA) and periodic (FFT, pulses, wavelets); engine picks best fit; projection range covers ~90% of future points; historical window is exponential-decay (recent data weighted more).
- Forecast in trend views: change-point detection + linear regression + cyclical analysis.
- **Recommended Size caps** (product-specific): oversized reclaim capped at 50% of currently allocated; undersized addition capped at 100% of currently allocated.
- **Demand model vs Allocation model**: demand model (actual consumption-based) is default and always affects capacity calculations; allocation model (overcommit ratios per object type: cluster compute resource CPU/memory/disk, datastore, datastore cluster) is optional per policy; if utilization exceeds the allocation ratio, Capacity Remaining becomes zero.
- **Policy settings for capacity**: policies on objects/object groups define custom metrics (incl. super metrics) for capacity calculations, symptom thresholds, alerts, recommendations, risk levels.
- **Views**: Capacity page (workload status + capacity remaining across data centers); per-object Capacity tab (Time Remaining + Capacity Remaining); predefined capacity dashboards (resource consumption trends, utilization patterns, potential bottlenecks; plan for growth).
- **Reclaim**: identify underutilized/overprovisioned VMs, reclaim idle CPU/memory, calculate potential cost savings.
- **Workload optimization**: move workloads across datastore clusters / data centers; policies define contention thresholds that trigger alerts and (optionally) automated actions; "optimized" label (balance/consolidation) is explicitly distinct from "days remaining" (exhaustion) — two different health measures.
- **What-If Analysis**: scenarios for workload planning (add/remove workloads → fits or not; time remaining; capacity remaining), infrastructure planning (add/remove capacity/nodes), migration planning (across VMware cloud variants and public cloud — cost + capacity), data center comparison (cost + capacity fit); scenarios can run singly or cumulatively.
- **Cost**: SDDC costing out-of-the-box; chargeback summary (VCD multitenancy); cost appears inside what-if migration/comparison results.
- **Reports**: scheduled snapshots of views/dashboards (report = scheduled snapshot; TOC, cover page, footer).
- Data collection via integrations ("Management Packs"/"Solutions") and cloud proxies for remote data centers.

## Product B — Virtana Infrastructure Observability (IO)

### Key observations

- **Predictive Capacity Management Analytics** ("forecast your capacity needs using the same solution that monitors your workloads"):
  - **Capacity Forecast**: reviews historical usage → predicts short- and long-term usage trends; purpose = "identify resource strain before it leads to performance and availability issues, and to plan for the growth required to support critical business applications." Run from Analytics home; select entity type among **Compute, Network, Storage**; advanced options: forecast thresholds, metric selection, percentile basis; minimum 6 months of data recommended (product-specific); can run in background → Outputs page. Results: summary pane (pinpoint issues) + detail panes (e.g., "5 datastores may reach the limit of their usage within 180 days").
  - **VM Deployment Advisor**: optimizes deployment of new VMs by examining historical usage → identifies which cluster/VM to deploy on for optimal performance and balance; determines how a new VM fits in CPU, Memory, Network, Disk.
  - **Capacity Auditor**: deep statistical analysis of capacity utilization across storage components; identifies where/when capacity adjustments are needed and how deduplication/compression/thin provisioning impact utilization.
- Per-integration capacity analytics: Capacity Forecast (and often Capacity Auditor) documented for ~30 integrations — storage arrays (NetApp, Dell PowerMax/Unity/PowerStore/PowerScale/PowerFlex/XtremIO, Hitachi VSP/NAS/HCP/UCP, HPE 3PAR/Primera/Alletra, Pure, IBM, Infinidat, Nutanix, Dell ObjectScale), OS (Linux, Windows, Solaris, KVM), network (Cisco UCS/Nexus, Brocade FC, IP switches, Redfish), OpenShift (beta).
- **Global View** (cross-domain layer): "On-Premises Compute Cost and Capacity" dashboard (compute infrastructure, utilization summary, utilization trend, host utilization, optimization insights); "On-Premises Storage Array Cost and Capacity Summary".
- **Platform workflow** "Planning for the future: Capacity forecasting and resource optimization": Step 1 review Global Capacity dashboard → Step 2 analyze cloud cost and utilization → Step 3 review Kubernetes resource management → Step 4 run automated capacity forecasting → Step 5 review workload right-sizing recommendations → Step 6 use VM Coordinator and cluster balancing → Step 7 detect seasonal trends and anomalies.
- Monitoring concepts page: "Health, Utilization, Capacity, and Performance" as the four assessment dimensions.
- Positioning has shifted toward "Hybrid Infrastructure Observability Platform" with capacity forecasting as one capability under Infrastructure Observability (Tier-2 product pages).

## Product C — Cast AI

### Key observations

- Platform framing: "all-in-one Kubernetes automation, optimization, security, and cost management platform"; cost monitoring at cluster/namespace/workload levels; automatic optimization via autoscaling, Spot automation, bin packing; **workload autoscaling to right-size containers based on actual resource usage**.
- **Workload Autoscaler**: continuously monitors workload metrics and compares against current recommendations; recommendations regenerated on a cycle (every 30 minutes, product-specific) and immediately on anomalous usage.
- **Scaling policies**: per-workload or default policy; settings include recommendation percentile (basis for the recommendation), overhead (extra on top), optimization threshold (when to apply), autoscaler mode (**immediate** = evict/recreate pods via Eviction API with PodDisruptionBudget enforcement; **deferred** = apply on natural pod recreation or in-place resize on K8s 1.33+).
- **Recommendation confidence**: full vs low confidence based on historical data quantity/quality; gradual scaling limits for new clusters (product-specific percentages); confidence indicators in UI.
- **Safety/exception machinery**: OOM event handling (overhead increase with linear decay; auto-disable after persistent OOMs with cooldown then re-enable), memory-pressure eviction handling, surge detection (progressive lookback shortening + quantile increase), CPU stall detection via pressure stall information, startup failure detection, HPA interplay (defer to HPA until max replicas), LimitRange/ResourceQuota compliance, GKE Autopilot constraint clamping, protected namespaces.
- Node autoscaling / bin packing / Spot automation sit on the cost-optimization side (boundary context toward FinOps).

## Product D — Kubex (Densify)

### Key observations

- Positioning: "autonomous resource optimization platform for Kubernetes and AI infrastructure"; combines analytics, recommendations, and controlled automation; audience includes SRE/platform engineering, FinOps/cloud ops, engineering leaders.
- Core capabilities: rightsizing Kubernetes containers; node optimization; **GPU optimization with coordinated CPU/memory/storage/GPU recommendations**; guardrail-based automation (approvals, maintenance windows); historical usage analytics for proactive resource decisions; multi-environment support.
- **Data collection**: Helm-deployed collector; data begins flowing within an hour; analysis runs overnight (product-specific cadence); data collection status page per cluster.
- **Automation Engine**: policy-driven automation of container resource configurations; automated resizing based on actual usage; zero-downtime in-place resizing (K8s 1.33+) with fallback to pod eviction; safety-first validation (HPA-aware, LimitRange/ResourceQuota enforcement, PodDisruptionBudgets, node capacity validation); annotation-based pausing for learning periods; configurable downsizing/upsizing rules; RBAC, audit trails, GitOps compatibility.
- **Automation visibility**: Automation status page (telemetry, recent change history); Container Overview Summary (counts enabled/automated over 7 and 90 days, drill-down to container lists); per-workload optimization history modal with CPU/memory utilization charts around each change event.

## Cross-product Comparison

| Dimension | Aria Operations | Virtana IO | Cast AI | Kubex (Densify) |
|---|---|---|---|---|
| Capacity-bearing resources | clusters, hosts, VMs, datastores, data centers, custom data centers | compute (hosts/VMs), storage arrays, network devices; ~30 integrations | K8s workloads (containers/pods), nodes, clusters | K8s containers/nodes/clusters; GPU/AI infrastructure |
| Consumption over time | metrics collected via integrations/agents; 5-min data points (product-specific) | collectors per integration; historical usage basis for all analytics | continuous workload metrics monitoring | Helm collector; overnight analysis cycle |
| Limits / usable capacity | total vs usable (HA-adjusted); allocation (overcommit) model optional | array/host/storage limits per entity type | requests/limits, node allocatable, quota/LimitRange constraints | requests/limits, node capacity, quotas |
| Demand-vs-capacity output | Time Remaining, Capacity Remaining, Recommended Size/Total Capacity | Capacity Forecast (trend + "may reach limit within N days" style results) | recommendations vs current requests; thresholds | recommendations + headroom/saturation risk framing |
| Forward-looking mechanism | capacity engine (linear/periodic models, risk levels, 1-year window) | forecast analytics w/ percentile + thresholds; min 6-month history | percentile/overhead-based recommendation (short-horizon) | historical analytics → proactive recommendations |
| Recommendations | right-size (capped), reclaim idle, rebalance | right-sizing recommendations; VM Deployment Advisor (placement) | right-size requests; apply via policies | right-size; node/GPU optimization |
| Scenario planning | What-If: workload/infrastructure/migration/data-center comparison (with cost) | not observed as named feature (forecast + advisor instead) | not observed | not observed |
| Automation posture | advisory-first; automation via policies/jobs possible | advisory analytics | continuous automated optimization (immediate/deferred modes) | autonomous optimization with guardrails |
| Cost dimension | SDDC costing, chargeback, cost in what-if | cost+capacity dashboards (Global View) | cost monitoring core | FinOps alignment stated |
| Interfaces | Capacity page, object Capacity tab, capacity dashboards, reports, what-if UI | Analytics home → forecast runs → outputs; Global View dashboards | console: workload drawer, scaling policies, event log | console: data status, automation status, container overview, history modal |
| Policies | capacity policies (risk level, custom metrics, thresholds, alerts) | forecast thresholds/percentile per run | scaling policies (percentile, overhead, threshold, mode) | automation policies (targeting, strategies, constraints) |

## Canonical Model (synthesis)

**L0 — Defining Invariant** (smallest structure without which the Type is unrecognizable):

1. **Capacity-bearing resources modeled as managed objects with defined limits** — an inventory of the infrastructure whose capacity is being managed (hosts, clusters, storage, network, cloud/container allocations), each with a notion of total/usable capacity.
2. **Consumption observed over time against those limits** — utilization data collected from the resources (integrations/collectors/agents), retained as history.
3. **Demand-vs-capacity assessment with a forward-looking risk determination** — how much headroom remains now, and when/whether demand will reach the limits (projection/forecast of exhaustion or saturation risk).

Historical check (§24): mainframe-era and storage-era capacity planning (MIPS/DASD consumption vs installed capacity, projected exhaustion dates), regional and platform-native tools, and modern cloud/K8s tools all satisfy this triple. Nothing cloud-specific, K8s-specific, or vendor-specific is required. If (3) is removed, the product collapses into utilization monitoring/reporting; if (1)/(2) are removed, there is nothing to manage.

**L1 — Common Mature Structure** (standard in mature products, not definitional):

- Utilization/capacity dashboards and per-resource capacity views (headroom, usage trends)
- Capacity alerts/thresholds (stress thresholds, warning windows)
- Forecasting engine with configurable behavior (models, risk levels/aggressiveness, percentiles, time windows)
- Right-sizing / reclaim recommendations (overprovisioned and undersized resources)
- Placement/deployment guidance (where new workloads fit)
- Scenario/what-if planning (add/remove workloads or capacity; migration comparisons)
- Policies governing calculations, thresholds, and automation scope
- Data acquisition layer (integrations, management packs, collectors, agents)
- Capacity reports (scheduled snapshots for planning/management audiences)
- Grouping/alignment structures (data centers, environments, clusters, services)
- Cost dimension attached to capacity (cost of recommended changes, chargeback context)

**L2 — Variant / Optional Structure**:

- Product form: standalone capacity suite vs feature area of an ITOM/ops platform vs SaaS optimization service vs in-cluster controllers (K8s)
- Scope specialization: virtualization capacity, storage-array capacity, network bandwidth capacity, Kubernetes capacity, cloud account/service capacity, GPU/AI capacity
- Posture: advisory (reports/recommendations) vs continuous automated optimization (apply changes with guardrails)
- Planning cadence: periodic planning cycles (forecast runs, overnight analysis) vs continuous recalculation
- Business alignment depth: cost+capacity dashboards, chargeback, migration cost comparison
- Automation safety machinery: eviction budgets, quotas, pause/learning windows, confidence gating, cooldowns
- Segment tuning: enterprise virtualization vs hybrid infrastructure vs cloud-native

**L3 — Vendor-specific** (research notes only):

- Aria: named engine outputs (Time Remaining/Capacity Remaining/Recommended Size/Recommended Total Capacity), 1-year projection window, 5-min data points, 120-day default warning threshold, 50%/100% recommendation caps, demand vs allocation model toggle, "optimized vs days remaining" distinction, What-If scenario taxonomy, SDDC costing.
- Virtana: named analytics (Capacity Forecast / VM Deployment Advisor / Capacity Auditor), Compute/Network/Storage entity selection, 6-month minimum history, percentile-based forecast options, per-integration analytics catalog, Global View cost+capacity dashboards, 7-step planning workflow.
- Cast AI: 30-min recommendation regeneration, immediate vs deferred apply modes, confidence levels and gradual-scaling percentages, OOM overhead/decay/2.5x cap/20-events-1h auto-disable/4h cooldown, surge/stall detection specifics, GKE Autopilot clamping.
- Kubex: overnight analysis cadence, in-place resize on K8s 1.33+ with eviction fallback, 7/90-day automation counts, annotation-based pause, specific guardrail set.

## Vendor-specific Findings

See L3 above. None promoted to the canonical document.

## Boundary Findings

- **vs Infrastructure Monitoring / Metrics Monitoring**: monitoring observes current state and detects incidents; capacity management projects future demand against limits and plans supply. Capacity tools consume monitoring-style data (some are embedded in monitoring platforms — Aria, Virtana). Test: remove forward-looking capacity risk → monitoring platform; remove current-state observation → capacity management cannot function. Boundary held; bundling is common.
- **vs Cloud Cost Management / FinOps**: FinOps centers on spend (billing data, commitments, unit economics); capacity management centers on resource supply vs demand (limits, headroom, exhaustion). Overlap: right-sizing, commitment planning, cost-of-change. Spot/Flexera docs (cost monitoring, commitment management) sit on the FinOps side. Test: remove resource-limit semantics → FinOps; remove cost → still capacity management. Boundary held; adjacent and increasingly bundled.
- **vs DCIM**: DCIM manages physical data-center capacity (power, cooling, space, racks); capacity management manages logical IT resource capacity (compute/memory/storage/network). Some dashboards overlap ("data center capacity"). Boundary held.
- **vs AIOps Platform**: AIOps correlates events/anomalies across the stack; capacity management does deterministic demand-vs-supply projection. ML is used in both but for different purposes. Boundary held.
- **vs Kubernetes Management Platform / Virtualization Management / Server Management**: those manage configuration/lifecycle of resources; capacity management plans supply vs demand over time. K8s management platforms may bundle capacity views. Boundary held.
- **vs Load Testing Platform**: load testing generates synthetic demand to probe limits at a point in time; capacity management observes real demand over time and projects. Boundary held.
- **vs ITSM**: capacity management is an ITIL-associated practice; ITSM platforms may govern the process (policy, review cadence) while capacity tools do the analytics. Boundary held (no precise ITIL sub-practice claims asserted — external reference fetch failed).
- **vs Bed & Capacity Management (§22)**: same term, different domain (hospital beds vs IT resources). No confusion risk in practice; noted for taxonomy clarity.
- **"去掉什么就变成另一个 Type" 判据**: remove the forward-looking demand-vs-capacity projection → Infrastructure/Metrics Monitoring; remove resource-limit semantics and keep spend → Cloud Cost Management/FinOps; remove logical IT resources and keep power/cooling/space → DCIM; remove observation of real demand and keep synthetic demand generation → Load Testing.

## Uncertainties

- The classic standalone capacity-suite pole (BMC TrueSight Capacity Optimization, ServiceNow Capacity Optimization) could not be fetched (403/JS-gate/timeout). Its structures are inferred at category level from the sampled products and from the products' own category framing; any claim specific to those vendors is absent from the final document.
- IBM Turbonomic (continuous application resource management) unreachable; the "continuous optimization" pole is covered by Cast AI/Kubex instead.
- ITIL framing: external reference fetch failed; the document describes the discipline generically without asserting specific ITIL sub-practice structures.
- Market consolidation direction (capacity features absorbed into observability/FinOps/AIOps suites — observed for Virtana and Aria/VCF) is a sample-level observation, not asserted as a market-wide trend in the final document.
- Whether long-horizon forecasting is strictly definitional: all sampled products express forward-looking risk, but cloud-native optimizers express it implicitly (recommendations anticipating demand) rather than as explicit exhaustion dates. L0 therefore phrases the invariant as "forward-looking demand-vs-capacity risk determination" rather than "forecasting engine with time-remaining output".

## Final Synthesis

Capacity Management software is the planning counterpart to infrastructure monitoring: it maintains an inventory of capacity-bearing resources with limits, tracks their consumption over time, and continuously determines how much headroom remains and when demand will exhaust it — then supports the capacity decisions that follow (add capacity, reclaim/resize, rebalance, migrate), ranging from advisory reports to guardrailed automated optimization. Mature products add forecasting engines with configurable risk posture, right-sizing/reclaim recommendations, placement advisors, what-if scenario planning, capacity dashboards/reports, policies, and a cost dimension. Product form varies from standalone suites to ops-platform feature areas to SaaS/in-cluster optimization services; scope varies across virtualization, storage, network, Kubernetes, cloud, and GPU/AI infrastructure.
