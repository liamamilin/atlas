# Nutrient Management

## Overview

A **Nutrient Management** application is the farm's nutrient-accounting system of record. It holds a **nutrient plan** for the operation's land units, assembles the **supply** of plant nutrients from every source available to the operation — the soil itself, organic materials such as manure and compost, commercial fertilizer, and credits from previous crops — matches that supply against the **demand** of the crops to be grown, and expresses the result as **planned applications**: which nutrient source goes on which field, at what rate, with what placement, and at what time. Mature products bound those plans with environmental loss-risk constraints (phosphorus runoff risk, nitrogen leaching, regulated spreading rules) and record what was actually applied against what was planned.

The defining structure is small:

```text
Land unit (field / block / farm)
└── Nutrient plan / budget of record
    │   (crop nutrient demand vs nutrient supply, per nutrient)
    ├── supply assembled from → all available sources
    │   (soil supply, organic materials, fertilizer, credits)
    └── expressed as → planned applications
        (rate, source, placement, timing)
```

Everything else commonly associated with the category — manure storage and allocation machinery, regulatory plan documents, multi-year rotation schedules, variable-rate maps, loss-risk assessments, benchmarking — is widespread in current products but is not what makes the product a nutrient-management application. The pre-digital routine (a written manure management plan or a soil-test-based fertilizer plan on paper) satisfies the same core with no software at all, and fertilizer-only plans satisfy it without any manure.

When the center of gravity shifts to the measured state of the soil resource, the crop cycle as a whole, the water decision, or animal rations, the product has drifted into a neighboring Application Type (Soil Management, Crop Management, Irrigation Management, Feed Management).

## Users & Context

The Type is operated from two directions, and most of the market sits between them:

**Planner/adviser pole (the dominant professional realization):**

- **Nutrient management planners and certified advisers** — build and maintain plans across many client farms; in several jurisdictions plan writing is a certified profession, and the plan is an accountable document whose assumptions and sources must be documented.
- **Technical service providers and consultants** — produce plans that regulators or certification programmes accept, often under specific national or state formats.
- **Livestock-operation managers** — plan how manure produced by the operation is allocated to land: where, when, how much, and whether the operation has enough spreadable acreage and storage capacity to handle it.

**Grower pole:**

- **Farmers and farm managers** — hold their own farm's plan, decide fertilizer and manure applications, and keep the records the regime requires.
- **Field staff and applicators** — record actual applications in the field.

Regulators and regional authorities are counterparties (plans and compliance reports flow to them), not operating users. The work rhythm is seasonal and rotational: plans are drafted before the season, revised as soil tests, manure analyses and cropping plans arrive, and judged over rotations and years.

## Core Model

### The Defining Core

**1. The nutrient plan/budget as the unit of record.** For each land unit — field, management block, or the whole farm — the system holds a persistent, revisable plan that budgets plant nutrients: on the demand side, what the planned crops will need (from crop requirements, yield goals, or modeled farm systems); on the supply side, what nutrients are already available. The plan is held per nutrient (nitrogen, phosphorus, potassium, and commonly sulphur, lime and others) and persists across the season or rotation, revised as inputs change. It is a record, not a one-off calculation: it states what was planned, when, and on what basis.

**2. Multi-source supply accounting.** This is what makes it *management* rather than a fertilizer recommendation. Supply is assembled and credited from multiple sources before anything is decided: the soil's own supply (from soil test results), organic materials (manure and other organic materials, with their analyzed or book nutrient content and availability estimates), commercial fertilizer, and credits (nitrogen from previous legume crops or prior manure applications, nutrients in irrigation water). The plan decides each source's contribution — how much of the crop's need each source covers — and what remains to be supplied. In livestock operations the accounting extends to the manure inventory itself: how much is produced, stored, imported, exported, and whether the operation has enough land, storage, and equipment to use it.

**3. Planned applications as the plan's output.** The plan expresses its conclusion as applications specified by **rate, source, placement, and timing** — the four dimensions every mature product plans against. Applications are scheduled (by month, growth stage, or application event), often across a multi-year rotation; rates may be computed by the system from recommendation systems and availability factors, or entered from professional judgment, with the source documented. The plan is re-derivable: change the soil test, the manure analysis, or the rotation, and the planned applications recompute.

Remove the plan → disconnected calculators and records. Remove the multi-source accounting → a single-source fertilizer recommendation tool. Remove the planned applications → a nutrient data archive with no operational output.

### Standard Capabilities

Mature products commonly add, without these defining the Type:

- **Soil test integration** — soil analysis results imported and attached to fields, feeding the supply side.
- **Manure and organic-material machinery** — manure analyses (lab or book values), availability estimates by application method and timing, allocation of manure across fields and months, storage inventories, imports and exports between operations, spreading-area sufficiency checks.
- **Application records** — what was actually applied recorded against the plan, with planned-versus-actual comparison.
- **Environmental loss-risk machinery** — phosphorus-index and nitrogen-loss assessments, erosion tools, setback and sensitive-area rules that determine where and when application is allowed; regulated spreading windows.
- **Plan documents** — generated plans and compliance reports in the formats regulators, certifiers, and programmes require.
- **Multi-year rotation planning** — plans spanning several years so credits, rotations, and long-term soil-test projections can be accounted.
- **Economic valuation** — the fertilizer value of manure and organic materials; cost of the planned program.
- **Adviser and multi-client operation** — one plan shared between farmer and adviser with permissioned access; consultants operating across many client farms.

### One Structure, Many Implementations

```text
Concept:            Nutrient plan/budget of record
Implementations:    multi-year monthly allocation plan (manure-centric),
                    whole-farm nutrient budget from a flow model,
                    seasonal field-level application plan,
                    within-season nitrogen recommendation set

Concept:            Supply sources
Implementations:    soil test results, lab-analyzed or book-value manure,
                    commercial fertilizer, legume/residual credits,
                    irrigation water, effluent, feed and supplements

Concept:            Demand basis
Implementations:    crop requirement tables and yield goals,
                    recommendation systems (regional guides),
                    scientific farm-system models,
                    crop-sensing measurements

Concept:            Plan output
Implementations:    monthly manure allocation grid, fertiliser plan PDF,
                    variable-rate application map, real-time rate guidance
```

A reader who has only seen one variant — say a regulatory manure-allocation planner — should still be able to recognize a whole-farm nutrient budgeting model or a within-season nitrogen advisory as the same Type from the Core Model.

## How It Works

### Building the plan

```text
Set up the operation (farm, fields/blocks, soils)
→ enter the demand side
   (crops, rotations, yield goals — or the farm system to be modeled)
→ enter the supply side
   (soil test results, manure/organic material analyses,
    planned fertilizer, credits from previous crops)
→ the system computes the balance per land unit and nutrient
   (recommendation systems, availability factors, or a flow model)
→ review and adjust
   (override defaults; document the source of custom values)
```

### The allocation loop (livestock operations)

```text
Quantify manure production and storage
→ allocate manure to fields month by month across the plan horizon
   (rates computed against crop needs and availability factors;
    months where the field needs no more are flagged)
→ handle surplus: export to other operations, or revisit the
   rotation and acreage
→ enter supplemental fertilizer for deficits
   (fields that received manure, and fields that did not)
→ check sufficiency: enough spreadable acres, storage capacity,
   and equipment for the manure produced?
```

### The compliance and record loop

```text
Generate the plan document in the required format
→ apply according to plan, respecting risk-based constraints
   (setbacks, spreading windows, rate caps where risk is high)
→ record actual applications
→ compare planned vs applied
→ the record and the next soil test round inform the next plan
```

### The within-season advisory loop (nitrogen-advisory variant)

```text
Measure the crop's nitrogen status in the field
   (handheld sensor, satellite biomass)
→ enter what has already been applied and the yield expectation
→ receive a rate recommendation for the next application
→ optionally generate a variable-rate application map
→ repeat at the next growth stage
```

### Capability tiers

**Defining core** — without these, not nutrient management:

- nutrient plan/budget of record per land unit
- multi-source supply accounting with credits
- planned applications specified by rate, source, placement, timing

**Standard capabilities** — present in most mature products:

- soil test integration; manure/organic-material machinery
- application records and planned-vs-actual comparison
- environmental loss-risk assessment bounding applications
- plan documents and compliance reports; multi-year planning
- economic valuation; adviser/multi-client operation

**Variant / optional** — depends on segment, region, and regime:

- regulatory bindingness (mandatory formats vs guidance-only tools)
- modeling depth (rule-based calculators vs scientific flow models vs crop-sensing advisories)
- whole-farm vs field scope; GHG and carbon extensions
- variable-rate map generation; benchmarking; scenario simulation

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Operation setup / fields view

The plan's foundation surface. Farms, fields or management blocks with their soils, acreage, and (where kept) boundaries. Primary actions: create the operation, define land units, attach soil types and soil test results.

### Plan / budget view

