# Research Notes — Sustainable Procurement Platform

Research date: **2026-09-10**

## Research Goal

Understand what the market actually sells under the "Sustainable Procurement" label: what the system centers on, which procurement decision points sustainability is embedded into, how criteria/data/improvement relate, and where the boundary sits against the already-processed §21 siblings (supplier-sustainability-management, scope-3-management-platform) and the processed §10 procurement Types (e-sourcing, procurement-management, procure-to-pay, supplier-management, supplier-risk, spend-analysis, government-procurement).

Duties this pass:

- Discharge the forward flag left by the scope-3-management-platform pass (procurement decision-making orientation vs emissions-account-and-engagement orientation).
- Discharge the joint-review flag left by the supplier-sustainability-management pass (sourcing-decision orientation vs standing-program orientation; IntegrityNext packages "Sustainable Procurement" as a distinct solution; EcoVadis program guidance stresses integrating ratings into procurement decisions).

## Initial Boundary

Working hypothesis before research:

- Core purpose: the buying organization's system for making sustainability (environmental, social, ethical) a criterion and constraint inside its procurement decisions — supplier qualification, tenders/sourcing events, award, contracting, in-life supplier reviews, and purchasing choices.
- Likely users: procurement/category managers, sourcing and buyer roles, supplier-quality/sustainability teams supporting them; suppliers on the other side.
- Nearest neighbors: Supplier Sustainability Management (§21), Scope 3 Management Platform (§21), E-sourcing Platform (§10), Procurement Management Platform (§10), Procure-to-pay Platform (§10), Supplier Management Platform (§10), Supplier Risk Management (§10), Spend Analysis Platform (§10), Government Procurement Platform (§24), ESG/Sustainability Management Platforms (§21).
- Known unknowns: Is there a distinct system-of-record object (criteria/policy layer? decision-chain configuration?), or is "sustainable procurement" just a solution label spanning the sibling Types and the sourcing suites? Does the improvement loop belong in the definition? Where does the public-sector GPP (green public procurement) practice fit? Does supplier diversity belong?

## Research Questions

1. What do products sold under "sustainable procurement" actually center on: the procurement decision flow, the supplier's sustainability standing, or a program?
2. Where do sustainability criteria live and how are they applied: policy/expectations, category-level goals, evaluation criteria/weightings, thresholds, targets?
3. Which procurement decision points are touched: qualification/pre-qualification, tendering/RFx, award, contracting, in-life reviews, purchasing/discovery?
4. Where does the supplier sustainability information come from: the buyer's own assessments, third-party rating networks, data enrichment, continuous monitoring?
5. What improvement machinery exists (corrective actions, development plans, targets) and is it definitional or common?
6. Who operates it day-to-day (procurement vs sustainability roles), and how is it packaged (standalone platform vs suite module vs solution inside a broader platform)?
7. Where are the boundaries vs supplier-sustainability-management, scope 3, e-sourcing/sourcing suites, and the other §10 procurement Types?
8. Would the pre-software discipline (ISO 20400-class guidance, paper-era green public procurement) satisfy the definition (historical check)?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer layers:

| Product | Philosophy / pole |
|---|---|
| EcoVadis | Third-party sustainability rating network; buyer-side "Sustainable Procurement" program = assessments + ratings integrated into procurement processes and decisions |
| IntegrityNext | Supply-chain sustainability platform packaging "Sustainable Procurement" as a distinct solution: ESG data/assessments embedded across the procurement lifecycle stages |
| JAGGAER | Procurement (source-to-pay) suite embedding ESG criteria into its own sourcing/award/category machinery — the suite pole |
| SAP | "Sustainable procurement" as an outcome area of the spend-management portfolio, delivered through Ariba modules + third-party partners — the portfolio/outcome pole |
| Supplier.io | Supplier-data/intelligence provider: sustainable procurement = discovery/vetting of sustainable suppliers + sustainable-spend goals — the data-and-discovery pole |

## Sources

