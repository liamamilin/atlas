# Data Exchange Platform

## Overview

A **Data Exchange Platform** is an inter-organizational data-sharing system of record. One party — the **data provider** — packages a defined set of data as an offering; other parties — **data consumers** — are bound to that offering through explicit, provider-controlled entitlements; and the data reaches the consumer through the platform's own sharing mechanism, as delivered copies, scheduled snapshots, or live query access.

The defining structure is small:

```text
Data Provider
└── Data Offering (a defined, described set of data made available to others)
    └── Entitlement (an explicit, provider-controlled binding of a consuming
        party to that offering — accept, subscribe, or approve)
        └── Platform-mediated access & delivery (standing channel with
            updates, revocable by the provider)
```

Everything else the market associates with the category — marketplace discovery, paid data products, live zero-copy delivery, open protocols, clean rooms — is common or optional, not definitional. Bilateral partner sharing with no marketplace and no commerce satisfies the definition, and so do older delivery patterns: a data vendor running a subscription file-delivery service, or a statistical agency exchanging datasets with authorized counterparts, is the same Type realized on older infrastructure.

When data moves only between systems owned by the same organization, the product is an integration or replication system, not an exchange. When structured *business transaction documents* (orders, invoices) rather than datasets flow between partners, the product is an EDI platform.

## Users & Context

Two role poles organize everything, and the same organization can occupy both:

**Provider side**

- *data provider admin / data engineer*: packages data into offerings, configures who may receive them, sets terms and update behavior, revokes access
- *product/publisher role (commercial pole)*: writes listing descriptions, samples, and pricing where data is sold

**Consumer side**

- *data engineer*: accepts entitlements, configures destinations or connections, lands received data into the organization's own analytics environment
- *analyst / data scientist*: the downstream consumer of received or live-shared data inside their own tools

Typical scenarios: a company sharing point-of-sale data with its suppliers on a schedule; a data provider selling market datasets to many subscribers; an industry consortium sharing data through a trusted member group; two organizations agreeing a one-off governed share. The work environment is cloud consoles and data-platform UIs on both sides, with APIs used for everything a console can do — providers in particular typically automate publishing and entitlement management.

## Core Model

### The Defining Core

Three objects. Remove any one and the product stops being a data exchange:

- **Data offering** — the durable unit of the system: a named, described set of data (tables, files, views, API endpoints, or a combination) that the provider deliberately makes available to others. The offering outlives any single transfer; it carries a description of what the data is, and commonly samples and provider identity. Without defined offerings, the product degrades into unstructured file movement.
- **Entitlement** — the provider-controlled access decision that binds a specific consuming party to a specific offering. It is realized as an accepted invitation, an accepted grant, a subscription, or an approved request — and it commonly records terms of use that the consumer must accept before receiving data. An open public tier, where the provider makes an offering available to all comers, is still an entitlement decision — one made once, for everyone. Without entitlements, the product is a publication portal.
- **Platform-mediated access & delivery** — the standing channel through which the consumer actually obtains the data: files delivered into the consumer's storage, scheduled snapshots copied into a destination the consumer chooses, a live read-only query surface against data the provider still hosts, or an API endpoint. The relationship is durable — updates flow, access can be revoked — rather than a one-off hand-off. Without it, organizations are back to bilateral FTP, e-mail, and ad-hoc APIs, which is precisely the state vendor documentation positions this Type against.

Around this core, the platform keeps **provider-side and consumer-side state**: which offerings exist, who is entitled to what and on what terms, what has been delivered or accessed, and when. That state — not the data itself — is what the platform owns; in copy-based modes the data lands in stores the consumer already controls, and in live modes it remains in the provider's environment.

### Capabilities Shared by Mature Products

These are widespread in current products and make the Type practical, but no single one defines it:

- **Discovery / listing surface** — a browsable, searchable catalog of published offerings with descriptions, samples, and provider identity. Ranges from an internal-facing list to a public marketplace.
- **Terms of use at the acceptance point** — the consumer reviews and accepts usage terms as part of gaining access; acceptance is recorded.
- **Update propagation** — new or changed data reaches entitled consumers without re-engineering: revisions of published datasets, scheduled incremental snapshots, or immediate/near-real-time availability of changes in live sharing.
- **Revocation** — the provider can withdraw access at any time, in mature products at several granularities (whole offering, single consumer, individual assets or credentials).
- **Provider-side monitoring** — visibility into what was shared with whom, when, and who is using it: share/consumer inventories, usage metrics, audit trails. Consumer-side audit trails appear in mature deployments too.
- **Consumer-side re-governance** — received data is placed under the consumer's own access control and queried with the consumer's own compute; shared data is consumed read-only.
- **Console + API parity** — both roles can work through a UI and programmatically; publishing and entitlement management are automatable.
- **Publication review** — commercial marketplaces review submissions and restrict what data may lawfully be sold or distributed.

### One Structure, Many Implementations

The core model is conceptual. Realizations vary:

