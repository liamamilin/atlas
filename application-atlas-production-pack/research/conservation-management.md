# Research Notes — Conservation Management

Research date: 2026-09-07
Leaf: Conservation Management (DIRECTORY §21 Environment, Sustainability & Climate)
Slug: conservation-management

---

## Research Goal

Understand what "Conservation Management" software actually is as an Application Type: what its system of record contains, who operates it, how conservation work flows through it, and where its boundaries sit against neighboring Types (Biodiversity Management, Natural Capital Management, Nature Risk Management, Environmental Monitoring Platform, Forestry Management, Environmental Management System).

## Initial Boundary

Initial hypothesis (pre-research): software used by conservation organizations (protected-area authorities, conservation NGOs, land trusts, government wildlife agencies) to manage conservation work — the entities being conserved, threats to them, actions taken, and monitoring of whether the work is working.

Potential confusions identified up front:

- Could be an alias of **Biodiversity Management** (species data) — must check whether the core is data-centric or work-centric.
- Could collapse into **Environmental Monitoring Platform** (sensor parameter monitoring) — must check data source and purpose.
- Could be confused with **Natural Capital Management / Nature Risk Management** (corporate valuation/risk framing).
- Could be confused with **Forestry Management / Farm Management** (production land use).
- The name is broad: in North America "conservation management software" also names land-trust stewardship software (easement/property stewardship). This pole must be checked.

## Research Questions

1. What is the unit of record — site, project, species, easement, patrol?
2. What objects exist inside the system (observations/events, patrols, threats, targets, strategies, indicators)?
3. What lifecycle / state changes matter (patrol lifecycle, event lifecycle, adaptive-management cycle)?
4. What rules matter (offline capture, data ownership, standardized data models, evidence quality for enforcement)?
5. What interfaces exist (map console, mobile field app, planning workspace, reports)?
6. How do products differ by segment (protected-area operations vs project planning vs stewardship)?
7. Where is the boundary to Biodiversity Management and to Environmental Monitoring?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Philosophy | Customer tier |
|---|---|---|---|
| SMART (Spatial Monitoring and Reporting Tool) | protected-area patrol/monitoring suite | open-source, partnership-governed (WWF/WCS/ZSL/FZS et al.), field-to-decision data flow, disconnected-first | park/site managers, government agencies, global South heavy |
| EarthRanger (Allen Institute for AI) | real-time protected-area operations platform | free SaaS, integration hub (sensors/collars/camera traps), real-time intelligence | protected areas in 80+ countries, tech-forward sites |
| Conservation Standards / Miradi (CMP) | conservation project planning & adaptive management | standardized method (Open Standards) + desktop software; planning-first, not field-first | NGO programs, funders, project teams |
| CyberTracker | field data collection tool (boundary/adjacent) | icon-based UI usable by non-literate trackers; long heritage (Kalahari San) | individual field projects, community science |

Rejected / unreachable samples:

- **LandTrust** (landtrust.cloud) — transport errors on two attempts; abandoned per network rule.
- **Terra Firma Solutions** — turned out to be an unrelated US government staffing contractor (name collision).
- **ConservationWorks** (conservationworks.org) — returned empty content.
- **LandGood.com** — domain-for-sale page, not a product.
- **Miradi.org** — JS-rendered; returned only the page title. The Conservation Standards framework was verified via the CMP/conservationstandards.org sites instead; Miradi-specific feature claims are NOT asserted.

## Sources

Tier 1 (official, directly fetched 2026-09-07):

- SMART — https://smartconservationtools.org/ (home), /en-us/SMART-Approach/Technology, /en-us/SMART-in-Practice/How-we-use-SMART
- EarthRanger — https://www.earthranger.com/ (home), https://support.earthranger.com/ (help hub), /en_US/earthranger, /en_US/learn-the-basics
- Conservation Standards — https://www.conservationstandards.org/about/ ; CMP — https://www.conservationmeasures.org/
- CyberTracker — https://cybertracker.org/ (home; uses; partner list)

Unreachable / degraded:

- Miradi product site (JS-rendered, no content) — Miradi features not directly observed.
- Land-trust stewardship software pole (LandTrust et al.) — no official documentation reachable in this pass.

