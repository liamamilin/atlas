# Research Notes — Cloud Cost Management / FinOps

Research date: 2026-09-07
Methodology: v1.1 (update-v1/WORKFLOW_v1.1.md, WRITING_GUIDE_v1.1.md)

## Research Goal

Understand what "Cloud Cost Management / FinOps" actually is as an Application Type: what objects it manages, how cloud spend data enters it, how spend is attributed to organizational accountability, what governance and optimization machinery exists, and where its boundary lies against Cloud Management Platforms, monitoring, SaaS Management, Telecom Expense Management, the sibling AI Cost / FinOps Platform, and corporate finance tools.

Joint-review obligation: the completed `ai-cost-finops-platform` leaf flagged this leaf for joint review of the §14/§13 sibling boundary ("same allocation/budget/anomaly/showback machinery, different metered object"). Discharged in Boundary Findings §1 below.

## Initial Boundary

Working hypothesis before research:

- Core use: give an organization visibility into and control over what it spends on cloud infrastructure, attributed to teams/products/environments, with budgets, anomaly detection, and optimization.
- Likely users: FinOps practitioners, finance/IT finance, platform and engineering leads, engineering managers, executives; MSPs managing multiple customers.
- Nearest Types: Cloud Management Platform (§14), Infrastructure Monitoring (§14), SaaS Management (§14), Telecom Expense Management (§14), AI Cost / FinOps Platform (§13 sibling), Spend Management Platform (§08/§10), Billing Platform (§08, vendor side), FP&A / Budgeting & Forecasting (§08), Capacity Management (§14).
- Open questions: is multi-cloud definitional or a posture? Are budgets/anomalies/recommendations defining or mature structure? Does the platform-native pole (AWS/Azure/GCP native consoles) belong to this Type? Where exactly is the line against a plain billing viewer?

## Research Questions

1. What is the central managed object (billing line item? cost record? allocation dimension? budget?)
2. How does cost data enter the system (provider billing exports/APIs, agents, custom uploads)?
3. What does the normalized cost model look like (dimensions, charge types, provider label mapping)?
4. How is spend allocated to organizational accountability (tags, rules, hierarchies, shared-cost splitting, showback/chargeback)?
5. What analysis surfaces exist (explorers, reports, dashboards, drill-down)?
6. What governance objects exist (budgets, alerts, anomaly detection, forecasts, policies)?
7. What optimization capabilities exist (rightsizing, idle resources, commitment management, automation)?
8. What unit economics / business-metric linkage exists?
9. Who are the users and how do roles differ (FinOps, finance, engineering, product, leadership, procurement)?
10. Where are the boundaries vs the adjacent Types listed above — especially the AI Cost / FinOps sibling?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer levels:

| Product | Philosophy | Customer level | Role in sample |
|---|---|---|---|
| Vantage | Modern multi-cloud FinOps SaaS, self-serve + enterprise | Startups → enterprise | deep Tier-1 docs; billing-side aggregation pole |
| CloudZero | Engineering-first "financial control plane", unit economics | Enterprise | deep Tier-1 docs; allocation-as-code + unit-economics pole |
| AWS Billing and Cost Management | Platform-native suite inside the cloud provider | Any AWS customer | platform-native pole (historical/market-sample check) |
| IBM Cloudability (Apptio) | Enterprise FinOps suite, TBM/ITFM heritage | Large enterprise | enterprise-suite pole (Tier-2 evidence only) |
| IBM Kubecost | Kubernetes-specialized cost monitoring, agent-based | K8s teams, self-hosted → SaaS | container-specialized variant pole (Tier-2 evidence only) |

## Sources

All fetched 2026-09-07 (Layer A unless noted):

