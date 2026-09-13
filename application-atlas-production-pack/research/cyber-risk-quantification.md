# Research Notes — Cyber Risk Quantification

Research date: 2026-09-07
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a Cyber Risk Quantification (CRQ) application actually is as a software Type: what objects and quantities it manages, how a quantification is produced and used, which capabilities are definitional vs common vs optional, and where its boundaries lie against neighboring security, risk, and GRC types.

## Initial Boundary Hypothesis

- Hypothesis at start: CRQ is a security-risk-analyst/CISO-facing application that expresses cyber risk in probabilistic, monetary terms (scenario → loss event frequency × loss magnitude → distributions/exceedance curves), used for security investment prioritization, board/regulator reporting, risk appetite setting, and cyber insurance decisions.
- Nearest neighbors expected: Security Ratings Platform (external ordinal score), GRC / risk registers (qualitative risks with owners), Enterprise Risk Management (org-wide, all risk domains), Financial Risk Management Platform (market/credit risk — same math, different domain), Vulnerability Management (technical weakness enumeration), Threat Intelligence Platform (threat data supply), Breach & Attack Simulation (empirical testing), Security Program Management.
- Key boundary question: is CRQ distinguishable from a GRC risk register with numbers attached? Is it distinguishable from a security rating with a dollar figure attached? Both resolved below.

## Research Questions

1. What is a "risk scenario" in these products — what structure must it have?
2. What quantitative quantities are produced (frequency, magnitude, expected loss, tail loss, exceedance curves)?
3. What calculation substrate is used (FAIR/OpenFAIR, Monte Carlo, proprietary actuarial/insurance models, multi-model)?
4. What inputs feed the model (org profile, technology footprint, control maturity, telemetry, threat intel, insurance loss data, expert judgment)?
5. What workflows surround the numbers (scenario authoring, calibration, what-if/decision simulation, register management, board reporting, re-runs over time)?
6. Who are the users (analyst vs CISO vs board vs insurer vs PE)?
7. How does insurance interact (limits/deductibles vs loss distribution; policy optimization)?
8. Where are the boundaries vs ratings platforms, GRC, ERM, vulnerability management, BAS?

## Representative Products

Selection rationale: market representation + distinct product philosophies + distinct audience packaging. Three products documented directly, plus the FAIR methodology layer that anchors one whole product pole.

| Product | Philosophy / pole | Notes |
|---|---|---|
| Kovrr | Insurance-grade financial modeling; automated top-down + bottom-up register; portfolio & decision simulation | CRQ is its heritage line (now also sells AI governance) |
| SAFE (Safe Security) | "CRQ-native" continuous platform; telemetry ingestion + AI agents; FAIR/MITRE/NIST standards positioning | Forrester Wave CRQ Q2 2025 "Leader" per vendor |
| X-Analytics | Board/PE/consulting-facing "cyber risk intelligence"; financial exposure + treatment actions; MCP connectors to live security tools | anti-heat-map positioning, "defensible/explainable" |
| FAIR (FAIR Institute / Open Group Open FAIR) | Methodology substrate, not a product; anchors the expert-analysis pole of the market (RiskLens-class tools) | O-RT (taxonomy) + O-RA (analysis) standards |

Attempted but not reachable (see Source-access Limitation): RiskLens (risklens.com — transport failures; now part of Black Kite), Axio (axio.com 403; acquired by SecurityScorecard), C-Risk (cr-risk.com — transport failures). Safe Security subpages beyond the homepage returned 403.

## Sources

Fetched 2026-09-07 (all Layer A unless noted):

- Kovrr — CRQ Platform Overview: https://www.kovrr.com/cyber-risk-quantification
- Kovrr — Top-Down Scenarios: https://www.kovrr.com/cyber-risk-quantification/top-down-scenarios
- Kovrr — CRQ FAQ: https://www.kovrr.com/faq/cyber-risk-quantification
- SAFE (Safe Security) — homepage: https://safe.security/ (subpages 403)
- X-Analytics — homepage: https://www.x-analytics.com/
- FAIR Institute — What is FAIR: https://www.fairinstitute.org/what-is-fair
- FAIR Institute — Automating FAIR: https://www.fairinstitute.org/automating-fair

