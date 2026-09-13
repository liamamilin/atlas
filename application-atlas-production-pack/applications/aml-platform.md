# AML Platform

## Overview

An **AML Platform** (Anti-Money Laundering platform) is the compliance system a regulated financial institution operates to detect potentially suspicious activity in its own customer and transaction data, investigate that activity through a documented human review process, and produce the regulatory reports (suspicious activity / suspicious transaction reports) that anti-money-laundering and counter-terrorist-financing laws require.

The defining structure is the end-to-end compliance loop:

```text
Monitored customers (with due-diligence context)
  ↓
Ingested institutional activity (transactions, behavior)
  ↓
Configurable detection (rules / scenarios / models) → Alerts
  ↓
Human investigation (alert → case → disposition, recorded)
  ↓
Regulatory report filed with the competent authority
  ↓
Everything auditable end to end
```

The platform is not a fraud-prevention tool and not a generic reporting tool: its purpose is a regulatory obligation. The institution must be able to show a regulator *what activity it monitors, how it decides what is suspicious, who decided, and what was reported*. This purpose shapes the whole product — detection logic is configurable rather than fixed, every analytical and human decision leaves an audit trail, and the workflow terminates in a formal report to a financial intelligence unit rather than in a business action such as blocking a payment.

## Users & Context

AML platforms are operated inside institutions that are legally obligated to run an AML program: banks, fintechs and payment companies, crypto-asset businesses, credit unions, money services businesses, and similar regulated entities.

Primary users:

- **Transaction-monitoring / alert analysts** — work the alert queue: open each alert, review the activity and customer context behind it, decide whether it is explainable or warrants escalation, and record the rationale.
- **Investigators** — take escalated alerts, build a case: assemble related transactions, linked customers, screening results and prior history; write the investigation narrative; recommend a disposition.
- **BSA/AML compliance officers (in some jurisdictions titled MLRO)** — own the program. They decide whether a case results in a report being filed, and they answer for the program to regulators.
- **Reporting / FIU liaison staff** — prepare and submit the regulatory report in the jurisdiction's required format.
- **Detection and model teams (compliance analytics)** — configure and tune rules, thresholds, segments and models; measure rule performance; manage model validation.

Secondary users:

- **IT/integration administrators** — connect data sources, manage users and permissions.
- **Internal audit and examiners** — read-only consumers of the audit trail, configurations, and decision history.

The work is queue-driven: analysts and investigators spend most of their day inside alert queues and case workspaces, while configuration and oversight surfaces belong to smaller, more specialized groups.

## Core Model

The platform's world is built from a small set of objects, connected by the compliance loop.

### Monitored customer

The unit of obligation. Every customer of the institution exists as an identified record carrying due-diligence context — who they are, their risk classification, and the results of screening and due diligence. Monitoring, alerts, cases, and reports are all anchored to customers (and, where applicable, to related parties such as beneficial owners or counterparties). The customer record is not static: mature products continuously update it as new activity, screening hits, and network associations arrive.

### Activity

The institution's real transactional data — payments, transfers, cash movements, trades, depending on the institution — flows into the platform. The platform does not generate this data; it is the analytical layer over the institution's actual behavior records. Detection quality depends on this ingestion being complete and well-structured.

### Detection logic (rules, scenarios, models)

The institution's configurable definition of "suspicious." Common implementations observed across the researched sample include:

- **Simple rules** — check attributes of a single transaction.
- **Aggregate rules** — track activity across multiple transactions over time (for example, velocity or accumulated-amount patterns).
- **Behavioral rules** — compare current activity against the customer's own past activity.
- **Risk-pattern scenarios** — encode known money-laundering typologies (structuring, layering patterns, mule behavior and similar named patterns).
- **ML models** — learn from historical labeled outcomes (including past investigator dispositions) to score how suspicious new activity is; also used for anomaly detection and customer segmentation.

Rules and scenarios are parameterized with **thresholds** and applied against **customer segments**; tuning these values to balance detection coverage against alert volume is a core ongoing activity, supported in mature products by testing environments (sandboxes) and calibration tooling.

### Alert

A generated flag that a rule, scenario, or model matched. An alert carries its triggering activity, the customer context, the detection logic that fired, and (in mature products) a risk score used to prioritize work. Alerts are the unit of daily analyst work.

### Case

The investigation container. An analyst escalates one or more related alerts into a case, assembles evidence (transaction history, related entities, screening results, prior alerts and cases, documents), and records the investigation narrative and rationale. The case is where scattered signals become a documented, reviewable investigation.

### Regulatory report

The terminal artifact. When a case concludes that the activity is suspicious, the platform assembles the jurisdiction-appropriate report — the suspicious activity / suspicious transaction report family (in the researched sample: SAR, STR, CTR, and goAML- and FINTRAC-format filings appear) — populated from the case record, and tracks it to submission. This object is what gives the platform its regulatory identity.

### Audit trail

