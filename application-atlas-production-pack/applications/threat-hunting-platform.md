# Threat Hunting Platform

## Overview

A **Threat Hunting Platform** is a security operations system that lets trained analysts proactively search an organization's security telemetry for malicious activity that automated controls have not surfaced — and turns that search effort into durable records whose findings feed incident response and detection engineering.

The problem it solves is specific: scheduled detection rules, correlation logic, and automated detectors only catch what they have been written to catch. An attacker who evades those controls produces no alert. Threat hunting is the discipline of looking anyway — starting from a hypothesis, an indicator, an anomaly, or a known coverage gap, and interactively interrogating the environment's data until the question is answered. The platform is the software that makes this discipline practical and institutional: it holds the data in a queryable form, gives the analyst search and investigation machinery, and remembers what was done so the organization keeps the benefit.

The defining core is small:

```text
The organization's security telemetry (searchable substrate)
└── Analyst-initiated proactive search
    (hypothesis / indicator / anomaly / coverage gap → iterative query → pivot → evidence)
    └── Durable hunt records → findings escalate into cases & incidents
        (and, in mature products, into new detection rules and intelligence)
```

When the starting point is a detection-generated alert and the record is the alert's lifecycle, the system is operating as a SIEM; when the substrate is collected endpoint telemetry with automated prevention, that is an EDR/XDR. Threat hunting is the layer where the analyst, not a rule, starts the search — and modern security platforms increasingly carry all of these loops side by side.

## Users & Context

The primary users are security specialists, not general IT staff:

- **Threat hunters and senior security analysts** — formulate hypotheses, run and refine searches, capture evidence, and decide whether what they found is a real adversary or noise.
- **Detection engineers** — consume proven hunting queries and turn them into permanent detection rules; use hunting to find coverage gaps in the rule set.
- **Incident responders / DFIR specialists** — use hunting to establish scope during and after an incident (has this attacker touched other hosts?).
- **SOC managers / program owners** — in some products, track the hunting program itself: hypotheses validated, incidents created, detections produced.

The work context is a security operations center (SOC) or an equivalent internal security team. Hunting runs continuously or on a cadence alongside alert triage: analysts hunt when new threats are disclosed, when anomalies catch their attention, when they want to verify coverage of a technique, or as scheduled proactive work. Everything the analyst sees is the organization's own environment — hunting platforms do not scan the internet or test controls; they examine the telemetry the organization already collected about itself.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the product collapses into a different type.

**1. The organization's security telemetry as the searchable substrate.** The platform's foundation is a large, persistent body of security-relevant event data about the environment: endpoint process and file activity, network traffic and DNS, authentication and directory events, cloud control-plane activity, email flows, and the alerts other security tools have already raised. The data is held in a form an analyst can interactively query — filtered, aggregated, joined, and drilled into — across time ranges that reach back before "now". How the data arrived is a variant, not a definition: some platforms collect telemetry with their own agents and services, others ingest logs from third-party sources, many do both.

**2. Analyst-initiated proactive search.** The search starts from the analyst's mind, not from an alert queue: a hypothesis ("if an attacker had credential-dumped on a domain controller, what would that look like in our logs?"), a new external indicator, an anomaly that never warranted an alert, or an uncovered attacker technique. The analyst then iterates: run a query, read the results, narrow or widen the filter, pivot from a suspicious user to that user's hosts to those hosts' network connections, change the time window, and try again. The platform exists to make this iteration fast and to preserve the analyst's context while they work.

**3. Durable hunt records with promotion outcomes.** Hunting that evaporates when the session ends is just searching. The platform records the effort — hunts or investigations as named, persistent objects; evidence captured from results (rows preserved together with the query and time range that produced them, notes, tags, pinned events); saved queries and reusable starting points. Findings escalate into cases and incidents for response, and — in mature products — proven hunting queries are promoted into scheduled detection rules so the same activity alerts automatically next time. This record layer is what distinguishes a hunting *platform* from a bare search console, and it is what makes hunting an organizational capability instead of a personal habit.

### Standard Capabilities

Mature products commonly add, without these being what defines the type:

- **Hunting query library** — out-of-the-box hunting queries authored by the vendor's security researchers, shipped and updated as content, each describing the behavior it hunts and the data it needs. A starting point for analysts who don't know where to begin.
- **Adversary-technique mapping** — organizing hunting content by attacker-behavior frameworks (MITRE ATT&CK-class tactics and techniques), including views that show which techniques have hunting coverage and which are gaps.
- **Result-change signals** — comparing query result volumes across time windows to highlight spikes and new activity worth a look.
- **Entity-centric investigation** — entity pages and graphs that gather everything known about a user, host, or IP in one place; process trees and session views that reconstruct what happened before and after an event.
- **Threat-intelligence integration** — indicator lists from intelligence feeds, cross-referenced against hunting results; the ability to push a hunt finding back into the organization's indicator store.
- **Promotion into detection content** — turning a validated hunting query into a scheduled detection rule with the query logic carried over.
- **Live endpoint interrogation** — querying running hosts from within the hunting context to confirm or rule out compromise (documented at some, not all, of the researched products).
- **Notebook / data-science depth** — programmable analysis environments for hunts too complex for query consoles (present in some products).
- **AI assistance** — natural-language query generation, result summarization, and cross-alert pattern correlation (era-current, spreading quickly).
- **Permissioned surfaces** — role-based access control over who can query which data and use which hunting features.

### One Structure, Many Implementations

The core is written conceptually; products realize each concept differently:

```text
Concept:        Searchable security telemetry
Implementations: logs ingested from many sources (SIEM pattern)
                 telemetry collected by the platform's own agents/services (XDR pattern)
                 both combined

Concept:        The hunt record
Implementations: named hunts with hypothesis states and status (one pattern)
                 saved investigation timelines with notes (another pattern)
                 structured investigations attached to findings (another pattern)

Concept:        Evidence capture
Implementations: bookmarks that preserve rows + query + time range
                 pinned events and attached notes
                 events added to an investigation file

Concept:        Escalation outcome
Implementations: new incident / added to existing incident
                 case in the platform's case system (with ticketing integration)
                 structured investigation with response plans
```

## How It Works

The canonical loop:

```text
1. Start the hunt
   hypothesis / new threat / anomaly / ATT&CK coverage gap
   → optionally pull starter queries from the hunting library

2. Search and iterate
   run queries over the telemetry
   → read results → narrow, widen, re-shape the query
   → pivot across entities (user → host → network → process) and time
   → compare result volumes against earlier windows to spot spikes

3. Capture evidence
   preserve the result rows that matter together with the query
   and time range that produced them
   → tag, annotate, attach notes
   → accumulate the evidence trail of the hunt

4. Escalate what's real
   collected evidence → new incident, or added to an existing one
   → entities enriched or registered as threat indicators
   → response handed to the incident-response workflow

5. Institutionalize
   hypothesis validated or rejected — recorded
   proven hunting queries → scheduled detection rules
   → the same activity alerts automatically next time
   → hunt closed; the program's metrics retain the outcome
```

Three flows deserve emphasis:

**Starting points are plural.** A hunt can begin from a hypothesis the analyst formed, from a new threat campaign in the news, from an anomaly in the data, or from a systematic walk of the adversary-technique map looking for detection coverage gaps. Mature products support all of these with content: researcher-authored hunting queries, campaign-specific content packs, and technique-mapped query collections.

**The iteration is the work.** Unlike alert triage, nothing tells the analyst when to stop; the hunt proceeds under the analyst's control until the hypothesis is validated, rejected, or abandoned. The platform's contribution is speed (query languages tuned for event data, fast pivots from any result field, persisted query tabs that survive navigation) and memory (bookmarks, notes, saved timelines) — so that hours of exploration don't collapse when the session ends.

**The outcome is institutional.** A hunt ends with recorded outcomes: an incident opened with the evidence attached, a hypothesis marked validated or not, and — the highest-value outcome — a hunting query promoted into a detection rule so the discovered behavior alerts forever after. Some products track the program at this level (validated hypotheses, incidents and detections produced by hunting), treating hunting as a measurable discipline rather than an ad-hoc activity.

## Interfaces

Described conceptually; layouts and names vary by product.

### Hunting console / query workspace

The primary surface: a query editor and results table over the security telemetry.

- typical information: query text, time range, result rows with event fields, result counts, sometimes result-volume change indicators
- primary actions: write/run/refine queries, switch data sources or schemas, save the query, persist multiple query tabs, capture results as evidence