## Product Observations

### SMART (evidence layer A — directly observed, official site)

- Self-description: "a holistic conservation area management platform, including mobile, desktop, and cloud-based components"; purpose is to "collect, visualize, store, analyze, report and act on a wide range of data relevant for protecting wildlife and improving your overall conservation impact."
- Stated activity scope: "biodiversity conservation, law enforcement, tourism and visitor management, natural resources use, intelligence, and performance and threat level assessments."
- Tool suite (official names): SMART Desktop (central database with analytical functions), SMART Connect (web-connected database), SMART Mobile / SMART Collect (mobile data collection; Collect = decentralized/citizen-science variant), Survey plug-in (ecological surveys), Profiles plug-in ("track entities" — individual animals, park entry traffic, community outreach, staff training records, equipment/infrastructure maintenance schedules, human-wildlife conflict incidences), Integrations.
- Field flow: rangers record "animals, illegal activities, and conservation actions taken" plus patrol tracks on SMART Mobile → fed into central database (Desktop/Connect) → "analyzed, visualized, mapped and acted upon so that park managers can rapidly respond to threats" → "standardized reports … delivered to decision-makers."
- Law enforcement monitoring: "collection, storage, communication, and evaluation of data on patrol efforts, patrol results, and threat levels"; emphasis on "information flow between rangers and conservation managers."
- Biodiversity monitoring: "capture, manage and map data from systematic surveys of species and their habitats"; analyze "species and habitat changes over space and time"; Survey plug-in with customizable data model; export for external analysis; "compile ecological and patrol data … to create a holistic protected area management strategy."
- Platform features: open-source, non-proprietary, free; functional in disconnected and connected environments; customizable data model/queries/reports per site ("design their own templates"); single site or network of sites; terrestrial/marine/freshwater; "respects ownership of data"; site-level maintainability; development driven by user base.
- Scale claim (vendor-stated): used at 1,100+ sites in 95+ countries.
- Governance: maintained by a partnership of 8 conservation organizations; now allied with EarthRanger in SERCA (SMART–EarthRanger Conservation Alliance).

### EarthRanger (evidence layer A — directly observed, official site + help center)

- Self-description: "collect data from the field, integrate your technology, see your wildlife and teams in real time, and develop strategies that accelerate your impact."
- Use cases listed: human-wildlife conflict mitigation, wildlife monitoring, personnel safety, habitat protection, protected area management.
- Help-center core concepts: "from subjects and devices to patrols, events, and maps."
  - **Subjects** — tracked entities (wildlife, vehicles, aircraft, personnel) with live positional data from attached devices.
  - **Patrols** — created in web, tracked/documented in mobile; "patrol info" can automate event creation.
  - **Events / Incidents** — field reports ("create and submit events"), area-based event locations, related events organized into incidents, events dashboard, shared events.
  - **Map** — map layers (web + mobile), base layers/terrain/overlays, heat maps, time slider.
- Integrations: animal collars, remote imagery, vehicle/asset trackers, IoT systems, radios, camera traps, aircraft trackers, personnel trackers; "150+ integrations" (vendor-stated); Gundi described as "the universal adaptor for conservation technologies."
- Operational behaviors: offline collection with automatic sync when connection restored; capture "GPS coordinates, polygons, photos, and notes"; instant alerts (SMS/WhatsApp/email) on movement patterns (immobility, speed changes, boundary crossings); messaging to teams; "look back to plan ahead" (visualize past patrols, surveys, events).
- Analysis: Ecoscope ("turning complex conservation data into action"); API access, ArcGIS integrations, analyzers (help-center "Master" tier).
- Posture: free to use; "your data stays yours … configurable access, encryption"; optional secure data sharing across protected areas/landscapes; owned by Allen Institute for AI; AI-driven integrations (e.g., video activity labeling).
- Scale claims (vendor-stated): 900+ conservation sites, 23K animals tracked via GPS, 80+ countries.

### Conservation Standards / CMP (evidence layer A for the framework; Miradi itself not directly observed)

