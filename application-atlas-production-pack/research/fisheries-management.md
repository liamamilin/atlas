# Research Notes — Fisheries Management

## Research Goal

Understand what "Fisheries Management" software actually is, from real products: what its central records are (fisheries/stocks, entitlements, vessels, trips, catch), how the catch-accounting and reporting machinery works, who operates it (authorities vs industry vs service providers), and where its boundary lies against Aquaculture Management, vessel/fleet management, monitoring/transparency platforms, and the science/assessment layer.

## Initial Boundary

- This leaf sits in §20 Agriculture, Food & Natural Resources, next to Aquaculture Management. The working hypothesis (inherited from the aquaculture pass, which pre-hung the flag): Fisheries Management targets **wild-capture** fisheries — capture effort, catch records, quotas, landings, vessels — not reared populations in owned production units.
- The leaf name covers several real populations: fishery administrations (licensing, quota, catch accounting, registers), fishing industry operators (quota holdings, fleet catch operations, compliance reporting), monitoring service providers (observers, dockside, electronic monitoring), and fisheries data management (national/regional catch-effort databases feeding stock assessment).
- Confusable neighbors: Aquaculture Management (§20, processed), Marine Fleet Management / Vessel Operations Platform (§18), Food Traceability Platform (§20), Government Licensing Management (§24), Environmental Monitoring Platform (§21), Public Data Portal (§02.12), stock-assessment science tools.

## Research Questions

1. What are the core records — fishery/stock, entitlement (quota/ACE), permit, vessel, trip, fishing event, catch, landing, return?
2. How does catch accounting work — validation, monthly returns, balancing catch against entitlement, overage consequences?
3. What is the capture layer — e-logbooks, landing reports, observers, dockside monitoring, electronic monitoring, vessel position reporting — and is it definitional or implementational?
4. Who are the seats: authority-of-record vs industry operations vs service providers? One Type or several?
5. Historical check: do pre-quota, paper-era, effort-based, and small-scale fisheries regimes satisfy the definition?
6. Boundaries: vs aquaculture (pre-hung flag), vs fleet/vessel management, vs monitoring/transparency platforms, vs traceability, vs science tools.

## Representative Products

Chosen for market representativeness, documentation quality, different seats/philosophies, and different geographies/regimes:

1. **Fishserve (New Zealand)** — administration-services company operating the registry/reporting system for NZ's Quota Management System since 1999; the market's cleanest "Fisheries Management System of record" specimen (self-described product name).
2. **SPC — TUFMAN 2 + e-reporting suite (Pacific Community, FAME division)** — national fisheries data management for Pacific Island Countries: cloud database, catch/effort query, field e-reporting apps (OnBoard, OnShore, OLLO, Tails, Ikasavea); the data-management/assessment-feed pole.
3. **Archipelago Marine Research (Canada)** — monitoring service provider + technology vendor: at-sea observers, dockside monitoring, electronic monitoring; FishVue product line (onboard EM, FLOAT e-logbook, Interpret review, Fleet real-time monitoring); the compliance-monitoring pole.
4. **Global Fishing Watch** — boundary specimen: public transparency/monitoring platform (AIS + satellite + ML), no records of record.
5. **Pelagic Data Systems** — boundary specimen: artisanal-fleet vessel tracking hardware + analytics; explicitly complements landings data rather than holding the management record.

Sought but unreachable: NOAA Fish Online / Alaska eLandings (US IFQ catch-accounting pole; repeated transport errors/404), Maritech (Norwegian seafood/catch management for industry; transport errors), TNC eCatch (transport error). See Sources.

## Sources

All fetched 2026-09-08.

Fishserve (Tier-1, official site, 7 pages):
- https://www.fishserve.co.nz/ (home)
- https://www.fishserve.co.nz/fishserve-website (Client Website = "Fisheries Management System" product page)
- https://www.fishserve.co.nz/qms-and-regulations (QMS concepts: FMA, QMA, TAC, TACC, ITQ, ACE)
- https://www.fishserve.co.nz/elogbook-providers (ERS APIs, e-logbook connection requirements)
- https://www.fishserve.co.nz/catch-reports (Catch vs ACE, Catch by Month reports)
- https://www.fishserve.co.nz/obligations (reporting obligations: GPR, e-catch reports, MHR/deemed values, protected species)
- https://www.fishserve.co.nz/about-public-registers (registers: quota, ACE, permits, vessels, fish farms)

