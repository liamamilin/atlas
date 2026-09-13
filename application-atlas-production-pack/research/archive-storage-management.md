# Research Notes — Archive Storage Management

## Research Goal

Understand what "Archive Storage Management" is as an Application Type in the IT / Cloud & Infrastructure domain: what systems of this type actually manage, what objects exist inside them, how data flows into and out of archive storage, how retrieval differs from normal access, and where the boundary lies against Storage Management, Backup Management, and Disaster Recovery.

## Initial Boundary

Working hypothesis at start:

- This is the storage-infrastructure application that governs long-term retention of cold data in a lower-cost archive tier: transition policies, archive destinations (cloud archive classes, object storage, tape), retrieval/rehydration semantics, retention, and cost visibility.
- Nearest neighbors in the directory: Storage Management (leaf directly above), Backup Management, Disaster Recovery Platform, Capacity Management, Cloud Cost Management / FinOps.
- Name-collision guards: "Archives Management System" (§23, institutional archives of cultural/records material) and "Web Archive Viewer" (§02.01) are unrelated Types. Email archiving / records management are content-type governance Types, not storage-infrastructure management.
- Risk: the Type could be an alias of Storage Management or a capability of Backup Management. This was a central research question.

## Research Questions

1. What does "archive" mean as a storage destination — and what distinguishes an archive tier from a backup copy, a cold tier, and a records repository?
2. What triggers transition of data into archive storage (age, access pattern, size, event, operator action)?
3. What are retrieval semantics — what must happen before archived data is usable again, and how does that differ across products?
4. What management surfaces exist (policy configuration, analytics, inventory, cost, retrieval operations)?
5. What substrates host archive storage (cloud object tiers, on-prem object, tape libraries, hybrid gateways)?
6. How do retention / immutability / compliance mechanisms appear?
7. Who operates these systems and why?
8. Where is the line against Storage Management, Backup Management, and Disaster Recovery?

## Representative Products

| Product | Philosophy / segment | Documentation quality |
|---|---|---|
| Amazon S3 storage classes + S3 Lifecycle (incl. S3 Glacier classes) | cloud-native: archive as storage class of the object service, managed by bucket lifecycle configuration | Tier 1 user guide, fully reachable |
| Azure Blob Storage archive tier + lifecycle management policies | cloud-native sibling with different retrieval semantics (explicit rehydration path with priorities) | Tier 1 docs (Microsoft Learn), fully reachable |
| Komprise Intelligent Data Management (Transparent Move Technology) | vendor-neutral unstructured-data tiering: analytics-driven, cross-NAS/cloud, transparent file access | Tier 2 product pages; official docs portal not fetched |
| QStar Archive Manager / Network Migrator | on-prem/hybrid active archive: virtualize disk + object + tape behind file/S3 interfaces, policy-based migration | Tier 2 product pages + solution pages |
| Veeam Backup & Replication Capacity Tier / Archive Tier | boundary sample: archive tier as part of a backup repository | Tier 1 user guide (help center), reachable |

Selection rationale: two hyperscalers (different retrieval models), one vendor-neutral tiering manager, one tape/active-archive specialist, one backup vendor used explicitly to test the backup boundary. Different philosophies (config-in-service vs external manager vs gateway-virtualized archive) and different customer layers (hyperscaler self-service through specialist appliance-oriented vendors).

## Sources

- AWS — Managing the lifecycle of objects: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html
- AWS — Understanding and managing Amazon S3 storage classes: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html
- Azure — Blob Storage lifecycle management overview: https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview
- Azure — Blob rehydration from the archive tier: https://learn.microsoft.com/en-us/azure/storage/blobs/archive-rehydrate-overview
- Komprise — product site and Transparent Move Technology page: https://www.komprise.com/ , https://www.komprise.com/product/transparent-move-technology/
- QStar — company/product pages: https://www.qstar.com/ , https://www.qstar.com/archive-manager/
- Veeam — Capacity Tier (User Guide for VMware vSphere): https://helpcenter.veeam.com/docs/backup/vsphere/capacity_tier.html

