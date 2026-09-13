# Nature Risk Management

## Overview

A **Nature Risk Management** application is a system for identifying, assessing, and prioritizing an organization's **nature-related risks** — the risks that arise from the organization's **dependencies on nature** (the ecosystem services its operations and value chain rely on, such as water, soil, pollination, flood regulation, and raw materials) and its **impacts on nature** (the pressures it places on ecosystems and biodiversity), which can manifest as physical, regulatory, and reputational risk.

The defining core is small:

```text
The organization's located interface with nature
  (sites, assets, holdings, supply-chain locations — each bound to a place and a business activity)
    → evaluated against authoritative nature data
      (protected areas, key biodiversity areas, threatened species,
       ecosystem condition, water, ecosystem services)
        → resolved into nature-related risk determinations
          (classifications, scores, or exposure measures)
            → used to prioritize locations and entities for response and disclosure
```

What makes this a distinct kind of application is the **spatial binding**: nature risk is assessed at places. The organization's footprint is grounded in geography, and the risk question is always "what is the state of nature at and around *this* location, and how does *this* activity depend on it or affect it?" A tool that shows nature data without binding it to an organization's locations is a data platform; a tool that tracks risks without the nature-data evaluation is a generic risk register. This Type is the application that joins the two.

The workflow in the market follows a recognizable arc — locate the organization's interface with nature, evaluate dependencies and impacts against nature data, assess and prioritize the resulting risks, and prepare responses and disclosures. This shape is reinforced by the Taskforce on Nature-related Financial Disclosures (TNFD) and by reporting regimes such as CSRD/ESRS, GRI, and SFDR, but it predates and does not depend on any single framework: project-finance biodiversity screening tools were doing located nature-risk assessment before these frameworks existed.

## Users & Context

Primary users:

- **Corporate sustainability and environment teams** — screen the company's sites, supply chains, and investments for nature-related exposure; prioritize sites; prepare biodiversity disclosures.
- **Risk and ESG analysts at financial institutions** — assess nature-related dependencies, impacts, and exposure across portfolios of equities, bonds, loans, or insurance holdings; support disclosure obligations and engagement decisions.
- **Project and site developers** (mining, energy, infrastructure, agriculture) — screen project locations for biodiversity sensitivity early in planning, often against lender performance standards for critical habitat.

Secondary users:

- **Risk and credit/underwriting functions** — consume nature-risk outputs alongside climate and conventional risk in lending and insurance decisions.
- **GIS and data teams** — integrate the underlying spatial data and outputs into internal analysis platforms.
- **Executives and disclosure owners** — consume prioritized results and framework-aligned reports.

The work context is assessment-driven and periodic rather than transactional: a screening or assessment cycle over a portfolio, typically tied to planning cycles and disclosure calendars, rather than a continuous operational flow. Both corporate (site-level) and financial-institution (portfolio-level) use are first-class in the market.

## Core Model

### The Defining Core

Three structures, held together:

**1. Located interface records.** The unit of assessment is a record of where the organization touches nature: an operating site, an asset, a supplier facility, a project location, or a financial holding whose underlying activities occur somewhere. Each record carries a geographic location (a point, polygon, or resolvable company-asset location) and a business activity or sector. Records are held in portfolios — a company's site list, a fund's holdings, a project's site set — and can be grouped (by company, business unit, or fund).

**2. Nature-context evaluation.** Each located record is evaluated against external, authoritative nature data describing the state of nature at and around the location:

- **protected and conserved areas** and **key biodiversity areas** — legally or internationally recognized places of importance;
- **threatened species** — presence and range in the surrounding area;
- **ecosystem condition** — integrity or intactness of ecosystems, land-cover change;
- **water** — water stress, flooding, and freshwater systems;
- **ecosystem services** — the flows nature provides that the activity depends on.

The evaluation surfaces the two risk-generating axes:

- **Dependencies** — which ecosystem services the activity at this location relies on, and what happens to the business if those services decline (the physical-risk side).
- **Impacts** — which pressures the activity places on nature at this location, and how that exposure interacts with regulation, stakeholders, and reputation (the regulatory and reputational side).

**3. Nature-related risk determination.** The evaluation resolves into risk outputs that can be compared and prioritized:

- **sensitivity or materiality classifications** — e.g., whether a site is in or near an ecologically sensitive area, flagged as a priority site;
- **risk scores or ratings** — per site, company, or portfolio, commonly organized as physical, regulatory, and reputational risk (exact labels vary by product);
- **exposure measures** — some products express materiality as a value-at-risk style metric (commonly labeled *Nature Value at Risk*), translating nature degradation into revenue or value exposure.

The determinations exist to drive **prioritization**: which sites, suppliers, holdings, or projects matter most, and where action or disclosure should focus.

### Standard Capabilities of Mature Products

These are widespread in the market but not what makes the product a nature-risk tool:

- **Portfolio aggregation** — roll site-level results up to company, group, sector, and portfolio level; compare across the roll-up.
- **Framework and disclosure alignment** — outputs mapped to the requirements of TNFD, GRI biodiversity standards, CSRD/ESRS biodiversity sections, SFDR indicators, CDP, science-based targets for nature, and lender performance standards (IFC PS6 / World Bank ESS6).
- **Visualization** — maps of the organization's footprint against nature layers, plus charts and tables of risk results; export to spreadsheets, PDF reports, and GIS formats.
- **Explicit methodology** — documented indicators, weightings, buffers, and thresholds that explain how raw nature data became a risk result.
- **Opportunity identification** — locating where threat abatement or restoration would have the greatest effect.
- **Integration delivery** — APIs and data feeds so risk, lending, underwriting, and reporting systems can consume the results.
- **Private assessment over a public layer** — public exploration of nature data and industry risk patterns, with account-gated private assessment of the user's own portfolio.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  Located interface records
Realized as:  uploaded site lists and geometries; company-asset locations
              resolved from securities; supplier-facility datasets

Concept:  Nature-context evaluation
Realized as:  proximity/overlap screening against protected areas, key
              biodiversity areas, and species ranges; indicator-based
              scoring of ecosystem state and pressures; sector dependency
              and impact profiles

Concept:  Risk determination
Realized as:  sensitive/not-sensitive classification with significance
              tiers; multi-risk indicator scores; value-at-risk style
              exposure metrics
```

A reader who has only seen one implementation — say, an investor-facing analytics platform — should still be able to recognize a free corporate screening tool or a project-finance site-screening service as the same Type.

## How It Works

### Build the picture of the organization's interface with nature

```text
Register / log in
→ enter the organization's footprint:
   upload sites (individually or in bulk, as lists or map geometries),
   or resolve a portfolio of companies into their asset locations
→ classify each record by business activity / sector
→ the application binds each record to its geographic location
```

This is the only heavy data-entry step, and products differ in how much of it they automate: some require the user to supply sites; others resolve company holdings into asset locations automatically.

### Evaluate against nature data

```text
For each located record:
→ the application overlays authoritative nature data
   (protected areas, key biodiversity areas, species ranges,
    ecosystem-condition indicators, water stress, ecosystem services)
→ applies its methodology — buffers around the location,
   sector weightings, indicator thresholds
→ surfaces dependencies (what this activity relies on)
   and impacts (what this activity pressures)
```

The user does not choose datasets or write queries; the evaluation is the product's methodology applied to the user's footprint.

### Assess, prioritize, and take results forward

```text
Review results per site / company / portfolio
→ in maps (where are the sensitive or high-risk locations),
   charts and tables (how do records compare)
→ prioritize: which locations are sensitive, material, or highest-risk
→ export results (spreadsheets, reports, GIS data)
   or feed them onward (APIs, data platforms)
→ use them for disclosure preparation, site selection,
   engagement, lending or underwriting decisions