SPC FAME (Tier-1, official site, 2 pages + nav):
- https://fame.spc.int/ (division home)
- https://fame.spc.int/fisheries-data/database-systems-and-access (Tufman 2, T2 Reports, CES, PREVIEW, Tails/Ikasavea/OnBoard/OnShore/OLLO)
- https://www.spc.int/ofp/tufman2 (JS shell, no content extracted)

Archipelago Marine Research (Tier-2, official product/service pages):
- https://www.archipelago.ca/ (services: at-sea observers, dockside monitoring, EM; products: FishVue Vantage/LIME/Mobile, Interpret, Fleet, FLOAT, AI)

Global Fishing Watch (Tier-2):
- https://globalfishingwatch.org/ (platform, map, Marine Manager, Vessel Viewer, APIs)

Pelagic Data Systems (Tier-2):
- https://pelagicdata.com/ (VTS hardware, analytics, fisheries-management use case framing)

## Product Observations

### Fishserve (NZ) — authority-registry pole

Evidence layer: A (directly observed, Tier-1).

- Operates "an online Fisheries Management System … referred to as the Fishserve Client Website" to administer the NZ Quota Management System (explicit product self-label "Fisheries Management System").
- Client Website functions: apply for fishing permits and Licensed Fish Receiver (LFR) status; register a vessel; correct validation errors on trip reports; correct data-entry errors from trip reports; submit Monthly Harvest Returns (MHR); submit Monthly Licensed Fish Receiver Returns (LFRR); make ACE and Quota transfers/purchases; run reports; view own record of transactions and current ACE balances.
- QMS concepts (from QMS page): 10 Fisheries Management Areas; Quota Management Areas per fish stock; TAC per stock (commercial + recreational + customary); TACC set from TAC; ITQ = percentage share of a TACC for a specific fish stock; ACE = annual entitlement in kg derived from TACC × ITQ; ACE purchasable by non-ITQ holders via transfer. QMS introduced 1986; Fisheries Act 1996 foundation.
- Catch reporting: fully electronic since 2019; all fishers report catch through an e-logbook meeting Fisheries (Reporting) Regulations 2017 specifications; all e-logbook providers must connect to the Fishserve Fisheries Management System; catch reports pass a validation process and are sent on to Fisheries New Zealand. Four ERS APIs: Authentication; Logbook Registration (public key); Event APIs (submit/retrieve/amend **Fishing and Non-Fishing Events** occurring on trips — e.g. a Trawl Event or a Processing Event); Master Data APIs (stock code lists, fishing methods).
- Obligations: GPR device required, on during fishing trips; Fisheries NZ maintains a 10-minute position record for all fishing vessels from port departure; electronic catch reports for **every fishing event**; MHRs "balance catch with ACE available"; catch above ACE triggers government "Deemed values" charges; protected-species interactions reportable via e-logbook.
- Public registers (managed for the Crown): quota, ACE, fishing permits (including high seas), fishing vessels, fish farms; statutory public access; plus aggregate catch reports (Catch vs ACE with % of ACE caught; Catch by Month with TACC and total ACE per fishing year).
- Structure visible: fishery/stock (QMA × species) → entitlements (ITQ/ACE per holder) → activity (trips, fishing events via e-logbook) → catch accounting (validation, MHR balancing, deemed values) → registers/reports (public + aggregate) → compliance hooks (GPR positions, protected-species interactions).

### SPC TUFMAN 2 + suite — national data-management pole

Evidence layer: A (Tier-1).

- TUFMAN 2 ("Tuna Fisheries Data Management system"): cloud-hosted web database for Pacific Island Countries to manage their tuna fishery data; evolved from paper forms/local databases; "secure, web-based systems for data entry, management, quality control, visualisation and reporting"; serves "national fisheries management needs" and "scientific analyses … to support our members' management processes".
- T2 Reports: secured reporting interface integrated into Tufman 2; figures/tables for WCPFC (Western and Central Pacific Fisheries Commission) reporting templates.
- CES (Catch and Effort Query System): extract summaries of operational **logsheet** data, aggregate public-domain catch and effort data, annual catch estimates; user-built filtered/aggregated extractions for national reports.
- PREVIEW: centralised reference data — country/field-staff/gear/port/species lists, conversion factors, observer data codes, vessel definition lists, FAO ASFIS species list.
- Field capture apps (e-reporting suite): OnBoard (electronic logsheet on fishing vessels), OnShore (landing-side), OLLO (Android observer app for longline), Tails (coastal staff collect tuna/reef catch info from small-scale fishers), Ikasavea (market, landing and socio-economic survey data, offline).
- Purpose framing: data collected for management (national needs, commission reporting, scientific advice) — no quota-balancing machinery described; management via the data record itself.

