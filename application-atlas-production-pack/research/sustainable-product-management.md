# Research Notes — Sustainable Product Management

Research date: **2026-09-10**

## Research Goal

Understand what the market actually sells under the "product sustainability" / "sustainable product management" label: what the system centers on, what the unit of record is, how assessment machinery relates to management machinery, and where the boundary sits against the already-processed §21 siblings — product-carbon-footprint-platform (which pre-framed this leaf's seam as "design decisions vs computed figure"), life-cycle-assessment-application (model-first), sustainability-management-platform (org-grain program), supplier-sustainability-management (supplier standing), sustainable-procurement-platform (buying decisions) — plus the processed §16 product-lifecycle-management-plm and §05.04 product-information-management-pim.

Duties this pass:

- Discharge the forward seam recorded by the product-carbon-footprint-platform pass (2026-09-09): "sustainable-product-management (design decisions vs computed figure)".
- Test whether this leaf is a distinct Type or an umbrella/alias over the LCA Application + PCF Platform cluster.
- Test whether the management/improvement loop is definitional or merely common.

## Initial Boundary

Working hypothesis before research:

- Core purpose: the product-making organization's system for managing the environmental sustainability of its own product portfolio — assessing products' life-cycle impacts, working those assessments into product design/improvement decisions, and producing compliance/communication outputs from the same record.
- Likely users: sustainability teams, product designers/R&D, LCA specialists, procurement, compliance, management.
- Nearest neighbors: Product Carbon Footprint Platform (§21), Life Cycle Assessment Application (§21), Product Lifecycle Management / PLM (§16), Sustainability Management Platform (§21), Circular Economy Platform (§21), Supplier Sustainability Management (§21), Sustainable Procurement Platform (§21), PIM (§05.04). Name-collision neighbor: Product Management Platform (§12) — software product management, a different domain entirely.
- Known unknowns: Is the product portfolio's sustainability standing a real system-of-record object, or just the output of LCA/PCF tooling? Is the design-decision loop definitional? Does every product in the population carry its own computation engine, or are import/default-model poles legitimate? Where does eco-design stop and this Type begin?

## Research Questions

1. What do products sold as "product sustainability" platforms actually center on: the assessment, the figure, the design decision, or the portfolio?
2. What is the unit of record — the product (SKU/item/material/variant), the LCA model, or the assessment study?
3. What assessment machinery exists and how much does it vary (own LCA engine vs automated PCF vs default models vs imported results)?
4. What product data feeds assessment (BOM, formula, ERP production data, PLM structure, supplier data) and is any single ingestion path definitional?
5. What does the management loop look like: hotspots, scenarios, design decisions, portfolio governance, improvement tracking?
6. What outputs are produced (PCF figures, EPDs, reports, labels, DPP data, Scope 3 inputs) and are any definitional?
7. Who operates it day-to-day, and how is it packaged (standalone vs suite module vs ERP-carried)?
8. Where are the boundaries vs the processed siblings (PCF, LCA, PLM, sustainability-management, circular-economy, supplier-sustainability, sustainable-procurement, PIM)?
9. Would pre-software practice (spreadsheet product-environmental registers, commissioned LCA studies, eco-design checklists, paper EPD processes) satisfy the definition (historical check)?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer layers:

| Product | Philosophy / pole |
|---|---|
| iPoint Product Sustainability | Compliance-heritage suite pole: LCA automation + sustainability data management + reuse of product-compliance data (IMDS), role-specific apps, embedded in product development/sourcing/strategy; automotive/electronics/manufacturing enterprise base |
| AllocNow Product Sustainability Platform (PSP) | Automation-first pole for chemical/pharma/process industries: fully automated LCA/PCF from ERP production-network data, one rule set across the portfolio, no manual modeling, validation/approval workflow |
| Ecochain | Manufacturer portfolio pole (mid-market): LCA automation built as a reusable foundation — Collect → Measure → Share → Improve; EPD/PCF outputs at portfolio scale for non-experts |
| Footprinter | R&D/design-decision pole (consumer goods): assessment built around the design workflow — PLM/stage-gate structure, benchmarks, scenarios, "Manage the Sustainable Portfolio" governance |
| Worldly (Product Impact Calculator) | Consumer-goods supply-chain-data pole: product-level emissions modeling at scale starting from industry-standard default models, progressively improved with primary supplier/materials data; outputs feed Scope 3, Eco-Scores, DPP readiness |

Boundary specimens observed but not sampled as representatives: Kinset ("Connected Products Platform" — product + sustainability data aggregation without an evidenced computation engine; search-capture only), EasyLCA (SME pole), Makersite (PLM/CAD-integrated automated LCA), Sustainable Minds / Trace One Ecodex (earlier-generation eco-design tools), Altruistiq (eco-design scenario modeling).

## Sources

All fetched 2026-09-10 unless noted. Tier 2 (official product/solution pages) throughout; no Tier-1 help-center depth reached.

- iPoint-systems (official product page, fetched directly):
  - Product Sustainability — https://www.ipoint-systems.com/software/ipoint-product-sustainability/
  - Solution taxonomy visible in site navigation: Life Cycle Management, LCA, Carbon Footprint, PCF, Sustainable Design, Circular Economy, Supply Chain Transparency, IMDS.
- AllocNow (official solution page + on-site FAQ, fetched directly):
  - Solution — https://www.allocnow.com/solution
  - Homepage — https://www.allocnow.com/ (search capture)
- Ecochain (official homepage/product page, fetched directly):
  - https://ecochain.com/ (homepage; four-step workflow, EPD/PCF solutions, FAQ)
  - LCA solution page — https://ecochain.com/life-cycle-assessment-lca/ (search capture, 2026-09-10)
- Footprinter (official homepage, fetched directly):
  - https://footprinter.com/ (features, benefits, customer quotes from Reckitt annual report and PepsiCo ESG Topics A-Z)
- Worldly (official homepage + Product Impact Calculator page, fetched directly):
  - https://worldly.io/
  - https://worldly.io/tools/product-impacts/
- Search-capture observations (Tier 2/3, reduced strength): EasyLCA (easylca.ai/product), Kinset (kinset.com), Makersite (makersite.io), Sustainable Minds (sustainableminds.com/software), Trace One Sustainability (traceone.com), Altruistiq (altruistiq.com), CarbonBright (carbonbright.co), Portia (portia.cloud).

Sourcing limitations: no Tier-1 help centers or in-app documentation were reached for any sampled product (help centers exist for Ecochain and Worldly but were not needed for the canonical model; iPoint support portal not attempted). All evidence is official product/solution-page level. Precise operational details (numeric limits, exact state names, exact workflow steps inside the apps, pricing mechanics beyond vendor-published claims) are therefore not asserted anywhere in this pass. Vendor numeric claims (e.g., "2M+ LCAs", "40,000 suppliers", "€50 per EPD") are recorded as vendor claims only and excluded from canonical assertions.

## Product Observations

### iPoint Product Sustainability (compliance-heritage suite pole)

Key observations (evidence layer A — official product page fetched directly):

- Self-label: "Sustainability Software for Product Management" / "Product Sustainability Software for Environmental Data Management". Positioning: "Automate life cycle assessments (LCA) and manage sustainability data with one platform".
- Three named pillars: **Automate LCA at Scale** ("parameterized models, BOM imports, and data mapping – enabling fast, scalable rollouts across entire product families and portfolios"); **Integrate LCA Results into Business Decisions** ("Embed environmental and carbon footprint data directly into your product development, sourcing, and strategy processes"); **Optimize Environmental Performance Continuously** ("identify environmental hotspots, reduce emissions, and improve product sustainability over the entire life cycle – from early design to production, usage and end-of-life").
- **Role-specific web applications** "for, e.g., LCA experts, product developers, buyers, or top managers enable interactive views of sustainability information" — the multi-role surface is explicit.
- **Data reuse across domains**: "Re-use compliance data in order to calculate environmental impacts. Leverage data from various sources like ERP, CAD or LCA databases." The vendor's heritage product domain (IMDS — the automotive industry's material data system) is a named data source; compliance and sustainability are unified under an "Impact Intelligence" umbrella.
- **Sustainable product innovation**: "Roll out automated LCAs and carbon footprints to entire product families and use actionable insights to plan, design, and develop environmentally optimized products from the start."
- Solution taxonomy under the same product: Life Cycle Management, LCA (ISO 14040/14044), Carbon Footprint (CSRD), PCF (ISO 14067 / GHG Protocol / PAS 2050), **Sustainable Design** ("Use Compliance and Sustainability Data to design and develop more sustainable products, faster"), Circular Economy ("Support circular economy strategies at every product life cycle stage"), Supply Chain Transparency, Responsible Sourcing, IMDS.
- Production-efficiency analysis via material flow cost accounting (MFCA) — vendor-specific extension.
- Customer evidence: AUNDE Group (corporate + product carbon footprint); Volvo Cars case study — "tailors life cycle assessment information in order to support decision making throughout the company".

