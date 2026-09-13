# Research Notes — Biodiversity Management

Research date: **2026-09-06**
Methodology: v1.1 (update-v1/)

## Research Goal

Understand, from real products, what "Biodiversity Management" software is: what objects it manages, who uses it, what data it runs on, how work flows through it, and where its boundaries lie against neighboring Application Types in the same directory section (Environment, Sustainability & Climate: Natural Capital Management, Nature Risk Management, Conservation Management, Environmental Monitoring Platform, ESG/Sustainability platforms, Environmental Impact Assessment Platform).

## Initial Boundary (hypothesis before research)

- Hypothesis: biodiversity management software helps an organization know what biodiversity exists at / around the locations it touches, assess how its activities impact and depend on it, decide and track management responses (mitigation hierarchy), monitor change, and disclose against nature frameworks (TNFD, CSRD/ESRS E4, GRI 101).
- Likely users: corporate sustainability/environmental teams, environmental consultants, financial institutions.
- Likely confusions: ESG platform (biodiversity as one KPI), Nature Risk Management (risk-analytics slice), Natural Capital Management (ecosystem-services valuation), Conservation Management (conservation-org operations), Environmental Monitoring (sensor telemetry), GIS (generic spatial analysis).
- Unknowns: is there a coherent product category, or is it (a) screening tools + (b) measurement labs + (c) ESG modules + (d) consultancy workflows glued by process?

## Research Questions

1. What are the core objects? (site/asset portfolio, biodiversity records, assessments, actions, disclosures)
2. What data sources feed the records? (global reference datasets: protected areas, key biodiversity areas, threatened-species ranges; primary survey data: eDNA, bioacoustics, camera traps, field forms; geospatial/modeled layers)
3. What is the end-to-end workflow? (portfolio → screen → ground-truth → assess → act → monitor → disclose → re-assess?)
4. How deep is framework integration (TNFD LEAP, CSRD/ESRS E4, GRI 101, IFC PS6/ESS6, SBTN, regional biodiversity-net-gain style regimes)?
5. Who are the users, and do finance institutions / consultancies / operators use the same software differently?
6. Where exactly are the boundaries to the neighboring Types above?
7. What variants exist (screening-first vs measurement-first vs finance-first vs field-first; subscription vs PAYG; corporate vs consultant vs fund)?

## Representative Products

Chosen for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Evidence obtained |
|---|---|---|
| IBAT (IBAT Alliance: BirdLife International, Conservation International, IUCN, UNEP-WCMC) | screening-first, authoritative global biodiversity data, corporates + finance | official site + services page (rich: report types, methodology, framework mapping) |
| NatureMetrics | measurement-first (eDNA/bioacoustics) + "Nature Intelligence Platform" system of record; enterprise operators across sectors | official site + product pages incl. Global Nature Risk FAQ |
| NatureAlpha (Geoverse) | finance-portfolio nature-risk analytics (TNFD/CSRD/GRESB, lending, insurance) | official site (marketing-heavy) |
| Wildnote (by Fulcrum) | field-evidence / consultancy survey data capture (boundary-informing sample) | official site + solutions page |

