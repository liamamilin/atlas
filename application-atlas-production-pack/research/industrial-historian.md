# Research Notes — Industrial Historian

Research date: 2026-09-08. Evidence layers: **[A]** = directly observed on an official source for a named product; **[B]** = cross-product commonality across the researched sample; **[C]** = canonical inference from cross-product comparison and Type-boundary reasoning.

---

## Research Goal

Understand what an Industrial Historian (process historian / plant historian / data historian) really is as an Application Type: what exists inside it, how process data flows through it, who consumes it, and where its boundary sits against SCADA, HMI, DCS, time-series database tooling, IIoT platforms, and compliance data systems (CEMS).

---

## Initial Boundary

Working hypothesis at start (to be tested, not asserted):

- Core purpose: continuously collect time-stamped process measurements (tags) from control/automation systems, store them efficiently for long periods, and serve them back for trending/analysis/reporting.
- Users: process/control engineers, operations, reliability, energy/quality/reporting roles, data analysts/IT.
- Nearest neighbors: SCADA (supervisory control), HMI (operator screens), DCS (control execution), Time-series Database Workbench (§13 IT-side sibling), CEMS (compliance machinery on similar data), IIoT platform (device connectivity), Meter Data Management (utility sibling).
- Known prior evidence in STATUS.md: the DCS pass (2026-09-07) explicitly held Industrial Historian as a distinct Type, corroborated by two vendors' product taxonomies (Emerson sells DCS/SIS/PLC/MES/SCADA as separate lines; Honeywell separates DCS vs SCADA vs safety), and noted "integrated historians (continuous + event + batch flavors)" as a standard capability of DCS — i.e., a bundled historian does not dissolve into the DCS Type. The HMI pass (2026-09-08) held "built-in historian" OUT of the HMI core. The CEMS pass (2026-09-08) defined its own seam as "remove limits → historian".

---

## Research Questions

1. What is the unit of storage — what exactly does a "tag"/"point" record look like (timestamp, value, quality, metadata)?
2. How does data get in — what collects it, over what protocols, and what happens when the network breaks?
3. How is data stored — why not a conventional relational database; what role do compression and interpolation play?
4. How does data get out — retrieval semantics (raw vs interpolated vs aggregated), query surfaces, export paths?
5. What client surfaces exist — trend viewers, dashboards, Excel, web, APIs?
6. What lives alongside process values — alarms, events, batch context, asset models, calculated tags?
7. Who uses the system for what jobs?
8. Where is the boundary vs SCADA/HMI/DCS-bundled historians, vs generic time-series databases, vs CEMS/MDM-class measurement archives?

---

## Representative Products

Selected for market representation, documentation reachability, differing product philosophy, and differing customer tier:

| Product | Company | Pole in the market | Tier reached |
|---|---|---|---|
| AVEVA PI System (PI Data Infrastructure) | AVEVA (formerly OSIsoft) | market-defining enterprise operations-data infrastructure | Tier 2 (official product page + FAQ) |
| AVEVA Historian (formerly Wonderware Historian) | AVEVA | high-speed historian bundled beside HMI/SCADA estates | Tier 2 (official product page, incl. Historian Client app detail) |
| Canary Historian (Canary System) | Canary Labs | independent lightweight/modern historian, site→enterprise | Tier 1/2 (official product tour pages with structural detail) |
| Aspen InfoPlus.21 (IP.21) | AspenTech | process-industries historian within a manufacturing/SCM suite | Tier 2 (official product page + FAQs) |

Targeted but unreachable (abandoned per source-access rules): GE Vernova Proficy Historian (404/403 ×2), Rockwell FactoryTalk Historian (404), Honeywell PHD (redirect to portal home), Inductive Automation Ignition Tag Historian docs (404 ×2), docs.aveva.com Zoomin documentation portal (SPA shell only ×2), COPA-DATA Zenon historian (404), AVEVA historian-myths white paper (binary PDF). The automation-suite-bundled and SCADA-embedded poles are therefore held at market-structure strength, corroborated indirectly (see Uncertainties).

---

## Sources