Source-access Limitation: the FAIR-workshop / expert-calibration product pole (RiskLens, C-Risk) and the program-assessment hybrid pole (Axio) could not be documented from their own product pages. Assertions about that pole are supported only by FAIR Institute methodology/automation pages (which describe the FAIR analysis practice its member products implement) and are marked accordingly (weaker: Layer B/methodology-level, not per-product Layer A). No product-specific UI/plan details were reconstructed from memory for these products.

## Product Observations

### Kovrr (Layer A — direct, three pages)

Platform positioning: "translates cyber risk into financial metrics that security and business leaders can act on … prioritize initiatives, justify investments, and report to leadership."

Onboarding arc (as marketed): Day 1 run first quantification and view modeled loss scenarios across the entity portfolio; outputs include **average annual loss, 1:100 tail risk, annual event likelihood**; identify event types, attack vectors, risk drivers. Day 14 build mitigation plan from control-level recommendations; simulate effect of investments/compliance/control upgrades; incorporate real-world incident intelligence into the cyber risk register. Day 28 boardroom-ready reports; compare modeled loss distributions against insurance coverage; track exposure over time via continuous control monitoring.

Platform modules (as named on the site):
- **Top-Down Scenarios** — macro-level exposure from minimal inputs; dozens of out-of-the-box scenarios (ransomware via phishing, data breach, credential theft, business interruption from third-party outages), each tied to real-world insurance coverage categories; tens of thousands of Monte Carlo simulations factoring industry, revenue, technology stack, security posture; outputs benchmarked against industry peers; every loss figure traceable to risk drivers (event types → impact scenarios → damage types); drill-down per event type or MITRE ATT&CK vector regenerates the full analysis for that one threat; full export of underlying simulation data; control ranking by financial impact of improving or failing, with expected loss reduction at average and 1:100 tail; controls breakable down by asset group; third-party contribution to exposure derived from mapped technology stack; **Quantifications History with changelog** (what moved: model version, security profile change, tech stack change), notifications, comparison across runs.
- **Cyber Risk Register (Bottom-Up Scenarios)** — define and quantify custom threat scenarios; track likelihood, impact, control recommendations, risk ownership in a centralized, continuously updated register; assign risk owners, define response plans, integrate with external workflow applications.
- **Portfolio Analysis** — quantify/compare exposure across a portfolio of entities; risk concentrations; correlation between entities; capital allocation.
- **Decision Simulator** — model financial impact of control improvements, security investments, compliance efforts before implementation; baseline vs simulated; return on security investment.
- **Insurance Data Insights** — map modeled exposure to coverage terms; evaluate limits, deductibles, sublimits, tower structures against quantified loss distributions.
- **Scenario Intelligence** — continuously updated database of real-world incidents, filtered by industry/country/revenue band; incidents mapped and added to the register in one click.
- **Continuous Control Monitoring (CCM)** — ingest live security signals from cloud/security infrastructure; as control posture changes, financial exposure recalculates automatically.
- **Cyber-Spheres / Asset Groups** — proprietary input granularity framework (e.g., employee endpoints split by country/region/operating group) reflected in more customized forecasts. (Vendor-specific.)

Modeling and data: multiple modeling technologies differentiating **systemic attacks, targeted attacks, and failures**; hundreds of thousands of simulated events; business-impact approach summarizing losses into **six categories aligned with standard insurance coverages**; calibrated against global data — threat intel feeds, proprietary cyber insurance claims data, vulnerability databases, risk event catalogs — plus internal company inputs (asset details, security control maturity). Control maturity per NIST CSF, CIS Controls, ISO informs quantification. **Loss exceedance curves** named explicitly. **Quantified materiality thresholds** (financial loss, data record compromise, outage time) supporting SEC cybersecurity disclosure, NIS2, DORA.

Anti-ratings positioning: "Security Scores Don't Tell the Full Story. Financial Impact Does."

### SAFE / Safe Security (Layer A — homepage only; subpages 403)