```text
Concept:      Data Offering
Realizations: marketplace data product, data share, listing, published dataset

Concept:      Entitlement
Realizations: accepted e-mail invitation, accepted data grant, catalog
              subscription, approved access request, managed member group

Concept:      Access & Delivery
Realizations: delivered files / exports into the consumer's storage,
              scheduled full+incremental snapshots into a chosen destination,
              live read-only query against provider-hosted data,
              API delivery of the offering
```

A reader who has only seen one realization — say, a public marketplace of paid data products — should still be able to recognize a bilateral invitation-based share, or a scheduled snapshot feed to suppliers, as the same Type.

## How It Works

### Provider loop — publish and govern

```text
Assemble the data (select tables/files/views, or prepare files and endpoints)
→ package it as an offering (name, description, samples; terms where applicable)
→ choose the audience (named partners, a member group, or the public)
→ publish, or invite/request-address the specific consumers
→ keep the data current (add objects, revise datasets, or let live sharing propagate)
→ monitor who is entitled and who is using it
→ adjust or revoke access as relationships change
```

There is no pipeline design and no transformation modeling here — the provider's work is packaging, audience, and governance, not data movement engineering.

### Consumer loop — acquire and consume

```text
Discover an offering (browse/search a catalog) or receive an invitation
→ review the description, samples, and terms
→ accept / subscribe / request access (provider approval may be required)
→ configure how to receive it (choose a destination store and schedule
   for copies; or establish the connection for live access)
→ land or connect the data in the organization's own analytics environment
→ keep consuming as updates arrive
```

On the consumer side there is also housekeeping: a consolidated view of current, pending, and expired entitlements, and the ability to place received data under the consumer's own governance.

### Update and lifecycle behavior

The offering is a living relationship, not a delivery event:

- in **copy-based** postures, the consumer receives a full copy on acceptance and incremental updates on a schedule the provider sets (or triggers refreshes on demand)
- in **live** postures, changes to the provider's data become available to the consumer immediately or near-immediately, with no storage cost or copy on the consumer side
- entitlements can expire; access can be revoked at any time; commercial subscriptions follow their offer terms

### Capability tiers

**Defining core** — without these, not a data exchange:

- provider-defined data offering
- explicit, provider-controlled entitlement of a consuming party
- platform-mediated, standing access/delivery with updates and revocation

**Standard capabilities** — present in most mature products:

- discovery/listing surface
- terms-of-use capture at acceptance
- revision/scheduled-update/live propagation machinery
- provider-side monitoring, usage metrics, audit trails
- revocation at multiple granularities
- consumer-side re-governance and read-only consumption posture
- console + API on both sides

**Optional / variant** — depends on market posture and product family:

- paid data products, pricing offers, and subscription commerce
- public open-data tiers alongside entitled sharing
- clean rooms and query-only collaboration (analysis over shared data without granting raw access)
- open protocols serving consumers on other platforms
- non-tabular offering content (files, API endpoints, AI models, notebooks)

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Provider console / publishing workspace

The provider's control surface.

- lists the provider's offerings, entitlements granted, and consumer activity
- primary actions: create/revise an offering, grant or invite a consumer, set terms and update behavior, revoke, inspect usage

### Consumer catalog / discovery surface

Where consumers find what they can request or subscribe to.

- searchable list of offerings with descriptions, samples, provider identity, and terms
- primary actions: browse, search, view offering detail, request/subscribe

### Entitlement inbox / subscription list

The consumer's record of relationships.

- entitlements under review, active, and ended; pending invitations awaiting acceptance
- primary actions: review terms, accept or reject, configure destination/schedule, remove

### Offering detail

The description surface of a single offering.

- what the data contains, its shape, samples, terms of use, provider identity
- primary actions: subscribe/request, preview/sample where offered

### Received-data / shared-data view

The consumer-side surface over data that has arrived or is live-shared.

- read-only datasets or catalogs placed in the consumer's environment
- primary actions: query, grant access to internal users, refresh (copy modes)

### Administration & APIs

Settings and programmatic access around all of the above: platform enablement, permissions for who may publish or receive, API keys/tokens where the delivery mechanism needs them, audit log access.

## Important Rules / Behaviors

### The provider stays in control

Access is a provider decision throughout: nothing reaches a consumer without the provider publishing the offering and the entitlement being granted — and access, once granted, can be withdrawn. This is the platform's core promise relative to ad-hoc methods — file drops, e-mail, hand-built APIs — where organizations lose track of who they have shared data with and on what terms.

### Entitlement precedes delivery

In every observed product, data does not flow until the consumer-side acceptance step completes (invitation accepted, grant accepted, request approved, terms agreed). The acceptance event is also where terms of use are typically captured.

### Consumption is read-oriented

Shared and delivered data is consumed read-only. Consumers work with the data in their own environment — their own storage, their own compute, their own access controls — but they do not modify the provider's data. Live-sharing modes make this explicit (read-only objects in the consumer's account); copy modes make it moot (the consumer owns the copy).

### The platform holds the relationship, not necessarily the data

In copy modes, the platform brokers delivery and then the data lives in consumer-controlled stores; in live modes, the data never leaves the provider's environment and consumers query in place. Either way, the platform's own records — offerings, entitlements, delivery history, usage — are the durable system of record for the relationship.

