# Research Notes — Scope 3 Management Platform

Research date: 2026-09-09
Leaf: Scope 3 Management Platform (DIRECTORY.md §21 Environment, Sustainability & Climate)
Slug: scope-3-management-platform

---

## Research Goal

Understand what the market actually sells under the "Scope 3 management" label: what the system of record is, who works in it, what the counterpart (supplier) side looks like, what the recurring workflow is, and where the boundary sits against the already-processed sibling Types — carbon-accounting-platform, greenhouse-gas-accounting (alias), esg-reporting-platform, product-carbon-footprint-platform, life-cycle-assessment-application, decarbonization-planning-platform, energy-carbon-management — and against the unprocessed siblings supplier-sustainability-management and sustainable-procurement-platform.

## Initial Boundary (hypothesis before research)

Working hypothesis: a Scope 3 Management Platform is the buyer-organization-side system for the value-chain slice of its carbon program — measuring value-chain (Scope 3) emissions, collecting primary data from suppliers, and driving/tracking reduction engagement. Nearest neighbors:

- carbon-accounting-platform (processed): whole-of-org inventory of record; its pass explicitly recorded "supplier engagement" as a standard capability, NOT definitional — so this leaf must carry weight beyond that.
- supplier-sustainability-management (unprocessed): supplier ESG performance/compliance broadly, not specifically the emissions account.
- decarbonization-planning-platform (processed): forward program of reduction levers; overlap risk on "reduction tracking".
- product-carbon-footprint-platform (processed): product-grain figures and their delivery; overlap risk on PCF collection from suppliers.

Key unknowns going in: (1) is this a distinct Type or just the supplier-engagement module of carbon accounting? (2) is the center upstream suppliers only, or the full upstream+downstream Scope 3 span? (3) does the "estimate → primary data" progression constitute a defining structure?

## Research Questions

1. What is the unit of record — the org's Scope 3 account? categories? suppliers? both?
2. How do products organize value-chain emissions (category schemes, calculation methods)?
3. What exactly does the platform manage about suppliers (records, states, data quality, maturity)?
4. What does the supplier-facing surface look like (portal, survey, network, PCF module)?
5. What is the recurring workflow (campaign → response → validation → recalculation → engagement)?
6. How do products treat the estimate→primary-data progression?
7. How is reduction engagement tracked (commitments, joint plans, maturity)?
8. Where do disclosure outputs (CSRD/CDP/SBTi/ISSB) sit — core or capability?
9. Do products cover downstream Scope 3 (use-phase, end-of-life) or center upstream?
10. Where is the seam vs carbon accounting, supplier sustainability, decarbonization planning, PCF?

## Representative Products

Selected for market representation + documentation reachability + different product philosophies + different customer tiers:

