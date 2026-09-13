# Research Notes — Data Quality Platform

Research date: 2026-09-07
Leaf: Data Quality Platform (DIRECTORY.md §13 Data, Analytics & AI Systems)
Slug: data-quality-platform

---

## Research Goal

Understand what a Data Quality Platform actually is as an Application Type: what objects exist inside it (rules, evaluations, results, dimensions, issues), how the define → execute → review → remediate loop works, which structures are defining vs merely common in the current market, and where its boundaries lie against the neighboring §13 Types (Data Observability Platform, Data Governance Platform, Data Catalog, MDM, ETL/ELT, DataOps) and against adjacent capabilities (dbt tests, data preparation tools, software test frameworks).

This pass also carries a **joint-review flag from the data-observability-platform pass** (recorded in STATUS.md Boundary Issues): that pass held that "DQ centers the defined rule/test and its pass-fail result as the primary object; observability centers ambient health evaluation over the whole estate plus the incident loop" and recommended joint review when this leaf is processed. This pass discharges that flag from this side (see Boundary Findings).

## Initial Boundary (working hypothesis before research)

- **What:** software that defines and executes rules/tests/expectations against an organization's data, measures it against quality dimensions (completeness, validity, uniqueness, consistency, accuracy, timeliness), records pass/fail results, and drives remediation.
- **Users:** data engineers, data stewards, data quality analysts, governance teams, business data owners.
- **Nearest Types:** Data Observability Platform (sharpest seam — flagged), Data Governance Platform, Data Catalog, Master Data Management, ETL/ELT Platform, DataOps Platform; capability-adjacent: dbt tests, data preparation/cleansing tools, software test frameworks.
- **Unknowns:** Is profiling definitional or supporting? Is remediation/cleansing definitional? Is the "quality dimension" taxonomy definitional or product vocabulary? Where exactly does the DQ/observability seam sit from this side? Do data contracts change the Type?

## Research Questions

1. What is the primary object — the rule/test/expectation/check? How is it defined (UI, code, templates)?
2. What data does the platform operate on — does it hold the data or evaluate it in place / on staged copies?
3. How are quality dimensions expressed, and are they definitional?
4. What is the execution model — evaluations, scans, monitoring projects, schedules, runs?
5. What result structures exist — pass/fail, scores/percentages, failed-record samples, history?
6. What happens after a failure — issues/incidents, remediation, cleansing, write-back?
7. What roles use the product, and how do authoring vs reviewing vs stewardship split?
8. How do products enforce quality (watch-only vs pipeline gates vs CI/CD)?
9. Where is the boundary vs Data Observability, Data Governance, Data Catalog, MDM, ETL, dbt tests, data preparation?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence tier |
|---|---|---|
| **Soda** (Soda Core / Soda Cloud) | checks-as-code + cloud workspace; modern data stack; explicitly self-labels "a data quality platform" | Tier 1 (docs.soda.io, extensive) |
| **Great Expectations (GX Core)** | OSS expectations-as-code library; developer-first validation framework | Tier 1 (docs.greatexpectations.io) |
| **Ataccama ONE Data Quality & Catalog** | unified DQ + catalog + observability platform; enterprise; steward-oriented | Tier 1 (docs.ataccama.com, extensive) |
| **Talend Studio Data Quality** (Qlik Talend) | suite module with OSS heritage; profiling + embedded cleansing components; enterprise IT | Tier 1 (help.qlik.com Talend Studio guide) |
| **Oracle Enterprise Data Quality** | legacy on-prem enterprise DQ environment | Tier 2 (positioning page only — see Sources) |

Cross-references from already-processed sibling passes (used as corroboration, not primary evidence): data-observability-platform, data-governance-platform, data-catalog, data-integration-platform (Informatica IDMC "Data Quality" suite service), data-labeling-platform, sales-data-enrichment-platform, clinical-data-management.

## Sources

Primary (fetched 2026-09-07):

