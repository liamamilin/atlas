# ABM Platform

## Overview

An **ABM Platform** (Account-Based Marketing platform) is a B2B marketing application organized around **target accounts — companies — rather than individual leads or contacts** as the primary audience unit. A marketing organization uses it to define and maintain lists of companies it has decided to pursue, run coordinated marketing toward the people at those companies across channels, and measure engagement and commercial progression at the company level.

The defining core is small:

```text
Target account (a company as an identified record)
└── Target account list / segment (the account-level audience object)
    └── Coordinated activation toward the account across one or more channels
        └── Account-level engagement and progression measurement
            (feeding back into prioritization)
```

Three properties hold the Type together. Targeting is defined and measured at the company level; the platform actually executes or orchestrates marketing toward those companies; and engagement plus commercial progression are tracked per account so the selection can be re-prioritized. Remove the account-level unit and the product becomes lead-centric marketing automation. Remove activation and it becomes account analytics. Remove account-level measurement and it becomes ordinary campaign or ad execution that happens to include company attributes.

Everything else the category is known for — website-visitor identification, third-party intent data, predictive scoring, journey stages, owned ad-tech, orchestration canvases, sales alerts — is widespread in mature products but is an elaboration of this loop, not the definition. Older and simpler implementations (a CRM-exported account list, display advertising against it, and a per-account engagement report) satisfy the same core without any of the modern machinery.

## Users & Context

**Primary users** are B2B marketing teams at companies whose revenue is concentrated in a manageable number of business accounts — long sales cycles, multiple stakeholders per purchase, deal sizes that justify coordinated pursuit:

- **ABM / demand-generation marketers** — build target account lists, define tiers, launch and tune programs
- **Marketing operations** — configure integrations, data mappings, stage definitions, and permissions

**Secondary users** consume the platform's output rather than operating it:

- **Sales representatives and SDRs** — receive account alerts, see engagement and stage context (often inside their CRM or a companion sales-intelligence surface), and act on in-market accounts
- **Revenue operations** — own the CRM/MAP data spine and the account-level reporting used for planning

**Context of use.** The platform sits beside a CRM (the sales system of record) and usually a marketing automation platform (the email/nurture engine). It does not replace either: it tells both systems which accounts matter, enriches their records with account-level signal, and pulls opportunity state back so marketing can see commercial progression. The typical working rhythm is a planning cycle (define/refresh target lists) overlaid on a continuous loop (monitor account engagement → prioritize → activate → measure).

## Core Model

### The account is the central object

A **target account** is a company record — identified in practice by attributes such as its web domain, name, country, and headquarters — that the organization has chosen to pursue. Accounts are the unit to which everything else attaches: signals, people, stages, campaigns, and revenue outcomes. Person-level records (contacts, buying-committee members) exist in the model, but they hang under accounts and roll up to them.

### The target account list is the primary audience object

Marketing work is organized around named **account lists** (also called segments). A list is built in two fundamentally different ways, and most products support both:

- **Dynamic (filter-based)** — the list is a saved query over a large company database combined with the customer's own CRM/MAP data and signal data. Membership re-evaluates automatically as data changes, so accounts enter and leave the list as they begin or stop matching.
- **Static (imported)** — the list is a fixed set of accounts uploaded from a file or synced once from a CRM list or report. Membership changes only when someone edits it.

On top of a list, products commonly support **account groups** (tiers): subsets defined by filters such as fit grade, revenue potential, journey stage, or deal stage, used to differentiate investment level and messaging — for example, a small "tier 1" group receiving intensive, personalized treatment and broader tiers receiving programmatic coverage.

### Signals qualify and prioritize accounts

Three signal families recur across the category:

- **Fit** — how similar a company is to the ideal customer profile (firmographics, technologies, and similarity to past won opportunities). Often expressed as a grade or score.
- **Intent** — evidence that people at the company are researching the relevant problem space: third-party research activity on publisher networks and review sites, consumption of topic/keyword content, and first-party engagement such as website visits, content downloads, and form fills.
- **Engagement** — the account's direct interactions with the vendor: website activity, ad impressions and clicks, email and content engagement, and sales outreach activity.

These signals feed **scores** and **stage models**. A typical product computes account-level scores (fit, engagement, in-market likelihood) and places each account in a **buying/journey stage** — a small ordered set of account-level lifecycle states running from no activity through engagement to open opportunity and won deal. Stage definitions are either vendor-computed (predictive models over intent signals) or customer-defined rules over the available data sources; both patterns exist in mature products, and some products let customers customize stage definitions to match their own funnel. Stage movement is tracked over time, including regression — accounts can move backward.

