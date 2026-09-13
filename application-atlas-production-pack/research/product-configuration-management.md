# Research Notes — Product Configuration Management

## Research Goal

Understand what a Product Configuration Management application is in the manufacturing sense: the software that manages a product's variant space — the options a product can be built with, the rules that define valid combinations, and the generation of concrete buildable variants from that model. Distinguish it from its nearest neighbors: Configure Price Quote (sell-side configuration), Bill of Materials Management (fixed product structure), PLM (the wider product-data estate), and Engineering Change Management (the change process over engineering objects).

## Initial Boundary

- Leaf: Product Configuration Management (DIRECTORY §16 Engineering, Manufacturing & Industrial).
- Working hypothesis: build-side configuration — the configuration model, variant resolution, and variant BOM/design generation — as opposed to CPQ's sell-side configuration (offer + price + quote). This seam was pre-recorded by the configure-price-quote-cpq pass (2026-09-07): "sell-side configuration (valid sellable offer + computed price + quote) vs build-side configuration (BOM/variants/engineering change)"; the Tacton ETO pole was held as a CPQ variant with a cross-check recommendation for this leaf.
- The bill-of-materials-management pass (2026-09-09) recorded: "configurable BOMs (options/variants) appear as L2 here; configuration-centered tools justify the separate leaf."
- Nearest confusables: CPQ, BOM Management, PLM (unprocessed leaf), Engineering Change Management (unprocessed leaf), PIM, Product Catalog Management, consumer-facing visual product configurators (e-commerce territory), MES (consumes variant BOMs).

## Research Questions

1. What is a "configuration model" / product model? What objects does it contain (characteristics/options, rules/constraints, structure linkage)?
2. How does a configuration session work — from selections to a concrete variant definition (variant BOM, route, design deliverables)?
3. How is the model itself maintained: versioning, validation, release/approval, effectivity over time?
4. Where does the capability live in the market: standalone layer, PLM module, ERP module, CAD-embedded tool, CPQ-suite component?
5. Who uses it (product engineering, sales, manufacturing, IT) and what surfaces do they touch?
6. What rules govern validity and completeness of configurations?
7. Where exactly is the seam vs CPQ, BOM management, PLM, ECM, PIM?
8. Historical check: would older/regional/platform-native products (paper option catalogs, 1980s expert-system configurators, 1990s ERP configurators) satisfy the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophy, and different hosting locus / customer tier:

1. **Configit Ace** (Configit A/S) — standalone SaaS "product configuration and variant management" layer; vendor-coined "Configuration Lifecycle Management (CLM)" approach; enterprise manufacturers (AGCO, CNH, Vestas, Siemens, Philips, Sidel, Knauf). The model-centric pole.
2. **PTC Windchill** (Product Variant Management / Configuration Management capabilities) — PLM-embedded variant management; enterprise discrete manufacturing (Volvo, Volvo CE, Polaris, Groupe Beneteau, Vestas). The PLM-suite pole.
3. **Microsoft Dynamics 365 Supply Chain Management — Product configuration** — ERP-native constraint-based product configuration models configured from sales/production order lines. The ERP-module pole; only sampled product with fully public Tier-1 operational documentation.
4. **DriveWorks** — SOLIDWORKS-embedded design automation / product configurator; SMB–midmarket; rules drive generation of order-specific CAD models, drawings, and manufacturing data. The CAD-embedded design-automation pole.
5. **Tacton** (Design Automation + Configuration Lifecycle Management + Configured Order Fulfillment within a CPQ-centered suite) — ETO/design-automation pole; primarily boundary evidence for the CPQ seam (consistent with the CPQ pass's Tacton observation).

## Sources

Fetched 2026-09-09 (Tier 1 = operational documentation; Tier 2 = official product/capability pages):

- Configit — home page, CLM approach page, Configit Ace product page, Align Engineering Data solution page (configit.com) — Tier 2 (product/solution pages; no public help center fetched)
- PTC — Windchill product page, Product Variant Management capability page, Product Configuration Management capability page (ptc.com) — Tier 2
- Microsoft — Dynamics 365 Supply Chain Management "Product configuration overview" (learn.microsoft.com/en-us/dynamics365/supply-chain/pim/build-product-configuration-model) — Tier 1
- Tacton — Design Automation use-case page (tacton.com) — Tier 2
- DriveWorks — home page (driveworks.co.uk) — Tier 2

Unreachable / not fetched:

- SAP Help Portal (help.sap.com) — JS shell; classic static help archive redirects to the same shell. SAP Advanced Variant Configuration (AVC) detail NOT evidenced. (Configit's own "migrate to SAP AVC" solution page confirms AVC exists as the S/4HANA configuration technology, but no operational detail asserted from SAP sources.)
- Siemens Teamcenter Product Configurator — docs.sw.siemens.com search 404; support portal gated. Not sampled.
- Aras Innovator Variant Management — aras.com product URL 404; timed out on retry. Not sampled.
- PTC help center (support.ptc.com) — not attempted after product pages proved rich; Windchill evidence is product-page strength.
- DuckDuckGo HTML search — timed out ×2; Bing site-restricted search region-localized and unusable for deep links.

## Product A — Configit Ace (Configit)

### Key observations (evidence layer A unless noted)

- Self-label: "SaaS product configuration and variant management solution enabling Configuration Lifecycle Management (CLM)" (Ace product page).
- CLM framing (CLM page): "CLM establishes a 'shared-source-of-truth' for configurable product options and rules... defined collaboratively and consumed efficiently by all departments, ensuring consistency and reducing errors across the entire organization." Benefits named: holistic view of "all configurable options and rules across product design, sales, manufacturing, and service"; traceability via "Digital Configuration Threads"; error reduction ("zero errors during product configuration"); automation of "the delivery of new products and the addition of new rules and options."
- Knauf quote (Ace page): "all product data across the organization must be aligned to a central configuration model."
- Ace capabilities (Ace page): "Define even the most complex product models with declarative rules and guided assistance using Configit Ace Model® UI and API"; "Consolidate existing product models, BOMs and pricing from multiple systems with Configit Ace® Compile API"; "Test and verify product models before release with conflict resolution guidance using the Configit Ace Verify® UI"; "Securely consume product models in any system or product configuration application with the Configit Ace® Configure API"; "Configit Effectivity — manage product configuration data over time"; "Analysis and optimization of all product variants and configurations over time"; "Guided Configuration... evolve your guided selling into guided configuration."
- Virtual Tabulation®: "multi-patented configuration AI technology" — the compilation/validation engine (vendor-specific technology, L3).
- Align Engineering Data page: "Configuration models and 150% BOMs create massive numbers of possible product combinations. Manual testing cannot reliably verify them, allowing rule conflicts and errors to surface later in quoting, ordering, or production." "Configuration data often lives across PLM, ERP, and CPQ in different formats. Teams must reconcile and interpret this data manually." "every configuration is accurate and buildable before it reaches sales, operations, or production." Portfolio challenge: "end-to-end insight into available, orderable, and sold configurations... Options may never be offered or rarely purchased."
- Solutions: "Validate and Align Engineering Data" (across PLM/ERP/CPQ), "Enable CTO with Partial ETO", "Customer Experiences for Customizable Products". SAP AVC migration page exists ("Explore This Capability for SAP").
- Integrations listed: SAP, PTC, Salesforce, Oracle, Dynamics, SolidWorks, Enovia, Aras, NVIDIA, Unity.
- Philips quote: "we are now able to guarantee that we have one shared source of truth. Our product management organizations can now manage the complete catalog in a single tool."
- Vestas customer story: "100% BOMs Validated for introducing new products into the configurator."
- Configit also sells **Configit Quote** (CPQ) as a separate product — the vendor itself splits the configuration layer from the CPQ layer.

## Product B — PTC Windchill (Product Variant Management / Configuration Management)

### Key observations

- Variant Management capability page: "Product variants are modifications of a master product, such as differing feature sets, materials, colors, or performance levels. Product variant management is the process of managing variants throughout the product lifecycle."
- "Platform options, choices, logic, and configuration rules are directly linked to the bill of material (BOM), 3D visualization, and CAD data to deliver a robust modular solution. Platform information can be fully lifecycle-managed, making it easily available to validate the product and share it with other enterprise tools such as ERP and CPQ."
- Key features (variant management page): "Option pool/option set — enterprise management and visibility to options and logic, removing the need for spreadsheets"; "Advanced logic — range-based variables, case tables"; "Product family matrix — quickly see how configurations are planned"; "Rules logic — a variety of rules that define how products can be configured... tie together engineering and marketing logic"; "Multiple development streams — manage multiple parallel development branches"; "Change management — synchronize changes from design through to plant-specific production information managed in ERP systems with local and global rule effectivity management"; "Configure variant BOM — create configurations for order specific variants or use these to describe stock offerings based off a common platform."
- Configuration Management capability page (ptc.com/en/technologies/plm/product-configuration-management — the leaf's exact vocabulary): "Product configuration, often referred to as knowledge-based configuration, is the process by which parts and components are selected and arranged, to meet a given set of requirements." Production strategies: "Assemble-to-stock and assemble-to-order (ATO) support fixed product features... Configure-to-order (CTO) builds on top of that and adds variable features, while engineering-to-order (ETO) can start from either ATO or CTO and deliver order specific engineering."
- "knowledge-based configuration seeks to manage customization requirements more quickly and accurately... improving the accuracy and timeliness of BOM generation."
- "Rather than reconfiguring a new product every time an order is placed, variant management allows engineering to reuse predefined configurations (or variants) and to apply change management, quality workflows, and other processes to all like variants simultaneously."
- Challenges named: lack of alignment, outdated product designs, lack of reuse, lack of governance ("Changes to a product's configurations throughout its lifecycle aren't traceable").
- FAQ distinction: "Product options are simply variants selected by the customer at time of purchase... product variants are pre-selected and produced by the manufacturer." Both "require advanced variant management capabilities."
- Related capabilities listed: Bill of Materials, Configuration Management, Change Management — variant management sits beside them inside the PLM estate.
- Codebeamer (ALM sibling) "extends ALM functionalities with product line configuration capabilities."

## Product C — Microsoft Dynamics 365 Supply Chain Management (Product configuration)

### Key observations (Tier 1)

- Purpose: "In both business-to-business and business-to-consumer relationships, you often need to configure products to meet special requirements. A manufacturer that supports configure-to-order scenarios can better address customer needs."
- Modeling principles named: "rule-based, dimension-based, and constraint-based modeling" — constraint-based preferred (declarative OML syntax, no developer license; rule-based X++ code legacy = "Product Builder" migration path).
- Model structure (all directly documented): **components** ("main building blocks... connect through subcomponent relationships"); **attributes** ("users choose the attributes during the configuration process. Attributes control both inter-component and intra-component relationships through inclusion in constraints or calculations. Through conditions applied to BOM lines, attributes can determine which physical parts the configured product consists of"); **expression constraints** (Optimization Modeling Language); **table constraints** (user-defined or system-defined); **calculations** ("arithmetic operations... determine the length of a specific piece of raw material or the processing time for a polishing operation"); **subcomponents** (nodes referencing product masters with "constraint-based configuration" technology); **user requirements** (phantom-BOM-like); **BOM lines** ("identify the manufacturing BOM for each component... properties can be set to a fixed value or mapped to an attribute"); **route operations** ("identify the manufacturing route... properties... mapped to an attribute").
- Validation: per-constraint, per-condition, per-table-constraint, and whole-model validation. Testing: "Testing a model is similar to running an actual configuration session... after a test session is completed, the system tries to create the BOM and the route that corresponds to the selected attribute values, and presents an error message if anything goes wrong."
- Finalizing: attribute groups (UI), configuration templates, translations, **versions**: "Create a version for the product configuration model. The version represents the relationship between the product master... and the product configuration model. A version must be approved and activated before it can be used in a configuration session."
- Configuration sessions: "You can configure products from the following places: Sales order line, Sales quotation line, Purchase order line, Production order line, Item requirement line (project)." "The purpose of the configuration is to create a distinct variant of the product that meets the customer's requirement. A unique configuration ID is created for each new configuration. This ID enables tracking through inventory."
- Multi-site/intercompany: "the BOM and the route are created for and put them at the supplier site in the supplying company. The product variant is released in all companies that participate in the supply chain."
- Extension API (PCAdaptor classes) for partners.

## Product D — DriveWorks

### Key observations (Tier 2)

- Self-label: "SOLIDWORKS® design automation and product configurator software"; "3D product configurator, CPQ, and SOLIDWORKS® design automation software."
- "DriveWorks technology enables you to accurately configure custom products, calculate pricing, and automatically create documents and data for sales and manufacturing."
- "DriveWorks captures and centralizes the decisions, information, experience, and product constraints teams use to configure products manually. This captured knowledge is then used to calculate values, make decisions, perform actions, and automatically create order-specific sales documents and SOLIDWORKS® manufacturing data."
- "Sales, engineering, and manufacturing are seamlessly linked with a shared source of truth."
- "DriveWorks configurators are based on rules, calculations and logic, improving the quality of outputs, reducing costly errors."
- "Automatically create order-specific SOLIDWORKS® parts, assemblies, and drawings."
- Solutions split: Design Automation / 3D Product Configurator (guided selling + 3D visualization) / CPQ for Manufacturing — three commercial surfaces over one rules engine.
- Products: DriveWorksXpress (free inside SOLIDWORKS), Solo (add-in), Pro (with Autopilot automation, Live web configurator, User). Integrations: SOLIDWORKS PDM, DELMIAWorks/SYSPRO ERP, Salesforce, QuickBooks.

## Product E — Tacton (boundary evidence)

### Key observations (Tier 2)

- Tacton Design Automation: "Connect your CAD tools to turn customer requests into instant, accurate 2D/3D CAD models"; "automatically applies configuration constraints implemented in your Tacton CPQ buyer engagement platform to all designs"; "rule-based engineer-to-order automation inside SOLIDWORKS... automatically generate complete 2D drawings, 3D models, and quote documents"; "uses a powerful constraint solver to validate all configurations."
- Customer quotes: "the drawings and even Bill of Materials are now generated at the same time as the proposal" (ClearStream); "Products are already validated from a design and manufacturing point of view before an order is placed" (Kramp).
- Suite structure: Configure Price Quote (configuration/pricing/quoting) + **Configuration Lifecycle Management** (Tacton also uses the CLM label) + **Configured Order Fulfillment** + Design Automation use case.
- Confirms the CPQ pass's finding: Tacton's center of gravity is the commercial loop; design automation and CLM are suite components. Held as boundary evidence, not a core PCM sample.

## Cross-product Comparison

| Dimension | Configit Ace | PTC Windchill | D365 SCM Product Configurator | DriveWorks | Tacton |
|---|---|---|---|---|---|
| Hosting locus | standalone SaaS layer across PLM/ERP/CPQ | PLM module | ERP module (product information management) | CAD-embedded (SOLIDWORKS) + web | CPQ suite component |
| Unit of record | configuration model (shared source of truth for options + rules) | platform options/choices/logic linked to BOM/CAD | product configuration model (components/attributes/constraints) | rules project capturing product constraints | configuration constraints in CPQ platform |
| Rule formalism | declarative rules; Virtual Tabulation compilation (vendor tech) | rules logic, range-based variables, case tables | expression constraints (OML), table constraints, calculations | rules, calculations, logic | constraint solver |
| Structure linkage | consolidates "product models, BOMs and pricing" | options/logic "directly linked to the BOM, 3D visualization, and CAD data" | BOM lines + route operations inside the model | generates SOLIDWORKS models/drawings/manufacturing data | generates drawings + BOM with the proposal |
| Resolution output | valid configuration data via API to any system | variant BOM (order-specific or stock offerings) | distinct variant + generated BOM + route, unique configuration ID | order-specific CAD parts/assemblies/drawings + sales documents | 2D/3D CAD models, drawings, BOM, quote |
| Model lifecycle | Verify (test/conflict resolution) before release; Effectivity over time | lifecycle-managed platform info; change management with rule effectivity | version must be approved + activated before use | projects maintained in CAD environment | constraints maintained in CPQ platform |
| Session trigger | guided configuration for sales/engineering/service | engineering-led; shared to ERP and CPQ | sales quote/order line, purchase line, production order line | sales/user forms, web configurator | sales/rep-driven, self-service |
| Validation claim | "zero errors"; "100% BOMs validated" (Vestas) | validate the product; governance/traceability | system generates BOM+route or errors | "100% reduction in design errors" (marketing) | constraint solver validates all configurations |
| Portfolio analysis | offered vs sold vs delivered vs serviced | product family matrix | — | — | analytics module |
| Cross-system sync | Compile/Configure APIs; align PLM/ERP/CPQ | share with ERP and CPQ; sync design→plant production info | variant released across supply-chain companies | integrations to ERP/PDM/CRM | integrations to ERP/CRM/PLM/PIM |

### Cross-product commonalities (evidence layer B)

1. **A rule-governed product model as the maintained artifact** — every sampled product centers on a persistent model of options/attributes + rules/constraints tied to the product's structure. (5/5)
2. **Resolution of selections into a concrete buildable variant definition** — variant BOM (Configit-consolidated, PTC, D365), BOM+route (D365), CAD models/drawings/manufacturing data (DriveWorks, Tacton). (5/5)
3. **Validity enforcement at configuration time** — constraints/constraint-solver reject invalid combinations during the session. (5/5)
4. **Model testing/validation before release** — Configit Verify, D365 test session + version approval/activation, PTC validation + change management. (3/5 explicit; DriveWorks/Tacton implied at product-page strength)
5. **Effectivity / validity over time** — Configit Effectivity, PTC local/global rule effectivity. (2/5 explicit — held common-mature, not definitional)
6. **Cross-system consumption/synchronization** — APIs to ERP/CPQ/PLM (Configit, PTC, Tacton, DriveWorks); variant release across companies (D365). (5/5)
7. **Guided configuration sessions** — D365 configuration pages, Configit guided configuration, DriveWorks forms/3D, Tacton visual configurator. (4/5 + PTC implied)
8. **150% BOM / variant BOM vocabulary** — Configit names "150% BOMs" explicitly; PTC "configure variant BOM"; D365 conditions on BOM lines. (3/5 explicit)

## Canonical Model

### Level 0 — Defining Invariant

Three jointly-held structures:

1. **The configuration model** — a persistent, rule-governed definition of one product's variant space: the selectable characteristics (options/attributes), the rules/constraints that define which combinations are valid, and the linkage to the product's structure (BOM/route/design). Remove → fixed-definition BOM management (one structure per product) or a generic rules engine with no product meaning.
2. **Variant resolution** — a configuration session in which selections over the model are validated against the rules and resolved into a concrete, buildable variant definition (variant BOM, route, order-specific design/manufacturing data), identified and tracked as its own record. Remove → an option catalog or guided-selling UI with no product definition output.
3. **The maintained model lifecycle** — the model itself is a controlled artifact: tested/validated, versioned/released, and changed as the product evolves, so the variant space stays current and consumable by other systems. Remove → a one-shot generator or spreadsheet of rules.

Jointly-held load-bearing:
- 1 alone = a rules/option database (no resolution, no output)
- 2 without 1 = ad-hoc order entry / guided selling with no governed variant space
- 3 without 1+2 = document control over configuration documents
- 1+2 without 3 = a generator that drifts from the product as it evolves
- 1+3 without 2 = a curated model nobody can configure against
- 2+3 without 1 = session tooling with no model behind it

The build-side orientation is carried by leg 2: the resolution output is a product definition consumed by engineering/manufacturing (BOM/route/design), not merely a priced offer. This is the seam vs CPQ.

### Level 1 — Common Mature Structure

- Option/attribute catalogs with enterprise visibility ("removing the need for spreadsheets" — PTC)
- Declarative rule/constraint authoring (expression languages, table constraints, case tables, calculations)
- Model validation and test sessions before release; conflict-resolution guidance
- Variant BOM generation (150% BOM → order-specific variant BOM) and route generation
- Effectivity management (rules/options valid per date/product line/plant)
- Cross-system delivery: APIs/sync so ERP, CPQ, PLM, and service consume the same model
- Guided configuration UI (attribute groups, templates, translations)
- Product family / portfolio views; offered-vs-sold analysis
- Unique identity per resolved configuration, tracked downstream (D365 configuration ID)

### Level 2 — Variant / Optional Structure

- Hosting locus: standalone CLM layer / PLM module / ERP module / CAD-embedded tool / CPQ-suite component
- Output flavor: BOM+route (ERP pole) vs CAD models/drawings (design-automation pole) vs validated model data via API (model-centric pole)
- CTO vs ETO posture; partial-ETO migration programs
- 3D/visual configuration surfaces
- Pricing integration (sell-side adjacency)
- AI-assisted model authoring; AI decision validation guardrails
- Migration tooling between configurator technologies (e.g., to SAP AVC)
- ALM/product-line configuration for software-intensive products (Codebeamer)

### Level 3 — Vendor-specific (Research Notes only)

- Virtual Tabulation® compilation technology, Ace Model/Verify/Compile API/Configure API product names, CLM-as-a-Service (Configit)
- OML expression language, PCAdaptor API, Product Builder legacy, dimension-based vs constraint-based technologies (Microsoft)
- Option pool/option set, choice links, product family matrix, Codebeamer pairing (PTC)
- Autopilot/Administrator/Live/User component split, DriveWorksXpress/Solo/Pro tiers (DriveWorks)
- Design Automation plug-ins for SOLIDWORKS/Inventor/Creo, Configured Order Fulfillment module (Tacton)

## Vendor-specific Findings

- Configit's CLM is a vendor-coined methodology label; Tacton now uses the same label for its suite component. Treat "Configuration Lifecycle Management" as market vocabulary for the shared-model-across-lifecycle posture, not a definitional term.
- PTC's own capability page uses the leaf's exact name ("Product Configuration Management") for knowledge-based configuration inside PLM — evidence the leaf name matches market vocabulary.
- D365 documents three modeling principles (rule-based, dimension-based, constraint-based) and a legacy "Product Builder" — evidence that rule depth and formalism vary widely within the Type.
- DriveWorks packages the same rules engine as three solutions (design automation / configurator / CPQ) — evidence that the CPQ surface is a packaging of the configuration core, not the core itself.

## Boundary Findings

- **vs Configure Price Quote / CPQ** (sibling pass, pre-recorded seam — CONFIRMED from this side): CPQ's center is the commercial offer (valid sellable offer + computed price + quote + approvals); PCM's center is the product's variant space and its resolution into buildable definitions. Evidence: Configit sells Ace (configuration/variant management) and Quote (CPQ) as separate products; DriveWorks sells "CPQ for Manufacturing" as a solution over its rules engine; Tacton holds Design Automation inside a CPQ suite while the quote loop remains the center. The same configuration model can feed both — the seam is the center of gravity, not exclusive capability. The CPQ pass's cross-check recommendation is discharged: keep both leaves; the engineer-to-order CPQ pole stays CPQ as long as the quote loop is the center.
- **vs Bill of Materials Management** (sibling pass): BOM management owns the structural definition of specific product records (item + structure + revision, change-controlled). PCM owns the variant space that generates many concrete BOMs from one model. The BOM pass itself held configurable BOMs at L2 and said "configuration-centered tools justify the separate leaf" — confirmed. Seam: one controlled structure vs a rule-governed space of structures. 去掉判据: remove the rules/variant space → BOM management; remove the structure linkage → a rules engine.
- **vs Product Lifecycle Management / PLM** (unprocessed leaf): PLM is the product-data estate (CAD/PDM/BOM/change/documents/requirements). Variant/configuration management appears inside PLM suites as one capability (PTC frames it exactly so). A standalone configuration layer (Configit) sits across PLM/ERP/CPQ without owning the estate. Proposed seam for the PLM pass: estate vs variant-space layer. No directory change recommended.
- **vs Engineering Change Management** (unprocessed leaf): ECM owns the change process (CR/CO/approval) over engineering objects. PCM embeds model versioning/release as one leg (D365 version approval; PTC change management with rule effectivity) but its center is the variant space, not the change process. The BOM pass flagged ECM's alias risk; this pass adds: PCM's model-lifecycle leg is object-scoped (the model), not the enterprise change discipline.
- **vs Product Information Management / PIM** (sibling pass): PIM manages commercial/catalog content for selling channels; PCM manages technical variant logic and buildable definitions. Consistent with the BOM pass's "no confusion risk" finding. Option lists may surface in PIM as selling content — different object content, same words.
- **vs Product Catalog Management / Digital Product Catalog** (processed siblings): catalogs organize sellable offerings; PCM defines what can be built and how options combine. A catalog may expose options; it does not resolve them into BOMs.
- **vs consumer-facing visual product configurators** (e-commerce/CPQ channel territory): buyer-facing 3D/visual configuration (DriveWorks' "3D Product Configurator" solution surface, Tacton's visual configurator) is a selling surface over the configuration model. The Type's invariant is the model + buildable resolution, not the visual selling experience.
- **vs Manufacturing ERP / Production Planning / MES**: ERP hosts configuration models (D365 pole) and consumes resolved variants into planning/production; MES executes released orders. Direction of truth-flow: the configuration model defines; planning/execution consumes. Consistent with the BOM pass's direction-of-truth discriminator.
- **去掉什么就变成另一个 Type 判据**: remove rules/constraints → simple attribute-variant lists (dimension-based variant management degenerates toward plain product variant records); remove structure linkage → generic rules/decision engine; remove resolution → option catalog/documentation; remove model maintenance → one-shot generator; shift center to offer/price/quote → CPQ; shift center to CAD-file vaulting → PDM; shift to the full product-data estate → PLM; shift to the change process over engineering objects → ECM; shift structure content to commercial selling data → PIM.

## Historical / Market-Sample Check (§24)

- Paper era: an option/feature catalog + a master specification listing available options + written combination rules + manual assembly of an order-specific build sheet/BOM satisfies all three legs (variant space defined; resolution by a person; the catalog maintained and revised). The definition holds without software-era machinery.
- 1980s: rule-based expert-system order configurators (the XCON/R1 generation at Digital Equipment Corp.) configured computer orders into buildable bills of material — the same three legs with different technology. Held as conceptual lineage (low strength, not fetched).
- 1990s: ERP-embedded product configurators (SAP LO-VC generation; D365's own docs describe migrating from the older rule-based "Product Builder") — the ERP pole predates SaaS/AI/constraint-compilation.
- Conclusion: L0 must not include SaaS delivery, APIs, constraint-solver technology, 3D visualization, or AI — all era-current. The historical check passes.

## Uncertainties

- SAP Advanced Variant Configuration (AVC) / LO-VC: help portal unreachable (JS shell ×3 attempts). SAP-specific operational detail NOT asserted anywhere. The ERP pole rests on D365's Tier-1 docs; SAP's existence as the dominant ERP configurator is supported only by Configit's SAP-integration/migration pages (layer B, indirect).
- Siemens Teamcenter Product Configurator: not sampled (gated docs). The PLM pole rests on PTC alone — single-product support for PLM-module specifics; PLM-module claims kept generic.
- Aras Innovator Variant Management: not sampled (404 + timeout).
- DriveWorks and Tacton evidence is product-page strength (Tier 2); no help-center depth. Their internal model/versioning mechanics not asserted.
- Effectivity management: explicit at 2/5 sampled products — held common-mature, not definitional; depth varies.
- Exact state names, numeric limits, performance figures (e.g., "92% faster") are vendor marketing claims — recorded here as claims, not asserted in the final document.
- The "150% BOM" term is Configit's explicit vocabulary; PTC/D365 describe the mechanism without the term. The mechanism is cross-product; the term is not universal.
- Historical anchors (XCON, LO-VC) used as low-strength conceptual lineage only; no archival documentation fetched.

## Final Synthesis

Product Configuration Management is the manufacturer's system of record for a product's variant space. Its defining structure is a triple: a persistent, rule-governed configuration model (selectable options/attributes + validity rules + linkage to the product's structure); variant resolution (a configuration session that validates selections and resolves them into a concrete buildable definition — variant BOM, route, order-specific design/manufacturing data — as an identified, tracked record); and a maintained model lifecycle (the model is tested, versioned/released, and changed under control as the product evolves). Around that core, mature products add option catalogs with enterprise visibility, declarative rule authoring, validation with conflict guidance, effectivity over time, cross-system delivery to ERP/CPQ/PLM/service, guided configuration surfaces, and portfolio analysis of offered-vs-sold configurations. The market realizes the Type at five hosting loci — standalone configuration layer, PLM module, ERP module, CAD-embedded design automation, CPQ-suite component — which are packaging variants of one model, not separate Types. The boundary is drawn by the center of gravity: the variant space and its buildable resolution — not the priced offer (CPQ), not one fixed structure (BOM management), not the product-data estate (PLM), not the change process (ECM), and not commercial selling content (PIM).
