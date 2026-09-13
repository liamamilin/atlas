# Research Notes — Climate Risk Management

Research date: 2026-09-07

## Research Goal

Understand what "Climate Risk Management" software actually is in the market: what object it manages, who operates it, how the climate risk process runs inside it, and where its boundaries lie against physical climate risk analytics, climate scenario analysis, enterprise risk management, ESG/sustainability platforms, climate adaptation planning, and climate data products.

## Initial Boundary (hypothesis before research)

- What: organization-side software running a climate risk process — identify climate-related risks (physical + transition), assess/quantify them against the organization's exposures, prioritize, decide/treat, monitor over time, and support disclosure (TCFD/ISSB-class frameworks).
- Users: corporate sustainability/risk/finance teams; financial institutions (banks, insurers, asset owners); infrastructure/real-asset owners; possibly municipalities.
- Most likely confusions: Physical Climate Risk Platform (hazard computation only), Climate Scenario Analysis (modeling machinery only), Enterprise Risk Management (generic register/controls without climate content), ESG Management/Reporting platforms (data/carbon/disclosure), Climate Adaptation Planning (plan-side counterpart, already processed), financial risk management platforms (FI-side market/credit/liquidity risk with climate as emerging variant).
- Unknowns: whether the Type is carried mainly by dedicated products or by suite modules; whether ERM-style register mechanics (owners, approvals, treatment plans) are part of the observed core; how the disclosure leg and the risk leg split between products.

## Research Questions

1. What is the central managed object — the exposure? the risk record? the assessment? the disclosure?
2. Which risk families does the software cover (physical acute/chronic, transition, nature)? Is dual coverage definitional?
3. How does climate evidence enter: embedded hazard models/scenarios, external data feeds, or frameworks as criteria?
4. What does an assessment output look like (scores, financial metrics, conformance verdicts)?
5. Does the product run a management loop (prioritization → response decisions → monitoring) or only produce analytics?
6. How does disclosure/regulatory alignment work (TCFD/ISSB/CSRD/EU Taxonomy/SEC)?
7. What delivery surfaces exist (interactive platform, API/data feeds, generated reports)?
8. Where does the Type dissolve into neighboring Types?

## Representative Products (sample rationale)

| Product | Pole | Philosophy | Customer level |
|---|---|---|---|
| Risilience (Riise platform) | corporate quantification + strategy | risk-first: financially-quantified physical+transition+nature analytics feeding strategy and transition planning | large corporates (F&B, fashion, retail, materials, automotive) + financial institutions |
| Jupiter Intelligence | FI-facing decision-grade physical risk analytics | data/decision-first: asset- and entity-level physical risk translated to credit/loss/cashflow metrics; adaptation ROI; model-governance posture | banks, insurers, asset managers, infrastructure/real estate (global) |
| XDI (Cross Dependency Initiative) | asset-portfolio physical risk workflow | workflow-first: screen → deep dive → report → stress test → resilience pathways | financial services, government, corporates, civil society (global) |
| Manifest Climate | disclosure-conformance assessment (pivot observed) | disclosure-first: AI assessment of climate disclosures against frameworks (CSRD/ISSB/TCFD/GRI...), gap analysis, benchmarking | public companies, asset managers/owners, advisors/auditors, NGOs, regulators |
| ISS STOXX Climate & Nature Analytics (sustglobal.com now redirects here) | investor-facing climate data & analytics | data-first: portfolio-level climate risk data covering physical, transition, net zero, biodiversity | institutional investors |

