# Research Notes — Environmental Laboratory Management

Research date: 2026-09-08
Slug: environmental-laboratory-management
Directory node: §21 Environment, Sustainability & Climate — "Environmental Laboratory Management"

---

## Research Goal

Understand what software the market actually sells and laboratories actually run under the banner of "environmental laboratory management" (in the market, almost always "environmental LIMS" or "Water & Environmental LIMS"): what the system of record holds, how an environmental testing lab's work flows through it, which structures are environmental-specific rather than generic lab informatics, and where the Type's boundaries sit against LIMS (§22), Research LIMS (§23), Environmental Data Platform (§21 sibling), Environmental Monitoring (§21), CDS (§22), and Environmental Compliance Management (§21, processed).

## Initial Boundary (hypothesis before research)

- Core purpose hypothesis: system of record for an environmental testing laboratory — environmental samples (water/wastewater/soil/air/waste) flow from receipt through analysis to validated results and client/regulator deliverables.
- Likely users: sample reception/custody staff, bench analysts, QA/QC officers, lab managers, client services; external clients (consultants, utilities, industry) at the boundary.
- Nearest types: LIMS (§22), Research LIMS (§23), Environmental Data Platform (§21), Environmental Monitoring Platform / CEMS (§21), Chromatography Data System (§22, processed), Environmental Compliance Management (§21, processed), Water Quality Management (§19).
- Open questions: is this leaf just "LIMS sold to environmental labs" (domain instance), or does it carry its own defining machinery? What exactly is environmental-specific vs generic lab informatics?

## Research Questions

1. What are the core objects: sample, container/bottle, test/analysis, method, analyte, result, QC, batch/worklist, client, project, location/sampling point?
2. How does the sample lifecycle flow (collection → login → analysis → validation → reporting → archival/disposal)?
3. Which environmental-regulatory machinery is definitional vs common: chain of custody, holding times, program-driven sampling schedules, permit/limit checking, QC batch rules, accreditation (ISO 17025 / TNI/NELAP), electronic data deliverables (EDD)?
4. Who uses the system and on which surfaces (login bench, analyst worklist, QA review, client portal, manager dashboards)?
5. What is the commercial loop of contract labs (quotes, price lists, billing, subcontracting)?
6. Where is the boundary vs generic LIMS, vs environmental data platforms (result consumers), vs field/continuous monitoring?

## Representative Products (sampled)

Selection logic: market representation (enterprise platform + mid-market configurable + platform/template vendor), documentation completeness, different product philosophies, different customer tiers (municipal utilities, contract labs, small labs). All evidence is Tier-2 official product/solution/case-study pages; no Tier-1 help-center articles were reachable (see Sources / Limitations).

1. **LabWare** — LabWare LIMS enterprise platform + "LabWare WATER" purpose-built SaaS for water/wastewater/environmental testing. Enterprise pole + purpose-built SaaS pole. URL: labware.com/industries/water-environmental (fetched OK).
2. **LabLynx** — Environmental LIMS industry solution on the LabLynx LIMS Suite platform. Platform/template pole. URL: lablynx.com/industries/environmental-lims/ (fetched OK).
3. **Autoscribe Informatics** — Matrix Gemini LIMS "Water & Environmental" solution + Blue Ridge Analytical case study (real VELAP-accredited environmental contract lab). Mid-market configurable pole + real-lab usage evidence. URLs: autoscribeinformatics.com/industries/environmental-water-lims, /case-studies/meeting-the-need-for-lims-in-an-environmental-laboratory (fetched OK).

