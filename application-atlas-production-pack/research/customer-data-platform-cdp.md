# Research Notes — Customer Data Platform / CDP

Research date: 2026-09-08
Directory leaf: "Customer Data Platform / CDP" (§06 Marketing, Advertising & Growth)
Slug: customer-data-platform-cdp

---

## Research Goal

Understand what a Customer Data Platform actually is as an application type — its defining structure, its core objects, its workflows, its interfaces, and its boundaries against neighboring types (DMP, CRM, Marketing Automation, Data Warehouse / Reverse ETL, CIAM, Audience Management Platform) — from real product documentation, not vendor marketing.

## Initial Boundary

Working hypothesis before research:

- A CDP assembles customer data from multiple source systems into persistent, individual-level customer profiles, resolves which records/events belong to the same person, derives attributes/segments, and makes profiles and audiences available to downstream marketing/engagement systems.
- Most confusable neighbors: Data Management Platform / DMP (cookie/third-party audience data), CRM (single-source relationship system of record), Marketing Automation Platform (campaign execution), Data Warehouse + Reverse ETL (analytical store + activation), CIAM (customer authentication), Audience Management Platform (audience-centric sibling leaf in the same directory section).
- Known market tension: "composable" / warehouse-native CDPs challenge the "packaged software with its own profile store" part of the classic definition (CDP Institute's definition: packaged software creating a persistent, unified customer database accessible to other systems).

## Research Questions

1. What exactly is a "unified customer profile"? What does it hold (attributes, events, computed traits, audience memberships)?
2. How does data get in — SDKs, event APIs, batch files, cloud-app sources, warehouse connections?
3. What is identity resolution — deterministic vs probabilistic, identity graphs, anonymous→known stitching, merge rules?
4. What are segments/audiences and how are they computed (batch vs streaming/real-time)?
5. How does activation work — destination catalogs, audience sync to ad platforms, profile export, real-time profile APIs?
6. Where do consent/privacy/governance surfaces sit?
7. What packaging variants exist (packaged CDP vs composable/warehouse-native vs event-pipeline-first)?
8. Where are the boundaries vs DMP, CRM, MA platforms, warehouses/reverse ETL, CIAM?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Why selected |
|---|---|---|
| Twilio Segment | developer / event-pipeline-first ("customer data infrastructure") | canonical API-first CDP; excellent public docs |
| mParticle | mobile-first enterprise customer data infrastructure | strong identity-resolution machinery (IDSync strategies) |
| Adobe Real-Time CDP | enterprise suite pole (built on Adobe Experience Platform) | heavyweight enterprise CDP with full governance/activation stack |
| BlueConic | pure-play marketer-oriented CDP | marketer-operated, includes on-site interaction execution |
| Tealium | tag-management-derived CDP (AudienceStream) | event/visitor attribute model + strong ad-platform connectors; also ships a composable pole (CloudStream) |

## Sources

All fetched 2026-09-08 (Tier 1 — official product documentation):

- Segment (Twilio Segment)
  - Docs root: https://www.twilio.com/docs/segment/
  - "How Segment works": https://www.twilio.com/docs/segment/getting-started/01-what-is-segment
  - Identity Resolution Overview: https://www.twilio.com/docs/segment/unify/identity-resolution
  - Engage Introduction: https://www.twilio.com/docs/segment/engage
  - (Note: segment.com/docs/getting-started/what-is-segment/ returned 404; docs now live under twilio.com/docs/segment)
- mParticle
  - Docs root: https://docs.mparticle.com/
  - User Profiles: https://docs.mparticle.com/guides/customer-360/profiles/user-profiles/
  - Components of IDSync: https://docs.mparticle.com/guides/idsync/components/
- Adobe Real-Time CDP (Experience Platform)
  - RT-CDP documentation home: https://experienceleague.adobe.com/en/docs/experience-platform/rtcdp/home
  - Real-Time Customer Profile overview: https://experienceleague.adobe.com/en/docs/experience-platform/profile/home
  - Destination types and categories: https://experienceleague.adobe.com/en/docs/experience-platform/destinations/destination-types
- BlueConic
  - Help Center root: https://support.blueconic.com/hc/en-us
  - Basics Glossary: https://support.blueconic.com/en/articles/247523-blueconic-basics-glossary
  - Segments Overview: https://support.blueconic.com/en/articles/247640-segments-overview
- Tealium
  - Docs root: https://docs.tealium.com/
  - AudienceStream CDP: https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/
  - About visitor stitching: https://docs.tealium.com/server-side/visitor-stitching/about/

Source-access limitations: none blocking. All five products' core documentation was reachable. Some deep pages (mParticle IDSync sub-pages, Adobe identity-service deep pages) were only sampled at TOC/overview level; precise numeric limits observed in passing (e.g., mParticle "Bad User" thresholds) were recorded in Research Notes only and deliberately excluded from the final document.

---

## Product Observations

### Segment (Twilio Segment)

Evidence layer: A (direct observation of official docs)

Key observations:

- Self-description: "customer data platform (CDP) that collects, cleans, and activates customer data, sending events to hundreds of tools with one API."
- Core pipeline: Sources (web JS library, mobile SDKs, server libraries, HTTP tracking API, pixel API, cloud-app sources) generate messages → Segment servers → translated and forwarded to Destinations (catalog of 400+) and Warehouses/storage.
- Tracking spec: four principal methods — Identify ("who is the user"), Page/Screen, Track ("what are they doing") — with shared common fields. This is an event-centric data model.
- Connection modes: cloud-mode (data goes to Segment, then forwarded) vs device-mode (library sends directly to destination too).
- Identity Resolution / Identity Graph (Unify): merges complete customer history into a single profile across web/mobile/server/third-party touchpoints; supports cookie IDs, device IDs, emails, custom external IDs; anonymous identity stitching (child sessions merged into parent); user:account relationships for B2B; "Merge Protection" priority-trust algorithm; multiple external IDs matched to one persistent ID; identifiers treated case-insensitively.
- Engage (marketing add-on, requires Business tier): unified customer profiles, Computed Traits (per-user or per-account metrics like "lifetime value", "lead score"), SQL Traits (warehouse query results imported back as traits), Predictions (likelihood of events like churn/purchase), Audiences (lists of users/accounts matching criteria), sync of traits/audiences to Destinations, Engage Channels (SMS/email/WhatsApp campaigns), Profile API (server-side-only lookup of profile data for personalization).
- Warehouses are first-class: raw event schemas archived and sent to databases/warehouses/bulk storage on intervals.

### mParticle

Evidence layer: A

Key observations:

- Self-description: "a customer data platform (CDP) that simplifies how you collect and connect your user data to hundreds of vendors without needing to manage multiple integrations."
- Inputs: client SDKs (Android/iOS/web/Roku/Unity/Xbox/…), Events API (HTTP + server SDKs), partner feeds (AppsFlyer, Braze, Branch…), custom CSV feed, Warehouse Sync API (ingest from warehouse).
- Outputs: event outputs (analytics tools, ad platforms), audience outputs (Facebook, Snapchat, Twitter, Braze, Pinterest…), Profile API ("real-time API to drive user personalization"), Firehose API for custom integrations.
- IDSync (identity resolution framework): Identity API with four endpoints — Identify (session start), Search, Login, Logout — each resolving "all known identifying information for the current user" into "a single, unique mParticle User Profile" (existing match / updated match / new profile). Five configurable identity strategies (profile conversion, default, profile link, profile isolation — for strict privacy compliance, best match — for no-login businesses) plus identity priority ordering of identifiers; aliasing support.
- Customer 360 / User Profiles: each profile has a unique MPID; profile view shows identities (email, customer ID, device ID), user attributes (reserved attributes like name/gender/address), calculated attributes, events timeline, audience memberships, consent state (privacy tab with Data Subject Requests), identity history (identifier changes with triggering events). Profile search by any known identifier; household reach (households as a grouping above users).
- Calculated Attributes: derived per-user metrics; Predictions (future behavior, next best action, similar customers) can build audiences.
- Audiences: create/connect/manage; audience sharing, expansion, match boost; predictive audiences.
- Composable Audiences: connect warehouses (BigQuery, Databricks, Redshift, Snowflake) with user/event data models and build audiences over warehouse data — the composable/warehouse-native pole inside the same product.
- Governance/quality: data plans (schema enforcement, linting), rules, filters, consent filters, live stream (debugging), data catalog, observability, audit logs, user roles; data privacy controls, opt-out, Data Subject Request API, bulk profile deletion API.
- Abuse protection: profiles exceeding platform limits get a "Bad User" tag and fall out of audiences (documented thresholds: batch count >10,000, event count >20,000, 30 MB total events, profile >1 MB — vendor-specific, Research Notes only).

### Adobe Real-Time CDP

Evidence layer: A

Key observations:

- Self-description: "bring together known and anonymous data from multiple enterprise sources in order to create customer profiles that can be used to provide personalized customer experiences across all channels and devices in real time."
- Four documented pillars: (1) data ingestion & management (batch + streaming ingestion, source connectors, XDM schemas, datasets, queries); (2) profiles & audiences (Real-Time Customer Profile, Identity service, Segmentation service); (3) data governance & trust (data usage labels, policies, privacy service); (4) data activation (destinations catalog, activate audiences, export datasets).
- Real-Time Customer Profile: "holistic view of each individual customer by combining data from multiple channels, including online, offline, CRM, and third party"; profile = primary entity composed of "traits, behaviors, and audience memberships"; record data (attributes) + time-series events (ExperienceEvent); supporting entities (dimensional/lookup, B2B entities for accounts/opportunities).
- Profile fragments vs merged profiles: each profile is composed of multiple fragments (one per primary identity per dataset) merged into a single view; merge policies determine conflict resolution and prioritization; union schemas provide the merged view.
- Identity Service: links identities from multiple channels into an identity graph per customer.
- Segmentation: audiences built via Segment Builder / APIs; audience ID added to qualifying profiles' audience memberships; streaming segmentation evaluates data as it is ingested (real-time inclusion/exclusion); computed attributes summarize event data into profile attributes.
- Activation / destinations: profile export destinations (batch file-based e.g. S3; streaming "advanced enterprise" e.g. HTTP API, Kinesis, Event Hubs, Snowflake), streaming audience export destinations (advertising/social: Google DV360, Google Ads, Facebook — audience IDs/user IDs), edge personalization destinations (Adobe Target, custom personalization for same/next-page personalization), dataset export destinations, tag extensions (event forwarding). Audience types: people, account, prospect.
- Governance: data usage labels & policies enforced on marketing actions; opt-out handling; privacy service; sandboxes; attribute-based access control.
- B2B edition: account profiles, related accounts, predictive lead/account scoring, lead-to-account matching.
- Composable drift: Federated Audience Composition — "federate datasets directly from your existing data warehouse to create and enrich Adobe Experience Platform audiences and attributes"; partner data support (prospect profiles, hashed PII from data partners).

### BlueConic

Evidence layer: A

Key observations:

- Marketer-operated pure-play CDP; glossary centers on: Unified profile ("single, centralized source of truth for all customer data"), known profiles vs anonymous profiles ("anonymous behaviors are tracked and merged with known profiles once identification occurs"), profile merging (consolidating duplicates via configured rules), BlueConic ID (unique per profile), unique identifier (email, customer ID).
- Data capture: Listeners ("data collectors placed on channels to gather behavioral information"), external trackers, channels (websites/apps/accounts), first-party data emphasis ("consented customer data collected directly from interactions with your channels"), progressive profiling.
- Profile structure: profile properties (key/value pairs), behavioral profile properties (recency, frequency, intensity, momentum), timeline / timeline events (time-based actions like orders, email opens), groups (households, accounts), profile origins.
- Segments: "dynamic groups of profiles based on shared characteristics"; update in real time; multidimensional; no coding; known and anonymous users both segmentable; prebuilt behavioral segments (recency/frequency/intensity/momentum-based); a user can belong to multiple segments simultaneously.
- Connections: "data integrations with other systems (e.g., marketing platforms, CRMs). They enable data import and export between BlueConic and other platforms"; batch or real-time modes; SFTP/CSV import for lists.
- Execution surfaces (this pole goes beyond data infrastructure): Dialogues (on-site conversations/interactions triggered by profiles/behaviors), Lifecycles (journey orchestration across channels), AI Workbench (Python notebooks for CLV, churn propensity, profile enrichment), Simulator (test environment).
- Privacy: Objectives ("configured goals used to manage privacy and consent actions"), data sensitivity settings (PII vs non-PII by role), consent management.
- Administration: user roles/permissions, tenants (licensed instance with dedicated database), REST API.

### Tealium (AudienceStream)

Evidence layer: A

Key observations:

- Product map: iQ Tag Management (client-side) + EventStream API Hub (server-side collection, event specs, feeds, data quality) + AudienceStream CDP ("unify customer profiles, build custom audiences, and manage real-time personalization") + CloudStream ("activate customer data directly from your data cloud, without storing or loading data into Tealium" — composable pole) + DataAccess (long-term storage) + Predict (ML attributes) + Moments API (real-time profile retrieval for personalization) + consent management.
- Data model: events → visit attributes → visitor attributes; attribute types include badges, tallies, funnels, timelines, sets; enrichments (rules that transform/derive attribute values); offline/omnichannel data import; data sources (platform SDKs, file import CSV/SFTP, cloud data sources — Snowflake/Databricks/Redshift/BigQuery, incoming webhooks from tools like Braze/HubSpot/Iterable, /vdata enrichment endpoint).
- Visitor stitching (identity resolution): anonymous identifier (per visit/app use, generated by Tealium Collect), user identifier (email etc.), visitor ID attribute (populated from user IDs; combining profiles with same visitor ID value into one master profile); stitching "replays the data from each of the stitched profiles, in order of occurrence"; stitched profiles kept with `replaces`/`replaced by` links; anonymous ID still usable for lookup/deletion; stitching is real-time; profiles cannot be separated after stitching; visitor switching (two users sharing a device) handled as a special scenario; evaluation order: anonymous ID first, then user identifiers/visitor ID attributes.
- Audiences: rule conditions over attributes; audience sizing, discovery (Snowflake-based), AI recommendations; segments vs audiences distinction in product UI.
- Connectors (activation): ad-platform connectors prominent — Google Ads Customer Match, Facebook Conversions/Audiences, LinkedIn Matched Audiences, Google DV360, TikTok, Pinterest, Snapchat; also batched/delayed actions, frequency capping, webhook connectors, templates.
- Governance/validation: server-side consent (incl. Global Privacy Control, consent orchestration), trace (event-level debugging), event health, live visitors, visitor search, user permissions, save/publish versioning.

---

## Cross-product Comparison

| Dimension | Segment | mParticle | Adobe RT-CDP | BlueConic | Tealium AudienceStream |
|---|---|---|---|---|---|
| Persistent individual profile of record | Unified user/account profiles (Unify) | User Profiles with unique MPID | Real-Time Customer Profile (merged from fragments) | Unified profile (known + anonymous) | Visitor profile (master profile via stitching) |
| Multi-source ingestion | Sources: web/mobile/server SDKs, HTTP/pixel APIs, cloud-app sources | SDKs, Events API, partner feeds, CSV, warehouse sync | Batch + streaming ingestion, source connectors, Adobe solutions | Listeners on channels, connections import, SFTP/CSV | Data sources: SDKs, file import, cloud data, webhooks, tag management |
| Identity resolution | Identity Graph; cookie/device/email/custom IDs; anonymous stitching; merge protection | IDSync: identify/search/login/logout; 5 strategies; identity priority | Identity Service graphs; profile fragments + merge policies | Profile merging rules; anonymous→known merge on identification | Visitor stitching: anonymous ID + user identifier + visitor ID attribute; replay merge |
| Profile content | Events + traits (computed/SQL/predictions) | Identities, attributes, calculated attributes, events, memberships, consent | Record data + time-series events + audience memberships; computed attributes | Properties, behavioral properties, timeline events, groups | Visitor/visit/event attributes (badges, tallies, funnels, timelines), enrichments |
| Segmentation | Audiences (Engage) over profiles/traits | Audiences (real-time; predictive; composable over warehouse) | Segmentation service; streaming segmentation; audience memberships on profiles | Segments (dynamic, real-time, multidimensional, no-code) | Audiences over attributes (rule conditions; sizing/discovery) |
| Activation out | 400+ destinations; warehouses; Profile API (server-side); Engage Channels | Event outputs, audience outputs (ad/social), Profile API, Firehose | Profile export (batch/streaming), audience export (ad/social), edge personalization, dataset export | Connections (import/export, batch or real-time) | Connectors (ad platforms first-class), webhooks, Moments API, DataAccess |
| Consent/privacy | Privacy docs area; (details not sampled deeply) | Consent filters, DSR API, bulk deletion, opt-out, data privacy controls | Data governance labels/policies, privacy service, opt-out, ABAC | Objectives (consent), data sensitivity (PII roles) | Server-side consent, GPC, consent orchestration |
| Real-time posture | Real-time event routing; profile merges real-time | Real-time Profile API; audiences | Streaming ingestion + streaming segmentation; edge personalization | Real-time segments; real-time dialogues | Real-time stitching and audience actions |
| Composable/warehouse pole | Warehouses first-class (raw events out); SQL Traits in | Composable Audiences over BigQuery/Databricks/Redshift/Snowflake | Federated Audience Composition (federate warehouse datasets) | — (SFTP/CSV import; no documented warehouse-native pole in sampled pages) | CloudStream (activate from data cloud without storing); cloud data sources |
| Execution beyond data | Engage Channels (SMS/email/WhatsApp) | — (activation only) | — (activation only; Journey Optimizer is a sibling product) | Dialogues, Lifecycles (on-site/journey execution) | — (activation only) |
| B2B/account layer | Group call; user:account graph; account-level traits | Household reach (household grouping) | B2B edition: accounts, opportunities, lead-to-account matching | Groups (households, accounts) | — (not sampled) |

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

A Customer Data Platform is definable by three jointly-held structures:

1. **The persistent individual customer profile of record** — a durable, individually addressable record per person (known or anonymous), accumulating attributes and behavior over time. It persists across sessions, channels, and systems; it is the system's central object.
   - Remove → an event pipeline / analytics tool (events without a durable per-person record).
2. **Multi-source consolidation with identity linkage** — customer data from multiple source systems and channels is continuously ingested and attached to the *right* profile via identity resolution (linking records, devices, and events to the same individual).
   - Remove → a single-source contact database (CRM territory) or a raw event store.
3. **Outbound availability of profiles and derived audiences** — profiles and profile-derived segments are selectable and delivered to other systems (ad platforms, messaging tools, personalization surfaces, warehouses) for use there.
   - Remove → a customer analytics database / data warehouse (data in, no activation out).

Jointly-held is load-bearing:

- 1+2 without 3 = customer data warehouse / analytics (no activation)
- 1+3 without 2 = contact database with export (no unification — CRM-like)
- 2+3 without 1 = event router / audience tool without durable profiles (DMP-like)

Historical / market-sample check (per §24 reasoning): a pre-CDP-era marketing customer database — unified customer master records assembled from multiple source systems, with list extracts sent to mail houses — satisfies all three legs without cloud, SDKs, real-time, or identity graphs. The definition therefore does not over-fit to the modern SaaS implementation. Conversely, a cookie-era DMP fails leg 1 (audience-level, non-persistent cookie pools, third-party-centric), and a CRM fails leg 2 (single system of record, not multi-source consolidation).

### L1 — Common Mature Structure

Present across the sample (evidence layer B), but not required to recognize the Type:

- Identity graphs with anonymous→known stitching (all 5)
- Event/behavioral data model: attributes + time-series events on the profile (all 5)
- Derived/computed profile attributes (Segment computed traits, mParticle calculated attributes, Adobe computed attributes, BlueConic behavioral properties/AI notebooks, Tealium enrichments/badges)
- Rule-based segmentation engines with real-time/streaming and batch evaluation (all 5)
- Destination/integration catalogs for activation — ad platforms, messaging/email tools, analytics, warehouses (all 5)
- Profile explorer/search UIs (mParticle User Profiles, Tealium visitor search, Segment Profile explorer, Adobe profile UI, BlueConic profile views)
- Consent/privacy machinery: opt-out, data subject requests, deletion, consent-gated processing (mParticle, Adobe, BlueConic, Tealium directly observed; Segment privacy area exists but was not sampled deeply)
- Data quality/validation layers: data plans/event specs, live streams/trace debugging (mParticle, Tealium, Segment Protocols)
- Real-time profile APIs for in-session personalization (Segment Profile API, mParticle Profile API, Tealium Moments API, Adobe edge personalization)
- Warehouse interop in both directions (all 5 in some form)

### L2 — Variant / Optional Structure

- Packaging posture: packaged CDP with own profile store vs composable/warehouse-native (mParticle Composable Audiences, Adobe Federated Audience Composition, Tealium CloudStream) vs event-pipeline-first (Segment's origins)
- B2B/account-level profiles and account audiences (Segment user:account, Adobe B2B edition, BlueConic groups; mParticle household reach is the consumer-household analog)
- Predictive/AI attributes and audiences (mParticle Predictions, Tealium Predict, Adobe Customer AI, BlueConic AI Workbench, Segment Predictions)
- On-site/journey execution surfaces (BlueConic Dialogues/Lifecycles — the pole that drifts toward personalization/execution territory)
- Household/grouping layers above the individual (mParticle households, BlueConic groups, Adobe B2B entities)
- Partner/third-party data enrichment and prospecting profiles (Adobe partner data support; BlueConic second/third-party data glossary entries)
- Data hosting regions/localization, sandboxes/environments, industry editions (Adobe B2B/B2C editions)
- Deployment: SaaS multi-tenant vs dedicated tenant (BlueConic tenant concept)

### L3 — Vendor-specific Structure (Research Notes only)

- mParticle: MPID, "Bad User" tag with documented thresholds, named identity strategies (profile conversion/link/isolation/best match), Firehose API, Smartype, value-based pricing metering
- Adobe: XDM schema classes (Individual Profile, ExperienceEvent), merge policies, union schemas, profile fragments, sandboxes, RT-CDP Prime/Ultimate editions, Destination SDK, Federated Audience Composition
- Segment: writeKeys, Spec methods naming (Identify/Page/Screen/Track), Protocols, Engage tier gating, case-insensitive identifier handling, Merge Protection priority-trust algorithm
- Tealium: TAPID cookie, visitor-stitching replay mechanism, `replaces`/`replaced by` profile links, badges/tally/funnel attribute types, iQ tag management lineage, Moments API
- BlueConic: Listeners, Dialogues, Lifecycles, AI Workbench notebooks, Simulator, Objectives, tenant model, prebuilt behavioral segments with score ranges (e.g., "high intensity ≥ 85/100")

## Vendor-specific Findings

- BlueConic is the only sampled product whose documented surface includes first-party on-site interaction execution (Dialogues) and lifecycle orchestration as core product areas — a packaging variant that drifts toward Marketing Personalization territory. Not generalizable.
- Segment's identity graph explicitly supports user:account (B2B) relationships via the Group call; mParticle's analog is household reach; Adobe's is the B2B edition. Account-level CDP is common but implemented very differently.
- Adobe exposes merge policies and union schemas as user-managed objects; Segment exposes merge protection as an automatic algorithm; Tealium exposes stitching merge rules and evaluation order; mParticle exposes identity strategies. Same concept (conflict/merge governance), four different control surfaces.
- Tealium documents that stitched profiles cannot be separated after stitching; mParticle documents identity history with triggering events. Reversibility of identity merges varies and is not generalizable from the sample.

## Boundary Findings

- **vs Data Management Platform / DMP**: the DMP is audience-centric, historically cookie/third-party-data-centric, with short-lived anonymous audience pools. The CDP is profile-of-record-centric: persistent, individual-level, first-party-led, with identity resolution across systems. Remove persistence + individual-of-record + multi-source consolidation → DMP. Market convergence note: with third-party cookie deprecation, DMPs have largely collapsed into CDP-like or warehouse-like postures; the sampled CDPs all emphasize first-party data.
- **vs CRM**: CRM is a system of engagement/record for sales/service relationships — its contact/account records are created and operated inside the CRM by sales staff. A CDP consolidates data *from* systems (often including the CRM) and serves profiles *to* other systems; its users are marketing/data teams, not deal owners. Remove multi-source consolidation + activation-to-other-systems → CRM. (Adobe explicitly lists CRM as one of the *sources* feeding the profile.)
- **vs Marketing Automation Platform**: MA owns campaign execution on owned channels (email/SMS journeys) over its own contact store. The CDP's profile store exists to serve *other* systems, including MA platforms. Overlap is real (Engage Channels, BlueConic Dialogues) — the seam is whether the profile-of-record + multi-source unification is the product's center or a side database.
- **vs Data Warehouse / Reverse ETL**: the warehouse is the analytical system of record for all enterprise data (tables, SQL, BI); it does not maintain activation-ready individual profiles as its central object. Reverse ETL activates warehouse data without owning a profile of record. The composable-CDP movement (mParticle Composable Audiences, Adobe Federated Audience Composition, Tealium CloudStream) deliberately blurs this seam: CDP functions (identity, audiences, activation) layered over warehouse data. Recorded as a taxonomy tension, not resolved by merging the types.
- **vs Customer Identity / CIAM**: CIAM authenticates customers and manages identity lifecycles (registration, login, consent-to-terms). The CDP *consumes* identity signals (login events, emails) as resolution inputs but does not authenticate anyone and holds no credentials.
- **vs Audience Management Platform** (directory sibling in §06): audience-centric management (building/managing targetable audiences, often lookalike/suppression) vs the CDP's profile-of-record + unification center. The CDP *produces* audiences as an output; an audience management platform holds audiences as the primary object. Keep separate; flag in STATUS.
- **vs Marketing Personalization Platform**: personalization platforms own the decisioning/delivery of individualized experiences. The CDP supplies profiles/audiences *to* personalization (Adobe edge personalization destinations, mParticle/Segment Profile APIs are the seam surfaces). BlueConic's Dialogues sit closest to this boundary.

## Uncertainties

- Segment's privacy/consent machinery was not sampled at page depth (only the docs area was noted); consent claims for Segment are held at low strength.
- BlueConic's warehouse-native/composable posture was not found in the sampled pages; absence of evidence is not evidence of absence — held as "not sampled" rather than "not offered".
- Adobe Real-Time CDP is inseparable from Adobe Experience Platform in documentation; the research treats RT-CDP as the CDP packaging of platform services. Whether "RT-CDP" would satisfy the L0 legs if stripped of platform services was not independently testable.
- Pricing/tier gating (e.g., Segment Engage requiring Business tier; Adobe Ultimate-only streaming profile export) was observed but deliberately excluded from the final document as plan-specific detail.
- The exact market share/positioning of composable vs packaged CDPs was not researched (no third-party market reports fetched); the composable pole is documented only as observed product capabilities.

## Final Synthesis

The Customer Data Platform is best understood as **customer data infrastructure whose product is the unified customer profile itself**: it continuously consolidates multi-source customer data into persistent individual profiles (via identity resolution), derives attributes and audiences from those profiles, and makes both available to other systems for marketing and engagement use.

The defining core is the jointly-held triple: persistent individual profile of record + multi-source consolidation with identity linkage + outbound activation. Everything else — identity graph sophistication, streaming vs batch, destination catalogs, consent machinery, AI attributes, warehouse interop, execution surfaces — is common mature structure or variant structure.

The Type's deepest current tension is packaging: packaged CDPs with their own profile stores vs composable CDPs layering the same functions over customer-owned warehouses. Both satisfy the L0 legs; the profile-of-record function simply changes substrate. The Type's sharpest boundaries are against CRM (single-source relationship system vs multi-source data infrastructure), DMP (non-persistent audience pools vs persistent profiles), and MA platforms (campaign execution vs profile infrastructure).
