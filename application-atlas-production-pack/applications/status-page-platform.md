# Status Page Platform

## Overview

A **Status Page Platform** is the stakeholder-facing publication system for an organization's service health. The operator describes its own services as named components, keeps a current health status on each of them, records disruptions and scheduled maintenance as dated reports with narrative updates, and the platform publishes all of it on a web page that customers, end users, and internal stakeholders can read without contacting support or holding a seat in the operator's tooling.

The defining core is small — three structures that only work together:

```text
Service-health model (components with health states)
└── Incident / maintenance reports bound to affected components
    └── Published page operated for stakeholders
```

- Remove the published page and what remains is an internal incident log — a different Application Type.
- Remove the incident/maintenance record machinery and what remains is a bare status board or uptime dashboard.
- Remove the component model and what remains is an outage blog.

Everything else the market associates with status pages — subscriber notifications, uptime metrics, automation from monitoring tools, templates, embeds, single sign-on — is a standard capability layered on this core, not what makes the product a status page platform.

## Users & Context

**Operators (authors).** The people responsible for the service — typically support, communications, and engineering staff — configure the component inventory, declare incidents and maintenance, write updates, and decide what gets published and when. During an outage this is done under time pressure; templates and automation exist to make it fast.

**Stakeholders (readers).** Customers, end users, and internal teams who need to know whether the service they depend on is working. They read the page, optionally subscribe to notifications, and are otherwise passive. A reader needs no account for a public page; private and audience-restricted pages authenticate readers instead.

**Typical context.** The page earns its keep during incidents ("is it down, or is it me?"), during planned maintenance windows, and as a standing trust surface linked from footers, status badges, and support sites. Vendors consistently frame the value the same way: let users check service health without filing a support ticket, and reduce the question load on support during outages.

## Core Model

### The defining core

**1. The service-health model — components with health states.**
The operator's own services are held as a persistent inventory of named **components** — "the individual parts of your infrastructure that your users depend on; the functioning pieces or features of your application or service", in one vendor's wording. A component might be the website, the API, the mobile app, a dashboard, or a data-processing pipeline. Each component carries a current health status on a severity-ordered scale: healthy, degraded performance, partial outage, major outage, plus an under-maintenance state. Components can be grouped and ordered, and some products allow sub-components or location-like containers. Mature products also compute a **top-level status** for the whole page ("All Systems Operational" and its degraded siblings) from the component statuses — the single banner most readers recognize.

**2. The incident report — the unit of record.**
An **incident** is a dated, persistent report of a service disruption, bound to the components it affects, that advances through lifecycle states by accumulating timestamped updates: what happened, what the operator is doing, what to expect next, and finally resolution. The vocabulary commonly runs investigating → identified → monitoring → resolved, though exact labels vary by product. **Scheduled maintenance** is the sibling event type: a planned window announced in advance, often with reminders to subscribers before it begins, that typically sets affected components to an under-maintenance state. Incidents and maintenance — not free-form posts — are the records, and past incidents remain readable as the page's history.

**3. The published page.**
The platform operates a standalone web page — usually on a `status.` subdomain or custom domain — presenting the current component statuses, any active incidents or maintenance with their update timelines, and past history. The page is consumable by people outside the operating team: public by default, or access-restricted (password, login, per-group permissions) for private and audience-specific variants. Publication is a distinct act from authoring: one product's incident form literally contains a "publish to status page" checkbox, and the purest product in the market is explicitly a communication tool with no other machinery at all.

### Standard capabilities mature products add

These are widespread and expected, but a product lacking any of them is still a status page platform:

- **Subscriber notifications** — stakeholders opt in (email, SMS, webhook, RSS/Atom, Slack, Microsoft Teams, and other chat targets) and are notified when incidents are created or updated; subscriptions can often be scoped to individual components.
- **Uptime and metrics display** — historical uptime bars per component and live charts (response time, uptime) fed from the platform's own or external sources.
- **Automation** — alert parsing from monitoring tools, email-based automation, and a public API so component statuses and incidents can be updated programmatically.
- **Incident templates** — pre-written update structures for fast, consistent communication under pressure.
- **Third-party components** — the page can show the health of external dependencies (cloud providers, payment processors) the service relies on.
- **Embeds and badges** — widgets that carry current status into the operator's own website or product.
- **Cross-posting** — incident updates broadcast to social channels such as Twitter/X.
- **Postmortems** — some products support a published final review attached to a resolved incident.

