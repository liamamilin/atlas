# Endpoint Detection & Response / EDR

## Overview

An **Endpoint Detection & Response (EDR)** application is security-operations software that instruments an organization's endpoints with a sensor, continuously collects the activity happening on those endpoints, detects malicious or suspicious behavior in that activity, lets analysts investigate what actually happened on a machine, and executes containment and remediation actions on the endpoint itself.

Its reason for existing is a gap that prevention-only tools cannot close: some attacks get past blocking — novel malware, malware-free techniques, abused legitimate tools — and when they do, the organization needs to *see* what happened on the endpoint, understand the scope, and push the attack back. EDR is built on the "assume breach" posture: prevention is running, but the system behaves as if something has already gotten through.

The defining core is small:

```text
Instrumented endpoint estate
└── continuous endpoint activity telemetry
    └── behavioral detection → analyst-facing alerts
        └── investigation into what happened on the endpoint
            └── response actions executed on the endpoint itself
```

Everything else commonly associated with modern EDR — cloud consoles, alert aggregation, MITRE ATT&CK mapping, threat-intelligence enrichment, AI triage, managed response services — is widespread standard capability, not what makes a product an EDR. Older on-premises EDR consoles and open-source host-detection platforms with scripted response satisfy the same core without any of those specifics.

## Users & Context

The primary users are security operations people, and the product is organized around their workflow:

- **SOC analysts (tier 1–2)** work the alert queue: review each detection, judge whether it is real, pivot across the entities involved, and either resolve it or escalate.
- **Incident responders and senior analysts (tier 3)** go deeper: reconstruct an attack's timeline on a machine, collect forensic data, and execute containment.
- **Threat hunters** proactively query the collected telemetry for signs of compromise that no rule caught.
- **Security administrators** deploy sensors, organize devices into groups, assign policies, and manage who may take which actions.

The work context is an organization's fleet of endpoints — employee workstations and laptops primarily, commonly servers, and in many products mobile devices — observed continuously from a central console. The endpoint user whose machine is being monitored is not a user of the application; they may only notice a sensor's presence or a containment action (for example, losing network connectivity when their device is isolated).

## Core Model

### The Defining Core

Four structures are held jointly. Remove any one and the product stops being an EDR:

**1. The instrumented endpoint estate.** Software sensors are deployed across the organization's endpoints, and each enrolled device becomes a managed, observable object. The estate is organized — devices grouped, tagged, and scoped — because every later action (policy, detection, response) is aimed at a device or a group of devices. Without the estate there is nothing endpoint-native to detect on, and the product collapses into network or log tooling.

**2. Behavioral detection over endpoint telemetry.** The sensors continuously report what endpoints do: processes and their parentage, file and registry changes, network connections, sign-in activity, and similar system-level behavior. The product evaluates this stream — with detection rules, behavioral analytics, threat intelligence, and machine learning — and surfaces malicious or suspicious activity as analyst-facing alerts or detections. Two properties make this the heart of the Type. First, the detection is *behavioral*: it judges what activity means, not just which file is known-bad. Second, the vendors themselves draw the line against prevention: detections surface activity that was *suspicious but not blocked*, which is exactly the population prevention tools never report. Without this leg the product is either a prevention engine or a raw log collector.

**3. The investigation surface.** An alert is a starting point, not an answer. The product lets the analyst reconstruct what happened on the endpoint: why the alert fired, which events came before and after it, how the involved processes relate to each other (process trees, attack lineage, threat graphs), which users, files, and network addresses were involved, and — critically — direct queries over the raw collected telemetry to answer questions no prebuilt view anticipated. Without this, the product is an alert forwarder.

**4. Response acting on the endpoint.** The "R" in EDR. The product can execute containment and remediation *on the endpoint itself, through the same channel that observes it*: isolating a device from the network while the sensor stays connected, terminating processes, quarantining files, opening a remote shell to the machine, collecting a forensic package, or running scripted responses. The action may be clicked by an analyst or triggered automatically by a rule; the invariant is that the system can *act on the endpoint*, not merely raise an alarm. Without this, the product is detection and investigation only.

