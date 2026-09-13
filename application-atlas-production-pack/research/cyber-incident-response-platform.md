# Research Notes — Cyber Incident Response Platform

Research date: 2026-09-07
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a Cyber Incident Response Platform actually is as an Application Type: what objects exist inside it, what its users do, how the response to a security incident flows through it, which states/rules matter, and where it begins and ends relative to SIEM, SOAR, SOC Platform, IT Incident Management, Digital Forensics, and Threat Intelligence.

## Initial Boundary (working hypothesis before research)

- Hypothesis: the Type is the security team's case-management layer for confirmed/active security incidents — structured incident records, response lifecycle, coordination, evidence, closure/lessons.
- The market term "Security Incident Response Platform" (SIRP) historically denoted standalone products (IBM Resilient heritage, DFLabs IncMan heritage); the term was later folded into "SOAR". Expected finding: today the Type mostly survives as the incident/case-management layer inside SIEM, SOAR, and TI platforms.
- Nearest neighbors: SIEM, SOAR, SOC Platform, Incident Management (IT/ITSM), Digital Forensics Platform, Threat Intelligence Platform, EDR, On-call Management.
- Key risk: the leaf may be judged an Alias/Variant of SOAR by a later reviewer; the counter-hypothesis (tested below) is that the incident case-management core is realizable without any automation/orchestration, which keeps it a distinct Type.

## Research Questions

1. What is the central object (incident vs case vs container), and what does it carry (severity, type, status, owner, evidence, entities/artifacts)?
2. How do incidents get created (integrations, alert triage, manual creation, API), and how are related signals deduplicated/grouped?
3. What is the lifecycle: states from creation to closure; closure reasons; re-open?
4. How is response work organized and standardized (tasks, workbooks, stages, queues, playbooks-as-procedure)?
5. How is coordination done (owner/assignee, comments, war room, escalation, permissions)?
6. Where does evidence live (timeline, bookmarks, attachments, artifacts/IOCs, activity log) and who records it (human vs automation)?
7. What happens at closure (reports, metrics like MTTR, documentation/compliance use)?
8. How does automation relate to the case (playbooks run on cases; approvals; SLAs) — where does IR case management end and SOAR begin?
9. What integrations define the ecosystem (SIEM/EDR/TI/ITSM ticketing/forensics)?
10. Historical check: would a pre-automation, standalone IR case tool still satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different realization layers (SIEM-native, SOAR-native, TI-native; hyperscaler, enterprise, cloud):

| Product | Realization layer | Philosophy |
|---|---|---|
| Microsoft Sentinel | cloud SIEM with native incident/case management | analytics/detection-led; incident as evidence aggregation |
| Cortex XSOAR (Palo Alto Networks) | SOAR with incident management core | automation-first; incident lifecycle driven by playbooks and content packs |
| Splunk SOAR (Cloud) | SOAR (Phantom heritage) | orchestration-first; case = promoted container with workbook tasks |
| Exabeam (New-Scale / Threat Center) | SIEM platform with case management | triage/behavioral-analytics-led; detections → alerts → cases |
| ThreatConnect | threat intelligence platform with case management | TI-led; incidents as intel-associated records with task workflow |

IBM QRadar SOAR (the direct descendant of the original standalone "Incident Response Platform" heritage) was selected as a sixth sample but was unreachable (403 on both fetch attempts); see Source-access Limitation.

## Sources

Official operational documentation, fetched 2026-09-07:

- Microsoft Learn — Microsoft Sentinel documentation:
  - "Microsoft Sentinel incident investigation" (incident-investigation) — defines incidents as case-management records; evidence layer A
  - "Investigate Microsoft Sentinel incidents in depth" (investigate-incidents) — incident details page, timeline, entities, bookmarks, activity log, closure context; A
  - "Work with incident tasks" (work-with-tasks) — task workflow, automation-created vs ad-hoc tasks; A
  - Documentation landing page — confirm module inventory (investigate and respond section); A