### One structure, many implementations

```text
Concept:  service-health model
Realizations:  manually curated component list (pure-play platforms)
               components backed by the platform's own monitors (monitoring-bundled)
               components fed by external monitoring via integrations/API

Concept:  incident report
Realizations:  authored in the status page's own dashboard
               authored in an incident-management tool and published outward
               created automatically from monitor alerts, then narrated by a human

Concept:  the published page
Realizations:  public page on a hosted subdomain or custom domain
               private page behind a password or SSO
               audience-specific pages with per-group visibility
```

## How It Works

### Steady state: build the service model

```text
Create the page (subdomain or custom domain, branding)
→ add components for each customer-visible part of the service
→ group and order them
→ optionally attach monitors, metrics sources, or third-party dependency components
→ publish — the page now shows every component as healthy
```

### The incident loop

```text
A disruption is detected (by a human, a monitor, or an integrated alert)
→ operator creates an incident: title, description, affected components, initial state
→ incident publishes to the page; subscribers are notified
→ as understanding grows, the operator adds updates
   (state advances: investigating → identified → monitoring)
→ components' statuses reflect the impact (degraded / partial / major outage)
→ the incident is resolved; components return to healthy
→ the incident remains on the page as history; some products add a published postmortem
```

The loop's rhythm is the product's essence: short, factual, timestamped updates pushed outward while engineering works on the actual fix elsewhere. The status page platform carries the *communication* of the response, not the response itself.

### Scheduled maintenance

```text
Operator schedules a maintenance window (time range, affected components, description)
→ page shows the upcoming maintenance; subscribers receive advance notice
→ window opens: affected components switch to under-maintenance
→ updates as work proceeds
→ window closes: components return to healthy, record kept in history
```

### Staying current without humans

Mature products can keep the page truthful automatically: monitoring tools (native or external) toggle component statuses when checks fail or recover, and a public API lets the operator's own systems update statuses and incidents programmatically. Automation changes who flips the switch; it does not change the model.

## Interfaces

**The published status page** — the product's public face. A top-level status banner, the component list with per-component status (and commonly historical uptime bars), active incidents and maintenance with their update timelines, incident history, and a subscribe control. Read-optimized; no login for public pages.

**The operator dashboard** — where the work happens:

- *Components* — add, edit, group, reorder, archive; set status directly or through incidents; attach historical uptime display.
- *Incidents* — the incident list and the incident editor: title, description, affected components, state, updates, publish control, subscriber-notification choice.
- *Maintenance* — schedule windows, edit them, send reminders.
- *Subscribers* — manage the notification audience: individual additions, CSV import/export, per-component subscription settings.
- *Settings / customization* — branding, custom domain, notification channels, templates, integrations, API keys.

**Notification surfaces** — email, SMS, webhooks, RSS/Atom, chat tools, and social channels carry updates to subscribers who never visit the page itself.

**Embeds and badges** — small live widgets placed in the operator's own web properties, reflecting current status in real time.

## Important Rules / Behaviors

**Component status drives the page.** The top-level banner is derived from component statuses — one vendor documents the exact decision rules; others show the same behavior. Changing a component's status (directly or via an incident) can change the whole page's headline message.

**Incidents are bound to components.** The affected-component selection is what computes an incident's severity/impact in mature products, scopes component-level subscriptions, and keeps the service model and the event record coherent. An incident with no affected components is possible but degenerate.

**Publication is separable from authoring.** An incident can exist unpublished (draft) and be pushed to the page deliberately; updates can be written without notifying subscribers, or with notification. This control is central during fast-moving incidents, where premature or noisy communication has real costs.

