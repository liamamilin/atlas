# Research Notes — Nature Risk Management

Research date: 2026-09-09

## Research Goal

Understand what a **Nature Risk Management** application actually is, from real products: what objects exist inside it, what users do with it, how the assessment work flows, what rules and states matter, and where its boundary sits against neighboring Types (Climate Risk Management, Natural Capital Management, Biodiversity Management, ESG platforms, ERM).

## Initial Boundary

Initial hypothesis (before research):

- Core use: identify, assess, prioritize, and manage an organization's **nature-related risks** — risks arising from its **dependencies on ecosystem services** (water, pollination, flood regulation, raw materials, soil) and its **impacts on nature** (biodiversity loss, land/water use, pollution), which manifest as physical, regulatory, reputational, and market risks.
- Likely shaped by the TNFD framework (LEAP: Locate, Evaluate, Assess, Prepare) and by disclosure regimes (CSRD/ESRS E4, GRI 101, SFDR).
- Nearest neighbors: Climate Risk Management / Physical Climate Risk Platform (same structural shape, different hazard domain), Natural Capital Management (measurement/accounting-centric), Biodiversity Management (strategy/action-centric), ESG Management Platform (generic multi-topic), Enterprise Risk Management (generic risk register).
- Unknowns: is the market reality a *management* system (registers, response plans, monitoring) or a *screening/assessment analytics* toolset? Is portfolio (financial-institution) use definitional or a variant? Is monetary valuation definitional?

## Research Questions

1. What is the central object — a risk, a location, a dependency/impact, a portfolio?
2. What is the canonical workflow (screen → assess → prioritize → respond → disclose)?
3. What data substrate do these products share (protected areas, species, ecosystem condition, water, ecosystem services)?
4. Who uses it (corporate sustainability, risk, financial institutions) and what interfaces do they see?
5. How does the TNFD LEAP shape the workflow — and is the Type dependent on TNFD?
6. What separates this Type from climate risk, natural capital accounting, biodiversity management, and generic ESG/ERM?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Role in sample |
|---|---|---|
| IBAT (Integrated Biodiversity Assessment Tool) | Conservation-NGO alliance subscription; authoritative biodiversity data + screening | data/screening pole; corporate + project-finance lineage |
| WWF Biodiversity Risk Filter | Conservation NGO free public tool | free corporate/portfolio screening pole; explicit risk typology |
| NatureAlpha (Geoverse) | Commercial AI/geospatial analytics for investors | analytics/score pole; financial-market orientation |
| GIST Impact | Commercial impact-data platform (nature one pillar) | impact-data/valuation pole; data-delivery orientation |

Deliberately excluded after sampling attempts: ENCORE (original domain taken over by an unrelated gambling site — see Sources), S&P Global Sustainable1 (403), tnfd.global (403 — framework treated as context, not a sampled product).

## Sources

Fetched 2026-09-09 (Layer A unless noted):

- IBAT — https://www.ibat-alliance.org/ (home), https://www.ibat-alliance.org/services (services, report types, DPR methodology, framework mapping)
- WWF Biodiversity Risk Filter — https://riskfilter.org/biodiversity (home), https://riskfilter.org/biodiversity/assess (Assess module, Portfolio Manager workflow)
- NatureAlpha — https://www.naturealpha.ai/ (home, Geoverse 2.0, use cases)
- GIST Impact — https://gistimpact.com/ (home), https://www.gistimpact.com/nature-and-biodiversity/ (nature solution detail)

**Source-access limitations:**