- AVEVA — AVEVA PI System product page: https://www.aveva.com/en/products/aveva-pi-system/ (fetched 2026-09-08)
- AVEVA — AVEVA Historian product page: https://www.aveva.com/en/products/historian/ (fetched 2026-09-08)
- Canary Labs — product tour pages: https://canarylabs.com/ , /product/historian.html , /product/data-collectors.html , /product/store-and-forward.html , /product/virtual-views.html , /product/events.html , /product/axiom.html (fetched 2026-09-08)
- AspenTech — Aspen InfoPlus.21 product page + FAQs: https://www.aspentech.com/en/products/pages/aspen-infoplus21 (fetched 2026-09-08)
- Prior-pass corroboration recorded in STATUS.md: distributed-control-system-dcs (2026-09-07), hmi (2026-09-08), emissions-monitoring-cems (2026-09-08), digital-twin-platform (2026-09-07)

Access limitations recorded: no Tier-1 operational documentation (installation/administration/query manuals) was reachable for any sampled product except Canary's product tour pages; docs.aveva.com is a JS-only portal; GE/Rockwell/Honeywell/Inductive sources 403/404. All precise operational facts below are confined to what the reached pages actually state.

---

## Product Observations

### AVEVA PI System (AVEVA / OSIsoft)

- Positioning: "an integrated portfolio... to collect, cleanse, store, enrich and visualize real-time operations data"; framed as "a single trusted source of truth" for industrial operations. [A]
- Storage granularity claim: "Collect and store real-time data from your operating assets with sub-second granularity." [A]
- Acquisition: "hundreds of data connectivity options for nearly all industry and vendor-specific protocols. Automatically capture high-volume data streams in real-time from on-premises control systems, remote and mobile assets, sensors, IIoT devices and gateways." Productized as PI Interfaces, PI Connectors, AVEVA Adapters. [A]
- Reliability machinery: "data collection options include data buffering... configure for high availability, automatic failover and auto-discovery of new data sources." [A]
- Context layer: "Configure reusable asset models, events and analytics based on multiple data streams and conditions without programming." (asset-framework concept; productized as add-ons). [A]
- Delivery/consumption: self-service visualization with "web and mobile accessible data displays" (PI Vision), Excel integration (PI DataLink), report generation (RtReports), transfer to BI/analytics (PI Integrator for Business Analytics), "open APIs, SDK and message format" (PI System Access). [A]
- Topology: "edge to cloud data management" — Edge Data Store for remote assets, on-prem storage, cloud aggregation of multiple sites. [A]
- Retention depth: "engineers and analysts can use decades worth of historical real time and forecasted operational data"; "Industrial operations have relied on AVEVA PI System... for over 40 years." [A] — strong signal for the historical check: the Type is 40+ years old.
- Named users: operators, process engineers, plant managers, data analysts, executives. [A]
- PI Server described as "the trusted, high-volume, and real-time data storage, contextualization, analytics, and notification engine at the heart" of the portfolio. [A]
- Commercial/positioning stats (25/25 top pharma, 1000+ utilities, 75% of crude production, 9/10 miners) — marketing claims, noted as vendor positioning only. [A]

### AVEVA Historian (AVEVA, formerly Wonderware Historian)

