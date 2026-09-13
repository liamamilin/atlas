# Research Notes — Cyber Asset Management

Research date: 2026-09-07

## Research Goal

Understand what a Cyber Asset Management (CAM) application actually is and how it works, from real products: what counts as a "cyber asset", how the inventory is built and kept current, what users do with it, and where its boundary lies against IT Asset Management, CMDB, Attack Surface Management, and Vulnerability Management.

## Initial Boundary (hypothesis before research)

- Core use: a continuously maintained, security-oriented inventory of an organization's technology estate (devices, cloud resources, identities, software, SaaS, OT/IoT), used to answer "what do we have, what's exposed, what's unprotected, what matters most".
- Primary users: security teams (asset/exposure management, SecOps), with IT operations and compliance as secondary.
- Nearest neighbors: ITAM (financial/lifecycle orientation), CMDB (service-oriented configuration records), ASM (external attacker view), Vulnerability Management (finding-centric), CSPM/DSPM (domain-specific posture).
- Unknowns at start: aggregation vs discovery as the dominant inventory-building mechanism; depth of relationship modeling; lifecycle rules; how far the category drifts into exposure management.

## Research Questions

1. What entity classes does the "cyber asset" population cover?
2. How is the inventory assembled and refreshed (adapters/integrations vs active/passive discovery vs agents)?
3. What is the central object, and how do multiple sources converge on one record (dedup/correlation keys)?
4. What attributes/enrichment does an asset record carry (identity, exposure, ownership, criticality, lifecycle)?
5. What do users do with the population (queries, coverage gaps, prioritization, compliance, incident response)?
6. How are relationships between assets modeled, if at all?
7. What rules matter (merge keys, offline/staleness, risk-vs-criticality, source conflicts, suppression)?
8. How does the population flow outward (tickets, SIEM, CMDB sync)?
9. Where are the boundaries vs ITAM / CMDB / ASM / Vulnerability Management?

## Representative Products

Selected for market representativeness, documentation quality, distinct product philosophies, and distinct customer tiers:

| Product | Philosophy | Tier / segment |
|---|---|---|
| Axonius | Aggregation-first: normalize/correlate data fetched from existing security & IT tools via adapters; SaaS; the product most associated with naming the CAM/CAASM category | Enterprise |
| runZero | Discovery-first: high-speed active scanning + passive sampling + API integrations; SaaS or self-hosted; exposure-management positioning | Mid-market → enterprise; MSSP guidance exists |
| Lansweeper | Sensor-based deep inventory: IT/OT/traffic sensors + agent + cloud APIs; credential-free recognition; long heritage in IT inventory now security-positioned ("Cyber Asset Intelligence") | SMB → enterprise (30,000+ environments claimed) |
| JupiterOne | Graph-first: entity-relationship graph over ingested resources, query language (J1QL), compliance/controls angle | Cloud-native enterprise; compliance-heavy orgs |

## Sources

All fetched 2026-09-07.

- Axonius (Tier 1 docs): https://docs.axonius.com/ (landing), https://docs.axonius.com/docs/cyber-asset-management , https://docs.axonius.com/docs/asset-cloud/llms.txt (section index), https://docs.axonius.com/docs/adapters-list.md , https://docs.axonius.com/docs/queries.md
- runZero (Tier 1 docs): https://www.runzero.com/docs/ (platform), https://help.runzero.com/docs/understanding-assets/ , https://help.runzero.com/docs/asset-risk-and-criticality/
- Lansweeper (Tier 2 official product pages): https://www.lansweeper.com/ , https://www.lansweeper.com/product/asset-discovery/
- JupiterOne (Tier 2 site + Tier 1 docs): https://jupiterone.com/ , https://docs.jupiterone.io/ , https://docs.jupiterone.io/data-model/jupiterone-data-model

Note: Lansweeper evidence is from official product/marketing pages (Tier 2), not a help center; operational claims from those pages are treated as vendor-stated and calibrated accordingly. JupiterOne evidence mixes the official site (positioning) with the official documentation site (data model — Tier 1).

