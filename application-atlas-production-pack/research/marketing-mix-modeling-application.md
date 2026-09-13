# Research Notes — Marketing Mix Modeling Application

Research date: 2026-09-08

## Research Goal

Determine what a Marketing Mix Modeling (MMM) Application actually is: its defining core (minimal), its standard mature capabilities, its variants, and its boundaries vs the neighboring §06 types — especially Marketing Attribution Platform (MTA) and Marketing Analytics Platform, both of which pre-hung seams for this leaf. Also resolve how "Media Mix Modeling" and "Marketing Mix Modeling" relate, and how the modern always-on SaaS shape relates to the historical consulting-delivered econometric study.

## Initial Boundary

Working hypothesis before research:

- MMM is a statistical modeling application that estimates how an advertiser's marketing spending (by channel) relates to business outcomes (sales/revenue), using aggregate historical time-series data — not user-level data.
- Primary users: marketing analytics / marketing-science teams at advertiser organizations, serving marketing leadership and finance stakeholders.
- Nearest neighbors to disentangle:
  - Marketing Attribution Platform — also "measures channel impact", but at user-journey level.
  - Marketing Analytics Platform — also "measures marketing performance", but descriptive KPI reporting, not an estimated causal spend-response model.
  - A/B Testing / Digital Experimentation — also causal, but controlled experiments, not observational modeling of the whole mix.
  - Budgeting & Forecasting (financial) — also allocates budgets, but no marketing spend-response modeling.
- Unknowns: is budget optimization/scenario tooling definitional or common? Is incrementality testing part of the Type or a bundled neighbor? Is "media mix" a separate Type from "marketing mix"? How does the open-source MMM framework shape (Robyn, Meridian) relate to the Type?

## Research Questions

1. What data does an MMM application consume, at what aggregation, and who owns the subject (whose marketing is being measured)?
2. What is the model in "modeling" — what does the system estimate, and what are its standard outputs (contribution, ROI, response curves, baseline)?
3. What does the user actually do, step by step: data → model → results → decision?
4. What surfaces/interfaces exist (dashboards, channel pages, optimizers, validators, refresh trackers)?
5. What rules and constraints shape behavior (aggregation-only data, refresh cycles, collinearity limits, optimization constraints, model validation)?
6. Where is the exact seam vs Marketing Attribution Platform (user-level journeys) and vs Marketing Analytics Platform (descriptive KPIs)?
7. How do incrementality experiments relate to the model (calibration loop), and is experimentation part of the Type?
8. Would older/regional/platform-native forms (consulting-delivered annual econometric studies, spreadsheet regressions) still satisfy the definition? (Historical check.)

## Representative Products

Selected for market representation, different product philosophies, and different customer tiers:

| Product | Shape / philosophy | Tier |
|---|---|---|
| Recast | Modern Bayesian MMM SaaS; "planning & analysis infrastructure"; automated engine + planning tools (Optimizer, Forecaster, Goals) + bundled GeoLift experiments | DTC / mid-market → enterprise |
| Measured | "Media Effectiveness Platform" for enterprise brands; test-calibrated "Causal MMM" ("triangulated measurement"); services-heavy | Enterprise brands |
| Sellforte | "Measurement & Optimization OS for Retail and Ecommerce"; always-on Causal Bayesian MMM + attribution correction + closed-loop activation into ad platforms | Retail / ecommerce, EU-origin, multi-market |
| Analytic Partners | Consulting-heritage enterprise; GPS-Enterprise (GPS-E) platform under a "Commercial Analytics" umbrella; scenario/forecast-centric UI | Large global enterprises |

Rejected / unreachable: Keen Decision Systems (site returned empty twice — abandoned per network rule); MassAnalytics/MassTer (domain parked/for sale — dead source); Nielsen MMM (consulting service, no operational docs attempted after 4-product saturation).

## Sources

All fetched 2026-09-08:

