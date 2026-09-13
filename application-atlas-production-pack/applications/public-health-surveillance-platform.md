# Public Health Surveillance Platform

## Overview

A **Public Health Surveillance Platform** is a public health authority's system of record for watching disease and health events across its jurisdiction's population. It receives reports of notifiable conditions and public health events from laboratories, healthcare providers, field investigators, and community sources; consolidates them into managed case and event records — or aggregated counts — classified against the authority's case definitions; continuously analyzes the resulting picture for trends, geographic clustering, and outbreaks; and turns that picture into public health action: alerts to health staff, situation reports, response tasking, and mandatory reporting to higher levels of the health system.

The problem it solves is specific: an authority responsible for the health of a whole population must know, continuously and systematically, what diseases are occurring where, whether unusual patterns signal an outbreak, and what must be reported onward — under national and international reporting obligations. Clinical systems record care for treated patients; this system watches a jurisdiction.

Its boundary: it is not the care organization's enrolled-population tool (that is Population Health Management), not a facility's infection-control program (that is Infection Prevention, which reports *into* public health), not the laboratory's system of record (that is the LIS, whose results it consumes), and not incident-response operations management (that is Emergency Management, which it feeds).

## Users & Context

The primary users are the public health workforce of a jurisdiction — a ministry of health, a national or subnational public health institute, a state or district health department:

- **Surveillance officers and epidemiologists** — the core professional role. They review incoming reports, classify cases against case definitions, investigate signals, analyze trends and geographic distribution, and produce situation reports and surveillance bulletins.
- **Field investigators and community health workers** — collect case investigation data and contact information in the field, commonly through mobile apps that work offline and sync later.
- **Laboratory staff and systems** — submit test results that flow into case records, often automatically through interfaces.
- **Program managers and decision-makers** — read dashboards, epi curves, and bulletins at district, regional, and national levels; during emergencies, emergency operations centers consume the same data.

The work context is a standing public health operation: routine weekly (or daily, during outbreaks) reporting cycles, continuous signal review, case investigation and follow-up, and recurring reports to national and international bodies. The platform is typically operated by or for the authority itself — data ownership and hosting sit with the jurisdiction, and access is governed by role-based permissions because the records identify people and their health conditions.

## Core Model

### The Defining Core

```text
Jurisdiction (geographic/administrative frame)
└── Health-event estate (cases & events across the jurisdiction's population)
    ├── Case / event record (or aggregated count)
    │   ├── classified against case definitions (commonly suspect / probable / confirmed)
    │   └── fed by reports from labs, providers, field investigators, community sources
    └── Epidemiological analysis-and-action loop
        ├── trends, epi curves, geographic distribution
        ├── outbreak / threshold detection → alerts
        └── situation reports, response tasking, upward reporting
```

Three structures. If any one is removed, the product is no longer recognizable as a public health surveillance platform:

- **The jurisdiction's health-event estate.** The watched population is the jurisdiction's — everyone in a defined geographic and administrative area — not an enrolled panel of patients attributed to a care organization. Records are anchored to place (community, district, region, nation) because geography is how outbreaks are seen. Without the jurisdiction frame, the product becomes a clinical registry or a care-population tool.
- **Health-event capture under the surveillance frame.** Reports arriving from many sources are consolidated into managed records — an individual case or event, or an aggregated count for a period and area — classified against the authority's reportable-conditions list and case definitions, with duplicates from different reporters resolved to one event. Without this, the product is a raw data feed or a lab-results store with no surveillance semantics.
- **The epidemiological analysis-and-action loop.** The estate is not a static archive: it is continuously analyzed — epidemic curves, incidence over time, geographic distribution, comparison against outbreak thresholds — and the findings drive action: alerts to health staff, tasking of investigation and response, situation reports, and mandatory reporting upward to national and international levels. Without the loop, the product is a data collection pipeline nobody watches.

### Standard Capabilities

Mature products commonly add the following. They make the platform practical but do not define the Type:

- **Laboratory integration** — test results received electronically from laboratories and linked to the cases they concern.
- **Alerts and outbreak thresholds** — configurable thresholds per condition; when counts or signals cross them, notifications go to the responsible staff by email, SMS, or in-app messaging.
- **Dashboards and statistics** — epidemic curves, case maps, incidence indicators, and exportable situation reports; dashboards commonly cover cases, contacts, and samples.
- **Mobile field collection** — Android-class apps for field investigators, commonly usable offline with automatic sync when connectivity returns.
- **Role-based access control** — fine-grained permissions over who can see, edit, and delete records, organized by the jurisdiction's administrative levels (facility → district → region → national).
- **Interoperability** — APIs and standards-based exchange with laboratories, other surveillance systems, and national health information platforms.
- **Contact tracing and chains of transmission** — in outbreak-capable products: contact records linked to cases, follow-up documentation, and visualization of transmission chains.
- **Event-based surveillance** — scanning of community reports, rumors, and media for unusual events, triaged and verified by trained staff into signals.
- **Task management** — assigning and tracking response tasks across institutes (hospitals, labs, surveillance officers).
- **Localization** — multi-language support, since deployments span countries and regions.