- Cortex docs (cortex-docs.paloaltonetworks.com):
  - "Cortex XSOAR concepts" (8.x SaaS reference) — incidents, incident fields/types, lifecycle, War Room, context, indicators, playbooks, integration categories; A
  - Documentation "ask" responses citing "Incident Lifecycle" administrator guide; A
- Splunk documentation (help.splunk.com / docs.splunk.com):
  - "About Splunk SOAR (Cloud)" — SOAR definition combining orchestration, playbook automation, and case management; terminology table (container, case, artifact, indicator, playbook, workbook, action, owner/approvals/SLA); A
  - "Overview of cases" — containers promoted to cases; phases and tasks in workbooks; automation to track policy/compliance and fulfill documentation requirements; A
- Exabeam Documentation Portal (docs.exabeam.com):
  - "New-Scale Security Operations Platform" index — Threat Center, Alert Triage, Automation Management, Action Editor sections; A
  - "Threat Center" index — triage and response scope; A
  - "Work on Cases" guide structure — manually create a case; respond to a case (investigate, remediate, close, document, track progress); close cases; alerts triage and alert→case conversion; case notes/attachments/tags/history; case stages/queues/closed-reason configuration; permissions (Cases: Read / Read-Write-Delete); A
- ThreatConnect developer documentation (docs.threatconnect.com):
  - REST API Overview (v2) — group types including Incidents; Tasks with assignees/escalatees/status fields; Victims/victim assets; indicators with rating/confidence; security labels; TcEx "Module: Case Management"; REST API TOC listing "Case Management Endpoints" (v3); A
- IBM — `www.ibm.com/docs/en/qradar-soar` returned HTTP 403 on 2026-09-07 (two attempts, direct and versioned URL). **Source-access Limitation applied**: no IBM-specific claims are made anywhere in this research; the IBM Resilient "IRP heritage" is treated only as context for the historical check, with zero product-behavior assertions.

## Product Observations

### Microsoft Sentinel (evidence layer A — direct)

- Self-description: "a complete, full-featured case management platform for investigating and managing security incidents."
- **Incidents** are "files that contain a complete and constantly updated chronology of a security threat": individual pieces of evidence (alerts), suspects/parties of interest (entities), insights, and "comments and logs of all the actions taken in the course of the investigation."
- Incidents aggregate alerts generated by built-in detection rules or imported from third-party security products; they inherit entities, severity, status, and MITRE ATT&CK tactics/techniques from the alerts.
- Incident details page = central investigation location; goal framed as reducing SOC mean time to resolve (MTTR).
- **Incident tasks**: workflow task lists (auto-applied by automation rules/playbooks configured by senior analysts/managers; analysts can add ad-hoc tasks; marked complete as worked; purpose = "uniform standard of care", "prevent crucial steps from being missed", support for shift change/escalation).
- **Activity log**: tracks actions taken on the incident "whether initiated by humans or automated processes", plus comments; auto-refreshing; comment edit/delete permission rules (author edits; Contributor deletes); playbook results can be written back as comments.
- **Incident timeline**: chronological diary of alerts and **bookmarks** (snapshots of evidence saved from hunting); per-item severity, provider, tactics; alerts can be removed from an incident if irrelevant.
- **Entities**: user accounts, hosts, IPs, URLs, domains, file hashes, Azure resources, IoT devices; entity dossier (info/timeline/insights); actions: view full entity page, add to threat intelligence as IOC, run playbook.
- **Similar incidents** widget (shared entities/rule/alert details) for context; investigation graph (entity-relationship map) for visual investigation.
- Lifecycle controls visible: owner drop-down, status, severity can be changed; similar-incident widget surfaces other incidents' "last status (including, if they are closed, the reason they were closed)" → closure reasons exist.
- Automation boundary inside the product: **automation rules** (incident-handling: trigger tasks, assign, change status/severity, run playbooks) vs **playbooks** (logic-app response automation); "run playbook", "create automation rule", "create Teams case-collaboration" are incident actions.
- RBAC: Microsoft Sentinel Responder role required to investigate; Contributor required to delete comments; guest-user directory-role constraint for assignment.

