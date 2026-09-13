# Research Notes — Site Selection Platform

## Research Goal

Understand, from real products, what a Site Selection Platform is: what the unit of work is (candidate site? market? trade area?), what location evidence platforms aggregate and how they attach it to places, how comparative evaluation against an organization's criteria actually works, who uses these platforms and for what facility decisions, and how this Type separates from Property Listing Platform, Real Estate Development Management, Real Estate Investment Management, GIS/BI platforms, Lease Administration, and Retail Space Planning.

This pass also carries **two forward flags** from processed §17 siblings, to be discharged here:

1. **real-estate-development-management** (2026-09-09): "the sampled UK land pole straddles pooled land/planning/ownership data discovery + appraisal + site pipeline — proposed seam = location discovery as the product vs the development project of record with a money spine."
2. **real-estate-investment-management** (2026-09-09): "corroborates dev pass's proposed seam: pooled market/comps data discovery vs the firm's investment record; Dealpath Market Tracking/Connect straddle from this side."

## Initial Boundary

Working hypothesis at start:

- What: software used by organizations deciding where to locate a physical facility — retail/restaurant chains choosing store sites, healthcare systems siting clinics, franchise brands planning territories, corporate real estate choosing offices/industrial land, developers sourcing land, civic bodies siting services. The center is the evaluation of candidate locations, not the transaction or the construction.
- Who: corporate real estate / expansion teams, franchise developers, healthcare planners, commercial real estate analysts, economic development organizations, private equity evaluating markets.
- Confusable neighbors: Property Listing Platform (transaction marketplace), Real Estate Development Management (development project of record), Real Estate Investment Management (investment record with capital-and-returns spine), GIS platforms and BI (general analysis without siting semantics), Lease Administration (post-commitment), Retail Space Planning (post-site store layout), Dealpath-class deal management (straddle), Government GIS (civic geospatial administration).
- Unknowns going in: what the unit of record is (site? market? candidate?); whether the location data layer is definitional or just common; whether scoring/forecasting machinery is definitional; whether a candidate pipeline with stages is definitional; whether the landlord-side "void analysis" pole belongs here; how civic/healthcare configurations fit.

## Research Questions

1. What is the unit of work — the candidate site? the market? the trade area? How do the grains relate?
2. What location evidence do platforms aggregate (demand-side, supply-side, property/site attributes), and how is it attached to candidates (rings, drive times, observed trade areas, geographies)?
3. How does evaluation work — scoring/weighting, forecasting, fit/profile matching, gap/void detection, threshold screens? What is the output judgment?
4. Is a managed candidate pipeline with stages definitional, or a variant?
5. Who uses the platforms, and does the same machinery serve locator-side (brand choosing where to open) and landlord-side (landlord choosing which tenant) decisions?
6. Where exactly are the seams: vs Development Management (dev pass flag), vs Investment Management (REIM pass flag), vs listing platforms, vs GIS/BI?
7. Would older/regional/minimal products (paper-era site files, ring studies, checklists) still satisfy the definition?

## Representative Products

Selected for market representativeness, different product philosophies, different customer tiers, plus one deliberate boundary straddle:

| Product | Philosophy / pole | Customer tier | Evidence tier reached |
|---|---|---|---|
| Buxton (now "Audiense In-Person", platform: SCOUT) | Data-and-models service pole: consumer-profile-led site scoring, market capacity, healthcare industry models; consultant-led heritage since 1994 | Enterprise consumer brands, healthcare systems, restaurants, hospitality, private equity | Tier-2 product page (Buxton domain redirects to Audiense) |
| SiteZeus (Locate) | AI-forecast-led pole: predictive revenue models per site, white space, territory management, cannibalization; franchise/multi-unit focus | Franchise and multi-unit brands (QSR, retail, c-store, gym, services), private equity | Tier-2 product pages ×3 (home, Locate, Olympus data) |
| Esri ArcGIS Business Analyst | GIS-platform pole: analyst-driven tooling over bundled demographic/consumer/business data; sites, suitability, voids, thresholds as documented workflows | Analysts at retailers, healthcare, government, agencies; small business to enterprise | **Tier-1 documentation** (welcome + create-sites + suitability + void + threshold pages) |
| Placer.ai | Foot-traffic-first analytics pole: mobility data as the evidence base; self-serve; site selection one use case among many | SMB to enterprise self-serve (retail, CRE, restaurants, civic, finance, healthcare) | Tier-2 product pages ×3 (home, platform, CRE) |
| Dealpath (Market Tracking) | Boundary straddle: deal/investment pipeline of record whose market-data layer feeds evaluation — sampled to discharge the REIM flag | Institutional CRE investors, REITs, corporate real estate | Tier-2 product page (+ prior pass's evidence) |

Checked and not pursued: Tango/Tango Analytics (lease/transaction management — Lease Administration territory), SiteSeer (retail site selection, would duplicate the Buxton/SiteZeus pole), LandTech/LandInsight (UK land pole — already sampled by the development-management pass; used here only as recorded straddle evidence), CoStar/Crexi (listing/data marketplaces — Property Listing Platform territory).

## Sources

All fetched 2026-09-09. WebFetch (text/markdown).

- Buxton by Audiense — Location Intelligence & Analytics Platform page https://www.buxtonco.com/ (redirects to Audiense In-Person product page) (Tier-2)
- SiteZeus — homepage https://sitezeus.com/ (Tier-2)
- SiteZeus — Locate product page https://sitezeus.com/products/site-selection-software (Tier-2)
- SiteZeus — Olympus Data Exchange https://sitezeus.com/data (Tier-2)
- Placer.ai — homepage https://www.placer.ai/ (Tier-2)
- Placer.ai — Analytics Platform page https://www.placer.ai/products/platform (Tier-2)
- Placer.ai — CRE solution page https://www.placer.ai/solutions/cre (Tier-2)
- Esri — ArcGIS Business Analyst resources https://doc.arcgis.com/en/business-analyst/ (Tier-2 hub)
- Esri — BA Web App help: Introduction https://doc.arcgis.com/en/business-analyst/web/welcome.htm (Tier-1)
- Esri — BA Web App help: Create sites https://doc.arcgis.com/en/business-analyst/web/create-sites.htm (Tier-1)
- Esri — BA Web App help: Perform a suitability analysis https://doc.arcgis.com/en/business-analyst/web/suitability-analysis.htm (Tier-1)
- Esri — BA Web App help: Perform a void analysis https://doc.arcgis.com/en/business-analyst/web/void-analysis.htm (Tier-1)
- Esri — BA Web App help: Create threshold areas https://doc.arcgis.com/en/business-analyst/web/threshold-areas.htm (Tier-1)
- Esri — BA Web App help topic listing https://doc.arcgis.com/en/business-analyst/web/flisting.htm (Tier-1; reveals full workflow surface incl. Projects, Benchmark comparisons, Nearby analysis, Smart map search, Points of Interest Search, Data Browser, Custom Data Setup, Business Analyst Assistant, Tapestry Segmentation)
- Dealpath — Market Tracking https://www.dealpath.com/market-tracking/ (Tier-2; boundary evidence; product also sampled by the real-estate-investment-management pass)

No fetch failures this pass. Limitations: no Tier-1 help-center reached for Buxton (client platform gated), SiteZeus, or Placer.ai — their evidence is official but marketing-weight; assertions calibrated to structure level. Esri numeric parameters observed in docs (buffer limits, site caps, credit metering) are vendor-specific and kept out of the final document.

## Product A — Buxton / Audiense In-Person (key observations)

Evidence: Buxton domain landing (Audiense In-Person product page). [A]

- Positioning: "Since 1994, leaders in healthcare, restaurants, hospitality, and retail have relied on Buxton to support market planning, site selection, and location performance optimization." Rebranded packaging: "The Buxton location intelligence platform is now part of Audiense" as "Audiense In-Person."
- Capability blocks: **Site selection analysis** ("Score sites and analyze trade areas"), **Market optimization** ("Prioritize markets for expansion or resource allocation"), **Foot traffic analysis**, **Location optimization** ("Improve site-level performance"), **Mapping & reporting**, **Territory optimization analysis** ("Support franchise growth").
- **SCOUT** — "Buxton's web-based location analytics platform for market planning, whitespace analysis, and geographic reporting" with five named verbs:
  - Plan — "Determine how many locations a market can support for your brand and which trade areas offer the strongest opportunities."
  - Score — "Analyze the potential of a specific site based on the consumers, competitors, and conditions in its surrounding trade area."
  - Visualize — "Map and report on potential customers, competitors, trade area size, visitation patterns, and other location-specific data."
  - Optimize — "Identify locations where sales fall short of forecasted potential, so teams can focus marketing and operations efforts."
  - Grow — "more confident decisions as you expand, infill, relocate, or improve your physical network."
- Site-selection detail: "Visualize consumer concentrations, spot potential drive-time trade area overlap with your existing locations, identify competitive presence, find areas with friendly co-tenants, and more with user-friendly GIS-based tools." Sites include permanent locations, "a strategic pop-up, or... a seasonal experience."
- Consumer-profile-led evaluation: "Build customer profiles… Identify concentrations of potential customers that match your best-customer profile… **Compare markets, trade areas, and sites based on the presence of the consumers most relevant to your brand**."
- Scenario planning: "Toggle between multiple scenarios, such as aggressive expansion plans vs. conservative strategies, to see how the roadmap shifts."
- Portfolio calibration: "Score current locations and compare forecasted potential against actual performance to identify gaps across your portfolio."
- Healthcare configuration: "Facility site selection — Select from a library of industry models for a customizable scoring experience for popular service lines and facility types"; specialized data on "payor mix, demand, supply, and social determinants of health."
- Data claims: 44 billion foot traffic data points for retail POIs, 36 healthcare industry models, 50+ data sources; SOC 2 Type II + HITRUST attestation.
- Audiences: "Real Estate Planners — Improve site and expansion decisions"; "Private Equity Firms — Evaluate markets and growth potential."

## Product B — SiteZeus (Locate + Olympus Data Exchange) (key observations)

Evidence: homepage, Locate product page, Olympus data page. [A]

- Positioning: "AI-Powered Site Selection Software for Franchise & Multi-Unit Brands… Combining sophisticated data and AI-powered predictions to enable faster, more confident expansion decisions."
- Zeus.ai assistant: "analyzes markets, forecasts revenue, and recommends optimal sites for you at scale" — example prompts: "Find the best locations for expansion in Tampa," "Forecast revenue for my new site in Dallas," "Analyze competitor density near 5th Ave, NYC."
- Locate feature surfaces: **Sales Forecast Dashboard** ("AI-powered revenue predictions for any location"), **Browse Real Estate Listings** ("Find inventory that aligns with your brand's performance drivers"), **Territory Management** ("Draw and optimize custom territories"), **Sales Impact** ("Measure the impact of new sites on existing locations"), **Mobile Data** ("Track device activity and path-to-purchase patterns").
- Use cases: white space analysis ("projects revenue potential nationwide"); "Predict revenue for any site to make confident decisions about whether to **pursue or pass** on a potential location"; "Avoid sales cannibalization — Map your customers' paths to purchase and calculate how opening a new site or closing an existing one would affect sales at your nearby locations"; "Improve overall portfolio performance — Identify which locations to remodel, relocate, or close"; "Visualize trade areas — Tap into mobile location data from your locations' visitors to map their individual paths to purchase and visualize your true trade area"; "Map and analyze territories — Draw, edit, and analyze custom shapes… annotate, organize, share, and assign your polygons."
- Vendor's own FAQ definition of the category: "Site selection software is a powerful tool that helps businesses choose the best location for new stores based on various criteria such as demographics, competition analysis, foot traffic, customer presence, and more. It uses advanced analytics and data visualization to streamline the decision-making and increase the chances of success for a new location."
- **Olympus Data Exchange** (the data foundation "fueling every product"): foot traffic ("Estimated visit counts at over one million points of interest… Validate potential sites, benchmark competitors"), mobile location data ("Visualize the true trade area of a location with visit-based polygons and paths-to-purchase"), advanced customer segmentation, credit card spend, restaurant brand sales (store-level annual sales for QSR/FSR), traffic volume ("traffic counts for time of day and day of week… which side of the road gives you the best positioning"), social media behavior segmentation, demographics, retail category sales, consumer expenditures, population movement, healthcare insights.
- Suite decomposition (seam evidence): Locate (site selection) is sold **separately** from Customer Insights (consumer intelligence), **Build** (construction management — "managing unit openings, tracking budgets… from deal to opening day"), and **Sell** (franchise CRM). Vendor decomposes siting from downstream execution.
- Customer quote (Dave's Hot Chicken SVP Real Estate): "Having territory management included was important for us so we could analyze, review, and map where our stores were, which territories were available, and how many stores each territory could accommodate."

## Product C — Esri ArcGIS Business Analyst (key observations)

Evidence: resources hub + five Tier-1 help pages + topic listing. [A, Tier-1]

- Welcome: "a web-based app that applies GIS technology to extensive demographic, consumer spending, and business data to deliver on-demand analysis and presentation-ready reports and maps." Site selection named directly: "How can I improve my site selection to find an optimal location for my business expansion?" Capabilities: "Analyze trade areas. Identify new store locations. Find new customers. Refine marketing messages. Evaluate sites. Reveal untapped markets." "Thousands of variables available… analyze specific locations, geographic areas, or custom regions you create on the map."
- **Create sites** (Tier-1): "a **site** is an area where analysis is performed." Three forms: point + buffers (rings, drive time, walk time, with bands; travel modes incl. trucking; traffic-aware), standard geographies (states/counties/ZIPs/tracts…), or drawn polygons. "By default, sites are stored in the project under Point locations (sites), Polygons (sites), and Geographies (sites)." Sites carry **attributes** ("site attributes for the default fields specified when creating the project"), photos, notes, attachments; run infographics/reports per site; "Move item — Move the site to a different layer in the same section of the project. You can also move the site to a different project."
- **Suitability analysis** (Tier-1): "identifies sites that meet criteria you define. First, select sites to include in the analysis, and choose and weight your criteria. The workflow **ranks your sites** — displayed as color-coded symbols on the map — and **adjusts the rankings as you add, remove, or change weights of criteria**." Criteria sources: data-browser variables (curated industry lists), saved custom lists, **site attributes** ("numeric fields, such as square footage or rent"), and **point layers** ("Count of points option to rank your sites based on the number of competitor locations within the area"; distance-to-nearest-point). Influence modes: Positive / Inverse / Ideal (ideal-value targeting). Scoring methods (preset preprocessing/combination; 0–100 scaling). Weighting: "The selected criteria are weighted equally by default. **Changing the weight of criteria significantly impacts the results and is a subjective part of the analysis. If you change the weight of criteria, it should be driven by domain knowledge and documented justification.**" Results pane: summary (top/bottom five ranked sites with per-variable score decomposition), histogram, bubble chart/scatterplot with regression, correlation matrix, table; save as layer, export to Excel/infographic. Location types: your sites, map features, standard geographies, or hexagons (market-grain and site-grain evaluation in one workflow). Use cases: laundromat expansion submarket ranking; "Rank census block groups to find the area most in need of new affordable housing" (civic configuration).
- **Void analysis** (Tier-1): "analyzes an area you choose (the analysis area) to detect **voids and gaps** in specific businesses and services, compared to another area (the reference area). A void means that a business or business type exists in the reference area but not in the analysis area, and a gap means that there are fewer of these businesses in the analysis area than in the reference area." Business categories, single brands, or custom lists; use case: "Assess market competition for a new juice bar location… whether your area of interest has a gap in juice bar businesses that a chain can fill by opening a new location."
- **Threshold areas** (Tier-1): "rings or drive times around a site that contain a specified amount of a variable… starts from the site locations you specify and expands outward until the threshold is met." Use case: "Perform market analysis to determine a new health food store location. Create a threshold area of 25,000 people for each of your potential new health food store locations. **Compare the threshold areas to see which potential location is most competitive**."
- Full workflow surface (topic listing): Projects, Benchmark comparisons, Nearby analysis, Smart map search, Points of Interest Search, Color Coded Maps, Data Browser, Custom Data Setup, infographics/reports builders, Business Analyst Assistant (AI), Tapestry Segmentation, data apportionment, hexagons, dashboards/sharing (PDF, image, Story Map, ArcGIS Dashboards).
- Delivery surfaces: Web App, Mobile App ("create and compare sites, run infographics"), ArcGIS Pro extension ("site evaluation, territory design"), Enterprise. License tiers gate advanced workflows (vendor fact).

## Product D — Placer.ai (key observations)

Evidence: homepage, platform page, CRE solution page. [A]

- Positioning: "Market Intelligence for the Physical World… Optimize Decision-Making with Advanced Location Analytics"; FAQ: "the leading location analytics platform describing physical locations, the people and businesses that interact with them, and the markets they inhabit." 4,000+ customers; self-serve signup; API + Data Feeds + Data Marketplace; mobile apps; data "refreshes daily" from "a panel of tens of millions of devices."
- Platform objects: **specific properties** ("Discover a location's **True Trade Area**: a precise, behavior-based view of the geographic area visitors come from… not arbitrary radius rings"; visit metrics/trends; audiences; customer journey & loyalty), **chains** (portfolio metrics, ranking), **industries**, **markets** (population & visitors, workforce & commuters).
- Site selection as named use case: FAQ — "Common use cases include: **Where should I open my next location?** … What tenants are missing from my trade area?"
- CRE solution page: "**Optimize Site Selection** — Leverage Placer's **site selection report** to help clients identify top locations for expansion. The report combines demographic, psychographic, and foot traffic analysis and highlights ideal sites for retailers that most effectively reach target audiences, **with minimal cannibalization risk**." Landlord-side pole: "**Attract the Right Tenants** — Identify ideal tenants based on demographic fit, cannibalization risk, and co-tenancy scoring with Placer's **Void Analysis**." Property data: "aggregated property details, including tax information, ownership details, and zoning information for your financial modeling." Office/industrial siting: "help you acquire or develop sites in close proximity to your target labor force"; "Track Utilization of Industrial Sites… ports, airports, and railyards."
- No candidate-pipeline surface observed: analysis attaches to any POI/property the user pulls up; the "site selection report" is a generated deliverable, not a persistent stage-managed pipeline (as far as the observed surface shows).

## Product E — Dealpath, Market Tracking (boundary evidence) (key observations)

Evidence: Market Tracking page. [A] (Product center documented by the REIM pass.)

- "Identify trends in real time, capture opportunities, penetrate new markets, and **bring clear, data-backed recommendations to the investment committee**."
- "a unified view of pipeline activity, brokered and off-market opportunities, and external market signals like **OMs, sale comps, and lease comps** in one place, structured for action."
- Machinery: AI Extract ("extracts relevant listing and property details, comps, and financials from offering memoranda… to streamline screening & deal evaluation, or to build your database of market data"); Dealpath Connect ("investment opportunities from the top institutional brokerage firms flow directly into your pipeline, filtered by the markets, asset types, and strategies you care about"); "Tag, structure, and store deal records, lease and sale comps, loan data, and past underwriting"; "Integrate with RCA, CompStak, and ESRI."
- Center of gravity remains the deal/investment record (pipeline → underwriting → IC → fund allocation → owned assets; per REIM pass). Market Tracking is the **discovery/data layer feeding that record**, not a siting-evaluation center: no trade-area machinery, no consumer/demand modeling, no site scoring observed.

## Cross-product Comparison

| Structure | Buxton/SCOUT | SiteZeus Locate | Esri BA | Placer.ai | Dealpath (boundary) |
|---|---|---|---|---|---|
| Candidate locations as the working subject | Yes (score/evaluate specific sites; pop-ups/seasonal too) | Yes ("any site"; pursue-or-pass; listings to shortlist) | Yes (sites as persisted objects w/ attributes, photos, notes, per-site reports) | Partial-as-observed (any property/POI pulled into analysis; site selection report; no formal pipeline surface) | Yes, but candidates are *deals* on the investment pipeline |
| Location evidence layer attached to geography | Yes (consumer profiles/lookalikes, foot traffic, competitors, co-tenants, trade areas; 50+ data sources claim) | Yes (Olympus: foot traffic, mobile/trade areas, spend, sales, traffic counts, demographics, healthcare) | Yes (thousands of demographic/consumer/business variables; POI search; custom data; Tapestry) | Yes (visitation, true trade areas, audiences, journeys; tax/ownership/zoning property details) | Yes (OMs, sale/lease comps, RCA/CompStak/Esri overlays) |
| Comparative evaluation vs the locator's criteria | Yes (site scoring vs industry models; market capacity; forecast-vs-actual; what-if scenarios) | Yes (AI revenue forecast per site; white space; sales impact/cannibalization) | Yes (suitability ranking with weighted criteria; void/gap; threshold screens; benchmark comparisons) | Yes (site selection report ranking ideal sites w/ cannibalization risk; void analysis; co-tenancy scoring) | Screening/underwriting vs investment criteria (not siting criteria) |
| Trade-area machinery | Yes (drive-time trade areas, overlap with existing locations) | Yes (visit-based true trade areas, paths-to-purchase) | Yes (rings/drive/walk-time buffers, bands, geographies) | Yes (observed visitor-origin "True Trade Area", explicitly anti-ring) | No (market-level comps view) |
| Market/territory grain screening | Yes (market optimization, whitespace, territory optimization for franchise) | Yes (white space nationwide; territory draw/assign; stores-per-territory) | Yes (suitability over geographies/hexagons; threshold areas; territory design in Pro) | Yes (market-level population/visitation; chain/industry rankings) | Market selection as investment filter |
| Cannibalization / network impact | Yes (trade-area overlap w/ existing locations; forecast-vs-actual gaps) | Yes (sales impact; open/close cannibalization calculation) | Partial (nearby analysis; overlap visible via buffers) | Yes ("minimal cannibalization risk"; co-tenancy) | No |
| Performance forecasting / models | Yes (industry model library; healthcare service-line models) | Yes (AI revenue predictions per site) | Partial (scoring models user-configured; no vendor sales-forecast model observed) | Partial (empirical benchmarks; no revenue forecast observed) | Underwriting models on deals (REIM content) |
| Candidate pipeline w/ stages | Not observed as stages | Not observed as stages (pursue/pass judgment) | Not observed as stages (projects hold site sets) | Not observed | Yes — deep (deal stages, IC gates) — but that is the REIM core |
| Existing-portfolio optimization | Yes (locations short of forecasted potential) | Yes (remodel/relocate/close) | Partial (sites can be existing locations) | Yes (chain ranking, underperformers) | Yes (Portfolio Insights — owned assets) |
| Map-centric working surface | Yes | Yes (heat maps, territory shapes) | Yes (color-coded maps, symbols by rank) | Yes | Yes (map of pipeline/market activity) |
| Real estate listings ingestion | Not observed | Yes ("Browse Real Estate Listings… aligns with your brand's performance drivers") | Not observed (POI search; import files) | Partial (property details; not a listings feed) | Yes (Connect private exchange → pipeline) |
| Reporting/export deliverables | Yes (mapping & reporting; board-style) | Yes (dashboards) | Yes (presentation-ready reports, infographics, Excel, PDF, dashboards) | Yes (site selection report; exports; API) | Yes (IC-ready reporting) |
| AI assistance | Era-current (platform packaging) | Yes (Zeus.ai conversational analyst) | Yes (Business Analyst Assistant) | Era-current (positioning) | Yes (Dealpath AI, AI Extract) |
| Territory design/assignment | Yes (franchise territories) | Yes (draw/assign polygons) | Yes (territory design in Pro) | Not observed as module | No |

Reading of the matrix:

- **All five products hold a location-evidence layer anchored to geography and serve some form of comparative evaluation of places** — including the boundary product (Dealpath), whose evidence layer (OMs/comps) feeds investment screening rather than siting fit (Layer B).
- **The candidate-site population as the working subject is present at all siting-native products**, but its *persistence form* varies: persisted attributed site objects (Esri), scored candidate sets (Buxton/SiteZeus), or per-analysis property selection without a formal pipeline (Placer as observed). A stage-managed candidate pipeline is NOT definitional — it appears strongly only at the deal-pole straddler (Layer A/B).
- **Two evaluation grains coexist everywhere**: market/area grain (white space, market capacity, territory design, geography ranking) and site grain (score/forecast a specific address). Same machinery, two grains — a within-Type axis, not a Type split (Layer B).
- **Cannibalization/network-impact analysis is common-not-definitional** (strong at Buxton/SiteZeus/Placer, partial at Esri, absent at Dealpath) — it exists only for locators that already operate a network (Layer B).
- **Forecasting depth is a philosophy axis**: vendor industry models (Buxton), AI-predicted revenue (SiteZeus), user-configured scoring (Esri), empirical benchmarks only (Placer) (Layer A; product-specific depths).
- Listings ingestion is common-not-definitional (SiteZeus, Dealpath, Placer-adjacent; absent at Buxton/Esri observed surfaces) (Layer B).

## Canonical Model

Three jointly-held structures (the defining core):

1. **Candidate locations under evaluation.** A working population of identified places — sites (addresses/parcels), areas, or whole markets — brought into the platform as candidates for locating a facility, held as the subjects the platform's evidence and judgment attach to. The population may persist as attributed site records organized in projects/workspaces, be scored as a standing candidate set, or be assembled per analysis; whether it carries a stage-managed pipeline is a variant.
   - Remove → a market-data service or BI dashboard with no candidates; or a bare address list / deal tracker.

2. **Location evidence attached to geography.** An evidence base about the candidates and their surroundings, attached through evaluation geographies (trade areas, buffers/rings, standard geographies, observed-visitor polygons): demand-side data (demographics, consumer profiles/segments, foot traffic/mobility, spending), supply-side data (competitors, co-tenants, business counts, traffic), and site/property attributes (size, rent, zoning, access — vendor-supplied or user-collected from site visits).
   - Remove → an opinionated scoring rubric with no evidence, or a plain map/list.

3. **Comparative evaluation against the locator's own criteria.** Machinery that turns evidence into a selection-grade judgment across candidates: weighted-criteria scoring and ranking, performance forecasting, best-customer/profile fit matching, gap/void detection, threshold screens — producing the pursue / pass / prioritize output that precedes commitment of capital. Criteria and weights are the organization's, not the vendor's.
   - Remove → a data feed or map viewer; the "selection" half of the name is gone.

Jointly-held load-bearing:

- 1 alone = an address list / pipeline tracker (CRM/deal-tracker territory).
- 2 alone = a location-data product / market analytics service (foot-traffic or demographics vendor).
- 3 alone = a generic scoring or decision-matrix tool.
- 1+2 without 3 = a data-enriched address book.
- 1+3 without 2 = checklist scoring with no evidence base (degenerate; paper-era practice still gathered evidence, so leg 2 includes user-collected site data).
- 2+3 without 1 = market research / analytics with no candidates under decision (the pure-data pole; in practice the sampled analytics products still attach evaluation to specific properties the user is considering).

## Abstraction Hierarchy (internal)

### L0 — Defining Invariant
- (1) candidate locations under evaluation (identified places held as the subjects of siting work)
- (2) location evidence attached to the candidates' geography (demand, supply, and site/property attributes, attached via trade areas/buffers/geographies)
- (3) comparative evaluation against the locator's own criteria producing a selection-grade judgment (pursue/pass/prioritize)

### L1 — Common mature structure
- Map-centric workspace (candidates color-coded by score/rank on a map)
- Trade-area definition machinery (rings, drive/walk-time polygons, observed visitor-origin polygons)
- Market/territory screening at coarser grain: white-space analysis, market capacity ("how many locations a market can support"), territory design/assignment for franchise networks
- Cannibalization / sales-impact analysis against the existing network (for locators that operate one)
- Performance models and forecasting; forecast-vs-actual calibration on opened/owned sites
- Comparison and reporting surfaces: side-by-side tables, benchmark comparisons, presentation-ready reports/infographics, Excel/PDF export
- Portfolio optimization of existing locations (remodel/relocate/close, underperformer detection)
- Projects/workspaces organizing evaluation work; per-site documents (photos, notes, attachments)
- Data access layers: bundled datasets, data marketplaces, APIs/feeds; listings/POI ingestion
- Mobile companion apps; AI assistants over the same data

### L2 — Variant / optional
- Industry packs: healthcare service-line models / payor-mix & SDOH data; restaurant/retail/c-store vertical packs
- Locator-side vs landlord-side direction (brand choosing where to open vs landlord recruiting tenants via void/co-tenancy scoring — same machinery, opposite seat)
- Civic/public configuration (ranking areas for affordable housing, service siting)
- Candidate-pipeline form: persisted attributed site objects vs scored candidate sets vs per-analysis assembly vs stage-managed pipeline (the deal-pole straddle)
- Real estate listings ingestion and private exchange feeds
- Data substrate philosophy: vendor panel mobility data vs census/business datasets vs credit-card spend vs broker comps vs user-collected site data
- Geography/coverage of datasets (US-centric in sample; country dataset switching)
- Self-serve no-code vs consultant/managed-analytics delivery; licensing/credit metering; cloud/web/mobile/desktop surfaces

### L3 — Vendor-specific (research notes only)
- Buxton: SCOUT platform name; Audiense In-Person packaging; Plan/Score/Visualize/Optimize/Grow verb set; 44B foot-traffic points / 50+ data sources / 36 healthcare models claims; SOC 2 Type II + HITRUST; "since 1994" heritage
- SiteZeus: Zeus.ai assistant; Olympus Data Exchange name; Locate/Customer Insights/Build/Sell stack; "one million points of interest"; "which side of the road" traffic framing; brand clientele (Raising Cane's, Dave's Hot Chicken, Pizza Hut quotes)
- Esri: site-object storage taxonomy (Point locations/Polygons/Geographies (sites)); suitability influence modes (Positive/Inverse/Ideal) and preset scoring methods; Advanced-license gating of suitability/void/threshold; credit-consumption metering; buffer limits (rings ≤1,000 mi; drive time ≤300 min); 5,000-site / 1,000-feature analysis caps; 10-site threshold cap; Tapestry Segmentation; hexagons; Business Analyst Assistant; Web/Mobile/Pro/Enterprise delivery
- Placer.ai: "True Trade Area" branding ("not arbitrary radius rings"); site selection report; Void Analysis naming; "data refreshes daily"; "tens of millions of devices" panel; 4,000+ customers; free tools (Chain Analysis, Placer 100, Migration Trends)
- Dealpath: AI Extract; Dealpath Connect private listing exchange; Market Tracking module; RCA/CompStak/Esri integrations; IC-oriented framing

## Vendor-specific Findings

See L3. Structural notes: (a) Buxton's rebrand under Audiense shows the category being bundled into broader "consumer intelligence" suites — the siting platform survives as a named capability block inside a larger product; (b) SiteZeus's own suite decomposition (Locate vs Build vs Sell) is vendor-confirmed evidence that siting, construction, and franchise sales are separate product surfaces; (c) Esri's suitability/void/threshold workflows show the same core realized as analyst-driven tooling with user-configured models rather than vendor-owned predictive models; (d) Placer shows the data-first pole where siting is one use case of a general location-analytics platform — the defining core is present in use, while the candidate population may not persist as a formal pipeline; (e) Dealpath shows the deal-pole straddle — its Market Tracking layer is structurally the "location evidence + discovery" leg, but the record center is the investment, so the product sits in Real Estate Investment Management territory.

## Boundary Findings

1. **vs Real Estate Development Management (§17, processed) — FORWARD FLAG DISCHARGED, keep-both RATIFIED.** The dev pass's proposed seam — "location discovery as the product vs the development project of record with a money spine" — holds from this side. None of the siting-native products (Buxton, SiteZeus, Esri BA, Placer) holds a development project record, a cost/commitment structure, or a construction arc; evaluation output is a pursue/pass judgment before commitment. SiteZeus sells construction/unit-opening as a **separate product** (Build) — vendor decomposition corroborates the seam. The dev pass's UK land pole (land/planning/ownership data discovery + appraisal + site pipeline) straddles exactly on this seam: while the product's center is discovering and appraising candidate land, it is siting work; once a site becomes a development project carried through a staged lifecycle with a cost/commitment spine, it is Development Management. Removal tests: strip the development arc + money spine from a development product → land sourcing/evaluation remains (this Type); strip candidates/evidence/evaluation from a siting product → it is not a development system.

2. **vs Real Estate Investment Management (§17, processed) — FORWARD FLAG DISCHARGED, keep-both RATIFIED.** The REIM pass's proposed seam — "pooled market/comps data discovery vs the firm's investment record" — holds from this side with Dealpath as the named straddler. Dealpath's Market Tracking/Connect provide exactly the evidence-and-discovery layer this Type centers on (structured market signals, comps, OMs flowing into evaluation), but the record center is the **investment** (deal → underwriting → IC → fund allocation → owned asset with capital-and-returns spine; per REIM pass), and its screening criteria are investment criteria (underwriting, returns), not siting-fit criteria (demand/trade-area/site characteristics). The siting-native products carry no capitalization/returns machinery and no held-asset record. Corroboration: Dealpath integrates **Esri** as a market-data overlay — the market itself treats the siting layer as a data feed into the deal record, not the same Type.

3. **vs Property Listing Platform (§17).** Listings appear inside this Type as candidate supply (SiteZeus "Browse Real Estate Listings — find inventory that aligns with your brand's performance drivers"; Dealpath Connect at the deal pole), but the listing platform's center is marketing/transacting properties between lister and seeker; the siting platform's center is evaluating locations against the locator's criteria. Sourcing-limitation note: property-listing-platform was processed separately (2026-09-09 batch logs); no conflict recorded with that pass.

4. **vs GIS platforms (generic) and Business Intelligence (§13).** Esri BA is GIS-family, but this Type is the productized siting configuration: named site objects, suitability ranking, void/threshold workflows, bundled siting datasets. General GIS or BI without candidate-siting semantics (no candidates, no selection judgment) is not this Type. The directory has domain-specific GIS leaves (Agricultural/Utility/Government GIS); this leaf covers the siting platform regardless of GIS substrate.

5. **vs Lease Administration / Commercial Property Management (§17).** Downstream of the decision: the siting platform's output is a recommendation before commitment; lease/property systems start at the executed lease/operating asset. No lease records, rent rolls, or operations in any sampled siting product.

6. **vs Retail Space Planning (§05.13).** Post-site store layout/assortment vs site choice. Different object (the store interior vs the location).

7. **vs Market Research Platform / Consumer Research (§06) and Marketing Analytics.** The evidence layer overlaps (consumer profiles, demand estimation), but those Types center research programs/campaign measurement, not candidate siting decisions; siting platforms exist to rank and select places. Buxton's absorption into a consumer-intelligence suite shows the adjacency without merging the Types.

8. **vs Dealpath-class deal management (REIM/§17-adjacent).** Covered in finding 2; the deal pole's pipeline-of-record machinery (stages, IC gates, due-diligence tasks) is the REIM core, not the siting core.

9. **Naming-collision note — clinical trial "site selection" (§22).** The CTMS pass recorded feasibility/site-selection analytics as an adjacent sponsor-side capability for choosing **investigational sites** (trial locations). That is a different domain object (trial sites/protocol feasibility), not facility siting; no merge. Recorded to prevent future confusion.

10. **Forward note — Government GIS (§24, unprocessed).** The civic configuration of this Type (ranking areas for service placement, e.g., Esri's affordable-housing suitability use case) shares machinery with government GIS work. Expected seam: Government GIS centers on the government's geospatial data administration/infrastructure; this Type centers on the locator's candidate-evaluation loop. Ratify at that pass if needed.

## Historical / Market-Sample Check (§24)

Paper-era site selection practice: a retailer's site-selection file with candidate addresses, hand-drawn drive-time/ring maps over census-tract printouts, traffic-count sheets, site-visit checklists and photos, and a scoring grid comparing candidates against the chain's criteria — satisfies all three L0 legs with no software machinery (candidates = site files; evidence = census/traffic/visit data attached to places; evaluation = comparative scoring toward a pursue/pass decision). Regional checks: UK land-sourcing products (LandInsight-class, per the dev pass) fit; healthcare facility planning with service-line models fits; civic area-ranking fits; franchise territory planning fits. The definition names no maps, no foot-traffic data, no AI, no weighted-suitability mathematics, no stage labels, no geography, and no industry — rings-on-paper and visit-note evidence satisfy leg 2. Pass.

## Uncertainties

1. **Tier-1 operational documentation reached only at Esri.** Buxton/SiteZeus/Placer evidence is official but marketing-weight (Tier-2). Structure-level assertions only; no numeric limits, default values, or state vocabularies asserted in the final document from these vendors.
2. **Placer.ai candidate-persistence form** is uncertain: no candidate-pipeline surface observed, but the product may persist saved/organized analyses behind the marketing surface; characterized as "per-analysis assembly" with a hedge.
3. **Landlord-side (void/tenant-recruitment) depth**: observed at Placer (Void Analysis, co-tenancy scoring) and Esri (void analysis mechanics); whether landlord-side users constitute a distinct customer population with distinct workflow depth was not fully verifiable — held as a variant axis.
4. **Buxton product internals** (SCOUT help center is client-gated): the SCOUT verb set comes from the product page; internal object model unverified.
5. **Dealpath's siting relevance** is deliberately partial: it sampled well as the boundary straddle, but corporate-real-estate "site selection" workflows inside deal-management products were not independently deep-sampled this pass (relied on REIM pass's product evidence).
6. **Non-US coverage**: all sampled data layers are US-centric in their public copy; international siting data products (e.g., UK land data) enter only via the dev pass's recorded sample — no independent evidence gathered.

## Final Synthesis

Site Selection Platform = the locator's evaluation system for siting decisions: a working population of **candidate locations** (sites, areas, or markets under consideration for a facility), each carrying **location evidence attached to its geography** (demand-side, supply-side, and site/property data bound through trade areas/buffers/geographies — vendor datasets, mobility feeds, comps, or user-collected site data), worked through **comparative evaluation against the locator's own criteria** (weighted scoring/ranking, forecasting, profile-fit matching, gap/void detection, threshold screens) to a selection-grade judgment — pursue, pass, or prioritize — before capital is committed. Mature products add the map-centric workspace, market/territory screening (white space, market capacity, territory design), cannibalization/network-impact analysis, forecast-vs-actual calibration on the existing portfolio, comparison/reporting deliverables, data marketplaces/APIs, and AI assistance. The Type realizes across four poles — data-and-models service (Buxton), AI-forecast-led brand tool (SiteZeus), GIS analyst tooling (Esri BA), mobility-data-first analytics (Placer.ai) — plus a deliberate straddler at the deal pole (Dealpath) whose market-data layer feeds an investment record. The seams are held by the record center: siting products evaluate places and end at the pursue/pass judgment; Development Management holds the project with the cost/commitment spine; Investment Management holds the investment with the capital-and-returns spine; listing platforms transact; lease/property systems operate what was chosen.

Status: leaf validated as a coherent, independent Application Type. No taxonomy change. Both §17 forward flags (real-estate-development-management, real-estate-investment-management) discharged with keep-both ratified. Consistency note recorded vs clinical-trial site selection (naming collision only); forward note left for Government GIS (§24).