Research date: 2026-09-06. All fetches succeeded on first attempt except komprise.com/products/ (404; root and TMT pages fetched successfully — no source abandoned).

Sourcing limitation: Komprise and QStar evidence comes from official product/solution pages (Tier 2), not operational manuals; their operational claims (dynamic links, symlink access, agentless operation, streaming recall) are vendor-documented, not independently verified. Komprise's dedicated docs portal was not fetched. No precise operational figures are asserted for these two vendors.

## Product A — Amazon S3 (Glacier storage classes + S3 Lifecycle) [Evidence layer A]

Key observations:

- The archive is a **storage class** of the object service. S3 Glacier Instant Retrieval / S3 Glacier Flexible Retrieval / S3 Glacier Deep Archive are "designed for low-cost, long-term data storage and data archiving", with **minimum storage durations** and **retrieval fees** ("making them most effective for rarely accessed data").
- The defining management artifact is the **S3 Lifecycle configuration**: "a set of rules that define actions that Amazon S3 applies to a group of objects". Two action types: **transition actions** (when objects move to another storage class — e.g., "archive objects to the S3 Glacier Flexible Retrieval storage class one year after creating them") and **expiration actions** (when objects are deleted at end of life, e.g., "after they have been stored for a regulatory compliance period").
- Rules select objects by scope (bucket-wide, prefixes, tags, object size, current vs previous versions — referenced in the topics list) and time conditions on the object.
- Rules apply to **existing and future objects**: adding a rule causes eligible existing objects to be queued for the same action.
- Billing follows eligibility, not completion: "if an object is scheduled to expire and Amazon S3 doesn't immediately expire the object, you won't be charged for storage after the expiration time."
- Archived objects (Glacier Flexible Retrieval, Deep Archive) are "archived, and not available for real-time access"; you "must first restore archived objects before you can access them" (RestoreObject per the topic list). Glacier Instant Retrieval keeps millisecond access with per-GB retrieval fees — a graded spectrum inside one vendor's classes.
- Retrieval-time shapes differ by class: Flexible Retrieval "retrieval times of minutes to hours", Deep Archive "retrieval times of hours"; availability is stated "after you restore objects".
- Cost mechanics are part of the management model: transition requests carry costs; ingestion/transition costs should be weighed before moving data; per-GB retrieval fees apply to archive classes.
- Monitoring exists for the effect of lifecycle rules ("How do I monitor the actions taken by my lifecycle rules?").
- Archive use cases named in official text: "digital media, financial, and healthcare records, raw genomics sequence data, long-term database backups, and data that must be retained for regulatory compliance."
- S3 Intelligent-Tiering exists as an automatic alternative: objects move between access tiers on non-access (30/90-day tiers, optional 90/180-day archive tiers, restore-before-access for the deep tiers) — the vendor's automated policy posture inside a storage class.
- Interesting rule-interaction fact: "You can't use a bucket policy to prevent deletions or transitions by an S3 Lifecycle rule" — the lifecycle policy operates as a system-level governance instrument over the data, above access policies.

## Product B — Azure Blob Storage (archive tier + lifecycle management policies) [Evidence layer A]

Key observations:

