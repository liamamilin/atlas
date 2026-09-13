# Research Notes — Public Health Surveillance Platform

## Research Goal

Understand, from real products, what a Public Health Surveillance Platform is: the software a public health authority uses to monitor disease and health events in its jurisdiction's population — how reports arrive, how cases/events are captured and classified, how the epidemiological picture is built, and how it feeds public health action and mandatory reporting.

## Initial Boundary

Initial hypothesis: this Type is the jurisdiction-level (national/state/regional/district health authority) counterpart of clinical and facility systems. Nearest neighbors:

- **Population Health Management** (§22, processed) — care organization's attributed/enrolled population; flagged by that pass for joint review.
- **Infection Prevention Platform** (§22, processed) — facility IPC program; its own doc states it is "not the public-health agency's population-level system (which it reports into)".
- **Emergency Management Platform** (§24) — response operations vs ongoing surveillance.
- **Public Alert & Warning System** (§24) — alerting the public vs alerting health staff.
- **LIS** (§22, processed) — lab results of record vs surveillance consumption.
- **Health Information Exchange** (§22, processed) — transport vs surveillance record.
- **Government Open Data Portal** (§24) — publishing vs operating surveillance.
- **Environmental Monitoring Platform** (§21) — environmental media vs human health events.

Unknowns going in: whether case-based and aggregate surveillance are one Type or two; whether outbreak-response tools (Go.Data-class) belong inside the Type or beside it; whether US state NEDSS-class systems fit the same core.

## Research Questions

1. What is the watched "population" — how is it scoped (jurisdiction vs enrolled panel)?
2. What enters the system (reports from whom: labs, providers, field investigators, community/media)?
3. What is the core record — individual case? aggregated count? event/signal?
4. How does classification work (case definitions, suspect/probable/confirmed, deduplication)?
5. What analysis surfaces exist (epi curves, maps, dashboards, statistics)?
6. How does the system feed action (alerts, thresholds, tasking, situation reports, upward reporting)?
7. Which capabilities are common vs variant (contact tracing, lab integration, EBS, One Health, mobile/offline)?
8. Where are the boundaries with the neighbors above?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different deployment scales — all open-source/global-good public-sector products, which is itself a finding about this market (see Uncertainties):

1. **SORMAS** (Surveillance Outbreak Response Management and Analysis System) — open-source ministry-level case-based surveillance + outbreak response platform; originated in the 2014 West Africa Ebola response, first deployed Nigeria 2015; used in 10+ countries across 5 continents.
2. **DHIS 2** (HISP/University of Oslo) — open-source national health information platform whose dedicated disease-surveillance capability is used in 40+ countries for integrated disease surveillance (aggregate + case-based + event-based).
3. **Go.Data** (WHO) — outbreak investigation tool for public health emergencies (case investigation, contact tracing, chains of transmission); included deliberately as the outbreak-response-emphasis boundary pole.

Rejected/considered: CDC Epi Info and CDC NEDSS/NSSP-class US systems (cdc.gov returned 403 on every attempt — recorded as sourcing limitation); WHO EWARS (page 404 ×2); commercial US state surveillance products (documentation not reachable this session).

## Sources

- SORMAS Foundation — https://www.sormas.org/ (home), /sormas/overview, /sormas/features — fetched 2026-09-10 (Tier 2, official product pages)
- DHIS2 — https://dhis2.org/ (home), https://dhis2.org/disease-surveillance/ — fetched 2026-09-10 (Tier 2, official product page; full body extracted)
- WHO Go.Data — https://worldhealthorganization.github.io/godata/ (home), /godata/outbreak-templates/ — fetched 2026-09-10 (Tier 1–2, official documentation site)
- WHO disease surveillance definition — quoted on the DHIS2 disease-surveillance page, citing https://www.who.int/emergencies/surveillance (Layer A for the definition as quoted; the WHO page itself not fetched)
- CDC Epi Info / NEDSS / NSSP — https://www.cdc.gov/epiinfo/... — 403 on all attempts (3 URLs), abandoned per network rules
- WHO EWARS — https://www.who.int/tools/ewars and alternate URL — 404 ×2, abandoned

