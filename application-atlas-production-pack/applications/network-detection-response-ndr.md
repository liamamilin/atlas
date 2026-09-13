# Network Detection & Response / NDR

## Overview

A **Network Detection & Response (NDR) application** is the security team's network-side threat detection system. It continuously observes an organization's network traffic from network vantage points — copies of traffic taken from taps, switch mirrors, or cloud mirrors, and/or flow records exported from network and cloud infrastructure — analyzes what it observes for malicious or suspicious behavior, and supports the investigation of, and response to, what it detects.

The defining core is small:

```text
Network observation plane (out-of-band traffic and flow collection)
└── Entity picture (devices, users, external endpoints) built from observed traffic
    └── Threat-oriented detection (signatures · behavioral baselines · ML · threat intel)
        └── Detection (persisted security finding bound to entities and time)
            └── Investigation & response loop (evidence, triage, containment)
```

Everything else commonly associated with the category — machine learning, cloud consoles, autonomous AI response, packet forensics at scale, MITRE ATT&CK dashboards — is widespread in current products but not part of what makes the product an NDR. Flow-only deployments, signature-heavy open-source-heritage products, and analyst-driven (non-autonomous) products are all fully NDR.

The category exists because preventive controls cannot keep everything out and because many devices cannot run security agents at all. An NDR watches the one medium an attacker cannot avoid using — the network — and gives the security operations center (SOC) both the warning and the evidence to act on it.

## Users & Context

The primary users are security operations people:

- **Tier 1 analysts** — watch the detection queue, triage new detections, close obvious noise, escalate real findings. They live in the detections list and entity pages.
- **Tier 2 analysts / incident responders** — investigate detections in depth: reconstruct what happened on a device, group related detections into an attack picture, decide and execute response actions.
- **Tier 3 analysts / threat hunters** — proactively query retained network evidence for patterns no automated detection caught.
- **Security engineers** — deploy and maintain the sensor fleet, tune detections, manage integrations with SIEM, EDR, firewalls, and identity systems.
- **Security leadership** — consume reporting on detections, coverage, and posture (secondary).

The work context is a SOC, staffed around the clock in larger organizations. Smaller organizations commonly wrap the same product with a managed detection and response (MDR) service, where vendor or provider analysts operate the product on the customer's behalf. The product is deployed once as an observation infrastructure and used daily as an operational console; unlike a scanner or an audit tool, it has no "run" — it is always watching.

## Core Model

### The defining core

**1. The network observation plane.** The system watches the network itself. Sensors are deployed out of band — they receive copies of traffic from taps, SPAN/switch mirror ports, or cloud packet mirrors — and/or ingest flow records (router-exported flow data, cloud flow logs) where packet mirroring is impractical. No software is installed on monitored endpoints, and the sensor does not sit in the traffic path. This is what makes the evidence source different from an endpoint agent's or a log collector's: the network is observed directly, including devices nobody manages.

**2. The entity picture.** From observed traffic the system builds and maintains its own model of who and what is communicating:

- **Devices / hosts** — discovered automatically as they communicate, classified by observed behavior (server, client, gateway, database, and similar roles), tracked across address changes where possible.
- **Users / identities** — attributed to devices where the observed protocols expose a username, and enriched from identity-system integrations in mature products.
- **External endpoints** — remote IPs and domains that internal devices talk to, with geolocation and reputation enrichment.

The entity picture is not a static asset register; it is continuously re-derived from live traffic, which is precisely why it covers unmanaged devices, IoT, and OT equipment that no agent can reach.

**3. The detection.** The detection is the product's unit of security output: a named, persisted finding that specific observed behavior is suspicious or malicious — bound to the involved entities, a time span, and the underlying evidence. Detections are generated continuously by a mix of machinery (see below), organized by attack behavior — reconnaissance, command-and-control, exploitation, lateral movement, actions on objective such as data theft — and commonly mapped to MITRE ATT&CK techniques. A detection has a lifecycle (see How It Works) and can be tuned, assigned, tracked, and grouped with other detections.

**4. The investigation & response loop.** Detections are meant to be worked, not just counted. The product supplies the analyst console, the retained evidence (related activity, structured records, captured packets), the grouping of many detections into one attack narrative, and the pathways to act: analyst-triggered containment, actions executed through connected tools, or — in some products — autonomous response. Response is part of the product's job even when the blocking action itself is performed by a firewall, an EDR agent, or a switch: the NDR supplies the evidence and the workflow that justify and drive the action.

Each element is load-bearing. Remove the network observation plane and the product becomes an endpoint or log tool. Remove threat orientation and it becomes network performance monitoring. Remove the investigation surface and it collapses to a classic intrusion-detection sensor emitting alerts. Remove the response loop and it becomes detection-only network traffic analysis — the historical shape of the category before it matured into NDR.

