# Attack Surface Management

## Overview

An **Attack Surface Management** application continuously discovers and maintains an inventory of an organization's internet-facing digital assets — seen from the outside, the way an attacker would see them — and attaches the exposures it observes to those assets.

The defining core is small:

```text
Organization scope (seeds / root assets / scan scope)
  ↓ outside-in discovery
External asset inventory (persistent, organization-scoped)
  ├── asset records with observed attributes
  ├── exposures/issues attached to assets
  └── ongoing monitoring of change
```

Four properties make the Type what it is:

- **Organization-scoped external asset inventory** — the system maintains persistent records of the organization's own internet-reachable assets: domains, hosts, certificates, web services, cloud-exposed resources. Without the inventory, there is no "management."
- **Outside-in discovery** — assets are found by observing the internet from outside the organization, starting from a few known identifiers and expanding through observed relationships. No internal agents, network access, or pre-existing complete asset lists are required. This is what makes the Type distinct: it finds assets the organization does not know it has.
- **Observations and exposures attached to assets** — each asset record carries what the system observed about it (services, certificates, technologies, context) and the issues or exposures detected on it.
- **Ongoing maintenance** — discovery and observation recur, so the inventory tracks a moving target: new assets appear, exposures change, assets disappear.

Everything else the market expects from a modern ASM product — risk scoring, dashboards, ticketing integrations, cloud connectors, policy engines — is standard capability layered on this core, not the definition of it.

## Users & Context

The primary users are security team members responsible for external exposure:

- **attack surface / exposure analysts** — work the inventory daily: review newly discovered assets, triage findings, confirm or reject attribution
- **vulnerability management owners** — consume ASM findings as input to remediation workflows, especially for assets their internal scanners never see
- **security operations** — use the inventory during incident response ("what do we have at this IP?") and emerging-threat response ("where is this vulnerable software exposed?")

Secondary users:

- **CISO / security leadership** — consume dashboards and reports on posture, inventory growth, and critical exposures
- **IT / infrastructure owners** — receive remediation tasks for assets attributed to their teams

Typical contexts that drive adoption:

- shadow IT and cloud sprawl creating infrastructure nobody tracked
- mergers and acquisitions bringing unknown acquired assets
- subsidiaries, franchises, and regional teams standing up services outside central IT
- certificate expiry, forgotten subdomains, and decommissioned-but-still-running services

The work environment is a web console used by a small security team, with findings pushed outward to the people who own the affected assets.

## Core Model

### Assets

The central object is the **asset**: a record of one externally reachable thing the organization is responsible for (or connected to). Across mature products, assets fall into recurring kinds:

- **domains and subdomains** — DNS names, with registration data (registrar, name servers, mail servers) and expiry
- **hosts / IP addresses** — machines reachable on the internet, with open ports and the services running on them
- **web services / pages** — name-and-port HTTP surfaces, their technologies, response behavior, and content signals
- **certificates** — TLS certificates observed on hosts, with issuer, expiry, and trust properties
- **cloud-exposed resources** — object storage buckets and other cloud resources observable from outside, with access posture
- **network-range and routing records** — IP blocks and autonomous system numbers associated with the organization
- **organizational records** — registration/whois organization and contact records that anchor attribution

An asset is identified by a stable key of its kind (a domain name, an IP address, a certificate fingerprint, a name-and-port pair). The same real infrastructure can surface as several related assets — a domain resolves to a host, the host serves a web service, the web service presents a certificate — and mature products keep these as distinct, linked records rather than merging them into one blob.

### Scope: seeds and root assets

Discovery needs a starting point. Products converge on the same mechanism under different names: the organization provides a small set of **known identifiers** — typically domains, IP addresses or ranges, and ASNs — and the system expands outward from them. Some products can also propose seeds they have themselves connected to the organization. The scope definition is the user's primary act of configuration: it decides what the system will consider "our surface."

### Observations

Each asset carries what discovery and repeated observation have produced: DNS resolutions, open ports and service banners, technology fingerprints, certificate metadata, geographic and cloud-hosting context, first-seen and last-seen timestamps. Observations are the raw material; they are usually inspectable down to the underlying evidence.

### Exposures / findings

