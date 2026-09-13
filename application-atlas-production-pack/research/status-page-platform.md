# Research Notes — Status Page Platform

## Research Goal

Understand what a Status Page Platform really is from real products: what objects exist inside it (components, incidents, maintenance, subscribers), what workflow operators follow during an outage, what the published page presents, and where the Type's boundary sits against Incident Management, monitoring Types, and ITSM.

This pass also **discharges a joint-review flag** left by the incident-management pass (2026-09-08, corroborated by on-call-management 2026-09-09): "internal response record vs stakeholder-facing publication surface; all four sampled products treat status pages as a separate surface (native module or integration)".

## Initial Boundary

Initial hypothesis before research:

- Core use: communicate service health (outages, degraded performance, scheduled maintenance) to people who *depend on* the service but do not operate it — customers, end users, internal stakeholders.
- Primary users: the service operator's support/comms/engineering staff; consumers are stakeholders who merely read the page.
- Nearest neighbors: Incident Management (same word "incident", different object role), monitoring Types (Synthetic/Infrastructure/Metrics Monitoring — detection vs communication), On-call Management (mobilization vs publication), ITSM (internal service desk vs external communication), Blog/CMS (structured records vs free-form posts).
- Suspected boundary: the status page is a *publication* surface over a *service-health model*; it is not the response record and not the detection machinery.

## Research Questions

1. What is the unit of record — what does the operator create and maintain?
2. What is the "component" model and what statuses do components carry?
3. What is an incident on a status page — how does it differ from an incident-management incident?
4. How does scheduled maintenance work as a second event type?
5. Who consumes the page, and how do subscriptions/notifications work?
6. How do status pages get their data — manual entry, monitoring integrations, native monitors, API?
7. What page variants exist (public / private / audience-specific)?
8. What does the page display besides current status (history, metrics, third-party components)?
9. Where exactly is the seam vs Incident Management, and vs monitoring Types?
10. Would older / self-hosted / non-SaaS products still fit the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Why sampled |
|---|---|---|
| Statuspage (Atlassian) | pure-play communication tool, no native monitoring; enterprise tier | category-defining product; richest official docs |
| Instatus | modern challenger; bundles monitoring + incident response + status pages; startup/SMB tier | different philosophy (speed, design); full help center |
| Status.io | independent dedicated player since 2013; enterprise compliance flavor | long-running independent; feature-complete marketing surface |
| Better Stack | monitoring-first suite (uptime monitoring + incident management + status page) | the "status page grows out of monitors" philosophy |
| Cachet | open-source, self-hosted status page system | self-hosted / non-SaaS pole for the historical check |

## Sources

Fetched 2026-09-09:

- Statuspage (Atlassian Support, Tier 1):
  - https://support.atlassian.com/statuspage/ (support root)
  - https://support.atlassian.com/statuspage/resources/ (documentation index)
  - https://support.atlassian.com/statuspage/docs/what-is-statuspage/
  - https://support.atlassian.com/statuspage/docs/what-is-an-incident/
  - https://support.atlassian.com/statuspage/docs/what-is-a-component/
  - https://support.atlassian.com/statuspage/docs/top-level-status-and-incident-impact-calculations/
  - https://support.atlassian.com/statuspage/docs/what-are-audience-specific-pages/
- Instatus (help center, Tier 1):
  - https://help.instatus.com/ (get started)
  - https://help.instatus.com/help/status-page/components
  - https://help.instatus.com/help/status-page/public-page
  - https://help.instatus.com/help/incident-response/incidents
- Status.io (product site, Tier 2 — docs.status.io unreachable, see Limitations):
  - https://status.io/ (features + plans)
- Better Stack (docs, Tier 1):
  - https://betterstack.com/docs/uptime/status-pages/ (Get started with status pages)
- Cachet (GitHub README, Tier 1 for OSS identity):
  - https://github.com/CachetHQ/Cachet

### Source-access Limitations

- `docs.status.io` returned a transport error and was not retried beyond one alternate attempt; Status.io evidence is therefore at product-page (Tier 2) level. Operational details for Status.io (exact incident state vocabulary, notification trigger semantics) are **not** asserted.
- `docs.cachethq.io` returned 404; Cachet evidence is limited to its official GitHub README (identity: "the open source self-hosted status page system"). No detailed Cachet feature claims are made.
- Better Stack's subscription/subscriber machinery was not directly observed in the fetched page; not claimed.
- No model-memory filling for any of the above.

