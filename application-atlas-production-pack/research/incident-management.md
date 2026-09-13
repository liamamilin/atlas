# Research Notes — Incident Management

Slug: incident-management
Directory leaf: Incident Management (§14 IT, Cloud & Infrastructure)
Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 + WRITING_GUIDE_v1.1)

---

## Research Goal

Understand what an "Incident Management" application actually is as an Application Type, in the IT/cloud-operations sense of the directory leaf: what objects exist inside it, how an incident moves from detection to resolution, who participates, what rules govern the response, and where its boundary lies against the many neighboring Types that share vocabulary (on-call management, status pages, ITSM, problem management, ticketing, AIOps, observability, security incident response, emergency management).

Note: the directory contains multiple "incident" leaves across domains (Cyber Incident Response Platform §15, Environmental Incident Management §21, Emergency Management Platform §24). This leaf is the IT/service-operations one. Both processed neighbors already articulate their boundary toward it.

## Initial Boundary (hypothesis before research)

- Core use: coordinating an organization's response to unplanned disruptions of services (outages, degradations, threats) so service is restored quickly and the response is recorded.
- Users: on-call engineers, SREs, NOC operators, IT service desk, incident commanders/managers, service owners, stakeholders.
- Nearest neighbors: On-call Management (schedules/escalation), Status Page Platform (stakeholder comms), ITSM (umbrella discipline), IT Problem Management (root cause), Ticketing System (generic record machinery), AIOps (signal analysis), monitoring/observability (detection), Cyber Incident Response Platform (security domain), Emergency Management Platform (physical-world domain).
- Unknowns: is on-call machinery definitional or a common implementation? Is stakeholder communication definitional? Where exactly does the record stop and the adjacent Types start?

## Research Questions

1. What is an "incident" in these products — how is it defined and what does the record carry?
2. What is the lifecycle/state model, and how strictly is it enforced?
3. How do incidents get created (machine vs human intake) and how are alerts related to incidents?
4. How are responders mobilized — what is the role of escalation policies, on-call schedules, acknowledgement?
5. What coordination surfaces exist during response (channels, war rooms, roles, tasks)?
6. How does stakeholder/customer communication work, and is it part of the product or an integration?
7. What happens after resolution — postmortems, follow-ups, metrics?
8. What anchors the incident (service catalog, teams, CIs)?
9. Where does this Type end and On-call Management / ITSM / monitoring / security / emergency management begin?

## Representative Products

Selected to span product philosophy and customer tier:

| Product | Philosophy | Customer tier | Evidence depth |
|---|---|---|---|
| PagerDuty | pure-play, mobilization-rooted (alert→page→respond heritage) | mid-market → enterprise engineering/ops | Tier 1 (support docs, incident lifecycle pages) |
| Atlassian (Jira Service Management + incident-management practice content) | ITSM-suite-anchored incident practice (Opsgenie heritage folded in) | small teams → enterprise, IT + dev | Tier 1–2 (official incident-management hub + lifecycle pages; product support pages unreachable) |
| Datadog | observability-platform-embedded incident management | dev/ops teams, mid-market → enterprise | Tier 1 (product docs) |
| incident.io | comms-platform-native (Slack/Teams), workflow-automated | startups → scale-ups | Tier 1 (help center + API object inventory) |

Cross-domain contrast (used for boundary reasoning, not as samples of this Type): Cyber Incident Response Platform (SOAR/SIEM case management), Emergency Management Platform (public-sector response coordination), Environmental Incident Management (EHS), Ticketing System (generic machinery).

## Sources

Fetched 2026-09-08 unless noted:

- PagerDuty — Incidents (statuses, lifecycle, trigger/declare, timeline): https://support.pagerduty.com/main/docs/incidents
- Atlassian — Incident Management overview (definition, ITIL workflow, DevOps process, postmortems): https://www.atlassian.com/incident-management
- Atlassian — Incident Response Lifecycle (7 stages, NIST comparison): https://www.atlassian.com/incident-management/incident-response/lifecycle
- Datadog — Incident Management (declare, describe, search, analytics, integrations): https://docs.datadoghq.com/monitors/incident_management/
- incident.io — Help center index (453 pages, structure) + Declaring incidents + API tag inventory: https://docs.incident.io/ , https://docs.incident.io/incidents/declaring , https://docs.incident.io/llms.txt