## Product A — SORMAS

### Key observations (evidence layer A unless noted)

- Self-description (home): "a free and open-source digital platform for epidemic and pandemic preparedness and response. The system allows epidemiological disease surveillance (indicator- and event-based surveillance), early detection, and management of disease outbreaks."
- Overview: "a comprehensive surveillance, management, and analysis tool for infectious diseases that enables countries to monitor and control outbreaks effectively. With SORMAS, public health officials can track infection rates, manage cases and contacts, and access real-time statistics and data visualizations."
- Multi-institute coordination: "facilitates seamless communication and coordination among different public health institutes, such as hospitals, labs, and surveillance officers."
- Features page:
  - **Surveillance dashboard** — case data/statistics in real time; indicators calculated automatically; epidemiological curve of case counts over time broken into categories; case status map showing geographical distribution; dashboards available for cases, contacts and samples; exportable graphs.
  - **Infection chain visualization** — "key to assess the spread of diseases and support decision-making related to control measures."
  - **Environmental module** — One Health: environmental locations (water sources, wastewater facilities, forests) with samples and results tracked.
  - **Interoperability** — API through which SORMAS "automatically receive[s] sample test results from laboratories, citizen address databases or other surveillance systems."
  - **Mobile version** — Android app for field data collection by public health experts; offline use with sync when connectivity returns.
  - **Customizable user rights** — "over 170 different rights", "26 different standard user roles", fully customizable roles.
  - **40+ infectious diseases** — surveillance and outbreak management per disease (Ebola, cholera, measles, mpox, dengue…).
  - **Contact follow-up** — documenting tracing effort, developed symptoms, symptom onset; "identify possible infections early and initiate any required next steps."
  - **Statistical analysis** — situation reports from a wide range of indicators; charts, maps, tables; exportable.
  - Localization in 18+ languages.
