# Research Notes — AML Platform

Research date: 2026-09-06

## Research Goal

Understand what an AML (Anti-Money Laundering) Platform actually is as an Application Type: its core objects, its end-to-end operational loop (detection → investigation → regulatory reporting), its roles, its rules, and its boundaries against neighboring Types (Transaction Monitoring Platform, Sanctions Screening Platform, Fraud Detection Platform, KYC/KYB Platform, Regulatory Reporting Platform, GRC/Compliance Management).

## Initial Boundary Hypotheses

- AML Platform = software used by regulated institutions (banks, fintechs, crypto/VASPs, MSBs, etc.) to meet AML/CTF regulatory obligations: detect potentially suspicious activity, investigate it with human analysts, and produce regulatory reports (SAR/STR and equivalents).
- Adjacent Types hypothesized:
  - **Fraud Detection Platform** — purpose is loss/customer protection; terminal outcome is a block/decline, not a regulatory filing.
  - **Transaction Monitoring Platform** — detection engine (alerts) as the headline capability; may or may not own case + reporting.
  - **Sanctions Screening Platform** — list-based name matching (sanctions/PEP/adverse media), no behavioral transaction analysis.
  - **KYC/KYB Platform** — onboarding identity verification and due diligence; AML platforms consume KYC data and do *ongoing* monitoring.
  - **Regulatory Reporting Platform** — broader regulatory reports (prudential, statistical); AML reporting is the suspicious-activity subset tied to the platform's own investigation flow.
- Unknowns at start: how far into CDD/EDD and screening typical AML platforms reach; the shape of the alert→case→report workflow; the role model; how detection is configured and governed.

## Research Questions

1. What are the core objects in an AML platform (customer, transaction, rule/scenario, model, alert, case, report, watchlist hit)?
2. What is the canonical alert → case → regulatory-report workflow, and which roles gate it?
3. How is detection configured and governed (rules, thresholds, segmentation, ML models, calibration, validation, audit)?
4. How is customer risk rating / CDD / EDD handled — defining or optional?
5. How does regulatory reporting work (report types, jurisdictions, filing support)?
6. What interfaces do users actually operate?
7. Where are the boundaries vs Transaction Monitoring, Sanctions Screening, Fraud Detection, KYC, Regulatory Reporting?

## Representative Products

Selected for market coverage across customer tier, product philosophy, and geography:

| Product | Vendor origin | Tier / segment | Philosophy in sample |
|---|---|---|---|
| NICE Actimize AML (SAM / STAR / X-Sight / Xceed) | US/IL | Global tier-1 banks, large FIs; also cloud "AML Essentials" for smaller FIs | Modular enterprise financial-crime suite, entity-centric |
| Oracle Financial Crime and Compliance Management (FCCM) | US | Large banks, on-prem heritage + cloud services | Bank-grade suite: scenarios + behavioral models + investigation hub + reporting |
| ComplyAdvantage Mesh | UK | Mid-market/enterprise fintechs, payments, banks | AI-native SaaS; proprietary risk-data feeds; agentic workflows; API-first |
| Feedzai RiskOps / AML Suite | PT/US | Global banks, PSPs, acquirers | ML-first platform unifying fraud + AML (RiskOps) |
| Unit21 | US | Fintechs, crypto platforms, sponsor banks, FIs | API-first unified fraud+AML ops with agentic AI, alert-to-case-to-SAR lifecycle |

## Sources

All fetched 2026-09-06. Evidence layer A unless noted.

- NICE Actimize — corporate site, AML solution page, SAM (Suspicious Activity Monitoring) product page:
  - https://www.niceactimize.com/
  - https://www.niceactimize.com/anti-money-laundering
  - https://www.niceactimize.com/anti-money-laundering/suspicious-activity-monitoring
- Oracle FCCM — Financial Crime and Compliance Management solution page (incl. FAQ on behavioral models and scenario calibration):
  - https://www.oracle.com/financial-services/aml-financial-crime-compliance/
- ComplyAdvantage — corporate site and Transaction Monitoring product page (incl. rules FAQ, decision chain, case workflows, regulatory reporting support):
  - https://complyadvantage.com/
  - https://complyadvantage.com/mesh/transaction-monitoring-software/
- Feedzai — corporate site and AML solution page (incl. FAQ):
  - https://www.feedzai.com/
  - https://www.feedzai.com/anti-money-laundering/
- Unit21 — corporate site (AML suite: transaction monitoring, case management, sanctions/payment screening, customer risk rating, regulatory filings):
  - https://unit21.ai/