### Standard capabilities

Mature products commonly add, on top of the core:

- **Sensor fleet management** — deploying and managing many sensors across sites, segments, and clouds from one console.
- **Asset discovery depth** — device roles, high-value designations, software/operating-system fingerprinting, and a searchable inventory built entirely from traffic.
- **Multiple detection engines in one product** — signature/IDS rules, behavioral baselines learned per device and per group, machine-learning anomaly models, and threat-intelligence matching (known-bad addresses, domains, file indicators), plus user-defined custom detections.
- **Prioritization machinery** — risk scores, triage recommendations (detections involving high-value assets, high-privilege users, rare detection types, or known-bad indicators), and automatic correlation of many detections into recommended investigations or attack narratives.
- **Detection lifecycle management** — statuses, assignment, notes, tuning/suppression rules, notification rules, and references into external ticketing.
- **Retained evidence** — packet capture stores and structured flow/transaction records that let analysts answer questions about past events, with packet-level drill-down and export.
- **Coverage breadth** — east-west (lateral) and north-south (boundary) traffic, remote-user and cloud segments, and analysis of encrypted traffic through its observable metadata; optional TLS decryption where policy permits.
- **Ecosystem integrations** — feeding detections and evidence to SIEM/SOAR, correlating with EDR, triggering containment in endpoint or firewall controls, and writing tickets; APIs for automation.
- **MITRE ATT&CK mapping** — detections and coverage visualized against the standard attack-technique matrix.
- **AI assistance** — AI-analyst investigation, agentic triage, and generated summaries in current products.

### One structure, many realizations

The core is conceptual; products implement each piece differently:

```text
Concept:        Observation plane
Realizations:   packet taps/SPAN into wire-data sensors · cloud packet mirrors ·
                router/cloud flow logs · mixed fleets

Concept:        Detection machinery
Realizations:   vendor-curated signature collections · per-organization behavioral
                learning · ML baselines · threat-intel feeds · custom rules · combinations

Concept:        Entity identity
Realizations:   hardware/address anchoring · hostname/DNS naming ·
                username attribution from observed protocols · cloud-metadata enrichment

Concept:        Response
Realizations:   analyst one-click containment · actions via EDR/firewall/SOAR
                integrations · autonomous AI response · some products combine these

Concept:        Console
Realizations:   self-managed on-premises console · vendor SaaS console · hybrid
```

## How It Works

### Deploy the observation plane

Security engineers identify the network points that matter — internet boundaries, data-center cores, critical segments, cloud environments — and place sensors there to receive copied traffic or flow records. Sensors sit out of band, so deployment does not touch the traffic path. Flow-based sensors extend coverage to cloud networks where packets cannot practically be mirrored. The sensor fleet is then managed as one estate from the console.

### Observe and learn

Sensors immediately begin discovering devices and their behavior. The entity picture builds up: devices classified by what they do, users attributed where protocols expose identity, external endpoints cataloged. Behavioral machinery establishes baselines of normal activity per device and per group; this learning period is why behavioral detections improve over time after deployment.

### Detect

As traffic flows, the detection engines run continuously: signature rules match known-bad patterns and exploit attempts; behavioral and ML analysis flags deviations from baseline (a device suddenly scanning peers, a first-time connection to a suspicious server, a spike in a protocol); threat-intelligence matches flag known-bad infrastructure. When something matches, the system creates a detection — with participants, time span, category, and evidence attached — while the behavior may still be ongoing.

### Triage

Analysts work the detection queue. Views group detections by type, participant, severity, or attack technique; prioritization machinery (risk scores, triage recommendations) surfaces what deserves attention first. An analyst either dismisses noise — ideally by creating a tuning rule that structurally suppresses that low-value pattern — or escalates the detection for investigation. Recipients outside the console (SIEM, SOAR, email, ticketing) receive notifications per configured rules.

### Investigate

An escalated detection is opened in its detail view: who was involved (offender and victim participants, linked users), what exactly was observed, the risk assessment, and links to evidence — related activity, structured records, and captured packets where available. The analyst pivots to entity pages to see everything known about a device or user, and groups related detections into an investigation — a single timeline and topology view that answers whether this is one isolated anomaly or one step of a broader attack. Some products perform part of this investigation automatically, producing an attack narrative with recommended next steps.

### Respond

Once behavior is validated, the analyst acts. Typical response actions, depending on product and integrations: containing a compromised host through an integrated endpoint agent or the platform's own containment capability, changing firewall policy to cut command-and-control paths, forcing reauthentication of an account, or dispatching the case to SOAR for orchestrated response. Every action is recorded against the case with its evidence. In products with autonomous response, the system itself executes containment actions within customer-set guardrails.

### Tune and hunt