- Soda — https://docs.soda.io (readme/What is Soda; llms.txt index; /data-testing; /manage-issues/incidents)
- Great Expectations — https://docs.greatexpectations.io/docs/home ; /docs/core/introduction/gx_overview
- Ataccama ONE DQ&C — https://docs.ataccama.com/one/latest/overview.html ; /data-quality/data-quality-overview.html ; /data-quality/data-quality-dimensions.html
- Talend (Qlik) — https://help.qlik.com/talend/en-US/ (help home) ; Talend Studio User Guide: what-is-talend-studio ; profiling-and-data-quality
- Oracle — https://docs.oracle.com/en/middleware/fusion-middleware/enterprise-data-quality/14.1.2/index.html (Get Started / positioning only)

**Source-access limitation:** docs.informatica.com returned HTTP 403 on two attempts (2026-09-07) and was abandoned per the network-restriction rule. Informatica — arguably the category-defining enterprise DQ vendor — is therefore absent from direct evidence. The enterprise-suite pole is covered by Ataccama, Talend, and Oracle EDQ, plus the data-integration-platform pass's captured observation that Informatica IDMC ships "Data Quality" as a suite service ("Ingest, integrate and cleanse your data"). No Informatica-specific claims are made in the final document. Oracle EDQ evidence is limited to its positioning page (deeper pages use redirect links that could not be resolved); its claims are kept at positioning strength.

---

## Product A — Soda (Soda Core / Soda Cloud)

### Key observations (evidence layer A unless noted)

- **Self-positioning:** "Soda is a data quality platform that helps organizations make sure their data can be trusted… monitor data quality, catch problems early, understand issues at source, and take action quickly." Defines data quality as "how well a dataset meets the expectations of completeness, accuracy, timeliness, uniqueness, and consistency."
- **Three modes of one platform:** data testing (proactive, defined expectations), data observability (reactive, ML-powered anomaly detection "without needing to define every rule up front"), data contracts (producer–consumer agreements made explicit and testable). Testing and observability are presented as complementary halves of "end-to-end data quality management."
- **Checks as the unit of definition:** SodaCL ("Soda Checks Language — a human-readable, domain-specific language for data reliability") defines checks in YAML; metric families include missing, validity, numeric, freshness, schema, distribution, reference (value-in-another-table), reconciliation (source vs target), failed rows, group-by, for-each (apply across many datasets), custom SQL, check templates (reusable SQL).
- **Data contracts:** "formal agreement between data producers and data consumers that defines what 'good data' looks like… testable artifacts that can be authored, versioned, verified, and monitored." Verification checks schema match + checks (missing, duplicate, invalid, custom). Two authoring styles: Cloud-managed (no-code UI for analysts/owners) and Git-managed (YAML via Soda Core CLI, CI/CD, Git as source of truth); hybrid collaboration (business users propose changes in UI, engineers sync to Git).
- **Data Standards:** "write data quality checks once and deploy them across many datasets at scale" — a scoped standard applied to a dataset population.
- **Execution:** scans (manual, scheduled, orchestrated via Airflow/Dagster/Prefect/ADF); Soda Core (OSS engine, run anywhere incl. CI) vs Soda Runner (managed/self-hosted runner for scheduled execution + observability features).
- **Results & review:** check results with pass/fail; failed row samples (configurable, can be rerouted away from cloud for sensitivity); dataset dashboards; organization dashboard; browse checks/datasets; check and dataset attributes (custom metadata for organization); analyze monitor and check results.
- **Incidents:** "An incident is created when a data issue, such as a failed or warning check, has been confirmed and assigned to someone for resolution." Incident = name/description + related check results + lead (required) + status + severity + reporter; resolution note mandatory on resolve; org-wide incidents view with filters; Slack/Teams/webhook/Incidents API integration. Permission "Manage Incidents" per dataset.
- **Roles:** global roles + dataset roles; SSO; SCIM provisioning; service accounts; audit trail.
- **Integrations:** catalogs (Alation, Atlan, Collibra, Purview, data.world, Metaphor), chat (Slack/Teams), ticketing (Jira, ServiceNow), webhooks, dbt (ingest dbt test results), BI (Looker/Tableau/Power BI/Sigma), orchestration.
- **Deployment:** Soda Core OSS library+CLI; Soda-hosted Runner; Self-hosted Runner (Kubernetes); data-source connections managed at environment level; in-memory sources (Spark/DataFrames) supported only via Core.
- **Profiling:** dataset/column profiling "provides a quick and comprehensive overview of a dataset's structure and key statistics" — positioned as input for writing checks (supporting, not the center).