## Product Observations

### Axonius (evidence layer A unless noted)

- Platform self-branded "Axonius Asset Cloud"; docs structure splits into **Asset Intelligence** (Cyber Assets, Exposures, Identities, SaaS Applications, Software Assets) and **Actionability** (Queries, Enforcements, Workflows, Dashboards, Findings Center, Cases, Reports, Asset Graph).
- Cyber Assets page: "Ensure every asset across every system is known, compliant, and protected… Axonius continuously collects, normalizes, and enriches your cyber asset data to give you a complete and trusted view of your entire technology footprint and attack surface." Framed as "step up from a static asset inventory to dynamic asset intelligence".
- Adapters: "To aggregate and correlate asset data, Axonius securely fetches data from your IT, Security, and business solutions using pre-built integrations with hundreds of security and management solutions, known as adapters." Adapter table filterable by solution category and "Types of Assets Fetched".
- Queries: "Axonius uses a sophisticated set of highly detailed queries to understand how assets adhere to their policies… Queries are the basis for many Axonius capabilities, such as Dashboards, Reports, and Enforcement Sets." Query Wizard (basic + advanced modes); saved queries; multi-level queries on Vulnerabilities and Software pages.
- Asset Cloud section index reveals the asset-class workspaces and enrichment machinery:
  - Agent Coverage (out-of-the-box visibility into agent deployment status across security tools), with dashboards, issues/actions, initial policies.
  - Device Inventory Classification (structured methodology page for classifying device inventory).
  - Asset Business Context, Business Units, Device Ownership, Device Lifecycle Status.
  - Exposures: Security Findings (specific CVEs on specific assets), Aggregated Security Findings, Vulnerability Repository, Exclusion Rules, Risk Score (create/preview/view; out-of-the-box risk score), Asset Criticality Management, Axonius Vulnerability Score (AVS, AI-assisted), Exposure Overview Workspace, Vulnerability Enrichment, Threat Intelligence, Exception Management (approval workflows), SLA Management, External Exposures (+ workspace), Remediation Ownership (rules mapping findings to teams), Recommended Actions (prioritized to-do list; tickets).
  - SaaS Applications: discovery workspace, posture workspace, licenses, expenses, extensions, keys, activities.
  - Software Assets: software catalog, approval list/registry, versions view; enrichment from ServiceNow CMDB data.
  - Identities: Identity & Access workspace, role mining simulator, entitlement consolidation, access-review campaigns, auto-revocation and guardrails.
  - Cyber-Physical Assets: IoT devices, OT devices, IoMT (medical) devices, Network Inspector devices, IoT/OT Discovery Workspace, Medical Devices Management Workspace, Device Intelligence Hub, Device Scan Jobs (query-based and IP-address-based scanning), scan fetch history.
- Asset Graph: "See the connections between all the assets in your inventory."
- Enforcements: "Use actions to automatically enrich data, create tickets, and remediate policy gaps."

### runZero (evidence layer A unless noted)