### One Structure, Many Realizations

The core is written conceptually. The same structure is realized differently across the market:

```text
Concept:   Health-event record
Realizations:  individual case record (case-based surveillance)
               aggregated count per period/area (indicator-based surveillance)
               event/signal record (event-based surveillance)

Concept:   Surveillance frame
Realizations:  national notifiable-disease lists with case definitions
               WHO/regional standard metadata packages (IDSR-class)
               disease-specific outbreak investigation templates
```

A reader who encounters only one realization — say, a case-based national system — should still recognize an aggregate-reporting system or an event-based system as the same Type.

## How It Works

### Reports arrive and become records

```text
A case occurs (lab result, clinician report, field investigation, community signal)
→ the report enters the platform (electronic feed, manual entry, mobile app)
→ duplicates from different reporters are resolved into one record
→ the record is classified against the case definition
   (commonly suspect → probable → confirmed, as evidence accumulates)
→ the case/event joins the jurisdiction's estate
```

Consolidation and classification are the heart of the capture step: the same person may be reported by a laboratory and a hospital, and the authority needs one case, not two.

### The estate is watched

```text
Records accumulate per condition, place, and time
→ dashboards and reports compute the picture
   (epi curves, incidence, geographic distribution, indicators)
→ configured outbreak thresholds and anomaly signals are evaluated
→ when a threshold is crossed or a signal is verified,
   alerts go to the responsible health staff
```

During emergencies, the reporting cadence itself shifts — routine weekly surveillance can move to daily reporting — and the same platform carries the emergency picture.

### Findings become action

```text
Alert or verified signal
→ investigation opened (case investigation, contact listing and follow-up)
→ response tasks assigned across institutes
→ situation reports and bulletins produced and pushed
   to user groups at every level of the health system
→ mandatory reports compiled for national and international reporting
→ outcomes recorded back into the estate
```

The loop closes: what was learned in the field updates the records, and the updated records sharpen the next analysis.

### Core vs Common vs Optional

**Defining core** — without these, not a public health surveillance platform:

- jurisdiction-scoped health-event estate
- report consolidation and case-definition classification
- epidemiological analysis feeding alerts, reports, and response

**Standard capabilities** — present in most mature products:

- lab integration, alerts/thresholds, dashboards/epi curves, mobile offline collection, role-based access, APIs, contact tracing, event-based surveillance, tasking, localization

**Variant / optional** — depends on segment, geography, and posture:

- modality mix (aggregate vs case-based vs event-based emphasis)
- syndromic surveillance data substrates
- One Health scope (animal and environmental surveillance)
- emergency-mode extensions (rapid response team rosters, traveler screening)
- platform posture (dedicated surveillance product vs one domain of a national health information platform)

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Surveillance dashboard

The operations center's primary surface.

- real-time case statistics, automatically computed indicators
- epidemic curve over a selectable period, broken down by category
- case status map showing geographic distribution and clusters
- filterable by condition, geography, and time; exportable charts and tables

### Case / event register

The working list of the jurisdiction's cases and events.

- filterable, searchable list with classification status, condition, location, and dates
- primary actions: open a record, create a record, merge duplicates, classify, assign

### Case / event detail

The record of one case or event.

- person and location details, classification and its evidence, reported sources, lab results linked to the case, investigation form content, follow-up history
- primary actions: edit, classify, link lab results, record follow-up, attach documents

### Contact tracing view (outbreak-capable products)

- contacts linked to cases, follow-up schedule and symptom documentation, chains of transmission visualized for control decisions

### Statistics and reporting

- indicator selection, charts, maps, tables; generated situation reports exportable in common formats; pre-defined bulletins automatically populated and pushed to user groups

### Configuration / administration

- disease and condition configuration, case definitions, outbreak thresholds, organizational hierarchy, user roles and rights, integration settings

## Important Rules / Behaviors

### One case, many reporters

Reports about the same person and condition from different sources must resolve to a single case record. Deduplication is a structural behavior, not an optional cleanup — without it, counts double and outbreaks are misjudged.

### Classification is evidence-driven

A case's classification — commonly suspect, probable, and confirmed — changes as laboratory and clinical evidence accumulates, under the case definition in force. The classification is part of the record, and the record retains its history.

### The jurisdiction frame governs visibility

Records belong to places in the jurisdiction's administrative structure. Role-based access follows that structure: a district officer sees their district; a national epidemiologist sees the country. This makes the administrative hierarchy both an organizing structure and an access-control surface.