- Same conceptual shape: "blob lifecycle management" = "rule-based policies that automatically transition data to cooler tiers or expire it". A policy is "a collection of rules in a JSON document"; each rule = conditions (creation / last-modified / last-accessed time) + filters (path prefixes, blob index tags) + actions (tier change or delete).
- Scope selection: rules apply to an entire storage account, select containers, or subsets via prefixes/tags.
- **Archive tier semantics**: "While a blob is in the archive access tier, it's considered to be offline and can't be read or modified. To access its data, first rehydrate the blob to an online tier: hot, cool, or cold."
- Two rehydration methods: copy the archived blob to a new online-tier blob, or change the blob's tier (Set Blob Tier). "You can't directly rehydrate archived snapshots or previous versions."
- Rehydration has **priorities**: Standard (default; "might take up to 15 hours" for objects under 10 GB) vs High ("might complete in less than one hour"; costs more; account-level throughput limit "10 GiB per storage account ... per hour with priority retrieval"). High priority is explicitly "reserve[d] ... for emergency data restoration."
- Completion is observable: Get Blob Properties polling, or Event Grid `BlobTierChanged` completion events.
- **Rehydration is not an access state but a tier change** — and the lifecycle policy can immediately re-archive rehydrated data (policy thresholds keyed on last-modified time); Azure documents a guard condition (`daysAfterLastTierChangeGreaterThan`) to prevent that. This is a directly observed policy/retrieval interaction.
- Minimum duration: archive-tier blobs "should be stored for a minimum of 180 days"; deleting or re-tiering earlier "incurs an early deletion fee."
- Execution model: policy runs are periodic ("processes objects periodically"); changes take up to 24 hours to take effect; a run in progress continues if the policy is deleted; run progress observable via events/metrics/logs.
- Billing model of management itself: "Lifecycle management policies are free of charge" — billed for the underlying Set Blob Tier operations.
- Deletion/retention interactions documented: lifecycle delete doesn't work on immutable containers; soft-delete retains deleted blobs for the soft-delete window.
- Access-time tracking can be enabled to drive last-accessed conditions ("billed ... at most once every 24 hours per object") — access-pattern conditions are a first-class policy input.

## Product C — Komprise (Intelligent Data Management / Transparent Move Technology) [Evidence layer B/A− (vendor-documented)]

Key observations (vendor product pages):

- Positioning: unstructured data management — "Discover, curate and prepare AI-ready enterprise data"; tiering is one data service among analysis, migration, classification, workflows. The Type-relevant module is **transparent data tiering**: "Find and tier cold data seamlessly across any NAS, cloud, object."
- Core mechanism (TMT): "File tiering moves cold data to low-cost storage but **preserves access via the original path**"; "Users open tiered files exactly as they always have via symbolic links"; "no stubs, agents, or proprietary formats"; "never in the hot data path — no impact on performance or active workloads."
- **File/object duality**: "Moved data is accessible as native objects at the cloud destination" — written in the target's format, readable with a standard S3 browser; "open standards (NFS/SMB/S3) ensure long-term portability"; "no rehydration when switching vendors."
- Policy inputs: "a range of ages as well as exclusions based on size, file type, directory ... granularly specify what to tier based on custom queries."
- Retrieval semantics: on-access recall is configurable ("configure just when an accessed data is rehydrated"); streaming access ("does not wait for the entire file to be read"; local caching for subsequent requests); **bulk recall** feature for bringing back large sets.
- Contrast table vs storage-array block tiering (NetApp FabricPool / Dell CloudPools named as the compared category): array tiering "can only specify an age", rehydrates "immediately" on access into reserved space, stores data in proprietary form, is per-cluster. Komprise claims cross-vendor single pane, granular policies, native-format targets, no vendor lock-in. (The contrast is marketing-framed but establishes the vendor-neutral posture and the two access models.)
- Estate analytics precede tiering: "deep insights into usage, aging, and access patterns", hot/cold analysis, duplicates, growth, savings modeling ("Estimate capacity, savings with interactive model tailored to your costs"), showback/chargeback reporting.
- Side effects claimed: backup scope shrinks as files move off primary ("Cuts storage + backup + DR costs"); ransomware surface shrinks by tiering to **immutable** object storage.
- "Zero rehydration penalty" is the vendor's headline differentiator — retrieval-on-access without a formal restore step.

## Product D — QStar (Archive Manager + Network Migrator + Storage Reporter) [Evidence layer B/A− (vendor-documented)]

Key observations (vendor pages):

