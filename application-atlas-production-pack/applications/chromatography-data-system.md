# Chromatography Data System

## Overview

A **Chromatography Data System (CDS)** is laboratory software that acquires detector signals from chromatography instruments (HPLC, GC, IC, CE, and hyphenated MS systems), turns those raw signals into identified and quantified peak results through integration and calibration against standards, and manages the results as persistent, reviewable records bound to named samples.

The defining structure is small:

```text
Sample measurement (injection)
└── Raw chromatographic signal — detector response over time, stored as reprocessable data
    └── Peak integration — peaks detected against a baseline (retention time, area, height)
        └── Calibration & quantitation — peak response converted to amount via standards
            └── Result record — stored per sample, reviewable and reportable
```

A stored **method** — the parametric recipe governing acquisition and processing — sits over this chain and can be re-applied to stored data at any time.

Everything else commonly associated with the category — direct instrument control, sequence automation, audit trails and electronic signatures, enterprise client/server deployment, system suitability testing, LIMS integration — is standard capability in mature products but is not what makes the software a CDS. Simpler and older forms of the Type (stand-alone computing integrators, non-regulated single-workstation packages) satisfy the core without any of them.

The CDS is not the laboratory's sample logistics system (that is a LIMS), not the experimenter's narrative documentation (an ELN), and not the instrument's own on-device control panel, although it commonly connects to all three.

## Users & Context

Primary users:

- **Analyst / lab technician** — prepares the run, builds the sequence of injections, starts the acquisition, monitors the instrument, and processes the resulting data into quantified results.
- **Method developer** — designs and refines methods (separation parameters, integration rules, calibration levels) and validates that results are reproducible.

Secondary users:

- **Reviewer / supervisor / QA** — checks results, approves or rejects them, and in regulated laboratories signs them electronically; in pharmaceutical quality control this review is a formal step before a result is reportable.
- **System administrator** — manages users, permissions, instrument connections, and the audit trail.

Typical contexts: pharmaceutical and biopharmaceutical QC laboratories are the dominant market (where GMP data-integrity expectations shape daily use), followed by food, environmental, petrochemical, contract-lab, and academic settings. The work is organized around instruments and instrument time: samples arrive as physical vials, the instrument runs an ordered series of injections, and the CDS is the software surface through which the analyst runs, watches, and then works up each run.

## Core Model

### The Defining Core

- **Raw chromatographic signal.** The detector's response over time — the chromatogram, possibly several parallel channels from multiple detectors — is captured (or imported from another system) and stored as a reprocessable data record. The stored signal is the foundation: everything downstream is computation applied to it, and it remains available unchanged for reprocessing.

- **Peak integration.** The software detects peaks in the signal: it finds where peaks start and end, constructs a baseline, and produces a peak table — retention time, area, height for each peak. Integration parameters are configurable and, in mature products, can be adjusted interactively on the graph.

- **Calibration and quantitation.** Peak responses are converted into amounts or concentrations. Standards of known content are measured under the same method; their responses form a calibration (response factors or curves) that is then applied to unknown samples. The two classical schemes — external standards measured separately, and an internal standard added to every vial — are both standard. Peak identification is tied to retention behavior against the calibration.

- **Method.** A named, stored, versioned set of parameters covering how the data is acquired (where control exists) and how it is processed: integration rules, compound identification, calibration levels, calculations. The method is what makes results reproducible — reapplying the method to stored raw data regenerates the results.

- **Sample-bound result records.** Every result belongs to an identifiable measurement of a named sample, and results are stored, reviewable, and renderable as a report. In regulated laboratories the record carries attribution (who did what, when) and signature state.

If the software does not store reprocessable raw data, or does not integrate peaks, or does not calibrate responses into quantities, it is not a CDS — it is a chart recorder, a signal viewer, or a generic data-acquisition tool.

### Standard Capabilities in Mature Products

Mature products add a well-established layer above the core:

- **Instrument control.** Driver or control modules let the CDS start and stop runs, set device parameters (flows, temperatures, gradients, injection programs), monitor status in real time, and queue work. The breadth of controllable instruments is a major competitive differentiator — some products control only their own vendor's instruments, others control instruments from many manufacturers.
- **Sequence table.** The batch container for automated work: an ordered list of injections (standards, samples, blanks, QC samples) with vial positions, methods, and per-row status, executed against an autosampler or manually.
- **Real-time acquisition display.** A live plot of the developing signal, elapsed time, and run state while an injection is in progress.
- **Multi-channel and spectral data.** Multiple detectors per run processed independently; diode-array and mass-spectrometric data as three-dimensional extensions.
- **Overlay and comparison.** Many chromatograms displayed together for comparison and mathematical manipulation.
- **Interactive re-integration.** Manual adjustment of baselines and integration events, with the change recorded and the before/after visible.
- **Recalibration and calibration history.** Curves updated from new standard runs; each chromatogram re-displayable under the conditions it was originally processed with.
- **Column performance calculations.** Symmetry, efficiency (plate counts), resolution — the numbers a chromatographer needs to judge a separation.
- **Custom result tables and calculations.** Configurable columns and user-defined formulas over the standard peak table.
- **Reporting.** Report templates and a report designer; export in interchange formats; automated post-run actions (display, print, export).
- **LIMS connectivity.** Import of sample lists from, and export of results to, a LIMS — the CDS participates in the sample workflow but does not own it.
- **Accounts, audit trail, electronic signatures.** User accounts with access rights; a running record of who changed what; electronic signing of results. The depth of this machinery varies strongly with the regulatory posture of the target laboratory.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:        Raw signal record
Implementations: file-based raw data on a workstation;  version-controlled raw data in a central relational database

Concept:        Method
Implementations: single combined method file;  acquisition and processing kept as distinct method parts

Concept:        Calibration
Implementations: single-level response factor;  multi-level curves with recalibration from sequence runs

