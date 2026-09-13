# Research Notes — Product Carbon Footprint Platform

## Research Goal

Understand what a Product Carbon Footprint (PCF) Platform really is from real products: what objects exist inside it, what users do with them, how a product's carbon figure is produced and maintained, how figures move between supply-chain parties, which rules govern the calculation, and where the Type's boundary lies against neighboring sustainability software (Life Cycle Assessment Application, Carbon Accounting Platform, Scope 3 Management, Supplier Sustainability Management).

This pass also discharges the joint-review flag left by the life-cycle-assessment-application pass (2026-09-08): that pass proposed the seam "PCF = single-impact (climate) deliverable centered on the carbon figure; LCA = method-layer center with multi-impact default" and recommended this pass treat LCA machinery as the PCF Type's substrate.

## Initial Boundary

Working hypothesis before research:

- Core use: computing and maintaining the greenhouse-gas footprint of individual products (kg CO₂e per unit) at portfolio scale, and delivering those figures to the parties who request or consume them (customers, regulators, labels, corporate inventories).
- Likely users: product sustainability managers, LCA/carbon analysts, procurement teams (requesting supplier PCFs), suppliers (computing and responding), R&D/product design (eco-design), ESG reporting teams.
- Nearest neighbors: Life Cycle Assessment Application (model-first, multi-impact), Carbon Accounting Platform (organization as unit of account), Scope 3 Management Platform (org-level supply-chain estimation), Supplier Sustainability Management (broad supplier ESG data), Sustainable Product Management (design-decision-centered).
- Likely confusion: PCF vs LCA (deliverable-first vs model-first); PCF vs carbon accounting (product vs organization as unit of analysis).

## Research Questions

1. What is the central managed object — the product record? the footprint? the calculation model?
2. How is the per-product figure computed: what data goes in (BOM, activity data, supplier data), what factors are applied, what boundary is declared?
3. Is the figure a one-off result or a maintained, re-computable record? What triggers recomputation?
4. Who consumes the figure, and through what surfaces (customer responses, reports, data exchange, labels, corporate-footprint pull-in)?
5. Is there a request/response loop between buyers and suppliers? How is it standardized (PACT, Catena-X, TfS)?
6. What role do emission-factor databases and LCA data play — bundled, licensed, integrated?
7. What standards govern the calculation (ISO 14067, GHG Protocol Product Standard, PAS 2050, PEF) and how do products signal conformance?
8. How do products handle portfolio scale (thousands of SKUs) — automation, AI matching, bulk edits?
9. Where does eco-design/scenario modeling sit relative to the deliverable?
10. Where is the seam to LCA applications and to organizational carbon accounting, concretely, in products that sell both?

## Representative Products

Selected for market representativeness, documentation reachability, and spread across product philosophy and customer tier:

| Product | Vendor | Philosophy / pole | Customer level |
|---|---|---|---|
| Sustamize (sustamizer platform) | sustamize | pure-play PCF data + calculation platform; CO₂e reference database as the foundation; ERP/PLM/costing-tool integration; manufacturing/cost-engineering angle | manufacturers, mid-market to enterprise, consultants |
| CO2 AI | CO2 AI | enterprise PCF at scale + free PCF exchange network (Product Ecosystem); corporate + product + supplier in one platform; CPG/chemicals/automotive | global enterprises |
| Vaayu | Vaayu (now part of Carbonfact) | retail/e-commerce automation pole; real-time impact computation from commerce systems; consumer-facing labels (Eco-Score, DPP) | retail brands, marketplaces |
| Sphera (LCA Automation + Supplier PCF Calculator) | Sphera | LCA-suite vendor producing PCF deliverables from LCA machinery; Managed LCA Content database; supplier-side PCF tooling | enterprise, expert teams |
| Watershed (Product Footprints) | Watershed | organizational carbon platform with a product-footprints module; PCF reports for customers + corporate-footprint pull-in | Fortune 500 |

The sample spans: pure-play data-first (Sustamize), exchange-network enterprise (CO2 AI), retail automation (Vaayu), LCA-suite (Sphera), org-suite module (Watershed). Standards context from PACT (WBCSD Partnership for Carbon Transparency).

