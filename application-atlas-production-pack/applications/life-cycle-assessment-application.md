# Life Cycle Assessment Application

## Overview

A **Life Cycle Assessment Application** is a modeling and assessment environment for product life cycles: it lets a practitioner build a quantified model of the processes behind a product, compile the environmental flows of that model into a life cycle inventory, and translate that inventory into environmental impact results using selectable impact assessment methods.

The defining core is small and held jointly:

```text
Product system (linked network of quantified unit processes)
└── anchored to a functional unit (the demand everything is normalized to)
    └── life cycle inventory (compiled flows over the whole network)
        └── impact assessment (characterization methods → impact results)
```

Everything else commonly associated with modern LCA software — licensed background databases, method libraries, contribution trees, Sankey diagrams, Monte Carlo uncertainty, parameters, EPD generation, cloud delivery — is widespread in current products but is not what makes the product an LCA application. Older desktop generations of the same product lineage, built before cloud delivery and bundled mega-databases, satisfy the same core; so does a code framework with no graphical interface at all.

When the center of gravity shifts from the product system to an organization's scopes and activity data, the product is drifting toward a different Application Type (Carbon Accounting Platform). When the deliverable narrows to a single impact category as the customer-facing output, it approaches the Product Carbon Footprint Platform.

## Users & Context

The primary user is an **LCA practitioner** — someone who models product life cycles as their craft: sustainability consultants, corporate LCA specialists, researchers, and students. They define goals and scopes, choose methods, defend modeling choices to reviewers, and need transparency into every assumption.

A second, growing user group is the **non-expert product or sustainability team inside a manufacturer**. SaaS-style products serve them with templates, guided workflows, and expert services: they import a bill of materials, connect it to background datasets, and generate footprint results and declarations without deep methodological training.

Typical reasons to open the application:

- quantify the environmental impacts of a product across its life cycle (cradle-to-gate or cradle-to-grave)
- find the hotspots — which processes, materials, or life cycle stages dominate the footprint
- compare design alternatives, material swaps, or suppliers before committing
- produce defensible outputs: LCA reports, Environmental Product Declarations (EPDs), product carbon footprints
- answer customer, tender, or regulatory requests with verifiable numbers

The work is iterative and evidence-driven: models are refined as data arrives, and every choice (boundary, data source, allocation rule) must be documented because it changes the result.

## Core Model

### The Defining Core

Three structures, held jointly, make the application what it is.

**1. The product system — a linked network of quantified unit processes.**
The central modeled object is not a document or a form; it is a *system*: a set of unit processes (raw material extraction, transport, manufacturing steps, energy provision, use, waste treatment) connected by flows. Each process carries quantified inputs and outputs of two kinds:

- **technosphere flows** (also called product or intermediate flows) — goods, materials, energy, and services exchanged *between* processes; these are the links of the network;
- **elementary flows** — resources drawn from, and emissions released to, the environment; these are what eventually become impacts.

Processes may be modeled at fine granularity (unit processes, each with its own inputs and links) or as aggregated blocks (a cradle-to-gate summary of everything upstream, treated as one record). Expert tools expose both forms and let the practitioner choose; the aggregated form is faster but hides its internals. The network is typically visualized as a graph the practitioner can inspect and edit link by link.

**2. The functional unit — the quantified anchor.**
Every model is calculated *for a demand*: a stated amount of function or reference flow (for example, a quantity of material, a packaged unit, a painted area). All flows in the network are scaled to deliver this demand, and all results are expressed per this unit. This is what makes two products comparable and what distinguishes an assessment from a pile of process data. Some studies, especially cradle-to-gate ones, use a simpler declared unit (per kilogram, per piece) instead of a full function-based unit; declarations under product category rules often prescribe the unit for a product group.

**3. The inventory → impact assessment calculation chain.**
When the practitioner runs a calculation, the application does two things in sequence:

