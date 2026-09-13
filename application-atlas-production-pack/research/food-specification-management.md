# Research Notes — Food Specification Management

Research date: 2026-09-08
Slug: `food-specification-management` (DIRECTORY.md §20 Agriculture, Food & Natural Resources)
Methodology: WORKFLOW v1.1 / WRITING GUIDE v1.1

---

## Research Goal

Understand what "Food Specification Management" software actually is by studying real products: what a specification is in the food industry, what the software holds, who works in it, what the lifecycle of a spec is, and how specs move between the manufacturer and its trading partners. Produce a vendor-neutral Application Document.

## Initial Boundary (hypothesis before research)

- **Guess at core use**: the product specification — a formal, structured statement of a food material's or product's properties and requirements — is the object of record; the software authors, versions, approves, stores, shares, and keeps specs current.
- **Likely users**: QA/technical, regulatory, R&D/NPD, procurement/supplier quality at food & beverage manufacturers; suppliers as external collaborators; retailers/customers as spec requesters.
- **Nearest Types** (from the already-processed §20 siblings):
  - Food Formulation Platform (processed 2026-09-08): composition of record vs formal statement of record. Its pass hung a flag on this leaf: "TraceGains sells Formula Management and Specification Management as separate products; SpecPDM contains both with the formula upstream of the spec."
  - Food Labeling Platform (processed 2026-09-08): label artifact vs the broader technical record; its pass wrote "the spec is the whole product record (physical, chemical, microbiological, packaging); the label is one derived output."
  - Food Manufacturing ERP (processed 2026-09-08): holds specifications as operational attributes feeding production and labels — dedicated spec management centers the spec record itself.
  - Food Safety Management (processed 2026-09-08): supplier approval machinery exists there too; discriminator = supplier's compliance program vs the product's technical statement.
  - Also: Food PLM (unprocessed sibling — flagged for container-vs-core), PIM (commerce-facing product info), Supplier Quality Management (§16), Document Management.
- **Unknowns going in**:
  1. Is trading-partner exchange definitional or just common?
  2. Is the spec-type triad (raw material / packaging / finished product) universal?
  3. What does the approval/version lifecycle concretely look like?
  4. How much of the spec content is computed from formulation vs entered?

## Research Questions

1. What is a specification in this domain, and what content does a spec record hold?
2. What kinds of specs exist (raw material, packaging, finished product, process)? Which are universal?
3. What is the spec's lifecycle — statuses, approvals, versions, effective dating, review cycles?
4. How do specs move between parties — who requests, who authors, who approves, who signs?
5. What data flows into the spec from upstream (formulation, declaration) and downstream (labels, quality, ERP)?
6. What interfaces do users actually work in?
7. What pain narrative does the category tell (i.e., what is the pre-digital state it replaces)?
8. Where exactly are the seams vs formulation, labeling, PLM, ERP, PIM, supplier compliance?

## Representative Products (sample rationale)

| Product | Pole | Customer tier / posture |
|---|---|---|
| TraceGains Specification Management | Category-naming networked suite; spec mgmt as named product line alongside separate Formula Management | Enterprise CPG (US) |
| SpecPage SpecPDM (Revalize) | Spec/data-led European suite; Tier-1 manual reachable | European mid/enterprise manufacturers |
| Foods Connected Specifications & NPD | Modular food supply-chain suite; specs + NPD as one solution | Mid-market retailers, manufacturers, SMEs (UK/IE origin) |
| Specright | Spec-first platform ("Specification Data Management"); packaging-heavy; deliberately multi-industry (boundary pole beyond food) | Enterprise + challenger brands |

Different product philosophies (networked exchange / master-data suite / modular supply-chain suite / spec-first platform), different geographies, different tiers. Specright included deliberately as the boundary pole that extends past food.

## Sources

**TraceGains (Tier 2, official product/marketing pages)**
- Product page: https://tracegains.com/product-development/specification-management/
- On-demand demo page: https://www.tracegains.com/resource/specification-management/
- Product-line navigation observed across pages (Formula Management, Specification Management, Packaging Spec Management, Finished Goods, Regulatory Global, NutriCalc as separate NPD products)

