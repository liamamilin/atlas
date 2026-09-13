# Research Notes — Customer Success Platform

## Research Goal

Understand **Customer Success Platform** as an Application Type: what its defining core is, what objects exist inside it, who operates it, how the post-sale customer relationship is actually managed in these products, and where its boundaries sit against the dense §07 neighbor cluster — especially the four siblings that recorded joint-review flags against this leaf (**Customer Health Monitoring**, **Renewal Management Platform**, **Customer Onboarding Platform**, **Product Usage / Adoption Platform**), plus **CRM**, **Strategic Account Planning Platform**, **Account Management CRM**, and **Customer Service Platform**.

This pass is the joint-review moment for three module-convergence flags recorded by earlier passes (health monitoring, renewal management, onboarding — all shipped as modules inside CS platforms).

## Initial Boundary

Working hypothesis carried in: the Type is the vendor-side platform for operating the post-sale customer relationship as managed workflow across a book of customer accounts — the system of record and the workflow system for the "customer success" practice in recurring-revenue businesses. CSMs are the primary operators.

Known risks going in:

1. **Module-convergence risk (three standing flags)**: health scoring, renewal management, and onboarding all ship inside CS platforms. Each sibling leaf recorded a joint-review flag; this pass must ratify or dissolve.
2. **CRM-dissolution risk**: a CS platform could be judged a post-sale variant of CRM. The CRM pass pre-drew the seam ("post-sale outcome machinery vs relationship of record spanning pre+post sale").
3. **Suite-adjacency**: vendors bundle adjacent products (communities, education, in-app engagement); the Type must not absorb them.

## Research Questions

1. What is the unit of record — account, relationship, customer journey?
2. What does a CSM actually do in the product day-to-day (workflow)?
3. What objects exist: accounts, people, health, usage, success plans, plays/playbooks, tasks/CTAs, lifecycle stages, segments, touchpoints, surveys, renewals?
4. How does customer data get in (CRM, product usage, support, billing integrations)?
5. How do lifecycle stages / journeys work?
6. What is the anatomy of a success plan?
7. How do plays/playbooks trigger and what do they do?
8. How is the whole book operated (segments, portfolio views, reporting, QBRs)?
9. What customer-facing surfaces exist (portals, shared plans)?
10. What roles exist (CSM, manager, ops, admin, viewer) and how do permissions work?
11. What are the boundaries vs the flagged siblings, CRM, service, account planning?
12. Historical check: would pre-software / spreadsheet-era customer success satisfy the definition?

## Representative Products

| Product | Positioning | Segment | Evidence tier |
|---|---|---|---|
| **Gainsight** | enterprise CS suite; the category archetype | enterprise | Tier-1 help center (Features Overview + Success Plan Overview + module category pages + 3 Scorecards articles from the health pass) |
| **Totango** | segment/journey-centric CS platform ("customer data platform for CS" framing) | mid-market | Tier-1 help center (Terminology guide, data objects, SuccessPlays, Workspace, + 4 health articles from the health pass) |
| **Planhat** | data-model-first "customer platform" | upper mid-market/enterprise | Tier-1 help center (glossary + collections + 2 health articles from the health pass) |
| **Catalyst** (Totango-owned) | activity/workflow-centric, CRM-integrated | mid-market | Tier-1 help center (overview, daily-use, automations guide, + health article from the health pass) |
| **ChurnZero** | mid-market CS platform, product-usage-embedded | mid-market | Tier-1 help center at section-listing level (Knowledge Base structure; article-level detail not fetched this pass) |

Rejected/abandoned samples (source-access limitation): **Vitally** (empty responses ×2, matching the health pass), **ClientSuccess** (transport error in the health pass), **HubSpot** (unreachable in the health pass). The SMB pole and the product-experience-infused pole therefore rest on structural reasoning only.

## Sources

- Gainsight — CS Features Overview: https://support.gainsight.com/gainsight_nxt/Getting_Started_for_Admins_and_End_Users/Gainsight_CS_Features_Overview
- Gainsight — Success Plan Overview: https://support.gainsight.com/gainsight_nxt/Success_Plans/About/Success_Plan_Overview
- Gainsight — Success Plans module: https://support.gainsight.com/gainsight_nxt/Success_Plans
- Gainsight — Cockpit and Playbooks module: https://support.gainsight.com/gainsight_nxt/04Cockpit_and_Playbooks
- Gainsight — NXT guide index: https://support.gainsight.com/gainsight_nxt
- Gainsight — Scorecards articles (from the customer-health-monitoring pass): support.gainsight.com Scorecards Overview / Calculation / Use in Rules and Reports
- Totango — Terminology guide: https://support.totango.com/hc/en-us/articles/27045856509460-Terminology-guide
- Totango — Understand data objects: https://support.totango.com/hc/en-us/articles/360043012931-Understand-data-objects
- Totango — Understand SuccessPlays: https://support.totango.com/hc/en-us/articles/205332175-Understand-SuccessPlays
- Totango — Understand Workspace: https://support.totango.com/hc/en-us/articles/204012969-Understand-Workspace
- Totango — health articles (from the health pass): account-level health, multidimensional profiles, best practices, Risk+Health page
- Planhat — Glossary: https://help.planhat.com/en/articles/10346456-planhat-glossary
- Planhat — Help center collections index: https://help.planhat.com/en/
- Planhat — health articles (from the health pass): How Health is Calculated; Health Scores: What You Can Include
- Catalyst — Overview: https://help.catalyst.io/hc/en-us/articles/36171282751380-Catalyst-overview
- Catalyst — Use Catalyst to view or manage customer accounts: https://help.catalyst.io/hc/en-us/articles/28924671873556-Use-Catalyst-to-view-or-manage-customer-accounts
- Catalyst — Build automations: https://help.catalyst.io/hc/en-us/articles/28924639841300-Build-automations-to-help-my-team-protect-and-grow-revenue
- Catalyst — Monitor customer health (from the health pass)
- ChurnZero — Help center Knowledge Base structure: https://support.churnzero.com/hc/en-us (+ Automation / Playbooks / Success Plans / Profiles section listings)