- Positioning: "a process database integrated with operations control that gives you access to your process, alarm, and event history data." [A]
- Storage: "combines advanced data storage and compression techniques with an industry-standard query interface"; "Unique 'history block' technology captures plant data hundreds of times faster than a standard database system and utilizes a fraction of the conventional storage space"; "Historian handles time-series data, as well as alarm and event data." [A]
- Data integrity semantics: "manages low bandwidth data communications, late-coming information, and even data from systems with mismatched system clocks. Ensuring high resolution data is captured accurately." [A] — direct evidence that out-of-order/late arrival and clock skew are first-class problems of this Type.
- Deployment span: "monitor a single process or an entire facility, storing data locally and aggregating data at the corporate level." [A]
- Relationship to control products: "the perfect companion to AVEVA's... HMI and SCADA"; integrates with InTouch HMI, Edge, Plant SCADA, System Platform. [A] — historian sits beside (not inside) the supervisory/control layer.
- Retention span: "Preserve everything from short-term diagnostics to long-term records needed to support regulatory requirements." [A]
- Historian Client surfaces (named, official): Trend application (desktop graphing for real-time and historical trend analysis; pause/play/replay; drag-drop data points; trend/stacked/X-Y/batch trend charts; "retrieval styles to transform data results"; annotations; alarm details overlaid in context incl. acknowledgment information); Query application (query generation without SQL expertise; drag-and-drop tag selection; retrieval styles; standalone or with Trend/Excel); Web application (indexed search over tags/keywords; dashboards with drilldown/pan/zoom; process comments, alarms and acknowledgements "captured inline with Historian data"); Excel add-in (import "live values, history values, aggregate values, summary system values, and event snapshot values"; Tag Analysis graphs/statistics/configuration/limit info). [A]
- Efficiency claim: "Reduce data storage costs by more than 80% through ultra-efficient data storage algorithms" (vendor claim; kept product-specific). [A]
- Continuity: "High availability and disaster recovery options." [A]

### Canary Historian (Canary Labs)

- Positioning: "The time series database built for industrial automation"; "The Data Historian For Industrial Automation"; same solution "works as well on site as it does for the entire enterprise"; "a single Canary Historian can hold up to two million tags" (vendor figure, product-specific). [A]
- Storage engine: "a NoSQL time series database that uses loss-less compression algorithms... without requiring data interpolation"; "specifically built and optimized for the writing and reading of this specialty time series data and never interpolates the data archive"; explicitly anti-relational framing ("too much data for a relational database to store"); SQL-compatible query surface ("users can still query the data using standard SQL"). [A]
- Tag anatomy (the most explicit structural statement in the sample): "Every tag... can contain: tag name; 100+ meta data properties (engineering units, descriptions, limits, and more); timestamps; values (booleans, floats, integers, strings, etc); quality score." [A]
- Acquisition: Data Collectors for OPC DA, OPC UA, MQTT Sparkplug B; from Ignition/CygNet/GEO/Plant SCADA; SQL databases (MSSQL, MySQL, Oracle); CSV files; manual data entry; custom collectors via gRPC and Web APIs; collectors deliberately unlicensed. [A]
- Delivery integrity: Store & Forward — "should your connection... be interrupted... the Store and Forward service will begin to write all data to the local disk automatically. As soon as the network connection returns, your locally buffered data backfills to the database"; redundancy and DMZ single-direction proxy uses. [A]
- Context layer: Virtual Views — "Modeling data should be done post-archiving"; views alias/restructure tag names via regular expressions and build asset models without duplicating data; "a single tag... can belong to multiple asset models"; access can be restricted per model ("limit their database access to only their equipment"); can incorporate external metadata tables. [A]
- Derived data: Calculation Server — calculated tags, real-time and historical KPIs. [A]
- Event machinery: Events — rules over tags/calculated tags; violations "documented" with notification; event reports compute metrics over event durations; "All events are written to an internal SQL database." [A]
- Consumption: Axiom (HTML web client: trending, ad-hoc calculations across trends, statistical analysis, time-shift for seasonal comparison, time buckets of aggregated values, CSV export, playback of historic events over saved dashboards, asset-templated dashboards, scheduled email reports); Excel add-in (live data inside Excel). [A]
- Scale/longevity claims: 30,000 installs in 70 countries; founded 1985 (vendor stats). [A]

### Aspen InfoPlus.21 (AspenTech)