**SpecPage (Tier 1 manual + Tier 2 product page)**
- SpecPDM Online Help manual root: https://help.specpage.com/SpecPDM/en/ (TOC)
- Data/Document Control: https://help.specpage.com/SpecPDM/en/daten-_dokumenten-lenkung.htm
- Master Data > Laboratory Data: https://help.specpage.com/SpecPDM/en/spezifikation.htm
- Reporting > Master data > Specification: https://help.specpage.com/SpecPDM/en/reporting_master_data_specification.htm
- Sub-report functionality/content (spec document anatomy): https://help.specpage.com/SpecPDM/en/reporting_master_data_specification_functionality_and_content.htm
- Declaration Automatic > Specifications: https://help.specpage.com/SpecPDM/en/specifications.htm
- SpecPDM product page: https://specpage.com/product-data-management/

**Foods Connected (Tier 2)**
- Root: https://www.foodsconnected.com/
- Specifications & NPD solution page + FAQ: https://www.foodsconnected.com/solutions/food-specifications-npd/

**Specright (Tier 2)**
- Root: https://specright.com/
- Category-definition page: https://www.specright.com/what-is-specification-management/

Prior-pass context (same production pack): research notes of food-formulation-platform, food-labeling-platform, food-manufacturing-erp, food-safety-management passes informed the boundary hypotheses.

### Source-access limitations
- TraceGains enterprise help center (enterprise-support.tracegains.com knowledge base) not attempted/deep articles not reachable; evidence rests on official product pages. Per evidence rules, no TraceGains workflow internals asserted beyond what its pages state.
- Foods Connected and Specright: official marketing/product pages only; their FAQ pages are explicit and used where they describe product behavior, still Tier 2.
- SpecPDM manual pages are Tier 1 (operational documentation) — the strongest evidence in this pass.

---

## Product Observations

### TraceGains Specification Management

Evidence layer: A for this product (official pages), Tier 2.

Key observations:

- **Positioning**: "Bring every spec into one trusted platform that streamlines updates and minimizes errors across your operation." Specs named across "ingredients, packaging, and finished goods" — the triad appears verbatim in its own questions ("How do I eliminate spec inconsistencies across ingredients, packaging, and finished goods?").
- **Pain narrative**: "Specifications spread across spreadsheets, PDFs, and emails make it hard to find what's current… risk working from outdated information." "It's the specs. There are so many of them… different versions, and the versions are in different statuses."
- **Six capability pillars** (its own words):
  - Standardize — "configurable templates that reduce errors and automatically update as changes are made"
  - Control — "full version history and automated effective-date workflows"
  - Configure — "customizable specs with configurable templates for labels, packaging, instructions, and tolerances"
  - Collaborate — "secure access, automatic alerts, and shared updates… audit-ready"
  - Connect — "link specifications to items and suppliers across a global network"
  - Optimize — "automate admin-heavy tasks… lower compliance and recall risks"
- **Questions it claims to answer**: "Who has the latest approved version and what changed?"; "Can I update hundreds of specs instantly without introducing risk?"; "How do I connect specs to formulas, items, and supplier data so nothing falls through the cracks?"; "standardize specs across suppliers without slowing down my innovation cycle?"
- **Downstream seam (its own words)**: "When specs aren't aligned, errors carry into formulation, labeling, and compliance workflows."
- **Supplier side**: "Smart & Final collaborates directly with suppliers to create and update specifications." Demo page: "Millions of supplier documents instantly available via TraceGains Marketplace"; "edit sections and attributes of specification templates, with auto-update of impacted specs"; "collaboration tools including full audit trails and correspondence tracking"; "flexible formatting for label images, packaging guidelines, preparation instructions, and in/out-of-spec tolerance images."
- **Customer-quoted surface**: QA manager cites dashboards ("keep everyone on the same page").
- **Family context**: Formula Management and Specification Management are separate products in the same NPD line — direct evidence for the formulation/spec seam. Packaging Spec Management is its own product page as well.

### SpecPage SpecPDM

Evidence layer: A, Tier 1 (operational manual) — strongest evidence in this pass.