The center of the product. Per land unit and nutrient: demand, supply by source, the computed balance, and the resulting planned applications. In allocation-style products this appears as a field-by-month grid with status flags (months where a field needs no more manure are visually flagged); in budget-style products as an inputs-versus-outputs table per nutrient; in advisory products as a recommendation per field and growth stage. Primary actions: compute rates, allocate sources to fields, adjust or override values with documented sources, schedule applications.

### Source data panels

Where supply is made trustworthy: manure analyses (lab values or book values, with source documented), soil test results, fertilizer products, credits. Primary actions: enter or import analyses, override estimates, document sources.

### Risk and constraint view

Where environmental limits are applied: risk assessment results per field, setback and sensitive-area constraints, permitted spreading windows, spreadable acreage. Primary actions: run assessments, review constrained fields, adjust the plan to fit.

### Records view

Actual applications recorded against the plan: what, where, when, how much, by whom. Primary actions: record an application, compare planned vs applied, export records for reporting.

### Reports / plan documents

The outward-facing surface: generated plan documents and compliance reports in regulator-accepted formats, adviser-shareable summaries, benchmarking where offered. Primary actions: generate, export, share.

## Important Rules / Behaviors

- **The plan is an accountable document.** Custom recommendations and measured analyses override system defaults, but the override must be documented with its source; plans may be reviewed by certifiers or regulators, so every figure is traceable to a basis (soil test, lab analysis, recommendation system, model).
- **Credits must be counted before purchases are planned.** The defining discipline: nitrogen from previous manure or legume crops, and nutrients already in the soil, reduce what still must be applied; a plan that ignores credits over-applies and over-spends, and in regulated settings may violate rate rules.
- **Availability is not content.** Nutrients in organic materials are not fully available to the crop in the application year; availability depends on material, method, timing, and weather, and mature products compute availability rather than treating analyzed content as crop-ready supply.
- **Environmental risk bounds the plan.** In regulated settings, risk assessment results determine what may be applied where and when — high-risk fields may be barred from commercial fertilizer or restricted to reduced rates; setbacks and sensitive features remove acreage from spreading; certain weather conditions prohibit application.
- **Sufficiency is a plan output, not an assumption.** A core planning question is whether the operation has enough land, storage, and equipment for the nutrients it produces; the plan surfaces the shortfall rather than assuming it away.
- **Planned and applied are distinct records.** The plan states intent; the application record states fact; planned-versus-actual comparison depends on the separation.
- **Decision support, not decision replacement.** Products across the sample position themselves as informing decisions — model outputs are estimates to be interpreted, not prescriptions; the user remains the decision-maker.

## Variants

- **By center of gravity:**
  - *regulatory manure-centric planning* — livestock operations; manure allocation, storage sufficiency, plan documents in mandated formats (the classic North American form)
  - *whole-farm nutrient budgeting* — the farm system modeled; budgets and losses per nutrient; scenario comparison (the farm-systems-model form)
  - *field-level nutrient planning* — fertilizer and organic materials planned per field against regional recommendation systems, with compliance records (the government-tool form)
  - *within-season nitrogen advisory* — crop-sensing-driven rate recommendations and variable-rate maps (the commercial-agronomy form)
- **By operating side:** certified planners and consultants (multi-client) · livestock operations (manure-centric) · arable growers (fertilizer-centric) · fertilizer vendors (advisory tooling) · government/public-good tools.
- **By regulatory regime:** mandatory plan formats with official software; compliance-report tools with no legal requirement to use them; advisory-only regimes. The regime shapes the outputs, not the core.
- **By era:** the defining loop predates software — paper manure management plans and soil-test-based fertilizer plans satisfy the same structure; desktop tools, then cloud services with shared farm accounts, are packaging generations.