### Activation: coordinated programs toward accounts

The platform activates toward accounts through a mix of channel types:

- **Account-targeted advertising** — display, video/CTV, and social programs delivered to the account's people or digital properties. Mature products either run this on their own ad infrastructure or sync account segments to external ad platforms (professional networks, search/social ad systems) that support company targeting.
- **People-level channels via orchestration** — because email and sales sequences address people, not companies, the platform orchestrates audiences into the systems that own those channels: adding contacts to marketing-automation lists, CRM campaigns, or sales-engagement sequences, typically driven by account-level triggers (stage change, engagement spike).
- **Web experiences** — in some products, account-aware personalization of website content.
- **Sales alerts and handoffs** — pushing prioritized accounts and engagement context to sellers.

Orchestration is commonly expressed as configurable workflows — in some products a visual canvas — combining audience sources and filters, decision logic, channel actions, timers, and exits, run on demand or on a schedule.

### Measurement closes the loop

Account-level analytics tie the loop together: engagement per account, stage distribution and progression/regression over time, program and segment performance, and — where CRM integration is in place — the relationship between marketing activity and opportunities/pipeline. These reports are not generic dashboards; their unit of analysis is the account and the account list.

### The integration spine

CRM integration (and, where used, MAP integration) is structural rather than optional in mature deployments:

- **Outbound:** account scores, stages, and segment memberships are written back to CRM/MAP records; audiences are pushed into MAP lists and sales-engagement tools.
- **Inbound:** opportunity and deal state flows from CRM so stages and revenue reporting reflect commercial reality.
- **Matching:** leads/contacts are commonly matched to their parent accounts (lead-to-account matching), with configurable rules for ambiguous cases.

```text
Signals (fit / intent / engagement)
        ↓ qualify & prioritize
Target Account List / Segment
        ↓ tier into
Account Groups
        ↓ activate
Advertising · Orchestration (MAP/SEP/email) · Web experiences · Sales alerts
        ↓ measured as
Account engagement & journey-stage progression
        ↓ synced with
CRM / MAP (accounts, scores, stages, audiences, opportunities)
```

## How It Works

The defining workflow is a continuous loop rather than a single transaction:

### 1. Define the target universe

The marketing team agrees with sales on which accounts to pursue, then expresses that decision in the platform: build an account list from an ideal-customer fit model, from intent and engagement filters, from an uploaded or CRM-synced list, or a combination. The list is the contract between marketing and sales — both organizations work from the same set of accounts.

### 2. Identify and track account engagement

A tracking tag on the vendor's website attributes anonymous visitor activity to companies (probabilistically — see Rules below). Third-party intent sources and the customer's own CRM/MAP activity feed the same account records. Over time each account accumulates an engagement picture: who visited, what they consumed, what they responded to.

### 3. Prioritize

Scores and stage models rank the list: which accounts fit best, which are showing buying activity, which have crossed into a stage that justifies sales attention. Accounts are tiered into groups so that investment (budget, personalization depth, sales effort) matches opportunity. Prioritization results are written back to CRM so sellers see the same ranking.

### 4. Activate

Programs run toward the prioritized accounts: advertising aimed at the account across web, social, and connected-TV inventory; orchestrated email and sales sequences aimed at the account's people through the MAP and sales-engagement tools; optionally personalized web experiences; and alerts telling sellers which accounts just became active. Activation is coordinated — the point of the category is that the same account receives consistent, sequenced treatment across channels rather than disconnected campaigns.

### 5. Measure and feed back

Account-level reports show engagement trends, stage progression and regression, program performance, and pipeline influence. Lists and tiers are refreshed; budgets shift toward what moves accounts; the loop restarts.

### Capability tiers

**Defining core** — without these, it is not an ABM platform:

- target account as the identified company record
- account list/segment as the audience object (dynamic or static)
- activation of marketing toward accounts on at least one channel
- account-level engagement and progression measurement feeding prioritization

**Standard capabilities** — present in most mature products:

- website-visitor identification into accounts
- intent data (third-party and/or first-party keyword)
- fit/ICP scoring and account groups/tiering
- buying/journey stage model with progression tracking
- account-targeted advertising (owned or via segment sync)
- orchestration into MAP/CRM/sales-engagement channels
- CRM/MAP integration with lead-to-account matching and score/stage export
- sales-facing alerts, dashboards, and CRM widgets
- people/buying-committee records under accounts
- account-level reporting (engagement, funnel, program performance)

