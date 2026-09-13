# Research Notes — Data Exchange Platform

Research date: 2026-09-07

## Research Goal

Understand, from real products, what a **Data Exchange Platform** actually is: the core objects it manages, how a data provider publishes an offering, how a consumer gains and keeps access, how data is delivered and updated, what governance exists on both sides, and where the boundary lies with neighboring data-family Types (Managed File Transfer, EDI Platform, Data Catalog, Data Integration Platform, Data Replication Platform, open-data portals).

## Initial Boundary (hypothesis before research)

- Core use: organizations share/govern data **with other organizations** as a standing relationship — one side publishes data, the other side is entitled to consume it.
- Likely users: data provider engineers/admins; data consumer engineers/analysts.
- Likely confusion neighbors: ETL/Data Integration (intra-org movement), MFT (file movement), EDI (partner document exchange), Data Catalog (description without delivery), data marketplaces (discovery face of the same thing).
- Unknowns: is a marketplace/discovery surface definitional? Is commerce definitional? Is "live" delivery definitional or just the current cloud posture?

## Research Questions

1. What is the unit of exchange, and what does a published offering contain?
2. How does a consumer gain access — invitation, subscription, request? What is the entitlement lifecycle (accept → use → update → expire/revoke)?
3. How is data delivered: delivered copies, scheduled snapshots, or live in-place access? How do updates propagate?
4. Is there a discovery/marketplace surface? What audiences exist (bilateral, group/consortium, public)?
5. What governance exists on the provider side (terms of use, monitoring, audit, revocation) and consumer side (re-governance of received data)?
6. Is pricing/commerce part of the Type or an optional posture?
7. What platform requirements bind each side (same cloud, same product, open protocol)?
8. Who uses it and through which interfaces?
9. How do clean rooms / query-only collaboration relate?
10. Where does the Type end against MFT, EDI, catalog, integration, replication, open-data portals?

## Representative Products

| Product | Philosophy / position | Tier of documentation used |
|---|---|---|
| AWS Data Exchange | Hyperscaler service for data entitlements at scale; third-party data products sold through AWS Marketplace; grant- and subscription-based | Official user guide (fetched) |
| Azure Data Share | Bilateral/partner governed sharing between Azure organizations; snapshot or in-place; no commerce | Official docs overview (fetched) |
| Snowflake Secure Data Sharing / Listings / Data Exchange | Platform-native live zero-copy sharing inside the lakehouse; shares, listings, private "data exchanges", clean rooms, reader accounts | Official docs (fetched) |
| Databricks OpenSharing + Databricks Marketplace | Open-protocol sharing that works regardless of the consumer's platform; open-source; marketplace + private exchanges + clean rooms | Official docs (fetched) |

Selection rationale: four different product philosophies (third-party marketplace service vs bilateral sharing vs platform-native live sharing vs open-protocol sharing), all hyperscaler/lakehouse market leaders with Tier-1 documentation, spanning both commercial (paid data products) and non-commercial (partner/consortium sharing) customer contexts.

## Sources

All fetched 2026-09-07 (evidence layer A — direct observation of official documentation):

- AWS — "What is AWS Data Exchange?" — https://docs.aws.amazon.com/data-exchange/latest/userguide/what-is.html
- Microsoft — "What is Azure Data Share?" — https://learn.microsoft.com/en-us/azure/data-share/overview
- Snowflake — "About Secure Data Sharing" — https://docs.snowflake.com/en/user-guide/data-sharing-intro
- Databricks — "Share data and AI assets securely" — https://docs.databricks.com/en/data-sharing/index.html
- Databricks — "What is OpenSharing?" — https://docs.databricks.com/aws/en/opensharing/
- Databricks — "What is Databricks Marketplace?" — https://docs.databricks.com/aws/en/marketplace/

Source-access limitation: Google Cloud Analytics Hub (BigQuery data exchange) was attempted twice and timed out both times; it was abandoned per the network-limited rule and is not used as evidence. Snowflake's marketplace pricing/terms pages were not fetched (the fetched sharing page covers sharing objects and audience options but not listing terms); commerce claims for Snowflake are therefore kept weak. Historical/regional samples (pre-cloud FTP-subscription data vendors, statistical-agency exchanges) were not directly fetched; the historical check for them is reasoned structurally rather than observed.