### Hunting query library

Where starting content lives.

- typical information: available hunting queries with descriptions, required data sources, result counts, technique/tactic mappings
- primary actions: run, run in bulk, filter by technique or data source, favorite, clone and customize, create from scratch

### Hunt / investigation record

The persistent container for one hunting effort.

- typical information: name, description/hypothesis, owner, status, linked queries, captured evidence, related incidents and detection rules
- primary actions: create hunt, add queries, run queries within the hunt, add evidence, comment/collaborate, update hypothesis state, close

### Investigation / timeline surface

Where results are explored visually and contextually.

- typical information: event sequences in time order, entity relationships, process trees, alert context
- primary actions: pin events, add notes, build correlations across event categories, open an entity page, attach the whole investigation to a case

### Entity page / graph

Everything known about one user, host, or other entity.

- typical information: the entity's activity timeline, related alerts and anomalies, risk indicators
- primary actions: pivot to related events, launch enrichment actions, register the entity as an indicator

### Case / incident escalation

The hand-off surface into response.

- typical information: evidence attached, severity, owner, response state
- primary actions: create incident from evidence, add evidence to an existing incident, integrate with external ticketing

### Program metrics (some products)

Where hunting program performance is tracked.

- typical information: validated hypotheses, incidents created from hunts, detection rules created from hunts, open/closed hunts
- primary actions: review trends, set program goals

## Important Rules / Behaviors

**Hunting observes first; response is handed off.** The hunting loop's job is discovery and evidence; containment, remediation, and enforcement belong to the incident-response and endpoint-protection sides. Even where a hunting surface can trigger actions on hosts or entities, the defining flow ends in escalation, not enforcement.

**Hunt records outlive sessions.** Evidence captures preserve not just the result rows but the query and time range that produced them — the reproducibility of a finding is part of the evidence. Peers can re-run, verify, and extend another analyst's hunt.

**Findings are provisional until dispositioned.** Unusual results are often benign; the escalation flow deliberately includes the possibility of concluding "not malicious" and closing the hunt with the hypothesis recorded as rejected — a legitimate, tracked outcome, not a failure.

**Promotion converts hunts into detections.** A hunting query that proves valuable is converted into a scheduled detection rule; the query logic carries over, and the hunt record and the new rule are linked. Hunting is thereby the discovery mechanism that feeds the SIEM's detection layer.

**Data availability bounds the hunt.** A query can only return what was collected and retained: hunting queries show which data sources they need, queries against unconnected sources are inert, and query windows and volumes are subject to retention and quota limits that vary by product and data tier.

**Hunting is permissioned.** Analysts query only the data their roles allow; hunting surfaces are access-controlled features in their own right. This follows from the data's sensitivity: security telemetry frequently contains the organization's most sensitive activity records.

**Hunting complements, never replaces, detection.** The platform's own framing treats hunting as the proactive layer *around* automated detection: detection rules keep watch continuously; hunting looks where no rule is watching yet, and closes the gap by creating rules.

## Variants