**Optional / variant** — depends on product and segment:

- account-aware web personalization
- owned ad-tech (DSP) versus sync-only advertising
- AI-generated email agents and conversational programs
- contact data acquisition (purchasing/unlocking contact records)
- self-serve free tiers versus enterprise sales-led onboarding
- bundled data-unification or attribution modules sold alongside

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Account list / segment builder

The audience construction surface.

- filter palette over company attributes, signals, scores, stages, and CRM/MAP data; live preview of matching accounts; import/upload for static lists
- primary actions: create/edit a list, save filters as templates, tier the list into groups, attach activations

### Account list view & account detail

The working view of the audience.

- list view: accounts with fit grade, engagement, stage, owner, and list membership; search and sort
- account detail: engagement timeline, intent topics, people/buying-committee members, scores, stage history, open opportunities
- primary actions: inspect engagement, add/remove from lists, exclude an account, hand off to sales

### Journey / stage dashboard

The progression surface.

- stage distribution of a list at a point in time; progression and regression between two snapshots
- primary actions: compare dates, filter by list/group, drill into stage membership, export stage data to CRM

### Campaign / advertising workspace

The activation surface for account-targeted media.

- creative library, campaign or playbook setup against an account list or group, channel selection (display, video/CTV, social), pacing and budget
- primary actions: launch/pause campaigns, set targeting, review delivery and engagement by account

### Orchestration / workflow canvas

The cross-channel automation surface.

- visual canvas of audience sources, filters, decision nodes, timers, and channel actions (MAP lists, CRM campaigns, sales-engagement sequences, ad audiences)
- primary actions: build/publish a workflow, schedule runs, review run history and errors

### Sales-facing surfaces

Where sellers consume the output.

- in-product alerts and account dashboards; CRM widgets/extensions showing account stage, engagement, and recommended actions
- primary actions: view account signal, log/act on outreach, configure alert preferences

### Reports & analytics

The measurement surface.

- account engagement reports, stage movement, segment/program performance, pipeline and opportunity influence
- primary actions: configure date ranges and filters, schedule reports, export

### Settings & integrations

Administrative surface.

- CRM/MAP connections, field mappings, tracking-tag installation, user roles and permissions, data-source and consent settings

## Important Rules / Behaviors

### The account is the unit; people roll up to it

Targeting decisions, budgets, stages, and reports are defined at the company level. Person-level actions (an email send, a sales call) are attributed upward to the account. This roll-up discipline is what makes "account-based" measurement meaningful.

### Account identification is probabilistic

Attributing anonymous website activity to companies relies on matching infrastructure (IP, cookies, device signals, domain data) against company databases. Match rates are imperfect and are reduced by VPNs, corporate firewalls, and privacy controls. Some products expose match-rate visibility rather than implying deterministic identification. Claims built on identification should be read as coverage estimates, not certainties.

### Dynamic and static lists behave differently

Filter-based lists re-evaluate as data changes — accounts enter and exit automatically. Imported lists hold their membership until edited. Which kind a program targets determines whether the audience drifts with signal changes or stays fixed; products label this explicitly.

### Stage models are configurable, and movement can regress

Journey/buying stages are defined either by the vendor's models or by customer rules over available data sources. Accounts can move backward (regress) as engagement decays or definitions change. Stage-based automations should therefore be designed for re-entry, not one-time progression.

### Activation channels differ in their addressable unit

Advertising can address accounts directly (company-level targeting). Email and sales sequences address people. The bridge is orchestration: account-level triggers select and route people into people-level channels. A consequence is that people-level channels depend on CRM/MAP/SEP integration quality in a way advertising does not.

### The CRM is the commercial system of record

Opportunity and deal state flows from CRM into stage models and revenue reporting; scores, stages, and segment memberships flow outward. Conflicts (duplicate accounts, a contact matching multiple accounts) are resolved by matching and tie-breaker rules that operations teams configure.

### Access is role-differentiated

Marketing users build lists and programs; sales users consume signals and alerts; administrators control integrations, mappings, and permissions. Read-only visibility is common for stakeholders who only need reports.

## Variants

Common shapes of the Type in the market:

- **Advertising-led platforms** — ad-tech heritage; strongest at account-targeted media and engagement measurement; orchestration and sales surfaces built around the advertising loop.
- **Intelligence/predictive-led platforms** — intent data and predictive scoring as the center of gravity; advertising and orchestration act on the model's output.
- **Orchestration-led platforms** — campaign coordination across MAP/CRM/SEP as the center of gravity, with advertising as one channel among several.
- **Suite platforms** — marketing, advertising, sales-intelligence, and data modules sold as one system with shared account semantics.
- **Self-serve / SMB tiers** — simplified onboarding, free or low-cost entry tiers, packaged "playbook" campaigns; the same core loop with less configuration depth.
- **ABM modules inside marketing automation suites** — the same account-centric capabilities shipped as features of a MAP rather than a standalone product; functionally overlapping, structurally a variant of where the capability lives.

A variant remains a variant of this Type as long as the account stays the audience and measurement unit. If a product's center of gravity moves to anonymous-audience advertising or to lead-centric nurture, it has become a neighboring Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Marketing Automation Platform | closest overlap | MAP's primary object is the lead/contact and its nurture campaigns; ABM's primary object is the account. ABM platforms push audiences *into* MAPs rather than replacing them. Remove the account-level unit → MAP |
| Demand-side Platform / Advertising Campaign Management | execution overlap | DSPs target anonymous audiences and optimize media delivery; they lack company-level identity and per-account engagement measurement. Remove account identity and account-level measurement → DSP |
| Sales Intelligence Platform | bundled sibling | Sales intelligence serves sellers (company/contact discovery, outreach context); ABM serves marketing orchestration and account-level measurement. Products often bundle both; the marketing-orchestration side is the ABM Type. Remove activation and marketing measurement → sales intelligence |
| Customer Data Platform | data-layer neighbor | CDPs unify customer identity data into activatable audiences, generally consumer/individual-centric; ABM carries B2B company semantics (fit, stages, buying committees) and account-level measurement |
| Lead Generation / Lead Capture Platform | funnel-adjacent | Lead generation captures demand (forms, content syndication, contact acquisition); ABM orchestrates toward a chosen account set regardless of how individual leads arrive |
| Account Management CRM | record-system neighbor | CRM accounts are the sales system of record; the ABM platform consumes those accounts, adds marketing signal and activation, and writes prioritization back. Remove the marketing loop → account records in CRM |
| Marketing Attribution Platform | measurement overlap | Attribution tools measure touchpoint-to-revenue generically across channels; ABM measurement is account-progression-centric and feeds re-prioritization, not just reporting |

The blurriest boundary is with sales intelligence, because several vendors ship both in one suite; the working test is which side owns the *activation and measurement loop* versus the *discovery and contact-data surface*.

## Representative Products

- **6sense** — predictive/intent-led enterprise platform; segments, predictive buying stages, advertising, orchestration workflows, sales intelligence
- **Demandbase** — suite platform (marketing, advertising, sales, data modules) with buying-group-centric positioning and B2B advertising heritage
- **AdRoll ABM (formerly RollWorks)** — advertising-led platform with self-serve tiers; account lists, journey stages, playbooks, sales insights
- **DemandScience (acquired Terminus)** — demand-generation suite spanning advertising, data, and measurement studios

These four were used because they represent different product philosophies (predictive-led, suite, advertising-led, demand-gen suite) and different customer tiers (enterprise through self-serve SMB).

## Sources

Research date: **2026-09-06**

- 6sense Knowledge Base (support.6sense.com) — Segments Overview; 6sense Scores Overview; Predictive Buying Stages; Account Identification and Enrichment; Compare Audience and Data Workflows and Orchestration; documentation index (llms.txt)
- AdRoll ABM Help Center (help.rollworks.com) — Account Lists Fundamentals; Journey Stages Overview; Advertising category; help-center home
- Demandbase (demandbase.com) — platform home and Marketing (ABM) product page
- DemandScience Help Center (support.demandscience.com) — help-center home and product-line category descriptions

> Sourcing limitation: Demandbase's support/help-center documentation was unreachable from the research environment (repeated transport failures) and DemandScience's article bodies require an authenticated login. Demandbase and DemandScience observations are therefore limited to official product pages and public category descriptions; operational mechanics for those two products are described only where cross-product evidence supports them, and precise vendor-specific details are intentionally omitted. Numeric limits, score bands, and package names observed in vendor documentation were treated as vendor-specific and excluded from this document.