- Platform definition: "runZero is an attack surface and exposure management platform that helps you see everything on your network, from managed IT systems to unmanaged OT, IoT, cloud, mobile, and remote assets. It combines high-speed active scanning, passive discovery, and API integrations to build a unified, continuously updated inventory you can trust."
- Architecture: hosted (SaaS) or self-hosted Console(s); distributed **Explorers** ("lightweight services at your points of presence"); CLI for offline collection/automation; MCP interface documented.
- Discovery: active scanning (scan templates, credential-based scanning, SNMP, custom fingerprints, autonomous discovery, gap identification), passive traffic sampling; IoT/OT scanning guidance; protocol/port documentation.
- Inbound integrations: cloud (AWS incl. EC2 enrichment, Azure, GCP), EDR (CrowdStrike, SentinelOne, Microsoft 365 Defender), vulnerability scanners (Tenable family, Qualys VMDR, Rapid7 InsightVM/Nexpose), identity/directory (Active Directory, Entra ID, Intune, MECM, Miradore, Google Workspace), CMDB (NetBox), external data (Censys, Shodan), OT (Dragos), virtualization (VMware), network (Meraki, Palo Alto), Tanium, Tailscale, Prisma Cloud; custom integration scripts (Starlark).
- Outbound integrations: Jira, Jira Service Management/Insight, ServiceNow Service Graph, Splunk, Sumo Logic (asset export + alerting), Panther, Tines, SecurityGate, Thinkst Canary.
- Inventory keyword classes (queryable): assets, services, software (groups + instances), vulnerabilities (groups + instances), certificates, wireless, users, groups.
- Asset model ("Understanding assets"): "runZero treats assets as unique network entities… An asset may have multiple IP addresses, MAC addresses, and hostnames and it may move around the network… runZero tries hard to follow assets by correlating new scan data with the existing inventory, using multiple attributes." Asset always belongs to exactly one **site**; the same system covered by multiple sites is treated as different assets (site-scoped correlation).
- Lifecycle: after each scan, unmatched systems become new assets; assets not found are **marked offline**; substantial fingerprint change (e.g., new NIC + firewall enabled) → old asset offline + new asset created; duplicates "usually marked as offline, and can be safely ignored or removed from the inventory by hand".
- Asset fields: primary/secondary addresses (secondary addresses "critical when trying to identify systems that bridge networks that should be isolated"), hostnames (DNS/PTR/probe-advertised), OS (fingerprint or guess), type, **category** (IT / OT / IoT — derived from device type, vendor, service protocols; e.g., Modbus/CIP/S7Comm → OT; manually overridable), **functions** (multi-valued OT-oriented labels: Process Control, Safety, Human Interface, Engineering, Monitoring, Environmental, Communications, Networking, Remote Access, Data Management, Power Management, Physical Security, Cyber Security, Management), hardware, MAC addresses, services (~100 TCP by default + UDP), RTT, detected-by, alive status, first seen, last seen, explorer, **outlier score** (0–5 heuristic for how unusual an asset is vs the rest of the inventory).
- Risk & criticality: **risk** is assigned automatically, "inferred from the risk associated with vulnerabilities or risky configurations on that asset", defaults to `none`, may come from the ingested vulnerability-management solution, overridable; **criticality** is assigned manually, defaults to `unset`, denotes importance to the organization (example given: database/web servers `critical`, end-user systems `medium`). Assignment via inventory (query-filter → bulk modify) or via alert rules (rule type `asset-query-results`, action "Modify asset", applied after scans). Asset risk report grouped by criticality, sorted by risk, exportable (JSONL/JSON/CSV), top vulnerabilities per asset (0–20).
- Data analysis surfaces: dashboards, AI Threads, inventory views, findings, certificates inventory, geolocation, ownership management, tasks, goal tracking, suppression, network segmentation view, fingerprints, alerts + rules engine, full search query syntax with saved/automated queries.
- Reports: Network Map, World Map, RFC 1918 coverage report, External Assets report, Site Comparison, Switch Topology, Network Bridge, Asset Route Pathing.
- Playbooks: "Building your complete asset inventory", "Finding gaps in endpoint protection", "Finding gaps in vulnerability scanning", "Achieving RFC 1918 coverage", OT scanning, MSSP guidance.
- Compliance alignment pages: CIS CSC, CISA BOD 23-01, C2M2, CMMC, ISO/IEC 27001, NERC CIP, NIST CSF, PCI DSS.
- Access model: organizations → sites hierarchy; user groups; SSO; external users; licenses (asset-count-based licensing).

### Lansweeper (evidence layer A for vendor-stated mechanics on official product pages; Tier 2 — no help-center fetch)