Research date: **2026-09-08**. All fetched pages are official vendor help centers (Tier 1). Fetch failures this pass: Totango "Manage customer success plans" article (403), Catalyst terminology-guide cross-link (404), Catalyst playbooks article cross-link (404), ChurnZero help.churnzero.com host (transport error; support.churnzero.com reachable), Vitally (empty ×2).

## Product A — Gainsight

### Key observations (Layer A unless noted)

- Framing: "The leading CS solution for retention, expansion, and efficiency." The NXT guide index enumerates the module map: 360, Cockpit and Playbooks, Success Plans, Customer Goals, Scorecards, Rules Engine, Journey Orchestrator, Timeline, People Management, Relationships/R360, Renewal Center, Reports and Dashboards, Gainsight Home, Team View, Surveys, Adoption Explorer, Connectors, Data Management, Spaces, Company Intelligence, Product Requests, Text Analytics, AI Assistants (Copilot/Sally/Insight Agent), Mobile, CSQL.
- **C360/R360**: "a central hub of your customer's business information… synthesizes business data from various sources and provides you with a holistic view of your customers. This minimizes the preparation time for your customer meetings." R360 extends the same idea to multi-product **Relationships**.
- **Cockpit**: "the CSM/AM team's home base for viewing and managing key customer activities. The backbone of Cockpit is Gainsight system alerts called Calls to Action (CTA). Call to action types, their associated tasks, and the Cockpit view can be customized by Admins." Playbooks are the reusable content layer behind CTAs.
- **Success Plans** (dedicated module): "define, track, and communicate your customer's strategic goals… a central workspace to align internal teams and customers, track progress through CTAs and tasks." Tabs: Plan Info (owner/status/timeline), Cockpit (CTAs + tasks), Gantt Chart, Timeline. Admin templates standardize plan structure; plan types target different initiatives; plans can be **auto-triggered at lifecycle milestones** ("ensure proper hand-off from one stage to another"); individualized plans per product/department/geography; shareable with customers; comments; API.
- **Customer Goals**: "cross-functional teams collectively capture, track, and measure customer goals… capture goals early to surface them in C360, and allow teams to plan work around goals by connecting to multiple CTAs and Success Plans."
- **Scorecards** (health machinery; from the health pass): measures/groups/overall score, manual or Rules Engine scoring, history objects, CTA creation on score drop.
- **Rules Engine**: multi-step data transformations; the automation backbone (e.g., create CTA when health drops).
- **Journey Orchestrator**: "automated emails… tailored by customer attributes such as health score, product usage, survey results, and lifecycle stage."
- **Timeline**: "your customers' official record… log information regarding customer interactions… track customer interactions over the course of a customer's lifecycle."
- **People Management**: contacts captured in **organizational charts** ("who influences whom").
- **Spaces**: "a secure customer portal that brings CSMs and their customers together in one shared environment to collaborate on… updates, insights, Customer Goals, Success Plans, reports, documents, and notes."
- **Success Snapshots**: generate PowerPoint business-review decks from Gainsight data for **EBRs and QBRs**.
- **Surveys**: multi-page surveys incl. NPS question type.
- **Renewal Center** (add-on module): renewal likelihood score from health/engagement, forecast reviews, late-renewal identification. **CSQL**: CS-generated leads delivered to sales CRM.
- **Adoption Explorer**: manages customer **usage data** at Company/Person level with entitlements, daily/weekly grain, derived fields.
- **Connectors**: out-of-the-box data-source integrations. **Team View**: Gainsight data surfaced inside Salesforce pages for sales/execs (Viewer license).
- **Gainsight Home**: "one-stop workspace for CSMs… centralized view of the insights and action items for your portfolio of customer accounts."
- **Horizon Analytics**: reporting/dashboards ("single source of truth" framing).
- AI: Copilot (natural-language Q&A over customer data), Sally (conversational data access + updates), Insight Agent/Staircase (analyzes emails/meetings/support for relationship health, risks, opportunities), Company Intelligence (external business events), Text Analytics (survey/text sentiment).
- Product Requests: CSMs capture customer product requests in 360 and push to Productboard/Aha.

