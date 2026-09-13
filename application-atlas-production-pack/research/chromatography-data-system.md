# Research Notes — Chromatography Data System

Research date: 2026-09-06

## Research Goal

Understand what a Chromatography Data System (CDS) actually is as an Application Type: its core objects, its defining workflow (from instrument signal to reported result), its compliance machinery, its deployment shapes, and its boundaries against LIMS, ELN, instrument firmware, and generic data-acquisition software.

## Initial Boundary

Hypothesis entering research:

- CDS = lab software that acquires detector signals from chromatography instruments (HPLC, GC, IC, CE, and hyphenated MS), controls instrument runs, processes raw signals into integrated/identified/quantified peak results, and manages those results as auditable records.
- Nearest neighbors: LIMS (sample-centric lab logistics), ELN (experiment documentation), instrument firmware/HMI (on-device control), SCADA/industrial historian (general process signals), Scientific Data Management System (cross-instrument archiving).
- Dominant market context: pharmaceutical QC labs (GMP / 21 CFR Part 11 / EU Annex 11), but also food, environmental, petrochemical, and academic labs.

## Research Questions

1. What are the core objects? (instrument, method, sequence, injection, channel/signal, chromatogram, peak table, calibration, result, report, audit trail)
2. What is the defining workflow from sample to reported result?
3. Is instrument control definitional, or a common but separable capability?
4. How do calibration and quantitation work (ISTD/ESTD, response curves, recalibration)?
5. What compliance machinery exists (user accounts, audit trail, e-signatures, validation support)?
6. What interfaces do users actually work in?
7. How do deployment shapes vary (single workstation → network → client/server enterprise)?
8. Where exactly are the boundaries vs LIMS / ELN / firmware / generic DAQ?
9. Historical check: would older / simpler products (computing integrators, chart recorders, freeware CDS) still fit the definition?

## Representative Products

| Product | Vendor | Why selected | Documentation reached |
|---|---|---|---|
| Chromeleon CDS | Thermo Fisher Scientific | enterprise-leader pole; multi-vendor instrument control; MS support; tiered deployment | Yes — 3 official pages (category, order, workstation) |
| Clarity | DataApex | independent, hardware-agnostic, mid-range/perpetual-license pole; smaller/academic labs | Yes — 4 official surfaces (product page, regulated-environment page, glossary, online help "Getting Started") |
| Empower | Waters | market anchor in pharma QC | No — waters.com 403 ×2 (abandoned) |
| OpenLab CDS | Agilent | market anchor, Agilent-instrument-centric | No — agilent.com 403, help.agilent.com transport error (abandoned) |

Waters and Agilent are retained as market anchors because DataApex's own product documentation explicitly positions both ("complex solutions with a wide scope of features and scalable design, such as OpenLAB, … Chromeleon, … or Empower are quite expensive"), but no product-specific operational claims are made for them in this pass.

## Sources

- DataApex — Clarity Chromatography Software product page — https://www.dataapex.com/clarity — 2026-09-06 (Layer A)
- DataApex — Clarity in a regulated environment — https://www.dataapex.com/clarity-in-regulated-environment — 2026-09-06 (Layer A)
- DataApex — Clarity and related chromatography key terms (glossary) — https://www.dataapex.com/document/chromatography-terms — 2026-09-06 (Layer A)
- DataApex — Clarity Guides & Documentation, "Getting to know Clarity" — https://www.dataapex.com/documentation/Content/getting-started/010-getting-started/010.000-getting-started/010-getting-to-know.htm — 2026-09-06 (Layer A)
- Thermo Fisher — Chromatography Data System / Chromeleon CDS category page — https://www.thermofisher.com/uk/en/home/industrial/chromatography/chromatography-data-systems-cds.html — 2026-09-06 (Layer A, marketing-tier)
- Thermo Fisher — Chromeleon CDS order/catalog page (CN mirror) — https://www.thermofisher.com/order/catalog/product/CHROMELEON7 — 2026-09-06 (Layer A, marketing-tier)
- Thermo Fisher — CDS Software — Workstation page (CN mirror) — https://www.thermofisher.com/uk/en/home/industrial/chromatography/chromatography-data-systems-cds/workstation-cds-software.html — 2026-09-06 (Layer A, marketing-tier)