Rejected/unreachable samples: Arbimon (acoustic monitoring; server 525 twice → abandoned), tnfd.global (403; framework content instead sourced from IBAT's official framework-mapping pages, which quote TNFD/GRI/ESRS requirements directly). Arbimon would have been the continuous-monitoring technology pole; its absence limits evidence on acoustic/AI monitoring workflows but does not affect the core model (monitoring was evidenced through NatureMetrics bioacoustics + Wildnote repeat-survey types).

## Sources

- IBAT — https://www.ibat-alliance.org/ (home), https://www.ibat-alliance.org/services (services, report types, DPR methodology, framework mapping). Fetched 2026-09-06. Layer A.
- NatureMetrics — https://www.naturemetrics.com/ (home), https://www.naturemetrics.com/products/nature-intelligence-platform, https://www.naturemetrics.com/products/global-nature-risk (incl. FAQ). Fetched 2026-09-06. Layer A.
- NatureAlpha — https://www.naturealpha.ai/ (home; Geoverse 2.0 description, use cases). Fetched 2026-09-06. Layer A, marketing-weighted.
- Wildnote — https://www.wildnoteapp.com/ (home), https://www.wildnoteapp.com/solutions (feature list, disciplines, taxonomy, exports). Fetched 2026-09-06. Layer A.
- Context: framework requirements (TNFD LEAP Locate/Strategy D; GRI 101 disclosures 101-4/101-5; ESRS E4 SBM-3/IRO-1/E4-2/E4-5; SFDR biodiversity indicators; IFC PS6 / World Bank ESS6 critical habitat) were read as quoted on IBAT's official services page (Layer A via IBAT). tnfd.global itself was not reachable.

Login-gated surfaces not accessible: IBAT app (app.ibat-alliance.org), NatureMetrics platform (platform.naturemetrics.com), both vendors' help centres (IBAT tutorials/FAQs behind web app; NatureMetrics Zendesk exists but was not fetched). Operational UI detail (exact screens, exact workflow steps in-app) is therefore NOT verified; interfaces are described at conceptual level only.

## Product Observations

### IBAT

Evidence layer: A (official site, including an unusually detailed services/methodology page).

Key observations:

- Core data offer: authoritative global biodiversity datasets — World Database on Protected & Conserved Areas (WDPA), IUCN Red List of Threatened Species, World Database of Key Biodiversity Areas (WDKBA) — plus derived datasets: STAR (Species Threat Abatement and Restoration metric) and rarity-weighted species richness. Datasets updated on a live cycle (site shows per-dataset "last updated" dates).
- Platform features (product's own words): "Upload site information easily" — bulk upload of site portfolios (project sites, supply chains, investments) in ESRI, KML, KMZ or Excel formats; "Access global spatial data" — GIS shapefile downloads + API for automated dataset updates; "Generate biodiversity reports"; "Visualise your biodiversity footprint" — maps of sites in relation to biodiversity-sensitive areas.
- Report products: Disclosure Preparation (up to 1,000 sites, TNFD/GRI/ESRS E4 output PDFs + Excel attribute lists + README methodology), Proximity (single site, user-specified buffers), PS6 & ESS6 (critical-habitat screening incl. candidate triggers, "How to assess" column, precautionary 50 km buffer on IUCN Red List), Species (STAR threat-abatement opportunity per site), Freshwater (upstream/downstream hydrobasin species), Multi-site (annual sustainability reporting, portfolio STAR totals), GIS Download, Global Database (Enterprise).
- Screening methodology (DPR): two stages — (1) sensitivity: site + buffer overlaps a protected area or KBA, or STAR scores exceed global median values; (2) significance score (high/medium/low) based on distance to KBA/PA relative to buffer size per operation type (buffer defaults differ by operation type: offices/warehouses/low-input agriculture vs high-input agriculture/onshore wind/construction/terrestrial oil & gas vs offshore/marine vs mining), or based on max STAR values.
- Framework mapping (extensive, quoted requirement-by-requirement): TNFD (LEAP Locate phase; Strategy D priority/sensitive sites — with explicit caveat that the report "currently only assesses sensitive sites that are important for biodiversity" and other TNFD criteria must be considered by the user), GRI 101 (101-4 identification of biodiversity impacts; 101-5 sites with biodiversity impacts: in/near ecologically sensitive areas, distance, hectares), ESRS E4 (SBM-3 material sites; IRO-1 process incl. LEAP; E4-2 policies; E4-5 impact metrics; supplier sites in risk-prone areas), SFDR biodiversity indicators (PAI core + additional), SBTN, CDP, IFC PS6 / World Bank ESS6.
- Audience & pricing: free basic account for all; paid tiers (Basic/Pro/Enterprise/Enterprise plus/PAYG); NGOs/academics free access to paid functionality; "collaborators" = service providers embedding IBAT data.
- Customer evidence (testimonials/case studies): corporate users for CSRD disclosure, site risk screening, prioritising restoration at operating sites, integrating analysis with GIS tools; a carbon-credit rating agency using the data for ratings; DFIs/fund-of-funds.

Interpretation: IBAT is the "screening against authoritative reference data" pole. It does NOT hold the organization's own measured field data; its biodiversity records are derived from global reference datasets (species ranges, PA/KBA boundaries). Its outputs are decision + disclosure artifacts (maps, ranked lists, report packs). Action management is limited to opportunity identification (avoidance in siting, threat abatement/restoration opportunity metrics).

### NatureMetrics

Evidence layer: A (official site + product pages incl. FAQ).

Key observations:

- Positioning: "complete nature intelligence system" / end-to-end: **Screen → Collect → Interpret → Manage**.
- Screen: "Global Nature Risk" — a 0–1 risk score per site combining three layers (State of Nature, Dependencies, Impact), built on "26 globally validated geospatial datasets", calibrated to operations, quarterly-updated, "audit-ready methodology, traceable to peer-reviewed sources", TNFD-aligned outputs; workflow: upload portfolio (site locations + activity codes) → score every asset → act on what matters (filter heatmap, single-site reports, export TNFD-aligned evidence packs, validate highest-risk sites on the ground) → quarterly re-score so "progress is visible in the same view".
- Collect: eDNA (sampling kits + own laboratory; "a single eDNA sample reveals the species present — vertebrates, invertebrates, bacteria, fungi"; "to the standard a permit or a lender accepts") and bioacoustics monitoring.
- Interpret: "Species & Habitat Insights" (comparable, standardized metrics from site to landscape; benchmark across asset base; track recovery; ecological indicators across water/soil/vegetation); "Ecosystem Condition Index" suite (0–100 biological condition score).
- Manage: "The Nature Intelligence Platform" — "the portfolio dashboard and system of record that centralises nature data across thousands of sites"; "One record, built from multiple sources" — unifies own site data + public/third-party datasets + ground sampling into one validated record; portfolio baselines, trends, outliers; prioritization categories ("Act Now / Monitor / Low Priority" with site counts); drill-down portfolio → site with connected eDNA/geospatial/modelled data behind every number; "Aggregated dashboards and standardised metrics make internal and external reporting against TNFD, CSRD and GRI faster".
- Use cases (named, with contents): Permitting & EIA (protected-species and habitat surveys to recognised protocols; critical habitat assessments); Lender due diligence (IFC PS6 baselines, drawdown/covenant evidence, Equator Principles); Biodiversity offsets (offset site verification, like-for-like equivalence, **mitigation hierarchy evidence**); Mine closure & rehabilitation bonds (closure-criteria baselines, recovery monitoring, bond-release evidence); Supply-chain nature risk (on-farm condition monitoring, deforestation-free & SBTN evidence); Corporate nature & disclosure (TNFD and ESRS E4 disclosure, nature strategy and targets).
- Named users: sustainability leaders; ESG/finance/reporting leads; heads of nature/environment; risk officers.
- Sectors: mining & extractives, energy, infrastructure & transport, consumer goods & agriculture, conservation & forestry, financial services, consultancies.
- Scale claims (vendor-stated, not independently verified): 600+ organisations in 126 countries; 4.3M+ validated species detections; 10 years of ground-truth data.
- Help centre (Zendesk) and kit instructions exist; platform itself login-gated.

Interpretation: NatureMetrics is the "integrated measurement + system of record" pole. Its distinctive claim is natively connecting modeled screening data with primary (lab-generated, validated) species detections in one site record, and closing the loop: screen → survey → act → re-score quarterly. It shows the full canonical loop including mitigation-hierarchy evidence and monitoring.

### NatureAlpha (Geoverse)

Evidence layer: A but marketing-weighted (official site; no operational docs fetched).

Key observations:

- Positioning: "Nature Risk Intelligence" for financial institutions; Geoverse 2.0 "interactive analytics platform" delivering "the data and analytics required to fulfil the Corporate Sustainability Reporting Directive (CSRD) related to biodiversity".
- Method (product's own words): "First we locate geospatial risk → Then we evaluate operations, supply chains, and footprints → Finally applying governance assessment → This allows us to translate company specific data into a regulation friendly risk score → Your materiality exposure is then converted into a revenue exposure (NVaR – Nature Value at Risk)."
- Structure: asset-level geospatial exposure (whether asset infrastructure overlaps sensitive/protected areas) mapped to companies and portfolios (securities). Vendor-claimed scale: 11,500 equities, 1.7M corporate bonds and private assets, 8.5M asset locations, high-frequency data-point updates. LLM-based extraction of company policies/controls/disclosures into "unmanaged risk" calculations; dynamic updates on M&A/expansion/divestiture.
- Use cases: TNFD submissions; CSRD; GRESB RM7 (real-estate biodiversity indicator); materiality assessments; physical & transitional risk; impact-investing metrics; lending risk; insurance underwriting (climate–nature interactions).
- Clients: asset/wealth managers (logos incl. Franklin Templeton, LGT, Royal London, Lombard Odier; plus IBAT as partner).

Interpretation: NatureAlpha is the "finance-portfolio" pole: the "site portfolio" is assembled from the investee/universe side (asset locations mapped to securities), the assessment is a risk score + revenue-exposure translation, and outputs feed investment/lending/underwriting decisions and disclosures. No primary field data; no operational mitigation-hierarchy tracking; monitoring = refresh cadence.

### Wildnote (boundary-informing sample)

Evidence layer: A (official site + solutions page).

Key observations:

- Positioning: "THE Environmental Consulting Platform" — fieldwork data collection, QA/QC and reporting for environmental consultants (now part of Fulcrum).
- Structure: projects → project locations (sampling points, bird nests, cultural sites, construction sites) → survey forms (library of professional-grade environmental forms; custom form builder) → field crews on iOS/Android (offline-capable, SmartSync) → web QA/QC (issue tracker, survey status lifecycle, photo gallery linked to data, role-based access) → exports/reports (PDF, Excel, KML, GDB, geoJSON; agency-ready reports e.g. USACE Wetland Determination, CA DPR; narrative report builder; photo sheets).
- Biodiversity-relevant machinery: taxonomy framework (USDA/USACE plant lists, wildlife lists, invasive species; Latin/common names; metadata such as listing status, native/non-native, wetland indicator status); "Species Export" report-ready table; dozens of named biological survey types (bat, raptor, burrowing owl, desert tortoise, fairy shrimp, migratory bird, nest monitoring, vegetation transects, habitat banking, mitigation banking...); repeat monitoring survey types (post-construction monitoring, vegetation monitoring, success criteria).
- What it does NOT have: no reference-dataset screening (no protected-area/KBA/species-range layers), no impact/dependency risk assessment, no disclosure-framework mapping (its "regulatory" frame is agency/permit report formats), no portfolio risk ranking.

Interpretation: Wildnote supplies the **primary-evidence layer** (site-anchored species/vegetation records, protocol compliance, QA) that integrated products like NatureMetrics bundle, but as a standalone tool it lacks the assessment/prioritization/disclosure loop. It therefore (a) evidences "structured field capture with taxonomy and QA" as a standard ingredient, and (b) marks a boundary: pure survey-data-collection platforms are an adjacent tool class feeding this Type rather than full members.

## Cross-product Comparison

| Capability / structure | IBAT | NatureMetrics | NatureAlpha | Wildnote |
|---|---|---|---|---|
| Identified location portfolio (bulk import) | Y — bulk upload ESRI/KML/KMZ/Excel (sites, supply chains, investments) | Y — upload site locations + activity codes | Y — asset locations mapped via securities/asset database | Y — project locations (points, per project) |
| Site-anchored biodiversity records | Y — from global reference datasets (PA/KBA overlap, species ranges, STAR-derived) | Y — modeled layers + validated eDNA/acoustic detections + third-party data ("one record, multiple sources") | Y — geospatial risk layers at asset level | Y — field survey records (species/vegetation/habitat forms, photos) |
| Screening/assessment vs reference data | Y — proximity/overlap + metrics (core of product) | Y — 0–1 composite risk score (state/dependencies/impact) | Y — geospatial exposure + risk score + revenue exposure | N |
| Critical-habitat / lending-standard screening | Y — PS6/ESS6 report with candidate triggers | Y — IFC PS6 baselines, Equator Principles evidence | partial — lending/underwriting risk use cases | N |
| Primary field-data capture | N (modeled ranges only) | Y — eDNA kits+lab, bioacoustics | N | Y — mobile forms, offline, taxonomy, GNSS |
| Standardized metrics/indices | Y — STAR (threat abatement/restoration), rarity-weighted richness | Y — ECI condition index (0–100), species/habitat insights | Y — composite risk score, NVaR | partial — agency-form calculations, species export tables |
| Site prioritization | Y — sensitivity → significance (high/medium/low) | Y — Act Now / Monitor / Low Priority | Y — portfolio ranking | N |
| Mitigation-hierarchy / action linkage | partial — avoidance in siting; STAR restoration opportunities | Y — offset verification, closure criteria, biodiversity action plans, score deltas after interventions | partial — "unmanaged risk" after governance/controls extraction | N (permit-compliance evidence) |
| Monitoring over time | partial — datasets refresh; reports repeatable per site | Y — quarterly re-score, trends, recovery tracking, repeat surveys | Y — refresh cadence (vendor-claimed dynamic updates) | Y — repeat monitoring survey types |
| Disclosure outputs (TNFD/CSRD/GRI/SFDR) | Y — DPR mapped requirement-by-requirement | Y — "TNFD, CSRD and GRI disclosure built in", evidence packs | Y — TNFD/CSRD/GRESB alignment | N — agency/permit report formats instead |
| GIS interoperability | Y — shapefile downloads, API | Y — geospatial sources integrated | Y — data delivery into risk stacks | Y — geoJSON/KML/GDB exports, ESRI integration |
| Primary customer tier | corporates + finance + NGOs/academia; PAYG→enterprise | enterprise operators across land-heavy sectors; consultancies; finance | financial institutions | environmental consultancies |
| Product philosophy | data authority: sell screened access to authoritative datasets as reports | vertical integration: own the measurement (lab) and the system of record | analytics layer over securities/asset universe | field-evidence tooling for consultants |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

A Biodiversity Management application is an organization-facing system that:

1. **Maintains a location portfolio** — identified sites/assets through which the organization interfaces with nature (operated sites, planned developments, supply-chain or financed exposures).
2. **Binds biodiversity records to those locations** — screening results against reference biodiversity data, and/or primary observations/condition indicators (species detections, habitat assessments, condition scores).
3. **Assesses the organization's nature interface at those locations** — evaluated impact, dependency, risk, sensitivity, or regulatory condition (e.g., critical-habitat screening), not just raw data storage.
4. **Produces prioritization and accountability outputs** — ranked/prioritized sites and report/disclosure artifacts that carry the assessment into management follow-up and external reporting.

Remove (1)–(2) → generic ESG/reporting tool. Remove (3) → survey data collection / GIS archive. Remove (4) → internal data science, not management. All four are needed for the Type to be recognizable.

Historical / market-sample check: pre-TNFD consultancy workflows (site + species records + impact assessment for EIA → reports to regulator), regional statutory calculators (e.g., habitat-based net-gain metrics computing loss/gain units per site for planning submissions), and older GIS-based ecology practices all satisfy (1)–(4) without modern SaaS features → the definition does not over-fit to the post-2023 disclosure-driven SaaS generation. Conversely, conservation-patrol systems (protected-area operations) fail (3)–(4) in this sense — they manage conservation delivery, not an organization's impact/dependency interface → correctly excluded.

### L1 — Common Mature Structure (cross-product B-layer)

- Bulk portfolio import (spreadsheets, GIS formats) as the onboarding step
- Reference biodiversity data layers (protected areas, key biodiversity areas, threatened-species ranges) with proximity/overlap screening and configurable/default buffers
- Standardized, comparable metrics/indices so heterogeneous sites can be ranked (condition indices, composite risk scores, threat-abatement/restoration metrics)
- Site prioritization tiers feeding work allocation
- Disclosure-framework mapping (TNFD LEAP locate/evaluate, ESRS E4, GRI 101, IFC PS6/ESS6) producing report packs with methodology/traceability documentation
- Primary-data capture channels (eDNA, bioacoustics, camera traps, structured survey forms with taxonomy) feeding site records
- Portfolio dashboard: map/score view + drill-down to per-site detail
- Repeat-assessment monitoring: trends, recovery tracking, intervention effectiveness
- GIS interoperability and API/data delivery

### L2 — Variant / Optional Structure

- Customer pole: corporate operator vs financial institution (portfolio analytics) vs consultancy (field evidence)
- Data posture: screening-only (modeled reference data) vs integrated primary measurement (own lab/sensors) vs hybrid validation loop
- Business model: subscription vs pay-as-you-go reports vs data licensing/API vs bundled lab services
- Vertical protocol packs: lender standards (IFC PS6, Equator Principles), mine closure/bond release, offsets/net gain, SBTN target-setting, supply-chain/on-farm monitoring
- Regional regulatory regimes (statutory net-gain metrics, national protected-area networks)
- AI usage: LLM extraction of company policies/governance (finance pole); AI species detection (monitoring)
- Depth of action management: from opportunity identification to tracked action plans with re-measurement (varies; often consultant-mediated)

### L3 — Vendor-specific (research notes only)

- IBAT: STAR metric productization; DPR buffer-default tables by operation type (5/10/20/50 km); PAYG tiers; alliance ownership model (fees fund the underlying datasets); "How to assess" column in PS6 workbooks.
- NatureMetrics: proprietary Ecosystem Condition Index (0–100); Global Nature Risk 0–1 methodology ("26 datasets" claim); "one validated record" framing; eDNA kit shop; AWS Marketplace distribution.
- NatureAlpha: NVaR (Nature Value at Risk); Geoverse 2.0 scale claims (11,500 equities; 8.5M asset locations; 14.8B calculations/sec); LLM governance extraction; Geoverse Explorer free tier.
- Wildnote: agency form libraries (CA DPR, NV IMACS, UT forms); Munsell soil chart dropdowns; GNSS device integrations (Trimble/EOS/Juniper/Bad Elf); Fulcrum ownership.

## Rejected Findings (considered and rejected as canonical)

- "Biodiversity management = eDNA/technology monitoring" — rejected: measurement technology is one data channel (NatureMetrics pole); IBAT and NatureAlpha run fully on modeled/reference data.
- "Must include framework disclosure (TNFD/CSRD) machinery in the defining core" — rejected: pre-TNFD EIA-era and regional-metric products satisfy the Type; framework mapping is the current dominant demand driver (L1, not L0), evidenced by its presence in 3/4 samples.
- "Must include mitigation-hierarchy action management as a product feature" — rejected as too strong: only clearly present in NatureMetrics' own description; IBAT/NatureAlpha stop at prioritization/opportunity; action execution is often consultant/project-mediated. Kept in L0 only as "outputs that carry assessment into management follow-up", not as tracked-action machinery.
- "Report packs (PDF+Excel+README) are canonical" — rejected: implementation detail of the screening pole.
- "Biodiversity data = species lists" — rejected: habitat/condition/ecosystem-condition records are equally first-class (condition indices, habitat assessments).
- Sample statistic claims (e.g., vendor counts of sites/assets/species detections) — rejected from canonical doc: vendor marketing claims, unverifiable.

## Boundary Findings

1. **vs Natural Capital Management**: NCM centers on ecosystem services / natural capital accounting and (often) monetary valuation of nature's contributions; biodiversity management centers on living-diversity records (species/habitat) and the organization's impact/dependency interface. Test: strip species/habitat impact assessment, keep service valuation/accounting → NCM. Overlap: geospatial condition data, TNFD framing. Siblings unprocessed — flag for joint review.
2. **vs Nature Risk Management**: heavy overlap. The risk-analytics slice (dependency/impact risk scoring, TNFD LEAP Evaluate, finance-first) is fully embodied by NatureAlpha and by NatureMetrics' Global Nature Risk. Boundary is emphasis: biodiversity management spans records → assessment → action → monitoring → disclosure; nature risk management is the risk-decision slice of that loop. Test: remove record-keeping/measurement/monitoring depth, keep risk scoring → Nature Risk Management. **Probable partial-overlap between siblings — flagged for joint review.**
3. **vs Conservation Management**: conservation-organization operations (protected areas, species programs, patrols, stewardship) manage nature itself as the beneficiary; biodiversity management manages the *organization's* interface with nature (impact/dependency/disclosure). Same data substrate (species records) but different actor, question and workflow. Test: if the software still makes sense with no corporate/operator "self" whose impacts and disclosures matter → Conservation Management.
4. **vs Environmental Monitoring Platform**: sensor telemetry of physico-chemical parameters (air/water/noise) vs biodiversity state records (species/habitat/condition). Overlap on "monitoring" and sometimes on shared sensing infrastructure; object of record differs.
5. **vs Sustainability/ESG Management Platform**: ESG platforms aggregate enterprise-wide ESG data including biodiversity KPIs, without site-anchored species/habitat machinery or reference-data screening; biodiversity management is topic-deep. Biodiversity often appears as a module/data source inside ESG suites — capability-inside-Type, not the Type.
6. **vs Environmental Impact Assessment Platform**: EIA platforms manage the project permitting lifecycle (scoping, chapters, consultation, conditions); biodiversity management supplies biodiversity evidence and ongoing portfolio monitoring across projects/operations. EIA is project-lifecycle-centered; biodiversity management is portfolio/state-centered. Hand-off at: EIA consumes the surveys/assessments this Type produces.
7. **vs survey-data-collection platforms (Wildnote-class)**: capture + QA + agency-form reporting without assessment/prioritization/disclosure machinery → adjacent feeding tool class, not the Type (fails L0-3/L0-4 as a product).
8. **vs GIS**: generic spatial analysis infrastructure; this Type is a domain application whose concepts (sites, sensitivity, mitigation, disclosure) do not exist in a GIS.

## Uncertainties

- Category youth: "biodiversity management software" as a named category is post-2023 (TNFD/CSRD-driven); the market is still repositioning older tools (screening, labs, consultancy apps) under this banner. Sample may under-represent (a) conservation/NGO-facing systems (likely belong to Conservation Management), (b) government biodiversity-data infrastructures (likely Public/GIS data platforms), (c) ESG-suite biodiversity modules (deep docs not fetched).
- Depth of **action/plan tracking** inside products is under-evidenced (no login-gated product docs observed). NatureMetrics narrative mentions biodiversity action plans and intervention tracking via score deltas; direct feature documentation was not accessible. Final doc keeps this at moderate strength.
- NatureAlpha page is marketing-heavy; all scale/precision numbers treated as vendor claims, none asserted in the final document.
- tnfd.global unreachable; TNFD/LEAP description relies on IBAT's official quoting of framework requirements (Layer A via one product).
- In-app operational detail (exact screens, exact defaults beyond what services pages state) not verified for IBAT/NatureMetrics (login-gated); interfaces described conceptually in the final doc.
- Regional (non-UK/EU/US) biodiversity management products not sampled; buffer/regional-protocol specifics kept out of the final doc.

## Final Synthesis

The Type is a coherent, identifiable application category with a stable canonical loop:

```text
Location portfolio (sites/assets where the organization interfaces with nature)
  → biodiversity records bound to each site
      (reference-data screening results · field observations · condition indicators)
  → assessed nature interface (impact / dependency / risk / sensitivity / regulatory condition)
  → portfolio prioritization
  → management follow-up (deeper survey, avoid/minimize/restore/offset decisions, monitoring)
  → disclosure/reporting artifacts (framework-mapped)
  → re-assessment on cadence
```

Products differ by pole (data-authority screening vs integrated measurement vs finance analytics vs consultancy field evidence) and by how much of the loop they implement; all recognizable members implement L0's four properties. The current market emphasis (TNFD/CSRD/GRI/IFC PS6) shapes the disclosure-output layer but is not the definition. L0 one-liner: **an organization-facing system of record for the biodiversity at the locations it touches: site-anchored biodiversity records + assessed impacts/dependencies/risks + prioritization and disclosure outputs.**