- "QStar is the leading global provider of enterprise-class archive and data management software solutions ... Our software **virtualizes any archive technology behind a file system or S3 compatible interface**, making the entire archive appear as one or more NAS disks or cloud buckets."
- **Archive Manager** "manages a range of storage technologies such as Tape Libraries, Object Storage, Disk Array, and Cloud (private, public and hybrid) to form an efficient, safe and cost-effective **Active Archive** environment by virtualizing differing storage technologies behind a file system or cloud interface. Users see ordinary file shares or S3 buckets and can easily **search, find and retrieve data directly from the archive**."
- Access is native and application-transparent: "POSIX, NTFS, S3 and Web Services support ... any local application immediate access ... without any modification ... the user's data access experience remains exactly the same." Data can be written with one protocol and read with another.
- **Active Archive** doctrine: "make all content available online or near online (in the case of tape libraries) whilst leveraging low-cost storage"; "does not require separate backup processes."
- **Network Migrator** is "a policy based tiered storage and data lifecycle manager ... uses advanced policy management to **monitor and automatically migrate, copy or move less frequently used files** from primary storage to tiered storage or else to a central archive or Cloud Storage" — agent-per-server deployment (Windows/UNIX/Linux/Mac) plus APIs for closed file systems. Backup-window reduction is an explicit rationale ("only the most recent or frequently changing files are included in the backup process").
- **Storage Reporter**: scan-based assessment of storage composition ("detailed analysis of data composition in the existing storage infrastructure"), results in a database, simulated reports ("determining how the storage would look after a migration").
- Technology selection logic is data-access- and retention-driven: "Archive data that is likely to be accessed during its archive life should be stored on random-access media ... Where data has little chance of being recalled ... tape"; "Data retention regulations will be the driving factor for how long data will reside in the archive and often what archive technology is most suitable."
- Adjacent products in the family: Archive Replicator / Disaster Prevention (archive replication to 2–4 targets), Q-WORM (immutability), Global ArchiveSpace (multi-node tape gateway for HPC-scale), certified "Long-Term Archive" integrations for backup vendors (Rubrik/Cohesity/Veeam/HYCU pages exist).
- Customer base visible on page: national archives, national libraries, government, universities, media (DreamWorks, Discovery), HPC (ISRO, MIT LL), finance — the regulated/permanent-retention segment.

## Product E — Veeam Backup & Replication (Capacity Tier / Archive Tier) [Evidence layer A — boundary sample]

Key observations (help center, Capacity Tier page + TOC structure):

- "Capacity tier is an additional tier of storage that can be attached to a **scale-out backup repository**. Data from the scale-out backup repository **performance extents** can be transported to the capacity tier **for long-term storage**."
- Mechanisms: "Move inactive backup chains to capacity extents", "Copy new backup files as soon as these files are created", manual move, "Download data that was moved from capacity extents back to the performance extents", "Restore from Capacity Tier".
- A separate **Archive Tier** exists ("long-term retention of backups", with its own limitations/immutability/encryption/restore pages), and Amazon S3 Glacier storage can be added as an object-storage target ("Adding Amazon S3 Glacier Storage").
- Session statistics for offload operations are viewable ("Viewing Capacity Tier Sessions Statistics").
- The unit of tiering is the **backup file/chain** — not production data. The archive tier here is governed by backup-job retention and repository design, not by data-age policies over live data.
- QStar's site corroborates the same pattern from the other side: certified "Long-Term Archive" target products for Rubrik/Cohesity/Veeam/HYCU — backup platforms offload long-term retention to archive targets.

→ This confirms the boundary: backup products carry an **archive-tier capability** (long-term storage of backup copies), while the dedicated Type manages archive storage for the organization's data (production data or storage-class policy), with the backup relationship appearing as a rationale (smaller backup scope) rather than as the object of work.

## Cross-product Comparison