Concept:        Result record
Implementations: per-chromatogram result set;  centrally aggregated results with review and signature state
```

A reader who has only seen an enterprise client/server deployment should still be able to recognize a single-workstation product — and a historical stand-alone integrator — as the same Type.

## How It Works

The defining workflow runs from vial to report:

### 1. Prepare the method and the system

The analyst selects or edits a method: acquisition parameters (where the CDS controls the instrument), integration rules, the compound list with expected retention times, and the calibration scheme. Instrument configuration — which detectors and channels belong to the system — is set up once and reused.

### 2. Build the sequence

The analyst composes the run as a sequence: rows for standards, samples, blanks, and QC injections, each bound to a vial position, a method, and the sample identity. In regulated laboratories a second person may review and approve the sequence before it is allowed to start, because a wrong sequence produces unusable results at the cost of instrument time.

### 3. Run and acquire

The CDS (directly, or through the instrument's own start mechanism) executes the sequence: each injection proceeds, the detector signal streams in, and the live display shows the developing chromatogram, elapsed time, and run state. The analyst monitors rather than intervenes; anomalies (pressure, leaks, failed injections) surface as status problems or visible signal artifacts.

### 4. Process and quantify

As injections complete, the software integrates each chromatogram against the method's rules, identifies peaks, builds or refreshes the calibration from the standard injections, and computes amounts for the unknowns. The analyst reviews peak tables, checks calibrations, and — where the automatic integration misjudged a peak — re-integrates manually.

### 5. Review and approve

Results are examined against expectations: known-sample recoveries, QC within limits, system suitability criteria met (in QC laboratories this suitability check is often computed automatically from the standard and QC injections). Out-of-limit items are flagged. In regulated contexts the reviewer inspects what changed (audit trail), compares manual re-integrations, and signs the result electronically.

### 6. Report and hand off

Approved results are rendered through report templates and exported — to the requesting lab system, a LIMS, or an archive. The raw data and its processing history remain stored and reprocessable.

## Interfaces

Exact layouts differ by product, but the working surfaces are consistent:

### Instrument control / monitor surface

The operator's view of the hardware: device status, live signal plot, elapsed time, queue of pending injections. Primary actions: start / stop / abort runs, adjust or view device parameters, acknowledge alerts. Present in depth where the CDS controls the instrument; reduced to a status view where acquisition is started on the instrument itself.

### Sequence table

A spreadsheet-like grid: one row per injection with sample name, vial position, method, injection count, and status. Primary actions: add/edit rows, fill down, copy methods, start the sequence, inspect per-row progress and errors.

### Data processing / review window

The analyst's main workspace after acquisition: one or more overlaid chromatograms with the integration drawn over the signal, the peak table beside or below, and result/calibration columns. Primary actions: re-integrate (adjust baseline or events), identify peaks, apply or change the method, compare against previous injections, inspect calculations.

### Calibration view

Standards, their measured responses, the fitted curve, and the quantitation results derived from it. Primary actions: build/refresh calibration, exclude or re-weight points, view calibration history.

### Report designer and output

Template-based composition of the printed/exported result document: chromatogram images, peak tables, summaries, method conditions, signatures. Primary actions: design templates, generate reports, export in interchange formats.

### Administration surface

Users and roles, permission configuration, instrument connections, audit-trail review. In regulated deployments this surface is where the review-and-approval regime is configured; the granularity of permissions varies considerably between products.

## Important Rules / Behaviors

- **Raw data is preserved.** Processing is a computation applied to stored raw data; reprocessing changes results, not the underlying signal. Mature products make the original data permanently retrievable and let every chromatogram be re-displayed exactly as it was originally processed. This is the property that separates a data system from a printout.
- **The method governs the result.** Two analysts processing the same raw data under the same method should obtain the same results; differences come from method differences or explicit manual re-integration — which is why manual changes are recorded and (in regulated use) reviewed.
- **Manual re-integration is a governed act.** Where results feed quality decisions, changing the integration by hand is permitted but visible: the before/after comparison and the audit entry are part of the record, and the reviewer, not the analyst alone, decides what stands.
- **The sequence is the automation contract.** Once started, the run proceeds row by row without the analyst; each row carries its own status, and a failed or aborted injection does not silently consume the rest of the sequence without a trace.
- **Suitability gates the batch.** In QC practice, results are only as good as the system suitability demonstrated by the standards and QCs inside the same sequence; mature products compute and flag this rather than leaving it to arithmetic outside the system.
- **Attribution is structural.** In regulated deployments, actions are attributable to named users with distinct roles: the person who runs the instrument, the person who processes, and the person who approves are expected to be able to be different people, and the audit trail assumes it.
- **The CDS holds instrument data, not sample logistics.** The sample list typically arrives from a LIMS (or is typed by the analyst), and results go back; the CDS is authoritative for the signal, the processing, and the computed result — not for the fate of the sample in the lab.

## Variants

- **Deployment shape.** From a single workstation holding its own raw data (historically even with a hardware license key) through small peer networks of workstations, up to strict client/server enterprises with a central relational database, central audit-trail review, and multi-site or cloud deployment. The same core model applies across the whole spectrum.
- **Regulatory posture.** Non-regulated editions (teaching labs, method development, simple analog-acquisition packages) omit the accounts/audit/signature machinery entirely; validated GMP-oriented deployments build it out fully, with qualification kits, validation declarations, and sequence approval steps.
- **Technique scope.** The base covers LC, GC, and IC signals. Products extend to capillary electrophoresis, size-exclusion/GPC polymer analysis, diode-array spectral data, mass-spectrometric data (up to high-resolution and multi-attribute biopharma workflows in some products), and norm-based petrochemical calculations (natural gas, hydrocarbon composition) as optional modules or extensions.
- **Product philosophy.** Independent, hardware-agnostic CDS products sell control modules for many manufacturers' instruments and perpetual licenses; instrument-vendor CDS products lead with deep control of their own instruments and integration into the vendor's wider informatics suite. Some instruments ship with bundled acquisition/processing software of CDS grade.
- **Shared-instrument mode.** Open-access / walk-up configurations for facilities where many occasional users share one instrument, with simplified flows that hide administrative complexity.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Laboratory Information Management System / LIMS | sample-centric: owns samples, chain of custody, lab-wide workflow, and cross-technique result aggregation; the CDS owns the instrument signal and its computed result — the two meet by exchanging sample lists (in) and results (out) |
| Electronic Laboratory Notebook / ELN | narrative experiment documentation and protocols as written records; the CDS holds instrument signals and computed results; they integrate but neither absorbs the other |
| Laboratory Information System / LIS | clinical specimen- and patient-order-centric workflows; no chromatography instrument-data processing core |
| Instrument firmware / on-device HMI | runs and monitors the hardware on the device; lacks the persistent reprocessable raw data, method-driven reprocessing, calibration, and result-record system of the CDS (modern firmware with built-in integration blurs but does not close this gap) |
| SCADA / Industrial Historian | acquires arbitrary process signals generically; cannot integrate peaks against a calibrated method or quantify a sample — the CDS is defined by chromatography semantics |
| Scientific Data Management System | generic cross-instrument archiving of data and files; the CDS processes a specific data species into scientific results |
| Statistical Process Control / SPC | consumes measured values for statistical monitoring; does not acquire or process the instrument signal itself |

The sharpest boundary is with the LIMS: both keep records about the same physical samples, but the CDS's unit of work is the injection and its signal, while the LIMS's unit of work is the sample and its journey through the laboratory. A product that drops instrument-data acquisition and processing while keeping sample workflows has become a LIMS; a product that adds sample logistics on top of a CDS is a suite, not a new core.

## Representative Products

- Thermo Scientific Chromeleon CDS (Thermo Fisher Scientific)
- Empower Chromatography Data Software (Waters)
- OpenLab CDS (Agilent)
- Clarity Chromatography Software (DataApex)

These span the enterprise instrument-vendor tier and the independent hardware-agnostic tier; the defining core was checked across both.

## Sources

Research date: **2026-09-06**

- DataApex — Clarity Chromatography Software (product page) — https://www.dataapex.com/clarity
- DataApex — Clarity in a regulated environment — https://www.dataapex.com/clarity-in-regulated-environment
- DataApex — Clarity and related chromatography key terms (glossary) — https://www.dataapex.com/document/chromatography-terms
- DataApex — Clarity Guides & Documentation, "Getting to know Clarity" — https://www.dataapex.com/documentation/Content/getting-started/010-getting-started/010.000-getting-started/010-getting-to-know.htm
- Thermo Fisher Scientific — Chromatography Data System / Chromeleon CDS (category page) — https://www.thermofisher.com/uk/en/home/industrial/chromatography/chromatography-data-systems-cds.html
- Thermo Fisher Scientific — Chromeleon CDS (product/catalog page) — https://www.thermofisher.com/order/catalog/product/CHROMELEON7
- Thermo Fisher Scientific — CDS Software — Workstation (product page) — https://www.thermofisher.com/uk/en/home/industrial/chromatography/chromatography-data-systems-cds/workstation-cds-software.html

> Sourcing limitation: official documentation for Waters Empower and Agilent OpenLab CDS could not be fetched from the research environment on 2026-09-06 (blocked requests). Both are included as market anchors based on market position and third-party vendor positioning, and no product-specific operational claims are made for them. Chromeleon observations rest on vendor product/category pages rather than deep help-center articles, so operational specifics (numeric limits, defaults, exact procedures) are intentionally not stated in this document.

Detailed evidence, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