## Product A — Statuspage (Atlassian)

### Key observations (Layer A unless noted)

- Self-definition: "Statuspage is a communication tool that helps you inform your users about outages and scheduled maintenance." Users "can subscribe to updates via email or text messages"; status can be embedded "directly into other interfaces and web properties".
- **Explicit non-monitoring**: "Statuspage does not do any direct monitoring of your websites or servers, but you can integrate monitoring tools with Statuspage, or use our API to programmatically update your page." — the pure-play pole.
- Structure: account → page(s). "Multiple pages can be managed from a single account… Pages are autonomous and they have separate billing subscriptions." A page "can be public or private. A public page is viewable by anyone with an internet connection. A private page is viewable by only those who have access to login and view the page."
- People: account owner (1), team members (full manage access), **subscribers** ("typically your customers, end-users, or employees… who subscribe to receive notifications from your page when you publish incidents"), **employees** (private-page viewers who log in; "not automatically subscribed").
- **Incidents**: "the main way to communicate with your customers when you are having downtime… you can add an incident to your page describing the issue, what you're doing about it, and when you expect the issue to be fixed." Incident statuses: **Investigating / Identified / Monitoring / Resolved**. Updates can trigger subscriber notifications. Backfilling past incidents supported. Incident History link appears to page viewers after the page has been operational (14 days — vendor detail, L3).
- **Components**: "the individual parts of your infrastructure that your users depend on; the functioning pieces or features of your application or service." Component statuses: **Operational / Under Maintenance / Degraded Performance / Partial Outage / Major Outage**. Component status "can be updated during the incident creation process or independently without an incident." Component groups exist. Historical uptime display per component. Third-party components (status of external dependencies). Component limit 1100 (L3).
- **Top-level status**: computed automatically from component statuses ("All Systems Operational", "Partial System Outage", etc.) with a documented decision-tree; pages with 0 components default to All Systems Operational unless an active incident exists.
- **Incident impact**: computed from affected components (None / Minor / Major / Critical / Maintenance), manually overridable.
- **Maintenance**: "Schedule maintenance" is a first-class flow alongside incidents.
- **Subscriptions/notifications**: email + SMS (+ webhooks, Slack subscriptions, component-level subscriptions); CSV import/export; quarantined subscribers; notification event triggers; custom email domain via SPF/DKIM.
- **System metrics**: "real-time and historical data such as response time and uptime", pushed from metrics integrations (Pingdom, New Relic, Datadog, Librato) or API.
- **Automation/integrations**: email automation, alert parsing from Pingdom/New Relic, PagerDuty, Opsgenie, xMatters, VictorOps, Jira/JSM, Zendesk, Slack, Teams; Twitter/X cross-posting; public REST API; "Status embed" widgets for other pages.
- **Audience-specific pages** (formerly "access control"): page type with pre-specified users/groups, per-group viewing and subscription permissions, component-level visibility; SAML for private/audience pages; IP allowlisting.
- Postmortems: "Create a postmortem" is a documented flow (published artifact).
- Incident templates + template library + template groups.

## Product B — Instatus

### Key observations (Layer A)

- Self-definition: "Instatus helps you monitor your services, fix incidents with your team, and share your status with customers." Three pillars: **Monitoring** (website/API/cron/ping/TCP-UDP/DNS monitors + alerts), **Incident response** (incidents, maintenance, templates, general notices, on-call, escalation policies, routing rules, Slack), **Status pages**.
- Status page section: public page, private page, select-audience, components, third-party components, customize, multi-language, widgets, custom domain, subscribers, metrics, notifications (email, SMS, webhook, X, Slack, Microsoft Teams, Discord, Google Chat, RSS & Atom, API).
- **Components**: "the building blocks of your service. These might be parts like your website, mobile app or API." Add/edit (name, status, group, historical-uptime display), archive/restore (archived component hidden "unless it's affected by an active incident or maintenance or its status is not operational"), groups, re-ordering, third-party components (e.g., AWS, Stripe).
- **Incidents**: created with title, description, **affected components**, start time (past allowed), status among **Investigating / Identified / Monitoring / Resolved**, and a **publish-to-status-page checkbox** — the incident exists in the response tooling and *publication is a separate act*. Incident **updates** change status/description/components/date and "optionally notify users". **Postmortem**: markdown document, dated after the last update, optionally notifies subscribers, "appears on your status page as the final entry in the incident's timeline"; can be added from Slack.
- **Maintenance**: separate object with maintenance updates (API objects list both).
- **General notices**: a third publication type distinct from incidents/maintenance.
- Public page: "one page for your customers to check your current status, and subscribe to updates"; public by default; branding/custom domain/multi-language.
- API objects confirm the model: monitors, incidents, incident updates, status pages, workspaces, components, teammates, maintenances, maintenance updates, templates, general notices, subscribers, metrics, outages, public data, private pages, audience groups, routing rules, escalation policies, on-call schedules.
- Integrations ingest from external monitors (Datadog, Grafana, PagerDuty, Pingdom, Prometheus, Uptime Robot, …) and metrics sources.

