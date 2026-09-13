# Customer Data Platform / CDP

## Overview

A **Customer Data Platform (CDP)** is customer data infrastructure whose central object is the **persistent, individual customer profile**: it continuously consolidates customer data from multiple source systems into one durable record per person, links records and events that belong to the same individual (identity resolution), derives attributes and audiences from those profiles, and makes the profiles and audiences available to other systems — ad platforms, messaging tools, personalization surfaces, analytics, and warehouses.

The defining core is small:

```text
Customer data from many source systems
  → consolidated into persistent individual profiles
  → linked to the right person via identity resolution
  → enriched and grouped into audiences
  → delivered outward to systems that act on them
```

Three properties hold the type together. Remove the persistent individual profile and the product becomes an event pipeline or analytics tool. Remove multi-source consolidation with identity linkage and it becomes a single-source contact database. Remove outbound delivery and it becomes a customer analytics database with nothing activated.

Everything else commonly associated with CDPs — identity graphs, streaming ingestion, destination catalogs, consent dashboards, AI-predicted attributes, warehouse interop — is widespread in current products but is not what makes the product a CDP. A pre-cloud marketing database that assembled unified customer records from several systems and exported lists to a mail house satisfies the same core without any of the modern machinery.

## Users & Context

The primary users are **marketing and growth teams** — marketers who build segments and activate audiences, and marketing engineers / data teams who wire up data sources and destinations. Typical roles:

- **marketer**: defines segments and audiences, inspects profiles, activates audiences to channels
- **marketing engineer / data engineer**: connects SDKs and APIs, maps fields, maintains data quality
- **analytics / data science**: consumes profile data, builds computed or predictive attributes
- **privacy / compliance**: manages consent, opt-outs, and data subject requests

The organizational context is a company that interacts with customers across many channels (web, mobile apps, stores, email, support, commerce) where each channel's system holds only a partial view of the customer. The CDP exists because no single source system sees the whole customer: the web analytics tool sees clicks, the commerce system sees orders, the email tool sees opens, the CRM sees the sales relationship. The CDP is the layer that joins those partial views into one per-person record and puts it back to work.

## Core Model

### The Customer Profile

The center of the system is the **customer profile** — a persistent, individually addressable record for one person. Every profile carries:

- **identifiers** — the keys by which the person is recognized: email address, customer ID, device IDs, cookie IDs, phone number, or custom external IDs
- **attributes** — descriptive data merged from all sources: name, contact details, preferences, plan, lifetime totals
- **behavior** — a history of events: page views, purchases, email opens, support tickets, app sessions
- **computed attributes** — values derived from behavior by the platform itself: engagement scores, lifetime value, category affinities, predicted likelihood of churn or purchase
- **audience memberships** — which defined audiences the profile currently belongs to
- **consent state** — what the person has consented to, and what processing is permitted

Profiles exist in two states that coexist by design: **anonymous** (recognized only by a cookie or device ID, no identifying information yet) and **known** (carrying at least one durable identifier such as an email or customer ID). Anonymous behavior is retained, and when the person is later identified, the accumulated anonymous history is merged into the known profile.

### Identity Resolution

Identity resolution is the mechanism that makes consolidation meaningful. Incoming events and records arrive with whatever identifiers the source system knows. The platform decides which profile each item belongs to:

- identifiers are matched against existing profiles (an email that already belongs to a profile attaches the event to it)
- an unidentified visitor gets a new anonymous profile
- when an identifying value appears (a login, a purchase with an email), the anonymous profile is linked to — or merged with — the known profile, carrying its history along

