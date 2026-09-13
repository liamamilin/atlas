# Research Notes — On-call Management

## Research Goal

Understand what an On-call Management application really is from real products: what its system of record is, how coverage is modeled, how an incoming event becomes a reached-and-acknowledged responder, and where its boundary lies against Incident Management (the pre-hung joint-review flag from the incident-management pass: "sharpest structural seam: coverage machinery (schedules/rotations/overrides, no incident record) vs incident response record; products fuse them… so that pass should fix the seam by unit-of-record"), monitoring/alerting, status pages, and employee scheduling.

## Initial Boundary

Working hypothesis before research:

- Core use: manage *who is on call, when*, and *make sure the right person is reached* when something needs attention.
- Users: on-call engineers/responders, team leads who build rotations, NOC/support tiers.
- Nearest neighbors: Incident Management (fused in most products), Infrastructure/Metrics Monitoring (upstream alert source), Status Page Platform (separate surface), Employee Scheduling Platform (§09 — superficially similar shift machinery), ITSM (umbrella), SRE Management (practice umbrella).
- Unknowns: is the alert/event record part of this Type's core or only a trigger? Is acknowledgment definitional or just common? Is the escalation structure definitional without schedules (static call trees)? How do products behave on coverage gaps?

## Research Questions

1. What is the persistent system of record — schedules? escalation policies? pages/incidents?
2. How is a schedule structured (rotations, layers, handoff, restrictions, time zones, overrides)?
3. How does escalation work (levels, targets, timeouts, fallback, repeat, round robin)?
4. What does "being on call" mean operationally (status determination, handoff, shift notifications)?
5. How do pages/escalations relate to alerts and incidents — what is this Type's unit of record vs Incident Management's?
6. What happens on coverage gaps (no one on call)?
7. What reach channels exist and how are they configured per responder?
8. What is common-but-not-definitional (mobile apps, Slack/ChatOps, HRIS/PTO feeds, coverage policies, quality scores, pay reports, AI)?
9. Would older/regional products (Opsgenie/VictorOps generation; paper rota + phone-tree lineage) still fit the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / position | Customer tier | Evidence tier |
|---|---|---|---|
| PagerDuty | standalone commercial on-call + incident category leader | mid-market → enterprise | Tier 1 (support docs, llms-indexed) |
| Datadog On-Call | observability-suite-embedded on-call (monitoring + paging + incident response in one platform) | enterprise | Tier 1 (product docs) |
| incident.io On-call | comms-platform-native (Slack/Teams) incident platform with on-call module; incident-first philosophy | startups → scale-ups | Tier 1 (help center, 453-page index) |
| Grafana OnCall | OSS-rooted alert routing + escalation inside the Grafana observability stack (OSS in maintenance period; Cloud continues) | self-host → cloud, OSS-leaning teams | Tier 1 (product docs) |

Market context (not sampled, used as existence/lineage evidence only): Opsgenie (Atlassian; discontinued — migration guides into Datadog On-Call, incident.io, and Jira Service Management all document it), Splunk On-Call/VictorOps (sunset generation), Jira Service Management on-call (Opsgenie heritage folded in), Better Stack On Call, Rootly, FireHydrant, xMatters.

## Sources

Fetched 2026-09-09:

- PagerDuty — Escalation Policy Basics: https://support.pagerduty.com/main/docs/escalation-policies
- PagerDuty — Schedule Basics (legacy): https://support.pagerduty.com/main/docs/schedules
- PagerDuty — Shift-Based Schedules (current generation): https://support.pagerduty.com/main/docs/shift-based-schedules
- Datadog — On-Call (overview/concepts): https://docs.datadoghq.com/incident_response/on-call/
- Datadog — On-Call Schedules: https://docs.datadoghq.com/incident_response/on-call/schedules/
- Datadog — On-Call Escalation Policies: https://docs.datadoghq.com/incident_response/on-call/escalation_policies/
- incident.io — Getting started with On-call: https://docs.incident.io/on-call/getting-started
- incident.io — Building schedules: https://docs.incident.io/on-call/building-schedules
- incident.io — Smart escalation paths: https://docs.incident.io/on-call/escalation-paths
- incident.io — Escalation status definitions: https://docs.incident.io/on-call/escalation-statuses
- incident.io — Schedule coverage policies: https://docs.incident.io/on-call/coverage-policies
- incident.io — What determines if you're on call: https://docs.incident.io/on-call/determining-on-call
- incident.io — Help center index (453 pages): https://docs.incident.io/llms.txt
- Grafana OnCall OSS — overview: https://grafana.com/docs/oncall/latest/
- Grafana OnCall OSS — On-call schedules: https://grafana.com/docs/oncall/latest/manage/on-call-schedules/
- Grafana OnCall OSS — Web-based schedules: https://grafana.com/docs/oncall/latest/manage/on-call-schedules/web-schedule/
- Grafana OnCall OSS — Escalation chains and routes: https://grafana.com/docs/oncall/latest/configure/escalation-chains-and-routes/