The four are load-bearing together: an estate without detection is device inventory; detection without an estate is generic log analytics; detection without investigation is an alert feed; all three without response is an early-warning system, not EDR.

### Standard Capabilities of Mature Products

Most current products carry these. They make EDR practical; they do not define it:

- **Central operator console** — cloud-hosted in the dominant implementation, self-hosted in the open-source pole; the single place where the estate, its alerts, and its actions are managed.
- **Alert aggregation** — related alerts grouped into a higher-level container (an "incident" or a "case") so one attack is worked as one object.
- **MITRE ATT&CK mapping** — detections labeled with the adversary tactic and technique they represent, linking the alert to shared industry vocabulary.
- **Threat-intelligence enrichment** — detection details augmented with verdicts and context from the vendor's intelligence and third-party services.
- **Proactive hunting** — a query surface over the collected telemetry for searching beyond what rules caught; hunting queries are often promotable into standing custom detection rules.
- **Estate governance** — device groups and tags, per-group policy assignment, role-based permissions distinguishing who may view from who may act.
- **Bundled prevention** — the same sensor usually also blocks known and unwanted software (the EPP layer). Dominant in the market, but documented counter-shapes exist: sensor-only deployments that run alongside third-party antivirus, and open-source platforms with no native prevention at all.
- **Automation and managed response** — automated investigation of alerts, automatic containment of confirmed attacks, and managed detection and response (MDR) service tiers where the vendor's analysts watch and respond on the customer's behalf.
- **SOC integration** — APIs and forwarding that stream detections and telemetry into SIEM, SOAR, and data-lake tooling.

### One Structure, Many Implementations

```text
Concept:  instrumented estate
Forms:    cloud-managed sensor fleet · self-hosted agent fleet · sensor-only add-on beside third-party AV

Concept:  behavioral detection
Forms:    vendor cloud analytics over uploaded telemetry · on-prem rules engine over agent events ·
          anomaly and rootkit checks · third-party AV log correlation

Concept:  investigation
Forms:    alert story trees and process timelines · attack graphs · raw-data and lineage views ·
          query languages over collected telemetry

Concept:  response
Forms:    operator-clicked containment (isolate, terminate, quarantine, remote shell, forensic collection) ·
          automation-triggered scripts (block, delete, disable) · vendor-analyst response (MDR)
```

A reader who has only seen one shape — say, a cloud console with AI triage — should still be able to recognize an on-premises console with scripted response, or an open-source agent platform, as the same Type.

## How It Works

### Deploy and organize the estate

```text
Install the sensor on endpoints (manually, via installer, or through device-management tooling)
→ sensors enroll and report to the console
→ organize devices into groups, attach tags
→ assign policies: what the sensor collects, what it prevents, how it behaves
→ assign roles: who can view, who can take response actions
```

Deployment is the gate on everything else: a device that carries no sensor is invisible to the product (some products add limited containment for unmanaged devices discovered through managed neighbors, but observation requires instrumentation).

### Detect

```text
Sensors continuously report endpoint activity
→ the detection layer evaluates the stream against rules, behavioral models, and threat intelligence
→ a match raises an alert/detection with severity, the involved device, the technique, and the evidence
→ related alerts may be grouped into an incident or case
```

Two kinds of security output coexist and must not be confused: *prevention events* (something known-bad was blocked) and *detections* (suspicious activity that was observed and surfaced for judgment). The second kind is the EDR's distinctive product.

### Investigate

```text
Open an alert from the queue
→ read the alert story: why it fired, what preceded and followed it
→ expand the entities: processes, files, users, network addresses
→ pivot: open the device page, similar detections, intelligence verdicts
→ query the raw telemetry when the prebuilt views are not enough
→ resolve the alert: true or false, with a determination; suppress recurring false positives
```

The loop is entity-pivot-driven: each entity on the screen is a doorway to more context, and the analyst moves between alert, device, and raw data until the scope of the activity is clear. Classification feedback (true/false, determination) tunes future detection.

### Respond