- Self-positioning: "Cyber Asset Intelligence" platform; "Total Asset Visibility For Every IT and Security Decision"; "one shared, trusted view across IT, OT, cloud, and IoT"; See / Know / Act framing:
  - See: "Continuously discover and classify every asset across IT, OT, cloud, and IoT — managed, unmanaged, and shadow — without manual effort."
  - Know: "Normalize and apply context, vulnerability data, and lifecycle signals to assess risk, forecast spend, and surface optimization opportunities."
  - Act: "Deliver trusted asset intelligence to ITSM, CMDB, and security tools so actions are accurate, scoped, and prioritized."
- Discovery mechanisms (product page): IT Sensor (passive detection on by default; credentialed active scanning adds installed software and config detail), OT Sensor (same model tuned for segmented industrial networks, "without touching the devices themselves"), Traffic Sensor (SPAN/RSPAN/ERSPAN/TAP/packet broker; adds application dependencies, service relationships, east-west patterns), IT Agent (Windows/macOS/Linux for laptops that rarely return to the corporate network), Cloud APIs (AWS, Azure, Google Cloud — VMs, containers, managed services).
- Identification depth ladder: **Detected** (passive: MAC + IP, type Unknown) → **Recognized** (credential-free ML fingerprint matched against a library of "175M+ devices" → manufacturer, model, OS) → **Fully Profiled** (credentialed active scan → installed software, configuration, lifecycle stage, vulnerability context).
- Reconciliation: "The same device gets found by more than one system. Lansweeper matches on MAC, serial, and hostname, never IP, and merges them into one record that lists every contributing source… Your total asset count may go down, but that is the correct answer."
- Currency: "New scans are evaluated against existing records continuously, not on a quarterly cycle. A device that moves to a new IP stays the same asset."
- Coverage honesty: "IP Range Coverage reports how much of each segment is identified, including what is not" — named IP ranges, per-segment identification completeness.
- Unmanaged/shadow devices: detect and classify as they appear; alert when a device joins the network; "shorten the window between a device appearing and being accounted for".
- Enrichment: lifecycle stage, vulnerability context, risk scoring; AI Usage Tracking (early access) bringing AI tools/models into the inventory.
- Outbound: Jira Service Management, HaloITSM, ServiceNow CI Synchronizer, Freshservice, TopDesk, ConnectWise (ITAM), Microsoft Sentinel, Splunk, Armis data connector.
- Use cases: Total Visibility; Coverage, Drift, and Exposure ("continuously verify control coverage, detect drift"); Risk to Remediation (findings → structured IT workflows with ownership); Zero Trust & Segmentation ("controls only scale when asset classification is accurate and current").
- Audience framing: "Where IT & Security Meet" — IT teams run operations, security teams see risk, on the same asset data.

### JupiterOne (evidence layer A for docs, A/B for site)