### Cortex XSOAR (evidence layer A — direct)

- **Incidents** = "potential security data threats that SOC administrators identify and remediate." Triggers: SIEM alerts, mail alerts, security alerts from third-party services (SIEM, mailboxes, CSV, API).
- **Incident fields** hold data from integrations, manual input, or API; **incident types** out-of-the-box plus custom types with custom fields; **layouts** present incident data; **classification mapping** decides how ingested events become incident types and maps fields.
- **Incident lifecycle** (administrator guide): planning (fields/types/layouts) → integrations ingest → classification & mapping → **pre-processing rules** (link new events to existing incidents; drop duplicates/unwanted) → incident created and shown in the Incidents page → playbooks run (enrich, remediate) → **post-processing** (e.g., notify requester, close in a ticketing system).
- **War Room** = "collection of all investigation actions, artifacts, and collaboration pieces for an incident... a chronological journal of the incident investigation"; commands runnable from it (`/` system commands, `!` integration commands).
- **Context**: per-incident JSON store of every command/script/playbook output.
- **Indicators**: IP, URL, email, file hash, domains, CIDR, registry key; extracted from War Room entries; verdict/reputation machinery (DBot); indicator types extensible.
- **Playbooks**: "prescriptive procedures that query, analyze, and take action"; YAML; out-of-the-box + marketplace content packs (integrations, playbooks, scripts, fields, layouts).
- Integration categories include **Case Management**, **Forensics and Malware Analysis**, **IT Services**, **Data Enrichment & Threat Intelligence**, **Endpoint**, **Messaging** — i.e., the ecosystem is integration-mediated; ticketing systems are post-processing targets, not the case system itself.
- Dashboards/reports over incident/indicator data; jobs (scheduled/triggered); MSSP multi-tenant instance patterns; playground for safe experimentation.

### Splunk SOAR (Cloud) (evidence layer A — direct)

- Self-description: SOAR system combining "security infrastructure orchestration, playbook automation, and case management capabilities." Audience: SOC staff member, analyst, or manager (not primarily admin).
- Terminology: **Container** = ingested security event (default label Events); **Case** = "a special kind of container that can hold other containers... promote one of those containers to a case and then add the other related containers to the case... consolidate your investigation rather than having to investigate each container individually."
- **Artifact** = piece of information added to a container (file hash, IP, email header); **Indicator/IOC** = data populating CEF fields in an artifact; "smallest unit of data that can be acted upon."
- **Workbook** = "template providing a list of standard tasks that analysts can follow when evaluating containers or cases"; cases "have phases and tasks, which are organized into workbooks to track and manage all the actions taken."
- **Playbook** = automation tasks acting on new data; can run on containers or as part of workbook workflow; **Action** = high-level primitive (block ip, suspend vm, terminate process) provided by apps/assets.
- **Approvals**: actions on assets may require owner approval; approvals carry an SLA ("requests to run a particular action on an asset... contain a service level agreement (SLA) dictating the expected response time"); SLAs can be set on events, phases, and tasks.
- Case reports: "Create case reports to download and share"; automation of tasks "allows Splunk SOAR (Cloud) to be used to track policy and compliance, and to fulfill documentation requirements."

### Exabeam — Threat Center / New-Scale (evidence layer A — direct)