1. **Sweep** (sweep.net) — enterprise value-chain carbon/ESG suite (L'Oréal, Casino, SSE, Swisscom class); "Supplier Emissions" as a first-class solution beside Carbon Management / Reporting / Decarbonization Strategy. French/European enterprise pole.
2. **Normative** (normative.io) — carbon-accounting-first product with a dedicated Supply Chain Engagement module (Carbon Network, EcoVadis integration, human enrichment services); mid-market/enterprise, advisory-coupled philosophy.
3. **Cozero** (cozero.io) — "carbon controlling" platform (Log/Act/Share) with a Scope 3 / supplier-engagement use case built on a PCF data-sharing module; German mid-market/industrial pole (logistics, manufacturing).
4. **ClimateCamp** (climatecamp.io) — Scope 3-first product: "Create business value from Scope 3 data"; supplier network + engagement + Scope 3 reduction simulation; Belgian SMB/mid-market pole (food & beverage, packaging, manufacturing).
5. **Watershed** (watershed.com) — US enterprise "sustainability AI platform" (Measure/Report/Act) with "Watershed Supply Chain" as a distinct solution; Fortune-500 pole (Klarna, Walmart, FedEx class); measurement-first philosophy.

This spans: standalone Scope-3-first products (ClimateCamp), carbon suites with a value-chain solution (Sweep, Watershed), accounting-first with engagement module (Normative), controlling-first with PCF exchange (Cozero); EU + US; enterprise + mid-market.

## Sources

All fetched 2026-09-09 (Tier 2 official product/solution pages; no help centers reached — see Sourcing Limitations):

- Sweep — https://www.sweep.net/ , https://www.sweep.net/supply-chain-emissions (https://www.sweep.net/product → 404, abandoned)
- Normative — https://normative.io/ , https://normative.io/platform/supply-chain-engagement/
- Cozero — https://www.cozero.io/ , https://www.cozero.io/supply-chain
- ClimateCamp — https://climatecamp.io/
- Watershed — https://www.watershed.com/ , https://www.watershed.com/solutions/supply-chain (https://www.watershed.com/product/supplier-engagement → 404, abandoned)

Sibling context (processed leaves, STATUS.md): carbon-accounting-platform (2026-09-07), greenhouse-gas-accounting (2026-09-08, alias), esg-reporting-platform (2026-09-08), energy-carbon-management (2026-09-08), decarbonization-planning-platform (2026-09-07), product-carbon-footprint-platform (2026-09-09), life-cycle-assessment-application (2026-09-08).

## Product Observations

### Sweep (evidence layer A unless noted)

- Root positioning: "Software helping companies track and act on their ESG and carbon emissions." Solutions: Carbon management / **Supplier Emissions** / Sustainability Reporting / Decarbonization Strategy. Platform framed as Track / Disclose / Act (per its IDC citation).
- Supplier Emissions page headline: "Measure, manage, and reduce the supply chain emissions that make up the bulk of your Scope 3 footprint."
- **Collect at scale**: "Several flexible collection methods, from sectoral estimates, to surveys, and supplier portals so you cover your full supply base from day one." Explicit program statement: "Hit 100% supply chain coverage from day one, then replace estimates with primary data as you go." Mechanisms: sectoral estimates → verified declared data → supplier portals; direct connectors to procurement systems and ERPs (plus API and invoice imports) for purchase data; pre-built campaigns by Scope 1/2, Scope 1/2/3, or fully custom surveys; imports from CDP Supply Chain, EcoVadis, S&P, SBTi "out of the box".
- **Engage**: "Free supplier accounts for every surveyed supplier, with their own footprint dashboard"; Sweep School (multilingual e-learning on GHG accounting and data collection); automated reminders; validator/approval workflows; full audit trails; SBTi commitments auto-imported via LEI/ISIN/SBTi identifier.
- **Act on hotspots**: "Fix the 20% of suppliers driving 80% of emissions, and model trade-offs before you change sourcing." Carbon intensity benchmarked across 200+ industry sectors and peer data; supplier scorecards comparing emissions, data quality, and climate commitments; procurement simulations to model carbon and cost trade-offs before sourcing decisions; **engagements module to track joint reduction commitments supplier by supplier**.
- FAQ (methodology): GHG Protocol's four methodologies — spend-based, average-data, hybrid, supplier-specific — "all supported within a single platform, enabling organisations to start with spend-based estimates on day one and replace them with primary supplier data over time." Supplier emissions located in Scope 3 Category 1 (purchased goods and services) and Category 4 (upstream transportation and distribution).
- Framework alignment claimed: CSRD, California SB 253, GHG Protocol Scope 3 category reporting, ISSB/IFRS S2, SBTi. Verdantix strength areas quoted: "Value chain emissions management", carbon data management, carbon financial management.

### Normative (evidence layer A)

- Root positioning: "Carbon Accounting Software — Audit-Ready Scope 1, 2 & 3 Data"; 349,000 verified emission factors; named GHG-Protocol-certified Climate Strategy Advisor per account; TÜV SÜD-verified calculation engine; traceability "from source data to output".
- Supply Chain Engagement page: "Collect and analyze supplier emissions data at scale. Deliver actionable reduction strategies. Make real cuts to scope 3 emissions with Normative." Frames the problem: value chain emissions "often account for 90% of a business' emissions"; challenges = engaging many suppliers, synthesizing different types of supplier reporting, incorporating supplier data into the carbon footprint.
- Feature set (as listed): **Direct Engagement** (invite suppliers to submit data via structured surveys, "ideal for reduction planning and collaboration"); **Normative Carbon Network** (browse and reuse data shared by suppliers or curated by Normative — "searchable, scalable, and continuously growing"); **EcoVadis Integration** (verified intensity data from rated suppliers into Scope 3 calculations); **Customer Upload** (bring in data you already have); **Supplier Data Enrichment Services** (GHGP-certified Climate Strategists research and deliver emissions data for your most important suppliers); **Connected Calculations** (connect primary supplier data to the holistic calculations to "refine, improve, and better understand your overall carbon footprint. Pinpoint targeted opportunities for emissions reduction and verify the impact of those initiatives over time").
- Customer quote (Restaurant Group): "pinpoint high-emitting products and suppliers, helping the wider business to make strategic decisions to decarbonise."

### Cozero (evidence layer A)

- Root positioning: "Carbon Controlling Software for Finance and Sustainability Leaders"; modules Log (emissions calculations/analysis), Act (decarbonization planning), Share (reporting/disclosure); feature: Supplier engagement; use case: "Scope 3 — Account for Scope 3 emissions and engage your suppliers."
- Scope 3 page: "Take control of your Scope 3 carbon exposure." Claims Scope 3 "up to 90% of an enterprise's total carbon footprint"; "Survey-based supplier portals consistently fail because suppliers don't engage with them. Cozero takes a different approach: structured supplier data sharing through the Cozero platform, combined with customer success engineering."
- Supplier data sharing flow (as listed): Request primary data → Automate emission calculation → Use supplier-specific emission factors → Invite suppliers to the platform. "Your suppliers access the Cozero PCF module directly to share their product carbon footprints with you." "Replaces static spreadsheets and one-off email requests with a workflow that produces auditable data." "Supports PCF, service carbon footprints, and iLEAP / PACT-aligned data exchange."
- Methodology: "GHG Protocol-aligned methodology applied consistently across all suppliers. Aggregated Scope 3 data structured for comparability, not a patchwork of different methodologies. Product-level accounting enables PCF calculations and direct Scope 3 data exchange with your customers."
- **Customer success engineering** (human service layer): "Supplier engagement is a hard problem nobody has fully solved with software alone… design a supplier data program calibrated to your supply chain reality: which suppliers to engage first, what data to ask for, how to sequence rollout, how to handle the long tail."
- From data to action: "Map your supply chain structure and surface the suppliers that drive the majority of your Scope 3 exposure. Compare supplier carbon intensity, track improvement over time, and prioritize engagement where the reduction potential and the regulatory risk is highest. Build joint decarbonization programs with the suppliers that matter most."
- FAQ: template data collection forms for consistency with per-supplier flexibility; ERP/procurement integration; ~40,000 emission factors; activities associated with GHG Protocol emission categories.

### ClimateCamp (evidence layer A)

- Root positioning: "Create business value from Scope 3 data. Improve emissions data quality to validate and incentivize value chain reduction initiatives."
- Platform features: **Supplier engagement** ("Collect and validate supplier primary data"); **Corporate Carbon Footprint** ("Generate audit-ready corporate carbon footprints"); **Product Carbon Footprint** ("Calculate product carbon footprints at scale"); **Scope 3 decarbonization** ("Simulate the impact of Scope 3 reduction initiatives").
- Engage-side features: agentic retrieval of public carbon data (agents scan sustainability reports, SBTi commitments, CDP filings, EcoVadis scores to pre-populate supplier profiles before outreach); automated supplier outreach (AI sends, follows up, schedules data-validation meetings); 35,000+ pre-built supplier profiles; **primary data validation team** (structured onboarding calls with key suppliers to verify, document, quality-check data "before it enters your footprint"); **autofill customer data requests** (a listed company answers its own customers' carbon data requests from its inventory).
- Reduce-side features: Scope 3 reduction simulation (model sourcing/design/logistics choices before committing); custom reduction lever tracking (supplier-specific inputs — recycled content, renewable energy share, transport mode — modeled against the buyer's Scope 3); **supplier carbon maturity tracking** ("Monitor how suppliers' carbon capabilities improve over time — from first disclosure to science-based targets — and use progress to inform procurement").
- CCF calculation: "Initially we perform a spend-based allocation, but where weight or distance data exists, we apply more precise activity-based emissions factors"; audit-ready inventory with traceable emission factors.
- Data sharing: auto-generated sustainability profile with per-datapoint sharing control; PACT-compliant PCF exchange; CDP/SBTi/EcoVadis alignment; open API; Excel/CSV export. "Explore ClimateCamp — Discover all companies listed on ClimateCamp" (network).
- FAQ (SBTi regime packaging): "If over 40% of your footprint is in Scope 3, you'll need to set a supplier engagement target… asking your suppliers responsible for 67% of your Scope 3 emissions to commit to setting their own science-based targets."
- Customer quotes: "tracking scope 3 with emissions data directly from our suppliers is the biggest challenge" (Haacht); "suppliers don't always have the necessary data, documentation or knowledge… ClimateCamp proved to be a great partner to guide suppliers and collect this primary data" (Duvel Moortgat).

### Watershed (evidence layer A)

- Root positioning: "The sustainability AI platform"; Measure / Report / Act; 2.3M emission factors; 4.1 Gt CO₂e estimated under management.
- Supply Chain solution page: "Take control of scope 3. Your supply chain likely accounts for 80% or more of your total emissions. Watershed gives you one platform to map suppliers, prioritize by impact, and drive reductions—**replacing estimates with supplier-specific data**."
- "Know exactly where to focus": "Watershed ranks suppliers by emissions impact and climate maturity so you can direct resources where they'll drive the greatest reductions. Build custom cohorts, manage performance, and save time."
- "Engage suppliers and prove progress": "Send data requests, target commitments, and reduction plans to any supplier through a guided portal with built-in climate education. Responses flow directly into your footprint—replacing industry averages with primary data—**so every engagement improves your measurement**."
- FAQ: "unifies the full Scope 3 journey—from granular, audit-ready measurement to supplier intelligence and engagement—so teams can move beyond surveys and averages to measurable reductions… rigorous calculation engine and transparent data lineage… tens of thousands of supplier disclosures, auto-mapped and enriched to prioritize action. Built-in workflows, supplier portals, and scorecards drive scaled engagement, while AI-powered Product Footprints connect real procurement choices to emissions outcomes."
- Klarna quote: "prioritize climate action in our supply chain, enabling us to focus on our most material suppliers."

## Cross-product Comparison

| Dimension | Sweep | Normative | Cozero | ClimateCamp | Watershed | Reading |
|---|---|---|---|---|---|---|
| Value-chain (Scope 3) emissions account, by category, period-over-period | ✔ (GHG Protocol Scope 3 category reporting) | ✔ (Scope 3 calculations, traceable) | ✔ (GHG Protocol emission categories in Log) | ✔ (CCF + Scope 3 categories) | ✔ ("full Scope 3 journey", audit-ready) | **All 5 — core** |
| Multiple calculation methods, estimates first-class | ✔ (spend/average/hybrid/supplier-specific named) | ✔ (factors + supplier data + enrichment) | ✔ (spend→supplier-specific factors) | ✔ (spend→activity allocation) | ✔ (estimates → supplier-specific) | **All 5 — core** |
| Suppliers as managed records (profiles, status, intensity, maturity) | ✔ (scorecards: emissions, data quality, commitments) | ✔ (supplier data per supplier; enrichment per supplier) | ✔ (supplier carbon intensity comparison) | ✔ (35k profiles; maturity tracking) | ✔ (rank by impact + climate maturity; cohorts) | **All 5 — core** |
| Counterpart-facing surface owned by the platform | ✔ (free supplier accounts w/ own footprint dashboard) | ✔ (surveys + Carbon Network) | ✔ (suppliers access PCF module directly) | ✔ (network profile; autofill customer requests) | ✔ (guided portal w/ climate education) | **All 5 — core; form varies** |
| Data request → response → validation machinery | ✔ (campaigns, reminders, validator/approval workflows, audit trails) | ✔ (structured surveys; enrichment services) | ✔ (request primary data; auditable workflow; template forms) | ✔ (outreach, validation team, quality-check before entry) | ✔ (data requests; responses flow into footprint) | **All 5 — core; depth varies** |
| Estimate→primary progression as explicit program | ✔ ("replace estimates with primary data as you go") | ✔ ("refine, improve" the footprint) | ✔ ("estimates… no longer sufficient"; primary data at scale) | ✔ ("improve emissions data quality") | ✔ ("every engagement improves your measurement") | **All 5 — core** |
| Hotspot / prioritization across categories & suppliers | ✔ (hotspots; 20/80 framing) | ✔ (pinpoint high-emitting suppliers) | ✔ (surface suppliers driving majority of exposure) | ✔ (simulation + prioritization) | ✔ (rank by impact; most material suppliers) | **All 5 — core** |
| Engagement/reduction tracking per counterpart | ✔ (engagements module; joint reduction commitments) | ✔ (verify impact of initiatives over time) | ✔ (joint decarbonization programs; track improvement over time) | ✔ (maturity tracking; lever tracking; simulation) | ✔ (target commitments; reduction plans; prove progress) | **All 5 — core** |
| Audit trail / data lineage / traceability | ✔ (full audit trails) | ✔ (traceable source→output; TÜV verification) | ✔ (auditable data; consistent methodology) | ✔ (traceable emission factors) | ✔ (transparent data lineage) | **All 5 — core** |
| Framework/disclosure outputs (CSRD/CDP/SBTi/ISSB…) | ✔ | ✔ | ✔ (Share module) | ✔ (CDP/SBTi/EcoVadis alignment) | ✔ | Common capability, not the center |
| Procurement/ERP integration for spend & purchase data | ✔ (connectors, invoice imports, procurement simulations) | — (not observed on fetched pages) | ✔ (ERP/procurement integration) | ✔ (procurement-informed maturity use) | ✔ (procurement choices ↔ emissions) | Common |
| Supplier education/training | ✔ (Sweep School) | — | ✔ (supplier onboarding materials) | ✔ (built-in education via outreach; Carbon Academy) | ✔ (portal with built-in climate education) | Common |
| Supplier network / third-party data reuse | ✔ (imports: CDP Supply Chain, EcoVadis, S&P, SBTi) | ✔ (Carbon Network; EcoVadis integration) | — (PACT/iLEAP exchange) | ✔ (35k pre-built profiles; Explore network) | ✔ (tens of thousands of supplier disclosures) | Common variant |
| PCF / product-level data exchange | — (not on fetched pages) | ✔ (PCF tool as separate module) | ✔ (PCF module; PACT/iLEAP) | ✔ (PCF at scale; PACT) | ✔ (AI product footprints) | Common capability; PCF-platform seam |
| Reduction simulation / levers | ✔ (procurement simulations) | — | — (Act module adjacent) | ✔ (Scope 3 reduction simulation; lever tracking) | — (not on fetched pages) | Optional; decarb-planning seam |
| Human service layer (advisors / customer success / validation teams) | — (not on fetched pages) | ✔ (Climate Strategy Advisors; enrichment) | ✔ (customer success engineering) | ✔ (validation team) | ✔ ("works directly with your vendors") | Common delivery posture |
| Downstream Scope 3 (use-phase, end-of-life) centered | ✘ (upstream supplier-centric page) | ✘ | ✘ | ✘ | ✘ | Not centered anywhere in sample |

## Canonical Abstraction

### L0 — Defining Invariant (three jointly-held structures)

**1. The value-chain emissions account of record.** The buying organization's value-chain (Scope 3) greenhouse-gas emissions computed and maintained as a persistent, period-over-period record, organized by emission source/category of the value chain. Estimates are legitimate first-class entries in this account — the account is explicitly a mixture of estimated and counterpart-provided data while the program improves it. Remove → a one-off footprint study or a supplier survey with no buyer-side account; the "management" object disappears.

**2. The value-chain counterpart population as managed data sources.** Suppliers (and other value-chain partners) held as identified records — with data status, emissions intensity, and engagement/maturity attributes — whose primary emissions data is requested, collected, and quality-assessed through the platform's own counterpart-facing surfaces (portal, survey, network, data-sharing module), progressively substituting for estimates in the account. Remove → carbon accounting computed wholly from the organization's internal activity data and published factors; the counterpart dimension disappears.

**3. The value-chain management loop.** The account drives continuous management: hotspot identification and prioritization across categories and counterparts, engagement actions (data requests, target commitments, joint reduction plans) tracked per counterpart, and emissions/data-quality progression tracked over time. Remove → a calculator plus a survey tool; the "management" loop disappears.

**Jointly-held load-bearing tests:**
- 1 alone = the Scope 3 slice of carbon accounting / an emissions data warehouse
- 2 alone = supplier survey/questionnaire tooling (supplier-sustainability territory)
- 3 without 1+2 = a generic engagement/program tracker
- 1+2 without 3 = carbon accounting with supplier-data ingestion (the modern carbon-accounting capability set — the closest failure mode)
- 1+3 without 2 = carbon accounting + reduction tracking with no counterpart collection
- 2+3 without 1 = a supplier engagement program with no account of record

**Historical / market-sample check (§24):** the minimal core is satisfiable without modern machinery. A spreadsheet-era buyer keeping a supplier-emissions workbook by spend category, collecting supplier figures by email, and tracking follow-ups satisfies all three legs (account + counterpart records + manual loop). Pre-2011 buyer-side supplier-carbon programs (CDP Supply Chain-style questionnaire collection, retailer supplier indexes) satisfy legs 2–3 with a thinner account — they are the class-level ancestry, reasoned not fetched this pass. The GHG Protocol's 15-category taxonomy (2011) is the dominant modern realization of "organized by emission source/category", not the invariant.

### L1 — Common Mature Structure

- **Category framework** — GHG Protocol Scope 3 categories as the dominant organizing scheme (named at Sweep, Cozero, ClimateCamp, Watershed; Normative computes Scope 3 under GHG Protocol).
- **Method hierarchy with documented progression** — spend-based → activity-based → supplier-specific; products state which method produced which figure (Sweep names all four GHG Protocol methods; ClimateCamp states spend-first-then-activity; Watershed "replacing industry averages with primary data").
- **Supplier profiles** — per-counterpart records carrying data status, emissions/intensity, and climate commitments/maturity.
- **Counterpart-facing surface** — portal account, structured survey, network profile, or data-sharing module; often with the counterpart's own footprint view and education content.
- **Data collection campaigns** — request creation, distribution, reminders, response intake, validation/approval before entry into the account.
- **Hotspot & prioritization views** — emissions by category and by supplier; ranking by impact and maturity; benchmarking.
- **Engagement tracking** — commitments, joint reduction plans, progress over time, per counterpart.
- **Audit trail / data lineage** — every figure traceable to source data, factor, and method; validation states.
- **Disclosure outputs** — CSRD/CDP/SBTi/ISSB-class reporting from the same record.
- **Procurement-system integration** — ERP/procurement connectors, spend/invoice ingestion.
- **Supplier education** — training content to raise data quality at source.

### L2 — Variant / Optional Structure

- **Supplier network / data reuse** — shared data marketplaces, pre-built profiles, third-party rating imports (EcoVadis, CDP, S&P), PACT/iLEAP-aligned exchange.
- **PCF collection & product-level exchange** — collecting suppliers' product carbon footprints; dual-sided data sharing (a supplier answers its own customers from the same platform).
- **Reduction simulation / lever modeling** — sourcing/design/logistics scenarios; supplier-specific reduction levers (recycled content, renewable share, transport mode).
- **Downstream Scope 3 depth** — use-phase/end-of-life categories carried through the category framework; not centered in the sampled products.
- **SBTi supplier-engagement target machinery** — engagement targets, commitment auto-imports.
- **AI machinery** — agents for outreach, enrichment, factor mapping (era-current).
- **Delivery posture** — standalone product vs module/solution of a carbon-management suite; advisory/customer-success-coupled vs self-serve.
- **Customer tier** — Fortune-500 enterprise vs mid-market/SMB poles.
- **Supplier-side self-service** — suppliers as (free) platform users with their own dashboards.

### L3 — Vendor-specific (research notes only)

- Sweep: Sweep School e-learning; 200+ sector benchmarks; LEI/ISIN/SBTi auto-import; "20% of suppliers driving 80% of emissions" framing; Track/Disclose/Act pillar naming.
- Normative: Carbon Network; named Climate Strategy Advisors; TÜV SÜD verification; 349,000 emission factors; EcoVadis integration as a named feature.
- Cozero: Log/Act/Share module names; iLEAP; "customer success engineering" as a packaged service; ~40,000 emission factors; "carbon belongs on the balance sheet" positioning.
- ClimateCamp: 35,000+ pre-built supplier profiles; 100+ retrieval agents; primary data validation team; PCF calculator; brewery/food customer base; PACT academy content.
- Watershed: CEDA/FLAG data foundations; cohorts; guided portal; 2.3M emission factors; 4.1 Gt EUM claim; sustainability-AI agent framing.

## Vendor-specific Findings

(see L3 above — none promoted to the canonical document)

## Rejected Findings

- **"Scope 3 = the 15 GHG Protocol categories" as definitional** — rejected. The category scheme is the dominant realization of "organized by emission source/category"; spreadsheet-era and pre-2011 programs organize value-chain sources without it. Historical check fails the narrow form.
- **"Supplier portal" as definitional** — rejected. Portals, structured surveys, data networks, enrichment services, and PCF-sharing modules are all realizations of the counterpart-facing surface.
- **"Downstream Scope 3 coverage" as definitional** — rejected. All sampled products center the upstream supplier population; downstream categories ride the category framework.
- **"PCF exchange" as definitional** — rejected. It is a common capability and the seam to product-carbon-footprint-platform; the unit of work here is the organization's value-chain account.
- **"SBTi supplier engagement targets (40%/67% rules)" as definitional** — rejected. Regime packaging; appears as FAQ content at one product.
- **"AI agents / automated outreach" as definitional** — rejected. Era-current implementation of outreach and enrichment.
- **"Supplier network/marketplace" as definitional** — rejected. Variant; two of five products lead with it, others import third-party data instead.
- **"Reduction simulation" as definitional** — rejected. Optional; decarbonization-planning seam.

## Boundary Findings

**vs carbon-accounting-platform (processed 2026-09-07) — keep-both, seam = object of work.**
Carbon accounting's unit of record is the organization's whole inventory (Scopes 1+2+3) computed from the organization's own activity data and documented factors; its pass explicitly recorded supplier engagement as a standard capability, NOT definitional. This Type's unit of work is the value-chain program: the counterpart population and the estimate→primary-data progression are the center, and the account is the Scope 3 slice that the program improves. The same vendors ship both (Watershed, Normative, Cozero, Sweep all also sell carbon accounting) — the market itself packages the value-chain program as a distinct solution/module (Watershed Supply Chain, Sweep Supplier Emissions, Normative Supply Chain Engagement, Cozero Scope 3 use case) and, at the ClimateCamp pole, as a standalone product. Removal tests hold both directions: strip the counterpart-collection loop and engagement tracking → carbon accounting's Scope 3 output remains; strip the whole-of-org inventory framing and keep the value-chain program → this Type remains.

**vs supplier-sustainability-management (§21 sibling, unprocessed) — forward flag.**
Candidate seam: that Type manages supplier ESG performance/compliance/ratings broadly (human rights, environment, social, audits, scores); this Type is specifically the emissions account plus carbon data collection from those same counterparts. Overlap risk: supplier scorecards and supplier data requests appear in both. To be ratified at that pass.

**vs sustainable-procurement-platform (§21 sibling, unprocessed) — forward flag.**
Candidate seam: procurement decision-making orientation (sourcing choices, supplier selection on sustainability criteria) vs this Type's emissions-account-and-engagement orientation. Sweep's procurement simulations and Watershed's "procurement choices ↔ emissions" touch the seam.

**vs decarbonization-planning-platform (processed 2026-09-07) — keep-both.**
That Type's object is the forward program: plan artifact, discrete levers/projects, planned-vs-realized progress. This Type's object is the value-chain data program: counterpart collection, data-quality progression, engagement tracking. Overlap: reduction tracking and hotspot analysis appear in both (ClimateCamp's reduction simulation is the closest approach). Seam: the plan/levers artifact vs the counterpart data program; neither sampled product here centers a plan artifact.

**vs product-carbon-footprint-platform (processed 2026-09-09) — keep-both.**
That Type's unit of account is the per-product figure and its delivery to external parties. Here, PCF collection from suppliers is a capability (Cozero PCF module, ClimateCamp PCF at scale, Watershed product footprints) in service of the organization's value-chain account, not the deliverable itself.

**vs esg-reporting-platform (processed 2026-09-08) — keep-both.**
Disclosure outputs are common capabilities here; the disclosure-back orientation (work begins from what must be disclosed) belongs to that Type. This Type is measurement/engagement-first.

**vs greenhouse-gas-accounting (alias of carbon-accounting-platform) — consistent.**
The alias resolution keeps methodology-name and product-name on one Type; this leaf is the value-chain program lens, not a third carbon-accounting name.

**Collapse tests for this leaf itself:**
- Remove the counterpart-collection loop and keep the buyer-side account → carbon accounting territory.
- Remove the account and keep the supplier surveys → supplier-sustainability/questionnaire territory.
- Remove the emissions subject and keep supplier management → supplier-sustainability-management territory.
- Remove the engagement loop → calculator + survey tooling, below the Type bar.

## Uncertainties

1. **Downstream Scope 3 depth** — none of the sampled products' fetched pages center downstream categories; their help centers (not fetched) might show downstream machinery. Assertions kept at "carried through the category framework; not centered".
2. **Downstream counterparts as data sources** — no sampled product page describes collecting data from customers/distributors as counterparts; possible at product-footprint-oriented vendors. Not asserted.
3. **Campaign mechanics detail** — question banks, cadence, and per-supplier sequencing observed only at marketing-page grain (Sweep pre-built campaigns; Cozero template forms). No precise mechanics asserted.
4. **Historical ancestry** — CDP Supply Chain / retailer supplier-index programs reasoned at class level for the historical check; not fetched. No specific claims made.
5. **Help centers unreachable** — all evidence is Tier 2 (official product/solution pages). Precise operational details (survey sizes, validation SLAs, category lists per product, factor counts) deliberately not stated in the final document.
6. **Type-vs-module tension** — the strongest risk to this leaf's independence is that modern carbon accounting platforms ship supplier-engagement modules. Mitigation: the keep-both pattern with the object-of-work seam, plus the market's own packaging (standalone Scope-3-first products exist). Recorded in Boundary Issues for the taxonomy owner.

## Final Synthesis

The Scope 3 Management Platform is the buying organization's value-chain carbon program system. Its defining core is three jointly-held structures: (1) the value-chain emissions account of record — the organization's Scope 3 emissions computed and maintained by source/category over time, with estimates as first-class entries; (2) the value-chain counterpart population — suppliers held as managed records whose primary emissions data is requested, collected, and validated through the platform's own counterpart-facing surfaces, progressively substituting for estimates; (3) the value-chain management loop — hotspots and prioritization across categories and counterparts, tracked engagement (data requests, commitments, joint reduction plans), and emissions/data-quality progression over time. Everything else — category taxonomy, supplier portals, PCF exchange, disclosure outputs, reduction simulation, AI outreach, supplier networks — is standard, variant, or vendor-specific structure layered on that core. The Type is documented from its own lens (the value-chain program) alongside carbon accounting (the whole-of-org inventory), consistent with the market's own packaging of both.