- Positions the **SAFE One Platform**; use cases listed under `/cyber-risk-quantification/` paths: **Board Reporting**, **Budget Justification**; additional product lines: Cyber Insurance, TPRM, CTEM; AI "co-workers" (SafeX, 100+ agents) ingest → reason → act.
- Three-stage architecture: **Ingest** (connect to systems defining "Business Context, Attack Surface, Controls, Threat Intelligence"; builds knowledge graph) → **Reason** (exposure, business impact, organizational context) → **Act** (investigate, prioritize, recommend, execute).
- Standards positioning: "Based on Open Standards: MITRE, The FAIR Institute, NIST."
- Customer stories (vendor claims, not independently verified): T-Mobile "75% faster cyber risk reporting", "1M+ digital assets continuously monitored"; Carvana "lowers breach risk by 40% while reducing insurance costs by 25%".
- Analyst positioning: Forrester Wave CRQ Q2 2025 Leader; vendor quotes the report calling it "the most comprehensive CRQ-native risk management solution in the market"; Gartner MQ Exposure Assessment Platforms Visionary — quote: "Safe's risk quantification features provide insights that are clearly differentiated from traditional vulnerability assessment technologies."

Interpretive note (marked): SAFE illustrates the **continuous-telemetry pole** of CRQ — quantification refreshed from live security signals rather than periodic assessments — but its own CRQ feature pages were unreachable, so detailed capability claims are not made here.

### X-Analytics (Layer A — homepage only)

- Self-description: "a Cyber Risk Intelligence Solution that **measures financial exposure to cyber risk and connects it to risk-reducing actions**."
- Use-case catalog: Vulnerability Prioritization, **Board & Executive Reporting**, Third-Party & Vendor Risk, "Putting the R in GRC", Mitigation Optimization / Investment Prioritization, M&A Due Diligence, **Insurance Optimization**, **Private Equity Portfolio**, CrowdStrike Configuration Intelligence.
- Live signals via **MCP connectors** (CrowdStrike Falcon first: coverage, detections, MITRE ATT&CK flow in automatically → "dollar-backed plan of the policy changes that reduce the most exposure"; ServiceNow/Tenable/WIZ listed as current/soon).
- Positioning: "Give your executives and board the answer, **not another heat map**"; "Patented, validated analytics: reliable, defensible, and explainable"; comprehensive profile "in minutes"; audiences: CISO & security leaders, Private Equity (one standard across portfolio companies), Consulting (embed into engagements).
- Resource titles confirm artifacts: "Data Breach Loss Curve: see the probability behind your largest loss category" (loss-curve output exists); "Effects of AI Adoption: calibrate your controls to the AI you have adopted".
- Numeric marketing stats (8 patents, 1,000+ enterprises, 10,000+ insurance policies informed annually, 35+ industry benchmarks) — vendor claims, not independently verified; not reused in canonical doc.

### FAIR methodology layer (Layer A for methodology; Layer B for the products that implement it)

- FAIR (Factor Analysis of Information Risk): international standard quantitative model for information security and operational risk (The Open Group standards **O-RT** risk taxonomy + **O-RA** risk analysis = Open FAIR); described as a Value-at-Risk model for cyber; explicitly contrasted with "qualitative color charts or numerical weighted scales".
- Model produces: **probable frequency of cyber events** and **probable magnitude of losses**, in financial terms; supports portfolio view of organizational risk; complements NIST/ISO/OCTAVE/ISACA frameworks which "prescribe the need to quantify risk" but leave computation open.
- **Automating FAIR** page (methodology-level evidence for the workflow of FAIR-based products):
  - Adoption barriers: staffing a dedicated analytics team with FAIR skills; scaling against changing threat landscape/telemetry floods; timeliness of "point-in-time" analyst assessments.
  - Ideal automated system: ingest threat data, actively monitor status of controls and assets at risk, pull latest loss data from industry statistics vendors and the org's own logs → **automated, on-demand FAIR analysis quantifying probable frequency and probable magnitude in dollar terms**.
  - Three must-haves: (1) **a clear scope of what's being measured** — assets at risk, relevant threats, type of event (outage, data compromise, fraud) that together form a **risk scenario**; mis-scoped scenarios fail the analysis; automated systems ideally pre-define scenarios to control for errors; (2) the FAIR model plus **FAIR-CAM** (controls analytics — how controls affect risk); (3) data aggregation across threat intel, vulnerability scans, SIEM, endpoints.
  - Benefits: ROI-based prioritization of security spending; material-risk reporting to board and regulators (SEC disclosure rule); tool consolidation.

