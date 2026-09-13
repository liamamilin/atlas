# Customer Relationship Management / CRM

## Overview

A **Customer Relationship Management (CRM) application** is a selling organization's shared system of record for its customer and prospect relationships. It holds persistent records of the people and organizations the organization does business with — or wants to — attaches a cumulative history of interactions to those records, and manages the commercial progression toward outcomes: deals moving through pipeline stages toward closed-won or closed-lost.

The defining core is deliberately small: relationship records, interaction history, and managed commercial progression, worked as shared organizational records rather than personal address-book entries. Everything else commonly associated with CRMs — lead objects, forecasting dashboards, email integration, custom objects, AI assistance, whole marketing and service suites — is widely supported by mature products but is not what makes a CRM a CRM. A paper-era sales office (card file of contacts, client folders, correspondence log, forecast board) already contains this core.

When the working center shifts to stewarding standing customer organizations rather than the acquisition-to-close selling motion, the product is drifting toward the Account Management CRM Type; when only the deals remain, toward Sales Pipeline Management; when the records serve service recovery rather than commercial progression, toward customer service Types.

## Users & Context

The primary users are people who sell or manage selling on behalf of an organization:

- **Sales representatives** — work their own set of records: prepare calls from the contact's history, log what happened, move their deals through stages, schedule next steps.
- **Sales managers** — inspect the pipeline across the team, review deal progress and stalled stages, forecast revenue, reassign records when territories or staffing change.
- **Sales operations / administrators** — configure the data model (fields, pipelines, stages), permission model, duplicate rules, and integrations.

Secondary users reach into the same records from adjacent jobs: marketing staff checking which contacts belong to their programs, service staff reading the relationship history, finance reading deal values. This cross-department reach is a consequence of the record design — one shared record per person and organization, not per department.

The typical setting is a team inside an organization whose income depends on winning and keeping customers — from a two-person firm to a global sales force. Records outlive job changes: when a representative leaves, their accounts and deals are reassigned, and the history stays with the organization.

## Core Model

### The Defining Core

```text
Selling organization
└── Relationship records
    ├── Person records (contacts)
    ├── Organization records (accounts / companies)
    │     └── associations bind persons ↔ organizations ↔ deals,
    │         often with labeled roles (e.g. decision maker)
    ├── Interaction history on every record
    │     (calls, emails, meetings, notes, tasks — the record's timeline)
    └── Shared working
        (ownership, assignment, permission-scoped visibility, dedup/merge)
        └── Managed commercial progression
            └── Deal / opportunity (value, owner, expected close)
                └── Pipeline = ordered, customer-defined stages
                    └── open stages → closed-won / closed-lost
```

Four structures. If any one is removed, the product stops being recognizable as a CRM:

- **Relationship records of record** — persistent, individually identified records for people (contacts) and organizations (accounts or companies) the organization has or pursues commercial relationships with. Records carry their own profile fields and unique identifiers, and are held by the organization: owned, assignable, permission-scoped. Without this, the product is a personal address book or a directory.
- **Cumulative interaction history** — every touch (call, email, meeting, note, task) is recorded against the relationship as a durable timeline. This history is why the record has value: it is the organization's memory of the relationship, surviving personnel change. Without it, the system is a contact list with no relationship memory.
- **Managed commercial progression** — the deal (or opportunity): a trackable potential outcome with a value, an owner, and an expected close, moving through the stages of a pipeline until it closes as won or lost. This is the structure that connects the relationship records to the organization's revenue motion. Without it, the product is a contact/account book, not a CRM.
- **Shared working over the records** — the records are worked collaboratively: each has an owner, visibility follows permission rules, duplicates are found and merged, and records move between people as circumstances change. Without it, the product is single-person contact software.

### How the Records Fit Together