### AllocNow Product Sustainability Platform (automation-first, process industries)

Key observations (evidence layer A — official solution page + FAQ fetched directly):

- Self-label: "Product Sustainability Platform (PSP)" — "an enterprise SaaS solution that automates lifecycle assessments (LCAs) and product carbon footprint (PCF) calculations... delivers product-level sustainability metrics at portfolio scale, across all products, all plants, for every team that needs them."
- **The product portfolio is the managed population**: "Automate lifecycle assessments for every product and intermediate, not just bulk products"; granularity at "material-production plant" level — "a product manufactured at multiple sites receives a distinct LCA/PCF for each location".
- **Computation from operational data, explicitly NOT BOMs**: "AllocNow does not rely on Bills of Materials for its calculations. Instead, the platform uses actual operational data, specifically the real material movements and transaction records from the ERP system, to model the production network." — strong anti-overfit evidence against making BOM ingestion definitional.
- **One rule set across the portfolio**: "One transparent rule set is applied consistently across every product and intermediate, eliminating discretionary modeling choices" — methodological consistency as a management requirement at portfolio scale.
- **No manual LCA modeling**: "the platform constructs and calculates the lifecycle assessment model automatically from existing operational data, without requiring any manual LCA modeling... This eliminates the need for LCA experts to configure individual product models."
- **Results management**: "a built-in results management workflow that supports the structured validation and approval of calculated PCF and LCA results... role-based access control... Automated deviation checks flag changes between calculation periods, and approval thresholds can be configured."
- **Portfolio aggregation**: "aggregation of product environmental footprints across both organizational hierarchies, such as regional and global rollups, and product hierarchies, such as product families and business units."
- **Decision machinery**: Contribution Analyzer ("drill down into contributions from raw materials, individual production processes, and intercompany transportation to identify the highest-impact levers"); Scenario Tool ("model changes to raw material emission factors, energy sources, supplier substitutions, or process configurations and immediately see the resulting effect... supporting collaborative, data-driven decisions about reduction levers and capital investments").
- **Outputs**: standardized configurable PDF reports for approved results "shared with customers, auditors, and regulators"; TfS PCF certification support; Scope 3.1 data for corporate reporting.
- **Roles**: "sustainability managers, procurement teams, R&D, marketing and sales, finance, and product management, each with access to the data and features relevant to their role."
- **Data currency**: "PCFs and Scope 3 data stay current with automated refresh cycles."
- Multi-impact: "Customers can choose relevant impact categories and methods such as the Product Environmental Footprint (PEF) method... global warming potential, water use, fossil fuel consumption, land use..." — carbon-led with multi-impact extension.