## Product A — AWS Data Exchange

### Key observations (layer A)

- Self-description: "a service that helps AWS customers easily share and manage data entitlements from other organizations at scale."
- **Data grant** = the unit of exchange created by a *data sender* to grant a *data receiver* access to a data set; a grant request is sent to the receiver's AWS account and must be **accepted**. Parts: the **data set** (five supported types: Files, API, Amazon Redshift, Amazon S3, AWS Lake Formation), grant details (name, description visible to receivers), recipient access details (receiver's AWS account ID and how long the receiver should have access).
- **Product** = the unit of exchange in AWS Marketplace, published by a provider, available to subscribers; parts: product details (name, short/long descriptions, data samples, logo, support contact), **product offers** (terms: prices and durations, data subscription agreement, refund policy, option for custom offers), and one or more data sets.
- Provider/receiver vocabulary throughout; receivers track "all of your current, pending, and expired data grants" in one console; discovery + subscription through the AWS Marketplace catalog.
- Provider access: console ("Publish data") plus APIs (Data Exchange API to create/update data sets, revisions, and import/export assets; Marketplace Catalog API for products).
- AWS reviews published products against guidelines; permitted data types are restricted (legal eligibility requirements).
- Delivery surfaces: export files to Amazon S3 programmatically, or direct access to providers' S3 buckets; API assets callable programmatically or from the console (OpenAPI spec downloadable); Redshift data sets give **read-only query access without ETL**; Lake Formation data-permission data sets let receivers query the provider's data lake.
- Open Data on AWS program integration: anyone, with or without an AWS account, can find and use publicly available data sets — a public, no-entitlement tier inside the same family.
- Region-scoped resources; single global product catalog.

## Product B — Azure Data Share

### Key observations (layer A)

- Self-description: "enables organizations to securely share data with multiple customers and partners. Data providers are always in control… makes it simple to manage and monitor what data was shared, when and by whom."
- Explicitly positioned **against the ad-hoc alternatives**: "FTP, e-mail, APIs to name a few. Organizations can easily lose track of who they've shared their data with."
- Flow: provider creates a **data share** and **invites recipients by e-mail**; consumer accepts the invitation; consumer **must accept terms of use before receiving data**; provider specifies update frequency; "Access to new updates can be revoked at any time by the data provider."
- Two sharing modes:
  - **Snapshot-based**: data moves from the provider's subscription into the consumer's own store; full snapshot on acceptance; **scheduled incremental updates** (hourly or daily options); consumer chooses destination store of their own (e.g., Blob → Data Lake Store; Synapse → ADLS/SQL DB/Synapse; parquet or csv from SQL sources).
  - **In-place sharing**: no copy; "a symbolic link is created between the data provider's source data store and the data consumer's target data store"; consumer reads/queries in real time (currently Azure Data Explorer).
- Scenarios named by the vendor: retailer sharing POS data with suppliers; "establish a data marketplace for a specific industry" (government/research sharing anonymized data); "establish a data consortium" (research institutions share with a trusted body, processed output shared onward).
- Key capability lists for both roles: provider (share with customers/partners **outside of your organization**, track who data was shared with, choose snapshot or in-place, set update frequency, allow pull or push of updates); consumer (view a description of the data being shared, view terms of use, accept or reject the invitation, receive into a supported store, trigger snapshots).
- Everything available through the Azure portal **or REST APIs**.
- Both sides must have Azure subscriptions. The service stores no copy of the shared data itself — data lives in the underlying stores.

## Product C — Snowflake (Secure Data Sharing / Listings / Data Exchange)

### Key observations (layer A)