## Cross-product Comparison

| Dimension | Kovrr | SAFE | X-Analytics | FAIR-practice pole (methodology-level) |
|---|---|---|---|---|
| Unit of analysis | Modeled loss scenarios (top-down library + bottom-up register) | Business context + attack surface + controls + threat intel (knowledge graph) feeding risk reasoning | Financial exposure of the enterprise + treatment actions | Explicitly scoped risk scenario (asset × threat × event type) |
| Quantities produced | AAL, 1:100 tail risk, event likelihood, LEC, driver decomposition | Financial exposure / risk quantification (details unreachable) | Financial exposure, loss curves per category, dollar-backed reduction plans | Probable loss event frequency + probable loss magnitude → dollar figures |
| Calculation substrate | Multi-model; systemic vs targeted vs failures; tens of thousands of Monte Carlo sims; insurance-loss calibration | Proprietary (FAIR/NIST/MITRE standards-based per vendor) | Patented/proprietary; "defensible, explainable" | Open FAIR (O-RT/O-RA) + Monte Carlo |
| Input mode | Minimal top-down (industry/revenue/stack/posture) + insurance claims + threat intel + vuln DBs + control maturity; optional CCM telemetry | Continuous ingestion from security stack; integrations marketplace | MCP connectors to live tools (EDR etc.); "no rip and replace" | Expert calibration + industry data + org logs (automation path described) |
| Decision workflow | Control ranking by financial impact; Decision Simulator (what-if, RoSI); insurance limits/deductibles vs loss distribution | Budget justification, board reporting; AI-recommended actions | Vulnerability prioritization in dollars; mitigation optimization; insurance optimization | ROI-based spending prioritization; materiality to board/regulators |
| Aggregate views | Entity portfolio with correlation/concentration; peer benchmarks | Enterprise view; benchmarks (details unreachable) | PE portfolio standard; industry benchmarks | Portfolio view of organizational risk |
| Time dimension | Quantification history + changelog; CCM auto-recalc; notifications | Continuous ("on loop") | Real-time as risk changes ("updated as your risk changes") | Historically point-in-time; automation drives continuous |
| Register/ownership | CRQ-powered cyber risk register: owners, response plans, workflow integration | Not directly observed | "Putting the R in GRC" | Risk register within FAIR programs |
| Regulatory use | Materiality thresholds vs SEC/NIS2/DORA; LEC for disclosure decisions | Compliance angle via platform (not directly observed) | Board/M&A use cases; compliance embed via consulting | SEC material risk reporting named as FAIR automation benefit |
| Audience packaging | CISO + risk managers + finance/compliance leaders | CISO, Cyber Risk Officer, TPRM leader | CISO, PE, consulting | Analyst + CISO + board |

## Canonical Model

### L0 — Defining Invariant

Two properties, deliberately minimal:

1. **Explicitly defined cyber risk scenarios** as the unit of analysis — a scenario binds a scope (assets / part of the organization / third party) to a threat event type (e.g., ransomware, data breach, business interruption) and its loss effect.
2. **Probability-weighted monetary exposure figures** produced per scenario by combining an estimate of loss-event frequency with an estimate of loss magnitude — yielding distributional financial outputs (expected/average annual loss, tail/percentile losses, event likelihood), not ordinal scores.

Remove the scenario structure → the product is telemetry, a ratings score, or a posture dashboard. Remove the probability × magnitude monetization → it is a qualitative GRC risk register or a heat map. With both, it is recognizably CRQ; with either missing, it is another Type.

### L1 — Common Mature Structure (cross-product commonality, not definitional)

