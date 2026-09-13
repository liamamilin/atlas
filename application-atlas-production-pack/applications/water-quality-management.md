# Water Quality Management

## Overview

A **Water Quality Management** application is a water utility's system of record for its drinking-water quality program: it holds the utility's monitoring obligations as an executable program, collects and validates the water-quality data that the program produces, evaluates that data against drinking-water standards, and produces the compliance record — regulator-facing reports and consumer-facing disclosures — that demonstrates the water the utility delivers is safe and legal.

The defining core is small:

```text
Water-quality monitoring program of record
└── identified sampling locations bound to regulated parameters,
    applicable standards, and monitoring requirements
    └── water-quality data estate
        (lab results + field/instrument readings, validated and defensible)
        └── compliance evaluation and the regulator-facing record
            (limit evaluation → exceedance handling → periodic reports and submissions)
```

Everything else commonly associated with the category — scheduling automation, laboratory integrations, chain of custody, dashboards, GIS mapping, SCADA feeds, operations data — is widespread in current products but is not what makes the product a water-quality management system. The subject is always the utility's **own drinking water**: the water it produces and delivers, from source through treatment into the distribution system, which must meet drinking-water standards. When the watched subject shifts to the live condition of the pipe network, to the utility's effluent discharges, or to ambient environmental waters, the work belongs to a different Application Type.

## Users & Context

The primary user is the utility's **water quality administrator or compliance manager** — the person accountable for keeping the utility's public-water-system obligations current: which locations must be sampled, for which contaminants, how often, and whether every result is inside the applicable standard.

Working alongside them:

- **sampling and laboratory staff** — collect compliance samples, maintain chain of custody, and receive laboratory results back into the system
- **plant and system operators** — contribute operational and process readings (disinfectant residuals, turbidity-class parameters) and work from bench sheets
- **utility leadership** — consume compliance status through dashboards and reports

On the other side of the relationship sits the **regulator** — the state or national agency that reviews the analytical results the utility reports — and, for some artifacts, the **public itself**, which receives consumer-facing water quality reports.

The context is a regulated public water system: a municipal utility, a special district, or an investor-owned water company, from the smallest township system to the largest metropolitan utility. The rhythm of the work is set by monitoring schedules — recurring sampling obligations with deadlines — and by the constant possibility that a result exceeds a standard, which converts routine data management into an active response.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being a water-quality management system.

**1. The water-quality monitoring program of record.**
The utility's quality obligations held as structured configuration, not as documents. Each identified **sampling or monitoring location** — a source water intake, a treatment plant point, a distribution system site — is bound to the parameters or contaminants it is monitored for, the drinking-water standard or limit that applies to each, and the monitoring requirements that produce the required data: which parameters, at which locations, at what frequency. This program is the axis of the whole system: schedules, data, evaluations, and reports all hang off it.

**2. The water-quality data estate.**
The results the program produces, held persistently against location, parameter, and date: laboratory sample results (imported from the certified laboratory), field readings, and commonly instrument or SCADA feeds. Around the raw results sits the machinery that makes them **defensible** — data validation, audit trails, and preservation of both original and corrected values — because these records may be reviewed by a regulator or produced in an audit years later.

**3. Compliance evaluation and the regulator-facing record.**
Results are evaluated against the applicable standards — limit comparisons and averaging-class computations — and every exceedance, and every missed monitoring requirement, is surfaced as a compliance event to be handled: alerts, corrective actions, and the notifications the regime demands. The loop closes in the **reporting artifacts**: periodic operating reports to the regulator, consumer-facing water quality reports, and electronic submissions to state or national reporting systems, assembled from the validated data in the authority's required form.

```text
Monitoring program of record
  (locations × parameters × standards × requirements)
        ↓ produces
Water-quality data estate
  (lab results, field/instrument readings — validated, defensible)
        ↓ evaluated against
Standards / limits
        ↓ yields
Compliance events (exceedances, missed monitoring)
        ↓ resolved through
Corrective actions + notifications
        ↓ assembled into
Regulator-facing reports & submissions + consumer-facing reports
```

