# Research Notes — Natural Capital Management

Research date: 2026-09-09

## Research Goal

Understand what "Natural Capital Management" software actually is as an Application Type: what real products that serve natural-capital work do, what structures they share, and where the Type's boundary sits against its dense sibling neighborhood (Biodiversity Management, Nature Risk Management, Conservation Management, Environmental Monitoring, Carbon Accounting, ESG platforms, GIS).

This pass also discharges the joint-review flag recorded by the 2026-09-06 biodiversity-management pass, which held: "natural-capital management shares the geospatial condition substrate but centers ecosystem-services valuation/accounting instead of species/habitat impact/dependency records."

## Initial Boundary (working hypothesis before research)

- Hypothesis: software that treats natural assets (land, habitats, water, soil, trees) as measurable, valuable stocks; quantifies the ecosystem services they produce (often monetized); accounts for stocks/flows/changes over time; and supports decisions (land-use planning, restoration investment, corporate accounting/reporting).
- Nearest Types: Biodiversity Management, Nature Risk Management, Conservation Management, Environmental Monitoring Platform, Carbon Accounting Platform, ESG/Sustainability platforms, GIS, Farm/Forestry Management, Natural Resource Rights Management.
- Known unknowns: (a) is there a coherent product category, or a loose family of modeling toolkits / land-planning services / corporate accounting tools? (b) is monetary valuation definitional? (c) does "management" imply operational execution (it does not, per sibling Types' precedent) or decision support?

## Research Questions

1. What is the unit of record — natural asset stock? land parcel? organization account?
2. How are ecosystem services represented and quantified (biophysical vs monetary)?
3. What accounting structures exist (extent, condition, services; baselines, scenarios, time series; frameworks like SEEA EA / Natural Capital Protocol)?
4. What decision loops do products serve (land-use planning, restoration investment, corporate disclosure, policy)?
5. What data do products consume (satellite EO, GIS layers, field inventory, statistics)?
6. Who are the users per product pole?
7. What interfaces do users face (map-centric, model workbench, accounting tables, dashboards)?
8. Where are the boundaries vs the sibling Types listed above?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer levels:

| Product | Operator | Pole | Customer level |
|---|---|---|---|
| InVEST (Integrated Valuation of Ecosystem Services and Tradeoffs) | Natural Capital Project (Stanford + partners) | open-source ecosystem-service modeling toolkit | researchers, governments, NGOs, consultants |
| ARIES / ARIES for SEEA | BC3 (Basque Centre for Climate Change) + UN SEEA | UN-standard natural capital accounting application | governments, researchers, businesses |
| SENCE | Environment Systems (UK consultancy) | satellite-EO natural capital spatial evidence service | governments, estates/land managers, water companies, developers, consultants |
| i-Tree | USDA Forest Service + partner consortium | free public ecosystem-service quantification for trees/urban forest | municipalities, practitioners, homeowners, students |
| GIST Impact (nature & biodiversity suite) | commercial data provider | corporate/finance impact valuation incl. natural capital (boundary-informing) | corporates, investors, banks |

Framework sources (not products): Capitals Coalition (Natural Capital Protocol), UN SEEA (referenced via ARIES).

## Sources

Fetched 2026-09-09 (Layer A unless noted):

- InVEST — https://invest.readthedocs.io/en/latest/ (project overview, licensing, CLI/API) and https://invest.readthedocs.io/en/latest/models.html (full model entry points with parameters)
- ARIES — https://aries.integratedmodelling.org/ (platform overview, topics), https://aries.integratedmodelling.org/aries-hub/what-is-natural-capital-accounting/ (NCA explainer), https://aries.integratedmodelling.org/aries-for-seea-user-guide/ (full application user guide)
- SENCE / Environment Systems — https://envsys.co.uk/ and https://envsys.co.uk/sence/ (key features, how it works, outputs, user list, case studies)
- i-Tree — https://www.itreetools.org/ (tool suite, mission, funding/partnership)
- GIST Impact — https://www.gistimpact.com/ and https://www.gistimpact.com/nature-and-biodiversity (Tier 2, marketing pages)
- Capitals Coalition — https://capitalscoalition.org/capitals-approach/ (natural capital definition, Protocol stages, biodiversity guidance framing)

Unreachable / limitations:

- https://naturalcapitalproject.stanford.edu/software/invest — HTTP 403 (2 surfaces tried)
- InVEST User's Guide at releases.naturalcapitalproject.org — transport error ×2; readthedocs mirror 404. Model-level detail taken from the readthedocs API/models pages instead; Workbench GUI detail not verified.
- Land App (UK land-planning SaaS pole) — transport error ×2 (landapp.org, www.landapp.org). Pole described via SENCE instead; self-serve SaaS land-planning platforms under-represented.
- Capitals Coalition tool finder not fetched (base approach page used instead).
- GIST Impact help center / in-app docs not accessible (login-gated); only marketing pages observed.

## Product Observations

### InVEST (Natural Capital Project) — evidence layer A

- Self-description: "a family of tools for quantifying the values of natural capital in clear, credible, and practical ways… enables decision-makers to quantify the importance of natural capital, to assess the tradeoffs associated with alternative choices, and to integrate conservation and human development."
- Structure: a family of independent ecosystem-service models sharing one Python API. Each model has an `execute` function taking an args dict with a `workspace_dir` plus model-specific inputs.
- Recurring input grammar across models: land use/land cover (LULC) raster; biophysical tables mapping LULC classes to coefficients (root depth, carbon pools per class, nutrient loads/retention, pollinator nesting/foraging suitability); watersheds/AOI vectors for aggregation; DEM; precipitation/ET rasters; scenario rasters (baseline vs alternate LULC triggering sequestration/change calculation).
- Model families observed: Annual Water Yield (hydropower), Carbon Storage & Sequestration (with optional NPV economic valuation: price per metric ton, discount rate, price change rate), Coastal Blue Carbon (transitions + valuation), Coastal Vulnerability (habitat protection ranks), Crop Production (percentile/regression), Forest Carbon Edge Effect, Habitat Quality (degradation/quality/rarity), Habitat Risk Assessment (habitat×stressor criteria scoring), Nutrient Delivery Ratio (N/P retention), Crop Pollination (bee guilds), Recreation/Visitation (remote server model), Scenic Quality (viewsheds + valuation), Sediment/SDR family (truncated), plus utilities (DelineateIt watershed delineation, RouteDEM routing, Scenario Generator: Proximity-Based producing alternate LULC).
- Valuation is optional and parameterized per model (e.g., carbon: `do_valuation`, price, discount rate; scenic quality: `do_valuation`).
- Outputs: rasters/vectors/HTML summaries written to a workspace; aggregation over AOI polygons; results suffix for repeat runs.
- Heritage: "Older versions of InVEST ran as script tools in the ArcGIS ArcToolBox environment, but have almost all been ported over to a purely open-source python environment." BSD-licensed.
- Users (from positioning): decision-makers quantifying natural capital importance and tradeoffs between alternative choices.

### ARIES / ARIES for SEEA (BC3 + UN) — evidence layer A

- Platform self-description: "ARtificial Intelligence for Environment & Sustainability… a shared knowledge space… using the semantic web paradigm"; focus areas: Ecosystem Services ("quantify the benefits nature provides to society, guide policies"), Natural Capital ("understand, value, and effectively manage ecosystems and their services"), Semantic Modelling. Users: "government agencies, universities and NGOs on research and training"; ~6,000 active users claimed (vendor claim, not asserted).
- NCA explainer (official article): "Natural Capital Accounting (NCA) is a framework for measuring and recording natural assets, their condition, how they change over time, and the many benefits they provide to people and the economy. These benefits are known as ecosystem services…" — "NCA does not replace ecological knowledge with economics. Instead, it provides a common evidence base that allows nature to be considered alongside financial and social information when important decisions are made." — "Sometimes this involves monetary valuation, but more often, it combines ecosystem extent and condition, spatial information, and measures of ecosystem services. Monetary values are simply one way of expressing information, but not the aim itself."
- ARIES for SEEA Explorer (user guide, full operational detail): web application on the k.LAB Integrated Modelling Platform; also downloadable for recurrent users.
  - Context selection: geographic area (map boundaries / administrative regions per UN M49 / river basins per FAO; or name search via OSM), spatial resolution (m/km; capped by finest available data), years (single-year or multi-year change analysis; gap-filling from closest available year).
  - Account types: **Extent accounts** (area of IUCN Global Ecosystem Typology types / land cover, in km², with change over time); **Condition accounts** (condition variables in observed values → indicators rescaled 0–1 against optimal reference → condition index via weighted mean; currently forest condition, others planned); **Ecosystem services accounts in physical terms** (biophysical quantities of services "provided by ecosystems and used by economic units"; four services available, a fifth in development); **Ecosystem services accounts in monetary terms** ("applying SEEA EA-compliant valuation method(s)"; three services available).
  - Aggregation options (primary context only in current version; subregions/protected areas/river basins planned); temporal accounting (first/last year or all years).
  - Outputs: accounting tables (Excel) + maps (GeoTIFF) downloadable as a zip; auto-generated report per account (introduction, framework, methods, results summary, caveats, references); resources section listing every data resource used; dataflow view diagramming model components; SEEA-relevant indicator panel (SDG, CBD indicators) added as pseudo-accounts.
  - Transparency machinery: documentation view, data flow view, resources list — "to provide full-transparency on the final output."
- SEEA named as "the United Nations' international standard for integrating environmental and economic information"; ARIES for SEEA is the practice vehicle ("enables governments, businesses and researchers to develop Natural Capital Accounts that support better planning and decision-making").

### SENCE (Environment Systems) — evidence layer A

- Self-description: "SENCE evidences where land management action can deliver the greatest environmental, social and natural capital benefits"; "the market leading, natural capital tool for spatial evidence on carbon, water, biodiversity and ecosystem services"; "land suitability modelling technology" (used for agriculture too).
- Key features: up-to-date satellite Earth observation for land cover and habitat condition; flexible integration of local GIS and ground-based data; "action-focused spatial layers — habitat and opportunity maps designed to support decision-making, not just observation"; interactive web tool or integration into existing GIS workflows; export maps/statistics/reports or share interactive views.
- How it works: "provides scientifically robust evidence to show: where the environment is working well; where environmental risks are present; where action can be most effective." Spatial prioritisation "identifies where nature-based interventions strengthen resilience, enhance ecosystem services and nature networks… targeting actions for the greatest biodiversity and climate impact."
- Outputs: "quantified outputs for carbon, relative performance for other ecosystem services"; comparable "across locations and time"; scalable "from individual estates to regional or national assessments"; transparent/traceable data sources and processing; "repeatable & accurate — for long term monitoring with known uncertainty"; "Project outcomes can be modelled as future scenarios to understand how places can change over time"; guidance on land management options.
- Use cases named: landscape restoration, climate adaptation, carbon quantification, flood risk, water quality, urban and rural.
- Users listed: national governments (policy/planning), local authorities, master planners, water companies/catchment managers, conservation orgs/NGOs, estate owners and land managers, NbS/natural capital specialists, agricultural supply-chain teams, community partnerships, "project developers for carbon and nature credits", metric developers, consultants.
- Case studies: nature-based resilience (Anguilla), net-zero (Jersey), climate adaptation (Turks & Caicos), prioritising sites for woodland investment.

### i-Tree (USDA Forest Service + partners) — evidence layer A

- Mission: "Quantify the ecosystem services of trees and forests through assessment, understanding, and communication of their value." "i-Tree is the worldwide standard when it comes to quantifying the benefits that trees provide." Free tools + support; public/private partnership (USFS 1:1 cost match with Davey Tree; since 2006 cooperative initiative).
- Services quantified (homepage): trees "remove hazardous pollutants from the air… absorb carbon dioxide from the air to store as wood, and control storm water by intercepting and absorbing rainfall."
- Tool suite (asset-class-specific):
  - Individual trees: MyTree (easiest, quick assessment), i-Tree Design ("estimates tree benefits for the current year and up to 99 years in the future" — forecasting), i-Tree Eco (flagship; "accommodates tree inventory IMPORT or field data evaluation to derive individual tree benefit estimates"; Windows desktop).
  - Canopy area: OurTrees (community canopy, US), i-Tree Landscape (canopy + Census maps; "Identify priority planting & protection areas for your local needs"), i-Tree Canopy (random point sampling on aerial imagery to estimate land cover + benefits).
  - Planting: i-Tree Planting ("Make a case to invest in tree planting by estimating the value those trees will provide in coming years"), i-Tree Species ("Find species for your location based on their ecosystem services").
- Users: "urban forest practitioners, students of all levels, private companies, municipal leaders, homeowners."
- Operational note on site: USDA Forest Service funding policy change has "indefinitely halted traditional funding for i-Tree" (continuity risk; not definitional).

### GIST Impact (nature & biodiversity suite) — evidence layer A (marketing pages; Tier 2)

- Positioning: "Decision-grade, AI-powered data and intelligence for assessing impacts, managing risks and quantifying value"; impact valuation across natural, human, social, produced capitals (client quotes: Ørsted — "quantify our impact in monetary terms across natural, human, social, and produced capitals"; Wipro — "assessing and understanding the valuation and impacts of our natural capital").
- Nature suite modules (marketing): proximity to areas of biodiversity importance (KBAs, WDPA, IUCN Red List — "In partnership with IBAT"); ecosystem integrity (BII, MSA); Indigenous Peoples/community lands; "Dependencies on Ecosystem Services — the extent to which a business depends on 25 types of ecosystem services"; dependencies on commodities; "Pressures on Ecosystems — 13 types"; impact on biodiversity (Potentially Disappeared Fraction); "Impact on Society — Quantify how much business activities decrease the collective stock of natural capital, in monetary terms"; deforestation exposure; "Nature Value at Risk"; physical risks; nature-related opportunities (species threat abatement, restoration).
- Framework alignment: TNFD, PBAF, SFDR (+ CSRD/IFRS/GRI etc. on the reporting side).
- Data foundations: 20,000+ companies, 3M+ assets in 105 asset types (vendor claims — not asserted in final doc); portfolio aggregation; delivery via data feeds, API, web apps.
- Assessment: this is the finance-pole impact-valuation/nature-risk population the biodiversity pass already characterized. Its natural-capital content (monetary stock impact, ecosystem-service dependencies) is real but embedded in a broader impact-valuation product. Treated as boundary-informing: it straddles Natural Capital Management and Nature Risk Management.

### Capitals Coalition (framework, not a product) — evidence layer A

- Definition: "Natural capital: The stock of renewable and non-renewable natural resources that combine to yield a flow of benefits to people."
- Capitals Approach: organizations' success underpinned by natural/social/human capital; decisions offering "the greatest value across all capitals."
- Natural Capital Protocol: "a decision-making framework that enables organizations to identify, measure and value their impacts and dependencies on natural capital"; 4 stages: Frame (Why?) → Scope (What?) → Measure & Value (How?) → Apply (What Next?).
- Biodiversity framing: "Biodiversity constitutes the living component of natural capital" (Biodiversity Guidance); Navigation Tool steers practitioners through Frame/Scope/Measure & Value/Apply for "a biodiversity-inclusive natural capital assessment."
- SEEA recognized as the government-side standard (case studies: SEEA in China, Japanese ecosystem-service valuation & ecosystem asset accounts).

## Cross-product Comparison

| Dimension | InVEST | ARIES for SEEA | SENCE | i-Tree | GIST Impact |
|---|---|---|---|---|---|
| Unit of record | landscape (LULC + AOI/watersheds) per model run | accounting context (area × years × resolution) | land base (estate→national) | tree population / canopy area / planting project | company assets + their locations (portfolio) |
| Stock/condition representation | LULC rasters + biophysical tables | extent accounts (ecosystem types/land cover km²) + condition accounts (variables→indicators→index) | satellite-derived land cover + habitat condition layers | tree inventory / field data / canopy cover | asset locations + ecosystem integrity measures |
| Service quantification | per-service models (water, carbon, nutrients, pollination, habitat, coastal, scenic, recreation…) | services accounts in physical terms (biophysical quantities used by economic units) | quantified carbon + relative performance of other services | air pollutant removal, CO2 storage, stormwater interception (per tree/canopy) | dependencies on 25 ecosystem-service types; pressures (13 types) |
| Monetary valuation | optional per model (NPV, price, discount) | separate monetary services accounts, "SEEA EA-compliant valuation" | not emphasized (carbon quantified; others relative) | dollar benefit values | central ("decrease the collective stock of natural capital, in monetary terms"; NaV at Risk) |
| Change/scenarios | baseline vs alternate LULC; Scenario Generator | multi-year change; first/last or all years | future scenarios ("how places can change over time") | Design: up to 99-year forecast; Planting: future value | point-in-time + forward-looking metrics |
| Decision-serving outputs | tradeoff assessment between alternative choices; aggregated AOI results | accounting tables + maps + auto-reports (methods, caveats, references) | opportunity/priority maps; land management options guidance; dashboards | benefit estimates; priority planting/protection areas; investment case for planting | portfolio risk/opportunity analytics; framework-aligned reporting |
| Framework anchoring | none named (science models) | SEEA EA (UN standard) + SDG/CBD indicators | none named on page | none (peer-reviewed USFS science) | TNFD, PBAF, SFDR |
| Delivery form | open-source Python API + CLI (+ GUI heritage in ArcGIS) | web app (k.LAB) + downloadable | consultancy service + web tool + GIS integration | free web tools + Windows desktop | commercial data/API/web platform |
| Primary users | decision-makers, researchers, NGOs, governments | governments, businesses, researchers | governments, estates, water companies, developers, consultants | municipalities, practitioners, homeowners, students | corporates, investors, banks |

### Stable commonalities (evidence layer B, across ≥3 products)

1. A defined, spatially identified natural asset base is the subject of record (landscape/AOI, accounting context, land base, tree population, asset locations).
2. The asset base's stocks and condition are represented (LULC/extent/condition/inventory/canopy).
3. Ecosystem services are quantified from those stocks — biophysical quantities in all five; monetary in four of five (SENCE emphasizes relative performance instead).
4. Change is handled against baselines, scenarios, or time series (all five).
5. Outputs are decision-serving artifacts: maps, accounting tables, reports, priority/opportunity layers, investment cases (all five).
6. Geospatial substrate throughout (rasters/vectors/maps/satellite EO) (all five).
7. Transparency/methodology machinery where outputs face scrutiny (ARIES reports+dataflow; SENCE traceability; InVEST user guide per model; i-Tree peer-reviewed science attribution).

### Not universal (variant-level)

- Monetary valuation (SENCE de-emphasizes; ARIES explicitly says it is "not the aim").
- Standard-framework anchoring (SEEA: ARIES; TNFD/PBAF: GIST; none named: InVEST, SENCE, i-Tree).
- Organizational/portfolio subject (GIST) vs landscape subject (others).
- Free/public vs commercial delivery.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (smallest stable structure)

Three jointly-held structures:

1. **The natural asset base as the unit of record** — a defined, spatially identified stock of natural assets (land, habitats, vegetation, water bodies; or the natural capital attributable to an organization's footprint) whose extent and condition are held as data. Remove → generic GIS / land-cover inventory / environmental monitoring.
2. **Ecosystem-service quantification bound to that asset base** — the benefits the assets yield to people are computed/estimated as service flows, in biophysical terms and/or monetary terms. Remove → habitat mapping or biodiversity records without service valuation; a bare value-factor calculator without an asset base.
3. **The accounting/decision loop over change** — stocks and services are evaluated against baselines, alternative scenarios, or time periods, and rendered as outputs (maps, accounts, reports, priorities, investment cases) that feed decisions about how the asset base is managed. Remove → a static one-off service map with no decision frame; the "management" gone.

Jointly-held load-bearing tests:

- 1 alone = GIS layer stack / natural resource inventory.
- 2 without 1 = free-floating benefit calculator (no asset to manage).
- 3 without 1+2 = generic scenario/planning tool.
- 1+2 without 3 = service map atlas; assessment without the management loop.
- 2+3 without 1 = valuation rhetoric unanchored to any asset base.

Anti-overfit notes:

- **Monetary valuation is NOT definitional.** Direct evidence: ARIES's own NCA explainer — monetary values are "simply one way of expressing information, but not the aim"; SENCE delivers "relative performance for other ecosystem services" without monetization. The invariant is quantified service flows (biophysical and/or monetary).
- **SEEA EA / Natural Capital Protocol are NOT definitional.** InVEST, SENCE, i-Tree name no accounting framework; the framework layer is a common implementation for accounting-facing products.
- **Satellite EO is NOT definitional.** i-Tree runs on tree inventories and field data; InVEST on user-supplied rasters; paper-era inventories satisfy the core (see historical check).
- **Organizational subject is NOT definitional.** Four of five samples anchor to landscapes/trees, not companies.

### L1 — Common Mature Structure

- Geospatial substrate: map layers, GIS interoperability, satellite Earth observation.
- Monetary valuation as an option (NPV/price/discount parameters; monetary accounts; dollar benefit values).
- Scenario modeling and forecasting (baseline vs alternate; future scenarios; multi-year change; long-horizon forecasts).
- Prioritization / opportunity mapping (where action is most effective; priority planting/protection areas; tradeoff assessment).
- Accounting tables and structured outputs (extent/condition/services accounts; aggregated results per area).
- Reporting artifacts with methodology transparency (auto-generated reports with methods/caveats/references; traceable processing; peer-reviewed science attribution).
- Repeatable re-runs for monitoring over time (results suffixes; repeatable/accurate for long-term monitoring; multi-year accounts).
- Aggregation across scales (individual trees→city; estate→region→nation; asset→portfolio).

### L2 — Variant / Optional Structure

- Delivery form: open-source toolkit (InVEST) / standards web app (ARIES for SEEA) / consultancy-delivered service + web tool (SENCE) / free public tools (i-Tree) / commercial data platform (GIST).
- Asset-class specialization: trees/urban forest (i-Tree); coastal zones (InVEST coastal models); whole landscapes (InVEST/ARIES/SENCE).
- Customer pole: governments/policy (ARIES, SENCE), landowners/estates (SENCE), municipalities (i-Tree), corporates/investors (GIST), researchers (InVEST/ARIES).
- Framework alignment: SEEA EA, TNFD/PBAF/SFDR, Natural Capital Protocol — per product and audience.
- Valuation emphasis: biophysical-first (ARIES default framing, SENCE) vs monetary-first (GIST, i-Tree dollar values, InVEST optional valuation).
- Subject type: landscape vs organizational/portfolio.
- Credit/market linkage: some products serve "project developers for carbon and nature credits" (SENCE user list) — adjacent market machinery, not the Type.

### L3 — Vendor-specific (research notes only)

- InVEST: specific model roster (DelineateIt, RouteDEM, Scenario Generator: Proximity-Based), `execute(args)` API shape, workspace/file-registry outputs, ArcGIS script-tool heritage, BSD license, k.LAB-free.
- ARIES: k.LAB Integrated Modelling Platform, semantic-web/FAIR annotation, M49/FAO-basin context pickers, OSM name search, condition-account metric rescaling (0–1 vs optimal reference), SDG/CBD indicator panel, dataflow view, planned features (custom weights, subregion reporting, drag-and-drop inputs).
- SENCE: branded name, "15 years of operational experience", "100+ projects worldwide" (vendor claims), B-Corp/certifications.
- i-Tree: tool names (MyTree, Design, Eco, OurTrees, Landscape, Canopy, Planting, Species), 99-year forecast horizon, USFS/Davey 1:1 funding match, 2006 cooperative founding, USDA funding-lapse notice.
- GIST Impact: 20,000+ companies / 3M+ assets / 105 asset types / 25 service types / 13 pressure types (vendor claims), IBAT/NHM/Global Canopy partnerships, investor portal login.

## Historical / Market-Sample Check (§24)

Would older, regional, platform-native products still fit the L0?

- **Paper-era natural resource management**: a forest/watershed management plan built on a resource inventory (stocks + condition), economic valuation of timber/recreation/water benefits (service quantification), inventory updates and plan reviews over time (change), and a plan recommending actions (decision outputs). Satisfies all three L0 structures with no software, no satellites, no SEEA. ✔
- **Early government environmental accounting** (pre-SEEA-EA national resource accounts, water accounts): stocks + flows recorded per jurisdiction over time for policy. ✔
- **Regional tools**: UK habitat/opportunity mapping, US urban forestry benefit tools, continental European ecosystem-service mapping projects — all fit the landscape-anchored core. ✔
- The current disclosure-driven generation (TNFD/CSRD) shapes the corporate pole's outputs but is not the definition — same conclusion as the biodiversity pass.

Conclusion: L0 holds across eras and regions; no re-abstraction needed.

## Vendor-specific Findings

See L3 above. None promoted to the canonical core. GIST Impact's data-coverage figures are vendor claims and are not restated in the final document.

## Boundary Findings

1. **vs Biodiversity Management** (processed 2026-09-06) — **joint-review flag DISCHARGED from this side; keep both as separate Types.** Biodiversity management centers species/habitat records and the organization's impact/dependency interface (screening against reference datasets, primary observations, disclosure). Natural capital management centers natural asset stocks and their ecosystem-service flows (extent/condition → services → accounts/valuation → decisions). The Capitals Coalition's own framing supports the seam: "biodiversity constitutes the living component of natural capital" — biodiversity is a component the NCM lens may include, but the NCM unit of record is the asset stock and its services, not species/habitat impact records. Test: strip species/habitat impact/dependency machinery, keep service valuation/accounting → NCM; strip service valuation/accounting, keep species/habitat screening → Biodiversity Management. Overlap: geospatial condition data; both feed disclosure. GIST Impact straddles (its nature suite is the risk slice; its monetary natural-capital stock impact is NCM-adjacent) — consistent with the biodiversity pass's observation that finance-pole products legitimately fit either label.
2. **vs Nature Risk Management** (unprocessed sibling) — probable overlap on the finance pole: the risk-decision slice (screen → score → materiality → disclosure) vs NCM's valuation/accounting/planning loop. **Flag for joint review when that leaf is processed.** Test: remove risk-scoring/materiality emphasis, keep asset→service→accounting → NCM.
3. **vs Conservation Management** (processed 2026-09-07) — conservation delivers on-the-ground work (patrols, stewardship, restoration operations) with an adaptive-management cycle; NCM values, accounts, and plans but does not execute conservation operations. Test: remove valuation/accounting, keep work execution → Conservation Management. (Conservation pass already held this seam from its side.)
4. **vs Environmental Monitoring Platform** (processed 2026-09-08) — monitoring holds measurement points + physico-chemical time series; NCM holds asset stocks + service flows. NCM consumes monitoring/EO data as inputs; the unit of record differs.
5. **vs Carbon Accounting Platform** — carbon is one service among many in NCM (InVEST carries carbon models inside a service family; SENCE quantifies carbon alongside other services); carbon accounting centers organization GHG inventories/emissions machinery. Test: keep only the carbon service with GHG-inventory semantics → Carbon Accounting.
6. **vs ESG/Sustainability platforms** — KPI aggregation across topics vs asset-anchored service accounting. NCM outputs may feed ESG reporting (GIST shows the pairing) but the ESG platform lacks the asset/service/accounting machinery.
7. **vs GIS** — substrate, not the Type: ecosystem services, natural capital accounts, opportunity/priority semantics do not exist in a generic GIS (same reasoning as the biodiversity pass).
8. **vs Farm/Forestry Management** — production economics (yields, operations, contracts) vs natural capital services. SENCE straddles via land suitability for agriculture; the seam is purpose (production vs natural-capital evidence).
9. **vs Carbon/Nature credit market platforms** — transaction/registry machinery vs valuation/accounting evidence. SENCE's user list includes credit project developers: adjacent customers, not the Type.
10. **vs Environmental Impact Assessment Platform** — project permitting lifecycle vs asset accounting/planning continuity (same seam as biodiversity pass).
11. **vs Natural Resource Rights Management (§20)** — rights/tenure records vs stocks/services accounting. Rights may bound who can act on the asset base but are not the NCM unit of record.

## Taxonomy observation (for STATUS Boundary Issues)

- The leaf name says "management", but the observed market population is assessment/accounting/valuation/planning software; the management loop is decision support (priorities, investment cases, accounts feeding plans), not operational work execution. Operational execution belongs to Conservation Management / Farm & Forestry Management. Held as-is: the Type stands with "management" read as the decision loop (L0-3), consistent with how the sibling passes read "management".
- Probable overlap with Nature Risk Management on the finance pole remains flagged (sibling unprocessed).

## Uncertainties

- Category fuzziness: "natural capital management software" is not a self-aware shelf label; products self-describe as ecosystem-services mapping, natural capital tools, impact valuation, accounting applications. The sample spans five poles; a self-serve land-planning SaaS pole (Land App class) could not be fetched (transport errors ×2) and is described only via the consultancy-delivered SENCE pole — self-serve planning platforms may have richer register/plan machinery than observed.
- InVEST's Workbench GUI and User's Guide were unreachable (403/transport errors); model-level behavior is evidenced by the API/models documentation, but GUI workflow detail is unverified and the final document describes interfaces conceptually.
- GIST Impact observed only through marketing pages (Tier 2); no help center. Its inclusion is boundary-informing; no operational claims from it enter the final document beyond its clearly stated module semantics.
- Monetary-valuation prevalence: biophysical-first evidence (ARIES article, SENCE) vs monetary-first evidence (GIST, i-Tree dollar values). Held as a variant axis, not resolved into a market norm.
- i-Tree's funding continuity (USDA policy lapse notice) is a product-level operational fact, irrelevant to the Type definition.
- Regional products outside UK/US/EU/Spain not sampled.

## Final Synthesis

Natural Capital Management software is a coherent Type with a stable canonical loop, realized by five genuinely different product shapes:

```text
Defined natural asset base (landscape / estate / tree population / organizational footprint)
  → stocks & condition represented (extent, land cover, habitat condition, inventory)
  → ecosystem services quantified from those stocks (biophysical quantities; monetary optional)
  → change evaluated (baselines, alternative scenarios, time series)
  → decision-serving outputs (maps, accounts, reports, priorities, investment cases)
  → decisions about how the asset base is managed; re-assessment on cadence
```

Products differ by pole (open science toolkit / UN-standard accounting app / consultancy spatial evidence / free public asset-class tools / commercial impact-valuation data), by subject (landscape vs organization), and by valuation emphasis (biophysical-first vs monetary-first); all recognizable members implement L0's three jointly-held structures. The accounting frameworks (SEEA EA, Natural Capital Protocol) and disclosure regimes (TNFD and successors) shape current outputs but are not the definition.

L0 one-liner: **a system that holds a defined natural asset base as the unit of record, quantifies the ecosystem services those assets yield (biophysically and/or monetarily), and accounts for stocks and services against baselines, scenarios or time to produce the evidence that feeds decisions about how the assets are managed.**
