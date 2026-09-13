# Research Notes — Customer Relationship Management / CRM

## Research Goal

Understand the general-purpose CRM as an Application Type: what objects its world is built from, how a prospect becomes a customer inside it, what users actually do day to day, which rules govern the records, and where its boundary sits against the many neighboring sales/customer Types (including the sibling leaf Account Management CRM, whose pass flagged a joint review with this one).

## Initial Boundary

Working hypothesis before research:

- CRM = the selling organization's shared system of record for its customer and prospect relationships: person/organization records, interaction history, and deal progression through a pipeline.
- Nearest neighbors: Account Management CRM (§07 sibling), Lead Management Platform, Sales Pipeline Management / Opportunity Management, Sales Engagement Platform, Customer Success Platform, Marketing Automation Platform (processed), Help Desk / Customer Service Platform, Sales Prospecting / Intelligence / Enrichment (data supply), domain CRMs (Nonprofit/Donor, Constituent, Creator, Real Estate Brokerage — all recorded in STATUS as family instantiations).
- Expected confusion: "CRM" is used by the market as a family label; the leaf must define the general Type whose center of gravity is the acquisition-to-close selling motion, distinct from account-stewardship-centric siblings.

## Research Questions

1. What are the core records (people, organizations, deals) and how do they relate?
2. How does a prospect enter the system and become a customer (lead → qualification → deal → won)?
3. What is the deal/pipeline model: stages, ownership, amounts, close outcomes, forecasting?
4. How is interaction/activity history attached to records, and how much is auto-captured?
5. What ownership/permission machinery governs shared records?
6. How do duplicates, merges, and record lifecycle (active/inactive) work?
7. What differs between the enterprise platform pole, the inbound freemium pole, the modular SMB pole, and the pipeline-first pole?
8. Where exactly is the seam to Account Management CRM (the flagged joint review)?
9. Historical check: does the pre-SFA (paper/pre-software) sales office satisfy the definition?

## Representative Products

Selected for market representativeness, distinct product philosophy, and distinct customer tier:

| Product | Pole | Why selected |
|---|---|---|
| Salesforce (Sales Cloud) | enterprise platform CRM | market-canonical CRM; attempted as enterprise pole |
| Microsoft Dynamics 365 Sales / Dataverse | enterprise platform CRM (second pole) | Tier-1 entity documentation reachable; carries enterprise semantics |
| HubSpot CRM | inbound / contact-centric freemium | Tier-1 developer docs reachable; documents the full object model openly |
| Pipedrive | pipeline-first minimal sales CRM | distinct product philosophy (deal/activity-driven selling) |
| Zoho CRM | modular SMB/mid-market | attempted for SMB modular pole |

## Sources

Fetched 2026-09-08:

- HubSpot Developers — "Understanding the CRM APIs" (Tier 1): https://developers.hubspot.com/docs/api/crm/understanding-the-crm
- HubSpot Developers — "Pipelines API guide" (Tier 1): https://developers.hubspot.com/docs/api-reference/latest/crm/pipelines/guide
- Microsoft Learn — Dataverse "Account table/entity reference" (Tier 1): https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/account
- Pipedrive — "Sales pipeline management" product page (Tier 2): https://www.pipedrive.com/en/features/sales-pipeline

Unreachable, abandoned after repeated failures per network rules:

- Salesforce Help (JS/CSS error) and Salesforce Developer Docs (403) — matches the account-management-crm pass's finding from 2026-09-07; Salesforce therefore contributes structural presence only, no product-specific claims this pass.
- Zoho CRM user guide / features / developer docs (404 ×2 paths; abandoned) — Zoho treated as structural SMB-modular pole, no direct claims.
- Dataverse Opportunity entity reference (404 ×2 path variants) — deal-side semantics carried by HubSpot (Tier 1) + Pipedrive (Tier 2) instead; Dynamics deal-side claims limited to what the Account entity reference directly shows (StageId/ProcessId/TraversedPath business-process fields, currency fields).
- Pipedrive support article path 404; Pipedrive evidence is the Tier-2 product page only — claims from it are worded accordingly.

## Product A — HubSpot CRM (Tier 1, direct observation)

### Key observations

