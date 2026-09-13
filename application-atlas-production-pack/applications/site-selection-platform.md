# Site Selection Platform

## Overview

A **Site Selection Platform** is a decision-support application for organizations that must choose where to locate a physical facility — a store, restaurant, clinic, gym, distribution center, office, or development site. It holds the **candidate locations under consideration**, attaches **geographic evidence** about demand, competition, and site characteristics to each candidate and its surrounding area, and **comparatively evaluates the candidates against the organization's own criteria**, so the organization can decide where to pursue, pass, or prioritize before committing capital.

The defining structure is small:

```text
Candidate locations under evaluation
└── Location evidence attached to their geography
    └── Comparative evaluation against the locator's own criteria
        └── Selection-grade judgment (pursue / pass / prioritize)
```

Everything else commonly associated with these products — foot-traffic data, AI revenue forecasts, weighted scoring models, territory maps, committee-ready reports — is widespread in current products but supports the evaluation loop rather than defining it. The platform's work ends at the recommendation: the lease negotiation, purchase, development, and construction that follow live in other systems.

## Users & Context

The primary user is a person or team responsible for **where an organization should grow its physical footprint**:

- **Expansion / real estate teams at multi-unit brands** (retail chains, restaurants, convenience stores, groceries, fitness, personal services) — screening markets, scoring candidate sites, and protecting existing locations from cannibalization.
- **Franchise development teams** — planning territories, deciding how many units a market can absorb, and assigning territory shapes to franchisees.
- **Healthcare network planners** — siting clinics and facilities against service-line demand and population health data.
- **Corporate real estate and workplace teams** — siting offices, warehouses, and industrial facilities near customers and labor.
- **Commercial real estate professionals** — from the landlord's side, using the same machinery in reverse to identify which tenants fit a property's trade area.
- **Civic and public-sector organizations** — ranking areas for services and facilities.

The work context is slow, capital-committing, and committee-driven: candidates are gathered from brokers, listings, field visits, and data screens; evidence is assembled around each one; comparisons and forecasts justify a recommendation; and the decision hands off to brokers, lawyers, and construction. The platform's output is a defensible ranking or score, not a transaction.

## Core Model

### The Defining Core

Three structures appear together in every product that is recognizably a site selection platform. Remove any one and the product stops being one.

- **Candidate locations under evaluation.** The working population: identified places — addresses, parcels, areas, or whole markets — brought in as candidates for a facility. This population takes different forms (persisted site records organized in projects, a scored candidate set, or places pulled in per analysis), but the evaluation always attaches to specific named places. Without candidates there is only market research.

- **Location evidence attached to geography.** An evidence base about each candidate and its surroundings, bound to the candidate through an evaluation geography — a trade area, a radius or drive-time buffer, an administrative geography, or an observed-visitor area. The evidence spans:
  - *demand* — demographics, consumer profiles and segments, foot traffic and movement, spending;
  - *supply* — competitors, co-tenants, business counts, road traffic;
  - *the site itself* — size, rent, zoning, access, photos, visit notes (vendor-supplied or collected by the user in the field).

  Without evidence there is only an opinionated checklist or a bare address list.

- **Comparative evaluation against the locator's own criteria.** Machinery that turns evidence into a judgment across candidates: weighted-criteria scoring and ranking, performance forecasting, best-customer fit matching, gap/void detection, minimum-threshold screens. The criteria and weights are the organization's — its model of its own customer and its own requirements — and the output is decision-grade: pursue, pass, or prioritize. Without this there is only a data feed or a map viewer.

### What Mature Products Commonly Add

These capabilities are standard in the current market but are not what makes a product a site selection platform:

- **Map-centric workspace** — candidates shown on a map, color-coded by score or rank, with evidence layers toggled around them.
- **Trade-area machinery** — rings, drive-time and walk-time polygons, or observed visitor-origin areas; the choice of method materially changes results.
- **Market and territory screening** — white-space analysis, estimating how many locations a market can support, and drawing/assigning territories for franchise networks. The same evaluation machinery operates at two grains: whole markets first, then specific sites.
- **Cannibalization and network impact** — estimating how a new (or closed) site would affect nearby existing locations, for organizations that already operate a network.
- **Forecasting and calibration** — projected performance for candidates, compared against the actual performance of opened sites, feeding portfolio decisions (remodel, relocate, close).
- **Comparison and reporting** — side-by-side tables, benchmark comparisons, presentation-ready reports and exports for committees and stakeholders.
- **Data access layers** — bundled datasets, data marketplaces, APIs and feeds; ingestion of real estate listings and points of interest as candidate supply.
- **Work organization** — projects or workspaces grouping candidates, per-site documents (photos, notes, attachments), mobile access for site visits, and AI assistants over the same data.

### One Structure, Many Implementations

The core is written conceptually. Current products realize each concept differently:

```text
Concept:            Candidate locations
Implementations:    attributed site objects in projects; scored candidate sets;
                    places pulled in per analysis; stage-managed pipeline
                    (at deal-management-flavored products)

Concept:            Evaluation geography
Implementations:    radius rings; drive/walk-time polygons; standard geographies;
                    observed visitor-origin trade areas

Concept:            Location evidence
Implementations:    census/demographic datasets; mobility & foot-traffic panels;
                    credit-card spend; broker comps and offering documents;
                    points-of-interest databases; user-collected site attributes

Concept:            Evaluation machinery
Implementations:    weighted suitability scoring; AI sales forecasting;
                    best-customer profile matching; void/gap analysis;
                    minimum-threshold screens
```

A reader who has only seen one style — say, AI revenue forecasts on a heat map — should still be able to recognize the ring-study analyst tool or the foot-traffic dashboard as the same Type from this table.

## How It Works

The typical loop, from framing to handoff:

```text
Frame the criteria
→ generate or gather candidates
→ attach evidence around each candidate
→ evaluate and compare
→ decide (pursue / pass / prioritize)
→ hand off; calibrate against what actually opens
```

1. **Frame the criteria.** The organization defines what it is looking for: a target customer profile, minimum thresholds (population, traffic, spending), scoring criteria and their weights, or an industry model that encodes these.

2. **Generate or gather candidates.** Candidates arrive from white-space and market-capacity screens, points-of-interest search, real estate listings, broker feeds and offering documents, imported lists, or field discovery.

3. **Attach evidence.** Each candidate gets an evaluation geography (trade area, buffer, or geography) and the evidence layers the criteria require: who lives, works, and visits around it; who competes and co-tenants there; what the site itself offers. Site attributes and visit photos are added by the team.

4. **Evaluate and compare.** The platform scores, ranks, or forecasts across the candidate set — often on a color-coded map and in comparison tables. Changing criteria or weights re-ranks the candidates, and what-if scenarios (aggressive vs. conservative expansion) shift the picture. For network operators, the impact on nearby existing locations is part of the judgment.

5. **Decide and hand off.** The output is a shortlist and a recommendation — pursue, pass, or prioritize — packaged as reports for the approval committee. The lease negotiation, purchase, or development that follows happens outside the platform.

6. **Calibrate.** Opened sites feed actuals back: forecast-versus-actual comparison refines the model, surfaces underperforming locations, and improves the next round of screening.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Map workspace

The primary surface. Candidates as map objects with score- or rank-based color coding; evidence layers (trade areas, competitor locations, customer concentrations) toggled around them.

- Typical information: candidate names/addresses, scores or forecasts, trade-area shapes, data overlays
- Primary actions: add or draw a candidate, adjust its geography, run an analysis, compare

### Candidate (site) detail

The per-place record.

- Typical information: address and geometry, user-maintained attributes (size, rent, status), collected photos and visit notes, evidence summaries, reports previously run
- Primary actions: edit attributes, attach documents/photos, run reports, move between projects

### Analysis builders

Where the organization's criteria become machinery.

- Typical information: criteria lists from a data browser, weights and influence settings, thresholds, model or industry-pack selection
- Primary actions: add/remove criteria, adjust weights, set influence direction (higher-is-better / lower-is-better / ideal-value), run and save the analysis

### Results and comparison surfaces

- Typical information: ranked tables, histograms, scatter plots, benchmark comparisons, per-candidate score decomposition
- Primary actions: filter by score or rank, export to spreadsheets or presentation formats, save results

### Market and territory surfaces

- Typical information: market capacity estimates, white-space maps, territory shapes and assignments
- Primary actions: screen markets, draw and assign territories, quantify available units per territory

### Reporting and administration

Presentation-ready reports and infographics for committees; dataset and data-marketplace management; user and organization preferences.

## Important Rules / Behaviors

### Rankings are criteria-and-weight driven

The same candidates rank differently as criteria and weights change. Mature products make weights explicit and user-controlled, and their own guidance treats weighting as the organization's judgment — a domain-knowledge decision that should be documented, because small weight changes visibly re-order the ranking.

### Trade-area definition is a modeling choice

Rings, drive-time polygons, and observed-visitor areas answer different questions and produce different demand pictures for the same site. Products increasingly contrast "arbitrary radius rings" with behavior-based areas; the organization must understand which method its numbers rest on.

### Evidence is estimated, not observed

Foot traffic, spending, demographics, and trade areas are modeled estimates from vendor panels and datasets — directional evidence, not ground truth. Coverage varies by dataset and country; a report's numbers are only as good as the data source behind them.

### Site knowledge is user-maintained

The organization's own facts about a candidate — size, rent, condition, access, photos, visit impressions — are entered and maintained by the team. The platform's data layers describe the surroundings; the site itself is often known best to the user.

### Output is decision support, not execution

The platform ends its work at the recommendation. Money, contracts, construction, and operations are downstream systems' territory; nothing in the candidate record constitutes a commitment.

### The loop closes through actuals