Failed/abandoned per source-access rules:

- https://www.pagerduty.com/what-is-incident-management/ → 404 (marketing page gone; support docs used instead)
- https://docs.datadoghq.com/incident_management/ and /incidents/ → 404 (docs reorganized; /monitors/incident_management/ reachable)
- https://support.atlassian.com/jira-service-management-cloud/docs/incident-management/ → 404 (JSM product support docs not reached; Atlassian official practice pages used)

Not attempted (time budget): ServiceNow (previously unreachable in other passes per logs), Rootly, FireHydrant, Freshservice. incident.io's own migration pages (PagerDuty, Opsgenie, Blameless, FireHydrant, Rootly, ServiceNow incident-history import; schedule mirroring to PagerDuty) serve as cross-product existence evidence for the category.

---

## Product A — PagerDuty

### Key observations (evidence layer A unless noted)

**Definition.** "An incident represents a problem or an issue that needs to be addressed and resolved. Incidents trigger on services, and a service's escalation policy prompts notifications to on-call responders to remediate the issue."

**Record.** Incidents are created on services; each has an incident number (occasionally skipped at creation), a title, description, optional impacted service, urgency (high/low), optional priority, assignee (required — escalation policy or user), additional responders, optional conference bridge/dial-in/meeting URL. Alerts are distinct objects attached to incidents (an event creates an alert and an associated incident; multiple alerts can aggregate into one incident via dedup key).

**States.** Exactly three: **Triggered → Acknowledged → Resolved** (+ reopen). Acknowledgement claims ownership and halts escalation; if the acknowledgement timeout is reached, the incident returns to Triggered and escalation resumes. Unacknowledge is possible (returns to Triggered). Resolve closes; reopen if further work is needed. Alerts cannot be acknowledged — only triggered or resolved; when all alerts in an incident are resolved, the incident resolves.

**Mobilization machinery.** Escalation policies with one or more levels, each targeting a schedule or a user; escalation timeout escalates to the next level; notifications continue per user notification rules (push, phone, Slack, email, SMS) until acknowledged/resolved/escalated. **If no one is on call per the service's escalation policy, no incident is created** (coverage gap ⇒ dropped event). "Paging" = incident triggering on a service and escalating through its policy.

**Intake.** Triggered (automatic: monitoring integrations, Events API, email integration, Slack commands) vs Declared (manual: web app, mobile, REST API). Initial status is always Triggered. Event Orchestration centralizes integrations into routing rules to services. Suppressed alerts collect data without paging.

**Timeline.** Every incident has a Timeline tab: timestamps of each status change plus all actions taken and notifications sent; filterable by event type.

**Governance.** Permissions gate manual declaration (stakeholder roles cannot trigger; observers restricted to their teams); Account Owner can redact an incident's details; auto-resolve is force-enabled for services with very high open-incident volume; acknowledgement count is capped.

**Structure implied.** Services (with escalation policies + integrations + urgency/support hours), escalation policies, schedules, users/teams, incidents, alerts, notification rules, timeline, analytics.

## Product B — Atlassian (Jira Service Management + official incident-management practice content)

### Key observations

**Definition.** "Incident management is the process used by development and IT Operations teams to respond to an unplanned event or service interruption and restore the service to its operational state." "We define an incident as an event that causes disruption to or a reduction in the quality of a service which requires an emergency response." ITIL-following teams may say "major incident."

**Nature of incidents.** Incidents "vary widely in severity, ranging from an entire global web service crashing to a small number of users having intermittent errors." An incident is resolved "when the affected service resumes functioning in its intended state. This includes only those tasks required to mitigate impact and restore functionality" — restoration-focused, not root-cause-focused.

