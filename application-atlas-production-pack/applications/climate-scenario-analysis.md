# Climate Scenario Analysis

## Overview

A **Climate Scenario Analysis** application is the scenario-projection machinery of the climate-risk stack: it holds a set of named climate scenarios — coherent, assumption-bearing descriptions of alternative futures — runs them through projection models against a defined subject such as a portfolio, a set of assets, a business, or a region, and delivers the resulting consequences for each scenario across explicit future horizons, in financially meaningful terms, as a comparison of plausible futures rather than a forecast.

The defining structure is small:

```text
Managed climate scenario set
        ↓ applied to
A defined subject (portfolio / assets / business / region)
        ↓ projected across
Explicit future time horizons
        ↓ producing
Scenario-conditioned consequences
  (physical impacts, transition impacts, financial effects)
        ↓ delivered as
A comparison across scenarios — plausible futures, not forecasts
```

Everything else commonly associated with the category — recognized public scenario frameworks, dual physical-and-transition coverage, stress testing, asset-level geospatial resolution, disclosure alignment — is widespread in current products but is not what makes one a scenario analysis application. The category's vocabulary comes from two authorities: the climate disclosure canon, which expects organizations to describe the resilience of their strategy against different climate-related scenarios including one at or below 2°C, and the central-bank scenario canon, which defines the widely used scenario families (orderly transitions, disorderly transitions, a hot house world, and a "too little, too late" failure) and named pathways such as Net Zero 2050, Delayed Transition, and Current Policies.

The boundary in this domain matters: when a product additionally maintains the subject as a persistent population of risk exposures, keeps assessments as records over time, and drives prioritization, response decisions, and recurring monitoring cycles, it has become a climate risk management application. When a product only computes hazard and loss for assets without the scenario-family structure, it is a physical climate risk engine. When it serves current-state scores without forward-looking projections, it is a climate data product.

## Users & Context

Primary users are the people who must understand how climate futures would affect something they are accountable for:

- financial-institution risk teams, who run portfolio-level scenario analysis and stress tests for internal capital decisions and regulatory climate exercises, often under model-governance scrutiny that demands explainable methods
- investors and asset owners, who want portfolio-level climate risk and resilience metrics aligned to recognized scenario frameworks
- corporate strategy, sustainability, and finance teams, who test the resilience of the business against transition and physical futures and feed scenario results into strategic planning and disclosure

Contributing users:

- analysts who configure scenario runs, bind portfolios or assets, and prepare comparisons
- treasury, capital-planning, and underwriting staff who consume the financial translations (loss, credit, cashflow, earnings impact)
- external consultants and data providers who supply scenarios, models, or delivery services

Secondary audiences:

- boards and executives, who receive resilience summaries under alternative futures
- regulators and supervisors, who prescribe scenario exercises for banks and insurers
- disclosure consumers — investors, auditors, frameworks — who read the scenario-based content that disclosure regimes expect organizations to describe

The work context is exercise-shaped rather than continuous: scenario runs are performed for planning rounds, disclosure cycles, and regulator-prescribed stress tests, and results are compared across scenarios, horizons, and vintages rather than consumed once.

## Core Model

### The Defining Core

Three properties. If any one is removed, the product is no longer recognizable as a climate scenario analysis application:

- **A managed climate scenario set.** The application holds scenarios as selectable, first-class objects: internally consistent bundles of assumptions about how the climate and the response to it evolve — policy stringency and timing, emissions pathways, warming levels, technology and market shifts. Scenarios are commonly drawn from recognized public families and named pathways, and mature products also allow custom or client-specific cases. Without a scenario set, the product is a forecast tool or a hazard model, not scenario analysis.
- **A projection machinery.** The application applies the selected scenarios to a defined subject — a lending or investment portfolio, physical assets and sites, a corporate business structure, or a regional economy — and projects consequences over explicit future horizons. The machinery draws on the model stack that the scenario canon itself is built from: transition pathways from integrated assessment models, chronic climate impacts from earth-system and climate-impact models, acute events from natural-catastrophe models, and macro-financial translation. The subject is the *input configuration* of a projection run; it is not, in this Type, maintained as a living population of risk records. Without the machinery, the product is a scenario library or data publication.
- **A comparative, exploratory posture.** Results exist per scenario and are presented side by side across scenarios and horizons. The insight is the *divergence between futures* — how outcomes change if policy is early versus delayed, warming contained versus severe. The output is deliberately framed as a range of plausible, hypothetical futures under stated assumptions, not as a prediction. Without the comparison, a single-scenario projection is just a conditional forecast.