## Product C — Status.io

### Key observations (Layer A on product page; Tier 2 — see limitations)

- Self-definition: "Status Pages & Incident Communications. Keep users informed during outages and maintenance with real-time updates." "Provide the ultimate source of truth for your system's status."
- **Incidents and Maintenance**: "incidents that trigger notifications and update component statuses automatically. Plan maintenance in advance, with reminders sent to subscribers before it begins. Review past events on the status history page."
- **Notifications**: "unlimited status notifications… via Email, SMS, Webhook, RSS, iCalendar, IRC, Microsoft Teams, Slack, Twitter/X and more." Component subscriptions (subscribers choose components).
- **Metrics**: live charts from Custom Metric API or external sources (New Relic, Pingdom); 90-day historical uptime charts per component.
- **Containers**: "flexible elements that can function as sub-components or represent locations or services, with the ability to be linked to multiple components."
- **Status automation**: "Link monitoring tools to automatically toggle the status."
- **Private status pages**: SSO via OIDC/SAML (OneLogin, Auth0, Okta, Azure, Google); IP access control.
- External service monitoring (display health of external services), location map, stats widget, calendar feed (iCalendar), status badges for embedding, custom domain + TLS, white-label, custom CSS/HTML/JS, audit trail, subscriber compliance tools.
- Plans include "One Public Status Page" — a single-page pole; multi-page is not universal in the market.
- Operating since 2013 (copyright range).

## Product D — Better Stack

### Key observations (Layer A)

- Definition: "A status page is a dedicated page that lets you inform your users about current outages and scheduled maintenance on your services. The main purpose of a status page is to allow users to check if a given service is operational without the need to contact customer support directly."
- Internal variant: "For company employees, an internal status page provides the same benefit" (developer teams save time answering other departments).
- Public vs private: password protection restricts the page "to only allow chosen people to access it… for your internal stakeholders, specific clients, or customers."
- **Monitoring-first construction**: "Before starting with the status page, it's best to set up the monitors for the services whose status you want to communicate." The page's **Structure** tab is populated by adding **monitors and heartbeats** as "displayed components", grouped into sections, with editable public names, explanations, and widget types.
- Subdomain (status.yourdomain.com convention discussed) or custom subdomain; personalization (logo, website URL).
- Embedding announcements into your site; incident communication templates.
- Better Stack platform context: uptime monitoring, incident management & on-call, status page, logs, infrastructure monitoring, error tracking, RUM, AI SRE — the status page is one surface of an operations suite.

## Product E — Cachet

### Key observations (Layer A, limited to README)

- Official identity: "Cachet, the open source self-hosted status page system." (GitHub topics: status-page, self-hosted.)
- Self-hosted PHP application (PHP 8.3+, MariaDB/MySQL/PostgreSQL/SQLite) — proves the Type exists **without SaaS delivery**, operated on the customer's own infrastructure.
- Detailed feature set not verified (docs site unreachable); no further claims made.

## Cross-product Comparison