- **Packaging** — the dominant market shape: hunting as a first-class layer inside a SIEM, XDR, or EDR platform, sharing its data, cases, and detection engine. Also seen: standalone hunting products, and hunting delivered as a managed service performed by the vendor's analysts (this service variant was not verifiable in the researched sample and is noted without operational detail).
- **Substrate ownership** — telemetry ingested from third-party sources (SIEM pattern) vs collected by the platform's own agents and services (XDR pattern) vs both in one workspace.
- **Query language** — each product exposes its own query language(s) for hunting; fluency in the language is a real skill requirement for users. Some products offer multiple languages (e.g., filter-style, sequence/correlation-style, and pipe-style).
- **Analyst depth** — query-console hunting vs notebook/data-science hunting (programmatic analysis, ML libraries) for complex investigations.
- **Execution model** — self-service hunting by the customer's analysts vs AI-assisted hunting (query generation, alert correlation) vs managed hunting by the vendor.
- **Program maturity** — ad-hoc hunting from the query console vs managed hunting programs with named hunts, hypothesis states, metrics, and goals.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| SIEM | closest neighbor, sharpest seam | SIEM's record is the detection-generated alert/finding and its loop is rule → alert → triage → response; hunting's record is the analyst-initiated hunt and its loop is hypothesis → search → evidence → escalation. Modern SIEMs embed hunting as a layer; the two loops coexist with separate records and vocabularies. Remove proactive analyst-initiated search → SIEM. |
| EDR / XDR | substrate and responder | EDR/XDR collects endpoint telemetry, auto-detects, and can take response actions; hunting is the proactive exploration layer over that (and other) telemetry. Remove collection + automated prevention/response → hunting layer; remove proactive search → EDR. |
| NDR | telemetry sibling | NDR detects from network telemetry; hunting is the proactive search discipline across all telemetry, network included. |
| Log Management / Observability | substrate without security semantics | Raw log search has the data and the query languages but no security entities, no detection content, no hunt records, no escalation/promotion machinery. Remove security hunting machinery → log analytics. |
| Threat Intelligence Platform | consumer/producer handshake | TIP manages external intelligence (feeds, indicators, reports); hunting consumes intelligence as starting points and matching targets, and can register hunt findings as new indicators. TIP's object is intelligence; hunting's object is the environment's telemetry. |
| SOC Platform / Cyber Incident Response Platform | downstream consumer | Those orchestrate workflow, cases, and response after discovery; hunting is the discovery layer that feeds them. Case management inside some hunting-adjacent products is convergence, not identity. |
| Digital Forensics Platform | different scope and standard | Forensics is deep, evidence-grade examination of specific hosts/artifacts, usually post-incident; hunting is broad, proactive, environment-wide search before an incident is known. |
| Vulnerability Management / Attack Surface Management | different phase | Those manage pre-compromise exposure; hunting looks for post-compromise adversary activity. |
| Deception Platform | trigger relationship | Deception plants decoys that generate high-fidelity alerts; hunting is human-initiated search. Deception output can spark a hunt. |
| Security Validation Platform | synthetic vs actual | Validation executes emulated attacks to test controls; hunting searches real telemetry for real adversary activity. |

## Representative Products

- Microsoft Sentinel (hunting and hunts) — cloud SIEM with a dedicated hunting program layer
- Elastic Security — search-native SIEM/XDR with investigation-timeline hunting
- Splunk Enterprise Security — classic SIEM whose hunting runs on its search substrate and investigation workflow
- Microsoft Defender XDR (advanced hunting) — XDR pole: proactive KQL hunting over vendor-collected telemetry

Research-adjacent market anchors (named for orientation; not researched in this pass): CrowdStrike Falcon (endpoint-first hunting + managed hunting service), Google Security Operations (cloud data-lake search hunting), Vectra AI (automated/AI-driven hunting posture).

## Sources

Research date: **2026-09-09**

Official product documentation (all fetched full-text on 2026-09-09):

- Microsoft Sentinel — Hunting capabilities in Microsoft Sentinel — https://learn.microsoft.com/en-us/azure/sentinel/hunting
- Microsoft Sentinel — Conduct end-to-end threat hunting with Hunts — https://learn.microsoft.com/en-us/azure/sentinel/hunts
- Elastic Security — solution overview / investigate / Timeline — https://www.elastic.co/docs/solutions/security , https://www.elastic.co/docs/solutions/security/investigate , https://www.elastic.co/docs/solutions/security/investigate/timeline
- Splunk Enterprise Security 8 — About / Mission Control overview — https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/introduction/about-splunk-enterprise-security , https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/mission-control/overview-of-mission-control-in-splunk-enterprise-security
- Microsoft Defender XDR — Advanced hunting in the Microsoft Defender portal — https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender

> Sourcing limitations: two of the five initially selected representative products could not be reached from the research environment — CrowdStrike's documentation portal (JavaScript-rendered, content not retrievable) and Google Security Operations documentation (repeated timeouts). They are held as market anchors only, with no operational claims made about them. The researched sample therefore includes two products from one vendor (different products, different hunting architectures); the cross-product claims in this document rest on the three-vendor evidence actually obtained. Precise operational details (retention windows, query quotas, exact state vocabularies, content-library sizes) are intentionally not stated; they are product-specific and recorded only in outline in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison, and the boundary analysis against SIEM / EDR / XDR / log management / threat intelligence / incident-response tooling are recorded in the paired Research Notes.