- **Master Data > Laboratory Data (= the specification content of a material)**: test criteria assigned per supplier; each criterion carries method, unit, and marginal values — **LA (lower alarm), MIN, TV (target value), MAX (upper required), UA (upper alarm)** — plus comments, code lists, analytical method, findings, CoA (certificate of analysis) availability flag. Criteria organized by an administrable **criteria structure** (areas/groups; mandatory criteria highlighted). Values can differ per supplier ("switch between suppliers"). "Define which parameters are to be accepted in the test specifications for quality testing." Exportable to Excel (one worksheet per supplier).
- **Data/Document Control (governance model)**: "all actions and results of data maintenance and development should take place according to uniform rules of a processing cycle of **creation/modification – validation – release**." Framed as fulfilling ISO 9001 and mapping a data life-cycle via History. Processing statuses are per-organization configurable and visible per work step (Material – Recipe – Declaration). Control statuses gate permissions/workflows: "a raw material cannot be released by every user and only those with certain permissions"; "if a status of an object is changed, a QA responsible person will automatically receive an e-mail notification." A **Change index (processing version)** is explicitly distinguished from the **release version**. Control-flow fields lock until the control step is disabled. Owner concept for protected objects.
- **Specification report (the generated document)**: generated per master-data object from a selectable **release version** ("After the selection of a provider, all provider releases will be loaded. The last release is set as default; you may… choose from all available release versions"), with **issuer** (from partner structure), provider/producer **contacts**, food-law context (GDA country/group), optional **inspection plan** inclusion, and profile-driven sections. **Specification Multilanguage** report type exists.
- **Spec document anatomy (default sub-reports)** — the manual enumerates the full section catalog: Header; General (material, vendor, producer, contacts); Definition; Product description (pictures, description criteria); Dosage; **Recipe composition** (component columns, sums, component order incl. mixing sequence); **Product composition** (declaration fields; ingredients as table or continuous text; %ON threshold excluding ingredients <1%; trade definition; allergen note per factory line); **Additives 1–3** (class filters); GDA; Declaration; **Allergens**; Status; **GMO**; **Nutritional values** (with comment/tolerance values); Vitamins; Minerals; **Microbiological characteristics** (from Laboratory data); **Chemical and physical characteristics / calibration**; Recipe parameters; **Shelf life / Storage**; Code; **Packaging information**; Other; **Foreign bodies**; **Confirmation** (completed on/by, stamp, signature, released by); Footer (**version, release date, print date**). Rounding configurable per section (decimal places vs significant figures).
- **Declaration Automatic > Specifications (admin)**: defines which recipe/declaration data flows into the finished material when recipe generation is initiated: base data, prices, ingredients (from recipe or declaration list), additional descriptions, customs info, calculation criteria, attributes, laboratory data, processing status. → Direct Tier-1 evidence that the finished-goods spec is **populated from the recipe/declaration**, i.e., formulation sits upstream.
- **Product page (Tier 2)**: "Specifications — automated management of product specification, ingredients and declarations list. Saves multiple templates. Automatic generation of reports; product data sheets, allergen lists. Histories, traceability. Certification-based management in accordance with ISO and IFS standards. Audit workflows." Master Data Management: "multiple suppliers/specifications per material or per recipe." Reporting: "unlimited templates for specifications, test reports, certificates and recipe reports." Family splits SpecPagePLM (lifecycle) vs SpecPDM (product data) vs SpecPIM (product information for commerce) vs GDSN/Buyer's/Supplier's Guide (exchange).

### Foods Connected — Food Specifications & NPD

Evidence layer: A for this product (official solution page + FAQ), Tier 2.