- **Life cycle inventory (LCI):** it resolves the whole linked network — following every upstream link, scaling every flow — and compiles the total elementary flows attributable to the functional unit;
- **Life cycle impact assessment (LCIA):** it applies an impact assessment method — a set of characterization factors that convert each elementary flow into contributions to impact categories (climate change, acidification, eutrophication, resource use, human toxicity, and similar) — and produces the impact results.

The method layer is *selectable and separable*: the same model can be calculated under different methods, and methods are managed objects (importable, editable, with per-flow characterization factors). Single-category methods (for example, climate change only) are legitimate members of this layer; multi-impact breadth is the typical posture, not the definition.

### Standard Capabilities of Mature Products

These capabilities are common across the researched sample and expected in practice, but they are additions to the core, not the definition:

- **Background LCI databases** — large licensed or curated datasets representing generic supply chains (electricity, materials, transport, waste treatment), which the practitioner links into the foreground model. Products differ in stance: some are database-agnostic and import many sources, some bundle a specific ecosystem, some let users supply their own. Databases come in versioned releases, and the version affects results.
- **Impact method libraries** — shipped or importable method sets alongside the ability to create or edit methods and characterization factors.
- **Result analysis surfaces** — impact results per category, inventory results, contribution trees and process contributions (which processes dominate), grouping, and flow diagrams of the result structure.
- **Scenario and comparison machinery** — parameters that drive amounts by formula, scenario copies of a model with modifications, and side-by-side comparison of alternative product systems.
- **Uncertainty and data quality** — Monte Carlo simulation and pedigree-style data quality assessment in expert tools.
- **Allocation and end-of-life machinery** — rules for splitting multifunctional processes and for modeling recycling and waste (see Rules below).
- **Import/export** — spreadsheets universally; standardized exchange formats between tools in the expert segment.
- **Reporting and declarations** — report templates, EPD generation support, and exportable result tables that feed verification.
- **Collaboration** — shared databases or workspaces, multi-user access, and server-based team storage in team-oriented products.

### One Structure, Many Implementations

The core is written conceptually; products realize it differently:

```text
Concept:            Product system
Implementations:    process network with a model graph (desktop tools),
                    product → objects → life cycle hierarchy (SaaS tools),
                    directed graph of activities and exchanges (code frameworks)

Concept:            Functional unit
Implementations:    reference process + target amount, calculation demand,
                    product units mapped to dataset units through explicit unit-mapping records

Concept:            Impact assessment method
Implementations:    importable method libraries, workspace-level method setting,
                    sets of characterization factors in code
```

A reader who has only seen one implementation should still be able to recognize the others from the core.

## How It Works

A study moves through a characteristic loop. The phases below follow the structure the domain standard (ISO 14040/44) prescribes; the application's job is to give each phase its working surface.

### 1. Define goal and scope

Before modeling, the practitioner fixes the purpose (internal improvement, comparison, declaration, claim), the **functional unit**, and the **system boundary** — which life cycle stages are inside (cradle-to-gate covers up to the factory gate; cradle-to-grave adds use and end-of-life). Many practitioners sketch a flowchart of the product system first; it becomes the blueprint for the model.

### 2. Build the model

```text
Create or pick the reference process (the last step of the chain)
→ enter or link its inputs and outputs (flows with amounts)
→ connect upstream processes providing the inputs
  (manually, or auto-linked from database provider information)
→ fill the remaining supply chain from background datasets
→ set parameters for anything that should vary between scenarios
```

The result is the product system: a network that can range from a handful of processes to many thousands of linked ones. Practitioners validate the model — checking for broken links, missing providers, and implausible amounts — before trusting any result.

### 3. Calculate

The practitioner chooses the impact assessment method (and calculation options such as aggregation behavior) and runs the calculation. The application resolves the network, compiles the inventory, and produces:

- **inventory results** — the compiled elementary flows (resources, emissions) per functional unit;
- **impact results** — the characterized scores per impact category.

### 4. Analyze and improve