- Positioning: "JupiterOne unifies assets, security, and compliance in one platform, exposing and prioritizing hidden risks across cloud, code, identity, and AI." Solutions list includes **CAASM**, exposure management, vulnerability prioritization, control management.
- Graph-native model: "All JupiterOne products use one graph-native model, so every finding reflects your full environment—no silos or reconciliation needed." "Unified asset graph — Everything connects in a single graph. Every change shows up everywhere instantly."
- Data model (docs, Tier 1): "The JupiterOne Data Model is a reference model that illustrates digital resources and their complex interconnections across all ingested resources of an organization within an entity-relationship graph."
  - **Entity** = node representing a resource; each has a source-specific **type** (e.g., `aws_instance`, `aws_s3_bucket`) and an abstract **class** (e.g., `Host`, `DataStore`, `User`). ~100 defined classes: Device, Host, Workload, Container, Cluster, Network, Gateway, Firewall, DataStore, Database, CodeRepo, Application, User, Person, UserGroup, Account, AccessRole/Policy/Key, NHI (non-human identity), Secret, CryptoKey, Certificate, Vulnerability, Weakness, Finding, Risk, Control, ControlPolicy, Standard, Framework, Incident, Alert, Domain/DomainZone/DomainRecord, IpRange, Internet, Root, etc.
  - Common entity properties include: `classification` (data sensitivity), `criticality` (1–10), `risk` (1–10), `trust` (1–10), `complianceStatus`, `status` (e.g., Active/Inactive/Decommissioned), `active`, `public`, `temporary`, `validated`, `trusted`, `createdOn/updatedOn/deletedOn/discoveredOn/expiresOn`, `createdBy/updatedBy/deletedBy/discoveredBy`, `owner`, `tags`, `notes`, `webLink`.
  - **Relationships** = edges with generic verb classes: HAS, CONTAINS, IS, OWNS, USES, CONNECTS, TRIGGERS, EXTENDS, IMPLEMENTS, MITIGATES, MANAGES, EVALUATES, MONITORS, PROTECTS, TRUSTS, ASSIGNED, IDENTIFIED, PROVIDES, DEPLOYED TO, EXPLOITS, IMPACTS, PERFORMED, COMPLETED, OPENED, CONTRIBUTES TO. Relationships carry their own properties — e.g., Vulnerability `IMPACTS` resource carries `identifiedOn`, `remediatedOn`, `remediationDueOn`, `issueLink` (the finding record lives on the relationship).
  - Severity normalization: ingested findings normalized to `j1_severity` (originals kept in raw properties).
  - Special singleton entities: `Everyone`, `Internet` (Network with CIDR 0.0.0.0/0), `Root`.
- Query: **J1QL** ("One query language across your environment"); natural-language AI asking on top; example: `find Finding with j1_severity = "high"`.
- Products built on the graph: UVM (Unified Vulnerability Management — dedupe vulnerabilities across cloud/code/identity/endpoints; prioritize by exploit paths; owner-aware routing), AI ASM (see every cloud, SaaS tool, AI integration — approved/shadow; "continuously discovered, relationship-aware, and queryable"), CCM (Continuous Controls Monitoring — evaluate controls against live technical data; map to SOC 2/DORA/CIS).
- Integrations: 200+ (Slack, SentinelOne, Kubernetes, Snowflake, Salesforce, GitHub, Splunk, Google Cloud shown).
- Competitive framing (vendor-stated): "If you're running an asset inventory tool… You'll see a list of what you have. You won't see how those assets connect… Relationships are what turn an inventory into risk insight."
- Audience: CISO, Security Architect, SecOps & Analysts, Compliance.

## Cross-product Comparison