- **Spec classes (its own menu)**: New Product Development; **Retail Pack Specifications** ("for all food types that your business produces, buys or sells… incorporate allergens, additives and nutritional information"; categories: ready meals, retail-packed meat/poultry/seafood, fresh produce, ambient, dairy, canned); **Raw Material Specifications** ("in one location, in a standardised format. Set up custom **reviewal periods** so that you and your suppliers have access to the most up-to-date information"); **Packaging Specifications** ("configure your packaging specification template to include all the information that you need from suppliers… country legislation, chemical legislation, recyclable data"); **Complex Ingredients Specifications** ("full recipe breakdown including **mixing bowl and percentage breakdown of each component part**… standardised format to simplify risk assessments"); **Manufacturing Process Specifications** ("visual storyboards, operative step-by-step guides… change tracking & version control… link to production quality checks").
- **Raw material spec features**: product photos & storyboards; quality & packaging requirements; **sharing with suppliers/customers**; **sign-off tracking**; mobile accessible on factory floor; link to product inspections.
- **FAQ (product-behavior statements)**: "streamlines the creation, **approval**, and management of product specifications"; spec types include "raw materials and ingredients, finished goods, packaging, allergen and nutritional information, **supplier-provided specs**"; "**Suppliers can be invited to input and update specifications directly in the system**… reduces email communication… central record of supplier documentation"; "embedding checks, validations, and approval processes throughout the workflow"; "workflows can be tailored… including **multi-level approvals**, automatic notifications, and user permissions"; integrates with Quality Management, Supplier Management, Traceability modules; benefits include "centralised specification repository… traceability and audit readiness."
- **Suite context**: root site FAQ groups "SAQs, Specs or standards and certifications like BRC…" as supplier-managed-once data; PLM section: "maintain accurate controls on product specifications in real time."

### Specright

Evidence layer: A for this product (official pages), Tier 2. Boundary pole (multi-industry).

- **Category definition (its own words)**: "Specification Management is the process of centralizing **DNA-level product and packaging data — the requirements, standards, and characteristics every product must meet — into a single system of record**… a true source of truth that helps supply chain teams work efficiently, reduce risk, and drive traceability from raw material to shelf."
- **Three spec types (its own taxonomy)**: product specifications ("what a finished good must be — ingredients, dimensions, materials, and performance requirements"); packaging specifications ("how a product is packaged, labeled, and transported"); manufacturing specifications ("processes, tolerances, and instructions"). "In a spec-first supply chain, all three are **linked**, meaning a change in one automatically surfaces its downstream impact on the others."
- **Specification Manager role**: "creating, maintaining, and governing product and packaging specifications… building out spec templates, managing **version control**, coordinating with **suppliers and R&D teams** on spec accuracy, and ensuring specifications stay aligned with **regulatory and quality requirements**."
- **Three problems the platform solves**: (1) lack of common language → "without a templated approach to spec creation, it's challenging to work efficiently"; (2) incomplete data owned by many departments and suppliers → need "a central source of information that updates in real-time to all necessary stakeholders"; (3) inability to share up-to-date information → "sharing specs often occurred via static formats, from emails, to spreadsheets, and even pen and paper."
- **SDM framing**: "goes beyond storing specs to actively **linking** them together… mapped and interconnected, from packaging to ingredients to manufacturing instructions, the data becomes actionable intelligence rather than static documentation." Patented many-to-many relationship structure (vendor claim). "5 million+ products on Specright's SDM platform" (vendor claim, unverified).
- **Modules**: Packaging Management; Product Data Management ("raw materials, ingredients, formulas, recipes, and finished goods"); Supplier Collaboration; R&D Workbench (formulation); Project Management. Industries: food & beverage, beauty, consumer goods, packaging, industrials, life sciences, QSR — **deliberately beyond food**.
- **Failure narrative (ROI report blurb)**: "suppliers using outdated formulas, labels that don't reflect the latest change, or approvals that sit in someone's inbox."

---

## Cross-product Comparison

