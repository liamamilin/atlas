# Research Notes — Life Cycle Assessment Application

## Research Goal

Understand what a Life Cycle Assessment (LCA) Application really is from real products: what objects exist inside it, what users do with them, how a study flows from data to results, which rules govern the modeling, and where the Type's boundary lies against neighboring sustainability software (carbon accounting, product carbon footprint, environmental impact assessment, ESG reporting).

## Initial Boundary

Working hypothesis before research:

- Core use: quantifying environmental impacts of a product/service across its life cycle by modeling a system of processes and applying impact assessment methods.
- Likely users: LCA practitioners, sustainability consultants, corporate sustainability teams, academics, product designers (in SaaS-flavored products).
- Nearest neighbors: Carbon Accounting Platform (organizational GHG), Product Carbon Footprint Platform (single-impact cousin), Environmental Impact Assessment Platform (project/regulatory EIA — different object entirely), Sustainability/ESG Management Platforms (org-level reporting), Environmental Management System (org-level compliance machinery).
- Likely confusion: LCA vs carbon accounting (product-system vs organizational boundary); LCA vs PCF (multi-impact method layer vs carbon-first deliverable).

## Research Questions

1. What is the central modeled object (product system? life cycle? model graph?) and how is it structured?
2. What role does the functional unit play, and where does it live in the software?
3. How are flows and processes represented (unit vs system processes, foreground vs background)?
4. How does the inventory → impact assessment calculation chain work?
5. What are impact assessment methods/categories in the software, and are they selectable/importable?
6. How is background data (LCI databases) handled — bundled, licensed, agnostic?
7. What modeling rules matter: allocation, recycling/end-of-life, cut-off, system boundaries?
8. What analysis surfaces exist: contribution trees, Sankey, scenarios, uncertainty (Monte Carlo), parameters?
9. What outputs: reports, EPDs, PCFs, exports?
10. How do expert desktop tools differ from SaaS "automation" tools and code frameworks?

## Representative Products

Selected for market representativeness, documentation quality, and spread across product philosophy and customer level:

| Product | Vendor | Philosophy / pole | Customer level |
|---|---|---|---|
| openLCA | GreenDelta | open-source, database-agnostic desktop practitioner tool (+ collaboration server, scripting) | practitioners, academia, industry |
| SimaPro | SimaPro B.V. (PRé; part of One Click LCA group) | classic expert desktop + cloud, ecoinvent-centric, scientific standard | LCA experts, consultants, enterprise |
| Ecochain Mobius (with Helix) | Ecochain Technologies | SaaS "LCA automation" for manufacturers; product/portfolio footprinting, EPD/PCF outputs | manufacturer sustainability & product teams (non-expert-friendly) |
| Brightway | open-source community | code-first Python framework, no GUI, performance-oriented | academia, power users |

Rejected/abstained: One Click LCA (SaaS, buildings-focused) — official help center unreachable from research environment (3 fetch failures); Umberto (MFA/Sankey lineage) — site unreachable (2 fetch failures). Sphera GaBi — enterprise docs gated; not attempted after two adjacent failures. These absences are recorded as source-access limitations.

## Sources

All fetched 2026-09-08.

- openLCA manual (official, GreenDelta): https://greendelta.github.io/openLCA2-manual/ — pages: introduction (what you can do), product systems (creating, calculating), result analysis (general information), LCIA methods overview. Plus https://www.openlca.org/ (site).
- SimaPro: https://simapro.com/ (positioning, editions); Help Center https://support.simapro.com/en/ — collections: SimaPro desktop (203 articles), SimaPro cloud (35); articles: "What are unit and system processes?", "How to model recycling in SimaPro?".
- Ecochain: https://ecochain.com/ (positioning, workflow, EPD/PCF); Help Center https://helpcenter.ecochain.com/ — collections Mobius/Helix/LCA Fundamentals/LCA Data/LCA Methods & Standards/LCA Toolkit; articles: "Mobius FAQ", "Explained: Goal & Scope phase".
- Brightway: https://docs.brightway.dev/en/latest/ (framework overview); glossary https://docs.brightway.dev/en/latest/content/overview/glossary.html.

## Product A — openLCA (GreenDelta)

### Key observations (Evidence layer A — official manual)

