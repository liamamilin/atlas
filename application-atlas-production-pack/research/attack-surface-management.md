# Research Notes — Attack Surface Management

Research date: 2026-09-06
Slug: attack-surface-management
Directory leaf: Attack Surface Management (§15 Cybersecurity, Identity & Trust)

---

## Research Goal

Understand what an Attack Surface Management (ASM) application actually is as a software Type: its core objects, how discovery works, how exposures attach to assets, how the inventory is maintained over time, who uses it, and where its boundaries lie against Vulnerability Management, Cyber Asset Management, Digital Risk Protection, Threat Intelligence, and adjacent security Types.

## Initial Boundary (hypothesis before research)

- Core purpose: continuously discover and inventory an organization's internet-facing digital assets from an attacker's outside-in perspective, attach exposures/observations to those assets, and monitor for change.
- Primary users: security teams (attack surface, vulnerability management, security operations), CISO office.
- Nearest neighbors: Vulnerability Management (known-asset, agent/credentialed scanning), Cyber Asset Management (internal inventory via integrations), Digital Risk Protection (brand abuse outside infrastructure), Threat Intelligence Platform (external threats, not own assets), Security Ratings (third-party scorecards), CSPM/CNAPP (cloud config posture), DAST (deep testing of known web apps), BAS (controlled attack execution).
- Key unknowns at start:
  1. Is "outside-in discovery without internal access" truly invariant, or do some ASM products require seeds/credentials?
  2. Is exposure/issue attachment part of the defining core or a common add-on?
  3. Is "continuous" required, or is recurring-scheduled enough?
  4. How is asset ownership attribution handled (the hardest problem in this Type)?
  5. Does the Type include internal networks (runZero claims "attack surface" includes internal), or is external the canonical center?

## Research Questions

1. What is an "asset" in ASM? Which asset types recur across products?
2. How does discovery work — seeds, recursion, passive datasets, active scanning? What is the role of "seedless" claims?
3. How is the inventory organized (asset records, attributes, relationships, source-of-asset)?
4. How is ownership attributed to discovered assets? What states exist (confirmed/candidate/dependency)?
5. How do exposures/findings attach to assets? What lifecycle do they carry (active/accepted/closed, severity, evidence, rescan)?
6. How does ongoing monitoring work — change detection, alerts, dashboards?
7. What interfaces exist (inventory explorer, asset detail, findings list, dashboards, scope config)?
8. How does ASM hand off to remediation (ticketing, VM tools, CMDB)?
9. Where is the EASM vs full-ASM (internal+external) boundary?
10. What rules matter (scope definition, ownership verification, severity overrides, dedup)?

## Representative Products (sample rationale)

Selected for market representativeness + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy | Customer tier | Evidence quality |
|---|---|---|---|
| Microsoft Defender EASM | suite-embedded EASM inside Azure/Defender ecosystem | enterprise | Tier 1 operational docs (Microsoft Learn) — excellent |
| Censys ASM | internet-scan-data-driven external ASM | mid-market/enterprise | Tier 1 operational docs (docs.censys.com) — excellent |
| CyCognito | pure-play external exposure platform, "attacker POV", seedless discovery | enterprise | Tier 2 product pages only; knowledge center login-gated |
| Detectify | SMB/mid-market scanner-style Surface Monitoring + Application Scanning | SMB/mid-market | Tier 1 support KB (support.detectify.com) — good |
| runZero | inventory-first unauthenticated discovery, internal + external | SMB/mid-market/enterprise | Tier 1 operational docs (help.runzero.com) — excellent |

Deliberately excluded: Palo Alto Cortex Xpanse, CrowdStrike Falcon Surface, Tenable ASM, Qualys, Wiz EASM — suite siblings would mostly repeat evidence; CyCognito's own comparison pages list them, confirming the market cluster without needing each one.

## Sources

Fetched 2026-09-06:

- Microsoft Learn — Defender EASM: Overview; What Is Discovery?; Understand Inventory Assets; TOC (asset filters: domain, host, page, contact, SSL certificate, IP address, IP block, ASN)
  - https://learn.microsoft.com/en-us/azure/external-attack-surface-management/overview
  - https://learn.microsoft.com/en-us/azure/external-attack-surface-management/what-is-discovery
  - https://learn.microsoft.com/en-us/azure/external-attack-surface-management/understanding-inventory-assets
  - https://learn.microsoft.com/en-us/azure/external-attack-surface-management/toc.json
- Censys docs (markdown views): Get Started with Censys ASM; Seed Your Attack Surface; Inventory Assets; Risks; llms.txt index (full ASM section list)
  - https://docs.censys.com/docs/asm-get-started.md
  - https://docs.censys.com/docs/asm-seed-your-attack-surface.md
  - https://docs.censys.com/docs/asm-inventory-assets.md
  - https://docs.censys.com/docs/asm-risks.md
  - https://docs.censys.com/llms.txt
- runZero docs: The runZero Platform; What is runZero?; Understanding assets; Understanding findings; Managing ownership
  - https://help.runzero.com/docs/what-is-runzero/
  - https://help.runzero.com/docs/understanding-assets/index.md
  - https://help.runzero.com/docs/understanding-findings/index.md
  - https://help.runzero.com/docs/managing-ownership/index.md
- CyCognito: homepage + platform nav (Discovery / Assessment / Prioritization / Validation / Remediation; products; use cases)
  - https://www.cycognito.com/
- Detectify support KB: home (full category tree); Assets and Root Assets
  - https://support.detectify.com/
  - https://support.detectify.com/support/solutions/articles/48001049287-assets-and-root-assets