## Product B — Totango

### Key observations (Layer A)

- Framing: help-center categories: **Daily Use** — "From touchpoints to success plans, manage your portfolio of customer accounts"; **SuccessBLOCs** — "Run customer journey programs using SuccessPlays, campaigns, and more."
- **Data objects**: **Account** ("a representation of a customer entity, such as a business, a division, or even a product"; unique Account ID required; **Status (Contract Status) required — "Totango calculates health and other key metrics for active customers"**; Contract Renewal Date, Contract Start Date, Contract Value (ACV) as core attributes; parent/child hierarchies; product modeling). **User** (person at the customer; Contact/Key Contact flags; Contact Account Role e.g. Champion). **Collections** (transactional tables on the account profile): system collections **Tasks, Touchpoints, Objectives, Campaigns**; custom collections (support tickets, survey data); virtual collections queried live from third-party systems. **Opportunities** (premium reserved account type). **Module usage and activity stream** (usage events: action/module/count per user, aggregated to account).
- **Account assignment**: "explicit naming of team members who work on an account in a formal capacity, known as a team role — Success Managers (CSM), Sales Managers, Onboarding Manager, Executive Sponsor."
- **Touchpoints**: "a record of meaningful engagement related to an account… keep track of important call details, day-to-day processes, and internal communications," categorized by flows/type/reason for reporting.
- **Tasks**: work records with priority, status, assigner/assignee, due date, effort.
- **Workspace / My Portfolio**: "a central location for account-related events… prioritize your daily workflow, see activity from other users or system updates, evaluate health changes, and take action on items that require immediate attention." Activity inbox (health changes, touchpoints, milestones) processed "the same way you would an email inbox"; tasks view; pinned accounts; admin-definable **portfolio scope**.
- **Segments**: saved filtered lists per object (accounts, users, opportunities, touchpoints, tasks, custom collections) with criteria and bulk update; segment **triggers** (enter/exit → add/remove tags, send email).
- **Success plan**: "a documentation tool within an account profile to track customer objectives… provide internal visibility for customer initiatives. Optionally share plan objectives and assign tasks to customers via **Customer Portal**." Customer Portal: "a shared website where your customer contacts can view shared success plan objectives, track the progress in real-time, and complete tasks assigned to them… mutual accountability."
- **SuccessBLOC**: "a ready-to-use toolkit to drive programs within the customer journey (e.g., Onboarding, Renewal, Expansion, Risk)… define, operationalize, and track outcomes for each program." Contents: **SuccessPlays** (automated workflows), **Campaigns** (email), **Scorecards** (KPI modules), **Reports**, **Canvas** (tracks mapping linear/non-linear phases; cards = campaigns or SuccessPlays).
- **SuccessPlay**: "pre-built workflow to automatically assign new internal tasks, update data, celebrate milestones, and more. Customers enter a SuccessPlay based on custom criteria." Event-based (condition-triggered) or manual; actions: create task (dynamic assignees/due dates, post-completion actions), request information (forms), update information, celebrate milestone, notify team, call webhook, create objective.
- **Lifecycle status attributes**: "a classification system to group customers within pre-defined stages… automatically track time between each stage until an 'end stage' is reached. An account can be going through multiple lifecycles… such as in the 'Onboarding' stage of the customer journey and the 'Integration' stage of the onboarding process."
- **Health** (from the health pass): two models (account health rank; multidimensional rank + 0–100 score), profiles scoped by segment with precedence, daily calculation, timelines, portfolio consoles.
- **Governance**: licenses (Practitioner / Contributor / Viewer), roles/permissions (Admin, Regular User, Team Admin, custom), **Teams** (visibility scoping), **Team Pool** (task assignment pools), Data Modeler (attributes, dimensions, custom metrics), employee hierarchy (manager ID).
- Data in: CRM connector, CSV, APIs (JS/HTTP/Data Hub), connectors catalog; usage via activity stream or aggregated import.

## Product C — Planhat

### Key observations (Layer A)