| Structure | Statuspage | Instatus | Status.io | Better Stack | Cachet | Strength |
|---|---|---|---|---|---|---|
| Component inventory with per-component health status | ✓ (5 statuses) | ✓ (status editable, groups, archive) | ✓ (+ containers as sub-components) | ✓ (components = displayed monitors/heartbeats) | identity-level (status page system) | Universal (A, 5/5) |
| Severity-ordered component status scale (healthy → degraded → partial → major) | ✓ documented | ✓ (status field) | ✓ implied ("update component statuses") | ✓ (monitor states drive page) | unverified | Strong (A, 3–4/5 direct) |
| Incident as dated report with lifecycle states + accumulating updates | ✓ (Investigating/Identified/Monitoring/Resolved) | ✓ (same 4 states) | ✓ (incident management + status history) | ✓ (incidents feed page) | unverified | Strong (A, 2/5 exact vocabulary + 2 more structural) |
| Incidents bound to affected components | ✓ | ✓ (affected-components selection) | ✓ (incidents update component statuses) | ✓ (monitors→components) | unverified | Strong (A, 4/5) |
| Scheduled maintenance as distinct event type | ✓ | ✓ (+ maintenance updates) | ✓ (planned maintenance + reminders) | ✓ (in definition) | unverified | Strong (A, 4/5) |
| Published stakeholder-facing page (public by default) | ✓ | ✓ (public by default) | ✓ ("one public status page") | ✓ | ✓ (self-hosted) | Universal (A, 5/5) |
| Private / restricted-audience pages | ✓ (private + audience-specific + SAML + IP allowlist) | ✓ (private + select-audience) | ✓ (SSO OIDC/SAML + IP control) | ✓ (password protection) | unverified | Strong (A, 4/5) |
| Subscriber notifications (email/SMS/webhook/chat/RSS) | ✓ | ✓ (10 channels) | ✓ (8+ channels) | not directly observed | unverified | Strong (A, 3/5) |
| Component-level subscriptions | ✓ | ✓ (via components) | ✓ | unverified | unverified | Common (A, 3/5) |
| Uptime/metrics display (history bars, response time) | ✓ (system metrics) | ✓ (metrics + historical uptime) | ✓ (90-day charts + metric sources) | ✓ (monitors feed page) | unverified | Strong (A, 4/5) |
| Third-party / external dependency components | ✓ | ✓ | ✓ (external service monitoring) | unverified | unverified | Common (A, 3/5) |
| Automation from monitoring tools | ✓ (alert parsing, email automation, API) | ✓ (native monitors + integrations) | ✓ (status automation) | ✓ (native monitors) | unverified | Strong (A, 4/5) |
| Native monitoring built in | ✗ (explicitly none) | ✓ | ✗ (link external tools) | ✓ | unverified | **Variant axis** |
| On-call / escalation bundled | ✗ | ✓ | ✗ | ✓ (in suite) | unverified | Optional |
| Incident templates | ✓ | ✓ | ✓ | ✓ (community templates) | unverified | Common (A, 4/5) |
| Postmortem as published artifact | ✓ | ✓ | unobserved | unobserved | unverified | Common (A, 2/5) |
| Embeds / badges / widgets | ✓ (Status embed) | ✓ (widgets) | ✓ (badges) | ✓ (announcements embed) | unverified | Common (A, 4/5) |
| Multiple pages per organization | ✓ (autonomous pages) | ✓ (workspaces/projects) | ✗ (one public page per plan) | unobserved | unverified | **Variant axis** |
| Cross-posting to social (Twitter/X) | ✓ | ✓ (X notifications) | ✓ | unobserved | unverified | Common (A, 3/5) |
| Audit trail / compliance tooling | activity log | activity log | ✓ (audit trail, subscriber compliance) | unobserved | unverified | Optional (enterprise) |
| SaaS-hosted vs self-hosted | SaaS | SaaS | SaaS | SaaS | **self-hosted** | **Variant axis** |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a Status Page Platform:

1. **The service-health model of the operator's own estate** — the operator's services held as a persistent, named component inventory (groupable, orderable), each component carrying a current health status on a severity-ordered scale (healthy → degraded → partial outage → major outage, with a maintenance state), from which the page's top-level status derives. This is the "what is affected" structure and the page's subject matter. Remove → an incident blog/changelog with no service model, or a monitoring dashboard with no published service model.
2. **The incident report as the unit of record** — persistent, dated, narrative reports of service disruptions bound to the affected components, advanced through lifecycle states (investigating → identified → monitoring → resolved vocabulary common) by accumulating timestamped updates, plus the scheduled-maintenance sibling event type in mature products. This is the "what happened and what we're doing about it" record. Remove → a bare status board / uptime dashboard with no event record.
3. **The published stakeholder-facing page** — the platform operates a standalone web page presenting current component status, active incidents/maintenance, and past history, consumable by people outside the operating team (public, or access-restricted for private/audience variants) without an operational seat in the response tooling. This is the "communication surface" structure. Remove → an internal incident log = Incident Management territory.

Jointly-held load-bearing:

- 1 alone = component list / uptime dashboard (monitoring territory)
- 2 without 1 = an outage blog / changelog
- 3 without 1+2 = a static "we're healthy" page with no record machinery
- 1+2 without 3 = internal incident log (Incident Management territory)
- 1+3 without 2 = status board with no event record
- 2+3 without 1 = outage blog with a homepage

