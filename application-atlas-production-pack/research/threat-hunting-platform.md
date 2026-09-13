# Research Notes — Threat Hunting Platform

Research date: 2026-09-09
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Threat Hunting Platform actually is as an application type: what objects exist inside it, what its users do, how a hunt flows from a starting idea to an outcome, and where its boundary lies against SIEM, EDR/XDR, log management, threat intelligence platforms, and incident-response tooling. Special attention to the market-structure question: hunting sounds like a product category, but initial scoping suggested it may predominantly ship as a capability/module inside SIEM/XDR/EDR platforms rather than as standalone products.

## Initial Boundary

Working hypothesis at start:

- Core use: proactive, analyst-driven search for malicious activity already present in an environment but not surfaced by automated detection (alerts, rules, ML detectors). The analyst starts from a hypothesis, indicator, anomaly, or coverage gap rather than from an alert.
- Users: threat hunters, senior SOC analysts, detection engineers, DFIR specialists inside a security operations function.
- Likely neighbors: SIEM (alert-driven aggregation/detection), EDR/XDR (endpoint telemetry + automated detection/response), NDR, Threat Intelligence Platform (manages external intel), SOC Platform (workflow/case orchestration), Cyber Incident Response Platform, Digital Forensics Platform, Log Management (raw log search).
- Open questions going in: Is there a distinct "unit of record" for hunting (hunt? hypothesis? bookmark? case?)? Is hunt persistence definitional or common? Is promotion of hunts into detection rules definitional? Is the standalone-product framing real?

## Research Questions

1. What is the unit of record in a hunting platform, and does it persist?
2. What is the canonical hunt loop (start → search → capture → outcome)?
3. What telemetry substrate does hunting run over, and who collects it?
4. How do hunting platforms help the analyst start (query libraries, ATT&CK mapping, content)?
5. How are findings promoted — into cases/incidents, and into detection content?
6. What machinery is hunting-specific vs generic log search?
7. Where are the seams against SIEM / EDR / XDR / log analytics / TIP / IR platforms?
8. What variants exist (self-service vs managed vs AI-assisted; query languages; substrate)?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different substrate philosophies:

| Product | Philosophy / pole | Evidence obtained |
|---|---|---|
| Microsoft Sentinel (hunting + hunts) | cloud SIEM with a dedicated hunting program layer (hunts as records, hypothesis states) | Tier-1 docs, 2 pages, full text |
| Elastic Security (investigate / Timeline) | search-native, open-stack; hunting inside an investigation workspace | Tier-1 docs, 2 pages, full text |
| Splunk Enterprise Security 8 | classic SIEM pole: detection-generated findings → investigations on a search substrate | Tier-1 docs, 2 pages, full text |
| Microsoft Defender XDR (Advanced Hunting) | XDR pole: KQL hunting over vendor-collected endpoint/identity/email/cloud telemetry schema | Tier-1 docs, 1 page, full text |

Vendor overlap note: two of the four are Microsoft products, but they are different products with different philosophies (SIEM data-layer hunts with hypothesis records vs XDR schema-table proactive hunting with custom detections). The overlap is recorded as a sampling limitation.

Attempted and abandoned (per network-access limitation rules; no operational claims made from them):

- CrowdStrike (Falcon docs portal is a JS application — unreachable; marketing URL 404). Would have been the endpoint-vendor + managed-hunting (OverWatch) pole.
- Google Security Operations / Chronicle (cloud.google.com timed out twice). Would have been the cloud-data-lake search pole.

These remain market anchors only.

## Sources

All fetched 2026-09-09:

- Microsoft Sentinel — "Hunting Capabilities in Microsoft Sentinel" — https://learn.microsoft.com/en-us/azure/sentinel/hunting
- Microsoft Sentinel — "Conduct End-to-end Threat Hunting with Hunts" — https://learn.microsoft.com/en-us/azure/sentinel/hunts
- Elastic Security — "Elastic Security solution overview" — https://www.elastic.co/docs/solutions/security
- Elastic Security — "Investigate security events" — https://www.elastic.co/docs/solutions/security/investigate
- Elastic Security — "Timeline" — https://www.elastic.co/docs/solutions/security/investigate/timeline
- Splunk Enterprise Security 8 — product manual root + "About Splunk Enterprise Security" — https://help.splunk.com/en/splunk-enterprise-security-8 , https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/introduction/about-splunk-enterprise-security
- Splunk Enterprise Security 8 — "Overview of Mission Control" — https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/mission-control/overview-of-mission-control-in-splunk-enterprise-security
- Microsoft Defender XDR — "Advanced hunting with Microsoft Sentinel data in Microsoft Defender" — https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender

Failed / abandoned (recorded for evidence calibration):

- docs.crowdstrike.com (JS-rendered application; content not retrievable) + crowdstrike.com marketing URL (404)
- cloud.google.com/security/products/security-operations and cloud.google.com/chronicle/docs/overview (timeouts)

Two failed attempts at the old docs.splunk.com page slugs redirected to the docs index (wrong paths, not a source failure); the current help.splunk.com portal was reached successfully.

## Product Observations

### Microsoft Sentinel (hunting + hunts)

Evidence layer A — direct observation from official docs.

- Positioning (vendor's own words): "you want to be proactive about looking for security threats … hunting queries guide you into asking the right questions to find issues in the data you already have"; hunting targets "new anomalies that aren't detected by your security apps or even by your scheduled analytics rules." Explicit anti-alert framing: "Waiting on detections isn't enough. Take proactive action…"
- Hunting queries: out-of-box hunting queries shipped via the Content hub (authored continuously by vendor security researchers), plus custom/modified user queries. Each query has a description of what it hunts and what data it runs on. Queries grouped by MITRE ATT&CK tactics; techniques shown per query; a tactic bar dynamically updates with filters. Query results counts, result spikes, "Results delta" (last 24h vs previous 24–48h) used to decide where to hunt. Favorites auto-run when the Hunting page opens.
- Hunts (first-class records, preview feature): a hunt is created from selected queries or blank; carries name, description ("a good place to verbalize your hypothesis"), owner, status, and a hypothesis state. Tabs: Queries (cloned, hunt-scoped copies), Bookmarks, Entities. Hunt lifecycle: hypothesis defined → queries run → results investigated → hypothesis state updated (validated/invalidated) → hunt closed when actions complete. Hunt page keeps new/active/closed hunts in one place and shows a metrics bar: validated hypotheses, new incidents created, new analytic rules created.
- Bookmarks: preserve specific result rows together with the query and time range that produced them; carry tags, notes, entity mappings, ATT&CK tactic/technique mappings; can be investigated in an interactive entity-graph; can create a new incident or join an existing one; stored in a queryable table (HuntingBookmark) for corroboration.
- Promotion machinery: right-click a hunting query → "Create analytics rule" (rule wizard pre-populated); hunts auto-link related analytics rules and incidents; actions on entities include adding indicators to threat intelligence and running playbooks.
- Investigation depth: UEBA entity pages; investigation graph (entities + timeline); Jupyter notebooks for complex hunts (data persistence, repeatability, ML/visualization libraries; vendor-published hunting library MSTICPy).
- Query substrate: KQL (same language as analytics rules); "useful operators" documented for hunting (where, summarize, join, find, adx() cross-resource); multi-tab persisted query experience within hunts ("keep context over time").
- Data: log tables such as process creation, DNS events; requires data sources connected (queries show N/A and recommendations when sources missing).
- Roles: hunts require Sentinel Contributor or custom RBAC roles — hunting is permissioned and role-gated.
- Era note: "livestreams are no longer available"; replaced by KQL jobs (persistent query results in the data lake), analytics rules, playbooks.

### Elastic Security (investigate / Timeline)

Evidence layer A — direct observation from official docs.

- Positioning: unified SIEM/XDR/endpoint/cloud security solution; use cases include "proactively search for threats using our powerful threat hunting and interactive visualization tools."
- Timeline is explicitly "the central workspace for investigations and threat hunting." Add alerts from multiple indices; drag fields from tables/histograms across the app into the Timeline to build queries; query languages KQL, EQL, ES|QL. Correlation tab for EQL sequence queries — ordered attack patterns across event categories ("identifying and predicting related events … a more complete picture of potential adversary behavior").
- Persistence & reuse: save Timelines (must save before navigating away), duplicate, favorite, export/import as .ndjson to share across instances/spaces; Timeline templates (saved starting configurations) attachable to detection rules so alerts open with the right filters.
- Evidence capture: pin interesting events; notes attached to alerts, events, or Timelines; notes are searchable/manageable as a page. Event renderers add contextual display.
- Promotion machinery: from a Timeline → "Create query rule from timeline" / "Create EQL rule from timeline" (hunting query becomes a detection rule); Timelines attach to cases (new or existing); cases attach alerts/events/notes/timelines and integrate with Jira, ServiceNow, IBM Resilient.
- Deeper instruments: visual event analyzer (process tree before/after an alert), Session View (Linux terminal-style sessions), Osquery live host interrogation (run from alerts or investigation guides; saved query library; scheduled packs), Indicators of Compromise page (from TI feeds) cross-referenced with investigations; indicator match rules auto-alert on known threats.
- Entity context: entity analytics (risk scores, behavioral anomalies for hosts/users/services); Attack discovery (LLM analysis correlating alerts, mapping to MITRE ATT&CK).
- Access control: Timeline feature gated by Kibana privileges — hunting surfaces are permissioned.
- Detection engine context: prebuilt + custom rules generate alerts; hunting operates on raw events + alerts in the same workspace.

### Splunk Enterprise Security 8

Evidence layer A — direct observation from official docs.

- Positioning: "threat detection, investigation, and response solution"; combines SIEM + SOAR + threat intelligence management; built on the Splunk platform's "search and correlation capabilities" (SPL). Analysts "capture, monitor, and report on data from security devices, systems, and applications."
- Mission Control page: analyst queue of findings and finding groups (generated by detections from raw events and third-party alerts) and investigations. Investigation = "a structured approach for gathering evidence and responding to a security incident," based on one or more findings; carries events, additional fields, notes, files; status values (New, In progress, Pending, Resolved, Closed); disposition values (True positive, Benign positive, False positive, Undetermined); owners; urgency classification.
- Workflow: triage finding → assign/self, update status → start investigation → add response plan (standardized tasks and phases) → run actions/playbooks (SOAR automation) → use threat intelligence sources to assess observables → set disposition → close.
- Risk-based alerting: risk analysis to create "high confidence alerts for investigations." Observables + threat intelligence attributes reviewable per finding. OCSF-aligned taxonomy.
- Search substrate: "Use the Splunk platform search function for Splunk Enterprise Security data on the Search page" — SPL over indexed data; charts/timeline visualization of findings/investigations.
- Security content: Enterprise Security Content Update (ESCU) delivers "regular, relevant, and actionable threat detection content"; Security Essentials app provides "tailored procedures" content. (Hunting-specific dashboards of older ES versions were not observed in the 8.x docs fetched.)
- Note: the ES 8 docs describe an alert/finding-driven investigation loop. Proactive hunting in the Splunk ecosystem is realized through the platform's search layer plus security content; the fetched pages document investigations triggered by findings, not hypothesis records. This contrast is used for boundary analysis, not as a claim that Splunk lacks hunting.

### Microsoft Defender XDR (Advanced Hunting, unified portal)

Evidence layer A — direct observation from official docs.

- Positioning: "Proactively hunt for threats with advanced hunting" — KQL hunting across "all the data sources available within the unified Microsoft Defender portal," spanning Microsoft Defender XDR and connected services (endpoint, identity, email, cloud); with Sentinel onboarded, Sentinel workspace tables/functions/queries join the same experience. Vendor framing: "Querying from a single portal across different data sets makes hunting more efficient."
- Structure: Schema tab (tables organized by solution, with schema viewer, sample-data preview, retention info, table capability tiers), Functions tab, Queries tab (shared and sample queries, foldered). The schema table set is the hunting substrate; the platform collected the telemetry with its own agents/services.
- Promotion machinery: custom detections created from hunting queries (near real-time for Defender data); "Link to incident" to attach query results to new/existing incidents; take-actions/guided hunting capabilities (Defender data only); AI (Security Copilot) prompts hunting queries.
- Constraints are explicit and documented: quotas/usage parameters, retention-dependent query windows, role-based access (querying only workloads your roles allow), table capability tiers (full query vs basic logs).
- Contrast note (documented by the vendor): bookmarks are not available in the unified advanced hunting experience (they exist in Sentinel's hunting page); linking results to incidents is the offered alternative. Useful evidence that evidence-capture machinery is product-specific in shape even when the concept is shared.

## Cross-product Comparison

| Dimension | Sentinel | Elastic Security | Splunk ES 8 | Defender XDR AH |
|---|---|---|---|---|
| Proactive framing (analyst-initiated, not alert-driven) | explicit ("proactive", "waiting on detections isn't enough") | explicit ("threat hunting" as a named activity in the investigation workspace) | implicit in search layer; native record is finding-triggered investigation | explicit ("proactively hunt") |
| Searchable security telemetry substrate | ingested log tables (process, DNS, etc.) + UEBA | raw events + alerts across indices; own agents possible | Splunk platform indexed data (SPL) | vendor-collected XDR schema tables (+ Sentinel tables when onboarded) |
| Query language | KQL | KQL / EQL / ES\|QL | SPL | KQL |
| Hunting query library / starting points | out-of-box researcher-authored queries, Content hub solutions, custom, favorites | saved Timelines, Timeline templates, sample queries | security content (ESCU, Security Essentials) | shared/sample queries, Functions |
| ATT&CK mapping | hunting queries grouped by tactics/techniques; ATT&CK map shows hunting-query coverage gaps | Attack discovery maps alerts to ATT&CK matrix (docs fetched); rules commonly ATT&CK-mapped | not directly observed in fetched pages (security content is ATT&CK-mapped market-wide, unverified here) | not directly observed in fetched page |
| Evidence capture objects | bookmarks (rows + query + time range + entities + tags + notes) | pinned events, notes on alerts/events/timelines, saved Timelines | investigation events, notes, files | link results to incident (bookmarks absent in unified AH) |
| Escalation to cases/incidents | bookmarks → incidents (new/existing) | Timeline → cases; cases → Jira/ServiceNow/Resilient | findings → investigations (structured, response plans, dispositions) | link query results to incidents |
| Promotion into detection content | hunting query → analytics rule (wizard pre-populated) | Timeline → query rule / EQL rule | not directly observed in fetched pages (ES content model implies it; unverified) | hunting query → custom detection |
| Entity/behavior investigation | UEBA entity pages, investigation graph | entity analytics risk, visual event analyzer, Session View | observables + threat intel attributes, risk-based alerting | entity context in tables/alerts |
| Live endpoint interrogation | playbook actions on entities | Osquery live queries, from alerts/guides | via SOAR actions/playbooks | take actions (Defender data) |
| Program management of hunting | hunt records with hypothesis states + hunt status + metrics bar | saved/shared Timelines + cases + notes | investigations queue with owners/status/dispositions | saved queries; program metrics not observed |
| Data-science depth | Jupyter notebooks, MSTICPy | ES\|QL pipe analytics | SPL + ML toolkit (adjacent) | not observed |
| AI assistance | Security Copilot (query/investigation) | AI chat, Attack discovery (LLM alert correlation) | AI Assistant summarization | Security Copilot query prompting |
| Permissions on hunting surfaces | RBAC roles for hunts | Kibana privileges for Timeline | analyst queue config, saved views (admin) | role-scoped workload access |

Evidence layers: all cells above are layer A (directly observed in that product's docs) unless marked otherwise; the cross-product generalizations drawn from them are layer B.

## Canonical Abstraction

### Level 0 — Defining Invariant

Three jointly-held structures. Removing any one collapses the type into a neighbor:

1. **The organization's security telemetry as the searchable substrate.** Large volumes of security-relevant event data about the environment — endpoint, network, identity, cloud, application — held in a form the analyst can interactively query and explore. Remove → threat-intelligence content with no environment data, or an intel feed; nothing to hunt over.
2. **Analyst-initiated proactive search for activity that automated controls have not surfaced.** The human, not a scheduled rule, starts the investigation: from a hypothesis, an indicator, an anomaly, or a coverage gap — then iteratively queries, filters, drills down, and pivots across entities and time. Remove the proactive, analyst-initiated posture → alert triage / SIEM operations; remove the iterative search machinery → static reporting.
3. **Durable hunt records with promotion outcomes.** The hunting effort persists as records (hunts/investigations, evidence captures such as bookmarks/notes/pinned events, saved queries/timelines) that outlive the session, and findings escalate into cases/incidents and are institutionalized as new detection content and intelligence. Remove → an ad-hoc search console over logs; the "platform" and the hunting program die.

Jointly load-bearing: 1 alone = a log warehouse; 2 without 1 = hypotheses with nothing to query (a methodology, not software); 3 without 1+2 = a case tracker; 1+2 without 3 = a search console (the pre-platform ancestor); 1+3 without 2 = an alert queue with persistence; 2+3 without 1 = a methodology tool over nothing.

Historical/market-sample check (§24 reasoning): before "threat hunting platform" existed as a category, hunting practice ran on SIEM search consoles and scripts — those satisfy legs 1–2 only, and are correctly understood as the ancestor tooling; the platform category is defined by adding leg 3 (persistence + institutionalization). Regional/older and platform-native products with hunt records (even simple saved-query + notes arrangements) satisfy the core without any modern machinery (AI, notebooks, UEBA, ATT&CK mapping). A phone-era-era analog is not relevant here; the type is young but the check still passes: definition does not depend on cloud delivery, ATT&CK, ML, or any specific query language.

### Level 1 — Common Mature Structure

Very common in mature products, not definitional:

- Hunting query library / starting content (vendor- or researcher-authored hunting queries, templates, sample queries), commonly organized by MITRE ATT&CK tactics/techniques (directly observed at 2 of 4 sampled products; ATT&CK as the organizing scheme is additionally market-standard but not observed in all fetched pages).
- Evidence-capture objects tied to results: bookmarks/pinned events/notes preserving the row + query + time context.
- Escalation paths from evidence into cases/incidents (all 4 sampled products).
- Promotion of proven hunting queries into detection rules (3 of 4 sampled products, direct).
- Entity-centric investigation: entity pages/graphs, process trees, session views, entity risk.
- Rich query languages with filtering/aggregation/sequence constructs.
- Role/permission gating of hunting surfaces.
- AI assistance for query generation, summarization, alert correlation (era-current but already common in-sample).
- Live endpoint interrogation from hunting context (2 of 4 sampled products).

### Level 2 — Variant / Optional Structure

- Substrate ownership: vendor-collected telemetry via own agents/services (XDR pole) vs ingested third-party logs (SIEM pole) vs both.
- Packaging: dedicated hunting layer inside a SIEM/XDR platform vs standalone hunting offering; hunting delivered as a managed service by the vendor's analysts (market-recognized variant; not verifiable in the fetched sample — noted without operational detail).
- Query language (KQL / KQL+EQL+ES|QL / SPL / SQL-like); notebook/data-science depth; data-lake/archival search tiers with different retention windows and quotas (all product-specific; no precise limits stated).
- Program metrics (validated hypotheses, hunts closed, detections created) — present at one sampled product.
- Live/continuous hunt sessions (continuous query streaming) — existed at one sampled product and was retired there; treat as optional/era-specific.

### Level 3 — Vendor-specific Structure (kept out of the final document)

Sentinel: Content hub, hunt metrics bar, HuntingBookmark table, KQL jobs, LIVE streams (retired), adx() cross-resource queries, MSTICPy, Sentinel-in-Defender unification mechanics. Elastic: Timeline brand, .ndjson export, Timeline templates attached to rules, EASE/Agent Builder, event renderers, specific privilege model. Splunk: Mission Control/analyst queue, finding groups, dispositions vocabulary, risk-based alerting, OCSF alignment, ESCU/Security Essentials packaging, SOAR response plans. Defender XDR: schema tab with capability tiers, custom detections frequency tiers, guided hunting mode, quotas, 30-day-default retention specifics, GCC limitations.

## Vendor-specific Findings

(See Level 3; the load-bearing items for boundary work are: Sentinel's hunt record with hypothesis states — the strongest documented instance of hunting-as-program-management; Splunk ES's finding→investigation loop — the clearest documented contrast showing the SIEM-native record is detection-triggered, not hunt-triggered; Defender XDR's explicit absence of bookmarks in the unified hunting experience — proof that evidence-capture form varies while the concept persists.)

## Rejected Findings

- "Hunting requires ATT&CK mapping" — rejected. Only directly observed at 2 of 4; ATT&CK is an organizing convenience, not structure.
- "Hunting requires notebooks / data science" — rejected. Single-product depth in-sample.
- "Hunting requires its own data lake / collected telemetry" — rejected. Ingestion-vs-collection is a variant axis; hunting runs over whatever security telemetry it is given.
- "Hunting is defined by being alert-free" — rejected as phrased. Hunts often *start* from alerts/anomalies; the definitional property is that the analyst can and does start searches proactively, not that alerts are absent.
- "Hunt metrics define the program layer" — rejected. Single-product; optional.
- "Threat hunting = managed hunting service" — rejected for this Type. The service pole is a delivery variant; the platform Type is the software substrate (and could not be verified in-sample for the service pole).

## Boundary Findings

- **vs SIEM** (closest seam, keep both): SIEM's native unit of record is the detection-generated alert/finding; its loop is rule → alert → triage. Hunting's unit of record is the hunt/investigation initiated analyst-side; its loop is hypothesis → search → evidence → escalation → detection-content. Modern SIEMs embed hunting as a layer (all sampled SIEM-shaped products do). Remove proactive analyst-initiated search + hunt records → SIEM. Remove scheduled detection/correlation at scale → pure hunting tooling. The seam holds at product level too: one sampled product documents both loops and keeps separate records for each (hunts vs incidents vs analytics rules).
- **vs EDR/XDR** (keep both): EDR/XDR collects endpoint/workload telemetry, auto-detects, and can take response actions; hunting is the proactive exploration layer that may run over XDR telemetry. Response actions belong to the EDR/XDR side; hunting platforms hand response off (escalate to incident/playbook) — even where a hunting surface offers some actions, they are bounded. Remove telemetry collection + automated prevention/response → hunting layer; remove proactive search → EDR.
- **vs Log Management / Observability / BI-style search** (keep both): raw log search has the substrate and query languages but no security semantics (entities, detections, ATT&CK, indicators), no hunt records, no escalation/promotion machinery. Remove security hunting intent and machinery → log analytics.
- **vs Threat Intelligence Platform** (keep both): TIP's object is external intelligence (feeds, indicators, reports) managed for distribution; hunting's object is the environment's telemetry. Hunting consumes intel as starting points and matching targets (documented: indicator pages, TI attributes, add-indicator actions). Remove environment telemetry search → TIP.
- **vs SOC Platform / Cyber Incident Response Platform** (keep both): those orchestrate SOC workflow/case/response after discovery; hunting is the discovery layer that feeds them. Splunk ES 8's investigations blur into case management — recorded as a market-convergence observation, not a taxonomy error.
- **vs Digital Forensics Platform** (keep both): forensics is deep, evidence-grade examination of specific hosts/artifacts, usually post-incident; hunting is broad, proactive, environment-wide search. Different scope and evidentiary standard.
- **vs Vulnerability Management / Attack Surface Management** (keep both): pre-compromise exposure vs post-compromise adversary activity. Different objects entirely.
- **vs Deception Platform** (keep both): deception plants decoys that *generate* high-fidelity alerts; hunting is human-initiated search. Deception output can be a hunt trigger.
- **vs Security Validation Platform** (keep both): validation executes emulated attacks to test controls; hunting searches real telemetry for real adversary activity. Synthetic vs actual.
- **"去掉什么就变成另一个 Type" 判据**: remove the proactive analyst-initiated search leg → SIEM/EDR operations; remove the security semantics + promotion machinery (keep search) → Log Management; remove the environment telemetry substrate (keep records) → case management / IR platform; remove persistence (keep search) → a search console, not a platform.

## Market-structure observation

The research supports treating "Threat Hunting Platform" as a capability-type: in the current market, hunting predominantly ships as a first-class layer inside SIEM/XDR/EDR platforms (all three SIEM/XDR-shaped sampled products document it as such), with only a thin tail of standalone hunting products and managed-hunting services. The directory's separate SIEM / EDR / XDR / NDR / TIP / SOC Platform leaves coexist with this leaf the way related-layer leaves do elsewhere in the taxonomy. Recorded in STATUS Boundary Issues as a note, not a proposed restructuring.

## Uncertainties

- Managed-hunting services (vendor analysts hunting on the customer's behalf): source unreachable in this pass (CrowdStrike OverWatch); variant noted without operational claims.
- ATT&CK mapping across the full market: observed directly at 2 of 4 sampled products; believed market-standard but not asserted beyond the sample.
- Older/standalone hunting products (e.g., research-oriented open-source hunting stacks): not sampled; the historical check was run conceptually (search-console ancestor) rather than against a fetched legacy product.
- Splunk's hunting-specific dashboards/content of current versions: the ES 8 pages fetched document investigations triggered by findings; hunting-content behavior (Security Essentials hunting views) not directly fetched — Splunk observations are limited to what was fetched.
- Exact retention windows, quotas, and query limits: deliberately excluded from both documents (product-specific and fast-moving; only their *existence* is documented).

## Final Synthesis

A Threat Hunting Platform is the proactive-search layer of security operations: it holds the organization's security telemetry as an interactively searchable substrate, gives trained analysts an environment to start from hypotheses/indicators/anomalies/coverage gaps rather than from alerts — querying, drilling down, and pivoting across entities and time — and turns that effort into durable records whose findings escalate into cases/incidents and, in mature products, into new detection rules and intelligence. It is defined by three jointly-held structures (searchable security telemetry; analyst-initiated proactive iterative search; durable hunt records with promotion outcomes) and is commonly realized as a first-class layer inside SIEM/XDR/EDR platforms, with packaging (standalone/module/managed), substrate ownership (collected vs ingested), query language, and program machinery as variant axes. Its sharpest seam is against the SIEM's alert-driven loop; the two loops coexist inside the same products while remaining distinct records with distinct vocabularies.
