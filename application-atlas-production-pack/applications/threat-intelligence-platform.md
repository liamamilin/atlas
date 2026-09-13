# Threat Intelligence Platform

## Overview

A **Threat Intelligence Platform** (TIP) is the security program's system of record for threat knowledge. It aggregates threat intelligence — indicators of compromise together with threat context such as threat actors, malware, campaigns, and attack techniques — from multiple external and internal sources into one persistent, curated knowledge base; it actively manages that knowledge through its lifecycle (deduplicating, enriching, prioritizing, and aging it); and it disseminates selected intelligence outward, into security controls such as SIEM, EDR, and firewall platforms and to the analysts who work threat detection, investigation, and response.

The problem it solves is not collection but operationalization. Raw threat data arrives fragmented across feeds, communities, vendors, and internal observations, in inconsistent formats, heavily duplicated, and decayingly stale. A TIP turns that stream into a governed knowledge base and delivers the relevant parts of it where they are consumed — the market's own shorthand for the delivered result is a continuously maintained "do not touch" list of hostile infrastructure, plus the context needed to judge and investigate it.

The boundary is knowledge versus operations: a TIP holds and distributes intelligence about threats; it does not itself collect the organization's event telemetry, decide on incidents, or execute response. When the primary object becomes the organization's own logs, alerts, or case files, the product is a different Application Type (SIEM, SOAR, Cyber Incident Response).

## Users & Context

Primary users are the people whose job is to know what threats exist and make the rest of the security program act on that knowledge:

- **Threat intelligence analysts** — the desk that runs the platform: connects and tunes sources, curates and enriches intelligence, investigates actors and campaigns, produces reports and briefings, and manages what is shared with external partners.
- **SOC analysts and incident responders** — consume rather than maintain: they look up indicators observed in alerts, pull context (who is behind this infrastructure, which campaign, how confident), and use the platform's verdicts to triage faster.
- **Threat hunters and detection engineers** — draw indicator sets and technique knowledge from the platform to hunt in the environment's own telemetry and to build detection rules.

Secondary users are security leadership (reports on the threat landscape), and — in community-oriented deployments — peer organizations: CSIRTs, sector ISACs, and national CERTs that exchange intelligence with each other through the platform.

The work context is a security operations center or a dedicated intelligence team. The platform typically runs as a SaaS service or a self-hosted instance, and its output must reach machines (detection and prevention tools) as well as people.

## Core Model

The defining core has four parts: multi-source aggregation, a curated threat knowledge base, lifecycle curation, and dissemination. Everything else the market associates with the category is layered on top of these.

```text
Sources: feeds · communities · vendor intelligence · internal observations
  ↓ ingested into
Threat knowledge base
  ├── Indicator of compromise (observable artifact: hash, domain, IP, URL, …)
  ├── Threat context (actors · malware · campaigns · techniques · vulnerabilities)
  └── Relationships & provenance linking them
  ↓ continuously curated
Deduplication · Enrichment · Prioritization · Aging
  ↓ disseminated to
Security controls (SIEM/EDR/firewall/SOAR) · Analysts · Sharing partners
```

### The defining core

- **Multi-source aggregation.** Intelligence is ingested from more than one channel: commercial and open-source feeds, sharing communities, vendor intelligence, government sources, and the organization's own observations. This is what separates the Type from a single intelligence feed: the market itself draws this line — a feed supplies data from one source, a platform brings many together and makes them usable as one body of knowledge. Without aggregation, the product is a feed client or a data vendor.
- **The threat knowledge base.** A persistent store of threat knowledge objects. The atomic object is the **indicator of compromise** — an observable artifact associated with malicious activity (file hashes, IP addresses, domains, URLs, email addresses, and product-specific structured types). Around indicators sit **threat context objects** — threat actors, malware families, campaigns, tactics/techniques/procedures, and vulnerabilities known to be exploited — and **relationships** connecting them ("this actor uses this malware, which communicated with this domain"), together with **provenance** (where each piece of intelligence came from). Without this memory, the product is a transient alert pipeline.
- **Lifecycle curation.** The store is actively managed, not just accumulated. Incoming data is normalized and **deduplicated** (the same observable reported by many sources becomes one record with multiple provenances), **enriched** with additional context (reputation, ownership, geography, sandbox verdicts), **scored or prioritized** for relevance and confidence, and **aged**: indicators go stale as infrastructure is taken down or burned, and mature products carry first-class freshness machinery — validity windows, decay rules, revoked states — so stale intelligence stops being distributed. Without curation, the store is an unusable dump; false positives and dead indicators poison every downstream control.
- **Dissemination to the security program.** Selected intelligence is pushed out to where it is used: into security controls (SIEM, EDR, firewall, SOAR, proxy) through integrations, feeds, and standard interchange formats; and to people through search, alerts on new relevant intelligence, and analyst-facing reports. Intelligence that is only stored — never delivered — is a research archive, not a platform.