### Reporting obligations shape the output

Surveillance bulletins, situation reports, and upward reports are produced on defined cycles and pushed to defined user groups; during emergencies the cadence can shift from weekly to daily. The platform's reporting surfaces exist because the authority owes these reports to higher levels and to international bodies.

### Data protection is structural

The records identify people and their health conditions. Mature products carry anonymization/pseudonymization and deletion capabilities, and access strictly by defined user rights; data ownership and hosting responsibility rest with the jurisdiction's authorities.

## Variants

- **Aggregate / indicator-based systems** — weekly counts of notifiable conditions reported by facilities; the traditional backbone of national surveillance.
- **Case-based systems** — individual case records with investigation, lab linkage, and classification; the dominant form for outbreak-prone diseases.
- **Event-based surveillance** — community reports, rumors, and media scanned for unusual events, triaged into verified signals.
- **Integrated national platforms** — several modalities in one system, toggling between routine and emergency modes; surveillance as one domain of a broader national health information platform.
- **Outbreak-response-emphasis tools** — field investigation and contact tracing for a single outbreak, implemented alongside standing surveillance systems; when the standing multi-disease estate is absent, such a tool sits at this Type's edge, toward emergency-response territory.
- **One Health deployments** — the same platform extended to animal health and environmental sources for zoonotic and climate-sensitive disease surveillance.
- **Desktop epidemiology toolkits** — free desktop tools for outbreak investigation and analysis used by health departments (a form whose fit with the full core could not be verified first-hand in this research; see Sources).

## Related Application Types

| Application Type | Distinction |
|---|---|
| Population Health Management | watches a care organization's **attributed/enrolled** population and runs a stratify→gap→act→measure loop for care delivery; this Type watches a **jurisdiction's** population for notifiable diseases and events, for public health action |
| Infection Prevention Platform | a single healthcare facility's infection-control program with its own surveillance criteria and registry; it reports **into** public health rather than replacing it |
| Emergency Management Platform | manages incident response operations; this Type's ongoing detection and analysis feeds emergency operations centers, but incident command is a different record world |
| Public Alert & Warning System | alerts the general public; this Type alerts health staff and reports to authorities |
| Laboratory Information System (LIS) | owns the lab result of record; this Type consumes lab results as evidence feeding case classification |
| Health Information Exchange | transports clinical data between organizations under a trust framework; this Type builds and watches the surveillance record on data it receives |
| Government Open Data Portal | publishes datasets for public access; this Type operates the surveillance loop itself |
| Environmental Monitoring Platform | monitors environmental media (air, water); environmental and animal surveillance inside this Type is a One Health variant extension, not the core |

The most important boundary is with Population Health Management, because both "watch a population." The structural difference is the population and the purpose: an enrolled care population managed for care gaps versus a jurisdiction's population watched for notifiable disease and public health events.

## Representative Products

- **SORMAS** (Surveillance Outbreak Response Management and Analysis System) — open-source ministry-level surveillance and outbreak response platform; case-based and event-based surveillance across 40+ diseases; used in over 10 countries
- **DHIS2** — open-source national health information platform whose disease-surveillance capability is used in more than 40 countries for integrated disease surveillance (aggregate, case-based, and event-based)
- **Go.Data** (WHO) — outbreak investigation tool for public health emergencies (case investigation, contact tracing, chains of transmission), designed to run alongside standing surveillance systems

The core was checked against the paper-era predecessor of this Type — physician notifiable-disease reports reaching a health department by post or telegram, hand-maintained case ledgers, weekly morbidity tables, and monthly reports to the national level — which satisfies all three defining structures with no software at all, confirming the definition is not over-fitted to the current digital generation.

## Sources

Research date: **2026-09-10**

- SORMAS Foundation — official site, Overview and Features pages — https://www.sormas.org/ , https://www.sormas.org/sormas/overview , https://www.sormas.org/sormas/features
- DHIS2 — official site and Disease Surveillance page — https://dhis2.org/ , https://dhis2.org/disease-surveillance/
- WHO Go.Data — official documentation site and Outbreak Templates page — https://worldhealthorganization.github.io/godata/ , https://worldhealthorganization.github.io/godata/outbreak-templates/
- WHO disease surveillance definition — as quoted on the DHIS2 Disease Surveillance page, citing WHO's surveillance materials

> Sourcing limitation: CDC-hosted systems (Epi Info, NEDSS, NSSP) and WHO EWARS could not be reached from the research environment (repeated access failures), and commercial US state surveillance vendors were not reachable either. The reachable sample is therefore entirely open-source public-sector products serving ministries of health. Claims about commercial products, US syndromic-surveillance mechanics, and precise operational details (reporting deadlines, threshold formulas, notification timeframes) are deliberately not made in this document. Detailed observations and limitations are recorded in the paired Research Notes.