- Framing: data-model-first. "Data is saved in various data models… The Company model is used for all organizations that you deal with (customers or prospects); the End User model is for external people." **Company is the parent model — almost all other models relate to it** (End Users, Licenses, Opportunities, Projects, Conversations, Assets, Churn). Parent/child **group structures** for hierarchies.
- **Health Score**: 0–10 + red/amber/green; configured via **Health Profiles** (rules) composed of **Health Factors**; different profiles per scenario (onboarding phase, SMB post-onboarding). **Success Units**: per-product/feature adoption signs — multiple per Company, each measuring one thing, manual (TBC/Not Applicable/Potential/On) or metric-linked. **CSM Score**: manual sentiment field on Company.
- **Time-series usage data**: **User Activities** (End-User events, e.g. "logged in", streamed in), **Custom Metrics** (other numeric series), transformed via **Calculated Metrics** ("combining time-series data, field data and mathematical operators… can then be used in various places, such as Health Scores").
- **Workflows (formerly Playbooks)**: two types — **Projects** ("designed for project management, displaying tasks in a customizable table — e.g. an Onboarding Project") and **Sequences** ("automatically sending series of emails to End Users, but can also include tasks — e.g. a Welcome Sequence"). **Workflow Templates** applied "automatically or manually… to individual records (e.g. to a specific Company)"; entry/exit criteria via Global Filters.
- **Automations**: "when x happens, do y" with branching/conditions, wait steps, webhooks, function executions; template library + custom flowchart builder; configured in App Center.
- **Conversations**: data model recording interactions — "emails, chats, meetings… 'logged activities'"; system types (chat) and custom types (e.g. "Training Session", "QBR"); **Inbox Pages** display Conversation data across Companies.
- **Portals**: "share information with a customer Company in a secure, branded environment, ensuring that you and your customer are aligned on key information/processes and the value they are getting… collaboration and transparency."
- **Pages** (content system): Data Table, **Board** (kanban; "drag and drop cards between columns — e.g. move Opportunities between Sales Stages"), Dashboard, **Presentation** (slides "for your team or your customers"), Full-Page Profile ("You may hear a Company Full-Page Profile be referred to as a 'Customer 360'"), Inbox; organized in Sections/Views/Libraries; Home Templates per role.
- **Revenue**: License model, Sales/Opportunity, **System Reports**: Revenue Base, Renewal Rate, Bookings, Renewals, Invoices. **Churn model**: "track lost customers/subscriptions and the reasons for churn."
- **Teams / portfolio permissions / Roles** (incl. data-model permissions, workflow permissions); email/calendar sync; Email Automation Provider (bulk sends via SendGrid); **App Center** integrations: CRM (Salesforce, HubSpot), support (Intercom, Zendesk), usage (Pendo, Mixpanel), AI connections; Source ID = CRM record ID.
- NPS survey data; PSA package (Time Entry, Timesheets) as a specialist add-on.

## Product D — Catalyst

### Key observations (Layer A)

- Framing: "the customer growth platform that helps you unify the GTM organization… Evolve your team to stop focusing on activities and instead, deliver impact." Core: **portfolio management** ("monitor all customer health signals, proactively engage at scale, and help customers achieve their goals"), **automations** ("playbooks and expansion signals"), **organization settings**, **data management and integration** ("connect customer data streams, including financial, product usage, support tickets, customer feedback, and more").
- **Daily workflow** (power-user guide): connect email/calendar (engagement module timeline of emails + meetings); navigate home page and object levels; create/manage **segments** and **layouts**; keep data up to date (field-level and bulk updates; add opportunities and contacts) — "These data updates help trigger strategic automation"; document work with **notes, tasks, comments, templates** — "Everything you do is featured on the account **activity stream**"; monitor the **notifications inbox** (incl. approving automated emails); "Lead customers to success… Monitor customer journey progress, track health over time, and take action on expansion signals."
- **Health profiles** (from the health pass): inputs → groups → account; Health/At Risk/Neutral + numeric score; most-impactful-field diagnosis; optional sync to Salesforce.
- **Customer journeys**: "a classification system to group customers according to their stage in defined milestones… Determine which fields at the account and opportunity levels represent specific journeys and stages… for each stage… criteria for how a customer should move through each stage. Once configured, your teams can monitor customer journey progress and prioritize their work."
- **Expansion signals**: "determine what levers (signals) your team uses to drive expansion, and customize signal notifications… take action on expansion signals"; optional sync to Salesforce.
- **Workflows (playbooks)**: "pre-built workflows to automatically assign new tasks, send personalized emails, and update field values… consistent customer experience for common workflows (e.g., renewal, customer escalation, executive business review)." Customers enter "based on custom criteria or journey stages"; actions + logic + a **primary objective**; impact tracked per workflow/action/objective.
- **Customer Hub** (from Totango terminology cross-ref): read-only shared surface for customers.

## Product E — ChurnZero

### Key observations (Layer A at section-listing level; article-level detail not fetched)

- Knowledge Base structure: **Reports** (Renewal and Forecast Hub, dashboards, Live Exports), **Automation** ("automate your workflows with plays, journeys, surveys, and alerts"), **Segments**, **Launchpad**, **Digital Tools** (Success Panels, In-App Messaging, WalkThrough Reports), **Customer Health** ("analyze the health of your customers using ChurnScores and Success Insights"), **Profiles** (profile pages, **Timeline** panel, Notes, Dynamic Slides presentations), **Meetings**, **My Account and Content Templates**.
- **Playbooks**: "how plays empower you to proactively engage with your contacts and accounts at the right time" (concepts / working with plays / play steps).
- **Journeys**: "ChurnZero's account-level project plans."
- **Success Plans**: create + "Collaborate on Success Plans" (sharing).
- Admin KB: integrations, data settings, authentication; Implementation Resources: JS snippets, HTTP APIs, batch uploads (usage ingestion).