Access limitations:

- waters.com returned 403 on both attempt shapes → abandoned; no Empower-specific claims.
- agilent.com 403 + help.agilent.com transport error → abandoned; no OpenLab-specific claims.
- Shimadzu LabSolutions pages 404 ×2 → abandoned; no bundled-suite product claims from Shimadzu.
- Thermo Chromeleon overview brochure PDF exceeded fetch size limit → abandoned; Chromeleon detail rests on 3 HTML pages only.
- Thermo pages fetched were marketing/product surfaces, not deep help-center articles: instrument-level operational claims (exact defaults, numeric limits) are NOT asserted for Chromeleon.

## Product Observations

### Product A — DataApex Clarity (independent, mid-range, hardware-agnostic)

Key observations (evidence layer A = directly observed on official pages):

**Positioning.** "Chromatography software for data acquisition, processing, and instrument control in regulated environment." Positioned explicitly against both small tools (PeakSimple, ChromPerfect, Chrom&Spec, Borwin, Azur, Multichro, Chrom-Card) and "complex solutions with a wide scope of features and scalable design" (OpenLAB, EZChrom, ChemStation, Chromeleon, TotalChrom, GCSolution, LCSolutions, Galaxie, Atlas, Class-VP, Chromquest, Empower) — Clarity presents itself as a "scalable medium-ranged solution."

**Object vocabulary (from vendor glossary, direct):**
- **Instrument** = "an independent chromatograph configuration with its own time base"; core software includes one, up to four configurable.
- **Channel** = "an individual data collection path from individual detectors"; each channel processed/visualized independently; multi-channel from a single run.
- **Signal** = "the output data from a detector during chromatographic analysis, representing the response of an analyte over time."
- **Device** = individual component (detector, pump, autosampler) within the analytical process.
- **Control module** (a.k.a. driver) = optional software module enabling control of autosamplers, GC, GC-MS, HPLC/CE, HPLC-MS systems; "software components that manage specific tasks by processing inputs and issuing commands between Clarity and connected chromatography devices."
- **Extension** = optional capability for specific techniques/calculations: PDA, MS, GPC, NGA (natural gas analysis), DHA (detailed hydrocarbon analysis), CE, EA (elemental analysis), SST (system suitability test).
- Chromatography-physics terms also defined: retention time, eluent, mobile phase, stationary phase, peak overlap, peak broadening, PDA/DAD, ISTD/ESTD, overlay, deconvolution (not supported by Clarity).
- Quantitation methods: **ISTD** (internal standard added to each sample) and **ESTD** (external calibration standards).

**Feature set (direct):**
- Measurement: simultaneous acquisition from up to four independent chromatographs, each up to 32 detectors ("4×32 signal configuration").
- Integration: "two advanced integration algorithms", extensive customization of peak detection; "fine-tuned integration parameters can be easily applied to other chromatograms"; interactive graphic baseline modification.
- Overlay: display of a "virtually unlimited number of chromatograms" plus mathematical modification (deduction, derivation).
- Calibration: internal and external standard methods, calibration of groups of peaks, reference peaks.
- Automated measuring: **Sequence tables** for any set of samples with or without autosampler; fill-down editing; per-row status symbols.
- Post-run options: automatically display/print/export/start other programs after measurement.
- Summary result tables across displayed chromatograms; custom user columns/calculations.
- Column performance: symmetry, efficiency, resolution "by several methods (tangent, moments, etc.)".
- Batch processing of any number of chromatograms.
- Method and calibration history: "Each chromatogram can easily be displayed under the same conditions as when it was printed, exported, or saved."
- LIMS connectivity: "both for sample submission and result output … via convenient ASCII transfers" (import/export, customizable formats).
- Export/import of chromatograms in text/AIA formats.
- Instrument method that controls the device is **saved in the measured chromatograms**.