| Dimension | TraceGains | SpecPDM | Foods Connected | Specright | Reading |
|---|---|---|---|---|---|
| Spec as record of record | specs as controlled digital data, "one trusted platform", single source of truth | material master's structured data (attributes, lab data, declaration) rendered as spec document | "centralised specification repository", standardized format | "DNA-level product and packaging data… single system of record" | **Universal (B)** — the spec-of-record leg |
| Structured data vs document | digitization from "disparate documents" to "secure digital data: indexed, organized, and controlled" | structured tabs → generated report; release-versioned rendering | centralised repository with templates | "beyond storing specs to actively linking them" | Structured-data-of-record with generated document output is the common software realization |
| Spec kinds | ingredients, packaging, finished goods (triad verbatim) | material specs (raw/semi/finished); packaging info & manufacturing instruction sections | retail pack (finished), raw material, packaging, complex ingredients, manufacturing process | product, packaging, manufacturing | Raw-material/ingredient + finished-product + packaging near-universal (B); process specs 2/4 (A each) — common, not definitional |
| Templates & standardization | configurable templates, auto-update of impacted specs | multiple templates saved; unlimited report templates; criteria structure | customisable templates per spec type; "standardised format for all suppliers" | "templated approach to spec creation" as problem #1 fix | **Common mature structure (B)** |
| Versioning & lifecycle | full version history; automated effective-date workflows; "latest approved version and what changed?" | create→validate→release control cycle; processing vs release versions; change index; QA notification on status change; history | creation, approval, multi-level approvals, sign-off tracking, change tracking & version control, reviewal periods | version control; "approvals that sit in someone's inbox" as failure | **Universal (B)** — governance leg; status vocabularies differ (Canonical states must stay conceptual) |
| Trading-partner exchange | supplier collaboration via network; suppliers create/update specs; correspondence tracking | spec report issued with issuer+contacts; multilanguage; Buyer's/Supplier's Guide products; GDSN adjacent | sharing with suppliers/customers; suppliers invited to input/update directly; sign-off tracking | supplier collaboration module; static-format sharing as the pre-digital problem | **Universal (B)** — exchange leg; mechanism varies (network/portal/report/invited editing) |
| Upstream link (formulation) | "connect specs to formulas, items, and supplier data"; separate Formula Management product | recipe/declaration generates the finished material's spec (Tier 1) | NPD recipe development; QUID & nutritional data management; complex-ingredient spec shows component breakdown | R&D workbench module; formulas among managed data | Composition flows into spec (B); formulation as separate product vs module varies |
| Downstream link (labels/quality) | "errors carry into formulation, labeling, and compliance workflows" | spec includes declaration/allergen/additive sections; links to inspection plans | links to product inspections, quality checks, traceability, supplier mgmt | "labels that don't reflect the latest change" as failure; change surfaces downstream impact | Specs feed downstream processes (B); label *generation* machinery NOT in this Type's core |
| Attribute/tolerance structure | "in/out-of-spec tolerance images"; labels, packaging, instructions in templates | LA/MIN/TV/MAX/UA per criterion; tolerance values on nutrients | quality & packaging requirements; food-safety/chemical legislation fields | "requirements, standards, and characteristics"; "processes, tolerances" | Limits/tolerances as first-class spec content (B) |
| Exchange artifact | shared updates, alerts, audit-ready | spec document (PDF/report) per release, multilanguage | shared spec records + sign-offs | connected spec records | The shareable spec document and/or live shared record (B) |
| dashboards/oversight | QA dashboards (customer quote) | reporting module, missing-data visibility | dashboards from supplier responses | real-time visibility for supply chain | Common (B) |
| Network/marketplace of supplier docs | TraceGains Marketplace ("millions of supplier documents") | — | — | — | **Vendor-specific (L3)** |
| NPD/project machinery | separate NPD line | Project module exists in suite | stage-gate workflow manager, Gantt, critical path | Project Management module | Common-but-variant placement (some bundle, some separate) |
| Sustainability data | Carbon Insights (separate) | — | recyclable data in packaging specs | EPR/PPWR/DoC automation | Optional (B, thin) — packaging-regulatory extensions |
| Cross-industry reach | F&B focus | food-focused (also MSDS) | food only | F&B + beauty + industrials + life sciences | Food is the center of gravity; the machinery generalizes (A, one pole) |

## Canonical Model (abstraction)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The specification of record** — a persistent, individually identified, structured statement of what a food material or product *is and requires*: identity and commercial context (supplier/producer/issuer), composition and ingredient/declaration data, measured attributes with limits or tolerances (microbiological, chemical, physical, sensory), nutritional and allergen data, packaging, shelf life and storage, and regulatory/certification status. Held as governed structured data from which the shareable document is produced. Breadth varies by spec kind; the *statement-with-requirements* character is invariant.
2. **The governed approval-and-version lifecycle** — the spec moves through drafting, review/approval, effective release, and revision/supersession under version control, with attributable history, so "the latest approved version and what changed" is always answerable. A spec is a controlled record, not a free document.
3. **Trading-partner exchange** — the spec exists to be shared with and often co-maintained by the counterparties it binds: requested/received from suppliers, issued to customers, collaborated on directly. The system is the sharing surface that replaces email/PDF/spreadsheet circulation.

