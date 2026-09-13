# OT Security Platform

## Overview

An **OT Security Platform** is a security team's system of record for an industrial control environment — the networks of controllers (PLCs, RTUs, DCS), engineering and operator stations, HMIs, and historians that run physical processes in factories, utilities, energy, water, transportation, and building operations — and the engine of that environment's security loop.

These environments share a structural property that shapes everything the platform does: the systems being protected run physical processes where **availability and safety outrank containment**. Controllers cannot run security software, cannot be casually scanned, patched, or rebooted, and must never be disturbed by the tool that watches them. A security platform therefore builds its knowledge of the environment from the outside — by observing the control network itself — and evaluates what it observes against expectations of how a control system should behave.

The defining core is two structures held together:

```text
OT control-estate record
    (self-assembled from network observation, classified in OT terms)
└── Control-aware security detection
    (baselines + threat intelligence + change rules → asset-bound findings)
```

- Remove the estate record, and detection loses its subject — a protocol-aware sensor with no picture of the environment.
- Remove detection, and the record is an asset inventory.
- Remove the OT orientation — the control-process semantics and the must-not-disturb constraint — and the product is generic IT network security.

Everything else the category is known for — zone and Purdue-model mapping, vulnerability and exposure management, risk scoring, threat intelligence, compliance reporting, AI assistants — is mature structure that makes the platform effective, not what makes it an OT security platform.

## Users & Context

The primary user is the **security function responsible for the control environment**, which in practice spans two worlds that must work together:

- **OT security analysts and engineers** — triage alerts, investigate activity on control networks, tune baselines and detection rules, and judge whether an observed anomaly is a threat or a legitimate process change. In many organizations these people sit between the corporate SOC and the plant.
- **Control / automation engineers** — the owners of the process itself. They validate what the platform sees against process reality (is this new device a planned addition? is this controller state change maintenance?), because only they can make that call.
- **SOC analysts** in converged organizations — consume OT alerts through the same tools they use for IT, with the platform forwarding alerts and asset context into the SOC stack.
- **Compliance and risk owners** — consume the risk and compliance reporting the platform produces for the frameworks that govern industrial environments (IEC 62443, NERC CIP, NIS2, and sector regulators, depending on industry and geography).
- **Plant / operations management** — consume risk views and posture reporting at site and enterprise level.

The work context is an environment that was historically isolated and is now converging with IT: assets installed and maintained by vendors and integrators, invisible to endpoint tooling, often unpatchable, and critical enough that a wrong response is worse than a slow one. The platform is deployed once against that environment — collection points placed at network vantage points — and then operated continuously as a standing surface, not opened occasionally.

## Core Model

### The Defining Core

```text
OT control-estate record
    (controllers, stations, HMIs, historians, network devices
     + the communications between them)
└── Control-aware security detection
    (what should happen → what is observed → findings bound to assets)
```

**The OT control-estate record.** Every asset the platform sees is held as an individually identified record. Identity is anchored in network identifiers and enriched with OT-specific classification: what the device *is* in control terms (controller, engineering station, HMI, historian, network device), which industrial protocols it speaks, its vendor/model/firmware, and where it sits in the production structure (site, zone, line, process area). Crucially, the record is assembled *by the platform itself*: passive analysis of control-network traffic, carefully limited active queries where they are safe, and enrichment from systems that already know the assets (engineering files, asset databases, other security tools). No one enrolls a PLC the way a user enrolls a laptop. Mature products carry OT attributes that have no equivalent in IT inventories — a controller's operating state, whether a workstation is an engineering station that programs controllers, a device's level in the production hierarchy — because these attributes are what make security judgments about a control environment possible.

**Control-aware security detection.** The platform continuously evaluates observed activity against security expectations, along several lines that recur across products:

- **Baseline deviation** — the platform learns what normal control behavior looks like (which devices talk to which, using which protocols, on what schedule) and flags departures: an unexpected talker, an unusual command, a communication that appears where none existed.
- **Protocol semantics** — the platform understands industrial protocols deeply enough to detect messages that violate their specification or use commands in ways the process never does (for example, an unauthorized write to a controller register).
- **Change rules** — new or unknown devices, new communication relationships, and changes to controller configuration, firmware, or control logic are security-relevant by default until a human accepts them.
- **Threat intelligence** — known threats targeting industrial environments are matched against observed activity.

Every finding is bound to identified assets — which is what makes triage actionable. An alert is never "suspicious traffic"; it is *this engineering station wrote to that controller*, read against the estate record and the two assets' history.