A person record and an organization record are related by an association — a contact "works at" a company; many contacts belong to one organization. A deal is associated with the organization it targets and with the specific people involved, sometimes with labeled roles (their example in one product's documentation: "decision maker"). The interaction history hangs off all of these: a call logged on the contact also appears in the organization's and the deal's picture of the relationship.

### One Structure, Many Implementations

The core is written in conceptual terms. Realizations vary:

```text
Concept:      person records            → contacts (several products), customer/partner people records
Concept:      organization records      → accounts, companies
Concept:      deal                      → opportunities, deals
Concept:      progression container     → pipelines with customer-defined stages; stage tracks on records
Concept:      interaction history       → activity/engagement timelines; auto-logged email/calendar where supported
```

A reader who knows only one implementation — say, a product where every record is a "contact" — should still recognize the others from this model.

### Capabilities Shared by Mature Products

These make a CRM practical, but a product can lack some and still be a CRM:

- **Prospect intake path** — how unqualified prospects enter the system before anyone commits to pursuing them. Implementations differ structurally: some products use a dedicated lead object that is later "converted" into contact, account, and deal records; others mark the person record with a lifecycle stage; others provide a lead inbox feeding the same records.
- **Duplicate detection and merge** — multiple records for the same person or organization are identified and consolidated, with unique identifiers (email for people, domain for organizations in one documented implementation) guarding against new duplicates.
- **Ownership and access control** — every record has an owner; visibility and edit rights follow role and team structures; records can be shared, reassigned, or transferred in bulk.
- **Email and calendar integration** — correspondence with a contact is logged to the record, often automatically; templates and one-click sending keep touches inside the system.
- **Activity management** — tasks, calls, and meetings with due dates, tied to records and surfaced in personal to-do and calendar views.
- **Forecasting** — open deals roll up into revenue projections, commonly weighted by each stage's win probability.
- **Views and search** — filterable list views, saved views, a pipeline board, a global search across all records.
- **Reporting** — win rates, conversion by stage, activity volume, pipeline movement.
- **Extensibility** — custom fields everywhere; custom objects and platform extensibility in the enterprise pole; APIs and integration ecosystems in essentially all current products.

## How It Works

### Bring a prospect into the system

```text
prospect appears (web form, import, manual entry, purchased list, inbound reply)
→ a record is created (lead object, or person record with an early lifecycle stage)
→ owner assigned
→ qualification: interactions logged, details enriched
→ qualified: the prospect is linked to an organization record (creating or matching one)
   and becomes attached to a deal
```

The same motion serves a returning customer: the record already exists, and work continues on it. Nothing in the defining core requires the lead to be a separate object — that is one implementation of the intake path.

### Work a deal through the pipeline

```text
create deal (value, expected close, owner, associated organization + contacts)
→ deal sits in an open pipeline stage
→ rep performs next steps (calls, meetings, proposals — logged to the record)
→ deal moves stage by stage as it advances
→ terminal outcome: closed-won, or closed-lost
   (lost deals can later be reopened; won deals may hand off to orders/fulfillment)
```

The stages are the selling organization's own process, expressed as configuration: their names, number, and order are defined by the customer, not fixed by the product. Movement is usually a drag on a board or a stage change on the record. Many products attach probability to stages so forecasting can weigh the pipeline; some restrict or validate unusual stage jumps.

### Maintain the relationship over time

```text
every interaction is recorded (manually, or auto-logged from email/calendar/phone)
→ the record's timeline grows
→ activity due-dates generate the rep's daily work queue
→ records are enriched (data from enrichment services, forms, imports)
→ duplicates merge; ownership transfers; records are deactivated when relationships end
```

This loop is continuous for the life of the relationship — before, during, and after any single deal — and it is why organizations adopt a CRM at all: the memory lives in the system, not in individual inboxes.

### Manage the system

Administrators define fields, pipelines and stages, duplicate rules, permission models, and integrations. In the enterprise pole this configuration extends to building whole new object types and process automation on the same platform; in lighter products it stays within fields-and-stages configuration.

### Defining core vs common vs optional

**Defining core** — relationship records (persons + organizations, associated), interaction history on records, deals managed through configurable pipeline stages to won/lost, shared organizational working (ownership, permissions, dedup/merge).

**Standard capabilities** — prospect intake path, email/calendar integration, activity queues, forecasting, reporting, saved views, global search, mobile apps, APIs, custom fields.

**Common variants** — dedicated lead objects vs lifecycle stages; kanban boards vs list-first interfaces; custom objects/platform extensibility; quotes and product catalogs attached to deals; workflow automation; AI assistance; suites that extend the same records into marketing, service, or commerce.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Record detail page (contact / account / deal)

The workhorse surface.

- Purpose: hold everything known about one relationship in one place.
- Typical information: profile fields, the interaction timeline, associated records (contact's organization, organization's contacts, deal's parties), open activities.
- Primary actions: edit fields, log a call/note/email, create a task or meeting, associate records, move a deal's stage.

### Pipeline board

- Purpose: show the selling motion at a glance and move it forward.
- Typical information: deals grouped by stage, value, owner, age, expected close.
- Primary actions: drag deal between stages, open deal, filter by owner/team, create deal.

### List views

- Purpose: work the population of records — segmentation, hygiene, bulk actions.
- Typical information: filtered record tables with sortable columns; saved views.
- Primary actions: filter, sort, bulk edit/reassign, export, merge duplicates.

### Activity / work queue

- Purpose: tell the rep what to do today.
- Typical information: overdue and upcoming tasks, calls, meetings tied to records.
- Primary actions: complete, reschedule, log outcome, jump to the record.

### Forecast / reports

- Purpose: aggregate the record base into management view.
- Typical information: pipeline by stage, forecast by period or rep, win/loss and conversion measures.
- Primary actions: adjust forecast inputs, drill into contributing deals, build reports.

### Administration / setup

- Purpose: configure the data model and rules.
- Typical information: fields, pipelines and stages, duplicate rules, permission roles, integration settings.
- Primary actions: create/modify configuration, manage users and permissions.

A mobile companion surface carries the same record-and-activity loop into the field.

## Important Rules / Behaviors

- **Ownership governs work.** Records and deals have owners; most day-to-day work happens on records a user owns or is granted access to. Visibility and edit rights follow role/team structures, and enterprise implementations expose record-level sharing (grant/modify/revoke access) as first-class machinery.
- **The pipeline's stages are configuration, not constants.** Stage names, order, and count are defined per organization (and an organization can run several parallel pipelines — new sales and renewals, for instance). The only fixed points in observed products are the terminal outcomes: won and lost.
- **Closed is a real state.** A deal that closes as won or lost leaves the open pipeline; forecasting counts open deals. Lost deals can typically be reopened, and stage regression is either allowed, flagged, or restricted depending on the product's rules.
- **Deduplication protects the record.** Because the record is the system of record, duplicate persons/organizations are treated as defects: products detect likely duplicates (using key identifiers) and provide merge machinery that consolidates them without losing history.
- **History is additive, not a scratchpad.** Logged interactions accumulate as a timeline; the expected behavior is that anyone stepping onto the record can reconstruct the relationship from it.
- **Records outlive relationships' active phases.** Ended relationships are typically deactivated rather than deleted, preserving history and reporting integrity.
- **Contact governance lives on the record.** Suppression-style flags (do not email / do not call) can be recorded against the person or organization and are respected by outbound actions — an organizational rule, not merely a setting.

## Variants

- **Enterprise platform CRM** — the record model is extensible (custom objects, automation, whole applications built on the same platform); deep permission and hierarchy models; often one module of a wider business suite.
- **Inbound / contact-centric CRM** — the person record is the universal center; organizations and deals hang off it; freemium entry pricing; typically one hub of a marketing/sales/service suite.
- **Pipeline-first CRM** — the deal board is the home surface and the product philosophy; minimal configuration surface, sold on selling discipline rather than platform breadth.
- **Modular SMB/mid-market CRM** — a CRM core plus separately licensed modules (marketing, service, inventory) sharing the record base.
- **Industry and domain instantiations** — real estate brokerage, nonprofit donor management, creator audience management, government constituent management, and similar vertical products are the same family shape (person-centric records + interaction history + progression toward domain outcomes) specialized to a domain; the directory treats several of them as their own Types.
- **Suite-embedded CRM** — CRM capabilities delivered inside an ERP or business-management system, where the customer record extends into order and billing data.
- **Deployment posture** — cloud SaaS dominates the current market; self-hosted and on-premises products persist in regulated and regional niches.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Account Management CRM | same family, sibling Type | center of gravity on the standing customer-organization record and ongoing stewardship; CRM's center is the acquisition-to-close selling motion over person records and deal progression. Same products often serve both; the split is emphasis, not disjoint machinery |
| Lead Management Platform | adjacent, upstream | centers the transient pre-qualification population; CRM holds the full prospect-to-customer relationship of record, with lead handling as one intake mechanism |
| Sales Pipeline Management / Opportunity Management | adjacent, slice | centers the deal and its board; in a CRM the pipeline is one structure over the relationship record |
| Sales Engagement Platform | adjacent, execution | executes outreach (sequences, dialers, tracking) and writes results back into the system of record; the CRM's center is the record, not the send |
| Customer Success Platform | adjacent, downstream | adds post-sale adoption/health/renewal machinery (telemetry, health scores, playbooks) on top of relationship data; a CRM can hold post-sale relationships without that machinery |
| Marketing Automation Platform | adjacent, upstream | centers the reusable automated program and per-contact program execution over its own consented person database; person records are the shared seam |
| Help Desk / Customer Service Platform | adjacent, different job | service case/ticket semantics; pipeline-style stage machinery can serve both jobs, so the distinguishing job is commercial progression vs service recovery |
| Sales Prospecting / Contact Discovery / Data Enrichment | supply side | supply data into the CRM record; they do not steward it |
| ERP / Order Management | downstream handoff | processes orders, billing, and fulfillment; won deals may convert into ERP transactions, but commercial relationship progression is not ERP's center |
| Customer Data Platform | data-layer adjacent | aggregates identity and events for marketing activation; the CRM's records are operational working records for selling |

## Representative Products

- Salesforce Sales Cloud — market-canonical enterprise platform CRM
- Microsoft Dynamics 365 Sales (Dataverse) — enterprise platform pole
- HubSpot CRM — inbound, contact-centric freemium pole
- Pipedrive — pipeline-first pole
- Zoho CRM — modular SMB/mid-market pole

The defining core was checked against the paper-era sales office and early sales-force-automation-era software to avoid defining the Type by the current SaaS implementation.

## Sources

Research date: **2026-09-08**

- HubSpot Developers — Understanding the CRM APIs: https://developers.hubspot.com/docs/api/crm/understanding-the-crm
- HubSpot Developers — Pipelines API guide: https://developers.hubspot.com/docs/api-reference/latest/crm/pipelines/guide
- Microsoft Learn — Dataverse Account table/entity reference: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/account
- Pipedrive — Sales pipeline management (product page): https://www.pipedrive.com/en/features/sales-pipeline

> Sourcing limitation: official Salesforce documentation (Help and Developer surfaces) and Zoho CRM documentation could not be fetched from the research environment (repeated access errors), so these two poles are treated structurally and no product-specific claims in this document derive from them. Pipedrive's support-knowledge-base articles were also unreachable; claims from that product rest on its official product page. Deal-stage lifecycle detail is therefore evidenced from two products directly, with the remaining sample contributing structural confirmation. Detailed evidence, per-product observations, and the cross-product comparison are recorded in the paired Research Notes.