**ITIL-shaped workflow.** Identify and log (incident tickets with report date/time, reporter, description, impact) → categorize → prioritize (impact assessment, predefined severity/priority levels, SLAs) → initial diagnosis → escalate to next tier → investigation and diagnosis → resolution and recovery → closure. Incidents can come "from anywhere: an employee, a customer, a vendor, monitoring systems."

**DevOps/SRE-shaped lifecycle (7 stages).** 1 Detect (monitoring/alerting tools; sometimes customers/team members) → 2 set up team communication channels (dedicated channel + video bridge) → 3 assess impact and assign severity (drives who to contact, resolution plans, external comms; triggers automated actions) → 4 communicate with customers/stakeholders → 5 escalate to the right responders (paging via alerting) → 6 delegate incident response roles (incident manager delegates; incident commander concept; pre-built playbook) → 7 resolve (impact ended; transition to cleanup and postmortem). "These approaches are not linear."

**Tooling claims.** Jira Service Management keeps "a robust incident timeline"; alerting + on-call features from Opsgenie are now part of JSM and Compass (migration deadline published); postmortem = post-incident review, capturing lessons learned; severity levels, on-call schedules, escalation policies, and alert fatigue are all first-class practice topics in the official content.

**Alternative frame.** NIST's security incident response lifecycle (Preparation; Detection & Analysis; Containment, Eradication, Recovery; Post-Event Activity) presented as the adjacent security-flavored variant.

## Product C — Datadog (Incident Management within the Datadog platform)

### Key observations

**Definition/positioning.** "Datadog Incident Management helps your team members identify, mitigate, and analyze disruptions and threats to your organization's services... design an automation-enhanced response process that helps your teams assemble around a shared framework and toolkit." Breadcrumb taxonomy: "Incident Response > Incident Management."

**Intake.** Incidents "live in Datadog alongside your metrics, traces, and logs." Declared from monitor alerts, security signals, events, cases; monitors can be configured to declare incidents automatically.

**Record.** Incidents carry title, severity level, incident commanders; updatable status, impact, root cause, detection methods, service impacts; custom responder roles; metadata attributes. Incident list is a searchable feed: filter facets include Status, Severity, Time To Repair, services, teams, responders, root-cause category; event-based search syntax (severity:SEV-1, state:active/resolved, etc.).

**Analytics.** Incident Analytics: time to resolution, customer impact tracked over time; graphable in dashboards/notebooks; provided templates (Incident Management Overview Dashboard, Notebook Incident Report).

**Ecosystem.** Native: Status Pages (public/private) connected to incidents; On-Call (escalate pages into incidents; page teams from an incident); Notebooks for postmortems; Workflow Automation. Third-party: Atlassian Statuspage, Confluence (postmortems), Jira/ServiceNow tickets, Slack/Teams channels + video meetings, PagerDuty/OpsGenie paging with auto-resolve on incident resolution, Zoom, webhooks. Seat-based SKU; mobile app for viewing/creating/managing incidents.

## Product D — incident.io

### Key observations

**Positioning.** "The all-in-one platform for on-call, incident response, Investigations and status pages." Products: On-call (alerting, flexible schedules, reliable paging), Response, Status Pages; platform: Catalog, Workflows, Insights, Integrations.

**Declaration.** Three incident types: **live** (happening now), **retrospective** (documenting something that already happened), **test** (practice). Declared from Slack (`/incident`, message shortcut), browser (inc.new), Teams tab, API; customizable declaration forms (fields configurable, required/optional); anyone can declare by default, admins can restrict per type; private incidents supported.

**Response workspace.** On declaration, the product automatically assembles: dedicated Slack/Teams channel (responders, updates, actions), video call war room (Meet/Zoom/Teams), linked ticket in the issue tracker (Jira/Linear/ServiceNow), announcement in an incidents channel. Workflows then automate role assignment, status updates, and more. Channelless incidents and incident "modes" exist; incidents can be merged, paused, reopened, made private, deleted/hidden (permissions-gated).

**Coordination.** Custom incident roles ("Knowing who's in charge" — incident lead/commander concept; roles assignable from on-call schedules); task tracking/actions; status updates to team; customer updates; escalating incidents; duplicate-prevention; subscriptions; active participants vs observers.