Merging is governed by configurable rules: which identifiers are trusted, which take precedence, and how conflicting attribute values are resolved (for example, which source's value wins when two systems disagree). Products differ in how much of this is automatic versus administrator-configured, but every CDP has this decision layer, because "which records describe the same person" is the question the whole type exists to answer.

### Segments and Audiences

A **segment** (or **audience**) is a named, rule-defined group of profiles — for example, "subscribers who opened nothing in 60 days" or "high-value customers likely to churn". Rules are built from profile attributes, behavior, computed attributes, and sometimes predictions. Membership is **dynamic**: as profile data changes, profiles enter and leave audiences continuously. Products evaluate rules in streaming (membership updates as data arrives) and/or batch (scheduled recomputation) modes; most mature products support both.

### Sources and Destinations

Data moves through the platform in two directions:

- **Sources** bring data in: client SDKs embedded in web and mobile apps, server-side event APIs, batch file imports, connectors that pull from other business systems (commerce, CRM, support, email platforms), and — increasingly — direct connections to the company's data warehouse.
- **Destinations** carry data out: advertising platforms (audience sync for targeting and suppression), messaging and email tools (audiences and profile attributes for campaign targeting), analytics systems, storage and warehouses, and real-time profile APIs that let other applications look up a profile mid-session to personalize an experience.

The profile store is deliberately positioned between the two: data is consolidated *onto* profiles, and profiles (or audiences drawn from them) are what get delivered *out*.

## How It Works

The canonical operating loop:

```text
1. Connect sources
   web/mobile SDKs, server APIs, file imports, system connectors, warehouse links
        ↓
2. Data arrives as events and records
        ↓
3. Identity resolution
   each event/record is matched to a profile;
   anonymous profiles are promoted and merged when identification occurs
        ↓
4. Profiles accumulate
   attributes updated, behavior appended, computed attributes derived
        ↓
5. Segmentation
   rule-defined audiences evaluated continuously or on schedule;
   membership updates as profiles change
        ↓
6. Activation
   audiences synced to ad platforms and messaging tools;
   profiles exported to warehouses or internal systems;
   profile APIs serve personalization in other applications
        ↓
7. Governance throughout
   consent state gates processing; opt-outs and deletion requests
   propagate across profiles and downstream deliveries
```

A typical first deployment follows the same order: an engineering team connects the primary digital properties and verifies data quality; marketing then defines its first audiences and connects one or two destinations (commonly an email/messaging tool and one or two ad platforms); identity resolution rules are tuned as duplicate and cross-device cases surface; computed attributes and predictive scores are added later, once behavioral history has accumulated.

Two postures for the profile store exist in the current market. In the **packaged** posture — the classic form — the CDP maintains its own profile database and the company feeds it. In the **composable** posture, the platform layers identity resolution, segmentation, and activation directly over the company's existing data warehouse, without requiring data to be copied into a new store. Both realize the same core loop; they differ in where the profile of record physically lives. Several established products now offer composable capability alongside a native store.

## Interfaces

The following surfaces are described conceptually; exact names and layouts vary by product.

### Profile explorer

The inspection surface for the system's central object.

- search for one person by any known identifier (email, customer ID, device ID)
- profile detail: identifiers, attributes, event history timeline, audience memberships, consent state, identity-change history
- primary actions: search, inspect, correct attribute values, submit privacy requests

### Segment / audience builder

Where marketers define targetable groups.

- rule conditions over attributes, behavior, computed attributes, and predictions
- estimated audience size; membership preview
- primary actions: create/edit rules, save audience, connect audience to a destination

### Source configuration

Where data ingestion is set up.

- catalog of SDKs, APIs, file imports, and system connectors
- field mapping and schema/event specifications
- primary actions: add source, map fields, validate incoming data

### Destination configuration

Where activation is set up.

- catalog of ad platforms, messaging tools, storage, warehouses, and API endpoints
- mapping of profile fields/audiences to destination formats
- primary actions: connect destination, select audiences/profile data, monitor delivery

### Identity management

Where the linking rules live.

- identity priority/strategy configuration, merge rules, duplicate handling
- views of identity graphs or merge history for individual profiles
- primary actions: configure rules, inspect merges, resolve problem profiles

### Data quality and debugging

Operational surfaces for the technical owners.

- live event streams, event validation against defined specs, trace of a single event through the pipeline
- primary actions: inspect incoming data, find schema violations, debug a profile's computation

### Consent and privacy console

- consent purposes and their enforcement, opt-out records, data subject request handling (access/deletion)
- primary actions: configure consent purposes, process requests, verify propagation

### Administration

- user roles and permissions, environments/sandboxes, data retention settings

## Important Rules / Behaviors

- **The profile persists and accumulates.** Profiles survive sessions, channel switches, and long gaps in activity. Accumulation over time is the point: computed attributes and predictions depend on history.
- **Anonymous and known coexist, and identification is a merge.** Work done anonymously is not discarded when the person is later identified; it is attached to the known profile. The reverse — un-merging — is generally not a designed operation; in the products researched, identity merges are treated as permanent, which is why merge rules are configured carefully.
- **Conflicting data is resolved by rules, not silence.** When two sources disagree about an attribute value, a merge policy (recency, source priority, or explicit rules) decides which value the profile carries.
- **Audience membership is dynamic.** A profile's membership changes as its data changes; audiences are living definitions, not exported snapshots — although snapshot exports to destinations are also a normal delivery mode.
- **Consent gates the loop.** Consent state on the profile determines whether data may be processed and whether the profile may be delivered to particular destination types; opt-outs and deletion requests must propagate to downstream systems that already received the data.
- **The CDP consolidates; it does not originate.** The platform does not create customer data; it reflects what sources send. Data quality problems upstream become profile problems downstream, which is why validation and monitoring surfaces are standard.
- **Activation is delivery, not execution.** The CDP hands profiles and audiences to other systems that act on them. (One market variant — marketer-operated CDPs with built-in on-site interaction and journey execution — crosses this line deliberately; see Variants.)

## Variants

- **Packaged vs composable.** Packaged CDPs maintain their own profile store; composable (warehouse-native) CDPs perform identity resolution, segmentation, and activation over the customer's existing warehouse. Several established products now offer composable capability alongside a native store.
- **Developer-first vs marketer-operated.** Event-pipeline-first products are implemented by engineering teams and expose APIs/specs prominently; marketer-operated products emphasize no-code segment builders and guided setup. Both converge on the same core model.
- **B2C individual vs B2B account.** Consumer CDPs center on people (sometimes grouped into households); B2B editions add account-level profiles, account audiences, and person-to-account linking.
- **With execution surfaces.** Some marketer-operated CDPs include on-site interaction and lifecycle orchestration (personalized messages and journeys executed by the CDP itself), drifting toward marketing personalization territory while keeping the profile infrastructure at the center.
- **Real-time emphasis vs batch.** Streaming ingestion with in-session profile APIs (personalization use cases) versus scheduled batch processing (campaign and analytics use cases); most products support a mix.
- **Suite module vs pure-play.** CDP capability is delivered both as standalone products and as the customer-data layer of larger marketing suites; the core model is the same in both packagings.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Data Management Platform / DMP | closest historical neighbor | DMPs hold audience pools — historically cookie-based, third-party-data-centric, short-lived; the CDP holds persistent individual profiles built mainly from the company's own (first-party) data |
| Customer Relationship Management / CRM | adjacent system of record | the CRM's contact/account records are created and operated inside it by sales/service staff for relationship work; the CDP consolidates data *from* systems (often including the CRM) and serves profiles *to* other systems |
| Marketing Automation Platform | downstream consumer | MA platforms execute campaigns on owned channels over their own contact store; a CDP's profile store exists to serve other systems, MA platforms included |
| Data Warehouse Platform | complementary substrate | the warehouse is the analytical system of record for all enterprise data (tables, SQL, BI); it does not maintain activation-ready individual profiles as its central object |
| Reverse ETL Platform | adjacent activation tool | reverse ETL syncs warehouse data out to tools without owning a profile of record or performing identity resolution; composable CDPs add exactly those missing pieces on top |
| Customer Identity / CIAM | different layer | CIAM authenticates customers and manages registration/login lifecycles; the CDP consumes identity signals (login events, emails) as resolution inputs but holds no credentials and authenticates no one |
| Audience Management Platform | output-centric sibling | audience management holds targetable audiences as the primary object; the CDP holds profiles as the primary object and produces audiences as an output |
| Marketing Personalization Platform | downstream consumer | personalization platforms own decisioning and delivery of individualized experiences; the CDP supplies the profiles/audiences they decide with |

The boundary that matters most in practice is against the **CRM**: both hold per-customer records, but the CRM is a single-source system of engagement operated around relationships, while the CDP is multi-source data infrastructure operated around unification and activation. The second sharpest is against the **DMP**: both produce audiences, but only the CDP's underlying object is a persistent individual profile.

## Representative Products

- Twilio Segment
- mParticle
- Adobe Real-Time CDP
- BlueConic
- Tealium (AudienceStream)

These were chosen to span the type's main poles: developer-first event pipeline (Segment), mobile-first enterprise infrastructure (mParticle), enterprise suite module (Adobe Real-Time CDP), marketer-operated pure play (BlueConic), and tag-management-derived with strong ad-platform activation (Tealium).

## Sources

Research date: **2026-09-08**

- Twilio Segment — "How Segment works", "Identity Resolution Overview", "Engage Introduction" — https://www.twilio.com/docs/segment/
- mParticle — Docs home, "User Profiles", "Components of IDSync" — https://docs.mparticle.com/
- Adobe — "Real-Time CDP documentation", "Real-Time Customer Profile overview", "Destination types and categories" — https://experienceleague.adobe.com/en/docs/experience-platform/rtcdp/home
- BlueConic — Help Center, "BlueConic Basics Glossary", "Segments Overview" — https://support.blueconic.com/hc/en-us
- Tealium — Docs home, "AudienceStream CDP", "About visitor stitching" — https://docs.tealium.com/

> Sourcing note: all five products' core operational documentation was directly accessible on the research date. Deep sub-pages (identity-strategy internals, consent enforcement details) were sampled at overview level; precise numeric limits and plan-gated capabilities observed during research were deliberately excluded from this document. Claims about consent machinery for one sampled product are held at reduced strength because its consent documentation was not sampled at page depth.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