- Self-definition: "openLCA is a tool for modelling and assessing life cycles, performing Life Cycle Assessments (LCAs). This covers modelling the life cycle in a narrow sense, by connecting processes visually or via tables, assessing them, regarding environmental, economic or social impacts, and analysing these results for the identification of hotspots. Also comparisons of products are possible, and also assessments and comparisons of organisations."
- Supported study variants (vendor list): carbon footprints (GHG Protocol, ISO 14067), LCA per ISO 14040, European Commission Environmental Footprint, EPDs per EN 15804, screening LCIA, organisational LCA, Life Cycle Costing, Social LCA.
- Manual structure = the application's object world:
  - **Databases**: elements, create from scratch, restore from file, update, import/combine, mapping files + validation, export. openLCA is database-agnostic (manual references ecoinvent, EF, GaBi, PSILCA as importable sources).
  - **Flows**: created and edited as first-class objects (flow property, CAS, locations).
  - **Processes**: tabs = general information, inputs/outputs, documentation, parameters, allocation, social aspects, direct impacts.
  - **Product Systems**: created from a reference process; auto-linking of upstream supply chains; provider linking (default providers: only/prefer/ignore); choice of unit process vs system process; cut-off threshold for auto-connection; model graph view; nested/advanced systems; calculation; export.
  - **LCIA methods and categories**: importable; methods/categories/characterization factors can be created and edited; regionalized calculation supported.
  - **Calculation and Result Analysis**: calculation properties dialog; results include general information (allocation method, target amount, LCIA method used, data quality), inventory result, impact analysis, process results, contribution tree, grouping, locations, Sankey diagram, analysis groups, LCIA checks; save/export results.
  - **Projects**: comparison of multiple product systems; report templates; project reports.
  - **Waste modelling**, **Allocation**, **Parameters** (types, hierarchy, parameter sets, parameter analysis, dependent parameters), **Background data** guidance, **Model validation**, **Data aggregation**.
  - Advanced: regionalized LCA, Life Cycle Costing, social aspects, data quality, Monte Carlo simulation, time parameter, system dynamics.
  - **EPDs**: create processes for target products → product systems → calculate → save results → create EPD; import EPD results (manual, soda4LCA, openEPD, ILCD); use EPD results inside life cycle models; upload to SmartEPD.
  - Libraries, scripting, collaboration server for teams.
- LCIA methods overview table: impact categories include water use, energy use, land use, acidification, climate change, resource depletion, ecotoxicity, eutrophication, human toxicity, ionising radiation, ozone layer depletion, particulate matter, photochemical oxidation. Methods listed: AWARE, CED, IPCC, USEtox 2, ReCiPe, Environmental Footprint, CML, TRACI. Note: "some impact methods only cover one specific impact category but represent also the foundation of other methods, e.g. IPCC is used in the Environmental Footprint method."
- Product system creation detail: reference process = "the process that models the last step of your supply chain"; auto-linking connects input/output flows between processes; cut-off threshold drops providers below a numeric contribution threshold across the whole connected supply chain.

## Product B — SimaPro (SimaPro B.V. / PRé)

### Key observations (Evidence layer A — official site + help center)

- Positioning: "SimaPro is life cycle assessment software that helps organizations measure, analyze, and reduce environmental impacts using robust datasets, scientific methods, and transparent modeling." Two editions: desktop ("expert modelling and analysis for comprehensive LCA studies") and cloud ("brings LCA into everyday business decision-making across products, teams, and workflows"). Vendor claims: 250k+ datasets, ~40 LCIA methods, pedigree matrices, Monte Carlo analysis, "full network visibility for complete traceability and audit readiness". (Marketing figures — recorded as vendor claims, not used as canonical facts.)
- Help center structure: SimaPro desktop (203 articles) / SimaPro cloud (35); collections: Getting Started, Use, Updates, Data (49), Impact Assessment Methods (12), Data Exchange (6), Results (8), Error Messages, Report Maker.
- **Unit vs system processes** (official article, quoting ISO 14040): "A unit process is the smallest element in the life cycle inventory analysis for which input and output data are quantified (ISO 14040)... A system process is a single, cradle-to-gate aggregation of all environmental flows caused by the provision of the reference product... also known as an aggregated life cycle inventory (LCI)." Unit process contains "only emissions and resource inputs from one process step, plus references to input from other processes"; system process "only contains inputs and outputs to and from the biosphere per reference product" — "experienced as a black box". Libraries ship in both forms; user chooses.
- **Network/tree calculation**: results window has a network tab; warnings when "not all products of this network are currently visible"; process contribution analysis; analysis of groups.
- **Parameters for scenario analysis**: parameters feature (license-dependent), calculated parameters, importing scenarios from Excel, linking data to Excel.
- **Monte Carlo**: license-dependent; "Behind the Scenes at Monte Carlo Simulations" article.
- **Recycling / end-of-life modeling** (official article): end-of-life allocation approaches listed — recycled content ("cut-off"), closed-loop scenarios, Circular Footprint Formula (CFF). ecoinvent cut-off system model: "wastes are the producer's responsibility ('polluter pays')... the resulting material or energy becomes available free of burden for a next application." Waste processing modeled directly or through **waste scenarios**; transformation processes under Waste treatment/Recycling are empty processes used in waste scenarios.
- **Multi-user**: user management, passwords, aliases, database management; integrated login.
- **Report Maker** as separate collection; EN 15804:A2 indicator calculation article; LCC possible; data exchange collection (import/export).
- Impact Assessment Methods collection (12 articles) — methods are managed objects; "How do I know if a substance is included in a method?" article shows flows ↔ method coverage checking.

