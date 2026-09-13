# Research Notes — Supplier Risk Management

## Research Goal

Understand what a Supplier Risk Management application really is from real products: what the "risk" object is, how risk is evaluated per supplier, where risk signals come from, what happens after risk is detected (the disposition loop), how risk feeds procurement decisions, and where this Type ends and neighboring Types begin — especially Supplier Management Platform (§10 sibling), Third-party Risk Management (§11), Third-party Cyber Risk Platform (§15), Supplier Sustainability Management (§21), and Supplier Quality Management (§16).

This pass also discharges the joint-review flag pre-held by the supplier-management-platform pass (2026-09-08): enterprise suites package supplier risk as a solution inside the supplier-management family (SAP Ariba Supplier Risk sits within SAP Ariba Supplier Management; JAGGAER ships risk as a pillar of its Supplier Management page) while the directory carries separate leaves.

## Initial Boundary

Hypothesis before research: the buying organization's procurement-side system for evaluating and managing the risk its suppliers pose — due diligence before selection/onboarding, continuous monitoring of the supplier base, and risk-driven disposition (mitigation/remediation) feeding procurement decisions. Nearest neighbors:

- Supplier Management Platform (§10 sibling; supplier lifecycle/record as centered object)
- Third-party Risk Management (§11; GRC-side, any third party)
- Third-party Cyber Risk Platform (§15; cyber-only lens)
- Supplier Sustainability Management (§21; ESG lens)
- Supplier Quality Management (§16; quality lens)
- Supply Chain Planning / TMS / Global Trade Management (plan and execute, not risk)
- Business Continuity Management (§10; org's own continuity)
- Credit Risk Platform (§08; FI lending exposure machinery)
- Government Vendor Management (§24; registry/eligibility emphasis)
- supplier risk data/intelligence services (feed-only shapes)

## Research Questions

1. What is the "risk" object — is there a per-supplier risk record/score/standing?
2. When does risk enter: pre-transaction due diligence, and/or continuous monitoring of existing suppliers?
3. What risk domains do products cover (financial, operational, ESG/social, regulatory/legal, cyber, geopolitical, catastrophic)?
4. Where do risk signals come from (external data/news, questionnaires, supplier-provided assessments, buyer-side business-criticality inputs)?
5. What happens after risk is detected — is there a disposition/mitigation workflow (alert → triage → action plan → corrective action → closure, with oversight)?
6. How does risk standing feed procurement decisions (supplier selection, onboarding, contracting, retention)?
7. Who uses it and what interfaces do they work in?
8. Boundary: vs Supplier Management Platform, Third-party Risk Management, Third-party Cyber Risk, Supplier Sustainability, Supplier Quality, and supply-chain planning/logistics Types?

## Representative Products

| Product | Pole | Tier reached | Customer tier |
|---|---|---|---|
| SAP Ariba Supplier Risk | enterprise S2P suite module (risk solution inside Supplier Management family) | Tier 2 (official product page + FAQ) | enterprise |
| Interos | standalone AI supply-chain/supplier risk platform (mapping + iScore) | Tier 2 (root + our-software pages) | large enterprise / government |
| Prewave | standalone supplier risk + sustainability due-diligence platform (monitoring-led) | Tier 2 (root + 2 platform pages) | large enterprise (manufacturing-heavy) |
| Sphera Supply Chain Risk Management (ex-Riskmethods; "Supplier 360 Intelligence") | standalone risk monitoring + due diligence + managed response services | Tier 2 (official solution overview page) | large enterprise |
| Everstream Analytics | standalone supply-chain risk intelligence (mapping, monitoring, scorecards, insights-to-action) | Tier 2 (root page) | large enterprise |

Cross-referenced evidence (recorded in the sibling pass, 2026-09-08): JAGGAER ships risk as a pillar of Supplier Management ("advanced risk models to assess factors such as financial stability and geographic risks"); Avetta frames itself as "Contractor Risk Management" with qualification/compliance machinery. Coupa, Ivalua, OneTrust, ProcessUnity, Prevalent not sampled (unreachable in prior passes / TPRM-side products kept for that leaf).

Deliberately different philosophies: suite module (1) vs standalone monitoring-led (2) vs due-diligence-led (1) vs network-mapping-led (1) vs managed-response-flavored (1). Market category naming verified twice: Prewave and Everstream both announce leadership positions in the Gartner Magic Quadrant for Supplier Risk Management Solutions (2026), and Everstream cites Gartner Critical Capabilities for Supplier Risk Management Solutions — "supplier risk management" is an established analyst category, not just a directory label.

## Sources

- SAP — SAP Ariba Supplier Risk product page: https://www.sap.com/products/spend-management/supplier-risk.html (fetched 2026-09-08)
- Interos — root: https://www.interos.ai/ (fetched 2026-09-08)
- Interos — Our Software: https://www.interos.ai/our-software (fetched 2026-09-08)
- Prewave — root: https://www.prewave.com/ (fetched 2026-09-08)
- Prewave — Platform / Monitoring & Alerting: https://www.prewave.com/platform/monitoring-and-alerting (fetched 2026-09-08)
- Prewave — Platform / Actions and Partners: https://www.prewave.com/platform/actions-and-partners (fetched 2026-09-08)
- Sphera — Supplier 360 Intelligence (Supply Chain Risk Management solution overview): https://www.sphera.com/supply-chain-risk-management/ (redirects to /solutions/supply-chain-risk-management/supplier-intelligence-solution/) (fetched 2026-09-08)
- Everstream Analytics — root: https://www.everstream.ai/ (fetched 2026-09-08)
- Sibling-pass evidence (recorded 2026-09-08, research/supplier-management-platform.md): SAP Ariba Supplier Management page, JAGGAER Supplier Management page, Avetta root, Precoro help center (risk/performance absent at that pole)

Failed/abandoned: none this pass (all fetches succeeded). No Tier-1 help-center documentation reached for any sampled product — all evidence is product/solution-page level (Tier 2). Precision implications recorded under Uncertainties.

## Product Observations

### SAP Ariba Supplier Risk (evidence layer A, Tier 2)

- Positioning: "With risk due diligence in your source-to-pay process, you can mitigate disruption while protecting revenue and reputation."
- Solution capabilities (bulleted): "Risk due diligence assessments about targeted suppliers in your supply base"; "Proactive risk monitoring and alerts plus ongoing compliance checks"; "Collaborative risk disposition and remediation to mitigate risk impact"; cloud-based deployment.
- Key features organized in three groups:
  - **Assessment**: "Conduct intelligent control assessments based on suppliers' inherent risk"; "Calculate exposure to risks based on your relationships, with due diligence based on your supplier engagement"; "Identify suppliers of greatest concern by applying filters to data from more than 600,000 public and private sources."
  - **Mitigation**: "Generate and execute issue management and action plans to proactively mitigate risks while working with team members on risk-disposition workflow actions"; "Connect the supplier risk solution to your source-to-pay process to improve compliance"; "Identify where forced labor may exist in your supply chain."
  - **Monitoring**: "Receive personalized risk alerts through automatic tracking of more than 200 risk incidents"; "Monitor financial, operational, environmental, social, regulatory, and legal risks proactively"; "Track special handling needs or problems that require remediation or exceptions from company policy."
- Key benefits: insight into "the location of at-risk suppliers, the problems they face or will likely face, and the orders and shipments impacted by risk"; "third-party risk assessments for each supplier engagement while reducing the assessment cycle time"; "responsible plans for supplier selection, onboarding, and contracting."
- FAQ defines the domain: "Supply risk, or supplier risk, is any risk created by the processes and decisions of a supplier that could negatively impact your company." Four primary dimensions named: **financial, operational, environmental and social, regulatory and legal**. "What is supplier risk management?" — "the process of evaluating supplier risk and managing it throughout the entire supplier lifecycle and all procurement processes."
- Regulatory tie-in: dedicated LkSG (German Supply Chain Due Diligence Act) compliance cross-link.

### Interos (evidence layer A, Tier 2)

- Positioning: "Supply Chain Risk Management... Uncover and rank supply chain risks, so you can address them before they become CEO-level problems"; "automated supplier resilience platform... map and monitor supply chains at scale."
- **iScore®**: "AI-powered score of extended supply chains against multiple risk factors using thousands of proprietary data points. It detects hidden ESG, Cyber, Financial, Restrictions, Geopolitical, Catastrophic and other vulnerabilities to pre-empt risk and stop disruption." Benchmarking within industry.
- Three functional pillars (Our Software page): **Due Diligence** ("risk-forward approach to supplier selection and onboarding. Pre-screen for weaknesses, compare short-listed suppliers, and identify risk negotiation and contracting topics"), **Continuous Monitoring** ("Expand risk monitoring to more suppliers with automated scalability. Assess risk from 6 different domains (and dozens of subfactors + hundreds of attributes)"), **Executive Reporting** ("on-demand supply chain risk intelligence, performance and recommendations to the Board, C-Suite, Investors").
- Six risk domains enumerated: Finance (insolvency/default/liquidity), Cyber (ransomware, data leakage, vulnerabilities), Restrictions (restricted/prohibited company lists — UFLPA, Section 889; disclosure rules — GSCA, DORA, SEC), Geopolitical (decoupling, unrest, specific conflicts), Catastrophic (hurricanes/earthquakes/pandemic), ESG (forced labor, environmental impacts, concentration, bad behavior).
- Knowledge-graph substrate: "continuously map and monitor 250 million+ companies and billions of relationships"; multi-tier mapping ("five layers deeper"); sub-tier disruption detection ("Quickly evaluate huge quantities of suppliers to detect those impacted by cyber-attacks including MOVEit, Log4j, SolarWinds").
- Consumer-grade surface: "Look Up A Supplier" → supplier scorecard.
- Named audience: "procurement and risk leaders."

### Prewave (evidence layer A, Tier 2)

- Positioning: "AI-Powered Platform for Supply Chain Intelligence"; "Prewave simplifies millions of risk events, across languages and networks, into focused, actionable alerts for your business." Named a Leader in the 2026 Gartner Magic Quadrant for Supplier Risk Management Solutions; case study titled "Supplier Risk Management at Kärcher."
- Platform pillars: **Monitoring & Alerting**; **Scoping & Rapid Onboarding**; **Scoring**; **Integrations**; **Actions and Partners**; plus Tier-N (multi-tier) and a supplier-facing network ("For Suppliers").
- Monitoring & Alerting page: filters critical events from global/regional/local sources; multilingual analysis; risk categories "including ESG, financial risks, labour disputes, natural disasters, and more"; predictive analytics ("report on risk events in specific categories before they happen"); vendor claims of alert speed (60 minutes) and response-time reduction (Kärcher: 3 days faster, 40x manual effort cut) — marketing figures, not independently verified.
- Actions and Partners page (the disposition half):
  - Maturity Assessments ("in-depth reports on suppliers – including certification and declarations")
  - Supplier Security Assessments
  - Integrated Scorecard ("comprehensive supplier performance via our integrated 360-degree scorecard")
  - Streamlined Reporting ("one-click integrated reporting system" for compliance and monitoring)
  - "Prewave Funnel Methodology: Prioritise High-Risk Suppliers"
  - "Risk Matrix: Right Actions, Right Suppliers, Right Time" (visual matrix of risk vs action)
  - "Supply Chain Risk Lifecycle: Turn Supply Chain Risks into Opportunities"
  - Take-action network: Action Consulting (GAP analyses, BAFA report checks), On-site Audits (bookable, e.g. TÜV SÜD), Desk Audits, Supplier Engagement (worker surveys assessing supplier conditions)
- Solutions span: Sustainability (Due Diligence, Product & Environmental Compliance, Forced Labour) and Resilience (Faster Time-To-Response, Proactive Resilience, Multi-Tier Management).

### Sphera Supply Chain Risk Management — Supplier 360 Intelligence (evidence layer A, Tier 2)

- Positioning: "Visibility, action, and resilience at every tier"; "Knowing about risk isn't enough – what matters is how you respond. Most organizations struggle to turn alerts into coordinated action... Sphera's solution provides continuous 360-degree monitoring and deep multi-tier visibility, linking AI-driven risk signals directly to pre-built mitigation workflows. With centralized dashboards, corrective action tracking, and enhanced supplier collaboration..."
- Product family: Supplier 360 Intelligence + Supplier Engagement (Supply Chain Due Diligence, SupplyScreen, Supplier PCF Calculator); services: Risk Response and Resolution Center, Compliance Incident Management, Impact Analyzer, N-Tier Intelligence, Risk Assessment, Risk Radar, Sub-Tier Visibility.
- Five-point value frame:
  1. "60-second supplier check — concise, AI-generated snapshot of financial, operational, structural, and reputational risks"
  2. "Latent + event risk monitoring — monitor evolving vulnerabilities and sudden disruptions in one integrated view"
  3. "Risk portfolio overview — scan your entire supplier base, spot concentrations, and identify priorities at scale"
  4. "Alerts into workflows — link AI-driven risk signals directly to structured response workflows"
  5. "Oversight & reporting — monitor progress in real time and maintain audit-ready documentation of every action"
- "85% of disruptions start beyond Tier 1" — vendor claim (not verified).
- Customer testimonials (Ypsomed, JLL, Signify, Dana) emphasize real-time global supplier information and transparency.

### Everstream Analytics (evidence layer A, Tier 2)

- Positioning: "Get ahead of supply chain disruption with risk intelligence... Alerts tailored to your supply chain turn that intelligence into measurable ROI." Named a Leader in the 2026 Gartner Magic Quadrant for Supplier Risk Management Solutions; ranked #1 in 3 of 4 use cases in the 2026 Gartner Critical Capabilities for Supplier Risk Management Solutions (vendor-cited).
- Platform products:
  - **Network Mapping** — "digital twin" of the supply chain to optimize resilience and predict risks
  - **Global Monitoring and Alerting** — "24/7 AI-driven, human-validated actionable alerts specific to your supply chain"
  - **Risk Assessment** — "Automated scorecards assess supplier vulnerability"; "Automated scores for today. Predictive scores for tomorrow. See where supplier risks are heading before they arrive."
  - **Sub-Tier Visibility** — "Map and monitor hidden sub-tier suppliers to eliminate blind spots in sourcing, compliance, and concentration risk."
  - **Insights-to-Action** — "Integrate risk intelligence into your planning, procurement, and logistics systems to turn insights into decisions."
- Solutions by team: Planning, Procurement, Logistics, Compliance, ESG & Sustainability. Case outcomes cited (Nissan: mitigation of impacts; Danone: sub-tier onboarding).

## Cross-product Comparison

| Structure | SAP Ariba Supplier Risk | Interos | Prewave | Sphera SCRM | Everstream |
|---|---|---|---|---|---|
| Risk anchored to the organization's own supplier base / prospective suppliers | ✓ ("targeted suppliers in your supply base") | ✓ (extended supply chain, per-supplier scorecards) | ✓ (scoped supplier network, 360 scorecard) | ✓ ("your entire supplier base") | ✓ (tailored to your supply chain) |
| Per-supplier risk evaluation → comparable measure/score | ✓ (inherent-risk control assessments; exposure by relationship) | ✓ (iScore across 6 domains) | ✓ (Scoring pillar; 360 scorecard) | ✓ (60-second supplier check; Risk Assessment) | ✓ (automated + predictive scorecards) |
| External signal ingestion (public/private sources, global news, lists) | ✓ (600,000+ sources claim; 200+ risk incidents tracked) | ✓ (knowledge graph, 250M+ companies) | ✓ (global/regional/local, multilingual) | ✓ (latent + event monitoring) | ✓ (24/7 monitoring, human-validated) |
| Pre-transaction due diligence (selection/onboarding) | ✓ (due diligence in source-to-pay; assessments per supplier engagement) | ✓ (pre-screen, compare shortlists, contract topics) | ✓ (Due Diligence solution; supplier assessments) | ✓ (Supply Chain Due Diligence solution) | — (not a named pillar; sourcing/compliance use cases named) |
| Continuous event monitoring → alerts | ✓ | ✓ | ✓ (core pillar) | ✓ (core pillar) | ✓ (core pillar) |
| Prioritization of the risky subset (portfolio view / funnel / matrix) | ✓ ("suppliers of greatest concern" filters) | ✓ (rank; benchmark) | ✓ (Funnel Methodology; Risk Matrix) | ✓ (portfolio overview; concentrations; priorities) | ✓ (predictive "where risks are heading") |
| Risk disposition/mitigation machinery (workflows, action plans, corrective actions) | ✓ ("issue management and action plans... risk-disposition workflow actions") | — (not evidenced on fetched pages) | ✓ (actions network: audits, consulting, engagement) | ✓ ("alerts into workflows"; corrective action tracking; Risk Response & Resolution Center) | partial (Insights-to-Action = integration into decision systems; outcome claims) |
| Supplier-facing participation (assessments, engagement, network) | partial (via SAP Business Network ecosystem) | — | ✓ (supplier network; worker surveys; maturity assessments) | ✓ ("supplier collaboration"; Supplier Engagement product) | — |
| Managed response services (analysts/audit partners) | — | — | ✓ (audit/consulting partner network) | ✓ (Risk Response and Resolution Center; human-validated alerts at Everstream) | partial (human validation) |
| Multi-tier / sub-tier network mapping | partial (location/shipment impact insight) | ✓ (core; "five layers deeper") | ✓ (Tier-N pillar) | ✓ (N-Tier Intelligence; Sub-Tier Visibility) | ✓ (core; Sub-Tier Visibility product) |
| Integration into procurement/execution systems | ✓ (source-to-pay connection) | — (not evidenced) | ✓ (Integrations pillar) | — (not evidenced on fetched page) | ✓ (Insights-to-Action into planning/procurement/logistics) |
| Governance/oversight reporting (board/audit posture) | ✓ (compliance emphasis) | ✓ (Executive Reporting pillar) | ✓ (one-click reporting) | ✓ (audit-ready documentation) | — (case-level outcomes only) |
| Regulatory due-diligence framing | ✓ (LkSG; forced labor) | ✓ (UFLPA, Section 889, GSCA, DORA, SEC as restriction domains) | ✓ (LkSG/BAFA; due diligence regime pages) | ✓ (compliance incident management) | ✓ (compliance team solution; risk-center regulatory pages) |

Reading: the first six rows are present in every product — that is the recognizable center of the Type. Rows below diverge: the disposition/mitigation machinery is explicit in SAP, Prewave, Sphera; thinner or integration-shaped at Interos and Everstream on the fetched pages (evidence limitation, not proof of absence). Multi-tier mapping is a pure-play signature, weak in the suite module. Supplier-facing participation is common but not universal. Regulatory framing is universal in vocabulary.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The supplier base as the risk-bearing subject.** Risk is anchored to the buying organization's own external supplier relationships (existing and prospective) — identified supplier records, often inherited from procurement systems, carry the risk view; the portfolio of those relationships is the standing monitoring subject. Remove → generic risk register, news monitoring, or financial-risk tooling with nothing procurement-anchored.
2. **Per-supplier risk evaluation producing a comparable risk standing.** Risk signals from defined external domains (financial, operational, environmental/social, regulatory/legal, cyber, geopolitical, catastrophic — the exact set varies) are combined with buyer-side inputs (due-diligence assessments, questionnaires, business-criticality/exposure) into an evaluative measure per supplier — score, level, or tier — that makes the risky subset prioritizable. Remove → a document collection or raw alert feed with no evaluation; nobody can say which suppliers are high-risk.
3. **The risk-driven action loop.** Evaluated and monitored risk converts into managed response: detection/alerts → triage/prioritization → mitigation and disposition (issue management, action plans, corrective-action tracking, audits, supplier engagement, or integration into procurement decisions such as selection, onboarding, contracting, retention) → tracked toward closure with governance/oversight evidence. Remove → risk intelligence/reporting only; the "management" half of the Type disappears.

Jointly-held is load-bearing:
- 1 alone = supplier list (Supplier Management Platform / vendor master territory, no risk lens)
- 2+3 without the buyer's own supplier base as subject = generic assessment machinery (GRC / third-party-risk territory)
- 1+2 without 3 = supplier risk intelligence/scorecard service (monitoring-only thin pole, below the Type)
- 1+3 without 2 = alert stream with no evaluation standard, no prioritization basis

### L1 — Common Mature Structure

- Continuous event monitoring at scale: AI/NLP pipelines over global/regional/local news and data sources, mapped to supplier identities and locations; personalized/tailored alerts.
- Multi-domain risk coverage: financial, operational, ESG/environmental/social, regulatory/legal/compliance, cyber, geopolitical, catastrophic — breadth is a selling point; no fixed canonical list.
- Portfolio-level risk views: heatmaps/rankings/concentration detection ("spot concentrations, identify priorities at scale").
- Pre-transaction due diligence: pre-screening candidates, comparing shortlisted suppliers, risk-informed negotiation/contracting topics; assessments triggered per engagement.
- Predictive scoring ("scores for tomorrow") alongside current standing.
- Executive/governance reporting; audit-ready documentation of actions.
- Integration into procurement/ERP/planning systems so risk standing reaches buying decisions.
- Supplier participation: questionnaires, self-assessments, evidence upload, corrective engagement (shape varies).
- Regulatory due-diligence regimes as first-class content (LkSG/CSDDD-class, UFLPA/Section 889-class, DORA/GSCA/SEC disclosure rules).

### L2 — Variant / Optional Structure

- Packaging: suite module inside a source-to-pay/supplier-management family (SAP) vs standalone platform (Interos, Prewave, Sphera, Everstream).
- Center-of-gravity poles: due-diligence-led (assessment cycles at onboarding) vs monitoring-led (event-first) vs network-mapping-led (sub-tier discovery as the core asset) vs response-led (managed services, bookable audits).
- Multi-tier/sub-tier network mapping depth (signature of pure-plays; suite modules often stop at Tier-1 supply base).
- Managed human services: vendor analysts validating alerts, response centers, partner audit/consulting networks.
- Industry flavors: automotive, electronics, aerospace/defense, federal government, energy, food (case-study evidence).
- Cyber-heavy or ESG-heavy emphasis drifting toward the adjacent §15/§21 Types.
- Supplier-side network products (suppliers register, complete assessments, book audits).

### L3 — Vendor-specific (research notes only)

- SAP: "risk-disposition workflow actions" branding; 600,000+ sources and 200+ risk incidents figures; LkSG solution cross-link; SAP Business Network ecosystem role.
- Interos: iScore® methodology branding; knowledge-graph "250 million+ companies / billions of relationships"; "five days sooner, five moves earlier, five layers deeper"; itracing/ireputation/itariffs named solutions; Resilience Watchtower®.
- Prewave: Funnel Methodology and Risk Matrix branding; "Supply Chain Risk Lifecycle" phrase; 60-minute alert claim; 200+ risk categories; 4.5M data points/day; 1.6M registered suppliers; Kärcher 3-days-faster/40x claims; TÜV SÜD/Taylor Wessing partner network; BAFA report checks.
- Sphera: Supplier 360 Intelligence / Risk Radar / Impact Analyzer / SupplyScreen product names; Risk Response and Resolution Center; "85% of disruptions start beyond Tier 1"; "60-second supplier check".
- Everstream: network "digital twin" phrasing; "human-validated" alert posture; Nissan/Danone case figures (7-figure cost avoidance, 90% mitigated, 60% categories onboarded — vendor-cited).

All vendor figures are marketing claims — recorded, not verified, not used in the final document.

## Rejected Findings

- **Continuous AI monitoring as definitional** — rejected: the historical base case (periodic re-review of critical suppliers) satisfies the core without it; also one sampled suite module leads with assessment/disposition rather than monitoring breadth. L1.
- **Multi-tier/sub-tier mapping as definitional** — rejected: absent from the suite module's core framing (which works on the supply base and order/shipment impact); a pure-play signature. L1/L2.
- **Specific risk-domain set as definitional** — rejected: SAP names four dimensions, Interos six domains, Prewave 200+ categories; only the existence of defined external risk domains is invariant, not any list. L0 leg 2 phrased accordingly.
- **Supplier-facing portal as definitional** — rejected: participation machinery is common but two sampled products evidence none on fetched pages. L1/L2.
- **Regulatory due-diligence machinery (LkSG/UFLPA) as definitional** — rejected: current-regime realizations of the due-diligence leg; era- and region-specific. L2.
- **"Supply chain risk" (network/disruption) vs "supplier risk" as separate Types** — rejected at this pass: every sampled product anchors risk to supplier relationships; the network-mapping pole is a variant of the same Type, not a different one. (If the directory ever wants a separate supply-chain-risk leaf, that is a taxonomy question — see Boundary Issues.)
- **Risk intelligence feeds (alerts tailored to a commodity/market, no buyer supplier base)** — below the Type: no anchored subject, no evaluation of the buyer's own suppliers. Not a product in this sample; recorded as the floor shape.

## Boundary Findings

- **vs Supplier Management Platform (§10 sibling)** — RESOLVED from this side; keep-both RATIFIED. Seam = centered object: SMP centers the supplier population's lifecycle and information standing (entry → qualification → in-life change → exit) with risk as one optional integration; SRM centers the risk lens (evaluate → monitor → disposition) over the supplier base, with lifecycle machinery absent or inherited. Evidence: standalone pure-play supplier-risk platforms exist as independent products and an analyst category ("Supplier Risk Management Solutions" MQ); the suite module is a separate solution inside the supplier-management family (SAP's own packaging); the mid-market SMP pole (Precoro, Tier-1 evidence) ships no risk machinery yet is recognizably supplier management. Suites bundle both — product packaging does not dissolve the seam. This discharges the supplier-management-platform pass's joint-review flag.
- **vs Third-party Risk Management (§11, unprocessed)** — the sharpest live seam. TPRM is GRC-side: any third party (service providers, vendors, partners, outsourcers), engagement/contract-centric assessment cycles (security, compliance, financial questionnaires at onboarding and renewal), risk acceptance governance. Supplier Risk Management is procurement-side: the supplier base as standing portfolio, continuous supply-market monitoring, disruption response, sourcing/onboarding integration. Convergence zone is real: Interos sells a "Third-Party Risk" solution beside its supply-chain-risk solutions; SAP's own feature list says "third-party risk assessments for each supplier engagement." Proposed seam for joint review when §11 is processed: subject universe + operating frame (buyer's supplier base + procurement/disruption loop vs third-party universe + GRC engagement cycle). Cyber-led TPRM products (SecurityScorecard-class) belong to §15 Third-party Cyber Risk.
- **vs Third-party Cyber Risk Platform (§15)** — clean: cyber-only lens with security-rating/attack-surface machinery; cyber is one domain among several here.
- **vs Supplier Sustainability Management (§21, unprocessed)** — ESG as the centered lens (ratings, audits, decarbonization programs, ESG reporting) vs ESG as one risk domain inside a broader lens. Overlap zone: due-diligence regimes (LkSG/CSDDD) and forced-labor monitoring are sold by both Prewave and Sphera alongside sustainability suites. Flag for joint review when that leaf is processed.
- **vs Supplier Quality Management (§16)** — quality lens (audits, PPAP, nonconformance/corrective action in production context) vs broad risk; audits appear here as mitigation instruments, not the quality record.
- **vs Supply Chain Planning / TMS / Logistics** — risk intelligence vs plan/execute optimization. Everstream's Insights-to-Action explicitly integrates INTO planning/procurement/logistics systems — integration is the seam; this Type does not own plans, orders, or shipments (SAP's "orders and shipments impacted by risk" insight is impact reporting, not execution).
- **vs Business Continuity Management (§10)** — BCM centers the organization's own continuity (BIAs, continuity plans, exercises); supplier risk supplies one external input to it.
- **vs Credit Risk Platform (§08)** — FI lending exposure machinery (obligors, PD/EAD/capital) vs procurement counterparties; supplier financial-health assessment borrows credit-report inputs but not the FI apparatus.
- **vs Government Vendor Management (§24)** — registry/eligibility standing of a government's vendor class vs risk evaluation and response over a buyer's supplier base.
- **vs supplier data services (Supplier.io posture)** — data foundation beneath both SMP and SRM; no risk evaluation or disposition loop → not this Type.
- **monitoring/intelligence-only feeds** — below the Type (rejected finding above): no supplier-anchored evaluation, no action loop.