| Dimension | AWS S3 lifecycle + Glacier classes | Azure Blob lifecycle + archive tier | Komprise TMT | QStar Archive Manager / Network Migrator | Veeam Capacity/Archive Tier |
|---|---|---|---|---|---|
| Archive destination | storage classes of the object service (Glacier IR / Flexible / Deep) | archive access tier of the blob service | low-cost cloud/object storage targets (vendor-neutral) | virtualized pool of tape libraries / object / disk / cloud behind file or S3 interface | capacity/archive extents of a backup repository |
| Transition governance | bucket lifecycle rules (age, scope, size, versions); or Intelligent-Tiering automatic | lifecycle policy JSON (time conditions + prefix/tag filters, tierToArchive/delete actions) | tiering policies by age/size/type/directory/custom queries; policy-driven, continuous | policy-based migration ("monitor and automatically migrate, copy or move less frequently used files") | move/copy policies for inactive/new backup chains, plus manual move |
| State of archived data | offline for Flexible/Deep ("must first restore"); instant-access variant exists | offline ("can't be read or modified" until rehydrated) | addressable in place via original path (dynamic links / symlinks); native objects at target | online/near-online via ordinary file shares or S3 buckets ("search, find and retrieve directly") | backup files in object storage; restore via backup application |
| Retrieval path | RestoreObject (restore before access; retrieval fees; minutes-to-hours per class) | rehydrate = Set Blob Tier or Copy Blob to online tier; Standard/High priority; completion events | configurable on-access recall + streaming + bulk recall; no separate restore ceremony | read directly from archive interface (near-line tape recall handled by the system) | download back to performance extents / restore from tier |
| Planning/analytics | Storage Class Analysis (topic in guide) | access-time tracking, metrics/logs, events | estate analysis: hot/cold, age, duplicates, savings modeling, showback | Storage Reporter scans + simulated reports | session statistics |
| End-of-life handling | expiration actions (delete at retention end) | delete actions (blocked by immutability/soft-delete interactions) | tiering to immutable tiers (deletion governance not primary) | retention regulations drive duration & technology; replication for durability | backup retention policy governs removal |
| Primary driver named by vendor | "store objects cost effectively throughout their lifecycle"; regulatory retention | "proactively optimize costs"; retention through immutable interplay | "cut 70% of costs"; ransomware surface; no lock-in | lowest TCO for long-term retention; regulated archives | long-term retention of backups |
| Operator | cloud admin (console/CLI/API/IaC) | cloud admin | storage/data-management team | storage admin / archive operator | backup admin |

Stable commonalities (B-layer):

1. A **distinct archive destination** whose access is constrained or delayed relative to active storage, chosen for low long-term cost.
2. **Rule- or policy-governed transition** of data into it over time (age / last access / size / scope / event / explicit operator action).
3. A **defined retrieval path back** that is a distinct, slower operation than normal access (restore, rehydrate, recall, download-back).
4. **Monitoring/reporting** of transitions and their effect (sessions, events, metrics, savings).
5. An **administration surface** for registering targets/sources and authoring policies.
6. Cost accounting woven through the model (retrieval fees, minimum durations, savings reporting) — the economic "why" is universally present.

## Canonical Model (abstraction layers)

### L0 — Defining Invariant (minimal)

Archive Storage Management = governing the retirement of data from active storage into a dedicated archive destination, and the path back:

```text
Archive destination   — a storage tier/target distinct from active storage,
                        with lower cost and constrained/delayed access semantics
Governed transition   — rules or explicit operator-governed actions that determine
                        what moves into the archive and when
Retrieval path        — a defined, distinct operation (restore / rehydrate /
                        recall) that returns archived data to usable access
```

Removal tests:
- Remove the archive destination's distinct access semantics (data stays normally readable at full speed) → ordinary storage tiering/capacity management, not archive.
- Remove governed transition (no mechanism determines what goes where over time) → it is just a cold storage volume/file share, not a management application.
- Remove a retrieval path (data in, nothing out) → it is a write-once sink, not archive management.

Historical check: classic HSM systems (policy-based migration of files to tape with stubs, recall on access), tape-based national-archive systems, and modern cloud storage-class management all satisfy the triple. The definition does not depend on cloud, object storage, stubs, links, or any specific retrieval-time figure.

### L1 — Common Mature Structure