- HubSpot defines its CRM as "a database of your business relationships and processes", organized into **objects** ("types of relationships or processes"), **records** (instances), **properties** (fields), and **associations** (relationships between records).
- Canonical objects (direct): **Contacts** ("stores information about an individual person"), **Companies** ("stores information about a business or organization"), **Deals** ("represent sales opportunities and transactions, tracked through pipeline stages"), **Tickets** ("customer requests for help or support, tracked through pipeline statuses"), **Leads** ("represent potential customers who have shown interest in your products or services"), plus products, line items, quotes, invoices, and **custom objects** (schema-defined).
- **Activities/engagements** are a documented activity family attached to records: calls, emails, meetings, notes, tasks, communications (SMS/LinkedIn/WhatsApp), postal mail.
- **Associations** connect records: multiple contacts ↔ company; company and relevant contacts ↔ deal; custom labeled association types (their example: "Decision Maker").
- **Unique identifiers & deduplication**: each record gets a record ID; contacts have email as an additional unique identifier; companies have domain; deduplication is documented in their KB.
- **Pipelines** (Tier 1, second doc): "a pipeline is where records are tracked through stages… sales pipelines can be used to predict revenue and identify roadblocks". Multiple pipelines per object (their example: one for *New Sales*, another for *Contract Renewals*). Stage labels are customer-defined; **each deal stage must carry a probability** (0.0 = Closed Lost, 1.0 = Closed Won); stage metadata includes an `isClosed` flag; pipelines have an audit trail; deleting a pipeline is blocked while records reference its stages.
- **Users/permissions**: Users object; pipeline metadata carries `writePermissions: CRM_PERMISSIONS_ENFORCEMENT`; subscription-gated capabilities exist (plan-dependent).
- CRM is one part of a wider suite: the same object model serves service (tickets), marketing events, commerce (orders, invoices, payments) — the Type's machinery is reused by adjacent Types.

## Product B — Microsoft Dynamics 365 Sales / Dataverse (Tier 1, direct observation)

### Key observations

- **Account** entity defined as: "Business that represents a customer or potential customer. The company that is billed in business transactions." — i.e., the organization record spans prospects through customers and is the billing anchor.
- **Ownership model**: `OwnershipType: UserOwned`; message set includes **Assign** (transfer ownership via `ownerid`), **GrantAccess / ModifyAccess / RevokeAccess** (record-level sharing machinery), **RetrievePrincipalAccess** — direct evidence that relationship records are owned, shareable, permission-checked organizational records.
- **Merge** message exists for the Account table — duplicate consolidation is platform machinery.
- **Hierarchy**: `ParentAccountId` (parent–child account hierarchies); **PrimaryContactId** links the account to a contact.
- **Relationship typing**: `CustomerTypeCode` ("Relationship Type") enumerates customer/prospect/partner/reseller/supplier/vendor/competitor/investor/press — the account record is polymorphic over relationship kinds, not just "current customer".
- **Lifecycle/state**: `StateCode`/`StatusCode` (active/inactive semantics), plus `StageId`, `ProcessId`, `TraversedPath` — business-process (stage) machinery attaches to records.
- Commercial profile fields on the account: credit limit, credit-on-hold, payment terms, revenue, employee count, industry, ticker; **contact-preference flags** (DoNotEmail, DoNotPhone, DoNotBulkEmail, DoNotPostalMail, DoNotSendMM) — suppression/consent-like contact governance at record level.
- Multi-currency (`TransactionCurrencyId`), address sub-structures, marketing-campaign linkage (`LastUsedInCampaign`) — the record is a hub for cross-department use.

## Product C — Pipedrive (Tier 2 product page, direct observation)

### Key observations

- Self-describes as "a Web-based Sales CRM"; its product philosophy centers the **visual deal pipeline**: "Pipeline management means staying on top of every opportunity as it moves through your sales cycle, from first contact to close."
- Pipeline stages are **customizable to the team's sales process** ("customize your pipeline with stages that match how your team sells"); multiple custom pipelines are supported; Kanban board with drag-and-drop moving of deals; list and dashboard views over the same data.
- **Activities are tied to deals**: "assign next steps to each stage, so reps know exactly what to do"; activity calendar; automation can trigger on stage changes ("trigger actions when deals reach certain stages").
- **Forecast view**: deals due to close this month / next month (customer testimonial describing forecast usage; the product page confirms forecasting intent: "reports that turn pipeline data into actionable insights… sales forecasting", win rate, conversion rates).
- **Contacts** as the person layer; **email sync/integration** pulling "all of the client's details in"; mobile CRM app; permissions/visibility management ("security and permissions management").
- **Lead capture add-on** (LeadBooster): prospecting database, chatbot, live chat, web forms feeding leads into the CRM — lead capture/prospecting is packaged as an add-on, not the core.
- Note: Pipedrive's support-knowledge-base path was unreachable; operational detail (exact behaviors) is therefore not asserted from this product beyond the Tier-2 page.