- Simulation engine producing full loss distributions; **loss exceedance curve** as a signature output artifact; expected/average annual loss and tail-risk figures (1:100-style exceedance framings appear in the sample; exact recurrence conventions are vendor-specific).
- Scenario libraries / out-of-the-box scenario catalogs (ransomware, data breach, credential theft, third-party outage, etc.).
- Risk-driver decomposition: event types → attack vectors (MITRE ATT&CK mapping appears in sample) → damage/loss categories (aligned with insurance loss categories in at least one product; broader loss taxonomies in the methodology).
- Security-control layer: control maturity (NIST CSF / CIS / ISO framings) as a model input; control ranking by financial impact; **what-if / decision simulation** of control upgrades and investments with ROI/return-on-security-investment framing.
- Benchmark context: peer/industry comparisons.
- Insurance analytics: comparing modeled loss distributions against limits/deductibles/sublimits; policy optimization support.
- Third-party/supply-chain exposure as a contribution to overall financial exposure.
- Register workflow: scenario inventory with likelihood/impact, owners, response plans, status; integration with external workflow tools.
- Board/executive reporting surfaces; downloadable/exportable visuals and reports; materiality framing tied to regulatory definitions (SEC/NIS2/DORA named in sample).
- Time dimension: re-runnable quantifications with history/changelog; in newer products, continuous ingestion from security infrastructure with automatic recalculation.
- Data spine: org profile (industry, revenue, geography), technology footprint, control posture, threat intelligence, industry loss data / insurance claims, vulnerability data; increasingly live telemetry via connectors.

### L2 — Variant / Optional Structure

- Methodology substrate: Open FAIR-based vs proprietary actuarial/cat-model vs multi-model hybrids.
- Input mode: minimal top-down (org attributes only) vs bottom-up expert-calibrated scenario building vs continuous telemetry-driven.
- Audience packaging: analyst workbench (FAIR practitioners) vs board-report-first vs PE-portfolio vs consulting-embed vs insurer/underwriter-facing analytics.
- Multi-entity portfolio aggregation with correlation/concentration (group/PE/investor context).
- Managed/advisory CRQ programs (services-led delivery).
- Regulatory materiality analysis as a distinct module.
- AI agents / LLM assistants layered on quantification (present in newer products; depth varies).

### L3 — Vendor-specific (Research Notes only)

- Kovrr: Cyber-Spheres / Asset Groups input granularity; Scenario Intelligence with Kovrr Agent one-click register addition; six insurance-aligned loss categories; systemic/targeted/failure model differentiation; full simulation-data export.
- SAFE: SafeX AI co-worker swarm; knowledge-graph ingest-reason-act architecture; Forrester/Gartner positioning claims.
- X-Analytics: MCP connector architecture; ARIA AI assistant; patented analytics claims; CrowdStrike Falcon-specific workflow.
- FAIR Institute: FAIR-CAM (controls analytics), FAIR-MAM (materiality), FAIR-TAM extensions; FAIR-U workbook; O-RT/O-RA standards.

## Vendor-specific Findings

See L3 above; none promoted into the canonical model. Numeric marketing claims (customer outcomes, patent counts, enterprise counts, policy counts) were not carried into the application document.

## Boundary Findings

- **vs Security Ratings Platform**: ratings produce an external, ordinal, posture-based score (letter/number) for an organization or vendor. No scenario structure, no probability × magnitude, no loss distribution. CRQ consumes posture/control signals as model inputs; one sampled vendor explicitly positions against scores ("Security Scores Don't Tell the Full Story"). Remove monetized scenarios from CRQ and you approach a ratings product; that is the seam.
- **vs GRC / risk registers**: GRC risk registers hold risks with qualitative/ordinal ratings, owners, and treatments. CRQ's output is a probabilistic financial distribution per scenario. Convergence is real and vendor-driven ("CRQ-powered cyber risk register", "Putting the R in GRC") — flag for joint review with GRC-type leaves: the register *workflow* is shared machinery; the defining difference is the quantified probability×magnitude engine underneath. If you remove the quantification engine, a CRQ product degenerates into a GRC register — which is exactly why the engine, not the register, is in L0.
- **vs Enterprise Risk Management**: ERM aggregates all enterprise risk domains, typically ordinally; CRQ is cyber-domain-specific and probabilistic-monetized; CRQ output feeds ERM aggregation. Remove the cyber-specific scenario/loss domain → it is ERM/an operational-risk quantification, not CRQ.
- **vs Financial Risk Management Platform (market/credit/liquidity)**: same probabilistic toolkit (distributions, VaR-style tail figures), entirely different risk domain and data. Cyber risk's data problem (scarce firm-specific loss history) is what drives CRQ's distinctive inputs (technology footprint, control maturity, threat intel, insurance claims). Not the same Type.
- **vs Vulnerability Management**: enumerates and tracks technical weaknesses on assets. CRQ monetizes aggregate exposure at business level and may consume vulnerability data for prioritization (a sampled product offers "Vulnerability Prioritization" as a use case). Remove scenarios/finances → vulnerability management.
- **vs Breach & Attack Simulation / Security Validation**: empirically tests whether controls stop attacks; produces technical findings, not financial distributions. Complementary evidence source for CRQ inputs.
- **vs Threat Intelligence Platform**: supplies threat data; no loss modeling. CRQ is a consumer of TI.
- **vs Cyber Insurance (the product)**: CRQ informs limits/deductibles/policy structure; it does not underwrite, bind, or administer policies. One sampled product's insurance-analytics module sits on this seam.
- **"Remove-what" test**: remove probability×magnitude monetization → GRC risk register / heat map; remove scenario structure → security ratings / posture score; remove cyber domain → ERM or operational risk quantification; remove financial expression (keep frequencies) → technical risk measurement, not CRQ as marketed.