Between incidents, the team tunes: suppressing recurring false positives, marking high-value assets and users so future prioritization is sharper, and writing custom detections for organization-specific concerns. Hunters query the retained evidence directly — searching traffic metadata, records, and packet stores for patterns that no standing detection covers. Detection content and threat intelligence update continuously from the vendor.

### The detection lifecycle

Conceptually, a detection moves: **generated** (open) → **acknowledged / in progress** as an analyst picks it up → **closed** (resolved or dismissed), with low-value patterns suppressible by tuning rules so their future instances are hidden rather than generated. While the observed behavior continues, the detection remains open-ended. Exact status labels vary by product; the managed lifecycle itself is standard.

## Interfaces

The analyst-facing surfaces, described conceptually (names and layouts vary by product):

### Detection queue

The primary working surface.

- Purpose: triage the stream of detections.
- Typical information: detection name/type, category, participants, time span, risk score or priority, status, triage-recommendation flags.
- Primary actions: filter/sort/group, open a detection, dismiss or tune, assign, add to an investigation.

### Detection detail

The single-detection workbench.

- Typical information: participants with roles (initiator/target), what was observed, risk explanation, the detection's method or signature, linked evidence (metrics, records, packets), tracking panel (status, assignee, notes).
- Primary actions: review evidence, pivot to entities, track/tune, add to investigation, trigger response actions where available.

### Entity / device pages

The profile of one discovered device, user, or external endpoint.

- Typical information: addresses and names observed over time, role/classification, software fingerprint, activity history, related detections and users.
- Primary actions: inspect activity, view related detections, mark high-value, pivot into investigations.

### Investigation workspace

The multi-detection view.

- Typical information: grouped detections on one timeline, often with a topology/map of involved entities.
- Primary actions: add detections, annotate, assess scope, drive response.

### Evidence viewers

Packet inspection and record search surfaces.

- Typical information: captured packets, structured flow/transaction records, traffic metadata over time.
- Primary actions: search, filter by entity/time, download packets for external forensics.

### Dashboards and reporting

Security-overview dashboards (detection volume, categories, top offenders), MITRE technique coverage views, and scheduled reports for management and compliance audiences.

### Administration

Sensor/fleet management, detection tuning rules, notification rules, threat-intelligence sources, integrations, user accounts and role-based access.

## Important Rules / Behaviors

- **Observation is out of band.** The NDR watches copies of traffic; it does not sit in the path. This is why its detections cannot block anything by themselves — response always executes through some enforcement point (a firewall, a switch, an endpoint agent), whether triggered by an analyst or by the product.
- **Detections inform, they do not decide.** Mature products explicitly frame detections as input to analyst judgment; documentation directs users to investigate before acting. Even autonomous-response products confine automatic actions to configured guardrails.
- **Noise control is a first-class operation.** Detection volume is managed structurally — tuning rules suppress defined low-value patterns, and prioritization weights detections by asset value, user privilege, rarity, and threat-intel context — because the alternative is analyst fatigue.
- **Network identity is inferred, not declared.** Devices are known by what they do on the wire: addresses may change, names come from observed traffic, and usernames are attributable only where the protocol exposes them. This makes the entity picture rich but inherently probabilistic; products handle address volatility by tracking identity at the device level where they can.
- **Encryption shapes what is visible.** Payloads of encrypted traffic are generally unavailable; products detect on connection metadata, sizes, timing, and protocol behavior instead. Decryption, where used, is selective and policy-governed; whether decrypted content is kept on disk varies by product.
- **Evidence retention is a design axis.** Continuous observation produces far more data than can be kept indefinitely; products manage aging of metrics/records and offer deeper packet retention as storage tiers. Forensic capability therefore depends on what was configured before the incident.
- **Detections are not incidents.** An important recurring behavior is correlation: many low-level detections across several entities may be one attack. The investigation layer exists to make that judgment possible.
- **Access is role-gated.** Detections reveal sensitive information about the environment; administration, tuning, and response actions are permission-scoped in mature products.

## Variants

Common shapes the Type takes; none of these changes the defining core:

- **Packet-depth vs flow-only** — full wire-data analysis where mirroring is available; flow-record-only coverage (especially cloud networks) where it is not. Many deployments mix both.
- **Self-managed vs SaaS console** — consoles run on customer infrastructure or as vendor-operated SaaS; some vendors ship both as distinct editions.
- **Standalone product vs platform module** — NDR sold alone, as a licensed module of a broader network-observability platform, or as one product in a multi-domain security suite.
- **Detection philosophy** — per-organization behavioral learning as the headline vs vendor-curated global detection content vs open/open-core detection collections; most products combine several.
- **Response posture** — analyst-triggered actions, integration-mediated response, or autonomous AI response within guardrails.
- **Domain extensions** — OT/ICS protocol visibility, identity-threat detection, cloud-native agentless coverage, and exposure/posture management as attached capabilities.
- **Operated vs self-run** — the product run by the customer's own SOC or operated day-to-day by an MDR/MSSP service.