- Overview "How it works": "Real-time, multidirectional data sharing with integrated task management that enables efficient coordination and structured communication."
- Ownership/security: data belongs to countries; GDPR-conformant concept (anonymization, pseudonymization, deletion); access per country-defined user rights.
- History: developed during the 2014 West Africa Ebola epidemic; first deployed Nigeria 2015; COVID-19 module 2020 drove adoption (France, Switzerland, Fiji, Côte d'Ivoire, Nepal, Germany…).

## Product B — DHIS2

### Key observations (evidence layer A unless noted)

- Disease-surveillance page (official product page):
  - Quotes WHO: "disease surveillance is the ongoing systematic collection, analysis, interpretation and use of health data. It is used as an early warning system to detect unusual disease patterns and possible outbreaks. Surveillance data also enables monitoring and evaluation of public health interventions, as well as providing routine epidemiological data to guide health program planning, priority setting and resource allocation." (Layer A for the definition as quoted on the page.)
  - "DHIS2 is used in more than 40 countries as a national scale platform for routine syndromic surveillance, case notification and case-based surveillance for notifiable diseases."
  - **Integrated disease surveillance (IDS)**: WHO framework combining Indicator-Based Surveillance (IBS) and Event-Based Surveillance (EBS).
  - **Aggregate and line-listed data in the same platform** (Data Entry and Capture apps); "During health emergencies or outbreaks, routine weekly surveillance can be adjusted to daily reporting."
  - **Case-based surveillance**: Tracker supports "case notification, investigation, linkage of lab results and case classification."
  - **Notifications, alerts & outbreak thresholds**: configure outbreak thresholds per disease and send alerts to health staff; immediate notification of a suspected case can trigger outbound messaging (messaging service, email, SMS, or interoperability with tools such as RapidPro).
  - **Standard reports / push analysis**: pre-defined daily/weekly/monthly surveillance bulletins automatically populated and pushed to user groups "at any level of the health system."
  - **Dashboards**: epi curves, case distribution and disease incidence on maps, surveillance indicators such as lab specimen adequacy — for epidemiologists, surveillance staff, and emergency operations centers.
  - **Event-based surveillance & rumor monitoring**: media/rumor/community sources scanned; signals triaged and verified by trained surveillance staff; Africa CDC customized DHIS2 as part of an event-based management system feeding WHO EIOS.
  - Emergency use: surveillance data as key source for Emergency Operations Centers; contact tracing; rapid response team rostering.
  - **Toolkits** (standards-based metadata): IDSR (WHO AFRO strategy; weekly indicator-based surveillance; metadata for 15 commonly notifiable diseases), case-based surveillance (WHO metadata for 9 vaccine-preventable diseases), acute febrile illness (CDC protocols), COVID-19, mpox (case-based and aggregate modalities).
  - One Health: zoonoses surveillance across sectors/ministries; climate data import for climate-sensitive disease analysis.
- Platform framing: DHIS2 is a general health information platform (HMIS, EMR, logistics, education…) — disease surveillance is one dedicated domain use of the same platform.

## Product C — Go.Data (WHO)

### Key observations (evidence layer A unless noted)

- Self-description (docs home): "Go.Data is an outbreak investigation tool for public health emergencies, and includes features for contact tracing, contact follow-up, and visualizing chains of transmission. Go.Data is designed to support outbreak responders and intended to be implemented alongside other systems for health surveillance, information management, and service delivery."
  - **Boundary evidence**: Go.Data positions itself *beside* surveillance systems, not as the standing surveillance platform — the outbreak-response pole of the space.
- **WHO Standardized Outbreak Templates**: activating an outbreak embeds "the relevant outbreak details and case investigation form structure already complete", aligned with WHO technical protocols (Outbreak Toolkit); templates for influenza with pandemic potential, yellow fever, mpox, cholera, Ebola, measles, SARS-CoV-2 — each with metadata overview and detailed data dictionaries aligned to published case report/investigation forms.
- Object model implied by docs and templates: **outbreak → case (case investigation form) → contact (contact listing/tracing/follow-up) → event; lab sample data importable; locations/facility registries configurable**.
- Analytics: dashboards plus connectors to Excel, R, Power BI, Tableau, Data Studio, Python, QGIS, ArcGIS.
- Interoperability toolkit: integration with HMIS/surveillance systems, lab sample import, mobile app integration, aggregate reporting to DHIS2 — documented as real-world patterns.
- Deployment: web + mobile app; demo sandbox; country/institution implementations.

## Cross-product Comparison

| Dimension | SORMAS | DHIS2 | Go.Data | Evidence |
|---|---|---|---|---|
| Watched unit | jurisdiction's cases/contacts/samples/events | jurisdiction's notifiable-disease data (aggregate + case) | one outbreak's cases/contacts/events | B |
| Core record | case (case-based), plus event-based surveillance | case record (Tracker) OR aggregated count (Data Entry) — both first-class | case + contact + event within an outbreak | B |
| Classification frame | disease configuration (40+ diseases) | case definitions / WHO-standard metadata (IDSR, VPD, mpox) | WHO outbreak templates per disease (case investigation forms) | B |
| Incoming reports | labs via API, field officers via mobile app | facilities/CHWs routine reporting, labs linked to cases, community/media for EBS | field investigators, lab sample import, mobile app | B |
| Analysis | dashboard, epi curve, case map, statistics module | dashboards, epi curves, maps, incidence, indicators | dashboards + external BI connectors (R/Power BI/QGIS…) | B |
| Action loop | task management, early detection, contact follow-up | outbreak thresholds → alerts (SMS/email/messaging); bulletins pushed to any level; EOC support | contact follow-up, chains of transmission for control decisions | B |
| Upward/outward reporting | situation reports, multi-institute coordination | surveillance bulletins at any level; regional bodies (WAHO, AFRO) | exports/interoperability into surveillance systems | B |
| Contact tracing | yes (follow-up view) | yes (COVID/emergency use; toolkit) | core feature | B — but absent in aggregate-only deployments → NOT definitional |
| Mobile/offline field capture | Android offline + sync | Android app | mobile app | B |
| Roles/permissions | 170+ rights, 26 standard roles | sharing/role model | user roles | B |
| Modality emphasis | case-based + event-based, outbreak response | aggregate (IBS) + case-based + EBS — full IDS span | outbreak investigation only | B |
| Scope posture | dedicated surveillance/outbreak platform | surveillance as one domain of a national HMIS platform | single-outbreak field tool | B |

## Canonical Model

### L0 — Defining Invariant (minimal)

A Public Health Surveillance Platform is a public health authority's system of record for watching disease and health events across its jurisdiction's population. Three jointly-held structures:

1. **The jurisdiction's health-event estate as the watched population.** Disease cases and public health events within a jurisdiction — held as records anchored to jurisdiction/geography (community, district, region, nation), not to an enrolled care population or a facility's patients. Remove → clinical registry / population health management / facility system.
2. **Health-event capture under the jurisdiction's surveillance frame.** Incoming reports (laboratories, providers, field investigators, community sources) are consolidated into managed records — individual case/event records or aggregated counts — classified against the authority's reportable-conditions and case-definition frame, with deduplication across reporters. Remove → raw data feed or lab-results store with no surveillance semantics.
3. **The epidemiological analysis-and-action loop.** The estate is continuously analyzed — trends, epi curves, geographic distribution, outbreak/threshold detection — and the results feed public health action: alerts to health staff, situation reports, tasking of response, and mandatory reporting upward (to national/international levels) and outward to decision-makers. Remove → data collection tool with no surveillance function.

Jointly-held is load-bearing: 1 alone = a demographic/geographic data warehouse; 2 without 1 = a registry with no jurisdiction frame; 3 without 1+2 = analytics over nothing; 1+2 without 3 = a case database nobody watches; 1+3 without 2 = reporting over unmanaged data.

### L1 — Common Mature Structure

- Laboratory result integration (electronic lab reporting / sample-result linkage)
- Outbreak thresholds, alerts and notifications (SMS/email/messaging)
- Dashboards, epi curves, case maps, statistics/situation-report generation
- Mobile (commonly offline-capable) field data collection with sync
- Role-based access control and multi-level (facility→district→national) organization
- Interoperability APIs / standards-based exchange
- Contact tracing and chains of transmission (outbreak-capable products)
- Event-based surveillance / rumor monitoring (signal triage and verification)
- Task management for response coordination
- Localization/multi-language
- Standard metadata/toolkits aligned to WHO/regional frameworks (IDSR-class)

### L2 — Variant / Optional Structure

- **Modality mix**: aggregate/indicator-based (IBS) vs case-based vs event-based (EBS) — a variant axis; mature national systems run several modalities in one platform
- **Syndromic surveillance** (e.g., emergency-department chief-complaint streams) — variant data substrate
- **One Health extension** — animal health and environmental surveillance (SORMAS environmental module; DHIS2 One Health) — variant scope
- **Outbreak-response emphasis** vs routine-surveillance emphasis (Go.Data pole vs DHIS2 pole)
- **Platform posture**: dedicated surveillance platform (SORMAS) vs surveillance as one domain of a national HMIS platform (DHIS2) vs single-outbreak field tool (Go.Data)
- Deployment: nationally hosted vs cloud; open source vs commercial; desktop epidemiology toolkit form (Epi Info-class, unverified this session)
- Emergency-mode behaviors: weekly→daily reporting cadence shift, contact tracing, RRT rostering, traveler/school screening

### L3 — Vendor-specific (Research Notes only)

- SORMAS: 40+ diseases, 170+ rights, 26 standard roles, 18+ languages, GDPR-conformant security concept, country data ownership, history (Ebola 2014 → Nigeria 2015 → COVID-19 module 2020), Digital Public Good / Global Good maturity status
- DHIS2: IDSR toolkit (15 notifiable diseases), VPD case-based toolkit (9 diseases), AFI toolkit, mpox toolkit, 7-1-7 targets, RapidPro integration, 55 countries using DHIS2 for COVID-19 surveillance, HISP network governance
- Go.Data: WHO outbreak templates per disease (influenza/yellow fever/mpox/cholera/EVD/measles/SARS-CoV-2) aligned to WHO protocols, sandbox resetting every two days, OpenWHO training, Community of Practice

## Vendor-specific Findings

See L3 above. None of these belong in the canonical core. The dominance of open-source global-good products in the reachable sample is itself a sampling artifact (commercial US state surveillance vendors were unreachable) — recorded under Uncertainties.

## Boundary Findings

| Neighbor | Relationship | Distinction / removal test |
|---|---|---|
| Population Health Management (§22, processed) | adjacent, most important | PHM watches a care organization's **attributed/enrolled** population and runs a stratify→gap→act→measure loop for care; this Type watches a **jurisdiction's** population for notifiable diseases/events and runs a detect→classify→analyze→report/act loop for public health action. Remove the jurisdiction/notifiable frame and add enrollment/attribution → PHM. (Discharges the PHM pass's flag: Arcadia's government use case still operates on enrolled populations — confirmed consistent from this side.) |
| Infection Prevention Platform (§22, processed) | adjacent, upstream/downstream | facility IPC program (its own surveillance criteria, its own infection registry) vs jurisdiction-level surveillance; the IPC platform **reports into** public health — that pass's own boundary statement confirms the seam |
| Emergency Management Platform (§24) | adjacent | ongoing surveillance/detection vs incident/response operations management; surveillance data feeds EOCs (DHIS2 evidence) but incident command is a different record world |
| Public Alert & Warning System (§24) | adjacent | alerts to health staff/authorities and upward reporting vs alerting the general public |
| LIS (§22, processed) | adjacent, feeder | lab results of record vs surveillance consumption; lab results flow in (SORMAS API, DHIS2 linkage, Go.Data import) but the lab owns the result |
| Health Information Exchange (§22, processed) | adjacent, substrate | transport/governed exchange vs the surveillance record built on received data |
| Government Open Data Portal (§24) | adjacent, output | publishing datasets vs operating the surveillance loop |
| Environmental Monitoring Platform (§21) | adjacent, One Health seam | environmental media monitoring vs human health events; environmental/animal surveillance inside this Type is a variant extension, not the core |
| Outbreak investigation field tools (Go.Data-class) | pole inside / beside the Type | Go.Data's own docs: "intended to be implemented alongside other systems for health surveillance" — a single-outbreak field tool without the standing jurisdictional estate sits at the Type's edge; when the standing multi-disease estate is absent, the product is drifting toward Emergency Management / field-response territory |

## Uncertainties

- **Commercial / high-income-market products under-sampled**: CDC-hosted systems (Epi Info, NEDSS, NSSP/ESSENCE) and commercial US state surveillance vendors were unreachable (cdc.gov 403 ×3; EWARS 404 ×2). The reachable sample is entirely open-source global-good public-sector products serving LMIC and European ministries. Claims are calibrated accordingly: no assertion is made about commercial-product feature depth, US syndromic-surveillance mechanics, or proprietary alerting algorithms.
- **Case-definition content depth** (exact case classification rules per disease) not researched — held at "case definitions / reportable-conditions frame" abstraction.
- **Whether a desktop epidemiology toolkit (Epi Info-class) satisfies the full core** could not be verified first-hand; held as an unverified variant form.
- **Precise operational details** (reporting deadlines, notification timeframes, threshold formulas) deliberately not asserted — none were directly evidenced.

## Final Synthesis

A Public Health Surveillance Platform is the public health authority's system of record for watching disease and health events across a jurisdiction's population. Its identity rests on three jointly-held structures: the jurisdiction's health-event estate (cases/events anchored to jurisdiction and geography, not to enrolled patients); health-event capture under the jurisdiction's surveillance frame (reports from labs, providers, field investigators and community sources consolidated into case/event records or aggregate counts, classified against reportable-conditions and case definitions, deduplicated); and the epidemiological analysis-and-action loop (trends, epi curves, geographic distribution, outbreak/threshold detection feeding alerts, situation reports, response tasking, and mandatory upward reporting). The defining core is deliberately modality-neutral: aggregate (indicator-based), case-based, and event-based surveillance are variant realizations of the same capture-and-watch structure, and contact tracing, lab integration, One Health scope, mobile/offline collection, and emergency-mode behaviors are common mature or variant capabilities, not identity. The Type's center of gravity is the jurisdiction: remove it and the product becomes a clinical registry or population health tool; remove the surveillance loop and it becomes a data collection pipeline; remove the public health semantics and it becomes generic epidemiological analytics.
