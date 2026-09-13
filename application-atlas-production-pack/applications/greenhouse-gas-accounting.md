# Greenhouse Gas Accounting

## Overview

A **Greenhouse Gas Accounting** application is an organization's system of record for quantifying its greenhouse gas emissions. It captures records of the organization's emitting activities, converts them into emissions using documented emission factors, and assembles the results into a structured emissions inventory — the organization's "GHG inventory" — for a defined reporting period. Because the inventory must survive external scrutiny, the path from every reported number back to its source data, factor, and calculation method is recorded and inspectable. The inventory then feeds disclosure, target setting, and reduction planning.

The defining loop is small:

```text
A bounded organization (the unit of account)
└── Activity data records (what the organization did, per unit and period)
    └── Emission factors (documented conversion coefficients)
        └── Computed emissions, per gas, aggregated to CO2e
            └── A GHG inventory for the reporting period
                └── Traceable and auditable end to end
```

One naming fact should be stated plainly: this is the same application that the market usually calls a **Carbon Accounting Platform**, documented in the atlas under that name. "Greenhouse gas accounting" is the methodology's own term — the international accounting standard for corporate GHG inventories is literally titled a Corporate Accounting and Reporting Standard — while "carbon accounting" is the commercial label under which most products are sold. The products themselves mix both vocabularies freely: a vendor's product pages describe "carbon accounting" while defining the work as measuring "greenhouse gas emissions"; certification marks advertise conformance to the GHG Protocol; public-sector implementations speak of "greenhouse gas inventories" where a commercial vendor would say carbon accounting. No separate product population answers to one label and not the other. Both directory entries describe one Type from two angles — this document from the methodology angle (the standard, the multi-gas CO2e inventory, conformance and certification, the public-sector inventory tradition), the sibling from the product-category angle. Both stand; consolidation of the leaves is recommended, and readers should treat the two as one application with two names.

Everything else commonly associated with these products — the Scope 1/2/3 taxonomy, supplier surveys, framework-specific disclosure formatting, decarbonization roadmaps, AI assistance — is standard or optional structure that mature products add, not what makes the product GHG accounting. A spreadsheet-era inventory built from activity data and published factors satisfies the same defining loop; indeed, the methodology itself has long shipped spreadsheet-style calculation tools, and modern platforms industrialize that practice.

## Users & Context

Primary users:

- **Sustainability manager / lead** — owns the inventory: defines the organizational boundary, drives data collection, reviews calculations, signs off on results.
- **ESG / carbon analyst** — does the hands-on work: imports data, maps emission factors, investigates anomalies, prepares reports.
- **Finance and controllership** — increasingly involved because emissions data is treated with financial-reporting discipline (audit trails, period closing, assurance).
- **Data providers across the organization** — facility managers, fleet and travel managers, procurement, HR: they supply utility bills, fuel records, spend data, travel bookings, usually interacting with the system only to upload files or answer surveys.

Secondary users:

- **Auditors and assurance providers** — consume the audit trail, calculation transparency, and closed-period data to verify the inventory. Some products maintain networks of vetted auditors or specifically support limited-assurance engagements.
- **Executives, boards, and (in public-sector deployments) councils and community stakeholders** — consume dashboards and disclosure outputs.
- **IT administrators** — manage integrations, permissions, and organizational structure.

Typical context: annual (sometimes quarterly or monthly) reporting cycles driven by climate disclosure regulation, voluntary disclosure programs, customer and investor questionnaires, and science-based target commitments. In the public-sector variant the "organization" is a local government and the context is community-wide or government-operations inventories feeding public climate action plans. The work is cyclical: collect → calculate → review → close → report, then repeat and compare against prior periods.

## Core Model

### The defining core

**1. A bounded organization as the unit of account.** The system accounts for one identifiable organization — a company, group, institution, agency, or (in the public-sector variant) a community or government's operations. What counts as "inside" the account is a recorded decision, because it determines the inventory's completeness claim. Without this, the product becomes a product-footprint tool or a consumer calculator.

**2. Activity data records.** Quantified records of what the organization did that emits: electricity purchased, fuel burned, materials bought, distance traveled, waste disposed. Each record belongs to an organizational unit and a time period. Without these, there is nothing to account for.

**3. Emission factors.** Coefficients that convert an activity into greenhouse gas emissions, drawn from published scientific and statistical sources and applied with a traceable methodology. The multi-gas character lives here: the accounting covers the greenhouse gases covered by the Kyoto Protocol (carbon dioxide plus methane, nitrous oxide, HFCs, PFCs, sulphur hexafluoride, and nitrogen trifluoride), not literally only "carbon." Without factors, activity data stays raw data.