### Ecochain (manufacturer portfolio pole)

Key observations (evidence layer A — official homepage fetched directly; LCA page via search capture):

- Self-label: "LCA automation software that helps manufacturers measure, manage and communicate the environmental impact of their products at scale."
- **The four-step workflow is the product's own articulation of the management loop**: "Collect — Centralize your product and supplier data in one place. Import your BOMs via CSV, Excel or API. Ecochain organizes all your product specs, supplier information, and facility details in one structured system" → "Measure — Turn your product data into measurable impact using digital twins of your products and production facilities. Run cradle-to-gate or cradle-to-grave LCAs with primary and secondary data" → "Share — Generate, verify and publish various product footprint reports at scale... Verified EPDs, PCFs, and environmental profiles – ready to publish via POs like NMD, MRPI, EPD Global, EPD International or IBU" → "Improve — Create what-if scenarios to make better product decisions. Run scenario analyses to test material swaps, supplier changes or production improvements before you commit."
- **Reusable foundation, not one-off studies**: "The LCA foundation you build on Ecochain grows with you. No rebuilding from scratch. You expand and reuse what you've already built"; "Calculated once, reused everywhere – never rebuilt from scratch for the next customer, tender or product innovation project" (LCA page, search capture).
- **Portfolio scale**: "Whether it's 5 products or 5000"; "Run LCAs for a handful of products or manage compliance across your entire catalog."
- **Built for non-experts**: "Built for non-experts. Low total cost of ownership"; "You don't need a PhD or LCA expertise to use Ecochain software" — with expert services alongside.
- **Outputs**: EPDs (EN 15804+A2, ISO 14025), PCFs (ISO 14067, GHG Protocol), environmental profiles, LCA reports; publish to program operators; "Environmental impact data structured for Digital Product Passports (DPPs)" (LCA page, search capture).
- **Decision support**: "Use LCA data directly into ecodesign and sustainable product development decisions"; customer quote (Lightronics R&D): "We identified hotspots to improve and made smarter design choices"; customer quote (Buffy): "print footprint decisions to the earliest stage of our planning process, allowing us to proactively plan more sustainable product lines."
- **Regulation-readiness as a standing property**: "Built for the regulations you're managing today. Ready for the ones coming tomorrow... When regulations change, you update your data and regenerate results in days, not months."