Rejected / unreachable candidates:
- **Promium (Element DataSystem)** — the archetype purpose-built environmental LIMS; promium.com timed out ×2 → abandoned per network rules. The independent purpose-built pole is under-sampled; LabWare WATER partially covers the purpose-built pole.
- **STARLIMS** — root page fetched OK (footer lists "Environmental Sciences"), but /environmental-sciences/ 403 ×2 → abandoned; no claims made about STARLIMS.
- **LabVantage** — root fetched OK; industries list has no environmental page (environmental sits under Government/Public Health at best) → not sampled as an environmental pole; no claims.
- **LabWare /solutions/environmental/** 403 ×1 — superseded by the reachable /industries/water-environmental page.

## Sources

- LabWare — "LIMS for Water, Wastewater & Environmental Testing Laboratories" — https://www.labware.com/industries/water-environmental — fetched 2026-09-08 (Tier-2, detailed product/solution page incl. FAQ)
- LabWare — root site — https://www.labware.com/ — fetched 2026-09-08 (Tier-2)
- LabLynx — "Environmental LIMS" — https://www.lablynx.com/industries/environmental-lims/ — fetched 2026-09-08 (Tier-2)
- LabLynx — root site — https://www.lablynx.com/ — fetched 2026-09-08 (Tier-2)
- Autoscribe Informatics — "Water & Environmental LIMS" — https://www.autoscribeinformatics.com/industries/environmental-water-lims — fetched 2026-09-08 (Tier-2)
- Autoscribe Informatics — root site + LIMS FAQ — https://www.autoscribeinformatics.com/ — fetched 2026-09-08 (Tier-2; includes vendor's own LIS-vs-LIMS-vs-ELN-vs-SDMS definitions)
- Autoscribe Informatics — case study "Meeting The Need For LIMS In An Environmental Laboratory" (Blue Ridge Analytical) — https://www.autoscribeinformatics.com/case-studies/meeting-the-need-for-lims-in-an-environmental-laboratory — fetched 2026-09-08 (Tier-2 case study)

**Source-access limitation:** no authenticated help-center / user-guide articles were fetched for any sampled product; all evidence is official marketing/solution/case-study pages. Per evidence rules: no numeric limits, no exact field schemas, no exact state-name lists, no default values asserted anywhere in the final document. The purpose-built independent vendor pole (Promium class) is under-sampled.

---

## Product A — LabWare (LabWare LIMS / LabWare WATER)

Evidence layer: A (directly observed on official pages), Tier-2.

Key observations:

- **Positioning**: "LIMS for Water, Wastewater & Environmental Testing Laboratories — streamline QC workflows while maintaining ISO/IEC 17025 compliance for soil, air, water & wastewater testing." Customers shown: water utilities (Scottish Water, Orange County Sanitation, OKC, City of Denton, Mass Water Authority, Rand Water, Sydney Water, Dutch Water Recycle Institute) — municipal/utility labs are a first-class audience, alongside environmental labs and regulatory agencies.
- **Six-step compliance workflow** (LabWare WATER): Plan → Collect → Test → Review → Report → Prove. Plan = sampling schedules (monthly/quarterly/annual/event-driven) in one place; Collect = sample locations, bottle types, preservatives, chain of custody, field instructions ready before crews leave; Test = sample tracking across in-house and contract labs; Review = flag exceedances, missing results, overdue samples, approaching reporting deadlines; Report = compliance reports generated from data already in the system; Prove = retrieve sampling history, results, CoC records, compliance documentation for inspectors.
- **Water LIMS**: sampling point registry with location-specific test/method/limit definitions ("the required tests, methods, QC, and limits travel with the location"); automated scheduling (routine/seasonal/event-driven); electronic CoC generated at the point of collection; field meter/sonde import with GPS + timestamp; real-time exceedance flagging against regulatory and internal limits; trend/control charting; unscheduled/complaint sample handling with full traceability.
- **Wastewater LIMS**: permit and outfall configuration with limits and averaging periods; influent/effluent/in-process monitoring; composite and grab sampling with flow-proportional support; automated BOD, solids, loading, removal-efficiency calculations; Discharge Monitoring Report (DMR) generation from approved results; industrial pretreatment and significant user tracking; biosolids/residuals testing and disposal records. Regulatory anchors named: Clean Water Act, NPDES, Biosolids 40 CFR 503.
- **Drinking water LIMS**: rule-driven monitoring schedules; coliform sampling with repeat/triggered source logic; disinfection by-product running annual averages; Lead and Copper Rule site tiering + 90th-percentile calculation; Consumer Confidence Report assembly from approved results; primacy-agency reporting formats + electronic submittal; deadline alerting. Anchors: SDWA, UCMR, EU Drinking Water Directive.
- **Environmental LIMS** (soil/air/waste): "The organizing unit is not the sample, it is the project" — project, site, and sample delivery group (SDG) structure; multi-matrix support (water, soil, sediment, air, waste); method-driven workflows with batch QC and control-limit evaluation; hold-time calculation from collection with prep and analysis tracking; TCLP and SPLP leachate handling; dry-weight-basis reporting; EDD generation in client and agency formats; contract-laboratory result import into the same project record. Anchors: RCRA, CERCLA, 40 CR methods, UK Environment Agency.
- **PFAS/UCMR**: analyte lists and reporting limits maintained per method; field/equipment/laboratory blanks tracked alongside associated samples; isotope dilution calculations and recovery acceptance criteria applied automatically; any detection in an associated blank flagged before results are released; trace-level significant-figure handling.
- **Lab operations surfaces**: sample login + CoC (pre-logged sampling runs, barcode label printing, single-scan receipt); field mobile capture (day's schedule download, GPS, field readings, real-time sync, iOS/Android); wet chemistry bench sheets/worklists by analyst and instrument with direct connections to balances, pH/DO meters, spectrophotometers, ion chromatographs; inorganics/metals (digestion/prep tracking, prep factors, autosampler worklist export, result import from ICP/ICP-MS/AA/GFAA); organics (purge-and-trap/extraction tracking, reagent lot/expiry, dilution/cleanup, bidirectional GC/GC-MS/LC-MS-MS interfaces); microbiology (TNTC, presence/absence, greater-than results, MPN calculation, membrane filtration with dilution accounting, coliform/HPC/Giardia/Cryptosporidium workflows); calculations (gravimetric, solids/moisture, Langelier Index, MPN, BOD); control charts, mean/SD, analyst comparison, automatic out-of-control flagging; multi-level review with electronic signature, configurable approval rules, complete audit trail (who/when/why), approved data locked and traceable; reporting (COA, operational reports, regulatory submittals, EDDs) from approved results; secure client portal.
- **Definitional framing in the vendor's own words** (high-value): "Water and environmental laboratories carry a burden most laboratories do not. The work is scheduled by regulation rather than by demand, hold times start ticking the moment a sample is collected rather than when it reaches the bench, and the output is not just a result but a defensible record that has to survive an audit years later."
- **Hold times** (FAQ): calculated from the collection timestamp (not receipt), per-method hold times, flags approaching/exceeding, prep/analysis steps timestamped, "Analysts can be prevented from entering results against a sample whose hold time has expired."
- **Accreditation** (FAQ): TNI/NELAC and ISO/IEC 17025:2017 require documented control over methods, personnel competency, instrument calibration, QC, data integrity, corrective action; the LIMS maintains these as part of daily operations (analyst certifications/training, instrument calibration/maintenance schedules, method definitions with control limits, QC batch acceptance criteria, audit trail, e-signature approval).
- **Integration**: instruments (uni/bidirectional across chromatography, spectroscopy, microbiology); SCADA/historian connections; utility compliance platforms (permit tracking, regulatory submittal); field instrumentation (sondes/field meters tied to sampling point + timestamp + collector); ERP (SAP, Oracle, Microsoft Dynamics) for billing/procurement/assets + accounting/invoicing; contract labs (structured EDD import validated against expected sample/method on arrival).
- **Commercial packaging**: LabWare WATER = pre-configured SaaS, "launch in under 30 days", aimed at small/mid municipal water utilities; enterprise platform for multi-site/multi-country scale. Badges: ISO/IEC 17025, NELAC/TNI, ELAP, GLP/GALP, 21 CFR Part 11.

## Product B — LabLynx (Environmental LIMS on the LabLynx LIMS Suite)

Evidence layer: A (directly observed), Tier-2.

Key observations:

- **Positioning**: "Environmental LIMS for Precision, Compliance, and Efficiency" — for labs testing "air, water, soil, and waste"; "meet EPA and ISO standards"; "defensible, audit-ready results"; high sample volumes.
- **Compliance & regulatory support**: automated compliance tracking (regulatory requirements tracked, audit-ready records); **chain of custody management** ("logging every sample movement from intake to final reporting"); customizable regulatory reporting templates aligned with environmental regulatory standards.
- **Sample management**: end-to-end sample tracking (collection to disposal, location, status, associated data); barcode labeling for intake/identification; real-time sample status.
- **Data & reporting**: centralized data repository for large environmental data sets; automated report generation meeting "both client and regulatory requirements"; data security.
- **Workflow**: automated task scheduling (assign/track tasks for sample processing); customizable workflows; real-time performance dashboards.
- **Platform context**: LIMS Suite / ELN Suite / Lab Automation Suite on one platform; solutions include Sample Tracking, Sample Analysis, QA/QC, Electronic Signatures, Audit Trails, Instrument Integration, Lab Portal (client/partner access), CRM, Accounting, Inventory, Instrument Management, Document Management; industry templates per vertical.
- FAQ defines Environmental LIMS as software "tailored to manage the specific needs of environmental testing labs… in air, water, soil, and waste testing."

## Product C — Autoscribe Informatics (Matrix Gemini LIMS Water & Environmental)

Evidence layer: A (directly observed), Tier-2, plus case study.

Key observations:

- **Positioning**: "Water and Environmental laboratories are responsible for testing water quality samples and reporting results to ensure compliance with local and national regulatory directives while maintaining tight quality standards and constantly reducing operating costs."
- **Sampling side** (distinctive depth): labs "typically collect samples from specific collection routes"; the system manages multiple sample zones with multiple sampling points, each requiring multiple bottles/containers specific to the testing required; scheduled sample collection "to ensure service level agreements are met"; collection rounds; bottle inventory; ad-hoc samples added as needed; web interface for remote sample collection, management, and reporting.
- **QC machinery** (distinctive depth): user-definable **runsheets** group multiple samples together with QC standards to test in a single run; QC standards include **spikes, duplicates, replicates, and controls**; daily work managed to allocate instruments and staff; **QC bracketing rules** let results be "automatically passed, or rejected, depending on the results of the QC samples being tested around the samples in the same run"; built-in QC charting monitors QC limits over time; **QC limits may be updated based on historic data** — "a common requirement within water/environmental laboratories."
- **Reporting**: Certificates of Analysis; pre-defined reports include sample turnaround time (TAT), test TAT, sample volumes and status, instrument and resource workloads — for monthly productivity/bottleneck reporting.
- **Matrices**: "water, wastewater, soil, air, gas or leachate samples."
- **Case study — Blue Ridge Analytical** (real environmental lab): family-owned environmental lab; VELAP (Virginia Environmental Laboratory Accreditation Program) accredited; offers sample collection, lab analysis, water/wastewater plant operations, consulting; previously spreadsheet-based records; adopted entry-level Matrix Express LIMS; results: shorter sample turnaround times, faster access to results. Testing capabilities listed: microbiological (coliform), general chemistry (BOD, COD, CBOD), metals (ICP, ICP-MS, GFAA), radiological methods, organics, TCLP, whole effluent toxicity; familiar with DEQ and VDH regulations/permits, pretreatment programs; nationwide subcontracted lab network.
- **Other case studies referenced**: The Water Lab (ISO 17025 environmental contract laboratory, Ireland — water and wastewater testing); WaterOne (large US drinking-water utility).
- **Vendor's generic LIMS definition** (root FAQ — useful for the LIMS boundary): LIMS "manage and track sample information through an analytical laboratory," with audit trails and e-signatures for standards such as 21 CFR Part 11, GxP, ISO 17025; instrument/ERP/EMR integration; staff competency, instrument maintenance/calibration, CAPA, inventory. Distinguishes LIS (patient-centric, clinical) from LIMS (batch/sample-centric); ELN (research experiments) from LIMS (defined tests against product/sample limits); SDMS (instrument files) as a LIMS subset; CDS as instrument software with LIMS interfaces.

---

## Cross-product Comparison

| Structure | LabWare (WATER / Env) | LabLynx (Environmental) | Autoscribe (Matrix Gemini W/E) |
|---|---|---|---|
| Environmental sample as unit of work | ✔ login, pre-logged runs, barcode, single-scan receipt | ✔ end-to-end tracking, barcode, real-time status | ✔ collection→testing management, collection rounds |
| Matrix anchoring (water/soil/air/waste…) | ✔ water, wastewater, soil, sediment, air, waste | ✔ air, water, soil, waste | ✔ water, wastewater, soil, air, gas, leachate |
| Location / sampling-point anchoring | ✔ sampling point registry; project/site/SDG | (general tracking) | ✔ sample zones, sampling points, routes |
| Requested tests / methods per sample | ✔ method-driven workflows | ✔ | ✔ tests assigned at collection |
| Chain of custody | ✔ electronic CoC at point of collection | ✔ CoC logging intake→reporting | (implied via collection management) |
| Analysis orchestration (worklists/batches) | ✔ bench sheets/worklists by analyst+instrument | ✔ task scheduling, customizable workflows | ✔ runsheets, daily work/instrument/staff allocation |
| Instrument integration | ✔ balances→ICP→GC-MS/LC-MS-MS, bidirectional | ✔ instrument integration solution | ✔ (charting; interfaces implied) |
| QC machinery | ✔ batch QC, control limits, spikes/duplicates, blanks, isotope dilution | ✔ QA/QC solution | ✔ spikes/duplicates/replicates/controls, QC bracketing auto pass/reject, QC charts, limits from history |
| Hold-time control | ✔ from collection, prep/analysis timestamps, entry blocking | — (not observed) | — (not observed) |
| Review / approval / audit trail | ✔ multi-level review, e-signature, audit trail, locked approved data | ✔ audit-ready records, e-signatures, audit trails | (implied) |
| Regulatory limit checking / exceedance flagging | ✔ real-time flagging; permit limits; DMR/CCR generation | ✔ regulatory reporting templates | ✔ (QC limits; compliance directives) |
| Deliverables | ✔ COA, regulatory submittals, EDD (client/agency formats) | ✔ automated client+regulatory reports | ✔ CoA, TAT/management reports |
| Client-facing surface | ✔ secure client portal | ✔ lab portal | ✔ web portal (remote collection/management/reporting) |
| Field collection integration | ✔ mobile, GPS, sondes | ✔ remote data collection solution | ✔ scheduled collection rounds, bottle inventory |
| Accreditation posture | ✔ ISO 17025, NELAC/TNI, ELAP, GLP/GALP, 21 CFR 11 | ✔ EPA/ISO alignment | ✔ ISO 17025 (case labs), VELAP |
| Commercial loop | ✔ ERP/accounting integration; client portal | ✔ CRM, accounting solutions | ✔ invoices (root FAQ); SLA-driven collection |
| Subcontracting | ✔ contract-lab EDD import into same project | — | ✔ subcontracted lab network (case study) |
| Scheduling by regulation | ✔ rule-driven monitoring calendars, deadline alerting | ✔ compliance tracking | ✔ SLA-driven collection scheduling |

Stable across all three: sample as unit of work with matrix + location anchoring; test/method assignment; analysis orchestration; QC evaluation; review/approval with audit posture; formal deliverables to client/regulator; client-facing portal; regulatory-compliance framing as the reason the lab exists.

Present in 2/3 or vendor-packaged differently: hold-time blocking (LabWare explicit), CoC as first-class object (LabWare, LabLynx), collection rounds/bottle inventory (Autoscribe, LabWare), subcontracted-result import (LabWare, Autoscribe case), CRM/accounting (LabLynx as solutions, LabWare via ERP integration, Autoscribe via invoices).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures. Remove any one and the product stops being an environmental laboratory management system:

1. **The environmental sample of record** — a persistent, individually identified record per physical sample: an environmental matrix (water, wastewater, soil, sediment, air, gas, waste/leachate…), tied to a collection point / location and to the submitting client or program, carrying the tests requested and the custody/accountability trail by which it entered the lab. Remove → a generic project/task tracker or a data platform with no laboratory subject.
2. **The managed analysis workflow** — the lab's production line: sample receipt/login → assignment of tests/methods → bench and instrument work orchestrated through worklists/batches/status → analyte results per sample and test. Remove → sample inventory or instrument-data tools with no laboratory operation being run.
3. **The validated deliverable** — results pass QC evaluation and review/approval into an audit-ready record, from which the lab's product is generated: formal client- and/or regulator-facing deliverables (analytical report / certificate of analysis / electronic data deliverable). Remove → raw data capture; the defensible result the lab exists to produce is gone.

Jointly-held is load-bearing:
- 1 alone = sample logbook / inventory
- 2 without 1 = instrument data processing (CDS-like)
- 3 without 1+2 = report generator
- 1+2 without 3 = sample tracker with raw results, no defensible product
- 1+3 without 2 = logbook plus report template, no operation
- 2+3 without 1 = anonymous data processing

What makes the Type *environmental* (rather than generic lab informatics) is carried inside L0 by: the sample's environmental anchoring (matrix + collection point/location) and the regulator-facing deliverable posture. The environmental-defensibility machinery below is L1 — universal in the market, but each item individually removable without collapsing the Type.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- **Chain of custody** as a first-class tracked object (electronic CoC from the point of collection; every movement logged)
- **Sampling-point / location registry** with location-specific tests, methods, and limits
- **Program-driven sampling schedules** (routine/seasonal/event-driven), collection rounds, bottle/container inventory, preservation tracking
- **Hold-time control** from the collection timestamp, with prep/analysis timestamps and (in some products) entry blocking on expiry
- **QC machinery**: batch/runsheet QC (method blanks, field/equipment blanks, spikes, duplicates, replicates, controls), QC bracketing with automatic pass/reject, control charts, QC limits maintained/updated from historic data
- **Regulatory limit checking / exceedance flagging** at result entry, against regulatory and internal limits
- **Instrument integration** (balances, pH/DO meters, spectrophotometers, ICP/AA metals, GC/GC-MS/LC-MS chromatography — uni- and bidirectional) and **field-instrument import** (sondes/meters with GPS + timestamp)
- **Barcode labeling** and scan-based receipt
- **Multi-level review with electronic signatures, complete audit trail, locked approved results**
- **Turnaround-time (TAT) tracking** and lab productivity reporting (workloads, bottlenecks)
- **Client portal** (status, results, deliverables)
- **Accreditation support**: method definitions with control limits, analyst competency/training records, instrument calibration/maintenance records maintained as part of daily operations (ISO 17025 / TNI-class posture)
- **Environmental calculations**: BOD/COD-class, solids/moisture, loading, MPN, dry-weight basis, leachate (TCLP/SPLP-class)
- **Subcontracting**: sending work out and importing contract-lab results into the same record
- **Commercial loop**: quotes/price lists, billing/invoicing (in-product or via ERP/accounting integration)

### L2 — Variant / Optional Structure

- **Lab type**: commercial contract labs (client-driven, SLA/TAT, billing) vs municipal/utility in-house labs (program-driven, permit compliance) vs government/regulatory agency labs
- **Program focus**: drinking water (rule-driven schedules, compliance reporting to primacy agencies), wastewater/discharge (permit/outfall structure, DMR-class reporting), site & waste testing (project/site/SDG structure, leachate, dry weight), emerging contaminants (trace-level blanks discipline)
- **Regulatory regime**: US (TNI/NELAP/ELAP accreditation, state/agency EDD formats, NPDES/SDWA/RCRA/CERCLA programs) vs EU/international (ISO 17025, national directives) vs other regional regimes — regime machinery is packaging, not core
- **Deployment**: SaaS (pre-configured, fast launch) vs cloud-hosted vs self-hosted/on-prem; single small lab vs multi-site enterprise
- **Field-collection integration depth**: mobile apps with GPS/sync vs web portals for remote collection vs none (samples walk in)
- **Suite breadth**: LIMS-only vs LIMS+ELN+SDMS+LES platforms; CRM/accounting/inventory as in-product solutions vs integrations

### L3 — Vendor-specific (kept out of the final document)

- LabWare: "LabWare WATER" brand, six-step Plan→Collect→Test→Review→Report→Prove packaging, "launch in under 30 days", named utility customers, SaaS tier structure
- LabLynx: LIMS/ELN/Automation Suite packaging, limsforum community, solutions catalog naming
- Autoscribe: Matrix Gemini / Matrix Express product split, concurrent-user licensing model, configuration-tools positioning, named case-study labs

## Vendor-specific Findings

See L3 above. Additionally: LabWare's FAQ makes specific operational claims (hold-time entry blocking, DMR/CCR generation, LCR 90th-percentile calculation, isotope-dilution automation) — these are product capabilities, not Type invariants; kept out of the final document except as attributed examples where useful.

## Rejected Findings

- "Environmental LIMS = water-utility compliance software" — rejected: the sampled population includes contract labs and site/project testing; water utilities are one customer tier, not the definition.
- "MODA-EM-style 'environmental monitoring'" (STARLIMS resource page) — rejected as a match: that is pharma QC *microbiology* environmental monitoring (cleanroom), a different domain; not used as evidence for this Type.
- "LabVantage has no environmental offering" — not asserted: its environmental work likely sits under Government/Public Health pages; simply not sampled.
- "EDD formats have a standard list" — rejected: only "client and agency formats" is directly evidenced; specific format names not asserted.
- "Billing is always in-product" — rejected: realized variously as in-product solutions (LabLynx), ERP integration (LabWare), invoices (Autoscribe FAQ); kept general.

## Boundary Findings

- **vs LIMS (§22, unprocessed) — the closest sibling.** The generic LIMS core (sample tracking through an analytical laboratory, audit trails/e-signatures, instrument integration, competency/calibration/CAPA records — per Autoscribe's own FAQ) is the shared substrate. This leaf is the **environmental-domain instance**: the sample is environmentally anchored (matrix + collection point), work is scheduled by regulation, results must survive regulatory audit, and the deliverable is regulator-facing (EDD/permit reports). Proposed seam for the LIMS pass: generic LIMS = the lab-informatics core; environmental laboratory management = that core + the environmental-defensibility layer as the center of gravity. If the directory prefers one LIMS Type with industry variants, this leaf becomes a variant — joint review recommended when laboratory-information-management-system-lims is processed (consistent with the ELN pass's standing joint-review flag vs both LIMS leaves).
- **vs Environmental Data Platform (§21 sibling, unprocessed) — producer vs consumer.** The lab system *produces* validated results and EDD deliverables; environmental data platforms (the ESdat/EQuIS/Locus EIM class documented in the contaminated-site pass) *ingest* those deliverables into the data consumer's environmental record. The EDD is the seam artifact. Remove the lab workflow → data platform; remove the data corpus → lab system. Cross-reference recommended when environmental-data-platform is processed.
- **vs Environmental Monitoring Platform / CEMS (§21)** — field/continuous instrumental monitoring vs laboratory analysis of physical samples. Lab results may enter monitoring/compliance systems as evidence; the lab system holds the lab's production record, not the monitoring network.
- **vs Chromatography Data System (§22, processed)** — CDS acquires/processes chromatographic instrument data; the lab system manages the whole lab workflow and receives results from CDS/instruments via interfaces. Consistent with the CDS pass's recorded boundary vs LIMS.
- **vs Environmental Compliance Management (§21, processed)** — the lab serves compliance (its clients' compliance depends on its results) but holds the lab's production record, not the operator's obligation register + conformance loop. Lab results feed compliance evidence; the two Types sit on opposite sides of the evidence flow.
- **vs Water Quality Management (§19, unprocessed)** — utility-side water-quality program vs the laboratory that analyzes the samples; producer/consumer seam again.
- **vs LIS (clinical)** — patient-centric clinical diagnostics vs sample/environment-centric testing; the vendor's own FAQ draws this line (LIS: HIPAA/patient; LIMS: ISO 17025/sample).
- **vs ELN (§22/§23, processed)** — experiment record as spine vs sample/specimen workflow as spine; consistent with the ELN pass's documentation-vs-operations seam.
- **"Remove what to become another Type?"** — remove the environmental matrix/location anchoring and regulator-facing deliverable → generic LIMS; remove the lab workflow (keep the data) → Environmental Data Platform; remove the laboratory (keep field/continuous measurement) → Environmental Monitoring; remove the lab and keep the obligation register → Environmental Compliance Management.

## Historical / Market-Sample Check (per §24)

- **Paper-era environmental lab**: sample log-in book with custody signatures, bench worksheets, QC notebooks (blank/duplicate/spike records), instrument logbooks, hand-typed client reports, state reporting forms — satisfies all three L0 structures (sample of record, managed analysis workflow, validated deliverable). No cloud, barcodes, AI, or EDD in the core. **Passes.**
- **Pre-software fragmented state** (LabWare's own framing): "spreadsheets, paper chain-of-custody forms, emailed lab reports, and personal calendar reminders" — the Type's core is the *connected* record, not any modern mechanism.
- **Older/regional labs**: a European ISO 17025 water lab (The Water Lab case) and a US state-accredited small lab (VELAP) both fit the core without US-specific machinery (TNI/NELAP/EDD are regime variants). **Passes.**
- Modern mechanisms deliberately NOT definitional: barcodes, mobile/GPS field capture, client portals, EDD automation, dashboards, AI.

## Uncertainties

- No Tier-1 help-center documentation was reachable for any sampled product; all evidence is Tier-2 official pages + one case study. Assertion strength in the final document is calibrated accordingly (no numeric limits, no exact state/field lists, no default values).
- The independent purpose-built environmental LIMS pole (Promium class) is under-sampled (unreachable ×2). If that pole has a materially different center (e.g., deeper EDD/agency-format machinery), the L1 list may under-represent it; the L0 is unlikely to change.
- STARLIMS's environmental solution could not be examined (403 ×2); no claims made.
- Whether hold-time entry blocking is industry-universal or product-specific is unconfirmed (directly evidenced in one product) — final document says "some products prevent…" rather than asserting universality.
- Exact QC-bracketing semantics (auto pass/reject) directly evidenced in one product; framed as a common pattern with attribution-level care.
- The commercial loop (quotes/billing) is evidenced at low depth; kept general.

## Final Synthesis

Environmental Laboratory Management is the environmental testing laboratory's system of record — in market vocabulary, the environmental LIMS. Its defining core is three jointly-held structures: the environmental sample of record (matrix + collection point + submitting client/program + requested tests + custody), the managed analysis workflow (login → test assignment → bench/instrument work → analyte results), and the validated deliverable (QC-evaluated, reviewed/approved, audit-ready results rendered as client/regulator-facing reports). Around that core, mature products add the environmental-defensibility layer — chain of custody, hold times, program-driven sampling schedules, sampling-point registries, batch QC with bracketing, regulatory limit checking, instrument/field integration, client portals, accreditation records — and vary by lab type (contract / utility / government), program (drinking water / wastewater / site & waste / emerging contaminants), regime (US TNI-class / ISO 17025 / other), and deployment. The Type sits between the generic LIMS core (its substrate) and the environmental data platforms that consume its deliverables; the EDD/report is the seam artifact in both directions.