## Product C — Ecochain Mobius (+ Helix)

### Key observations (Evidence layer A — official site + help center)

- Positioning: "LCA automation software" for manufacturers; "Calculate high-quality product footprints at scale"; outputs = EPDs, PCFs, environmental profiles; compliance claims: ISO 14040/44/67, EN 15804+A2; vendor claims: 2M+ LCAs, 450+ manufacturers. (Marketing figures — vendor claims.)
- Two products: **Mobius** ("everything product footprinting") and **Helix** ("everything portfolio footprinting" — facility/portfolio level). Help center collections: Mobius (29 articles), Helix (19), LCA Fundamentals (8), LCA Data (14), LCA Methods & Standards (8), LCA Toolkit ("everything related to executing environmental modeling", 7).
- Workflow (site): Collect (import BOMs via CSV/Excel/API; centralize product specs, supplier info, facility details) → Measure ("digital twins of your products and production facilities"; "cradle-to-gate or cradle-to-grave LCAs with primary and secondary data") → Share (generate/verify/publish EPDs, PCFs, LCA reports; publish via program operators NMD, MRPI, EPD Global, EPD International, IBU) → Improve (what-if scenarios: material swaps, supplier changes, production improvements).
- Mobius object model (FAQ): pages organized as **Products, Objects, Life cycles**; "you can certainly model a process in Mobius — provided you have the required data". Impact added to objects either via **LCI database datasets (e.g. ecoinvent)** or via **Custom Impact** (manual entries for selected impact categories).
- **Properties**: "Every object containing impact from an LCI database in Mobius should have a property attributed to it. Properties... help you tell Mobius what the relationship is between (i) the unit of the object in your inventory, and (ii) the unit of measurement of the ecoinvent dataset." Missing/wrong properties → zero impact.
- **Workspace settings**: calculation method + LCI database selected per workspace; incompatibility between database version and calculation method → impact displays as zero (e.g. ecoinvent dataset inside a PEF-method workspace).
- **Scenario feature**: "easily make a copy of your product's LCA, and make any desired changes to the copy... compare differences within a matter of minutes."
- Templates for key industries: Textile, Construction, Electronics, Food, Packaging; demo workspace (T-shirt).
- PCF guidance: ISO 14067 for carbon-only; PEF or EN 15804 for broader impact categories; IPCC method offered for carbon calculations; ISO 14021 for claims; Green Claims Directive context.
- Reporting: "Mobius has limited (automated) reporting capabilities" — automated 1-pager PDF; structure export (.csv) and total impact results (.xlsx); ISO 14044-compliant LCA background report possible; EPD writing currently manual (templates + expert services); third-party verification of Mobius LCAs is common and supported.
- Goal & Scope article (LCA Fundamentals): ISO 14040 four phases (Goal & Scope, LCI, LCIA, Interpretation); functional unit = "unit of measurement for your product", function-based for comparability; declared unit as fallback for cradle-to-gate; flowchart = "blueprint for constructing the LCA model"; system boundaries; PCRs prescribe functional units for EPD product groups.
- Subscription tiers: Professional (single user) / Business (unlimited objects, multiple colleagues). Pricing figures (€/month, €/EPD) are vendor marketing — recorded, not canonical.

