# Deception Platform

## Overview

A **Deception Platform** is a defender-operated security system that plants fake-but-plausible assets — decoy hosts and services, planted credentials, deceptive documents and data, triggerable tokens — across an organization's own environment. Because legitimate users have no business reason to touch any of these assets, **any interaction with them is treated as a high-fidelity signal of malicious activity**, and the platform captures what the interacting party did.

It solves a specific detection problem: signature- and behavior-based tools watch real assets for signs of evil and drown analysts in plausible-looking alerts. A deception platform inverts this — it adds assets whose *only* function is to be touched by someone who should not be there. The result is alerts that are rare and, by construction, near-zero false positives.

The defining core is small:

```text
Decoy assets of no production function
  └── any interaction = presumptively malicious → high-fidelity alert
      └── observation of what the interacting party did
          └── all held together by a central management plane over the decoy fleet
```

Everything else commonly associated with the category — lures and breadcrumbs, credential seeding, automated decoy placement, SIEM integration, forensics capture — is standard capability that makes the core practical, not what makes the product a deception platform.

## Users & Context

Primary users are the organization's security team:

- **SOC analysts** — receive and triage deception alerts; any hit is high-priority by default
- **Incident responders** — use the captured engagement detail (what the attacker touched, ran, and tried) to scope and investigate an intrusion
- **Security architects / engineers** — plan decoy coverage, deploy and maintain the deception surface, tune noise controls
- **Threat hunters** — use decoy engagement as a starting point for deeper hunts

Secondary involvement: IT administrators who host decoy VMs or distribute deception artifacts to endpoints, and (in some products) identity teams when the deception surface covers Active Directory.

The operating context is the organization's own production environment — internal networks, cloud accounts, endpoint fleets, and identity infrastructure. Decoys sit alongside real assets and must be believable enough that an intruder cannot easily tell them apart. The threat model covers both external attackers who have gained a foothold and insiders misusing access; both are expected to eventually probe for credentials, shares, and services, and both have no legitimate reason to touch a decoy.

## Core Model

### The Defining Core

**1. The deception surface — decoy assets of no production function.**
The platform creates and maintains fake assets deployed into the environment. They imitate things an attacker wants: file servers and shares, login pages, databases, industrial-control systems, cloud storage, admin credentials, juicy-looking documents. What unifies them is that they serve no legitimate business purpose — their entire function is to be found by the wrong person. Decoys take many forms (see Variants); the invariant is the asset itself, not any particular form.

**2. The presumptive-malice engagement signal.**
Any interaction with a decoy — a connection, a login attempt, a file opened, a credential used — is surfaced as an alert to defenders. The premise is structural: there is no legitimate workflow that touches a decoy, so engagement is presumptively malicious. This is what makes the alert high-fidelity and the false-positive rate near zero (with limited tuning for known scanners — see Rules).

**3. The engagement observation.**
When a decoy is engaged, the platform records what the interacting party did: source and protocol detail, commands run, credentials attempted, files accessed, the direction of lateral movement. This turns a single alert into evidence — for triage, for incident response, and for understanding attacker techniques.

**4. The management plane.**
A central console deploys, configures, monitors, and reports on the whole decoy fleet: where decoys live, what they imitate, which alerts fired, and what the engagement looked like. This is what makes the product a *platform* rather than a single trap.

### One Structure, Many Implementations

The core is conceptual; products realize each piece differently:

```text
Concept:      Decoy asset
Realizations: emulated host/service (appliance, VM, container, cloud instance)
              agentless imitation on real endpoints (fake credentials, sessions, files)
              identity-layer decoys (fake AD objects and credentials)
              triggerable artifacts (documents, URLs, API keys, login pages)
              canary files placed on real shares

Concept:      Engagement signal
Realizations: console incident, webhook, syslog, email, SIEM event

Concept:      Engagement observation
Realizations: session/protocol logs, command capture, endpoint forensic collection,
              attacker timeline, sandbox detonation of captured files
```

A reader who has only seen one form (e.g. hardware decoy appliances) should still recognize the other forms as the same Type.

### Standard Capabilities

Mature products commonly add:

- **Lures and breadcrumbs** — small planted artifacts (shortcuts, config entries, browser history, orphaned directory objects, tempting file names) that point from real systems toward the decoys, steering an intruder's natural reconnaissance into the trap
- **Credential seeding** — fake credentials placed where attackers harvest them (memory, files, directory objects); their use anywhere is an immediate signal
- **Deployment automation and coverage guidance** — profiling the environment, recommending or automating decoy placement, and mass-deploying deception artifacts across endpoints
- **Decoy realism maintenance** — automatically refreshing decoys so they keep mirroring the changing real environment; a stale decoy is a detectable decoy
- **SOC integration** — forwarding alerts into SIEMs and ticketing via webhook/syslog, so deception alerts land in the workflow analysts already use
- **Forensics on engagement** — packet capture, endpoint forensic collection, or safe detonation of files the attacker dropped
- **Noise controls** — ignore lists and scoping so that known vulnerability scanners and admin tooling don't fire the traps
- **Console RBAC** — role-based access to the management plane (e.g. per-scope managers vs viewers)

## How It Works

The characteristic loop is mostly passive — the platform waits for the attacker to make the mistake:

```text
1. Plan and deploy
   profile the environment → decide where decoys go (near crown jewels,
   along likely lateral-movement paths, in each subnet/zone)
   → deploy decoy assets and seed lures/credentials

2. Wait (the normal state)
   the deception surface sits silently among real assets;
   legitimate users never touch it; nothing fires

3. Engagement
   an attacker (or misused insider access) probes, logs in, opens a file,
   or uses a planted credential → the decoy registers the interaction

4. Signal
   the platform raises a high-fidelity alert and delivers it to the
   console and/or the SOC's existing channels (SIEM, webhook, email)

5. Observe
   the analyst opens the engagement record: who/what/where, what the
   attacker ran and tried, how close they are to critical assets

6. Respond
   containment follows the organization's incident process; the captured
   detail feeds investigation, hunting, and longer-term defense tuning
```

Two secondary flows are common:

- **Token/tripwire flow** — generate a triggerable artifact (a document, a URL, an API key, a fake login page), place it where only an intruder would find it, and receive an alert the moment it is used. This extends the deception surface to places where a full decoy host would be impractical.
- **Maintenance flow** — the environment changes; the platform (or its automation) refreshes decoys and re-seeds credentials so the deception layer keeps matching reality.

## Interfaces

### Management console

The operator's primary surface.

- Purpose: deploy, configure, and monitor the decoy fleet; triage alerts
- Typical information: fleet/decoy inventory and health, deployment scope, incidents with source and engagement detail, attacker timelines, coverage status
- Primary actions: deploy/configure decoys and lures, review and acknowledge incidents, tune ignore lists and scoping, manage notification channels and user roles

### Engagement / incident view

The analyst's window into a triggered decoy.

- Typical information: which decoy, when, from where, what protocol or action, credentials used, related activity over time, proximity to critical assets
- Primary actions: inspect details, export or forward to SIEM/ticketing, annotate, drive response

### Notification channels

Not a page but a surface family: webhooks, syslog, email, and SIEM-specific formats that carry deception alerts into the SOC's existing tooling.

### The decoy surfaces themselves

The attacker-facing side: fake login pages, emulated file shares and services, deceptive documents. These are product surfaces too — their realism is the product's efficacy — but they are operated, not administered, by the security team.

## Important Rules / Behaviors

- **Presumptive malice, with tuned exceptions.** The near-zero-false-positive premise holds only if the traps are scoped correctly. Known scanners, monitoring tools, and admin workflows that might legitimately sweep the network are excluded via ignore lists and scoping; everything else that touches a decoy is treated as an intrusion signal.
- **Decoys must stay believable.** A deception layer only works while it mirrors the real environment; products automate decoy refresh for this reason. A decoy that has gone stale relative to its surroundings is a liability.
- **Decoys carry no production function and no sensitive data.** They exist only to be touched by the wrong party. Hosting real data on them would create real risk; this is a standing constraint of the approach.
- **Alerts are few and loud.** Unlike signature-based tooling, a deception alert is inherently rare; SOC practice treats it as high-priority by default.
- **Coverage is a design decision.** The deception surface must be placed where intruders actually go — near valuable assets and along lateral-movement paths — or it will simply never fire. Placement guidance and automation exist because coverage, not realism alone, determines value.
- **Both outsiders and insiders are in scope.** The same decoy that catches an intruder's lateral movement catches an insider misusing privileged access; products treat both as legitimate detection targets.