- Positioning: "scalable, real-time data historian... purpose-built for the process industries, it collects, merges and analyzes time-series data across industrial operations and applications." [A]
- Role framing (FAQ): historians "provide a centralized, accurate record of all process data, which is essential for performance monitoring, troubleshooting, compliance, process improvement, and as a foundation for advanced analytics and AI/ML initiatives." [A]
- Acquisition breadth (FAQ): "time-series data from automation and control systems (DCS, SCADA, PLCs), ERP systems, manufacturing execution systems (MES), laboratory information management systems (LIMS), and other third-party applications." [A]
- Computation: "Embedded real-time computation engines (KPI, SPC/SQC) support performance management and analysis across an enterprise." [A]
- Interfaces: aspenONE Process Explorer ("modern, web-based interfaces for rich visualizations, dashboards, and reporting"); connectivity "standard interfaces (e.g., OPC, ODBC, COM, REST services)" incl. ERP (SAP) integration. [A]
- Batch flavor: Aspen Production Record Manager — "collecting and contextualizing event and batch process data... production loss analysis, electronic batch sheet generation, and compliance with industry standards such as ISA-88"; "Capture critical continuous and batch process data." [A]
- Long-retention reality: case study — DuPont migrated 23 years of historical data from OSI PI into IP.21 (also evidence that archives outlive products and migrate between historians). [A]

---

## Cross-product Comparison

| Dimension | AVEVA PI System | AVEVA Historian | Canary Historian | Aspen IP.21 |
|---|---|---|---|---|
| Unit of record | tags of sub-second operations data [A] | tags in "history blocks"; process + alarm/event data [A] | tags: name + 100+ metadata + timestamped values + quality [A] | "centralized, accurate record of all process data" [A] |
| Acquisition | hundreds of vendor-neutral connectors; buffering; auto-discovery [A] | high-speed collection; low-bandwidth handling; late data; clock skew [A] | collectors: OPC DA/UA, Sparkplug B, SCADA, SQL, CSV, manual; unlicensed [A] | DCS/SCADA/PLC + ERP/MES/LIMS; OPC/ODBC/COM/REST [A] |
| Storage philosophy | high-volume real-time storage at portfolio heart [A] | compressed "history blocks", fraction of conventional storage [A] | NoSQL time-series, lossless compression, never interpolates archive [A] | (not stated on reached page) |
| Retrieval | "decades" of data usable "in seconds"; APIs/SDK [A] | retrieval styles; query builder w/o SQL; web search [A] | standard SQL queries; aggregates via clients [A] | computation engines KPI/SPC/SQC; web visualization [A] |
| Context | asset models, events, analytics (configurable) [A] | integrates w/ System Platform context [A] | Virtual Views: post-archive aliasing + asset models [A] | batch/event contextualization (Production Record Manager) [A] |
| Clients | PI Vision (web/mobile), DataLink (Excel), RtReports [A] | Trend / Query / Web / Excel add-in [A] | Axiom (web trending/dashboards/playback), Excel add-in [A] | aspenONE Process Explorer (web) [A] |
| Topology | edge→on-prem→cloud aggregation [A] | single process ↔ facility ↔ corporate aggregation [A] | site historian ↔ enterprise historian; backfill; DMZ proxy [A] | enterprise-wide, multi-plant benchmarking [A] |
| Side data | events/analytics configurable [A] | alarm/event history inline w/ process data [A] | Events module w/ SQL store; calculated tags [A] | event/batch records (ISA-88) [A] |
| Suite relationship | infrastructure product feeding BI/analytics/AI [A] | "companion" to HMI/SCADA lines [A] | independent; collects from SCADA systems [A] | member of aspenONE manufacturing suite [A] |

Convergences that appear in all four regardless of philosophy or tier: **[B]**

1. Named process measurements (tags) held as long-term time-stamped archives.
2. Continuous automated acquisition from control/automation systems (never primarily manual), with explicit machinery for interrupted/low-bandwidth delivery (buffering; late-coming data; clock mismatch).
3. A purpose-built storage engine for high-rate time-series at economic storage cost (compression emphasized everywhere; storage substrate itself varies).
4. Trend-first retrieval (every product leads with a trend/graphing surface), plus query/API/Excel paths.
5. Site-to-enterprise scaling with aggregation.
6. Context and derived data (asset models, calculated tags, events) layered on top of the raw archive, productized in different places.
7. Long retention measured in decades; archives migrate between products.

Divergences (implementation space, not Type space): compression mechanism (lossless/no-interpolation vs compressed blocks), storage substrate (SQL-extended vs NoSQL vs proprietary), where asset context is built (pre-archive model vs post-archive virtual views vs batch record manager), packaging (standalone vs suite companion), collector licensing.