## Historical / Market-Sample Check

Pre-software purchasing practice satisfies the core: a buyer reviewing critical suppliers for financial stability (credit reports, audited financial statements) before award; site audits and insurance/certification checks at qualification; risk-tiered approved-vendor lists; dual/multi-sourcing and buffer stock as mitigation for supplier failure; periodic re-review of critical suppliers; incident-driven escalation when a supplier stumbled. That is: supplier base as risk subject + evaluative judgment producing tiers + mitigation decisions feeding sourcing. No AI feeds, no sub-tier graphs, no cloud, no regulatory content engines in the core. Continuous monitoring, multi-tier mapping, and predictive scores are modern additions (L1), and named regulatory regimes are current realizations (L2). The definition does not depend on the current AI-monitoring packaging.

## Uncertainties

- No Tier-1 help-center documentation reached for any sampled product — all observations are product/solution-page level (Tier 2). Workflow mechanics inside the disposition loop (statuses, approval steps, closure semantics) are therefore asserted only at existence level ("disposition/mitigation machinery exists"), never at operation-detail level.
- Interos and Everstream disposition-loop depth is under-evidenced on fetched pages (monitoring/intelligence-first marketing); the action loop may exist behind login. Their L0 fit rests on the due-diligence + scorecard + tailored-alerts + decision-integration evidence that is visible.
- Whether every product carries a formal per-supplier risk *record* with history (vs computed views) is not verifiable at Tier 2 — the final document says "risk standing," not "risk record lifecycle."
- Vendor figures (60 minutes, 200+ categories, 600,000 sources, 250M+ companies, 85%, 1.6M suppliers) are unverified marketing claims.
- Coupa, Ivalua, Zycus (suite risk modules) and OneTrust/ProcessUnity/Prevalent/SecurityScorecard (TPRM pole) not sampled; the TPRM seam is drawn from structure, not from a §11-side product study.

## Final Synthesis

A Supplier Risk Management application is the buying organization's risk-side system over its supplier base. Its defining core is three jointly-held structures: the supplier base as the risk-bearing subject (identified supplier relationships, existing and prospective, held as the standing monitoring portfolio); per-supplier risk evaluation producing a comparable risk standing (external risk signals across defined domains combined with buyer-side due diligence and business-criticality, into scores/levels that make the risky subset prioritizable); and the risk-driven action loop (alerts → prioritization → mitigation/disposition — action plans, corrective actions, audits, supplier engagement — tracked with oversight, feeding procurement decisions on selection, onboarding, contracting, and retention). Around that core, mature products add continuous AI event monitoring, multi-domain coverage, multi-tier network mapping, predictive scoring, supplier participation channels, managed response services, governance reporting, and procurement-system integration. The Type's center is the risk lens over the supplier population — Supplier Management centers the population's lifecycle and records, Third-party Risk Management centers the GRC engagement cycle over any third party, Supplier Sustainability centers the ESG lens, Supplier Quality centers the quality lens, and planning/logistics systems own what risk information flows into.