| Dimension | Axonius | runZero | Lansweeper | JupiterOne |
|---|---|---|---|---|
| Self-positioning | Asset Cloud / asset intelligence ("known, compliant, protected") | Attack surface & exposure management platform | Cyber Asset Intelligence | Unifies assets, security, compliance (CAASM solution) |
| Inventory assembly | Adapter fetches from existing tools ("hundreds" of integrations) | Active scanning + passive sampling + API integrations | IT/OT/Traffic sensors + agent + cloud APIs | Integration ingestion (200+) into graph |
| Central object | Normalized/correlated cyber asset (devices, users, SaaS, software, findings, cyber-physical) | Asset = unique network entity, site-scoped | One merged record per asset | Entity node (type + class) in relationship graph |
| Dedup/identity resolution | Correlation engine across adapters (vendor-stated "normalizes") | Correlation across scans via multiple attributes; offline marking | Merge on MAC/serial/hostname, "never IP"; lists contributing sources | Entity keying by integration; type/class layering |
| Asset classes | Devices, users/identities, SaaS apps, software, vulnerabilities/findings, IoT/OT/IoMT | Assets, services, software, vulnerabilities, certificates, wireless, users, groups | IT/OT/cloud/IoT devices (+ users, software implied by profile depth) | ~100 classes incl. cloud resources, code, identity, data, controls, findings |
| Security enrichment | Agent coverage, security findings, risk scores, AVS, asset criticality, threat intel | Vulnerability ingestion, risk (auto) + criticality (manual), outlier score | Vulnerability context, risk scoring, lifecycle stage | Findings/vulnerabilities as entities; criticality/risk/trust properties; exploit paths |
| Coverage-gap machinery | Agent Coverage hub | RFC 1918 coverage report, scan-gap identification, endpoint-protection gap playbook | IP Range Coverage ("including what is not") | Control evaluation (CCM) |
| Query surface | Query Wizard, saved queries, queries as basis of dashboards/reports/enforcements | Search query syntax, saved/automated queries, query library | (not directly evidenced — Tier 2 gap) | J1QL + natural language |
| Relationships | Asset Graph ("connections between all assets") | Network map, route pathing, switch topology, segmentation | Traffic sensor: application dependencies, service relationships, east-west patterns | First-class relationship graph with typed edges |
| Action layer | Enforcements (enrich, tickets, remediate), Workflows, Cases | Alert rules, tasks, goals, exports, outbound integrations | Findings → ITSM workflows; integrations to ITSM/SIEM/CMDB | Owner-aware routing (UVM), control monitoring (CCM) |
| Compliance | Policy adherence queries, exception/SLA management | Framework alignment pages (CIS, NIST CSF, ISO, PCI, CMMC, NERC CIP, CISA BOD) | Audit-ready inventory claims, NIS2/DORA framing | CCM: controls mapped to SOC 2/DORA/CIS; complianceStatus property |
| Deployment | SaaS | SaaS or self-hosted; Explorers on-prem | Sensors on-prem + cloud; free trial SaaS | SaaS |
| Hierarchy | (workspaces) | Organizations → sites | (not evidenced) | Workspace |
| Audience | Security (asset/exposure) teams | Security teams, MSSPs | IT + Security jointly | CISO/architect/SecOps/compliance |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the product is not recognizable as Cyber Asset Management:

1. **Cyber-asset population** — a standing set of records, one per identified asset of the organization's technology estate, spanning more than one asset class (devices at minimum; mature products span cloud resources, identities, software/services).
2. **Environment-derived assembly** — the population is created and refreshed automatically from data observed in or ingested from the environment (network observation, API ingestion, agents), not hand-maintained. The system, not a person, keeps the population current.
3. **Asset identity resolution** — multiple observations and multiple sources converge on one record per real asset (correlation/merge/dedup across scans and sources).
4. **Security-decision orientation** — the population and its attribute vocabulary exist to answer security questions (what exists, what is exposed, what is unprotected, what matters most) and to feed security workflows (gap analysis, prioritization, response, compliance evidence).

Test: remove (1) → no product; remove (2) → a manually curated register/CMDB-style documentation tool; remove (3) → a raw data aggregator, not an inventory; remove (4) → IT Asset Management.

### L1 — Common Mature Structure

Present across the researched sample (evidence layer B):

- Multi-source ingestion breadth: connectors/adapters to EDR, vulnerability scanners, cloud APIs, directory/identity, MDM, CMDB, external attack-surface data.
- Discovery machinery: active scanning and/or passive observation; agents for off-network endpoints.
- Enrichment: security findings/vulnerabilities attached to assets; business context (owner, business unit, location); lifecycle signals.
- Classification: device type/category (IT/OT/IoT), criticality, risk scoring.
- Query surface: query builder or query language; saved queries; query libraries.
- Coverage-gap analysis: control/agent/scanner coverage; honest reporting of unidentified space (IP range coverage, RFC 1918 coverage).
- Dashboards and reports; export.
- Outbound flow: tickets (Jira/ServiceNow), SIEM export, CMDB/ITSM sync.
- Relationship/visualization surface: asset graph, network map, or traffic-derived dependencies.
- Alerts/rules on inventory change (e.g., new device joined).
- Compliance framework mapping (CIS, NIST CSF, ISO 27001, PCI DSS, and region-specific regimes).
- Role-based access, SSO, audit of the system itself.

### L2 — Variant / Optional Structure