- Secure Data Sharing lets an account "share selected objects in a database… with other Snowflake accounts": databases, tables (incl. dynamic/external/Iceberg/Delta), views (regular/secure/materialized/semantic), Cortex search services, UDFs, models.
- **Share** = a named Snowflake object encapsulating all information required to share a database; the provider grants privileges on objects to the share and adds consumer accounts; provider-controlled: "New objects added to a share become immediately available… Access to a share… can be revoked at any time."
- **No data is copied or transferred**; sharing uses the services layer and metadata store; shared data takes no storage in the consumer account; the consumer pays only compute for querying. Consumer gets a **read-only** database from the share, governed by the consumer's own standard RBAC.
- Four sharing options named by the vendor:
  1. a **Listing** — "you offer a share and additional metadata as a data product to one or more accounts";
  2. a **Direct Share** — directly share objects to another account in the region;
  3. a **Data Exchange** — "you set up and manage a group of accounts and offer a share to that group" (the vendor's own feature named like the Type);
  4. a **clean room** — "share data and control which queries can be run against your data."
- Provider/consumer role vocabulary; any full account can be both provider and consumer; third-party (publisher–subscriber) accounts and **reader accounts** exist for consumers who are not Snowflake customers (reader accounts can only consume from their creating provider, query-only).
- Provider-side **usage metrics**: for private listings, data exchanges, and the marketplace, providers get metrics about consumer usage and the consumer accounts accessing their listings.

## Product D — Databricks OpenSharing + Databricks Marketplace

### Key observations (layer A)

- OpenSharing = "the secure data sharing platform in Databricks that lets you share data and AI assets with users **outside your organization**, **regardless of whether they use Databricks**"; basis for Marketplace and Clean Rooms; available as an **open-source project / open protocol** usable from other platforms.
- Core objects: **shares** (read-only collection of tables and table partitions; in Databricks-to-Databricks also views incl. row/column-filtered dynamic views, volumes, models, notebook files; add/remove assets at any time; securable object in Unity Catalog), **providers** (entity that shares), **recipients** ("securable object that represents an organization and associates it with a credential or secure sharing identifier"; deleting a recipient removes all its access).
- Provider setup flow: enable sharing on the metastore → create a share → create a recipient → grant the recipient access to one or more shares → send connection info (activation link to download token credentials for open sharing; sharing identifier for Databricks-to-Databricks; OIDC federation as alternative).
- Recipients access **read-only**; updates to provider data "appear in near real time"; recipients on Unity Catalog workspaces can grant/deny access to their own users (consumer-side re-governance).
- Auth models: long-lived bearer token, OIDC federation, or platform-managed Databricks-to-Databricks identity (no token).
- Governance/audit: audit logging and system tables on both sides — "understand who is accessing which data"; provider can revoke access on demand at several granularities (per share, per IP, per recipient, revoke tokens).
- **Databricks Marketplace**: "an open exchange where data providers, software vendors, and technology partners publish offerings that Databricks customers can discover, evaluate, and connect with directly from their workspace. Listings include datasets, AI models, notebooks, apps, and MCP servers."
  - Consumers browse/search listings; an open marketplace is browsable **without** a Databricks workspace; requesting access happens in the workspace.
  - Audiences: *public marketplace* (everyone) vs *private exchange* ("a provider shares their listings only with member consumers").
  - Entitlement: "Some data products are available instantly, as soon as you request them and **agree to the terms**. Others might require **provider approval** and transaction completion using provider interfaces."
  - Providers list via a partner program (public) or self-service (private exchanges); free and commercialized offerings both exist.

## Cross-product Comparison

| Dimension | AWS Data Exchange | Azure Data Share | Snowflake | Databricks |
|---|---|---|---|---|
| Unit of exchange | data grant / marketplace data product (product = details + offer + data sets) | data share (invitation) | share; listing = share + metadata as data product | share; marketplace listing |
| Offering description | name, descriptions, samples, logo, support contact | description of data being shared | listing metadata | listing (datasets, models, notebooks, apps, MCP servers) |
| Terms | product offer: prices/durations, data subscription agreement, refund policy, custom offers | terms of use must be accepted before receiving | (listing terms not directly observed) | agree to terms at request; provider approval possible |
| Entitlement act | accept grant / subscribe in catalog | accept e-mail invitation | account added to share; consumer imports | request + terms/provider approval; recipient grant |
| Delivery | export to S3, direct S3 access, Redshift read-only query, API assets | snapshot copy (scheduled incremental) or in-place link | live zero-copy query; no storage in consumer account | live open protocol; read-only; near-real-time updates |
| Updates | revisions of data sets | scheduled full/incremental snapshots; consumer can pull | immediate (new/changed objects) | near-real-time |
| Revocation | grant expiry; managed grants | revoke access at any time | revoke at any time | revoke on demand (share/recipient/IP/token) |
| Provider monitoring | grant/subscription console views | monitor what/when/by whom | usage metrics per listing/exchange | audit logs + system tables, both sides |
| Consumer-side governance | — (copies into own S3) | receives into own store | read-only DB under consumer RBAC | read-only catalog; recipient grants own users |
| Commerce | yes (Marketplace offers, pricing) | no | listings (commerce not directly observed) | free + commercialized; provider approval/transactions possible |
| Audience scope | public marketplace + private offers + direct grants | bilateral invitations; consortium/marketplace scenarios named | direct share / group exchange / listing | open marketplace / private exchange / direct share |
| Platform coupling | AWS accounts both sides | Azure subscriptions both sides | Snowflake accounts (+ reader accounts for outsiders) | open protocol; consumers need no Databricks |
| Interfaces | console + APIs + Marketplace catalog | Azure portal + REST APIs | Snowflake UI/SQL + listings UI | workspace UI + provider console + open marketplace site |

### Layer-B findings (cross-product commonality, all four)

1. Two explicit role poles: **data provider** (sender/sharer/publisher) and **data consumer** (receiver/recipient/subscriber) — the same party can be both.
2. A **defined, described offering** (dataset/share/listing) is the durable object; it outlives any single transfer.
3. **Explicit entitlement** binds a specific external party (or an open public tier) to that offering — invitation acceptance, grant acceptance, subscription, or request + approval.
4. **Revocation at any time by the provider** is stated in all four.
5. **Update propagation** is a first-class concern (revisions, scheduled snapshots, immediate/near-real-time availability).
6. Provider-side visibility into **what was shared with whom and who used it** (monitoring/usage metrics/audit).
7. Both console/UI **and API** access on both sides.
8. Consumption is **read-oriented**; consumers place received data under their own analytics/governance environment.
9. Terms-of-use capture at the acceptance point is directly observed in three of four (AWS offer terms, Azure terms acceptance, Databricks agree-to-terms).

### Definitional reasoning (layer C)

- The smallest structure that makes this a recognizable Type and that survives the historical check (FTP-subscription data vendors, statistical-agency exchanges): (1) a **provider-defined data offering**, (2) an **explicit entitlement** binding a consumer to it, (3) a **standing platform-mediated delivery/access channel** with updates. Remove the entitlement → open-data publication portal. Remove the defined offering → ad-hoc file movement (MFT). Remove the standing mediated channel → bilateral custom FTP/email/API, which is precisely the "before" state the vendors describe.
- Marketplace/discovery, commerce, live query, clean rooms, open protocols are all real but none is required: Azure Data Share has no marketplace and no commerce; Snowflake/Databricks bilateral shares have no discovery; AWS files-based products have no live query. None of these belongs in the defining core.

## Canonical Model (abstraction layers)

### L0 — Defining Invariant (minimal)

```text
Data Provider (holder of data)
└── Data Offering: a defined, described set of data made available to others
    └── Entitlement: explicit, provider-controlled binding of a consuming party
        to that offering (accept/subscribe/approve; may be open-public as a tier)
        └── Platform-mediated Access & Delivery: the consumer obtains the data
            through the exchange's standing sharing mechanism (delivered copy,
            scheduled snapshot, or live query), with updates, revocable
```

Three invariants. Each removal test:
- Remove the offering (defined/described data product) → unstructured file movement → Managed File Transfer territory.
- Remove the entitlement (provider-controlled access decision) → public publication/download → Government Open Data Portal / open-data program territory.
- Remove the standing mediated channel (one-off ad-hoc transfer) → bilateral FTP/email/API — the exact "before" state named in the vendor docs.

### L1 — Common Mature Structure (very common, not definitional)

- Discovery/listing surface (marketplace face) with descriptions, samples, provider identity
- Terms of use captured at the acceptance/entitlement point
- Revision/update machinery (revisions, scheduled incremental snapshots, live propagation)
- Provider-side monitoring/usage metrics/audit trails; consumer-side audit too in mature products
- Revocation at multiple granularities (per offering, per consumer, per asset)
- Consumer-side re-governance (received data placed under the consumer's own access control)
- Console + API surfaces for both roles
- Read-only posture of the delivered/shared data
- Offering content beyond raw tables: files, API endpoints, views, models, notebooks, volumes
- Provider review/policy gates on what may be published (legal eligibility guidelines)

### L2 — Variant / Optional Structure

- Audience scope: bilateral invitation ↔ private exchange/consortium (managed member group) ↔ public marketplace
- Commercialization: free/partner sharing vs paid data products with pricing offers, private offers, subscriptions
- Delivery posture: copy-based (files/snapshots) vs in-place/live query vs API delivery
- Platform coupling: both sides on the same cloud/product vs open protocol with cross-platform consumers
- Public open-data tier inside the same product family (no-cost, no-per-party entitlement)
- Clean rooms / query-only collaboration (control which queries run without raw access)
- Industry/regional consortium deployments; regulator/trusted-body hub shapes
- Source-asset breadth (tables vs files vs APIs vs AI models/notebooks)

### L3 — Vendor-specific Detail (kept out of the canonical document)

- AWS: five data-set types; grant parts (account ID + duration); Region-scoped resources; Open Data on AWS integration; Redshift/Lake Formation access modes; BYOS offers.
- Azure: hourly/daily snapshot schedule options; parquet/csv format choice; in-place currently Azure Data Explorer only; symbolic-link mechanism; regional metadata placement.
- Snowflake: share/database-role privilege model; reader accounts; third-party publisher–subscriber accounts; object types shareable (Cortex search services, semantic views); usage-metric views schema.
- Databricks: Unity Catalog securables; bearer-token/OIDC activation-link flow; sharing identifiers; egress/billing attribution tables; feature-support matrix; commit drawdown program; MCP server listings.

## Vendor-specific Findings

- The words "data exchange" and "marketplace" are vendor feature names as well as Type names (Snowflake "Data Exchange" = a managed group of accounts; Databricks "private exchange" = member-scoped listings). The Type must be defined independently of any single vendor's feature naming.
- Clean rooms appear in two of four samples as a distinct adjacent capability (query-controlled collaboration without raw data access) — treated as adjacent, not core.
- Commerce machinery (pricing offers, refund policies, custom/private offers, transactions via provider interfaces) is product-specific depth on the marketplace pole, not a Type requirement.

## Rejected Findings

- "A data exchange is a marketplace" — rejected: bilateral sharing with no discovery surface satisfies the Type (Azure; Snowflake direct shares; Databricks open sharing).
- "Both parties must be on the same platform" — rejected: Databricks open protocol explicitly serves consumers with no Databricks; reader accounts serve non-Snowflake consumers.
- "Data must be delivered live, zero-copy" — rejected: snapshot/copy delivery is a first-class mode in AWS and Azure and the historical default.
- "Commerce/pricing is definitional" — rejected: Azure Data Share and partner-sharing postures have no commerce.
- "The Type is only about tabular data" — rejected at L1/L2 level: files, APIs, models, notebooks, volumes are shared across the sample; raw datasets remain the center.

## Boundary Findings

| Neighbor Type | Relationship | Distinction (and the removal test) |
|---|---|---|
| Managed File Transfer (§13) | closest operational neighbor | MFT moves files per transfer event between endpoints with transfer-level audit; an exchange manages a **durable offering + entitlement relationship** (who is entitled to which data product, with updates and revocation). Remove offering/entitlement objects → MFT. MFT docs do not speak of providers publishing data products with terms. |
| EDI Platform (§13) | both are "organizations exchanging structured data" | EDI exchanges standardized **business transaction documents** (orders, invoices, ship notices) whose semantics are fixed by industry standards, processed transactionally. Exchange delivers **datasets/data products for consumption/analysis**. Replace dataset offerings with standardized transaction-document flows → EDI. |
| Data Catalog (§13) | complementary pairing | A catalog **describes** data living in other systems and grants no access; an exchange **delivers/entitles** access to data it brokers. Catalog metadata feeds exchange listings; catalog suites now bolt on marketplace/exchange surfaces (see STATUS flag). |
| Data Integration Platform / ETL-ELT (§13) | often named together | Integration moves/transforms data among an organization's **own** systems via engineer-defined pipelines; an exchange is an **inter-organization** publishing/entitlement relationship with no transformation as its center. |
| Data Replication Platform / CDC (§13) | copy mechanics overlap | Replication continuously copies data between stores **for the same owner's** systems (availability/analytics); an exchange grants **external parties** governed access to an offering. Replication has no entitlement/offering/terms objects. |
| Data Virtualization Platform (§13) | both offer "query without copying" | Virtualization federates queries across sources for the organization's own consumers; an exchange is a provider→consumer entitlement between organizations. |
| Government Open Data Portal (§24) / Public Data Portal (§02.12) | the no-entitlement pole | Portals publish datasets for anyone to download; no per-party entitlement, subscription lifecycle, or revocation. Remove the entitlement invariant from the exchange and you get this. (AWS Open Data integration is the exchange family absorbing a public tier.) |
| API Marketplace / Model API Platform (§12/§13) | commerce face overlap | Those sell access to **services** (API calls, model inference); the exchange delivers **data products**. AWS's API-as-data-set type is the documented edge where the two meet. |
| Health Information Exchange / HIE (§22) | domain-specialized sibling | HIE exchanges clinical records/messages between care providers under health-data standards and consent regimes; the generic exchange's unit is a dataset offering, not patient records routed for care delivery. |
| Virtual Data Room (§11) | secure external sharing, different unit | VDRs share **documents** for deal diligence under heavy access audit; the exchange's unit is a data product for ongoing consumption. |

Taxonomy note: no separate "Data Marketplace" leaf exists in the directory; the marketplace face is treated here as a common (not definitional) surface of the Data Exchange Platform Type. This also answers the data-catalog pass's flag ("data products / marketplace layer inside catalog suites — watch whether it deserves a distinct leaf"): the distinct leaf exists — it is this Type, populated by dedicated hyperscaler services and lakehouse sharing platforms, with catalog vendors embedding exchange surfaces as one packaging variant.

## Uncertainties

- Snowflake listing commerce/terms details were not directly fetched; Snowflake monetization claims kept weak.
- Google Cloud Analytics Hub unreachable (two timeouts) — the sample is four products, all with direct evidence; a fifth would likely only repeat observed structures (its published model — listings + subscriptions across organizations — is publicly known but was not verified here and is not used as evidence).
- Standalone vendor-neutral exchange products outside the hyperscaler/lakehouse population (legacy B2B data-delivery suites, data-marketplace startups) were not directly examined; the historical check for subscription-file-delivery vendors is structural, not observational.
- In-place sharing breadth within Azure (observed for one store at fetch time) may have widened; asserted here only as observed.
- Precise numeric limits, schedule options beyond the observed ones, and per-product pricing are intentionally not stated in the canonical document.

## Final Synthesis

A Data Exchange Platform is the inter-organizational data-sharing system of record: a data provider packages a defined, described data offering; the platform binds specific consuming parties to that offering through explicit, provider-controlled entitlements (accept/subscribe/approve, with terms); and the consumer obtains the data through the platform's standing sharing mechanism — delivered copies, scheduled snapshots, or live in-place query — with update propagation, provider-side revocation, and two-sided visibility into what was shared with whom and who used it. Marketplace discovery, commerce, live zero-copy delivery, clean rooms, and open protocols are common or optional structures, not the definition. The Type stands on its own between MFT (ad-hoc file movement), EDI (transaction documents), Data Catalog (description without delivery), and integration/replication (intra-organization movement).