### Revocation has consumer-visible consequences

Revoking an entitlement (or expiring a subscription) ends the consumer's access to future updates — and in live modes, to the data itself. Copy-based deliveries that already landed remain in the consumer's environment, which is why terms of use, not just technical access, carry part of the governance load.

## Variants

- **Bilateral partner sharing** — provider and consumer set up a governed share directly (invitation-based); no marketplace, no commerce. The classic supplier/customer/consortium posture.
- **Commercial data marketplace** — providers publish products with pricing to a public catalog; consumers subscribe, sometimes with provider approval and private/custom offers; platform review gates what may be sold.
- **Private exchange / consortium** — a managed member group inside which providers share offerings visible only to members; used for industry data sharing and trusted-body hub models.
- **Open data tier** — the same machinery used to publish datasets to everyone at no cost, without per-party entitlements.
- **Platform-coupled vs open-protocol** — some products share only between accounts of the same platform (with bridge accounts for outsiders); others implement open protocols so consumers on any platform can connect.
- **Delivery posture** — copy-based (files, snapshots) vs live in-place query vs API delivery; larger products offer more than one.
- **Domain-specialized exchanges** — regulated industries run exchanges with the same structure (defined offerings, entitlements, mediated delivery) under domain-specific standards and consent regimes, such as clinical data sharing between care providers.

A variant remains a variant unless it changes the core: audience scope, commerce, and delivery posture all leave the defining structure intact.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Managed File Transfer | moves files per transfer event between endpoints with transfer-level audit; an exchange manages durable offerings and entitlement relationships (who is entitled to which data product, with updates and revocation) |
| EDI Platform | exchanges standardized business transaction documents (orders, invoices) between trading partners for transaction processing; an exchange delivers datasets/data products for consumption and analysis |
| Data Catalog | describes data living in other systems and grants no access; an exchange entitles and delivers access. Catalog metadata commonly feeds exchange listings; catalog suites increasingly embed exchange surfaces as one packaging |
| Data Integration Platform / ETL-ELT | moves and transforms data among an organization's own systems via engineer-defined pipelines; an exchange is an inter-organization publishing/entitlement relationship with no transformation at its center |
| Data Replication Platform | continuously copies data between stores for the same owner's systems (availability/analytics); an exchange grants external parties governed access to an offering |
| Data Virtualization Platform | federates queries across sources for an organization's own consumers; an exchange is a provider→consumer entitlement between organizations |
| Government Open Data Portal | publishes datasets for anyone to download, without per-party entitlement, subscription lifecycle, or revocation — the no-entitlement pole of this family |
| API Marketplace / Model API Platform | sells access to services (API calls, model inference); an exchange delivers data products. API-delivered datasets are the documented edge where the two meet |
| Health Information Exchange | a domain-specialized sibling: clinical records exchanged between care providers under health-data standards and consent regimes, rather than dataset offerings |
| Virtual Data Room | shares documents for deal diligence under heavy access audit; the exchange's unit is a data product for ongoing consumption |

The load-bearing boundaries are with Managed File Transfer (standing entitlement relationship vs transfer event) and EDI (dataset products vs standardized transaction documents): both neighbors also move data between organizations, and the difference is the object being managed.

## Representative Products

- AWS Data Exchange
- Azure Data Share
- Snowflake (secure data sharing, listings, data exchanges)
- Databricks (OpenSharing, Databricks Marketplace)

The four sample deliberately spans the category's poles: a marketplace-centered entitlement service, a bilateral partner-sharing service, and two lakehouse platforms — one platform-native live sharing, one open-protocol sharing — across both commercial and non-commercial postures.

## Sources

Research date: **2026-09-07**

Official product documentation (all directly fetched):

- AWS — *What is AWS Data Exchange?* (AWS Data Exchange User Guide) — https://docs.aws.amazon.com/data-exchange/latest/userguide/what-is.html
- Microsoft — *What is Azure Data Share?* (Azure Data Share overview) — https://learn.microsoft.com/en-us/azure/data-share/overview
- Snowflake — *About Secure Data Sharing* (Snowflake Documentation) — https://docs.snowflake.com/en/user-guide/data-sharing-intro
- Databricks — *Share data and AI assets securely* — https://docs.databricks.com/en/data-sharing/index.html
- Databricks — *What is OpenSharing?* — https://docs.databricks.com/aws/en/opensharing/
- Databricks — *What is Databricks Marketplace?* — https://docs.databricks.com/aws/en/marketplace/

> Sourcing limitations: a fifth hyperscaler data-exchange service (Google Cloud Analytics Hub) could not be fetched from the research environment and is not used as evidence. Snowflake's listing commerce/terms pages were not reachable in this pass, so that product's monetization details are not asserted. Historical samples (pre-cloud subscription file-delivery vendors, statistical-agency exchanges) were checked structurally rather than by direct fetch; the definition was deliberately kept free of cloud-era, marketplace-era, and live-delivery assumptions so that those older realizations still fit. Precise limits, schedule options, and pricing are intentionally not stated; product-by-product observations are recorded in the paired Research Notes.
