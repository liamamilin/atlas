# Research Notes — Integrated Workplace Management System / IWMS

Directory location: §17 Construction, Real Estate & Facilities (after "Coworking / Flexible Workspace Management", before "Facility Management System")
Slug: integrated-workplace-management-system-iwms
Research date: 2026-09-08

## Research Goal

Understand what an Integrated Workplace Management System (IWMS) actually is as an Application Type: what its system of record is, which management domains it integrates, what "integrated" means operationally, who uses it and for which decisions, which capabilities are definitional vs merely common in the current market, and where its boundaries sit against the dense sibling neighborhood (Facility Management System, Space Management, Lease Administration, Workplace Management Platform, CMMS/EAM, BMS, property management, energy management).

## Initial Boundary

Working hypothesis before research:

- An IWMS is the occupier organization's enterprise suite integrating real estate & lease management, space management, facility operations/maintenance, and (commonly) capital projects and sustainability on one shared record base.
- Closest neighbors: Facility Management System (§17 sibling — proposed seam from that pass: IWMS = integrated multi-domain suite of record, FMS = estate-anchored operational service loop regardless of packaging); Space Management Platform (processed — module relationship); Workplace Management Platform (§10 — label drift flagged: suite vendors use "workplace management" for the integrated platform); Lease Administration (domain inside); CMMS/EAM (machinery); BMS (OT control layer); Commercial Property Management (landlord side); ERP (finance backbone).
- Pre-hung flags to discharge: (1) FMS pass — "JOINT REVIEW REQUIRED with integrated-workplace-management-system-iwms"; (2) workplace-management-platform pass — "LABEL-DRIFT boundary recorded for the unprocessed IWMS leaf: … the IWMS pass should separate by the suite-of-record criteria".

