# Research Notes — Climate Scenario Analysis

## Research Goal

Understand what a "Climate Scenario Analysis" application actually is as a product category: what objects it manages, what machinery it runs, who uses it, and — critically, because three sibling leaves in §21 straddle the same products — how it is separated from **Climate Risk Management** (processed 2026-09-07), **Physical Climate Risk Platform** (unprocessed), and the climate-data-products neighborhood.

The sibling pass (research/climate-risk-management.md §Boundary Findings) recorded a working seam that this research must confirm or amend:

- physical-climate-risk-platform = physical-only hazard/loss computation engine side
- climate-scenario-analysis = scenario projection machinery without a managed exposure population
- climate-risk-management = the organizational risk loop (exposure population + maintained assessments + prioritization/decision/monitoring/disclosure cycles)

## Initial Boundary (hypothesis before research)

- Core use: model plausible climate futures under named scenarios and project their consequences for a defined subject (portfolio, assets, business, region), for strategy, stress testing, and disclosure support.
- Likely users: FI risk teams, investors, corporate sustainability/strategy, insurers, central-bank-exercise participants.
- Nearest confusions: Climate Risk Management (process loop), Physical Climate Risk Platform (engine), climate data/analytics products (static scores), ESG disclosure platforms (report production), financial risk stress-testing platforms (generic stress machinery), Energy Forecasting Platform (power-domain forecasting).
- Unknowns: does a distinct product category exist under this exact label, or is "scenario analysis" only a capability inside CRM/physical-risk products? Is there a scenario-led product with no exposure population at all?

## Research Questions

1. What is the canonical definition of climate scenario analysis in the framework canon (TCFD; NGFS as the scenario-design authority)?
2. What are scenario families and named pathways that products anchor to?
3. What machinery do products actually expose: scenario libraries, projection engines, subjects, horizons, outputs?
4. What subjects do products bind scenarios to (portfolios / assets / corporates / regions)?
5. Which products carry a *managed exposure population + risk-management loop* (→ CRM) and which carry *only scenario machinery* (→ this Type)?
6. How do products deliver results (platform, data feed, reports) and what comparison/posture do they expose across scenarios?
7. Where do scenario-analysis products drift into climate data products or disclosure products?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| Jupiter Intelligence | FI-grade proprietary physical-risk engine, model-governance posture | strongest engine-side scenario machinery; FI customer tier; MRM defensibility framing |
| XDI (Cross Dependency Initiative) | asset-portfolio physical risk, engineering-based, stress-testing | explicit RCP/SSP/NGFS scenario vocabulary; regulator stress-test use case; platform+API+reports delivery |
| Risilience (Riise) | corporate strategy-led, financially quantified scenario analysis | transition+physical "single lens"; corporate tier; consultancy-heritage quantification |
| MSCI Climate (Climate Scenario Analysis product) | investor data-platform pole; product literally named "Climate Scenario Analysis" | NGFS/IPCC-anchored scenario metrics at portfolio scale; data-provider philosophy |
| Carbon4 Finance | boundary sample | FI data provider (footprints, alignment, hazard scores) — shows where scenario machinery is *absent* (current-state data), anchoring the drift boundary |