## Product D — Salesforce (structural presence only)

- Both official documentation surfaces attempted (Help: JS/CSS render error; Developer Docs: 403) — no direct evidence obtainable this pass, consistent with the sibling account-management-crm pass (2026-09-07).
- Salesforce is treated as the market-canonical enterprise CRM for naming purposes only. No product-specific claims from this pass derive from it, and none were filled from memory.

## Product E — Zoho CRM (structural presence only)

- User guide, features page, and developer docs paths all 404/abandoned. Treated as the SMB modular pole structurally; no claims.

## Cross-product Comparison

| Dimension | HubSpot (T1) | Dynamics/Dataverse (T1) | Pipedrive (T2) | Commonality |
|---|---|---|---|---|
| Person-level records | Contacts ("individual person"), email as unique identifier | Contact entity exists (Account references PrimaryContactId) | Contacts | Universal (A) |
| Organization-level records | Companies ("business or organization"), domain unique ID | Account = "customer or potential customer… billed company" | marketed via customizable CRM (not detailed on fetched page) | Present in both Tier-1 poles; org record is the family's standing spine (B) |
| Deal/opportunity | Deals object, "tracked through pipeline stages" | Opportunity entity is platform-standard (not directly fetched); Account carries StageId/ProcessId/TraversedPath stage machinery | Deal pipeline is the product's center | Universal (A/B) |
| Pipeline stages | Customer-defined labels; per-stage probability; isClosed flag; audit trail | stage fields on records; process flows | customizable stages; drag-and-drop board | Stage model customer-configurable; won/lost terminal states (B) |
| Activities/history | engagements: calls/emails/meetings/notes/tasks/communications | campaign linkage fields visible; activity machinery platform-standard (not directly fetched) | activities tied to deals; activity calendar | Universal as concept (A/B); auto-capture depth varies |
| Ownership & permissions | Users object; write-permission enforcement metadata | UserOwned; Assign; GrantAccess/ModifyAccess/RevokeAccess | permissions/visibility management marketed | Universal (A) |
| Duplicates/merge | record IDs + unique identifiers + documented deduplication | Merge message | not evidenced this pass | Common (A/B) |
| Relationship typing | associations with labels ("Decision Maker") | CustomerTypeCode (customer/prospect/partner/…) | — | Common (A) |
| Hierarchy | — | ParentAccountId | — | Platform-pole structure (A, single-product) |
| Contact governance | — | DoNotEmail/DoNotPhone/etc. flags | — | Common concept, single-product direct evidence (A) |
| Forecasting | "predict revenue" via sales pipelines | — | forecast view; forecasting in reports | Common (A/B) |
| Suite adjacency | tickets/marketing/commerce share the same object model | Dataverse is a platform shared with ERP/other apps | add-ons (lead capture, email marketing) | CRM machinery is embedded in wider suites everywhere (B) |

## Canonical Model

```text
Selling organization
└── Relationship records of record
    ├── Person records (contacts)
    ├── Organization records (accounts/companies)
    │   └── associations bind persons ↔ organizations ↔ deals (labeled roles)
    ├── cumulative interaction history (activities/timeline) on every record
    └── shared working: ownership, assignment, permission-scoped visibility, dedup/merge
        └── managed commercial progression
            └── Deal/opportunity (value, owner, expected close)
                └── Pipeline = ordered customer-defined stages
                    └── open stages → closed-won / closed-lost (forecast basis)
```

## Abstraction Levels

### Level 0 — Defining Invariant (deliberately minimal)