- Inventory-building emphasis: aggregation-first (Axonius) vs discovery-first (runZero, Lansweeper) vs graph-first (JupiterOne).
- Deployment: SaaS vs self-hosted; sensor placement models; agent vs agentless posture.
- Scope emphasis: OT/IoT/IoMT/medical specialization; external attack-surface inclusion (external exposure workspaces, Censys/Shodan ingestion); identity/SaaS/software as first-class workspaces.
- Exposure-management depth: risk scores, SLA management, exception workflows, remediation ownership, recommended actions (drift toward Exposure Management / CTEM).
- Compliance-automation depth (drift toward continuous controls monitoring).
- Multi-tenant/MSSP structures (organizations/sites, external users).
- AI assistance (natural-language query, AI threads, AI-derived enrichment).
- Business model: community/free editions, asset-count licensing, per-node pricing.

### L3 — Vendor-specific (research notes only)

- Axonius: adapter catalog, Enforcement Center, Enforcement Sets, Axonius Vulnerability Score (AVS), Agent Coverage hub, Windows Patch Tuesday workspace, Cases, Workflows, Device Intelligence Hub, query-based device scan jobs.
- runZero: Explorer architecture, sites/organizations, outlier score (0–5), RFC 1918 report, Starlark custom integrations, AI Threads, Thinkst Canary integration, MCP interface, asset-count licensing.
- Lansweeper: 175M+ device fingerprint library, Credential-Free Device Recognition, IP Range Coverage, IT/OT/Traffic sensor trio, AI Usage Tracking (early access), Armis data connector.
- JupiterOne: J1QL, entity type/class two-layer model, singleton entities (Internet/Root/Everyone), IMPACTS relationship semantics, UVM/AI ASM/CCM product split, j1_severity normalization.

## Vendor-specific Findings

See L3 above. Additionally:

- Axonius and JupiterOne both reposition around "exposure management" language while keeping the asset population central; runZero self-titles "attack surface and exposure management platform". The category label is drifting; the asset-population core is stable across all four.
- Lansweeper's heritage is IT asset discovery/management; its current positioning is explicitly security ("You cannot protect the business if you don't know what assets you have" — customer quote on official site). This straddling is itself evidence for the ITAM↔CAM family resemblance.

## Rejected Findings

- "CAM = vulnerability management": rejected. Vulnerabilities appear in all four products as enrichment/findings attached to assets, but the population — not the findings — is the central object. runZero's gap playbook ("finding gaps in vulnerability scanning") only makes sense from an asset-centric position.
- "CAM requires an agent": rejected. Axonius and JupiterOne are ingestion-based with no discovery agent; Lansweeper's core model is agentless with an optional agent; runZero uses network sensors. Agentless is not incidental — it is a common posture.
- "CAM = external attack surface scanning": rejected. External feeds (Censys/Shodan, external-exposure workspaces) are optional enrichment; the defining population is the organization's internal estate.
- "CAM requires a relationship graph": rejected as definitional. Only JupiterOne makes typed relationships the primary structure; Axonius has an Asset Graph, runZero/Lansweeper have network-topology/dependency views. Graph is L1/L2, not L0.
- "CAM = CMDB": rejected. See Boundary Findings.

## Boundary Findings

