# Climate Risk Management

## Overview

A **Climate Risk Management** application is an organization-side system that runs the organization's climate risk process: it holds the organization's own exposures — assets, sites, business units, or portfolio holdings — as a managed population, assesses them against climate hazards and transition drivers under scenario-based, forward-looking views, keeps those assessments as maintained, traceable records, uses them to prioritize and decide responses, and sustains the risk picture over recurring monitoring and reporting cycles, typically aligned to climate disclosure frameworks.

The defining structure is small:

```text
Managed exposure population
        ↓ assessed against
Climate drivers under scenarios and time horizons
        ↓ producing
Maintained climate risk assessments
        ↓ feeding
Prioritization and response decisions
        ↓ sustained by
Recurring monitoring and reporting
```

Everything else commonly associated with the category — dual physical-and-transition coverage, financial quantification, embedded hazard engines, framework certifications, AI assistance — is widespread in current products but is not what makes one a climate risk management application. The category's market vocabulary comes from the climate disclosure canon (governance, strategy, risk management, metrics and targets), which frames scenarios as exploratory views of plausible futures, not forecasts.

When the managed exposure population, the maintained assessments, or the decision-and-monitoring loop is removed, the product stops being climate risk management and becomes something else: a climate data product, a modeling engine, or a one-shot study.

## Users & Context

Primary users are the people accountable for understanding and steering climate-related risk inside an organization:

- sustainability and climate leads, who own the assessment process and the disclosure outputs
- risk managers, who integrate climate results into the organization's wider risk picture
- finance and strategy teams, who translate exposures into financial terms and capital decisions

Contributing users:

- analysts who run assessments, screen portfolios, and prepare deep dives
- business-unit and asset owners who supply exposure data and act on findings for their own units
- treasury, insurance, and capital-planning staff who consume loss and cost projections

Secondary audiences:

- executives and boards, who receive risk summaries and oversee climate governance
- auditors, regulators, and investors, who consume the disclosure outputs
- external consultants and data providers, who supply methodology, hazard data, or assessment services

The work context is periodic and iterative rather than continuous operations: assessments are run and re-run against scenario sets and disclosure deadlines, results are compared year over year, and the risk picture is formally revised rather than treated as a one-time study. In financial institutions the same work additionally lives under model-governance scrutiny, where assessment methods and outputs must be explainable and defensible.

## Core Model

### The Defining Core

Three properties. If any one is removed, the product is no longer recognizable as climate risk management:

- **A managed exposure population.** The risk-bearing "things" are identified and held in the system: physical assets and sites, business units and sub-entities, portfolio holdings, or assessed entities. Every analysis is bound to this population; without it, the product is a general climate data or mapping surface.
- **Maintained climate risk assessments.** Exposures are assessed against climate drivers — physical hazards (acute events such as floods, storms, heat, wildfire; chronic shifts such as water stress and sea-level rise) and/or transition drivers (policy, technology, market, and reputational change) — under named scenario families and time horizons. The output is a risk record per exposure and in aggregate: ratings, scores, and/or financial metrics, traceable to the method and data behind them. Assessments are maintained state, re-run and revised as scenarios, data, and the exposure set change.
- **A management loop.** Results drive prioritization (screening the population down to the most material exposures, then deep-diving those), support response decisions (adaptation, mitigation, or strategic options evaluated for cost and benefit), and are kept alive across recurring cycles of monitoring, re-assessment, and reporting. Without the loop, the product is a one-shot analytics study or a dataset.

### Standard Capabilities of Mature Products

These capabilities are common across mature products and make the process practical, though they do not define the Type:

- **Dual risk-family coverage** — the physical and transition frames side by side, with nature-related risk as an emerging extension in some products.
- **Financial quantification** — translation of exposure into business terms: damage and loss estimates, earnings and operating-cost impact, asset value, or credit and cashflow metrics.
- **Scenario and stress-test machinery** — scenario libraries and stress-testing workflows aligned to recognized climate pathways, with configurable horizons.
- **Screening → deep-dive workflow** — a high-level pass across the whole population to surface the most-at-risk exposures, followed by detailed analysis of those.
- **Disclosure alignment** — reporting outputs structured against climate disclosure frameworks and regulatory regimes; standardized reports for internal briefings and external filing.
- **Multi-surface delivery** — the same assessment content served through an interactive platform, data/API feeds for the organization's own systems, and generated reports.
- **Monitoring and trend views** — dashboards showing how risk results evolve, progress against targets, and year-over-year comparisons.
- **Cross-functional collaboration** — shared workspaces connecting sustainability, risk, and finance users, with business-unit participation for exposure data and follow-up.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:                  Exposure population
Realizations:             corporate operational structures (sites, supply
                          chains, units), lending or investment portfolios,
                          owned asset portfolios, assessed entities

Concept:                  Climate evidence source
Realizations:             embedded proprietary hazard engines, licensed
                          climate data feeds, imported assessments,
                          framework criteria applied to documents

Concept:                  Assessment output
Realizations:             quantitative loss/financial metrics, risk scores
                          and ratings, disclosure-conformance verdicts