1. **The relationship records of record** — persistent, individually identified records for the people and organizations with which the selling organization has or pursues commercial relationships, held as shared organizational records (owned, permission-scoped), not as personal address-book entries. Remove → contact directory / personal address book.
2. **The cumulative interaction history attached to those records** — recorded touches (calls, emails, meetings, notes, tasks) forming the relationship's durable memory that survives personnel change. Remove → address book / inbox with no relationship memory.
3. **The managed commercial progression** — deals/opportunities as trackable potential outcomes (value, owner, stage) moving through configurable pipeline stages toward closed-won/closed-lost, connecting the relationship records to the organization's revenue motion. Remove → contact/account book or a bare pipeline board.

Jointly-held is load-bearing: 1 alone = directory; 2 without 1 = inbox/calendar/notes; 3 without 1–2 = pipeline board over anonymous deals; 1+2 without 3 = contact/account book (Account Management CRM's center or a contact manager); 1+3 without 2 = lead tracker with no relationship memory.

Evidence basis: three structures directly observed at Tier 1 (HubSpot objects/engagements/pipelines; Dataverse account + ownership/merge machinery), cross-confirmed by Pipedrive (Tier 2). The workflow's own CRM example (relationship records → associations → activity/history → commercial workflow) matches.

### Level 1 — Common Mature Structure

- prospect intake & qualification path (lead handling — implementations differ: dedicated lead object vs lifecycle stage on the person record vs lead inbox)
- duplicate detection and merge
- record ownership + reassignment; role/team/permission-scoped visibility
- email integration (log to record, templates); task/activity management with due dates
- list/table views with filters and saved views; pipeline kanban board; record detail page with timeline + related lists
- forecasting roll-up from open deals (stage probability in some products)
- reports/dashboards; custom fields; global search; notes/files; mobile app; API

### Level 2 — Variant / Optional Structure

- custom objects and platform extensibility (enterprise pole)
- quotes/products/line items, CPQ adjacency; billing/order handoff to ERP
- workflow automation rules; territories; team structures
- AI assistance (era-current: summaries, next-step suggestions, AI agents)
- marketing/service/commerce modules riding the same object model (suite packaging)
- deployment: SaaS-dominant today; on-prem/self-hosted historical/regional
- vertical/industry instantiations (real estate brokerage, nonprofit donor, creator, constituent — sibling Types in the directory)

### Level 3 — Vendor-specific (research notes only; not for the final document)

- HubSpot: numeric object type IDs (0-1 contacts, 0-2 companies, 0-3 deals); per-stage probability required on deals (0.0–1.0); stage-count limits (30/100 by object); portal IDs; subscription-gated pipelines; `CRM_PERMISSIONS_ENFORCEMENT` metadata.
- Dataverse: full field catalog (CreditLimit, SIC, YomiName, MarketCap…); message-level API surface (AssignRequest etc.); adx_/msa_ extension fields.
- Pipedrive: LeadBooster packaging; "100,000+ companies in 179 countries" marketing claim; 400M-profile prospector database claim.
- Salesforce: none asserted (unreachable).

## Vendor-specific Findings

- HubSpot is the sampled product that requires win-probability metadata on every deal stage; stage probability is best written as a common forecasting implementation, not a universal rule.
- Dataverse uniquely (in this sample) documents account hierarchies (ParentAccountId) and billing-anchor framing ("the company that is billed") in its entity definition.
- Pipedrive is the only sampled product whose identity is pipeline-first (deal board as the home surface); HubSpot's home surface is the contact/company record; this is a philosophy difference within one Type, not two Types.

## Boundary Findings

1. **vs Account Management CRM (§07 sibling — joint-review flag from that pass discharged here)**: same CRM family; the four account-management sampled products are recognizably CRMs with accounts as one canonical object. Adopted seam: **center of gravity**. Generic CRM: acquisition-to-close selling motion — person records + deal progression are the working center; the standing account is one structure among several. Account Management CRM: the standing customer-organization record as the organizing spine, with ongoing-stewardship emphasis; deal machinery present but secondary. Keep-both ratified from this side; the leaf pair is a center-of-gravity split within one family, not disjoint machinery. (Cross-checked: HubSpot's own docs present companies and deals as sibling objects in one database; the seam cannot be object-level.)
2. **vs Lead Management Platform**: lead management centers the transient pre-qualification population; CRM holds the full prospect→customer relationship of record. In CRM the lead path is an intake mechanism whose implementation varies (lead object / lifecycle stage / lead inbox) — the implementation split (HubSpot lifecycle vs Salesforce-style lead object) is documented and confirms lead-object is NOT definitional.
3. **vs Sales Pipeline Management / Opportunity Management**: those center the deal and its board; in CRM the pipeline is one structure over the relationship record. Remove relationship records (people/orgs/history) and keep only deals → pipeline management territory.
4. **vs Sales Engagement Platform**: execution of outreach (sequences, dialers, tracking) vs the system of record the execution writes back into. CRM products commonly ship lighter outreach features; the record, not the send, is the center.
5. **vs Customer Success Platform**: post-sale adoption/health/renewal machinery (telemetry, health scores, playbooks) vs the relationship system of record spanning pre- and post-sale. A CRM can hold post-sale relationships without health/telemetry machinery.
6. **vs Marketing Automation Platform (processed 2026-09-08)**: MA centers the reusable automated program + per-contact program execution over its own consented person database; CRM centers the shared selling record + deal progression. Person records are the shared seam; each pass has documented the other's center from its own side.
7. **vs Help Desk / Customer Service Platform**: HubSpot's own docs show tickets tracked through their own pipelines — the same stage machinery serves the service job. The CRM Type is defined by the commercial-relationship job (prospect→customer→ongoing commercial relationship), not by the pipeline primitive itself.
8. **vs Sales Prospecting / Contact Discovery / Data Enrichment**: those supply data INTO the CRM record; the CRM stewards the record. Pipedrive packaging lead capture as an add-on supports the seam.
9. **vs Domain CRMs (Nonprofit/Donor, Constituent, Creator, Real Estate Brokerage)**: family instantiations — person-centric records + interaction history + progression toward domain outcomes (donations, service delivery, audience→payer, property transactions), usually without the account/deal machinery. This pass records the family shape and claims the general commercial-sales usage of the term.
10. **Historical check**: the pre-software sales office satisfies the core — card file/Rolodex of person records + client folders (organization records) + correspondence/meeting log + a forecast/sales ledger or pipeline board worked by the office, with accounts assigned to salesmen. Early 1990s SFA software (contacts, accounts, activities, opportunities, forecast reports) satisfies it without cloud/AI/custom objects. Single-seat contact managers satisfy the record+history+progression legs with the shared-organizational leg carried by the organization's possession of the records (ownership machinery is L1, organizational possession is conceptual).

## Uncertainties

- Salesforce and Zoho contributed no direct evidence this pass (both official documentation surfaces unreachable); the SMB-modular pole (Zoho) and the market-canonical platform (Salesforce) are asserted structurally only. Definition is triangulated from two Tier-1 poles + one Tier-2 pole; risk of over-fitting to the HubSpot/Dataverse shape is mitigated by the Pipedrive philosophy counter-pole and the historical check.
- Dynamics-side deal semantics (opportunity entity) not directly fetched; deal-side claims rest on HubSpot (T1) + Pipedrive (T2) + generic stage fields observed on the Dataverse Account entity.
- Pipedrive operational detail (support KB) unfetched; no operational rules asserted from it.
- Whether every modern CRM retains a distinct "account" object (vs person-only models like early lightweight CRMs) is only partially evidenced; the abstract "person + organization records" phrasing is used precisely to avoid over-fitting.
- Auto-capture depth (email/calendar sync writing activities automatically) is widely marketed; direct Tier-1 documentation of the mechanism was not fetched this pass — kept as "common" with moderate wording.

## Final Synthesis

A CRM is the selling organization's shared system of record for its customer and prospect relationships. Its world is built from person records and organization records bound by labeled associations, a cumulative interaction history attached to every record, and managed commercial progression: deals with value and owner moving through customer-defined pipeline stages toward closed-won/closed-lost. Ownership, permission-scoped visibility, and duplicate/merge machinery make the records organizational rather than personal. Everything else widely associated with CRMs — lead objects, forecasting, email integration, custom objects, AI, suite modules — is mature-but-not-definitional. The defining core is small enough that the paper-era sales office satisfies it, while the center of gravity (acquisition-to-close selling over shared relationship records) separates it from Account Management CRM (standing stewardship), Lead Management (transient prospects), Sales Pipeline Management (deal-only), Sales Engagement (execution), and Customer Success (post-sale outcome machinery).