### Capabilities Shared by Mature Products

Mature products commonly carry most of these. They are not what makes the product a water-quality management system, but they make the program practical:

- **Monitoring schedules with automation** — recurring sampling events generated from the program, with reminders, task assignment, and flags for late or missing samples (a missed sample is itself a compliance failure)
- **Laboratory data integration** — electronic import of lab results (LIMS/EDD-class feeds), eliminating manual re-entry and its errors
- **Chain of custody** — the documented trail that accompanies a compliance sample from collection to result; some products make it a first-class tracked object
- **Bench sheets and computations** — guided calculation surfaces for operational readings and the averaging-class computations (running annual averages and similar) that compliance determinations require
- **Exceedance alerting** — notifications when results cross limits or arrive out of range
- **Dashboards, trends, and GIS mapping** — compliance status at a glance; results mapped across the distribution system
- **Mobile field collection** — sample collection and field readings captured on devices, offline-capable, synced to the estate
- **Permit and rule tracking** — the utility's permits and the rule-driven requirements behind the program, held where the schedule can reference them

### One Structure, Many Implementations

The core model is conceptual. Products realize it differently:

```text
Concept:  Monitoring program of record
Realizations:  rule-pack-driven schedules built in from drinking-water regulations;
               user-configured sampling plans; permit-linked requirements

Concept:  Data acquisition
Realizations:  laboratory EDD/LIMS import, mobile field collection,
               SCADA/instrument feeds (read-only), manual entry

Concept:  Regulator-facing record
Realizations:  preformatted operating reports, consumer confidence reports,
               electronic submissions to state/national portals
```

A reader who has only seen one implementation — say, a US rule-pack product — should still be able to recognize a utility running its quality program on configured schedules and manual lab entry: the core is the same.

## How It Works

### Build and maintain the program

```text
Define monitoring locations (source, treatment, distribution)
→ bind parameters and applicable standards to each location
→ set monitoring requirements (which parameters, how often)
→ the system generates the recurring sampling schedule
→ adjust as regulations or the system's configuration change
```

This is configuration work done once and maintained, and it is what turns regulations into an executable calendar.

### Run the sampling cycle

```text
Schedule surfaces upcoming sampling events
→ staff collect samples (mobile capture, chain of custody recorded)
→ samples go to the certified laboratory
→ results import electronically (or are entered)
→ data is validated; anomalies flagged
→ results land against location, parameter, and date
```

The cycle repeats on the schedule's rhythm — weekly, monthly, quarterly, annually, depending on the parameter and the regime. Missing it is not a neutral event: the system flags late or missing samples because monitoring failures are themselves violations.

### Evaluate and respond

```text
Results are compared against applicable standards
→ inside limits: the compliance record accumulates
→ exceedance (or missed sample): alerts fire
→ corrective actions are assigned and tracked
→ regime-required notifications are prepared and issued
→ the event and its resolution become part of the record
```

Response duties escalate with the severity of the event — from routine corrective action to urgent public notification when the water itself may pose a risk. The system's role is to make sure nothing is discovered late and nothing goes undocumented.

### Report

```text
Reporting period closes
→ the system assembles the report from validated data
  (operating report to the regulator; consumer report to the public)
→ staff review and certify
→ submission (paper, or electronic to state/national portals)
→ deadlines tracked for the next cycle
```

Reporting is the loop's payoff: the same data estate that drives daily alerts is assembled, in the authority's required form, into the artifacts that demonstrate compliance.

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- monitoring program of record (locations, parameters, standards, requirements)
- water-quality data estate with validation and defensibility
- compliance evaluation with exceedance handling
- regulator-facing reports and submissions

**Common mature structure** — present in most modern products:

- schedule automation with late/missing-sample flags
- laboratory data integration
- chain of custody
- bench sheets / averaging computations
- exceedance alerting
- dashboards, trends, GIS mapping
- mobile field collection
- consumer-facing report generation

**Variant / optional** — depends on scale, regime, and product philosophy:

- operations-data breadth (daily rounds, process data, preventive maintenance)
- permit lifecycle tracking
- customer-complaint tracking as a quality signal
- instrument/QC calibration management
- AI-assisted anomaly and missing-sample detection
- companion programs (backflow prevention, pretreatment, stormwater) sold as sibling products

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Monitoring program / sampling schedule

The program's control surface.

- locations with their parameters, standards, and frequencies; upcoming and overdue sampling events
- primary actions: configure locations and requirements, generate schedules, assign sampling tasks

### Data review / validation

Where results become records.

- imported lab results, field entries, and instrument feeds; out-of-range and suspect-value flags; original vs corrected values with audit trail
- primary actions: validate or correct results, flag for review, preserve history

### Compliance status / exceedance view

The system's answer to "are we compliant right now?"

- evaluations against standards, open exceedances, missed-monitoring failures, notification status
- primary actions: acknowledge, assign corrective action, prepare notifications

### Reporting surface

- report templates per authority and artifact type; period selection; assembled drafts for review and certification; electronic submission and deadline tracking
- primary actions: generate report, review, certify, submit

### Dashboards / maps

- compliance posture over time; results and sampling points on the system map; trends by parameter or zone
- primary actions: filter, drill into locations and results, export

### Administration

- rule and limit configuration, user roles, laboratory and SCADA connections, historical data migration

## Important Rules / Behaviors

### The schedule is a compliance instrument

Monitoring requirements are not reminders; they are obligations. A missed or late sample is itself a violation in most regimes, which is why mature products flag missing samples with the same seriousness as exceedances.

### Defensibility governs the data estate

Compliance data may be reviewed by regulators or produced in enforcement contexts years after collection. Hence the standard machinery: audit trails, validation workflows, and preservation of original values alongside corrections. Silent overwriting of a result is the cardinal sin of this data estate.

### Evaluation rules are configured, not improvised

How results combine into a compliance determination — which average over which period, which percentile, which comparison — is defined by the applicable regulation and configured into the system. The system computes; it does not invent the rule.

### Exceedances trigger duties beyond the record

An exceedance is not just a red cell: regimes attach notification and corrective-action duties to it, escalating with the risk to public health. The system tracks these duties as part of the event, not as a separate to-do list.

### The consumer is sometimes the audience

Unlike most compliance records, one artifact — the consumer confidence report class — is addressed to the public. Products that serve full drinking-water programs generate it from the same data estate as the regulator-facing reports.

### SCADA is a guest, not the host

Operational instrument feeds enter as data sources, commonly read-only, deliberately separated from control systems. The quality program holds records; it does not run the network — that distinction belongs to the operations side.

## Variants

- **Pure-play compliance automation** — the SDWA-style rule packs, electronic submissions, and schedule automation are the product's center; operations data is peripheral
- **Compliance + operations data management** — the same core wrapped in plant operations: daily rounds, process data, bench sheets, maintenance tracking; common in products that grew out of plant data systems
- **Platform app** — the quality program as one application on a broader environmental-data platform, sharing a validated analytical corpus with sibling water apps
- **Scale variants** — from the smallest township system (simple configured schedules, manual lab entry) to the largest investor-owned utility (multi-system roll-ups, GIS integration, historical data migration)
- **Regime variants** — the structure generalizes across national drinking-water regimes; the sampled evidence is US-centered (SDWA rule families, state primacy submissions), with other regimes realized as different rule packs and report formats over the same core
- **Companion programs** — backflow prevention and cross-connection control, industrial pretreatment, and stormwater programs are commonly sold as sibling products by the same vendors; they manage obligations toward external parties or other media rather than the utility's own water quality record

## Related Application Types