Results are rarely the end point. The practitioner inspects **contributions** — which processes, flows, or life cycle stages dominate each category — often visualized as contribution trees or flow diagrams. Then the improvement loop: copy the model into a scenario, change a material, a supplier, or an amount, recalculate, and compare. Parameters make this systematic: one model, many parameter sets.

### 5. Report and publish

Results are exported into reports, spreadsheets, or declaration workflows. For public claims, the study is typically documented in a background report and, where required, verified by a third party; EPD publication goes through program operators that check conformity with the applicable product category rules.

## Interfaces

The surfaces below are described conceptually; names and layouts vary by product.

### Library / navigation tree

The entry surface: a browsable tree of databases, flows, processes, product systems, methods, and projects. Primary actions: search, open, create, import.

### Process editor

Where the data lives. A process record shows general information, its input/output table (flows with amounts and units), documentation, parameters, and allocation settings. Primary actions: add or edit flows, set amounts, choose providers, assign allocation rules.

### Model graph / network view

The visual heart of expert tools: the product system drawn as a linked graph of processes and flows. Primary actions: inspect links, add or remove connections, trace upstream chains, zoom from the reference process to raw materials.

### Calculation setup

A dialog where the practitioner selects the impact method, the amount or scenario to calculate, and calculation options, then runs the computation.

### Results views

- **Impact results** — scores per impact category, per functional unit.
- **Inventory results** — the compiled elementary flows.
- **Contribution tree / process contributions** — ranked contributors to a selected result, drillable down the network.
- **Flow diagrams** — visualizations of where impacts arise; Sankey-style flow diagrams in some products.

### Scenario / parameter panels

Where parameters are defined and scenario variants are created, compared, and switched.

### Comparison / project view

Side-by-side comparison of multiple product systems under the same method — the surface for design-decision support.

### Report / export surfaces

Report templates, exportable tables (spreadsheets, exchange formats), and declaration-generation support where the product offers it.

## Important Rules / Behaviors

### Everything is per functional unit

Results have no absolute meaning; they are impacts *of delivering the functional unit*. Changing the unit rescales the entire model. Comparing two products requires the same functional unit — a rule that also drives declaration standards, which prescribe units per product group.

### Boundary choices change results

Cradle-to-gate and cradle-to-grave models of the same product produce different numbers by construction. Omitting a known part of the value chain underestimates impacts; practitioners are expected to document boundaries and justify exclusions.

### Multifunctional processes force allocation decisions

Real processes often yield several products (and recycling loops couple systems). The practitioner must choose how to split burdens and benefits — allocation factors, recycled-content (cut-off) approaches, closed-loop assumptions, or substitution-based formulas. Different standards prescribe different approaches, and the choice materially changes results. This is one of the most consequential modeling decisions in the domain.

### Unit process vs aggregated process is a transparency trade-off

Fine-grained unit processes keep every upstream link inspectable; aggregated (system) processes collapse the upstream chain into a single record — faster and simpler, but a black box. Products ship databases in both forms and let the practitioner choose per study.

### Database and method must fit together

Background datasets are tied to database versions and, in some products, to method families. Mixing incompatible datasets and methods can silently produce zero or missing impacts — a known failure mode that products surface through validation checks and workspace settings.

### Cut-off is a modeling lever, not an error

Practitioners can exclude tiny contributors below a threshold to keep large networks manageable; the exclusion is deliberate, applied across the supply chain, and must be documented.

### Results feed claims, and claims invite scrutiny

Public comparisons and declarations typically require third-party verification. The application's role is to make the model transparent and reproducible — full network visibility, documented assumptions, exportable evidence — so that a verifier can reconstruct the result.

### The loop is iterative

Scope, data, and even the functional unit may be revised as data arrives; models are living artifacts that get updated when databases, methods, or products change.

## Variants