## Cross-product Comparison

| Dimension | Gainsight | Totango | Planhat | Catalyst | ChurnZero |
|---|---|---|---|---|---|
| Unit of record | Company (+ Relationship for multi-product) | Account (business/division/product) | Company (parent model) | Account | Account |
| People | Contacts + People Management org charts | Users (Contact/Key Contact/Champion) | End Users | Contacts | Contacts (Profiles) |
| Commercial context on account | Renewal Center (add-on); CSQL | Contract status/value/renewal dates as core attributes | License model + revenue System Reports | Opportunities; financial data streams | Renewal and Forecast Hub |
| Standing success picture | Scorecards (health) + Adoption Explorer (usage) | Health profiles + usage activity stream | Health Score + Success Units + Calculated Metrics | Health profiles + usage/support/feedback streams | ChurnScores + Success Insights |
| Engagement record | Timeline ("customers' official record") | Touchpoints + Timeline | Conversations (emails/chats/meetings/custom types) | Activity stream + engagement module (email/calendar) | Timeline panel + Notes |
| Managed work | Cockpit CTAs + tasks; Playbooks | Tasks; SuccessPlays | Workflow tasks (Projects); Automations | Tasks; workflow actions | Plays + play steps; Alerts |
| Success plan | Success Plans module (objectives as CTAs, Gantt, share, auto-trigger at milestones) | Success plans (objectives; share via Customer Portal) | Projects (workflow) + Pages + Portals | Goals + objectives in workflows; Customer Hub (read-only) | Success Plans (create + collaborate/share) |
| Proactive automation | Rules Engine → CTAs; Journey Orchestrator emails | SuccessPlays + Campaigns + segment triggers | Workflows + Automations | Workflows (entry by criteria/journey stage) | Plays; alerts |
| Lifecycle | Lifecycle stage attribute; plan auto-trigger at milestones | Lifecycle status attributes (time-in-stage, multiple lifecycles) | (phase fields; onboarding Projects) | Customer journeys (milestone stages + criteria) | Journeys (account-level project plans) |
| Portfolio operation | Gainsight Home; Horizon Analytics; segments via reports | My Portfolio/Workspace; Segments; My Business | Home Sections/Views; Data Explorer; dashboards | Home layouts; Segments | Launchpad; Segments; dashboards |
| Customer-facing surface | Spaces portal; shared Success Plans | Customer Portal (shared objectives + customer tasks) | Portals | Customer Hub (read-only) | Shared Success Plans |
| Reviews/decks | Success Snapshots (EBR/QBR PPT) | Automated presentations | Presentation Pages | (EBR named as workflow example) | Dynamic Slides |
| Surveys/feedback | Surveys (NPS); Text Analytics; Product Requests | CSAT/NPS collections; campaigns | NPS data | Customer feedback streams | Surveys |
| Data in | Connectors; Adoption Explorer; APIs | CRM connector, CSV, APIs, activity stream | App Center integrations (CRM/support/usage); APIs | Salesforce + data streams; email/calendar sync | Integrations, JS/HTTP APIs, batch uploads |
| CRM posture | Team View embeds in Salesforce; two-way sync | Accounts auto-created from CRM connector | Source ID = CRM ID; two-way sync | Health/signals synced to Salesforce | CRM sync (renewal pass: two-way opportunity sync) |
| Roles/licenses | Full/Viewer licenses; admin config | Practitioner/Contributor/Viewer; roles; teams | Roles (data-model/workflow/portfolio permissions); teams | Standard access tiers; roles | Admin vs end-user KBs; permissions |
| AI (era-current) | Copilot, Sally, Insight Agent | Unison/Cadence era features | AI overview collection; connections to LLMs | (era-current) | ChurnZero AI (Engagement AI, AI Hub) |

### Cross-product commonalities (Layer B)

1. **The customer account is the unit of record** — the vendor's own customer organizations held as standing records, with attached people (contacts/end users, sometimes with roles like champion and org charts) and commercial context (contract value, renewal/contract dates, status). Account hierarchies (parent/child) are common.
2. **Multi-source aggregation into the account**: CRM, product usage, support, billing/financial, survey/feedback data streams are merged into one customer record — the platform presents itself as the place where disparate customer data becomes "a single source of truth."
3. **A standing per-account success picture**: health machinery (scored, multi-signal, configurable — the health-monitoring core), usage/adoption indicators, engagement recency, journey/lifecycle stage — continuously maintained state telling the team how each customer is doing.
4. **An engagement record**: touchpoints/activities/notes/conversations logged against the account and rendered as a timeline — the relationship's memory.
5. **Managed work on the relationship**: tasks/CTAs with owners, priorities, due dates; success plans holding customer objectives broken into tracked work; plays/playbooks/SuccessPlays/workflows that trigger on conditions (health changes, segment entry, journey stage) and execute multi-step actions (assign tasks, send emails, update data, webhooks).
6. **Lifecycle/journey structure**: accounts classified into stages (onboarding → adoption → renewal…) with stage criteria and time tracking; automation keys off stage transitions.
7. **Portfolio operation at book scale**: saved segments, personal/team workspaces (activity inbox + task queue), portfolio dashboards and reports, review-deck generation (QBR/EBR).
8. **Customer-facing collaboration surfaces**: portals/shared plans where customers see objectives, progress, and sometimes complete assigned tasks — "mutual accountability."
9. **Assigned ownership**: each account has named internal owners in defined roles (CSM/Success Manager, plus sales/onboarding/executive roles); internal teams scope visibility; license tiers (full/contributor/viewer) and admin configuration are universal.
10. **Revenue-motion adjacency**: renewal views/likelihood, expansion signals, CS-generated leads — present as modules or native objects, but as *adjacent* machinery (see Boundaries).
11. **Surveys/feedback capture** (NPS/CSAT) as one input family.
12. **AI assistance** (Q&A over customer data, drafting, conversation intelligence) is era-current across the sample.