### Archipelago Marine Research — monitoring-services pole

Evidence layer: A for services/product existence (Tier-2), B for workflow details (product pages, not user manuals).

- Services: At-Sea Observers ("monitor compliance … supporting in-season management, stock assessment, and scientific research"); Dockside Monitoring ("independent verification of landed catch", certified dockside observers for "data collection, validation"); Electronic Monitoring ("EM products and services for commercial fisheries worldwide").
- Products: FishVue Vantage (EM hardware, HD cameras + gear sensors, real-time transmission cellular/satellite); FishVue LIME (zero-touch real-time data collection for coastal/inshore fleets); FishVue Mobile (trial deployments); FishVue FLOAT (ELOG) — "electronic fishing log application; vessel operators enter and submit their fishing log information electronically"; audits; species ID materials; retains log data from previous trips; FishVue Interpret (review/annotation of EM data — "a typical fishing trip may generate hundreds of hours of data"); FishVue Fleet (real-time visibility for "agencies, industry, skippers, and service providers … monitoring, compliance, and operational decision-making"; current + historical vessel activity; detect events); FishVue AI (AI-assisted review, human-validated).
- Position: the verification/capture layer that feeds the same record world; serves both regulators and industry.

### Global Fishing Watch — boundary specimen

Evidence layer: A (Tier-2).

- Public-interest transparency platform: satellite imagery, vessel GPS/AIS data, machine learning over "millions of gigabytes"; open map, Marine Manager portal, Vessel Viewer, open APIs; trains fisheries authorities to use tracking data; supports MPA monitoring.
- Crucially: publishes/visualises activity; no entitlements, no catch records of record, no reporting obligations, no balancing machinery. Sits beside the Type (consumable by it), not inside it.

### Pelagic Data Systems — boundary specimen

Evidence layer: A (Tier-2).

- Vessel Tracking System hardware for any size vessel (solar, self-activating), add-on sensors (temperature, gear immersion), cloud analytics dashboard (trips, vessel history, MPA incursion alerts, CPUE).
- Its own framing: fishing effort + "in conjunction with landings data" → management insight. Confirms tracking is an input layer; the management record lives with landings/catch accounting elsewhere.

## Cross-product Comparison

| Dimension | Fishserve (NZ) | SPC TUFMAN 2 | Archipelago | GFW / PDS (boundary) |
|---|---|---|---|---|
| Seat | Crown-contracted registry/administration | National/regional data management | Monitoring service provider + tech | Transparency / tracking |
| Frame objects | QMA × species stocks; TACC/ITQ/ACE | Fisheries (tuna) data programs | Fisheries programs under client regulations | Ocean areas, vessels |
| Activity record | Trips, fishing/non-fishing events via e-logbook; GPR positions | Logsheets (operational), observer data, landing surveys | Trips/hauls via EM + FLOAT e-log; positions via sensors | Detected fishing activity (AIS/imagery) |
| Catch record | Per-event e-catch reports; MHR/LFRR returns; balances vs ACE | Catch/effort data, catch estimates | Verified catch (dockside/EM/observer) | none (PDS: needs landings data) |
| Entitlement accounting | Core (ITQ/ACE, transfers, deemed values) | none | verifies against rules/quotas (client-defined) | none |
| Verification layer | validation + error correction in-system | QC processes | observers/dockside/EM as product | ML detections |
| Reporting out | Public registers, aggregate catch reports | T2 Reports, WCPFC templates, CES extracts | compliance reports to agencies/industry | open data/APIs |
| Users | permit/quota holders, LFRs, public | national fisheries administrations | agencies, industry, skippers | public, authorities, researchers |