**Alert pipeline.** Alert sources from monitoring/error-tracking/ticketing tools; deduplication; alert grouping ("triage, escalate and attach them to incidents as one"); escalations from alerts; incidents created automatically via alerts; alert notes/timelines exist without needing an incident; maintenance windows; priority/urgency/severity distinction documented (same triad as PagerDuty).

**On-call substrate.** Schedules (rotations, timezones, holidays/PTO via HRIS, overrides, shift swaps, coverage policies), escalation paths (round robin, snoozing, reassignment, out-of-hours delays), notification policies, mobile/SMS/voice ack. Schedule mirroring to PagerDuty; migrations from PagerDuty/Opsgenie.

**Post-incident.** Post-incident flow; debriefs; post-mortems as collaborative AI-native documents (templates, sharing/export to Google Docs/Notion/Confluence/SharePoint, external postmortems); generated incident timeline; follow-ups (action items) synced to issue trackers with priorities and completion policies.

**Structure.** Catalog = services/systems/teams/ownership (imports from Backstage/Cortex/Opslevel), consumed by on-call routing and incident scoping; Insights = incident volume, MTTR/MTTA, pager load, out-of-hours paging, follow-ups; Nexus = AI agent for investigation/root cause over catalog + incidents + telemetry + code.

**API object inventory** (structural evidence): incidents, incident statuses, incident roles, incident participants/memberships, incident updates, incident timeline items, incident timestamps, incident alerts, incident attachments/relationships/types/templates, severities, escalations + escalation paths, schedules + entries + overrides, follow-ups, postmortem documents, status pages + status-page incidents/updates, catalog entries/types, workflows/workflow runs, maintenance windows, activity log entries, audit logs.

---

## Cross-product Comparison

| Dimension | PagerDuty | Atlassian (JSM) | Datadog | incident.io |
|---|---|---|---|---|
| Unit of record | Incident on a service | Incident ticket (ITIL) / incident (DevOps) | Incident in platform | Incident (live/retro/test types) |
| Creation | auto-trigger from integrations + manual declare | from anywhere: employees, customers, vendors, monitoring | monitor alerts, security signals, events, cases; auto from monitors | alerts (auto) + manual declare (Slack/Teams/web/API) |
| State model | Triggered → Acknowledged → Resolved (+reopen; ack timeout re-triggers) | ITIL: log→categorize→prioritize→diagnose→escalate→resolve→close; lifecycle stages | Status facet incl. active/resolved; updatable status | lifecycle page; statuses object; pause/merge/reopen; retro incidents |
| Classification | priority (incident) / urgency (notification) / severity (alert) | impact → severity level; predefined levels | severity (SEV-n); root cause; detection method; service impacts | severities; priority/urgency/severity triad documented |
| Mobilization | escalation policies over schedules/users; paging; ack stops escalation; no on-call ⇒ no incident | escalate to right responders (paging); on-call rotations | On-Call integration: escalate pages into incidents; page from incident | escalation paths over schedules; escalations from alerts; ack machinery |
| Coordination | responders, conference bridge | comms channel + video bridge; roles (incident commander) | incident commanders, custom responder roles | auto channel + war-room call; custom roles; tasks/actions |
| Comms | notifications to responders (paging channel) | internal + customer comms; templates | stakeholder notifications; Status Pages | status updates; customer updates; Status Pages |
| Timeline | Timeline tab, timestamped, filterable | "robust incident timeline" kept by tool | incident activity (timeline items in API era) | generated timeline; editable |
| Anchor object | service (+ escalation policy) | service/ticket categories (ITIL) / services (modern) | services, teams | catalog (services, teams, ownership) |
| Post-incident | reopen; analytics | postmortem / post-incident review | postmortems via Notebooks/Confluence | post-mortems, debriefs, follow-ups |
| Metrics | analytics on incidents | KPIs: severity levels, common metrics (MTTA/MTTR-class) | time to resolution, customer impact | MTTR/MTTA, pager load, volume |
| Status pages | external product territory | incident communication (JSM); Statuspage integration | native + Atlassian Statuspage | native public/internal |
| On-call machinery | native core | native (Opsgenie heritage) | via Datadog On-Call | native On-call product |

