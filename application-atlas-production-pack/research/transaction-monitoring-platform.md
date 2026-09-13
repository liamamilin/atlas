# Research Notes — Transaction Monitoring Platform

Research date: 2026-09-08
Slug: transaction-monitoring-platform
Directory location: §08 Finance, Banking, Insurance & Investment (between Liquidity Risk Platform and AML Platform)

---

## Research Goal

Understand what a Transaction Monitoring Platform actually is as an Application Type: what objects exist inside it, how the institution's transaction flows are watched for suspicious behavior, how alerts are produced and worked, where the Type's loop ends, and where its boundaries sit against the three sibling Types that share its machinery shape — AML Platform, Fraud Detection Platform, Sanctions Screening Platform — plus KYC, Regulatory Reporting, SIEM, and generic stream/rules machinery.

## Joint-review obligations carried into this pass

This leaf is the named counterparty of three recorded flags in STATUS.md Boundary Issues; all three are discharged in §Boundary Findings below:

1. **fraud-detection-platform (processed 2026-09-07)**: "machinery shape is nearly identical (records → rules/scenarios → alerts → cases → dispositions)… honest distinction is objective/outputs (regulatory artifacts vs loss-preventing decisions with chargeback feedback)".
2. **aml-platform (processed 2026-09-06)**: "TM leaf = detection/alerting engine whose terminal output is alerts handed elsewhere; AML Platform = system of record owning customer-risk context + case investigation + regulatory reporting; recommend both leaves state this distinction when Transaction Monitoring Platform is processed".
3. **sanctions-screening-platform (processed 2026-09-07)**: three-way ratification recommended — sanctions-screening vs aml-platform vs transaction-monitoring-platform share one converged machinery shape and vendors bundle them in single fincrime suites; the honest discriminator is "the question asked and artifact produced".

## Initial Boundary (pre-research hypothesis)

- Core use: software that watches a financial institution's transaction flows for patterns indicating money laundering / terrorist financing / other financial crime, and generates alerts for human compliance review.
- Users: AML transaction-monitoring analysts, detection/tuning teams, compliance officers.
- Nearest neighbors: AML Platform (owns the case + regulatory-report program), Fraud Detection Platform (loss-prevention decisions), Sanctions Screening Platform (list matching).
- Working hypothesis from the sibling passes: the TM leaf is the detection/alerting layer; case investigation and regulatory reporting belong to the AML program layer even when bundled in the same product.
- Unknowns at start: whether alert triage/disposition is definitional or optional for TM; whether customer context is definitional; whether "real-time" or "ML" is definitional; how standalone TM products (vs suite modules) shape the core.

## Research Questions

1. What is the monitored subject — what data flows in, from where, at what latency?
2. What detection machinery exists (rules, scenarios, thresholds, segmentation, models, typologies) and who owns it?
3. What is an alert, how is it prioritized, and what happens to it (triage → disposition → escalation)?
4. Where does the TM loop terminate — at the alert, at the case, or at the regulatory report?
5. What customer/entity context does TM consume vs own?
6. What tuning/governance machinery surrounds detection (sandbox, backtesting, calibration, audit)?
7. Which capabilities commonly bundled in TM products (case management, SAR filing, screening, consortium data) are definitional vs the AML program layer?
8. Where are the boundaries vs AML Platform, Fraud Detection Platform, Sanctions Screening Platform, and generic machinery (SIEM, stream analytics, BRMS)?

## Representative Products

Selected for market coverage across customer tier, product philosophy, geography, and packaging shape:

| Product | Vendor origin | Tier / segment | Philosophy / packaging in sample |
|---|---|---|---|
| NICE Actimize SAM (Suspicious Activity Monitoring) | US/IL | Global tier-1 banks | Enterprise suite module; layered rules + ML + graph; entity-centric |
| Nasdaq Verafin (Transaction Monitoring solution inside AML/CFT Compliance and Management) | CA (Nasdaq) | North American regional banks, credit unions; also global tier-1 via consortium | Cloud platform + cross-institutional consortium; targeted typology analytics |
| ComplyAdvantage Mesh — Transaction Monitoring | UK | Mid-market/enterprise fintechs, payments, banks | AI-native SaaS; agentic alert resolution; natural-language rules; API-first |
| Napier AI Transaction Monitoring | UK | Banks, payments, wealth/asset management (150+ FIs claimed) | TM-focused modular platform; 100+ inbuilt typologies; no-code rule builder + sandbox |
| Unit21 (AML Transaction Monitoring) | US | Fintechs, crypto, sponsor banks, FIs | API-first agentic platform; unified fraud+AML data core; alert-to-case-to-SAR suite |