| Application Type | Distinction |
|---|---|
| Water Network Monitoring | watches the **live condition** of the distribution network (pressures, flows, quality signals) and drives leak/burst/quality **events** to field response; this Type holds the quality **program** — schedules, compliance determinations, reports. The real-time quality signal lives there; the compliance record lives here |
| Wastewater Compliance Management | the effluent twin: same compliance-monitoring grammar, but the subject is the utility's (or a discharger's) **discharge** under discharge permits, reported through discharge-monitoring artifacts — not the drinking water delivered to customers |
| Environmental Water Monitoring | observes **ambient/receiving waters** as an environmental observation loop, without the utility's compliance program semantics |
| Environmental Laboratory Management | the laboratory's sample→analysis→deliverable workflow; the lab is the measurement instrument whose results this Type consumes |
| Environmental Data Platform | the validated long-term analytical corpus; this Type is the compliance program that produces and consumes portions of it |
| Environmental Compliance Management | the obligation register + conformance loop over legal requirements; this Type centers the operational monitoring program and its data, not the obligations register |
| Water Utility Management | the customer-service business system (accounts, charges, bills); no object overlap with the quality program |
| SCADA | control/telemetry machinery with point semantics; appears here only as a read-only data source |

The closest boundary is with Water Network Monitoring, because both touch water quality. The structural test: if the work is about the **network's operating condition and events**, it is network monitoring; if it is about the **program of record that proves the water meets standards**, it is this Type.

## Representative Products

- **WaterTrax / Hach WIMS / WIMS Rio** (Aquatic Informatics) — water-sector specialist family serving drinking-water and wastewater compliance data for utilities and agencies
- **Locus Drinking Water Quality** (Locus Technologies) — drinking-water compliance as an app on an environmental-data platform, from small townships to investor-owned utilities
- **SAMS Water** (NJBSoft) — pure-play drinking-water compliance automation with built-in rule packs and electronic state submissions

Naming note: the market label "water quality management" is also used by EHS-suite products for **discharger-side** water compliance (e.g. Intelex's product of the same name, oriented to discharge permits and discharge monitoring reports). That sense belongs to the wastewater-compliance sibling Type; it is recorded here as a boundary, not as a member.

## Sources

Research date: **2026-09-10**

Primary vendor surfaces (product/solution pages):

- Aquatic Informatics — Drinking Water solution: https://aquaticinformatics.com/solutions/applications/drinking-water-data-management/
- Aquatic Informatics — WIMS Rio: https://aquaticinformatics.com/products/water-compliance-operations-solution-rio/
- Locus Technologies — Water Data Management: https://www.locustec.com/applications/water-data-management
- Locus Technologies — Drinking Water Quality: https://www.locustec.com/applications/environmental-information-management/drinking-water-quality/
- NJBSoft — SAMS Water: https://njbsoft.com/sams-water/

Regulatory substrate:

- US EPA — SDWA Compliance Monitoring: https://www.epa.gov/compliance/safe-drinking-water-act-compliance-monitoring
- US EPA — Public Notification Rule: https://www.epa.gov/dwreginfo/public-notification-rule
- US EPA — Online Water Quality Monitoring Resources (OWQM-DS guidance): https://www.epa.gov/waterresilience/online-water-quality-monitoring-resources
- Arizona ADEQ — EPA CMDP compliance-data portal: https://azdeq.gov/CMDP

Inherited evidence: WaterTrax and Hach WIMS product-page observations were fetched in the wastewater-compliance-management research pass (2026-09-10) and are recorded in the paired Research Notes.

> Sourcing limitation: no Tier-1 help-center or user-manual documentation was reachable for any sampled product; all product evidence is product/solution-page level. Precise operational details (per-rule averaging windows, exact report formats, numeric thresholds, workflow states) are intentionally not stated in this document; they remain in the Research Notes. Non-US drinking-water regimes are reasoned from the regulatory structure rather than directly sampled.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the naming-collision resolution are recorded in the paired Research Notes.