## Variants

Common forms of the Type:

- **Decoy-appliance deception** — emulated hosts and services deployed as hardware, virtual, container, or cloud instances, imitating servers, workstations, IoT, and industrial systems
- **Agentless endpoint deception** — deception artifacts (fake credentials, sessions, connections, documents) imitated directly on real endpoints without a persistent agent
- **Identity / directory deception** — fake directory objects and credentials inside the production identity system, catching reconnaissance and credential theft at the identity layer
- **Token / tripwire services** — lightweight triggerable artifacts (documents, URLs, keys, login pages) deployed individually or at scale; often available free or as a complement to a fuller platform
- **Open-source honeypot platforms** — self-hosted multi-honeypot systems with central aggregation and dashboards; the same core in a self-managed, research-friendly form
- **Packaging variants** — standalone products vs deception modules inside broader XDR or identity-threat platforms; the core is the same either way

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| SIEM | consumer of its output | aggregates and correlates alerts from many sources; deception is one high-fidelity *source* feeding it |
| EDR / NDR | complementary detection | watch *real* assets for signs of evil; deception watches *fake* assets whose only function is to be touched |
| Breach & Attack Simulation / Security Validation | opposite direction of synthesis | BAS runs *synthetic attacker behavior* against *real controls*; deception plants *fake targets* for *real attackers* |
| Threat Hunting Platform | trigger vs search | hunting is human-initiated search; deception passively generates the high-fidelity alerts that can launch a hunt |
| Vulnerability Management / Attack Surface Management | opposite surface | those discover and reduce *real* exposure; deception *creates* fake surface (some legacy product names overlap confusingly) |
| Insider Risk Management | overlapping threat, different object | both catch insiders, but IRM monitors human behavior; deception's object is the decoy asset |
| IAM / ITDR | packaging overlap | identity deception (fake directory objects/credentials) is one variant surface; access management and identity analytics remain different Types |
| Honeypot tooling | precursor | a standalone trap lacks the managed fleet and operational SOC framing; the open-source platform form can satisfy the full core |

The most important boundary: **EDR/NDR and deception are complements, not substitutes** — one watches what is real, the other adds what is fake. And against BAS: both are "proactive," but BAS tests *your controls* with simulated attacks, while deception catches *the actual adversary* with simulated targets.

## Representative Products

- **Thinkst Canary** — canary devices + triggerable tokens, simplicity-first standalone pole
- **Fidelis Deception** — network-forensics-centric deception with environment mapping, standalone or XDR-integrated
- **SentinelOne Singularity Hologram / Identity** — deception inside an XDR suite, network + identity decoys
- **Proofpoint Shadow** — agentless endpoint/identity deception, automation-first, ITDR-platform component
- **T-Pot** — open-source multi-honeypot platform, the self-managed research pole

## Sources

Research date: **2026-09-10**

- Thinkst Canary — API documentation & terminology: https://docs.canary.tools/ ; Help Centre (Canarytokens): https://help.canary.tools/
- Fidelis Security — Deception solution page: https://fidelissecurity.com/solutions/deception/
- SentinelOne — Singularity Hologram datasheet; Identity platform page: https://www.sentinelone.com/platform/identity/ ; Attivo acquisition announcement: https://www.sentinelone.com/press/sentinelone-completes-acquisition-of-attivo-networks/
- Proofpoint — Shadow product page: https://www.proofpoint.com/us/products/identity-threat-detection-response/shadow ; Identity Threat Defense solution brief and ITDR Buyer's Guide (PDF)
- T-Pot — project README: https://github.com/telekom-security/tpotce

> Sourcing limitation: one additional enterprise vendor in this category could not be reached (site returned errors on 2026-09-10); the enterprise pole is covered by the sampled products above. Evidence for two sampled products comes partly from vendor datasheets and solution briefs rather than operational help centers, so workflow claims for those products are stated only at the level their sources support. Precise operational facts (decoy-count limits, pricing, deployment sizing) were not researched and are intentionally not stated.