A first-class object, not an afterthought. Every analytical configuration change (rules, thresholds, models), every alert disposition, every case decision, and every filing is recorded with who, when, and why. Several products extend this to making AI-driven scores and decisions explainable in natural language for the same audience.

### Relationship graph

Mature products maintain connections between entities — customers, accounts, counterparties, devices — so investigators can see networks (linked accounts, mule patterns, clusters) rather than isolated records. This is a standard capability of current products rather than a requirement for the Type to exist.

## How It Works

The platform runs one defining loop plus a continuous customer-side process.

### The detection loop (alert → case → report)

```text
Activity is ingested from institutional systems
  → detection logic evaluates it against configured rules/scenarios/models
  → matches become alerts, scored and prioritized
  → an analyst reviews the alert: explainable? → close with recorded rationale
                                    → suspicious? → escalate into a case
  → an investigator builds the case: evidence, related entities, narrative
  → a senior compliance decision: file or not file
  → the platform assembles and tracks the regulatory report
  → every step is written to the audit trail
```

Two things about this loop are structurally important:

1. **The human is the decision-maker.** Detection is automated; disposition is not. The platform surfaces, scores, and documents, but the suspicion judgment and the filing decision are made (and signed for) by people. Even in products with agentic AI that pre-resolves routine alerts or pre-drafts narratives, the observed pattern keeps a human decision gate.
2. **The loop must be defensible, not just correct.** The institution must reconstruct, months later, why an alert was closed, why a case was filed, and why detection was configured the way it was. This is why configuration versioning and audit trails are structural rather than optional.

### Detection management (tuning cycle)

```text
Draft or adjust a rule/scenario/model
  → test (sandbox / below-the-line analysis / threshold comparison)
  → measure impact on alert volume by segment
  → approve and version the change
  → monitor performance (hit rates, false-positive trends)
  → recalibrate
```

False positives are the operational reality of this software: legitimate activity routinely triggers rules. A large share of the platform's tooling exists to keep alert volume compatible with available analyst capacity while maintaining detection coverage — segmentation, scoring, threshold calibration, and per-rule performance measurement.

### The customer-side process (ongoing monitoring)

```text
Customer onboarded (via KYC processes; the AML platform consumes this context)
  → initial risk rating and screening results recorded
  → activity and behavior continuously update the customer's risk picture
  → new screening hits or risk-relevant changes trigger review (EDD)
  → periodic review cycles re-confirm due diligence
```

This is what distinguishes an AML platform from an onboarding-time KYC tool: the platform watches the entire customer relationship, not just the entry point.

## Interfaces

The surfaces below are described conceptually; exact names and layouts vary by product.

### Alert queue / monitoring dashboard

- Purpose: the daily work surface for alert analysts.
- Typical information: prioritized alerts with risk scores, triggering rule/scenario, customer, amounts, aging.
- Primary actions: open an alert, assign, disposition (close / escalate), record rationale.

### Alert / investigation workspace

- Purpose: understand one alert in context.
- Typical information: the triggering activity, surrounding transaction history, customer profile and risk rating, related entities, screening hits, prior alerts and cases.
- Primary actions: inspect linked records, annotate, escalate to case, close with reason.

### Case workspace

- Purpose: conduct and document an investigation.
- Typical information: consolidated evidence, related alerts, entity relationships (often as a graph view), the narrative, decision history.
- Primary actions: attach evidence, edit narrative, request review, record disposition, hand off to reporting.

### Detection configuration

- Purpose: let the institution own its detection logic.
- Typical information: rule/scenario library, parameters and thresholds, customer segments, model versions and performance.
- Primary actions: create/modify logic, set thresholds, test before deployment, version and approve changes.

### Customer 360 / risk profile

- Purpose: view a customer's complete risk picture.
- Typical information: identity and due-diligence status, risk rating and its drivers, screening results, activity patterns, network associations, alert/case history.
- Primary actions: adjust risk rating, trigger EDD review, open related cases.

### Reporting / filing screens

- Purpose: assemble and track regulatory reports.
- Typical information: report forms for the relevant jurisdiction, pre-populated case data, filing status.
- Primary actions: review populated fields, submit/export, track submissions.

### Analytics and oversight dashboards

- Purpose: manage the program, not individual alerts.
- Typical information: alert volumes and false-positive trends per rule, analyst productivity and queue aging, model performance.
- Primary actions: tune priorities, reallocate capacity, prepare for examinations.

## Important Rules / Behaviors

- **The institution owns the detection logic.** The platform ships detection frameworks, typology libraries, and calibration tools, but the rules, thresholds, and segments reflect the institution's risk assessment and must be defensible as such. Two institutions on the same product typically run different configurations.
- **Suspicion is judged by humans; only detection is automated.** Products differ in how much AI assists (scoring, pre-analysis, narrative drafting), but the filing decision remains a human, senior-compliance-level act in the observed sample.
- **Multi-stage review is configurable to mirror the institution.** Alert triage, investigation, and decision stages are configured to match the institution's own structure; the number and naming of stages vary by product and institution.
- **Nothing is disposable.** Alerts closed as false positives remain recorded; superseded rules and thresholds remain versioned; case narratives and evidence remain attached. The historical record is the compliance evidence.
- **Screening is continuous, not one-time.** Watchlist and sanction list changes, as well as changes in customer behavior, re-open risk on existing customers through ongoing monitoring.
- **Regulatory formats are jurisdiction-specific.** The report an institution files — and the data fields it requires — depend on the jurisdiction; platforms therefore maintain multiple report formats rather than one universal schema.
- **Auditability extends to AI.** Where models score alerts or agents assist investigations, current products expose the reasoning behind those outputs to the same audit standard as human decisions.