Concept:                  Response support
Realizations:             adaptation-option cost-benefit testing, transition
                          and mitigation planning, portfolio prioritization,
                          disclosure-gap remediation
```

A reader who encounters only one implementation — for example, an asset-portfolio physical-risk platform — should still be able to recognize the corporate transition-planning or disclosure-assessment carriers from the core model.

## How It Works

Climate risk management runs as a repeating cycle rather than a single linear flow.

**1. Assemble the exposure population.** The organization registers what it wants managed: assets and their locations, business units, portfolio holdings, or entities. Data comes from internal systems, uploads, or provider-maintained geospatial databases.

**2. Assess against climate drivers.** Each exposure (or the population in aggregate) is assessed against physical hazards and/or transition drivers under selected scenarios and horizons. Depending on the product, this runs through an embedded hazard engine, licensed climate data, or a structured methodology applied to supplied data. The output is a set of maintained risk records: per-exposure results and portfolio- or organization-level aggregates.

**3. Screen and prioritize.** A first pass ranks the population by materiality; the most significant exposures receive deeper analysis — component-level failure points, disruption and recovery characteristics, financial impact ranges.

**4. Evaluate responses.** Options are tested against the assessment: adaptation measures for physical risk, mitigation or strategic shifts for transition risk, with cost, benefit, and return compared. In disclosure-led implementations, this step appears instead as remediation of disclosure gaps against framework criteria.

**5. Decide and integrate.** Results and option analyses feed management decisions — capital allocation, resilience investment, transition plans — and are summarized for risk and governance bodies. The disclosure canon expects the climate process to connect into the organization's overall risk management; the depth of that integration varies by product and organization.

**6. Monitor, re-assess, and report.** The risk picture is re-run as scenarios, data, and exposures change; results are tracked over time and compared year over year; disclosure outputs are produced on the reporting rhythm. The cycle repeats.

A practical note on tool boundaries: the assessment engine is frequently split between systems. Dedicated hazard and scenario engines compute the climate evidence; climate risk management platforms either embed such engines or consume their outputs and run the process around them. Mature products accommodate both postures — proprietary engines inside the platform, or data ingested from providers.

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Exposure / portfolio workspace

The system's home for the managed population.

- typical information: the registered exposures, their attributes and locations, coverage of assessments
- primary actions: add or import exposures, organize into groups or portfolios, assign assessments

### Screening view

The first-pass surface across the whole population.

- typical information: relative risk results per exposure, hazard breakdowns, filters and rankings
- primary actions: sort and filter, flag exposures for deeper analysis

### Assessment / deep-dive view

The detailed analysis surface for a selected exposure.

- typical information: hazard-specific results, scenario and horizon comparisons, component-level detail, financial impact estimates, method and data traceability
- primary actions: run or re-run assessments, compare scenarios, record notes or decisions

### Scenario / stress-test explorer

Where forward-looking views are configured and compared.

- typical information: scenario families, time horizons, parameter assumptions, stress cases
- primary actions: select scenarios, run stress tests, compare outputs across cases

### Decision / response view

Where prioritized exposures meet candidate responses.

- typical information: material exposures, response options with cost and benefit characterizations, investment or remediation status
- primary actions: compare options, record decisions, hand outputs to planning or capital processes

### Monitoring dashboard

The over-time surface for management and governance audiences.

- typical information: risk-result trends, target or progress tracking, portfolio-level summaries
- primary actions: review changes, drill into drivers, export summaries

### Disclosure / report generator

The framework-aligned output surface.

- typical information: disclosure metrics, assessment narratives, evidence and traceability references
- primary actions: generate, customize, and export framework-aligned reports; in disclosure-led products, review conformance verdicts with cited evidence and gap findings

### Data delivery surface

For organizations embedding results in their own systems.

- typical information: datasets, indicators, and results available via API or feeds
- primary actions: configure delivery, integrate into internal risk or finance systems

## Important Rules / Behaviors

### Scenarios are views, not forecasts

The scenario frame is deliberately exploratory: results describe plausible futures under stated assumptions, not predictions. Mature products carry this posture through their outputs, which present ranges and scenario comparisons rather than single-point outcomes.

### Assessments are records, not reports

A risk result persists as a traceable record — bound to the exposure, the scenario, the horizon, and the method that produced it. It can be re-run, compared against earlier results, and defended to auditors or regulators. This traceability is what distinguishes a management system from a study.

### Results must translate into decisions

The category's center of gravity is financial and operational materiality: scores that cannot be expressed in business terms have limited standing in the process. Response support — cost, benefit, return on adaptation or mitigation options — is how assessments become decisions.

### Prioritization precedes depth

Screening the full population and deep-diving the material subset is the standard economy of the workflow; detailed analysis of everything is neither expected nor typical.

### The disclosure leg is structural

Framework alignment is not an afterthought: disclosure requirements shape which assessments are run, at which horizons, and with what traceability. In some products the disclosure workflow (conformance and gap assessment) is the primary object; in most it is the reporting output of the risk process.

### The engine may be inside or beside the platform

Where the climate computation lives — embedded proprietary models, licensed data feeds, or imported assessments — is a deployment posture, not a boundary of the Type. The management loop persists across all three.

## Variants

Common shapes of the Type:

- **Corporate risk and strategy carriers** — the organization's operational structure (sites, supply chains, business units) is the exposure population; assessments feed strategy, transition planning, and disclosure.
- **Financial-institution carriers** — lending or investment portfolios are the population; assessments translate physical and transition risk into credit, loss, and cashflow metrics; stress testing and model-governance defensibility are prominent.
- **Asset-portfolio carriers** — owned or financed physical assets are the population; screening and deep dives drive resilience investment and due diligence.
- **Disclosure-led carriers** — the assessed object is the organization's climate disclosure against framework criteria; the output is conformance, evidence, and gap analysis rather than risk quantification. Adjacent to disclosure-management territory; included here because it operates on the same process canon.
- **Data-led carriers (drift boundary)** — portfolio climate data and analytics consumed in investor workflows; when the org-side management loop disappears, these products belong to the climate data and analytics neighborhood.
- **Depth variants** — embedded hazard engines versus licensed data versus methodology-only; physical-led versus transition-led versus dual; with or without nature-related extension; AI assistance for assessment or for querying results.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Physical Climate Risk Platform | overlapping engine | computes physical hazard exposure and loss for assets — physical only, engine-side; this Type runs the organizational risk process over maintained assessments and decisions, commonly spanning transition risk as well |
| Climate Scenario Analysis | input machinery | models futures under scenario families and supplies projections; holds no managed exposure population or risk records |
| Enterprise Risk Management | adjacent generic process | manages any enterprise risk in register and control form without climate science content; climate risk management supplies the climate-specific assessments and evidence that integrate into it |
| ESG Management / ESG Reporting Platform | adjacent domain suite | centers on sustainability data collection, carbon accounting, and report production; this Type centers on risk assessment and treatment of exposures |
| Climate Adaptation Planning | downstream counterpart | holds the managed adaptation plan — goals, actions, owners, public progress; this Type holds the risk assessments and option analyses that justify and steer such a plan |
| Financial Risk Management Platform | FI-side sibling | manages market, credit, and liquidity risk on financial positions; climate enters it as one emerging risk type, whereas this Type is climate-specific and disclosure-framework-driven |
| Business Continuity Management Platform | adjacent | procedures and recovery plans for operational disruption; this Type is the long-horizon risk assessment and steering layer above them |
| Climate data products | drift boundary | when exposure-bound assessment records, decision support, and recurring cycles disappear, the product becomes a data or analytics feed rather than a management application |

The most important boundary is with the physical-risk engine: analytics products quantify the threat and can test what options would buy, while climate risk management keeps the organization's risk picture alive — assessments maintained over time, decisions recorded and supported, monitoring and disclosure recurring. The second most important is with generic ERM: the same process shape, but the climate content — hazards, scenarios, pathways, disclosure frameworks — is what makes this a distinct Type.

## Representative Products

- **Risilience (Riise platform)** — corporate climate-and-nature risk quantification and strategy: physical, transition, and nature risk through one analytical lens, financially quantified scenario analysis, transition and mitigation planning, progress tracking
- **Jupiter Intelligence** — decision-grade physical climate risk analytics for financial institutions: asset- and entity-level projections translated into credit, loss, and cashflow metrics, with adaptation ROI modeling and a model-governance posture
- **XDI (Cross Dependency Initiative)** — physical climate risk workflow for asset portfolios: screening, asset-level deep dive, framework-aligned reporting, stress testing, and adaptation-pathway exploration
- **Manifest Climate** — AI-powered assessment of climate disclosures against frameworks: conformance verdicts with cited evidence, gap analysis, peer benchmarking, and year-over-year trend tracking (disclosure-led boundary sample)
- **ISS STOXX Climate & Nature Analytics** (sustglobal.com now resolves here) — investor-facing climate risk data and analytics across physical, transition, net-zero, and biodiversity dimensions (data-led boundary sample)

## Sources

Research date: **2026-09-07**

- Risilience — https://risilience.com/ , https://risilience.com/product-overview/
- XDI — https://xdi.systems/
- Jupiter Intelligence — https://www.jupiterintel.com/
- Manifest Climate — https://www.manifestclimate.com/
- ISS STOXX Climate & Nature Analytics (via sustglobal.com redirect) — https://www.sustglobal.com/
- TCFD Recommendations (Task Force on Climate-related Financial Disclosures) — https://www.fsb-tcfd.org/recommendations/

> Sourcing limitation: deep help-center or user-manual documentation for the sampled products was not reachable in this research pass; evidence comes from official product pages and one official framework portal. Accordingly, this document deliberately states no precise numeric claims (scenario counts, data resolutions, horizons, limits, or defaults), describes cross-product findings at commonality strength, and keeps product-specific mechanisms out of the general description. Process-canonical vocabulary (governance, strategy, risk management, metrics and targets; scenarios as exploratory constructs) is drawn from the TCFD recommendations portal, which also documents the framework's handover to the IFRS Foundation.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