Failed / abandoned per source-access rules (1–2 attempts each, then abandoned):

- https://docs.datadoghq.com/on_call/ → 404; https://docs.datadoghq.com/service_management/on_call/ → 404 (docs reorganized; /incident_response/on-call/ reachable — used instead)
- https://www.datadoghq.com/products/on-call/ → 404 (product marketing page not reached; docs used)
- https://betterstack.com/docs/on-call/ → 404 (Better Stack abandoned as a sample; not claimed anywhere)
- https://grafana.com/docs/oncall/latest/llms.txt → 404 (index pages used instead)
- https://incident.io/features/on-call → 404 (help center used instead)
- Opsgenie / Splunk On-Call / Jira Service Management product docs not attempted (sunset/known-unreachable per prior passes); used only as market context via migration guides hosted by the sampled products.

## Product A — PagerDuty

### Key observations (evidence layer A unless noted)

**Positioning.** Standalone commercial platform; on-call machinery (schedules, escalation policies) is the mobilization layer that services use to reach responders when incidents trigger.

**Coverage record — two documented generations.**
- *Legacy schedules*: built from **schedule layers**; last-created layer takes precedence; only one user per schedule on call at a time; rotation types daily/weekly/custom with a **handoff time**; **restrictions** limit on-call duty to specific times of day or days of the week (creating **coverage gaps**); layers can be **end-dated** rather than deleted "to preserve historical accuracy"; max 60 layers.
- *Shift-based schedules* (current, rolling out 2026): built from **named rotations**, each defining active days, active times, a handoff, and a **shift assignment type** (rotate through members vs **all members on-call simultaneously**); **custom shifts** (one-off changes) vs **overrides** (manual one-time adjustments such as vacations or shift swaps); **open schedules** with unassigned rotations that members claim; **future-dated** rotation changes with pending-update cards; schedule templates (Weekly Handoff, Workday/Weekend, Follow the Sun).
- Schedules connect to services **only via an escalation policy** — "If you do not add your schedule to an escalation policy, incident notifications will not be sent to users on call on the schedule."
- Calendar export: WebCal (live) and iCal (static) feeds, "my shifts" or "everyone's".

**Escalation machinery.** Escalation policy = ordered **rules (levels)**; targets are **users or schedules**; on trigger, first rule notified immediately; responder has the **escalation timeout** to acknowledge/resolve/reassign; on timeout, next rule notified; continues until someone acknowledges or the final rule is reached; policy can **repeat up to 9 times**; up to 20 rules; multi-user notifications per level (limits vary by plan); **round robin** assignment option; minimum timeout 1 minute (single target) / 3 minutes (multiple targets). "Acknowledging an incident tells PagerDuty that a responder is working on it, which stops the policy from escalating… Acknowledgment does not resolve the incident." An incident follows the escalation policy **snapshot** taken at trigger time; later policy edits don't affect open incidents.

**Coverage-gap behavior (high-value rule).** "If nobody is on-call in the first rule (due to a coverage gap in a schedule, for example), PagerDuty assigns the incident to the next escalation rule with an on-call responder." And: "If no one is on call on the entire escalation policy, **an incident will not be created**" — trigger events are dropped; manual creation errors with "Incident cannot be assigned."