Boundary/context sources: TCFD Recommendations (fsb-tcfd.org — the market's process canon, disbanded 2023 with monitoring handed to IFRS Foundation); prior processed leaf climate-adaptation-planning (plan-side counterpart, with its own boundary row for this Type).

## Sources

All fetched 2026-09-07 (Layer A unless noted):

- Risilience — https://risilience.com/ (root: positioning, Quantify/Strategize/Deliver, client quotes from annual reports)
- Risilience — https://risilience.com/product-overview/ (platform benefits: Risk Screening, Transition/Physical/Nature Risk, Digital Twin, Financial Quantification, Transition & Mitigation Planning, RiiseIQ, Business Unit Analysis)
- XDI — https://xdi.systems/ (solutions: assess/deep dive/reporting/stress test/resilience/APIs; Climate Risk Hub; sectors; use cases)
- Jupiter Intelligence — https://www.jupiterintel.com/ (positioning, ClimateScore Global capability list, product family, resilience journey Assess→Evaluate→Decide)
- Manifest Climate — https://www.manifestclimate.com/ (AI assessment workflow: entities → documents → methodology → engine → conformance/evidence/gap/benchmark/trend; roll-ups; use cases)
- ISS STOXX — https://www.sustglobal.com/ (redirects to ISS STOXX Climate & Nature Analytics: carbon footprinting, physical risk data & analytics, transition risks, scenario alignment/temperature score, net zero, biodiversity)
- TCFD — https://www.fsb-tcfd.org/recommendations/ (four pillars: governance, strategy, risk management, metrics & targets; scenario analysis guidance; disbandment notice and IFRS Foundation handover)

Sourcing limitation: deep help-center / user-manual documentation was not reachable in this pass; evidence comes from official product surfaces plus one official framework portal. Per evidence rules: no precise numeric claims (counts, horizons, limits, defaults) are made in the final document; cross-product findings are stated at commonality strength; single-product observations remain product-specific.

## Product Observations

### Risilience (Riise platform) — Evidence layer A (direct, official pages ×2)

- Positioning: "Climate and Nature Risk is Business Risk"; the Riise platform "delivers financially-quantified analytics to turn risk into business opportunity." Named key vendor in a climate financial data & analytics buyer's guide (Verdantix, named on page).
- Loop: **Quantify → Strategize → Deliver**. Quantify: integrated views of climate-and-nature risks/opportunities; quantify potential financial impacts on earnings, operating costs, long-term business value. Strategize: financially costed "what if" scenario analysis. Deliver: prioritize initiatives based on cost, risk exposure and ROI; "track progress against targets, ensuring ongoing alignment with financial and sustainability goals."
- Risk coverage through "a single analytical lens": Transition Risk (NGFS-aligned climate pathways; policy, technology, legal, reputational, investor/consumer preference shifts), Physical Risk (acute and chronic hazards; business interruption, infrastructure impairment, supply constraints; probability distributions for event return periods, disruption levels, recovery timelines, damages), Nature Risk (TNFD-aligned, double materiality — impact on and dependency on nature).
- Digital twin: maps the commercial and physical structure of the company across operations, supply chains, customer segments; shows how environmental risks spread through the business; unified analytical view of exposure. Business Unit Analysis extends the twin to sub-entities/brands/assets.
- Financial quantification: scenario modelling across climate pathways (interest rates, inflation, carbon pricing, sectoral demand shifts); stress testing of low-probability/high-impact events (sudden regulatory changes, climate disasters) affecting asset valuations and business continuity.
- Transition & mitigation planning: identify/assess/refine emissions-reduction initiatives optimizing climate impact, risk mitigation and ROI; plans costed and stress-tested under multiple scenarios; shared data environment for cross-functional buy-in.
- RiiseIQ: AI-native layer to interrogate model results in plain language, understand methodologies, explore follow-on questions.
- Disclosure: "Reporting and Disclosure" solution — meet reporting commitments across multiple jurisdictions and standards. Customer evidence: scenario-analysis narratives embedded in corporate annual reports (fashion, consumer goods) and a bank piloting an earnings-value-at-risk model built with the vendor.

### Jupiter Intelligence — Evidence layer A (direct, official root page)

- Positioning: "Decision-grade risk intelligence for financial institutions. Translate physical risk into capital advantage." "Climate risk is capital risk."
- Core engine: ClimateScore Global — asset-level, multi-peril projections with scenario steps and long-term horizons (now to 2100); "22k+ data values per location"; scenarios in 5-year increments; damage & loss modeling; portfolio & asset level assessment; stress testing (credit, portfolio & operational risk); economic impact data; entity modeling; regulatory disclosure & compliance; adaptation planning & ROI. (Numeric specifics = product-specific; kept out of final doc.)
- Financial translation: "Financial translation to credit, loss, and cashflow metrics your teams use"; outputs designed to "clear MRM" (model risk management) and "support regulatory reviews" — transparent, auditable methods; "MRM-approved by Tier 1 banks" claim.
- Management framing: "The resilience journey: **Assess** your exposure → **Evaluate** business impact → **Decide** what to do"; "assess how risks evolve over time"; "model decisions, not just exposure."
- Product family on the engine: RiskSignal, Adaptation Hub, Compliance Hub, MRM Accelerator, Entity Modeling, MetricEngine, Site Intelligence.
- Critique of the market, in the vendor's own words: most physical risk data is "disclosure-first and decision-light"; opaque outputs don't clear model risk management; metrics without cashflow impact don't move boardrooms.
- Customers: banks (3 of 5 largest US banks claimed), energy/power producers, insurers, infrastructure, real estate.

### XDI — Evidence layer A (direct, official root page; second pass)

- Positioning: "The Physical Climate Risk Experts" since 2007; "XDI quantifies the cost of extreme weather and climate change impacts to physical assets." Analyzes assets in 175+ countries (claim).
- Solution ladder (the journey): Screen for assets most-at-risk (high-level overview across multiple assets) → Asset-level deep dive ("manage and reduce risk"; results "specific, traceable and assurable," traceable to point of failure within assets/components) → Meet reporting requirements (standardised reports aligned with TCFD, ISSB, EU Taxonomy; also CSRD and SEC named) → Stress test (aggregate asset-level analysis to portfolio insights across asset classes and scenarios including RCPs, SSPs, NGFS) → Engage clients on a pathway to resilience (explore forward-looking projections, risk-reduction and adaptation opportunities; adaptation pathways with cost-benefit) → Delivered the way you want (Climate Risk Hub platform, API into own systems, off-the-shelf reports, visualisation tools).
- Platform: XDI Climate Risk Hub — on-demand physical climate risk analysis from single asset to portfolios of tens of thousands; ISO27001 compliance claim.
- Powered by the Climate Risk Engines: sub-asset level data + climate, hazard and engineering data.
- Sectors: financial services (stress testing, central-bank mandated exercises, lending portfolios), government, corporates, civil society.
- Critical boundary note (consistent with prior adaptation-planning research): no managed plan object, no action records with owners/status — outputs are analyses and decision support feeding external plans.

### Manifest Climate — Evidence layer A (direct, official root page; positioning pivot observed)

- Current positioning: "The trusted AI engine for sustainability assessments." Not framed as climate risk management; framed as AI-powered assessment of sustainability/climate disclosures.
- Workflow: apply your methodology across any number of entities and documents (sustainability reports, annual reports & filings, policies & strategy docs) → AI Assessment Engine → outputs: conformance (met / not met, datapoint by datapoint), evidence (verbatim quotes with page-level citations), gap analysis (where disclosure falls short), benchmark (side by side against peers/sector), trend (progress tracked year over year). Roll-ups at two levels: datapoint → topic → framework, and company → sector → portfolio.
- Methodologies supported: custom methodology, CSRD, ISSB, TCFD, GRI, OSFI, SB 261 "and more."
- Use cases: benchmarking, compliance, due diligence, gap analysis, portfolio monitoring, research, supplier assessment; audiences include advisors & auditors, asset managers & owners, NGOs, public companies, regulators.
- Enterprise posture: source-cited findings, audit trail, SOC 2 claim, speed claims (kept product-specific).
- Boundary reading: the managed object is **disclosure conformance against framework criteria**, not the organization's risk itself. This is the disclosure leg of climate risk management carried by an assessment engine — adjacent to ESG Disclosure Management rather than the risk-process core.

### ISS STOXX Climate & Nature Analytics (sustglobal.com redirect) — Evidence layer A; Product Mismatch noted

- sustglobal.com now resolves to ISS STOXX "Climate & Nature Analytics" — market-consolidation evidence (Sust Global heritage within ISS STOXX group).
- Offering: 1,000+ indicators claim; Carbon Footprinting (PCAF); GHG emission data (Scope 1/2/3, PCAF quality scores); Physical Risk Data & Analytics ("evaluates a company's climate risk exposure against recognized scenarios using footprinting, geospatial data and financials"; metrics at corporate, real asset, and portfolio level; geospatial asset database; scores, financial risk, operational risk, value-at-risk metrics); Transition Risks & Opportunities (carbon pricing, demand changes, operating costs/revenues, fossil reserves); Scenario Alignment Data & Temperature Score (25+ scenarios claim); Net Zero Solutions; Biodiversity Impact Assessment Tool (TNFD context).
- Audience: investors ("help investors manage climate and nature risks, meet regulations, build resilience").
- Boundary reading: portfolio climate *data and analytics* consumed in investor workflows — no organizational risk process loop (no treatment decisions on the investor's own exposures; the "exposure" is the investment portfolio, and the workflow is screening/engagement/regulatory data supply). Drifts toward data platform / stewardship tooling.

### TCFD Recommendations — Evidence layer A (official framework portal; process canon)

- Four thematic pillars structuring how organizations manage and disclose climate-related risk: **Governance** (board oversight; management's role in assessing and managing), **Strategy** (risks/opportunities identified over short/medium/long term; impacts on businesses, strategy, financial planning; resilience under different climate-related scenarios including a 2°C-or-lower scenario), **Risk Management** (processes for identifying and assessing; processes for managing; integration into overall risk management), **Metrics and Targets** (metrics used to assess and manage; Scope 1/2(/3) emissions; targets and performance).
- Scenario analysis guidance: scenarios are "hypothetical constructs and not designed to deliver precise outcomes or forecasts" — they let organizations consider how the future might look under certain trends/conditions.
- Status: TCFD disbanded October 2023, having fulfilled its remit; FSB asked the IFRS Foundation to take over monitoring of climate-related disclosures (ISSB/IFRS S2 is the successor regime). The four-pillar vocabulary persists in market products (ISSB, CSRD, and vendor methodology names observed above).
- This canon supplies the market's process vocabulary for the Type: identify → assess → manage → integrate into overall risk management → disclose, under governance.

## Cross-product Comparison

| Dimension | Risilience | Jupiter | XDI | Manifest Climate | ISS STOXX C&NA |
|---|---|---|---|---|---|
| Subject whose risk is managed | corporate (digital twin: operations, supply chains, segments, sub-entities) | FI portfolios and entities (loans, assets, counterparties) | asset portfolios (single asset → tens of thousands) | assessed organizations' disclosures | investor portfolios |
| Risk families | physical + transition + nature, one lens | physical-led (extreme weather, multi-peril) | physical-led | framework criteria (incl. physical & transition datapoints) | physical + transition + net zero + biodiversity |
| Evidence base | NGFS-aligned pathways; proprietary models (Cambridge risk-studies heritage) | ClimateScore-class hazard models, scenarios to long horizons | Climate Risk Engines: climate/hazard/engineering data | framework criteria + source documents | peer-reviewed climate models; geospatial + financial data |
| Assessment output | financial quantification (earnings, operating costs, business value) | credit, loss, cashflow metrics; damage & loss | asset-level risk/damage results, traceable to components | conformance verdicts + verbatim evidence + gaps | scores, financial/operational risk, VaR-class metrics |
| Scenario machinery | what-if scenario analysis; stress testing | scenario steps, stress tests (credit/portfolio/operational) | RCP/SSP/NGFS stress testing | n/a (frameworks are the methodology) | 25+ scenario models, temperature scores |
| Prioritization | initiatives by cost/risk/ROI | portfolio prioritization to target assets | screen → deep dive on most-at-risk | gap analysis (weakest datapoints) | screening/monitoring (investor workflow) |
| Response/treatment support | transition & mitigation planning; track progress vs targets | adaptation ROI modeling; capital-allocation decisions | adaptation pathways with cost-benefit | remediation implied but not claimed on fetched page | none org-side (engagement/stewardship instead) |
| Monitoring over time | track vs targets; re-run scenarios | how risks evolve; re-run | re-run analyses; pathway exploration | year-over-year trend | ongoing portfolio monitoring |
| Disclosure support | reporting & disclosure solution | compliance hub; regulatory disclosure | TCFD/ISSB/CSRD/EU Taxonomy/SEC-aligned reports | core function (conformance & gap analysis) | regulatory data/reports |
| Delivery surfaces | platform | engine + product family | hub platform + API + reports + visualizations | SaaS engine | data feeds + reporting tools |

### Stable commonalities (cross-product, layer B)

1. **A managed exposure population** — the risk-bearing "things" are identified and maintained in the system: assets, sites, business units/sub-entities, portfolio holdings, or assessed entities. Every product organizes analysis around such a population (corporate twin / lending portfolio / asset portfolio / entity set).
2. **Climate-anchored, scenario-based, forward-looking assessment** — exposures are assessed against climate hazards and/or transition drivers under named scenario families (NGFS/RCP/SSP-class) and time horizons; TCFD guidance explicitly frames scenarios as exploratory, not forecasts — vendors echo this posture.
3. **Assessment results as risk records** — per-exposure (and aggregated) results: scores and/or financial metrics (damage, loss, earnings, value, credit metrics) and/or conformance verdicts. Results are traceable/citable to method and source in mature products.
4. **The physical + transition frame** — the dominant market vocabulary (TCFD heritage). Physical-led and transition-led emphases both exist; dual coverage is common but not universal.
5. **Prioritization via screening → deep dive** — narrow the population to the most material exposures before detailed analysis.
6. **Decision support for response** — adaptation/mitigation/transition options evaluated for cost, benefit, ROI; decisions feed capital planning or strategy. Present in the process-carrying products; absent in pure data poles.
7. **Recurring cycles** — re-assessment as risks evolve, target/progress tracking, trend views, annual disclosure rhythms. Management is continuous, not one-shot.
8. **Disclosure & regulatory alignment** — TCFD/ISSB/CSRD/EU Taxonomy/SEC-class framework alignment is a standard capability across the sample (core function in one).
9. **Multi-surface delivery** — interactive platform + data/API feeds + generated reports; the same assessment content flows to different audiences (analysts, management, regulators).

### Product-specific / weaker-evidence observations

- Corporate digital-twin modeling of exposure structure: Risilience only → product-specific mechanism, not core.
- Model-governance/MRM posture (outputs designed to pass model risk management): Jupiter only in this sample → product-specific, though structurally implied for FI customers of others (e.g., central-bank stress-test use cases at XDI).
- AI query layer over results (RiiseIQ) and AI disclosure assessment (Manifest): two different AI postures → product-specific.
- Nature/biodiversity extension: Risilience (TNFD-aligned) and ISS STOXX → common direction, not definitional.
- Conformance assessment as the managed object: Manifest only → boundary evidence, not core.
- ERM-style register mechanics (risk owners, approval workflows, treatment-plan status tracking): **not directly observed** on any fetched page in this pass. The management loop is evidenced at decision-support strength (prioritize → decide → track progress → re-assess), not as full register/approval machinery. Keep register mechanics as unverified/common-in-adjacent-ERM expectation, not core.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Climate Risk Management software exists to run, for a managing organization, the climate risk loop:

```text
Managed exposure population
  (the organization's own identified assets / sites / business units /
   portfolio holdings / assessed entities)
        ↓ assessed against
Climate drivers under scenarios & horizons
  (physical hazards and/or transition drivers; NGFS/RCP/SSP-class
   scenario families; forward-looking, explicitly not forecasts)
        ↓ producing
Maintained climate risk assessments
  (per-exposure and aggregated results: ratings and/or financial
   metrics, traceable to method and data)
        ↓ feeding
Prioritization and response decisions
  (screen → deep dive on material exposures; evaluate options)
        ↓ sustained by
Recurring re-assessment / monitoring and reporting
  (risk picture kept alive over cycles; internal and
   framework-aligned disclosure outputs)
```

Three properties. Removal test:
- Remove the **managed exposure population** (analysis no longer bound to the organization's own exposures) → general climate hazard data/maps — a data product, not management software.
- Remove the **maintained assessment records** (no per-exposure risk results, only raw drivers) → climate data/analytics feeds — the Physical Climate Risk Platform / data pole.
- Remove the **management orientation** (no prioritization/decision support, no re-assessment cycles, no reporting continuity) → a one-shot assessment study or dataset — an artifact, not an application.

Historical / market-sample check: the definition holds for pre-current carriers — insurer catastrophe-risk workflows (exposure books assessed against hazard models), consultant-produced corporate climate assessments bound to an asset register, spreadsheet risk registers fed with scenario outputs. It does not require cloud delivery, embedded hazard engines, AI layers, or named framework certifications (all modern-market commonalities).

### L1 — Common Mature Structure

Very common in mature products, not required for recognition:

- dual physical + transition coverage (the TCFD-derived frame), with nature/TNFD as an emerging extension
- financial quantification (damage/loss, earnings impact, value/credit metrics)
- embedded or licensed scenario libraries and stress testing
- screening → deep-dive workflow over the exposure population
- framework-aligned reporting (TCFD/ISSB/CSRD/EU Taxonomy/SEC-class)
- dashboards for management/board; generated disclosure reports
- multi-surface delivery: platform + API/data feeds + report outputs
- collaboration across sustainability/risk/finance functions

### L2 — Variant / Optional Structure

- customer tier: corporate vs financial institution vs public/asset owner; FI tier adds model-governance posture (MRM-class approval) and portfolio aggregation
- risk-family emphasis: physical-led vs transition-led vs dual; nature extension
- assessment engine posture: embedded proprietary engine vs licensed/imported data vs framework-criteria methodology
- delivery: interactive platform vs API/data-first vs report-led service hybrid
- disclosure regime depth: voluntary TCFD-style vs regulated regimes (CSRD/SEC-class/jurisdiction-specific)
- AI posture: AI assessment of documents vs AI query over model results vs none
- ERM integration depth: decision-support-only vs feed into enterprise risk registers (mechanics not directly evidenced in this pass)

### L3 — Vendor-specific (kept out of the final document)

- Risilience: Riise platform/RiiseIQ naming, digital twin framing, Cambridge Centre for Risk Studies partnership, Business Unit Analysis, client annual-report citations, specific claims (50% of corporate earnings at risk in Paris-Aligned scenario etc.).
- Jupiter: ClimateScore Global engine, product family names (RiskSignal, Adaptation Hub, Compliance Hub, MRM Accelerator, Entity Modeling, MetricEngine, Site Intelligence), scenario step cadence, "22k+ data values" and market-share claims.
- XDI: Climate Risk Hub, Climate Risk Engines heritage, AdaptXDI-style pathway analysis, 175-country coverage and ISO27001 claims, reseller program.
- Manifest Climate: roll-up vocabulary (datapoint→topic→framework; company→sector→portfolio), methodology name list (OSFI, SB 261), speed/price claims, SOC 2 claim.
- ISS STOXX: indicator counts, PCAF/TNFD alignment specifics, temperature-score methodology, biodiversity metrics (PDF/MSA), 200-datapoint net-zero assessment.

## Rejected Findings (considered, not promoted)

- "Climate risk management always covers both physical and transition" — rejected: two of the strongest process-carrying products are physical-led; dual coverage is common but not definitional.
- "Always financial quantification" — rejected: conformance-verdict and rating outputs exist; financial translation is common, not invariant.
- "It is an ERM module: risk register + owners + approvals + treatment plans" — rejected as core: register/approval mechanics were not observed on fetched pages; the management loop is evidenced at prioritization/decision/monitoring strength. ERM-style machinery belongs to Enterprise Risk Management; integration is the seam, not the core.
- "Insurer catastrophe modeling is this Type" — rejected: cat modeling serves insurance pricing/reserving from hazard event models; organizational climate risk management serves the organization's own risk process. Different directory leaf territory (actuarial/cat-modeling side).
- "Investor portfolio climate data = this Type" — rejected: the ISS STOXX pole shows the investor-data variant dissolving into data/analytics products; the org-side risk process is what keeps the Type.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what makes it a different Type) |
|---|---|---|
| Physical Climate Risk Platform | overlapping engine | computes physical hazard exposure/loss (physical only; the engine); climate risk management runs the organizational risk process over maintained assessments and decisions, commonly spanning transition as well. Products blend; the process scope is the seam. |
| Climate Scenario Analysis | input machinery | produces scenario projections/model futures; no managed exposure population or risk records of its own; feeds this Type. |
| Enterprise Risk Management | adjacent generic process | manages any enterprise risk in register/control form without climate science content (hazards, scenarios, pathways). Climate risk management = the climate-specific content and assessment machinery; integration into ERM is the documented seam (TCFD pillar c). |
| ESG Management / Reporting / Disclosure platforms | adjacent domain suite | center on sustainability data, carbon accounting, and report production; climate risk management centers on risk assessment and treatment of exposures. Manifest's pivot shows the disclosure leg living beside the risk leg. |
| Climate Adaptation Planning | downstream counterpart (already processed) | adaptation planning holds the plan artifact (goals, actions, owners, public progress); climate risk management holds the risk assessments and decisions that justify/steer it. Risk platforms can test option cost-benefit; planning software governs the response program. |
| Financial Risk Management Platform | FI-side sibling | market/credit/liquidity risk on financial positions; climate enters it as an emerging risk type and via stress tests; org-side climate risk management is risk-family-specific (climate) and framework-driven. |
| Business Continuity Management | adjacent | operational response to disruption (procedures, recovery); climate risk management is the long-horizon risk assessment/steering layer. |
| Climate data products / stewardship data | drift boundary | when assessment records, decision support, and recurring cycles disappear, the product becomes a data/analytics feed (observed directly in the investor pole). |

Removal tests:
- Remove exposure binding → climate data/maps product.
- Remove maintained assessments → analytics/data platform.
- Remove decision/monitoring loop → one-shot study or disclosure checklist.
- Replace climate drivers with any enterprise risk → ERM.
- Replace risk records with plan/actions → climate adaptation planning.

## Uncertainties

1. Deep operational documentation (help centers, manuals) unreachable in this pass; workflow internals (exact assessment states, re-assessment cadence, permission models) stated at moderate strength only.
2. ERM-style register mechanics (owners/approvals/treatment plans) could not be verified for this Type; deliberately excluded from the core.
3. Whether suite-module delivery (GRC/ESG suites carrying climate risk modules) is a major carrier: Diligent's ESG page was found retired (redirect) and MetricStream unreachable — suite posture left as variant/uncertain.
4. Sust Global → ISS STOXX consolidation observed mid-research; investor-data pole labeled by current owner.
5. Manifest Climate's historical TCFD-gap-analysis positioning could not be verified from current official pages (pivot); treated cautiously.
6. FI-side climate risk via financial risk platforms (per financial-risk-management leaf notes) not directly sampled here.
7. Regional/regulatory-regime specialists (e.g., CSRD-first suites) not sampled.

## Final Synthesis

Climate Risk Management software is the organization-side system that keeps a climate risk process alive: it holds the organization's own exposures as a managed population, assesses them against climate hazards and transition drivers under scenario-based forward-looking views, maintains the resulting risk assessments as traceable records, uses them for prioritization and response decisions, and sustains the picture across recurring monitoring and reporting cycles, with framework-aligned disclosure as a standard output. The market's process canon (governance, strategy, risk management, metrics & targets) supplies the vocabulary; the physical+transition frame and financial quantification are common mature structure rather than definition; the assessment engine may live inside the product or beside it as a data/licensed-engine dependency. The Type dissolves into a data platform when exposure-bound assessment records disappear, into ERM when the climate content disappears, and into adaptation planning when risk records are replaced by a managed response plan.