**4. A computed inventory over a reporting period.** The system calculates emissions (activity × factor, per gas, converted to CO2-equivalent using global warming potentials) and aggregates them into an inventory of the organization for a defined period. The inventory — not a dashboard, not a report — is the deliverable. Without it, the product is only a data collector.

**5. Auditability.** The path from every reported figure back to its source data, factor, and calculation method is recorded and inspectable. The underlying accounting standard is explicitly designed so inventories can be verified, and current products carry this into software: audit trails, per-calculation transparency, lineage views. Without this, the output cannot serve the disclosure and assurance purposes that motivate the accounting.

### Standard capabilities of mature products

These make the inventory practical and disclosure-grade; none is the definition:

- **Organizational hierarchy** — facilities, sites, business units, regions (sometimes assets, product lines, joint ventures) as the attribution and roll-up dimension.
- **Scope organization** — the inventory organized by emission scope: direct emissions from owned or controlled sources (Scope 1), emissions from purchased energy (Scope 2), and other indirect value-chain emissions (Scope 3, with its categories). This taxonomy comes from the GHG Protocol and is effectively universal in current products; it is the dominant implementation of "organized emission categories," not the definition itself — alternative category schemes exist, and community-scale inventories follow community protocols instead.
- **Data ingestion machinery** — integrations with business systems (utilities, ERP, travel, expense), file upload, manual entry, and supplier surveys or portals; with mapping and transformation along the way.
- **Factor library management** — factors loaded from published sources (national agencies, energy agencies, input-output databases), versioned by publication year, mapped to fuels, facilities, materials, and disposal methods; custom factors where published sets don't reach; estimation factors that convert proxy data (building area, hotel nights) into usable activity data.
- **Calculation method choices** — spend-based versus activity-based estimation; location-based versus market-based accounting for purchased energy; distance-, fuel-, or spend-based methods for transport; attribution methods for financed emissions. The chosen method is itself recorded data.
- **Data quality machinery** — anomaly detection, completeness and plausibility checks, approval staging, period locking, data lineage.
- **Conformance and certification signaling** — products advertise alignment with the GHG Protocol (sometimes with third-party certification of the measurement methodology), and the standards body itself maintains a public register of tools built on the standard. This trust machinery is characteristic of the Type, though the specific schemes vary.
- **Disclosure outputs** — reports and exports aligned to climate frameworks and regulations, reusing one measured inventory across many frameworks.
- **Analytics** — emissions by scope, category, unit, and time; hotspots; year-over-year comparison.
- **Targets and progress tracking** — reduction targets (often science-based-target aligned), progress against a base year.

### One structure, many implementations

The core model is conceptual; specific products realize it differently:

```text
Concept:  the bounded organization
Implementations:  legal-entity structures, facility hierarchies, equity-share or
                  operational-control approaches; community-wide or
                  government-operations scales in public-sector deployments

Concept:  the emission categories
Implementations:  GHG Protocol scopes and Scope 3 categories (dominant),
                  ISO-style category schemes, community-scale protocol categories

Concept:  the factors
Implementations:  national agency factor sets, grid factors, input-output
                  economic models, supplier-specific factors, custom factors

Concept:  the conformance layer
Implementations:  alignment claims, third-party certification of the
                  measurement methodology, registration in the standards
                  body's tools register
```

A reader who has only seen a spend-based commercial tool should still recognize a supplier-survey-driven enterprise platform, or a city government's community-scale inventory tool, as the same Type.

## How It Works

### 1. Define the boundary and structure

The sustainability team sets up what the organization includes: legal entities, facilities, regions, business units — or, in a public-sector deployment, the community and the government's own operations, typically as two distinct inventory scales. This structure becomes the attribution skeleton; the boundary approach is a recorded decision because it determines the completeness claim.

### 2. Collect activity data

Data enters from many directions — system integrations, file uploads (bills, spreadsheets), manual entry, supplier surveys — and is mapped into activity data records: quantity, unit, organizational unit, time period, source. Gaps are common; mature products surface them as exceptions and offer estimation paths, with estimates flagged rather than hidden.

### 3. Match factors and calculate