Framework authorities (not products, but the type's vocabulary source):

- TCFD Recommendations (fsb-tcfd.org) — defines scenario analysis itself; TCFD disbanded 2023, IFRS Foundation took over monitoring.
- NGFS Scenarios Portal (ngfs.net) — central-bank scenario design authority; defines families, named pathways, model stack, and applications.

## Sources

Fetched 2026-09-07 (all Layer A unless noted):

- Jupiter Intelligence — https://www.jupiterintel.com/ (home; product family ClimateScore Global, RiskSignal, Adaptation Hub, Entity Modeling, MetricEngine, Compliance Hub, MRM Accelerator, Site Intelligence)
- XDI — https://xdi.systems/ (home; solutions ladder incl. /solutions/stress-test, /solutions/resilience; banking stress-testing use case)
- Risilience — https://risilience.com/ (home; product module URLs incl. /product-overview/financially-quantified-scenario-analysis/, /product-overview/risk-screening/, digital twin, transition and mitigation planning; client-report quotes from Burberry, Reckitt, Nestlé, Barclays)
- MSCI — https://www.msci.com/data-and-analytics/climate-solutions (Climate Solutions; product card "Climate Scenario Analysis"; Physical Risk Solutions; GeoSpatial Asset Intelligence; Energy Transition Framework)
- Carbon4 Finance — https://carbon4finance.com/ (home; climate transition risks / physical risks / biodiversity solutions; regulatory use cases)
- NGFS Scenarios Portal — https://www.ngfs.net/ngfs-scenarios-portal/ (introduction page: families, named scenarios, model stack, applications, short-term scenarios, uncertainty caveats)
- TCFD — https://www.fsb-tcfd.org/recommendations/ (scenario analysis definition; strategy pillar 2°C-or-lower recommendation; IFRS handover note)

Abandoned sources (per network-limitation rule): Ortec Finance (2 URL failures — 404s; dropped; no memory-based claims substituted), S&P Global Sustainable1 (403 anti-bot). MSCI /our-solutions/climate-investing redirected to generic Sustainability Solutions page; the dedicated /data-and-analytics/climate-solutions page was fetched instead and is the cited source.

Sourcing limitation: as with the two sibling passes, deep help-center / user-manual documentation for the sampled products was not reachable in this pass; evidence is from official product pages and framework portals. Assertions below are calibrated accordingly; no precise operational claims in the final document.

## Product Observations

### Jupiter Intelligence (Layer A — direct observation of official site)

- Positioning: "decision-grade risk intelligence for financial institutions"; physical and extreme-weather risk translated into capital decisions; industries: banking/lending, asset management/PE, infrastructure/industrial, real estate/REITs.
- Engine/product family: **ClimateScore Global** described as the platform powering RiskSignal, Adaptation Hub, Entity Modeling, MetricEngine, Compliance Hub, MRM Accelerator, Site Intelligence.
- Scenario machinery observed (vendor-stated claims): "asset-level, multi-peril projections with scenario steps and long-term horizons"; "scenarios in 5-year increments"; "now to 2100 (50+ year horizon)"; "22k+ data values per location"; client quote: modeling "probable impacts of perils from extreme weather at hyperlocal resolution, based on different emissions scenarios."
- Output translation: "financial translation to credit, loss, and cashflow metrics"; damage & loss modeling; economic impact data; entity modeling; stress testing of "credit, portfolio & operational risk".
- Posture: "transparent, auditable methods that clear MRM and support regulatory reviews"; "trace every assumption; validate results against observed events; stress-test portfolios across transparent scenarios"; "MRM-approved by Tier 1 banks".
- Journey framing: Assess exposure → Evaluate business impact → Decide what to do; adaptation planning & ROI modeled.
- Overlap note: adaptation ROI + portfolio prioritization edge into CRM loop territory (see Boundary Findings).

### XDI (Layer A)

- Positioning: "the physical climate risk experts"; quantifies "the cost of extreme weather and climate change impacts to physical assets"; clients across financial services, government, corporates, civil society; assets analyzed in 175+ countries (vendor claim).
- Engine: powered by the **Climate Risk Engines** (engineering-based methods); outputs "traceable to the point of failure within individual assets" and components; "specific, traceable and assurable", "more than just a score".
- Solutions ladder (journey): Screen for assets most-at-risk → Asset-level deep dive → Meet reporting requirements (TCFD, ISSB, EU Taxonomy; CSRD/SEC in report framing) → **Stress test for climate risk** ("aggregate asset-level analysis to portfolio level insights across a range of asset classes and scenarios including RCPs, SSPs and NGFS") → Engage clients on a pathway to resilience ("explore varied forward-looking projections under different assumptions") → Delivered the way you want it (Climate Risk Hub platform, API data feed, off-the-shelf reports, visualization tools).
- Stress-test use case (banking): large-scale Monte Carlo simulations across global residential/commercial lending portfolios for a regulatory climate stress test, plus a deterministic scenario prescribed by the regulator.
- Overlap note: the screen→deep-dive ladder and reporting solutions are CRM-loop-shaped; scenario stress testing and projections-under-assumptions are this Type's machinery.

### Risilience (Riise platform) (Layer A)

- Positioning: "climate and nature risk is business risk"; financially-quantified analytics; corporate + financial-institution audiences (banks, PE, asset managers).
- Product modules observed in navigation: Product Overview; **Digital Twin**; **Risk Screening**; **Financial Quantification** (module URL slug literally "financially-quantified-scenario-analysis"); **Transition and Mitigation Planning**; RiiseIQ; Business Unit Analysis.
- Framing: "assesses both physical and transition risks through a single analytical lens"; Quantify → Strategize → Deliver.
- Client evidence of scenario-analysis practice built on the platform (vendor-published quotes): Burberry annual report "five-year scenario analysis"; Reckitt "underpinned by scenario analysis … quantitative analytics … built on research and frameworks pioneered by Cambridge Centre for Risk Studies"; Nestlé "scenario analysis allows us to better understand the impact of climate change … critical tool for strategic and financial planning and risk management"; Barclays piloting an "Earnings Value at Risk" model "by simulating 'what if' scenarios".
- Scenario family evidence: "Paris-Aligned (Net Zero) climate scenario" used in headline quantifications (e.g., earnings-at-risk over a 10-year period under that scenario; global average carbon price in 2030 under it — vendor-stated figures, kept out of final doc).
- Heritage: platform partner of the Cambridge Centre for Risk Studies (University of Cambridge).

### MSCI Climate Solutions (Layer A)

- The type label is a literal product name: **"Climate Scenario Analysis"** — "Quantify financial climate risks based on NGFS and IPCC scenarios with insights designed to help you manage portfolios, optimize performance and align with regulations."
- Broader climate suite context: Physical Risk Solutions (investors and banks); GeoSpatial Asset Intelligence (asset-location data; "4 million+ asset locations" vendor claim); Energy Transition Framework; Total Portfolio Footprinting; Carbon Markets; Nature & Biodiversity; Supply Chain Intelligence.
- Cross-cutting capability language: "monitor climate-related financial risks and investment resilience … using detailed insights under various risk scenarios and geospatial asset intelligence"; "climate data and metrics aligned with global frameworks and disclosure rules".
- Audience: investors, financial institutions, insurers, corporates, advisors; scale claims (top-50 asset-manager penetration) — vendor-stated, not carried to final doc.

### Carbon4 Finance (Layer A — boundary sample)

- FI environmental data provider: transition risk solution (verified carbon footprints, "dynamic assessment of transition performance", "portfolio alignment to the Paris Agreement"); physical risk solution ("assessing climate hazards and portfolio vulnerabilities"); biodiversity solution; regulatory reporting (CSRD, SFDR, CRR3/CRD6, French Energy-Climate Law).
- Use cases: portfolio steering, credit-process integration, customer-facing transparency features, "risk mitigation & reporting" (screening, dependency scores, risk scores).
- Boundary relevance: strong current-state scoring/data machinery, but no scenario-family projection machinery is presented on the fetched surface — the drifting pole toward "climate data products" rather than scenario analysis.

### NGFS Scenarios Portal (Layer A — framework authority)

- Scenario families: **Orderly** (early, gradually more stringent policies; both physical and transition risk relatively subdued), **Disorderly** (delayed or divergent policies; higher transition risk), **Hot house world** (insufficient policy action; severe physical risk including irreversible impacts), **Too little, too late** (late, uncoordinated transition fails to limit physical risk).
- Named scenario examples shown in the portal's matrix: Net Zero 2050, Low Demand, Delayed Transition, Below 2°C, NDCs, Fragmented World, Current Policies.
- Purpose framing: "The future is uncertain… a window into different plausible futures"; scenarios are "hypothetical"; "a common and up-to-date reference point" for how physical risk and transition risk "could evolve in different futures".
- Model stack (what scenario machinery is made of): transition pathways from Integrated Assessment Models; chronic climate impacts from Earth System Models + Climate Impact Models; acute climate impacts from Natural Catastrophe Models; macro-financial impacts from Global Macroeconomic Models. Multiple models per scenario to represent uncertainty.
- Documented applications: (1) "Scenario analysis and disclosure" — granular data "can enhance strategic thinking and form a key part of climate-related financial disclosures"; (2) strategy and policy alignment; (3) academic research.
- Horizon structure: long-term scenarios (version 5.0, Nov 2024) plus a first vintage of **short-term scenarios (three to five years)** published May 2025 for near-term shocks and financial-stress analysis.
- Data delivery: public explorers (NGFS IIASA Scenario Explorer for transition pathways/temperature/economic data; Climate Impact Explorer for climate impact data). Caveat posture: "care should be taken in using the results, particularly at the most granular levels".

### TCFD Recommendations (Layer A — framework authority)

- Definition: "Scenario analysis is a process for identifying and assessing the potential implications of a range of plausible future states under conditions of uncertainty. Scenarios are hypothetical constructs and not designed to deliver precise outcomes or forecasts."
- Strategy pillar recommended disclosure: describe "the resilience of the organization's strategy, taking into consideration different climate-related scenarios, including a 2°C or lower scenario."
- Four thematic pillars: governance, strategy, risk management, metrics and targets. Site documents TCFD's disbanding (Oct 2023) and handover of monitoring to the IFRS Foundation.

## Cross-product Comparison

| Dimension | Jupiter | XDI | Risilience | MSCI | Carbon4 (boundary) |
|---|---|---|---|---|---|
| Primary subject | FI portfolios, assets, entities | asset portfolios (debt/equity holders, governments, corporates) | corporate business + FI portfolios | investment portfolios / issuers | FI portfolios |
| Risk families | physical (peril-led) | physical | physical + transition ("single lens") | transition + physical | transition + physical + biodiversity (data-led) |
| Scenario vocabulary | emissions scenarios, scenario steps, long horizons | RCPs, SSPs, NGFS | Paris-Aligned (Net Zero) family; "what if" scenarios | NGFS and IPCC scenarios | none presented (current-state alignment/scores) |
| Projection machinery | proprietary global climate models + damage/loss + entity/economic modeling | Climate Risk Engines (engineering-based hazard→damage) | digital twin + financial quantification of scenario outcomes | scenario-based risk metrics over portfolio data | — (scores/footprints, not projections) |
| Stress testing | credit/portfolio/operational stress testing | Monte Carlo + regulator-prescribed deterministic scenarios | Earnings-VaR-style "what if" simulation (client-documented) | scenario-aligned metrics for regulatory alignment | — |
| Financial translation | credit, loss, cashflow metrics; adaptation ROI | asset damage/loss cost; portfolio cost of risk | financially quantified risk; earnings at risk | financial climate risk metrics | risk scores (financial framing lighter) |
| Comparison posture | scenario steps, stress-test across transparent scenarios | forward-looking projections "under different assumptions"; scenario range | scenario ranges across horizons (client reports) | insights "under various risk scenarios" | — |
| Disclosure alignment | regulatory disclosure & compliance product | TCFD/ISSB/EU Taxonomy/CSRD/SEC framing | reporting & disclosure solution | metrics aligned to frameworks and disclosure rules | CSRD/SFDR/CRR3 reporting |
| Delivery | platform family + data (MRM posture) | Climate Risk Hub platform + API + reports + visualization | platform + advisory services | data platform/feeds + indexes | data platform/feeds |
| Managed exposure population | assets/portfolios configured for analysis | assets/portfolios configured for analysis | corporate structure/business units | portfolio holdings via data | portfolio holdings via data |
| Risk-management loop (prioritization records, response decisions, monitoring cycles) | partial (adaptation ROI, prioritization language) | partial (screen→deep-dive, resilience pathway) | partial (transition planning module) | no | no |

## Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

1. **A managed scenario set.** Named climate scenarios — coherent, assumption-bearing descriptions of alternative futures (policy, emissions, temperature, technology pathways), commonly drawn from recognized public families — held by the application as selectable objects. Remove this → a forward projection/forecast tool or a hazard model, not scenario analysis.
2. **A projection machinery.** The application applies the selected scenarios to a defined subject (portfolio, assets, business, region) across explicit forward time horizons and produces scenario-conditioned consequences (physical impacts, transition impacts, financial effects). Remove this → a scenario library or data publication (e.g., the NGFS portal itself), not an application.
3. **A comparative, exploratory posture.** Results exist per scenario and are compared across scenarios and horizons; the output is a range of plausible futures under stated assumptions, explicitly not a forecast or single-point outcome. Remove this → a single-scenario projection = a conditional forecast, which is not scenario analysis.

Note the deliberate absence from L0: a *managed exposure population maintained as risk records feeding a prioritization/decision/monitoring/disclosure loop* — that is the Climate Risk Management seam. In this Type the subject is the *input configuration* of a projection run, not a managed risk population.

### L1 — Common Mature Structure (cross-product)

- Recognition-anchored scenario vocabulary: public framework families (NGFS; IPCC RCP/SSP) used directly or echoed in proprietary families (Layer B: XDI, MSCI, Risilience explicitly; Jupiter by "emissions scenarios" phrasing; NGFS portal as the authority).
- Dual risk-family coverage or at least an explicit stance toward it: physical + transition (Risilience, MSCI, Carbon4-data-side) vs physical-led (Jupiter, XDI) (Layer B).
- Financial quantification of scenario outcomes: damage/loss, credit/loss/cashflow metrics, earnings impact, carbon-price exposure (Layer B: Jupiter, XDI, Risilience, MSCI).
- Stress testing as a headline workflow, including regulator-prescribed deterministic scenarios and probabilistic (Monte Carlo) computation for FI exercises (Layer B: Jupiter, XDI; Risilience via client-documented VaR-style simulation).
- Asset/portfolio-level resolution, commonly geospatial (Layer B: Jupiter asset-level "hyperlocal"; XDI sub-asset traceability; MSCI GeoSpatial Asset Intelligence).
- Disclosure-framework alignment (TCFD/ISSB lineage; CSRD/EU Taxonomy/SEC mentions) — NGFS itself names "scenario analysis and disclosure" as an application (Layer B).
- Multi-surface delivery: interactive platform, data/API feeds, generated reports (Layer B: XDI explicitly enumerates all three; MSCI data platform; Jupiter platform family).
- High-level screening before depth (Layer B: Risilience risk screening; XDI screen solution).
- Forward-looking option exploration (adaptation ROI / resilience pathways / transition planning) as an output leg feeding decisions that live elsewhere (Layer B: Jupiter adaptation ROI, XDI pathway to resilience, Risilience transition planning).

### L2 — Variant / Optional

- Subject domain: FI lending/credit portfolios, investment portfolios, corporate business and assets, real assets/infrastructure, sovereign/regional views.
- Risk-family emphasis: physical-led vs transition-led vs integrated dual.
- Scenario source posture: proprietary internally-developed scenarios vs public-framework scenarios vs hybrid.
- Horizon emphasis: multi-decade long-term vs short-term (central-bank style, 3–5 years per NGFS short-term vintage) vs both.
- Computation style: deterministic scenario runs vs probabilistic (Monte Carlo) simulation.
- Carrier: standalone SaaS platform vs data provider suite module vs consulting-delivered studies vs engine consumed by other systems.
- Model-governance/MRM defensibility posture for FI/regulatory use.
- Nature/biodiversity extension.

### L3 — Vendor-specific (kept out of final document)

- Jupiter: ClimateScore Global and product-family names (RiskSignal, Adaptation Hub, Entity Modeling, MetricEngine, Compliance Hub, MRM Accelerator, Site Intelligence); vendor-stated figures ("scenarios in 5-year increments", "now to 2100", "22k+ data values per location", customer-penetration percentages).
- XDI: Climate Risk Hub, Climate Risk Engines names; 175+ countries claim.
- Risilience: Riise, RiiseIQ, Digital Twin module names; Cambridge Centre for Risk Studies partnership; vendor-stated scenario headline figures (50%/60%/$244-per-tonne claims).
- MSCI: product name "Climate Scenario Analysis" within Climate Solutions; "4 million+ asset locations" GeoSpatial claim; "2250+ climate metrics" claim.
- Carbon4: Carbon Impact Analytics (CIA) naming; Nutriscore-style retail feature; founder personal-brand framing.

## Rejected Findings (considered, not promoted)

- "Scenario analysis always includes a 2°C-or-lower scenario" — TCFD recommends it for disclosure contexts, but products anchor to whole families (NGFS/IPCC/proprietary); the 2°C anchor is a disclosure-convention, not an application invariant.
- "Scenarios run to 2100" — only observed as a Jupiter vendor claim; NGFS long-term scenarios and product pages support "multi-decade" generically; precise horizons are vendor/version-specific.
- "Scenario analysis is a corporate-disclosure activity only" — FI stress testing (XDI banking use case, NGFS short-term scenarios for supervisors) and investor workflows are equally first-class.
- "Climate Scenario Analysis = Climate Risk Management with a different name" — rejected after comparison: the sample contains products (MSCI's scenario product, XDI stress-test service, Carbon4-negative contrast) whose observed surface is scenario machinery without an organizational risk-management loop; the seam is real, though blurry at the edges (see Boundary Findings).
- Ortec Finance / S&P Sustainable1 as samples — abandoned (fetch failures); no claims made about them.

## Boundary Findings

**vs Climate Risk Management (the critical seam).** CRM = managed exposure population + maintained risk assessments + management loop (screen→deep-dive prioritization, response decisions, monitoring/re-assessment cycles, disclosure program). CSA = scenario machinery (scenario set + projection + comparison) whose subject is an input configuration, not a maintained risk population. Practical test: if the product's center of gravity is *running and re-running futures and comparing them*, it is CSA; if it is *keeping the organization's risk picture alive over time with decisions recorded against exposures*, it is CRM. Several sampled products straddle: Jupiter (adaptation ROI, portfolio prioritization) and XDI (screen→deep-dive ladder) were simultaneously the CRM pass's strongest physical-risk-engine samples; MSCI's scenario product and Carbon4's data pole sit cleanly on the CSA/data sides. **Remove the management loop while keeping scenario machinery → still this Type; add a maintained assessment population with prioritization/decision/monitoring records → becomes Climate Risk Management.**

**vs Physical Climate Risk Platform (unprocessed sibling).** The engine side, physical-only: hazard/loss computation for assets. CSA adds the scenario-family/horizon structure and typically transition coverage; physical-risk engines often supply CSA machinery. The CRM pass's seam is adopted: physical-climate-risk-platform = engine side without scenario-family structure or org process. Joint review recommended (see STATUS).

**vs Climate data products (Carbon4, ISS STOXX-class).** Data products serve current-state scores, footprints, alignment metrics, hazard scores. CSA is forward-looking and scenario-conditioned. **Remove the scenarios/horizons and keep the scores → climate data product.** MSCI straddles both (data + scenario product in one suite).

**vs ESG Disclosure Management / ESG Reporting.** Disclosure platforms produce reports against frameworks; scenario analysis produces the forward-looking analytical content that disclosure regimes (TCFD strategy pillar) *ask organizations to describe*. Scenario outputs feed disclosure; they are not report production.

**vs Financial Risk Management Platform / generic stress testing.** Generic stress machinery operates on market/credit/liquidity positions under macro scenarios; CSA brings climate-specific scenario content (policy pathways, warming levels, hazard models) and climate-economy model stacks. FI climate stress tests are the bridge (XDI banking use case).

**vs Energy Forecasting Platform.** Power-domain demand/price/renewables forecasting — different domain object, different horizon structure; not climate scenario families.

**vs Climate Adaptation Planning.** Projections justify adaptation; the plan/goals/actions/owners artifact belongs to adaptation planning (per that leaf's processed definition). CSA's option-exploration leg (adaptation ROI, resilience pathways) feeds it.

## Uncertainties

- Deep help-center documentation unreachable for all sampled products (same limitation as both sibling passes); all product observations derive from official product/marketing surfaces. Interface-level detail (what users actually see and click inside these products) is therefore under-evidenced; the final document describes interfaces at conceptual strength only.
- Whether the market sustains a *standalone* scenario-analysis product with literally no exposure-binding at all is unconfirmed — every sampled product binds scenarios to some subject. The L0 formulation ("defined subject as input configuration") is canonical inference (Layer C), defended by the NGFS-portal contrast (scenario publication without a subject = not an application).
- MSCI's scenario product details (methodology documents, Climate VaR mechanics) were not fetched; only the product card and suite language are evidenced.
- The Ortec Finance / S&P Sustainable1 / Moody's cluster (well-known scenario-analysis providers) was not sampled; no claims about them are made.
- Product-marketing language ("decision-grade", "transparent") was deliberately not carried into canonical findings.

## Final Synthesis

A Climate Scenario Analysis application is the **scenario-projection machinery layer of the climate-risk stack**: it holds a managed set of named climate scenarios, runs them through projection machinery against a defined subject over explicit future horizons, and delivers scenario-conditioned, financially translated consequences in a comparative, exploratory posture that is explicitly not forecasting. Its market vocabulary is set by the disclosure canon (TCFD/ISSB strategy-pillar scenario analysis) and the central-bank scenario canon (NGFS families: orderly / disorderly / hot house world / too-little-too-late, with named pathways). Its customers span FI risk teams (stress testing, MRM defensibility), investors (portfolio risk metrics), corporates (strategy resilience, transition planning inputs), and governments/regulators. It is bounded above by Climate Risk Management (which adds the managed exposure population and the management loop over maintained assessments), sideways by the physical-risk engine (computation without scenario-family structure), and below by climate data products (current-state scores without forward scenarios). The leaf is retained as a distinct Type with the process-scope seam recorded by the CRM pass; a joint review of the three-way overlap (CRM / Physical Climate Risk Platform / CSA) is recommended.