- Policy configuration surface (scope/condition/action rules) with periodic or continuous execution
- Transition monitoring (sessions, events, metrics) and lifecycle-integration events
- Estate analytics to plan tiering (hot/cold, age, access patterns, duplicates) and savings estimation/reporting
- Inventory / continuous view of what is archived, with search
- End-of-life actions (expiration/deletion at retention end) alongside tier-down actions
- Cost accounting: retrieval-fee awareness, minimum-duration economics, showback/chargeback
- Registered sources & destinations management (accounts, buckets, NAS, libraries)
- Admin vs requester role separation (operators configure; data owners request retrievals)

### L2 — Variant / Optional Structure

- Substrate: cloud object storage classes / on-prem object / tape libraries / hybrid gateways
- Archived-state access model: fully offline (explicit restore/rehydrate before read) vs near-online active archive (file/S3 interface with system-handled recall) vs transparent on-access (links, streaming recall)
- Retrieval priority/cost options (e.g., standard vs high-priority rehydration) and temporary-restore semantics
- Automatic tiering (system-decided, access-pattern-driven) vs declared rules vs operator-initiated moves
- Immutability / WORM retention for regulated archives
- Stub-based (classic HSM) vs stub-free/link-based (modern file tiering) representation of tiered files
- Vendor-neutral multi-target architecture vs single-ecosystem (cloud-native) management
- Backup-integrated archive tiers (long-term retention of backup copies) vs production-data archiving
- Replication of archives for durability/DR (2–4 targets) as an add-on capability

### L3 — Vendor-specific (research notes only)

- Azure: JSON policy document; ≤10 prefixes and ≤10 index-tag conditions per rule; policies free, Set Blob Tier billed; last-access updates billed at most once per 24 h/object; `daysAfterLastTierChangeGreaterThan` guard against re-archiving; 180-day archive minimum duration; rehydration Standard "up to 15 hours" / High "less than one hour" for <10 GB objects; account-level 10 GiB/h priority-rehydration limit; snapshots/previous versions not directly rehydratable; no lifecycle rehydration (policies tier down only); immutable containers block lifecycle deletes; Event Grid `BlobTierChanged` completion event.
- AWS: lifecycle rules cannot be blocked by bucket policy; billing follows eligibility not completion; Glacier Flexible/Deep need RestoreObject first; class-level retrieval-time bands (Flexible minutes-to-hours; Deep hours); 40 KB/object archive metadata overhead; 128 KB min billable size on some classes; 30/90/180-day minimum durations across classes; Intelligent-Tiering monitoring fee model.
- Komprise: Transparent Move Technology™ (patented), Dynamic Links, showback/chargeback UI, Elastic Shares, Global File Index / Global Metadatabase Service, contrast positioning against NetApp FabricPool / Dell CloudPools block tiering.
- QStar: product family split (Archive Manager = virtualization gateway; Network Migrator = policy migration engine; Storage Reporter = assessment; Archive Replicator / Data Director = multi-target replication; Q-WORM = immutability; Global ArchiveSpace = multi-node HPC-scale tape gateway); LTFS/LTO lineage; certified long-term-archive integrations for backup vendors.

## Vendor-specific Findings

- Azure's documented re-archiving hazard (policy tiers data back to archive based on last-modified time; rehydrated blobs can bounce back unless the policy guards on tier-change time) is the clearest single illustration that **transition policy and retrieval interact** and that retrieval is a state change, not an access grant. Treated as a canonical behavior pattern (policy/access interaction), with the mechanism itself as vendor implementation.
- AWS's "lifecycle rules override bucket policies" is a governance-position statement: the lifecycle policy acts on behalf of the account owner over the whole dataset regardless of access controls. Canonicalized as "policies operate over scoped datasets, not per-user actions".
- Komprise and QStar both make backup-footprint reduction a first-class selling point of archiving production data — evidence for the archive↔backup relationship flowing both directions (archive shrinks backup; backup offloads long-term retention to archive targets).

## Boundary Findings