### Findings stable across the sample (evidence layer B)

1. The incident is a persistent, identified record — numbered/title/severity/status — distinct from raw alerts and from chat.
2. A managed lifecycle from creation (triggered/declared) through acknowledgement/working to resolution, with recorded dispositions and timestamps of every action.
3. Severity/priority classification assigned during triage, driving routing and communication.
4. Mobilization machinery: routing to accountable responders through assignment/escalation, commonly implemented as escalation policies over on-call schedules, with acknowledgement tracking.
5. Multi-person response coordination: roles (commander/lead), a dedicated communication surface (channel/bridge/war room), tasks/actions.
6. Stakeholder communication is a named concern in all four (status updates; customer communication; status pages).
7. An accumulated incident timeline of what happened and who did what.
8. Post-incident learning (postmortem/review) and follow-up actions, plus response metrics (MTTA/MTTR-class).
9. Intake is multi-source: monitoring integrations (machine) and humans (declared); alert-to-incident aggregation (dedup/grouping) exists in the alerting-rooted products.

### Layer C — canonical inference

The Type is best modeled as the **on-call operations response system of record**: it holds the incident of record, runs the managed restore-response loop over it, and does so through standing mobilization machinery. Detection (monitoring), coverage (schedules), and communication publication (status pages) surround it but do not constitute it.

---

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The incident of record** — a persistent, individually identified record of a declared abnormal condition disrupting or threatening a service/operation, carrying state, severity/priority classification, and an accumulating timestamped trail.
   - remove → alert stream / monitoring dashboard / ops log with nothing managed.
2. **The managed restore-response loop** — the record is triaged/classified by severity and impact, mobilized to accountable responders, worked under time pressure toward mitigation/restoration of the service, and resolved to a recorded disposition; the lifecycle is managed by the system (states, timestamps), not free-form.
   - remove → a static incident log or a chat war room; the "management" is gone.
3. **The standing mobilization structure** — predefined, severity-driven organizational machinery that decides who responds and how fast: assignment/escalation routing to responders/teams (commonly escalation policies over on-call schedules), engaged at declaration time.
   - remove → generic ticket-queue handling; machinery alone without the record → paging tool (On-call Management territory).

Jointly-held is load-bearing:
- 1 alone = incident log / postmortem archive.
- 2 alone = ephemeral war-room coordination with nothing of record.
- 3 alone = alert-routing/paging tool (On-call Management).
- 1+2 without 3 = issue tracker with incident states but no accountability routing.
- 1+3 without 2 = pager dump — escalation machinery with no worked-to-restoration record.
- 2+3 without 1 = live response choreography with no system of record.

### L1 — Common Mature Structure

- Monitoring/alert integrations as first-class intake; alert dedup/grouping into incidents; maintenance windows/suppression.
- Severity/priority/urgency taxonomy (three distinct concepts in the alerting-rooted products; severity/priority in the ITSM pole) configured by the org.
- On-call schedules + escalation policies + paging + acknowledgement tracking as the standard implementation of the mobilization structure.
- Dedicated response coordination surface: auto-created channel, conference/video war room, responder roles (incident commander/lead), task/action tracking.
- Stakeholder communication: status updates, subscriber/customer messaging, status-page publication (native or integrated).
- Auto-generated incident timeline (editable in some products).
- Service catalog / team / ownership anchoring for scoping and routing.
- Post-incident layer: postmortem/post-incident review documents, follow-up/action items (often synced to issue trackers), debriefs.
- Response analytics: MTTA/MTTR-class measures, incident volume, pager load.
- Access governance: who can declare/ack/resolve; private incidents; audit trails.

### L2 — Variant / Optional Structure

