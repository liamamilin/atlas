# Research Notes — Physical Climate Risk Platform

Research date: 2026-09-09

## Research Goal

Understand what a "Physical Climate Risk Platform" actually is in the market: what object it computes for, what machinery it runs, who consumes it, and — critically, because three sibling leaves in §21 straddle the same products — how it is separated from **Climate Risk Management** (processed 2026-09-07), **Climate Scenario Analysis** (processed 2026-09-07), and **Nature Risk Management** (processed 2026-09-09).

Two sibling passes recorded working seams that this research must confirm or amend, and a joint review was explicitly delegated to this pass:

- climate-risk-management pass: "physical-climate-risk-platform = physical-only hazard/loss computation engine side (no org-side risk process over maintained assessments)"; candidate outcomes: keep-all-three with process-scope seams, or consolidate engine-side products under this leaf.
- climate-scenario-analysis pass: "distinguish from CSA by absence of scenario-family/cross-future comparison structure (hazard-loss computation without the scenario set as first-class object)"; keep-all-three with process-scope seams remains the working outcome.
- nature-risk-management pass: the risk-generating system decides — ecosystem/biodiversity state = nature risk; climate hazards + transition = climate risk; bundling is packaging.

## Initial Boundary (hypothesis before research)

- What: software that computes physical climate risk — how climate-change-driven natural hazards translate into damage and financial loss for located physical assets — as a computation engine delivered through a platform, APIs, and reports.
- Users: banks/lending, insurers, asset managers/PE, real estate, infrastructure owners, governments.
- Most likely confusions: Climate Risk Management (org risk process), Climate Scenario Analysis (scenario-projection machinery), climate/hazard data products (scores served, not computed), catastrophe modeling (insurer event-loss machinery), GIS/hazard mapping tools.
- Unknowns: whether "physical-only" holds across the market; whether financial translation is definitional or common; whether current-state-only hazard assessment (no climate conditioning) is in-type; where the cat-modeling boundary sits.

## Research Questions

1. What is the analyzed subject — the asset? the portfolio? the location? the company?
2. What does the platform actually compute (hazard → what intermediate → what output)?
3. Is climate-change conditioning (future scenarios/horizons) definitional, or is current-state hazard scoring also in-type?
4. Is financial translation (loss/credit/cashflow metrics) definitional or common?
5. What delivery surfaces exist (platform, API, reports, on-demand)?
6. What portfolio machinery exists (upload, save, aggregate, compare, screen)?
7. Where does the Type dissolve: into CRM (process), CSA (scenario machinery), data products (no computation), cat modeling (insurance event loss)?
8. Does the sampled population justify keeping this leaf distinct from the two processed siblings (joint review)?

## Representative Products (sample rationale)

| Product | Pole | Philosophy | Customer level |
|---|---|---|---|
| XDI (Cross Dependency Initiative) | asset-portfolio physical risk, engineering-based | traceability-first: results traceable to point of failure within assets/components; screen→deep-dive→report→stress-test→resilience ladder | financial services, government, corporates, civil society |
| Jupiter Intelligence | FI decision-grade physical risk analytics | decision-first: physical risk translated to credit/loss/cashflow metrics; model-governance (MRM) posture; adaptation ROI | banks, asset managers/PE, infrastructure, real estate |
| Climate X (Spectra) | asset-level financial loss metrics, self-serve + API | self-serve computation: search/upload assets → select scenario parameters → download financial impact report; API for scale | banks, real estate, PE/asset managers, insurers, consultancies |
| Munich Re Location Risk Intelligence | reinsurer-heritage modular hazard/climate rating platform | edition-based: hazard scores/ratings per edition, from current natural hazards to climate-conditioned financial impact; portfolio machinery | insurers, banks, investors, corporates |
| One Concern | AI + catastrophe-modeling digital twin, business interruption | dependency-first: outside-the-fence infrastructure risks → business interruption; resilience metric in time | capital markets, insurance, real estate |

XDI and Jupiter were re-sampled fresh this pass (they were also the strongest engine samples in both sibling passes — expected overlap, documented as such). Climate X, Munich Re LRI, and One Concern are new samples, adding the self-serve/API pole, the reinsurer-edition pole, and the cat-modeling-heritage pole.

## Sources

All fetched 2026-09-09 (Layer A unless noted):