### Footprinter (R&D/design-decision pole)

Key observations (evidence layer A — official homepage fetched directly):

- Self-label: "A complete, customizable software platform for product sustainability assessment, innovation and improvement." Positioning: "embed sustainability in R&D and make better and earlier sustainable design decisions."
- **Assessment fitted to the development workflow**: "LCA that fits your products, your process, your language... Use your PLM structure — Match your stage-gate naming, product specs, serving sizes, and BOMs."
- **Design-decision surfaces**: "Informed Design Decisions — Actionable insights at the moment of design... Benchmark performance — Instantly compare versions, brands, and category norms... Explore what's possible — Experiment fast with flexible, intuitive bottom-up modeling. Try substitutions, right-size components, or eliminate entirely."
- **Portfolio governance**: "Manage the Sustainable Portfolio — Tools to move from green ideas to green results: Stage-gate ready (set approvals and checkpoints at key design decisions); Find the winners early (identify high-impact projects and course-correct weak ones); Report with confidence (track, share, and scale success across your organization)." A "Performance Framework built to a single score."
- **Non-expert users named**: "Product designers. Packaging designers. Category and brand managers. R&D leadership and managers. Sustainability team. No training required."
- **Collaboration machinery**: "Team-based projects — Multi-user collaboration with project-level permission settings; Clear handoffs — Visual chevrons track completion status across the project lifecycle."
- **AI machinery**: factor assignment, ERP/PLM integration, industry benchmarking, component benchmarking (including recycled content and renewable inputs).
- **Customer-program evidence** (from customers' own documents, quoted on the vendor page): PepsiCo "Sustainable from the Start (SftS), an internal product design program, provides life cycle analysis tools to estimate products' total environmental impact during their early design and development phase... Results from SftS are then incorporated into the new product development business process for visibility and decision-making. When the SftS process identifies an opportunity between a product and our design standards or long-term sustainability goals – such as non-recyclable packaging – the product team is required to develop a future solution or mitigation plan." Reckitt: "A key tool is our Sustainable Innovation Calculator. This helps us compare the sustainability of product innovations with existing benchmarks."

### Worldly / Product Impact Calculator (consumer-goods supply-chain-data pole)

Key observations (evidence layer A — official homepage + PIC page fetched directly):

- Platform self-label: "the leading sustainability data and analytics platform for retail and consumer goods companies" — supply-chain-data-centric overall; the product-grain machinery is the **Product Impact Calculator** ("Product-level Scope 3 calculations at scale"), grouped on the site under "Product compliance & impacts" alongside Materials LCA, French Eco-Scores, Digital Product Passport, Product Environmental Footprint.
- **Product-level modeling at portfolio scale**: "a product-level emissions modeling tool that helps consumer goods brands quantify environmental impact at scale — starting with industry-standard default models and improving accuracy by integrating primary supplier and materials data. It covers product categories across seven consumer goods industries."
- **Estimate-first posture is explicit and legitimate**: "Detailed lifecycle assessments are precise, but slow and expensive. Spend-based estimates are fast but too blunt... Worldly's Product Impact Calculator enables you to model emissions at scale, starting with industry-standard defaults, then replacing averages and assumptions with primary supplier and materials data." — the standing is explicitly a mixture of default-model estimates and progressively substituted primary data.
- **One connected dataset, many outputs**: "combines product, materials, and supplier performance data into one connected dataset. The same dataset powers multiple outputs, supporting Scope 3 reporting and product-level compliance" — Scope 3 Cat 1, French Eco-Score outputs, EU PEF and DPP readiness.
- **Decision orientation**: "Identify emissions hotspots, prioritize action, and prove decarbonization progress"; customer story (KMD Brands): "a way to connect product decisions, supplier performance, and emissions outcomes—at scale."
- **Methodological consistency over one-off studies**: customer quote (Komar): "we benefit from one consistent methodology even as we expand our data collection efforts... which isn't the case for typical lifecycle assessments."
- **Distinction from LCA stated by the vendor itself**: "A traditional lifecycle assessment is precise but resource-intensive — typically conducted product by product... Worldly's Product Impact Calculator is designed to deliver product-level emissions modeling at scale... Unlike standalone LCAs, it connects to existing supply chain data already in Worldly."

## Cross-product Comparison

| Dimension | iPoint | AllocNow | Ecochain | Footprinter | Worldly PIC |
|---|---|---|---|---|---|
| Unit of record | product / product family, portfolio | product + intermediate, per plant | product / portfolio / facility | product, project, portfolio | product (SKU), product categories |
| Assessment machinery | parameterized LCA models, BOM import, auto-mapping | fully automated from ERP production network; no BOMs; one rule set | LCA engine + digital twins of products/facilities | LCA fitted to workflow; bottom-up modeling | industry-default models → primary-data progression |
| Impact breadth | multi-impact + carbon | carbon-led + selectable multi-impact (PEF) | multi-impact (LCA) + carbon | GHG, water, water risk, packaging recyclability | emissions-led + Eco-Score (multi-criteria) |
| Product data ingestion | BOM, ERP, CAD, compliance data (IMDS) | ERP material flows, energy, emissions | BOM (CSV/Excel/API), specs, supplier, facility | PLM structure, stage-gate naming, BOMs | purchase orders, supplier data, materials data |
| Hotspot/contribution analysis | yes | yes (Contribution Analyzer) | yes | yes (Drivers) | yes |
| Scenario / what-if | design optimization options | yes (Scenario Tool) | yes (step 4) | yes (substitutions, right-sizing) | not evidenced on PIC page |
| Design-decision embedding | product development, sourcing, strategy | reduction levers, capital decisions | ecodesign, planning stage | stage-gate approvals, design moment | product decisions ↔ supplier performance |
| Outputs | PCF, LCA results, CSRD inputs | PCF/LCA reports, TfS certification, Scope 3.1 | EPDs, PCFs, profiles via program operators, DPP data | performance framework, business-ready results | Scope 3 Cat 1, Eco-Scores, DPP/PEF readiness |
| Non-expert posture | role-specific apps incl. buyers, top managers | cross-functional; minimal training | built for non-experts + expert services | "no training required" designers | brands' sustainability/sourcing teams |
| Governance machinery | role-specific views | validation/approval workflow, deviation checks | verify-once scope | stage-gate checkpoints, permissions | audit-ready default models |
| Portfolio aggregation | product families | org + product hierarchies | portfolio/facility | portfolio, brands, categories | full portfolio from day one |
| Suite context | compliance suite (Impact Intelligence) | standalone | standalone + services | standalone, custom-fit | supply-chain data platform |

Cross-product commonalities (evidence layer B):

1. **Product-grain managed population** — every sampled product manages a portfolio of identified products (SKU/item/material/variant/intermediate), not one-off studies. 5/5.
2. **Per-product assessed sustainability standing, maintained and re-computable** — results attach to products, are refreshed as data/products change (AllocNow refresh cycles; Ecochain regenerate-in-days; iPoint "all phases of your product development cycle"). 5/5.
3. **Assessment machinery over a declared life-cycle boundary** — product data × impact data (LCI databases / factors / default models) through LCA/PCF-class computation. 5/5, with radically different realizations (see anti-overfit).
4. **Hotspot/contribution analysis** — 5/5.
5. **Decision/improvement loop on the product itself** — scenarios, design trade-offs, reduction levers, portfolio governance; outcomes tracked. 5/5 (depth varies: Footprinter deepest, AllocNow lightest).
6. **Outputs for parties beyond the calculating team** — customer responses, reports, certifications, labels/passports data, Scope 3 inputs. 5/5 (form varies).
7. **Multi-role surfaces beyond LCA experts** — designers/product developers, procurement, sustainability, management. 5/5 (iPoint, AllocNow, Footprinter name them explicitly).
8. **Methodological consistency at portfolio scale** — one rule set / one methodology / reusable foundation, contrasted by vendors themselves with one-off studies. 4/5 explicit (AllocNow, Worldly, Ecochain, Footprinter-implied).
9. **Estimates as first-class entries** — secondary databases, industry defaults, screening LCAs. 4/5 explicit (AllocNow, Ecochain, Worldly; iPoint via LCI databases).
10. **Integration with product-development and enterprise systems** — PLM/ERP/CAD/APIs. 5/5.

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest stable structure without which the system stops being recognizable as this Type:

```text
Product portfolio's sustainability standing of record
└── Assessment machinery producing that standing
    └── Product-decision loop working that standing
```

1. **The product portfolio's sustainability standing of record** — persistent identified product records (SKU/item/material/variant grain) each carrying sustainability standing: assessed environmental impacts (carbon among them, multi-indicator common), sustainability attributes (materials, recycled content, recyclability-class facts), and compliance/labeling status — accumulating across product versions/periods as a managed portfolio, not one-off studies. Remove → product master data with ESG fields (PIM/PLM territory) or a pile of disconnected studies.
2. **The assessment machinery producing that standing** — product data (BOM/formula/production/supplier) × impact data (LCI databases, emission factors, industry-default models) through LCA/PCF-class computation over a declared life-cycle boundary, held re-computable and traceable. Sourced variably: in-product engine, automated network models, default-model progression, imported assessment results. Remove → labels of unknown provenance; the management loop has nothing to work with.
3. **The product-decision loop working the standing** — the standing exists to be worked into decisions about the products themselves: hotspot/contribution analysis → design/scenario/improvement choices (ecodesign trade-offs, reduction levers, portfolio governance) → tracked outcomes feeding back into the record, plus outward outputs (figures, declarations, label/passport data) produced from the same record. Remove → figure-delivery machinery (the PCF platform's center) or a static scorecard nobody decides with.

Jointly-held load-bearing:

- 1 alone = product master data with sustainability attributes (PIM/PLM drift).
- 2 alone = LCA/PCF tooling (the sibling Types).
- 3 alone = generic design governance with sustainability vocabulary.
- 1+2 without 3 = the product-footprint platform pole — the closest failure mode; distinguished from this Type only by center of gravity (figure-first vs standing-and-decisions-first).
- 2+3 without 1 = one-off consulting study with recommendations.
- 1+3 without 2 = claims with no computation behind them.

### L1 — Common Mature Structure

Present in most mature products, not required to define the Type:

- product data ingestion (BOM/formula imports, ERP/PLM/CAD connections)
- impact data foundations (licensed LCI databases, emission-factor libraries, industry-default models)
- hotspot / contribution analysis with drill-down
- scenario modeling / what-if comparison
- output generation (PCF figures, EPDs, reports, label/passport data, Scope 3 inputs)
- multi-role surfaces with role-based access
- versioning, audit trails, validation/approval workflows
- portfolio aggregation across product and organizational hierarchies; benchmarking
- supplier-data integration (supplier-specific factors, primary data collection)
- integrations with PLM/ERP/PIM and APIs

### L2 — Variant / Optional Structure

Depends on segment, industry, era, regulatory context:

- computation posture: full in-product LCA engine / automated PCF-first / default-model progression / imported assessments
- impact breadth: carbon-led vs multi-indicator
- decision depth: design-workflow-embedded (stage-gates, performance frameworks) vs figure-and-report-first
- output regime: EPD program-operator publishing, DPP data, eco-scores, consumer labels, certification support
- industry packaging: chemicals/process, manufacturing/construction, consumer goods/apparel, food & beverage
- packaging: standalone vs compliance-suite module vs ERP-carried
- customer scale: enterprise vs SME
- AI machinery (factor matching, auto-mapping) — era-current
- regulatory-regime machinery (CSRD, ESPR, CBAM, CPR, French Eco-Score) — regime packaging

### L3 — Vendor-specific Structure

- iPoint: IMDS compliance-data reuse, MFCA production-efficiency analysis, "Impact Intelligence" umbrella, role-app taxonomy
- AllocNow: Production Network Model from ERP transactions, Scope 3 Matching App, DQR ratings per TfS, biogenic-carbon split reporting, SiGreen integration
- Ecochain: verify-once-pay-once EPD commercial model, four-step Collect/Measure/Share/Improve articulation, program-operator publishing set (NMD/MRPI/IBU/EPD Global)
- Footprinter: dynamic templating engine / near-custom fit, single-score Performance Framework, visual chevron handoffs, sandbox→pilot→rollout motion
- Worldly: Higg FEM facility data as upstream substrate, Axion risk intelligence, 7-industry category coverage, purchase-order-connected product units

## Vendor-specific Findings

See L3. Additionally: Ecochain and iPoint both sell LCA/PCF/EPD as named solutions under one roof — packaging overlap with the sibling Types, not Type collapse (same pattern the LCA and PCF passes recorded for Sphera/Sustamize). Worldly's platform center is supply-chain data; its Product Impact Calculator is the product-grain member of this Type's population inside a broader platform — suite-carried realization.

## Boundary Findings

**vs Product Carbon Footprint Platform (§21, processed 2026-09-09)** — the closest seam; that pass pre-framed it as "design decisions vs computed figure". Ratified from this side, keep-both: the PCF platform's object of work is the maintained per-product carbon figure and its delivery to requesting parties; this Type's object of work is the product portfolio's sustainability standing and the decisions taken on it (design, improvement, compliance). Overlap zone is wide — both compute product-grain footprints, both carry hotspot/scenario machinery (the PCF pass holds those as standard-capability-not-definitional), and vendors sell both from one engine (Ecochain: EPD + PCF solutions over one LCA foundation; iPoint: PCF as one solution inside Product Sustainability). Center of gravity decides per product, per the sustainability-management/esg-reporting precedent. A carbon-led, delivery-first product belongs to the PCF pole; a portfolio-managed, decision-first product belongs here.

**vs Life Cycle Assessment Application (§21, processed 2026-09-08)** — keep-both: the LCA application's object of work is the editable multi-impact product-system model (product system graph + functional unit + inventory→impact chain; expert tool). This Type treats the LCA model as machinery — often automated, parameterized, or hidden (AllocNow: "without requiring any manual LCA modeling"; iPoint: "parameterized models... auto mapping"; Worldly: default models instead of models). The unit of record differs: the model vs the product portfolio. Worldly states the distinction from its own side ("Unlike standalone LCAs...").

**vs Product Lifecycle Management / PLM (§16, processed 2026-09-09)** — keep-both: PLM is the system of record for the product's *definition* (items/BOM/revisions/change processes). This Type is the system of record for the product's *sustainability standing* (impacts, attributes, compliance status). They interlock by ingestion (Footprinter matches PLM structure and BOMs; iPoint leverages ERP/CAD data; Makersite integrates PLM/CAD) — direction of truth-flow: PLM defines, this Type assesses and works. PLM vendors adding sustainability modules are suite extensions, not this Type's collapse.

**vs Sustainability Management Platform (§21, processed 2026-09-10)** — keep-both: that Type is the organization's own sustainability program (org/site-grain estate + collection + program). This Type is product-grain: the unit of record is the product, the decision surface is product design. Product footprints feed corporate/CSRD reporting upward (AllocNow, iPoint, Worldly all name this), but the estate and program are not the center here.

**vs Circular Economy Platform (§21, processed 2026-09-07)** — keep-both: that Type is a multi-party platform for keeping products/materials in circulation (loops across organizations). This Type manages the sustainability of one organization's own portfolio; circularity appears as design-time assessment (recyclability, end-of-life scenarios — iPoint's Circular Economy solution, Footprinter's packaging recyclability) rather than multi-party circulation machinery.

**vs Supplier Sustainability Management (§21, processed 2026-09-10)** — keep-both: that Type's unit of record is the supplier company's sustainability standing; this Type's is the product's. Supplier data enters here as assessment input (supplier-specific factors, primary data — AllocNow, Worldly), not as the managed population.

**vs Sustainable Procurement Platform (§21, processed 2026-09-10)** — keep-both: that Type embeds sustainability into buying decisions (qualification, tenders, award); this Type works sustainability into product design/management decisions. Different decision surface, different unit of record.

**vs Product Information Management / PIM (§05.04, processed 2026-09-06)** — keep-both: PIM governs commercial product content for selling channels; this Type holds assessed sustainability standing and works it into decisions. The Kinset-style "single source of truth for product + sustainability data" aggregation pole (search-capture only, no computation engine evidenced) marks the uncertain seam toward a data-hub shape — recorded under Uncertainties.

**vs Product Management Platform (§12, unprocessed)** — name collision only: software product management (roadmaps, discovery) is a different domain; no boundary work needed beyond noting the collision.

**Leaf-name observation**: the market says "product sustainability platform/software" (AllocNow, iPoint, CarbonBright) or "sustainable product design"; the directory leaf says "Sustainable Product Management". Same population, label variant. No directory change.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the L0?

- **Pre-software practice**: a manufacturer keeping a per-product environmental data register (spreadsheet/card file), commissioning LCA studies per product from consultants, applying eco-design checklists/guidelines in development, applying for eco-labels and producing paper EPDs — satisfies all three legs (portfolio standing + assessment machinery + decision loop) with no cloud, AI, or modern machinery. The Type predates its current label; historical check passes at class level (moderate-high confidence, practice-inferred).
- **Earlier-generation software**: Sustainable Minds (circa 2010s, "Eco-concept + Life Cycle Assessment software... integrate life cycle thinking and LCA into their product development processes") and Trace One Ecodex (eco-design for formulas, non-experts) fit the L0 — design-decision-oriented assessment over product populations.
- **Corporate-program pole**: PepsiCo's documented "Sustainable from the Start" internal program (LCA tools in early design, results incorporated into the NPD business process, mitigation plans required) shows the management loop predating and independent of any specific vendor — the loop is the discipline, the software its current substrate.
- **Regional output regimes**: Dutch NMD, German IBU, French Eco-Score — regional realizations of the output leg, not definitional.

The check warns against defining the Type by the current automation-era implementation (AI factor matching, ERP network models): the invariant is the standing + machinery + loop, not any specific computation posture.

## Uncertainties

1. **The no-engine pole**: whether a product-sustainability data-estate product without its own computation engine (Kinset-style aggregation + compliance outputs) belongs inside this Type (leg 2 satisfied by "imported assessment results") or marks the boundary toward PIM/data-hub territory. Search-capture evidence only; unresolved. The L0 wording ("sourced variably... imported assessment results") deliberately leaves room, but the population boundary is uncertain.
2. **The PCF seam's operational sharpness**: because the PCF platform's standard capabilities include hotspot/scenario machinery, the two Types' feature sets overlap almost entirely; the seam rests on center of gravity (figure-first vs standing-and-decisions-first). This is consistent with sibling §21 seams but is the softest boundary in this pass.
3. **Worldly's Type membership**: the platform's center is supply-chain data; only its Product Impact Calculator (plus Materials LCA / Eco-Score / DPP tools) sits in this Type's population. Treated as a suite-carried realization; if the whole platform were the unit of analysis it would drift toward supplier-sustainability/supply-chain-data territory.
4. **SME pole depth**: EasyLCA/Portia-class SME products (search-capture) appear to satisfy the L0 but were not directly fetched; no claims rest on them.
5. **ERP-suite pole**: SAP-class product footprint management was not sampled; the suite-carried variant is inferred from iPoint's suite context + market structure, held at variant strength.

## Final Synthesis

The market population is real and distinct from both sibling Types: products sold as "product sustainability" platforms are portfolio-management systems for the environmental sustainability of a manufacturer's own products. Their defining core is three jointly-held structures: the product portfolio's sustainability standing of record; the assessment machinery producing it (radically variable in realization — from expert LCA engines to fully automated ERP-driven computation to default-model progression — which is why no single ingestion path or engine posture is definitional); and the product-decision loop working the standing (hotspots → scenarios → design/improvement/compliance decisions → tracked outcomes), which is what separates the Type from the figure-delivery PCF pole and the model-first LCA pole. Everything else — BOM ingestion, multi-impact breadth, EPD publishing, DPP, AI matching, stage-gates, industry packaging — is common, variant, or vendor-specific. The Type sits in a three-way cluster with Product Carbon Footprint Platform and Life Cycle Assessment Application; the seams are center-of-gravity seams, ratified keep-both/all-three, with the overlap zone documented for future joint review.