## Product B — Great Expectations (GX Core)

### Key observations

- **Self-positioning:** "GX is a framework for describing data using expressive tests and then validating that the data meets test criteria. GX Core is a Python library that provides a programmatic interface to building and running data validation workflows."
- **Component model (the cleanest statement of the DQ object graph):**
  - Data Context — the environment holding configurations, metadata, actions, and validation results.
  - Data Source → Data Asset → Batch Definition → Batch — how GX connects to and partitions the data it validates (databases, schemas, cloud object storage files; a Data Asset can be a table or a select query).
  - **Expectation** — "a verifiable assertion about data… similar to assertions in traditional Python unit tests… a flexible, declarative language for describing expected data qualities." Expectation Gallery = the library of available expectations.
  - **Expectation Suite** — a collection of Expectations; multiple suites per dataset for different use cases; same suite applicable to different batches.
  - **Validation Definition** — explicit association of a Batch Definition with an Expectation Suite.
  - **Validation Result** — returned per validation; "tell you how your data corresponds to what you expected of it."
  - **Checkpoint** — "the primary means for validating data in a production deployment": runs a list of Validation Definitions with shared parameters; can trigger **Actions**.
  - **Actions** — process validation results automatically (email, Slack/Teams, custom notifications) — the integration seam into pipelines.
  - **Data Docs** — "human-readable documentation generated by GX that host your Expectation Suite definitions and Validation Results."
- **Workflows:** interactive/exploratory validation (validate a batch immediately, review results) and production validation (orchestrator-triggered scheduled checkpoints over essential tables; consistent suites across sharded infrastructure).
- No UI stewardship surface in GX Core (OSS library); the platform layer (history, docs, actions) is what makes it operational.

## Product C — Ataccama ONE Data Quality & Catalog

### Key observations

