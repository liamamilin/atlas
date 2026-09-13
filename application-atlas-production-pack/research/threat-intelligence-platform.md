# Research Notes — Threat Intelligence Platform

## Research Goal

Understand what a Threat Intelligence Platform (TIP) actually is as an Application Type: what objects exist inside it, where its intelligence comes from, what happens to that intelligence between ingestion and consumption, who operates it, and where its boundaries sit against the neighboring security Types already documented in the Atlas (SIEM, SOAR, Threat Hunting Platform, Vulnerability Management, Digital Risk Protection, Dark Web Monitoring, Cyber Incident Response Platform, Malware Analysis Sandbox).

Two inherited flags to discharge from earlier passes:

- digital-risk-protection pass (2026-09-08): "TIP = curated knowledge about actors/IOCs/vulnerabilities for the security program (no protected footprint, no enforcement); DRP = protection loop over the customer's own external identity with enforcement... recommend the TIP pass treat brand/DRP capability as an embedded module, not a duplicate leaf."
- dark-web-monitoring pass (2026-09-07): "dark web monitoring commonly ships as a module of Threat Intelligence Platforms — recommend the threat-intelligence-platform pass treat it as an embedded capability, not a duplicate leaf."

## Initial Boundary (hypothesis before research)

- Core hypothesis: a TIP aggregates threat intelligence (indicators, actor/campaign/malware context, reports) from multiple sources into one managed store, curates it (dedupe, enrich, score, age out), and disseminates it to security controls and analysts. It is a knowledge-management system for threat intelligence, not a detection or response system.
- Users: threat-intelligence analysts, SOC analysts, threat hunters, detection engineers, incident responders, CSIRT/CERT teams.
- Nearest neighbors: SIEM (own telemetry), SOAR (response automation), Threat Hunting (querying own telemetry), DRP/DWM (protected-subject watches), CIRP (incident cases), Vulnerability Management (own vulnerabilities).
- Main unknowns: whether multi-source aggregation and dissemination are both definitional; where the Anomali-style "fuse with environment data" packaging drifts; how sharing communities fit the core.

## Research Questions

1. What are the core knowledge objects (indicators, observables, actors, campaigns, malware, TTPs, vulnerabilities, reports)?
2. What sources does intelligence arrive from, and how is ingestion realized (feeds, TAXII, connectors, manual, communities)?
3. What curation machinery exists (normalization, deduplication, enrichment, scoring/prioritization, decay/aging, false-positive control)?
4. How is intelligence analyzed (search, pivoting, graphs, actor profiles, dashboards)?
5. How is intelligence disseminated (SIEM/EDR/firewall/SOAR integrations, exports, APIs, feeds out, alerts, reports)?
6. How does sharing with external communities work (ISACs, trust groups, markings)?
7. What roles and permission structures exist?
8. Where is the boundary vs SIEM / SOAR / Threat Hunting / Vulnerability Management / DRP / DWM / sandbox / CIRP?
9. Which capabilities are market-common vs definitional vs vendor-specific?

## Representative Products

| Product | Pole / philosophy | Customer tier | Evidence layer |
|---|---|---|---|
| MISP | open-source sharing-first platform; community/event-centric; self-hosted | CSIRTs/CERTs, trust communities, self-hosting teams | A — misp-project.org + official CIRCL user guide |
| OpenCTI (Filigran) | open-source knowledge-graph-first platform; connector ecosystem | community + enterprise, government | A — official docs (multiple pages) |
| ThreatConnect | commercial platform; intelligence management + case management + app/playbook automation | enterprise | A — official developer docs (data model, API surface) |
| Anomali ThreatStream Next-Gen | commercial market leader; curated aggregation → fusion → operationalization; 2026 repositioned as "Managed Intelligence as a Service" | large enterprise | A — official product page + official glossary page |

Selection rationale: market representation (two commercial leaders, two dominant open-source platforms), different product philosophies (open sharing standard vs knowledge graph vs workflow platform vs curated service), different customer tiers (CSIRT community / self-hosted → enterprise), and coverage of both the aggregation-management pole and the intelligence-led pole. Recorded Future (the pure intelligence-led SaaS pole) was attempted once this pass (support.recordedfuture.com — timeout) and twice in the digital-risk-protection pass; per the network rule it was abandoned and is documented structurally only (it appears in the OpenCTI/Filigran connector ecosystem and the Anomali marketplace as a connectable intelligence source). No claims are made from it.