**Compliance machinery (direct, from regulated-environment page):**
- "Fully validatable, FDA 21 CFR Part 11 and EU Annex 11 compliant"; developed under ISO 9001.
- ALCOA data-integrity principles; customizable user accounts and "rigorous audit trail".
- User accounts with access rights, passwords, password policy (minimum length, validity).
- Audit trail "records selected events and operations into a special file. Records selected operations directly into a chromatogram."
- Electronic signature: "Each chromatogram can be signed electronically. Signature selection is based on the username or the signature certificate."
- Validation support: inbuilt IQ/OQ features, PQ assistance, Validation Kit, Declaration of Software Validation per GAMP5.
- Network solution: "not a strict client–server system" but multi-station network configurations; **Clarity Offline** for data evaluation/processing/method preparation without acquisition.
- Target segments: pharma/biotech QC-QA, CROs, academic and government labs, development and manufacturing control labs. "Operational responsibility remains with the user organization."

**Windows (from screenshots/annotations, direct):**
- Clarity window (entrance to instruments), Instrument window ("control center of the whole process of data acquisition and evaluation" — sample info table with applied template method, acquisition mode; status line with elapsed time and state; analysis-processing diagram icons), Chromatogram window (chromatogram + results; edit via graph or Integration table; Result/Summary/Column Performance tabs), Device Monitor (control instrument parameters during analysis), Event table (digital I/O control, start synchronization, fraction collector control), Sequence table.

**Editions:** Clarity (full), Clarity Lite (simplified, one chromatograph via analog output, "suitable for non-regulated environments"), Clarity Offline (evaluation only), Demo/Trial (simulated acquisition).

### Product B — Thermo Scientific Chromeleon CDS (enterprise leader, instrument-vendor)

Key observations (evidence layer A on marketing-tier pages; operational depth NOT reached):

**Positioning.** "Chromatography Data System (CDS)" supporting chromatography (LC, GC, IC), third-party capillary electrophoresis, and Thermo Scientific single/triple-quadrupole and HRAM mass spectrometers — "complete GMP compliance support", "connects people, instruments and enterprise data management."

**Scale and deployment tiers (direct):**
- Single **Workstation** → **Workstation Connect** (multiple workstations as a small network without a separate server; remote instrument control and data processing) → **Enterprise** (multi-site, central data server, cloud-capable; "manage more than 500 chromatography instruments (including third-party CE)" per system, >1000 instruments/users/workstations in enterprise tier).
- Enterprise: "version-controlled data storage in a relational database" for raw metadata and results; "hundreds of configurable permissions"; role-level security "to meet GMP and 21 CFR Part 11"; centralized management; 247 Instrument Controller hardware appliance.

**Lab-facing capabilities (direct):**
- Instrument control of "more than 500 chromatography instruments from more than 25 manufacturers" plus Thermo MS — single-software multi-vendor control is a headline claim.
- **eWorkflow procedures** — "create sequences quickly and accurately, avoiding errors."
- **Intelligent Run Control** and automated **System Suitability Testing (SST)** (dedicated technical note exists).
- Pre-acquisition **sequence review/approval step** to reduce out-of-specification (OOS) results.
- Customizable UI; spreadsheet-based custom reporting engine / integrated report designer.
- Outlier flagging by custom conditions: "calibration failures, out-of-specification QC samples, and any sample or compound producing a positive result"; result sorting/filtering.
- Manual re-integration with visualized "before/after" comparison.
- **Centralized audit trail** review; comparing changes across results, methods, or the system; "sequence-based electronic signature workflows."
- MS workflows: peptide analysis / MAM, cross-technique confirmation (GC-MS vs LC-MS), background processing, pesticide-analysis report templates.
- SmartStatus instrument monitoring (maintenance/consumables decisions).
- **Chromeleon XPS open access software** (walk-up open-access mode exists as a separate SKU).
- Integration with other informatics: "LIMS, LES or ELN" (SampleManager named as companion).

**Market applications (direct):** pharmaceutical, biopharma (R&D→QC), petrochemical, environmental, food & beverage.

### Product C — Waters Empower (market anchor only)