- Vantage docs index: https://docs.vantage.sh/llms.txt
- Vantage — Cost Reports: https://docs.vantage.sh/cost_reports.md
- Vantage — Segments: https://docs.vantage.sh/segments.md
- Vantage — Budgets: https://docs.vantage.sh/budgets.md
- Vantage — other capabilities (Data Dictionary, Tagging/Virtual Tags, Anomaly Detection, Cost Alerts, Forecasting, Cost Recommendations, Commitments, Business Metrics, Kubernetes, MSP, RBAC/SSO, VQL, API, Terraform, Snowflake Data Sharing, Custom Providers, provider integrations): index-level evidence (official page titles + descriptions in llms.txt)
- CloudZero docs index: https://docs.cloudzero.com/llms.txt
- CloudZero — Overview: https://docs.cloudzero.com/docs/cloudzero.md
- CloudZero — Cost Organization with Dimensions: https://docs.cloudzero.com/docs/organize-your-costs.md
- CloudZero — Cost Types: https://docs.cloudzero.com/docs/cost-types.md
- CloudZero — other capabilities (Explorer, Views, Budgets, Anomaly Detection, Optimize, Unit Economics, AnyCost/CBF, Telemetry Streams, AI Hub, SSO/RBAC, Snowflake shares, Jira/Slack): index-level evidence
- AWS Billing and Cost Management User Guide — overview: https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html
- AWS — Cost Categories detail page attempted (https://docs.aws.amazon.com/cost-management/latest/userguide/cost-categories.html) — did not render (JS-only shell); split-charge-rule evidence taken from the overview page
- IBM Cloudability product page: https://www.apptio.com/products/cloudability/ (Tier 2 — positioning, feature-domain names, role descriptions; no operational detail)
- IBM Kubecost product page: https://www.kubecost.com/ (Tier 2 — positioning, capability pillars, editions; no operational detail)

Source-access limitations:

- IBM docs (https://www.ibm.com/docs/en/cloudability) returned 403; Cloudability help-center depth unavailable. All Cloudability assertions kept at product-page level; no operational rules claimed.
- Kubecost docs (https://docs.kubecost.com/) returned 403; product page used instead. Same restriction.
- AWS Cost Categories detail page did not render; allocation evidence for AWS is overview-level.
- FinOps Foundation framework pages not fetched; the inform/optimize/operate framing is inferred from vendor positioning only and was not needed for the product-structure conclusion.

## Product Observations

### Vantage (Layer A, deep)

Positioning: "cloud cost observability and FinOps platform" aggregating costs across providers; docs cover provider integrations, Cost Reports, budgets, Autopilot, API, Terraform.

Key observations:

- **Provider billing data as raw material.** Integrations ingest from AWS, Azure (MCA/EA/CSP), GCP, Oracle, Linode, Kubernetes, plus SaaS/observability vendors (Snowflake, Databricks, Datadog, New Relic, Elastic, Fastly, Twilio, Vercel, GitHub, CircleCI, ClickHouse, Confluent, MongoDB Atlas, PlanetScale, Redis, Cloudflare, Temporal, Grafana, Coralogix) and AI providers (OpenAI, Anthropic, etc.). "Custom Providers" allow CSV cost uploads. Security page: read-only billing access.
- **Normalized cost model.** A Data Dictionary documents "normalized data dictionary … field mappings across cloud providers" (e.g., Azure Subscription → `costs.provider_account_id` → AWS Billing Account). Cross-provider filters fall back to AWS-style labels when provider labels differ. A normalized **Charge Type** taxonomy spans providers (usage, credits, discounts, taxes, fees, amortized/unamortized variants, Savings Plan/RI-specific types).
- **Cost Reports as the central analysis object.** A default "All Resources" report; filter by provider/dimensions (Account, Billing Account, Region, Service, Resource, Provider, Category, Subcategory, Charge Type, Tagged, Tag, Usage Unit); group by multiple dimensions; drill-down sequences; date bins; automatic per-report forecast; previous-period comparison; saved filters; folders; dashboards; annotations; usage-based reporting (Y axis = usage, locked to Usage Unit).
- **Amortization as a view toggle.** Commitment costs (RI/Savings Plan) can be amortized across the covered period; charge-type guidance shows how to detect unused commitment capacity (gap between total commitment cost and allocated commitment cost).
- **Allocation machinery.** Virtual Tags (rule-based tag normalization/creation across providers); **Segments** — hierarchical cost allocation ("bottom-up": child filters claim costs, roll up to parents; costs "allocated only once and not duplicated in cases of showback/chargeback"; priority-ordered allocation; explicit **Unallocated** tracking as a tag-governance burn-down surface); percent-based cost allocation on report filter sets (showback shared resources like support costs or multi-tenant databases).
- **Governance objects.** Budgets (Standard + Hierarchical up to 10 levels; budget periods by day/week/month/year; CSV import; performance view with utilization states On Track / At risk / Over / Not Started; budgets rendered as a line on the attached Cost Report; budget alerts on percentage thresholds with optional period windows, delivered via email/Slack/Teams/Jira; only actual costs, not forecasts, trigger); Cost Alerts (threshold-based); Anomaly Detection (ML-powered); Forecasting (baseline/dynamic/scenario); Scenario Models; Report Notifications.
- **Optimization.** Cost Recommendations; Autopilot (automated AWS Savings Plans purchases); Savings Planner; Commitments (view/manage RI/SP); Issues (collaboration on optimization); FinOps Agent ("identify and remediate cloud waste automatically", with MCP integrations to Datadog/GitHub/Linear/Notion).
- **Kubernetes.** Vantage Kubernetes Agent; Kubernetes costs and efficiency metrics; pod-level network cost attribution.
- **Unit economics.** Business Metrics import (unit cost, usage unit cost, gross margin, raw value) overlaid on cloud costs.
- **Enterprise/MSP.** Workspaces, RBAC with per-action permission tables, SSO with JIT provisioning, audit logs; Vantage for MSPs (multi-customer), MSP Invoicing (generate/approve/distribute invoices), SQL Billing Rules (modify cost data, apply discounts, exclude items).
- **Programmability.** REST API, VQL (SQL-like cost query language), Terraform provider, Snowflake Data Sharing, data exports.

### CloudZero (Layer A, deep)

Positioning: "the financial control plane for your cloud and AI spend."

Key observations:

- **Connections.** AWS (CUR-based), Azure (MCA/EA/CSP), GCP, OCI, SaaS platforms (Databricks, Datadog, Snowflake, Elastic, Fastly, Twilio, MongoDB, New Relic, ClickHouse, Confluent, GitHub), AI platforms (Anthropic, OpenAI, Cursor), Kubernetes agent, and **AnyCost** custom sources (REST API or S3 bucket in a Common Bill Format) as the escape hatch for unsupported providers.
- **Dimensions as the allocation concept.** "Dimensions are how you turn raw spend into business context" — team, product, feature, environment, customer, or any category; built from bill metadata (accounts, services, regions, usage types) so "you do not need clean resource tags to get started"; tags are optional enrichment; inconsistent tag variants (`env`, `ENV`, `Environment`) normalized; changes are **retroactive across full cost history**. Built visually (Dimension Studio) or as code (CostFormation YAML, versionable, publishable via API, VS Code extension); Namespaces separate dimension definitions with independent version history and access control.
- **Shared-cost splitting.** Two documented methods: split by proportion (based on each team's share of related spend — no extra data required) or split by usage (customer-supplied consumption data: API calls, storage per customer, query counts — via Telemetry Streams: allocation telemetry + unit-metric telemetry).
- **Cost Types as the normalized money model.** Seven named views of the same spend: Real Cost (default; filters taxes/support/overhead — "every engineering decision is a buying decision"), Billed Cost (invoice reconciliation), Discounted Cost, Amortized Cost, Discounted Amortized Cost (chargeback/showback default), Invoiced Amortized Cost (AWS only), On-Demand Cost (not available for Azure). Documented mappings to AWS CUR columns; provider-specific behaviors documented.
- **Analysis.** Explorer (filter/group/drill-down by service, account, team, product, or any defined category), Views (shareable saved analyses), period comparison, usage data viewing, Kubernetes efficiency metrics, Dashboards with scheduled reports.
- **Governance.** Anomaly Detection "on from the moment you connect, with no configuration required"; Budgets; Notifications (Slack/email/Google Chat); engineering-activity Events (e.g., deployments) correlated with cost changes.
- **Optimization.** Optimize recommendations across AWS/Azure/GCP/Kubernetes with status/effort/comments/work-item linkage; Insights.
- **Unit economics.** Unit Economics as a headline capability ("track costs per customer, transaction, or any unit"); tutorial for unit-cost dashboards.
- **AI Hub.** Natural-language questions over spend; Model Right Sizer.
- **Users.** FinOps/finance (track, allocate, budget, ROI), platform/DevOps engineers (drivers, anomalies, optimization), engineering/business leaders (dashboards).
- **Enterprise.** SSO (Okta/Entra/OIDC/SAML), Users & Permissions with roles/permission sets, Namespace access control, Snowflake data shares, Jira integration.

### AWS Billing and Cost Management (Layer A, overview level)

Positioning: the cloud provider's native suite — "analyze, organize, plan, and optimize your costs."

Key observations:

- **Cost analysis.** Cost Explorer (visuals, filtering, grouping, forecasting, custom reports); data exports to warehouses/BI; Cost Anomaly Detection (automated alerts); Free Tier monitoring; split cost allocation for shared ECS resources; Cost Management preferences (member-account visibility, granularity).
- **Cost organization.** **Cost categories** — "map costs to teams, applications, or environments, and then view costs along these dimensions in Cost Explorer and data exports. Define split charge rules to allocate shared costs"; **cost allocation tags** — resource tags viewed as cost dimensions.
- **Budgeting and planning.** Budgets (custom cost/usage budgets, threshold alerts); pricing calculators (in-console with discounts/commitments; public on-demand).
- **Savings and commitments.** Cost Optimization Hub (tailored recommendations: deleting unused resources, rightsizing, Savings Plans, reservations); Savings Plans (inventory, purchase recommendations, purchase analyses, utilization/coverage); Reservations.
- **Billing layer.** Bills/invoices/payments/credits/purchase orders; consolidated billing via Organizations (management account pays member accounts; volume discount sharing); billing transfer across organizations; **Billing Conductor** — a custom-billing service supporting "showback and chargeback workflows of AWS Partners reselling AWS services" (models billing relationships, applies custom rates, doesn't change the actual AWS bill).
- **Access control.** IAM controls on billing console pages; Cost Management preferences for linked-account Cost Explorer access.

Significance for the Type: the platform-native pole demonstrates that the defining structure does not require multi-cloud, third-party ingestion, or a separate vendor — a single provider's own console implements the same core (ingest-from-own-billing, organize/allocate, analyze, budget, optimize).

### IBM Cloudability (Layer B — product-page level; no operational detail)

Positioning: "market leading, enterprise grade FinOps platform that provides unified visibility across technology spend, connects costs to ownership and accountability, helps organizations improve forecasting, optimize spending, and unlocks AI and cloud value."

Key observations (feature-domain names and role descriptions only):

- **Feature domains** (three pillars): ownership/visibility (Business Mapping, Commercial Billing, Container Cost Allocation, Cost Sharing, Dashboards & Reports, Sustainability, Tagging, True Cost Explorer, Views); scale/invest confidence (Anomaly Detection, Budgets & Forecasts, Cloud Financial Planning, Governance, Scorecards, Unit Economics, Views, Workload Planning); cost efficiency (savings automation — page section truncated).
- **Role mapping** (vendor-described): FinOps practitioner (single pane of glass, org-wide dashboards, personalized Views, 100% allocation via "purpose-built mapping and cost-sharing tools", benchmarking, AI usage by model/token type/direction); DevOps (rightsizing with utilization/performance, policies that prioritize opportunities and "automatically create tickets in ITSM tools", automated orphaned-resource termination, Kubernetes cost/efficiency with pod placement/cluster scaling/container sizing); IT Finance (accurate chargeback at scale via business mapping and cost sharing, commitment planning, finance-ready analytics, "AI-backed, bottom-up forecasting and top-down budgeting workflows"); Product (fully loaded product costs across cloud/AI/SaaS, unit economics with business metrics, proactive budget/anomaly notifications); Leadership (spend-to-outcome linkage, financial control, early risk); Procurement (vendor negotiation data, commitment coverage/utilization, pricing comparison across providers).
- **Editions.** Cloudability, Cloudability Savings Automation, Cloudability MSP.
- Marketing outcome claims (30%+ unit-cost reduction, 100% allocation, 90% commitment coverage) are vendor claims — not used as evidence.

### IBM Kubecost (Layer B — product-page level; no operational detail)

Positioning: "Understand and optimize your Kubernetes costs in real-time"; "real-time visibility, allocation, optimization, and governance."

Key observations:

- **Capability pillars.** Visibility (real-time K8s costs across clusters, teams, namespaces, workloads, shared resources; "break down spend by any Kubernetes object and reconcile it with your cloud bill for defensible showback and chargeback"); Operability (multi-cloud and hybrid; "native cloud billing and custom pricing"); Optimization (over-provisioned workloads; "automated actions like automated request sizing or namespace turndown"); Governance (budgets, forecasting, anomaly detection, alerts, role-based access, reporting).
- **Deployment.** Agent runs locally on clusters; editions: Foundations (free self-hosted, unlimited clusters up to 250 cores, 15-day metric retention, CSP bill reconciliation), Enterprise Self-hosted (unlimited scale, custom pricing, RBAC, enterprise integrations, GPU optimization, resource-quota automations), Enterprise Cloud (SaaS-managed agent, HA/DR, BYO identity).
- **Heritage.** Open-source project origins; cloud-native ecosystem; now part of IBM Apptio alongside Cloudability.

## Cross-product Comparison

| Dimension | Vantage | CloudZero | AWS native | Cloudability | Kubecost |
|---|---|---|---|---|---|
| Philosophy | modern multi-cloud FinOps SaaS | engineering-first financial control plane | platform-native suite | enterprise FinOps suite (TBM heritage) | Kubernetes-specialized, agent-based |
| Cost data source | provider billing APIs/exports (read-only) + custom CSV providers | provider billing (CUR etc.) + AnyCost (REST/S3, CBF) + K8s agent | its own billing system | provider billing (detail unavailable) | K8s agent measurement + cloud-bill reconciliation |
| Normalized money model | Data Dictionary field mappings + Charge Type taxonomy + amortization toggle | 7 named Cost Types + CUR mappings + provider caveats | native schema (CUR), blended/amortized views | True Cost Explorer (detail unavailable) | K8s object costs reconciled to bill; custom pricing |
| Allocation concept | Virtual Tags + Segments (hierarchical, allocate-once, unallocated tracking) + percent-based allocation | Dimensions (visual or CostFormation code; retroactive; metadata-first, tags optional) + shared-cost split (proportion or usage telemetry) | Cost categories + split charge rules + cost allocation tags + ECS split | Business Mapping + Cost Sharing + Container Cost Allocation + Tagging | allocation by any K8s object (cluster/team/namespace/workload/shared) |
| Analysis surfaces | Cost Reports, Resource Reports, Dashboards, drill-down, saved filters/folders | Explorer, Views, Dashboards, period comparison | Cost Explorer, data exports | True Cost Explorer, Dashboards & Reports, Views | real-time dashboards by K8s object |
| Governance | Budgets (std/hierarchical), Budget Alerts, Cost Alerts, ML Anomaly Detection, Forecasting, Scenario Models | Budgets, default-on Anomaly Detection, Notifications, activity Events | Budgets, Cost Anomaly Detection | Budgets & Forecasts, Anomaly Detection, Governance, Scorecards | Budgets, forecasting, anomaly detection, alerts |
| Optimization | Recommendations, Autopilot, Savings Planner, Commitments, Issues, FinOps Agent | Optimize recommendations + Insights (AWS/Azure/GCP/K8s) | Optimization Hub, Savings Plans, Reservations | rightsizing, orphaned-resource automation, ITSM policies, commitment planning | request sizing, namespace turndown, GPU optimization |
| Unit economics | Business Metrics (unit cost/margin) | Unit Economics (headline) | not emphasized | Unit Economics + Scorecards | efficiency metrics (requested vs used) |
| Showback/chargeback | Segments (explicit) | Dimensions + unit economics | Billing Conductor (partners) + cost categories | Business Mapping + Cost Sharing ("chargeback at scale") | showback/chargeback reconciled to bill |
| Enforcement posture | read-only (observe) | read-only (observe) | n/a (native) | observe + automation into ITSM | observe + automated K8s actions (in-cluster) |
| Scope | cloud + K8s + SaaS/observability vendors + AI providers | cloud + SaaS + AI | single cloud | cloud + AI + SaaS | Kubernetes (multi-cloud/on-prem) |
| Deployment | SaaS | SaaS | native console | SaaS | self-hosted agent / SaaS-managed |
| Programmability | REST API, VQL, Terraform, Snowflake share | REST API, CostFormation API, Snowflake shares | data exports, Price List API | (unavailable) | API (docs unreachable) |

### Cross-product commonalities (Layer B)

1. **Ingested provider billing data is the raw material.** Every product's facts come from cloud-provider billing systems — third-party tools read billing exports/APIs read-only; the native suite reads its own billing; the K8s specialist measures consumption in-cluster and reconciles to the cloud bill. None generates the spend.
2. **A normalized, queryable cost model.** Every product reorganizes raw billing line items into a unified schema with shared dimensions (time, service, account/project, region, resource, charge type) and explicit provider-label mapping (Vantage Data Dictionary; CloudZero Cost Types + CUR mappings; AWS native schema).
3. **Allocation to organization-defined accountability.** Every product maps spend onto dimensions the organization defines (teams, products, environments, customers) — via tags, categories, dimensions, segments, or business mapping — including machinery for shared-cost splitting and untagged/unallocated spend tracking. This is the headline FinOps capability in all five.
4. **Analysis surfaces over allocated spend.** Every product ships an explorer/report surface with filter/group by dimensions over time, plus dashboards.
5. **Budgets + alerts + anomaly detection** appear in all five (mature structure, not defining — reporting-first predecessors and simpler native views exist without them).
6. **Optimization recommendations** (rightsizing, idle/orphaned resources, commitment purchase/utilization) appear in all five in cloud-appropriate forms.
7. **Commitment economics** (RI/Savings Plan/CUD visibility, amortization, coverage/utilization) is standard in cloud-level products; the K8s specialist reconciles rather than purchases.
8. **Enterprise governance** (RBAC, SSO, audit) in enterprise-tier products; self-serve tiers emphasize fast setup.
9. **Export/API/warehouse sharing** (REST APIs, CSV, Snowflake shares, data exports) — the cost data is treated as an organizational dataset, not just a UI.
10. **Read-only posture** for third-party platforms (explicit in Vantage security docs and CloudZero connection docs): cloud FinOps platforms observe and advise; they do not cut off spend (enforcement lives in adjacent gateway/runtime Types).

### Divergences (candidate L2/L3)

- Coverage posture: multi-cloud third-party vs platform-native single-cloud vs container-scoped — posture, not invariant.
- Data path: billing-export aggregation (lagged, reconciled to invoice) vs agent-measured real-time (K8s) vs hybrid.
- Unit-economics emphasis: headline (CloudZero, Cloudability) vs optional module (Vantage) vs absent (AWS native).
- Scope extensions: SaaS/observability/AI provider spend as additional ingested sources (Vantage, CloudZero, Cloudability) — additive, not defining.
- MSP/multi-customer operation (Vantage MSP, Cloudability MSP) — segment variant.
- TBM/ITFM alignment and finance-process integration (ITSM ticketing, procurement support) — enterprise variant (Cloudability).
- Sustainability/emissions modules — optional (Cloudability).
- Allocation authoring style: UI rules (Vantage, AWS) vs code-as-allocation (CloudZero CostFormation) — implementation philosophy.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Minimal structure without which the product is not a Cloud Cost Management / FinOps application:

```text
Ingested provider billing/cost data
  (the platform's facts come from cloud-provider billing systems —
   read-only ingestion for third-party tools; native billing for provider suites;
   agent-measured consumption reconciled to bills for container specialists)
  └── Normalized cost model
      (billing line items reorganized into a unified queryable schema:
       time × service × resource × account/project × charge type, with provider-label mapping)
      └── Allocation to organizational accountability
          (spend mapped to organization-defined dimensions — team/product/environment/project —
           with shared-cost splitting and unallocated-spend tracking; showback/chargeback)
          └── Cost visibility surface
              (the allocated spend is browsable/filterable/groupable over time for decisions)
```

Four properties:

1. **Ingested provider billing data as raw material** — the system does not generate the spend; it ingests billing/cost data from cloud providers (or measures consumption and reconciles it to provider bills). Remove → not about cloud cost.
2. **Normalized cost model** — raw billing line items reorganized into a unified queryable schema across services/accounts/charge types. Remove → a pile of provider CSVs / a static bill page, not a platform.
3. **Allocation to organizational accountability** — spend mapped to owners and dimensions the organization defines, with shared-cost handling. Remove → a billing viewer; the FinOps job (who owns what, showback/chargeback, per-team accountability) collapses. This is what separates the Type from the provider's bare billing page.
4. **Cost visibility surface** — the allocated spend is queryable/browsable for analysis and decisions. Remove → a data pipeline, not an application.

§24 historical/market-sample check: the platform-native pole (AWS Billing and Cost Management) satisfies all four properties without multi-cloud, third-party ingestion, budgets-as-products, or a separate vendor — so multi-cloud is NOT definitional. Reporting-first predecessors of the sampled platforms (and the sampled platforms' own early forms) satisfy the core without budgets/anomaly detection/recommendations — so those are NOT definitional. A bare provider bill page (no allocation, no queryable model) fails properties 2–3 and is the adjacent minimal form, not the Type.

### L1 — Common Mature Structure

- Multi-provider integration library (third-party tools); full native coverage (provider suites)
- Budgets with periods and threshold alerts (hierarchical roll-ups in mature products)
- Anomaly detection (ML or rule-based), often default-on
- Forecasting (per-report or platform-level; scenario modeling in some)
- Optimization recommendations: rightsizing, idle/orphaned resources, commitment purchase/utilization
- Commitment management: RI/Savings Plan/CUD visibility, amortization views, coverage/utilization tracking
- Shared-cost splitting (proportional or usage-based) and untagged/unallocated spend governance
- Tagging governance (tag normalization, virtual/derived tags, tag-compliance burn-down)
- Unit economics / business-metric linkage (cost per customer/transaction/feature)
- Kubernetes/container cost allocation and efficiency metrics
- Dashboards, saved views/reports, scheduled notifications (email/Slack/Teams)
- RBAC/SSO/audit trails (enterprise tier)
- Export/API/warehouse sharing (REST API, CSV, data exports, Snowflake shares)
- Collaboration on savings (issues/comments, work-item linkage)

### L2 — Variant / Optional Structure

- Coverage posture: multi-cloud third-party vs platform-native single-cloud vs container-specialized
- Data path: billing-export aggregation (lagged, invoice-reconciled) vs agent-measured real-time vs hybrid
- Allocation authoring: UI rules vs allocation-as-code (versioned, API-published)
- Enforcement posture: observe-only (sampled norm) vs in-cluster automated actions (K8s specialist) — spend cutoff enforcement belongs to adjacent runtime/gateway Types, not this one
- Scope extensions: SaaS spend, observability-vendor spend, AI-provider spend as additional ingested sources
- Customer tier: self-serve teams vs enterprise FinOps programs vs MSPs managing many customers (multi-customer invoicing)
- Finance-process integration: ITSM ticketing, procurement/negotiation support, TBM/ITFM alignment, top-down budgeting workflows
- Deployment: SaaS vs self-hosted agent vs SaaS-managed agent
- Sustainability/emissions modules
- Framework alignment: FinOps Foundation framing, TBM taxonomies

### L3 — Vendor-specific (Research Notes only)

- Vantage: VQL; Canvas (NL-generated reports); Autopilot; Savings Planner; Build Hours (compute for virtual-tag processing); MSP Invoicing + SQL Billing Rules; budget hierarchy rules (max 10 levels, children must share identical periods, child usable once per hierarchy but in multiple hierarchies, cadence locked after periods exist); utilization states (On Track/At risk/Over/Not Started); budget alerts percentage-only, actual-cost-only, most-severe-only notification; FinOps Agent + MCP integrations (Datadog/GitHub/Linear/Notion/ChatGPT); annotations; exchange-rate upload; per-action RBAC permission tables.
- CloudZero: CostFormation (YAML allocation language) + publish jobs + 10 MB payload limit; Dimension Studio; Namespaces with RBAC; AnyCost + Common Bill Format (5 MB uncompressed drop limit); Telemetry Streams (allocation + unit metrics, sum/replace/delete semantics); engineering-activity Events; AI Hub + Model Right Sizer; Real Cost default philosophy ("every engineering decision is a buying decision"); Invoiced Amortized Cost AWS-only; On-Demand Cost Azure-unavailable; GCP Real Cost includes CUD credits.
- AWS: Billing Conductor (custom billing versions for partners/showback); billing transfer; consolidated billing volume-discount sharing; Free Tier monitoring; ECS split cost allocation; CUR column mappings per cost type; in-console vs public pricing calculators; IAM-gated billing console pages.
- Cloudability: Business Mapping; True Cost Explorer; Scorecards; Cloud Financial Planning; Workload Planning; Sustainability module; Savings Automation edition; MSP edition; benchmarking against peers; ITSM policy integration; AI usage by model/token type/direction.
- Kubecost: Foundations edition limits (250 cores, 15-day retention); namespace turndown; automated request sizing; GPU optimization; resource-quota automations; custom pricing; BYO identity in SaaS edition.

## Vendor-specific Findings

See L3. Notable: Vantage's segment model guarantees costs are "allocated only once and not duplicated" — an allocation-integrity rule likely shared conceptually but only directly documented there. CloudZero's Real Cost default (filtering taxes/support as "not engineering-influenceable") is a philosophy statement unique in the sample. Vantage's budget-alert mechanics (percentage thresholds only, actual costs only, most-severe alert wins) are precise operational rules that stay here.

## Boundary Findings

1. **vs AI Cost / FinOps Platform (§13 sibling) — JOINT REVIEW DISCHARGED.** Confirmed from the cloud side: the machinery (allocation, budgets, anomaly detection, showback, unit economics, recommendations) is identical across both Types; the difference is the metered object — infrastructure consumption (compute/storage/network) vs AI consumption (models/tokens/AI providers). Direct evidence of the gradient: Vantage and CloudZero ingest AI providers (OpenAI, Anthropic, Cursor…) through the *same* connection/allocation machinery as cloud providers — AI cost is absorbed as additional data sources, not a separate subsystem. The AI leaf's test holds from both directions: remove AI-specific consumption/pricing → generic cloud FinOps remains; remove infrastructure cost → AI cost platform remains. **Conclusion: probable scope-variant relationship; both leaves stand** — the AI leaf is justified by AI-specific data paths (request-side telemetry, token-level pricing volatility) and AI-specific unit economics that cloud FinOps platforms treat as just another source. Recorded in STATUS.md.
2. **vs Cloud Management Platform (§14).** CMP is the operational control plane (resource inventory, provisioning, orchestration, configuration/compliance); CCM is the money layer over billing data. CMPs bundle cost modules; CCMs do not manage resources. Test: remove cost data → CMP still stands; remove resource control → CCM still stands.
3. **vs Infrastructure Monitoring (§14).** Telemetry/performance (metrics, logs, traces) vs money (billing line items). Different data sources, different anomaly semantics (performance degradation vs cost spikes). Some CCM platforms join telemetry for investigation (Vantage's Datadog MCP) — an integration, not a merger.
4. **vs SaaS Management (§14).** SaaS subscriptions/licenses (contract- and seat-based, renewal-driven) vs metered cloud consumption (usage-based billing). Some CCM platforms ingest SaaS-vendor spend as additional sources, but license optimization and renewal management are the SaaS Management Type's core.
5. **vs Telecom Expense Management (§14).** Same bill-management pattern (invoice audit, allocation, optimization) applied to telecom carriers; TEM predates cloud FinOps and targets carrier invoices/devices rather than cloud billing APIs. Historical sibling discipline.
6. **vs Spend Management Platform (§08/§10).** Corporate spend broadly (cards, invoices, procurement, AP) vs metered technical consumption. Different objects (expense records vs billing line items) and different users (finance/procurement vs FinOps/engineering).
7. **vs Billing Platform (§08).** Vendor-side revenue billing vs buyer-side cost management — opposite sides of the transaction. (CloudZero's docs even import a vendor-side metering platform's data as a *business metric* source, underscoring the separation.)
8. **vs Financial Planning & Analysis / Budgeting & Forecasting (§08).** FP&A models corporate money top-down (accounts × time × org segments); CCM manages cloud consumption bottom-up from billing line items. CCM budgets are consumption guardrails scoped to cost selections, not corporate budget models; integration points exist (budget CSV import from spreadsheets; "Cloud Financial Planning" in Cloudability).
9. **vs Capacity Management (§14).** Capacity planning projects future resource needs; CCM accounts for money already committed/spent. Related through rightsizing and workload planning, but different primary objects.
10. **vs provider billing consoles (adjacent minimal form).** A bare bill page (static, no allocation, no queryable model) fails the defining core. The full native suites (AWS Billing and Cost Management) DO implement the core and belong to the Type in platform-native form.

## Uncertainties

- Cloudability and Kubecost operational detail unavailable (IBM docs 403 on both; docs.kubecost.com 403). Their evidence is product-page level; no operational rules were claimed for them. The canonical model does not depend on them.
- AWS Cost Categories detail page did not render; split-charge-rule evidence is overview-level.
- Whether every third-party platform enforces read-only access (explicitly documented for Vantage and CloudZero; assumed-but-unverified for others) — kept as "sampled norm" wording.
- FinOps Foundation's framework (inform/optimize/operate) was not fetched; the framing appears in vendor positioning but was not needed for the product-structure conclusion.
- Exact refresh cadences, retention windows, and numeric limits vary by product and contract (e.g., Vantage retention is contract-dependent) — deliberately excluded from the final document.

## Final Synthesis

A Cloud Cost Management / FinOps application is the buyer-side application that turns an organization's cloud consumption into attributable, governable spend. Its defining core is small: ingested provider billing data → normalized queryable cost model → allocation to organizational accountability (with shared-cost handling) → cost visibility surfaces. Everything else — budgets, alerts, anomaly detection, forecasting, recommendations, commitment management, unit economics, Kubernetes allocation, enterprise governance, warehouse export — is mature structure layered on top, and the specific mix varies by posture: platform-native suites implement the core inside one provider's console; multi-cloud platforms aggregate across providers read-only; container specialists measure in-cluster consumption and reconcile it to the bill. The Type sits between Cloud Management Platforms (same resources, operational not financial), Infrastructure Monitoring (same systems, telemetry not money), the sibling AI Cost / FinOps Platform (same machinery, different metered object), and corporate finance tools (same money, top-down models not bottom-up consumption).