- Attempted, gated/failed (not used): https://docs.unit21.ai/docs (sign-in gated), https://www.niceactimize.com/aml/suspicious-activity-monitoring (404; replaced by correct URL), https://feedzai.com/aml-transaction-monitoring/ (404; replaced by /solutions/ pages). Vendor datasheet/brochure PDFs referenced from pages were not fetched.

Source-access limitation: deep operational help centers were mostly not reachable (Unit21 docs sign-in gated; Oracle/Actimize operational detail lives in PDF datasheets not fetched). Observations below therefore lean on official product/solution pages and on-page FAQs (still vendor-official, layer A), and precise operational details (exact SLAs, exact stage counts beyond what vendors state, exact list coverage counts, numeric limits) are deliberately not asserted in the final document.

## Product Observations

### NICE Actimize

Key observations (evidence A):

- Positions AML as a suite: SAM (Suspicious Activity Monitoring = transaction monitoring), KYC / Client Lifecycle Management, Sanctions Screening, X-Sight Entity Risk, STAR (Suspicious Transaction Activity Reporting), CTR (Currency Transaction Reporting), AML Essentials (cloud offering), Xceed ("Integrated FRAML").
- Entity-centric positioning: "putting the entity at the heart of all AML risk management processes"; "full AML compliance coverage and auditability."
- SAM structured as layered defense:
  - **Rules** — "extensive and industry-proven library of rules" to detect known threats and "ensure regulatory compliance."
  - **ML analytics** — unsupervised-ML customer segmentation, anomaly/outlier detection, predictive alert risk scoring, model-performance optimization.
  - **Graph/network analytics** — uncover relationships ("Community Analytics to detect clusters of high-risk threats"; mule-ring case studies).
- Self-developed analytics: business users can build their own ML analytics ("Studio for AML").
- Fraud is a **separate** solution family (Enterprise Fraud Management); FRAML convergence offered via Xceed.
- Reporting products named explicitly: STAR (suspicious activity/transaction reporting) and CTR automation.
- Marketing-numbers layer (do not generalize): 1000+ clients, 5B+ transactions monitored daily.

### Oracle Financial Crime and Compliance Management (FCCM)

Key observations (evidence A):