## Sources

All fetched 2026-09-08. Evidence layer A (directly observed on official vendor pages) unless noted.

- ComplyAdvantage — Transaction Monitoring product page (rules taxonomy FAQ, decision chain, case/workflow configuration, reporting support, analytics, API posture):
  - https://complyadvantage.com/mesh/transaction-monitoring-software/
- Nasdaq Verafin — corporate site (product family nav) and Transaction Monitoring solution page (flow-of-funds detection, structuring alerts, targeted typology analytics, segmented alerts, SAR automation, case management, watchlist scanning, cross-institutional analysis):
  - https://verafin.com/
  - https://verafin.com/solution/transaction-monitoring/
- NICE Actimize — SAM (Suspicious Activity Monitoring) product page (defense layers: rules library / ML analytics / graph; segmentation, optimization, anomaly detection, predictive scoring; self-developed analytics; collective intelligence):
  - https://www.niceactimize.com/anti-money-laundering/suspicious-activity-monitoring
- Napier AI — corporate site and Transaction Monitoring solution page (100+ inbuilt typologies, no-code rule builder, sandbox, dual rule/ML scoring, workflow and case management automation, Insights AI, Regulatory Reporting Manager, audit trail):
  - https://napier.ai/
  - https://napier.ai/transaction-monitoring/
- Unit21 — corporate site and AML Transaction Monitoring product page (data ingestion breadth, AI detection + smart rules, backtesting/shadow mode, real-time monitoring, graph-based rules, 314(a) agent, dashboards; suite nav separating TM from screening/case/filings):
  - https://unit21.ai/
  - https://www.unit21.ai/products/aml-transaction-monitoring
- Prior-pass counterparty context (local): research/aml-platform.md, research/fraud-detection-platform.md, research/sanctions-screening-platform.md §Boundary Findings; STATUS.md Boundary Issues entries.

Not fetched / gated (no claims rest on them): Unit21 developer docs (password-gated), NICE Actimize brochure PDFs (linked but not fetched), Verafin feature-sheet PDFs (linked but not fetched), Oracle FCCM and Feedzai (covered by the aml-platform pass; not re-fetched here).

## Product Observations

### Product A — NICE Actimize SAM (evidence layer A)

- Positioning: "Suspicious Activity Monitoring… Detect true suspicion and minimize false positives with a multidimensional approach to transaction monitoring… through an entity-centric approach."
- Three named defense layers: **Retain Rules** ("extensive and industry-proven library of rules… ensure regulatory compliance"), **Explore Analytics** ("reduce false positives and capture anomalous outliers with ML and AI"), **Uncover Risk** ("uncover and explore relationships with graph technology").
- Analytics machinery: segmentation (unsupervised ML customer groupings), optimization (ML to assess/optimize model performance), anomaly detection ("identify previously undetected suspicion"), predictive scoring ("determine alert risk and focus resources on the truly suspicious activity").
- Transaction Monitoring Evolution framing: self-developed analytics (build your own ML analytics — "Studio for AML"), connected risk ("transaction monitoring must be connected across the enterprise, using extensive risk signals and disposition decisions to optimize suspicious activity detection"), collective intelligence ("leverage industry-trained models" — Insights Network).
- Data / Detection / Investigation triad on the page: "Know your customers and their risk… Multiple layers of protection… Swifter, smarter investigations."
- Suite context (from nav): AML family sits beside Enterprise Fraud Management, Investigation and Case Management, KYC/CLM — TM is one module of a financial-crime suite.

### Product B — Nasdaq Verafin (evidence layer A)