## Product D — Brightway

### Key observations (Evidence layer A — official docs)

- Self-definition: "Brightway is an open-source software package for life cycle assessment (LCA) written in Python... designed to make it easy to work with large datasets and perform LCA calculations quickly and accurately. It focuses on flexibility and performance... strong user community in academia, and is increasingly gaining power users from industry and consulting." No GUI — code framework.
- Glossary (with explicit ISO mapping — strong evidence for the canonical concept set):
  - **Activity** = ISO "(unit) process or elementary flow".
  - **Production exchange** = ISO "product".
  - **Technosphere exchange** = ISO "intermediate flow" (exchange between two technosphere activities).
  - **Characterization factor**: "a biosphere exchange characterized (scaled) to a unit".
  - **Impact assessment method** = "a set of characterization factors" (ISO: impact category).
  - **Demand** = ISO "functional unit" ("the demand from the system to calculate for (e.g. 'one kilogram of steel')").
  - **Functional unit**: "the demand of goods and services used in a given calculation... made up of products, not processes... can have more than one product."
  - **Project**: "an isolated set of data sufficient to do LCA calculations" (own storage).
  - **Graph**: nodes (processes, products, biosphere flows, impact categories) + directed numeric edges; **functional edge** expresses the function of a process; **multifunctional process** = more than one functional edge.
  - **Database**: container for inventory nodes; "Brightway does not make a distinction between foreground and background databases" (practitioner-determined boundaries).
  - **Datapackage**: numerical data as arrays; "can also represent uncertainty and scenarios".

## Cross-product Comparison

| Aspect | openLCA | SimaPro | Ecochain Mobius | Brightway |
|---|---|---|---|---|
| Form | open-source desktop GUI (+ server, scripting) | commercial desktop + cloud | SaaS web app | Python framework, no GUI |
| Central modeled object | Product system built from processes (model graph) | Processes (unit/system) linked into networks/trees | Product → Objects → Life cycles | Activity graph (nodes + edges) |
| Functional unit | reference process + target amount | demand/reference flow at calculation | product + properties (unit mapping) | demand (explicit ISO mapping) |
| Inventory representation | flows in/out of processes | unit vs system (aggregated) processes | objects + linked datasets + custom impact | exchanges (technosphere/biosphere) |
| Impact assessment | LCIA methods/categories, CFs, editable/importable | IA methods collection; substance-in-method checks | workspace calculation method (PEF, EN 15804+A2, NMD…) | methods = sets of CFs |
| Background data | database-agnostic (ecoinvent, EF, GaBi, PSILCA importable) | ecoinvent-centric libraries (unit + system) | ecoinvent datasets + Custom Impact | user-supplied databases |
| Results surfaces | inventory + impact results, contribution tree, Sankey, groups, locations | network/tree results, process contributions, groups | per-product impact results, 1-pager PDF, xlsx export | programmatic matrix results |
| Scenarios/comparison | parameters + parameter sets; Projects compare systems | parameters for scenario analysis; Excel scenarios | scenario = copy & modify | datapackages/scenarios |
| Uncertainty | Monte Carlo, data quality | Monte Carlo, pedigree matrices | not observed in fetched docs | uncertainty in datapackages |
| End-of-life/recycling | waste modelling, allocation | cut-off / closed-loop / CFF, waste scenarios | not observed in fetched docs | not observed in fetched docs |
| Outputs | EPD creation, project reports, exports | Report Maker, EN 15804 indicators, data exchange | EPD/PCF support, verification-ready data | programmatic results |
| Audience | practitioners, academia, industry | LCA experts, consultants, enterprise | manufacturer sustainability/product teams | academia, power users |

### Cross-product commonalities (Evidence layer B)