Pre-hung notes from sibling passes reused as context (not as evidence for this pass's claims):

- facility-management-system pass: "IWMS = enterprise-suite packaging integrating real estate + space + facility/maintenance + capital + sustainability as named modules (Planon's own module list is the exemplar)… proposed seam: IWMS defined by the integrated multi-domain suite (RE portfolio + space + FM + sustainability as one system of record), FMS defined by the estate-anchored operational service loop regardless of suite packaging. Note: Planon now brands away from 'IWMS' ('Smart Sustainable Building Management') — naming drift to record."
- workplace-management-platform pass: "suite vendors use the same words for the integrated space+facility+real-estate platform of record (FM:Systems 'complete Workplace Management Platform' = OpenBlue IWMS families incl. Space Management/Move Management/Facility Maintenance/Asset Management/Real Estate & Lease; Eptura 'IWMS for complex environments' + Archibus) — the IWMS pass should separate by the suite-of-record criteria."
- space-management-platform pass: "IWMS (§17) will likely bundle it with facility maintenance/assets/lease — keep-both/module relationship, not duplicates."

## Research Questions

1. Which management domains do IWMS products actually ship, and which are universal vs variable?
2. What does "integrated" mean operationally — single database/platform? What breaks when domains are bought separately (point solutions)?
3. What is the system of record — what objects does it hold (properties, leases, spaces, assets, projects, meters)?
4. Who are the users, and what decisions does the system serve (operational vs tactical vs strategic)?
5. What cross-domain workflows exist (move management, lease events driving space decisions, capital projects handing over to operations)?
6. Boundaries: vs FMS, space management, lease administration, workplace management platform, CMMS/EAM, BMS, property management, ERP.
7. Historical check: do pre-suite and CAFM-era products fit the definition? Is the modern module set (esp. sustainability, workplace experience) being over-fitted into the definition?

## Representative Products

Selection rationale: market representation (all four are recognized leaders in the IWMS category), documentation completeness at product-page level, different product philosophies (monolithic suite / platform-of-apps / product families), different heritages (RE+capital heavyweight, European FM suite, CAD-integrated classic, space/CAFM lineage), different customer tiers (corporate, government/FedRAMP, higher education).

| Product | Vendor | Pole | Customer tier / segment | Evidence tier reached |
|---|---|---|---|---|
| IBM Maximo Real Estate and Facilities (evolution of IBM TRIRIGA) | IBM | North American enterprise RE+lease+capital heavyweight, now inside Maximo Application Suite | corporate real estate, government (FedRAMP), healthcare, education | Tier 2 (product page; docs portal 403) |
| Planon Integrated Workplace Management Solution | Planon | European enterprise suite ("Smart Sustainable Building Management"), four named modules on one platform | corporates, universities, municipalities, museums (global/EU strong) | Tier 2 (product pages + vendor-articulated IWMS glossary) |
| Eptura Archibus | Eptura | Classic CAD/BIM-integrated IWMS, on-prem + FedRAMP SaaS, partner-sold | government, healthcare, education, Fortune-500 corporates | Tier 2 (product pages + platform pages) |
| FM:Systems (OpenBlue Workplace, Johnson Controls) | FM:Systems / JCI | Space/CAFM lineage; IWMS as integrated space + facility platform with employee & analytics families | corporate, government, higher ed, finance, healthcare, tech | Tier 2 (product structure + Real Estate & Lease page) |

Rejected/abandoned samples:

- **Nuvolo** (ServiceNow-platform cloud IWMS, healthcare/gov pole) — nuvolo.com root fetch: transport error; second URL: 404. Abandoned per network rule; pole held at market-structure knowledge only, no claims made.
- **Accruent, MRI Software IWMS** — not fetched (sample stop conditions met; sibling passes already recorded their positioning).
- IBM docs portal (ibm.com/docs/en/tririga) — 403; product page used instead.

## Sources

- IBM — "Real estate and facilities management with IBM Maximo" product page (domain list, single-source-of-truth positioning, industries, deployment paths): https://www.ibm.com/products/tririga (fetched 2026-09-08). IBM docs portal 403 — operational-manual depth not reachable.
- Planon — US site root (solution structure: IWMS + four modules; Campus; Lease Accounting; Planon for SAP; Platform): https://www.planonsoftware.com/us/ (fetched 2026-09-08)
- Planon — "IWMS | Integrated Workplace Management Systems" glossary page (vendor-articulated definition citing Gartner's five components on a single platform and database repository; benefits; integration requirements): https://www.planonsoftware.com/us/glossary/iwms/ (fetched 2026-09-08)
- Planon — "Planon Integrated Workplace Management Solution" product page (module set, platform, single source of truth, services): https://www.planonsoftware.com/us/software/iwms/ (fetched 2026-09-08)
- Eptura — site root (platform + app structure; Archibus as "FedRAMP Authorized and on-premise IWMS"; G2 IWMS Leader): https://eptura.com/ (fetched 2026-09-08)
- Eptura — "Archibus by Eptura" product page (feature set: BIM asset management, field technicians, capital projects, space planning, booking, lease & contract management; government; integrations; FAQs): https://eptura.com/our-platform/archibus/ (fetched 2026-09-08)
- FM:Systems — site root ("Integrated Workplace Management Software Platform"; OpenBlue Workplace/Employee/Insights product families; industries): https://fmsystems.com/ (fetched 2026-09-08)
- FM:Systems — "Real Estate Portfolio Software" page (spreadsheet → departmental CAFM → IWMS lineage statement; owned+leased portfolio definition; lease critical dates): https://fmsystems.com/products/workplace-management-solutions/real-estate-portfolio-software/ (fetched 2026-09-08)

Source-access limitation: no Tier-1 help-center/user-guide articles were reachable for any sampled product (IBM docs 403; Eptura knowledge center behind customer login; FM:Systems and Planon publish no open article-level operational docs). All evidence below is product-page level (Tier 2). Consequence: this document asserts market/product structure, not precise operational rules (no state names, numeric limits, approval chains, or workflow step sequences are asserted as fact). Vendor marketing statistics (e.g., cost-reduction percentages, sq-ft managed, Fortune-500 shares) are recorded as vendor claims only, never as Type facts.

## Product Observations

### IBM Maximo Real Estate and Facilities (ex TRIRIGA)

Key observations (A = directly observed on the product page):

- Positioned as "the evolution of IBM TRIRIGA… a comprehensive all-in-one solution… providing a single source of truth for all real estate and facilities data." (A)
- Five named capability areas ("What you can do"): Lease management; Space management; Capital planning; Maintenance and operations; Environmental and energy management. (A)
- Lease: "Streamline lease administration and lease accounting"; AI-powered lease abstraction extracting key dates, financial terms, clauses; "centralized lease data, advanced document management… automated reconciliation, and deeper portfolio-level reporting." (A)
- Space: space planners design/adjust layouts; IoT occupancy analytics; ghost-booking removal; hybrid-work framing. (A)
- Capital: "plan, budget, and manage capital projects"; procurement, risk mitigation, automated project workflows. (A)
- Maintenance: "unified data flowing across Maximo"; "aligned locations, assets, and work orders streamline workflows"; mobile-optimized. (A)
- Energy/environment: "unified platform for managing environmental impact and energy consumption"; AI predictive models for energy savings. (A)
- Industries: Government (FedRAMP offerings documented), Healthcare, Public and higher education, Corporate real estate. (A)
- Deployment: SaaS "Essentials" per domain (Space Management Essentials, Lease Management Essentials, Capital Planning Essentials) purchasable individually; full solution in Maximo Application Suite Standard/Premium; customer-managed on-prem/hybrid. (A)
- Reading: the module-as-Sku packaging shows the domains are separable commercially but designed as one system ("unified data flowing across Maximo"). The suite spine is IBM Maximo Application Suite — the IWMS lives inside a broader asset-management platform.

### Planon

Key observations:

- Company positioning: "the recognized world leader in Smart Sustainable Building Management software" — the IWMS label is deliberately de-emphasized in branding while the product remains "Planon Integrated Workplace Management Solution" with the IWMS solution page intact. (A) — naming-drift evidence.
- IWMS solution = four named modules: Real Estate Management; Space & Workplace Services Management; Asset & Maintenance Management; Energy & Sustainability Management. (A)
- Campus Management Solution = the same four modules packaged for higher education. (A)
- Vendor-articulated definition on the IWMS glossary page: "True IWMS software, as defined by Gartner, is an enterprise class software platform that integrates five key components of functionality, operated from a single technology platform and database repository." The five: Real estate and lease management; Facilities and space management; Asset & Maintenance management; Project management; Environmental sustainability. (A)
- Benefits framing: transparency ("creating a standardized and structured data repository for all your processes. You know the exact amount of space available for future growth, the floor areas for contracting the cleaning, the expiration of lease contracts, and when the next maintenance order needs to be executed"); efficiency; "proven compliance" (health & safety, maintenance, security, sustainability, IFRS/FASB lease accounting); decision support ("operational, tactical, and strategic decision making with reports, analyses, dashboards, and benchmarks"); cost savings. (A)
- Integration posture: "it should also connect to other IT solutions, like ERP, HR, Building Management Systems or Smart Meters… the IWMS should send financial charge back information to ERP, or update room- and phone information in the HR system." (A)
- IWMS vs point solutions: vendor publishes an "IWMS vs Point Solution Infographic" ("the differences between having an IWMS and a collection of point solutions") — the market's own articulation of the integration axis. (A)
- Global-estate requirements: multi-language, currency, time-zone, measurements. (A)
- Platform: "one integrated open platform" — AppBuilder, IoT Services, Data & Analytics Services, Integration & Configuration Tools, Planon Cloud. "The Planon Platform combines the advantages of IWMS software with the capabilities of IoT into one smart building platform." (A)
- Separate solutions beside the IWMS: Lease Accounting Solution (Lease Administration + FASB/IASB accounting + ERP integration), Field Services business solution (provider side: Hard-FM/Soft-FM), Commercial Real Estate suite (owner/investor side: Portfolio & Asset Management, Property Management, Development Management, Project Control). (A) — the vendor's own seam between occupier IWMS and landlord property management.
- Service model: implementation consultancy, business consultancy, training, project management (Prince2 named), managed services, cloud service (AWS-based) — IWMS as a long-lifecycle enterprise deployment. (A)
- History: "Over the past four decades" recognized in the IWMS category by Gartner/Verdantix/IDC/Frost & Sullivan. (A)
- Customers: universities (ETH Zürich, Michigan State, King's College London, Eindhoven), corporates (Bayer, Ahold Delhaize, Danfoss), municipality of Rotterdam, museums, arenas. (A)

### Eptura Archibus

Key observations:

- Positioned twice on one page: "IWMS for complex environments — A tailored solution that's FedRAMP Authorized" and "Archibus: FedRAMP Authorized and on-premise IWMS"; "OnPrem/SaaS IWMS"; sold exclusively through partners. (A)
- Audience split: Facility Managers ("Oversee maintenance, space planning, and asset tracking from a single dashboard"), IT/Security (FedRAMP, compliance), Executive Leaders ("Track space usage, sustainability, and costs to make informed decisions"). (A)
- Feature set: BIM-powered asset management (BIM Viewer for spaces and equipment); Archibus OnSite field-technician mobile app (offline-capable); capital project tracking (plan, budget, milestones, costs); space planning and hybrid work (drag-and-drop layouts, BIM integration); workspace booking (rooms/desks, find colleagues, services); lease and contract management ("Centralize lease data, automate alerts, and analyze costs. Manage property contracts, renewals, and compliance with dashboards and interactive mapping tools"). (A)
- Government pitch: "helps federal agencies manage buildings, assets, and people securely… Agencies can easily reallocate costs and optimize every square foot"; real estate portfolio visibility, asset optimization with audit-ready reporting, compliance. (A)
- Integrations: Microsoft, Autodesk (BIM), GIS, visitor management, IoT systems, HR, finance, analytics tools. (A)
- Customer stories: NOAA (space insights/cost), UMass Medical (lease cycle times), San Diego Gas & Electric (asset uptime via PM scheduling). (A)
- Parent platform structure: modular apps — Eptura Asset (facility maintenance + asset management), Eptura Engage (workplace experience/hybrid work), Eptura Workplace (workplace operations + space management), Eptura Visitor; specialized solutions — Archibus (the IWMS) and Serraview (portfolio and real estate management, scenario planning, block-and-stack). "Our apps share one architecture." (A)
- Reading: within one vendor, the market's own layering — Archibus = the integrated IWMS of record; Engage/Visitor = the workplace-experience cluster (§10 sibling territory); Serraview = portfolio optimization; Asset = the maintenance/asset layer. G2 "Leader IWMS" category alongside separate WEX/EAM/CMMS categories confirms the market treats IWMS as its own category.

### FM:Systems (OpenBlue Workplace)

Key observations:

- Site root headline: "Integrated Workplace Management Software Platform — An integrated space and facility management platform to create exceptional workplace experiences, improve portfolio performance, drive building efficiencies, support workplace mandates and enhance well-being." Self-labels as IWMS throughout industries pages. (A)
- Product families: **OpenBlue Workplace** (Workplace Management: Space Management, Move Management, Strategic Planning, Real Estate & Lease, Project Management; Facility Operations: Facility Management, Facility Maintenance, Asset Management, Work Order Ticketing, Preventative Maintenance, Sustainability), **OpenBlue Employee** (Workplace Experience: desk booking, room scheduling, interactive floorplans, catering/services, panels & kiosks, visitor management), **OpenBlue Insights** (portfolio analytics, utilization/sensor analytics, environmental monitoring, real-time dashboards, performance scoring). (A)
- Solution audiences: Employees & Occupants / Facility Managers / Real Estate Executives — "Strategic decisions about your real estate portfolio." (A)
- Historical lineage statement (Real Estate & Lease page): "In the past, portfolios were either managed by manual reporting in spreadsheets…, or using a desktop-based, departmental CAFM (computer-aided facility management) system, which didn't connect across departments well. Enter the world of IWMS (integrated workplace management system,) an enterprise-wide alternative to intelligently managing multiple facilities." (A) — the market's own three-stage lineage.
- Real estate portfolio definition: "twofold: it includes managing both owned and leased real estate as well as all of your real estate assets including buildings, land, parking lots, decks, etc." (A)
- Lease administration machinery: "Centralize your entire lease portfolio"; "Configurable workflows, notifications and forms… your entire real-estate team will stay informed and up to date on all lease critical dates such as renewals, rent increases"; live reports; past/present/future analysis (historical costs, portfolio trends). (A)
- Portfolio decision language: "reveal opportunities to lease, sell, or consolidate underutilized facility and real-estate assets." (A)
- Space/product family blurb: "An Integrated Workplace Management System (IWMS) that centralizes space and portfolio data, creating opportunities to reduce costs and optimize performance." (A)
- Company stats (vendor claims only): 3B+ sq ft managed, 250,000+ sensors, 40M+ reservations, 1,200+ customers, 80+ countries. (A, marketing)
- Ownership: "FM:Systems is now a part of Johnson Controls" — OpenBlue branding; workplace experience family rides the same platform (the §10 workplace cluster as a product family inside an IWMS vendor). (A)

## Cross-product Comparison

| Structure | IBM Maximo RE&F | Planon | Eptura Archibus | FM:Systems | Strength |
|---|---|---|---|---|---|
| Occupier's real estate & facility portfolio of record (properties/buildings/leases/space as persistent records) | ✓ "single source of truth for all real estate and facilities data" | ✓ "standardized and structured data repository for all your processes" | ✓ "real estate portfolio" government pitch; lease/contract centralization | ✓ "bird's eye view of your entire lease portfolio"; owned+leased definition | Universal (A, 4/4) |
| Real estate & lease domain (lease administration; commonly lease accounting) | ✓ admin + accounting + AI abstraction | ✓ RE Management + separate Lease Accounting solution | ✓ lease & contract management | ✓ Real Estate & Lease (critical dates) | Universal (A, 4/4) |
| Space domain (inventory, allocation, planning) | ✓ space management + IoT occupancy | ✓ Space & Workplace Services Management | ✓ space planning + BIM layouts | ✓ Space Management + Move + Strategic Planning | Universal (A, 4/4) |
| Operations & maintenance domain (work orders, PM, assets) | ✓ maintenance and operations (locations, assets, work orders) | ✓ Asset & Maintenance Management | ✓ maintenance + BIM asset mgmt + OnSite technicians | ✓ Facility Maintenance + Asset Mgmt + Work Order Ticketing + PM | Universal (A, 4/4) |
| Capital projects domain | ✓ capital planning | ~ project management in the five-component list; not a named module of the four-module pack | ✓ capital project tracking | ✓ Project Management (family member) | Common, packaging-variable (3.5/4) |
| Energy & sustainability domain | ✓ environmental and energy management | ✓ Energy & Sustainability Management | ✓ sustainability in executive benefits; sustainability product family member | ✓ Sustainability (family member) | Common (4/4 present, but named-module status varies) |
| Shared record base / single platform (the "integrated" invariant) | ✓ "single source of truth"; "unified data flowing across Maximo" | ✓ Gartner-cited "single technology platform and database repository" | ✓ "all in one place"; "apps share one architecture" | ✓ "integrated space and facility management platform" | Universal (A, 4/4) — THE discriminator vs point solutions |
| Executive/portfolio decision layer (op/tactical/strategic reporting, scenario/consolidation decisions) | ✓ "data-driven decision making… portfolio" | ✓ "operational, tactical, and strategic decision making" | ✓ executive leaders: "space usage, sustainability, and costs" | ✓ "lease, sell, or consolidate"; Strategic Planning | Universal (A, 4/4) |
| Workplace experience / employee booking surfaces | ~ hybrid work inside space mgmt | ✓ separate Workplace App | ✓ workspace booking; Engage sibling app | ✓ OpenBlue Employee family | Common, packaging-variable |
| Sensors/IoT/BMS integration | ✓ IoT occupancy | ✓ IoT Services; BMS/smart meters | ✓ IoT, Autodesk/BIM, GIS | ✓ sensors, environmental monitoring | Common (A, 4/4) |
| ERP/finance integration | ✓ under Maximo/IBM suite | ✓ Planon for SAP; chargeback to ERP | ✓ finance/HR integrations | ~ (not surfaced on fetched pages) | Common |
| Government/regulated posture (FedRAMP-class) | ✓ | ~ (public-sector customers) | ✓ | ~ (gov industry page) | Common variant |
| Multi-language/currency/time-zone global estate support | ~ | ✓ stated explicitly | ~ | ~ (80+ countries claim) | Common (explicit only at Planon) |
| Partner-led/long-lifecycle delivery model | ~ (Essentials vs suite SKUs) | ✓ services layer documented | ✓ "sold exclusively by our Partners" | ✓ partner hub | Common |
| Older/leaner packaging of the same estate spine | ✓ Essentials per-domain SKUs | ✓ modules purchasable (Lease Accounting standalone) | ✓ on-prem Archibus | ✓ product families purchasable separately | Universal |

## Canonical Model (abstraction hierarchy)

### Level 0 — Defining Invariant

Three jointly-held structures. If any one is removed, the product stops being recognizable as an IWMS:

1. **The occupier organization's real estate & facility portfolio of record.** The organization's own buildings and land — owned and leased — held as persistent, individually identified records: properties, buildings, leases, spaces, and the equipment/assets inside them. Not an income-property portfolio (no landlord/tenancy economics); the estate the organization itself occupies and operates. (Remove → generic enterprise suite with no built-environment substance.)

2. **The integrated multi-domain span.** Several distinct built-environment management domains carried as domains of the same system, not as separate products: real estate & lease administration, space management, and facility operations/maintenance are the constant core observed across the sample; capital project management and energy & sustainability are the commonly-added fourth and fifth. The system's identity is the span, not any single domain. (Remove the span → a single-domain Type: Lease Administration, Space Management, or Facility Management System.)

3. **The shared estate spine — one record base serving every domain.** The domains read and write the same underlying records: the lease record, the space record, the asset record, the building record are the same objects to every domain, so cross-domain operations and portfolio-level analysis ride on one system rather than on integrations between departmental tools. The market's own vocabulary: "single technology platform and database repository" (Gartner-cited definition), "single source of truth", the vendor-published IWMS-vs-point-solutions contrast, and the documented pre-history of "departmental CAFM systems, which didn't connect across departments well". (Remove → a bundle of point solutions, not an IWMS.)

Jointly-held load-bearing:

- Span without shared spine = a collection of point solutions (explicitly the market's rejected alternative).
- Shared spine without span = a single-domain system (FMS, space platform, lease admin).
- Portfolio-of-record without span+spine = a property/building registry.
- Span + spine without the occupier framing = landlord-side property management or a generic ERP module.

### Level 1 — Common Mature Structure

- **Lease administration depth** — lease abstraction, critical dates (renewals, rent steps), documents, obligations; lease accounting (FASB/IASB-class) as a compliance layer, sometimes a separately SKUs solution.
- **Space planning machinery** — floor-plan/CAD/BIM-anchored space inventory, allocation, occupancy analytics, scenario/strategic planning, move management.
- **The operations/maintenance substrate** — asset register, work orders, preventive maintenance, technician mobile execution (the CMMS-shaped layer, estate-bound).
- **Capital project management** — project planning/budgeting/milestones for facility capital work.
- **Energy & sustainability** — utility consumption capture, carbon/ESG reporting, energy performance.
- **Portfolio analytics & executive reporting** — utilization, cost per area, benchmarks, dashboards serving operational/tactical/strategic decisions.
- **Outward integration fabric** — ERP (chargebacks, accounting), HR (people/room data), BMS/IoT (building signals), GIS, calendars, visitor systems.
- **Global-estate machinery** — multi-language/currency/time-zone/site hierarchies, role-scoped access across CRE/FM/finance/security seats.
- **Long-lifecycle delivery** — implementation services, configuration-not-customization posture, managed services, partner channels.

### Level 2 — Variant / Optional Structure

- Packaging: monolithic suite (one product, named modules) vs platform-of-apps vs product families vs per-domain SaaS SKUs vs on-prem deployments.
- Sector shapes: higher education (campus), government (FedRAMP/regulated), healthcare, corporate real estate, finance.
- Regional vocabulary: North American IWMS lineage vs European CAFM-rooted suites.
- Employee-facing breadth: from none (classic back-office suites) to full workplace-experience families (booking, visitor, wayfinding).
- Service-provider side: some vendors run a separate FM-services business solution for contracted providers (occupier suite vs provider suite split).
- Branding posture: the IWMS label itself is de-emphasized by some vendors ("smart sustainable building management", "real estate and facilities management") while the structure persists.

### Level 3 — Vendor-specific (Research Notes only)

- Planon: Planon Universe; CPIP term ("Connected Portfolio Intelligence Platform"); AppBuilder; Accelerator best practices; Prince2 service methodology; acquisitions (control.IT, Ubigreen); "Smart Sustainable Building Management" rebrand; the four-module solution naming; EcoVadis claims.
- IBM: TRIRIGA heritage name; Maximo Application Suite packaging; Space/Lease/Capital "Essentials" SaaS SKUs; AI lease abstraction; AWS Marketplace SKUs.
- Eptura: Archibus brand; BIM Viewer; Archibus OnSite; partner-exclusive sales; Serraview (block-and-stack); Engage/Workplace/Visitor app split; G2 badge claims; "Powering 50% of the Fortune 500" marketing claim.
- FM:Systems: FM:Interact heritage; OpenBlue Workplace/Employee/Insights family naming; FMS:Marketplace; JCI ownership; stats (3B+ sq ft, 250k sensors, 1,200+ customers, 80+ countries).

## Rejected Findings

- **"IWMS = the five Gartner pillars" as a definitional module list.** Rejected as L0: the pillar set varies by vendor packaging (Planon's own four-module solution omits a named capital-projects module; sustainability arrives only in the modern era). The invariant is the integrated multi-domain span with the constant core trio, not a fixed module list. The five-pillar articulation is recorded as the market's most common description.
- **"IWMS = facilities management software."** Rejected: FM software (the FMS Type) is one domain inside the IWMS and exists standalone. The FMS pass's own module-vs-suite observation and this sample both support keep-both.
- **"IWMS = workplace management platform."** Rejected as identity: suite vendors use "workplace management" language, but the workplace-experience/operations cluster (booking, service requests, employee surfaces) is one slice — visibly packaged as separate product families (OpenBlue Employee, Eptura Engage) inside IWMS vendors. The estate/portfolio spine is the IWMS's center.
- **"Sustainability/energy is definitional."** Rejected by historical check: CAFM-era integrated systems predate the sustainability module; the domain trio + shared spine suffices.
- **"Employee booking/hybrid work is definitional."** Rejected: classic back-office suites and on-prem Archibus deployments operate without employee-facing surfaces (booking is a separate app/family at Eptura and FM:Systems).
- **"IWMS = ERP module."** Rejected: ERP integration is the seam, not the identity; the built-environment domain model (leases, spaces, buildings, assets) is the IWMS's own substance; Planon's "ERP vs IWMS" framing and SAP-solution-extension packaging show coexistence, not containment.
- **"IWMS = real estate portfolio management (investor side)."** Rejected: Planon ships a separate Commercial Real Estate suite for owners/investors beside the corporate-RE IWMS; income/tenancy economics is the property-management family, not the occupier IWMS.

## Boundary Findings

- **vs Facility Management System (§17 sibling, joint review REQUIRED — DISCHARGED this pass):** Seam ratified as proposed: the FMS is the estate-anchored operational service loop (requests, work orders, crews/providers, served-organization accountability) and exists standalone; the IWMS is the integrated multi-domain suite of record. Evidence from this side: every sampled IWMS contains the FMS layer as a named domain/family (IBM "Maintenance and operations"; Planon "Asset & Maintenance Management"; Archibus maintenance+asset; FM:Systems "Facility Operations"), and every sampled vendor also sells or corresponds to standalone-FMS-shaped products in the market. Removal tests: strip lease+space+capital+sustainability domains from an IWMS → its operations domain is an FMS; add the RE/lease+space+capital span and the shared record base to an FMS → it operates as an IWMS. Naming drift recorded: the market label is unstable (Planon brands "Smart Sustainable Building Management"; IBM brands "Real Estate and Facilities Management"), but the category persists (G2/analyst IWMS categories; Eptura "IWMS" positioning). Keep both leaves, cross-referenced.
- **vs Workplace Management Platform (§10, label-drift flag — DISCHARGED this pass):** The WMP Type = the workplace team's operational/experience cluster (booking, service loop, employee surfaces). Inside IWMS vendors that cluster is visibly a separate family (OpenBlue Employee; Eptura Engage/Visitor; Planon Workplace App). The IWMS = the portfolio/estate system of record for CRE & facilities leadership. Removal tests: strip the portfolio/lease/capital/space-planning domains from an IWMS → the WMP cluster remains; add the estate-of-record domains to a WMP → operating as an IWMS. Keep both.
- **vs Space Management Platform / Space & Occupancy Management (§10/§17):** space is a domain inside the IWMS; standalone space platforms exist (prior pass confirmed the module relationship). Keep both.
- **vs Lease Administration (§17):** lease administration is the RE domain inside; standalone lease-admin products serve the same function separately. Module relationship.
- **vs CMMS / Maintenance Management and EAM (§16):** the IWMS's operations/maintenance domain is CMMS-shaped, but the IWMS's center is the multi-domain estate span; CMMS/EAM are domain-generic machinery. Consistent with both prior passes' recorded seams.
- **vs Building Management System / BMS (§17):** BMS is the OT control layer beneath; IWMS consumes BMS/IoT signals (Planon explicitly connects HVAC/lighting; FM:Systems sensors; IBM IoT). Layered, not duplicate.
- **vs Commercial / Residential Property Management (§17):** landlord income side (tenancies, rent, recoveries) vs occupier-side portfolio of record. Planon's own catalog separates the two (Corporate Real Estate IWMS vs Commercial Real Estate suite). The commercial-property pass's "occupier-side, no income loop" seam holds.
- **vs ERP (§10):** finance backbone vs built-environment domain suite; chargeback/accounting integration is the seam (Planon: "send financial charge back information to ERP").
- **vs Building Energy Management (§17) / Energy & Carbon (§21):** energy/sustainability is one domain module inside the IWMS; dedicated sibling Types center that data loop. Consistent with the building-energy pass's recorded seam.
- **vs Capital Improvement Planning / Building Condition Assessment / Construction Project Management (§17):** capital planning and project machinery appear as a domain inside IWMS suites; the dedicated Types center the capital-planning workflow itself. Feeder/consumer relationship.
- **"去掉什么就变成另一个 Type" 判据：** remove the multi-domain span → Lease Administration / Space Management / FMS; remove the shared record base → a point-solution bundle; remove the occupier framing (add tenancy income) → property management; remove the built-environment substance → a generic enterprise suite.

## Historical / Market-Sample Check

- The market's own documented lineage: "manual reporting in spreadsheets → desktop-based, departmental CAFM system, which didn't connect across departments well → IWMS, an enterprise-wide alternative" (FM:Systems, verbatim). The analog ancestor — a corporate real estate & facilities department holding lease files, space plans, maintenance logs, and capital budgets bound to the same building records — satisfies the three-leg core at paper level.
- Longevity: Planon claims four decades in the category; Archibus is the documented 1980s–90s CAD-integrated generation (space pass record); TRIRIGA is the 2000s RE+capital lineage now evolved under Maximo.
- Older/leaner configurations satisfy the core without modern machinery: on-prem Archibus (no cloud), classic suites without employee booking surfaces, suites without sustainability modules (pre-2000s), per-domain SKUs. Therefore: cloud, IoT, sensors, hybrid-work surfaces, ESG modules, AI abstraction, FedRAMP, partner-marketplaces are all era/market machinery — characteristic, not definitional.
- Regional check: the European CAFM-rooted pole (Planon) and the North American RE/ERP-rooted pole (IBM) both fit the same three-leg core, satisfying the flag from the FMS pass about under-sampled European vocabulary (partially resolved: Planon documents the CAFM/IWMS/CMMS/EAM/FSM vocabulary set on its glossary hub).

## Uncertainties

- **Minimum domain composition.** All four sampled products carry real estate & lease + space + operations/maintenance. Whether a product integrating space + operations + sustainability but *without* lease/RE management would be marketed as an IWMS is unverified — no such product surfaced. The L0 wording uses the constant trio as observed, with the caveat recorded here.
- **Operational rule depth.** With no Tier-1 help-center articles reachable, in-product operational rules (work-order state machines, lease-critical-date automation specifics, approval chains, chargeback calculation mechanics) are unverified. The final document deliberately names no precise operational parameters.
- **Service-provider-side suites.** Planon's Field Services business solution shows the provider-side counterpart exists as a separate product; whether any vendor ships an IWMS that natively spans both occupier and provider sides in one system was not verified.
- **Smaller-market IWMS products** (regional suites, mid-market CAFM packages branding themselves IWMS) were not sampled; the three-leg core is expected to hold but is only checked at the enterprise poles.

## Final Synthesis

An Integrated Workplace Management System is the occupier organization's integrated multi-domain system of record for the real estate portfolio it occupies and operates. Three jointly-held structures define the Type: (1) the portfolio of record — owned and leased properties, buildings, leases, spaces, and assets held as persistent identified records; (2) the integrated multi-domain span — real estate & lease administration, space management, and facility operations/maintenance as the constant core, with capital projects and energy & sustainability as the commonly-added domains, carried as domains of one system; (3) the shared estate spine — one record base that every domain reads and writes, so cross-domain operations and portfolio-level decisions (lease events, moves, renew/sell/consolidate, cost per area, ESG posture) ride on a single source of truth rather than on integrations between departmental tools. Mature products add lease-accounting depth, CAD/BIM-anchored space planning, move management, the CMMS-shaped maintenance substrate, capital project machinery, sustainability reporting, portfolio analytics, ERP/HR/BMS integration, global-estate machinery, and increasingly employee-facing workplace surfaces — all characteristic, none definitional. The FMS seam (operational layer vs multi-domain suite) and the workplace-management label drift (experience cluster vs estate spine) are discharged from this side; the domain-module relationships (space, lease, energy, capital) are held as module-of-suite, keep-both.