- Packaging: "Transaction Monitoring" is a named solution inside the **AML/CFT Compliance and Management** product; **Fraud Detection and Management** is a separate product family; **Sanctions Screening and Management** is a third product. Direct vendor-side separation of the three sibling Types.
- Money-laundering detection features:
  - **Suspicious flow-of-funds detection** — "analyzes a customer's deposit and withdrawal activity across channels to find indicators of attempts to launder illicit funds."
  - **Transaction structuring alerts** — "transactions are monitored across an extended period for evidence they may be structuring their deposits to avoid reporting thresholds. You are alerted to potentially suspicious activity."
  - **Targeted Typology Analytics** — predicate-crime-specific detection groups (human trafficking, terrorist financing, drug trafficking) using "AI, such as Bayesian Belief Networks… and consortium insights focused on a specific predicate crime typology."
  - **Segmented alerts** — "flow-of-funds agents are segmented by distinct groups — individuals, businesses, sole proprietors, groups and households. This segmentation allows for easy alert review and triage, including the ability for users to set appropriate alert thresholds specific to your institution's risk tolerance."
- Alert philosophy: "generates an alert when advanced analysis uncovers a legitimate threat of suspicious activity, not every time a simplistic rule is broken."
- Downstream (bundled in the same product): automated SARs ("auto-populated SAR directly from a case… e-file directly from Nasdaq Verafin to FinCEN… 90-day refiling reminders"), integrated case management ("fully audited and tracked investigation… assign tasks… document your decisions"), watch list scanning (nightly OFAC/314(a)/internal lists), cross-institutional analysis and 314(b) information sharing via the Verafin consortium.
- Fraud-side contrast (same vendor): "real-time interdiction to release or reject a payment directly from an alert or case" — interdiction belongs to the fraud product, not TM. Also offered: "real-time risk scores via API" as a fraud product offering.

### Product C — ComplyAdvantage Mesh Transaction Monitoring (evidence layer A)

- Positioning: "Transaction Monitoring on Mesh unifies detection across every risk – from money laundering and fraud to human trafficking – within one AI-native engine."
- Rules taxonomy (FAQ, directly observed): **simple rules** (check data within a transaction), **aggregate rules** ("track activity over multiple transactions (e.g., velocity rules)"), **behavioral rules** ("compare with past activity (e.g., average transaction amount)"), **risk-pattern rules** ("cross-reference activity against a known AML/CTF risk pattern"). "The transaction monitoring solution uses an advanced rules-based system to evaluate the AML/CTF risk of a transaction in real-time."
- Customization: "Rules are completely customizable… can run on any data that you provide… using your own variables, codes, definitions." Thresholds set via "effective customer segmentation, statistical analysis, and – crucially – tuning."
- Configuration surface: natural-language rule builder, intelligent segmentation ("group customers by multiple attributes and risk levels"), dynamic thresholds, sandbox testing ("validate new rules safely… to see the impact on alert volumes before going live").
- **Decision chain** (named workflow): "our end-to-end workflow that manages an alert from the moment it is detected to its final resolution. It seamlessly connects our high-speed detection engine with AI agents and human analysts. In this chain, AI agents autonomously resolve 65-85% of routine false positives [vendor claim], while complex, high-risk patterns are instantly escalated to your expert team with full natural language reasoning and a transparent audit trail."
- Case/workflow capability: "Configurable case management and compliance workflows… Tailor up to eight review and decision stages to mirror your internal team structures… Built-in support for global reporting – including SAR, CTR, and FINTRAC STR and EFT reports."
- Analytics: rule performance (hit rates, false-positive trends per scenario), team productivity, trend analysis.
- Integration: REST API + web UI; CSV export of transaction data "with rule and alert information"; sub-second latency claims (vendor-claimed).
- Suite context (nav): Customer Screening / Company Screening / Ongoing Monitoring / Transaction Monitoring / Payment Screening / Fraud Detection as separate applications over one risk-intelligence layer.

### Product D — Napier AI Transaction Monitoring (evidence layer A)