### Standard Capabilities of Mature Products

These are common across mature products and make the machinery practical, though they do not define the Type:

- **Recognized scenario anchoring** — scenario libraries aligned to public frameworks (the central-bank families and named pathways; IPCC-consistent emissions/warming pathways), optionally extended with proprietary scenarios.
- **Dual risk-family coverage** — transition impacts (policy, carbon pricing, technology, demand shifts) alongside physical impacts (acute hazards and chronic shifts), or an explicit single-family specialization.
- **Financial quantification** — translation of projected consequences into business terms: damage and loss, credit and cashflow metrics, earnings impact, exposure to carbon prices, portfolio value effects.
- **Stress testing** — running the subject through scenario cases for capital and regulatory purposes, including regulator-prescribed deterministic cases and probabilistic simulation approaches.
- **Asset- and portfolio-level resolution** — geospatial binding of exposures to locations, with results traceable down to assets or components, and aggregateable to portfolio or enterprise views.
- **Disclosure alignment** — outputs structured to support climate-related disclosure regimes, which expect organizations to describe strategic resilience under climate scenarios.
- **Multi-surface delivery** — the same scenario results served through an interactive platform, data and API feeds for the organization's own systems, and generated reports.
- **Screening before depth** — a high-level pass across the subject to locate the most-affected exposures, followed by deeper analysis of those.
- **Option exploration** — testing how responses (adaptation measures, transition moves) would change projected outcomes; the results feed decisions that are managed elsewhere.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:                Scenario source
Realizations:           public framework families (central-bank / IPCC),
                        proprietary internally-developed scenarios,
                        hybrid, client-defined cases

Concept:                Subject binding
Realizations:           lending and investment portfolios, asset and site
                        registers, corporate business structures,
                        regions and sovereigns

Concept:                Projection engine
Realizations:           proprietary climate-and-damage model chains,
                        licensed public pathway data + in-house translation,
                        engineering-based hazard-to-damage engines

Concept:                Output carrier
Realizations:           interactive platform, data/API feeds, generated
                        reports, consulting-delivered studies