### L1 — Common Mature Structure

Very common in mature products, not definitional:

- subscriber notifications (email, SMS, webhook, RSS/Atom, Slack/Teams/Discord/Google Chat/X; component-level subscriptions; CSV import/export)
- top-level status auto-computation from component statuses ("All Systems Operational" banner)
- scheduled maintenance as a first-class event type with advance reminders
- historical uptime display / system metrics (uptime bars, response-time charts) fed from native or external sources
- incident templates (and template libraries)
- third-party/external dependency components (status of providers like AWS/Stripe shown on the page)
- embeds/badges/widgets for other web properties
- incident history on the page
- cross-posting to social channels (Twitter/X)
- automation: alert parsing from monitoring tools, email automation, public REST API for programmatic updates
- postmortems as published artifacts (2/5 sampled explicitly)

### L2 — Variant / Optional Structure

Depends on segment, deployment, scale, security posture:

- delivery substrate: SaaS-hosted (dominant) vs self-hosted open source (Cachet)
- scope posture: pure-play communication (Statuspage — explicitly no monitoring) vs monitoring-bundled (Better Stack, Instatus) vs module of an incident-management/ITSM suite (per the incident-management pass: PagerDuty, Datadog, incident.io, Grafana all ship status pages as separate surfaces)
- audience model: public / private (password, login) / audience-specific (per-group permissions, SAML, IP allowlisting)
- single page vs multiple autonomous pages per organization (Statuspage multi-page vs Status.io one-public-page pole)
- bundled incident-response machinery (on-call schedules, escalation policies, routing rules — Instatus; suite context — Better Stack)
- enterprise compliance surfaces: audit trail, subscriber compliance tools, custom TLS/headers (Status.io)
- multi-language pages, general notices (non-incident publications), location maps, calendar feeds, stats widgets
- hosting separation: page hosted on independent infrastructure so it survives the customer's own outage (SaaS marketing point) vs self-hosted on customer infra

### L3 — Vendor-specific Detail (research notes only)

- Statuspage: 1100-component limit; Incident History link appears after 14 days; exact top-level-status decision tree; Librato/Pingometer integrations; "audience-specific pages" formerly "access control"; Localize translation service.
- Instatus: Slack `/incident postmortem` command; magic-link signup; instat.us status domain.
- Status.io: plan-tier subscriber counts (500/2000/5000); Twilio/Vonage SMS carriers; IRC/iCalendar channels; 90-day chart window; $79/$149/$349/$999+ pricing.
- Better Stack: `*.betteruptime.com` subdomains; widget types per component; status.stripe.com vs githubstatus.com naming conventions discussed in docs.

## Rejected Findings

- **"A status page platform must include monitoring"** — rejected. Statuspage explicitly does no monitoring and is the category-defining product. Detection is an integration or a bundle, not the Type.
- **"Subscriber notifications are definitional"** — rejected. A status page without subscriptions is still a status page (passive publication); subscriptions are the common mature engagement layer.
- **"Multi-page per organization is definitional"** — rejected. Status.io's one-public-page pole and Statuspage's multi-page pole both in-sample.
- **"The page must be hosted on independent infrastructure"** — rejected as definitional. Cachet (self-hosted) satisfies the Type on customer infrastructure. Independence is the SaaS-dominant realization.
- **"Incident states are universally Investigating/Identified/Monitoring/Resolved"** — rejected as universal claim; that exact vocabulary is directly observed in 2 products (Statuspage, Instatus); written as "commonly" in the final document.
- **"Postmortems are part of the core"** — rejected; only 2/5 sampled document them; common-not-definitional.

## Boundary Findings

### vs Incident Management (joint-review flag DISCHARGED)

The incident-management pass (2026-09-08) flagged: "internal response record vs stakeholder-facing publication surface; all four sampled products treat status pages as a separate surface (native module or integration)". Corroborated by on-call-management (2026-09-09).

**Keep-both RATIFIED** on the audience/surface seam:

- Incident Management's incident = the **internal response record** (triage/severity, mobilization, resolution workflow, timestamps for the response organization).
- Status Page Platform's incident = the **published communication** (narrative updates for stakeholders, subscriber notifications, published postmortem).
- Same word, different object role. Evidence from this side: Statuspage self-defines as "a communication tool… inform your users"; its incident docs are framed entirely as customer communication ("describing the issue, what you're doing about it, and when you expect the issue to be fixed"). Instatus's incident carries an explicit **publish-to-status-page checkbox** — authoring in the response tooling and publication are separable acts. Statuspage has no mobilization machinery at all (no on-call, no assignment, no severity-driven routing) — a status page platform can be a full product with zero response machinery.
- Fusion is real and bidirectional: incident tools ship status-page surfaces (their pass's evidence); status-page platforms add response tooling (Instatus on-call/escalation). The seam is the unit of record: response record vs publication.

### vs Monitoring Types (Synthetic / Infrastructure / Metrics Monitoring)

- Monitoring detects and records telemetry for the operator; the status page publishes health to stakeholders. Statuspage's own words: "does not do any direct monitoring of your websites or servers." Remove the published page → monitoring; remove detection → still a status page (manual updates). Bundled products (Better Stack, Instatus) keep both objects distinct internally (monitors feed components).

### vs On-call Management

- On-call = coverage estate + paging act (internal mobilization); status page = outward publication. No coverage/escalation/ack machinery is required here (Statuspage has none).

### vs ITSM / Enterprise Service Management

- ITSM's record base serves the internal service desk (tickets, requests, SLAs); the status page serves external/enterprise-wide stakeholders reading service health. Different audience, different record (published report vs worked ticket).

### vs Blog / CMS / Changelog

- Incident reports are structured records bound to components with enforced lifecycle states and notification triggers — not free-form posts. Remove the component binding and lifecycle → a blog.

### vs Public Alert & Warning System (§24 government)

- Name-adjacent only: that Type broadcasts emergency alerts to citizens from authorities; the status page publishes an organization's own service health. Different subject, audience, and record.

### "去掉什么就变成另一个 Type" 判据

- 去掉 published stakeholder-facing page → Incident Management / internal ops tool
- 去掉 incident/maintenance record machinery → monitoring dashboard / status board
- 去掉 service-health component model → outage blog / changelog
- 去掉 severity-ordered health states → announcement banner (not a status page)

## Historical / Market-Sample Check (§24)

- **Pre-platform era**: ISPs, universities, and hosting providers published hand-edited "system status" HTML pages listing services and current problems. Component list + incident notices + public page — satisfies L0 with no SaaS, no subscriptions, no metrics, no automation. ✓
- **Self-hosted pole**: Cachet (open-source, self-hosted) satisfies the Type without SaaS delivery. ✓
- **Single-page pole**: Status.io plans ship one public page; multi-page is not definitional. ✓
- **Pure-play pole**: Statuspage with zero monitoring and zero response machinery is the category archetype. ✓
- **Social-channel era**: companies tweeted outages; platforms treat Twitter/X as a *notification channel* (cross-posting), not the record. The record remains the platform's. ✓
- Conclusion: the L0 holds across eras and delivery substrates; nothing era-current (subscriptions, metrics, automation, SSO, embeds, AI) leaked into the core.

## Uncertainties

- Status.io operational documentation unreachable; its incident-state vocabulary and notification-trigger semantics unverified (product-page evidence only).
- Cachet feature depth unverified beyond identity/self-hosting (docs 404).
- Better Stack subscriber/subscription machinery not directly observed; subscriptions written as "common" from 3/5 products only.
- Whether every product computes top-level status automatically: documented for Statuspage; visible as banner behavior in Instatus ("All systems operational" footer) and implied elsewhere — written as common, not universal.
- Exact component-status vocabularies beyond Statuspage/Instatus not directly observed; final document describes the scale conceptually (healthy → degraded → partial → major, plus maintenance) rather than asserting universal labels.

## Final Synthesis

A Status Page Platform is the stakeholder-facing publication system for an organization's service health. Its defining core is three jointly-held structures: (1) the operator's services held as a named component inventory carrying severity-ordered health states, (2) the incident report — with its accumulating updates and lifecycle states, plus scheduled maintenance in mature products — as the unit of record bound to affected components, and (3) the published page the platform operates for stakeholders outside the response team, public or access-restricted. Everything else — subscriber notifications, metrics, automation, templates, embeds, SSO, multi-page, monitoring, on-call — is common mature structure, variant, or vendor detail. The Type's seam against Incident Management is the unit of record (published communication vs internal response record); its seam against monitoring is direction (outward publication vs inward detection). The historical check passes from hand-edited ISP status pages through self-hosted Cachet to modern SaaS suites.