Alongside security findings, mature platforms commonly surface **operational signals** — a device that stopped responding, a controller that left its running state — because in control environments a security compromise and an equipment failure present the same way at the observation point, and the platform is the only place both are visible.

### One Structure, Many Implementations

The core model is written conceptually. Products realize each concept differently:

```text
Concept:      OT control-estate record
Realization:  passive network sensors at taps/mirror ports; limited "safe"
              active queries; analysis of engineering project files;
              enrichment from asset databases and other security tools;
              network-anchored identity (address pairings, behavior)

Concept:      OT classification
Realization:  device role/type vocabularies; protocol identification;
              controller operating states; engineering-station designation;
              site/zone/process-area placement; production-level mapping

Concept:      Control-aware detection
Realization:  learned behavioral baselines; protocol-conformance rules;
              change/new-device rules; ICS-specific threat intelligence;
              custom detection rules written in control terms
```

A reader who has only seen one implementation — say, a passive sensor appliance feeding a cloud console — should still recognize the others from this model.

### Capabilities Beyond the Core

**Standard capabilities** — present across mature products, expected by the market, but not what defines the Type:

- **Production-structure organization** — assets organized by sites, zones, and process areas, commonly mapped to the Purdue reference levels; the organizing geometry for navigation, alerting scope, and risk aggregation.
- **Vulnerability and exposure management** — matching known vulnerabilities against the observed estate, prioritized by operational impact, with remediation guidance that assumes most assets cannot be patched; commonly including attack-path analysis showing how an adversary could reach critical controllers.
- **Risk scoring with operational context** — asset criticality (what happens if this controller stops) folded into per-asset, per-zone, and site-level risk views.
- **OT threat intelligence** — curated knowledge of threats that target industrial environments, delivered as updates to detection.
- **SOC integration** — forwarding alerts and asset context to SIEM/SOAR platforms and mapping detections to common attack-framework vocabularies.
- **Compliance reporting** — evidence and posture reports mapped to industrial security frameworks and sector regulations.
- **Multi-site aggregation** — central management over many sites, cloud-hosted or fully on-premises; air-gapped deployments supported where networks must stay isolated.
- **Learning period and baseline governance** — behavioral detection matures with observation; products run in a learning mode before alerting is trusted, and triage outcomes (accept as normal / suppress / investigate) feed back into the baseline.
- **AI assistance** — analyst assistants that summarize, prioritize, and answer questions over the estate's security data; a current-market overlay, not structural.

**Optional / variant capabilities** — depend on product philosophy, heritage, and customer segment:

- **Enforcement** — some products recommend and orchestrate segmentation through the organization's existing firewalls, switches, and network-access controls; a few descend from network-access-control heritage and can enforce admission themselves; the majority in the researched sample detect and integrate without enforcing at all.
- **Endpoint and embedded collection** — sensors installed on capable stations (engineering workstations), sensors embedded inside controllers by the controller vendor, or agents for device builders.
- **Secure remote access** — brokered, controlled remote access for vendors and third parties who must reach the control network.
- **Managed detection and hunting** — the platform operated by the vendor's or a partner's analysts as a service.
- **Collective defense** — anonymized sharing of detection outcomes across customer communities.
- **Vertical packaging** — editions for electric utilities, water, oil & gas, manufacturing, healthcare devices, or building automation, usually the same core with domain-specific classification and compliance content.

## How It Works

### Deploy and discover

```text
Place collection points at network vantage points
  (passive first — taps or mirror ports; no software on controllers)
→ assets appear in the estate record as they communicate
→ the platform classifies each asset in OT terms
→ enrichment adds what engineering files and other systems know
→ a learning period establishes normal control behavior
```

Deployment is deliberately non-disruptive: the platform's first obligation is to not disturb the process. Passive observation produces a usable estate picture quickly; classification and behavioral baselines deepen over days to weeks. Active querying, where used at all, is limited to techniques judged safe for the network.

### Operate the detection loop

```text
Observe control-network activity continuously
→ evaluate against baselines, threat intelligence, and change rules
→ raise a finding bound to identified assets
→ triage: inspect the assets, their history, the communication
→ resolve: accept as normal (baseline update), suppress,
  investigate further, or hand off to responders
→ the outcome is recorded against the estate
```

This loop is the platform's daily life. Triage depends on the OT-specific attributes of the estate record: an alert about a controller state change is judged by whether the control engineers planned a maintenance window; an alert about an engineering station is judged by whether that station should be programming controllers at all. Detection policy is commonly tuned to focus on OT-relevant events — many products deliberately suppress generic IT-network noise so that the alerts that reach analysts are the ones that matter to the process.

### Manage exposure over time