- **Packaging** — the dominant variant axis: (a) ITSM-suite-embedded (incident as one practice among request/problem/change), (b) pure-play incident response (PagerDuty/incident.io class), (c) observability-embedded (Datadog), (d) comms-platform-native (incident.io's Slack/Teams posture).
- Incident taxonomies: incident types (security, data, customer-impact...), private incidents, test/drill incidents, retrospective-only incidents (documented after the fact).
- AI assistance: summaries, suggested actions, AI investigation/root-cause agents over telemetry and catalog (era-current; strongest in newest products).
- Channelless incidents vs channel-mandatory (comms-platform-native pole).
- Alert-tier triage without incidents (alert notes/timelines) in alerting-rooted products.
- Mobile-first responder apps; SMS/voice paging reach (regional constraints noted by incident.io for China).

### L3 — Vendor-specific (research notes only)

- PagerDuty: three-state model with acknowledgement-timeout re-triggering; no-on-call ⇒ no incident created; 100-event dedup cap per incident; forced auto-resolve for services with >100K open incidents; redaction; skipped incident numbers; stakeholder role gating.
- Atlassian: 7-stage published lifecycle; NIST comparison; Opsgenie migration deadline into JSM/Compass.
- Datadog: "Time To Repair" facet; seat-based SKU; Notebooks-based postmortems; breadcrumbs "Incident Response > Incident Management."
- incident.io: inc.new shortcut; live/retro/test incident types; Nexus AI agent; Scribe call transcription; "Rate this incident"; schedule mirroring to PagerDuty.

## Historical / Market-Sample Check (per methodology)

- **ITIL-era service desk (1990s–2000s ITSM suites: Remedy-class products).** Incident record + log/categorize/prioritize/diagnose/escalate/resolve/close + assignment groups and priority matrices satisfies all three L0 structures without paging integration, chat war rooms, status pages, or postmortem automation. Satisfied — the definition does not depend on the modern mobilization stack (schedules/escalation policies are the common *implementation* of the mobilization structure, not the invariant).
- **Alerting/paging heritage (2000s–2010s NOC paging tools, Opsgenie-class).** Strong mobilization machinery; incident record thinner but present (pages grouped into incidents). Satisfied.
- **Pre-software practice.** NOC major-incident practice: incident ticket + duty roster + phone tree + bridge call + handwritten timeline. Structurally satisfies L0 (record, managed loop, standing mobilization) — C-level inference, qualitative.
- Conclusion: the L0 holds across eras; the L1 machinery is era-current. Phone/chat-tool coupling, status pages, AI, and postmortem automation are deliberately NOT in the defining core.

## Vendor-specific Findings

See L3 above; none promoted to the canonical core.

## Boundary Findings

| Neighboring Type | Relationship | Boundary judgment |
|---|---|---|
| On-call Management (§14, unprocessed) | closest sibling; commonly fused in products | On-call Management's unit is **coverage**: schedules, rotations, overrides, fairness, notification reach — no incident of record. Incident Management's unit is the **incident**: it *consumes* schedules/escalation paths as the mobilization implementation. Pure paging/routing without incident record = On-call Management. Joint review recommended. |
| Status Page Platform (§14, unprocessed) | integrated neighbor | Status page = stakeholder-facing communication publication surface (components, subscribers, uptime display). Incident Management = the internal response record that *publishes to* status pages. All four sampled products treat it as a separate surface (native module or integration). Separate Type. Joint review recommended. |
| IT Service Management / ITSM (§14, unprocessed) | umbrella discipline | ITSM = the whole service-management practice (request, incident, problem, change, assets, CMDB). Incident Management is one practice, sold standalone (pure-play) or embedded. Keep both; the ESM pass (processed) already treats incident/problem/change as "the IT provider's practices." |
| IT Problem Management (§14, unprocessed) | downstream sibling | Problem = root cause of recurring incidents; receives post-incident output. Atlassian's own definition draws the line: incident resolution is "only those tasks required to mitigate impact and restore functionality" — diagnosis of underlying cause is problem territory. |
| Ticketing System (§07, processed) | machinery vs semantics | Ticketing System = generic demand-processing record machinery (queues, states, disposition), domain-neutral. Incident Management adds emergency-response semantics: severity-driven mobilization, standing escalation, restore-service goal under time pressure. An incident ticket is a specialization the ticketing leaf explicitly anticipates. |
| AIOps Platform (§14, processed) | upstream analysis | AIOps = machine-executed analysis over the operational signal stream; its output ("correlated incident, probable cause") drives response "through notifications, tickets, and automation." Incident Management is where the human-coordinated response of record lives. AIOps products' incidents are signal-correlations, not managed response records. |
| Infrastructure Monitoring / APM / Log Management (§14, processed) | detection side | Monitoring detects conditions and emits alerts; no response record, no mobilization. The seam is the alert handoff (Datadog: monitors "declare incidents automatically"). |
| Cyber Incident Response Platform (§15, processed) | name collision, adjacent domain | Its own pass: "IT incidents are service disruptions resolved by restoring service; security incident cases are adversarial events investigated through evidence and containment... if it moves to restoring disrupted services under service-management semantics, it is IT incident management." Boundary ratified from both sides. |
| Emergency Management Platform (§24, processed) | name collision only | Its own pass: "Technology incident response with its own object world (services, on-call, alerts); shares the word 'incident,' not the structure." Consistent. |
| Environmental Incident Management (§21, processed) | name collision only | EHS domain: environmental consequence, regulatory reportability. Different object world (media, substances, agencies). |
| Error Tracking Platform (§12, unprocessed) | upstream signal source | Error aggregation is detection; spikes feed incident declaration (incident.io lists Sentry as an alert source). Different unit of record. |
| Enterprise Service Management (§10, processed) | scope expansion | ESM extends service machinery to all departments; "incident, problem, change... belong to the IT provider." Incident Management remains the IT-operations instance. |

"Remove test": strip the standing mobilization structure and severity-driven urgency → a ticketing/issue tracker. Strip the incident record → on-call paging. Strip the restore-service loop and keep only detection → monitoring. Strip the IT-service subject matter and swap in adversary/evidence machinery → cyber incident response. Each removal yields a different Type — the boundary is real.

## Uncertainties

1. **ServiceNow evidence** — the largest enterprise ITSM vendor was not fetched (time budget; historically unreachable from this environment per prior passes). The ITSM pole is evidenced via Atlassian's ITIL-workflow documentation and incident.io's ServiceNow migration/integration pages; claims about the ITSM pole are kept at cross-product/common level, not ServiceNow-specific.
2. **JSM product-level support docs** unreachable (404); Atlassian evidence comes from official practice/hub pages (Tier 1–2). Product-specific state labels for JSM incidents not verified.
3. **State-label universality** — PagerDuty's Triggered/Acknowledged/Resolved is product-specific; the canonical states are written conceptually (open/being-worked/closed classes) with the observation that alerting-rooted products converge on an acknowledgement step while ITSM poles use workflow states. Exact labels vary by product.
4. **Relative frequency of packaging variants** (pure-play vs embedded) is asserted from market familiarity, not quantified — no source in the sample states market share. Kept qualitative.
5. **On-call Management and Status Page Platform leaves are unprocessed**; the boundaries here are one-sided (this side only). Flags recorded in STATUS.md for joint review.

## Final Synthesis

An **Incident Management** application is the on-call operations response system of record. Its world has three load-bearing structures: the **incident of record** (persistent, identified, classified, timestamped), the **managed restore-response loop** (triage → mobilize → work to restoration → resolved disposition), and the **standing mobilization structure** (predefined severity-driven routing to accountable responders, commonly escalation policies over on-call schedules). Around this core, mature products add alert intake and aggregation, coordination surfaces (channels, war rooms, roles, tasks), stakeholder communication (status updates, status pages), service-catalog anchoring, post-incident learning (postmortems, follow-ups), and response analytics. The Type is realized in four packagings — ITSM-embedded, pure-play, observability-embedded, comms-native — which are variants, not separate Types. The word "incident" is shared with security, environmental, and public-safety Types, but the object worlds differ; the sharpest *structural* boundary is with On-call Management (coverage machinery without an incident record) and with Ticketing (generic machinery without emergency semantics).