**Lifecycle states are enforced by the system.** Incidents move through their states via updates with timestamps; the resolved state closes the loop but the record persists. Maintenance windows have their own before/during/after behavior.

**The page must survive the outage.** The published page is deliberately kept reachable when the operator's own services are down — hosted services emphasize redundant, independent infrastructure for exactly this reason. (Self-hosted products give up some of this independence by design.)

**Reader access is a spectrum.** Public pages are open to anyone; private pages authenticate readers; audience-specific pages show different components and accept different subscriptions per group. The publication machinery is the same; the audience differs.

## Variants

- **Pure-play communication platform** — no monitoring, no response tooling; the page and its records are the whole product. Integration or API work supplies freshness.
- **Monitoring-bundled platform** — uptime monitors (and often heartbeats) are first-class; components are backed by checks, and failures can open incidents and flip statuses automatically.
- **Operations-suite module** — the status page ships as a surface inside an incident-management or observability suite, fed by that suite's incidents and monitors.
- **Self-hosted open source** — the same core operated on the customer's own infrastructure.
- **Audience variants** — public customer page; private internal page for employees; audience-specific pages for per-customer or per-tier visibility (common in single-tenant or sharded hosting situations).
- **Scale variants** — a single page for one product line vs multiple autonomous pages (per brand, per region, per product) under one organization.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Incident Management | closest neighbor, same word "incident" | incident management holds the *internal response record* (triage, severity, mobilization, resolution workflow); the status page holds the *published communication*. Incident tools commonly ship a status-page surface; status-page platforms commonly integrate with incident tools — the seam is the unit of record |
| On-call Management | adjacent in the response chain | coverage schedules, escalation paths, and page-and-acknowledge machinery mobilize responders; the status page informs stakeholders. No coverage or acknowledgment machinery is required here |
| Synthetic / Infrastructure / Metrics Monitoring | upstream data source | monitoring detects and records telemetry for the operator; the status page publishes health outward. A status page platform explicitly needs no monitoring of its own |
| IT Service Management / Enterprise Service Management | discipline-level neighbor | ITSM's record base serves the internal service desk (tickets, requests, SLAs); the status page serves stakeholders reading service health. Different audience, different record |
| Blogging / CMS | surface-level resemblance | incident reports are structured records bound to components with enforced lifecycle states and notification triggers — not free-form posts; remove the binding and lifecycle and it degrades into a blog |
| Public Alert & Warning System | name-adjacent only | that Type broadcasts emergency alerts to citizens from authorities; a status page publishes an organization's own service health to its stakeholders |
| Customer Communication Management | adjacent communication Type | CCM manages produced documents and outbound correspondence; the status page is a live, self-service service-health surface |

## Representative Products

- **Statuspage (Atlassian)** — the category-defining pure-play communication tool; explicitly performs no monitoring of its own.
- **Instatus** — modern challenger bundling monitoring, incident response, and status pages.
- **Status.io** — long-running independent dedicated platform with an enterprise-compliance flavor.
- **Better Stack** — monitoring-first suite where status pages are built from the platform's own monitors and heartbeats.
- **Cachet** — open-source, self-hosted status page system; the non-SaaS pole.

## Sources

Research date: **2026-09-09**

- Statuspage (Atlassian Support): What is Statuspage? · What is an incident? · What is a component? · Top-level status and incident impact calculations · What are audience-specific pages — https://support.atlassian.com/statuspage/
- Instatus Help: Get started · Manage your components · Get started with public status pages · Get started with Incidents — https://help.instatus.com/
- Status.io: product and plans page — https://status.io/
- Better Stack Documentation: Get started with status pages — https://betterstack.com/docs/uptime/status-pages/
- Cachet: official repository README — https://github.com/CachetHQ/Cachet

> Sourcing limitation: Status.io's operational documentation site was unreachable from the research environment (product-page evidence only; no operational specifics asserted for it), and Cachet's documentation site was unreachable (identity and self-hosted nature confirmed from its official repository README only). Precise vendor-specific figures (component limits, plan quotas, chart windows, exact state-label sets beyond the two products that document them) are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