---

## Abstraction

### Level 0 — Defining Invariant (deliberately small)

An Industrial Historian is the plant-side archival infrastructure for process measurement data. Its defining core, held jointly:

1. **The automated process-measurement archive of record.** Named process measurements ("tags") are acquired continuously and automatically from control/automation sources (DCS/SCADA/PLC/protocols/gateways), and each tag is held persistently as a time-ordered series of timestamped samples (value; commonly with a quality indication). Remove → a live dashboard or a manual-entry data warehouse; no longer a historian.
2. **A high-density archival engine built for industrial rates and long retention.** A storage layer purpose-built to sustain continuous high-frequency writes and to hold the archive economically for years-to-decades — this is why conventional relational databases are consistently framed as inadequate across the sample. Remove → SCADA screens/logger output that cannot hold or serve years of high-rate history.
3. **Retrieval for analysis — the archive exists to be replayed.** Consumers query across arbitrary time ranges and receive trends, series, aggregates, and reports; consumption is trend-first and time-range-based, not just last-value display. Remove → a black-box recorder with no analysis surface.

Jointly-held is load-bearing:

- 1 without 2+3 = current-value table / simple logger.
- 1+2 without 3 = black-box recorder (strip-chart lineage), not a software historian.
- 1+3 without 2 = generic/manual time-series store, not an industrial archive.
- 2+3 without 1 (no control-system acquisition, no plant semantics) = generic IT time-series database — Time-series Database Workbench territory.

### Level 1 — Common Mature Structure (expected in the market, not definitional)

- Delivery integrity: store-and-forward buffering at the collector, timestamped backfill after outages; handling of late-coming and out-of-order data, low-bandwidth links, clock mismatch. [A: Canary, AVEVA Historian, PI buffering]
- Alarm/event history alongside or beside process values (products differ on whether it is inline, a module, or an add-on). [A: AVEVA Historian inline; Canary module; PI configurable "events"]
- Context/asset model layer over flat tags (equipment hierarchies, aliasing, multi-model views). [A: PI asset models; Canary Virtual Views; IP.21 batch records]
- Derived/calculated tags and KPI machinery. [A: Canary Calculation Server; IP.21 KPI/SPC/SQC engines]
- Trend viewer, web dashboards, Excel add-in as the standard consumption trio; APIs/SDK/SQL for third-party consumption. [B: all four]
- Site→enterprise hierarchy: local/edge historians aggregating to a corporate one; cloud aggregation appearing in the modern era. [A: PI edge-to-cloud; AVEVA Historian local↔corporate; Canary site↔enterprise]
- Redundancy / high availability / disaster-recovery postures. [A: PI, AVEVA Historian; Canary via redundant logging sessions]
- Long retention (decades) with archival tiering implied by "short-term diagnostics to long-term records". [A]

### Level 2 — Variant / Optional Structure

- Compression philosophy: lossy, interpolation-friendly compressed snapshots vs lossless raw storage with interpolation only at query time — explicitly a market split (Canary markets against interpolation; AVEVA markets compression efficiency). Mechanism is a variant; economical density is the invariant.
- Packaging: standalone enterprise infrastructure vs automation-suite companion (HMI/SCADA line) vs DCS-bundled historian (PHD/Process-Historian class, corroborated via the DCS pass) vs SCADA-platform-embedded tag historian (Ignition class — market-structure strength only).
- Customer tier: enterprise multi-site vs single-process/single-facility deployment. [A: AVEVA Historian spans this explicitly]
- Domain flavor: continuous process vs batch (ISA-88 event/batch records). [A: IP.21]
- Protocol portfolio per product (OPC DA/UA, MQTT Sparkplug B, proprietary suite links, SQL/CSV/manual sources).
- Manual data entry as an auxiliary collector option. [A: Canary]
- Licensing models (unlicensed collectors vs tag/point-based commercial models).
- Security postures (DMZ proxying, unidirectional flows). [A: Canary]

### Level 3 — Vendor-specific (kept out of the canonical document)