- Platform self-description: "unifies cloud-native SIEM and analytics... for threat detection, investigation, and response"; Threat Center = "Manage your entire triage and response."
- Object hierarchy: **Detections** (analytics/correlation/phishing/advanced-analytics detections) grouped by **detection grouping rules** into **Alerts**; **Alerts** triaged; alerts **converted into Cases**; **Cases** = "create a case to start tracking your response to a threat and assign the case to the person responsible for responding."
- Case work: "After you create a case, investigate, remediate, and close it. **Document your response and track your progress**." Closing = "change the case stage to closed."
- Case configuration: **Case Stages** (create/reorder/delete), **Case Queues** (create/edit/delete), **Case Closed Supporting Reason** (closure-reason configuration), detection grouping rules.
- Case collaboration & record: update case attributes (single/bulk), tags, **attachments** (attach/download/remove files on a case), **case notes** (add/edit/delete), case/alert **history**, share case info to email/webhooks.
- Investigation aids: entity watchlists (pre-built + custom; open/closed cases and alerts per entity; event timeline), risk scores, sort/filter by risk score/stage/queue/assignee/priority, search (query language + natural language), saved searches, case/alert metrics in dashboards, notifications, Threat Center APIs.
- Automation: run playbooks on cases or alerts (manual trigger); automation history per case/alert; Automation Management module integrates security tools.
- Permissions: object-scoped (Threat Center Cases: Read / Read-Write-Delete; Alerts same; Detection Grouping Rules; Watchlist).

### ThreatConnect (evidence layer A — direct, developer docs)

- Platform with both Threat Intelligence endpoints and **Case Management endpoints** (v3) and a TcEx "Module: Case Management" (create/get/delete) — case management is a named pillar of the product.
- **Incidents** exist as a **group type** (`/v2/groups/incidents`) alongside adversaries, campaigns, documents, emails, signatures, threats; groups associate with indicators, victims, tags, security labels, attributes.
- **Tasks** (`/v2/tasks`): assignees, **escalatees**, status field (observed value "Not Started"), escalated/reminded/overdue flags, associations to groups/indicators/tags; task workflow UI paths (workflow/task pages).
- **Victims** and victim assets (affected persons/assets) associate to incidents/groups/tasks — victim-centric response records.
- Indicators carry rating/confidence/threat-assess values; security labels gate sensitivity; owners scope data by organization/community.
- Interpretation: the incident is an intel-associated record with a task workflow — TI-led variant of the same case-management core (evidence A for object structure; interpretation layer C).

## Cross-product Comparison

| Dimension | Sentinel | XSOAR | Splunk SOAR | Exabeam | ThreatConnect |
|---|---|---|---|---|---|
| Central object name | Incident | Incident | Case (promoted container) | Case | Incident (group type) + Cases (CM endpoints) |
| Security-specific classification | severity, status, ATT&CK tactics inherited + editable | incident types + custom fields | labels; CEF artifacts | priority, detection-grouping attributes, risk score | incident group + rating/confidence on indicators |
| Evidence aggregation | alerts + bookmarks timeline | war room journal + artifacts/indicators | containers into case; artifacts | attachments, notes, history; alert linkage | associations (indicators, victims, files) |
| Recorded activity | activity log (human + automation) + comments | war room chronological journal | "all the actions taken" tracked in phases/tasks | case notes + case history | task/attribute records |
| Response lifecycle | status + closure reason; owner/severity editable | lifecycle stages: create → investigate → post-process → close (ticketing) | container → case; phases/tasks; reports | stages; queued; closed + supporting reason | task status/escalation; case workflow |
| Standard procedures | incident tasks auto-applied | playbooks as prescriptive procedures | workbooks (task templates) | playbooks run on cases | task templates/escalation |
| Assignment/coordination | owner; Teams case collaboration | assignee (field); MSSP instances | owner; approvals w/ SLA | assignee, queues, share to email/webhook | assignees, escalatees |
| Automation posture | automation rules + playbooks inside SIEM | playbook-first; context JSON | playbook-first; actions via apps | playbooks on cases/alerts | playbooks (v2) / automation apps |
| Metrics/reporting | MTTR framing; dashboards | dashboards, reports, email delivery | case reports; policy/compliance documentation | case & alert metrics dashboards | owner metrics; custom metrics |
| Permissions | platform RBAC roles | role-based (platform) | role-based (platform) | object-scoped Read / Read-Write-Delete | owner/organization scoping; security labels |

Stable commonalities (evidence B — cross-product, all five):