- The Open Standards for the Practice of Conservation ("Conservation Standards", CS): "a widely adopted set of principles and practices that bring together common concepts, approaches, and terminology for conservation project design, management, and monitoring."
- Developed by the Conservation Measures Partnership; version 1.0 in 2004; built on a "Rosetta Stone" crosswalk of member organizations' planning terminology.
- Framework: "a cyclical framework, structured around five interconnected steps" (training videos named Assess, Plan, Implement, and two further steps — analyze/adapt and capture/share; exact step labels not fully verified from fetched text).
- Purpose language: "managing, monitoring, planning, and learning from past conservation efforts"; "prioritization at various stages, testing of assumptions, and data sharing"; "we don't have a fully functional system to assess the effectiveness of our actions. Without more rigorous measurement of effectiveness and disciplined recording of our efforts, we cannot know or demonstrate that we are achieving desired results."
- Scope: "developed for biodiversity and resource conservation efforts … evolved to better reflect … connections between nature and humans."
- Miradi is listed by CMP as the companion software ("Collaborators … Miradi"); Miradi's own site title reads "Miradi - Conservation Project Management Software" (title only — content not fetchable).
- IUCN–CMP Threats Classification exists as a standardized vocabulary (v4.0 referenced).

### CyberTracker (evidence layer A — directly observed, official site)

- Field data collection software with icon-based smartphone UI designed for non-literate users; originated with Kalahari San trackers.
- "The CyberTracker Software is being used worldwide in conservation management, scientific research, farming, forestry, social surveys and education."
- Uses: indigenous knowledge, protected areas, scientific research, community science, education, farming, forestry, social surveys, crime prevention.
- Partners/integrations listed: Esri ArcGIS Online, SMART, KoBoToolbox, EarthRanger; also aligned with TNFD, Biodiversity Credit Alliance, MRV Collective, UNDP Digital X.
- Vision: "a Worldwide Environmental Monitoring Network."
- Interpretation: CyberTracker is a **field-data-collection capability/tool**, not a management system of record — it lacks (per its own positioning) the management cycle, threat/action planning, and reporting-to-decision-maker spine. Useful as the lower boundary of the Type.

## Cross-product Comparison

| Dimension | SMART | EarthRanger | Conservation Standards/Miradi | CyberTracker |
|---|---|---|---|---|
| Managed unit | conservation area / site (single or network) | conservation site / landscape | conservation project | (none — data collection only) |
| Field collection | SMART Mobile / Collect, offline-first | EarthRanger Mobile, offline sync | not the core (planning-first) | core purpose, icon UI |
| Map-centricity | yes (mapping/analysis) | yes (map layers, live positions) | diagrams over maps | map export/partners (Esri) |
| Patrol / work record | patrol efforts/results/threats | patrols (web create, mobile track) | strategies/actions (planned) | n/a |
| Event/observation model | standardized data model, customizable | events + incidents, configurable | indicators/monitoring plan | observation forms |
| Threat model | threat levels, LEM | illegal activities, HWC, boundary crossings | IUCN–CMP threats classification | n/a |
| Monitoring/evaluation | analysis + standardized reports | Ecoscope analysis, trends | five-step adaptive cycle, effectiveness measurement | n/a |
| Real-time | no (batch sync emphasis) | yes (live subjects, alerts) | no | no |
| Sensors/IoT | integrations module | collars, camera traps, vehicles, radios | no | partner integrations |
| Entity/subject tracking | Profiles plug-in | subjects (wildlife/vehicles/personnel) | no | no |
| Reporting to decision-makers | standardized reports, few clicks | dashboards, alerts, exports | monitoring/effectiveness reporting | export only |
| Governance/deployment | open-source, partnership, desktop+cloud | free SaaS (AI institute) | open standard + desktop software | free/open tool + online service |
| Business model | free, non-proprietary | free to use | open standard (CC) | free tool + paid online tiers |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

1. **Conservation subject** — a persistent managed record of the entity being conserved: a site/conservation area, a project scope, a species population, or a protected asset; spatially bounded where applicable.
2. **Threat & value assessment** — recorded threats endangering the subject and the values/targets being protected; the assessment layer that gives conservation work its direction.
3. **Conservation work record** — planned and executed actions/interventions directed at the subject (patrols, stewardship, restoration, strategies), held as records, not just calendar items.
4. **Evidence loop** — monitoring/evaluation of subject state, threats, and work, whose results feed back into management decisions over time (adaptive management).