A variant remains a variant unless it changes the core: a product whose center is the laboratory's analysis workflow, the environmental monitoring program, or the animal ration belongs to a different Type even though nutrients appear in all of them.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Soil Management | centers the soil resource itself — the measured soil state, the sampling/measurement cycle, and soil-improving decisions; nutrient management consumes the soil test as one input and centers the nutrient inputs applied to the land. The soil test is the shared artifact; the decision object differs |
| Agronomy Management | the multi-domain recommendation practice (seed + nutrients + crop protection) on the field record; nutrient management is the nutrient domain's own accounting discipline, including the sufficiency questions (enough acres, storage, equipment) that agronomy does not own |
| Feed Management | manages nutrients into animals (rations against nutrient targets); nutrient management manages nutrients onto land — manure is feed's output and this Type's input; livestock operations may run both |
| Crop Management | integrates all operation classes across the crop cycle; nutrient management owns the nutrient accounting in depth, as one domain the crop cycle passes through |
| Precision Agriculture Platform | centers the variable-rate execution loop (prescription → machine → as-applied verification); nutrient management produces the prescription basis, of which a variable-rate map is one output form |
| Irrigation Management | centers the water decision; in some systems nutrients are dosed with irrigation water (fertigation) — a coordination seam, with the nutrient accounting remaining this Type's |
| Fertilizer recommendation calculators | a single-source recommendation without the multi-source budget and plan of record is a capability, not this Type |
| Environmental Monitoring / Water Quality (§21) | nutrient loss to water is the environmental stake shaping the plan, but the subject of record here is the farm's nutrient inputs, not environmental monitoring or permitting |
| Carbon Accounting / GHG (§21) | greenhouse gas reporting is an extension some nutrient models carry; when emissions become the center, the product belongs to §21 |

The closest boundary is **Soil Management**: both read the same soil test, but one manages the soil resource (its measured state and improvement) while the other manages nutrient inputs (their budgeting, application, and constraint-bounded planning). Lime sits at the seam — soil products decide it from pH; nutrient-planning products carry lime recommendations from the same recommendation systems that drive N/P/K.

## Representative Products

- **Purdue MMP — Manure Management Planner** (US) — free desktop planner nationally supported by USDA-NRCS and EPA for nutrient management plan and CNMP development; multi-year manure allocation, state recommendation systems, risk-assessment tools, plan document generation
- **OverseerFM** (New Zealand) — whole-farm nutrient budgeting service modeling nutrient flows and losses for N, P, K, S, Ca, Mg, Na, with GHG extension and adviser ecosystem
- **PLANET / MANNER-NPK / NMPT-GB** (UK) — free national planning tools (now consolidated into Defra's web-based Plan and Manage Nutrient Applications Tool) built on the RB209 recommendation system, with organic-material supply estimation and Nitrate Vulnerable Zone compliance reporting
- **Yara Atfarm** (global) — commercial nitrogen advisory: field-level N-rate recommendations from crop sensing (handheld N-Tester, satellite biomass), variable-rate application maps

The Core Model was checked against a fertilizer-only plan form (a documented plan template inside the sampled sample) and a within-season advisory pole to avoid over-fitting to the regulatory manure-planning pattern.

## Sources

Research date: **2026-09-10**

- Purdue MMP — Help file: https://www.agry.purdue.edu/mmp/mmphelp.html ; program page: https://ag.purdue.edu/department/agry/research/manure-management-planner.html ; MyFarms partnership page: https://www.purduemmp.myfarms.com/
- USDA NRCS — Manure Management Planner fact sheet: https://www.wcc.nrcs.usda.gov/ftpref/wntsc/nutrientMgt/MMP.pdf
- US EPA — CAFO guidance, Section 6 (MMP): https://www.epa.gov/sites/default/files/2015-08/documents/cafo_manure_guidance_section6.pdf
- NRCS Conservation Practice Standard 590, Nutrient Management (national and state editions): https://www.nrcs.usda.gov/
- OverseerFM — product page: http://overseer.org.nz/overseerfm ; Knowledge base: https://support.overseer.org.nz/hc/en-us ; NZ MPI Overseer page: https://www.mpi.govt.nz/agriculture/farm-management-the-environment-and-land-use/overseer-a-nutrient-management-tool-for-farmers-and-growers
- ADAS — Planet and MANNER-NPK: https://adas.co.uk/projects/planet-and-manner-npk/ ; Defra NMPT-GB announcement: https://defrafarming.blog.gov.uk/2026/02/04/introducing-the-new-nutrient-management-planning-tool-on-gov-uk ; tool site: https://nmp-dev1.azure.defra.cloud/
- Yara — Atfarm support (N-Tester): https://support.at.farm/ ; N-Sensor product pages: https://www.yara.co.uk/crop-nutrition/farmers-toolbox/n-sensor

> Sourcing limitation: evidence for all four sampled products is official documentation (help centers, product pages, government guidance) fetched on 2026-09-10; no Tier-1 source was unreachable after retries. Precise vendor facts (state-specific recommendation sources, model version details, pricing, numeric limits) are recorded in the paired Research Notes rather than asserted here. Regional coverage is weighted toward US/UK/NZ regulatory regimes; continental-EU and other regional products were not deeply sampled, so region-specific claims are stated at correspondingly moderate strength.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis against neighboring Types are recorded in the paired Research Notes.