## Canonical Model (Layer C — canonical inference)

Three jointly-held structures:

1. **The managed customer book** — the vendor's own post-sale customer relationships held as standing identified accounts (with attached people and commercial context), each under assigned internal ownership, operated as a portfolio rather than one-off records. Remove → a contact store or generic analytics; nothing is being "managed."
2. **The standing customer-success picture per account** — multi-source customer signals (product usage/adoption, engagement, support, sentiment, commercial) continuously aggregated into per-account standing state — health, adoption, engagement, journey stage — that classifies how each customer is doing. Remove → a task tracker with customer names; the "success" premise (knowing how customers are doing at scale) is gone.
3. **The managed relationship work loop** — planned and triggered work on each account (success plans with customer objectives, condition-triggered plays, tasks with owners and due dates, lifecycle stages, logged touchpoints) executed by the assigned team and reviewed across the book, moving accounts through the post-sale lifecycle toward retention and expansion. Remove → health monitoring plus a dashboard; the workflow "platform" is gone.

Jointly-held is load-bearing: (1) alone = account list/CRM-lite; (2) without (1) = signal analytics (usage-platform/health-monitoring territory); (3) without (2) = blind task management; (1)+(2) without (3) = Customer Health Monitoring + CRM (watching without managed work); (1)+(3) without (2) = CRM with tasks (working blind); (2)+(3) without (1) = generic workflow automation over event streams.

## L0 / L1 / L2 / L3

### L0 — Defining Invariant