Attached to assets are **exposures**: issues the system detected that matter to security — a vulnerable software version, an expired certificate, an unauthenticated database, a subdomain ripe for takeover, a misconfigured storage bucket, an end-of-life system still serving traffic. A finding typically carries:

- a severity rating (often adjustable by the team)
- a category (exposure, vulnerability, certificate, misconfiguration, end-of-life, compliance)
- **evidence** — a link to the observation that triggered it, so an analyst can verify rather than trust
- a lifecycle state — active, accepted (deliberately tolerated, usually with a recorded reason), or closed (no longer detected)

### Attribution and ownership

Because discovery starts from the outside, the system must answer "is this actually ours?" Attribution machinery is a structural part of the Type:

- **source of asset** — whether it came from a provided seed, was discovered by the system, or arrived from a connected cloud account
- **ownership states** — mature products separate assets they are confident belong to the organization from those that need human review, and commonly mark third-party-operated dependencies and related-but-not-controlled assets as distinct categories
- **owner assignment** — naming the team or person responsible, so findings can be routed; some products auto-populate owners from directory and cloud integrations

Attribution is probabilistic by nature. Confidence in a discovered asset's relationship to the organization decreases as discovery moves further from the seeds, which is why candidate-review is a normal, permanent activity rather than a one-time setup step.

### Change over time

The inventory is a living record. Assets have first-seen and last-seen timestamps; assets no longer observed may be marked historic or offline rather than deleted. The system tracks what was added and removed, and surfaces change through alerts and change dashboards.

## How It Works

The operational loop of an ASM product runs continuously:

```text
Define scope (provide seeds: domains, IP ranges, ASNs)
  → discover (expand from seeds through observed relationships:
     DNS records, certificate reuse, shared registrants,
     co-hosted addresses, cloud accounts)
  → attribute (label each discovered asset: confirmed /
     candidate / dependency; route candidates to human review)
  → observe (collect services, technologies, certificates,
     cloud context on every confirmed asset)
  → assess (detect exposures on observed assets, with evidence)
  → prioritize (severity + context; curated finding lists)
  → hand off (assign owners; push to ticketing / VM / SIEM)
  → verify (rescan to confirm remediation)
  → monitor change (alert on new assets, new findings, removals)
  ↺ (discovery and observation repeat on an ongoing basis)
```

**Define scope.** The team registers the identifiers it knows about — usually the corporate domains, known IP ranges, and ASNs. Some products verify that the team controls a domain (for example, via a DNS record) before actively scanning it; this protects against scanning infrastructure the team does not actually own.

**Discover.** From each seed, the system follows observable relationships outward: other domains registered by the same registrant, hosts that share certificates, addresses that co-resolve, IP blocks under the same ASN, resources in connected cloud accounts. Each expansion step yields new candidates; strong connections are accepted automatically, weaker ones are queued for review. Discovery is deliberately recursive — the point is to reach assets that no internal system of record lists.

**Attribute.** Every discovered asset gets a source and an ownership state. Analysts review candidates and either accept them into the owned inventory, mark them as dependencies or monitor-only, or dismiss them. This review loop never fully ends, because the surface keeps changing.

**Observe and assess.** On confirmed assets, the system collects service and technology detail and evaluates exposures. Findings are recorded with evidence linking back to the underlying observation — a defining behavior of the Type, since analysts must verify externally-derived claims before acting on them.

**Prioritize and hand off.** Teams work from curated finding lists rather than raw scan output. Findings are assigned to owners and pushed into ticketing, vulnerability management, or SIEM tools, where remediation actually happens. The ASM product is the discovery and tracking system of record; remediation execution usually lives elsewhere.

**Verify.** After a fix is claimed, a rescan confirms the exposure is gone. This closes the loop without waiting for the next scheduled observation cycle.

**Monitor.** Between full cycles, the system watches for change: a new subdomain, a newly opened port, a certificate nearing expiry, a fresh finding on a known asset. Alerts (email, chat, webhooks) and change dashboards keep the team ahead of the surface rather than rediscovering it annually.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Inventory explorer

The primary working surface: a searchable, filterable table of all assets.