```

Response support — mitigation recommendations, restoration opportunities, strategy guidance — exists at the edge of the Type (as roadmap modules, service layers, or opportunity identification) rather than as its operational center. The center of gravity is **assess and prioritize**.

### The assessment loop

The workflow is cyclical rather than one-shot: portfolios change (sites added and divested, holdings traded), nature data is updated (species assessments, protected-area designations, ecosystem-condition layers), and disclosure cycles recur. Mature products keep the footprint as a persistent, editable record and re-run the evaluation against updated data.

## Interfaces

Described in conceptual terms; exact layouts vary by product.

### Portfolio manager

The user's private workspace for the organization's footprint.

- lists the sites, companies, groups, or holdings under assessment
- primary actions: add/edit records (upload lists or geometries, resolve holdings), organize into groups, select a subset for analysis

### Map view

The signature surface of the Type.

- shows the organization's locations against nature layers — protected areas, key biodiversity areas, species ranges, risk surfaces
- primary actions: inspect a location's surroundings, compare locations spatially, export map data

### Results / analysis view

The risk-output surface.

- risk classifications, scores, or exposure results per site, company, or portfolio, with the contributing factors visible
- primary actions: compare across records, drill into a single record's result, export to spreadsheet or report

### Industry / context exploration

A public-facing layer in many products.

- industry-level dependency and impact profiles, country or landscape profiles, methodology documentation
- primary actions: explore how a sector interacts with nature before assessing a specific portfolio

### Reports and exports

The deliverable surface.

- framework-aligned reports (disclosure preparation, site screening, portfolio comparison), spreadsheet exports, GIS downloads
- primary actions: generate, download, and hand off results to reporting, risk, or planning processes

## Important Rules / Behaviors

### The location is the anchor

Every result is bound to a place. A record without a usable location cannot be assessed; the quality of location data directly bounds the quality of the risk result. Products differ in how they handle imprecise locations, but the spatial binding itself is not optional.

### Assessment is methodology-mediated, not raw data

The user sees risk results, not raw dataset joins. The product's methodology — which indicators, which buffers, which weightings, which thresholds — stands between the nature data and the result. Methodologies are documented and product-specific; two products can legitimately produce different risk classifications for the same site. Results are screening-grade inputs to decisions, not measurements of actual on-site condition.

### Screening is not ground truth

A sensitive-area or high-risk classification indicates exposure to assess further, not proof of impact. Products document their methodologies and their limitations, and frame results as screening-grade inputs; downstream processes (site surveys, due diligence, engagement) are expected to verify.

### Dependencies and impacts generate different risk kinds

The dependency axis drives physical risk (what happens to the business when nature declines); the impact axis drives regulatory and reputational risk (what exposure the business carries for what it does to nature). A complete assessment covers both; some tools weight one axis more heavily depending on their audience.

### Direct operations versus value chain

Assessments commonly distinguish the organization's own sites from its upstream (supply chain) and downstream (value chain, investments) interface. Data availability degrades with distance from direct operations, and products differ in how far along the value chain they reach.

### Private footprint, public context

The user's portfolio is private to their account; the nature data and industry-level context are shared. This split shapes the account model of most products.

## Variants

- **Free public screening tools** — NGO-operated, free corporate and portfolio screening with public exploration layers; assessment depth is indicator-based.
- **Authoritative-data subscription platforms** — built on conservation-science datasets; deep site-level screening, standardized reports, GIS delivery; strong in project finance and site operations.
- **Investor-facing analytics platforms** — resolve securities and bonds into asset locations and produce portfolio-level scores and exposure metrics for disclosure and investment decisions.
- **Impact-data platforms** — add monetary valuation of impacts and natural capital to the risk assessment; nature is one pillar beside climate and social impact.
- **Sector-shaped deployments** — the same core serves mining, agriculture, energy, real estate, and finance with different indicator emphases and weightings.
- **Water-paired deployments** — some products pair a nature risk tool with a water risk tool sharing the same portfolio, since water stress is both a nature and a business risk; others fold water into their nature indicators.

A variant remains a variant as long as the located-footprint → nature-evaluation → risk-determination core holds. If the product's center moves to managing conservation actions and biodiversity projects, it is drifting toward Biodiversity Management; if the center moves to measuring and valuing natural capital stocks, toward Natural Capital Management.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Climate Risk Management / Physical Climate Risk Platform | adjacent, partially overlapping | Same structural shape (located assets → hazard data → risk scores), different risk-generating system: climate risk centers on climate hazards and the transition; nature risk centers on ecosystems, biodiversity, and ecosystem services. Water stress and flooding appear in both domains, and products increasingly bundle the two; the biodiversity/ecosystem axis is what makes this Type distinct. |
| Natural Capital Management | adjacent | Measurement- and accounting-centric: quantifying and valuing natural capital stocks and flows. Nature risk management is risk-process-centric: screening, assessing, prioritizing. Monetary impact valuation straddles the seam. |
| Biodiversity Management | adjacent | Broader strategy and action management: biodiversity targets, footprint programs, conservation projects, monitoring. Nature risk management is the risk-assessment lens over the business–nature interface. |
| ESG Management Platform | adjacent, integration partner | Handles nature as one topic among many with questionnaire and reporting machinery; nature risk management is nature-specialized with geospatial depth. ESG platforms often consume nature-risk data. |
| Enterprise Risk Management | consumer | Generic risk registers and processes; nature risk management supplies specialized assessments whose prioritized results can feed ERM. |
| Environmental Management System | adjacent | Site-level compliance management (ISO-14001-style); nature risk management is portfolio-level assessment against external nature data. |
| Environmental Monitoring Platform | upstream, data relationship | Collects observational data from sensors and sites; nature risk management consumes authoritative nature datasets to assess business exposure. |
| Environmental Data Platform | upstream | Serves nature data to many consumers; nature risk management binds that data to one organization's located records and produces risk determinations. |

The closest boundary is with **Climate Risk Management**: the two Types share the located-asset risk-assessment shape and overlap on physical risks such as water stress and flooding. The structural difference is the risk-generating system being assessed — climate hazards versus the state of ecosystems and the organization's dependencies on and impacts on them.

## Representative Products

- **IBAT (Integrated Biodiversity Assessment Tool)** — conservation-alliance subscription platform; authoritative biodiversity data, site and portfolio screening, standardized reports
- **WWF Biodiversity Risk Filter** — free corporate and portfolio screening tool with public exploration layers
- **NatureAlpha (Geoverse)** — investor-facing geospatial nature-risk analytics with portfolio scores and exposure metrics
- **GIST Impact (Nature & Biodiversity)** — impact-data platform with nature-risk intelligence, dependencies/impacts assessment, and monetary valuation

The defining core was checked across these products' different philosophies (free NGO tool, data-alliance subscription, AI analytics, impact economics) and customer tiers (corporate site-level and financial-institution portfolio-level) to avoid over-fitting to any one implementation.

## Sources

Research date: **2026-09-09**

- IBAT — https://www.ibat-alliance.org/ , https://www.ibat-alliance.org/services
- WWF Biodiversity Risk Filter — https://riskfilter.org/biodiversity , https://riskfilter.org/biodiversity/assess
- NatureAlpha — https://www.naturealpha.ai/
- GIST Impact — https://gistimpact.com/ , https://www.gistimpact.com/nature-and-biodiversity/

> Sourcing limitations: the ENCORE tool's original documentation was not reachable (its former domain now serves unrelated content), the TNFD framework site returned access errors on repeated attempts, and one major data provider's pages were access-restricted. TNFD-shaped workflow language is therefore described as it appears in the products' own documentation rather than from the framework's primary source. Precise vendor figures (indicator counts, buffer tables, coverage claims, thresholds) are intentionally not stated in this document; they are recorded in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