- XDI — https://xdi.systems/ (root: solutions ladder, Climate Risk Hub, Climate Risk Engines, Automated Resilience launch, sectors, use cases incl. banking stress testing)
- Jupiter Intelligence — https://www.jupiterintel.com/ (root: ClimateScore Global capability list, product family, MRM posture, resilience journey, industries)
- Climate X — https://climate-x.com/ (root: product family Spectra/Adapt/Carta, industries, regulation pages, FAQs)
- Climate X — https://climate-x.com/spectra (Spectra product page: workflow step-by-step, methodology, delivery surfaces, integration points, MRM framework)
- Munich Re — https://www.munichre.com/rmp/en/products/location-risk-intelligence.html (Location Risk Intelligence: six editions, On-Demand version, platform functionalities incl. portfolio management/aggregation/comparison, areas & lines, REST API)
- One Concern — https://www.oneconcern.com/ (root: positioning, digital twin, business interruption, resilience metric in time)
- One Concern — https://oneconcern.com/en/about/ (about: AI + deep catastrophe modeling heritage, Swiss Re partnership)

Abandoned sources (per network-limitation rule): Verisk climate-risk page (404 on first URL; dropped rather than retrying alternates). No claims made about Verisk, Moody's RMS, or other cat-model vendors from this pass.

Sourcing limitation: as in both sibling passes, deep help-center / user-manual documentation was not reachable; evidence comes from official product surfaces. Per evidence rules: no precise numeric claims (asset counts, hazard counts, data-point counts, resolution figures, AUM figures) are carried into the final document; vendor-stated figures are recorded here as product-specific claims only.

## Product Observations

### XDI — Evidence layer A (direct, official root page; re-confirmed this pass)

- Self-label: "The Physical Climate Risk Experts", since 2007. "XDI quantifies the cost of extreme weather and climate change impacts to physical assets."
- Solutions ladder: Screen for assets most-at-risk (relative materiality across multiple assets) → Asset-level deep dive ("manage and reduce risk") → Meet reporting requirements (aligned with TCFD, ISSB, EU Taxonomy; CSRD and SEC named in report framing) → Stress test ("aggregate asset-level analysis to portfolio level insights across a range of asset classes and scenarios including SSPs, RCPs and NGFS") → Engage clients on a pathway to resilience (forward-looking projections under different assumptions; risk-reduction and adaptation opportunities) → Delivered the way you want (Climate Risk Hub platform, API into own systems, off-the-shelf reports, visualisation tools).
- Traceability posture: "More than just a score, our results are specific, traceable and assurable. Each of our outputs is traceable to the point of failure not only within individual assets, but also within their components, even across a portfolio of tens of thousands."
- Engine: "Powered by the award-winning Climate Risk Engines, XDI brings together sub-asset level data with extensive climate, hazard and engineering data."
- New capability observed this pass: **Automated Resilience** — "helps asset owners and investors identify where adaptation could deliver the greatest reduction in physical climate risk across large portfolios. By comparing potential risk reduction and financial value, it helps prioritise where deeper assessment and resilience investment may have the greatest impact."
- Use cases: banking stress testing (large-scale Monte Carlo simulations across global residential/commercial lending portfolios for a regulatory exercise, plus a regulator-prescribed deterministic scenario); brownfield infrastructure due diligence (port; unexpected opex/capex risk); city planning (urban heat for a state-owned water utility, exploring adaptation options); public data releases (sub-sovereign physical risk comparison).
- Sectors: financial services, government, corporates, civil society.
- Boundary note (consistent with both sibling passes): no managed plan object, no risk owners/approvals/treatment plans; outputs are analyses and decision support feeding external processes.

### Jupiter Intelligence — Evidence layer A (direct, official root page; re-confirmed this pass)

- Positioning: "Decision-grade risk intelligence for financial institutions. Translate physical risk into capital advantage." "Climate risk is capital risk."
- Market critique in vendor's own words: most physical risk data is "disclosure-first and decision-light"; "Opaque outputs don't clear MRM"; "Metrics without cashflow impact don't move boardrooms"; "No proof of ROI, no execution."
- Engine: ClimateScore Global — "Asset-level, multi-peril projections with scenario steps and long-term horizons"; "Financial translation to credit, loss, and cashflow metrics your teams use"; "Transparent, auditable methods that clear MRM and support regulatory reviews"; capability list includes portfolio & asset level risk assessment, stress testing (credit, portfolio & operational), damage & loss modeling, economic impact data, entity modeling, adaptation planning & ROI, regulatory disclosure & compliance. Vendor-stated figures ("22k+ data values per location", "Scenarios in 5-year increments", "Now to 2100") = product-specific claims, kept out of final doc.
- Product family on the engine: RiskSignal, Adaptation Hub, Entity Modeling, MetricEngine, Compliance Hub, MRM Accelerator, Site Intelligence; "Jupiter AI" appears in navigation.
- Posture: "MRM-approved by Tier 1 banks" (vendor claim); "Trace every assumption; Validate results against observed events; Stress-test portfolios across transparent scenarios"; "We give you everything but the IP."
- Journey framing: "Assess your exposure → Evaluate business impact → Decide what to do"; "Model decisions, not just exposure."
- Industries: banking and lending, asset management and private equity, infrastructure and industrial, real estate and REITs.