1. A named, individual **security incident case** object, distinct from the alert stream, with security-specific classification (severity/priority; incident type; in several products ATT&CK mapping).
2. The case **aggregates related security signals and artifacts** (alerts/detections; entities; IOCs/artifacts; files) — the case is the aggregation point of the response.
3. A managed **lifecycle** from creation through working states to closure, with **closure reason** recorded (directly documented in three of five).
4. A **recorded response activity** layer: chronological log of actions (human and automated), notes/comments, tasks — explicitly framed as documentation, accountability, continuity.
5. **Tasks** as the unit of standardized response procedure (ad-hoc + template/auto-applied), with assignment.
6. **Assignment/ownership** of cases (and queues/stages as routing structures in some).
7. **Investigation aids** binding the case to security semantics: entity/IOC extraction, enrichment, similar-incident context, drill-down to underlying logs.
8. **Integration-mediated ecosystem**: detection sources feed in; ticketing (ITSM), forensics, TI, messaging connect out — the case system integrates with, rather than replaces, neighbors.
9. **Permissions** gate case access/actions (role- or object-scoped).
10. **Metrics/reporting** over cases (dashboards, reports; MTTR framing; documentation/compliance use).

Variable dimensions (variants): automation depth (none→full orchestration); packaging (SIEM-embedded, SOAR-embedded, TI-embedded, standalone-heritage); evidence granularity (bookmarks vs artifacts vs attachments); approval/SLA machinery; collaboration surfaces (built-in comments vs external team chat); victim records (TI-heritage); case-stage/queue configurability; entity-risk scoring.

## Canonical Model (three-layer filter applied)

### L0 — Defining Invariant (deliberately minimal)

```text
Security Incident Case (structured record of one security incident under managed response;
                        security-specific classification: severity/priority + incident type;
                        aggregation point for related alerts/detections, entities, artifacts/IOCs)
└── Response Lifecycle (managed states from creation to closure; closure carries an outcome/reason)
└── Recorded Response Activity (who did what, when, what was found — notes/comments, tasks,
                                logged actions by humans and automation — the response record)
```

Three invariants. Remove the incident case (keep only detection/alerting) → SIEM/EDR, not IR management. Remove the security-specific classification/aggregation semantics (keep generic service tickets) → IT Incident Management. Remove the recorded activity/lifecycle (keep only automated action execution) → an automation engine, not incident response management.

Nothing in L0 requires: cloud delivery, playbook automation, AI, MITRE mapping, specific integrations, queues/stages, approval workflows, or any specific object name ("incident" vs "case" both qualify).

### L1 — Common Mature Structure (standard capabilities; all evidenced across the sample)

- Intake machinery: automated ingestion of alerts from detection products (SIEM/EDR/mail/third-party/API), manual case creation, alert-triage with convert-to-case, deduplication/linking of related signals (pre-processing rules, detection grouping, container promotion).
- Task workflow: task lists on cases; template/auto-applied standard procedures; ad-hoc tasks; task completion tracking; assignment.
- Routing & organization: owner/assignee; queues; case stages; priority/severity adjustment; bulk operations.
- Collaboration: comments/notes; activity history; case sharing (email/webhook in one product; team-chat creation in another).
- Investigation aids: entity/IOC extraction and enrichment, threat-intelligence linkage, similar-incident surfacing, drill-down to underlying logs/queries, investigation graphs (some), entity watchlists (some).
- Evidence handling: bookmarks/saved query results, file attachments, artifacts/CEF fields; case reports for download/share.
- Automation hooks: playbooks runnable on cases/alerts; automation history on the case; automation-created tasks/comments.
- Metrics & reporting: case dashboards, response-performance metrics (MTTR framing), reports for stakeholders; documentation/compliance use.
- Permissions: role- or object-scoped read/write/delete; separation between analyst work and admin configuration.
- APIs: programmatic case management surfaced in the sample.

### L2 — Variant / Optional Structure