```text
Choose the action proportionate to the finding
→ the action is delivered to the endpoint through the sensor channel
→ the endpoint changes state: isolated, process terminated, file quarantined, shell opened, package collected
→ the action's status is tracked (submitted, succeeded, failed) with who ordered it
→ containment is released when the threat is handled; the device returns to normal
```

Containment is deliberately visibility-preserving: an isolated device keeps its sensor connection so the analyst can keep watching it while the attacker loses the network. High-impact actions are permission-gated and often reversible, because a wrong containment on a business-critical machine has real operational cost.

### Hunt

```text
Query the collected telemetry directly (guided or query-language mode)
→ look for indicators, behaviors, weak spots no rule flagged
→ promote a successful query into a standing custom detection rule that runs automatically
```

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Alerts / detections queue

The analyst's entry surface.

- lists detections with severity, type, involved device, time, technique
- primary actions: open a detection, filter and sort, group, add to a case

### Alert / detection detail

The judgment surface for one detection.

- alert story or lineage: why it fired, related events before and after, involved entities as expandable cards
- raw data view; threat-intelligence verdicts; similar detections
- primary actions: pivot to entities, run a query, take an action on the device, resolve with classification

### Device / endpoint page

The per-machine surface and the response cockpit.

- device identity, group, health of the sensor, security state
- timeline of what happened on the machine
- primary actions: the response actions (isolate, scan, remote session, collect package, restrict execution), tags, linked alerts

### Investigation / hunting query surface

The raw-telemetry surface.

- query editor (guided builder or query language) over the collected data
- primary actions: run query, inspect results, save query, promote to a custom detection rule

### Cases / incidents

The multi-alert work surface.

- grouped detections, affected devices and users, techniques observed, status and owner, activity history, notes
- primary actions: assign, change status, add detections, document findings

### Estate management

The administrator's surface.

- device list with sensor health; groups and tags; policy assignment; role management
- primary actions: deploy, group, tag, assign policy, manage permissions

### Action center / action history

The accountability surface for response.

- every response action with its status, who ordered it, when, and whether it succeeded

## Important Rules / Behaviors

**Detection and prevention are different outputs.** A blocked known-bad file is a prevention event; a detection is raised for suspicious activity that was *not* blocked. Mature products keep the two visibly distinct, because they demand different analyst responses.

**Telemetry is selective, not a full audit log.** Sensors throttle repetitive identical events; the collected stream is tuned for security relevance, not completeness. Investigation answers questions about security-relevant activity, not every operation ever performed on the machine.

**Containment preserves visibility.** Isolation cuts the endpoint off from the network while the sensor's own channel stays open — the analyst keeps watching a machine the attacker can no longer reach. This design constraint shapes the whole response model.

**Response actions are high-impact and governed.** Isolating the wrong machine, or containing a shared network address, disrupts the business. Products therefore gate actions behind roles and device-group scope, track every action with its outcome, and make containment reversible. Some products let organizations restrict specific actions on designated high-value machines.

**Automation acts with the same powers as analysts.** Automated investigation, custom detection rules, and scripted response execute real actions on real endpoints; products expose scoping and safeguards (exclusions, approval paths, managed-service review) because a poorly scoped automated response increases risk rather than reducing it.

**Alerts are worked to a recorded conclusion.** An alert is resolved as true or false with a determination; recurring false positives are suppressed by rule. The queue is a workflow with closure, not a log.

**Capability depth is often tiered.** Products commonly gate response-action sets, retention, and automation behind license plans; two organizations on the same product may face materially different action vocabularies.

## Variants