Load-bearing tests:
- 1 alone = product data sheet generator / PIM-lite
- 2 without 1 = generic document approval workflow
- 3 without 1+2 = file-exchange portal / shared drive
- 1+2 without 3 = internally governed product master data (ERP/PIM territory — the ERP pass showed specs held as internal attributes; the formulation pass's SpecPDM "commit to master data" evidence shows the internal side)
- 1+3 without 2 = spec sheets emailed around (the named pre-digital state)
- 2+3 without 1 = workflow tool with attachments

Historical check (paper era): a manufacturer's specification binder — typed spec sheets with attribute tables and limits, revision numbers and dates, approval signatures, superseded sheets withdrawn; supplier specs requested by letter and filed; spec copies issued to customers with contracts. Satisfies all three legs at analog level (structured statement ≈ tabular typed sheet; lifecycle ≈ revision register + signatures; exchange ≈ post/phone). The 1990s Office/email state (specs as Word/Excel attachments) satisfies legs 1–3 weakly (statement + informal approval + exchange) but is exactly the "static formats" state all four vendors name as the problem. Cloud/template/propagation machinery is standard, not definitional. → **L0 survives the historical check.**

### L1 — Common Mature Structure

- configurable spec **templates** (sections/attributes; standardized formats across suppliers)
- **spec kinds/classes**: raw material/ingredient, packaging, finished product (process specs common but not universal)
- **propagation & linkage**: changing an ingredient/template auto-updates impacted specs; a change surfaces downstream impact; links to items, suppliers, formulas, quality checks
- computed/flowed-in content: nutrition, allergen, declaration data arriving from recipe/formula; percentage thresholds
- limits/tolerances as first-class attribute values (min/max/target/alarm-class semantics)
- version/release rendering: the spec document per release with version, release date, confirmation/signature block
- multilanguage / multi-market spec output
- review/renewal cycles (reviewal periods)
- audit trails, correspondence tracking, sign-off tracking
- oversight dashboards and reporting

### L2 — Variant / Optional

- networked supplier document libraries / spec marketplaces
- NPD/project machinery (stage gates, Gantt, critical path) — bundled or separate
- formulation module inside the platform (vs separate product)
- label generation as a module (vs dedicated labeling platform)
- sustainability/packaging-regulatory extensions (recyclability, EPR/PPWR declarations)
- GDSN/retail master-data synchronization adjacency
- complaint management, MSDS, sample stock (suite extras)
- mobile factory-floor spec access
- AI assistance (Q&A over spec data, AI formulation)
- cross-industry generalization (beauty, industrials, life sciences)

### L3 — Vendor-specific (stays here)

- TraceGains: Gather/Marketplace network scale, Packaging Spec Management as separate SKU, WebCenter Go (artwork), NutriCalc pairing
- SpecPDM: LA/MIN/TV/MAX/UA column vocabulary; Change index vs release version; VAL-I-PAC, RSPO, Swissness tabs; BLS/Ciqual/USDA nutrient databases; %ON <1% exclusion option; Specification Multilanguage report type
- Foods Connected: "Retail Pack" / "Complex Ingredients" class names; "mixing bowl breakdown" concept
- Specright: "Specification Data Management (SDM)" trademark; patented many-to-many structure; "5 million+ products" (unverified vendor claim)

## Vendor-specific Findings

See L3. Additionally: TraceGains' "hundreds of specs instantly" mass-update phrasing is its own marketing claim — capability direction (mass update) is cross-product plausible but the figure is not evidence. Specright's industry breadth shows the machinery is not food-intrinsic; the directory leaf remains food-scoped, and the food-specific content (allergen/declaration/food-law sections) is what makes it the food Type.

## Boundary Findings

1. **vs Food Formulation Platform** (processed): the formula is the composition of record (ingredients + quantities; computed properties; R&D iteration loop). The specification is the formal statement of record (declared attributes/requirements; governed approval; exchanged with partners). Tier-1 SpecPDM evidence: the recipe/declaration *generates* the material's spec data — composition flows into the statement. TraceGains ships them as separate products. Seam: remove the composition-iteration loop and keep the governed statement → spec management; remove the statement/exchange and keep composition → formulation.
2. **vs Food Labeling Platform** (processed): the label is the regulated retail-facing artifact (nutrition panel, ingredient statement, allergen declaration). The spec is the whole technical statement including micro/chem/physical/packaging/storage, and is B2B-facing. A spec *contains* declaration sections (SpecPDM spec report) but label generation machinery (formats, rounding rules, label rendering) is the labeling platform's defining core.
3. **vs Food PLM** (unprocessed sibling — flag): PLM is the lifecycle container (projects, stage gates, artwork); spec management is the product-data core. SpecPage splits SpecPagePLM vs SpecPDM. Foods Connected bundles NPD workflow with specs; Specright pitches "spec-first PLM". Posture gradient; keep both Types, note the seam for the food-plm pass.
4. **vs Food Manufacturing ERP** (processed): the ERP holds specs as operational attributes feeding production and labels; the dedicated Type centers authoring/approval/exchange of the spec record. Coexistence, not duplication.
5. **vs Supplier Quality/Compliance Management (§16)**: supplier compliance centers the supplier's program machinery (certificates, audits, SAQs, non-conformances); spec management centers the product/material's technical statement. Overlap: "supplier-provided specs" arrive as onboarding data (Foods Connected FAQ); TraceGains' supplier management line sits adjacent.
6. **vs PIM**: PIM manages commerce-facing product information for sales channels; spec management manages the technical/regulatory B2B statement. SpecPage's own split (SpecPIM vs SpecPDM) is direct vendor evidence of the seam.
7. **vs Document Management / QMS doc control**: generic controlled-document machinery lacks the product-technical content model (attributes with tolerances, declarations, packaging, shelf life) and the trading-partner spec semantics. SpecPDM's document-control model is the general machinery *applied to* the spec content model.

## Uncertainties

- TraceGains deep operational documentation unreachable → all TraceGains claims stay at the level its product pages state (no workflow internals, no precise limits).
- Effective dating: observed in TraceGains ("automated effective-date workflows") and SpecPDM (release dates, validity periods); treated as common-mature (B), not definitional.
- Process/manufacturing specs: 2/4 products give them first-class status; treat as common-but-optional, do not put the triad into the defining core — the invariant is the spec statement per se, not any particular kind taxonomy.
- E-signature formality: SpecPDM confirmation block (stamp/signature/released-by) vs Foods Connected "sign-off tracking" — depth varies; kept at conceptual level in the final document.
- "Reviewal periods" (scheduled spec re-review) observed in one product explicitly; likely common but recorded as common-mature with one explicit A-source.
- Whether buyers "request" specs via the platform as a tracked workflow (vs suppliers pushing specs) — Foods Connected and TraceGains evidence supplier-directed collaboration; a formal tracked "spec request" object is plausible but not directly evidenced; kept out of the final document's rule claims.

## Final Synthesis

Food Specification Management is the manufacturer-side system of record for the **product specification** — the formal, structured, governed statement of what a food material or product is and requires — moved through an approval-and-version lifecycle and exchanged with the trading partners the statement binds (suppliers upstream, customers downstream). Its content model spans identity/commercial context, composition and declaration data, measured attributes with limits, nutrition/allergen data, packaging, shelf life/storage, and regulatory status; its governance model is creation→validation→release with versions and effective dating; its exchange model replaces email/PDF/spreadsheet circulation with networks, portals, invited editing, and generated, versioned spec documents. Upstream it consumes composition (formula/recipe data flows in); downstream it feeds labels, quality checks, and production systems. The Type holds as an independent leaf: the composition/statement seam with formulation, the label-artifact seam with labeling, and the ERP/PIM/internal-master-data seams all held under direct evidence.