## Historical / Market-Sample Check

- The modern cloud platforms in the sample are telemetry-connected and benchmark-rich. Would an older/simpler product fit L0? Yes: spreadsheet-and-workshop FAIR analysis (the documented FAIR practice: scope a scenario, estimate frequency and magnitude ranges, Monte Carlo, annualized loss exposure and LEC) satisfies both L0 properties without connectors, AI, benchmarking, or continuous monitoring. The definition therefore does not over-fit the current automation-heavy generation. (§24 check passed at the abstraction level of "scenario + probabilistic monetization".)
- Insurer-side catastrophe modeling of cyber risk (a close cousin practiced within insurance) shares the math but serves underwriting portfolios rather than the insured organization's management loop; treated here as adjacent context, not a boundary failure.

## Uncertainties

1. FAIR-workshop product pole (RiskLens-class) documented only at methodology level; per-product workflow claims for that pole are not asserted in the final document.
2. SAFE's CRQ feature depth beyond its homepage is unobserved (403s); its continuous-ingestion characterization rests on homepage self-description plus analyst-report quotes.
3. Exact recurrence conventions for tail metrics (e.g., "1:100") vary by vendor and are reported here only as observed in one product; no market-wide convention is asserted.
4. The degree to which "CRQ platform" vs "CRQ module inside GRC/ERM suites" splits the market was not fully explored (Archer-class GRC quantification modules exist but were not sampled); the canonical model should hold for suite-embedded realizations, but this is an inference, not a sampled fact.
5. Market boundary drift: several sampled vendors are expanding into AI-governance/exposure-management packaging; the CRQ core described here is stable across that drift, but taxonomy neighbors (CTEM, Exposure Assessment Platforms) were not separately researched in this pass.

## Final Synthesis

A Cyber Risk Quantification application is the security-risk analysis application whose defining core is: **explicitly defined cyber risk scenarios analyzed into probability-weighted monetary exposure figures** — loss-event frequency × loss magnitude, computed (typically by Monte Carlo simulation over calibrated data) into distributional financial outputs such as expected annual loss, tail/exceedance losses, and event likelihood.

Around that core, mature products add: scenario libraries and a quantified risk register with owners and response plans; risk-driver decomposition (event types, attack vectors, damage categories); security-control maturity as a model input with control-level financial impact ranking and what-if decision simulation; peer benchmarking; insurance structure analysis against loss distributions; third-party exposure contribution; board/regulator reporting including quantified materiality; and re-runnable, increasingly continuous quantification with history. Methodology substrates vary (Open FAIR standard vs proprietary actuarial/multi-model approaches); input regimes vary (minimal top-down org profiling vs bottom-up expert calibration vs live telemetry ingestion); audience packaging varies (analyst workbench, board-first, PE portfolio, consulting, insurance).

Boundary summary: CRQ is distinguished from security ratings by scenario-based monetization instead of ordinal posture scoring; from GRC by the probabilistic financial engine beneath an otherwise shared register workflow; from ERM by domain specificity and probabilistic outputs; from vulnerability management and BAS by financial aggregation instead of technical enumeration/testing; and from financial-market risk platforms by its cyber risk domain and its distinctive data spine.