- Recast — homepage https://getrecast.com/ (A); Knowledge Base root https://docs.getrecast.com/docs/?l=en (A)
- Measured — homepage https://www.measured.com/ (A); MMM explainer FAQ "What is Marketing or Media Mix Modeling (MMM)?" https://www.measured.com/faq/what-is-marketing-media-mix-modeling-mmm/ (A — official vendor educational)
- Sellforte — homepage https://sellforte.com/ (A); "Causal Marketing Mix Modeling" methodology page https://sellforte.com/marketing-mix-modeling (A)
- Analytic Partners — homepage https://analyticpartners.com/ (A — product/platform positioning level; no help-center operational docs reachable at this tier)
- Mirror-side seams recorded in STATUS.md by prior passes (B): marketing-analytics-platform pass (Funnel ships "Measure" [MTA/MMM/incrementality] as a separate product line from its Data Hub; Improvado lists MMM as a use case; 2/4 samples lack MMM entirely); marketing-attribution-platform pass (MTA vs MMM seam documented; sampled measurement-suite vendor ships both as distinct methodologies with separate onboarding tracks, UI view families, doc categories).

Source-access limitations: no authenticated help-center articles requiring login were reachable; Recast KB article bodies beyond the KB index were not fetched (index itself documents the product's surface structure — A for structure); Analytic Partners evidence is product/solution-page level, not operational docs (assertion strength reduced accordingly). Keen and MassTer unreachable — any claims about those products are absent.

## Product A — Recast

Observations (layer A unless noted):

- Self-positioning: "Marketing planning & analysis infrastructure", "Powered by a proprietary Bayesian MMM". Product lines: Recast MMM, Forecasting & Planning, GeoLift by Recast, Reports Library.
- Model claims: "Time-varying ROIs, channel interactions, promotional spikes, multi-stage funnels" — the model handles non-stationary channel performance and multi-step conversion funnels (signup → activation → revenue) modeled per stage.
- Experiment loop: GeoLift — "Plan tests, pick treatment markets, build synthetic controls, and read results. Every lift finding feeds back into your MMM to sharpen its estimates over time." Experiment design and analysis is an in-product surface.
- Planning tools: "Build powerful forecasts, plans & scenarios"; "Optimize budgets across every channel and constraint — Get the optimal allocation under your real-world caps and floors. See exactly how to shift spend to maximize incremental revenue."
- KB structure (A — surface inventory): Insights (Overview, Single Channel Pages, All Channels), Planning Tools (Optimizer, Forecaster, Goals), Reporter, The Refresh Tracker, Geolift by Recast, How To Guides, Implementation with Recast, Data Guide, Recast for Data Scientists, Troubleshooting, Reporting Standards/Glossary, FAQ, Recast API, Recast MCP.
- Validation posture: "Every Recast model is checked against real outcomes, out-of-sample. Performance scorecards show exactly how past forecasts held up" — accuracy dashboards as a first-class surface.
- Delivery model: every deployment "configured for your business" — either with the Recast team or a "Certified Operator" (consulting partner). Testimonial notes "weekly MMM data" refresh cadence (vendor claim, single source — not generalized).
- Extensibility: versioned public APIs and an MCP server; open-source report template library.
- Customers: Fortune 500 / CPG / fintech / pharma / DTC brands.

## Product B — Measured

Observations (layer A):

- Self-positioning: "Media Effectiveness Platform" for enterprise brands. Modules: Media Mix Modeling ("Causal MMM calibrated with incrementality tests"), Incrementality Testing ("automated geo and audience split experiments"), Media Plan Optimizer ("AI-powered scenario planning"), Cross-Channel Dashboard, Benchmarks. Framing: "triangulated measurement" = MMM (portfolio view) + incrementality testing (causal ground truth) + platform attribution (tactical signal).
- MMM definition (official FAQ): "a statistical method that estimates each marketing channel's contribution to sales by analyzing historical spend, sales, and external factor data — typically 2–3 years' worth." Strengths: covers every channel incl. offline/non-addressable, captures long-term effects, privacy-resilient "because it relies on aggregate data, not user-level tracking". Weakness: traditional models measure correlation, not causation.
- Documented process (official FAQ): Data Collection and Validation (weekly, in some cases daily, historical data for any factor expected to relate to sales; media spend/impressions/clicks plus non-media factors: seasonality, special events, economic conditions, weather, competitive activities, pricing, operational data; alignment, gap-filling, outlier removal, QA sign-off) → Modeling (model structure choice; "most models follow a similar multiplicative model structure"; coefficients) → Calculation (regression) → Results and Output (Contribution — also called "Components", "Due-tos", "Decomps"; general approach: simulate expected loss to total sales when a channel is removed from the mix; ROI/ROAS = contribution ÷ spend).
- Baseline sales: sales realized without any media support — the decomposition anchor.
- Optimization (official FAQ): three strategies — max sales for fixed budget, min spend for a sales goal, max spend while maintaining profitable ROI; reallocate from lower mROI to higher mROI until portfolio ROI is maximized; mROI = marginal ROI of the next dollar; real-world constraints (pre-committed sponsorship budgets, demand-capped search, minimum channel budgets) prevent theoretical equalization.
- Model machinery documented: additive vs multiplicative structures; indirect/intermediate models ("model within a model" to handle demand-driven media, e.g. search clicks); Bayesian priors (external known ranges; experiment results enter as priors or coefficient constraints — "Causal MMM"); response functions with diminishing returns; adstock and lag transforms.
- MTA vs MMM (official FAQ): MTA is "bottom-up" — user-level journeys aggregated; MMM is "top-down" — aggregate. MTA cannot address TV, radio, print, podcasts where impressions aren't trackable at user level.
- Market-structure tiers (official FAQ): Open Source (Meta's Robyn, Google's Meridian — "inexpensive… truncated feature set… heavy lifting done by your team"), Agile MMM (semi-automated data infrastructure, standardized model structures, lightweight service), Enterprise MMM (custom cross-sections by product/region/channel; "hefty price tag, usually over $1M annually"; best for brands spending at least $100M annually on marketing) — vendor-educational claims, not asserted in final doc.
- Naming (official FAQ): "Media Mix Modeling" generally addresses paid advertising directly; "Marketing Mix Modeling" quantifies the impact of any and all marketing efforts (PR, sponsorships, promotional pricing, coupons, in-store events).
- Use cases (official FAQ): optimal total media budget; allocation across channels at monthly/quarterly level; forecasting hypothetical scenarios; insight into external factors.

## Product C — Sellforte

Observations (layer A):

- Self-positioning: "The Measurement & Optimization OS for Retail and Ecommerce"; "unifies Marketing Mix Modeling, Incrementality Testing, and Attribution into a single, always-on Operating System"; "true incremental ROAS at the campaign and ad-set level". Framing: "Your attribution says ROAS is 9.0. Your incrementality test says it's 5.0. Sellforte tells you which one is right."
- Three-layer framing: (1) Incrementality Testing = "The Causal Layer" (geo lift tests, conversion lift studies, A/B tests unified in an Experiments Hub; "results feed back into the MMM as Bayesian priors, sharpening accuracy"); (2) MMM = "The Integration Layer" ("always-on Causal Bayesian MMM that fills the gaps experiments cannot cover across every channel and every market, continuously refreshed. It calculates marginal return on the next dollar spent"); (3) Attribution Correction = "The Execution Layer" (calibration multipliers derived from MMM & experiments applied to MTA output).
- MMM outputs (methodology page): base sales (sales without marketing), incremental sales driven by marketing, incremental sales driven by promotions, ROI for each channel and campaign, response curves. MMM defined as "an approach for estimating marketing's incremental sales impact and ROI through time-series analysis".
- Calibration framework: two calibration data types — incrementality tests (conversion lift studies, geo lift tests, shutdown test) and attribution data (ad platform attribution, GA4, multi-touch attribution).
- Validation (methodology page): statistical validation (actual vs predicted sales, MAPE, R2 — a model validation view in the platform) plus output validation (comparing model outputs to incrementality tests and attribution data; stability checks across model updates; forecast accuracy). Explicit statement: "Your model can show green in statistical tests, but generate non-sensical results."
- Closed loop: Measure → Plan → Execute → Track. Approved budget/bid recommendations pushed directly to Meta, Google, TikTok via API ("You confirm every change before it goes live, nothing is applied automatically"); outcomes measured "against a modeled counterfactual" and fed back into the model.
- Non-media drivers: promotions, weather, seasonality, major events modeled explicitly; promotion-driven sales separated from media-driven sales (grocery/fashion emphasis). Multi-market: separate models per country/region with consistent methodology; multi-brand within one instance.
- Positioning vs traditional MMM (FAQ): "Traditional Marketing Mix Modeling is delivered as a consulting engagement… results are presented in a report once or twice a year… Sellforte is an always-on MMM platform, not a consulting study. The model runs continuously, ingests new data automatically, and delivers updated incremental ROAS… on a daily cadence." (vendor claim on cadence — single source)
- Audiences: agencies as solution segment; performance marketing, insights & analytics roles; "for in-house analytics teams… your data scientists have full access to your model configs."

## Product D — Analytic Partners

Observations (layer A, product-page level only — no operational docs):

- Consulting-heritage enterprise (25 years; multiple analytics-firm acquisitions). Platform: GPS-Enterprise (GPS-E), under a "Commercial Analytics" umbrella that "fuses information from marketing, sales, operations, finance".
- MMM as a named solution line: "Level up your MMM with models that integrate external factors to enable forward-looking decisioning." Other solution lines: Incrementality Testing, Brand Impact, Pricing Optimization, Customer Segmentation.
- Market-category name evidence: "Gartner® Names Us a Leader… 2025 Magic Quadrant™ for Marketing Mix Modeling Solutions" — the analyst market category itself is "Marketing Mix Modeling Solutions" (B — corroborates the directory leaf naming).
- UI evidence from platform screenshots (A for surface existence): scenario/plan creation; scenario cards ("budget optimization", "offset headwinds", "portfolio optimization", "campaign timing", "budget cut", "growth target"); forecasting; multi-KPI outputs (CAC, LTV, margins, payback) for finance alignment.
- Role framing: Finance ("measure the financial impact of marketing activations… aligning budgets with CAC, LTV, margins, payback"), Marketing, Analytics ("models tailored to your unique strategy… analytics transparency"). Human-services emphasis: "dedicated change agents embed themselves deeply in your business".
- This product evidences the scenario-planning-first pole: the platform's center of gravity is decision scenarios over a measured/estimated model, delivered with heavy services.

## Cross-product Comparison

| Dimension | Recast | Measured | Sellforte | Analytic Partners |
|---|---|---|---|---|
| Measured subject | client's own marketing (channels/campaigns) → revenue | client's own media portfolio → incremental sales | client's own retail/ecommerce marketing → incremental sales/GMV | enterprise's commercial decisions incl. marketing → sales/ROI |
| Data shape | aggregate historical time series (Bayesian fit) | aggregate historical weekly/daily (vendor claim) + experiment results | aggregate time series per market; promotions/weather/events as drivers | enterprise data across marketing/sales/ops/finance |
| User identity | none (no user-level journeys) | explicitly none — "aggregate data, not user-level tracking" | none; MMM layer is identity-free; identity only in the corrected-attribution layer | not surfaced |
| Model output | contribution/ROI, time-varying ROI, response behavior, multi-stage funnels | Contribution/Decomp, baseline vs media sales, ROI/ROAS, response curves | base vs incremental sales split, per-channel/campaign ROI, response curves | ROI, scenario outcomes, forecasts |
| Experiment linkage | GeoLift in-product, feeds MMM | incrementality tests calibrate MMM (priors/constraints) | geo lift/conversion lift/shutdown tests as Bayesian priors | separate Incrementality Testing solution line |
| Optimization/scenario | Optimizer with caps/floors + Forecaster + Goals | Media Plan Optimizer (mROI reallocation, constraints) | Optimizer + budget simulation + activation into ad platforms | scenario cards, portfolio optimization, budget scenarios |
| Validation surface | out-of-sample holdout accuracy, performance scorecards, accuracy dashboards | QA of data; priors anchored to experiments (docs stress MMM fragility) | model validation view: actual vs predicted, MAPE, R2, stability, forecast accuracy | not documented at this tier |
| Refresh | "Refresh Tracker" + on-demand refresh (testimonial: weekly) | continuous/test-calibrated (cadence not documented) | "always-on… continuously refreshed" (vendor claim) | not documented at this tier |
| Delivery | configured with vendor team or Certified Operator | services-heavy enterprise | SaaS + dedicated CSM/data scientist | consulting-embedded, platform-enabled |
| Extras (vendor-specific) | MCP server, API, Reports Library, multi-stage funnel modeling | Benchmarks/competitive intelligence, audience split tests, readiness assessment | attribution-correction multipliers, Media Buyer Agent activation, multi-market model registry, Full iROAS | ROI Genome, GPS-E, Commercial Analytics umbrella, Brand Impact/Pricing lines |

Cross-product commonalities (layer B):

- Every sampled product measures the advertiser's own marketing, on aggregate historical time-series data, with a fitted model whose outputs are per-driver contribution and channel-level return (ROI/ROAS/marginal return).
- Every sampled product pairs the model with some budget-allocation decision support (optimizer, scenario planner, or recommendations).
- Every sampled product has some connection to incrementality experiments — bundled in-product (Recast, Sellforte, Measured) or as a sibling solution line (Analytic Partners). The experiment→model feedback direction is consistently stated.
- Every sampled product surfaces model-quality machinery (validation, out-of-sample checks, calibration) — marketing the model's trustworthiness is a structural concern of this Type.
- None of the sampled products operates on user-level identity in the MMM layer.
- Multiple sampled products include non-media drivers (promotions, seasonality, weather, events, pricing) alongside media spend.

## Canonical Model

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The aggregate marketing-spend-and-outcome record of the organization being measured.** The organization's own marketing investments by channel (and typically non-media drivers: promotions, seasonality, pricing, events) and its business outcome (sales/revenue/KPI), held as historical time series at aggregate level — no user-level identity. Remove → there is nothing to model (the app becomes an empty framework); the identity-free aggregate grain is also the Type's privacy stance.
2. **The estimated mix model.** A fitted statistical/causal model of that data that expresses how aggregate spend relates to outcome across the whole marketing mix, whose standard outputs are per-driver contribution/decomposition (and, derived from it, channel return estimates such as ROI/ROAS and marginal return). Remove → raw spend reports (Marketing Analytics territory) or a controlled-experiment tool with no model of the whole mix.
3. **The mix-allocation decision purpose.** The model's outputs exist to inform how the marketing budget is allocated across the mix — realized as recommendations, scenario comparisons, or an optimizer; the "mix" in the Type's name is load-bearing. Remove → a marketing econometrics archive with no decision layer.

Jointly-held is load-bearing:
- 1 without 2 = marketing spend reporting (marketing-analytics/BI);
- 2 without 1 = a textbook simulation with no measured subject;
- 3 without 2 = generic budget planning (FP&A territory);
- 2+3 without 1 = a scenario toy detached from the advertiser's actual data.

### L1 — Common Mature Structure

- Baseline vs incremental split (sales without marketing vs sales driven by marketing).
- Response curves / diminishing-returns (saturation) behavior per channel; carryover/adstock and lag treatment in the model machinery.
- Calibration with incrementality experiments (geo lift, conversion lift, holdouts/shutdowns) entering the model as Bayesian priors or coefficient constraints — the "causal MMM" framing of the current market.
- Side-by-side reconciliation with attribution numbers (MMM vs platform/GA4/MTA views; calibration multipliers in one sampled product — see L3).
- Model validation surfaces: actual vs predicted, out-of-sample holdout accuracy, error metrics, stability checks across refreshes, forecast accuracy.
- Scenario planning & budget optimization tooling: what-if budget shifts, constraints (committed budgets, channel minimums, demand caps), optimal allocation under constraints.
- Forecasting (projecting outcome under planned spend).
- Data integration into the marketing stack (ad platforms, warehouses, file import) and multi-market/multi-brand model management.
- Ongoing refresh: the model re-fits as new periods accrue ("always-on" positioning of the current market; refresh trackers in-sample).
- Reporting surfaces for leadership/finance (the finance-facing accountability narrative is consistent across the sample).

### L2 — Variant / Optional Structure

- Methodology family: Bayesian vs classical frequentist regression; multiplicative vs additive structures (documented as alternative model structures, not a Type split).
- Deliverable shape: consulting-delivered periodic study (historical norm; still the enterprise pole) vs always-on SaaS vs in-house build on open-source frameworks (Robyn, Meridian — model libraries rather than managed applications; adjacent to the Type, run by the advertiser's own data scientists).
- Scope naming: "Media Mix Modeling" (paid media focus) vs "Marketing Mix Modeling" (all marketing levers incl. promotions, price, PR) — same machinery, scope variant, per vendor-educational documentation in-sample.
- Output granularity: channel-level canonical; some current products push corrected/marginal returns down to campaign or ad-set level by recombining the mix model with attribution data.
- Industry packaging: retail/ecommerce, CPG, DTC, financial services, QSR, telecom — packaging and driver sets vary.
- Activation: closed-loop execution of recommendations into ad platforms (one sampled product) — optional, not definitional.
- Configuring party: vendor team, certified consulting operator, in-house data scientists, or dedicated CSM — services model varies.

### L3 — Vendor-specific (Research Notes only)

- Recast: GeoLift product name, MCP server, Reports Library, Certified Operators program, performance scorecards framing, multi-stage funnel stitching, time-varying ROI claims.
- Measured: "Triangulated Measurement" branding, Benchmarks/competitive intelligence module, audience split tests, readiness assessment, exact data-history guidance ("2–3 years"), enterprise price/spend thresholds (vendor claims).
- Sellforte: calibration multipliers, Media Buyer/Planner/Experiments Agents, activation into Meta/Google/TikTok, multi-market model registry (separate model per market), Full iROAS formula, Marketing X-Ray module, cadence claims ("daily").
- Analytic Partners: GPS-Enterprise, ROI Genome, Commercial Analytics umbrella, scenario-card UI vocabulary, Gartner MQ positioning.

## Boundary Findings

- **vs Marketing Attribution Platform (pre-hung seam, ratified from this side).** Attribution assigns credit for individual conversions across recorded user-level touchpoint journeys; MMM estimates the spend→outcome relationship from aggregate time series with no user identity at all. The Measured FAQ independently documents the same seam (MTA "bottom-up" user-level vs MMM "top-down" aggregate; MMM covers channels where user-level tracking doesn't exist). Remove the user-level journeys from attribution → it collapses toward MMM's grain but retains per-conversion allocation; remove the estimated mix model from MMM → marketing analytics. Keep both. In the market the two are frequently sold together and sometimes contradict each other — reconciling them (side-by-side views, calibration multipliers) is work products of this Type do, which further evidences they are different deliverables.
- **vs Marketing Analytics Platform (pre-hung seam, ratified from this side).** Marketing analytics consolidates marketing data and reports descriptive KPIs (spend, response, conversion, efficiency) — it does not estimate a causal spend-response model. This pass's evidence corroborates the marketing-analytics pass's finding that MMM is a neighboring layer, not its center: Funnel ships "Measure" (MTA/MMM/incrementality) as a separate product line from its Data Hub; Improvado lists MMM as a use case; the MMM products here consume consolidated data (connectors/warehouses) — they sit above or beside the analytics layer, not inside it. Keep both.
- **vs Digital Experimentation / A/B Testing Platforms.** Experiments impose controlled interventions and measure lift directly; MMM is observational modeling of the whole mix over history. Media incrementality tests (geo lift, conversion lift) are a distinct experiment family aimed at media, and current MMM products bundle their design/analysis because their results calibrate the model. A pure experiment platform with no mix model is not this Type. Directory observation (no change made): media-incrementality testing has no dedicated leaf in the directory — nearest existing leaves (A/B Testing Platform, Digital Experimentation Platform) are product-experimentation-flavored; if a leaf is ever added, the seam is media-channel lift tests vs product/website experiments.
- **vs Budgeting & Forecasting platforms (financial).** FP&A plans money across the business from financial assumptions; MMM derives allocation from an estimated response of sales to marketing spend. The finance audience overlaps (both Types court CFO confidence) and MMM outputs can feed a marketing budget in FP&A — but the modeling object differs entirely.
- **vs Business Intelligence / Dashboard platforms.** MMM is marketing-spend-response semantics with an estimated model; BI is generic. Same drift-zone treatment as the marketing-analytics pass recorded vs BI.
- **vs Marketing Automation / Campaign Management / Email/SMS/Push platforms.** Execution vs measurement — consistent with the marketing-analytics pass's framing. MMM consumes these platforms' spend/activity data; it does not execute campaigns.
- **Naming observation (no directory change).** "Media Mix Modeling" and "Marketing Mix Modeling" are used for the same Type with a documented scope nuance (media = paid advertising; marketing = all levers). The market category itself (Gartner MQ 2025) is "Marketing Mix Modeling Solutions", matching the directory leaf. "MMM" abbreviation is universal. No alias decision needed; scope nuance recorded as variant.

## Uncertainties

- Refresh cadence claims (weekly/daily/always-on) are vendor claims from single sources; not generalized in the final document.
- Typical data-history requirements ("2–3 years") and enterprise price/spend thresholds are vendor-educational claims (Measured FAQ); held in research notes only.
- The exact statistical machinery of any product (specific priors, distributions) was not researched; final document speaks of "fitted statistical/causal model" generically.
- Keen Decision Systems and MassTer unreachable — the scenario-planning pole beyond Analytic Partners and the classic European econometric-software pole are evidenced only indirectly.
- Recast KB article bodies (beyond the index) not fetched; Recast's operational details rest on homepage claims + KB structure inventory.
- Open-source frameworks (Robyn, Meridian) documented only via Measured's FAQ (secondhand); treated as adjacent market shape, not deeply researched.

## Final Synthesis

A Marketing Mix Modeling Application is the advertiser-side application that holds an organization's aggregate historical marketing spend and business outcomes, fits a statistical/causal model of how spend across the marketing mix relates to the outcome, and turns that model into allocation decisions — contributions, channel returns, response behavior, scenario/optimization support. It is identity-free by construction (aggregate data, no user journeys), which is both its privacy resilience and its definitional seam vs attribution. The current market wraps this core in a calibration loop (incrementality experiments feed the model), validation surfaces (the model's trustworthiness is a first-class concern), consolidation plumbing, and — increasingly — activation; and sells it across three delivery shapes (consulting-heritage enterprise, always-on SaaS, open-source framework). The historical norm — a consulting-delivered econometric study producing contribution decompositions and budget recommendations — satisfies the defining core exactly: aggregate data, fitted model, allocation purpose. Nothing modern (cloud, Bayesian machinery, AI agents, dashboards) is required for the Type to be recognizable.