1. **Product system as linked process network** — all four model a life cycle as processes/nodes connected by product flows (openLCA product system + auto-linking; SimaPro network/tree; Mobius life cycles over objects; Brightway graph).
2. **Functional unit / reference demand** — all four anchor quantification to a demand (reference process + target amount; demand; product unit; demand).
3. **Two-layer flow ontology** — technosphere (intermediate/product) flows vs elementary/biosphere flows appears in all four (openLCA flows + elementary flows; SimaPro unit/system process definitions; Brightway explicit ISO mapping; Mobius dataset-vs-object unit mapping).
4. **Impact assessment as a separate, selectable method layer** — methods with characterization factors applied to the inventory (openLCA LCIA methods; SimaPro IA methods collection; Mobius workspace calculation method; Brightway method = CF set).
5. **Background LCI databases** — all four connect to or ship large life cycle inventory datasets (ecoinvent named in three of four; openLCA additionally database-agnostic; Brightway user-supplied).
6. **Scenario/comparison machinery** — parameters, scenario copies, or project-level comparison in all four.
7. **Contribution/hotspot analysis** — contribution trees, process contributions, top-contributor views (openLCA, SimaPro; Mobius hotspots via site copy; Brightway programmatic).
8. **Import/export and exchange formats** — Excel/CSV in all; ILCD/EcoSpold-class formats in openLCA/SimaPro; data exchange collections.
9. **Reporting toward standards** — ISO 14040/44 frame named by all; EPD (EN 15804) machinery in openLCA/SimaPro/Ecochain; PCF (ISO 14067) in Ecochain/openLCA.

### Divergences (implementation, not Type)

- GUI vs code (Brightway has no GUI; still unmistakably LCA software).
- Database stance: agnostic (openLCA) vs bundled-ecoinvent-centric (SimaPro, Mobius) vs bring-your-own (Brightway).
- Expert depth vs automation: SimaPro/openLCA expose allocation, waste scenarios, Monte Carlo; Mobius hides/alleviates them (limited automated reporting, guided templates, expert services).
- Unit of analysis: product (Mobius focus) vs portfolio/facility (Helix) vs organization (openLCA organisational LCA variant).

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Life Cycle Assessment Application is recognizable by exactly three jointly-held structures:

1. **The life cycle model of a product system** — a linked network of unit processes spanning a defined system boundary of a product's life cycle, each process carrying quantified input/output flows (product/technosphere flows between processes; elementary flows to/from the environment). Remove → a flow-diagram tool or a process data catalog, not an assessment environment.
2. **The functional unit as the quantified anchor** — a stated demand (quantity of function or reference flow) to which the entire model and all results are normalized; the calculation is "impacts of delivering this unit". Remove → process data collection with no assessment anchor.
3. **The inventory → impact assessment calculation chain** — the system computes (a) the compiled life cycle inventory (aggregated flows over the whole linked network) and (b) characterized impact results by applying selectable impact assessment methods (characterization factors) to that inventory. Remove → a database or calculator; the "assessment" disappears.

Jointly-held load-bearing checks:
- 1+2 without 3 = process data collection / life cycle diagram (no results).
- 3 without 1+2 = emission-factor arithmetic with no product system (carbon calculator territory).
- 1+3 without 2 = unanchored chain; results not comparable or interpretable per function.