- "History block" technology (AVEVA Historian); >80% storage-cost reduction claim; Historian Client app names.
- PI portfolio module names (AF-class asset models, DataLink, Vision, RtReports, Edge Data Store, CONNECT); 40-year/industry-share stats.
- Canary: 2M-tags-per-historian figure, unlicensed collectors/SAF, gRPC API, Sparkplug B advocacy, Views-service regex machinery, Axiom playback.
- AspenTech: Production Record Manager, electronic batch sheets, ISA-88 packaging, embedded SPC/SQC engines, DuPont 23-year migration case.

---

## Rejected Findings (anti-overfit)

- **"Historian = OPC connectivity."** Sample acquires via OPC DA/UA, MQTT Sparkplug B, SQL, CSV, REST/COM, and vendor-native links; PI claims hundreds of connectivity options. Protocol-agnostic is the invariant. Rejected as definitional.
- **"Historian = lossy compression with interpolated raw data."** Contradicted in-sample: Canary is lossless and "never interpolates the data archive." Compression *mechanism* is a variant; density/retention is the invariant.
- **"Historian = relational/SQL Server-based."** AVEVA Historian's lineage is SQL-based; Canary is explicitly NoSQL; both are historians. Storage substrate is implementation.
- **"Historian = single-plant software."** All four products scale site→enterprise; conversely AVEVA Historian explicitly serves "a single process." Scale is a deployment variant.
- **"Historian = standalone product only."** DCS/SCADA-bundled historians satisfy the same core (DCS pass recorded vendor taxonomies selling historians as distinct lines, and DCS listing "integrated historians" as a capability, not the DCS core). Bundling is packaging.
- **"Alarm/event storage is part of the definition."** Only one product headlines inline alarm/event history; others modularize it. Held at Level 1.
- **"Cloud aggregation / AI-readiness is definitional."** The Type is 40+ years old [A]; cloud and AI layers are modern additions.
- **"Manual entry disqualifies."** One product offers manual entry as an auxiliary collector; the defining acquisition is machine-sourced. Auxiliary capability, not boundary.

### Historical / market-sample check (required before freezing)

- The oldest operational claim in-sample: PI "relied on... for over 40 years" [A]. A 1990s-generation historian (PI Data Archive, Wonderware IndustrialSQL Server, Honeywell PHD class, early IP.21) — tags from DCS/PLC over proprietary/OPC-DA-era links, compressed archives, trend + Excel/report retrieval — satisfies all three defining legs with no cloud, no asset model, no web client, no Sparkplug.
- DCS-bundled historians (Experion PHD class, PCS 7 Process Historian class) satisfy the same core with bundling as a variant — consistent with the DCS pass's vendor-taxonomy evidence.
- The conceptual predecessor lineage (circular-chart recorders, strip charts, data loggers) satisfies legs 1–2 in primitive form but not leg 3 (no query/replay surface) — correctly excluded as black-box recorders, confirming leg 3 is load-bearing.
- Conclusion: the definition holds across eras, packaging, and tiers; nothing era-specific (web/cloud/OPC-version/compression-brand) enters the core.

---

## Boundary Findings

