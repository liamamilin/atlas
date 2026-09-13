# Physical Climate Risk Platform

## Overview

A **Physical Climate Risk Platform** computes how climate-change-driven natural hazards would translate into damage and financial impact for physical assets. It holds located assets — a single property or a portfolio of thousands — as the analyzed population, runs hazard projections under climate-change scenarios across forward time horizons, and produces asset-level results: damage and loss estimates, financial metrics, and risk scores that roll up to portfolio views. Results are delivered through an interactive, map-centric platform, data and API feeds, and disclosure-aligned reports.

The defining structure is small:

```text
Located assets (single asset → large portfolios)
        ↓ combined with
Climate-conditioned hazard projections
  (multi-hazard, under climate scenarios, across time horizons)
        ↓ run through
Hazard-to-impact computation
  (hazard × asset exposure × vulnerability)
        ↓ producing
Asset-level impact results
  (damage, loss, financial metrics, scores)
        ↓ delivered as
Platform views, data/API feeds, reports
```

Everything else commonly associated with the category — financial translation into credit and cashflow metrics, model-governance approval postures, AI assistance, named disclosure-framework certifications — is widespread in current products but is not what makes one a physical climate risk platform.

The category sits on the computation layer of the climate-risk stack. When a product additionally runs the organization's risk process over maintained assessments — prioritization, response decisions, monitoring cycles, disclosure programs — it has become a climate risk management application. When its center of gravity is a managed set of climate futures compared side by side, it is a climate scenario analysis application. When it serves hazard scores without computing them for the customer's own assets, it is a data product. And when it computes event-based insurance losses under the current climate for pricing and reserving, it is catastrophe-modeling territory — the ancestor this Type grew out of.

## Users & Context

Primary users are the people who must price, lend against, underwrite, or own physical assets whose value depends on how climate hazards evolve:

- **banks and lenders**, who screen collateral and lending portfolios, run climate stress tests for regulators, and feed physical risk into credit decisions and origination
- **insurers**, who assess exposure of underwriting portfolios and steer risk accumulation
- **asset managers, private equity, and real estate investors**, who run due diligence before acquisitions and monitor portfolio exposure across the investment cycle
- **infrastructure and industrial asset owners**, who understand where their sites are exposed and what adaptation could buy

Contributing users:

- analysts who upload portfolios, configure scenario parameters, and prepare reports
- sustainability and risk teams who consume the results for disclosure and internal briefings
- consultants and advisors who run assessments on behalf of clients

Secondary audiences:

- regulators and supervisors, who prescribe climate stress-test exercises for banks and insurers
- boards and investment committees, who receive portfolio risk summaries
- disclosure consumers — auditors, investors, framework regimes — who read the physical-risk content that reports must contain

The work context is transaction- and exercise-shaped rather than a continuous program: an assessment is run for a due-diligence decision, an origination check, an underwriting review, a regulatory stress test, or a reporting cycle. The same computation machinery serves all of these; what happens with the results — the credit decision, the investment committee, the adaptation budget — lives in the surrounding processes.

## Core Model

### The Defining Core

Three properties. If any one is removed, the product is no longer recognizable as a physical climate risk platform:

