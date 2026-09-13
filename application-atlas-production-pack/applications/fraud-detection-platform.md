# Fraud Detection Platform

## Overview

A **Fraud Detection Platform** is the operational system an organization uses to evaluate customer activity for fraud risk, decide what should happen to each activity record, route suspicious records to human review, and improve its own accuracy over time from confirmed outcomes.

The defining core is small:

```text
Activity records (transactions, orders, logins, signups, claims)
  → evaluated by configurable fraud logic (rules and/or models)
  → risk assessment (score and/or decision)
  → outcome on the record (allow / decline / review-class, sometimes a challenge)
  → suspect records reviewed by humans, who record dispositions
  → confirmed outcomes feed back into the logic
```

Everything else commonly associated with modern fraud platforms — device fingerprinting, behavioral biometrics, shared cross-customer network intelligence, chargeback modules, AI-generated rules — is widespread in current products but is not what makes the product a fraud detection platform. Older batch scoring systems with manual alert queues, and claims-fraud systems built on adjuster workflows, fit the same core without any of those specifics.

The platform sits inside someone else's flow: a checkout, an authorization switch, an onboarding journey, a claims process. Its job is to return a defensible fraud decision at the moment the host system needs one — and to record enough evidence that the decision can be explained, audited, and improved.

## Users & Context

Primary users:

- **Fraud analyst / fraud operations specialist** — works the review queue: opens suspect records, inspects signals and history, investigates linked activity, and records a disposition (confirm fraud, clear as legitimate, escalate). Throughput and accuracy of this role are first-class metrics of the platform.
- **Fraud / risk operations manager** — owns strategy: tunes rules and score thresholds, manages lists, balances fraud loss against false positives and customer friction, monitors dashboards.

Secondary users:

- **Data scientist / model risk roles** (strongest in banking and issuer deployments) — develop, test, and govern the scoring models; run champion-challenger comparisons.
- **Integration engineers** — connect the host system (checkout, banking, gaming, lending platform) to the platform's API and webhooks.
- **Compliance/AML teams** — in platforms that bundle fraud and AML, they share the case-management layer while keeping distinct workflows.
- **Executives** — consume loss, approval-rate, and operations dashboards.

The work environment is an operations console used continuously by the fraud team, plus an API surface consumed by engineering. Unlike most Application Types in this atlas, the platform's most important "user" interaction is often machine-to-machine: the host system asks for a decision in real time and acts on it without a human in the loop.

## Core Model

### The Defining Core

Three structures. If any one is removed, the product is no longer recognizable as a fraud detection platform:

- **Activity records under evaluation** — the platform receives records describing user-initiated activity: a payment transaction, an order, a login, an account signup, a funds transfer, an insurance claim. It is the system of record for fraud risk on those records: each record carries its evaluation history, its score, its outcome, and its review trail. Without this, there is nothing to detect fraud on.
- **Evaluation machinery producing a risk assessment** — configurable fraud logic (business rules, machine-learning models, or both) evaluates each record against the customer's history, the record's signals, and cross-record patterns, and produces a risk assessment: a score and/or a recommended decision. Without this, the product is just a data store or a signal provider.
- **Decision outcome with a human review path** — the assessment resolves into an outcome on the record — allow, decline, or a review-class state — and records that land in the review class can be routed to human reviewers who investigate and record a disposition. Without an outcome, the platform is analytics; without any review path, it degenerates into a scoring service.

### Standard Capabilities

Mature products commonly add the following. They make the platform effective but do not define the Type:

- **Signal enrichment** — the record is augmented before evaluation: device and browser intelligence, email/phone/IP reputation and digital footprint, behavioral signals, geolocation, and third-party data sources. Enterprise deployments orchestrate internal data (customer, account, transaction history) with external providers.
- **Entity profiles** — customer, user, account, and device records that aggregate history and risk over time, so a decision about one event can draw on the entity's past behavior and on links between entities (shared devices, addresses, payment instruments).
- **Cross-record pattern detection** — velocity rules (rates of events per entity or instrument), aggregates over time windows, similarity and duplicate detection, and link/network analysis that surfaces coordinated or related activity (mule accounts, account rings, multi-accounting).
- **Lists** — managed sets of known-bad, known-good, and watch values (devices, emails, IPs, cards, user IDs) that force or anchor outcomes: block-listed values are declined regardless of score; allow-listed values pass regardless of score; watch-listed values are flagged for monitoring or use in rules.
- **Review queues and case management** — worklists of suspect records with assignment, priority, notes, attached documents, linked records, and a full audit trail; dispositions are recorded against the record or an associated case.
- **Feedback loop** — analyst dispositions, labels, chargebacks, and confirmed-fraud outcomes flow back into the platform and are used to tune rules, train or retrain models, and measure rule/model accuracy.
- **Performance analytics** — dashboards over fraud loss, chargeback rates, block/decline rates, false-positive indicators, manual review volume, analyst throughput and accuracy, and rule/model performance.
- **Change governance** — sandbox or test environments for rule and model changes, staged or approved rollout (including maker-checker approval for consequential changes), audit logs of configuration changes, and role-based access.
- **Step-up and challenge as an outcome** — between allow and decline, platforms can return an intermediate outcome that adds friction: step-up authentication, a challenge, or a hold — letting risk, not a blanket policy, decide where friction applies.
- **Chargeback and dispute handling** — ingestion of chargeback/dispute data (which arrives after fulfillment and is a primary ground-truth signal) and, in commerce-focused products, dispute workflow modules.
- **API and webhooks** — synchronous decision calls at decision points, plus asynchronous event notifications for outcomes that resolve later (manual review completion, chargebacks, list changes).

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Activity record
Implementations:  transaction/order event (commerce), authorization message (issuer),
                  login/signup event (account fraud), claim (insurance), manual entry