## Sources

- MISP — https://www.misp-project.org/ (fetched 2026-09-09)
- MISP user guide (official) — https://www.circl.lu/doc/misp/ and .../general-concepts/ (fetched 2026-09-09)
- OpenCTI documentation — https://docs.opencti.io/latest/ , .../usage/data-model/ , .../usage/indicators-lifecycle/ (fetched 2026-09-09)
- Filigran — https://www.opencti.io/en/ (fetched 2026-09-09)
- ThreatConnect developer documentation — https://docs.threatconnect.com/en/latest/ (fetched 2026-09-09)
- Anomali ThreatStream Next-Gen — https://www.anomali.com/products/threatstream (fetched 2026-09-09)
- Anomali glossary "What is a Threat Intelligence Platform (TIP)?" — https://www.anomali.com/glossary/tip-threat-intelligence-platform (fetched 2026-09-09)
- Unreachable: Recorded Future support portal (timeout; also unreachable 2026-09-08 pass)

## Product Observations

### MISP (evidence layer A — official site + official user guide)

- Self-description: "Open Source Threat Intelligence Platform & Open Standards For Threat Intelligence Sharing"; one-line verbs: "Share. Store. Correlate. Analyse."; "an open source software solution for collecting, storing, distributing and sharing cyber security indicators and threats"; "designed by and for incident analysts, security and ICT professionals or malware reversers".
- Core data model: **MISP core format** — Events contain Attributes (indicators); tagging; **taxonomies** (TLP, ATT&CK, estimative language, CSIRT classifications); **galaxies** (threat-actor, malware, tool clusters — MITRE ATT&CK, Ransomware, Exploit-Kit, Threat actor…); **MISP objects** (structured composites); default feeds list.
- Correlation engine: attributes correlate across events; users **pivot** from event to event through correlation links; visualization options "helping analysts find the answers".
- Sharing machinery (the product's signature): MISP **communities** of organizations; **synchronisation** between instances via push/pull with sync users; per-event/per-attribute **distribution settings**; a **publishing** step (event visible locally but not synchronised/exportable until published); **proposals** (other organizations propose corrections to an event, accepted by the creator org); delegation of events; **sightings**; email notifications on publish.
- Ingestion: **feeds management** (external feeds); manual event creation with templates; imports via modules.
- Exports/automation: "automated exports for IDS, or SIEM, in STIX or OpenIOC"; synchronize to other MISP instances; REST API (PyMISP); **ZeroMQ publish-subscribe**; scheduled TAXII push (release notes 2.5.42); scheduled tasks (caching exports, pull, push).
- False-positive control: **warninglists** (known-good lists to exclude values), noticelists.
- Enrichment: MISP modules (expansion/import/export) as autonomous extension services.
- Roles: org admins vs site admins; roles with granular permissions; instances hold data locally with distribution-based sharing.

### OpenCTI (evidence layer A — official documentation)

- Self-description: "an open source platform allowing organizations to manage their cyber threat intelligence knowledge and observables... to structure, store, organize and visualize technical and non-technical information about cyber threats."
- Core data model: **knowledge graph** — entities (nodes) + relationships (edges); based on **STIX 2.1** (SDO: Attack Pattern, Malware, Threat Actor…; SCO: IP address, domain, hash…; SRO: relationships, sightings); extensions for disinformation/cybercrime objects (channels, events, narratives).
- Ingestion: **connectors** (external import), streams, feeds (TAXII, RSS, CSV, JSON), file import (incl. AI document extraction), manual creation, form intake, analyst workbench, draft workspaces.
- Curation: dedicated **deduplication** and **merging** machinery; **reliability and confidence** attributes; rules engine / inferences; enrichment connectors; exclusion lists; data-consistency manager.
- Indicator lifecycle (first-class): `valid_from`/`valid_until` validity windows; **score decay rules** (score decreases over time; after expiry the indicator is marked revoked and its detection flag auto-set false); decay rules configured platform-wide, stored per indicator at creation. (Precise default score = 50: vendor detail, kept out of the final document.)
- Org-relevance configuration: **Priority Intelligence Requirements (PIR)** — exploring knowledge against the organization's stated priorities; custom dashboards; notifications & alerting; entity workflows.
- Analysis surfaces: overview, search, insights/summaries (AI), browsing by entity type (Analysis, Cases, Events, Observations, Threats, Arsenal, Techniques, Entities, Locations), **pivot and investigate**, graph relationships.
- Action surfaces: **case management** (cases as entity type), background tasks, **playbook automation**, security coverage.
- Dissemination out: **native feeds**, manual export, GraphQL API, data streaming.
- Governance: RBAC; **marking restrictions** (TLP-style data markings); **organization segregation** (multi-org platforms); retention policies; custom taxonomies; audit/activity.
- Ecosystem: Filigran XTM suite — OpenCTI is the "Cyber Threat Intelligence" pillar (G2 category "Threat Intelligence"); OpenAEV (adversarial exposure validation) and OpenCRQ (risk quantification) are siblings; connector library spans intel providers (Recorded Future, Mandiant, CrowdStrike, MISP, VirusTotal, OTX, Flashpoint, Shodan, GreyNoise…) and consumers (Splunk, Microsoft Sentinel, QRadar, Elastic, Defender, SentinelOne, ServiceNow, TheHive, Tines, Zscaler…).

### ThreatConnect (evidence layer A — official developer docs; layer B via sibling CIRP pass)

- Developer docs split the API into **"Threat Intelligence Endpoints"** and **"Case Management Endpoints"** — the product carries both pillars explicitly.
- Data model (v2 API): **Groups** (Adversary, Campaign, Document, Email, Incident, Signature, Threat), **Indicators** (EmailAddress, File, Host, IPAddress, URL, plus custom indicator types), **Owners** (organizations and communities — the sharing unit), **Tags**, **Attributes**, **Associations** (links between indicators/groups/victims/tasks), **Security Labels**, **Victims** + **Victim Assets**, **Tasks**, **Notifications**, **Playbooks**, **Batch API** for bulk indicator writes.
- Indicator metadata includes **rating and confidence** (sibling CIRP pass: "rating/confidence/threatAssess on indicators"); observations with **false-positive** reporting; activity log.
- Interoperability: **TAXII 1.x and 2.1 services**; Python/Java/JavaScript SDKs; **TcEx app framework** with app classes for **feed apps** (source name/category config), job apps, playbook apps — the integration/enrichment extension model.
- From the CIRP pass (consistent): ThreatConnect = "threat-intelligence platform with a dedicated case-management pillar associating incidents with indicators, victims, and task workflows"; owners = org/community.

### Anomali ThreatStream Next-Gen (evidence layer A — official product page + official glossary)

- Positioning: "The industry's leading threat intelligence platform (TIP) that provides curated access to the world's largest repository of curated threat intelligence." 2026 packaging: **"Managed Intelligence as a Service Powered by ThreatStream Next-Gen"** — an explicit three-step canonical flow on the product page:
  1. **Collect & Curate** — "Aggregate intelligence from hundreds of open, commercial, and community sources"; "Machine learning and analyst review normalize, deduplicate, and score continuously. Low-confidence noise never reaches your tools."
  2. **Fuse & Contextualize** — "External intelligence is fused with your environment context: your assets, your users, your event logs, your incident history"; "actor attribution, campaign mapping, and a confidence score your team can act on."
  3. **Operationalize** — "Push fused intelligence to detection tools, response playbooks, and AI agents automatically. Create detection rules, block malicious infrastructure."
- Use cases: threat-informed detection; accelerated investigation ("enrich alerts with full threat context"); AI-powered triage; **Intelligence Sharing** — "Distribute finished intelligence to ISACs, partners, and internal teams via Trusted Circles and STIX/TAXII"; proactive defense.
- Marketplace: purchasable threat-intelligence feeds and enrichment/analysis tools; SDKs.
- Customer quote (official page): "allows us to tag our own intelligence, apply confidence ratings, and collaborate with other intel sources."
- Official glossary page (the market's own category definition): "A threat intelligence platform (TIP) is a security technology that **collects, normalizes, enriches, analyzes, and shares cyber threat intelligence from multiple sources**." Four core functions listed: **threat intelligence aggregation** (commercial, open-source, government, community, internal sources); **normalization and enrichment** (standardize, deduplicate, score, add context); **security integrations** (SIEM, SOAR, XDR, EDR, firewalls); **analysis and sharing**. Managed intel types: tactical/operational/strategic/technical — "IOCs, malware information, threat actor profiles, campaigns, vulnerabilities, TTPs, and contextual intelligence." Users: "threat intelligence analysts, SOC teams, threat hunters, detection engineers, incident responders, and security leaders." Explicit **TIP vs feed** distinction: "A threat intelligence feed provides threat data from a specific source. A TIP brings together intelligence from multiple feeds and other sources, then normalizes, enriches, analyzes, and distributes that information." Delivered intelligence to controls framed as a "cyber no-fly list." Analysis features: explore threats, investigation workflows, context, indicator expansion/research, incident escalation, "producing intelligence products and sharing them with stakeholders."

## Cross-product Comparison

| Dimension | MISP | OpenCTI | ThreatConnect | Anomali ThreatStream | Strength |
|---|---|---|---|---|---|
| Multi-source aggregation | feeds + community sync + manual/API | connectors + streams + feeds (TAXII/RSS/CSV/JSON) + files + manual | feed apps via TcEx + TAXII + batch + manual | "hundreds of open, commercial, and community sources" + marketplace | **A×4 — definitional** |
| Knowledge objects: indicators + threat context | Events→Attributes + galaxies/taxonomies/objects | STIX 2.1 entities (Threat Actor, Malware, Attack Pattern, Indicator, Observable…) + relationships | Indicators + Groups (Adversary/Campaign/Threat/Incident…) + associations | "IOCs, malware, threat actor profiles, campaigns, vulnerabilities, TTPs" | **A×4 — definitional** |
| Curation: dedupe/normalize | correlation + warninglists; org-published events | deduplication + merging pages, data-consistency manager | batch writes, attributes/tags, owner model | "normalize, deduplicate, and score continuously" | **A×4 — definitional** |
| Scoring / prioritization | sighting/taxonomy-driven judgment; no vendor scoring engine on site pages | indicator **score** + decay; confidence/reliability | **rating + confidence** per indicator | "confidence-scored", "intelligence-driven prioritization" | **A×4 — common core machinery, exact models vendor-specific** |
| Aging / freshness | timestamps, warninglists, publish workflow | **valid_from/valid_until + decay rules + revoked state** | batch/observation updates (aging detail not on fetched pages) | "maintained continuously — not static feeds" | A×2 explicit machinery; A×2 posture-level — **aging is common core, mechanisms vary** |
| Enrichment | MISP modules (expansion/import/export) | enrichment connectors | TcEx apps, attributes | marketplace enrichment tools + in-product | **A×4 — standard** |
| Analysis surfaces | event view, pivoting on correlations, visualization | graph, search, PIR, dashboards, pivot & investigate | investigation workflows, associations, victims | explore/investigate, context that travels | **A×4 — standard** |
| Dissemination to controls | "automated exports for IDS/SIEM, STIX/OpenIOC", TAXII push, ZeroMQ, API | native feeds, streaming, API, connectors out | TAXII services, batch, SDKs, integrations per TcEx | "push to detection tools, response playbooks, AI agents automatically" | **A×4 — definitional** |
| Human-facing intelligence products | events + email notifications on publish | reports/analysis entities, dashboards, notifications | documents/signatures, reports | "intelligence products and sharing them with stakeholders", ISAC distribution | **A×4 — standard** |
| External sharing / communities | **the product's signature**: communities, push/pull, distribution settings, proposals, TLP taxonomies | organization segregation, marking restrictions, sharing/exports | **Owners = organizations/communities**, security labels | **Trusted Circles**, ISAC distribution, STIX/TAXII | **A×4 — common, deepest at MISP** |
| Case / incident handling | none first-class (events ≠ cases) | Cases entity type + case management | full **Case Management pillar** (cases, tasks, victims) | incident-history context, escalation workflows | optional/variant; product-shaped |
| Playbook automation | none | playbook automation page | Playbooks (v2 API) | "response playbooks" as push target | optional — SOAR seam |
| Environment-data fusion (own telemetry/assets) | none | none (separate products) | not on fetched pages | "fused with your environment context" | **single-product 2026 packaging drift — variant, not definitional** |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

```text
Multi-source threat intelligence aggregation
  (intelligence ingested from multiple external and internal sources —
   feeds, communities, vendor intelligence, own observations)
└── Curated threat knowledge base
    (persistent threat knowledge objects — indicators of compromise and
     threat context: actors, malware, campaigns, TTPs, vulnerabilities —
     held with relationships and provenance, as the security program's
     shared intelligence memory)
    └── Intelligence lifecycle curation
        (the store is actively managed: deduplicated, enriched with context,
         scored/prioritized for relevance, and aged out as it goes stale)
    └── Dissemination to the security program
        (selected intelligence is pushed out to security controls —
         SIEM/EDR/firewall/SOAR via integrations, feeds, exports —
         and surfaced to analysts via search, alerts, and reports)
```

Four properties. Removal tests:

- Remove multi-source aggregation → a single-feed downloader / data vendor. The TIP-vs-feed distinction is drawn by the market itself (Anomali glossary: "A threat intelligence feed provides threat data from a specific source. A TIP brings together intelligence from multiple feeds and other sources...").
- Remove the persistent curated knowledge base → a transient alert pipeline; no intelligence memory exists.
- Remove lifecycle curation → an unmanaged dump; indicator noise and staleness make it unusable for detection.
- Remove dissemination → a research library / archive nobody consumes; intelligence never reaches detection or analysts.

§24 historical check: pre-STIX-era CSIRT indicator sharing lists (email/portal distribution), analyst-maintained IOC databases with manual CSV export into IDS/SIEM, and early-2010s MISP instances synchronizing events between national CERTs all satisfy all four properties without STIX/TAXII, graph UIs, decay engines, SaaS, or AI. Regional CSIRT deployments, national CERT communities, and sector ISAC instances fit directly. The defining core survives the historical check; modern machinery (standards, graph, AI, SaaS) is implementation.

### L1 — Common Mature Structure

- **Enrichment framework** — extending each indicator/context object with third-party context (reputation, whois/geolocation, sandbox verdicts, passive DNS), realized as extension mechanisms in all sampled products (MISP modules, OpenCTI enrichment connectors, ThreatConnect TcEx apps, Anomali marketplace tools). (B)
- **Org-relevance configuration** — expressing what the organization cares about (watchlists/target profiles/PIR/owners/tags) so new intelligence can be matched and prioritized against it; notifications/alerts on relevant new intel. (B; OpenCTI PIR and Anomali prioritization explicit — A×2 — same machinery elsewhere in weaker form)
- **Investigation surfaces** — search, relationship/graph exploration, actor and campaign profiles, dashboards. (B)
- **Integration spine** — SIEM/EDR/firewall/SOAR/ticketing connectors; STIX/TAXII import and export; REST/GraphQL APIs; scheduled exports for detection systems. (B)
- **Sharing and trust machinery** — trusted groups/circles/communities (ISACs), data markings (TLP-style), and the ability to contribute intelligence back. (B; signature capability at MISP, present in all)
- **Intelligence products for humans** — reports, briefings, dashboards for stakeholders beyond the analyst desk. (B)
- **Roles and governance** — role-based access, organizational segregation, data markings, audit. (B)

### L2 — Variant / Optional Structure

- **Philosophy poles**: curated-intelligence-led (vendor operates collection and analysts; Anomali 2026 posture) ↔ aggregation-management platform (bring your own feeds; classic ThreatStream/ThreatConnect posture) ↔ open sharing platform (community-operated sync; MISP) ↔ knowledge-graph platform (OpenCTI).
- **Packaging**: standalone TIP ↔ intelligence pillar of a wider SOC platform (Filigran XTM; Anomali Agentic SOC) ↔ managed intelligence service (vendor analysts run the loop; Anomali 2026 packaging, DRPS-adjacent drift).
- **Deployment**: self-hosted open-source (MISP, OpenCTI) vs SaaS; community-operated instances for CSIRT/ISAC constituencies.
- **Sharing posture**: private internal store ↔ bidirectional community sharing (the MISP pole).
- **Embedded modules**: dark web monitoring, brand/DRP and takedown, attack-surface checks, sandboxing, case management, playbook automation — sold inside TIP suites as modules (per sibling passes and this sample: OpenCTI cases/playbooks; ThreatConnect cases/playbooks). Module ≠ defining structure.
- **Environment-data fusion**: fusing external intel with the customer's own assets/users/logs/incident history (Anomali 2026 packaging) — drifts toward the security-data-lake/SIEM seam; single-product framing; variant.
- **AI assistance**: AI summaries/insights, AI analysts, agentic triage (era-current; OpenCTI Copilot, Anomali Agentic AI).
- **Interoperability substrate**: STIX/TAXII dominant but not definitional — MISP carries its own core format and OpenIOC/STIX exports; the invariant is structured interchange, not one standard.

### L3 — Vendor-specific (research notes only; NOT in final document)

- MISP: event/attribute/object/galaxy/taxonomy/warninglist/noticelist vocabulary; proposals and delegation; publish permission workflow; site-admin vs org-admin split; ZeroMQ pub-sub; PyMISP; CTI-Transmute conversion service; scheduled TAXII push (2.5.42).
- OpenCTI: STIX 2.1-first model with extensions; GraphQL API; decay default score 50; "detection" flag semantics; PIR; analyst workbench/draft workspaces; CTI Copilot; Filigran XTM suite composition (OpenAEV/OpenCRQ/XTM One); G2 "Threat Intelligence" leader badges; SOC 2/ISO badges.
- ThreatConnect: Group taxonomy (Adversary/Campaign/Threat/Incident/Signature/Email/Document); Victims/Victim Assets; Owners as sharing units; Security Labels; rating/confidence/threatAssess fields; Playbooks; TcEx app framework with feed/job/playbook app classes; TC Exchange.
- Anomali: "Managed Intelligence as a Service" 2026 repositioning; "48–72 hours from IOC discovery to operationalized detection" and "60–70% analyst time saved" (marketing claims, single-source); Anomali Match™/Lens™ trademarks; Trusted Circles; STAXX (free STIX/TAXII utility); Anomali Marketplace; "world's largest repository of curated threat intelligence" claim; "thousands of sources" vs "hundreds of open, commercial, and community sources" (inconsistent marketing phrasing across pages).
- Recorded Future: no direct evidence this pass or the DRP pass (4 timeout attempts total); structural position only — appears as a connectable intelligence source in OpenCTI's and Filigran's integration ecosystems and Anomali's marketplace. Nothing asserted from memory.

## Rejected Findings

- **"TIP = STIX/TAXII machinery."** Rejected as definition: MISP's own core format and export set, plus generic feed/CSV/JSON ingestion, show the invariant is structured multi-source interchange, not one standard. STIX/TAXII is the dominant realization.
- **"TIP must include case management."** Rejected: strongest at ThreatConnect (a dedicated pillar) and present in OpenCTI (cases), absent as a first-class object in MISP. Optional/module.
- **"TIP must include dark web monitoring or brand protection."** Rejected as definitional per the dark-web-monitoring and digital-risk-protection passes: module-level bundling; the TIP core has neither a protected-subject watchlist nor an enforcement path.
- **"TIP must fuse the customer's own telemetry/assets."** Rejected: single-product 2026 packaging (Anomali); contradicts the hunting/SIEM boundary and the historical check.
- **"Scoring engines with numeric scales are definitional."** Rejected in that form: scoring/prioritization is common core machinery, but exact scales/decay parameters are vendor implementations (OpenCTI decay rules, ThreatConnect rating+confidence, Anomali ML scoring). Final doc keeps the concept, drops the numbers.
- **"A TIP is defined by producing finished strategic reports."** Rejected: human-facing intelligence products are standard, but the defining object base is the indicator/context knowledge base; strategic-reporting depth is product posture.

## Boundary Findings

| Neighbor | Test / distinction | Status |
|---|---|---|
| **SIEM** (processed) | SIEM's defining substrate is the organization's own event telemetry collected and correlated in-product; TIP's substrate is threat knowledge about external/internal threat activity held as reusable intelligence objects. Removal tests: remove the org's own log collection/correlation engine → TIP; remove external threat-knowledge aggregation/curation → SIEM with enrichment. Bidirectional integration is the integration spine, not identity. | Held (consistent with siem.md's "everything else" framing) |
| **SOAR** (processed) | SOAR = playbook/orchestration engine over response workflows; TIP = intelligence content store feeding those workflows. TIPs may bundle playbooks (ThreatConnect, OpenCTI playbook automation) — module, not core. | Held |
| **Threat Hunting Platform** (processed) | Hunting's defining substrate is the org's own security telemetry queried interactively; the hunting pass's own removal test states removing environment data leaves "an intel feed." A TIP serves hunts (indicators to hunt on) but holds no environment telemetry. | Held — reciprocally confirmed |
| **Digital Risk Protection** (processed; inherited flag) | DRP = protected external footprint + standing abuse detection + takedown enforcement; TIP = program-wide threat knowledge with no protected subject and no enforcement path. Brand/DRP capability appears inside TIP suites as an embedded module (market-structure evidence from the DRP pass; OpenCTI/Filigran module pattern). Flag DISCHARGED from this side: keep-both, module-level straddle; recommend joint review only if a standalone TIP-branded enforcement product surfaces. | DISCHARGED — keep-both ratified |
| **Dark Web Monitoring** (processed; inherited flag) | DWM = subject-bound watchlist + standing underground-source watch + exposure findings + alerts; inside a TIP, underground/dark-web content is one source among many feeding program-wide knowledge, with no subject-bound watchlist as the organizing object. Both dark-web-pass TIPs realized it as a module/solution — embedded capability, not duplicate leaf. Flag DISCHARGED from this side. | DISCHARGED — keep-both ratified |
| **Vulnerability Management** (§15 sibling) | VM's unit of record is the org's own vulnerabilities and their remediation state; a TIP holds vulnerability knowledge (exploited-in-the-wild context) as threat context objects. Overlap: intelligence-driven vulnerability prioritization uses TIP content inside VM workflows. | Held (brief; VM pass not re-read this session) |
| **Malware Analysis Sandbox** (processed) | Sandbox executes samples and produces verdicts/IOCs — an upstream intel source and enrichment service feeding TIPs; its object of work is a sample, not a knowledge base. | Held |
| **Cyber Incident Response Platform** (processed) | CIRP = incident case lifecycle; TIP = threat knowledge. Intel-led products associate incident cases with adversary/indicator knowledge (CIRP pass documents ThreatConnect as exactly this hybrid). Cases inside a TIP = module. | Held — consistent with CIRP pass |
| **Security data lake / agentic-SOC packaging** (drift orbit) | Anomali's 2026 framing fuses intelligence with the customer's environment data (assets/users/logs/incident history) — this drifts toward SIEM/data-lake territory. Recorded as packaging drift of one vendor; the canonical TIP core does not include holding the org's telemetry. | Recorded — no directory change |

## Taxonomy Note

No alias/duplicate problem: "Threat Intelligence Platform" is a market-recognized category (vendor product pages, G2 category "Threat Intelligence", the Anomali glossary entry). The directory leaf holds a real, distinct Type. The two inherited joint-review flags (DRP, DWM) are discharged above with module-level seams; no new flags requiring directory changes.

## Uncertainties

1. Recorded Future unreachable this pass and in the DRP pass (timeouts ×4 total). The intelligence-led SaaS pole is therefore evidenced only structurally; the sampled commercial poles (ThreatStream, ThreatConnect) carry that side. No claims made from memory about it.
2. Anomali evidence is product-page + glossary tier; docs.anomali.com was not fetched. Operational detail (feed counts, Match mechanics, exact integration list) is not asserted.
3. ThreatConnect evidence is developer-docs tier (data model/API); the admin console's day-to-day UI workflows were not directly observed this pass; the CIRP pass's developer-docs observations corroborate.
4. MISP/ThreatConnect aging machinery is thinner in direct evidence (MISP relies on timestamps/warninglists/publish workflow; ThreatConnect aging not on fetched pages). "Aging as common core" rests on A×2 explicit (OpenCTI decay, Anomali continuous-curation posture) plus the domain's universal staleness problem; written with moderate wording in the final document.
5. Exact scoring models, decay parameters, feed counts, and confidence scales are vendor-specific and excluded from the final document.

## Final Synthesis

A Threat Intelligence Platform is the security program's threat-knowledge system of record: it aggregates threat intelligence from multiple external and internal sources into one persistent, curated knowledge base of indicators and threat context (actors, malware, campaigns, TTPs, vulnerabilities) with relationships and provenance; it actively manages that store (deduplication, enrichment, scoring/prioritization, aging of stale intelligence); and it disseminates selected intelligence outward — into security controls (SIEM/EDR/firewall/SOAR) via integrations, feeds, and standard interchange, and to analysts via search, alerts, reports, and sharing communities. Around this core, mature products add enrichment frameworks, org-relevance configuration, investigation graphs, dashboards, trust-group sharing, roles/markings, and human intelligence products; packaging spans standalone platforms, pillars of wider SOC suites, managed services, and community-operated open-source instances. The Type is separated from SIEM/SOAR/Threat Hunting by the substrate (threat knowledge, not the org's own telemetry/workflows), from DRP and Dark Web Monitoring by the absence of a protected subject and enforcement/watchlist core (their capabilities appear as embedded modules), from Vulnerability Management by the unit of record (threat knowledge vs the org's own vulnerabilities), and from sandboxes and incident-response platforms by the object of work (knowledge base vs samples and incident cases).