```

A reader who encounters only one implementation — for example, a data platform serving portfolio climate metrics under public scenarios — should still be able to recognize a consulting-delivered, financially quantified corporate scenario study as the same Type from the core model.

## How It Works

Scenario analysis runs as a repeatable cycle rather than a one-off study.

**1. Choose the scenario set.** The user selects which futures to examine — typically a small set spanning the risk space (an orderly transition, a delayed or disorderly one, a high-warming world), drawn from the scenario library or defined as custom cases. The choice of set determines everything downstream, and the disclosure canon's expectation of at least one low-warming case shapes the default composition.

**2. Bind the subject.** The exposures under analysis are loaded and located: portfolio holdings mapped to issuers and assets, physical sites geocoded, business units and value chains structured. This is configuration for a run, not the creation of a managed risk population.

**3. Run the projections.** For each scenario and horizon, the machinery translates the scenario's assumptions into consequences for the subject: hazard conditions at asset locations under the scenario's warming pathway, transition costs and demand shifts under its policy pathway, and the resulting financial effects. Depending on the product this runs through an embedded model chain, licensed public pathway data with in-house translation, or an engineering-based hazard engine; probabilistic simulation may be layered on for stress-testing purposes.

**4. Translate into business terms.** Raw hazard and pathway outputs are converted into the metrics the audience acts on: damage and loss, credit and cashflow impact, earnings effects, exposure to carbon prices, portfolio value at risk under each future.

**5. Compare across scenarios and horizons.** The defining analytical step: results are laid side by side to show how outcomes diverge between futures — which exposures deteriorate only in a disorderly world, which physical impacts arrive even in an orderly one, where the ranges are wide and therefore the most uncertain.

**6. Deliver and feed decisions.** Results are packaged as platform views, reports aligned to disclosure frameworks, and data feeds into risk, finance, or planning systems. The scenario results inform strategy, capital allocation, and disclosure narratives — but the decisions, response tracking, and reassessment cadence belong to the surrounding management processes (climate risk management, adaptation planning, enterprise risk), which typically re-run the analysis on their own cycles.

A practical note on tool boundaries: the machinery is frequently split between systems. Scenario authorities publish pathway and impact data; projection products consume that data or maintain their own model chains; management platforms consume the resulting metrics. Mature products accommodate this by being data-consumable (APIs, feeds) as well as platform-delivered.

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Scenario library / configuration

Where futures are selected and managed.

- typical information: scenario families and named pathways, their assumptions and parameters, available horizons, custom cases
- primary actions: select scenarios for a run, inspect assumptions, define custom cases

### Subject / portfolio binding

Where the thing being analyzed is assembled.

- typical information: imported holdings or assets, their attributes and locations, mapping coverage
- primary actions: import or connect exposure data, geocode assets, organize into groups

### Projection workspace / results view

Where scenario runs produce their outputs.

- typical information: per-scenario, per-horizon results for the bound subject, hazard and transition breakdowns, drill-down to assets or holdings
- primary actions: run or re-run projections, adjust scope, drill into drivers

### Comparison explorer

The surface where divergence between futures becomes visible.

- typical information: side-by-side scenario results, changes across horizons, ranges and spreads between futures
- primary actions: switch scenarios, compare horizons, isolate the exposures driving the largest differences

### Stress-test surface

The exercise-shaped surface for capital and regulatory use.

- typical information: prescribed scenario cases, portfolio-level aggregates, simulation outputs
- primary actions: execute stress cases, produce exercise-aligned outputs

### Financial impact view

The business-translation surface.

- typical information: loss, credit, cashflow, and earnings metrics under each future; carbon-price exposure
- primary actions: switch metrics, aggregate and disaggregate, export

### Report / disclosure generator

The output surface for disclosure and governance audiences.

- typical information: framework-aligned scenario narratives, results tables, method and assumption references
- primary actions: generate, customize, and export reports

### Data delivery surface

For organizations consuming results in their own systems.

- typical information: datasets and metrics available by feed or API
- primary actions: configure delivery, integrate into internal risk and finance tools

## Important Rules / Behaviors

### Scenarios are hypothetical constructs, not forecasts

The framework canon is explicit that scenario analysis explores plausible futures under stated assumptions and is not designed to deliver precise outcomes. Mature products carry this posture through their outputs — ranges and cross-scenario comparisons rather than single-point predictions — and through their language.

### The divergence is the insight

A scenario run that produces one number has not done scenario analysis. The defining behavior is comparative: what changes between an orderly and a disorderly transition, between contained and severe warming. Products are organized around making that comparison visible.

### Traceability underpins defensibility

Because results feed capital decisions and regulatory exercises, the chain from scenario assumptions through models to each output figure must be inspectable. In financial-institution contexts this extends to formal model-governance scrutiny: methods that cannot be explained cannot be approved.

### The subject is input, not state

In this Type, the analyzed portfolio or asset set is a configuration of an analysis run. It is not maintained as a population of risk assessments with owners, decisions, and monitoring histories — that is the surrounding management process's role. Products that make the population persistent and managed have crossed into climate risk management.

### Results must be legible to capital

Scenario projections earn their place by translating into the metrics decision-makers already use — loss, credit, cashflow, earnings, value. Hazard projections that stop at physical units remain inputs rather than finished outputs.

### Finer granularity carries wider caveats

The scenario canon itself warns that results should be handled with care at the most granular levels, and products inherit this: asset-level and component-level projections are presented with uncertainty context rather than as precise point values.

## Variants

Common shapes of the Type:

- **Financial-institution portfolio carriers** — lending and investment portfolios as subjects; stress testing, credit and loss translation, and model-governance defensibility are prominent; often serve regulatory climate exercises.
- **Investor data-platform carriers** — scenario-based climate risk metrics served as data at portfolio scale, anchored to public frameworks, alongside broader climate datasets.
- **Corporate strategy carriers** — the corporate business (and its transition exposure) as subject; financially quantified scenario results feeding strategy, transition planning, and disclosure.
- **Asset and real-asset carriers** — physical assets and infrastructure as subjects; hazard-engine projections of damage and loss under warming pathways; used for due diligence and resilience investment.
- **Emphasis variants** — physical-led versus transition-led versus integrated dual coverage; long-horizon versus short-horizon (regulator-style) focus; proprietary versus public scenario anchoring.
- **Computation variants** — deterministic scenario runs versus probabilistic simulation; embedded model chains versus licensed pathway data with in-house translation.
- **Carrier variants** — standalone platform, data-provider suite module, engine consumed by other systems, consulting-delivered studies.
- **Extensions** — nature- and biodiversity-related scenario analysis as an adjacent coverage layer in some products.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Climate Risk Management | surrounding process layer | adds a managed exposure population, maintained risk assessments, and the management loop (prioritization, response decisions, monitoring, disclosure cycles); scenario analysis is the projection machinery that feeds it |
| Physical Climate Risk Platform | engine-side sibling | computes physical hazard exposure and loss for assets without the scenario-family structure across futures; often supplies machinery that scenario analysis products embed or consume |
| Climate Adaptation Planning | downstream consumer | holds the managed adaptation plan (goals, actions, owners, progress); scenario analysis supplies the forward-looking evidence that justifies it |
| Climate data products | drift boundary | serve current-state scores, footprints, and hazard ratings without forward-looking scenario machinery; remove the scenarios and horizons and a scenario product becomes one of these |
| ESG Reporting / Disclosure Management | adjacent output layer | produces disclosure reports; scenario analysis produces the forward-looking analytical content those reports must describe |
| Financial Risk Management Platform | FI-side sibling machinery | runs stress tests on market, credit, and liquidity positions under macro-financial scenarios; climate scenario analysis brings the climate-specific scenario content, and FI climate stress tests bridge the two |
| Energy Forecasting Platform | different domain | projects power-market demand, supply, and prices; not climate-future scenario families over a subject's exposures |
| Carbon Accounting Platform | adjacent measurement | quantifies actual and attributable emissions; scenario analysis projects consequences of alternative futures rather than measuring present emissions |

The most important boundary is with climate risk management: the products overlap heavily in the market, and several vendors serve both labels from one platform. The structural test is whether the application's center of gravity is *running and comparing futures* (scenario analysis) or *keeping an organization's risk picture alive over time with decisions recorded against maintained assessments* (climate risk management). The second most important is with climate data products: forward-looking scenario conditioning is what separates the two, and suites commonly ship both kinds of capability side by side.

## Representative Products

- **Jupiter Intelligence** — decision-grade physical climate risk analytics for financial institutions: asset-level multi-peril projections under emissions scenarios across long horizons, financial translation to credit, loss, and cashflow metrics, stress testing, adaptation ROI, and a model-governance posture
- **XDI (Cross Dependency Initiative)** — physical climate risk for asset portfolios: screening, asset-level deep dives, portfolio stress testing across recognized scenario families (RCP, SSP, NGFS) including regulator-prescribed and probabilistic cases, with platform, API, and report delivery
- **Risilience (Riise platform)** — corporate and financial-institution scenario analysis: physically and financially quantified scenario outcomes across transition and physical risk through one lens, with risk screening, digital-twin modeling, and transition planning
- **MSCI Climate (Climate Scenario Analysis)** — investor-facing scenario analysis product quantifying financial climate risks under NGFS and IPCC scenarios at portfolio scale, within a broader climate data and analytics suite
- **Carbon4 Finance** — boundary sample: financial-institution environmental data (verified footprints, Paris-alignment metrics, hazard and vulnerability scores) illustrating the data-product pole where scenario projection machinery is absent

## Sources

Research date: **2026-09-07**

Product surfaces:

- Jupiter Intelligence — https://www.jupiterintel.com/
- XDI — https://xdi.systems/
- Risilience — https://risilience.com/
- MSCI Climate Solutions — https://www.msci.com/data-and-analytics/climate-solutions
- Carbon4 Finance — https://carbon4finance.com/

Framework authorities:

- NGFS Scenarios Portal (Network for Greening the Financial System) — https://www.ngfs.net/ngfs-scenarios-portal/
- TCFD Recommendations (Task Force on Climate-related Financial Disclosures; monitoring now with the IFRS Foundation) — https://www.fsb-tcfd.org/recommendations/

> Sourcing limitation: deep help-center or user-manual documentation for the sampled products was not reachable in this research pass; evidence comes from official product pages and two official framework portals. Accordingly, this document states no precise operational figures (horizon years, data resolutions, scenario counts, or vendor-stated metrics), describes cross-product findings at commonality strength, and keeps product-specific mechanisms and named modules out of the general description. Two known scenario-analysis providers (a pension-sector analytics vendor and a major index-data provider) were dropped from the sample after repeated fetch failures; no claims are made about them.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