### One structure, many implementations

The core is conceptual; products realize it differently, and the differences are variant axes rather than definitional:

```text
Concept:   Indicator of compromise
Realized as: hashes, IPs, domains, URLs, email addresses, structured
             object types; standalone records or embedded in event/report containers

Concept:   Threat context objects
Realized as: actor/malware/campaign/technique entities in a knowledge graph;
             clustered reference libraries (actor and malware "galaxies");
             typed group records (adversary, campaign, threat, incident)

Concept:   Interoperable interchange
Realized as: STIX/TAXII, community data formats, plain CSV/JSON feeds,
             REST/GraphQL APIs — the invariant is structured exchange, not one standard

Concept:   Relevance to this organization
Realized as: watchlists and priority intelligence requirements; owner and
             tag structures; confidence and rating scales
```

A reader who has only seen one implementation — say, a feed-aggregation console — should still be able to recognize a community-sharing platform or a graph-first intelligence product as the same Type.

## How It Works

The platform's operational loop runs continuously and has five phases.

### 1. Connect sources

The operator subscribes the platform to intelligence sources: feed endpoints (commercial, open-source, government), community sharing connections (trusted partner instances or sharing groups), vendor intelligence packages, and internal inputs — incident observations, analyst-written reports, imports from files, and outputs of adjacent tools such as malware sandboxes. Sources are configured once and then flow; each source remains identified so every record keeps provenance.

### 2. Ingest and curate

Ingested data is normalized into the platform's model and deduplicated: the same file hash reported by three feeds becomes one indicator carrying three source references. Enrichment attaches context to indicators — reputation, registration and geolocation data, verdicts from analysis services. New records receive whatever judgment metadata the platform carries (confidence or rating, tags, classifications) — assigned by the source, by the platform's scoring, or by the organization's own analysts, who can rate and tag intelligence themselves. Noise is filtered here: platforms deliberately prevent low-confidence intelligence from reaching downstream tools.

### 3. Analyze

The analyst explores the knowledge base: searching for indicators seen in an alert, pivoting across relationship links (this domain → the campaign it belongs to → the actor behind it → the other infrastructure attributed to the same actor), reading actor and campaign profiles, and judging how the intelligence relates to the organization. The platform expresses what the organization cares about — watchlists, priority intelligence requirements, or equivalent relevance configurations — so that new incoming intelligence can be matched against it, and analysts receive alerts when relevant intelligence arrives.

### 4. Disseminate

Curated intelligence leaves the platform through several channels: continuous synchronization into detection and prevention systems (SIEM, EDR, firewall, proxy), exports and feeds in standard interchange formats, APIs for automation and orchestration, and notifications to analysts. Human-facing outputs include reports, briefings, and dashboards on the threat landscape. The machine-facing delivery is the point: intelligence must arrive inside the controls where it blocks, detects, and enriches — without an analyst copying it by hand.

### 5. Share and age

Where the deployment includes external sharing, the organization contributes intelligence back — its own observations, sightings, and judgments — governed by distribution markings that state who may see what. Meanwhile the knowledge base ages: indicators pass their validity, lose their score under decay rules, or are revoked; expired intelligence stops flowing to controls. The loop is never finished — sources keep flowing, curation keeps running, and the disseminated picture keeps changing.

## Interfaces

Surfaces described conceptually; exact layouts and names vary by product.