- **vs IT Asset Management (ITAM)**: same object (asset records), different decision vocabulary. ITAM is procurement/financial/lifecycle-oriented (contracts, licenses, cost, depreciation, refresh). CAM is security-oriented (exposure, control coverage, criticality, attack relevance). Lansweeper straddles both (IT heritage, security positioning; its "Know" pillar includes "forecast spend"). Discriminator: remove the security orientation and keep financial lifecycle → ITAM.
- **vs CMDB**: CMDB maintains configuration items in service of IT service management (services, change, incident); records are often curated/federated to support service models. CAM's population is auto-derived from the environment and security-shaped. They interconnect: runZero ingests NetBox; Axonius enriches from ServiceNow CMDB; Lansweeper syncs CIs to ServiceNow. Discriminator: remove automatic environment-derived assembly and security orientation, keep service-oriented curated records → CMDB.
- **vs Attack Surface Management (ASM)**: ASM is the outside-in, attacker-view of internet-facing exposure. CAM is the inside-out estate view. CAM products ingest external data (runZero ← Censys/Shodan; Axonius External Exposures) but the population remains internal-first. Discriminator: remove the internal estate and keep only external discovery → ASM.
- **vs Vulnerability Management**: VM is finding-centric (scan, rank, remediate vulnerabilities). CAM is asset-centric; vulnerabilities are one enrichment stream. CAM asks questions VM cannot ("which assets have no scanner coverage at all?"). Top-end CAM products drift into exposure management (Axonius Exposures, runZero exposure management, JupiterOne UVM) — boundary blurring noted, but the asset population remains the spine. Discriminator: remove asset-centricity and make findings the primary object → Vulnerability Management.
- **vs CSPM/DSPM**: domain-specific posture management (cloud configuration, data). CAM is domain-general. A CSPM's resource inventory is one ingestion source for CAM.
- **vs Network Management/Monitoring**: those optimize network device health/performance; CAM treats network devices as one asset class among many, oriented to security questions.
- **"去掉什么就变成另一个 Type" summary**: 去掉安全导向 → ITAM；去掉自动持续组装 → CMDB/资产台账；去掉内部群体只留外部视角 → ASM；去掉资产中心性 → Vulnerability Management；去掉"一资产一记录"的统一群体 → 单纯的数据聚合器。

## Historical / Market-Sample Check

- Older, simpler products: 2000s-era LAN inventory scanners (Lansweeper's own heritage), NAC-era discovery, single-sensor network inventories — these satisfy L0 (auto-assembled population, identity resolution across scans, security use) without adapters, graphs, or exposure scoring. L0 holds.
- Hand-maintained security asset registers (spreadsheets) fail L0's "environment-derived assembly" — appropriately so: the defining promise of the software category is that the system discovers and keeps current what humans would otherwise have to enumerate by hand.
- Platform-native alternatives: NetBox-style network source-of-truth tools are curated documentation systems (CMDB family), and appear in this research as *inbound integrations* to CAM products — confirming the boundary rather than refuting it.
- Conclusion: L0 does not over-fit the current aggregation-heavy market shape.

## Uncertainties

- Lansweeper evidence is Tier 2 (official product pages); its query surface, permission model, and lifecycle states were not directly observed from a help center. Claims about Lansweeper mechanics are vendor-stated and calibrated.
- JupiterOne's current product packaging (UVM/AI ASM/CCM) is recent; the docs' data model is stable evidence, but the exact current workspace/permission model was not fetched.
- Axonius "hundreds of adapters" is vendor-stated; the adapter table is a remote JSON and was not enumerated.
- Exact merge-key behavior in Axonius (which fields drive correlation) was not directly evidenced; only "normalizes and correlates" is documented.
- The category's market naming is in flux (CAM / CAASM / asset intelligence / exposure management). This research treats them as one application family with the asset population as spine; a future pass may need to check whether "Exposure Management" deserves a separate leaf.

## Final Synthesis

A Cyber Asset Management application is defined by a small core: a standing, environment-derived, deduplicated population of the organization's cyber assets, maintained continuously and shaped for security decisions. Around that core, mature products converge on a common structure — multi-source ingestion, discovery machinery, security enrichment (findings, coverage, criticality, risk), a query surface, coverage-gap analysis, outbound flow into tickets/SIEM/CMDB, and compliance mapping — while differing sharply in philosophy: aggregation-first (Axonius), discovery-first (runZero, Lansweeper), graph-first (JupiterOne). The type's boundaries are held by orientation: security vs ITAM's finance, auto-derivation vs CMDB's curation, internal estate vs ASM's outside-in view, asset-centricity vs vulnerability management's finding-centricity. The category is drifting toward "exposure management" branding at the top end, but the asset population remains the defining spine across all sampled products.