Forecasts are compared against the performance of opened locations. This calibration is a first-class behavior in mature products — it disciplines the model and turns the platform from a one-shot scorer into a learning system for the network.

## Variants

Common forms of the Type:

- **Data-and-models service** — vendor-owned industry models and consumer data, often consultant-supported; scoring candidates against "how many locations can this market support" and best-customer fit (enterprise brands, healthcare).
- **AI-forecast-led brand tool** — predictive revenue per candidate site, white-space projection nationwide, cannibalization calculation, territory management; the franchise/multi-unit pole.
- **GIS analyst tooling** — the organization's analysts configure criteria, weights, and geographies themselves over bundled demographic and business datasets; maximal flexibility, steeper skill requirement.
- **Foot-traffic-first analytics** — mobility data as the evidence base, self-serve, with site selection as one use case among many (retail, CRE, civic, finance); evaluation attaches to any property the user pulls up rather than a formal candidate pipeline.
- **Landlord-side configuration** — the same machinery reversed: void and gap analysis to identify which tenants a property's trade area would support.
- **Civic configuration** — ranking areas for public facilities and services rather than commercial sites.
- **Deal-flavored extension** — expansion teams that adopt a pipeline-of-record posture, carrying candidates through stages toward committee approval (structurally adjacent to real estate deal management).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Property Listing Platform | adjacent upstream | listings market and transact properties between lister and seeker; site selection consumes listings as candidate supply and evaluates them against the locator's criteria |
| Real Estate Development Management | downstream | holds the development project of record with a cost/commitment spine carried to a built outcome; site selection ends at the pursue/pass judgment on the location |
| Real Estate Investment Management | downstream / straddle zone | holds the investment record with a capital-and-returns spine; deal-flavored products straddle by feeding market evidence into an investment pipeline whose center is the deal, not the location's fit |
| Lease Administration / Commercial Property Management | downstream | operate the executed lease and the running asset; no candidate evaluation |
| Retail Space Planning | downstream | plans the chosen store's interior (layout, fixtures, assortment); the location decision has already been made |
| GIS / Business Intelligence platforms | tool substrate | general analysis and mapping without candidate-siting semantics; site selection platforms are a productized siting configuration, whether or not built on GIS |
| Market Research / Consumer Research platforms | evidence adjacency | share consumer and demand data, but center research programs rather than ranking and selecting places |
| Government GIS | adjacent (civic pole) | centers the government's geospatial data administration; the civic siting configuration shares machinery but centers the locator's evaluation loop |
| Clinical trial site selection (CTMS capability) | naming collision only | chooses investigational sites for trials — a different domain object despite the shared name |

## Representative Products

- **Buxton** (now packaged as Audiense In-Person; SCOUT platform) — data-and-models service pole; consumer-profile-led scoring; healthcare and franchise market depth
- **SiteZeus (Locate)** — AI-forecast-led pole; revenue prediction per site, white space, territory management, cannibalization
- **Esri ArcGIS Business Analyst** — GIS analyst-tooling pole; sites, suitability ranking, void and threshold workflows over bundled demographic/business data
- **Placer.ai** — foot-traffic-first analytics pole; self-serve location intelligence with site selection as a named use case

**Dealpath** was additionally examined as a deliberate boundary sample: its market-tracking layer feeds siting-like discovery into a real estate investment record, marking the seam against Real Estate Investment Management rather than the center of this Type.

## Sources

Research date: **2026-09-09**

- Buxton / Audiense — Location Intelligence product page: https://www.buxtonco.com/ (resolves to the Audiense In-Person page)
- SiteZeus — homepage: https://sitezeus.com/ · Locate product page: https://sitezeus.com/products/site-selection-software · Olympus Data Exchange: https://sitezeus.com/data
- Placer.ai — homepage: https://www.placer.ai/ · Platform: https://www.placer.ai/products/platform · CRE solutions: https://www.placer.ai/solutions/cre
- Esri — ArcGIS Business Analyst documentation: https://doc.arcgis.com/en/business-analyst/web/welcome.htm · Create sites: https://doc.arcgis.com/en/business-analyst/web/create-sites.htm · Suitability analysis: https://doc.arcgis.com/en/business-analyst/web/suitability-analysis.htm · Void analysis: https://doc.arcgis.com/en/business-analyst/web/void-analysis.htm · Threshold areas: https://doc.arcgis.com/en/business-analyst/web/threshold-areas.htm
- Dealpath — Market Tracking: https://www.dealpath.com/market-tracking/ (boundary evidence)

> Sourcing limitation: Tier-1 operational documentation was reached only at Esri; the other vendors' evidence is official product-page level (help centers for the Buxton client platform are gated). Accordingly, this document states structure-level claims only and intentionally omits numeric limits, default settings, license tiers, data-vendor figures, and named state vocabularies; such vendor specifics remain in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, the historical market-sample check, and boundary analysis are recorded in the paired Research Notes.