### Intelligence workbench / dashboard

The analyst's entry surface. Purpose: show the state and freshness of the intelligence base.

- Typical information: indicator counts and trends, source health, recent notable intelligence, expired/stale statistics.
- Primary actions: search, open records, configure sources, set notifications.

### Indicator and object detail

The record surface for one indicator or context object.

- Typical information: the observable value and type, confidence/rating, sources and first/last-seen provenance, associations to actors/campaigns/malware, sightings and false-positive reports, lifecycle state (validity, decay, revoked).
- Primary actions: rate/confirm, tag, associate to other objects, add sightings or false positives, edit or revoke, check enrichment.

### Relationship / graph exploration

Investigation surface over the knowledge graph.

- Typical information: entities as nodes and their relationships as edges, expandable by pivoting.
- Primary actions: pivot from an indicator to its campaign and actor, expand related infrastructure, save an investigation view.

### Source and integration configuration

Administrative surface over the pipeline.

- Typical information: connected feeds/communities/connectors and their status, export/integration endpoints, enrichment services, aging and decay rules, exclusion lists.
- Primary actions: add or pause a source, configure an export to a control, tune aging rules, manage API keys.

### Alerts and reports

The human-facing delivery surfaces: notifications when new intelligence matches the organization's relevance configuration, and produced intelligence products — landscape reports, campaign briefings, stakeholder dashboards — for consumption beyond the analyst desk.

### Sharing administration

For community-connected deployments: what is shared with whom, under which distribution markings, and what peer organizations have contributed or proposed.

## Important Rules / Behaviors

### Intelligence decays, and the platform must show it

Unlike most reference data, threat intelligence has a shelf life: infrastructure disappears, malware families rebrand, indicators burn. Mature products therefore treat freshness as a first-class property — validity windows on indicators, decay rules that lower confidence or score over time, revoked states, and automatic removal of expired indicators from downstream distribution. The exact mechanisms vary by product; the property is structural.

### Provenance and judgment are user-visible

Every record carries where it came from and how much to trust it — source identity, confidence or rating, sightings (how often it was actually observed, by whom), and false-positive reports. Analysts both consume and produce this metadata: rating an indicator, confirming a sighting, or reporting a false positive is normal work that changes how the record is distributed.

### Deduplication and merging are continuous

Multiple sources report the same observable constantly. The platform must converge them into one record with multiple provenances — not a pile of duplicates — and handle conflicting judgments between sources. The quality of this machinery directly determines whether downstream tools receive clean or noisy intelligence.

### Distribution is governed

Outbound sharing is an explicit, scoped act: intelligence records carry distribution settings or markings (a common convention is traffic-light-style handling limits) stating which audiences may receive them; publication to a community is a deliberate step, not an automatic side effect of saving. Organizations can consume widely while contributing narrowly.

### Relevance is configured, not assumed

The platform does not treat all incoming intelligence as equally important. The organization declares what it cares about — sectors, geographies, technologies, named adversaries — and the platform matches new intelligence against that configuration to prioritize, alert, and filter. This configuration is what turns a general threat database into the organization's intelligence.

## Variants

The Type is realized in several recognizably different shapes:

- **Curated-intelligence-led service** — the vendor operates collection and analyst verification, delivering maintained, confidence-scored intelligence into the customer's workflow (a managed-intelligence posture common among large commercial platforms).
- **Aggregation-management platform** — the classic enterprise form: the customer subscribes to its own feeds, and the platform's job is aggregation, curation, and distribution of them.
- **Open-source community sharing platform** — self-hosted instances run by CSIRTs, ISACs, and enterprises, exchanging intelligence peer-to-peer with strong sharing governance; the community, not a vendor, is the source network (MISP is the reference form).
- **Knowledge-graph platform** — analysis-first form where the graph of entities and relationships is the primary surface rather than indicator lists.
- **Intelligence pillar of a wider platform** — threat intelligence packaged as one pillar of a broader security-operations suite, beside case management, automation, or exposure-management modules; case handling and playbook automation frequently appear here as embedded modules.
- **Managed intelligence service** — the vendor's analysts run the platform loop on the customer's behalf.