Convergences (layer B → C):
- All management-side products organize records around **defined fisheries/stocks under governing rules** (B: 3/3).
- All maintain **fishing-activity records** (trips/events/logsheets) attributed to **vessels** (B: 3/3).
- All carry **catch records** — per-event declarations, landing/harvest returns, or verified catch (B: 3/3).
- The record feeds **management consequence**: balancing against entitlements and charges; commission/national reporting; compliance verification; assessment data (B: 3/3).
- Capture is multi-channel: self-declaration (e-logbooks/logsheets), independent verification (observers/dockside/EM), automatic position reporting (GPR/VMS/AIS) (B: 3/3, implementations vary).

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant (jointly-held; remove any one and the Type collapses)

1. **The fishery's governing frame** — the system organizes its world around defined fisheries (identified fish stocks × areas, i.e. management units) carrying the rules and limits under which capture is allowed — catch limits/entitlements, effort limits, seasons/closures, gear rules — as applied configuration, not static documents. Remove → generic marine/fleet operations or a statistics database with no governed subject.
2. **The fishing-activity-and-catch record of record** — persistent identified records of fishing operations (trips/voyages, fishing events with effort attributes, and species-level catch, at-sea or at landing) attributed to authorized participants (vessels/fishers) within the frame; captured through self-declaration (logbooks/e-logbooks, landing reports), independent verification (observers, dockside, electronic monitoring), and/or automatic position reporting. Remove → pure vessel tracking, monitoring dashboards, or science samples.
3. **The management loop over the record** — the system acts on the record so the record has management consequence: catch/effort accounted against the frame's limits and obligations (balances, overage treatment), records validated and corrected, obligations reported (regulatory returns, commission reporting, public registers), and/or data accumulated to govern the resource (assessment feed). Remove → an anglers' logbook app or an inert statistics archive.

Jointly-held is load-bearing: 1 alone = a rules compendium / generic operations manager; 2 alone = fishing logbook; 3 alone = enforcement machinery with no governed record; 1+2 without 3 = logbook archive; 2+3 without 1 = disconnected reporting; 1+3 without 2 = empty rule engine.

### L1 — Common Mature Structure (very common, not definitional)

- vessel register and fishing permits/licensing; participant registers (incl. licensed receivers/processors)
- quota/entitlement machinery (shares, annual entitlements, transfers, balances) — dominant in commercial ITQ regimes
- electronic catch reporting with validation and error-correction workflows
- periodic returns/declarations (harvest returns, landing/processor reports)
- vessel position monitoring (VMS/GPR/AIS) with retention
- observer / dockside / electronic-monitoring verification programs
- master/reference data (species codes, stock areas, gear types, conversion factors, vessel lists)
- regulatory and inter-governmental reporting outputs; aggregate catch reporting
- public registers / transparency publications
- field-side mobile capture; offline-capable survey apps for small-scale fisheries
- dashboards, alerts (MPA/closed-area incursions), real-time fleet/compliance monitoring

### L2 — Variant / Optional Structure

- regime family: quota-based (ITQ/ACE), effort-based, license-plus-limits, community/artisanal data collection
- quota trading/marketplace functionality (inside the registry in NZ; third-party elsewhere — not verified outside sample)
- protected-species / bycatch interaction reporting hooks
- science layer interfaces (assessment tools, conversion factors, CPUE analytics)
- supply-chain/traceability extensions from landing onward
- recreational-fisheries licensing populations (adjacent, not sampled)
- high-seas / RFMO obligation contexts
- small-scale/artisanal variants (data collected from fishers at landing/markets, sometimes without vessel identity)

### L3 — Vendor-specific (kept out of the final document)

- Fishserve: CEDRIC product; MHR/LFRR/ERS API specifics; deemed values; GPR 10-minute records; TACC Atlas
- SPC: TUFMAN 2/T2/CES/PREVIEW naming; OnBoard/OnShore/OLLO/Tails/Ikasavea suite; WCPFC template specifics
- Archipelago: FishVue Vantage/LIME/FLOAT/Interpret/Fleet/AI product line
- GFW: Marine Manager/Vessel Viewer naming; PDS: VTS hardware specifics

## Rejected Findings