- Positioning: "Real-time monitoring of transactions with 100+ inbuilt AML typologies… built for AML compliance teams to create, test and implement the rules needed to accurately flag suspicious activity."
- Detection: 100+ prebuilt AML typology library + no-code rule builder + sandbox ("test new rules on real data and compare the results before deploying to live"); "drop-down menus make it simple to build rules and scenarios on real data."
- Dual scoring: "produces two scores: one from rule-based scenarios; and the other from advanced machine learning algorithms. Compare these scores to understand and prioritise daily workload."
- Workflow: "automating task assignments and group alerts… workflow and case management automation"; "manage cases through a single, self-auditing platform that defines and unifies every step of an investigation"; highly configurable dashboard (80+ widgets — vendor claim).
- Insights AI: "embedded directly within… Transaction Monitoring… surfaces behavioural patterns and potential new or emerging risk directly within transaction monitoring tasks… clear, AI-driven explanations of customer behaviour… while keeping human judgement firmly in control."
- Regulatory Reporting Manager: separate module "designed to be used with… Transaction Monitoring and Screening solutions… auto-populate report fields… supports timely, compliant filing" — i.e., filing is an adjacent module, not the TM core.
- Audit: "full audit trail on all user and system generated actions."
- Scale/deployment: big-data architecture, "hundreds of millions of transactions"; hosted or on-prem; SaaS.
- Suite context (nav): **Client Screening / Transaction Screening / Transaction Monitoring** as three separate solutions — the vendor's own nav separates list screening (clients, payment messages) from behavior monitoring.

### Product E — Unit21 AML Transaction Monitoring (evidence layer A)

- Positioning: "Find hidden financial crime risk across your entire data ecosystem. Use all of your data, not just transactions… Most systems generate alerts. Unit21 resolves them."
- Documented pipeline (product page, "How AML transaction monitoring works"): **Ingest any relevant data** (transactions, behavioral signals, device data, customer attributes in real time) → **Deploy AI detection + smart rules** (built-in detection models or configured rules; AI rule recommendations) → **Validate with backtesting & shadow mode** ("test AI models and rules against historical or live shadow data… before deployment") → **Monitor in real time** ("AI risk scoring and adaptive rule logic. Trigger alerts, escalate cases, and prioritize investigations automatically") → **Investigate with full context** ("linked entities, behaviors, transactions, and AI risk signals in one place").
- Graph-based rules: "money mules can be identified using graph-based rules, which programmatically runs link analysis across your entire dataset."
- 314(a) compliance: AI agent validates matches against key identifiers; audit-ready documentation.
- Rules/filtering: "customizable filtering to pinpoint suspicious behaviors on a particular set of transactions, accounts, devices, or customers."
- Program measurement: "40+ dashboards… track alerts, cases, and SAR trends over time, measure investigator productivity, and see KPI progress across queues and dispositions."
- Suite context (nav): Transaction Monitoring / Case Management / Payment Screening / Sanction Screening / Customer Risk Rating / Regulatory Filings as separate named products; fraud side (Real-Time Monitoring with sub-250ms blocking, device intelligence, consortium) is a separate persona track. Direct vendor-side separation of fraud blocking from AML alerting.

## Cross-product Comparison