Common embedded modules inside TIP products — dark web monitoring, brand and digital-risk protection, malware sandboxing, case management — are packaging, not the defining structure: each has its own center of gravity and is bounded as a separate Application Type or module.

## Related Application Types

| Application Type | Distinction |
|---|---|
| SIEM | SIEM's defining substrate is the organization's own event telemetry, collected and correlated in-product; a TIP's substrate is threat knowledge about external and internal threat activity held as reusable intelligence objects. They integrate bidirectionally — TIP content enriches SIEM detections and investigations — but neither's core can replace the other's. |
| SOAR | SOAR is the orchestration engine that automates response workflows; a TIP supplies intelligence content into those workflows. Playbook automation inside a TIP is an embedded module, not the Type. |
| Threat Hunting Platform | Hunting interactively queries the organization's own security telemetry; a TIP holds no environment telemetry. A TIP serves hunts (what to hunt for), the hunting platform executes them (where to hunt). |
| Vulnerability Management | Manages the organization's own vulnerabilities and their remediation state; a TIP holds vulnerability knowledge as threat context (what is exploited in the wild) used to prioritize that work. Different unit of record. |
| Digital Risk Protection | DRP runs a protection loop over the organization's own external identity — standing detection of impersonation and abuse of its footprint, ending in takedown enforcement. A TIP has no protected subject and no enforcement path; brand-protection capability appears inside TIP suites only as an embedded module. |
| Dark Web Monitoring | A subject-bound watch over hidden/illicit sources for the organization's own exposure identifiers, alerting on findings. Inside a TIP, underground-source content is one source among many feeding program-wide knowledge — there is no subject-bound watchlist as the organizing object. |
| Cyber Incident Response Platform | Manages incident cases and the response lifecycle; a TIP manages threat knowledge. Intel-led products associate incident cases with adversary and indicator knowledge, and some platforms carry both pillars — as separate modules. |
| Malware Analysis Sandbox | Executes samples and produces verdicts and extracted indicators — an upstream intelligence source and enrichment service feeding TIPs. Its object of work is a sample; the TIP's is the knowledge base. |

The load-bearing boundary is the substrate test: SIEM, SOAR, and threat hunting all operate on the organization's own operational data and workflows; the TIP alone operates on threat knowledge as a managed, distributable asset.

## Representative Products

- **MISP** — open-source sharing-first platform; the reference form of community-operated threat intelligence sharing (CSIRT/ISAC deployments)
- **OpenCTI** — open-source knowledge-graph platform with a connector ecosystem; intelligence pillar of a wider threat-management suite
- **ThreatConnect** — commercial platform combining intelligence management with case management and playbook automation
- **Anomali ThreatStream** — commercial market-leading aggregation and curation platform, now also delivered in a managed-intelligence posture

The defining core was checked against older and community-operated forms (analyst-maintained indicator databases with manual exports into IDS/SIEM, and early national-CERT sharing instances) to avoid over-fitting the definition to current SaaS-era machinery.

## Sources

Research date: **2026-09-09**

- MISP — official project site: https://www.misp-project.org/
- MISP — official user guide (general concepts): https://www.circl.lu/doc/misp/
- OpenCTI — official documentation (home, data model, indicators lifecycle): https://docs.opencti.io/latest/
- Filigran / OpenCTI — official product site: https://www.opencti.io/en/
- ThreatConnect — official developer documentation: https://docs.threatconnect.com/en/latest/
- Anomali — ThreatStream Next-Gen product page: https://www.anomali.com/products/threatstream
- Anomali — "What is a Threat Intelligence Platform (TIP)?" glossary: https://www.anomali.com/glossary/tip-threat-intelligence-platform

> Sourcing limitations: the intelligence-led SaaS pole of the market could not be reached this pass (its support portal timed out; it was also unreachable during a sibling research pass), so that pole is documented only through its structural position in other vendors' integration ecosystems, and no claims are made from it. Commercial-product evidence is product-page and developer-documentation tier rather than end-user-guide tier; operational details such as exact scoring scales, decay parameters, and source counts are therefore intentionally not stated in this document. Detailed observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