Each activity record is matched to an emission factor, directly or through mappings to reference data (this facility's electricity → this regional grid factor; this spend category → this input-output factor). The calculation multiplies activity by factor, produces emissions per greenhouse gas, converts them to CO2e using global warming potentials, and stores the result tied to the source data. Method choices are configured per scope or category and recorded with the results.

### 4. Review, verify, close

The inventory is reviewed: analysts investigate anomalies, data owners approve contributions, the team reconciles against prior periods. When the period is accepted, it is **closed or locked** — edits, imports, and recalculations affecting it are blocked or require an explicit, logged reopening. This is the discipline that turns a working dataset into an auditable record, and it mirrors financial close. Where external assurance is sought, auditors work from the retained trail: every figure resolves back to its data, factor, and method.

### 5. Report the inventory

From the closed inventory the team produces outputs: the GHG inventory statement itself, internal dashboards, and framework- or regulation-aligned disclosures. Mature products reuse the same measured data across multiple reporting formats rather than recalculating per framework.

### 6. Set targets and track

Against a base year, the organization defines reduction targets and tracks progress as new periods are measured. Many products extend into reduction planning — hotspot analysis, initiative modeling, supplier engagement programs — with the measured inventory remaining the anchor. In the public-sector variant this extension takes the form of emissions forecasts and climate action plans.

### 7. Recalculate when the ground shifts

Factor libraries update, methodologies evolve, organizations change shape. Past periods are recalculated under changed assumptions so comparisons stay valid, with the difference explained rather than silently absorbed.

### Capability tiers at a glance

**Defining core** — bounded organization as unit of account; activity data records; documented emission factors; computed multi-gas inventory over a reporting period; end-to-end traceability.

**Standard in mature products** — organizational hierarchy, scope organization, ingestion machinery, factor libraries with mappings and estimation factors, method choices, data-quality machinery, conformance signaling, disclosure outputs, analytics, targets.

**Common variants / optional** — financed emissions for financial institutions, supplier engagement programs, decarbonization planning and forecasting, extended environmental metrics, product-footprint extensions, AI assistance, community-scale and public-sector deployments.

## Interfaces

Described conceptually; exact layouts vary by product.

### Dashboard / analytics

The overview surface. Typical information: total emissions by scope, trends over periods, breakdowns by organizational unit and category, hotspot highlights. Primary actions: filter, drill down, export.

### Data collection / import workspace

Where activity data enters. Typical information: import sources, mapping previews, validation and error lists, pending records, per-department collection progress. Primary actions: connect a source, upload a file, map fields, fix rejected rows, submit for approval.

### Emission factor library

The reference-data surface. Typical information: factor sets by source and version, individual factors with units and gas breakdowns, mappings to fuels, facilities, materials. Primary actions: load or update a library, add a custom factor, create a mapping.

### Inventory / emissions records

The system-of-record surface: the computed emissions themselves. Typical information: emission records with source activity, factor, method, organizational unit, period, and per-gas values. Primary actions: filter, inspect calculation detail, export, manually add or correct.

### Reporting / disclosure workspace

Where outputs are produced. Typical information: framework requirements, mapped data points, draft reports, disclosure status. Primary actions: generate a framework report, review pre-populated figures, export.

### Supplier engagement surface

For value-chain data: surveys or portals where suppliers report their own activity or emissions data, feeding Scope 3 calculations.

### Administration

Organizational structure, user roles and permissions, integrations, reporting-period settings, audit-log access.

## Important Rules / Behaviors

### The gases are plural by definition

The accounting covers the suite of greenhouse gases covered by the Kyoto Protocol and aggregates them to CO2-equivalent using global warming potentials. "Carbon" in the market label is a metonym; a tool that accounts only for carbon dioxide is not delivering what the methodology defines.

### Reporting periods have a lifecycle

A period is open while data is collected and corrected, then closed or locked; after closing, changes require an explicit, logged reopening. This state rule is what makes the inventory assurance-ready.

### Every number must be traceable

Reported figure → calculation method → emission factor (with version and source) → activity record → original source. Verification and internal review depend on the lineage; products that break it lose their reason to exist.

### Method choices are recorded decisions

Spend- versus activity-based, location- versus market-based — visible, documented choices that materially change results, labeled on the figures they produce.

### Data quality is hierarchical

Primary data (meters, bills, supplier-specific figures) outranks secondary estimates (industry averages, spend-based proxies). The inventory records input quality, and improving it over time is an explicit goal — which is why supplier engagement exists.

### The methodology's own boundary is respected

The corporate accounting standard explicitly does not cover quantifying reductions from mitigation projects for use as offsets or credits — that belongs to separate project-accounting methodology, and credit instruments belong to credit-management systems. Product-level accounting likewise has its own standard. The organizational inventory is this Type's object of record.

## Variants

- **Enterprise audit-grade platforms** — deep data governance, assurance workflows, multi-entity hierarchies; sold to large and regulated organizations.
- **Suite-module deployments** — the accounting core as one module of a broader cloud platform or of an ESG/compliance suite that also handles other regulatory reporting.
- **SMB self-serve products** — streamlined onboarding, spend-based first-pass measurement, guided expert or AI support; faster time to a first footprint.
- **Financial-services specialization** — financed emissions: attributing the emissions of loans and investments to the institution using attribution methodologies.
- **Public-sector and community-scale** — local-government platforms completing community-wide and government-operations greenhouse gas inventories, with forecasts and climate action plans attached; the vocabulary shifts to "GHG inventory" and "emissions management" but the accounting core is the same.
- **Consultancy-served accounting** — the inventory assembled by advisory firms using the platform, with the organization as the accountable owner.
- **Regional factor regimes** — factor libraries and templates shaped by national or regional schemes; products often carry multiple regional libraries.
- **Product-footprint extensions** — per-product footprint calculation as an adjacent capability riding on the organizational machinery.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Carbon Accounting Platform | The same application under the market's other label. The methodology is named GHG accounting; the product category is named carbon accounting; every researched product answers to both vocabularies. One Type, two directory entries — consolidation recommended. |
| Sustainability Management Platform / ESG Management Platform | Broader: adds social and governance metrics and wider ESG data management. The structural test is the center of gravity — if the emissions inventory (activity data + factors + computed, auditable CO2e over periods) is the system of record, it is this Type; if emissions are one metric among many, it is an ESG platform carrying an accounting module. |
| ESG Reporting Platform / ESG Disclosure Management | Output-centric: starts from the disclosure requirement and formats data for it; this Type starts from measurement, with disclosure as an output. |
| Emissions Monitoring / CEMS | Different measurement physics: continuously measures actual emissions at sources with instruments, versus computing organizational emissions from activity data and factors. |
| Energy & Carbon Management | Energy-first: optimizes consumption (metering, efficiency, control); this Type is organization-wide including the value chain, with energy as one input. |
| Product Carbon Footprint Platform | Different unit of account: the product and its lifecycle, not the organization — the methodology itself maintains a separate standard for product-level accounting. |
| Life Cycle Assessment Application | Deeper product modeling methodology per product; the organizational inventory is not its object. |
| Scope 3 Management Platform | Focused slice: value-chain emissions data collection and supplier engagement are the center; this Type owns the full organizational inventory of which Scope 3 is one part. |
| Decarbonization Planning Platform | Forward-looking abatement planning versus measurement of what happened; planning is a common extension of the measured inventory. |
| Carbon Credit Management | Different object: credits and offsets as instruments (registries, retirement). Project-level reduction accounting follows a separate methodology from corporate inventory accounting. |
| Climate Risk Management | Different question: physical and transition risk exposure versus quantifying emissions actually emitted. |

## Representative Products

- **Plan A** — mid-market product titled "Carbon Accounting Software"; measure → report → decarbonize journey; measurement methodology certified as GHG Protocol compliant by an independent testing body.
- **Coolset** — mid-market ESG and supply-chain compliance platform whose carbon management module ("measure and reduce Scope 1–3 emissions") carries GHG Protocol methodology certifications from two certification bodies; customer stories use "GHG emissions reporting."
- **ICLEI ClearPath** — public-sector pole: an established emissions management platform for completing greenhouse gas inventories, forecasts, and climate action plans for U.S. local governments at community-wide or government-operations scale; relaunched generation powered by a planning-platform engine.
- **Watershed** — enterprise platform whose "carbon accounting" page defines the work as measuring the company's greenhouse gas emissions: data ingestion, factor assignment, anomaly detection, supplier engagement, disclosure formatting, and full calculation lineage.

These four span commercial and public-sector deployments, standalone product and suite-module postures, and enterprise and mid-market tiers. The sibling entry (Carbon Accounting Platform) additionally documents an enterprise suite module, an ESG data platform, and an SMB self-serve product from the same population.

The definition was checked against the practice the software digitizes — the accounting standard's own spreadsheet-style calculation tools and the prior generation of the public-sector tool sampled — so the core is not fitted to any one era, region, or vendor pattern.

## Sources

Research date: **2026-09-08**

- GHG Protocol — Corporate Accounting and Reporting Standard page (methodology definition, covered gases, calculation tools, project-accounting boundary, tools register): https://ghgprotocol.org/corporate-standard
- Watershed — "Getting started with carbon accounting": https://www.watershed.com/platform/measure/carbon-accounting
- Plan A — product site: https://www.plana.earth/
- Coolset — product site: https://www.coolset.com/
- ICLEI USA — ClearPath: https://icleiusa.org/clearpath/
- Emitwise — transition page (category naming across acquisition): https://www.emitwise.com/

> Sourcing limitation: no sampled product's help center or operational documentation was reachable this pass; all product claims rest on official product pages, and are stated only at the level those pages support. Two candidate products (Sweep, Carbon+Alt+Delete) could not be fetched and were excluded. Numeric limits, prices, factor counts, and plan-specific details are intentionally not stated; vendor-specific observations remain in the Research Notes. The pairing entry, Carbon Accounting Platform (researched 2026-09-07), carries the operational-depth evidence for the shared Type.

Detailed evidence, product-by-product observations, the cross-product comparison, and the leaf-boundary verdict (including the joint review this pass discharges) are recorded in the paired Research Notes.