| Dimension | Actimize SAM | Verafin TM | ComplyAdvantage TM | Napier TM | Unit21 TM | Evidence layer |
|---|---|---|---|---|---|---|
| Monitored subject: institution's own transaction/activity data ingested | yes (entity-centric over transactions) | yes (deposit/withdrawal activity across channels) | yes ("any data that you provide… captured within a transaction") | yes (transactions; big-data ingestion) | yes (transactions + behavioral + device + customer attributes) | A |
| Attribution to customers/accounts/entities | yes (entity-centric) | yes (customer deposit/withdrawal; segmented agents) | yes (customer segmentation) | yes (customer behaviour baselines) | yes (accounts, customers, devices) | A |
| Rules/scenarios with thresholds + segmentation | yes (rule library + segmentation) | yes (thresholds per segment, risk tolerance) | yes (4 rule classes, thresholds, segmentation) | yes (rule builder + typologies) | yes (smart rules + filtering) | A |
| ML/AI detection layer | yes (anomaly, predictive scoring) | yes (Bayesian networks for typologies) | yes (AI agents, behavioral insights) | yes (second ML score) | yes (AI detection models) | A |
| Alerts as managed records, scored/prioritized | yes (predictive alert risk) | yes (segmented alerts, triage) | yes (decision chain, priorities) | yes (dual-score prioritization) | yes (risk scoring, prioritization) | A |
| Human alert triage/disposition in-product | yes (investigation layer) | yes (alert review and triage) | yes (up to 8 review/decision stages) | yes (workflow/case automation) | yes (L1 triage, escalate cases) | A |
| Escalation toward case investigation | via suite (STAR/ICM) | in-product (integrated case management) | in-product (case management) | in-product (case management) | in-product (case management) | A |
| Regulatory reporting support | via suite | in-product (SAR e-filing to FinCEN) | in-product (SAR/CTR/FINTRAC support) | adjacent module (Regulatory Reporting Manager) | in-product (Regulatory Filings) | A |
| Detection tuning machinery (sandbox/backtest) | yes (self-developed analytics, optimization) | threshold setting per risk tolerance | yes (sandbox testing) | yes (sandbox test-and-deploy) | yes (backtesting + shadow mode) | A |
| Performance analytics (hit rates, false positives) | yes (optimization) | yes (alert quality framing) | yes (rule performance dashboards) | yes (FP/FN reduction framing) | yes (40+ dashboards) | A |
| Audit trail as first-class property | yes (connected risk, disposition decisions) | yes (audited investigations) | yes (transparent audit trail) | yes (self-auditing platform, full audit trail) | yes (audit-ready documentation) | A |
| Graph/network analytics | yes (Uncover Risk layer) | via consortium/cross-institutional analysis | related entities in context | via case management | yes (graph-based rules) | A |
| Consortium / cross-institutional intelligence | yes (Insights Network industry models) | yes (Verafin Cloud consortium, 314(b) sharing) | proprietary risk data (screening-side) | third-party data vendors | yes (fraud consortium; AML-side signals) | A (vendor-claimed scale) |
| Real-time/streaming posture | not asserted on page | real-time risk scores = fraud product; TM monitoring across extended periods | real-time evaluation claimed | real-time monitoring claimed | real-time ingestion + monitoring claimed | A (posture varies) |
| Payment blocking / interdiction | no (fraud suite separate) | no (fraud product interdicts) | no | no | no (fraud Real-Time Monitoring blocks; AML TM alerts) | A |

Reading of the comparison:

- Every sampled product implements the same three-part spine: institution transaction data in → configurable suspicious-pattern detection (rules + commonly ML) → alerts worked by humans to a recorded disposition with escalation as the exit.
- Case management and regulatory-reporting support appear in most sampled TM offerings but with different packaging (in-product, adjacent module, or sibling suite module) — consistent with the aml-platform pass's capability-vs-program test: they are the AML program layer bundled into TM products, not what makes TM recognizable.
- No sampled TM product blocks or interdicts payments; interdiction appears only in the fraud-detection sibling products of the same vendors (Verafin, Unit21 directly observed).
- All four multi-product vendors separate screening (list matching) from monitoring (behavior patterns) in their own product navs.

## Canonical Model (abstraction levels)

### Level 0 — Defining Invariant

Three jointly-held structures. Remove any one and the product is no longer recognizable as a Transaction Monitoring Platform:

1. **The institution's monitored transaction stream** — the institution's own transaction/activity data (payments, transfers, deposits/withdrawals across channels), attributable to its customers/accounts, flowing into the platform from institutional systems as the standing subject of surveillance. The platform does not generate this data; it is the analytical watch layer over it.
2. **Configurable suspicious-behavior detection** — institution-tuned detection logic (rules/scenarios parameterized by thresholds and applied over customer segments; commonly ML models) evaluating the stream against suspicious-activity patterns — single-transaction checks, multi-transaction aggregates/velocity, behavior-vs-history comparisons, named typologies — and generating alerts on potentially suspicious activity.
3. **The alert-to-disposition loop** — alerts held as managed records, scored/prioritized, worked by human reviewers who record a disposition (close as explained/false positive, or escalate for investigation), with escalation as the loop's exit toward case investigation and regulatory reporting.

Jointly-held is load-bearing:

- 1 alone = a transaction data warehouse.
- 2 alone = a rules engine / scoring service.
- 3 alone = a generic alert queue.
- 1+2 without 3 = an alert generator whose output nobody manages — detection without monitoring.
- 1+3 without 2 = manual review of transaction reports (the pre-software ancestor — humans eyeballing listings; the software Type exists to automate leg 2).
- 2+3 without 1 = detection machinery with no institution's actual activity behind it.

What the L0 deliberately excludes (tested below): customer due-diligence context ownership, case investigation, regulatory reporting, list screening, real-time latency, ML, typology libraries, consortium data.