```text
Match known vulnerabilities against the observed estate
→ prioritize by operational impact, not CVSS alone
→ remediate where the asset can be patched
→ compensate where it cannot: segmentation, access rules,
  monitoring emphasis on the exposed asset
→ track posture and produce evidence for auditors
```

Because patching a running control system is frequently impossible for the operator, exposure management here leans on *compensating* controls — limiting what a vulnerable asset can reach, and watching it more closely — far more heavily than IT vulnerability management does. This is a structural consequence of the estate, not a product preference.

### Govern the estate

```text
Maintain the record as assets appear, change, and retire
→ aggregate risk across sites and zones
→ produce compliance and posture reporting
→ keep baselines and detection current as the process changes
```

The estate record is living: controllers are replaced, HMIs move, engineering laptops come and go. The platform's governance value is that this churn is captured automatically rather than reconciled by hand.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Asset inventory

The platform's center of gravity.

- Purpose: hold and present every identified asset in the control environment.
- Typical information: network identity, OT classification (role, protocols, vendor/model/firmware), production-structure placement (site/zone/level), criticality, risk standing, last-seen activity, authorization status.
- Primary actions: search and filter the estate, open an asset detail view, annotate and mark criticality, accept or flag unknown assets, export.

### Asset detail

The single-asset investigation surface.

- Typical information: full attribute set (often including controller operating state and engineering-station designation for controllers), communication history and peers, vulnerabilities, findings involving the asset, timeline of changes.
- Primary actions: inspect communications, trace peers, correlate findings, correct classification, adjust criticality or authorization.

### Alerts / events

The operations surface where the detection loop runs.

- Typical information: finding type (threat, baseline deviation, protocol violation, change, operational incident), the assets involved, severity, first/last detection, context.
- Primary actions: triage, accept-into-baseline, suppress, investigate into asset detail, forward to SOC tooling, annotate for teammates.

### Network map / topology

- Purpose: show how the control environment actually communicates.
- Typical information: assets as nodes grouped by zone and site, communication paths, protocol relationships.
- Primary actions: explore paths, spot unexpected relationships, validate segmentation design.

### Exposure / risk views

- Purpose: make the risky subset of the estate actionable.
- Typical information: vulnerability matches per asset, risk scores with criticality context, attack paths toward critical controllers, recommended remediation or compensating controls.
- Primary actions: prioritize, assign, track remediation, generate reports.

### Policy / baseline management

- Purpose: define what "normal" means for this environment and what must always be flagged.
- Typical information: learned baselines per zone, authorized assets and communications, custom detection rules (often expressible in control terms — specific commands, specific assets), threat-intelligence update status.
- Primary actions: review proposed baseline updates, authorize expected changes, write custom rules, tune alert focus.

### Administration

- Purpose: operate the platform itself — collection points, sites and zones, users and roles, integrations, licensing, threat-intelligence updates.

## Important Rules / Behaviors

### The platform must not disturb the process

The defining behavioral constraint. Observation is passive-first; active techniques are used only where they are safe for the network; nothing is installed on controllers. Response posture follows the same ordering: alerting and recommendation outrank automatic action, and where enforcement exists at all it is exercised cautiously, because availability and safety outrank containment. A product that assumed it could freely scan, patch, or block inside a control network would not fit this Type.

### Detection matures with the learned baseline

Behavioral alerting is only trustworthy after the platform has observed normal operation. Products commonly run an initial learning period, and triage outcomes feed the baseline: accepting a finding as normal adds the underlying behavior to what is expected. A legitimate change — new equipment commissioned at scale — can generate a burst of anomalies until the baseline absorbs it.

### Unknown is security-relevant by default

After the learning period, newly observed assets and communication relationships are treated as unauthorized or new until a human accepts them. This inversion of IT-default trust is structural: in a control network, the set of things that should exist is small and stable, so novelty itself is signal.

### Most assets cannot be remediated directly

The estate's defining constraint. Actual fixes require vendor coordination and scheduled downtime; day-to-day risk reduction happens through compensating controls — segmentation, access limitation, and monitoring emphasis. Exposure views that assumed patchability would mislead the operator.

### Security and process failure share one observation point

A controller that stops responding may be compromised — or may have failed. Mature platforms surface both readings and route them to different owners (security vs. control engineering), because at the network observation point the two failure modes are indistinguishable.

### Coverage equals observation points

Everything the platform knows, it knows from where it listens. Unmonitored network segments translate directly into invisible assets and undetectable activity — the platform's knowledge is only as good as its vantage points.

### The platform never writes to the process

It observes, records, evaluates, and recommends. Control actions remain with the control system. This is what separates the security platform from the operational systems it protects.

