# Carbon Accounting Platform

## Overview

A **Carbon Accounting Platform** is an organization's system of record for its greenhouse gas emissions. It captures quantified records of the organization's emitting activities, converts them into emissions using documented emission factors, and aggregates the results into a structured emissions inventory for a defined reporting period. That inventory is then used for climate disclosure, target setting, and reduction planning.

The defining loop is small:

```text
Activity data (what the organization did)
× Emission factors (documented conversion coefficients)
= Computed emissions (CO2e)
→ aggregated into an inventory for a reporting period
→ made auditable and reportable
```

Everything else commonly associated with these products — the Scope 1/2/3 taxonomy, supplier surveys, framework-specific disclosure formatting, decarbonization roadmaps, AI assistance — is widespread in current products but is not what makes the product a carbon accounting platform. A spreadsheet-era inventory built from activity data and published factors satisfies the same defining loop; modern platforms industrialize it.

When the center of gravity shifts away from the emissions inventory — toward broader environmental, social, and governance data, toward physical measurement of emission sources, toward the product as the unit of account, or toward forward-looking abatement planning — the product is drifting toward a different Application Type.

## Users & Context

Primary users:

- **Sustainability manager / lead** — owns the inventory: defines the organizational boundary, drives data collection, reviews calculations, signs off on results.
- **ESG / carbon analyst** — does the hands-on work: imports data, maps emission factors, investigates anomalies, prepares reports.
- **Finance and controllership** — increasingly involved because emissions data is treated with financial-reporting discipline (audit trails, period closing, assurance).
- **Data providers across the business** — facility managers, fleet and travel managers, procurement, HR: they supply utility bills, fuel records, spend data, travel bookings. They usually interact with the platform only to upload files or answer surveys.

Secondary users:

- **Auditors and assurance providers** — consume the audit trail, calculation transparency, and closed-period data to verify the inventory.
- **IT administrators** — manage integrations, permissions, and organizational structure.
- **Executives and board** — consume dashboards and disclosure outputs.

Typical context: annual (sometimes quarterly or monthly) reporting cycles driven by climate disclosure regulation (such as the EU CSRD, California climate disclosure laws, and investor frameworks), voluntary disclosure programs, customer and investor questionnaires, and science-based target commitments. The work is cyclical: collect → calculate → review → close → report, then repeat and compare against prior periods.

## Core Model

### The Defining Core

```text
Organizational boundary
└── Activity data records (bound to org unit + time period)
    └── Emission factors (documented, sourced, versioned)
        └── Calculation (activity × factor → gases → CO2e)
            └── Emissions inventory for a reporting period
                └── Audit trail over all of the above
```

Five properties. If any one is removed, the product is no longer recognizable as a carbon accounting platform:

- **Organizational boundary** — the unit of account is the organization (a company, group, institution) and the parts it includes. Without this, the product becomes a product-footprint tool or a personal calculator.
- **Activity data records** — quantified records of emitting activities: electricity purchased, fuel burned, materials bought, distance traveled, waste disposed. Each record belongs to an organizational unit and a time period. Without these, there is nothing to account for.
- **Emission factors** — coefficients that convert an activity into greenhouse gas emissions, drawn from published scientific and statistical sources and applied with a traceable methodology. Without factors, activity data stays raw data.
- **Computed inventory over a reporting period** — the platform calculates emissions (per gas, converted to CO2-equivalent using global warming potentials) and aggregates them into an inventory bounded by a reporting period. Without the computed inventory, the product is only a data collector.
- **Auditability** — the path from every reported number back to its source data, factor, and calculation method is recorded and inspectable. Without this, the output cannot survive disclosure-grade scrutiny, which is the reason organizations use these platforms at all.

### Standard Capabilities of Mature Products

Mature products commonly add the following. They make the inventory practical and disclosure-grade, but they are not the definition:

- **Organizational hierarchy** — facilities, sites, business units, regions (sometimes assets, product lines, joint ventures) as the attribution and roll-up dimension. Emissions are calculated at the point of activity and roll up the hierarchy.
- **Scope organization** — the inventory is organized by emission scope: Scope 1 (direct emissions from owned or controlled sources), Scope 2 (indirect emissions from purchased energy), Scope 3 (all other indirect emissions across the value chain), with Scope 3 further divided into categories (purchased goods, transportation, business travel, use of sold products, investments, and so on). This taxonomy comes from the Greenhouse Gas Protocol and is effectively universal in current products; it is the dominant implementation of "organized emission categories," not the definition itself.
- **Data ingestion machinery** — pre-built integrations with business systems (utilities, ERP, travel, expense), file upload (spreadsheets, bills), manual entry, and supplier surveys or portals; with field mapping and transformation along the way.
- **Factor library management** — emission factors loaded from published sources (national environmental agencies, energy agencies, input-output databases), versioned by publication year, mapped to reference data (fuel types, facilities, materials, disposal methods); plus custom factors for cases the published sets don't cover. Some products also provide estimation factors that convert proxy data (such as building area or hotel nights) into usable activity data.
- **Calculation method choices** — spend-based versus activity-based estimation; location-based versus market-based accounting for purchased energy; distance-, fuel-, or spend-based methods for transport; attribution-based methods for financed emissions. The chosen method is itself recorded data.
- **Data quality machinery** — anomaly detection, completeness and plausibility checks, data approval staging, period locking, and full data lineage.
- **Disclosure outputs** — reports and exports aligned to climate frameworks and regulations (CSRD/ESRS, CDP, TCFD/ISSB, regional climate laws), often with guided workflows that reuse one measured inventory across many frameworks.
- **Analytics** — dashboards of emissions by scope, category, organizational unit, and time; hotspot identification; year-over-year comparison.
- **Targets and progress tracking** — reduction targets (often science-based-target aligned), progress against a base year, and reduction roadmaps.

### One Structure, Many Implementations

The core model is conceptual. Specific products realize each concept differently:

```text
Concept:  Organizational boundary
Implementations:  legal-entity structures, facility lists, equity-share or
                  operational-control approaches defined per reporting standard

Concept:  Activity data
Implementations:  utility bills, meter readings, ERP spend records, travel bookings,
                  fuel logs, supplier-reported data, survey responses

Concept:  Emission factors
Implementations:  national agency factor sets (EPA, Defra, ADEME, NGER...),
                  energy-agency grid factors, input-output economic models,
                  supplier-specific factors, custom in-house factors

Concept:  Inventory organization
Implementations:  GHG Protocol scopes and Scope 3 categories (dominant),
                  ISO-style category schemes, custom category trees

Concept:  Auditability
Implementations:  audit logs, per-calculation formula/factor display,
                  data lineage views, closed-period snapshots
```

A reader who has only seen one implementation — for example, a spend-based tool that ingests accounting data — should still be able to recognize an activity-based, supplier-survey-driven product as the same Type.

## How It Works

### 1. Define the organizational boundary and structure

The sustainability team sets up what the organization includes: legal entities, facilities, regions, business units. This structure becomes the attribution skeleton — every later data record and computed emission hangs on one of its nodes. The boundary approach (which entities, which control criterion) is a recorded decision because it determines the inventory's completeness claim.

### 2. Collect activity data

Data enters from many directions:

```text
System integrations (utilities, ERP, travel, expense, meters)
+ file uploads (bills, spreadsheets, exports)
+ manual entry
+ supplier surveys / portals (for value-chain data)
→ mapped and transformed into activity data records
  (quantity, unit, org unit, time period, source)
```

Gaps are common: missing months, wrong units, implausible values. Mature products surface these as exceptions — anomaly warnings, completeness checks — and some offer estimation paths (proxy-based estimation factors) so the inventory can be completed and the estimates flagged.

### 3. Map factors and calculate