- **A located-asset population.** The analyzed things are physical assets bound to geographic locations — buildings, sites, infrastructure, facilities — held individually or as portfolios. Assets enter the system by search (address, coordinates, map selection), upload (portfolio files), entity mapping (a company's asset footprint), or drawn geometries (a rail line, a plant area). The asset, not the company or the region, is the unit of analysis; company and sector views are aggregations over assets. Without this, the product is a hazard map or a data feed with no subject.
- **Hazard-to-impact computation.** The platform computes rather than serves: it combines hazard data with each asset's exposure and vulnerability to produce impact results — damage, loss, financial metrics, and/or risk scores — traceable down to the asset and, in mature products, to the components within it. Without computation, the product is hazard data licensing.
- **Climate-change conditioning.** Impacts are computed under climate-change projections — scenarios of future emissions and warming, across explicit time horizons from near-term to multi-decade — so results show not only today's exposure but how risk evolves as the climate changes. Without this, the product is a current-climate hazard-scoring or catastrophe-modeling tool: the ancestor computation, not a climate risk platform.

### Standard Capabilities of Mature Products

These are common across mature products and make the computation useful, though they do not define the Type:

- **Financial translation** — converting physical impact into the terms decisions are made in: expected loss, damage cost, credit and cashflow impact, P&L effect. Some products deliver scores and ratings instead of, or alongside, currency figures.
- **Multi-hazard coverage** — catalogs spanning acute perils (flood, wind and tropical cyclone, wildfire, heat, hail, subsidence) and chronic shifts (water stress, sea-level rise, drought-class hazards); hazard breadth varies by product, and some offer deep single-peril models.
- **Portfolio aggregation and screening** — rolling asset results up to portfolio views, visualizing the risk distribution, and flagging the most-at-risk assets for deeper analysis.
- **Traceability and defensibility** — the trust mechanism of the category: results traceable to the point of failure within an asset, assumptions that can be inspected, validation against observed events, and formal model-risk-management reviews where financial-institution use demands it.
- **Stress testing** — running portfolios through prescribed deterministic scenario cases and probabilistic simulation for regulatory exercises and internal capital work.
- **Disclosure alignment** — report outputs structured against climate disclosure frameworks and regulatory regimes (the TCFD/ISSB lineage, EU taxonomy and CSRD-class regimes, jurisdiction-specific rules).
- **Adaptation option analysis** — testing what risk reduction adaptation measures would achieve and at what cost, so resilience investment can be prioritized; the results feed decisions managed elsewhere.
- **Asset discovery** — mapping a company's or portfolio's real-world asset footprint as the substrate for risk analysis.
- **Current-state hazard assessment alongside** — many platforms also assess present-day natural-hazard exposure, including non-climate perils such as earthquake, as part of the same platform.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:              Analyzed population
Realizations:         uploaded portfolios, searched single assets,
                      entity-mapped corporate footprints,
                      user-drawn areas and lines, prescored zones

Concept:              Hazard evidence
Realizations:         proprietary climate-and-damage model chains,
                      downscaled multi-model projections with
                      proprietary vulnerability data,
                      engineering-based hazard engines,
                      reinsurer-heritage hazard datasets

Concept:              Impact output
Realizations:         currency-denominated loss metrics, damage
                      estimates, risk scores and ratings,
                      business-interruption / downtime metrics

Concept:              Delivery carrier
Realizations:         interactive SaaS platform, enterprise API,
                      on-demand single-asset assessment,
                      off-the-shelf reports, managed analysis
```

A reader who encounters only one implementation — for example, a self-serve platform where portfolios are uploaded and loss reports downloaded — should still be able to recognize a reinsurer-operated hazard-rating service or an engineering-delivered portfolio analysis as the same Type from the core model.

## How It Works

**1. Assemble the assets.** The user brings the population under analysis into the platform: searching individual locations by address or coordinates, uploading a portfolio file, connecting entity data to map a corporate footprint, or drawing areas and lines for assets that are not points. Assets are saved and organized as reusable portfolios.

**2. Select hazards, scenarios, and horizons.** The computation is parameterized: which hazards to assess, under which climate scenarios, across which forward time horizons, at what depth. In some products these are per-run selections; in others they are bundled into data editions. This is configuration of a computation, not the assembly of a set of alternative futures to be compared — that distinction separates this Type from climate scenario analysis.

**3. Run the computation.** For each asset, the platform combines the hazard conditions at its location under the selected scenario and horizon with the asset's exposure characteristics and vulnerability, and computes the impact: damage, loss, and derived metrics. Depending on the product this runs through a proprietary model chain, an engineering-based hazard engine, or licensed projections translated in-house; probabilistic simulation may be layered on for stress-testing purposes.

**4. Translate into decision terms.** Raw physical results are expressed in the currency of the consuming decision — financial loss, credit and cashflow impact, P&L effect — or as standardized risk scores and ratings where the workflow calls for comparable grades rather than figures.

**5. Screen and drill down.** Portfolio views surface the risk distribution and flag the most-exposed assets; the user drills into individual assets and, in mature products, into the components where failure would originate. Aggregation, filtering, and portfolio-to-portfolio comparison support steering at scale.

**6. Deliver the results.** Outputs leave the platform as interactive views, generated reports aligned to disclosure frameworks, and data delivered by API into the customer's own systems — credit engines, underwriting workflows, investment processes, disclosure production. The decisions themselves are made elsewhere; the platform's job is to make the physical-risk evidence computable, inspectable, and deliverable.

A practical note on tool boundaries: the computation is frequently split between systems. Hazard and climate model chains may be operated by the platform vendor, licensed from data providers, or consumed by other systems through APIs; management platforms that run the organizational risk process commonly embed or ingest this engine's outputs. Mature products accommodate all three postures.

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Map-centric asset view

The platform's home surface, organized around geography.

- typical information: assets and portfolios on a base map, hazard layers, risk colorings
- primary actions: search a location, inspect an asset's hazard exposure, toggle hazard layers and map settings

### Asset assessment view

The detailed surface for a single asset.

- typical information: per-hazard scores and ratings, hazard zones, scenario and horizon results, component-level detail where offered, method references
- primary actions: run or re-run assessment, switch scenario or horizon, inspect traceability detail

### Portfolio screening view

The at-scale surface across the whole population.

- typical information: portfolio risk distribution, rankings, red-flag identifications, per-hazard breakdowns
- primary actions: filter and sort, flag assets for deep dives, aggregate portfolios; some products also support comparing one portfolio against another

### Scenario / parameter configuration

Where the computation is set up.

- typical information: hazard selections, climate scenarios, time horizons, computation depth options
- primary actions: configure a run, save parameter sets, launch computation

### Financial impact view

The business-translation surface.

- typical information: loss and damage figures, credit/cashflow/P&L metrics, score-to-financial mappings
- primary actions: switch metrics, aggregate and disaggregate, export

### Report / export generator

The output surface for disclosure and stakeholder audiences.

- typical information: framework-aligned report content, assessment summaries, method and data references
- primary actions: generate and customize reports, download in document or data formats

### Data delivery surface

For organizations consuming results in their own systems.

- typical information: available scores, metrics, and datasets via API
- primary actions: configure queries, integrate into credit, underwriting, or risk systems

## Important Rules / Behaviors

### Results are computed, not served

The defining behavior of the Type: the platform runs hazard data through asset exposure and vulnerability for the customer's own assets. A product that only serves pre-computed scores or hazard layers has left the Type and become a data product.

### Traceability is the trust mechanism

Because results feed credit decisions, underwriting, and regulatory exercises, the chain from hazard data through method to each output figure must be inspectable. Mature products trace results to the failing component within an asset, document assumptions, validate against observed events, and submit to formal model-risk-management review. Outputs that cannot be explained cannot be approved.

### Scenarios are parameters, not managed futures

Climate scenarios enter as configuration of the computation. The product's center of gravity is the asset-level impact result, not a comparison across alternative futures; a product organized around a managed scenario set and cross-future comparison has crossed into climate scenario analysis.

### The asset list is configuration, not a managed risk population

Portfolios persist and are reused, but the platform does not maintain the organizational risk process over them — no assessment owners, response decisions, or monitoring cycles. A product that adds that structure has become a climate risk management application.

### Finer granularity carries wider caveats

Asset-level and component-level results are presented with uncertainty context; the underlying climate science warns that precision degrades at the most granular levels, and mature products inherit that posture rather than presenting point values as certainties.

### The frame is physical

The Type covers physical hazards — acute events and chronic shifts. Transition risk (policy, technology, market change) is out of frame; products that assess both families through one process belong to the climate risk management and scenario analysis territory.

## Variants

Common shapes of the Type:

- **Banking and lending carriers** — collateral and lending portfolios as the population; origination screening, stress testing, and credit-metric translation are prominent; model-governance defensibility expected.
- **Insurance carriers** — underwriting portfolios and hazard accumulation; often reinsurer-heritage data and rating scales.
- **Real estate and investment carriers** — due diligence and investment-cycle integration; adaptation cost and ROI analysis for owned assets.
- **Infrastructure and government carriers** — public assets and municipal exposure; adaptation planning support and public-purpose data releases.
- **Engine-posture variants** — proprietary embedded model chains versus licensed hazard data with in-house translation; deterministic versus probabilistic computation.
- **Delivery variants** — self-serve SaaS platforms, API-first data delivery, on-demand credit-based single-asset assessment, off-the-shelf reports, and managed analysis delivered by the vendor or resellers.
- **Resolution variants** — asset-level depth (down to components), user-drawn areas and lines for linear or areal assets, and prescored administrative zones for regional views.
- **Hazard-emphasis variants** — all-peril breadth versus deep single-peril models; high-resolution wildfire modeling is a recurring specialization.
- **Impact-framing variants** — currency-denominated loss metrics versus score/rating scales versus time-denominated downtime and business-interruption metrics.
- **Module variants** — current-state-only hazard editions and non-climate natural-hazard coverage (earthquake-class perils) riding within climate-conditioned platform families.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Climate Risk Management | process layer above | runs the organization's climate risk process — managed exposure population, maintained assessments, prioritization, response decisions, monitoring, disclosure cycles; this Type computes the physical-risk evidence such a process consumes |
| Climate Scenario Analysis | projection-machinery sibling | holds a managed scenario set as first-class objects and compares plausible futures across scenarios and horizons; here scenarios are computation parameters and the asset-level impact is the center |
| Climate data products | drift boundary | serve hazard scores, footprints, and ratings without computing hazard-to-impact for the customer's own assets; remove the computation and a platform becomes one of these |
| Catastrophe modeling (adjacent territory) | ancestor computation | event-based probabilistic loss for insurance pricing and reserving under the current climate; this Type is climate-change-conditioned and serves lending, investment, ownership, and disclosure decisions |
| Nature Risk Management | adjacent risk family | assesses ecosystem, biodiversity, and ecosystem-service state and dependencies; this Type assesses climate hazards; platforms may bundle both as separate editions on one data spine |
| ESG Disclosure Management | adjacent output layer | produces disclosure reports against frameworks; this Type produces the physical-risk analytical content those reports describe |
| Climate Adaptation Planning | downstream consumer | holds the managed adaptation plan — goals, actions, owners, progress; this Type supplies the risk-reduction and cost-benefit evidence that justifies it |
| GIS / hazard mapping tools | interface cousin | visualize hazard zones and layers; without asset-bound impact computation they are data surfaces, not risk platforms |

The most important boundary is with climate risk management: the products overlap heavily in the market, and several vendors serve both labels from one platform. The structural test is whether the application's center of gravity is *computing asset-level physical impact evidence* (this Type) or *keeping the organization's risk picture alive over time with decisions recorded against maintained assessments* (climate risk management). The second most important is with climate scenario analysis: scenarios as computation parameters versus scenarios as managed, compared futures.

## Representative Products

- **XDI (Cross Dependency Initiative)** — asset-portfolio physical climate risk with engineering-based methods: screening, asset-level deep dives traceable to the point of failure, portfolio stress testing across recognized scenario families, adaptation-prioritization analysis, delivered as platform, API, and reports
- **Jupiter Intelligence** — decision-grade physical risk analytics for financial institutions: asset-level multi-peril projections under emissions scenarios, financial translation to credit, loss, and cashflow metrics, stress testing, adaptation ROI, and a model-governance posture
- **Climate X (Spectra)** — self-serve physical climate risk analytics: search or upload assets, select climate scenario parameters, download asset- and portfolio-level financial loss reports; enterprise API for portfolio-scale computation, with adaptation-cost analysis as a sibling product
- **Munich Re Location Risk Intelligence** — reinsurer-heritage modular platform: hazard scores and ratings across natural-hazard and climate editions, financial-impact and company-level editions, portfolio management with aggregation and comparison, on-demand single-asset assessment, API delivery
- **One Concern** — AI and catastrophe-modeling heritage platform: digital-twin computation of business-interruption vulnerability from infrastructure dependencies, with resilience benchmarking across properties, companies, and sectors

## Sources

Research date: **2026-09-09**

- XDI — https://xdi.systems/
- Jupiter Intelligence — https://www.jupiterintel.com/
- Climate X — https://climate-x.com/ , https://climate-x.com/spectra
- Munich Re Location Risk Intelligence — https://www.munichre.com/rmp/en/products/location-risk-intelligence.html
- One Concern — https://www.oneconcern.com/ , https://oneconcern.com/en/about/

> Sourcing limitation: deep help-center or user-manual documentation for the sampled products was not reachable in this research pass; evidence comes from official product pages. Accordingly, this document states no precise numeric claims (asset counts, hazard counts, data resolutions, horizon years, or vendor-stated market figures), describes cross-product findings at commonality strength, and keeps product-specific mechanisms and named modules out of the general description. One insurance-analytics vendor was dropped from the sample after a failed fetch; no claims are made about it.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