## Variants

Common shapes of the Type:

- **Enterprise banking suites** — modular platforms for large institutions spanning transaction monitoring, screening, KYC lifecycle, case management, and reporting, often with long on-premises heritage and current cloud delivery.
- **Cloud-native mid-market platforms** — SaaS products with proprietary risk data (sanctions/PEP/adverse-media intelligence), self-service configuration, and API-first integration, aimed at fintechs, payments companies, and smaller banks.
- **ML-first / converged risk platforms** — platforms that treat fraud and AML as one risk discipline ("FRAML") on a shared data core, selling behavioral analytics as the differentiator.
- **API-first operations platforms** — developer-oriented platforms for fintech/crypto operations teams, with custom object models, embedded AI agents, and heavy workflow automation.
- **Scaled-down editions** — "essentials"/starter cloud versions of enterprise suites for smaller institutions with lighter configuration needs.

Deployment, industry (banking vs crypto vs payments), and regulatory regime (US, EU, UK, Canada, goAML jurisdictions) cut across all of these; they change formats, integrations, and emphasis, not the core loop.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Transaction Monitoring Platform | subset / adjacent | the detection-alerting engine that every AML platform contains; a TM-type product's terminal output is alerts (handed to another system), whereas an AML platform owns the case investigation and the regulatory report |
| Sanctions Screening Platform | adjacent | list-based name matching (sanctions/PEP/adverse media) gating customers and payments; no behavioral transaction analysis; commonly integrated into an AML platform but independently deployable |
| Fraud Detection Platform | adjacent | purpose is loss and customer protection; terminal outcome is a real-time block/decline/recovery action, not a regulatory report; converging products exist but the disciplines keep different objectives and evidence trails |
| KYC / KYB Platform | adjacent | identity verification and due diligence at onboarding; the AML platform consumes KYC context and adds ongoing behavioral monitoring over the relationship |
| Regulatory Reporting Platform | adjacent | broader regulatory reporting (prudential, statistical, transaction reporting); the AML platform produces specifically the suspicious-activity report derived from its own investigation flow |
| GRC / Compliance Management Platform | different domain | manages policies, controls, obligations, and assessments at the governance layer; the AML platform is an operational detection and investigation system executing part of the AML program |

The most important boundary is with **Transaction Monitoring Platform**: in the market, "transaction monitoring" is often the headline capability under which full AML platforms are sold. The distinction holds when the TM Type is understood as the detection/alerting capability, and the AML Platform as the program-level system of record ending in regulatory reporting.

## Representative Products

- NICE Actimize (AML suite: SAM, STAR, entity risk, screening, KYC lifecycle)
- Oracle Financial Crime and Compliance Management (FCCM)
- ComplyAdvantage Mesh
- Feedzai RiskOps / AML Suite
- Unit21

These span enterprise banking suites, cloud-native mid-market platforms, ML-first converged platforms, and API-first operations platforms.

## Sources

Research date: **2026-09-06**

- NICE Actimize — corporate site, AML solutions page, SAM (Suspicious Activity Monitoring) product page: https://www.niceactimize.com/ , https://www.niceactimize.com/anti-money-laundering , https://www.niceactimize.com/anti-money-laundering/suspicious-activity-monitoring
- Oracle — Financial Crime and Compliance Management solution page (including FAQ on behavioral models and scenario calibration): https://www.oracle.com/financial-services/aml-financial-crime-compliance/
- ComplyAdvantage — corporate site and Transaction Monitoring product page (including rules/configuration/case-management/reporting detail): https://complyadvantage.com/ , https://complyadvantage.com/mesh/transaction-monitoring-software/
- Feedzai — corporate site and AML solution page (including FAQ): https://www.feedzai.com/ , https://www.feedzai.com/anti-money-laundering/
- Unit21 — corporate site (AML product suite: transaction monitoring, case management, screening, customer risk rating, regulatory filings): https://unit21.ai/

> Sourcing limitation: vendor help centers and detailed operational documentation were largely not reachable from the research environment (e.g., Unit21's documentation portal is access-gated; several vendors keep operational detail in datasheets not accessible here). All observations come from official vendor product and solution pages, including on-page FAQs. Operational specifics that could not be verified — exact stage counts, SLAs, filing-integration depth, list-coverage counts — are intentionally not asserted in this document; workflow and capability claims are phrased at the strength the reachable evidence supports.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical-sample check are recorded in the paired Research Notes.