- **"Fisheries Management = quota management (ITQ/ACE)"** — rejected: TUFMAN 2 (evidence A) manages fishery data with no quota-balancing machinery and is squarely in-type; effort-based and small-scale regimes also satisfy. Quota machinery is the dominant modern implementation (L1/L2), not the invariant.
- **"Fisheries Management = vessel tracking/VMS"** — rejected: PDS/GFW/AMR Fleet show tracking is an input layer; tracking products explicitly need landings/catch data to become management; no entitlements/records of record.
- **"Fisheries Management ≈ Aquaculture Management"** — rejected: no sampled fisheries product holds reared populations in owned production units or stocking→harvest cycles; no sampled aquaculture product holds wild-capture entitlements/effort/landings (consistent with the aquaculture pass's own rejection).
- **"The Type is government-only"** — rejected: AMR's products serve industry/skippers; the record world is shared across seats.

## Boundary Findings

- **vs Aquaculture Management** (§20, processed) — pre-hung flag DISCHARGED from this side: keep-both RATIFIED. Seam = the object world: reared population in an owned production unit across a stocking→harvest cycle (aquaculture) vs wild stock under a fishery's governing frame with capture effort, catch records, and entitlements/obligations (fisheries). Removal tests: remove production units + stocking/harvest cycle and add capture/quota/vessel/landing objects → Fisheries Management (the aquaculture pass's own test, confirmed); remove the fishery frame + capture records and add owned units + rearing loop → Aquaculture Management. No structural overlap beyond "fish + water".
- **vs Marine Fleet Management / Vessel Operations Platform (§18)** — vessels as logistics/maintenance/crew assets vs the fishery's entitlement/catch world; vessels appear here as authorized participants in the fishing-activity record, subordinate to the fishery frame. (Unprocessed siblings; flag noted for their passes.)
- **vs monitoring/transparency platforms (GFW class) and VMS/telematics (PDS class)** — layers feeding the Type; no records of record, no entitlements, no obligations. If a platform starts holding authoritative catch/entitlement records, it crosses into this Type.
- **vs Food Traceability Platform** (§20) — post-landing chain of custody vs the fishery's capture-side record; traceability starts where landing records end.
- **vs Government Licensing Management** (§24) — licensing is one register slice here (permits), embedded in the catch/effort/quota world; the government-licensing Type centers the licensing program itself.
- **vs Environmental Monitoring Platform / stock-assessment science tools** — consumers/analysts of the record; assessment instruments (e.g. MULTIFAN-CL class) are science tools, not the management system of record.
- **vs Forestry Management** (§20 sibling, unprocessed) — parallel resource-governance pattern (harvest rights, permits, harvest records on a regulated resource); no conflict; watch at that pass.
- **vs Public Data Portal** (§02.12) — GFW/PDS publish data; registers/reports here are outputs of a record, not the Type's center for the portal itself.

## Uncertainties

- US IFQ catch-accounting systems (NOAA Fish Online, Alaska eLandings) unreachable (timeouts/404 ×2 each) — the quota-balancing workflow is evidenced primarily via NZ Fishserve; claim strength for "balancing catch against entitlement" kept at cross-product-commonality level with a single deep implementation.
- Industry/fishing-company products (Maritech class) unreachable — the industry seat is evidenced via Fishserve's client-side functions, AMR's industry-facing products, and PDS/GFW framing; deeper industry-ERP catch/quota workflows unverified.
- TUFMAN 2 module detail behind a JS shell — module claims kept at the FAME division-page level (general capabilities, no UI specifics).
- No precise operational numbers (deadlines, file formats, position-report intervals beyond the directly-observed GPR note) asserted in the final document.
- Recreational fisheries management software not sampled (license-sales platforms) — treated as adjacent, not surveyed.

## Final Synthesis

Fisheries Management software is the system of record for governing wild-capture fisheries. Its world model: defined fisheries (stocks × areas) carry the governing rules and limits; authorized vessels/fishers hold rights and obligations within those fisheries; their fishing operations (trips, events, effort) and their catch are recorded through self-declaration, independent verification, and position reporting; the record is then acted upon — validated and corrected, balanced against entitlements and limits, reported to authorities and commissions, published through registers and aggregate reports, and accumulated as the data record that governs the resource. Two dominant seats share this model: the authority/registry pole (Fishserve class — permits, quota/ACE, returns, public registers) and the national data-management pole (TUFMAN class — catch/effort databases feeding commission reporting and assessment), with the monitoring-service pole (AMR class) supplying the verification layer and boundary platforms (GFW, PDS) supplying visibility inputs. The defining core is deliberately regime-neutral: quota machinery, VMS, electronic monitoring, and e-logbooks are common modern implementations, while paper logbooks, license registers, and effort-based regimes satisfy the same core historically.
