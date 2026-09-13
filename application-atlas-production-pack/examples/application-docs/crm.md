# Customer Relationship Management / CRM

## Overview

A **Customer Relationship Management (CRM)** application is a shared operational system for maintaining business relationships with people and organizations, recording interaction history, assigning responsibility, and tracking potential commercial outcomes.

For a sales-oriented CRM, the core can be summarized as:

```text
People + Organizations
        ↓ associations
Relationship History
        +
Potential Business
        ↓
Pipeline / Outcome
```

A CRM may be sold as part of a much larger suite, but marketing automation, help desk, CPQ and customer-success functionality are not required to define the core Application Type.

## Users & Context

Typical primary users include:

- **sales representative / account executive** — manages contacts, accounts and active deals
- **business development representative** — works prospects and qualification
- **account manager** — maintains an ongoing commercial relationship

Secondary users often include:

- **sales manager** — reviews pipeline and team activity
- **sales operations / CRM administrator** — configures fields, pipelines, users and rules

The system becomes valuable when customer knowledge must survive beyond one salesperson's inbox, memory or personal notes.

## Core Model

CRM is best understood as a **relationship graph plus commercial workflow**.

### People and organizations

A **Contact** represents a person.

An **Account** or **Company** represents an organization.

These records are not isolated. The CRM links them so that users can answer questions such as:

- Who works at this organization?
- What interactions have we had?
- What open commercial opportunities involve them?
- Who inside our company owns the relationship?

### Activity history

Calls, meetings, emails, notes and tasks form a chronological history around customer/prospect records.

This changes the product from a directory into an operational relationship record.

### Deal / Opportunity

A **Deal** or **Opportunity** represents a potential commercial outcome.

It is typically connected to:

- one or more people
- an organization
- an owner
- an amount/value
- a pipeline/stage
- activity history

A compact relationship model is:

```text
Account / Company
├── Contacts
├── Activities
└── Deals / Opportunities
      └── Pipeline Stage
```

### Lead

Many sales CRMs add a **Lead** as a pre-qualification record.

A common conceptual flow is:

```text
Lead
→ qualify
→ Contact + Account
→ Deal / Opportunity
```

However, a separate Lead object is not universal and should not be treated as mandatory for all CRM implementations.

## How It Works

### Build and maintain the relationship record

```text
Create/import Contact or Account
→ associate related records
→ assign owner
→ log calls/emails/meetings/notes
→ inspect the relationship history over time
```

### Turn a prospect into potential business

Where a Lead model is used:

```text
Capture Lead
→ assign
→ contact/work
→ qualify
→ convert/link to durable customer records
→ create Deal / Opportunity
```

### Move a deal through the sales process

```text
Create/open Deal
→ associate people/company
→ set owner/value/stage
→ log activity and next steps
→ move through pipeline
→ Closed Won
or
→ Closed Lost
```

The specific open stages vary by organization.

### Core vs common vs optional

**Core**

- customer/prospect records
- record associations
- activity/history
- ownership
- deal/opportunity management
- pipeline/stage progression
- search/list/filter

**Common**

- Leads and conversion
- tasks/reminders
- pipeline board
- dashboards/reports
- import/export
- custom fields
- deduplication
- email/calendar integration

**Optional / broader-suite**

- CPQ
- marketing automation
- customer support tickets
- advanced forecasting
- territory management
- AI sales assistance

## Interfaces

### Record list

Used for Contacts, Accounts/Companies, Leads or Deals.

Typical information:

- name
- owner
- status/stage
- important attributes
- recent activity

Primary actions:

- create
- search/filter
- assign
- bulk update
- open record

### Contact / Account detail

This is the relationship hub.

It commonly exposes:

- identity/contact data
- associated people/company
- activity timeline
- deals
- notes/tasks
- ownership

### Deal / Opportunity detail

The commercial working surface.

Typical information:

- company/contact associations
- owner
- amount
- pipeline/stage
- expected outcome/close
- activity history

Primary actions:

- update stage
- log activity
- change owner
- close won/lost

### Pipeline

Often rendered as a stage-grouped list or board.

Its purpose is to make commercial work visible as a lifecycle rather than a flat record list.

### Reports / Dashboard

Aggregates pipeline, activity, conversion and team performance.

This is common but not what makes the product a CRM.

## Important Rules / Behaviors

### Record association

Relationship context depends on linking records correctly.

A Contact, Account and Deal may all exist independently, but the CRM becomes much more useful when those records are associated.

### Ownership

Records commonly have an internal owner responsible for follow-up or commercial action.

### Deal lifecycle

A canonical conceptual model is:

```text
Open stage(s)
→ Closed Won
or
→ Closed Lost
```

Open stage names are configurable.

### Lead lifecycle

Where Leads are used:

```text
New / Unworked
→ Working
→ Qualified → Converted
         ↘ Disqualified
```

Exact names vary.

### Permissions

Organizations commonly restrict:

- record visibility
- edit/delete
- ownership reassignment
- export
- field changes
- pipeline/settings administration

### Important edge cases

- duplicate person/company records
- a Lead matches an existing Contact/Account
- a person changes employer
- one Deal involves multiple Contacts
- a lost Deal reopens
- the organization does not use Leads

## Variants

Common variants include:

- sales CRM
- account-management CRM
- SMB CRM
- enterprise CRM
- industry-specific CRM

An industry CRM should remain a Variant unless the industry's users, core records, workflow and rules materially change the product model.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Lead Management Platform | acquisition, routing and qualification are primary |
| Sales Pipeline Management | Deal/stage workflow is primary; broader durable relationship records may be secondary |
| Marketing Automation | audience, campaign and automated nurturing are primary |
| Help Desk | Ticket/Case resolution is primary |
| Customer Success Platform | post-sale health, adoption, renewal and expansion are primary |

## Representative Products

- Salesforce Sales Cloud
- HubSpot CRM
- Zoho CRM

## Sources

Research date: **2026-09-05**

Primary research sources:

- Salesforce Trailhead — Customize Sales Cloud  
  https://trailhead.salesforce.com/content/learn/modules/sales-cloud-configuration-basics/customize-sales-cloud
- Salesforce Trailhead — Create and Convert Leads  
  https://trailhead.salesforce.com/content/learn/modules/leads_opportunities_lightning_experience/create-and-convert-leads-lightning
- Salesforce Trailhead — Work Your Opportunities  
  https://trailhead.salesforce.com/content/learn/modules/leads_opportunities_lightning_experience/work-your-opportunities
- HubSpot Knowledge Base — Create companies  
  https://knowledge.hubspot.com/records/create-companies
- HubSpot Knowledge Base — Create deals  
  https://knowledge.hubspot.com/records/create-deals
- Zoho CRM — Core data model  
  https://help.zoho.com/portal/en/kb/crm/crm-reference/product-architecture-and-reliability/articles/zoho-crm-s-core-data-model-and-how-you-extend-it-safely

See the paired Research Notes for the cross-product evidence and boundary decisions.