- EcoVadis (Tier 1 help center + Tier 2 product pages):
  - Setting up a successful sustainability program with EcoVadis — https://support.ecovadis.com/hc/en-us/articles/360015860112 (fetched 2026-09-10)
  - Enterprise page ("Embed Sustainability Into Every Procurement Decision") — https://ecovadis.com/enterprise (search capture, 2026-09-10)
  - Homepage / platform positioning — https://ecovadis.com/ (search capture, 2026-09-10)
  - Integrating Sustainability in Procurement Processes (training description) — https://resources.ecovadis.com/ecovadis-solution-materials/integrating-sustainability-procurement-processes (search capture, 2026-09-10)
  - Making Sustainable Purchasing the Easy Choice at Scale (Amazon Business integration webinar page) — https://resources.ecovadis.com/webinars/making-sustainable-purchasing-the-easy-choice-at-scale (search capture, 2026-09-10)
  - Buyer solutions page (legacy marketing mirror) — https://ecovadis.webflow.com/buyer-solutions (search capture, 2026-09-10)
  - Help-center search page returned JS-rendered empty content on direct fetch; Tier-1 depth limited to the program-setup article.
- IntegrityNext (Tier 2, official solution page, fetched 2026-09-10):
  - Sustainable Procurement solution — https://integritynext.com/sustainable-procurement
  - Platform overview — https://integritynext.com/platform (search capture)
- JAGGAER (Tier 2, official product pages + official ESG report PDF, 2026-09-10):
  - ESG Intelligence — https://www.jaggaer.com/solutions/esg-intelligence (search capture)
  - Sourcing — http://jaggaer.com/solutions/sourcing (search capture)
  - JAGGAER 2024 ESG Report (PDF) — https://www.jaggaer.com/wp-content/uploads/JAGGAER-2024-ESG-Report.pdf (search capture)
- SAP (Tier 2, official product page, fetched 2026-09-10):
  - Sustainable Procurement — https://www.sap.com/products/spend-management/sustainable-procurement-software.html
- Supplier.io (Tier 2, official pages, fetched 2026-09-10):
  - Homepage — https://supplier.io/
  - Supply chain sustainability software (sustainable procurement solution) — https://supplier.io/solutions/supply-chain-sustainability-software/
- ISO 20400:2017 Sustainable procurement — Guidance (Tier 1 standard record, 2026-09-10):
  - https://www.iso.org/standard/63026.html ; OBP excerpt https://www.iso.org/obp/ui#iso:std:iso:20400:ed-1:v1:en

Sourcing limitations: no Tier-1 help-center depth was reachable for the suite pole (SAP help portal is a JS shell per prior passes; JAGGAER evidence is product pages + its own ESG report). EcoVadis Tier-1 evidence is limited to the program-setup article (search page JS-rendered). Precise operational details (exact weighting mechanics, exact gate behaviors, numeric thresholds) are therefore not asserted anywhere in this pass.

## Product Observations

### EcoVadis (rating network; buyer-side sustainable procurement program)

Key observations (evidence layer A unless noted):

- The buyer-side engagement is framed as a **sustainability program run by/for the procurement organization**: EcoVadis commits to the platform, supplier onboarding management, reliable data, supplier support, a dedicated account manager and quarterly steering committees; the buyer is expected to provide clean supplier data and quarterly assessment capacity planning, inform suppliers before campaigns, follow up on non-responders, incentivize long-term improvement, **"consistently integrate EcoVadis sustainability data in the existing procurement processes"**, and designate a program manager with quarterly steering committees including procurement leadership (Tier 1, program-setup article).
- Program success factors named by the vendor: **Communication** ("how you will integrate the results into your procurement decisions"); **Processes** ("clear and transparent rules for selecting the trading partners to be rated and integrates the EcoVadis Rating into procurement processes" — onboarding approach by procurement categories/locations/divisions, campaign frequency and volumes, functions involved such as lead buyers and internal compliance, incentives; **sustainability performance targets for trading partners**, e.g. reaching a defined performance level or working a corrective action plan); **Organization** (centralized coordination, C-level sponsorship, procurement-team support) (Tier 1).
- Enterprise positioning: "Embed Sustainability Into Every Procurement Decision — access analyst-validated sustainability ratings… identify high and low performing suppliers… **inform sourcing and decisions with benchmarked sustainability performance**… continuous improve with Corrective Action Plans and supplier training" (Tier 2, enterprise page).
- A customer procurement lead states the rating "is 30% of our overall vendor rating" — sustainability data as a weighted input in vendor evaluation (Tier 2, marketing quote; treated as illustrative).
- Training material maps "the EcoVadis platform features to your daily procurement processes such as RFPs, supplier reviews or market watch" (Tier 2).
- A B2B-purchasing integration embeds ratings "directly into the purchasing workflow… into the search filters" of a large business store, so buyers filter everyday purchases by supplier sustainability rating (Tier 2, webinar page).
- Legacy solution page describes the "EcoVadis Sustainable Procurement solution" as "turnkey supplier CSR/sustainability assessment, rating, risk and performance management… smoothly integrated in your procurement processes", with scorecards benchmarked "within the same purchasing category or within the same country" (Tier 2/3, legacy mirror).