No official page reachable (403 ×2). From third-party documentation (DataApex's own list): a "complex solution with a wide scope of features and scalable design", positioned in the same enterprise class as Chromeleon/OpenLAB. **No product-specific operational claims made.**

### Product D — Agilent OpenLab CDS (market anchor only)

No official page reachable (403 + transport error). Same third-party positioning as above. **No product-specific operational claims made.**

## Cross-product Comparison

| Dimension | Clarity (DataApex) | Chromeleon (Thermo) | Cross-product reading |
|---|---|---|---|
| Self-description | "data acquisition, processing, and instrument control in regulated environment" | "Chromatography Data System" with acquisition, control, analysis, compliance | The CDS label is used by both poles; acquisition + processing + control is the shared triad (A) |
| Raw data unit | Signal/Channel per detector; chromatogram persists; re-displayable "under the same conditions as when saved" | version-controlled raw metadata + results in relational DB | Raw signal is a persistent, reprocessable record, not a printout (A×2) |
| Integration | two algorithms; global parameters + interactive graphic baseline; Integration table | processing of chromatograms; manual re-integration with before/after comparison | Peak integration w/ editable events is universal (A×2) |
| Calibration | ISTD/ESTD, peak groups, reference peaks | calibration-failure flagging; IC auto calibration-curve selection (tech note) | Calibration→quantitation loop is universal (A×2) |
| Sequence | Sequence table, fill-down, per-row status, with/without autosampler | eWorkflow-driven sequence creation; pre-acquisition sequence approval | Sequence as batch container is common in mature products; approval step is regulated-segment depth (A on both, depth differs) |
| Instrument control | optional control modules ("over 1000 instruments"), incl. Agilent ICF | headline: 500+ instruments / 25+ manufacturers + Thermo MS | Control is a competitive differentiator (breadth varies), NOT definitional — Clarity Lite/Offline/older integrators work without it (A×2) |
| Compliance | user accounts, audit trail (file + per-chromatogram), e-sig (username or certificate), IQ/OQ/PQ, GAMP5 declaration, Part 11/Annex 11 | role-level security w/ hundreds of permissions, centralized audit trail review, e-sig workflows, GMP/Part 11 | Compliance machinery common in the regulated market; absent in non-regulated edition (Clarity Lite) → variant depth, not core (A×2) |
| SST | optional Extension | built-in automated SST | QC-context commonality; implementation depth varies (A×2) |
| LIMS relationship | explicit import/export of sample lists and results (ASCII/customizable) | "integrate other informatics solutions: LIMS, LES or ELN" | CDS connects to LIMS but is not the sample-logistics system (A×2) |
| Deployment | single station w/ HW key; "not a strict client–server" network; Offline companion | Workstation → Connect → Enterprise (central server, multi-site, cloud) | Deployment is a spectrum, not a Type boundary (A×2) |
| Segment tunings | NGA/DHA/EA/GPC extensions for petrochemical/spec techniques | pharma/biopharma/petro/environmental/food pages; MS/MAM workflows | Technique- and segment-specific modules are variant-layer (A×2) |
| Review workflow | per-chromatogram e-signature; audit trail | sequence approval, outlier flagging, audit-trail comparison | Human review gate over results is common in regulated contexts (A×2, depth varies) |

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

A Chromatography Data System exists when all of the following hold:

1. **Persistent raw chromatographic signal** — the detector response over time (a chromatogram/channel) is captured or imported as a stored, reprocessable data record, bound to an identifiable measurement of a named sample.
2. **Peak integration** — the software detects peaks in the signal against a baseline and produces peak descriptors (retention time, area/height).
3. **Calibration-based quantitation** — peak responses are converted into amounts/concentrations via standards calibration (response factors/curves; internal- or external-standard logic).
4. **Method as stored parametric recipe** — a named set of processing (and where applicable acquisition) parameters governs how raw data becomes results, and can be re-applied to stored data (reprocessing).
5. **Results as records** — quantified results are stored per sample measurement and can be reviewed and rendered as a report.

Test — remove one element:
- Remove persistent reprocessable raw data → chart recorder / paper output, not a CDS.
- Remove integration/calibration → a signal viewer or generic DAQ tool.
- Remove the method concept → one-off ad-hoc analysis, not a manageable data system (every product organizes work as methods applied to measurements).
- Remove sample-bound results → an oscilloscope.

### L1 — Common Mature Structure

Very common in mature modern products; expected by the market; not definitional:

- Instrument control via driver/control modules: start/stop runs, set device parameters, live monitoring, queues; direct digital control of whole instrument families.
- Sequence table as the batch container (samples, standards, blanks, QC; per-row status; automation via autosamplers).
- Real-time acquisition display (live signal plot, elapsed time, run state).
- Multi-signal/multi-channel acquisition; multi-detector and spectral (PDA/DAD 3D, MS) data.
- Chromatogram overlay and comparison; mathematical manipulation.
- Integration event tables; manual re-integration with audit-visible before/after.
- Calibration tables/curves from standard injections; recalibration; reference peaks.
- Column-performance calculations (symmetry, efficiency/plates, resolution).
- Result/summary tables with customizable columns and user calculations.
- Report designer/templates; export (text, AIA-format, clipboard) and post-run automation (auto print/export/launch).
- LIMS connectivity (import sample lists / export results).
- User accounts, access rights, audit trail, electronic signatures — the regulated-lab posture.
- Batch processing; method/calibration history; offline or client-side processing companion.

### L2 — Variant / Optional Structure

- **Deployment shape**: single workstation with hardware license key → peer network of workstations → strict client/server enterprise with central relational database, multi-site, cloud posture.
- **Regulatory depth**: non-regulated editions (analog-acquisition "Lite" products) vs fully validated GMP stacks (Part 11/Annex 11 support, ALCOA, IQ/OQ/PQ kits, GAMP5 validation declarations, sequence approval, audit-trail review tools, permission granularity in the hundreds).
- **Technique scope**: LC / GC / IC / CE base; extensions or built-ins for GPC/SEC, PDA spectral, MS (incl. HRAM/MAM workflows), and norm-based petrochemical calculations (natural gas, detailed hydrocarbons, elemental analysis).
- **Product philosophy**: independent hardware-agnostic CDS (control modules for many manufacturers, perpetual licenses) vs instrument-vendor CDS (deep control of own instruments, enterprise suites, MS integration).
- **Open-access/walk-up mode** for shared instrument rooms.
- **Bundling posture**: standalone CDS vs CDS embedded in vendor lab-informatics suites (CDS + LIMS/LES/ELN integration layers; some instrument vendors ship CDS-like software bundled with the instrument).

### L3 — Vendor-specific (research notes only)

- Chromeleon: eWorkflow procedures, Intelligent Run Control (IRC), SmartStatus, Chromeleon XPS open access, 247 Instrument Controller appliance, ">180 system permissions" marketing figure, ChromSword Chromeleon Connect (automated method development), AppsLab, 500+/1000+ instrument scale claims.
- Clarity: Colibrick A/D converter hardware, HW key/dongle + User Code licensing, Instrument = time-base unit (1–4 per station), 4×32 signal configuration, Postrun module, Event table (digital I/O, start synchronization, fraction collectors), .cfg/.dsk file concepts, named extensions (PDA, MS, GPC, NGA, DHA, CE, EA, SST), Clarity2Go mobile monitoring, Demo/Trial modes, localization set.

## Rejected Findings

- "CDS = instrument control software." Rejected: control is optional (Clarity control modules are add-ons; Clarity Lite/Offline lack it; historical integrators had none). Control breadth is a differentiator, not a defining property.
- "CDS = 21 CFR Part 11 compliance software." Rejected as definitional: non-regulated editions and academic/food/environmental usage exist; compliance depth is variant-layer, though dominant in the pharma QC segment.
- "Sequence table is definitional." Rejected: single manual measurements are valid CDS work (products support "with or without an autosampler"; historical integrators processed single runs). Sequence is the common batch container, not the core.
- "CDS includes statistics/SPC or trend analysis as core." Not observed as a shared core element in the documented sample; SST exists but is QC-context (L1). Not promoted.
- "MS data processing is core." Rejected: hyphenated-MS support is a variant extension (both products treat MS as extension/built-in module territory); base CDS semantics are detector-signal chromatography.

## Boundary Findings

- **vs LIMS** (sharpest boundary): LIMS is sample-centric — samples, chain of custody, lab workflows, result aggregation across techniques. CDS is instrument/data-centric — the unit of work is the injection/measurement and its signal. Both documented products explicitly *connect* to LIMS by exchanging sample lists (in) and results (out) rather than absorbing the function. Test: remove detector-signal acquisition and peak integration/quantitation → LIMS; remove sample logistics → CDS. Suites that bundle both exist (instrument vendors ship informatics suites); the bundle does not merge the Types.
- **vs ELN**: ELN holds narrative experiment documentation and protocols as written records; CDS holds instrument signals and computed results. They integrate (Chromeleon lists ELN among integration targets) but neither replaces the other's center of gravity.
- **vs instrument firmware / HMI**: an instrument's on-device interface runs and monitors the hardware. What makes the CDS a separate Type is the data side: persistent reprocessable raw data, method-driven reprocessing, calibration, result records, audit trail. Modern firmware with built-in integration blurs the edge but does not carry the result/audit system of record (boundary nuance — noted from product structure, not a direct doc quote).
- **vs SCADA / industrial historian / generic DAQ**: those acquire arbitrary process signals generically. The CDS is defined by chromatography semantics: retention time, peak integration algorithms, standards/calibration levels, column performance, suitability. A generic DAQ tool cannot quantify a sample.
- **vs Scientific Data Management System / SDMS**: SDMS archives files/data across instruments generically; the CDS processes a specific data species into scientific results.
- **"Remove what to become another Type" tests**: remove chromatography-specific processing semantics → generic DAQ/historian; remove the instrument/data center and keep samples → LIMS; remove persistence/reprocessing → integrator printout or firmware HMI.

## Historical / Market-Sample Check

- **Computing integrators** (stand-alone box instruments of the pre-PC era) performed acquisition → integration → calibration → printed report, with no instrument control, no sequences, no audit trail. They satisfy L0 elements 1–5 → definition holds for the historical form.
- **Paper chart recorders** perform only signal display → fail L0 → correctly excluded.
- **Non-regulated editions** (e.g., a "Lite" analog-acquisition product "suitable for non-regulated environments") satisfy L0 without audit/e-sig machinery → compliance is not definitional.
- **Small freeware-class CDS** (acquisition + integration + calibration only) satisfy L0 → definition does not over-fit the enterprise tier.
- Conclusion: the minimal core survives the historical and market-structure check; instrument control, sequences, compliance machinery, and enterprise deployment all sit above the core.

## Uncertainties

- Empower and OpenLab CDS internal structures were not verified against official documentation (blocked); their inclusion as representative products rests on market position plus third-party vendor positioning. Risk: low for the canonical model (two fully different poles already agree), but any Empower/OpenLab-specific claim would be unsupported and was therefore omitted.
- Chromeleon claims rest on marketing-tier pages only; features named there (eWorkflow, IRC, approval step, permissions) are treated as existence claims, not operational descriptions (no defaults, no numeric limits used).
- Whether modern instrument firmware provides CDS-grade audit trails in some ecosystems was not researched; the firmware boundary is stated structurally, not as a market survey.
- Exact mechanics of calibration mathematics (e.g., weighting models) not researched; kept generic (response curves, ISTD/ESTD).
- Bundled suite products (e.g., Shimadzu LabSolutions) unreachable; the "bundled suite" variant is inferred from Chromeleon's suite integration language and instrument-vendor bundling common knowledge — marked as inference, not observation.

## Final Synthesis

A Chromatography Data System is the laboratory's instrument-data system of record for chromatography: it captures detector signals as persistent reprocessable raw data bound to named sample measurements, applies stored methods to integrate peaks, calibrate responses against standards, and quantify analytes, and manages the results as reviewable, reportable, and (in regulated contexts) attributable and auditable records. Instrument control, sequences, compliance machinery, enterprise deployment, and technique extensions are the standard capability layers that mature products add above this core; none of them is required to recognize the Type.