- **EPP-converged suite** — the dominant shape: prevention and EDR on one sensor, sold as endpoint security (most of the sampled market).
- **Standalone / sensor-only EDR** — detection, investigation, and response without the prevention stack, running beside third-party antivirus; also the shape of open-source host-detection platforms.
- **Platform-native EDR** — the endpoint layer of a broader security platform, feeding a unified portal where endpoint signals are correlated with identity, email, and cloud sources.
- **Cloud SaaS vs self-hosted** — vendor-operated cloud console vs on-premises server components the customer operates.
- **Managed-service tier (MDR)** — the vendor's analysts monitor and respond on the customer's behalf, from consultation to full 24/7 response.
- **Object-domain breadth** — user-endpoint-focused estates; estates that include servers; estates that include mobile devices. Server coverage overlaps the neighboring cloud-workload-protection Type, whose boundary is the workload operational context rather than the presence of an agent.
- **AI-era assistance** — AI triage of detections, natural-language investigation assistants, automated attack disruption; current differentiators, not structural features.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Endpoint Protection Platform / EPP | closest sibling; same devices, usually same sensor | EPP centers on preventing execution (blocking known/unwanted software); EDR centers on detecting what got through, investigating it, and responding. Most products bundle both; the Types are distinguished by center of gravity, and both pure poles have existed. |
| Extended Detection & Response / XDR | umbrella above | XDR correlates endpoint signals with other domains (identity, email, cloud, network) into unified incidents. Remove the non-endpoint sources → EDR. |
| SIEM | adjacent; data-plane overlap | SIEM aggregates organization-wide logs with correlation and compliance machinery; EDR's data is endpoint-telemetry-native and its response acts on endpoints. Some open-source platforms straddle both. |
| Cloud Workload Protection / CWPP | sibling with converging machinery | CWPP's object is the server/container/cloud-workload estate and its image/vulnerability context; EDR's is the endpoint estate and user-device operational context. The boundary is object domain and workflow, not agent technology. |
| Network Detection & Response / NDR | structural sibling on another path | NDR instruments the network path; EDR instruments the host. |
| Threat Hunting Platform | capability vs Type | Hunting is a standard EDR capability over its own telemetry; a dedicated hunting platform centers the hunt workflow across many sources. |
| Digital Forensics Platform | adjacent; opposite evidence posture | Forensics examines preserved, verified copies offline with defensibility machinery; EDR investigates live telemetry in production. |
| Cyber Incident Response Platform | downstream | IR platforms manage incidents as cases with a response lifecycle; detection is the EDR/SIEM's job. EDR case-like containers are detection-triage-shaped, not response-program-shaped. |
| Mobile Threat Defense | object-domain slice | Mobile devices are part of the endpoint estate in many EDR products; the specialized mobile-security pole is its own Type. |
| Endpoint Management / UEM | different job on the same devices | UEM configures, complies, and manages devices; EDR detects and responds to threats on them. Agents may be shared; the jobs are not. |
| Browser Security Platform | adjacent | Browser security binds enforcement to the browsing session; remove that session binding and the machinery is EDR-shaped. |

## Representative Products

- Microsoft Defender for Endpoint — platform-native EDR inside a broader security portal
- CrowdStrike Falcon (Falcon Insight) — cloud-native pure-play endpoint security platform
- Sophos EDR / XDR — EPP-converged suite with a sensor-only variant and a managed-response service
- Wazuh — open-source, self-hosted detection-and-response platform (SIEM/XDR-branded, EDR-shaped endpoint machinery)

The defining core was checked against older and differently positioned shapes — on-premises console-era EDR and open-source host-detection lineage — to avoid defining the Type by the current cloud/AI implementation.

## Sources

Research date: **2026-09-08**

- Microsoft — Microsoft Defender for Endpoint documentation (overview; endpoint detection and response capabilities; response actions on devices; alert investigation; advanced hunting): https://learn.microsoft.com/en-us/defender-endpoint/ and https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview
- Sophos — Sophos Central Admin help (EDR and XDR; Endpoint; Detections; Cases): https://docs.sophos.com/central/customer/help/en-us/
- Wazuh — Wazuh documentation (capabilities: Active Response; Malware detection): https://documentation.wazuh.com/current/
- CrowdStrike — Endpoint Security product page (positioning only): https://www.crowdstrike.com/products/endpoint-security/

> Sourcing limitation: the CrowdStrike documentation portal was not reachable from the research environment (JavaScript-only application), and SentinelOne, Elastic Defend, and Cortex XDR documentation could not be retrieved after repeated attempts. Operational detail in this document is therefore calibrated to the products whose official documentation was directly observed, with the market leader represented at positioning level only. Precise product-specific numbers (retention windows, quotas, plan-gated action lists, isolation timers) are intentionally not stated here; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