Concept:   Evaluation machinery
Implementations:  transparent point-scoring rules, opaque vendor ML models,
                  hybrid rules + separate model score, prebuilt industry models

Concept:   Outcome
Implementations:  approve/decline/review states returned in the API response,
                  allow/step-up/block friction decisions, guarantee-backed approval
```

A reader who has only seen one implementation — say, an API that returns a score at checkout — should still be able to recognize a bank's batch scoring system with next-morning analyst queues as the same Application Type.

## How It Works

### Connect activity to the platform

```text
Host system (checkout / banking app / gaming platform / claims system)
  → calls the platform's API at a decision point with the activity's data
  → or streams/batches records for monitoring
  → or an operator enters a record manually for a one-off check
```

Integration is the platform's front door. The host decides which moments are decision points (typically payment, signup, login, payout) and what data to send. Platforms commonly also offer packaged integrations for major commerce platforms.

### Enrich and evaluate

```text
Record received
  → signals gathered (device, digital footprint, behavioral, third-party, internal history)
  → entity profile and cross-record patterns consulted (velocity, links, lists)
  → rules and models evaluate the enriched record
  → risk assessment produced (score, rule hits, model output)
```

Rule hits and signal values are recorded against the evaluation so the assessment is explainable after the fact.

### Decide and act

```text
Assessment
  → mapped through thresholds, rules, and lists to an outcome
  → outcome returned to the host system (synchronously, at the decision point)
  → host system acts: fulfill / decline / hold / challenge / route to review
  → post-decision automations may fire (notify, tag, hold fulfillment, trigger workflow)
```

The platform may own the final decision or return a score the customer's own logic acts on; both shapes exist. In guarantee-model products, an approval also carries the vendor's financial liability for the outcome.

### Review what the machines did not resolve

```text
Review-class records (and alerts from monitoring rules)
  → queued, prioritized, assigned
  → analyst opens the record: score, signals, rule hits, entity history, linked activity
  → investigates (searches related records, inspects network/link views, contacts customer in some deployments)
  → records a disposition: confirmed fraud / legitimate / escalate / reclassify
  → disposition updates the record and feeds the learning loop
```

Case management carries the investigation: notes, documents, linked records, audit trail. Governance features (approval requirements, four-eyes-style controls) gate consequential actions in mature products.

### Learn and govern

```text
Confirmed outcomes (dispositions, chargebacks, confirmed fraud)
  → labeled data feeds rule tuning and model training
  → rule/model changes tested (sandbox, backtesting, champion-challenger in enterprise products)
  → changes approved and rolled out; every change audited
  → dashboards track whether loss, block rate, and review load actually improved