### Level 1 — Common Mature Structure

Present across the researched sample (evidence layer B unless noted):

- **Customer/entity context layer** — profiles, attribute- and risk-based segmentation, behavioral baselines consumed from institutional data; entity-centric analysis (Actimize explicit; all five sample).
- **ML/AI detection layer** — anomaly detection, predictive alert scoring, behavioral models, with explainability of AI outputs to the audit standard (Actimize, ComplyAdvantage, Napier, Unit21 explicit; Verafin via Bayesian typology networks).
- **Typology/scenario libraries** — vendor-maintained prebuilt detection content, including predicate-crime-targeted analytics (Napier 100+ typologies; Actimize industry-proven rule library; Verafin targeted typologies).
- **Detection management** — no-code/natural-language rule builders, sandbox testing, backtesting/shadow mode, threshold calibration, versioning (ComplyAdvantage, Napier, Unit21 explicit; Verafin threshold setting; Actimize Studio).
- **Alert prioritization/risk scoring** — predictive scoring to focus analyst effort (all five).
- **Case management + investigation workspaces** (when bundled) — evidence assembly, narratives, task assignment (Verafin, ComplyAdvantage, Napier, Unit21 in-product; Actimize via suite).
- **Regulatory reporting support** (when bundled) — SAR/CTR/STR-format generation and filing support (Verafin e-filing; ComplyAdvantage built-in support; Napier adjacent module; Unit21 filings product).
- **Network/graph analytics** — linked entities, mule detection (Actimize, Unit21 explicit; others via case context or consortium).
- **Consortium/cross-institutional intelligence** — shared signals across institutions (Verafin consortium; Actimize Insights Network; Unit21 consortium on the fraud side).
- **Performance analytics** — hit rates, false-positive trends, analyst productivity, program KPIs (all five).
- **End-to-end audit trail** — configuration changes, dispositions, AI reasoning recorded (all five).
- **Integration spine** — API/streaming and batch ingestion from institutional systems; export paths.

### Level 2 — Variant / Optional Structure

- **Latency posture**: batch/end-of-day (heritage mode) vs near-real-time/real-time streaming — current products emphasize real-time, but batch satisfies the Type (historical check).
- **Packaging**: standalone TM solution (Napier) vs named module inside an AML suite (Actimize SAM; Verafin solution inside AML/CFT product) vs one application in a converged fraud+AML platform (ComplyAdvantage, Unit21).
- **Customer segment**: universal banks vs regional banks/credit unions vs fintech/payments/crypto vs wealth/asset management.
- **Regulatory regime**: US BSA/FinCEN, Canada FINTRAC, EU/UK, goAML jurisdictions — shapes typologies, thresholds, and reporting formats, not the core.
- **Deployment**: cloud SaaS vs on-premises vs hybrid (Napier explicitly both).
- **Data philosophy**: institution-data-only vs vendor consortium/industry-trained models.
- **AI posture**: rules-only → ML scoring → agentic auto-triage with human gates (era-current; ComplyAdvantage and Unit21 lead the agentic pole).
- **Adjacent modules**: watchlist scanning, 314(a) request processing, customer risk rating, screening — present in some suites as sibling capabilities.

### Level 3 — Vendor-specific (kept out of the final document)

- Actimize: SAM name; Retain Rules / Explore Analytics / Uncover Risk layer names; Studio for AML; Insights Network; X-Sight/Xceed platforms.
- Verafin: Targeted Typology Analytics (Bayesian Belief Networks); flow-of-funds agents segmented by individuals/businesses/sole proprietors/groups/households; automated SAR e-filing to FinCEN with 90-day refiling reminders; 314(b) information sharing; consortium scale claims (2,800+ partners, 1.8B transactions/week — vendor-claimed).
- ComplyAdvantage: decision chain; natural-language rule builder; agentic 65–85% auto-resolution and ≤82% false-positive-reduction claims; composable data model; 3.5B daily messages and <20ms aggregation claims; up-to-eight review stages.
- Napier: 100+ inbuilt typologies; Insights AI; Regulatory Reporting Manager; 80+ widgets; dual rule/ML score model; six-week deployment claim (Starling testimonial).
- Unit21: Detection/Investigation AI agents; graph-based rules; 314(a) AI agent; 40+ dashboards; backtesting/shadow mode "any timeframe"; sub-250ms fraud-side latency claim; 4.5B monthly events claim.