- Packaging: SIEM-embedded, SOAR-embedded, TI-embedded, or standalone; suite module vs free-standing product (this axis is the dominant market-shaping variant).
- Automation depth: manual-checklist-only → suggested/templated procedures → machine-executed response actions with approvals/SLAs.
- Deployment: cloud SaaS vs self-hosted; data-residency options (documented in one product).
- Customer tier: single-SOC enterprise vs MSSP multi-tenant operations (documented in one product).
- Security-semantic depth: ATT&CK tactic mapping, UEBA/risk scoring, entity pages — common but not definitional.
- Victim-centric records (affected persons/assets) — TI-heritage variant (one product).
- Regulatory/breach-reporting depth — not directly evidenced in the reachable sample; treated as unverified.

### L3 — Vendor-specific (research notes only; excluded from the final document)

- Sentinel: SecurityIncident table record-size and comment limits; similar-incident count/window; entity-timeline window; investigation-graph age limit; specific role names; Teams integration; bookmark object; UEBA insights.
- XSOAR: War Room CLI (`/` vs `!` commands); per-incident JSON context; DBot indicator extraction/reputation scripts; content packs/marketplace; playground; engines; EDL indicator export; classification/pre-processing/post-processing stage naming; COPS YAML.
- Splunk SOAR: container→case promotion mechanics; CEF fields; apps/assets/actions model; owner approvals with SLAs on events/phases/tasks; Phantom heritage; Python playbook API.
- Exabeam: Threat Center naming; detections→alerts→cases hierarchy via detection grouping rules; case stages/queues/closed-supporting-reason configuration; risk scores; watchlists; Action Editor; EQL/natural-language search; portfolio licensing tiers.
- ThreatConnect: incidents-as-group-type; victims/victim assets; rating/confidence/threatAssess on indicators; security labels; owners (org/community); escalatees on tasks; TcEx app framework.

## Vendor-specific Findings

- The case-management layer exists in every sampled platform even though none of the five sells itself primarily as a "Cyber Incident Response Platform" — four self-identify as SIEM/SOAR/TI platforms and one (Sentinel) explicitly self-identifies as providing "case management" for security incidents. This is the central market finding of this pass.
- Only Splunk documents formal approval/SLA gating of response actions; do not generalize.
- Only ThreatConnect documents victim/victim-asset records; do not generalize.
- Only Exabeam documents explicit configurable case stages/queues/closure-supporting-reason objects; Sentinel evidences closure *reasons* on incidents (via the similar-incidents display) without documenting a configurable reason catalog in the fetched pages.

## Boundary Findings

- **vs SIEM**: SIEM's defining core is telemetry collection + detection (alerts). The IR platform's defining core is the managed response case. Observed realization: SIEM products embed an incident/case-management layer with its own object family and lifecycle — recognizable as this Type inside the SIEM. Test: remove the case layer and the product is still a SIEM; remove detection and it can still be an IR case platform.
- **vs SOAR**: SOAR's defining core is orchestration + automation (playbooks executing actions across tools). Case management is one named pillar of sampled SOAR products, but the case layer is realizable without any automation (manual task checklists satisfy the core), so automation is not the invariant. Test: remove playbooks/orchestration from the product and the incident case core remains this Type; remove the case core and what remains is an automation engine. → The leaf is NOT an alias of SOAR; it is the case-management core that SOAR contains. However, see Taxonomy Note.
- **vs Incident Management (IT/ITSM)**: ITSM incidents are service disruptions with restore-service semantics; security incident cases are adversarial events investigated through evidence, entities/IOCs, containment. Observed seam: a sampled SOAR product's post-processing explicitly closes incidents *in a ticketing system* — IR case systems integrate with ITSM rather than replace it. Test: replace security classification/evidence semantics with service-restoration semantics and it becomes IT Incident Management.
- **vs Digital Forensics Platform**: forensics platforms acquire/examine disk/memory/data images; the IR platform records and coordinates response; forensic tooling appears as an integration category (documented in one product) and forensic artifacts attach to cases as evidence. Test: remove the case/coordination record and keep evidence acquisition/examination → Digital Forensics Platform.
- **vs Threat Intelligence Platform**: TIP's core is indicator corpora/adversary knowledge; IR consumes indicators for enrichment. One sampled TI platform embeds case management — same embedded-realization pattern as SIEM/SOAR.
- **vs SOC Platform**: umbrella/aggregation category; the case layer is one component.
- **vs On-call Management / EDR**: paging/escalation of responders is adjacent (task escalation exists in one sample) but not the case system; EDR response actions are endpoint-scoped detections, not incident case management.
- **"去掉什么就变成另一个 Type" 判据**: (a) remove the incident case + lifecycle → detection product (SIEM/EDR) or TI platform; (b) remove security-specific case semantics → IT Incident Management; (c) remove recorded response activity/lifecycle → automation/orchestration engine; (d) remove evidence aggregation but keep tickets → generic ticketing/ITSM.