- the managed customer book (vendor's own post-sale customer accounts + people + commercial context, assigned ownership, operated as a portfolio)
- the standing customer-success picture per account (multi-signal aggregation into maintained per-account state: health/adoption/engagement/journey stage)
- the managed relationship work loop (success plans + plays + tasks + lifecycle stages + logged engagement, executed by the assigned team and reviewed across the book)

### L1 — Common Mature Structure

- health machinery (configurable multi-signal scores/ranks with history) — the embedded health-monitoring core
- usage/adoption analytics at account level (activity streams, calculated metrics, license utilization, entitlements)
- success plans with objectives/milestones, Gantt/timeline views, templates, per-segment plan types, sharing
- plays/playbooks/SuccessPlays/workflows: condition-triggered multi-step automation (tasks with dynamic assignment, emails, data updates, webhooks, milestones)
- lifecycle stages/journeys with stage criteria and time-in-stage tracking
- segments (saved filtered lists per object) with bulk actions and enter/exit triggers
- touchpoint/activity logging with account timeline; notes; meetings
- people management (contacts, key-contact/champion flags, org charts)
- portfolio dashboards/reports; QBR/EBR deck generation
- customer-facing portals / shared plans / read-only hubs
- surveys (NPS/CSAT) capture
- CRM two-way sync + integration catalog (support, billing, product usage)
- roles/licenses/permissions; teams; admin configuration layer (data modeler, health/automation builders)
- renewal/expansion adjacency surfaces (renewal likelihood views, expansion signals, CS-generated leads)
- AI assistance (Q&A, drafting, conversation intelligence) — era-current

### L2 — Variant / Optional

- segment-motion packaging: high-touch CSM-led vs digital/low-touch automation-led vs hybrid
- in-app digital tools (success panels inside the customer's product UI, in-app messaging, walkthroughs)
- service-delivery/PSA modules (time entries, timesheets) in some products
- conversation intelligence / external company intelligence as signal multipliers
- through-partner customer success (partners operate CS on the vendor's behalf)
- communities/education/advocacy adjacency (usually separate products in the same vendor suite)
- deployment posture: standalone platform vs CRM-embedded widgets vs suite module
- revenue-module depth: light renewal views vs full renewal-management modules
- B2C-flavored deployments; vertical tunings

### L3 — Vendor-specific (research notes only)

- Gainsight: Cockpit/CTA type customization, Rules Engine, Journey Orchestrator, Spaces, Success Snapshots, Customer Goals object, C360/R360 split, Adoption Explorer, Renewal Center add-on licensing, CSQL, Sally/Copilot/Insight Agent (Staircase), Company Intelligence, Product Requests (Productboard/Aha), Sightline Vault, Team View, Text Analytics add-on
- Totango: SuccessBLOC/SuccessPlay/Campaign/Canvas vocabulary, Team Pool, Practitioner/Contributor/Viewer licenses, My Business pages, two health models, Data Modeler/dimensions, contract-status-required design, virtual collections
- Planhat: data-model-first architecture (Company as parent model), Workflows=Projects+Sequences (Playbook renamed), Success Units, CSM Score, Calculated/Custom Metrics/User Activities time-series stack, Pages system (Data Table/Board/Dashboard/Presentation/Inbox), System Reports (Revenue Base/Renewal Rate/Bookings/Renewals/Invoices), Churn model, App Center, PSA package
- Catalyst: journeys (milestone criteria at account/opportunity level), expansion signals, workflow objectives + impact tracking, notifications inbox with email approvals, engagement module (email/calendar sync), Customer Hub read-only
- ChurnZero: plays/play steps, journeys as account-level project plans, Launchpad, Digital Tools (Success Panels/In-App Messaging/WalkThroughs), ChurnScores, Dynamic Slides, Renewal and Forecast Hub

## Vendor-specific Findings

See L3. None promoted to the canonical document except as neutral structural examples. Notable market-structure facts: Catalyst is now Totango-owned (both help centers share the Totango footer; Totango's terminology guide cross-references Catalyst terms) — a consolidation data point, not a structural one.

## Rejected Findings

- **"A CS platform is a CRM variant."** Rejected as identity. The CRM holds the relationship of record spanning pre+post sale with deal progression; the CS platform's center is post-sale outcome machinery (standing success picture + managed relationship work). Every sampled product treats the CRM as a data substrate (accounts auto-created from CRM; Source ID = CRM ID; health/signals synced back), not as the same system.
- **"Health scoring defines the Type."** Rejected. Health is one standing signal among several; removing it leaves a functioning CS platform (usage, support, engagement, commercial signals). Health monitoring is a distinct center of gravity (ratified below).
- **"Renewal management defines the Type."** Rejected. Renewal modules ship inside CS platforms with distinct objects/licensing/roles; the CS core stands without them.
- **"Success plans are account plans."** Rejected as identity; shared plan anatomy (goals + actions + reviews), different center of gravity (customer outcome realization across the base vs vendor-side growth planning of a named relationship).
- **"The Type requires SaaS/ARR vocabulary."** Rejected. The abstract core (book + standing picture + work loop) holds for any recurring post-sale relationship; spreadsheet-era and pre-SaaS account management satisfy it.
- **"Customer-facing portals define the Type."** Rejected to L1: portals are the modern realization of customer collaboration; the work loop functions without them (and historically did).

## Boundary Findings

1. **vs Customer Health Monitoring (joint-review flag — RATIFIED keep-both).** From this side: remove the health measure → the CS platform still functions on usage, support, engagement, and commercial signals (every sampled product treats health as one configurable signal family among several; Totango computes "health and other key metrics"; Planhat separates Health Scores from Success Units and CSM Score; Catalyst separates health profiles from journeys and expansion signals). Remove the CS workflow (plans, plays, tasks, lifecycle, portfolio operation) → the health measure + monitoring loop still stands (the health pass's test). Seam: the health measure + monitoring loop vs the managed relationship workflow that consumes health among many signals. Module-convergence acknowledged (health machinery ships inside CS platforms), but the center of gravity differs; keep-both ratified from both directions.
2. **vs Renewal Management Platform (joint-review flag — RATIFIED keep-both).** From this side: the CS platform centers the ongoing relationship at any lifecycle point; renewal machinery in the sample is packaged as separable modules with their own objects and licensing (Gainsight Renewal Center add-on; Totango renewals SuccessBLOC; ChurnZero Renewal and Forecast Hub; Planhat Renewals System Report). A CS platform without renewal-decision machinery is still fully a CS platform; a renewal tool needs no full CS stack. Seam: ongoing managed relationship vs the renewal decision event + forward renewal book. Keep-both ratified.
3. **vs Customer Onboarding Platform (joint-review flag — RATIFIED keep-both).** From this side: onboarding appears inside CS platforms as a lifecycle stage plus program toolkit (Totango SuccessBLOC "Onboarding"; Gainsight plan auto-trigger at lifecycle milestones; Planhat Onboarding Projects), but the unit of record differs — the per-customer transition engagement ending at first value vs the ongoing account relationship across the whole lifecycle. A distinct onboarding product family exists (per the onboarding pass). Keep-both ratified.
4. **vs Product Usage / Adoption Platform.** Measurement vs managed customer workflow. CS platforms integrate usage platforms as data sources (Planhat App Center lists Pendo/Mixpanel integrations; Totango activity streams accept third-party behavioral tools; Gainsight PX objects sync into CS objects per the usage pass). Remove usage capture → the CS platform still functions on other signals; remove the CS workflow → the usage platform still functions for product teams. Keep-both.
5. **vs CRM.** The CRM is the relationship of record spanning pre+post sale with deal progression; the CS platform is post-sale outcome machinery layered over account data that typically originates in the CRM (Totango: "most Totango customers create new accounts automatically from CRM connector"; Planhat Source ID = CRM ID; Gainsight Team View embeds in Salesforce; Catalyst syncs health/signals to Salesforce). Keep-both; complementary substrate.
6. **vs Strategic Account Planning Platform.** Naming collision only: "success plans" share the plan anatomy (customer goals + actions + reviews) with account plans, and one sampled vendor markets "prescriptive account plans." Seam = center of gravity: CS plans the customer's outcome realization (adoption/health/renewal) across the whole customer base, operated by CSMs; account planning plans the vendor's growth of a named relationship, operated by the account team. Keep-both; no drift action needed.
7. **vs Customer Service Platform.** Different loop: issue resolution (case of record, agent workspace) vs outcome realization (relationship work loop). Support tickets appear in CS platforms as an input signal family (Catalyst data streams; Totango custom collections; Planhat Zendesk/Intercom integrations), not as the unit of record.
8. **vs Account Management CRM.** The account-management CRM centers the standing customer-organization record with ongoing-stewardship emphasis; the CS platform adds the outcome machinery (standing success picture + plays/plans/lifecycle). Consistent with the account-management pass's seam.
9. **vs Customer Training / Academy, Voice of Customer, Customer Feedback Management, Customer Advocacy.** Adjacent signal/program surfaces; training content, survey programs, feedback pipelines, and advocacy motions may feed the CS platform but are distinct centers (each has its own directory leaf).

**"去掉什么就变成另一个 Type" 判据**：去掉 managed work loop（只看信号）→ Customer Health Monitoring + usage analytics；去掉 standing success picture（只管任务）→ CRM/任务管理；去掉 customer book（只跑工作流）→ 通用工作流自动化；去掉 post-sale frame（回到成交前）→ CRM/销售管道；把尺度缩到单客户过渡 → Customer Onboarding Platform；把焦点缩到续约决策事件 → Renewal Management Platform；把焦点缩到健康测量 → Customer Health Monitoring；把焦点缩到使用量测量 → Product Usage / Adoption Platform。

## Historical / Market-Sample Check

- Spreadsheet-era customer success: an account book (spreadsheet of customers with owners, contract values, renewal dates), a standing picture (columns for usage, open tickets, NPS, last contact, RAG status), and a work loop (per-account success plans, QBR decks, task lists, renewal prep, weekly book review). All three L0 legs present with zero software. ✓
- Pre-SaaS account management (maintenance contracts, key-account binders with meeting logs and review cadences): book + picture (service history, meeting notes) + loop (account plans, regular reviews). Fits the abstract core; no SaaS vocabulary required. ✓
- Modern additions — cloud, health-score UIs, plays, portals, AI — are all L1/era-current, not definitional. ✓

## Uncertainties

1. **Vitally unreachable** (empty responses ×2 across passes): the product-experience-infused CS pole is unverified; assertion strength for that variant reduced accordingly.
2. **ChurnZero evidence is section-listing level** (Tier 1 structure, no article-level detail this pass); its renewal-module detail comes from the renewal pass.
3. **Totango success-plan article 403'd** this pass; the success-plan anatomy rests on the Terminology guide (Tier 1) plus the Customer Portal definition.
4. **Suite-embedded pole** (CRM-suite-native CS modules, e.g. a first-party CRM vendor's CS add-on) not directly verified; Salesforce help unreachable in prior passes. Held as a variant on structural grounds only.
5. **Exact license tiers, numeric limits, cadences** deliberately not asserted; product-specific facts stay in these notes.
6. **Market consolidation** (Totango–Catalyst) observed but not analyzed; does not affect the Type definition.

## Final Synthesis

A Customer Success Platform is the vendor-side platform for operating post-sale customer relationships as managed workflow across a book of accounts. Its defining core is three jointly-held structures: the managed customer book (the vendor's own customers as standing identified accounts with people and commercial context, under assigned ownership, operated as a portfolio); the standing customer-success picture per account (multi-source signals — usage/adoption, engagement, support, sentiment, commercial — continuously aggregated into maintained per-account state: health, adoption, engagement, journey stage); and the managed relationship work loop (success plans holding customer objectives, condition-triggered plays, tasks with owners and due dates, lifecycle stages, logged touchpoints — executed by the assigned team and reviewed across the book, moving accounts toward retention and expansion). Around that core, mature products add health machinery, usage analytics, play automation, segments, portfolio dashboards, QBR deck generation, customer portals, surveys, CRM/integration substrate, role/license governance, and AI assistance. The Type sits deliberately among siblings it hosts as modules or consumes as signals: health monitoring (the signal core), renewal management (the decision event), onboarding (the transition engagement), usage platforms (the measurement layer), CRM (the record substrate) — all four joint-review flags ratified as keep-both with center-of-gravity seams. The historical check confirms the core predates the modern packaging: a spreadsheet account book with RAG columns, QBR decks, and task lists is already this Type.