Remove #1 → generic field-data collection or GIS. Remove #2 → generic work/task management. Remove #3 → biodiversity data platform (data without work). Remove #4 → work tracking with no conservation learning loop. All four are required for the Type to be recognizable.

### L1 — Common Mature Structure (very common, not definitional)

- Mobile field data collection with offline capture and later sync (SMART Mobile, EarthRanger Mobile, CyberTracker)
- Map/GIS-centric operational interface (map layers, geospatial features) — operational pole
- Patrol/work scheduling and tracking with effort-vs-result orientation
- Standardized, site-configurable event/observation data model
- Central database with analysis, visualization, and standardized reporting to decision-makers
- Tracked subjects/entities (animals, vehicles, personnel) and entity profiles
- Multi-site / network-of-sites scale
- Explicit data-ownership/privacy posture (both SMART and EarthRanger state it)
- Long time horizons: multi-year monitoring and trend analysis

### L2 — Variant / Optional Structure

- Real-time operations and alerting (EarthRanger pole; SMART is batch-sync oriented)
- Sensor/IoT integration depth (collars, camera traps, vehicle trackers, radios)
- Law-enforcement/intelligence depth (LEM, intelligence profiles)
- Citizen science / decentralized community reporting (SMART Collect, CyberTracker community science)
- Ecological survey design and management (SMART Survey)
- Formal planning method (Conservation Standards five-step cycle, results chains, situation models)
- Cross-site/landscape data sharing (EarthRanger optional sharing)
- AI assistance (image labeling, analytics)
- Funder/program-level rollup (implied by CS "demonstrate impact" language; not directly verified)
- Land-trust stewardship/easement pole (segment known to exist; NOT verified in this pass — see limitations)

### L3 — Vendor-specific (research notes only)

- SMART tool names (Desktop/Connect/Mobile/Collect/Survey/Profiles), 8-partner governance, SERCA alliance, 1,100+ sites / 95+ countries claims
- EarthRanger: Gundi adaptor, Ecoscope, EarthRanger Identity/Buoy, free-to-use model, AI2 ownership, SMS/WhatsApp/email alert channels, 900+ sites / 23K animals / 150+ integrations claims
- CyberTracker: icon UI for non-literate users, Kalahari San origins, tracker certification program
- CS: version 1.0 (2004), Rosetta Stone exercise, IUCN–CMP Threats Classification v4.0, five video-documented steps

## Historical / Market-Sample Check (§24)

Would older, regional, platform-native products still fit the L0?

- Pre-software conservation practice: ranger patrol registers (paper), species recovery plans with monitoring and revision cycles, land-trust easement monitoring files, protected-area management plans — all exhibit subject + threats + actions + monitoring/revision. The L0 holds without cloud, mobile apps, GPS, or real-time telemetry.
- CyberTracker (1990s-heritage, Palm-era origins) fits the field-collection layer without any modern SaaS machinery.
- CS v1.0 (2004) predates the modern sensor-integration era; its planning-first pole still fits L0.
- Conclusion: L0 is not over-fitted to the current real-time SaaS pattern. Real-time, sensors, AI, cloud delivery are correctly excluded from the definition.

## Vendor-specific Findings (kept out of final document)

See L3 above. Notably: all scale numbers (1,100+ sites, 900+ sites, 23K animals, 150+ integrations) are vendor-stated marketing statistics — not asserted as facts in the final document.

## Boundary Findings