### Taxonomy Note (escalation candidate)

Modern market realization is overwhelmingly embedded: in the five-product sample, zero products market primarily under the "incident response platform" label; the case-management core is a layer inside SIEM/SOAR/TI suites. The historical standalone-IRP lineage (IBM Resilient heritage; DFLabs IncMan heritage) was not directly verifiable in this pass because IBM docs were unreachable. Recommendation: joint review of `cyber-incident-response-platform` with `soar` and `soc-platform` leaves to decide variant-vs-sibling presentation; the documented core here is deliberately automation-free so it can serve as the shared case-management layer definition either way. Recorded in STATUS.md Boundary Issues.

## Historical / Market-Sample Check

- The synthesized L0 contains no automation, cloud, AI, or vendor-era machinery. A pre-automation incident-response case tool (case record + lifecycle + tasks + activity record) satisfies the definition; only the *intake* (manual reporting vs machine alerts) and *execution* (human vs playbook) mechanisms differ, and both are mechanism-variants in the model.
- Older/regional/security-specific-but-smaller deployments (e.g., a national CSIRT case system, an IR consultancy's case tracker with severity/lifecycle/notes) fit the L0. A team managing incidents purely in a generic IT ticket queue does *not* instantiate the Type (no security-specific case semantics), which matches the boundary test against IT Incident Management.
- Conclusion: the definition is not over-fitted to the current SIEM/SOAR-embedded realization. Check passed.

## Uncertainties

1. IBM QRadar SOAR (heritage standalone IRP) unreachable — the standalone-pole behavior is unverified from primary sources; all claims rest on the five reachable products.
2. Whether any current standalone pure-play "cyber incident response platform" products hold meaningful market share — not verifiable from the reachable sample; the final document therefore presents packaging as a variant spectrum rather than asserting the standalone pole is extinct.
3. Reopen/reopened-case behavior — not directly evidenced; not claimed.
4. Regulatory breach-notification machinery depth — not evidenced in fetched pages; not claimed.
5. Exact status vocabularies (state names) vary and were not uniformly documented; the final document describes lifecycle conceptually without asserting a universal state list.
6. Whether case management endpoints (v3) in the TI-heritage sample differ materially from its v2 incident groups — v3 detail pages not fetched; treated structurally.

## Final Synthesis

A Cyber Incident Response Platform is the application a security team uses to manage the response to security incidents. Its defining core is the **security incident case**: a structured, individually identified record of a security incident under managed response, classified with security-specific dimensions (severity/priority, incident type), serving as the aggregation point for the related alerts/detections, entities, and artifacts/IOCs. The case moves through a managed **response lifecycle** from creation to closure (closure carries an outcome/reason), while the platform accumulates the **recorded response activity** — notes/comments, tasks, and logged actions by humans and automation — as the response's durable record. Around this core, mature products add intake machinery from detection sources with deduplication/grouping, task workflows standardizing the response, routing (ownership, queues, stages), collaboration, investigation aids (entity/IOC enrichment, similar incidents, log drill-down), automation hooks, metrics/reporting (including MTTR framing and documentation/compliance use), permissions, and APIs. The Type's most distinctive market fact: it is realized today mostly as the case-management layer inside SIEM, SOAR, and TI platforms rather than as standalone products, with automation depth the principal axis differentiating realizations.