```

This loop is why the platform is a *platform* rather than a one-shot scorer: fraud adapts, and the system is expected to adapt with it, under control.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Dashboard

- Purpose: ongoing situational awareness of the fraud program.
- Typical information: fraud loss and chargeback trends, block/decline rates, manual review volume, queue depth, analyst throughput, alert volumes.
- Primary actions: drill into segments, open queues, configure alerts.

### Activity list and record detail

- Purpose: the system of record view — every evaluated activity with its outcome.
- Typical information: score, outcome/state, amount, date, entity, signals, rule hits, labels/tags, review status.
- Primary actions: search and filter, change state, tag, assign for review, export, bulk operations.

### Review queue / case workspace

- Purpose: human investigation of suspect records and alerts.
- Typical information: prioritized worklist; per-case timeline, signals, entity history, linked records, notes, documents.
- Primary actions: claim/assign, investigate, record disposition, escalate, annotate, close.

### Entity profile

- Purpose: the risk history of a customer/user/device — the context a single record lacks.
- Typical information: past activity and outcomes, linked devices/accounts/instruments, network/link views, list memberships.
- Primary actions: inspect history, explore links, add to list, open related records.

### Rule / scoring configuration

- Purpose: author and manage the evaluation logic.
- Typical information: rule conditions, score effects, state effects, rule categories, performance stats per rule.
- Primary actions: create/edit/enable/disable rules, run test or batch evaluations, propose changes for approval, revert.

### Lists manager

- Purpose: curate known-bad / known-good / watch values.
- Typical information: list entries, sources (manual, chargeback-derived, rule-derived), hit counts.
- Primary actions: add/remove entries, import/export, set list behavior (force outcome vs feed rules).

### Model management (enterprise/banking deployments)

- Purpose: govern the model layer.
- Typical information: model versions, performance metrics, champion/challenger comparisons.
- Primary actions: deploy, compare, roll back, schedule retraining.

### Analytics / reporting

- Purpose: measure the program and the machinery.
- Typical information: loss and chargeback trends, false-positive indicators, rule/model accuracy, analyst performance, cohort breakdowns.
- Primary actions: build reports, export, schedule delivery.

### Administration

- Purpose: access control and platform governance.
- Typical information: users/roles, SSO configuration, audit logs, sandbox environments, API keys.
- Primary actions: manage roles/permissions, review audit trail, configure integrations.

### API and webhooks

- Purpose: the machine-facing surface.
- Typical shape: decision/score endpoints called at decision points; event-submission endpoints; webhook notifications for asynchronous outcomes; sandbox endpoints for integration testing.

## Important Rules / Behaviors

### Decisions are requested, not scheduled

The platform's most important behavior is answering a host system's synchronous question at a decision point. This makes latency a product property: evaluation must complete within the host flow's tolerance, which constrains how much enrichment and how many models can run inline. (Post-transaction and batch monitoring variants relax this, at the cost of deciding after the fact.)

### Lists override scores

Where products maintain explicit block/allow lists, listed values force outcomes regardless of what the score says: block-listed values are declined and allow-listed values approved even when the evaluation machinery disagrees. This precedence is a structural safety valve: it lets operators guarantee outcomes for known cases without touching the model. Products without dedicated list management express the same effect through rules that set outcomes directly.

### Thresholds are policy

The mapping from score to outcome is a tunable business decision, not a fixed property. Raising a review threshold trades fraud loss for review load; lowering it does the opposite. Much of day-to-day fraud operations is managing this trade-off, and the platform's analytics exist largely to make it visible.

### Dispositions are training data

What analysts conclude in review is not just case closure — it is the labeled ground truth that rules and models learn from. Products treat labeling as a first-class activity, and review quality directly shapes detection quality.

### Ground truth arrives late and asymmetrically

Chargebacks and confirmed fraud surface only after the activity they judge — often well after fulfillment — and only for a subset of mistakes (a wrongly blocked good customer often never reports itself). The feedback loop therefore runs on delayed, partial labels — a defining operational constraint that shapes how tuning and measurement work.

### Changes are governed

Because a bad rule change can block thousands of good customers in minutes, mature products surround changes with controls: sandbox/test evaluation, staged rollout, approval requirements for consequential changes, and complete audit trails. In banking deployments, model changes additionally fall under formal model-governance obligations.

### Every decision is attributable

The platform records which rules fired, which model version scored, which analyst dispositioned, and when. This is not an optional nicety: decisions that cost customers money are contested, regulated, and audited, and the record is the platform's defense.

## Variants

Common variants of the Type:

- **By position in the flow** — merchant-side pre-transaction screening (checkout/order), issuer-side authorization scoring, post-transaction monitoring, and onboarding/application fraud screening. These change what data is available and how fast an answer is needed, not the core model.
- **By business model** — tooling (the platform returns scores/decisions; the customer owns the outcome), guarantee-based (the vendor financially backs its approvals against chargebacks), and score-feed (the platform's intelligence is consumed inside the customer's own risk engine).
- **By segment** — digital commerce and marketplaces (order fraud, promo abuse, account takeover), banking and payments (payment scams, money mules, check fraud, application and synthetic-identity fraud, with deep model governance), iGaming (multi-accounting, bonus abuse), insurance (claims fraud with adjuster-style review).
- **Fraud + AML convergence** — platforms that bundle anti-money-laundering screening, monitoring, and regulatory reporting on a shared case-management layer with fraud. The fraud core is intact; the compliance layer is an adjacency.
- **By data posture** — platforms that pool signals across many customers (network intelligence) versus deployments that evaluate only the customer's own data.
- **By deployment** — multi-tenant SaaS consumed via API; cloud-native enterprise platforms deployed in the customer's cloud; legacy on-premises installations in regulated institutions.
- **By automation depth** — decision-support (score + queue for humans) through straight-through automation where the large majority of records never reach a human.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| AML Platform | sibling in the finance domain, heavy vendor overlap | same machinery shape (records → rules → alerts → cases), but the objective is regulatory compliance: suspicious-activity detection, sanctions/PEP screening, regulatory filings. Fraud's objective is financial loss, with decisions and chargeback feedback as outputs |
| Transaction Monitoring Platform | sibling in the finance domain | monitoring-focused machinery over posted activity; fraud detection platforms add decisioning at the point of activity and loss-oriented feedback. In practice the terms overlap heavily and vendors ship both |
| Fraud Prevention Platform | probable overlap | a same-named family also exists in the cybersecurity domain of the directory; the sampled products straddle both (account takeover, fake accounts). This document covers the finance-domain leaf — transaction/activity fraud operations; the cybersecurity sibling's exact scope needs joint review |
| Account Abuse Protection | narrower | fake accounts, automation abuse, account takeover as abuse control; fraud detection platforms are broader money-loss systems that may include these as fraud types |
| Payment Orchestration Platform | consumer of decisions | orchestration routes charges across providers and may call fraud services as connected decision points; the fraud platform owns the model and decision, the orchestrator consumes them as routing conditions |
| Identity Verification / KYC Platform | adjacent, often bundled | verifies identity claims at onboarding (document/data checks, pass-fail); fraud platforms evaluate activity and behavior for risk across the lifecycle. Verification results commonly serve as signals into fraud scoring |
| Sanctions Screening Platform | sibling in the finance domain | list matching with match/no-match semantics against designated lists; fraud detection is probabilistic risk assessment over behavior |
| Credit Decisioning Platform | same shape, different risk | both turn applications/records into scored decisions, but credit decisioning assesses ability and willingness to repay, with repayment performance as feedback; fraud detection assesses illegitimacy, with confirmed fraud and chargebacks as feedback |
| SIEM | same operational shape, different domain | events → detection rules → alerts → cases describes both, but SIEM works on security telemetry for SOC teams; fraud platforms work on customer commercial activity for fraud operations |
| Business Rules / Decision Management Platform | generic substrate | generic decision automation lacks the fraud data model, entity graphs, velocity machinery, and chargeback feedback loop; it can power part of a fraud platform but is not one |

The most important boundary is with the AML/transaction-monitoring siblings: the machinery is nearly identical, and vendors increasingly ship both, so the honest distinction is one of objective and outputs — regulatory compliance artifacts versus loss-preventing decisions — rather than of structure.

## Representative Products

- **SEON** — API-first platform with transparent rule-based scoring plus machine learning; strong public documentation of the scoring engine, lists, review, and case management.
- **Sift** — network-intelligence platform combining shared cross-customer signals with a decisioning engine, workflow automation, and analyst tooling for digital businesses.
- **SAS Fraud Decisioning** — bank-grade enterprise platform pairing real-time transaction scoring with model management, champion-challenger testing, and alert/case management for financial institutions.
- **Signifyd** — guarantee-based commerce protection: automated order decisions backed by the vendor's financial liability for chargebacks, with dispute-recovery modules.

These four were chosen to span different product philosophies (transparent tooling, network intelligence, enterprise model governance, outcome guarantee) and different customer tiers (SMB/mid-market digital business through large financial institutions and enterprise ecommerce).

## Sources

Research date: **2026-09-07**

- SEON — official documentation: Product overview, Scoring Engine overview, Case management overview, Transactions (user manual) — https://docs.seon.io/
- Sift — official site and platform page — https://sift.com/ , https://sift.com/platform/
- SAS — SAS Fraud Decisioning product page — https://www.sas.com/en_us/software/fraud-management.html
- Signifyd — official site — https://www.signifyd.com/ ; public API fundamentals — https://docs.signifyd.com/
- Sardine — documentation hub (context anchor for fraud/compliance convergence) — https://docs.sardine.ai/

> Sourcing limitations: developer-level documentation for Sift (developers.sift.com) was unreachable (HTTP 403), and deep documentation for Signifyd, Sardine, Ravelin, Unit21, and Feedzai is login-gated; SAS product documentation was not fetched. Claims for those products therefore rest on official product/platform pages (weaker evidence tier), and no precise operational details (latency figures, score ranges, state names, numeric limits) from any single vendor were promoted into this document. Exact vendor-specific values observed during research are recorded in the paired Research Notes.