| Neighboring Type | Relationship | Discriminator (what to remove/add to cross the seam) |
|---|---|---|
| SCADA | adjacent, same vendors | SCADA = supervisory **control** of distributed assets: telemetry, alarming, operator control write-back. Historian = neutral archival infrastructure with no control duty. Evidence: AVEVA positions Historian as "companion" to its HMI/SCADA lines [A]; Canary collects *from* SCADA historians to make the record "more robust... for reporting" [A]; DCS pass: distinct vendor product lines. Remove the archive/analysis layer → SCADA dashboard; give the historian control write-back → it stops being a historian. |
| HMI | adjacent | HMI = engineered operator screens + live process-data layer + write-back loop (per HMI pass). The HMI pass itself held "built-in historian" OUT of its core — from this side the seam is consistent: the historian has no operator write-back and no screen-engineering core. |
| Distributed Control System / DCS | adjacent, bundle relationship | DCS = control execution + integrated plant-wide configuration. A historian may be bundled in the DCS estate (standard capability of DCS per the DCS pass) but the archival-analysis core is a distinct Type; Emerson/Honeywell sell historians as separate lines. |
| Time-series Database Workbench (§13) | sibling on the IT side | Generic TSDB tooling serves arbitrary machine-generated metrics for IT/analysis users; the industrial historian is defined by control-system acquisition + quality-carrying process semantics + plant consumption (trends, replay, operations reporting). Convergence noted (Canary exposes SQL; TSDBs gain industrial connectors) but the seam (source + semantics + consumer) holds. |
| CEMS / Emissions Monitoring (§21, processed) | consumer machinery on similar data | That pass's own formulation: CEMS = historian-like handling + regulated-source identity + limit evaluation + compliance record; "remove limits → historian." The historian holds process data without compliance transformations or permit semantics. |
| Industrial IoT Platform (§16, unprocessed) | adjacent | Per the digital-twin pass's forward note: IIoT's packaged outcome is device connectivity/device management; the historian's packaged outcome is the measurement archive of record. An IIoT platform typically *feeds* a historian. |
| Meter Data Management System (§19, unprocessed) | structurally near sibling | MDMS = time-stamped meter-read archive + validation/estimation + billing consumption — same archival skeleton, but meter-domain VEE and billing semantics replace plant acquisition/consumption. Flagged for that pass to sharpen. |
| OEE / MES / APM applications | consumers | They consume historian data and add their own object models (production orders, asset health); none is the neutral archive of process measurements. |
| Environmental Monitoring Platform (§21, processed) | adjacent domain loop | That Type monitors defined environmental media/points with alerts; the historian is open-ended plant measurement infrastructure whose tags may *include* environmental points. Different defining loop (observation-vs-limit alerts vs archive-of-record + analysis). |
| Building Energy Management / BMS trend logging | distant variant | Same archival core in a building domain; scale and consumer set differ. Held as domain variant, not boundary failure. |

---

## Uncertainties

1. **No Tier-1 operational manuals reached** for PI, AVEVA Historian, or IP.21 (SPA portal / 403s). Structural claims rest on official Tier-2 pages plus Canary's detailed pages. Precision about archive internals (specific compression algorithms, interpolation modes, retention tiering, backfill windows) was deliberately not asserted anywhere.
2. **Automation-suite poles unreached**: GE Proficy Historian, Rockwell FactoryTalk Historian, Honeywell PHD, Ignition Tag Historian — the DCS-bundled and SCADA-embedded variants are held at market-structure strength (corroborated by the DCS pass's vendor-taxonomy evidence and AVEVA Historian's companion positioning), not by direct documentation this pass.
3. **Alarm/event storage universality**: evidenced inline in one product, modular in another, configurable in a third — held common-but-not-definitional.
4. **Interpolation-on-retrieval**: "retrieval styles" (AVEVA Historian) and "never interpolates the archive" (Canary) show retrieval semantics vary; exact modes were not documented on reached pages — no precise claims made.
5. **Interpolation/quality semantics at scale** (how quality propagates through aggregates) — unknown from reached sources; excluded from the document.

---

## Final Synthesis

An **Industrial Historian** is the industrial operation's archival system of record for process measurement data. Its defining structure is three jointly-held legs: (1) named process measurements acquired automatically and continuously from control/automation sources, held persistently as timestamped sample series (value + commonly quality); (2) a purpose-built high-density archival engine that makes years-to-decades of high-rate data economical to keep — the shared reason every product rejects conventional relational storage; (3) time-range retrieval for analysis — trends, aggregates, replay, reports, APIs — because the archive exists to be replayed and examined, not merely displayed live. Compression mechanism, storage substrate, packaging (standalone / suite companion / DCS-bundled), site-vs-enterprise scale, protocol portfolio, and context machinery (asset models, events, calculated tags, batch records) are variant space. The Type is 40+ years old and the definition survives the historical check; the boundary that matters most is against SCADA/HMI/DCS (control and supervision vs archive-and-analysis) and against generic time-series databases (control-system acquisition + plant semantics vs arbitrary machine telemetry).