### Climate X (Spectra) — Evidence layer A (direct, official root + product pages; new sample)

- Self-label: "Climate Risk Analytics for Resilience & Long-Term Asset Protection"; "Physical Climate Risk Intelligence". Product family: **Spectra** (physical risk), **Adapt** (adaptation), **Carta** (corporate asset mapping), Adaptation Finance, Infrastructure Screener.
- Spectra: "translates physical climate risks into financial loss metrics at the portfolio and asset levels"; "run short & long-term physical risk assessments quickly and independently"; "Quantify the P&L impact of physical risk."
- Observed user workflow (step-by-step, vendor's own description): "Search assets by postcode or upload your portfolio, select climate scenario parameters, then download your financial impact report directly." "Evaluate short & long-term risk in seconds and take timely action, with risk ratings, hazard probability and severity metrics in a couple of clicks."
- Method: "integrates evolving climate projections with proprietary building vulnerability data"; FAQ: "Spectra combines downscaled, multi-model climate projections with Climate X's proprietary vulnerability datasets and geospatial hazard models enabling validated, asset-level financial loss analysis globally."
- Delivery: web platform ("Replace outdated PowerBI and Excel files with an intuitive interface that's as easy to use as Google Maps") + "Enterprise API to scale your analysis to handle hundreds of thousands of input assets."
- Integration points (vendor-named): "Due Diligence and Investment Cycle process, Originations, Stress Testing, Client Engagement."
- Governance: "regular model reviews through the model risk management framework and ISO certifications"; "Integrate Spectra into your existing risk management frameworks for model risk management - aligned short & long-term climate physical risk assessment at asset and portfolio scales."
- Compliance surfaces: IFRS S2/TCFD, EU Taxonomy, ECB, CSRD, SEC; dedicated regulation pages for SB 261, PRA SS5/25 ("Physical climate risk analytics platform delivering property-level financial loss metrics aligned with PRA SS5/25 and SS1/23 expectations"), AASB S2, CSDS/OSFI B-15, ESRS.
- Adapt (sibling product): "quantifies capital expenditure and ROI for an asset's adaptation investment… integrate adaptation to your investment cycle and finance climate adaptation."
- Carta (sibling product): asset-level mapping of companies' global footprints ("18.7 million public and private companies" — vendor claim) — asset discovery feeding risk analysis.
- Vendor-stated figures (product-specific, kept out of final doc): 1.5 billion+ assets covered, 12 hazards, 200 trillion data points, 30m wildfire-model resolution, clients with $13.5tn combined AUM.

### Munich Re Location Risk Intelligence — Evidence layer A (direct, official product page; new sample)

- Self-label: "the solution for assessing and managing physical risks from natural hazards and climate change, calculating their financial impact and even integrating them into your reporting." "The modular SaaS solution for managing physical climate and natural disaster risks."
- Six data editions (the same platform, different depth/angle):
  - **Natural Hazards Edition** — current exposure to a comprehensive collection of natural hazards; Overall Risk Score plus detail scores (earthquake, storm, flood) and dedicated ratings for 15 natural hazards (vendor count). Score basis: past events.
  - **Climate Change Edition** — "analyse and assess the physical risks associated with climate change in different future scenarios. Considering both acute and chronic climate risks… 13 climate hazards… risk scores are not only calculated on the basis of past events, but also include projected changes in the intensity and frequency of future events under different climate scenarios" (250+ scores — vendor count).
  - **Climate Financial Impact Edition** — "predicting the potential financial impact of climate risks. Thanks to integrated financial metrics…"
  - **Company Climate Risk Edition** — "financially quantify climate risk in corporate portfolios. It aggregates physical climate risk across entire companies, including their underlying assets, and expresses that risk in relevant financial metrics… for credit and capital allocation processes."
  - **Wildfire HD Edition** — higher-resolution wildfire analysis for named countries.
  - **Reporting Edition** — "out-of-the-box… assessment of their exposure to meet increasing regulatory reporting requirements… according to the EU taxonomy, CSRD, TCFD or ISSB for all your sites worldwide via an intuitive user interface."
- **On-Demand version**: credit-based, no contract — "determine risk assessments for individual locations (not entire portfolios) and download them in meaningful reports."
- Platform functionalities (observed, unusually detailed for this market):
  - Single asset assessment: search by coordinates/address/map click; two result types — grouped risk scores ("red flags") and hazard zones with detailed asset score representation.
  - Portfolio assessment: "Assess climate risk for portfolios with multi-million sites in a single operation"; traffic-light visualisation; per-hazard drill-down; downloadable reports.
  - Portfolio management: upload via drag-and-drop (Excel/CSV), save scored locations as assets, move assets to portfolios, add/delete/rename, filtering, visualisation, sharing.
  - Portfolio aggregation and comparison: aggregate portfolios, benchmark one portfolio (or subset) against another.
  - Areas & Lines: user-drawn areas/lines and predefined geometries (railway lines, roads, airports, plants, energy parks); percentage-of-area exposure; prescored areas (countries, administrative zones, postcodes, NUTS zones, CRESTA zones).
  - Export manager: CSV/Excel/PDF exports, customisable report selections saved as reusable templates.
  - Maps (base maps, opacity, layer selection), elevation profile (flood-risk precision), interactive guides, support centre, REST API ("retrieve all scores… integrate almost all of Location Risk Intelligence's assessment tools and datasets into your own application environment"), SSO.
- Heritage/positioning: reinsurer product (Risk Management Partners); Chartis ClimateRisk50 top-3 ranking quote citing strength "for a variety of industry sectors, including insurance, banking, real estate and manufacturing."
- Boundary note: a separate **Biodiversity and Nature Risk Edition** exists in the same platform family — direct packaging evidence for the nature-risk seam (bundling is packaging; the nature leg is a separate edition, not the same object).

### One Concern — Evidence layer A (direct, official root + about pages; new sample; thin surface)

- Positioning: "Planetary-Scale Resilience Software Platform"; "Bridging Climate Risk to Financial Risk in Capital Markets, Insurance, and Real Estate."
- Method: "AI, data science, and deep catastrophe modeling… a digital twin of our physical world"; differentiates "properties and businesses based on their real-world business interruption vulnerabilities due to the infrastructure they depend on—from crippling power outages to chaotic web of supply chain disruptions, revealing exposure to uninsured business losses."
- Metric framing: "a consistent, comparable metric for physical risk measured in the form of time to evaluate and benchmark properties, companies and sectors" — resilience/downtime measured in time units rather than currency.
- Partnership: strategic partnership with Swiss Re "to Reveal Nat Cat Business Interruption Risk with AI."
- Heritage: catastrophe-modeling + AI (founders' structural-engineering/CS background; technical working group of earthquake/coastal engineers).
- Boundary note: the "outside-the-fence" infrastructure-dependency angle (lifeline disruption → business interruption) is a distinctive computation pole; the site surface is thin, so observations are held at positioning strength.

## Cross-product Comparison

| Dimension | XDI | Jupiter | Climate X (Spectra) | Munich Re LRI | One Concern |
|---|---|---|---|---|---|
| Analyzed subject | asset portfolios (single asset → tens of thousands) | FI portfolios, assets, entities | uploaded/searched assets and portfolios | single locations, portfolios (multi-million sites), drawn areas/lines, prescored zones | properties, businesses, sectors |
| Hazard scope | multi-hazard physical (extreme weather + climate change) | multi-peril physical (extreme weather) | multi-hazard physical (12 hazards — vendor count) | natural hazards (incl. earthquake) + climate hazards (13 — vendor count) | nat-cat perils + infrastructure dependency |
| Climate conditioning | SSPs/RCPs/NGFS; forward-looking projections under different assumptions | scenario steps, long-term horizons (to 2100 — vendor claim) | climate scenario parameters; short & long-term | Climate Change Edition: future scenarios, acute+chronic; Natural Hazards Edition: current-only | climate change acceleration framing |
| Computation output | cost of impacts; damage results traceable to point of failure/component | damage & loss; credit/loss/cashflow metrics; economic impact | financial loss metrics; risk ratings; hazard probability & severity | risk scores/ratings per hazard; financial-impact metrics (edition-dependent) | business-interruption vulnerability; resilience metric in time |
| Financial translation | cost/financial value framing; adaptation ROI comparison | headline capability (credit, loss, cashflow) | headline capability (P&L, financial loss metrics) | dedicated edition (Climate Financial Impact; Company Climate Risk) | financial-decision framing; time metric |
| Traceability/defensibility | "specific, traceable and assurable"; point-of-failure traceability | "transparent, auditable methods that clear MRM"; trace every assumption; validate vs observed events | model risk management framework reviews; ISO certifications | reinsurer data heritage; "reliable and trustworthy data, using the latest scientific standards" | not evidenced on fetched surface |
| Portfolio machinery | screen → deep dive; portfolio aggregation | portfolio & asset level assessment; entity modeling | upload portfolio; API for hundreds of thousands of assets | upload/save/share/aggregation/comparison; areas & lines; prescored zones | properties/companies/sectors benchmarking |
| Delivery surfaces | Climate Risk Hub platform + API + off-the-shelf reports + visualization | platform product family + data (MRM posture) | web platform + Enterprise API (+ PowerBI/Excel replacement framing) | modular SaaS + On-Demand credits + REST API + exports | platform (surface thin) |
| Disclosure alignment | TCFD, ISSB, EU Taxonomy; CSRD/SEC in report framing | regulatory disclosure & compliance product | IFRS S2/TCFD, EU Taxonomy, ECB, CSRD, SEC + jurisdiction pages | Reporting Edition (EU taxonomy, CSRD, TCFD, ISSB) | not evidenced |
| Stress testing | Monte Carlo + regulator-prescribed deterministic (banking use case) | credit/portfolio/operational stress testing | stress testing named as integration point | not headline on fetched page | not evidenced |
| Adaptation/resilience leg | Automated Resilience (prioritise adaptation investment); resilience pathways | Adaptation Hub; adaptation planning & ROI | Adapt product (adaptation CapEx & ROI); Adaptation Finance | not headline on fetched page | resilience framing |
| Org-side risk process (owners/decisions/monitoring/disclosure program) | absent (decision support only) | partial (decide framing; adaptation ROI) | absent (integration points named, process lives elsewhere) | absent (assessment + reporting outputs) | absent |
| Managed scenario set as first-class object (CSA test) | absent (scenarios = computation parameters) | absent (scenario steps = parameters) | absent (scenario parameters selected per run) | absent (edition-bundled scenarios) | absent |

### Stable commonalities (cross-product, layer B)

1. **Located assets as the analyzed population.** Every product binds computation to geolocated physical assets — searched, uploaded, entity-mapped, or drawn — individually and as portfolios. The asset (not the company, not the region) is the unit of analysis; company/sector views are aggregations over assets.
2. **Hazard-to-impact computation.** The platform computes, not just serves: hazard data is combined with asset exposure and vulnerability to produce impact results — damage, loss, financial metrics, and/or risk scores. All five products describe this computation; none merely resells hazard maps.
3. **Climate-change-conditioned forward projections.** Impacts are computed under climate-change scenarios/projections across time horizons, showing how risk evolves (all five; Munich Re's current-only Natural Hazards Edition is a module within a platform whose climate editions carry the conditioning).
4. **Portfolio-level aggregation and screening.** Roll asset results up to portfolio views; identify red flags / most-at-risk assets for deeper analysis (all five in some form).
5. **Multi-hazard physical scope.** Multiple acute hazards (flood, wind/tropical cyclone, heat, wildfire, drought, subsidence, hail-class) and commonly chronic shifts; hazard catalogs vary by product.
6. **Traceability/defensibility posture.** Results must be explainable: component-level traceability (XDI), assumption tracing and validation against observed events (Jupiter), model-risk-management reviews (Climate X, Jupiter), reinsurer data heritage (Munich Re).
7. **Multi-surface delivery.** Interactive (map-centric) platform + API/data feeds + generated reports; on-demand single-asset assessment exists as a light tier (Munich Re On-Demand; Climate X self-serve).
8. **Disclosure-framework alignment.** TCFD/ISSB/CSRD/EU Taxonomy/SEC-class alignment and regulator-exercise use cases are standard (four of five evidenced; One Concern not evidenced on fetched surface).
9. **Adaptation/resilience option analysis.** Testing what risk reduction is achievable and what it costs (XDI Automated Resilience, Jupiter Adaptation Hub, Climate X Adapt) — an output leg feeding decisions managed elsewhere.
10. **Physical-only frame.** None of the five centers transition risk; the physical/transition dual frame belongs to the CRM/CSA siblings. (Layer B, strong: all five physical-led or physical-only.)

### Product-specific / weaker-evidence observations

- Engineering-based traceability to component-level "point of failure": XDI's signature framing → product-specific emphasis.
- MRM (model risk management) approval posture as headline: Jupiter (and Climate X's MRM-framework reviews) → FI-tier common, not universal.
- Edition-based modular packaging with a current-hazards-only edition: Munich Re → product-specific packaging.
- Business-interruption/infrastructure-dependency computation ("outside-the-fence") and a resilience metric in time units: One Concern → product-specific.
- Asset discovery/mapping of corporate footprints as a sibling product: Climate X Carta, Jupiter Entity Modeling → common direction, product-specific realizations.
- On-demand credit-based single-asset assessment: Munich Re → product-specific packaging.
- Elevation-profile and user-drawn area/line geometries: Munich Re → product-specific interface features.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Physical Climate Risk Platform exists to compute, for located physical assets, how climate-change-driven hazards translate into impact:

```text
Located-asset population
  (single assets → large portfolios, bound to geographic locations)
        ↓ combined with
Climate-conditioned hazard projections
  (multi-hazard, under climate scenarios/projections, across
   forward time horizons)
        ↓ run through
Hazard-to-impact computation
  (hazard × asset exposure × vulnerability → damage/loss)
        ↓ producing
Asset-level impact results
  (damage, loss, financial metrics, and/or risk scores,
   aggregable to portfolio level)
```

Three properties. Removal test:

- Remove the **located-asset population** (computation no longer bound to identified assets) → hazard maps / climate projection data — a data product, not a risk platform.
- Remove the **hazard-to-impact computation** (scores served without computing hazard × exposure × vulnerability for the user's assets) → hazard data licensing / rating feed — a data product.
- Remove the **climate-change conditioning** (no forward projections; current-climate hazard loss only) → natural-hazard risk scoring / catastrophe-modeling territory — the ancestor computation, not a *climate* risk platform.

Jointly-held load-bearing checks:

- 1 alone = hazard map / asset registry.
- 2 without 1 = a computation engine with no subject (data product).
- 3 without 1+2 = a climate projections publication (NGFS-portal-class).
- 1+2 without 3 = current-state natural-hazard scoring platform (Munich Re Natural Hazards Edition as a module; cat-modeling territory as a standalone) — the ancestor, not this Type.
- 1+3 without 2 = hazard projections over locations with no asset impact translation.

Historical / market-sample check: FEMA HAZUS-class hazard-loss estimation tools (1990s) compute damage/loss for assets under hypothetical hazard scenarios but without climate-change conditioning — they fail leg 3 and sit in the ancestor territory. Insurer catastrophe models (event-based probabilistic loss for insurance books, 1980s–present) likewise fail leg 3 as a defining property and serve a different decision context. Municipal hazard maps + GIS fail leg 2. The Type is specifically the climate-change-conditioned generation of hazard-loss computation, delivered as a standing platform. The definition does not require cloud delivery, AI layers, or named framework certifications (all modern-market commonalities).

### L1 — Common Mature Structure

Very common in mature products, not required for recognition:

- financial translation (expected loss, damage cost, credit/cashflow/P&L metrics)
- multi-hazard catalogs (acute + chronic)
- portfolio aggregation, screening, red-flag identification
- traceability/defensibility machinery (component-level traceability, assumption tracing, validation, MRM reviews)
- map-centric interactive platform + API/data feeds + generated reports
- disclosure-framework alignment (TCFD/ISSB/CSRD/EU Taxonomy/SEC-class) and regulator stress-test use cases
- stress testing (deterministic prescribed cases + probabilistic simulation)
- adaptation/resilience option analysis (risk-reduction vs cost/ROI)
- asset discovery/entity mapping (corporate footprint → assets)
- current-state natural-hazard assessment riding alongside (including non-climate hazards such as earthquake)

### L2 — Variant / Optional Structure

- customer tier: banking/lending, insurance, asset management/PE, real estate/REITs, infrastructure/industrial, government/municipal
- engine posture: proprietary embedded model chains vs licensed hazard data with in-house translation vs reinsurer-heritage data
- computation style: deterministic scenario runs vs probabilistic (Monte Carlo) simulation
- delivery packaging: SaaS platform vs API-first vs on-demand credits vs off-the-shelf reports vs managed service/reseller delivery
- resolution: asset-level (down to components) vs user-drawn areas/lines vs prescored zones (admin/postcode/NUTS/CRESTA-class)
- hazard emphasis: all-peril breadth vs single-peril depth (e.g., high-resolution wildfire)
- current-state-only editions/modules within a climate-conditioned platform family
- impact framing: currency-denominated loss vs score/rating scales vs time-denominated resilience metrics
- infrastructure-dependency / business-interruption modeling depth

### L3 — Vendor-specific (kept out of the final document)

- XDI: Climate Risk Hub, Climate Risk Engines, Automated Resilience, ResilienceArc (open-access platform with Climate Arc), 175+ countries claim, reseller program, fossil-fuels/weapons statement.
- Jupiter: ClimateScore Global, product-family names (RiskSignal, Adaptation Hub, Entity Modeling, MetricEngine, Compliance Hub, MRM Accelerator, Site Intelligence), Jupiter AI, "22k+ data values per location", "scenarios in 5-year increments", "now to 2100", market-penetration claims (Global 100 %, largest-bank counts), "everything but the IP" framing.
- Climate X: Spectra/Adapt/Carta/Adaptation Finance/Infrastructure Screener names, 1.5B+ assets, 12 hazards, 200 trillion data points, 44M miles of infrastructure, 30m wildfire resolution, $13.5tn AUM claims, "Google Maps"-ease framing, jurisdiction regulation pages (SB 261, SS5/25, AASB, CSDS, ESRS).
- Munich Re: Location Risk Intelligence name, six editions and their hazard/score counts (15 natural hazards, 13 climate hazards, 250+ scores), On-Demand credits, areas & lines, elevation profile, prescored NUTS/CRESTA zones, Chartis ClimateRisk50 ranking, "get started within 2 days" claim.
- One Concern: digital-twin framing, "outside-the-fence" vocabulary, resilience metric in time, Swiss Re partnership, founder/technical-working-group composition.

## Rejected Findings (considered, not promoted)

- "Financial translation is definitional" — rejected: Munich Re's base editions deliver scores/ratings without financial metrics (financial impact is a separate edition); scores are a legitimate impact output. Financial translation is the dominant realization (L1), not the invariant.
- "Current-state-only hazard assessment is out of type" — rejected as a blanket claim: Munich Re ships a current-only Natural Hazards Edition inside the same platform family. The resolution: climate conditioning is definitional for the *Type*; current-state-only assessment exists as modules/editions within such platforms and as the drift boundary toward hazard-data products when it is all a product does.
- "The platform must maintain the asset population as a living managed register" — rejected: assets/portfolios are held as computation configuration (saved, reusable), but the maintained-assessment-with-decisions-and-monitoring structure is the CRM seam. No sampled product carries owners/approvals/treatment plans/monitoring cycles over assessments.
- "Scenario families must be first-class managed objects" — rejected: that is the CSA seam. In all five products, scenarios are parameters of computation (selected per run or bundled per edition), not a managed comparative-futures structure.
- "Cat modeling is this Type" — rejected: event-based probabilistic loss machinery for insurance pricing/reserving under the current climate serves a different decision context and lacks climate-change conditioning as its center; it is the ancestor/adjacent territory. Heritage overlap is real (One Concern, Munich Re) and documented as straddling.
- "Non-climate natural hazards (earthquake) disqualify a platform" — rejected: hazard breadth including non-climate perils rides along as platform extension; the climate-conditioned leg is what names the Type.

## Boundary Findings

**vs Climate Risk Management (the critical seam, joint review discharged this pass).** CRM = the organization-side risk loop: managed exposure population + maintained climate risk assessments + prioritization/decision/monitoring/disclosure cycles. PCRP = the computation engine: located-asset hazard→impact computation under climate conditioning, delivered as platform/API/reports. Practical test: if the product's center of gravity is *computing asset-level physical impact evidence*, it is PCRP; if it is *keeping the organization's risk picture alive with decisions recorded against maintained assessments*, it is CRM. Products straddle: XDI and Jupiter (the CRM pass's strongest engine samples) carry partial loop features (screen→deep-dive, adaptation ROI, decide framing) — seams are center-of-gravity, not mutual exclusion; a single product can legitimately instantiate both Types. **Remove the org-side process while keeping the computation → still this Type; add maintained assessments with decisions/monitoring/disclosure program → becomes Climate Risk Management.**

**vs Climate Scenario Analysis (joint review discharged this pass).** CSA = managed scenario set (first-class objects) + projection machinery + comparative exploratory posture across futures; the subject is input configuration. PCRP = hazard-to-impact computation where scenarios are parameters, not managed objects; no cross-future comparison structure as the center; physical-only (CSA commonly spans transition). Confirmed against all five fresh samples: none presents a managed scenario set or cross-scenario comparison explorer as its center. **Add the managed scenario set with comparative posture → becomes Climate Scenario Analysis; keep hazard→asset-impact computation → this Type.**

**vs Nature Risk Management (seam ratified from the nature pass).** The risk-generating system decides: ecosystem/biodiversity/ecosystem-service state and dependencies = nature risk; climate hazards (+ transition) = climate risk. Packaging evidence this pass: Munich Re ships a separate Biodiversity and Nature Risk Edition beside its climate editions — bundling is packaging on one platform spine, not the same object.

**vs Climate/hazard data products (drift boundary).** When computation disappears — scores and hazard layers served without computing hazard × exposure × vulnerability for the customer's own assets — the product becomes a data/licensing product (hazard-data vendors, current-state score providers). The five sampled products all describe computation for the customer's assets; data products were the Carbon4-class pole in the CSA pass.

**vs Catastrophe modeling (adjacent territory, no directory leaf).** Cat models compute event-based probabilistic loss for insurance portfolios under the current climate, serving pricing/reserving/capital. PCRP computes climate-change-conditioned forward impact for lending/investment/ownership/disclosure decisions. Heritage overlap (One Concern's "deep catastrophe modeling", Munich Re's reinsurer heritage) is documented as straddling, not identity. **Remove climate conditioning and the multi-audience decision orientation → cat-modeling territory.**

**vs GIS / hazard mapping tools.** Maps are the dominant interface, not the product: without asset-bound impact computation, a map layer is a data product. The map-centric platform UI (all five) sits on top of computation.

**vs ESG Disclosure Management / ESG Reporting.** Disclosure-aligned reports are an output surface (all major products); the managed object is the asset-level impact computation, not the disclosure. Disclosure-led products (Manifest-class) belong to the disclosure sibling territory.

**vs Climate Adaptation Planning.** The platform's adaptation leg (risk-reduction vs cost/ROI comparison) produces evidence; the plan artifact (goals, actions, owners, progress) belongs to adaptation planning (processed leaf). XDI's Automated Resilience explicitly "helps prioritise where deeper assessment and resilience investment may have the greatest impact" — prioritization evidence, not plan management.

**Joint review outcome (discharges the flags recorded by the CRM and CSA passes):** keep-all-three RATIFIED with process-scope seams. The consolidation alternative (fold engine-side products under CRM) is rejected on fresh evidence: the engine-side population includes products with no organizational risk process at all (Munich Re's editions, Climate X's self-serve Spectra, on-demand single-asset assessment), and the customer workflows are distinct (due diligence, origination, underwriting, transaction screening vs governance/disclosure programs). The three Types form a stack: PCRP computes the physical evidence; CSA projects futures through scenario machinery; CRM runs the organizational risk process over both.

## Uncertainties

1. Deep help-center documentation unreachable for all sampled products (same limitation as both sibling passes); interface descriptions in the final document are at conceptual strength; no numeric claims carried.
2. One Concern's product surface is thin (root + about pages only); its observations are held at positioning strength; its business-interruption computation details are not evidenced.
3. Verisk/Moody's RMS cat-model cluster not sampled (fetch failure/abandonment); the cat-modeling boundary is drawn from the sampled heritage straddlers plus the sibling passes' rejection notes, not from direct cat-vendor evidence.
4. Whether a pure hazard-data licensing product would self-identify with this leaf's label is untested; the drift boundary is inferred from the computation requirement, not from sampling a data vendor this pass.
5. Munich Re's Climate Change Edition scenario vocabulary (which named families) is not detailed on the fetched page; scenario-parameter depth varies unverified across products.
6. Regional/regulatory-regime specialists (e.g., PRA SS5/25-first vendors) observed only through Climate X's regulation pages; not independently sampled.

## Final Synthesis

A Physical Climate Risk Platform is the computation engine of the climate-risk stack for physical hazards: it holds located assets — singly or as large portfolios — as the analyzed population, runs climate-change-conditioned hazard projections through hazard-to-impact computation (hazard × exposure × vulnerability), and produces asset-level damage, loss, financial metrics, and/or risk scores that aggregate to portfolio views, delivered through a map-centric platform, APIs/data feeds, and disclosure-aligned reports. Its customers span banks (origination, stress testing), insurers (underwriting, portfolio steering), asset managers and real estate (due diligence, investment cycles), infrastructure owners, and governments. Financial translation, multi-hazard breadth, traceability/MRM defensibility, screening, stress testing, and adaptation option analysis are common mature structure; the defining core is the located-asset population, the hazard-to-impact computation, and the climate-change conditioning. The Type is bounded above by Climate Risk Management (which adds the organizational risk process over maintained assessments), sideways by Climate Scenario Analysis (which adds the managed scenario set and comparative futures posture), below by climate/hazard data products (scores without computation), and behind by catastrophe modeling (event-based insurance loss machinery without climate conditioning). Keep-all-three with process-scope seams is ratified; the three leaves form a computation → projection → process stack with real product straddling at the seams.