Not in L0 (checked against the historical/market-sample rule): background LCI databases (1990s tools used hand-entered data; openLCA can build databases from scratch; Mobius supports Custom Impact), GUI/model graph (Brightway is code-only), multi-impact breadth (single-category methods like IPCC climate-change-only are legitimate LCIA methods per openLCA's own overview), Monte Carlo, EPD machinery, cloud delivery, parameters, collaboration. All are standard or optional, not definitional.

### L1 — Common Mature Structure

- Background LCI database connectivity + database management (import/combine/update/validate; unit vs system process forms).
- Impact method libraries (ReCiPe, EF, CML, TRACI, IPCC, USEtox, AWARE, CED observed in-sample) + editing/creating methods and characterization factors.
- Result analysis: inventory results, impact results per category, contribution trees/process contributions, grouping, Sankey diagrams, locations.
- Scenario and comparison machinery: parameters/parameter sets, scenario copies, project-level comparison of alternative systems.
- Uncertainty and data quality: Monte Carlo simulation, pedigree/data-quality matrices (observed in openLCA + SimaPro; not universal in-sample).
- Allocation machinery for multifunctional processes (allocation factors; recycling/end-of-life approaches: cut-off, closed-loop, CFF; waste modeling/waste scenarios).
- Parameterization (global/process parameters, formula-driven amounts).
- Import/export: Excel/CSV universally; ILCD/EcoSpold-class exchange formats in expert tools.
- Reporting: report templates, EPD generation support, ISO 14044-class background reports.
- Collaboration: multi-user, shared databases/workspaces, servers.

### L2 — Variant / Optional Structure

- Deployment: desktop install vs SaaS vs code framework vs collaboration server.
- Audience posture: expert-practitioner depth vs non-expert automation (templates, guided flows, expert services).
- Sector packaging: buildings/EPD (EN 15804), food/agriculture, chemicals, electronics, textiles.
- Scope variants: cradle-to-gate vs cradle-to-grave; product vs organizational LCA; screening vs full studies.
- Extended assessment: Life Cycle Costing, Social LCA, regionalized LCA.
- Output channels: EPD program-operator publishing (NMD, IBU, EPD International…), PCF reporting, verification workflows.
- Portfolio/facility-level footprinting as a sibling product (Helix pattern).

### L3 — Vendor-specific (research notes only)

- openLCA: Nexus marketplace, SmartEPD upload, soda4LCA/openEPD import, collaboration server, scripting.
- SimaPro: unit/system library split of ecoinvent, Report Maker, license-tier feature gating (Monte Carlo, parameters, Power User), integrated login.
- Ecochain: Mobius "properties" unit-mapping mechanism, Custom Impact, Helix sibling product, "verify once, pay once" verification model, program-operator publishing set.
- Brightway: graph/datapackage architecture, project-as-directory storage, no foreground/background distinction.

## Vendor-specific Findings

See L3 above; also: SimaPro's marketing figures (250k+ datasets, ~40 methods, 35 years) and Ecochain's commercial figures (subscription prices, €/EPD, 2M+ LCAs) are vendor claims — not used in the canonical document.

## Boundary Findings

- **vs Carbon Accounting Platform**: different unit of analysis. Carbon accounting centers on the organization (scopes 1/2/3, activity data × emission factors, org boundary); LCA centers on the product system (functional unit, process network, multi-impact methods). Overlap exists (organizational LCA is a variant; carbon accounting platforms may embed product modules). Test: remove the functional-unit/product-system core and keep org/scope accounting → Carbon Accounting Platform.
- **vs Product Carbon Footprint Platform**: PCF is the single-impact (climate) deliverable; LCA applications center on the method layer with multi-impact assessment as the default posture (single-category methods supported as subsets). Many PCF-first platforms are LCA machinery with carbon-first UX (Ecochain sells both from one engine). This is the closest boundary in the directory; flagged for a taxonomy note.
- **vs Environmental Impact Assessment Platform**: EIA is regulatory assessment of projects/developments (site baselines, noise, ecology, mitigation) — a different object entirely despite the shared word "assessment".
- **vs Environmental Management System / ESG / Sustainability Management Platforms**: org-level management and reporting systems; they may consume LCA results but do not model product systems.
- **vs Scope 3 Management Platform**: supply-chain GHG estimation at organizational level (spend-/activity-based), not product-system modeling.
- **"去掉什么就变成另一个 Type" 判据**: remove the impact-assessment method layer → inventory/data tool; remove the product-system network → carbon calculator; remove the functional unit → process data collection; remove life-cycle scope (single stage only) → footprint calculator.

## Uncertainties

- One Click LCA and Umberto could not be fetched (source-access limitation); the SaaS pole is covered by Ecochain only, and the MFA/Sankey lineage (Umberto) is unverified in-sample. Assertions about those products are avoided.
- Mobius Monte Carlo / uncertainty support and end-of-life modeling depth were not observed in fetched docs — recorded as "not observed", not "absent".
- Exact numeric claims (dataset counts, method counts, prices, years) are vendor marketing and were deliberately excluded from the canonical document.
- The exact set of "standard" impact categories varies by method and region; the document names categories only as observed examples, not as a canonical list.

## Final Synthesis

The LCA Application is the modeling-and-assessment environment for product life cycles. Its world has three load-bearing structures held jointly: the product system (a linked network of quantified unit processes within a defined boundary), the functional unit (the demand that anchors and normalizes everything), and the inventory→impact calculation chain (compile flows, then apply selectable characterization methods to produce impact results). Around this core, mature products add background databases, method libraries, contribution/Sankey analysis, scenarios, uncertainty, allocation/recycling machinery, exchange formats, reporting/EPD support, and collaboration. Products differ legitimately in form (desktop/SaaS/code), audience (expert vs automated), and sector packaging — these are variants, not the Type. The nearest boundaries are carbon accounting (organizational vs product-system unit of analysis) and product carbon footprint platforms (carbon-first deliverable vs method-layer center).