- ENCORE (encore.naturalcapital.finance) — the domain now serves an unrelated crypto-gambling site that describes the original Natural Capital Finance Alliance in a "merger" post. The original ENCORE documentation is not reachable. ENCORE is **not** used as a sampled product; its name ("Exploring Natural Capital Opportunities, Risks and Exposure") is only noted as historical confirmation of the dependency/impact framing.
- tnfd.global — 403 on two attempts (root and LEAP page). TNFD is treated as context reconstructed from product-side descriptions (IBAT's framework pages quote TNFD Locate-phase and sensitive-site criteria; GIST uses "locate, evaluate, assess, prepare" language). No TNFD-primary claims are made.
- S&P Global Sustainable1 — 403. Not sampled.
- No product help-center requiring login was accessed; all evidence is from public official pages.

## Product Observations

### Product A — IBAT (Layer A: directly observed)

**Positioning:** "The world's most authoritative biodiversity data for your world-shaping decisions." Founded and operated by a coalition of four conservation organizations (BirdLife International, Conservation International, IUCN, UNEP-WCMC). Subscription revenue is stated to fund the underlying datasets.

**Core datasets (the substrate):** IUCN Red List of Threatened Species; World Database on Protected & Conserved Areas (WDPA); World Database of Key Biodiversity Areas (WDKBA); derived datasets: STAR (Species Threat Abatement and Restoration) metric, rarity-weighted species richness.

**Users:** corporates ("map biodiversity risks, prioritise action, report"); NGOs/academics (free access to paid functionality); collaborators/service providers (embed IBAT data via API). Demo-form use cases: "Screen sites to assess biodiversity risk across operations, supply chains, or investments"; "Create bespoke reports to support decision making and sustainability disclosure"; "Assess species impact risk and conservation opportunities"; "Explore spatial data for internal GIS platforms"; "Discuss integration of data via API".

**Platform features (the workflow surface):**

- **Upload site information** — bulk portfolios of project sites, supply chains, investments in ESRI, KML, KMZ, or Excel formats.
- **Access global spatial data** — GIS shapefile downloads (core + derived datasets); API for automated monthly dataset updates.
- **Generate biodiversity reports** — tailored reports for risk assessment (IFC PS6, World Bank ESS6) and disclosure (GRI, TNFD, CSRD).
- **Visualise biodiversity footprint** — maps of sites in relation to protected areas and KBAs.

**Report products:** Disclosure Preparation Report (up to 1,000 sites; automatic buffers by operation type), Proximity (single site, user-specified buffers), PS6 & ESS6 (critical-habitat screening), Species (STAR threat abatement), Freshwater (upstream/downstream hydrobasins), Multi-site (portfolio comparison), GIS Download, Global Database (enterprise tier).

**Assessment methodology (DPR, 2-stage):** Stage 1 — a site is *sensitive* if its area of influence (site + buffer) overlaps a protected area or KBA, or if STAR Threat Abatement/Restoration scores exceed global median values. Stage 2 — sensitive sites get a significance score (high/medium/low) based on proximity relative to an operation-type-specific buffer, or on maximum STAR scores. Operation-type buffers: 5 km (offices, warehouses, low-input agriculture), 10 km (high-input agriculture, onshore wind, construction, terrestrial oil & gas), 20 km (offshore wind, marine oil & gas, hydropower), 50 km (mining); 20 km default for uncategorized operations.

**Framework alignment:** TNFD (Locate phase; Strategy D "priority sites" — the page quotes TNFD's sensitive-site criteria: areas important for biodiversity; high ecological integrity; rapid decline in ecosystem integrity; high physical water risks; importance for ecosystem service provision), GRI 101 (Disclosures 101-4, 101-5), CSRD/ESRS E4 (SBM-3, IRO-1, E4-2, E4-5), SFDR biodiversity indicators, CDP, Science Based Targets for Nature.

**TNFD description quoted from IBAT's page:** "TNFD provides a risk management and disclosure framework to help organisations assess, report, and respond to nature-related risks and opportunities."

**Pricing:** free basic account; Basic / Pro / Enterprise / Enterprise plus / PAYG tiers.

### Product B — WWF Biodiversity Risk Filter (Layer A: directly observed)

**Positioning:** "Corporate and portfolio-level screening tool to help companies and investors to prioritize action on what and where it matters the most to address biodiversity risks for enhancing business resilience." Free online tool; account required only for the Assess module.

**Module structure (the workflow):**

1. **Inform** — industry-level overview of dependencies & impacts; investigate specific industries. Explicitly limited to **direct** impacts and dependencies of each industry sector.
2. **Explore** — maps of physical, regulatory (deficiency), and reputational biodiversity risks; country profiles; data & methods (70 indicators describing state of biodiversity health and pressures).
3. **Assess** — Portfolio Manager + Analyse Biodiversity Risk.
4. **Act** — "Coming soon": corporate-level mitigation recommendations based on the user's own risk results.

**Risk model (explicit):**

- **Dependency on biodiversity** → ecosystem-service decline creates **Physical Risk** for business locations that depend on those services.
- **Impact on biodiversity** → **Regulatory (Deficiency) Risk** (inadequacy of the regulatory system in a jurisdiction/sector) and **Reputational Risk** (stakeholder/community perception, linked to operational performance and landscape pre-conditions such as media scrutiny, conflict, protected areas).

**Assess workflow (4 steps):** Login → Portfolio Manager (add/edit companies, groups, sites; select what to analyse) → Analyse Biodiversity Risk (visualise per company/group/single site in maps, charts, tables; export to Excel) → optionally flip to the sister Water Risk Filter ("biodiversity and water risk assessments are complementary").

**Input data required:** location + industry sector of sites. The tool then assesses via **33 risk indicators** with **default industry sector weightings**.

**Users:** companies and financial institutions; sectors named: food & beverage, textile, retail, mining, manufacturing, finance.

### Product C — NatureAlpha / Geoverse (Layer A: directly observed)

**Positioning:** "Nature Risk Intelligence. Simplified." AI-powered geospatial analytics; free "Geoverse Explorer" tier plus commercial platform.

**Stated workflow (vendor's own sequence):** "First we locate geospatial risk → Then we evaluate operations, supply chains, and footprints → Finally applying governance assessment → This allows us to translate company specific data into a regulation friendly risk score → Your materiality exposure is then converted into a revenue exposure (NVaR – Nature Value at Risk)."

**Coverage claims (vendor-stated, not independently verified):** 11,500 equities, 1.7M corporate bonds and private assets, 8.5M asset locations, 130M monthly data points; SLA of 99.5% accuracy on asset location data; LLMs extract governance/mitigation data points from company reports, policies, controls, disclosures.

**Use cases (vendor-stated):** TNFD disclosure submissions; CSRD biodiversity reporting; GRESB RM7 (real-estate biodiversity indicator); rapid materiality assessments; physical and transitional risk analysis; asset-level biodiversity risk assessment (asset infrastructure overlapping sensitive or protected areas); climate–nature risk interactions for insurance underwriting (ecosystem degradation → flood/drought impact on insured assets); nature risk in credit/lending decisions for borrowers in ecologically sensitive areas.

**Clients:** investment firms (Franklin Templeton, LGT, Royal London, Lombard named on page), banks; affiliate of the Circular Bioeconomy Alliance.

### Product D — GIST Impact (Layer A: directly observed)

**Positioning:** "Decision-grade, AI-powered data and intelligence for assessing impacts, managing risks and quantifying value." Nature & Biodiversity is one of three intelligence solutions (alongside Climate Risk and Impact on Society) on a broader impact-data platform.

**Nature solution framing:** "Locate, evaluate and assess your nature-related dependencies, impacts, risks and opportunities"; "whether you want to locate, evaluate, assess or prepare — GIST Impact offers the market-leading suite" (LEAP-shaped language, vendor's own words).

**Intelligence Suite modules (nature):** Areas of Biodiversity Importance (proximity to Key Biodiversity Areas, WDPA Protected Areas, IUCN Red List species — in partnership with IBAT); Ecosystem Integrity (Biodiversity Intactness Index, Mean Species Abundance, land-area change — with London's Natural History Museum); Indigenous Peoples and Community Lands; Dependencies on Ecosystem Services (25 types); Dependencies on Commodities; Pressures on Ecosystems (13 types); Impact on Biodiversity (Potentially Disappeared Fraction of species); Impact on Society (monetary decrease of natural-capital stock); Deforestation exposure (with Global Canopy / Forest IQ Pro); **Nature Value at Risk** (risk to operations and value chain from nature degradation); Physical Risks (water stress, flooding, heatwaves, cyclones); Nature-Related Opportunities (species threat abatement and restoration — with IBAT).

**Data foundations:** ESG data, revenue data, asset data (3M+ assets classified into 105 asset types); AI curation + scientific validation; data-gap filling; aggregation from single assets to portfolios; delivery via data feeds, API, and web apps; investor portal.

**Alignment:** TNFD, PBAF, SFDR (nature page); CSRD/IFRS/EBA/BIS/TCFD/GRI etc. on the reporting page.

**Clients:** asset owners/managers, banks, wealth managers, exchanges, tech platforms, corporates, consultants, academia.

## Cross-product Comparison

| Dimension | IBAT | WWF BRF | NatureAlpha | GIST Impact | Reading |
|---|---|---|---|---|---|
| Unit the user brings | sites/portfolios of sites, supply chains, investments (geometries or lists) | companies, groups, sites (location + sector) | companies/assets resolved from securities & bonds | companies + 3M+ assets (type + location) | **B: located interface records are universal** |
| Nature data substrate | IUCN Red List, WDPA, KBAs, STAR | 70 state/pressure indicators; risk maps | geospatial nature layers (vendor-curated) | KBAs/WDPA/Red List (via IBAT), integrity indices, ecosystem services, pressures | **B: external authoritative nature data is universal** |
| Dependency axis | implicit (site sensitivity focus) | explicit (industry dependencies → physical risk) | explicit ("evaluate operations, supply chains, footprints") | explicit (25 ecosystem-service dependencies; commodity dependencies) | **B: dependencies + impacts are the two risk-generating axes** |
| Impact axis | site sensitivity vs protected areas/species | explicit (impacts → regulatory deficiency + reputational risk) | explicit (materiality matrix) | explicit (13 pressures; PDF metric; monetary impact) | B |
| Risk output | sensitive/not-sensitive + high/medium/low significance; critical-habitat flags | physical / regulatory (deficiency) / reputational risk results | "regulation friendly risk score"; NVaR revenue exposure | risk scores; Nature Value at Risk; physical-risk exposure | **B: risk determination (classification/score/exposure) is universal** |
| Prioritization | significance scores; site prioritization in DPR | "prioritize action on what and where it matters most" | materiality → exposure ranking | portfolio aggregation to rank | **B: prioritization is a shared purpose** |
| Response/act | strategy service; STAR opportunities (abatement/restoration) | Act module "coming soon" | "understand, manage, and mitigate" (governance layer) | nature-related opportunities module | **A→B: response support exists but is thin/optional — not the center** |
| Disclosure alignment | TNFD, GRI 101, ESRS E4, SFDR, CDP, SBTN, PS6/ESS6 | positioned for corporate strategy; framework-neutral on fetched pages | TNFD, CSRD, GRESB | TNFD, PBAF, SFDR, CSRD, GRI | **B: framework alignment is near-universal but varies in depth** |
| Delivery | web app + reports + GIS downloads + API | free web app | web platform + free Explorer tier | data feeds + API + web apps + portal | **B: form factor varies widely** |
| Business model | subscription + PAYG; free basic | free (NGO) | commercial + free tier | commercial data licensing | **B: pricing is a variant axis** |
| Financial-institution orientation | investments among upload types; SFDR support | companies AND financial institutions | equities/bonds/loans/insurance | asset owners/managers/banks native | **B: FI use is common but corporate site-level use is equally first-class** |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

A Nature Risk Management application is recognizable by three jointly-held structures:

1. **Located interface records** — the organization's points of interface with nature (operating sites, assets, holdings, supply-chain locations) held as records bound to geographic locations and to a business activity/sector. *Remove → a biodiversity data portal or a generic asset registry.*
2. **Nature-context evaluation** — each located record is evaluated against external nature/biodiversity data (state of nature at and around the location: protected/conserved areas, key biodiversity areas, threatened species, ecosystem condition/integrity, water, ecosystem services) to surface the organization's **dependencies on nature** and/or **impacts on nature**. *Remove → GIS viewer or raw data download; the business–nature interface is gone.*
3. **Nature-related risk determination** — the evaluation resolves into risk classifications, scores, or exposure measures (commonly organized as physical / regulatory / reputational) that support **prioritization** of locations and entities. *Remove → a data viewer; the "risk" product is gone.*

Jointly load-bearing: (1) alone = asset registry; (2) without (1) = biodiversity data portal; (3) without (1)+(2) = scores over nothing; (1)+(2) without (3) = screening data source below the Type; (1)+(3) without (2) = generic ERM register with spatial dressing.

### L1 — Common Mature Structure (common, not definitional)

- Portfolio-level aggregation (companies → groups → sites; corporate and financial-institution views over the same records)
- Framework/disclosure alignment (TNFD LEAP-shaped workflow, GRI 101, CSRD/ESRS E4, SFDR, CDP, SBTN, IFC PS6/World Bank ESS6)
- Map + chart + table visualization of results; export (Excel, PDF reports, GIS shapefiles)
- Explicit sensitivity/priority methodology (buffers, significance tiers, sector weightings)
- Risk typology organized around physical / regulatory / reputational (labels vary)
- Exposure metrics of the "Nature Value at Risk" family (observed in 2 of 4 products under the same name)
- Opportunity identification (species threat abatement and restoration)
- API / data-feed delivery for integration into risk, lending, underwriting, and reporting systems
- Account-gated private assessment over a public exploration layer

### L2 — Variant / Optional Structure

- Free public tool vs subscription commercial vs data-licensing pole
- Single-site deep screening vs bulk portfolio screening vs security-level portfolio analytics
- Monetary valuation of impacts/natural capital (present in the impact-economics pole only)
- AI/LLM augmentation of governance and disclosure data
- Default sector weightings vs custom materiality matrices
- Water as a sister module (water risk filter pairing) vs water folded into nature indicators
- Response/action modules (mitigation recommendations, strategy support) — present as roadmap or service layer, not the center
- Industry verticals (mining, agriculture, energy, real estate, finance) as weighting/content variants

### L3 — Vendor-specific (Research Notes only)

- IBAT: operation-type buffer table (5/10/20/50 km), STAR global-median thresholds, named report products (Disclosure Preparation Report, PS6 & ESS6 report, Freshwater report), PAYG pricing, dataset funding model
- WWF BRF: 33 risk indicators / 70 explore indicators, default industry weightings, "Regulatory (Deficiency) Risk" label, Water Risk Filter pairing, Act module roadmap
- NatureAlpha: NVaR branding, Geoverse 2.0 coverage figures, LLM governance extraction, FINMA-specific compliance page, GRESB RM7 content
- GIST Impact: 25 ecosystem-service types, 13 pressure types, PDF (Potentially Disappeared Fraction) metric, partnerships (IBAT, Natural History Museum, Global Canopy/Forest IQ), investor portal

## Rejected Findings (considered, then rejected as definitional)

- **"Monetary valuation is definitional"** — rejected: only the impact-economics pole monetizes; IBAT and WWF BRF operate in classification/score space. Held as L2.
- **"TNFD alignment is definitional"** — rejected: IBAT's project-finance screening lineage (PS6/ESS6, critical habitat) predates and is independent of TNFD; the Type must survive without any single framework. Framework alignment held as L1.
- **"Financial-institution/portfolio orientation is definitional"** — rejected: corporate site-level screening is equally first-class (IBAT single-site reports; WWF corporate use). Held as L2/variant.
- **"AI/geospatial analytics engine is definitional"** — rejected: WWF BRF and IBAT deliver risk determinations with indicator/weighting methodologies, not AI pipelines. Held as L2.
- **"Response/action management is definitional"** — rejected: the flagship free tool's Act module is explicitly "coming soon"; IBAT's response support is a service layer. The Type's center is assess-and-prioritize; response support held as L1/L2.
- **"Water risk is a separate definitional axis"** — rejected as separate: water appears both inside nature indicators (physical risk) and as a sister module; held as L2 bundling.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (the "remove → becomes" test) |
|---|---|---|
| Climate Risk Management / Physical Climate Risk Platform | adjacent, partially overlapping | Same structural shape (located assets → hazard data → risk scores), different risk-generating system: nature risk centers on **ecosystems/biodiversity/ecosystem services**; climate risk centers on **climate hazards and transition**. Overlap zone: water stress, flooding, and physical-risk exposure appear in both (GIST lists water stress/flooding under nature physical risks; NatureAlpha markets climate–nature interactions). Remove the biodiversity/ecosystem axis → climate risk platform. Products increasingly bundle both. |
| Natural Capital Management | adjacent | Natural capital management is **measurement/accounting-centric** (stocks, flows, valuation of natural capital); nature risk management is **risk-process-centric** (screen → assess → prioritize). Monetary impact valuation (GIST "Impact on Society") straddles the seam. Remove the risk determination → natural capital accounting. |
| Biodiversity Management | adjacent | Biodiversity management is broader **strategy/footprint/action** management (targets, projects, conservation actions, monitoring); nature risk management is the **risk assessment lens** over the business–nature interface. IBAT's "Biodiversity Strategy" service straddles. Remove the risk lens → biodiversity management. |
| ESG Management Platform | adjacent, integration partner | ESG platforms handle nature as one topic among many with questionnaire/reporting machinery; nature risk management is **nature-specialized with geospatial depth**. ESG platforms consume nature-risk data (GIST partners with data-management platforms). |
| Enterprise Risk Management | consumer/adjacent | ERM is a generic risk register and process; nature risk management supplies the **specialized nature data and assessment methodology** whose outputs (prioritized risks) can feed ERM registers. |
| Environmental Management System | adjacent | EMS is site-level **compliance management** (ISO-14001-style); nature risk is portfolio-level **risk assessment against external nature data**. |
| Environmental Monitoring Platform | adjacent, data relationship | Monitoring collects observational data from sensors/sites; nature risk management **consumes authoritative nature datasets** to assess business exposure. |
| Environmental Data Platform | upstream | Data platforms publish/serve nature data; nature risk management binds that data to a specific organization's located records and produces risk determinations. |

## Uncertainties

- **TNFD-primary detail** — tnfd.global was unreachable; LEAP phase names and sensitive-site criteria are known only through product-side quotations (IBAT, GIST). The final document therefore describes the workflow shape without attributing specific phase names to TNFD itself.
- **ENCORE** — unreachable; the historical free-tool pole is represented only by WWF BRF. The claim "free screening tools are a stable pole" rests on one live sample plus the (unverifiable) ENCORE precedent.
- **Response/Act depth** — no sampled product documents a mature, in-product response-management loop (mitigation plans, action tracking, effectiveness monitoring). It is unclear whether any market product centers this; if one does, it may stretch the Type toward Biodiversity Management. Recorded as an open question, not resolved.
- **Scenario analysis** — climate risk products commonly offer scenario analysis; for nature, no sampled product documents scenario machinery on fetched pages (WWF's Water Risk Filter has an archived "Scenarios Maps" section — nature-side scenario support unverified). Held as uncertainty.
- **Vendor coverage claims** (NatureAlpha asset counts, GIST company counts) are vendor-stated and not independently verified; kept out of the final document.

## Final Synthesis

The market realizes **one Type** with a stable three-part core: the organization's **located interface with nature** (sites/assets/holdings/supply-chain locations), an **evaluation of each location against authoritative nature data** that surfaces dependencies and impacts, and a **risk determination** (classification/score/exposure) that supports prioritization. Around that core, mature products add portfolio aggregation, framework/disclosure alignment, map/chart/table surfaces, explicit methodologies, and integration delivery. Form factor, business model, monetization, AI, and financial-institution orientation are variant axes. The workflow is LEAP-shaped in the market's own vocabulary (locate → evaluate → assess → prepare/act), but the Type predates and does not depend on TNFD. Response/action management exists at the edges (roadmap modules, service layers, opportunity identification) and is not the definitional center. The Type is distinct from climate risk (different risk-generating system), from natural capital accounting (risk lens vs measurement lens), and from biodiversity management (assessment lens vs strategy/action lens) — with a documented overlap seam on physical risks like water stress and flooding.