All numeric claims above are vendor-claimed and recorded here only; none are promoted to the canonical document.

## Rejected Findings

- **"Real-time is definitional"** — rejected. Batch/end-of-day scenario engines (the 2000s heritage form) satisfy the Type fully; real-time is the current dominant posture (L2).
- **"ML/AI is definitional"** — rejected. Rules-only detection machinery constitutes a TM platform (historical check; Actimize's own "Retain Rules" layer frames rules as the compliance safety net with ML as enhancement).
- **"TM owns the whole AML program"** — rejected as identity. The market sells TM as the detection/alerting layer; case investigation and regulatory reporting are the AML program layer, bundled into TM products with varying packaging (in-product / adjacent module / sibling module). The aml-platform pass's capability-vs-program test is ratified from this side with fresh evidence (Napier sells filing as an adjacent module; Actimize splits SAM from case management across suite modules).
- **"TM includes payment blocking/interdiction"** — rejected. No sampled TM product blocks payments; interdiction appears only in the same vendors' fraud-detection products (Verafin "release or reject a payment"; Unit21 sub-250ms fraud blocking). TM observes and alerts; it does not decide the payment.
- **"Typology libraries are definitional"** — rejected. Institution-built rules satisfy; prebuilt libraries are common mature content (L1).
- **"Consortium data is definitional"** — rejected. Several sampled products run on institution-data-only deployments (L2).

## Boundary Findings

1. **vs AML Platform (§08 sibling — discharges the aml-platform flag)**: the two Types interlock at the escalation seam. TM is the detection/alerting layer: transaction stream in, alerts out, dispositions recorded, escalation as the exit. The AML Platform is the program system of record: monitored customers with due-diligence context + case investigation with recorded rationale + regulatory reporting as the terminal artifact. TM products commonly bundle case+reporting capabilities (observed in 4/5 sample) — the boundary holds on the capability-vs-program test: what makes the product recognizable as TM is the detection/alerting spine, not the program layer. Test: remove case+reporting → still a TM platform; remove detection/alerts → not TM (case management only). Consistent with research/aml-platform.md §Boundary Findings (reverse direction).
2. **vs Fraud Detection Platform (§08 sibling — discharges the fraud-detection-platform flag)**: same machinery shape (records → rules/scenarios → alerts → cases → dispositions), different objective and output. TM: regulatory surveillance of transaction behavior; terminal output is dispositioned alerts escalating toward compliance artifacts; no decision on the payment itself; feedback loop is investigator dispositions feeding detection tuning. Fraud: loss prevention; terminal output is a decision on the activity (allow/decline/step-up/interdict); feedback includes chargebacks and confirmed fraud. Direct vendor-side evidence: Verafin ships real-time payment interdiction in its Fraud product and behavior-pattern alerting in its AML/TM product; Unit21 separates Real-Time Monitoring (fraud, blocking) from AML Transaction Monitoring (alerts, escalation). Convergence exists (ComplyAdvantage markets one engine "across every risk"; Unit21 unified data core) but the two Types keep distinct objectives, users, and outputs — consistent with research/fraud-detection-platform.md §Boundary Findings.
3. **vs Sanctions Screening Platform (§08 sibling — completes the three-way ratification requested by the sanctions pass)**: sanctions screening makes list-membership determinations on named parties (customers, payment messages) and produces screening evidence; TM detects behavior patterns over transaction streams and produces alerts. Direct vendor-side evidence: all four multi-product vendors separate the two in their own navs — Napier (Client Screening / Transaction Screening / Transaction Monitoring), Unit21 (Payment Screening / Sanction Screening / Transaction Monitoring), Verafin (Sanctions Screening and Management vs AML/CFT Compliance containing TM), ComplyAdvantage (screening applications vs Transaction Monitoring application). Three-way ratification from the TM side: sanctions = list-membership determination + screening evidence; TM = behavior-pattern detection + alerts; AML = program of record + regulatory filing. Keep all three as separate Types.
4. **vs KYC / KYB Platform (§15)**: KYC verifies identity at onboarding; TM watches ongoing transaction behavior. TM consumes customer attributes/segmentation but does not own the identity/CDD program (that context belongs to the AML program layer and KYC systems).
5. **vs Regulatory Reporting Platform (§08)**: generic regulatory reporting covers prudential/statistical/transaction returns. The suspicious-activity report grows out of the TM→AML investigation flow; TM products support filing formats as a bundled capability, which does not make them regulatory-reporting platforms.
6. **vs SIEM (§15)**: same alert-triage operational shape (events → detection rules → alerts → cases) but different domain and record semantics (security telemetry vs financial transactions), different users (SOC vs AML compliance), different regulatory purpose.
7. **vs Stream Analytics / Event Stream Processing (§13) and Business Rules Management System (§10)**: generic pattern/rule machinery could power part of a TM platform; the TM Type is defined by the AML purpose, the transaction data model, typologies, and the compliance alert workflow — not by the machinery.
8. **"Remove what to become another Type" test**: remove behavior-pattern detection (keep list matching) → Sanctions Screening; remove the regulatory/compliance purpose and add payment decisions → Fraud Detection; remove alerts and add case+reporting ownership → AML Platform; remove the institution's transaction stream → generic alert/case tooling.

## Historical / Market-Sample Check

Would older, regional, differently positioned products fit the proposed L0?

- **2000s batch scenario engines** (the Mantas lineage now inside Oracle FCCM, per the aml-platform pass): ETL'd transaction data + scenario rules with thresholds + alert queue + analyst triage/disposition — satisfies all three legs. No real-time, no ML, no cloud required.
- **Manual pre-software practice**: compliance staff reviewing transaction reports and currency-transaction listings against known typologies and reporting thresholds, flagging accounts and escalating for investigation — the thin ancestor. It satisfies the abstract shape with human detection (1+3, detection by hand); the software Type exists to industrialize leg 2. Correctly excluded as a *platform*, retained as the ancestry.
- **Regional regimes** (FINTRAC, goAML jurisdictions, UK/EU): fit — the Type is jurisdiction-generic; regimes shape typologies and reporting formats (L2).
- **Non-bank TM** (payments, crypto, wealth): fit — the monitored stream is whatever the institution's transaction data is.
- **Real-time streaming, ML scoring, agentic auto-triage, consortium intelligence**: era-current capabilities, all correctly outside L0.

The definition survives the historical check.

## Uncertainties

- Exact alert-stage counts, threshold values, SLAs, and scoring scales are institution-configured or vendor-claimed; none are asserted in the canonical document.
- Filing-integration depth varies (direct e-filing documented for Verafin; "built-in support" language for ComplyAdvantage; adjacent-module packaging for Napier); per-product filing mechanics were not verifiable beyond the reached pages.
- Unit21's developer documentation is password-gated; its pipeline description rests on the public product page (Tier 2 for operational detail).
- Actimize brochure PDFs and Verafin feature sheets were linked but not fetched; SAM and Verafin observations rest on product-page depth.
- Whether a pure "alerts-out-only" TM engine (no triage surface at all) exists as a standalone product in the current market was not observed; the sampled TM offerings all carry at least workflow/triage. If such products exist, they would sit at the Type's edge (detection engine below the platform).
- Oracle FCCM and Feedzai were not re-fetched in this pass; their TM behavior is inherited from the aml-platform pass's observations and was not used as primary evidence here.

## Final Synthesis

A Transaction Monitoring Platform is the financial institution's detection-and-alerting system over its own transaction flows: the institution's transaction data — attributable to its customers — flows in (batch or streaming); configurable detection logic (rules/scenarios with thresholds and segmentation, commonly augmented by ML models and typology libraries) evaluates the stream against suspicious-activity patterns and generates alerts; alerts are scored, prioritized, and worked by human analysts who record a disposition — closing the alert as explained or escalating it toward case investigation and regulatory reporting. Around that spine, mature products add customer/entity context, explainable AI scoring, detection-management tooling (rule builders, sandboxes, backtesting), network analytics, consortium intelligence, performance analytics, and end-to-end audit trails; case management and regulatory-reporting support ride along as the AML program layer bundled into the product. The Type's edges: it watches behavior patterns (not list membership — sanctions screening), it alerts for compliance judgment rather than deciding payments (not fraud detection), and it ends at the escalation seam rather than owning the case-and-filing program (not the AML platform).