- **Self-positioning:** "Ataccama ONE Data Quality & Catalog unifies Data Quality, Data Catalog, and Data Observability into a single, AI-augmented platform." Five sections: Knowledge Catalog, Business Glossary, **Data Quality**, Data Observability, ONE Data (+ Data Stories BI).
- **Definition of DQ:** "There is no single definition of what makes data high quality: data quality is a measure of the condition of your data according to your needs. Evaluating data quality helps you identify issues in your dataset that need to be resolved."
- **Core flow (vendor-documented):** glossary terms applied to catalog items (via detection rules, AI suggestions, or manually) → DQ evaluation rules mapped to terms (or directly to attributes) → run DQ evaluation → result is a **data quality percentage** = share of records passing all applied rules. The metric appears throughout the app (sources, terms, catalog items, attributes).
- **DQ rules:** rule types DQ vs Detection; evaluation rules with conditions determining pass/fail; aggregation rules; component rules; advanced expressions (ONE Expressions); rules can be created from profiling results; rule suggestions (AI); lookups (reference tables) usable in rules; validation components.
- **DQ dimensions:** "different logic types for data quality rules… when creating a DQ rule, you must select to which dimension the rule should belong." Fully configurable; presets: **Validity, Uniqueness, Completeness, Accuracy, Timeliness** (each with configurable named results, e.g. Valid/Invalid). Each result has an effect on overall quality: Pass / Fail / Not applicable (N/A excluded from the percentage). Overall Quality is computed per record (any fail fails the record; all-N/A records excluded) then aggregated: passed / (passed + failed) × 100. Dimension settings are published through a governance workflow (publish/discard); dimensions in use cannot be deleted, only deactivated.
- **Monitoring projects:** select catalog items, apply rules, run scheduled + ad hoc, configure notifications; DQ reports with per-dimension results, filters, custom alerts; invalid samples (view the failing data); record-level results not stored by default — post-processing jobs (transformation plans, post-processing plans, **data remediation plans**, export invalid records) run with each monitoring run.
- **Remediation:** invalid records can be loaded into ONE Data (the platform's own table layer) for "data remediation" — fix errors directly, then re-evaluate; compare and merge records.
- **Enforcement:** DQ Firewalls; **DQ Gates** — run rules locally in Python, as Snowflake UDFs, or with Snowflake DMFs (evaluate quality inside the warehouse/pipeline); Data Transformation Plans.
- **Data reconciliation:** source-vs-target comparison as a DQ capability.
- **Explicit DQ-vs-observability separation (load-bearing for the boundary):** "Additional checks are available in monitoring projects and in the Data Observability module: structure checks and AI anomaly detection. **However, these don't contribute to the data quality metric.**" Data Observability = "monitor whole sources quickly and easily… automatically discover data domains… apply bundled DQ evaluation rules, detect anomalies, and monitor other changes, alerting you in case of issues."
- **Governance machinery:** stewardship assignment, governance roles, access levels, share access to assets, data protection classification, policies, comments, tasks, workflows, publish changes, audit.
- **Deployment:** Ataccama Cloud, hybrid (customer-hosted processing engine DPE + cloud control plane), self-managed; pushdown processing for Snowflake/Databricks/BigQuery/Synapse.

## Product D — Talend Studio Data Quality (Qlik Talend)

### Key observations

- **Positioning within a fabric:** Talend Studio is "a comprehensive data quality and data management solution"; DQ ships as the **Profiling perspective** + DQ components in the Integration perspective; part of Talend Data Fabric alongside Data Preparation, Data Stewardship, Data Catalog, Data Inventory.
- **Profiling perspective:** connect to data sources (metadata repository stores structure: catalogs, schemas, tables) → analyses (table analyses, column analyses, correlation analyses) → results browsed in Data Explorer; **patterns** (predefined regular expressions + SQL LIKE patterns) and **indicators** (system + custom) as the reusable evaluation vocabulary; **reports** with a **report database** "where you can keep a history of created reports and share results among team members."
- **Cleansing embedded in pipelines:** "From the Integration perspective, you have access to hundreds of components… including many data quality components that are used to cleanse data" — DQ logic embedded in data integration Jobs (the ETL seam).
- **Stewardship sibling:** Talend Data Stewardship (separate product in the fabric) handles task-based remediation/certification — the remediation leg lives outside the profiling tool.
- License-gated (enterprise editions); desktop Studio + cloud; feature installed via Feature Manager.

## Product E — Oracle Enterprise Data Quality

### Key observations (Tier 2 — positioning only)

- "Oracle Enterprise Data Quality is a comprehensive data quality management environment, used to understand, improve, protect and govern data quality."
- Ships with **Address Verification Server** (postal/address verification — the reference-data validation pole) and a **Customer Data Services Pack** (CRM/CDS integration).
- On-prem Fusion Middleware heritage (release 14.1.2; lineage back to 12.2.1.x); integrates with Oracle Data Integrator and Siebel.
- Deeper operational pages were not reachable (redirect-based doc links); no operational claims made beyond positioning.

---

## Cross-product Comparison

| Structure / capability | Soda | GX | Ataccama | Talend Studio DQ | Oracle EDQ | Assessment |
|---|---|---|---|---|---|---|
| Defined rule/expectation/check as named reusable object | A (SodaCL checks, templates, standards) | A (Expectation, Suite) | A (DQ evaluation rules, detection rules) | A (patterns, indicators, rule components) | B (positioning: "understand, improve") | **Defining** |
| Evaluation against the organization's data (platform not the system of record for that data) | A (scans against warehouses/DBs; data stays in source) | A (batches from data sources; data stays in source) | A (catalog items over connected sources; pushdown) | A (analyses over connected sources) | B (staged processing environment) | **Defining** (in-place or staged-copy both observed; "not system of record" is the invariant) |
| Recorded pass/fail results attributed to data + rule | A (check results, scans) | A (Validation Results, Data Docs) | A (DQ evaluation results, Overall Quality %) | A (analysis results, report database history) | B | **Defining** |
| Quality dimension taxonomy | B (metric families: missing/validity/freshness/schema…) | B (expectation gallery categories) | A (configurable dimensions; presets Validity/Uniqueness/Completeness/Accuracy/Timeliness) | B (indicator types) | B | Common vocabulary, **not definitional** (shape varies; Ataccama makes it configurable) |
| Profiling | A (supporting role: input to checks) | (not central in GX 1.x docs) | A (profiling flows; rules can be created from profiling results) | A (the profiling perspective is the DQ entry point) | B | Common, **not definitional** |
| Scorecards / dashboards / reports | A (org + dataset dashboards) | A (Data Docs) | A (DQ reports, Overall Quality everywhere) | A (reports + report database) | B | Common |
| Failed-record drill-down / samples | A (failed row samples) | A (validation result details) | A (invalid samples; export invalid records) | A (analysis drill-down) | B | Common |
| Scheduling / orchestration | A (scheduled scans, orchestrators, Runner) | A (Checkpoints triggered by orchestrators) | A (monitoring projects scheduled + ad hoc) | A (via Talend Management Console / Administration Center) | B | Common |
| Alerting / notifications | A (notification rules, Slack/Teams/webhook) | A (Checkpoint Actions) | A (notification templates, Teams/Slack) | (via fabric) | B | Common |
| Issue / incident tracking | A (incidents: lead/status/severity/resolution note) | (not in GX Core OSS) | B (tasks/workflows; remediation plans) | B (Data Stewardship sibling) | B | Common, depth varies |
| Remediation / cleansing | (not a Soda focus — issue resolution at source) | (not in GX Core) | A (remediation plans, ONE Data fix + re-evaluate) | A (cleansing components in Jobs; Data Stewardship sibling) | B (improve; AVS correction) | Common-to-optional; **not definitional** |
| Enforcement in pipelines / warehouse | A (CI/CD testing; pipeline integration) | A (orchestrated checkpoints as gates) | A (DQ Firewalls, DQ Gates as Snowflake UDFs/DMFs, Python) | A (DQ components inside Jobs) | B | Common, depth varies |
| Reconciliation (source vs target) | A (reconciliation checks) | (possible via custom expectations) | A (data reconciliation projects) | (possible via jobs) | B | Optional |
| Data contracts | A (first-class: testable producer–consumer artifacts) | (not in GX Core docs) | (not as such; DQ Gates instead) | (not as such) | B | Optional / variant (single-product-led) |
| Standards applied across dataset populations | A (Data Standards with scope) | (suites reusable across batches) | (rules mapped to terms = population-level by design) | (patterns/indicators reusable) | B | Common in different shapes |
| Catalog / glossary integration | A (integrations; results pushed to catalogs) | (not in GX Core) | A (native catalog + glossary; rules attach to terms) | A (Data Catalog sibling) | B | Common (native or integration) |
| ML anomaly detection / observability mode | A (metric monitors, anomaly detection — a separate mode) | (not in GX Core) | A (Data Observability module — explicitly outside the DQ metric) | (not observed) | B | Optional; the observability seam |
| AI assistance | A (Ask AI checks, Contract Copilot/Autopilot, MCP) | (not observed in Core docs) | A (term suggestions, rule suggestions, anomaly detection, MCP server) | (not observed) | B | Optional, era-typical |
| Authoring surface | A (code-first SodaCL + no-code Cloud UI) | A (code/Python only) | A (UI-first + expressions) | A (desktop IDE UI) | B | Variant axis |
| Deployment | A (OSS core / hosted runner / self-hosted K8s) | A (OSS library; cloud offering exists beyond Core docs) | A (SaaS / hybrid / self-managed; pushdown) | A (desktop + cloud engines) | B (on-prem) | Variant axis |
| Roles / governance | A (global + dataset roles, SSO, SCIM, audit) | (not in GX Core) | A (governance roles, stewardship, policies, publish workflow, audit) | B (license tiers) | B (LDAP/AD) | Common at platform depth |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Three structures. Remove any one and the product stops being a Data Quality Platform:

1. **The defined quality rule as the primary managed object.** A named, reusable, governed condition ("expectation", "check", "DQ rule", "indicator/pattern") that states what the data should satisfy, attached to a target (dataset/table/column/term). The rule library — not any single run — is what the product centers on. Remove it → ad-hoc SQL scripts or one-off test code, not a platform.
2. **Execution of rules against the organization's data, which the platform does not own as system of record.** The platform connects to data systems (or stages working copies for processing) and evaluates the data there; the authoritative data remains in the organization's systems. Remove the evaluation → a rule editor/report builder; make the platform the system of record for the data → MDM or a data platform.
3. **Recorded pass/fail results attributed to data and rule.** Each evaluation produces a durable result (which data, which rule, pass/fail or score, when), reviewable with drill-down to failing records and retained as history. Remove it → a rules engine/SDK returning ephemeral booleans, not a managed quality system.

### L1 — Common Mature Structure

Present across the sample; expected in mature products but not required to recognize the Type:

- quality dimensions as an organizing vocabulary for rules and results (shape varies: configurable dimension objects, metric families, expectation categories)
- profiling (dataset/column statistics) as an input to rule authoring
- scorecards / dashboards / reports with trends and per-dimension breakdowns
- failed-record samples and drill-down
- scheduling and orchestration integration (managed runners, orchestrator triggers)
- alerting/notifications into chat and ticketing systems
- issue/incident tracking for confirmed failures (depth varies; strongest in Soda, present as tasks/workflows elsewhere)
- rule templates / reusable standards applied across dataset populations
- catalog/glossary integration (native or via connectors)
- roles/permissions/SSO/audit at platform depth
- APIs/CLI for programmatic control

### L2 — Variant / Optional Structure

- **Authoring surface:** code-first (SodaCL, GX Python) vs UI-first (Ataccama, Talend) — a philosophy axis, not a definition
- **Data contracts** as producer–consumer agreements (Soda-led; others express the same need via gates/standards)
- **Enforcement depth:** watch-only → pipeline gates (DQ Firewalls/Gates, orchestrated checkpoints, embedded cleansing components) → CI/CD shift-left
- **Reconciliation** (source vs target comparison)
- **Reference-data validation** (address/email/postal verification — Oracle AVS pole; regional)
- **Remediation depth:** none → export invalid records → in-platform fix-and-reevaluate (Ataccama ONE Data) → stewardship task queues (Talend sibling)
- **ML anomaly detection / observability mode** embedded as a second detection philosophy (Soda, Ataccama)
- **AI assistance** (rule/check suggestions, contract drafting, MCP servers)
- **Deployment:** SaaS, self-hosted, hybrid control/processing split, pushdown into warehouses, OSS library
- **Segment/tier:** developer-first OSS, mid-market data teams, enterprise steward-oriented suites

### L3 — Vendor-specific (kept out of the final document)

- Soda: SodaCL language, Soda Runner, Data Standards scoping, Contract Copilot/Autopilot, RAD
- GX: Data Context / Checkpoint / Action / Data Docs component names, Expectation Gallery
- Ataccama: ONE Data, DQ Gates (Snowflake UDF/DMF), DQ Firewalls, detection rules, term-suggestion AI, Data Stories
- Talend: patterns vs indicators vocabulary, report database, Feature Manager install, Data Stewardship sibling
- Oracle: Address Verification Server, Customer Data Services Pack, Fusion Middleware deployment

## Vendor-specific Findings

- Soda is the only sampled product that leads with **data contracts** as the primary organizing artifact (testable producer–consumer agreements) — treat as variant, not definition.
- Ataccama is the only sampled product with an explicit, documented **rule that observability features do not contribute to the DQ metric** — strong evidence for the DQ/observability boundary from the vendor side.
- Talend is the only sampled product where **cleansing components embedded in ETL jobs** are a first-class DQ surface — the pipeline-embedded pole.
- Oracle EDQ is the only sampled product with **postal address verification** as a named subsystem — the reference-data-validation pole (regional).
- GX is the only sampled product that is purely a **code library** with no stewardship UI in its OSS form — the minimal pole.

## Rejected Findings (considered and not promoted)

- **"DQ = the six classic dimensions"** — rejected: dimension sets differ per product (Soda metric families vs Ataccama configurable dimensions vs GX expectation categories); the dimension *concept* is common, any fixed taxonomy is not definitional.
- **"DQ platforms hold/cleanse the data"** — rejected as definitional: most sampled products evaluate in place; remediation is optional and varies from none to in-platform fix-and-reevaluate. The invariant is "not the system of record for the evaluated data," not "never touches data."
- **"DQ = ML anomaly detection"** — rejected: ML detection is the observability philosophy; DQ's defining detection is the defined rule. Products embed both, but the rule remains the DQ center (Ataccama explicitly excludes anomaly detection from the DQ metric).
- **"DQ requires a catalog/glossary"** — rejected: GX and Soda-core work without one; integration is common-optional.
- **"Data contracts define the Type"** — rejected: single-product-led; gates/standards/rules express the same intent elsewhere.

## Boundary Findings

### vs Data Observability Platform (§13) — DISCHARGES the joint-review flag from the observability pass

The observability pass held: "DQ centers the defined rule/test and its pass-fail result as the primary object; observability centers ambient health evaluation over the whole estate plus the incident loop." This pass confirms that split from the DQ side with direct evidence:

- The DQ sample centers on **authored rules**: Soda's checks/contracts ("define every rule up front" vs ML monitoring), GX's Expectations ("verifiable assertions"), Ataccama's DQ evaluation rules, Talend's patterns/indicators.
- The observability philosophy appears **inside** DQ products as an embedded second mode (Soda metric monitors/anomaly detection; Ataccama Data Observability module) — and Ataccama explicitly states structure checks and anomaly detection "**don't contribute to the data quality metric**." Vendor framing itself separates the two.
- Conversely (from the other pass), observability products embed quality rules as one monitor family. The interlock is real and bidirectional; the primary-object test (authored rule + recorded pass/fail vs ambient baseline + incident loop) cleanly separates the Types.
- **Verdict:** two distinct Types with a documented, bidirectional capability interlock and heavy packaging convergence (Ataccama ships both as sibling modules; Soda ships both as modes of one platform). The joint-review flag is discharged; no merge recommended. Boundary Issues entry updated accordingly.

### vs Data Governance Platform (§13)

Governance platforms integrate quality as one governed dimension (scores, rules surfaced in governance views); DQ platforms center the rule/evaluation machinery itself. From the governance pass: "quality platforms center rule/test/monitoring machinery; governance platforms integrate quality as one governed dimension." Seam held. Ataccama straddles by packaging (DQ&C + governance roles in one platform), but its DQ section is a recognizable instance of this Type.

### vs Data Catalog (§13)

The catalog surfaces quality signals on entries; the DQ platform produces them. From the catalog pass: "Data Quality Platforms exist separately; surfacing signals is common-optional." Seam held.

### vs Master Data Management (§13)

MDM is the system of record for master data (golden records); DQ evaluates data it does not own. They interlock (DQ rules often validate MDM outputs; Ataccama connects to MDM/RDM as sources; Oracle EDQ serves Fusion/Siebel master data). Remove "not system of record" and DQ collapses toward MDM.

### vs ETL/ELT Platform (§13)

Movement vs evaluation. The seam is pipeline-embedded DQ (Talend cleansing components inside Jobs; Soda/GX checks invoked by orchestrators; Ataccama DQ Gates in warehouses) — a capability relationship, not a Type merge. The data-integration-platform pass already recorded the inverse seam (Informatica IDMC ships Data Quality as a sibling service).

### vs dbt tests / test frameworks (capability, not Type)

dbt tests, SQL check constraints, and unit-test-style assertions express the same "verifiable assertion" pattern but lack the managed platform layer (cross-source connections, result history, stewardship, scorecards, incident workflow). DQ platforms ingest external test results (Soda ingests dbt test results) — the capability feeds the platform.

### vs Data Preparation / Cleansing tools

Preparation tools interactively transform a working copy (Talend Data Preparation sibling); DQ platforms continuously evaluate the data of record against governed rules. Cleansing appears in DQ as optional remediation, not as the center.

### vs Software Test frameworks (§12)

Same assertion pattern, different object: code behavior vs data condition. Different users (developers vs data teams), different result semantics (build pass/fail vs data quality scores over time).

### "去掉什么就变成另一个 Type" 判据

- Remove the defined-rule library → ad-hoc scripting/test code (capability, not platform)
- Make the platform the system of record for the data → MDM / data platform
- Remove recorded results/history → rules engine or SDK
- Replace authored rules with ambient learned baselines + incident loop as the center → Data Observability Platform
- Replace data evaluation with data movement → ETL/ELT Platform
- Replace data condition with code behavior → software test framework

## Historical / Market-Sample Check

- **Older products fit:** Oracle EDQ (2000s on-prem), Talend OSS DQ (2000s), and the classic enterprise DQ suites (Informatica-class, per sibling-pass evidence) are all rule/analysis-based, on-prem, no cloud, no ML — they satisfy the L0 (defined rules + evaluation + recorded results). The L0 does not depend on cloud, ML, contracts, or catalogs.
- **Even older / pre-platform forms:** SQL check constraints, validation scripts, and postal-address batch tools implement rules + evaluation but lack the managed rule library and result layer; they are capabilities or minimal precursors, not the platform form. The minimal platform form (GX Core as a library) still carries the managed rule + result objects, which supports keeping L0 at three structures.
- **Dimension taxonomy is era-stable but not definitional:** completeness/validity/uniqueness/accuracy/timeliness vocabulary predates all sampled products (DAMA/ISO heritage) and appears as presets in Ataccama and as metric families in Soda — but products reconfigure it freely, so it stays L1.
- **The contract wave is current-market, not definitional:** data contracts are a 2020s framing; older products satisfy the Type without them.

## Uncertainties

- **Informatica absent from direct evidence** (docs 403 ×2). The enterprise-suite pole is triangulated via Ataccama/Talend/Oracle + the data-integration-platform pass's captured IDMC structure. If a later pass can access Informatica docs, re-verify the steward-oriented rule/monitoring model.
- **Oracle EDQ operational detail not verified** (redirect-based docs); only positioning-level claims used.
- **Precisely (Trillium), SAP, Collibra DQ not directly researched** — the enterprise pole rests on three products; no claims depend on them individually.
- **Data contracts' trajectory** (whether they become the standard organizing artifact across the category) is uncertain; treated as variant.
- **Real-time/streaming DQ** was not directly evidenced in the sampled docs (Soda/Ataccama operate on scheduled/pushdown evaluation); not claimed.

## Final Synthesis

A Data Quality Platform is the rule-centered quality system for an organization's data. Its defining core is small: **defined quality rules** (named, reusable conditions stating what data should satisfy) are the primary managed object; the platform **executes those rules against the organization's data** — data it connects to or stages for processing, but never owns as system of record; and every execution produces **recorded pass/fail results** attributed to the data and rules, reviewable with drill-down to failing records and retained as history. Around that spine, mature products add the dimension vocabulary, profiling, scorecards and reports, scheduling and orchestration, alerting, issue/incident tracking, reusable standards, catalog integration, roles and audit, and programmatic control; variants add contracts, pipeline enforcement gates, reconciliation, reference-data validation, remediation depth, embedded anomaly detection, AI assistance, and a spread of deployment and authoring philosophies. The Type sits between the Data Observability Platform (ambient health + incident loop — the two interlock and increasingly ship together, but the authored rule with its recorded pass/fail result remains the DQ center), the Data Governance Platform (quality as one governed dimension), the Data Catalog (signals vs production), MDM (system of record vs evaluator), and ETL/ELT (movement vs evaluation).