- Suite modules: Transaction Monitoring ("advanced analytics and scenarios built and proven for the financial services industry"), KYC (CDD/EDD) with "continuous monitoring … throughout the customer lifecycle," Customer Screening, Transaction Filtering (sanctions on payments), Compliance Regulatory Reporting ("generate and file suspicious activity reports and suspicious transaction reports"), Investigation Hub (case management with "AI, machine learning, and graph analytics"), Compliance Studio (modeling suite), Compliance Monitor (risk assessments, dashboards), Compliance Agent (adversarial simulation of the program's controls).
- On-page FAQ gives unusual operational depth (evidence A):
  - **Behavioral models** = supervised ML trained on historical labeled outcomes "for example, investigator dispositions"; produce risk scores to prioritize alerts; features are amount/count aggregates by time window, breakdowns by type/channel, velocity/trend indicators; evaluated with AUC; deployed through draft → publish → approved runtime with versioning for traceability.
  - **Automated Scenario Calibration** = structured threshold tuning with below-the-line/above-the-line (BTL/ATL) analysis, alert-volume comparison by segment/jurisdiction/run date, documented threshold-set versioning and audit trail for governance.
- This documents the rule/model governance lifecycle: tune → compare → justify → version → audit.

### ComplyAdvantage Mesh

Key observations (evidence A):

- Platform = "financial crime risk applications" (Customer Screening, Company Screening, Ongoing Monitoring, Transaction Monitoring, Payment Screening) + proprietary "financial crime risk intelligence" (Sanctions & Watchlists, PEPs & RCAs, Adverse Media) + case management + agentic workflows.
- Transaction Monitoring product page (evidence A):
  - Rule taxonomy in FAQ: **simple rules** (per-transaction checks), **aggregate rules** (multi-transaction, e.g. velocity), **behavioral rules** (compare with past activity, e.g. average amount), **risk-pattern rules** (cross-reference against known AML/CTF risk patterns).
  - Self-serve configuration: natural-language rule creation for compliance staff, customer segmentation by attributes/risk, dynamic thresholds, **sandbox testing** of new rules before go-live.
  - Case management: "configurable case management and compliance workflows"; "tailor up to eight review and decision stages to mirror your internal team structures"; 360° case context (transaction history, related entities, risk evolution).
  - Regulatory readiness: "built-in support for global reporting – including SAR, CTR, and FINTRAC STR and EFT reports – ensures seamless filing and comprehensive audit capabilities."
  - Performance analytics: per-scenario hit rates and false-positive trends, analyst productivity, trend analysis.
  - Decision chain: detection engine → AI agents → human analysts; agents auto-resolve a vendor-claimed share of routine false positives; natural-language reasoning recorded in the audit trail.
  - API-first: REST/JSON API mirroring the web UI; CSV export of transactions + rule/alert output.
- Customer risk context comes via screening + ongoing monitoring of the customer lifecycle.

### Feedzai

Key observations (evidence A):

- RiskOps platform positions fraud + AML + identity on one platform "across the entire customer lifecycle."
- AML Suite = "transaction monitoring, watchlist screening and case management on a single platform."
- AML Transaction Monitoring: "identify potential AML and Terrorist Financing patterns using rules and trusted AI to prioritize alerts," letting "investigators focus on high-risk cases."
- Watchlist Management: sanctions/PEP/transaction screening; "automate alerts, document decisions, and maintain transparent audit trails."
- On-page FAQ (evidence A) frames the AML compliance components: "customer due diligence, transaction monitoring, reporting suspicious activity, and maintaining comprehensive records," under regimes such as the Bank Secrecy Act, USA PATRIOT Act, and EU AML Directives.
- Explicit contrast against legacy: "Unlike static, rules-based systems, Feedzai leverages AI…" (vendor positioning; rules remain present in its own TM description).

### Unit21

Key observations (evidence A):

- AML product line: Transaction Monitoring, Case Management, Payment Screening, Sanctions Screening, Customer Risk Rating, Regulatory Filings.
- Transaction Monitoring: "configurable rules, behavioral models, and AI agents. Adaptive risk scoring surfaces the highest-risk activity first."
- Case Management: "configurable alert-to-case-to-SAR workflows guide analysts through the full investigation lifecycle"; AI gathers evidence, drafts narratives, logs every step; "graph analysis automatically connects entities across thousands of data points."
- Customer Risk Rating: "automatically calculate and update customer risk profiles based on activity, device signals, sanctions exposure, and network associations. Supports EDD workflows and ongoing monitoring."
- Regulatory Filings: "AI agents pre-populate SARs, STRs, CTRs, 314(a), and goAML filings with evidence, timelines, and policy references. Every filing includes a complete audit trail."
- Sanctions Screening: OFAC/PEP/adverse-media lists, fuzzy matching, configurable thresholds, continuous monitoring — a separate product line inside the same platform.
- Unified fraud+AML: "unifies fraud, AML, EDD, and sanctions in a connected data model, transforming flat records into real-time entity networks."
- Human-in-the-loop AI posture: AI executes, humans approve; "regulator and audit-ready" traceability of AI decisions.
- Docs portal is sign-in gated (not used). Vendor-claimed metrics (e.g. share of US SARs filed) not generalized.

## Cross-product Comparison

| Aspect | Actimize | Oracle FCCM | ComplyAdvantage | Feedzai | Unit21 |
|---|---|---|---|---|---|
| Monitored customers / KYC context | entity-centric risk (X-Sight Entity Risk); KYC/CLM module | KYC CDD/EDD lifecycle, continuous monitoring | customer/company profiles via screening + ongoing monitoring | customer lifecycle across RiskOps | customer risk rating (dynamic; EDD support) |
| Activity ingestion | transactions at scale (vendor-claimed) | transactions | transactions via API, billions/day (vendor-claimed) | events at scale (vendor-claimed) | events (vendor-claimed) |
| Detection configuration | rule library + ML analytics + user-built analytics | proven scenario library + calibration tooling | simple/aggregate/behavioral/risk-pattern rules; NL rule builder; sandbox | rules + AI prioritization | configurable rules + behavioral models |
| Alert prioritization | predictive scoring | behavioral-model risk scores | AI decision chain | rules + trusted AI | adaptive risk scoring |
| Investigation | case management (separate suite pillar) | Investigation Hub (AI/ML/graph) | configurable stages (vendor states up to 8), 360° view | case mgmt in AML Suite | alert-to-case-to-SAR workflow, evidence + narrative drafting |
| Watchlist/sanctions screening | dedicated Sanctions Screening line | Customer Screening + Transaction Filtering | screening apps + proprietary risk data | watchlist screening in suite | sanctions + payment screening |
| Regulatory reporting | STAR, CTR | compliance regulatory reporting (generate and file SAR/STR) | SAR, CTR, FINTRAC STR/EFT support | reporting via AML suite (FAQ framing) | SAR/STR/CTR/314(a)/goAML pre-population |
| Network/graph analytics | community analytics, graph | graph analytics in Investigation Hub | related entities in case view | Feedzai IQ network intelligence | graph entity connection |
| Model/rule governance | model optimization; auditability emphasis | versioned thresholds/models, AUC evaluation, calibration audit trail | explainability, bias management, independent validation, audit trail | explainability emphasis | traceable AI decisions, audit trail |
| Fraud relationship | separate suite; FRAML via Xceed | separate from fraud | separate fraud-detection product | unified (RiskOps) | unified platform |
| Tier emphasis | global banks → cloud essentials tier | large banks (on-prem heritage, cloud now) | mid-market/enterprise SaaS | banks/PSPs | fintech/crypto/sponsor banks |

### What is stable across all five (evidence B)

1. Ingested institutional transaction/activity data evaluated against **configurable detection logic** (rules/scenarios, increasingly ML models).
2. Alerts feed a **human investigation workflow** with case records, evidence, and recorded rationale.
3. The workflow terminates in **regulatory reporting** of suspicious activity (SAR/STR family; jurisdiction-specific formats observed: FinCEN SAR/CTR, FINTRAC STR/EFT, goAML).
4. **Customer context** (identity, KYC/due-diligence, risk rating) anchors monitoring; ongoing monitoring of the customer is standard.
5. **Screening integration** (sanctions/PEP/adverse media) is present in every sample, as own module or sibling product.
6. **Auditability** is an explicit, first-class property in every product (audit trail of dispositions, threshold/rule/model versioning, explainability of AI decisions).
7. False-positive management (thresholds, segmentation, scoring, calibration, sandbox testing) is a central operational concern.
8. Fraud detection exists as either a separate product family or an integrated convergence ("FRAML"), demonstrating the market treats AML and fraud as related but distinct disciplines.

## Canonical Model (abstraction levels)

### Level 0 — Defining Invariant

The minimal structure without which the Type is not recognizable:

1. **Monitored customers/parties with due-diligence context** — identified records of the institution's customers whose activity the institution is obligated to monitor.
2. **Ingested activity** — the institution's own transactional/behavioral data flowing into the platform.
3. **Configurable suspicious-activity detection** — institution-tuned logic (rules/scenarios; commonly models) evaluating activity and producing alerts on potentially suspicious behavior.
4. **Human investigation with recorded rationale** — alert triage → case investigation → disposition, documented as audit evidence.
5. **Suspicious-activity regulatory reporting** — production of the regulatory report to the competent authority as the terminal outcome of confirmed suspicion.

Remove customers/KYC context → generic anomaly monitoring (not AML). Remove ingested activity → list screening or pure case management. Remove detection → case management only. Remove human investigation → an alert generator (Transaction Monitoring engine). Remove regulatory reporting → fraud/risk monitoring whose outcome is a business action, not a regulatory artifact.

### Level 1 — Common Mature Structure

- Customer risk rating, often dynamically updated from activity/behavior/network signals, supporting EDD and ongoing monitoring
- Sanctions/PEP/adverse-media screening (integrated module or connected sibling system)
- Alert prioritization/scoring (increasingly ML-driven)
- Detection management: scenario/rule libraries, thresholds, customer segmentation, calibration/tuning, sandbox or pre-production testing
- Model governance: versioning, validation, performance measurement, explainability, documented approvals
- Multi-stage case workflow (triage → investigation → senior compliance decision) with evidence attachment and narrative drafting
- Multi-jurisdiction filing support (SAR/STR/CTR families; goAML-type formats)
- Entity/graph/network analytics (linked entities, mule networks, cluster detection)
- End-to-end audit trail
- Performance analytics (rule hit rates, false-positive trends, analyst productivity)
- CDD/EDD lifecycle support (periodic review, profile-change monitoring)

### Level 2 — Variant / Optional Structure

- Deployment: on-premises (bank heritage) vs cloud/SaaS; batch vs API/real-time ingestion
- Industry: banking, fintech/payments, crypto/VASP, credit unions, sponsor banks, MSBs, gaming
- Regulatory regime: US BSA/FinCEN, EU AMLD, UK, Canada FINTRAC, goAML jurisdictions — report formats and eligibility rules vary
- Fraud+AML posture: separate suites vs unified "FRAML" platforms
- Data philosophy: platform-internal detection only vs bundled proprietary risk intelligence/data feeds
- AI posture: decision-support scoring vs agentic auto-disposition with human review
- Scale packaging: enterprise suites vs "essentials"/starter cloud editions for smaller institutions

### Level 3 — Vendor-specific (kept out of the final document)

- Actimize: SAM, STAR, CTR, X-Sight Entity Risk, Xceed, AML Essentials, Insights Network (shared industry models)
- Oracle: Investigation Hub, Compliance Studio, Compliance Monitor, Compliance Agent (adversarial simulation), BTL/ATL calibration workflow
- ComplyAdvantage: Mesh, decision chain, proprietary risk database, natural-language rule builder, vendor-claimed agentic resolution rates
- Feedzai: RiskOps, Feedzai IQ, Feedzai Orchestration
- Unit21: AI detection/investigation agents, fraud consortium, sponsor-bank operating system, vendor-claimed SAR share

## Boundary Findings

- **vs Transaction Monitoring Platform**: transaction monitoring is the detection *engine* inside every sampled AML platform; several vendors sell it as a standalone module. The AML Platform Type is distinguished by owning the full compliance loop — customer risk context, case investigation, and regulatory reporting. If the system's terminal output is alerts handed to another system, it is a TM platform; if it owns the case-to-report lifecycle, it is an AML platform. **Overlap risk is real** (see Boundary Issues).
- **vs Sanctions Screening Platform**: screening matches names against lists (sanctions/PEP/adverse media) and gates customers/payments; it does not analyze behavioral transaction patterns. Every sampled AML platform integrates or bundles screening, but screening is a separate Type and also exists standalone.
- **vs Fraud Detection Platform**: fraud's purpose is loss/customer protection; its terminal outcome is a real-time block/decline/recovery action. AML's purpose is regulatory detection and documentation; its terminal outcome is a filed report (plus program auditability). Several products now unify both (FRAML) on one data core, but the two disciplines keep distinct objectives, users, and outcomes.
- **vs KYC/KYB Platform**: KYC platforms verify identity at onboarding. AML platforms consume that context and add behavioral surveillance over the ongoing relationship (ongoing monitoring, risk-rating updates, EDD triggers). Overlap occurs in CDD/EDD lifecycle modules.
- **vs Regulatory Reporting Platform**: generic regulatory reporting covers prudential/statistical returns etc. The AML platform generates the suspicious-activity report *from its own investigation flow*; jurisdictions' report schemas are specific (SAR/STR/CTR/goAML/FINTRAC observed).
- **vs GRC / Compliance Management**: GRC manages policies, controls, obligations, assessments. The AML platform is an operational detection/investigation system executing part of the AML program, not a control-catalog system.
- **"Remove what to become another Type" test**: remove case+reporting → TM platform; remove activity monitoring → screening platform; remove regulatory purpose → fraud platform; remove ongoing monitoring → KYC platform.

## Historical / Market-Sample Check

Would older, regional, differently positioned products fit the proposed Level 0?

- 2000s-era bank AML systems (behavior-detection scenario engines + alert queues + case management + SAR generation, e.g. the Mantas lineage now inside Oracle FCCM) fit fully.
- Older/regional watchlist-only products do **not** fit — correctly, they belong to Sanctions Screening.
- goAML-based FIU regimes, FINTRAC jurisdictions, and UK/EU regimes fit: the reporting node is jurisdiction-generic ("suspicious activity report to the national FIU in the locally mandated format").
- Automated dynamic risk rating is newer; older systems held static customer risk data — this confirms risk *records* belong in Level 0 while dynamic *rating engines* belong in Level 1.
- The definition survives the historical check.

## Uncertainties

- Exact alert-to-SAR stage counts, SLAs, and approval hierarchies vary by institution configuration; only the existence of configurable multi-stage review is well evidenced.
- Degree of CDD/EDD lifecycle depth varies (some platforms run full customer-lifecycle programs; others rely on KYC systems of record).
- Filing integration depth (direct e-filing vs report export for manual filing) was not verifiable per product from the reachable sources; only "generate and file"/"built-in support" vendor statements were observed.
- Agentic-AI auto-disposition is emerging; its regulatory acceptance is an open industry question and should not be written as settled behavior.

## Final Synthesis

An AML Platform is the institution-operated compliance system that (1) holds the monitored customer population with due-diligence context, (2) ingests the institution's real activity, (3) evaluates it with institution-configured detection (rules/scenarios/models) to generate alerts on potentially suspicious behavior, (4) routes alerts through a documented human investigation workflow with senior-compliance decision gates, and (5) produces the jurisdiction-appropriate suspicious-activity report as the terminal, auditable outcome. Everything else — screening, risk rating, network analytics, model governance, filing formats, fraud convergence, AI agents — is common structure or variant, not definition.