| Neighboring Type | Relationship | Distinction | "Remove what → becomes the other Type" |
|---|---|---|---|
| Biodiversity Management | adjacent, highest confusion risk | the processed biodiversity-management pass (2026-09-06) defines that Type as the organization's interface with nature: location portfolio + site-anchored biodiversity records + assessed nature interface (impact/dependency/risk) + disclosure outputs. Conservation management is the delivery side: subjects, threats, actions, evidence loop. Both may record field species observations; the spine differs (assess-and-disclose vs act-and-adapt). This pass's boundary wording was aligned with the sibling pass to avoid contradiction | remove the work/action/management layer, keep the assessed nature interface → Biodiversity Management; remove the assess-and-disclose framing, keep work delivery → Conservation Management |
| Environmental Monitoring Platform | adjacent | sensor-based parameter monitoring (air/water quality, CEMS) for compliance; conservation monitoring is field-observation-based against conservation indicators | replace field-staff observations with sensor telemetry + compliance parameters → Environmental Monitoring |
| Natural Capital Management | adjacent | ecosystem-service valuation/accounting framing | remove the operational work layer, keep valuation → Natural Capital |
| Nature Risk Management | adjacent | corporate dependencies/impacts risk (TNFD-style) | remove operations, keep corporate risk framing → Nature Risk |
| Forestry Management / Farm Management | adjacent | production-oriented land management; CyberTracker shows the tool layer is shared, the purpose differs | orient the subject record to production/harvest → Forestry/Farm |
| Environmental Management System (ISO 14001) | adjacent | organizational compliance loop (policy→audit→corrective) vs site/species conservation loop | replace conservation subject with organizational compliance obligations → EMS |
| Environmental Incident Management | adjacent | incidents as compliance events with regulatory reporting | keep only incident/compliance flow → Environmental Incident Management |
| Project Management Application (generic) | genus | Miradi is project management shaped by conservation semantics (targets, threats, results chains, indicators); generic PM lacks this domain model | strip the threat–strategy–indicator domain model → generic PM |
| GIS applications | surface | maps are the dominant surface of the operational pole but not the core (CS pole is diagram-centric) | keep only mapping/analysis → GIS |
| Wildlife tracking apps / telemetry | capability | subject tracking is a capability inside the Type, not the Type | keep only live tracking → tracking product |

Boundary verdict: Conservation Management is a defensible distinct Type whose center of gravity is the **management cycle over conserved subjects**, not the data (biodiversity) nor the parameters (environmental monitoring) nor the valuation (natural capital). The boundary vs Biodiversity Management was cross-checked against the already-processed biodiversity-management pass (STATUS 2026-09-06), which had anticipated this seam as "org-impact interface vs conservation delivery" — this pass's wording was aligned accordingly; no joint-review flag required.

## Uncertainties

1. **Land-trust stewardship pole unverified.** LandTrust unreachable (transport errors ×2); Terra Firma name collision; ConservationWorks empty; LandGood domain-for-sale. The segment is described only conceptually in the final document; no product-specific claims are made. If a later pass reaches land-trust software, the L0 should be re-checked against easement/stewardship semantics (predicted to fit: subject=easement/property, threats=violations, actions=monitoring visits/enforcement, evidence loop=annual monitoring → follow-up).
2. **Miradi features not directly observed** (JS-rendered site). The CS framework is verified via CMP; Miradi-specific capabilities are not asserted anywhere.
3. **CS five-step exact labels** not fully verified from fetched text (videos named Assess/Plan/Implement + two unnamed steps). Final document describes the cycle generically (assess → plan → implement → analyze/learn → adapt) without asserting vendor step names.
4. **Funder/program rollup tools** (e.g., MERIT) not researched — whether they belong to this Type or to grant/program management is unresolved.
5. Whether "Conservation Management" should eventually be renamed/narrowed (e.g., "Conservation Area Management") — the sampled market uses both framings; recorded as a taxonomy observation, not changed unilaterally.

## Final Synthesis

Conservation Management is the operational system of record for conservation work. Its defining core is a four-part structure: a persistent conservation subject (site/area/project/species population), a threat-and-value assessment that directs work, recorded conservation actions/work (patrols, stewardship, strategies), and an evidence loop in which monitoring feeds back into management decisions. Around this core, mature products add field/mobile offline collection, map-centric operations, patrol and event models, standardized reporting, entity tracking, and multi-site scale. The Type spans three recognizable poles — protected-area operations (SMART, EarthRanger), conservation project planning under a formal adaptive-management method (Conservation Standards/Miradi), and (unverified this pass) private land stewardship — plus an adjacent tool layer (CyberTracker) that supplies field collection without the management cycle. The Type is distinct from Biodiversity Management (data-centric), Environmental Monitoring (sensor/parameter-centric), and Natural Capital/Nature Risk (valuation/risk-centric).