Rejected/abstained: Ecochain Mobius (already deeply sampled by the LCA pass; product-footprint pole overlaps), One Click LCA and Umberto (unreachable in the LCA pass; not retried), Carbonfact (Vaayu's acquirer; site not fetched this pass — consolidation recorded as market-structure evidence only).

## Sources

All fetched 2026-09-09.

- Sustamize: https://www.sustamize.com/ (home), https://www.sustamize.com/product-carbon-footprint-calculation (PCF calculation workflow + tools), https://www.sustamize.com/lca-vs-pcf (LCA vs PCF differentiation page)
- CO2 AI: https://co2ai.com/ (home + FAQ), https://co2ai.com/platform/product-carbon-footprint (PCF module), https://co2ai.com/co2-ai-free-carbon-data-exchange-platform-pcf (Product Ecosystem exchange)
- Vaayu: https://www.vaayu.tech/ (home + FAQ; Carbonfact acquisition banner)
- Sphera: https://sphera.com/product-sustainability-software/ (LCA for Experts + solution tree), https://sphera.com/solutions/product-stewardship/life-cycle-assessment-software-and-data/lca-automation/ (LCA Automation), https://sphera.com/solutions/supply-chain-risk-management/supplier-engagement-solution/supplier-pcf-calculator/ (Supplier PCF Calculator)
- Watershed: https://www.watershed.com/ (platform), https://www.watershed.com/solutions/product-footprints (Product Footprints)
- PACT: https://www.carbon-transparency.org/pact-methodology (PACT Methodology V3, network, industry framework alignment)

Sourcing limitation: no product's gated help-center / in-app documentation was reachable in this pass; all product evidence is from official product pages, solution pages, and on-site FAQ sections. Precise operational details (exact data schemas, exact exchange-format implementations, pricing, numeric limits) are therefore not asserted. Vendor numeric claims (factor counts, speed multipliers, customer counts) are recorded as vendor claims only.

## Product A — Sustamize

### Key observations (Evidence layer A — official product pages)

- Self-positioning: "Reliable CO₂e Data for Product Carbon Footprint (PCF) Calculations"; product lines: CO₂e Databases, PCF Calculation, Sustamizer (the platform, separate login domain), API Integration, PCF Service, Data Research. A customer testimonial names the "sustamize Product Footprint Engine".
- PCF calculation workflow (three steps, vendor-stated): 1) Define scope and life-cycle boundaries — "Determine whether to apply a cradle-to-gate approach, covering emissions up to the factory gate, or a cradle-to-grave perspective, including use phase and end-of-life. Clear boundaries ensure comparability and standards alignment." 2) Collect & structure data — "Gather data across materials, manufacturing, logistics and use phase. Integrate supplier inputs and secondary emission factors to build a consistent and transparent calculation model." 3) Calculate & apply results — "Apply LCA methodologies to quantify emissions in kg CO₂e. The resulting PCFs enable Scope 3 reporting, hotspot identification and targeted decarbonization strategies."
- Named tools: **Matcher** ("Automatically map custom BoM names to the correct entries in the PCF database using AI"), **Assembler** ("Create ISO 14067-compliant PCFs fast, no deep LCA expertise or complex software needed"), **Interpreter** ("Paste or upload a BoM and instantly get matched materials with CO₂ values, one-click to Assembler"), **MPN Search** ("Enter a Manufacturer Part Number to retrieve emission factors (kgCO₂/kg and kgCO₂/pcs)").
- Data foundation: validated material CO₂e values; bottom-up modeling "mapping real-world processes step by step"; sources = peer-reviewed LCA studies, industry datasets, scientific publications, standardized environmental reports; Kyoto gases → CO₂e via IPCC GWP; aligned with GHG Protocol and ISO 14067. Vendor claims: 7M+ verified emission factors, biannual updates, API-first.
- Maintenance posture: "PCFs Are Not Static Values. Changes in material sourcing, supplier performance, energy mixes or updated emission factors directly impact CO₂e results. Static databases or one-time LCA studies quickly become outdated and limit comparability over time." Platform "designed for portfolio-level recalculation".
- Integration: "Sustamize connects carbon data directly to your ERP, PLM, or reporting systems"; software-provider use case embeds CO₂e data into costing tools (cost engineering).
- Use cases by role: cost engineering (carbon alongside cost), procurement (Scope 3 upstream, supplier hotspots), product design (early-stage impact), sustainability (ESG/CSRD/CBAM compliance), non-EU suppliers (supplier data workflows).
- LCA vs PCF page (vendor's own differentiation): LCA = "multiple environmental indicators such as climate change, ozone depletion, land use and resource depletion or human and ecosystem toxicity"; PCF = "Using the same methodological foundation as an LCA but limited to CO₂e emissions"; PCF scopes cradle-to-gate / cradle-to-grave; PCF standards ISO 14040/14044/14067, GHG Protocol Product Standard, PAS 2050; "Choose PCF to start measuring and managing your product-level CO₂e emissions quickly... Choose LCA to expand beyond carbon... With sustamize's smart data tools, you can easily start with PCF and scale toward full LCA-based sustainability insights."
- Verification: "Unverified Product Carbon Footprints expose companies to reputational, regulatory and financial risk... structured documentation and standards-aligned methodologies provide a strong foundation for third-party verification."
- Internal vs external use: internally hotspot identification, low-carbon design, material substitution, procurement decisions; externally "structured Product Carbon Footprints strengthen carbon reporting and regulatory readiness... meet growing B2B and B2C demand for transparent, verifiable product emissions data".
- Member of Catena-X (automotive data ecosystem).

## Product B — CO2 AI

### Key observations (Evidence layer A — official product pages + FAQ)

- Platform modules: Platform Overview, Corporate Carbon Footprint, **Product Carbon Footprint**, Supplier Engagement Hub, Eco-Design; plus Carbon Data Layer, AI, Professional Services, Dashboards & Reports.
- PCF module positioning: "Scale from dozens to thousands of product footprints"; "Know the Carbon Footprint of Every Product You Make... turning raw inputs into certified, shareable footprints. No manual work. No trust gaps."
- The customer-request loop is explicit: "Respond to customer PCF requests at scale. Whether you receive 10 or 10,000 PCF requests per year, CO2 AI handles it. Automated computation and exchange workflows let you respond faster without adding headcount." "Your customers want proof that your products are getting cleaner. With CO2 AI, you can deliver verified, PACT-compliant PCFs on demand."
- Computation: "Compute audit-ready footprints for thousands of products from scattered data in minutes"; "Automatically match bill of materials data to the most accurate emission factors across global databases"; "Identify emission hotspots at every lifecycle stage — from raw materials to production and transport".
- Eco-design: "Use carbon cockpits to model reduction scenarios based on emission hotspots per lifecycle stage"; "When R&D teams can see the carbon impact of every design choice, sustainability becomes a driver of product innovation".
- Supplier primary data: "Through CO2 AI's Supplier Hub, you can collect verified primary emissions data directly from your suppliers and integrate it into your product footprints — replacing generic emission factors with real data".
- Delivery: "Meet customer demands by delivering PCFs compliant with PACT, TfS, PEF, ISO 14067/14044 and GHG Protocol, through a versatility of formats and API-based integrations"; "Share footprints directly with customers and partners via API-based integrations".
- **Product Ecosystem** (free PCF exchange platform, separate from the paid platform): "connects you, your clients and your suppliers on a shared network so PCF data flows without friction, manual emails, or guesswork". Flow: create account (client or supplier) → connect supply chain (invite suppliers or join a client network) → request or compute PCFs ("Clients send requests. Suppliers calculate with CO2 AI, or enrol in SPARC if it's their first time") → share, track, improve ("Verified data flows back to clients. Both sides can monitor progress over time").
- Supplier-side surfaces: "Manage all incoming requests centrally. No more duplicate emails from multiple clients asking the same questions"; "Calculate & respond with confidence. CO2 AI guides you through the PCF methodology, step by step. No expertise needed"; "Monitor your PCF portfolio over time. Track emissions by product, flag improvements, and benchmark against past periods".
- **SPARC**: free onboarding cohort for Tier-1 suppliers "starting from scratch" — expert guidance, structured methodology, "compute your first verified product carbon footprints".
- Data reliability: "Every PCF calculated through Product Ecosystem follows a methodology aligned with ISO 14067 and the GHG Protocol Product Standard... CO2 AI's calculation engine applies consistent rules across all suppliers, so the data you receive as a client is structured, comparable, and audit-ready."
- Scale claims (vendor): 25k products footprinted for Reckitt; Symrise "measure product-level emissions at scale, from our 10,000 raw materials to our 90 production sites".
- Standards named across pages: PACT, TfS, PEF, ISO 14067/14044, GHG Protocol, CSRD, SBTi, CDP, GRI.

## Product C — Vaayu

### Key observations (Evidence layer A — official site + FAQ)

- Positioning: "the world's first automated AI software empowering retail brands and businesses to track and cut environmental impact in real-time". Retail/e-commerce pole.
- Mechanism: "connect your shop platform and internal systems or use our API. Our proprietary Kria Impact Modeling Engine uses AI, machine learning and certified methodology, automating robust activity-based life cycle assessment data."
- Scope: "Granular footprinting at scale monitors 16 impact categories, including emissions, water and waste... measure Scope 1-3 impact, including complex supply chains, using your real-time dashboard." (Multi-impact — the LCA-drift direction; carbon remains the headline.)
- Data sources: "automates the majority of Scope 3 accounting using activity-based modeling, supplier data, product attributes and operational systems (ERP, PLM, PIM, POS). It captures upstream and downstream impacts across materials, manufacturing, logistics, e-commerce flows and end-of-life."
- Product-level outputs for consumers: "Vaayu powers the granular product-level data required for DPPs [Digital Product Passports], French Environmental Cost labels ('Eco-Scores') and other product/supply chain labels. This includes traceability, material origins, process impacts and multi-impact categories needed for compliance and transparency." Klarna partnership: product impact insights in the consumer shopping flow.
- Circular economy: "quantifies the impacts of resale, rental, repair and recycling programs, including avoided emissions and other environmental benefits, like cost-per-wear."
- Workflow framing: Automate impact calculations → Track your footprint → Cut your climate impact (reduction scenarios/roadmaps) → Communicate your journey.
- Market-structure fact: site banner — "Vaayu is now part of Carbonfact. We're bringing our work together to give fashion brands one platform built for the new wave of product environmental regulation." (Consolidation toward product-environmental-regulation platforms for fashion.)

## Product D — Sphera

### Key observations (Evidence layer A — official product pages)

- LCA-suite vendor (LCA for Experts, formerly GaBi lineage; Managed LCA Content "over 20,000 datasets"). PCF appears as a deliverable produced from LCA machinery, not as a separately named platform.
- **LCA Automation Software**: "the ability to automatically perform life cycle assessments across your full product portfolio with minimal manual input"; "Ability to generate and analyze product environmental footprints"; "LCAs created automatically across large product portfolios"; variants for process / discrete / chemical manufacturing; built on LCA BOM Import for discrete manufacturing; supports Scope 3 initiatives.
- **Supplier PCF Calculator** (inside Supply Chain Risk Management → Supplier Engagement): "designed to assist organizations in accurately managing and reporting Scope 3, Category 1 emissions while empowering suppliers to take ownership of their carbon footprint data."
  - "Standardized Methodology: The calculator employs standardized calculation methods, aligning with Catena-X, PACT, and ISO 14067/14044 standards, ensuring consistency and comparability across different products and suppliers."
  - "Suppliers can input their Bill of Materials (BoM) into the complimentary calculator, enabling them to determine the cradle-to-gate carbon footprint of their products without significant costs or delays."
  - "enables suppliers, regardless of their maturity level, to calculate cradle-to-gate PCFs for the products you've purchased without sacrificing accuracy."
  - Buyer benefit: "procurement teams can integrate sustainability into supplier evaluations and make informed decisions to reduce embodied carbon in the supply chain." Supplier benefit: "Suppliers gain access to detailed carbon data for their products... effectively communicating these improvements to clients."
- Consulting line pairs "Life Cycle Assessment (LCA) and Product Carbon Footprint (PCF)" as one service family; resource library has a "Product Footprint (LCA & PCF)" category beside "Environmental Product Declarations (EPD)".
- The solution tree shows the full neighborhood: LCA for Experts, LCA Automation, LCA Calculator, Managed LCA Content, LCA Database Server, EPD services, corporate carbon footprint services — PCF sits inside an LCA-centered portfolio.

## Product E — Watershed (Product Footprints)

### Key observations (Evidence layer A — official product pages)

- Organizational carbon platform (Measure / Report / Act; 2.3M emission factors — vendor claim) with a dedicated **Product Footprints** solution: "PCFs in moments that reflect your unique supply chain. Respond to every customer PCF request in a fraction of the time, and get the insights needed to build and market lower-carbon products."
- Capability list (vendor): automate PCFs across your portfolio; create PCF reports for customers ("Respond to customer requests in a fraction of the time with AI-powered reports"); edit PCFs across the entire portfolio in moments; model scenario impacts of changes to manufacturing, sourcing, or product design; "View the full supply chain behind each PCF — Every PCF is backed by a production graph that breaks down every input process and material"; compare emissions and cost side-by-side; "Pull PCFs into your corporate footprint — Get credit for product-level progress"; market lower-carbon goods and pinpoint emissions differences.
- Data sources: integrations with food & beverage data providers (HowGood, Quantis, ecoinvent, Agri-footprint logos displayed).
- FAQ topics (questions visible, answers collapsed in fetch): number of PCFs, sustainability intelligence in the AI, confidence levels/uncertainty ranges for AI datapoints, handling vague purchasing data, connection to corporate GHG inventory, supplier-specific data, simulating procurement changes/product redesigns, accuracy vs spend-based estimates. (Questions alone evidence the intended capability surface; answers not verified.)
- Customer testimonials (vendor): Burton — "By running scenarios for lower-carbon materials, we could support overall financial and operational planning"; Charter Next Generation — "respond more quickly and with a higher-value PCF" (supplier responding to customer requests); Specialized — "really fast bulk edits: change these product names to this percent lower emission aluminum"; Thermo Fisher — "cuts through millions of lines of supplier, product and material data".
- The corporate↔product relationship is explicit: product footprints feed the corporate footprint ("get credit for product-level progress") — the org-suite pole.

## Standards context — PACT (WBCSD Partnership for Carbon Transparency)

### Key observations (Evidence layer A — official methodology site)

- PACT Methodology V3: "Methodology for Calculating and Exchanging Cradle-to-Gate Product Carbon Footprints (PCFs)" — "builds on existing frameworks and standards to provide guidance on accounting, verification, and exchange of cradle-to-gate PCFs with the aim of creating more accurate, granular, and comparable emissions data."
- Problem framing: "Inconsistent & non-accessible PCF calculation in supply chains" — different guidelines and standards, different technical solutions, poor data quality (lack of granular, accurate, verified primary data). Buyer requests granular product emission data (per GHG Protocol or ISO 14067); supplier may have no PCF yet or only corporate-level granularity.
- Solution framing: "PACT helps to calculate, standardize and exchange Product Carbon Footprint across frameworks, tools and stakeholders." Data qualities: **Accurate** (supplier-specific verified data), **Granular** ("Linked to individual products rather than aggregated corporate data"), **Comparable** ("Based on one standardized approach for calculation and exchange").
- Exchange machinery: PACT Network (technical infrastructure enabling automated data exchange across solutions), PACT Conformance for solution providers, OpenAPI Schema, data model extensions (RMI steel/aluminum, iLEAP logistics), "PCFs are exchanged alongside a set of data reliability KPIs that provide insights into the data quality and share of primary data".
- Industry framework alignment: PEF/OEF, ISO, Together for Sustainability (TfS), Catena-X, RMI; sector rulebooks — Catena-X Product Carbon Footprint Rulebook (automotive), TfS PCF Guideline for the chemical industry, Global Battery Alliance GHG Rulebook, metals guidance (IAI aluminium, RMI steel/aluminium, nickel, zinc, cobalt), GFLI (animal feed), GLEC (logistics), FEFCO (paper packaging).
- Member quotes evidence the buyer-side pull: Schneider Electric ("Exchange of product environmental data with suppliers is critical to decarbonizing supply-chains"), BASF ("manufacturers will need to embrace the principle to share their product carbon footprint data with their partners along the value chain"), Unilever, Dow, P&G.

## Cross-product Comparison

| Aspect | Sustamize | CO2 AI | Vaayu | Sphera | Watershed |
|---|---|---|---|---|---|
| Form | pure-play PCF data + calculation platform (Sustamizer) + API | enterprise suite module + free exchange network | retail automation SaaS | LCA-suite products (LCA Automation, Supplier PCF Calculator) | module inside org carbon platform |
| Unit of record | products/materials mapped to CO₂e reference data | products/SKUs at portfolio scale | retail products/transactions in real time | products via BOM import / automation | products with production graphs |
| Computation | BOM → AI matching to CO₂e database → kg CO₂e (ISO 14067) | BOM + activity data → AI factor matching → audit-ready PCF | commerce/ERP/PLM/PIM/POS feeds → Kria engine → activity-based LCA data | BOM import → automated LCA generation → PCF among outputs | purchasing/supply-chain data → AI → PCF with production graph |
| Boundary | cradle-to-gate or cradle-to-grave, user-declared | lifecycle stages materials→production→transport (cradle-to-gate posture) | upstream + downstream incl. end-of-life | cradle-to-gate (supplier calculator); full LCA elsewhere | production graph per PCF (boundary configurable) |
| Data foundation | own CO₂e database (bottom-up modeled, biannually updated) | global factor databases + AI matching | certified methodology + AI/ML | Managed LCA Content (20k+ datasets) | ecoinvent, HowGood, Quantis, Agri-footprint integrations |
| Delivery surfaces | Scope 3 reporting, ERP/PLM/costing integration, API, reports | customer PCF responses, API exchange, Product Ecosystem network | consumer labels (Eco-Score), DPP, dashboards | supplier→client sharing, Scope 3 Cat 1 reporting | PCF reports for customers, corporate-footprint pull-in, marketing |
| Request/response loop | supplier data workflows (non-EU supplier page) | explicit (Product Ecosystem: request → compute → share → track) | not the framing (consumer-facing) | explicit (Supplier PCF Calculator: buyer provides, supplier computes, shares back) | explicit ("respond to every customer PCF request") |
| Standards named | ISO 14067, GHG Protocol, PAS 2050, ISO 14040/44 | PACT, TfS, PEF, ISO 14067/14044, GHG Protocol | certified methodology (unnamed on fetched pages) | Catena-X, PACT, ISO 14067/14044 | (FAQ collapsed; not verified) |
| Eco-design/scenarios | scenario calculations via consultants; product-design use case | carbon cockpits, reduction scenarios | reduction scenarios/roadmaps | LCA-level modeling depth | scenario impacts of sourcing/design changes |
| Multi-impact | no (PCF-only; "scale toward full LCA" as roadmap) | corporate + product carbon (PEF named) | 16 impact categories | full LCA multi-impact | carbon headline; platform measures water/land |
| Scale posture | portfolio-level recalculation | thousands of SKUs in parallel | real-time, full assortment | full product portfolios automatically | portfolio bulk edits |

### Cross-product commonalities (Evidence layer B)

1. **The product as the managed unit** — every product maintains footprints bound to identified products/SKUs/materials, at portfolio scale (Sustamize portfolio recalculation; CO2 AI "thousands of products"; Vaayu "entire assortment"; Sphera "full product portfolio"; Watershed "across your portfolio").
2. **The computed per-product carbon figure in kg CO₂e** — universal deliverable; computed from product data (BOM/materials, production, logistics, use, end-of-life as applicable) × emission factors, greenhouse gases aggregated to CO₂e via GWP.
3. **A declared life-cycle boundary** — cradle-to-gate is the dominant posture (Sustamize explicit choice; Sphera supplier calculator cradle-to-gate; PACT methodology cradle-to-gate); cradle-to-grave as the extended option (Sustamize, Vaayu).
4. **Emission-factor / LCA data foundation** — every product connects computation to a managed factor or LCA dataset source (own database, licensed content, or integrations). LCA machinery is the substrate, exactly as the LCA pass predicted.
5. **Standards conformance as a first-class property** — ISO 14067 and GHG Protocol Product Standard named across the sample; PACT/PACT-conformance, TfS, Catena-X, PEF, PAS 2050 as the conformance vocabulary. Conformance is a selling point and a data property, not an afterthought.
6. **The deliverable/exchange orientation** — every product produces figures for parties other than the calculator: customer PCF responses (CO2 AI, Watershed, Sphera supplier calculator), Scope 3 reporting inputs (Sustamize, Sphera), consumer labels/passports (Vaayu), corporate-footprint pull-in (Watershed), API exchange (Sustamize, CO2 AI).
7. **Traceability/audit-readiness** — every product claims traceable, audit-ready calculations with documented methodology (verification support is a stated concern in four of five).
8. **Hotspot analysis per lifecycle stage** — universal analysis surface (materials/production/transport breakdowns).
9. **Supplier primary data as the accuracy upgrade path** — replacing generic factors with supplier-specific data is a named mechanism in four of five (Sustamize supplier inputs; CO2 AI Supplier Hub; Sphera Supplier PCF Calculator; Watershed supplier-specific data FAQ).
10. **Scenario/what-if for reduction and eco-design** — present in all five in some form (carbon cockpits, material-swap scenarios, reduction roadmaps).

### Divergences (implementation, not Type)

- Data-foundation posture: proprietary factor database (Sustamize) vs licensed LCA content (Sphera) vs integrations with multiple providers (Watershed) vs AI-matched global databases (CO2 AI).
- Direction of the exchange: buyer-side collection (Sphera Supplier PCF Calculator is bought by the buyer for its suppliers; CO2 AI Product Ecosystem serves both sides) vs supplier-side response tooling (CO2 AI supplier surfaces, Charter Next Generation testimonial) vs consumer-facing output (Vaayu).
- Multi-impact breadth: carbon-only (Sustamize) vs carbon + corporate (CO2 AI, Watershed) vs 16 categories (Vaayu) vs full LCA (Sphera) — a breadth gradient, not a boundary.
- Real-time vs campaign posture: continuous commerce-driven computation (Vaayu) vs periodic portfolio recomputation (Sustamize biannual data updates; annual reporting cycles).
- Suite embedding: standalone pure-play vs module of an org carbon platform vs product line of an LCA suite.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Product Carbon Footprint Platform is recognizable by exactly three jointly-held structures:

1. **The product as the unit of account** — a persistent, identified record per product (SKU/item/material/variant) forming a managed population; the footprint attaches to the product, not to the organization or the facility. Remove → organizational carbon accounting (unit = company + scopes) or a one-off calculator.
2. **The computed, maintained per-product carbon figure** — a quantified greenhouse-gas footprint per product unit (kg CO₂e per unit), computed from product data (materials/BOM, production, logistics, use and end-of-life as applicable) against emission factors over a declared life-cycle boundary, held as a re-computable record with traceable inputs (not a one-off estimate). Remove → a product data catalog (PLM) or a static consulting report.
3. **The deliverable orientation** — the figure is produced as a communicable, standards-aligned artifact for parties other than the calculating team: responses to customer PCF requests, reports, structured data exchange to buyers, consumer-facing labels/passports, or inputs to corporate inventories. Remove → internal analytics or a private modeling environment (LCA territory).

Jointly-held load-bearing checks:
- 1 without 2+3 = product master data with carbon labels of unknown provenance.
- 2 without 1 = unanchored carbon arithmetic (calculator).
- 2+3 without 1 = one-off PCF studies (consulting deliverable), not a platform.
- 1+2 without 3 = internal footprint analytics; the "platform" exchange character dies and the object drifts to LCA/modeling territory.
- 1+3 without 2 = a request/response mailbox with no computation.

Not in L0 (checked against the historical/market-sample rule): the buyer→supplier request/response loop (dominant modern driver but the deliverable can be proactive — labels, reports), cradle-to-gate specifically (cradle-to-grave and partial boundaries are legitimate), any specific standard (ISO 14067 / GHG Protocol Product Standard / PAS 2050 / PACT are the current conformance vocabulary, not the definition), AI matching, exchange networks, consumer labels, corporate-footprint integration, multi-impact breadth, real-time computation, cloud delivery. A spreadsheet-era PCF (product list + factor-based calculation + report sent to the requesting customer, as practiced under PAS 2050 since 2008) satisfies all three legs with none of the modern machinery.

### L1 — Common Mature Structure

- Emission-factor / LCA data foundation: managed factor databases (proprietary or licensed LCA content) and/or integrations with data providers; factor provenance and update cadence treated as data quality.
- Product-data ingestion and factor matching: BOM import (CSV/Excel/API/ERP-PLM-PIM-POS feeds), AI-assisted matching of materials/parts to factors, manufacturer-part-number lookup.
- Boundary configuration: cradle-to-gate default posture with cradle-to-grave extension; declared boundaries recorded with the figure for comparability.
- Standards conformance layer: ISO 14067 / GHG Protocol Product Standard calculation alignment; PACT-conformant data exchange; sector rulebooks (Catena-X automotive, TfS chemicals, battery/metals/packaging guidance); conformance signaling on outputs.
- Hotspot / contribution analysis: emissions broken down by lifecycle stage, material, and process; per-product and portfolio views.
- Scenario modeling: material substitution, supplier changes, design alternatives; eco-design decision support.
- Supplier primary-data machinery: supplier data requests, supplier-side calculation tools, integration of supplier PCFs into the buyer's figures (replacing generic factors).
- Audit trail and verification support: traceable path from figure to inputs, factors, and method; documentation structured for third-party verification.
- Portfolio-scale operation: bulk computation and bulk edits across thousands of SKUs; portfolio-level recalculation when factors or supply chains change.
- Delivery surfaces: PCF reports/documents for customers, structured data exchange (API, PACT-format), Scope 3 category-1 reporting inputs, corporate-footprint pull-in.

### L2 — Variant / Optional Structure

- Sector packaging: automotive (Catena-X rulebook), chemicals (TfS), food & beverage (specialized data providers), fashion/retail (labels, DPPs), batteries (Global Battery Alliance), metals (IAI/RMI guidance), packaging.
- Consumer-facing surfaces: eco-labels/scores (e.g., French Eco-Score), Digital Product Passports, e-commerce product-page impact display.
- Regulatory outputs: CBAM embedded-emissions data, CSRD product-level inputs, EU product regulation (battery regulation, ESPR/DPP direction), green-claims substantiation.
- Multi-impact extension: water, waste, and broader impact categories beside carbon (the drift direction toward LCA/EPD territory).
- Corporate integration depth: product footprints feeding the organizational inventory (Scope 3 Cat 1) vs standalone product work.
- Side-of-the-supply-chain posture: buyer-side collection/aggregation vs supplier-side computation/response vs two-sided exchange networks.
- Delivery posture: self-serve SaaS vs managed service with expert/consulting layers.
- Real-time vs periodic recomputation cadence.
- EPD generation as an adjacent output (multi-impact declared documents under program operators).

### L3 — Vendor-specific (research notes only)

- Sustamize: Sustamizer platform name; Matcher/Assembler/Interpreter/MPN Search tool names; biannual database updates; "7M+ verified emission factors" claim; Catena-X membership; German-market manufacturing/cost-engineering angle.
- CO2 AI: Product Ecosystem free exchange network; SPARC supplier accelerator program; MAC-curve abatement prioritization; "25k products for Reckitt" and "10,000 raw materials / 90 production sites" (Symrise) claims; analyst-recognition badges.
- Vaayu: Kria Impact Modeling Engine; 16 impact categories; cost-per-wear circularity metric; Klarna consumer integration; acquisition by Carbonfact (fashion-focused product-environmental-regulation platform).
- Sphera: Managed LCA Content (20k+ datasets); LCA Automation product line (process/discrete/chemical variants); Supplier PCF Calculator as a complimentary buyer-procured tool; GaBi lineage.
- Watershed: production-graph ("digital twin") per PCF; AI agents; "2.3M emission factors" claim; HowGood/Quantis/ecoinvent/Agri-footprint integrations; Burton/Specialized/Charter Next Generation/Thermo Fisher testimonials.

## Vendor-specific Findings

See L3. All numeric claims (factor counts, speed multipliers, product counts, savings figures) are vendor marketing and are excluded from the canonical document.

## Boundary Findings

- **vs Life Cycle Assessment Application** (the closest seam; joint review discharged from this side): the LCA pass defined the seam as deliverable-first vs model-first, and this pass's evidence **ratifies keep-both**. The PCF platform's object of work is the maintained per-product carbon figure and its delivery; the LCA application's object of work is the editable product-system model and its multi-impact assessment. LCA machinery (process networks, factors, boundaries) is the PCF platform's computation substrate — visible at Sphera (PCF produced by LCA Automation from the same Managed LCA Content) and acknowledged by Sustamize's own LCA-vs-PCF page ("same methodological foundation... limited to CO₂e"; "start with PCF and scale toward full LCA"). Test: remove the carbon-figure deliverable orientation and center the editable multi-impact model → LCA Application; strip the model-building depth and center the maintained, exchanged figure → PCF Platform. Vendors legitimately sell both from one engine (Sphera; Ecochain per the LCA pass) — packaging overlap, not Type collapse.
- **vs Carbon Accounting Platform**: unit of analysis. Carbon accounting centers the organization (boundary + scopes + activity data + inventory per reporting period); the PCF platform centers the product (identified product + declared boundary + per-unit figure). The two interlock: product footprints aggregate up into Scope 3 category 1 (Sphera's Supplier PCF Calculator is explicitly "Scope 3, Category 1" machinery; Watershed pulls PCFs into the corporate footprint "to get credit for product-level progress"), and carbon platforms extend down into product modules (Watershed, CO2 AI). Test: remove the product unit and keep the org/scope inventory → Carbon Accounting Platform; remove the org inventory and keep per-product figures → PCF Platform. Confirms the carbon-accounting pass's recorded seam from this side.
- **vs Scope 3 Management Platform**: Scope 3 management estimates supply-chain emissions at organizational grain (spend-/activity-based categories); the PCF platform produces product-grain figures that are the granular end of the same demand. A PCF platform can feed Scope 3 Cat 1, but its unit of record is the product, not the scope category.
- **vs Supplier Sustainability Management**: supplier sustainability platforms collect broad supplier ESG data (questionnaires, audits, ratings, targets); the PCF platform's supplier machinery is specifically the product-carbon data exchange. Supplier PCF collection is one use case inside the broader supplier-sustainability Type.
- **vs Sustainable Product Management / eco-design tools**: eco-design centers design decisions and workflows; the PCF platform centers the computed figure and its delivery. Scenario modeling for design is a common capability of the PCF platform, not its center.
- **vs EPD machinery / LCA program operators**: an EPD is a multi-impact declared document under a program operator (EN 15804-class); the PCF is the single-impact carbon figure. PCF platforms may feed EPD processes (Sphera's portfolio spans both), but the deliverables differ.
- **"去掉什么就变成另一个 Type" 判据**: remove the product unit of account → Carbon Accounting Platform; remove the carbon-only deliverable focus and center the multi-impact model → LCA Application; remove the maintained/reproducible calculation → one-off consulting study; remove the deliverable/exchange orientation → internal analytics or modeling environment; remove factors and computation → PLM/product catalog.

## Uncertainties

- No gated help-center or in-app documentation was reachable for any sampled product; all evidence is official product/solution pages and on-site FAQs. Operational details (exact data schemas, exchange-format implementations, workflow states, pricing) are not asserted anywhere in the canonical document.
- Watershed's FAQ answers were collapsed in the fetch; its capability surface is evidenced by the feature list and customer testimonials, not by FAQ answers. The corporate-footprint pull-in and supplier-data incorporation are evidenced by the page's own capability list.
- Vaayu's "real-time" computation is vendor positioning; the operational meaning (what triggers recomputation, latency) was not verifiable. Vaayu's acquisition by Carbonfact postdates most of its public documentation; the combined product's shape is unknown.
- CO2 AI's Product Ecosystem workflow states (request → compute → share → track) are observed at marketing level; the exact request/response data model was not verifiable.
- The exact set of sector rulebooks a given product implements (Catena-X, TfS, battery, metals) varies and was only spot-checked; no claim made about completeness.
- Historical depth: the PAS 2050 (2008) / GHG Protocol Product Standard (2011) / ISO 14067 (2013) era establishes that product carbon footprinting predates the platform generation; the spreadsheet-era realization is inferred from the standards' own practice (factor tables + product data + report), not from a sampled historical product. Confidence: moderate-high for the conceptual claim, low for tooling specifics of that era.

## Final Synthesis

The Product Carbon Footprint Platform is the product-grain carbon accounting system of the supply chain. Its world has three load-bearing structures held jointly: the product population as the unit of record (identified products/SKUs/materials), the computed and maintained per-product carbon figure (product data × emission factors over a declared life-cycle boundary, in kg CO₂e, traceable and re-computable), and the deliverable orientation (the figure produced as a standards-aligned artifact for customers, buyers, regulators, labels, or the corporate inventory). Around this core, mature products add factor/LCA data foundations, BOM ingestion with AI factor matching, standards conformance layers (ISO 14067, GHG Protocol Product Standard, PACT, sector rulebooks), hotspot analysis, eco-design scenarios, supplier primary-data machinery, audit trails, portfolio-scale operation, and multiple delivery surfaces. The market's defining interaction is the buyer↔supplier PCF loop: buyers request granular product emissions; suppliers compute and share standardized, quality-annotated figures — a loop now formalized by the PACT methodology and sector rulebooks. Products differ legitimately in data-foundation posture, side of the supply chain served, sector packaging, multi-impact breadth, and real-time vs periodic cadence — variants, not the Type. The nearest boundaries are the LCA Application (deliverable-first vs model-first; LCA machinery is the substrate) and the Carbon Accounting Platform (product vs organization as unit of analysis; the two interlock through Scope 3 category 1).