## Variants

- **Enforcement posture** — detect-and-integrate only; recommend-and-orchestrate through existing network controls; native enforcement lineage (network-access-control heritage). The researched sample spans all three, with detect-and-integrate the most common.
- **Deployment shape** — cloud-managed consoles; fully on-premises management; locally-managed sensors for air-gapped or low-connectivity sites. All three are first-class, not legacy.
- **Collection mix** — passive-only postures for the most sensitive environments; passive plus limited active queries; endpoint sensors on capable stations; sensors embedded in controllers; analysis of engineering project files.
- **Population scope** — OT-only estates; OT plus enterprise IoT; OT plus IoT plus medical and building devices under a "cyber-physical systems" umbrella. The same platform family is commonly sold across this spectrum.
- **Philosophy poles** — threat-intelligence-led (detection organized around known adversaries targeting industry), asset/exposure-led (the estate record and its risk as the organizing spine), and network-monitoring-led (continuous observation with analytics on top).
- **Service packaging** — product only; product plus managed detection and threat hunting; product plus incident-response retainers.

A variant remains a variant while the defining core — the control-estate record plus control-aware detection under the must-not-disturb constraint — still describes it.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| IoT Security Platform | sibling | one market family, two centers of gravity: IoT security centers the enterprise/facility device estate (printers, cameras, badge readers, medical and building devices) with per-device assessment emphasis; OT security centers the industrial control environment — controllers, control protocols, production structure, safety-and-availability-first posture. Most products serve both populations; the leaves differ by emphasis. Recorded for joint review |
| Network Detection & Response / NDR | adjacent | both may watch network traffic behaviorally; NDR's subject is IT-network traffic and entities for threat hunting, with no control-protocol/process model, no control-estate record, and no must-not-disturb constraint |
| Network Monitoring (IT) | adjacent | monitors operational health of IT infrastructure; the OT platform's purpose is security of the control estate — it emits operational signals as a secondary reading, not as its purpose |
| Vulnerability Management | adjacent | VM assesses IT software assets scan-centrically with patch pipelines; OT exposure management runs without credentialed scans against unpatchable controllers and leans on compensating controls |
| Cyber Asset Management | adjacent | holds a multi-class estate inventory kept current, inventory-centric; the OT platform holds the control estate as the substrate for a continuous security detection loop |
| Network Security Platform (inline) | adjacent | enforces security policy on traffic paths; the OT platform observes — even enforcement-capable relatives act at connection admission or orchestrate existing controls |
| SIEM | downstream | aggregates security events org-wide; the OT platform is a specialized detection source and asset-context provider feeding it |
| SCADA / DCS / HMI / Industrial Historian | protected systems | these are the operational control systems that run the process; the OT security platform observes and protects them and never controls the process |
| Industrial IoT Platform | different domain | connects and operationalizes industrial devices for production purposes (telemetry, monitoring, control enablement); not a security system of record |

The most important boundary is with the **IoT Security Platform**: the two Types are one market family split by center of gravity, and the seam should be reviewed jointly. The second most important is with **NDR**: the shared passive-observation pattern hides the fact that the unit of record and the detection semantics are entirely different.

## Representative Products

- Microsoft Defender for IoT
- Nozomi Networks
- Dragos
- Claroty
- Forescout (eyeSight)

These products were used to derive and check the core model. They differ in heritage (cloud security ecosystem, network monitoring, OT-native threat intelligence, exposure management, network access control) and in enforcement philosophy, which is exactly why their shared structure is informative.

## Sources

Research date: **2026-09-09**

- Microsoft Learn — Microsoft Defender for IoT documentation (documentation hub; OT architecture and components; device inventory; alerts): https://learn.microsoft.com/en-us/azure/defender-for-iot/
- Nozomi Networks — Platform page: https://www.nozominetworks.com/platform
- Dragos — The Cybersecurity Platform: https://www.dragos.com/cybersecurity-platform/
- Claroty — Platform and Asset Inventory pages: https://claroty.com/platform , https://claroty.com/platform/asset-inventory
- Forescout — eyeSight product page: https://www.forescout.com/platform/eyesight/

> Sourcing limitation: only Microsoft's documentation was reachable at full operational-documentation depth; the other four products were observed at official product-page depth (their technical documentation sites were unreachable or returned no content in this pass). An intended historical probe of the earlier SCADA-intrusion-detection generation was also unreachable, so the historical fit of the definition rests on conceptual lineage with reduced confidence. Accordingly, precise operational details (numeric limits, time windows, named engine lists, protocol-coverage counts) are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
