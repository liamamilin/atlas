# SOC Platform

## Overview

A **SOC Platform** (security operations platform) is a single product that unifies a security operations center's working machinery — the organization-wide security event data plane with continuous threat detection, case/incident management, and response automation — so that the full workflow from event ingestion through detection, triage, investigation, response, and closure runs in one system with shared data, shared entities, and one console.

It exists because the SOC's work was historically split across separate products: a SIEM for analytics and alerting, a case-management tool for incidents, and a SOAR for automation. The SOC Platform is the consolidation-era product that holds those layers natively as one designed system. Its unit of value is not any single layer but the unified workflow across them.

The boundary is structural: strip the automation and case layers and what remains is a SIEM; strip the data plane and detection and what remains is a SOAR plus a case tool sitting on someone else's analytics. The platform is defined by natively holding all of them together.

## Users & Context

The primary users are the members of a security operations team:

- **Tier-1 analysts** — work the alert queue: triage incoming alerts, close false positives, escalate real threats into cases
- **Tier-2/3 analysts and incident responders** — investigate cases: pivot across events, entities, and threat intelligence; drive response actions
- **Detection engineers** — author and tune the detection rules and analytics that run over the collected events
- **SOC managers** — watch queue health, response metrics, coverage, and reporting

Secondary users include threat-intelligence and hunting specialists working inside the same platform, compliance staff consuming its reporting, and — in a common variant — the platform operated by a managed security service provider on behalf of many customer organizations.

The work environment is a dedicated operations console used continuously through shifts; the platform is the system the SOC lives in, not a tool visited occasionally.

## Core Model

The platform's world is the union of its layers, operating on shared objects:

```text
Security event data plane (org-wide events, normalized and stored)
        ↓ runs
Continuous detection (rules / analytics / behavioral models)
        ↓ raises
Alerts  →  triaged into
Cases / Incidents (managed investigation and response records)
        ↓ driven by
Response automation (playbooks executing actions across tools and the environment)
        ↓ measured by
Operations metrics & reporting
```

### The defining structure

Four properties together make the product a SOC Platform:

- **Native data and detection layer** — the platform itself collects the organization's security-relevant events (endpoints, network, identity, cloud, applications, security products) and runs continuous detection over them. This is the SIEM's core, held inside the platform rather than integrated from a third party.
- **Native case/incident layer** — alerts become managed cases or incidents inside the platform: records that aggregate related alerts, entities, and evidence, carry severity and status, and persist the investigation and response history.
- **Native response automation layer** — playbooks and automation execute response actions — across the platform's own instrumentation and through integrations with external security tools — triggered by alerts, cases, or schedules, with runs recorded.
- **One unified system** — the layers share one data store, one entity model, and one console. The alert an analyst triages is detected by rules running on data the platform holds, in a case the platform manages, with automation the platform executes. This unity is what distinguishes the platform from a stack of separately purchased products.

### Standard capabilities of mature platforms

Mature products commonly add, on the same substrate:

- **Behavioral analytics (UEBA)** — baselines of normal user and entity behavior with risk scoring, catching threats rules miss
- **Threat intelligence** — ingestion and enrichment of external and internal indicators, feeding detection and investigation context
- **Threat hunting** — analyst-initiated proactive search over the platform's own telemetry
- **MITRE ATT&CK mapping** — detections and coverage organized against the tactic/technique framework
- **Entity and asset context** — profiles of users, devices, and assets used to prioritize risk
- **Compliance and operational reporting** — audit-relevant and management reporting produced from the same data

### One structure, many implementations

The layers are conceptual; products realize them with different emphasis:

```text
Concept:   data + detection layer
Forms:     dedicated security data plane; security layer on a shared log-analytics platform

Concept:   case layer
Forms:     first-class case/incident objects; investigation workflows built on the alert queue

Concept:   automation layer
Forms:     bundled SOAR product line; low-code automation integrated into the same console
```

## How It Works

The platform's operating loop is the SOC's daily cycle:

### Collect and detect

```text
Connect data sources (endpoints, network, identity, cloud, apps, security tools)
→ events stream in, are normalized and enriched
→ detection rules, analytics, and behavioral models evaluate continuously
→ alerts are raised with severity and entities
```

### Triage

```text
Analyst opens the alert queue
→ reviews alert context (entities, related events, intelligence, risk score)
→ closes false positives, or escalates into a case/incident
→ increasingly, AI agents perform first-pass triage with human oversight
```

### Investigate

```text
Case opened → related alerts, entities, and artifacts aggregated
→ analyst pivots across event history, entity profiles, and intelligence
→ investigation steps and findings recorded on the case
→ hunting and ad-hoc queries over the same data feed the investigation
```

### Respond

```text
Playbook triggered (from the case, an alert, or manually)
→ automated steps execute across connected tools and the environment
  (containment actions, enrichment, notifications)
→ human-approval gates where configured
→ actions and outcomes recorded back onto the case
```

### Close and measure

```text
Case closed with a recorded outcome
→ metrics accumulate (response times, volumes, dispositions)
→ coverage and posture reporting produced from the same data
→ detection rules tuned based on outcomes
```

The loop is continuous: tuning feeds detection, detection feeds triage, and the platform's shared substrate means every stage works on the same events, entities, and history.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Alert queue / triage console

The analyst's primary entry surface.

