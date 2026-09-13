# Research Notes — Fraud Detection Platform

Research date: 2026-09-07
Slug: fraud-detection-platform
Directory location: §08 Finance, Banking, Insurance & Investment (between Transaction Monitoring Platform and Sanctions Screening Platform)

---

## Research Goal

Understand what a Fraud Detection Platform actually is as an Application Type: what objects exist inside it, how activity is evaluated for fraud risk, how decisions are produced and acted on, how human review works, how the system improves over time, and where its boundaries sit against adjacent Types (AML Platform, Transaction Monitoring Platform, Fraud Prevention Platform §15, Account Abuse Protection, Payment Orchestration Platform, Identity Verification/KYC, Sanctions Screening, Credit Decisioning, SIEM).

## Initial Boundary (pre-research hypothesis)

- Core use: evaluate customer-initiated activity (transactions, orders, logins, signups) for fraud risk and drive decisions (approve / decline / review / challenge).
- Users: fraud analysts, fraud operations managers, risk/data science teams, integrating developers.
- Nearest neighbors: AML Platform and Transaction Monitoring Platform (same machinery shape, different objective); Fraud Prevention Platform (§15 sibling leaf — potential overlap problem); Payment Orchestration (fraud decisions consumed as routing conditions — already recorded in that leaf's research).
- Unknowns: whether "detection" vs "prevention" is a real structural split or just marketing; whether the guarantee business model (Signifyd-class) changes the core model; how bank-grade (SAS-class) platforms differ structurally from API-first (SEON/Sift-class) ones.

## Research Questions

1. What is the unit of evaluation (transaction? order? event? claim?) and what does a record look like?
2. What evaluation machinery exists (rules, models, scores, lists) and how do they combine into a decision?
3. What decision outcomes exist and how are they returned to the calling system?
4. How does human review work (queues, cases, dispositions, assignment, governance)?
5. What signals/enrichment feed the evaluation (device, digital footprint, behavioral, third-party, network)?
6. How does the feedback loop work (chargebacks, labels, confirmed fraud → model/rule tuning)?
7. What cross-record pattern detection exists (velocity, aggregates, link/network analysis)?
8. What governance surrounds changes (sandbox, approvals, audit, model management)?
9. Who uses the product and through which interfaces?
10. Where does this Type end and AML / abuse prevention / identity verification / credit decisioning begin?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / segment | Evidence tier reached |
|---|---|---|
| SEON | API-first, transparent scoring; SMB/mid-market digital businesses (ecommerce, iGaming, fintech, lending) | Tier-1 (public docs: product overview, scoring engine, case management, transactions user manual) |
| Sift | Network-intelligence + workflow automation; mid/large digital businesses | Tier-2 (main site + platform page; developer docs 403) |
| SAS Fraud Decisioning (formerly SAS Fraud Management) | Bank-grade enterprise FI; model + rules + case management on cloud-native platform | Tier-2 (product page; documentation.sas.com not fetched) |
| Signifyd | Outcome-based commerce protection with chargeback guarantee; enterprise ecommerce | Tier-2 (main site) + Tier-1 API fundamentals page (shallow; deep docs login-gated) |
| Sardine | Fintech fraud + compliance convergence | Context anchor only (docs hub public, full docs login-gated) |

Rejected/unreachable: Feedzai (docs Atlassian-gated), Unit21 (docs sign-in gated), Ravelin (docs login gated), FraudLabs Pro (404 on both attempted URLs), NICE Actimize (not attempted after repeated gating pattern).

## Sources

- SEON Docs (docs.seon.io): /getting-started/product-overview, /knowledge-base/transactions-scoring/scoring-engine-overview, /knowledge-base/case-management/case-management-overview, /knowledge-base/user-manuals/transactions — fetched 2026-09-07.
- Sift (sift.com): homepage, /platform/ — fetched 2026-09-07. developers.sift.com → 403 (×1, abandoned).
- SAS (sas.com): /en_us/software/fraud-management.html ("SAS Fraud Decisioning") — fetched 2026-09-07.
- Signifyd (signifyd.com): homepage — fetched 2026-09-07. docs.signifyd.com root + /docs/order-api (both return the same public "Fundamentals" page; deeper docs require login).
- Sardine (docs.sardine.ai): hub page only — fetched 2026-09-07.
- Prior leaf context: research/payment-orchestration-platform.md §Boundary Findings (fraud vendors as connected services inside orchestration flows).

## Product Observations

### SEON (Evidence layer A — official operational docs)

Key observations:

- **Fraud API as the core integration**: "a versatile and modular API that consolidates digital footprinting, decisioning, and risk scoring capabilities into a single, streamlined response" — businesses submit data inputs and receive enriched insights, rule evaluations, and risk scores in real time.
- **Unit of evaluation = "transaction"**: the Transactions page lists "all customer interactions with your platform that SEON has checked", submitted over API calls or through manual entries (Manual Lookup page allows use without API integration). Records carry: score, transaction amount and date, state, status, labels and tags.
- **Signal enrichment**: Digital Footprint (Email API, Phone API, IP API — linked profiles, data breaches, reputation of contact details); Device Intelligence (device attributes, behavioral biometrics, bot/device-farm/automation detection, multi-accounting, VPN/proxy detection); Identity Verification (document verification, eKYC, selfie/liveness, NFC, payment card verification) as an adjacent module.
- **Scoring Engine**: enriches incoming transaction data → analyzes data points → calculates a fraud score → categorizes the transaction into one of three states: **APPROVE / REVIEW / DECLINE**. Rules add points to the score (example rules shown with specific point values, e.g. "+7" for no online profiles found, "+4" for undeliverable email — precise values observed but treated as vendor examples). A rule can also directly set a state (example: DECLINE when cookies disabled).
- **Rule management**: Default rules (pre-configured by vendor specialists; toggle on/off, cannot be modified or deleted), Custom rules (modify scores, adjust states, add data points to lists), AI rule suggestions (auto-generated from historical data, with accuracy metrics, enabled manually or by accuracy thresholds).
- **Separate ML score**: "AI insights score" — a separate fraud probability score (0–100 range stated) independent of the standard fraud score, usable inside rules.
- **Lists**: Blacklist (auto-DECLINE, sets score to max), Whitelist (auto-APPROVE, sets score to min), Custom lists (monitor without immediate score impact; list membership usable in rules). List management described as "a crucial component… helping control decisioning outcomes".
- **Rule categories**: group rules by fraud pattern/use case; category-level scores and states; "structured, layered decisioning".
- **Velocity/aggregates**: regular aggregates, velocity rules with performance checks, similarity features, clone search, network analysis, email clusters.
- **Console surfaces** (Interface section of docs): Dashboard, Transactions, Transaction details, Customers, Alerts, Cases, Manual Lookup, AML, Scoring Engine, Lists, Monitoring (workbench), Channels (merchants/affiliates), Settings, API license keys, Logs, Four-eye principle, Sandbox Environment.
- **Review workflow**: transactions in REVIEW state; state can be changed from the list view (Approve/Review/Decline + labels); "Manual reviews and labels provide essential feedback to our machine learning solutions"; assigning transactions for review; tagging (up to 100 tags per transaction — precise limit observed); multi-select bulk state changes; exports (400,000-row limit stated).
- **Case management**: alert engine (real-time, configurable triggers; fraud example: device/IP mismatch vs usual activity; AML example: structured transactions below $10,000 in high-risk jurisdictions); collaborative cases (notes, documents, progress tracking, full audit trail); regulatory reporting (SAR narratives AI-supported, pre-filled fields, validation, direct filing to FinCEN with more FIUs planned).
- **Feedback loop**: "Feedback Loops & Label API" — labeling best practices, labels vs tags; ML models "trained using labels provided by the Label API"; chargeback management (automated chargeback management; Shopify chargeback settings).
- **Governance**: Four-eye principle page; "proposed system-level changes and approvals" (streamlining teamwork); Sandbox Environment; SSO guides (Azure AD, Ping, Okta, Google); roles & permissions configuration; Logs.
- **Post-decision automations**: "How to run post-decision automations" — actions triggered after a decision.
- **Deployment shapes**: direct API integration; Shopify app (dedicated doc section with scoring threshold, automation rules, order hold/cancel automations); workflows module (building/managing/reviewing workflow runs, shareable verification links).

### Sift (Evidence layer A-limited — official marketing/platform pages; developer docs unreachable)

Key observations (all from sift.com homepage and /platform/):

- **Positioning**: "fraud prevention platform… automated fraud decisioning and transparent control over every decision"; "Clearbox Control" (transparency into signals, models, workflows behind every decision).
- **Journey coverage**: signup/account creation → login/account access → account activity/behavior monitoring → transaction/payment processing → post-transaction/chargeback prevention.
- **How-it-works loop** (vendor's own four stages): Ingest & Enrich Data → Evaluate Risk → Decide & Act → Optimize & Learn.
- **Decisioning Engine**: "Build rules and adapt risk strategy in real time"; decision workflow mockup shows a login event with a risk score (42) and Allow/Step-up/Block distribution; "Real-time control over thresholds, workflows, and friction".
- **Automation & Workflows**: "Automate review, routing, and repetitive fraud ops work"; console dashboard mockup shows: workflows with runs/block rate/accuracy (Create Order, Transaction, Queues, Chargeback, ATO), manual decisions (Accept/Block/Watch), top agents (analyst reviews, block rate, accuracy, bulk share), queues, chargebacks received, orders blocked.
- **Network Intelligence**: global data network "1T+ annual events"; "New-to-you users are often not new to Sift"; identity-level context; 700K+ sites & apps sharing signal (vendor claims).
- **Products**: Payment Protection (real-time fraud decisions on transactions), Account Defense (ATO, fake accounts, identity fraud), Sift Score API ("bring Sift intelligence into your own risk models" — external risk signal for teams with internal models), Expert Services (managed workflow auditing, model tuning, labeling).
- **Fraud types**: payment fraud (stolen card, card testing, BOPIS), account takeover, fake accounts (bot signups, synthetic accounts, trial abuse, multi-accounting/promo abuse), marketplace abuse (fake listings, cash-out), iGaming (deposit fraud, gnoming, bonus abuse), travel/ticketing, food & delivery, fintech (onboarding, money movement).
- **Step-up friction**: "Built-in multi-factor authentication tools and step-up friction"; "Apply friction only where risk justifies it"; "dynamic friction".
- **Analyst efficiency**: "Reduce manual review by automating low-risk decisions and giving analysts the context… to investigate high-priority cases faster"; auto-resolution counts; "72% less manual review" (vendor claim).
- **Real-time posture**: "Real-time scoring in less than 150 milliseconds" (vendor claim — precise number, marketing source); "Continuous risk scoring across account and transaction events".
- **Integration**: "designed to work with existing systems through APIs and configurable decisioning tools"; consume via Sift Console, partner integrations, or Score API into custom risk engines.

### SAS Fraud Decisioning (Evidence layer A-limited — official product page; product documentation not fetched)

Key observations:

- **Positioning**: "cloud-native fraud detection and prevention solution on SAS Viya… real-time decisioning, AI, machine learning, predictive analytics and automated investigation workflows to detect, prevent and manage fraud across the customer life cycle." Audience: "banks, credit unions, payment providers and other financial institutions."
- **Fraud types**: payment fraud, payment scams/social engineering, account takeover, application fraud, synthetic identity, check fraud (with check image analysis), money mules & funnel accounts, bust-out fraud, e-commerce fraud, digital fraud.
- **Real-time posture**: "Profile, score and evaluate 100% of transactions in real time using high-throughput, low-latency processing"; "profiling, scoring and decisioning transactions in real time with millisecond response times" (vendor claim); monitors "payments, nonmonetary transactions and events".
- **Data orchestration**: "Orchestrate internal and external data sources… Integrate transaction, customer, account and third-party data regardless of source or format"; "Configure how incoming events are transformed, validated and enhanced before entering fraud detection workflows."
- **Evaluation machinery**: business rules + machine learning + adaptive analytics + anomaly detection; "automatically recommend new rules and scenarios"; champion-challenger testing, A/B testing, impact analysis; "Compare models, rules and data providers"; prebuilt fraud models as add-ons.
- **Customer profiling**: "profiling customer behavior across transaction types and channels"; "enterprise-wide view of fraud activity, customer behavior and transaction events across channels"; "uncover hidden relationships".
- **Review workflow**: "Integrated alert triage and investigation workflows support both analyst-led reviews and automated decisioning"; alert triage and case management named as key features; executive dashboard; dashboards and reporting.
- **Model governance**: "model management and governance" named as a key feature.
- **Deployment**: cloud-native on Viya; SAS-managed or self-managed; Azure/AWS/GCP/OpenShift.

### Signifyd (Evidence layer A-limited — official marketing site; public API docs shallow)

Key observations:

- **Business-model pole**: outcome-based — "Guaranteed Fraud Protection… backed by a 100% financial guarantee"; "Complete Chargeback Protection — total freedom from chargebacks"; "$0 in fraud losses" positioning; "100% order automation" (vendor claims). The vendor takes financial liability for its decisions on approved orders — a fundamentally different commercial shape from tooling-only vendors.
- **Commerce Protection Platform** module set: Account Protection, Authorization Rate Optimization (issuer integrations), Guaranteed Fraud Protection, Complete Chargeback Protection, Chargeback Recovery (representment support), Return Insights, Instant Refunds.
- **Journey coverage**: Fulfillment, Return, Dispute, Promotion, Application, Account, Login, Checkout, Refund — protection "across the entire shopper journey".
- **Transparency stance**: "Machine learning shouldn't leave you in the dark. We provide the data needed to understand decisions"; "Complete control… ultimate control over protection".
- **Integration**: public REST API (Fundamentals page: JSON, versioning policy, webhooks mentioned as API resources; "Adding a new webhook event" listed in backward-compatible changes — webhooks are part of the integration surface). Deep/Enterprise API docs and console documentation are login-gated.
- **Customer posture**: "instant recognition of legitimate customers allows… approve more good orders and automate fulfillment" — the review burden is deliberately shifted into automation + guarantee rather than analyst queues (no public evidence of case-management tooling depth).

### Sardine (context anchor only — docs hub public, full docs login-gated)

- Positions as "fraud prevention, compliance, and risk management platform"; "manage risk across the customer journey". Confirms the fraud+compliance convergence trend in fintech. No structural claims made (docs gated).

---

## Cross-product Comparison

| Dimension | SEON | Sift | SAS Fraud Decisioning | Signifyd |
|---|---|---|---|---|
| Unit of evaluation | "transaction" (any checked customer interaction; manual entries possible) | events across journey (signup, login, transaction, post-transaction) | transactions + nonmonetary transactions + events | orders (commerce transactions) |
| Integration shape | Fraud API at decision points; manual lookup; Shopify app | API + console + partner integrations + Score API | data orchestration from internal systems; real-time decisioning in channels | Order-style REST API + webhooks; platform integrations |
| Signal enrichment | digital footprint (email/phone/IP), device intelligence, behavioral biometrics | global network signals, identity-level context, linked accounts | internal + external + third-party data orchestration, check image analysis | not publicly detailed |
| Evaluation machinery | rules (default/custom/AI-suggested) + lists + separate ML score | rules + thresholds + workflows + models | business rules + ML + anomaly detection + prebuilt models | ML (opaque by default, transparency data provided) |
| Score | fraud score + separate AI insights score | risk score per event | scoring of 100% of transactions | decision + guarantee outcome |
| Decision states | APPROVE / REVIEW / DECLINE | Allow / Step-up / Block (+ Watch in manual decisions) | decisioning + alert triage (analyst-led or automated) | approve (guaranteed) vs decline |
| Human review | REVIEW queue, assignment, cases, four-eye principle | queues, manual review, case investigation, analyst dashboards | alert triage + case management, investigation workflows | minimized by design (automation + guarantee) |
| Lists | blacklist / whitelist / custom lists (explicit) | not directly observed on fetched pages | rules can encode hard outcomes | not publicly detailed |
| Cross-record detection | velocity rules, aggregates, network analysis, clone search, similarity | linked-account intelligence, network intelligence | hidden relationships, mule/funnel detection, customer profiling across channels | not publicly detailed |
| Feedback loop | Label API, manual reviews + labels feed ML, chargeback management | chargeback data, workflow analysis, model tuning (services) | champion-challenger, A/B, impact analysis, continuous improvement | chargeback recovery; guarantee payouts as outcome data |
| Governance | sandbox, proposed changes + approvals, four-eye, logs, roles | workflow auditing (services), Clearbox transparency | model management and governance | not publicly detailed |
| Business model | tooling (score returned, customer decides) | tooling | tooling (enterprise licensing) | guarantee (vendor carries liability) |
| Segment | SMB/mid digital businesses | mid/large digital businesses | large financial institutions | enterprise ecommerce |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being a Fraud Detection Platform:

1. **Activity records under evaluation** — the platform receives/ingests records describing user-initiated activity (transactions, orders, logins, signups, claims) and is the system of record for fraud risk on those records.
2. **Evaluation machinery producing a risk assessment** — configurable fraud logic (rules and/or models) evaluates each record and produces a risk assessment (score and/or decision).
3. **Decision outcome with a human review path** — the assessment resolves into an outcome on the record (allow / decline / review-class), and suspect records can be routed to human reviewers who record a disposition.

Remove #1 → it is not evaluating anything (just a rules engine). Remove #2 → it is a data warehouse. Remove #3 → it is an analytics/scoring API with no operational loop; without any review path the "detection platform" degenerates into a pure scoring service.

Historical check: a 1990s card-issuer batch scoring system (records → rules/models → alert queue → analyst disposition) satisfies all three. An insurance claims-fraud system (claims → rules → adjuster queue) satisfies all three. A pure shared blacklist/consortium lookup service does NOT (no evaluation machinery, no decision) — it belongs to screening/identity verification. A device-fingerprint SDK does NOT (signal provider only).

### L1 — Common Mature Structure

Present across the researched sample (evidence layer B unless noted):

- **Signal enrichment layer** — device intelligence, digital footprint (email/phone/IP reputation), behavioral signals, third-party data (SEON explicit; Sift network signals; SAS data orchestration).
- **Entity profiles** — customer/user/device-level aggregation of history and risk (SEON Customers page; Sift identity-centric profiles; SAS customer behavior profiling).
- **Cross-record pattern detection** — velocity rules and aggregates, link/network analysis, similarity/clone detection (SEON explicit; Sift linked accounts; SAS hidden relationships/mule detection).
- **Lists** — block/allow/watch lists that override or anchor scoring (SEON explicit; other products encode hard outcomes in rules; treat "dedicated list management" as common rather than universal).
- **Case management** — queues, assignment, notes/documents, audit trail, dispositions (SEON, SAS explicit; Sift console investigation; Signifyd deliberately minimizes it).
- **Feedback loop** — analyst labels/dispositions and chargeback/confirmed-fraud outcomes feed rule and model improvement (SEON Label API explicit; Sift optimize-and-learn; SAS champion-challenger; Signifyd chargeback recovery).
- **Performance analytics** — dashboards over fraud loss, block/decline rates, manual review volume, analyst throughput, rule/model accuracy (all four).
- **Change governance** — sandbox/testing, staged or approved changes, audit logs, roles/permissions (SEON explicit four-eye + sandbox + logs; SAS model governance; Sift workflow auditing via services).
- **Step-up / challenge as a decision output** — friction (step-up authentication, challenges) as an intermediate outcome between allow and block (Sift explicit; SEON via rules/workflows; common in the market).
- **Chargeback/dispute handling** — chargeback data ingestion and dispute workflows as a module (SEON chargeback management; Signifyd Complete Chargeback Protection/Recovery; Sift chargeback workflows).
- **API + webhooks integration surface** — decisions returned synchronously at decision points; events/webhooks for async outcomes (SEON, Signifyd explicit; Sift API posture).

### L2 — Variant / Optional Structure

- **Position in the flow**: pre-transaction merchant screening (checkout/order) vs issuer-side authorization scoring vs post-transaction batch monitoring vs onboarding/application fraud. Changes data available and latency posture, not the core model.
- **Business model**: tooling (customer owns final decision) vs guarantee (vendor carries chargeback liability — Signifyd pole) vs score-only data feed (Sift Score API pole).
- **Segment tuning**: digital commerce/marketplace (order fraud, promo abuse, ATO) vs bank/issuer (payment scams, mules, check fraud, application fraud, model governance depth) vs iGaming (multi-accounting, bonus abuse) vs insurance claims fraud (claims as records).
- **Fraud + AML convergence**: unified platforms spanning fraud and AML screening/case management/regulatory reporting (SEON case management covers both; SAS financial-crime family; Sardine positioning). AML capability is optional adjacency, not definitional.
- **Shared network intelligence**: cross-customer signal pooling (Sift explicit; consortium data in card networks — not directly sampled) vs customer-data-only deployments.
- **Deployment**: multi-tenant SaaS API vs cloud-native enterprise platform (SAS Viya) vs (historically) on-prem.
- **Bundled identity verification**: document/eKYC/liveness modules adjacent to fraud scoring (SEON bundles; others integrate third-party IDV as signals).
- **Automation depth**: from decision-support (score + queue) to full straight-through automation with post-decision automations (SEON post-decision automations; Signifyd 100% order automation claim).

### L3 — Vendor-specific (research notes only)

- SEON: APPROVE/REVIEW/DECLINE exact state names; AI Insights score 0–100; default-vs-custom rule toggle model; four-eye principle as named feature; FinCEN direct SAR filing; Shopify app specifics; example rule point values (+7/+4); blacklist/whitelist score clamping to 100/0; 400,000-row export limit; 100-tag limit; $10,000 AML structuring example.
- Sift: "Clearbox" branding; Payment Protection / Account Defense product split; Sift Score API; FIBR benchmarking; 150ms scoring claim; 1T+ annual events / 700K+ sites network claims; 99.4% acceptance / 72% less manual review claims.
- SAS: Viya platform; champion-challenger terminology; prebuilt fraud models as packaged add-ons; millisecond response claim; check image analysis.
- Signifyd: 100% financial guarantee; Complete Chargeback Protection / Chargeback Recovery / Instant Refunds / Return Insights / Authorization Rate Optimization module names; Fearless Conversions branding; Spark release naming.

## Rejected Findings

- **"Detection vs prevention" as a structural split**: rejected. The sampled products mix detection (scoring/monitoring) and prevention (blocking/step-up) in the same decision loop; the words are marketing posture, not different architectures. The directory's §08 "Fraud Detection Platform" and §15 "Fraud Prevention Platform" leaves likely overlap for the same reason (see Boundary Findings).
- **"Real-time" as definitional**: rejected as an L0 property. Real-time scoring is dominant today (all four sampled products claim it) but older/regional batch systems (end-of-day scoring + next-morning queues) still satisfy the Type. Real-time posture is a variant dimension.
- **"AI/ML" as definitional**: rejected. Rules-only evaluation machinery still constitutes a fraud detection platform (historical check). ML is the current dominant implementation, not the invariant.
- **Guarantee model as definitional**: rejected — it is a business-model variant (L2), even though it changes the commercial relationship fundamentally.
- **Chargeback management as definitional**: rejected — common module (L1), absent in non-payment fraud variants (e.g., application fraud, internal fraud).

## Boundary Findings

- **vs AML Platform / Transaction Monitoring Platform (§08 siblings)**: same machinery shape (activity records → rules/scenarios → alerts → cases → dispositions). Difference is objective and outputs: AML targets regulatory compliance (suspicious-activity detection, sanctions/PEP screening, SAR/regulatory reporting, KYC context); fraud targets financial loss (decisions on customer activity, chargeback feedback, loss analytics). Convergence is real (SEON unified case management; SAS financial-crime family) — vendors ship both. Test: if the primary outputs are regulatory filings and list-screening matches, it's AML; if the primary outputs are loss-preventing decisions with chargeback/label feedback, it's fraud detection. Both leaves stand; flag for joint review given heavy vendor overlap.
- **vs Fraud Prevention Platform (§15) and Account Abuse Protection (§15)**: probable overlap problem. §15's framing is cybersecurity/identity/abuse (device fingerprinting, bot mitigation, account abuse); §08's framing is transaction/payment fraud operations. The sampled products (Sift especially) straddle both (ATO, fake accounts, promo abuse). Taxonomy question recorded for STATUS.md Boundary Issues — recommend joint review of the two leaves; do not silently merge.
- **vs Payment Orchestration Platform (§08)**: consistent with that leaf's recorded boundary — the fraud platform owns the model and decision; orchestration consumes fraud decisions as routing conditions among connected services. A fraud module bundled inside a PSP/orchestrator is a gradient case.
- **vs Identity Verification / KYC Platform (§15)**: IDV verifies identity claims at onboarding (document/data checks, pass/fail); fraud platform evaluates activity and behavior for fraud risk across the lifecycle. IDV outputs commonly serve as signals into fraud scoring (SEON bundles both; SAS integrates third-party verification into decisions). Test: pass/fail on identity claims vs risk assessment on activity.
- **vs Sanctions Screening Platform (§08 sibling)**: sanctions screening is list matching with match/no-match semantics against designated lists; fraud detection is probabilistic risk assessment over behavior. Different record semantics, different outputs.
- **vs Credit Decisioning Platform (§08)**: same decisioning shape (application → score → decision → outcome feedback) but different risk object: underwriting risk (ability/willingness to repay) vs fraud risk (illegitimacy of the actor/activity); different feedback data (repayment performance vs confirmed fraud/chargebacks). Vendors and even modules can overlap in application-fraud use cases.
- **vs SIEM (§15)**: same alert-triage operational shape (events → detection rules → alerts → cases) but different domain and record semantics (security telemetry vs customer commercial activity), different users (SOC vs fraud ops).
- **vs Business Rules Management System / Decision Management Platform (§10)**: generic decision automation vs domain-specific platform with fraud data models, entity graphs, velocity machinery, and chargeback feedback. A BRMS could power part of a fraud platform; it is not one.
- **Signal providers / device-fingerprint SDKs**: products that only supply signals (no scoring, no decision, no review) are data providers, not fraud detection platforms. Test recorded above.

## Uncertainties

- Sift's developer/API documentation was unreachable (403); Sift observations rest on marketing/platform pages (Tier-2). Console internals (list management, rule editor specifics) unverified for Sift.
- Signifyd's deep API/console documentation is login-gated; its case-management/review tooling depth is unverified (its positioning suggests deliberate minimization, but this is inference from marketing posture, not observed tooling).
- SAS product documentation (documentation.sas.com) was not fetched; SAS observations rest on the product page. Alert/case internals and model-management specifics unverified.
- Whether "Fraud Detection Platform" (§08) and "Fraud Prevention Platform" (§15) should remain separate leaves is a taxonomy question requiring joint review; this research documents the §08 leaf's side.
- Precise latency figures, score ranges, and state names are vendor-specific; none were promoted to the canonical document.
- Enterprise FI vendors (NICE Actimize, Feedzai, FICO Falcon, Mastercard-class network scoring) were not directly sampled (gated/unreachable); bank-grade generalizations rest on SAS alone and are marked accordingly.

## Final Synthesis

A Fraud Detection Platform is the operational system an organization uses to decide, record, and improve fraud risk outcomes on customer activity. Its defining core is small: activity records flow in (via API at decision points, batch feeds, or manual entry); configurable fraud logic — rules and/or models — evaluates each record and produces a risk assessment; the assessment resolves into an outcome (allow / decline / review-class, sometimes a challenge), with suspect records routed to human review where analysts record dispositions. Around that core, mature products add signal enrichment, entity profiles, cross-record pattern detection (velocity, link/network), lists, case management, a feedback loop (labels + chargebacks → tuning), performance analytics, and change governance. The Type's center of gravity is the decision loop, not the algorithm: whether rules, ML, or a vendor's opaque model produces the score, the platform's job is to turn activity into defensible fraud decisions and to get better at it over time. Business model (tooling vs guarantee), position in the flow (pre-transaction vs issuer vs post-transaction), and segment (digital commerce vs bank vs insurance) are variant dimensions, not definitional ones.