If a "variant" changes the evidence plane to endpoint agents or puts the product inline in the traffic path, it has stopped being this Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Endpoint Detection & Response / EDR | Complementary sibling. EDR instruments endpoints with agents; NDR observes the network from network vantage points — covering the many devices that cannot run agents. Vendors position them as mutually completing visibility layers; the response-loop shape is shared, the evidence plane is not. |
| SIEM | SIEM aggregates logs from many sources for correlation, retention, and compliance; NDR generates its own detections from its own network-derived telemetry and feeds the SIEM. A SIEM has no sensors; an NDR is mostly sensor. |
| Network Monitoring | Same observation plane, different question. Network monitoring watches traffic for performance and availability (is it slow or down?); NDR watches for threats (is it compromised or attacking?). The two can share sensor infrastructure, and some platforms ship both as separately licensed, permissioned modules. |
| Network Security Platform / NGFW / IPS | Inline enforcement versus out-of-band observation. Firewalls and IPS stand in the traffic path applying policy; NDR stands aside watching it. They cooperate — an NDR detection can trigger a firewall change — but the roles differ. |
| XDR | XDR correlates signals across endpoint, network, identity, and cloud domains; NDR is the network-domain specialist whose high-fidelity detections and evidence feed that correlation. NDR remains its own product category even when consumed inside an XDR strategy. |
| Deception Platform | Deception plants decoy assets and detects interaction with them; NDR observes real traffic among real assets. Deception findings may land in NDR-class consoles, but the mechanisms differ. |
| Threat Hunting Platform | Hunting is an analyst activity; NDR is a standing detection system. NDR products support hunting over their retained evidence, but hunting is a capability here, not the defining loop. |
| Cyber Asset Management | NDR builds an entity inventory from traffic as a byproduct of detection; asset-management products make the inventory itself the managed record of business value. |
| SOAR | SOAR orchestrates response workflows across tools; NDR supplies detections and evidence into those workflows and, in some products, executes contained actions itself. |

The closest boundary inside the directory is **Network Monitoring** — the two types can literally share one sensor plane, and the split is the security-vs-performance question asked of the traffic. The closest boundary in practice is **EDR** — the two are bought as complements, and vendors' own comparisons (NDR vs EDR vs SIEM visibility models) draw the line exactly at the evidence plane.

## Representative Products

- **Darktrace** — Darktrace / NETWORK (self-learning per-organization behavioral AI; autonomous response; part of a multi-domain security platform)
- **Vectra AI** — Vectra AI Platform (behavioral attack-surface detection for SOC prioritization; network, identity, and cloud extensions)
- **ExtraHop** — RevealX (wire-data and flow analysis; NDR and network performance monitoring as licensed modules on one sensor platform)
- **Corelight** — Open NDR Platform (open network-security-monitoring heritage; evidence-first sensors with Zeek and Suricata; SaaS investigation console)

The defining core was checked against flow-based telemetry realizations and against the category's open-NSM and detection-only lineage (network traffic analysis / classical network intrusion detection) to avoid defining the Type by any one product philosophy or era.

## Sources

Research date: **2026-09-08**

- ExtraHop — Documentation portal: https://docs.extrahop.com/
- ExtraHop — Introduction to the ExtraHop system: https://docs.extrahop.com/current/intro-to-eh-system/
- ExtraHop — Detections: https://docs.extrahop.com/current/detections-overview/
- Corelight — All Products: https://corelight.com/products
- Corelight — Investigator: https://corelight.com/platform/investigator
- Corelight — "What is NDR" glossary: https://corelight.com/resources/glossary/ndr-network-detection-and-response
- Darktrace — Darktrace / NETWORK: https://www.darktrace.com/products/network
- Darktrace — corporate site: https://darktrace.com/
- Vectra AI — AI Cybersecurity Platform: https://www.vectra.ai/platform/ai-cybersecurity-platform
- Vectra AI — corporate site: https://www.vectra.ai/

> Sourcing limitations: one additional flow-based vendor's product page (Cisco Secure Network Analytics) was unreachable (HTTP 403) and was not researched first-hand; the flow-telemetry realization is documented through other sampled products' flow-sensor documentation. Vendor help centers for two sampled products (Darktrace, Vectra AI) were not reachable in the research environment; their observations rest on official product pages and are calibrated accordingly. Precise vendor-specific figures (throughput tiers, retention windows, scoring bands, automation cadences) are intentionally not stated in this document; they are recorded in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, vendor-specific findings, and the boundary analysis are recorded in the paired Research Notes.