**vs Storage Management** — Storage Management runs the live storage estate (provisioning, capacity, health, replication of active data). Archive Storage Management centers on the governed retirement of data into an archive destination and its retrieval. Strip the archive destination + transition governance + retrieval semantics → generic Storage Management; keep them and the estate-operations focus disappears → Archive Storage Management. Adjacent, not alias. (Storage Management leaf not yet processed; no overlap conflict observed in the reachable evidence.)

**vs Backup Management** — Backup creates recovery copies under job schedules and restore-point retention (object of work = protection of systems/data). Archive retains data long-term under retention/cost policy (object of work = the data's storage lifecycle). Veeam evidence: even in backup products, the archive tier is a tier **of the backup repository**, moving backup files/chains, governed by backup retention — the archive capability embedded in the Backup Type. Komprise/QStar evidence: the dedicated Type archives **production data** (or manages archive storage classes) and treats smaller backup scope as a *consequence*. Center-of-gravity test: whose data is being moved — backup copies → Backup Management; the organization's cold data → this Type.

**vs Disaster Recovery Platform** — DR restores operability within recovery objectives after a site/system loss; archive retrieval is deliberately slow and is not an availability mechanism. Archive products may add replication for durability (QStar Archive Replicator / Disaster Prevention as named adjacent products), which remains an add-on capability, not the core.

**vs Enterprise Records Management** — ERM governs business records (declaration, schedules, legal hold, evidenced disposition of content). Archive Storage Management moves arbitrary data at the infrastructure layer under cost/age policy. Retention *inputs* may come from records policy, but the objects, users, and decisions differ (storage lifecycle vs record disposition).

**vs cold storage tiers themselves (cloud services)** — the leaf is the management application/layer (lifecycle rules, tiering policies, rehydration operations, reporting), not the storage engine. The clouds' archive tiers are the most common substrate, managed through this Type's policy surfaces.

**vs Archives Management System (§23) / Web Archive Viewer (§02.01)** — pure name collision; unrelated objects and users.

**Removal-test summary**: take away the archive destination's delayed-access semantics → capacity/tiering management; take away the retrieval path → write-once storage; take away transition governance → a cold file share; take away production-data scope (keep only backup copies) → the archive-tier capability inside Backup Management.

## Uncertainties

- Komprise/QStar operational detail rests on product pages, not manuals; the exact behavior of their recall and policy engines (e.g., what "dynamic links" resolve to under the hood beyond the documented symlink statement, retention enforcement depth) is vendor-claimed. Assertions about them are kept qualitative.
- Google Cloud's Archive storage class was not sampled (two hyperscalers already established the cloud-native pattern with A-layer evidence); no claims about it are made.
- The precise shape of retrieval pricing (per-GB vs per-request mix) is deliberately not asserted anywhere in the final document; only the existence of retrieval fees / priority premiums / minimum durations is claimed (directly observed on both cloud vendors).
- Whether the market ever offers a pure standalone "archive storage manager" UI without any tiering/analytics module is uncertain — the sampled dedicated vendors all bundle assessment (Komprise Analysis, QStar Storage Reporter). The final document therefore treats estate analytics as common, not core.
- Historical HSM fit is argued from the structure of the L0 triple, not from fetched HSM documentation (IBM/Oracle HSM docs not fetched); kept as reasoning, not sourced fact.

## Final Synthesis

Archive Storage Management is the application that governs an organization's long-retention cold data as it moves from active storage into a dedicated, lower-cost archive destination and (rarely) back. Its world has three load-bearing structures — the archive destination with constrained access semantics, governed transitions into it, and a defined retrieval path out — plus a common mature layer of policy configuration, estate analytics, transition monitoring, inventory, end-of-life actions, and cost accounting. The economic motive (cheaper long-term retention) is universal; the substrate (cloud classes, object, tape) and the archived-state access model (offline restore vs near-online recall vs transparent on-access) are the main axes of variation. The Type is distinct from Storage Management (estate operations), Backup Management (protection copies vs data lifecycle; backup products embed archive tiers as a capability), and Disaster Recovery (retrieval is not availability). The definition survives the historical check: tape-era HSM, national-archive tape systems, and modern cloud storage-class management all satisfy the same minimal triple.