Not fetched (limitations):
- CyCognito knowledge center (https://platform.cycognito.com/help) — login-gated. CyCognito evidence is positioning-level (official product pages), so no precise operational claims are made for it.
- Detectify individual articles beyond the two fetched — category tree read as structure evidence.
- Palo Alto Cortex Xpanse / CrowdStrike Falcon Surface docs — not fetched; used only as market-cluster confirmation via CyCognito's public comparison nav.

---

## Product A — Microsoft Defender EASM (Evidence layer A: operational docs)

Key observations:

- Positioning: "continuously discovers and maps your digital attack surface to give you an external view of your online infrastructure"; purpose = "identify unknowns, prioritize risk, eliminate threats, and extend control of vulnerabilities and exposure beyond the firewall."
- Discovery model: proprietary recursive discovery. Intake known assets ("discovery seeds": domains, IP address blocks, hosts, email contacts, ASNs, whois organizations) → scan connections (whois records: same registrant email/org/name servers; DNS records: hosts, co-resolved IP blocks, mail servers; SSL certificates: certs on hosts and other hosts using same certs; ASN records: other IP blocks under same ASN) → recurse outward "until it reaches the edge of your organization's management responsibility."
- Attribution state machine on every asset: **Approved Inventory** (owned, directly responsible), **Dependency** (third-party-owned but supports owned assets), **Monitor Only** (relevant but not controlled, e.g. franchisees/related companies), **Candidate** (some relationship, not strong enough — manual review required), **Requires Investigation** (confidence-score-flagged for review). Strong connections are auto-labeled "Confirmed Inventory" during discovery.
- Asset types in inventory: domains, hosts, pages, contacts, SSL certificates, IP addresses, IP blocks, ASNs (from inventory-filters TOC).
- Ongoing behavior: assets categorized "recent" (currently active) vs "historic"; Approved Inventory "scanned daily to ensure data recency"; Candidate assets scanned only during discovery; dashboards show Approved Inventory by default.
- Change tracking: "Inventory changes" dashboard with added/removed counts per asset type, filterable by 7/30-day ranges and by date.
- Dashboards: "attack surface insights" generated from vulnerability and infrastructure data; areas include vulnerabilities, compliance, security hygiene.
- Automation: policy engine automation; data connections; Microsoft Security Copilot integration.
- Roles: Azure RBAC — Owner/Contributor (create/delete/edit resources and inventory assets), Reader (view only). No cross-tenant access.
- Packaging: deployed as an Azure resource; billable assets concept; customer labels stored in selected region (data residency).

## Product B — Censys ASM (Evidence layer A: operational docs)

Key observations:

- Positioning: "take control of your organization's external attack surface… automatically discovers and monitors these assets, detecting risks such as misconfigurations, vulnerabilities, and unknown exposures."
- Seeds: known public-facing assets that start discovery — domains, other DNS names, IP addresses, CIDR blocks, ASNs. Added manually (console/CSV upload) or via API. Seed Data page splits "Provided by You" vs "Found by Censys" (Censys can discover seeds itself).
- Inventory asset types: **hosts** (IP-identified computers/devices; fields: ASN, geo, DNS names, services with ports/protocols), **web entities** (name+port HTTP services, collections of instances), **certificates** (parsed contents, trust info, CT logs), **domains** (eTLD+1; registrar, name servers, MX), **storage buckets** (S3/GCS/Azure Blob; access settings readable/writable/editable), plus aggregated **software** (fingerprinted, >1,433 software fingerprints; from scan fingerprints, x-powered-by, server headers).
- Source-of-asset column: Seed you Provided / Censys Found Seed / Censys Scan (attribution) / AWS Connector / GCP Connector / Azure Connector. Cloud connectors add cloud-account context (account IDs).
- Risks: "over 400 types of risks" associated with inventory assets. Risk Instances page: default view = active risk instances; tabs for accepted and closed; "new since" definition adjustable. Quick filters: severity, category, type, asset type, environment (cloud vs other).
- Risk lifecycle: active → accepted (with reason; reversible) or closed (no longer detected). Severity can be edited per instance or in bulk with reason. Risks carry **evidence** — plain-language explanation linking to the exact scan data (field-value pair) that triggered classification. **Rescan** button on a risk validates remediation.
- CVE risks: named "Vulnerable [vendor] [product] [CVE count]"; separate "Rapid Response" risks for emerging threats (no CVSS/KEV/attack-vector info on those).
- Integrations: Jira, ServiceNow (CMDB/ITSM/Vulnerability Response), Splunk, Microsoft Sentinel, Google SecOps, Slack, Teams, Webex, Qualys VMDR, Tenable VM, Wiz, webhooks, risk email notifications, Rapid Response email.
- Governance: ASM workspaces + user access; Activity Logbook (audit); RBAC; SAML/SCIM; API (seeds, inventory aggregation); CSV export.
- Use-case pages: Shrink Your Attack Surface; Secure Subsidiaries/Acquisitions/Mergers; Eliminate Shadow IT; Identify Unsanctioned Cloud Usage.

## Product C — CyCognito (Evidence layer A on positioning pages; operational detail NOT accessible)

Key observations (positioning-level):

- Positioning: "Preemptive Exposure Management"; products: Attack Surface Management ("Attacker POV"), Continuous AI Pentesting, Adversarial Validation, Exploit Intelligence.
- Platform loop (official nav): Discovery → Assessment (Contextualization) → Prioritization → Validation (Active Security Testing) → Remediation (Remediation Acceleration).
- Discovery claims: "Seedless Discovery — see your attack surface instantly, just like attackers do… No asset lists or setup needed"; "Critical Blind Spots — untracked IP ranges, inherited and third-party assets"; "Continuous Monitoring — daily scans."
- Context: "Cyber Asset Inventory" (external insights classified by business and tech context, third-party apps, PII exposures); "Attacker's Point of View" (attractiveness, discoverability, exploitability); "Detailed Discovery Evidence — trace each asset back to your organization — across subsidiaries, supply chains, and third-party connections."
- Validation: autonomous pentesting, "100,000+ testing modules", security control validation (WAF, API security, CSPM coverage).
- Prioritization: risk scoring aligned with exploit data + business impact ("surface the 0.01% of issues worth fixing first").
- Remediation: "Owner-linked Workflows" (identify asset owners, delegate tasks, track fixes across integrated platforms e.g. ServiceNow); guided remediation steps; autonomous validation closing the loop.
- Integrations (logos): Armis, Palo Alto Networks, Tenable, Wiz, Axonius, CrowdStrike, Cobalt, JupiterOne, ServiceNow, Splunk, Zendesk, Jira.
- Use cases: EASM, CAASM ("Unmanaged assets are invisible to CAASM solutions. Close the gaps"), UVM, CNAPP, AppSec, CTEM, M&A risk, subsidiary risk, supply chain risk.
- Market cluster confirmation: public competitor-comparison nav lists CrowdStrike Falcon Surface, Microsoft Defender EASM, Palo Alto Cortex Xpanse, Qualys, Tenable ASM as the ASM category.

Limitation: knowledge center login-gated; all CyCognito-specific mechanics (how seedless discovery actually works, exact workflows) are NOT verified. Treat as vendor positioning.

## Product D — Detectify (Evidence layer A: support KB)

Key observations:

- Asset model: "Domains, IPs, Subdomains and APIs that are added to your Detectify account are called assets. Root domains and IPs added to Detectify are called Root Assets. These define the scope of what is included in your attack surface." If a subdomain is added without its root, the highest subdomain becomes the root.
- Four ways to add assets: connectors (AWS Route53, Azure, Google Cloud DNS, Cloudflare, IBM NS1), zone files / DNS zone transfer (AXFR), adding a single domain, adding a single IP. "All domains added or imported make out the seed from where the rest of your subdomains, root domains, and IPs can be discovered."
- Ownership verification: domain ownership verification required before scanning (DNS TXT record or txt file) — "Why do you require verification of domain ownership?"
- Two monitoring/testing layers:
  - **Surface Monitoring**: attack surface monitoring — port discovery and scanning, technologies, subdomain takeover detection, scan recommendations and asset classification, custom "Attack Surface Custom Policies".
  - **Application Scanning**: DAST-style deep scanning of selected assets with scan profiles, port/URL include-avoid settings, behind-login scanning (Recorded Login / Trails service), crawl coverage.
- Attack Surface Policies: user-defined policies over the attack surface (examples for hosting providers, open ports, technologies) — policy violations as findings.
- Insights surfaces: Domains page, Overview page, Attack Surface view, IP addresses view, Technologies page.
- Findings: Prioritization Overview; Vulnerabilities page; CVSS v3.1 via API.
- Operations: continuous monitoring emphasized ("The importance of continuous monitoring"); WAF allowlisting guidance (scans blocked by WAF; per-provider instructions for AWS/Azure/GCP/CloudFront); Integrations 2.0 + Slack; Attack Surface API v3; teams/groups, SAML SSO, 2FA.
- Scanning permission posture: articles about notifying hosting providers before scanning — the product actively scans customer-verified assets.

## Product E — runZero (Evidence layer A: operational docs)

Key observations:

- Positioning: "attack surface and exposure management platform that helps you see everything on your network, from managed IT systems to unmanaged OT, IoT, cloud, mobile, and remote assets." — notably broader than external-only; internal networks included.
- Architecture: Console (SaaS or self-hosted) + distributed **Explorers** (lightweight collectors at points of presence) + CLI. Organizations → Sites structure; assets are site-scoped.
- Data sources: high-speed active scanning (protocol fingerprinting), passive traffic sampling (SPAN/broadcast), inbound/outbound API integrations (cloud, EDR, CMDB, VM tools: AWS, Azure, GCP, CrowdStrike, Qualys, Tenable, Wiz, Shodan, Censys, etc.).
- Live inventory: **assets** (unique network entities, correlated/merged across sources; fields: primary/secondary IPs, hostnames, OS, device type, category IT/OT/IoT, functions, hardware, MAC, services ~100 TCP by default, RTT, detected-by, alive status, first seen, last seen, explorer, outlier score 0–5), **services**, **screenshots** of exposed web services, **software**, **vulnerabilities** (per-asset + grouped; found by Explorer or imported), **certificates** (expired/soon-to-expire, issuer, chain), **wireless**, **users & groups** (from directory integrations).
- Asset lifecycle: after each scan, assets not found are marked **offline**; substantial fingerprint changes can split an asset (old marked offline, new created); duplicates can be removed by hand.
- Findings (distinct from vulnerabilities): "curated, aggregated and prioritized list of risks most likely to be targeted by attackers." Categories: **Internet Exposure** (potentially unintentionally exposed), Certificates (expired/soon-to-expire/shared private keys), Vulnerability (actively exploited or critical), End-of-Life, Open Access (unauthenticated databases/sensitive apps), Compliance, Best Practice, Rapid Response (emerging threats). Each finding: description, remediation steps, risk rankings, list of affected assets. A finding may group several vulnerabilities; not always CVE-tied.
- Ownership: configurable ownership types (Security owner, IT owner, Compliance owner; custom); default "Asset Owner" auto-populated from integrations (prioritized attribute mapping, e.g. Google Workspace owner, LDAP managedBy, Intune userDisplayName); ownership assigned via inventory bulk actions or alert rules; asset ownership inherited by unowned vulnerability records; separate built-in "Issue owner" type synced with Jira.
- Monitoring: alerts on inventory changes, new results for saved queries, system events; delivery in-product/email/webhook/Slack; goals and dashboard widgets track progress; suppression management; External Assets report (the EASM slice); compliance-alignment mappings (CIS, CISA BOD 23-01, NIST CSF, PCI, ISO 27001…).
- Roles: superusers/administrators/users/annotators; user groups; SSO; external users; licenses.

---

## Cross-product Comparison

| Dimension | Defender EASM | Censys ASM | CyCognito | Detectify | runZero |
|---|---|---|---|---|---|
| Scope center | external only | external only | external (attacker POV) | external (domains/IPs/subdomains/APIs) | internal + external ("everything on your network") |
| Discovery substrate | proprietary recursive crawl from seeds | internet-wide scan dataset + attribution + seeds | claimed "seedless" (mechanism undisclosed) | seeds = Root Assets + DNS connectors + zone transfer | active scans by Explorers + passive sampling + integrations |
| Seed/scope concept | discovery seeds (domains, IP blocks, hosts, email contacts, ASNs, whois orgs); discovery groups | seeds (domains, names, IPs, CIDRs, ASNs) | none needed (claim) | Root Assets define scope | scan scope via sites/networks + integrations |
| Asset types | domains, hosts, pages, contacts, SSL certs, IPs, IP blocks, ASNs | hosts, web entities, certificates, domains, storage buckets, software | assets with business/tech context, subsidiaries, third-party | domains, subdomains, IPs, APIs | assets (IT/OT/IoT), services, software, certs, wireless, users/groups |
| Ownership attribution | 5-state machine: Approved / Dependency / Monitor Only / Candidate / Requires Investigation | source column (seed provided / found / scan / cloud connector) + tags | "trace each asset back to your organization" (claim) | Root Asset scope + domain ownership verification | ownership types (Security/IT/Compliance), auto-populated from integrations, rules |
| Findings/exposures | attack surface insights (vulnerabilities, compliance, hygiene) | risks (400+ types; severity; evidence; accept/edit; rescan) | exposures with exploit-aligned risk scoring (claim) | vulnerabilities + attack surface policy violations | findings (Internet Exposure, Certificates, Vulnerability, EOL, Open Access, Compliance, Best Practice, Rapid Response) |
| Finding lifecycle | insights on dashboards | active / accepted / closed; "new since" | remediation workflows w/ owner + validation | prioritization + remediation tips | curated list; issue owner; Jira sync |
| Monitoring cadence | continuous; Approved Inventory scanned daily | continuous scanning | "daily scans" (claim) | continuous monitoring | scheduled scans + alerts on changes |
| Change detection | Inventory changes dashboard (added/removed by type, 7/30d) | logbook; collection events | continuous monitoring | new findings | alerts on inventory changes / query results / system events |
| Remediation handoff | policy engine, data connections, Copilot | Jira, ServiceNow ITSM/VR/CMDB, Splunk, Sentinel, webhooks | ServiceNow, Jira, Zendesk (claim) | Integrations 2.0, Slack, API v3 | Jira, ServiceNow, Splunk, Sumo, Tines; inbound VM tools |
| Prioritization | insights dashboards | severity + quick filters + evidence | exploit-aligned scoring (claim) | prioritization overview | curated findings + outlier score + asset risk/criticality |
| Roles/governance | Azure RBAC Owner/Contributor/Reader | workspaces, RBAC, audit logbook | enterprise (unverified) | teams/groups, SSO, 2FA | superuser/admin/user/annotator, groups, SSO |
| Deployment | SaaS (Azure resource) | SaaS | SaaS | SaaS | SaaS or self-hosted |
| Deep app testing | page-level inspection via crawler | web entity inspection | autonomous pentesting (claim) | Application Scanning (DAST, behind-login) | screenshots + service fingerprinting (no DAST) |

### Stable commonalities (cross-product, layer B)

1. Organization-scoped persistent inventory of externally reachable assets — all five.
2. Discovery starts from known identifiers (seeds/root assets/scan scope) and expands by observed relationships — four of five (CyCognito claims seedless but does not document an alternative mechanism; its "trace back to organization" implies the same attribution problem).
3. Assets carry observed attributes (DNS, services/ports, certificates, technologies, geo/cloud context) — all five.
4. Exposures/issues attached to assets with severity and evidence — all five (form varies: insights / risks / findings / vulnerabilities).
5. Ownership attribution is a first-class problem with explicit machinery (states, sources, owner assignment) — all five.
6. Ongoing/recurring observation with change detection (new assets, new findings, removed assets) — all five.
7. Handoff to remediation via integrations (ticketing/SIEM/VM) + API/export — all five.
8. Search/query over the inventory as a primary interaction — all five.
9. Dashboards/reports summarizing posture and inventory change — all five.
10. Team/role model with SSO in mature products — all five.

### Points of divergence

- External-only vs internal+external scope (runZero vs the rest).
- Passive-dataset-driven vs active-scanning-driven discovery (Censys heritage vs runZero/Detectify active scanning vs Microsoft proprietary crawl).
- Whether deep application testing (DAST) is bundled (Detectify, CyCognito) or left to other tools (Microsoft, Censys, runZero).
- Whether cloud accounts are connected for context (Censys/Detectify connectors; Microsoft data connections) or assets observed purely externally.
- Packaging: suite-embedded (Microsoft), standalone platform (Censys, CyCognito, runZero), self-serve SaaS (Detectify).

---

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

An Attack Surface Management application is:

1. **Organization-scoped external asset inventory** — persistent records of the organization's internet-facing digital assets (domains, hosts/IPs, certificates, web services, cloud-exposed resources), maintained by the system as an inventory.
2. **Outside-in discovery** — assets are found from an external vantage point (observing the internet as an attacker would), starting from known identifiers and expanding through observed relationships; no internal agents or pre-existing complete asset lists are required.
3. **Observations and exposures attached to assets** — each asset record carries what the system observed (services, certificates, technologies, context) and issues/exposures detected on it.
4. **Ongoing maintenance** — discovery and observation recur, so the inventory tracks the changing surface: new assets appear, exposures change, assets disappear.

Removal tests:
- Remove outside-in discovery → internal asset inventory / vulnerability management (different Type).
- Remove organization scoping → internet-wide search engine (different Type).
- Remove the inventory spine → one-time external recon report (not "management").
- Remove ongoing maintenance → point-in-time assessment (external pentest), not ASM.

### L1 — Common Mature Structure (very common, not defining)

- Seed/scope configuration: domains, IP ranges/CIDRs, ASNs, org names; DNS-provider connectors; zone-file import; ownership verification of seeds.
- Asset detail pages: attributes, first/last seen, related assets, source-of-asset.
- Attribution machinery: asset states (approved/confirmed vs candidate/dependency/monitor-only), source labels, confidence, manual review queues.
- Exposure/issue records: severity, category, evidence linking to raw observation, lifecycle (active / accepted / closed), severity overrides with reason, rescan-to-verify.
- Prioritization: severity + context + curated/aggregated finding lists.
- Dashboards & reports: posture overview, inventory changes (added/removed), trends.
- Alerts/notifications: new assets, new findings, query matches; email/Slack/webhook.
- Integrations & handoff: ticketing (Jira/ServiceNow), SIEM, VM tools, CMDB; API + CSV/JSON export.
- Inventory search/query language; saved queries.
- Roles/teams/SSO/audit log.

### L2 — Variant / Optional Structure

- Scope posture: EASM-only (dominant market form) vs internal+external unauthenticated discovery (runZero-style) vs CAASM-style aggregation.
- Discovery substrate: passive dataset-derived (scan-data heritage) vs active scanning vs proprietary crawl; "seedless" marketing posture.
- Cloud connectors / cloud asset context (account IDs, cloud resource types, storage buckets).
- Bundled deep application testing (DAST, behind-login scanning, autonomous pentesting).
- Third-party/subsidiary/brand-adjacent monitoring (Monitor Only states; M&A and subsidiary use cases).
- Policy engines over the attack surface (custom policies on ports/technologies/hosting).
- Compliance-framework mappings and reports.
- Managed-service delivery / free external risk assessment as go-to-market.
- Deployment: SaaS-only vs self-hosted option.
- AI assistance (query assistants, Copilot integration, AI pentesting).

### L3 — Vendor-specific (research notes only)

- Microsoft: discovery groups; exact state names (Approved Inventory / Dependency / Monitor Only / Candidate / Requires Investigation); "Confirmed Inventory" auto-labeling; billable assets; Azure resource deployment; data-residency guarantees (75/180-day deletion policies); Security Copilot integration.
- Censys: internet-wide dataset heritage (Global Inventory); "over 400 types of risks"; Rapid Response risk naming convention; CenQL; credits system; Activity Logbook event catalog; >1,433 software fingerprints; storage-bucket access booleans (readable/writable/editable).
- CyCognito: "seedless discovery" claim; "up to 20× more exposures" claim; attractiveness/discoverability/exploitability scoring; "100,000+ testing modules"; "0.01%" prioritization claim; daily-scan claim. All positioning-level, unverified operationally.
- Detectify: Root Asset concept; researcher-community-derived test content (hacker team heritage — implied by "Go hack yourself" branding and remediation-tip library, not verified in fetched docs); Recorded Login / Trails service; Surface Monitoring vs Application Scanning product split; per-hosting-provider WAF allowlist guides.
- runZero: Explorer architecture; site-scoped correlation; offline marking on missed scans; outlier score 0–5; IT/OT/IoT category + OT function taxonomy; ~100 default TCP services; ownership auto-population priority tables; External Assets report; self-hosting.

## Rejected Findings (considered and not promoted)

- "ASM requires zero setup / seedless discovery" — rejected as defining: contradicted by four of five products that require seeds/scope; CyCognito-only claim (kept as L2 marketing posture / L3 detail).
- "ASM = external vulnerability management" — rejected: VM's defining structure (enumerating known hosts, agent/credentialed scanning, CVE-centric remediation workflow) differs; ASM's defining act is discovering unknown external assets. Overlap exists in findings handling.
- "ASM includes brand abuse / typosquat / dark-web monitoring" — rejected as defining: that is Digital Risk Protection; some ASM products bundle it, but no sampled product made it structural. (Not observed in fetched docs for any of the five.)
- "ASM must scan daily" — rejected: only CyCognito claims "daily scans" and Microsoft states Approved Inventory is scanned daily; others document scheduled/continuous scanning without a universal cadence. L0 says "ongoing/recurring," not a specific cadence.
- "Attack-path / exposure-graph modeling is core" — insufficient evidence: only CyCognito review quotes mention attack paths; not documented as structure in fetched docs for the sample. Kept as uncertain/optional.
- "ASM is inherently cloud-posture management" — rejected: cloud connectors add context, but config evaluation inside cloud accounts is CSPM's structure.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove from ASM to become the neighbor) |
|---|---|---|
| Vulnerability Management | closest operational neighbor; findings handoff | Remove outside-in discovery of unknown assets (assume a known, internally-enumerated host population; scan with agents/credentials) → VM. ASM discovers the target set; VM manages CVE remediation on known targets. |
| Cyber Asset Management | inventory sibling | Remove the external/attacker vantage point (build the inventory from internal integrations/agents) → CAM. runZero straddles by doing unauthenticated discovery on both sides; CyCognito markets "closing CAASM gaps." |
| Digital Risk Protection | outside-in sibling | Remove the infrastructure-asset inventory spine (monitor brand abuse, typosquats, dark-web mentions instead) → DRP. |
| Threat Intelligence Platform | data sibling | Remove org-scoped own-asset inventory (track external actors/IOCs/infrastructure instead) → TIP. Censys straddles at platform level (threat-hunting module). |
| Security Ratings Platform | posture sibling | Remove the working inventory + finding lifecycle (produce third-party scorecards instead) → Security Ratings. |
| CSPM / CNAPP | cloud sibling | Remove outside-in observation (evaluate configs inside connected cloud accounts) → CSPM. Cloud connectors are the bridge, not the core. |
| DAST / web app scanning | depth sibling | Remove breadth-first discovery of unknown assets (deep-test a known web app) → DAST. Detectify bundles both layers in one product. |
| Breach & Attack Simulation | validation sibling | Remove passive observation (execute controlled attacks against production controls) → BAS. CyCognito's "security control validation" straddles. |
| Internet-wide search engines (Shodan/Censys Search) | substrate sibling | Remove organization scoping + inventory management (serve a public queryable dataset instead) → search engine. Censys ASM is literally built on top of such a dataset. |
| Penetration Testing Management | service sibling | Remove continuous automated observation (manage human engagements/scope/reports instead) → PTM. |

Sharpest seam: **Vulnerability Management** — the two share findings/severity/remediation vocabulary, and ASM findings are often exported into VM tools. The structural test is whether the system's defining act is *discovering the target set from outside* (ASM) or *assessing a known target set* (VM).

Historical / market-sample check: a recurring external scanning service from a regional MSSP (monthly external scan + report, no dashboards, no ML prioritization, no cloud connectors) still satisfies L0 (org-scoped external inventory + outside-in discovery + observations attached + recurring maintenance). A one-off external pentest recon does not (no ongoing maintenance). An internet-wide scanner without org scoping does not. The L0 therefore does not over-fit the current enterprise platform era.

## Uncertainties

1. CyCognito operational mechanics unverified (knowledge center login-gated). All CyCognito-specific claims are positioning-level; none were promoted into the canonical model.
2. Detectify's exact discovery mechanics (how much is passive DNS observation vs active scanning) not fully detailed in fetched pages; only that seeds/root assets drive discovery and that Surface Monitoring performs port discovery/scanning.
3. Whether attack-path graphing is becoming common structure — insufficient evidence in this sample.
4. runZero's self-description as "attack surface management" including internal networks creates a scope question for the Type: the researched market's center of gravity is external (EASM), with internal+external as a variant posture. The directory leaf "Attack Surface Management" (not "External Attack Surface Management") is treated as the broader Type, with EASM as the dominant variant — no taxonomy change proposed, but this is worth a joint review if an "External Attack Surface Management" leaf is ever processed separately.
5. Microsoft's "email contacts" and "whois organizations" as asset types are unusual (organizational/contact records as inventory citizens); treated as vendor asset-type choices, not canonical.

## Final Synthesis

The Type's canonical model:

```text
Organization scope (seeds / root assets / scan scope)
  ↓ outside-in discovery (recursive expansion through observed relationships)
External Asset Inventory (persistent, org-scoped)
  ├── Asset records (domains, hosts/IPs, certificates, web services, cloud-exposed resources)
  │     ├── observed attributes (DNS, services/ports, technologies, geo/cloud context)
  │     ├── attribution (source, ownership state, owner)
  │     └── exposures/issues (severity, evidence, lifecycle: active → accepted/closed)
  └── change over time (new assets, new exposures, removals) → alerts → remediation handoff
```

Defining core (4 properties): org-scoped external asset inventory; outside-in discovery; observations/exposures attached to assets; ongoing maintenance. Everything else in the market's expectations — dashboards, risk scoring, integrations, cloud connectors, DAST depth, policy engines — is common mature structure or variant, not definition.