- typical information: asset identifier and type, ownership state, source, key attributes (services, certificates, cloud context), finding counts, first/last seen
- primary actions: search and filter (by attribute, state, severity, source), open asset detail, tag or annotate, export

### Asset detail page

Everything the system knows about one asset.

- typical information: attributes and their history, related assets (the domain behind a host, the certificate behind a web service), observations with raw evidence, exposures with severity and evidence, ownership and state
- primary actions: change ownership state, assign owner, accept/dismiss a finding, trigger a rescan, pivot to related assets

### Findings / exposures list

The remediation-facing surface: all detected issues across the inventory.

- typical information: finding name, severity, category, affected assets, detection date, lifecycle state, evidence link
- primary actions: filter by severity/category/asset type, edit severity with reason, accept a risk (recorded, reversible), export, push to ticketing

### Dashboards

Management- and posture-facing summaries.

- typical information: inventory size and growth, added/removed assets over recent windows, exposure counts by severity and category, posture trends
- primary actions: filter by asset type or time range, drill into the underlying inventory

### Scope / seed configuration

Where the organization defines its surface.

- typical information: current seeds with type and label, source (provided vs system-found), discovery run status
- primary actions: add seeds (individually, by upload, via API, via cloud/DNS connectors), remove seeds, schedule discovery

### Alerts and integrations

The connective tissue to the rest of the security stack.

- typical information: alert rules (new asset, new finding, query match), delivery channels, connected tools
- primary actions: create rules, connect ticketing/SIEM/chat tools, configure API keys

## Important Rules / Behaviors

### Attribution is probabilistic and review-bound

Discovery from the outside cannot be certain. Mature products therefore separate confirmed assets from candidates and route the latter to human review. A candidate that is actually owned must be promoted manually; the system does not silently absorb weakly-connected assets into the owned inventory. This is a structural rule, not a UI convenience.

### Findings carry verifiable evidence

Because the system observes from outside, its claims can be wrong (a fingerprint mismatch, a shared hosting neighbor). Findings therefore link to the observation that produced them, and analysts are expected to verify before remediating. A finding without inspectable evidence would not fit the Type's contract with its users.

### Accepted risk is a recorded state

Teams can accept a finding — deliberately tolerating it — and the acceptance is recorded (often with a reason), reversible, and excluded from active counts while preserved for audit. Acceptance is distinct from closure: closure happens when the system stops detecting the issue.

### Scope defines everything

The inventory only contains what the scope can reach. An unregistered domain, an unknown subsidiary's cloud account, or an IP range never provided as a seed will not appear until something links it to a seed. Expanding scope is a normal operational activity, not a one-time setup.

### Ownership verification before active testing

Products that actively probe assets typically require the customer to verify control of the domains in scope first (for example, via a DNS record). This keeps the product from being used to test infrastructure the customer does not own — a boundary imposed by both ethics and law.

### Rescan validates remediation

Fix verification is done by observing again, not by trusting a ticket status. A rescan either confirms the exposure is gone (finding closes) or shows it persists (finding stays active).

### Assets age; they do not simply vanish

Assets no longer observed are marked historic or offline and remain queryable. The inventory is a longitudinal record of the surface, which is what makes trend views and "what did we have at this address last quarter?" questions answerable.

## Variants

Common forms of the Type:

- **external-only ASM (EASM)** — the dominant market form: inventory and monitoring restricted to internet-facing assets
- **internal + external discovery** — the same unauthenticated discovery machinery pointed at internal networks as well, producing one inventory across both (an inventory-first philosophy)
- **dataset-driven vs scan-driven discovery** — some products derive the surface largely from accumulated internet-wide observation data; others actively scan the customer's scope; most blend both
- **with bundled application testing** — some products add deep, per-application testing (DAST-style scanning, authenticated scanning behind logins, or continuous automated penetration testing) on top of surface discovery
- **with cloud connectors** — connecting cloud accounts to enrich assets with account context and catch cloud resources that external observation alone would miss
- **suite-embedded vs standalone vs self-serve** — delivered as a module of a large security platform, as a standalone exposure platform, or as a self-service SaaS for smaller teams
- **with managed service** — vendor analysts run discovery and triage; the customer consumes reports and validated findings
- **self-hosted option** — some products offer on-premises collection and console deployment alongside SaaS