**Reach machinery.** Per-user notification rules (push, phone, Slack, email, SMS per the incident-management pass's observation of the same docs); **on-call handoff notifications** (OCHONs) can notify users up to 48 hours before they go on-call; inactive/deleted users are skipped when the policy runs.

**Organizational binding.** Services bind one escalation policy each; policies/schedules/users/services attach to Teams; role-based permissions gate who can create/edit schedules and policies (User/Manager/Admin/Account Owner; stakeholders excluded from schedules).

## Product B — Datadog On-Call

### Key observations

**Positioning.** "Datadog On-Call integrates monitoring, paging, and incident response into one platform." Suite-embedded: Pages originate from monitors, incidents, security signals, or API calls.

**Concepts (vendor's own list).** **Pages** ("represent something to get alerted for… status of Triggered, Acknowledged, or Resolved"); **Teams** ("the central organizational unit"); **Routing rules** (set urgency, route Pages to different escalation policies by event metadata, **support hours** to delay escalation notifications to defined windows); **Escalation policies** ("determine how Pages are escalated within or across Teams"); **Schedules** ("set timetables for when specific Team members are on-call to respond to Pages").

**Coverage record.** Schedules structured in **layers** (example: JP / EU / US business-hours layers); **Final Schedule** composed of all layers, "lower layers take precedence over higher layers"; layer config: start date/time, **shift length** (one day / one week / custom), **handoff time**, end time, **conditions** (restrict shifts, e.g. Mon–Fri 9–5), **members** (take shifts in the order added). Overrides accommodate "temporary shift adjustments and holidays"; **override requests in Slack/Teams** (`/dd override`) that teammates accept with "Take it". Export via `.webcal` (my shifts / entire schedule). Departed users remain in schedules until manually removed; deactivated accounts stop receiving notifications.

**Escalation machinery.** Policy = ordered **steps**; per step choose targets (**individual users, teams, or whoever is on-call in a schedule**) and method (**Notify All** default vs **Round Robin** — pages distributed across targets in rotating order for load balancing; unacked round-robin pages escalate to the next *step*, not the next person, unless the single step repeats); per-step **acknowledgment window** in minutes; **repeat count** for the whole policy; optional **auto-resolve** after all rules execute. Empty schedules: "the escalation step gracefully skips and the process moves forward"; UI indicates the skip. Limits: max 10 steps, 10 targets per step, 1-minute minimum escalation delay. A default escalation policy is created when a team onboards.

**Governance.** Granular access control per resource: **Viewer / Overrider (schedules only — can create overrides) / Editor** on schedules, escalation policies, and team routing rules. **No deletion** of Pages, escalation policies, or schedules ("to preserve incident history"). Seat-based SKU. Not supported on government sites (ddog-gov) — deployment-scope variant.

**Category existence evidence.** First-party migration guides: "Migrate OpsGenie resources to Datadog On-Call", "Migrate PagerDuty resources to Datadog On-Call", "Migrating from your current on-call provider", plus team import from PagerDuty.

## Product C — incident.io On-call

### Key observations

**Positioning.** "The all-in-one platform for on-call, incident response, Investigations and status pages." On-call is one module; the product is comms-platform-native (Slack/Teams first).

**On-call's own decomposition (vendor's words).** "On-call… consists of three main components: **Alerts** (configure alerts from your observability tools), **Escalations** (route alerts to the appropriate escalation paths, schedules, and team members), **Schedules** (define who is on-call to receive escalations). Once these are set up, we'll page the right people so they can acknowledge the alert and jump into resolving the issue."

**Alerts vs escalations — explicitly separated objects.** "An alert is an event or issue that can trigger an escalation… An escalation will include information about who was paged." Alert statuses: Firing / Resolved only. "You **cannot acknowledge an alert**, only an escalation." Escalation statuses: **Pending, Triggered, Acknowledged, Resolved, Expired** (ran the whole path unacknowledged), **Cancelled** (e.g. attached alert resolved), **Snoozed** (responder-paused), **Delayed** (at a delay node), **Pending repeat** (terminated while alert still firing).

**Coverage record.** Schedules with **rotations** (daily/weekly/monthly), **asymmetric intervals** (e.g. 3- and 4-day shifts, auto-balanced), **advanced rotas** (multiple rotas per schedule, e.g. follow-the-sun US/UK), **shadow schedules** for onboarding, **holidays & PTO** (public-holiday subscriptions per country, iCal calendar feeds, direct HRIS integrations: Workday, HiBob, BambooHR), **overrides** (including `NOBODY` sentinel via API), **Cover me** (`/inc cover me` — request cover, teammates volunteer), **shift swaps**, future-dated changes with preview, **version restore** ("won't change historical shifts"), multi-schedule view (up to 10), **calendar feeds** (Google Calendar/Outlook), **Slack user-group sync** with schedules, Slack notifications for schedule changes. **Schedule coverage policies**: check schedules have someone on call "around the clock (24/7)", look ahead 60 days, flag gaps ("needs cover" banner), evaluate at schedule or rotation level, reminders anchored to gap-identification or gap-start, dismiss with reason (permission-gated).

**Escalation machinery ("smart escalation paths").** Levels with targets (schedules — **currently on-call / next on-call / everyone on schedule / a specific rotation** — individuals, or Slack/Teams channels); **branches** by priority and/or working hours (e.g. high-urgency page out of hours only for P1, low-urgency held until working hours); **per-level retries** (notify every N minutes up to 10 attempts; round-robin levels and channel levels cannot retry); **retry across the path** (restart from an earlier node, re-evaluating conditions); **reassign to another path** (hand unacknowledged escalation to a different path); **delay nodes** (fixed duration or until working hours; alert resolving during delay stops everything); **snoozing**; **repeating acknowledged escalations** while the alert still fires; manual escalation (`/inc escalate`, `/inc page`); manual reassignment; round robin; out-of-hours delays; "wait for investigation" (hold escalation while AI investigates, page with context).

**Being on call — status determination (vendor's own rule).** "We will consider you as on-call if you *can currently receive high urgency notifications for an escalation, before anyone else*." Conditions: you must be on an escalation path (directly or via a schedule — "There is no way to escalate to a schedule" [i.e., schedules are reached through paths]); if via schedule, you must be currently active on it and within its working hours; you must be on the first reachable level configured for high-urgency notifications. API exposes `current_responders` per escalation path and `current_shifts`/`next_shifts` per schedule. Slack status auto-updates while on call.

**Reach machinery.** Per-user notification preferences (mobile push iOS/Android, SMS, voice, WhatsApp, Slack, email), **test your on-call notifications** ("Prove a page will reach you before you get paged for real"), **notification policies** (ensure every responder is set up), bulk acknowledging, supported-countries constraints, dedicated China on-call behavior (SMS/voice/mobile in Mainland China). Responder onboarding: "When responders are added to a schedule or escalation path, they'll automatically receive notifications to set up their on-call configuration."

**Deactivated-responder handling.** Notification to schedule editors when a member is deactivated; "If an escalation reaches a deactivated user, we will automatically escalate to the next escalation level"; the gap is flagged by the coverage policy.

**Migration evidence.** Import schedules and escalation policies from PagerDuty and OpsGenie; migrate from PagerDuty/Opsgenie/Datadog monitors; schedule mirroring *to* PagerDuty.

## Product D — Grafana OnCall

### Key observations

**Positioning.** "Grafana OnCall OSS allows you to automate alert routing and escalation to ensure swift resolution and service reliability." OSS plugin in a **maintenance period** (vendor's own wording, twice); Grafana Cloud continues (label-based routing and the declare-incident step are Cloud-only). OSS-rooted pole of the market.

**Coverage record.** Web-based schedules (rotations with live preview, teammates' time zones, overrides); **iCal import** (manage schedules in any calendar service; imported as read-only schedules); **Terraform** management (as-code, read-only in UI); **shift swap requests** (teammates volunteer to take affected shifts). Schedule view: three interactive weekly calendars — **Final schedule** (combined rotations + overrides), **Rotations**, **Overrides** ("any events on this calendar will take precedence over the rotations calendar"); 24-hour on-call status bar. **Schedule quality report**: 0–100 score from **gaps** (time with no one on-call) and **balance** (uneven distribution), with "29% not covered"-style gap percentages and overloaded-user flags, over a 52-week horizon. Schedule settings: Slack channel for shift notifications, Slack user group receiving current on-call updates, notification frequency, **action for slot when no one is on-call** (gap behavior), current/next shift notifications. iCal export.

**Escalation machinery.** **Routes** (per integration; Jinja2 routing templates; first matching route wins; publish to ChatOps) select an **escalation chain**; chains = ordered **steps**: Wait, Notify users, **Notify users from on-call schedule**, Notify all team members, Resolve incident automatically, Notify Slack channel members / user group, Trigger outgoing webhook, **Round robin notifications**, **Time-based escalation** (only within a time range), **Threshold-based escalation** (only if N alerts in a window), **Repeat escalation** (loop up to 5 times), **Declare incident** (Cloud only). "The chain continues until a user intervenes by acknowledging, resolving, or silencing the alert." Per-user **notification policies** with two sets: Default and Important (high-priority), selectable per step.

**Permissions.** Admin/Editor manage schedules; Viewer "cannot receive alert notifications, therefore, cannot be on-call" — role gates on-call participation itself.

## Cross-product Comparison

| Dimension | PagerDuty | Datadog On-Call | incident.io | Grafana OnCall |
|---|---|---|---|---|
| Coverage record | schedules (legacy layers / shift-based rotations) | schedules (layers → final schedule) | schedules (rotas + intervals + shadow) | schedules (rotations + overrides; iCal/Terraform import) |
| Schedule anatomy | handoff time, rotation type, restrictions, time zone | shift length, handoff time, conditions, members order | handover times, active hours, intervals, working hours | rotation active days/times, time zones, overrides |
| Escalation structure | escalation policy (rules/levels) | escalation policy (steps) | escalation path (levels + branches) | escalation chain (steps) |
| Level targets | users, schedules | users, teams, schedules | schedules (current/next/everyone/rotation), individuals, channels | users, schedules, teams, Slack groups/channels |
| Ack semantics | ack stops escalation; ack ≠ resolve | Page: Triggered/Acknowledged/Resolved | ack stops auto-escalation; 9 escalation statuses | chain continues until ack/resolve/silence |
| Fallback trigger | escalation timeout per level | ack window per step | time-to-ack per level + retries | wait steps |
| Repeat | policy repeat ×9 | policy repeat count | per-level retries + path retry + repeat-while-firing | chain repeat ×5 |
| Round robin | assignment option | step method | level option | step type |
| Overrides/swaps | overrides, custom shifts, open schedules | overrides + Slack/Teams override requests | overrides, cover me, shift swaps | overrides, shift swap requests |
| Gap behavior | skip level; **no one on call → no incident created** | skip step gracefully | coverage policies flag gaps; deactivated user → next level | gap action setting; quality report |
| Reach channels | push/phone/SMS/email/Slack | email/SMS/phone/mobile push | push/SMS/voice/WhatsApp/Slack/email | SMS/phone/mobile/ChatOps/email |
| Handoff | OCHONs up to 48h before | handover automation | schedule-change Slack notifications; calendar feeds | shift start/next notifications |
| Calendar | WebCal/iCal export | webcal export | calendar feeds (in/out) | iCal import + export |
| Trigger intake | services + integrations + Event Orchestration | monitors/incidents/signals/API → team routing rules | alert sources + alert routes (dynamic via catalog) | integrations + routes (Jinja2) |
| Incident record | fused (page = incident) | Pages promotable to incidents | alerts → escalations → incidents (distinct objects) | declare-incident step (Cloud only); OSS core pages without incidents |
| Org binding | service → escalation policy; Teams | team owns policies/schedules/rules | teams/catalog → escalation paths | team assigned to chains/schedules |
| History posture | end-date layers; snapshot at trigger | no deletion of resources | version restore; historical shifts preserved | quality report over future 52 weeks |
| Admin surface | roles gate schedule/policy editing | Viewer/Overrider/Editor per resource | policies/permissions; responder setup nudges | role gates on-call participation |

**Layer-B findings (cross-product commonality, evidence layer B):**

1. Every product holds a persistent **schedule** as the coverage record, structured as repeating **rotations/layers** with **handoff** moments, **active windows** (restrictions/conditions/working hours), **time zones**, and **overrides** on top.
2. Every product holds an ordered **escalation structure** (policy/path/chain) whose levels target **whoever is currently on call on a schedule** and/or fixed users/teams, with a **time-bounded acknowledgment window** per level, **fallback to the next level** on non-acknowledgment, and a bounded **repeat**.
3. Every product implements **acknowledge** as the act that stops escalation; acknowledgment is distinct from resolution.
4. Every product delivers pages through **multiple contact channels** configured per responder (push/SMS/voice/email plus chat), with per-user notification rules/preferences and a way to **test** them (test notifications documented at incident.io; shift/handoff notifications at all four).
5. Every product surfaces **who is on call right now / next** (schedules list, on-call status bars, `current_responders`/`current_shifts` APIs, Slack user-group sync).
6. Every product handles **coverage gaps**: skip the empty level (PagerDuty, Datadog), flag gaps ahead of time (incident.io coverage policies, Grafana quality report), and define behavior when nobody is on call at all (PagerDuty drops the event; Grafana has a configurable "action for slot when no one is on-call").
7. Every product supports **ad-hoc coverage adjustment**: overrides, and (where documented) shift swaps / cover requests, with chat-mediated request flows in three of four.
8. Every product binds schedules and escalation structures to an **owning container** (team and/or service).
9. Every product consumes **upstream alert events** from monitoring/error-tracking sources through routing rules; the alert pipeline (dedup, grouping, enrichment) exists in all four but with different depth and ownership.
10. Every product keeps **history**: end-dated layers, no-deletion, version restore, snapshots.

**Layer-C canonical inference:** the Type is the *coverage-and-mobilization machinery* of operations: a persistent answer to "who is responsible right now, and how do we reach them", plus the machinery that turns a need-attention event into a reached, acknowledging responder. The page/escalation is the routing act; the incident is (in fused products) the response record that may grow out of it.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The on-call schedule as the coverage record** — a persistent, time-based rotation binding an owning unit (team/service) to specific responders: who is responsible, when. Editable, with ad-hoc adjustments (overrides). *Remove → an alert-routing/notification tool with no coverage model.*
2. **The escalation path as the consequence machinery** — ordered levels evaluated against an incoming need-attention event: notify the current coverage, wait an acknowledgment window, fall back to the next level, repeat a bounded number of times. *Remove → a rota display with no operational consequence.*
3. **The reach-and-acknowledge loop** — pages delivered to the responsible person through contact channels, with explicit acknowledgment that stops escalation and takes responsibility. *Remove → a passive schedule plus a notification log that nobody is required to answer.*

Jointly-held load-bearing tests:

- 1 alone = shift planner / rota tool
- 2 without 1 = static call tree (fixed recipients, no rotation)
- 3 without 1+2 = broadcast notification sender
- 1+2 without 3 = paper escalation policy nobody receives
- 1+3 without 2 = paging the rota with no fallback
- 2+3 without 1 = fixed-recipient paging

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Multi-channel reach breadth (push/SMS/voice/email/chat) and per-user notification rules with urgency tiers
- Mobile responder app (receive, ack, snooze, swap)
- Handoff notifications before shifts; shift-start/next-shift notifications
- Calendar subscribe/export feeds (personal and whole-schedule)
- "Who is on call now / next" surfaces and APIs; Slack user-group sync
- Coverage assurance: gap detection/policies, schedule quality scores, balance metrics
- Round-robin and load-balancing options
- Alert intake pipeline: sources/integrations, routing rules, dedup/grouping, maintenance windows, heartbeats
- Admin/permission models over schedules and policies; audit/history preservation
- Migration tooling between products (category maturity marker)
- ChatOps surfaces (Slack/Teams commands for overrides, escalation, ack)

### L2 — Variant / Optional Structure

- Packaging: standalone (PagerDuty) vs observability-suite-embedded (Datadog) vs incident-platform module (incident.io) vs OSS/self-hosted (Grafana) vs ITSM-embedded (JSM/Opsgenie heritage)
- Escalation intelligence: priority/working-hours branches, delay nodes, reassignment chains, AI-held escalations (single-product today)
- Coverage assurance depth: 24/7 coverage policies with reminders and dismissal (single-product depth), quality scores (single-product)
- HRIS/PTO integration for schedule awareness (Workday/HiBob/BambooHR — single-vendor depth)
- On-call pay reporting, readiness insights (single-product)
- Regional constraints: supported-country lists for SMS/voice, China-specific notification behavior
- Deployment scope: government-cloud exclusion (Datadog ddog-gov), OSS maintenance posture (Grafana)
- Schedule authoring medium: in-product builder vs external calendar (iCal) vs Terraform as-code

### L3 — Vendor-specific (research notes only)

- PagerDuty: legacy-vs-shift-based schedule generations; 60-layer / 20-rule / ×9-repeat limits; OCHONs 48h; "Default Mobilization EP"; Live Call Routing; escalation-policy snapshot semantics; plan-tier limits (Free = 1 schedule/1 policy)
- Datadog: Pages concept; team routing rules with support hours; Viewer/Overrider/Editor resource permissions; no-deletion posture; seat-based SKU; ddog-gov exclusion; 10-step/10-target/1-minute limits; `/dd override`
- incident.io: alerts-vs-escalations object separation with 9 escalation statuses; `NOBODY` override sentinel; catalog-driven dynamic escalation; "wait for investigation" AI hold; pay reports; readiness insights; China pages; `/inc cover`, `/inc escalate`, `/inc page`
- Grafana: Jinja2 routing templates; threshold-based and time-based escalation steps; quality score 0–100 with 52-week horizon; iCal/Terraform read-only schedules; Cloud-only label routing and declare-incident step; Viewer role cannot be on-call

## Historical / Market-Sample Check

- **Older generation (2000s–2010s):** Opsgenie-class and VictorOps-class paging/escalation tools — schedules + escalation policies + SMS/voice/push paging with ack. All three L0 legs present; no Slack-native surfaces, no HRIS feeds, no AI, no coverage policies. Fits.
- **Conceptual lineage (pre-software):** NOC pager rota (who is on call tonight) + phone/pager escalation tree (if primary doesn't answer, call secondary) + pager/phone acknowledgment. All three legs present in paper form. Fits at concept level.
- **Within-product generations:** PagerDuty's own legacy-layer vs shift-based-rotation schedules are two structural generations of the same coverage record; both satisfy L0.
- **Regional/deployment poles:** Grafana OSS self-hosted (no SaaS, no mobile push of its own — relies on configured channels) satisfies L0; incident.io's China-constrained notification behavior is a regional variant, not a structural difference.
- **Conclusion:** the L0 contains no era machinery — no mobile app, no chat platform, no SaaS, no AI, no HRIS, no cloud. The definition survives the historical check.

## Vendor-specific Findings

See L3 above. The most consequential for boundary work: **PagerDuty drops the trigger event when nobody is on call** ("an incident will not be created") — coverage is a hard precondition of mobilization in the purest form; and **incident.io's explicit alerts-vs-escalations separation** ("You cannot acknowledge an alert, only an escalation") — the cleanest vendor articulation of the trigger-vs-routing-act distinction this Type depends on.

## Boundary Findings

**vs Incident Management (§14, processed 2026-09-08 — pre-hung joint-review flag DISCHARGED here).** Unit-of-record test, ratified from this side exactly as that pass proposed:
- On-call Management's system of record = the **coverage estate**: schedules, rotations, overrides, escalation policies (plus the escalation/page as the routing act with its own lifecycle).
- Incident Management's system of record = the **incident**: the response record (declare → respond → resolve, timeline, roles, postmortems).
- Products fuse them — PagerDuty's page *is* an incident; Datadog promotes Pages to incidents; incident.io chains alerts → escalations → incidents as distinct objects; Grafana Cloud has a declare-incident step.
- Natural experiment: **Grafana OnCall OSS pages people through escalation chains with no incident record in the OSS core** (declare-incident is a Cloud-only step) and remains recognizably On-call Management. Remove the coverage machinery and what remains is incident management (manual responder assembly, no schedules). Keep-both; seam fixed by unit-of-record.
- Interlock: an alert/event triggers the escalation; when responders convene, an incident record may be opened (in fused products the page object doubles as the incident).

**vs Status Page Platform (§14, unprocessed — corroborates the incident pass's flag).** Internal coverage/response machinery vs stakeholder-facing publication surface. All four sampled products treat status pages as a separate surface (Datadog: separate Status Pages product with its own docs section; incident.io: separate status-pages help section with its own object set; PagerDuty/Grafana: integrations). No boundary failure.

**vs Infrastructure Monitoring / Metrics Monitoring / APM / Log Management (§14, processed).** Detection vs reachability. Monitoring evaluates conditions and emits alerts; it holds no coverage model and no escalation-to-humans. On-call consumes alert events as triggers; it holds no signal-evaluation model. The alert pipeline (dedup/grouping/enrichment) is shared machinery in fused products (Datadog monitors → Pages; incident.io alert sources; Grafana integrations) — capability absorption, not Type merger. Consistent with the incident pass's "alert handoff" seam.

**vs AIOps Platform (§14, processed).** AIOps = machine-executed analysis over the signal stream (correlation, noise reduction) upstream; on-call = human responsibility routing downstream. Consistent with the incident pass's reading.

**vs Employee Scheduling Platform (§09, processed 2026-09-06).** Sharpest cross-domain seam because the surface vocabulary overlaps (rotations, shifts, swaps, open shifts, calendar feeds). That pass's L0: schedulable employee roster + time-organized shift schedule + assignment binding + publication of when employees work. The distinction: an employee-scheduling shift obliges *working* at a time/place (labor coverage for operations); an on-call shift obliges *being reachable* for pages (standby responsibility), and only on-call carries the escalation/ack consequence machinery. Remove escalation+ack → employee scheduling territory; remove labor-publication semantics → on-call. Keep-both.

**vs Agent Scheduling Platform (§07, processed).** Contact-center interval scheduling derived from forecast demand — labor scheduling for a shift workplace, same seam as employee scheduling. No escalation/ack machinery.

**vs IT Service Management (§14, processed 2026-09-08).** ITSM = the IT organization's service-management system of record (umbrella of practices); on-call = one operational practice's machinery. The Opsgenie heritage folded into Jira Service Management is packaging evidence that the machinery exists inside suites without merging Types. Consistent with the incident pass's expectation.

**vs SRE Management (§14, unprocessed — forward flag).** SRE Management is expected to be the practice-level Type (SLOs, error budgets, toil, production excellence); on-call is one practice's machinery inside it. Joint review expected on that side.

**vs Ticketing System / Help Desk (processed).** Tickets are demand-processing work items assigned to queues/people during working processes; pages are responsibility routing to whoever is on call now, with escalation and ack. Different unit of record and different urgency semantics.

**vs Error Tracking Platform (§12, unprocessed).** Error aggregation is detection; error spikes feed alert sources that trigger escalations (incident.io documents Sentry as an alert source). Upstream signal source, not this Type.

**"Remove what to become the neighbor" summary:**
- Remove the incident/response record → still On-call Management (Grafana OSS pole proves it).
- Remove the coverage machinery (schedules/rotations/overrides) → alert routing/notification tool or incident management.
- Remove escalation+ack → employee/shift scheduling or a rota display.
- Remove the human-reach loop → monitoring/alerting evaluation.

## Uncertainties

1. **Datadog On-Call reach-channel detail** — notification preferences page not fetched (time budget); channel list (email/SMS/phone/mobile) taken from the docs index description and overview; per-channel behavior not verified.
2. **Opsgenie/VictorOps structure** — not directly documented (sunset products; docs not attempted per access rules); the "older generation satisfies L0" claim rests on migration-guide existence evidence plus the incident pass's category evidence, held at lineage strength.
3. **Jira Service Management on-call** — product support pages were 404 in the incident pass and were not retried here; the ITSM-embedded pole is evidenced via Atlassian practice pages (that pass) and migration guides, not JSM product docs.
4. **Non-software-industry on-call** — all four sampled products center software/technical operations. Whether dedicated on-call machinery for non-IT operations (utilities, healthcare IT, facilities) constitutes the same Type or a variant is unverified; the L0 as written should fit them, but no direct evidence was collected.
5. **On-call compensation/compliance depth** (pay reports, union/regulated contexts) — single-product evidence (incident.io pay report); held as optional variant.
6. **Market-size claims** — none made; no pricing/market-share assertions beyond seat-based SKU observations.

## Final Synthesis

On-call Management is the coverage-and-mobilization machinery of operations. Its defining core is exactly three jointly-held structures: the **on-call schedule** (persistent time-based rotation binding a team/service to specific responders, editable with overrides), the **escalation path** (ordered levels that turn an incoming need-attention event into time-bounded notification attempts against current coverage, falling back level by level until someone acknowledges, with bounded repeats), and the **reach-and-acknowledge loop** (multi-channel page delivery with explicit acknowledgment that stops escalation and takes responsibility). The incident record is deliberately outside the core — it belongs to Incident Management; the alert pipeline belongs upstream to monitoring; the stakeholder publication belongs to Status Pages; labor-shift scheduling without escalation/ack belongs to Employee Scheduling. Everything else modern products carry — channel breadth, mobile apps, ChatOps, HRIS feeds, coverage policies, quality scores, pay reports, AI — is standard capability or variant, not definition.