### IntegrityNext (supply-chain sustainability platform; "Sustainable Procurement" as a packaged solution)

Key observations (evidence layer A — official solution page fetched directly):

- The solution's own framing: "Embed flexible assessments, seamless integration of ESG data and full supplier coverage into procurement workflows… everything procurement needs to embed sustainability into decision-making."
- Three named procurement workflows: **Supplier Pre-Qualification & Discovery** ("assess and onboard suppliers based on ESG criteria and compliance readiness from the start"); **Supplier Risk & Performance Management** ("continuously evaluate supplier-specific ESG risks, benchmark sustainability performance"); **Supplier Development & Capacity Building** ("structured training, practical tools, and targeted actions" — the vendor's Academy).
- The lifecycle-stage model is explicit — "Embed Sustainability Into Every Stage of the Procurement Lifecycle":
  - **Tendering** — inform suppliers early about ESG expectations; reference the platform in tender invitations so suppliers are prepared for ESG assessments and disclosure.
  - **Pre-Qualification** — screen suppliers for ESG readiness before engagement; use assessments to identify high-risk or non-compliant suppliers during pre-screening or initial qualification.
  - **Supplier Selection & Awarding** — "use ESG assessment results and risk insights as evaluation criteria to guide award decisions aligned with sustainability priorities."
  - **Contracting** — "include ESG assessment requirements, improvement plans, or risk thresholds directly in supplier contracts."
  - **Supplier Relationship Management** — ongoing ESG data, automated risk alerts, AI-powered news tracking to flag issues between assessments.
  - **Procurement Performance & Governance** — "integrate ESG criteria into supplier scorecards, quarterly reviews, and corrective action workflows — ensuring sustainability becomes business-as-usual."
- Configuration follows the buyer's procurement strategy: "Tailor risk severity, assessment topics, supplier engagement and more based on your procurement strategy and **category-specific ESG goals**."
- Integration is a first-class surface: "Integrate ESG risk and compliance insights directly into ERP, SRM, and supplier management systems"; ready-made connectors to e-sourcing/ERP tools (SAP Ariba, Coupa named in integration graphics) plus APIs — "ensure procurement teams have the latest ESG scores and supplier risk data embedded directly into their day-to-day tools."
- Supplier-side machinery: multilingual assessment surveys, a pre-onboarded supplier network (2M+ profiles claimed), corrective actions assigned to suppliers with progress tracking, e-learning Academy.
- Customer role evidence: "Head of Sustainable Procurement" as a buyer-side job title (ACCIONA Infrastructures quote about pre-qualification/assessment automation).

### JAGGAER (procurement suite pole)

Key observations (evidence layer A for its own pages/report; Tier 2):

- ESG Intelligence solution: "Gain ESG visibility across the entire Source-to-Pay process with unified supplier data in one centralized, actionable hub… consolidates emissions, risk scores, certificates and more to support smarter, compliant decisions."
- Procurement-led framing: "Let Procurement Lead Your ESG Transformation — by **pricing carbon in decisions, rewarding responsible suppliers**, and improving transparency, procurement becomes the central force in meeting ESG goals."
- Sourcing page: "Integrate ESG, Risk, and Compliance into Sourcing Decisions — buyers embed ESG, risk, and compliance considerations into both direct and indirect sourcing processes… gather critical information through questionnaires or by automatically pulling data directly from supplier profiles, enhanced by third-party intelligence. This ensures smarter, more **responsible awarding decisions**."
- The vendor's own ESG report describes the capability set concretely: "Embedding Sustainability Into Every Sourcing Decision — organizations embed ESG criteria directly into sourcing processes. From supplier certifications to workforce representation and emissions per unit metrics…"; scenario modeling lets teams "weigh carbon pricing, governance risks, and social value alongside traditional cost and performance metrics." Sourcing-stage bullets: "Embed ESG questions and scoring into RFI/RFQ processes"; "Evaluate suppliers during negotiations based on sustainability criteria (e.g., EV usage, carbon impact)"; "Filter and block unqualified suppliers using real-time supplier intelligence"; ESG scenario modeling in the Advanced Sourcing Optimizer for transportation/packaging decisions; "Understand the commercial impact and costs of your ESG related procurement policies."
- Category management carries the goals layer: "Set ESG goals — from improving compliance to driving sustainable innovation… Embed actionable sustainable strategies across your supply chain using Category Management. When supplier performance falls short, **automated development plans are triggered**."
- Data layer: standardized ESG questionnaires sent to suppliers; an "actionable ESG data lake" across suppliers through the procurement lifecycle.

### SAP (portfolio/outcome pole)

Key observations (evidence layer A for its own page; Tier 2, thin):

- Framing: "Reach your procurement and sustainability goals by transitioning from **price-driven procurement to sustainable procurement**."
- The outcome area is delivered through portfolio modules plus partners, not a standalone product: track Scope 3 emissions from suppliers (regulation-driven); "conduct human rights due diligence — assess suppliers via questionnaires, **enforce ESG obligations with SAP Ariba Contracts**, and use third-party partners such as EcoVadis to manage risks and support sustainability"; respond to deforestation regulation with product-traceability tooling, Ariba Supplier Risk, and partners.
- Interpretive care: SAP's page is an umbrella over Ariba sourcing/supplier/contract modules + partner integrations; it corroborates that "sustainable procurement" is a recognized solution category at the suite level, but provides no operational depth (no workflow mechanics asserted from this page).

### Supplier.io (data-and-discovery pole)

Key observations (evidence layer A for its own pages; Tier 2):

- The "sustainable procurement" solution is framed around supplier discovery and vetting: "Sourcing sustainably is difficult when supplier sustainability data is self-reported and hard to verify. We help you **search, find, vet, and onboard credible suppliers** with industry-leading data and tools."
- Solution page: "Track supplier sustainability data, certifications, and environmental ratings in one place to make **confident sourcing decisions** and deliver accurate reports to your stakeholders"; "Find the right suppliers — discover and vet sustainable suppliers using up-to-date information, including CDP scores, Scope 3 emissions, and more."
- Sustainable-spend goals: "Track, analyze, and report your spend with small, diverse, and sustainable suppliers down to the business unit level. **Set clear goals, monitor progress** in dashboards."
- Data layer: supplier records enriched with "certifications, sustainability ratings, GHG emissions metrics… from over 450 trusted sources, including BCorp, EcoVadis, and Fair Trade"; CDP partnership for climate scores and science-based targets; carbon analytics for Scope 1/2/3 visibility; benchmarking against peers.
- The FAQ defines the category from the data seat: supply-chain sustainability software "centralizes ESG… information, such as supplier certifications, to **support sustainable sourcing decisions**."
- Note: supplier diversity is a co-equal dimension in this vendor's framing (diverse + sustainable + small suppliers), illustrating the breadth of "sustainability" criteria in the US market.

### ISO 20400:2017 (discipline anchor, historical check)

- "Provides guidance to organizations, independent of their activity or size, on **integrating sustainability within procurement**, as described in ISO 26000. It is intended for stakeholders involved in, or impacted by, **procurement decisions and processes**." (Tier 1, standard record)
- OBP excerpt: principles and core subjects of sustainable procurement; managing risks; "addressing adverse sustainability impacts through due diligence, setting priorities, **exercising positive influence**…"
- Interpretation: the discipline predates the current software wave and is defined by integration into procurement policy/strategy/processes — not by any specific tool mechanism. This anchors the historical check: a paper-era green-public-procurement process (environmental criteria written into tender documents, weighted in award) satisfies the criteria+decision structure with no modern machinery.

## Cross-product Comparison

| Dimension | EcoVadis | IntegrityNext | JAGGAER | SAP | Supplier.io |
|---|---|---|---|---|---|
| Centered object | ratings integrated into procurement processes/decisions via a managed program | ESG data/assessments embedded across procurement lifecycle stages | ESG criteria embedded in the suite's sourcing/award/category machinery | outcome area over Ariba modules + partners | sustainable-supplier discovery/vetting + sustainable-spend goals |
| Buyer criteria layer | rules for whom to rate; performance targets for suppliers; rating as weighted vendor-rating input | category-specific ESG goals; tailored risk severity/topics; contract thresholds | ESG goals in category management; ESG questions/scoring in RFx; policy cost impact | ESG obligations enforced in contracts | sustainable/diverse spend goals |
| Qualification gate | rules for selecting partners to rate | pre-qualification screening for ESG readiness | filter/block unqualified suppliers | supplier risk/questionnaires | vetting before onboarding |
| Tender / RFx | RFPs named as integration surface | tendering stage (early ESG expectations) | ESG questions + scoring in RFI/RFQ; sustainability criteria in negotiations | — | — |
| Award decision | ratings inform sourcing decisions | ESG results as evaluation criteria guiding award | "responsible awarding decisions"; scenario modeling with carbon pricing | — | — |
| Contracting | — | ESG requirements/improvement plans/risk thresholds in contracts | — | ESG obligations enforced with Ariba Contracts | — |
| In-life review | supplier reviews; benchmark by purchasing category | scorecards, quarterly reviews, corrective-action workflows | development plans triggered on shortfall | ongoing supplier risk | progress dashboards |
| Discovery / purchasing | ratings in B2B purchasing search filters (integration) | supplier discovery on ESG criteria | — | — | search/filter 20M+ supplier database on sustainability attributes |
| Data sourcing | own assessment network (shared scorecards) | own surveys + 2M+ network + AI monitoring | own questionnaires + supplier profiles + third-party intelligence | questionnaires + partners (EcoVadis) | enrichment from 450+ sources (incl. EcoVadis, CDP) |
| Improvement loop | corrective action plans + targets + training | corrective actions + Academy capacity building | automated development plans | via partners | weak (program growth/benchmarking) |
| Sustainable spend tracking | program metrics | — | — | — | first-class (goals, dashboards, benchmarking) |
| Carbon | one topic (Carbon Scorecard/CAM) | one solution family | one input (carbon pricing in scenarios; Scope 3 insights) | one outcome (Scope 3 tracking) | one dataset (carbon analytics) |
| Host form | standalone platform + integrations | standalone platform + integrations | module inside S2P suite | portfolio area of spend management | standalone data platform + integrations |

Reading of the comparison:

- All five products exist to put **sustainability into the buyer's procurement decisions** — none centers the purchase transaction itself (that is the P2P suite's job) and none centers the supplier's standing record as such (that is the sibling's job).
- All five carry a **buyer-defined criteria/expectations layer** (targets, category goals, evaluation criteria, contract obligations, spend goals) — the normative content without which the data has no decision meaning.
- All five carry **decision-ready supplier sustainability information** — sourced from the vendor's own assessment network, the buyer's own questionnaires, third-party enrichment, or monitoring.
- The **improvement loop** is present as real machinery in four of five (EcoVadis CAP/targets, IntegrityNext actions/Academy, JAGGAER development plans, SAP via partners) and reduced to program-growth tooling in the fifth (Supplier.io). It is the dominant mature structure, not the recognition condition: a criteria+decision product without it (paper-era GPP practice; a pure pre-qualification gate) is still recognizably sustainable procurement.
- Carbon appears everywhere as **one input/topic among several** — the emissions account of record is absent from every sampled product (consistent with the scope-3 pass's prediction).
- The market packages the label across three host forms: standalone sustainability platforms with a procurement solution (EcoVadis, IntegrityNext), procurement suites with embedded sustainability (JAGGAER, SAP), and data providers with a sustainable-sourcing solution (Supplier.io).

## Canonical Model

### L0 — Defining Invariant

The Sustainable Procurement Platform is the buying organization's system for embedding sustainability into its procurement decisions. Three jointly-held structures:

1. **The buyer's sustainability requirements for purchasing, held as an operational layer** — the expectations, criteria, thresholds and targets the organization attaches to its buying (supplier sustainability expectations/codes, category-level ESG goals, evaluation criteria and weightings, performance thresholds, contract obligations, sustainable-spend goals). This is what makes the sustainability content *normative* for this buyer's decisions rather than merely displayed. Remove → a criteria library / policy documents, or a generic sourcing tool with an unused ESG field.

2. **Decision-ready supplier sustainability information** — curated, comparable sustainability data about suppliers (assessment results/ratings, certificates, risk signals, emissions figures) assembled from the buyer's own collection, third-party rating networks, data enrichment, or continuous monitoring, and maintained so it can be applied at decision time. Remove → a policy layer with nothing feeding it, or a raw data feed.

3. **The procurement decision points where requirements meet information** — the embedding of the information into the actual decision moments of the buying cycle: supplier qualification/pre-qualification gates, tender/sourcing-event evaluation (ESG questions, scoring, weighting), award decisions, contracting (sustainability obligations/thresholds), in-life supplier reviews/scorecards, and (in some poles) supplier discovery/purchasing search. Remove → the sibling Type's standing program (data + improvement with no decision embedding), or a score display that is an integration rather than a platform.

Jointly-held load-bearing test:

- 1 alone = policy documents / criteria library
- 2 alone = supplier sustainability data store (sibling territory)
- 3 alone = sourcing workflow machinery with an empty sustainability field
- 1+2 without 3 = supplier-sustainability-management (standing program: criteria + data + improvement, decisions only downstream)
- 1+3 without 2 = criteria configured at decision points with no decision-ready data
- 2+3 without 1 = sustainability scores displayed at decision points — an integration, not a platform

### L1 — Common Mature Structure

- **Procurement-leveraged supplier improvement loop** — corrective actions, development plans/capacity building, improvement targets tracked against the commercial relationship, outcomes feeding back into future decisions and program goals (4/5 sampled; the dominant mature structure).
- **Integration into the procurement system landscape** — ESG scores/risk data pushed into ERP/SRM/e-sourcing tools (APIs, connectors) so buyers see sustainability in their day-to-day surfaces.
- **Program machinery** — supplier onboarding/campaign management, coverage planning, steering/governance routines, program KPIs.
- **Sustainable-spend measurement** — spend with sustainable/diverse suppliers tracked against goals, benchmarked.
- **Risk monitoring between assessments** — news/controversy monitoring, alerts.
- **Supplier-facing surfaces** — assessments/questionnaires, action workspaces, e-learning/academy.
- **Benchmarking** — supplier performance vs purchasing category / country / industry peers.

### L2 — Variant / Optional Structure

- **Host form**: standalone sustainability platform with a procurement solution vs procurement-suite module vs data-provider solution.
- **Decision-coverage depth**: full lifecycle embedding (tender→award→contract→SRM→governance) vs sourcing-event focus vs program/ratings focus vs discovery/spend focus.
- **Criteria breadth**: environmental-only (GPP-style) vs full ESG vs ESG + supplier diversity (US market pattern).
- **Public-sector GPP variant**: sustainability criteria mandated in public solicitations — the public/ruled solicitation machinery belongs to the Government Procurement Platform; the criteria layer is this Type's variant context.
- **Regulatory regimes** (CSDDD/LkSG/UFLPA/EUDR/CBAM-class): current realizations driving adoption, not definitional.
- **Carbon depth**: from a scored topic to carbon-priced sourcing scenarios; the emissions account of record belongs to the carbon/scope-3 Types.

### L3 — Vendor-specific (research notes only)

- EcoVadis: 21-indicator/4-theme scorecard vocabulary; medals/badges; scorecard validity period; CAP mechanics (scorecard-based vs general improvement requests); Amazon Business purchasing-filter integration; benchmark by purchasing category or country; "EcoVadis rating = 30% of overall vendor rating" customer configuration.
- IntegrityNext: 2M+ pre-onboarded supplier network; AI Intelligence Layer (sentiment analysis, smart prioritization); Academy; Verdantix/Gartner analyst positioning; named lifecycle-stage packaging.
- JAGGAER: Advanced Sourcing Optimizer ESG scenario modeling; JAI AI branding; ESG data lake; automated development-plan triggers in Category Management; "pricing carbon in decisions" framing.
- SAP: Ariba module names (Contracts, Supplier Risk); SAP Green Token; partner-ecosystem delivery (EcoVadis, IntegrityNext webinars); "price-driven → sustainable procurement" positioning.
- Supplier.io: Atlas entity-resolution platform; Trust IQ; 450+ data sources; CDP partnership; Tier 2 spend reporting; economic-impact modeling.

## Vendor-specific Findings

(Consolidated from L3 — none of these enter the canonical document as definitional.)

- EcoVadis runs the improvement loop through scorecard-derived corrective action plans plus buyer-set supplier performance targets — the program article makes target-setting an explicit success factor.
- IntegrityNext is the clearest market witness for the leaf: it packages "Sustainable Procurement" as a distinct solution with a named six-stage procurement-lifecycle model, beside its due-diligence/standing solutions.
- JAGGAER witnesses the suite pole: ESG criteria live inside the sourcing event machinery (RFx scoring, supplier filtering/blocking, award scenarios) rather than in a separate sustainability product.
- SAP witnesses the portfolio pole: "sustainable procurement" is sold as an outcome area assembled from modules + partners, with no standalone product.
- Supplier.io witnesses the data pole: sustainable procurement as verified-data discovery/vetting plus sustainable-spend goal tracking, with the improvement loop essentially absent.

## Rejected Findings

- "Sustainable procurement = supplier sustainability management with a different name" — rejected; the centered object differs (procurement decision chain vs supplier standing of record), and the market packages them as distinct solutions (IntegrityNext) or distinct program phases (EcoVadis program setup vs process integration).
- "Sustainable procurement = a sourcing-suite feature only" — rejected; standalone platforms and data providers sell the label outside any suite.
- "Sustainable procurement = green/carbon purchasing only" — rejected; human rights, ethics, labor, and supplier diversity are all in-sample criteria content.
- "The improvement loop is definitional" — rejected; criteria+decision products without a systematic loop (GPP-style practice; pure pre-qualification gates) remain recognizable; the loop is the dominant mature structure (4/5) but not the recognition condition.
- "Sustainable spend reporting is definitional" — rejected; first-class only at the data pole (Supplier.io), program-level elsewhere or absent.
- "Public-sector GPP is a separate Application Type" — not supported; the public solicitation machinery is the Government Procurement Platform's center; GPP functions here as a regulatory/sector variant of the criteria layer.

## Boundary Findings

**vs Supplier Sustainability Management (§21, processed) — joint-review flag DISCHARGED; keep-both RATIFIED.** Seam = the centered object, exactly as that pass proposed. There: the supplier's sustainability standing of record (per-supplier assessments/scores/certificates/audit findings accumulating across cycles) + the two-sided collection/assessment loop + the corrective-action loop; procurement decisions are downstream consumers of outcomes. Here: the procurement decision chain itself (requirements → qualification → tender → award → contract → in-life review) with sustainability embedded at each point; supplier sustainability information is an input layer, often sourced from third-party networks or from the sibling Type's outputs. Overlap zone confirmed as predicted: supplier data collection, scorecards, and corrective actions appear in both. Corroboration: IntegrityNext sells "Sustainable Procurement" as a distinct solution beside its standing/due-diligence solutions; EcoVadis separates program setup (sibling territory) from "integration into procurement processes and decisions" (this territory). Removal tests hold both directions: strip the decision-point embedding → the sibling remains; strip the standing-of-record center and keep the decision chain + criteria → this Type remains.

**vs Scope 3 Management Platform (§21, processed) — forward flag DISCHARGED; keep-both RATIFIED.** Seam = object of work, as that pass proposed. There: the value-chain emissions account + counterpart data collection + engagement loop serving the account. Here: carbon is one decision input among several (carbon-priced sourcing scenarios, carbon analytics datasets, Scope 3 tracking as an outcome) — the account-of-record framing is absent from every sampled product here. Removal tests hold: strip the decision embedding → scope-3's program remains; strip the account → this Type remains.

**vs E-sourcing Platform (§10, processed) — keep-both.** E-sourcing centers the sourcing event as a bounded competition (RFx machinery, sealed bids, calendars). Here sustainability is the criteria/data layer applied at decision points; the sourcing event is one host surface among several (JAGGAER embeds ESG scoring INTO its sourcing module; EcoVadis/IntegrityNext/Supplier.io carry no RFx competition machinery at all and remain the Type). An e-sourcing platform without sustainability criteria remains e-sourcing.

**vs Procurement Management Platform / Procure-to-pay Platform (§10, processed) — keep-both.** Those center the managed purchase operation (supplier base, governed demand, PO lifecycle, approval/policy enforcement, payable chain). Here the center is the sustainability criteria/data in the decision flow, not the purchase transaction. SAP's own packaging corroborates: sustainable procurement is an outcome area delivered *through* the spend-management modules + partners.

**vs Supplier Management Platform (§10, processed) — keep-both.** The supplier of record + commercial lifecycle there; the sustainability decision layer here. Consistent with that pass's reading of sustainability as one qualification domain inside supplier management.

**vs Supplier Risk Management (§10, processed) — keep-both.** Risk lens (threat evaluation, continuous monitoring, disposition) vs sustainability-criteria lens (requirements, embedding, improvement). The Prewave dual-recognition straddle was ratified at the sibling pass; not re-litigated here. IntegrityNext's risk alerts/news monitoring sit in this Type as decision-support inputs, not as a risk-disposition center.

**vs Spend Analysis Platform (§10, processed) — keep-both.** Spend analysis centers consolidated multi-source spend classification/analytics; sustainable-spend tracking here is a program KPI capability (goals, dashboards) feeding procurement decisions, not the analytical center.

**vs Government Procurement Platform (§24, processed) — variant note, no conflict.** Public-sector green public procurement embeds environmental criteria into public solicitations; the public/ruled solicitation machinery is the GPP Type's center. When the buyer is public, this Type's criteria layer operates as a variant context inside that machinery. No directory change.

**vs ESG/Sustainability Management Platforms (§21, processed) — keep-both, consistent with sibling passes.** Those center the organization's own program data and disclosures; this Type centers sustainability in the organization's buying decisions. Supplier sustainability data feeds both.

**vs Strategic Sourcing Platform (§10, unprocessed) — forward flag.** The market uses "strategic sourcing" and "sourcing" interchangeably with e-sourcing (per the e-sourcing pass's joint-review flag). When that pass runs, it should hold the same seam struck here vs e-sourcing: sourcing-event machinery vs sustainability decision layer; suite-embedded ESG scoring (JAGGAER-class) will be the overlap specimen.

## Historical / Market-Sample Check

- ISO 20400:2017 (guidance standard, confirmed current) defines the discipline as integrating sustainability within procurement policy/strategy/processes, addressed to "stakeholders involved in, or impacted by, procurement decisions and processes" — predating the current software wave and naming no tool mechanism.
- Paper-era green public procurement (environmental criteria written into tender documents and weighted in award decisions) satisfies structures 1+3 with no modern machinery; supplier questionnaires and file-based evidence satisfy structure 2.
- The improvement loop, integrations, AI monitoring, and supplier networks are era-current additions and are kept out of the definition (L1/L2).
- Conclusion: the definition holds at class level across eras; the L0 does not over-fit to the current cloud/AI implementation.

## Uncertainties

- No Tier-1 help-center depth for the suite pole (SAP help portal JS-shell per prior passes; JAGGAER at product-page + own-ESG-report level). Precise mechanics of how suites weight ESG criteria in award calculations are not asserted.
- EcoVadis help-center search was JS-rendered; Tier-1 evidence limited to the program-setup article. The exact mechanics of EcoVadis's procurement-integration features (e.g., RFP-attachment workflows) are not asserted.
- The discovery/purchasing pole (sustainability at the point of everyday purchase — Supplier.io search, Amazon Business filters) is thinner in evidence; treated as a variant surface, not a defining decision point.
- Supplier.io's improvement-loop absence rests on its public pages; a deeper help center could reveal action tooling. The L1 (not L0) placement of the improvement loop is robust to this either way.
- The exact boundary vs the unprocessed strategic-sourcing-platform leaf is flagged, not resolved.

## Final Synthesis

The market sells "Sustainable Procurement" as the buying organization's system for making sustainability operational inside its procurement decisions. The recognizable core is three jointly-held structures: the buyer's sustainability requirements for purchasing (criteria/goals/thresholds/targets held as an operational layer), decision-ready supplier sustainability information (from own collection, third-party networks, enrichment, or monitoring), and the procurement decision points where the two meet (qualification gates, tender/RFx evaluation, award, contracting, in-life reviews, discovery). The procurement-leveraged improvement loop is the dominant mature structure but not the recognition condition. The Type is distinct from supplier-sustainability-management (standing-of-record center) and from scope-3 management (emissions-account center) while sharing data machinery with both; it is distinct from the §10 sourcing/procurement Types (which own the event/transaction machinery this Type embeds into). Both inherited forward flags are discharged as keep-both ratifications.