A variant remains a variant as long as the defining core — outside-in, org-scoped, asset-anchored, ongoing — is intact. When the outside-in perspective disappears entirely (internal agents, credentialed enumeration of known hosts), the product has become a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Vulnerability Management | closest operational neighbor; findings handoff | VM assesses a **known**, internally-enumerated host population (agents, credentialed scans) and manages CVE remediation. ASM's defining act is **discovering the target set from outside**. ASM findings are routinely exported into VM tools. |
| Cyber Asset Management | inventory sibling | CAM builds the asset inventory from **internal** integrations and agents. Remove the outside-in vantage point and ASM becomes CAM. |
| Digital Risk Protection | outside-in sibling | DRP monitors **brand abuse** (typosquatted domains, dark-web mentions, impersonation) rather than the organization's own infrastructure exposure. Remove the infrastructure inventory and ASM becomes DRP. |
| Threat Intelligence Platform | data sibling | TIP tracks **external** threats, actors, and infrastructure. ASM tracks the organization's **own** assets. Some platforms bundle both. |
| Security Ratings Platform | posture sibling | Ratings produce **third-party scorecards**; ASM operates a working inventory with a finding lifecycle for the organization itself. |
| Cloud Security Posture Management (CSPM/CNAPP) | cloud sibling | CSPM evaluates configurations **inside** connected cloud accounts. ASM observes exposure **from outside**; cloud connectors are the bridge, not the core. |
| DAST / Web Application Scanning | depth sibling | DAST deep-tests **known** web applications. ASM is breadth-first discovery of unknown surface; some ASM products bundle DAST as a second layer. |
| Breach & Attack Simulation | validation sibling | BAS **executes controlled attacks** to test controls. ASM passively observes exposure. |
| Penetration Testing Management | service sibling | PTM manages human engagements, scope, and reports. ASM is continuous automated observation. |
| Internet-wide search engines | substrate sibling | The same observation data without organization scoping or inventory management is a search engine, not an ASM product. |

The sharpest seam is with **Vulnerability Management**: the two share vocabulary (findings, severity, remediation) and interoperate constantly. The structural test: does the system's defining act include discovering previously unknown, externally reachable assets without internal access (ASM), or does it assess a known asset population (VM)?

## Representative Products

- **Microsoft Defender External Attack Surface Management (Defender EASM)** — suite-embedded EASM; recursive seed-based discovery with a five-state ownership model (approved / dependency / monitor-only / candidate / requires investigation)
- **Censys Attack Surface Management** — dataset-driven external ASM built on internet-scan data heritage; seeds, typed asset inventory (hosts, web entities, certificates, domains, storage buckets), evidence-linked risks
- **CyCognito** — pure-play external exposure platform; attacker-perspective positioning with "seedless" discovery claims and owner-linked remediation workflows
- **Detectify** — self-serve SaaS for smaller teams; root-asset-scoped Surface Monitoring plus optional deep Application Scanning
- **runZero** — inventory-first platform applying unauthenticated discovery to internal and external networks; asset/service/software/certificate inventories with curated findings

## Sources

Research date: **2026-09-06**

- Microsoft Learn — Defender EASM documentation: Overview; What Is Discovery?; Understand Inventory Assets — https://learn.microsoft.com/en-us/azure/external-attack-surface-management/
- Censys documentation: Get Started with Censys ASM; Seed Your Attack Surface; Inventory Assets; Risks — https://docs.censys.com/
- runZero documentation: What is runZero?; Understanding assets; Understanding findings; Managing ownership — https://help.runzero.com/docs/
- Detectify Knowledge Base: Assets and Root Assets; support-center category tree — https://support.detectify.com/
- CyCognito official site and platform pages (positioning-level) — https://www.cycognito.com/

> Sourcing limitation: CyCognito's product knowledge center is login-gated; evidence for that product is limited to official positioning pages, so no precise operational claims are made for it in this document. Precise vendor figures (risk-type counts, scan cadences, scoring mechanics) were observed in single-product documentation and are intentionally not generalized here; they remain in the paired Research Notes.