- **Expert desktop tools** — deep modeling control, method and database management, uncertainty analysis; the practitioner's workbench.
- **SaaS automation platforms** — guided, template-driven product footprinting for manufacturer teams; BOM import, dataset linking, scenario features, and declaration outputs with expert services alongside.
- **Code frameworks** — no GUI; programmatic model building and high-performance calculation for research and large-scale or unconventional analyses.
- **Sector-packaged editions** — buildings and construction (EPD-centric), food and agriculture, chemicals, electronics, packaging; sector templates and prescribed methods.
- **Scope variants** — cradle-to-gate screening studies vs full cradle-to-grave studies; product vs organizational LCA.
- **Extended assessment** — life cycle costing and social life cycle assessment alongside environmental impacts in some products.
- **Portfolio-level footprinting** — facility- or portfolio-scale variants that reuse product-level models at company scale.

A variant remains a variant as long as the product-system / functional-unit / inventory→impact core still applies. A tool that abandons the product system for organizational scopes is no longer this Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Carbon Accounting Platform | adjacent | unit of analysis is the organization (scopes, activity data, emission factors), not a product system with a functional unit; typically single-impact (GHG) |
| Product Carbon Footprint Platform | closest sibling | centers on the carbon figure as the deliverable; LCA machinery may sit underneath, but the method layer is not the center; LCA applications treat impact assessment as a selectable, typically multi-impact layer |
| Environmental Impact Assessment Platform | name-adjacent only | regulatory assessment of construction/industrial projects (site baselines, noise, ecology, mitigation) — a different object despite the shared word "assessment" |
| Environmental Management System | broader org context | org-level compliance and management machinery (audits, objectives, legal registers); may consume LCA results but does not model product systems |
| ESG / Sustainability Management Platform | broader org context | organization-level data collection and reporting frameworks; not product-system modeling |
| Scope 3 Management Platform | adjacent | supply-chain GHG estimation at organizational level (spend- or activity-based), not functional-unit-based product modeling |
| Sustainable Product Management | downstream consumer | manages product sustainability processes and decisions; the LCA application is the calculation engine its numbers may come from |

The two boundaries that matter most: against **Carbon Accounting** (product system vs organization as the unit of analysis) and against **Product Carbon Footprint Platforms** (method-layer center vs carbon-first deliverable). Products exist on both seams, and some vendors sell both from one engine.

## Representative Products

- **openLCA** (GreenDelta) — open-source, database-agnostic desktop practitioner tool with collaboration server and scripting.
- **SimaPro** (SimaPro B.V.) — classic expert desktop and cloud editions, scientific standard in consultancy and academia.
- **Ecochain Mobius** (Ecochain Technologies) — SaaS product-footprinting platform for manufacturers, with a portfolio-level sibling (Helix).
- **Brightway** (open-source community) — Python framework for LCA calculation at scale; the code-first pole.

The core was checked against older and differently-shaped implementations to avoid defining the Type by today's database-and-cloud pattern: the sampled expert desktop product's own lineage spans decades and predates cloud delivery and modern mega-databases; the open-source desktop tool can build databases and models entirely from scratch; and the code-framework pole proves that no graphical interface is required.

## Sources

Research date: **2026-09-08**

- openLCA manual (GreenDelta) — https://greendelta.github.io/openLCA2-manual/ (introduction; product systems; calculation and result analysis; LCIA methods overview) and https://www.openlca.org/
- SimaPro — https://simapro.com/ ; Help Center https://support.simapro.com/en/ (unit and system processes; recycling modeling; collections overview)
- Ecochain — https://ecochain.com/ ; Help Center https://helpcenter.ecochain.com/ (Mobius FAQ; Goal & Scope phase)
- Brightway — https://docs.brightway.dev/en/latest/ (framework overview; glossary)

> Sourcing limitation: One Click LCA and Umberto documentation could not be reached from the research environment on 2026-09-08; the SaaS pole is therefore evidenced by one product, and the material-flow-analysis lineage is not directly evidenced. Vendor marketing figures (dataset counts, method counts, prices, years in business) were recorded in the Research Notes as vendor claims and are deliberately not stated as facts in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