- lists current alerts with severity, entities, and risk indicators
- typical information: detection name, affected entities, related intelligence, ATT&CK mapping
- primary actions: triage (close / escalate to case), assign, enrich, pivot to investigation

### Case / incident workspace

The investigation surface for an escalated threat.

- case detail: timeline, related alerts, entities, artifacts, evidence, activity log
- primary actions: record findings, run or trigger playbooks, add tasks, collaborate, close with outcome

### Detection management

Where the platform's detection logic is authored and maintained.

- rule/analytics catalog with coverage views (commonly ATT&CK-mapped)
- primary actions: create/tune rules, enable/disable, review firing history

### Automation / playbook editor

Where response automation is authored.

- playbook list and editor, integration catalog for external tools
- primary actions: author/edit playbooks, configure integrations, review run history

### Search / investigation query surface

Direct query access to the underlying event data — used by both investigations and hunting.

- query interface over the normalized event store, saved searches, dashboards

### Dashboards and reporting

Management and compliance surfaces.

- queue health, response metrics, detection coverage, compliance reports

### Administration

Data-source onboarding, user/role management, tenant configuration (multi-tenant in the MSSP variant).

## Important Rules / Behaviors

- **The layers share one substrate.** An alert, its case, its automation runs, and the events behind them all reference the same data and entity model — this is what makes pivoting between stages immediate and is the platform's structural signature.
- **Cases persist the response record.** What was triaged, investigated, decided, and executed is retained on the case — the audit and learning record of the SOC's work.
- **Automation acts with configurable oversight.** Playbooks may execute containment automatically or stop at human-approval gates; the configuration is the operator's risk decision, and runs are recorded either way.
- **Detection is tunable content.** Rules and analytics are customer-maintained (or vendor-maintained content) over the customer's own data; tuning based on alert outcomes is a normal, expected loop.
- **Role-scoped access matters.** Analyst, responder, detection-engineer, and administrator roles see and do different things; in the multi-tenant variant, customer-organization boundaries are enforced structurally.
- **Data economics shape behavior.** What is ingested, how long it is kept, and at what query speed are first-class operational decisions in these products; retention and storage tiering are commonly configurable.

## Variants

- **Full-replacement platform** — the platform is the SOC's entire stack, replacing the separate SIEM/SOAR/case products (the dominant positioning)
- **Modular / augment-or-replace** — the platform's analytics and automation layers can run beside an existing third-party SIEM, with a path to full replacement
- **Platform-first** — security operations as one face of a broader log-analytics/observability platform sharing the same data plane
- **MSSP-operated** — the platform run multi-tenant by a managed security service provider serving many customer organizations
- **Self-hosted vs cloud-native SaaS** — cloud SaaS is the dominant current form; self-hosted lines persist in some portfolios
- **AI-analyst era** — most current products embed AI agents for triage, investigation summarization, and rule authoring; depth and autonomy vary widely and none of it is definitional

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| SIEM | substrate layer | The SIEM is analytics over the org's own event data — data plane + detection + investigation loop. The platform holds that core natively and adds case management and response automation as first-class layers. A SIEM stands alone; the platform unifies. |
| SOAR | automation layer | The SOAR's center is orchestration across external tools, without owning the org's data plane or detection. The platform owns the data plane and detection natively; its automation layer is one part of its own system. |
| Cyber Incident Response Platform | case layer | The standalone case-management Type for running incident response. The platform realizes the same case semantics natively as one layer among several. |
| XDR | detection/response product | XDR is the cross-domain detection-and-response product (vendor-curated telemetry, unified cross-domain incident, actuated response) feeding the operations layer; the platform is the whole-operations system over the org's own event plane. |
| Threat Intelligence Platform | integrated function | TI appears inside the platform as a native layer or integrated module; the standalone TIP manages and produces intelligence as its own Type. |
| Threat Hunting Platform | discovery layer | Hunting is a first-class capability inside most platforms; the hunting Type's defining loop (proactive analyst-initiated search with durable hunt records) coexists with the platform's alert-driven loop. |
| Log Management | adjacent substrate | Log management holds and searches logs without the security detection, case, and automation layers. |
| MDR (service) | delivery model | Managed detection and response is a service delivered on a platform or stack; it is an operating model, not this product Type. |

## Representative Products

- Securonix (Unified Defense SIEM)
- Exabeam (New-Scale Fusion Security Operations Platform)
- Devo (Security Data Platform)
- Sumo Logic (SIEM + Cloud SOAR on a shared log-analytics platform)

## Sources

Research date: **2026-09-10**

- Securonix — product and platform pages: https://www.securonix.com/ , https://www.securonix.com/products/platform-overview/ , https://www.securonix.com/products/siem-solutions/
- Exabeam — New-Scale Fusion platform pages: https://www.exabeam.com/product/ , https://www.exabeam.com/platform/exabeam-new-scale-fusion-security-operations-platform/
- Devo — platform pages: https://www.devo.com/ , https://www.devo.com/platform/
- Sumo Logic — security solutions page: https://www.sumologic.com/solutions/security/

> Sourcing limitation: Google Security Operations documentation was unreachable from the research environment (repeated timeouts) and is therefore not characterized in this document. Deep documentation portals (docs.exabeam.com, docs.devo.com) were not fetched; observations are official product-page level. Precise operational details (connector counts, retention defaults, pricing) are intentionally not stated. Detailed evidence, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
