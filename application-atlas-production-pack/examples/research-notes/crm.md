# Research Notes — Customer Relationship Management / CRM

## Research Goal

Identify the stable external model of a general **sales-oriented CRM** without treating the full Salesforce/HubSpot/Zoho suites as the definition of CRM.

## Initial Boundary

Target:

> Customer Relationship Management / CRM

Nearest confusing types:

- Lead Management Platform
- Sales Pipeline Management
- Marketing Automation
- Help Desk
- Customer Success Platform

Working hypothesis:

> CRM is fundamentally a shared relationship record system linking people, organizations, activities, ownership and potential commercial outcomes.

## Research Questions

- What kinds of customer/prospect records are stable across products?
- How are people and organizations related?
- How is potential business represented?
- How are activities attached to relationships?
- What role does ownership play?
- How do deals/opportunities progress?
- Is Lead a universal object or a common sales-CRM pattern?
- Which suite modules should be excluded from CRM core?

## Representative Products

| Product | Why selected |
|---|---|
| Salesforce Sales Cloud | enterprise reference with explicit sales object model |
| HubSpot CRM | modern CRM with strong record association model |
| Zoho CRM | broad SMB/midmarket CRM exposing standard record modules |

## Sources

Research date: 2026-09-05

### Salesforce

- Customize Sales Cloud  
  https://trailhead.salesforce.com/content/learn/modules/sales-cloud-configuration-basics/customize-sales-cloud
- Create and Convert Leads  
  https://trailhead.salesforce.com/content/learn/modules/leads_opportunities_lightning_experience/create-and-convert-leads-lightning
- Work Your Opportunities  
  https://trailhead.salesforce.com/content/learn/modules/leads_opportunities_lightning_experience/work-your-opportunities

### HubSpot

- Create companies  
  https://knowledge.hubspot.com/records/create-companies
- Create deals  
  https://knowledge.hubspot.com/records/create-deals

### Zoho CRM

- Zoho CRM core data model  
  https://help.zoho.com/portal/en/kb/crm/crm-reference/product-architecture-and-reliability/articles/zoho-crm-s-core-data-model-and-how-you-extend-it-safely
- Customize modules  
  https://help.zoho.com/portal/en/kb/crm/customize-crm-account/customizing-modules/articles/customize-modules

## Product Observations

### Salesforce Sales Cloud

Stable visible concepts:

- Lead
- Account
- Contact
- Opportunity

Important behavior:

```text
Lead
→ qualification
→ conversion
→ Account + Contact (+ Opportunity)
```

Opportunity carries the potential sale and progresses through sales stages.

### HubSpot CRM

Stable visible concepts:

- Contact
- Company
- Deal
- associations between records

A Deal represents potential revenue and can be associated with Contacts and Companies.

The explicit association model reinforces that CRM is not merely a collection of independent lists.

### Zoho CRM

Standard modules include:

- Leads
- Accounts
- Contacts
- Deals
- Activities

This supports the same broad model:

```text
relationship records
+
commercial record
+
activity history
```

## Cross-product Comparison

| Finding | Salesforce | HubSpot | Zoho | Canonical decision |
|---|---|---|---|---|
| person record | Contact | Contact | Contact | Core |
| organization record | Account | Company | Account | Core |
| potential sale | Opportunity | Deal | Deal | Core |
| record associations | yes | explicit | yes | Core |
| activity/history | yes | yes | Activities | Core/Common |
| owner/responsibility | yes | yes | yes | Core/Common |
| pipeline/stages | yes | yes | yes | Core |
| Lead object | explicit | deployment/setup varies | explicit | Common; often core in sales CRM |
| support case/ticket | suite/ecosystem | available | available | Optional/bundled |
| quote/product catalog | available | available | available | Optional |

## Canonical Model

The strongest abstraction is not “Lead + Contact + Deal.”

It is:

```text
People
+
Organizations
+
Relationships / Associations
+
Activity History
+
Potential Business
+
Ownership
+
Pipeline Lifecycle
```

One useful structural view:

```text
Account / Company
├── Contacts
├── Activities
└── Deals / Opportunities
      └── Pipeline Stage
```

Lead, where used:

```text
Lead
→ qualify
→ Contact / Account
→ Deal / Opportunity
```

## Vendor-specific / Rejected Findings

Do not define CRM core using:

- Salesforce-specific clouds/modules
- ticket/service depth
- marketing automation
- CPQ
- territory management
- AI assistant features
- vendor-specific forecasting modules

## Boundary Findings

### vs Lead Management

Lead Management focuses on prospect intake, routing and qualification.

CRM continues beyond lead qualification into durable relationship records and commercial history.

### vs Sales Pipeline Management

Pipeline Management can focus almost entirely on deals/stages.

CRM also maintains people, organizations and relationship history.

### vs Help Desk

Help Desk centers on Tickets/Cases and service resolution.

### vs Customer Success

Customer Success centers on post-sale health, adoption, renewal and expansion.

## Uncertainties

- not every CRM uses a separate Lead object
- exact distinction between Contact and Account/Company may change in B2C or person-account models
- “CRM” in the market can denote broad suites; this example intentionally models the sales-oriented canonical center

## Final Synthesis

Canonical sales CRM:

```text
shared relationship record
=
people
+ organizations
+ associations
+ activities
+ ownership
+ commercial opportunities
+ pipeline/lifecycle
```