Each activity record is matched to an emission factor — directly, or through mappings to reference data (this facility's electricity → this regional grid factor; this spend category → this input-output factor). The calculation multiplies activity by factor, produces emissions per greenhouse gas, converts them to CO2e using global warming potentials, and stores the result as an emission record tied to the source data. Method choices (spend vs activity, location vs market) are configured per scope or category and recorded with the results.

### 4. Review, approve, close

The inventory is reviewed: analysts investigate anomalies, data owners approve their contributions, and the team reconciles against prior periods. When the period is accepted, it is **closed or locked** — a state change that prevents further edits to that period's data and calculations. This is the discipline that makes the inventory assurance-ready; it mirrors financial close.

### 5. Report and disclose

From the closed inventory, the team produces outputs: internal dashboards, management reports, and framework-aligned disclosures. Mature products reuse the same measured data across multiple frameworks rather than recalculating per framework, and keep the lineage from each disclosed figure back to source data.

### 6. Set targets and track

Against a base year, the organization defines reduction targets and tracks progress as new periods are measured. Many products extend into reduction planning: identifying hotspots, modeling reduction initiatives, and tracking projects — the measured inventory remains the anchor.

### 7. Recalculate when the ground shifts

Methodology changes, factor-library updates, acquisitions, or boundary changes force recalculation of past periods so comparisons stay valid. Platforms support this by keeping calculation logic separate from data, so a changed factor or method can be re-applied and the difference explained.

## Interfaces

Described conceptually; exact layouts vary by product.

### Dashboard / analytics

The overview surface. Typical information: total emissions by scope, trends over periods, breakdowns by organizational unit and category, hotspot highlights. Primary actions: filter, drill down, export.

### Data import / collection workspace

Where activity data enters. Typical information: import sources, mapping previews, validation and error lists, pending records. Primary actions: connect a source, upload a file, map fields, fix rejected rows, submit for approval.

### Emission factor library

The reference-data surface. Typical information: factor sets by source and version, individual factors with units and gas breakdowns, mappings to fuels/facilities/materials. Primary actions: load or update a library, add a custom factor, create a mapping.

### Emissions ledger / records

The system-of-record surface: the computed emissions themselves. Typical information: emission records with source activity, factor, method, org unit, period, and per-gas values. Primary actions: filter, inspect calculation detail, export, manually add or correct.

### Reporting / disclosure workspace

Where outputs are produced. Typical information: framework requirements, mapped data points, draft reports, disclosure status. Primary actions: generate a framework report, review pre-populated figures, export.

### Supplier engagement surface

For value-chain data collection: surveys or portals where suppliers report their own activity or emissions data, which then feeds Scope 3 calculations.

### Administration

Organizational structure, user roles and permissions, integrations, reporting-period settings, audit-log access.

## Important Rules / Behaviors

### Reporting periods have a lifecycle

A period is open while data is collected and corrected, then closed or locked. After closing, edits, imports, and recalculations affecting that period are blocked (or require an explicit, logged reopening). This is the single most consequential state rule in the Type: it is what turns a working dataset into an auditable record.

### Every number must be traceable

The platform maintains the chain: reported figure → calculation method → emission factor (with version and source) → activity data record → original source. Assurance and internal review depend on this lineage; products that break it lose their reason to exist.

### Method choices are recorded decisions

Spend-based versus activity-based, location-based versus market-based — these are not hidden implementation details but visible, documented choices that materially change results. Mature products keep both views where frameworks require it (notably dual reporting for purchased energy) and label which method produced which figure.

### Data quality is hierarchical

Primary data (meters, bills, supplier-specific figures) outranks secondary estimates (industry averages, spend-based proxies). The inventory records the quality of its inputs, and improving data quality over time is an explicit goal — which is why supplier engagement exists: to replace spend-based estimates with supplier-specific data.

### Estimates are flagged, not hidden

Where activity data is missing, estimation fills the gap — but the estimated nature stays visible in the record, so reviewers and auditors can weigh it.

### Recalculation is expected, not exceptional

Factor libraries update annually; methodologies evolve; organizations change shape. The inventory is designed to be recomputed under a changed method while preserving the ability to explain what changed and why.

## Variants

- **Enterprise audit-grade platforms** — deep data governance, assurance workflows, multi-entity hierarchies, custom methodology control; sold to large and regulated organizations.
- **Suite-module deployments** — carbon accounting embedded in a broader cloud platform (ERP or data-platform ecosystem), trading standalone depth for integration with existing business systems.
- **ESG-data-suite members** — carbon accounting as the strongest module inside a wider ESG data management product that also handles other environmental and social metrics.
- **SMB self-serve products** — streamlined onboarding, spend-based first-pass measurement, guided expert or AI support; lower data burden, faster time to a first footprint.
- **Financial-services specialization** — financed emissions: attributing the emissions of loans and investments to the financial institution using attribution methodologies (an established industry standard for this segment).
- **Regional factor regimes** — factor libraries and reporting templates shaped by national or regional schemes (US, UK, EU, France, Australia, Taiwan, and others); products often carry multiple regional libraries.
- **Extended-environmental variants** — the same record-calculate-report machinery applied to water, waste, or other environmental metrics alongside carbon.
- **Product-footprint extensions** — some organizational platforms add per-product footprint calculation as an adjacent capability.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Greenhouse Gas Accounting | sibling concept | names the methodology this software implements; the platform is the software realization — probable near-alias at the directory level |
| Sustainability Management Platform / ESG Management Platform | broader | adds social and governance metrics and wider ESG data management; carbon accounting's center of gravity is the emissions inventory itself |
| ESG Reporting Platform / ESG Disclosure Management | output-centric | starts from the disclosure requirement and formats data for it; carbon accounting starts from measurement, with disclosure as an output |
| Emissions Monitoring / CEMS | different measurement physics | continuously measures actual emissions at sources with instruments; carbon accounting computes organizational emissions from activity data and factors |
| Energy & Carbon Management | energy-first | optimizes consumption (metering, efficiency, control); carbon accounting is organization-wide including the value chain, with energy as one input |
| Product Carbon Footprint Platform | different unit of account | the product (and its lifecycle) is the measured unit, not the organization |
| Life Cycle Assessment Application | deeper product modeling | full lifecycle modeling methodology per product; organizational inventory is not its object |
| Decarbonization Planning Platform | forward-looking | plans and prioritizes future abatement; carbon accounting measures what happened — planning is a common extension of the measured inventory |
| Carbon Credit Management | different object | manages offsets/credits as instruments (registries, retirement); the emissions inventory is a different record system |
| Climate Risk Management | different question | assesses physical and transition risk exposure; carbon accounting quantifies emissions actually emitted |

The most important boundary is with the ESG/sustainability suite family: current products blur it by adding water, waste, and social metrics. The structural test is the center of gravity — if the emissions inventory (activity data + factors + computed, auditable CO2e over periods) is the system of record, it is a carbon accounting platform; if emissions are one metric among many with no inventory discipline, it is an ESG management platform.

## Representative Products

- **Watershed** — enterprise platform with a data-quality and audit-grade posture; measurement, disclosure, and reduction in one product line
- **Persefoni** — enterprise carbon accounting with financial-ledger-style controls and a dedicated financial-services (financed emissions) line
- **Microsoft Sustainability Manager** — carbon accounting as a module of a broader cloud platform; integration-first, deeply documented calculation and import machinery
- **IBM Envizi** — ESG data management suite with an emissions calculation engine at its core; finance-grade validation posture
- **Greenly** — SMB-to-enterprise carbon management with self-serve onboarding and AI-assisted data processing

These five were chosen to span enterprise and SMB tiers, standalone and suite deployments, and different product philosophies (data-quality-first, ledger-discipline-first, integration-first, data-management-first, self-serve-first).

## Sources

Research date: **2026-09-07**

- Microsoft — Microsoft Sustainability Manager documentation (overview; manage emissions; configure emission factors; calculate Scope 2; calculate Scope 3; data import overview): https://learn.microsoft.com/en-us/industry/sustainability/
- Watershed — platform and carbon accounting pages: https://www.watershed.com/ , https://www.watershed.com/platform/measure/carbon-accounting , https://www.watershed.com/platform/measure
- Persefoni — product pages: https://www.persefoni.com/ , https://www.persefoni.com/business/carbon-footprint-measurement-analytics
- IBM — Envizi product page: https://www.ibm.com/products/envizi
- Greenly — product pages: https://greenly.earth/en-us , https://greenly.earth/en-us/products/carbon-footprint

> Sourcing limitation: only Microsoft publishes deep public operational documentation among the sampled products; Watershed, Persefoni, IBM Envizi, and Greenly were studied from official product and platform pages (their public help centers were not reachable from the research environment, and IBM's documentation portal returned an access error). Claims about those products are therefore kept at the level their official pages support. Numeric limits, prices, factor counts, and plan-specific details are intentionally not stated in this document; vendor-specific observations remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
