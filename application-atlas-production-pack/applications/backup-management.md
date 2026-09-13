# Backup Management

## Overview

A **Backup Management** application is the administrative control plane for data protection: an organization uses it to define which data and systems must be protected, to run scheduled backup jobs that store point-in-time copies on backup storage the application itself manages, and to restore data from those copies after loss, corruption, accidental deletion, or a destructive attack.

The defining core is small:

```text
Protected scope (workloads brought under protection)
└── Backup policy (what, where, when, how long to keep)
    └── Backup job execution
        └── Recovery points held on dedicated backup storage
            └── Restore from a chosen recovery point
```

Everything else commonly associated with modern backup products — agents, agentless hypervisor integration, deduplication, content catalogs, recovery verification, secondary copies, immutable storage, tape libraries, cold cloud tiers, disaster-recovery modules — is widespread in current products but is not what makes the application a backup application. Older tape-era network backup software and consumer disk-image tools fit the same definition without any of those specifics.

When the primary purpose shifts from *keeping restorable copies* to *administering production storage*, *orchestrating failover to secondary infrastructure*, or *retaining inactive records for compliance*, the product is drifting toward a different Application Type (Storage Management, Disaster Recovery Platform, Archive Storage Management).

## Users & Context

The primary users are IT operations people responsible for not losing data:

- **backup administrator / backup architect** — designs protection coverage: registers workloads, defines policies, manages backup storage and its capacity
- **backup operator / infrastructure administrator** — watches job results, fixes failed jobs, runs routine restores, handles retention requests
- **MSP service desk** (in managed-service deployments) — performs the same duties for many customer tenants from one console

Secondary users touch the system without running it daily:

- **security / incident response** — during a ransomware or data-destruction event, drives the recovery: choose clean recovery points, restore at scale
- **help desk / end users** — self-service recovery of individual files or mailbox items
- **compliance / audit** — consumes backup reports and evidence that protection ran and retention was honored

The work context ranges from self-hosted software managing a data center, to cloud consoles protecting a cloud subscription, to multi-tenant consoles operated on behalf of many client companies.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product is no longer recognizable as Backup Management:

- **Protected scope** — a managed registry of what is under protection: virtual machines, physical servers, databases, file shares, cloud resources, application data, endpoints. Workloads must be explicitly brought under protection (via an installed agent, an agentless hypervisor integration, or a cloud API assignment). Without this, the product is a copy tool or a storage service, not a protection management system.
- **Backup policy** — a persistent definition of how each protected item is copied: what to include and exclude, which backup storage to write to, when to run, and how long recovery points are kept. Without a policy layer, protection exists only as ad-hoc manual copies and is not *managed*.
- **Recovery points on dedicated backup storage** — each executed job stores a point-in-time copy in backup storage managed by the application (a repository, vault, or pool of backup media), separate from the source. Multiple recovery points accumulate per protected item and expire under the retention policy. Without retained points in time, the product is mirroring or syncing, not backup.
- **Restore** — the ability to recover data by selecting a protected item, a recovery point, and a target, executed as a tracked operation. Without restore, there is no backup application at all.

### Standard Capabilities of Mature Products

These are present in essentially all current products and make backup practical, but they are implementation and maturity layers rather than the definition:

- **Backup job execution and tracking** — the job is the unit of work; every run leaves a result (success, warning, failed) with logs, and failed jobs generate alerts. A backup environment is operated through this loop.
- **Central management console** — one administrative surface across many workloads: protection status, job history, alerts, reports, and configuration of targets and credentials.
- **Workload connectors** — agents for physical machines and endpoints, agentless integration for virtualization, native APIs for cloud resources, application plugins for databases and mail systems.
- **Storage efficiency** — incremental/differential/synthetic copy levels, deduplication, and compression so that frequent recovery points remain affordable.
- **Content catalog / index** — an index of what was backed up, enabling browsing and item-level recovery (single files, mailbox items, database objects) without restoring everything.
- **Restore granularity spectrum** — from full machine or VM recovery (including rapid-restart and bare-metal methods) down to single files or objects; restore to the original location or an alternate one.
- **Retention management** — expiration and pruning of aged recovery points, typically organized into separate retention generations (for example daily, weekly, monthly).
- **Secondary copies** — copy jobs that duplicate backup data to a second storage location, second site, second account, or offline media.
- **Recovery verification** — mechanisms to confirm copies are actually restorable (test restores, verification jobs, integrity checks).
- **Restore permissions and reporting** — control over who may restore what, plus reports and alerts for operations and compliance evidence.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. How specific products realize each concept varies widely:

```text
Concept:      Protected scope
Realized as:  agent installed on the machine, agentless hypervisor
              integration, cloud resource assignment (often by tag),
              SaaS application connector

Concept:      Backup policy
Realized as:  job definition wizard, backup plan applied to tagged
              resources, configuration-file resources on a server

Concept:      Backup storage
Realized as:  disk repository, deduplication appliance, cloud vault,
              pool of tape volumes, object-storage tiers

Concept:      Recovery point
Realized as:  restore point inside a backup file, vault-stored
              recovery point, labeled tape volume contents

Concept:      Catalog
Realized as:  database index, embedded index in backup files,
              per-resource-type native browse
```

A reader who has only seen one implementation (e.g. a cloud-managed vault service) should still recognize a 2000s tape-based network backup product from the Core Model — both fit.

## How It Works

### Bring workloads under protection

```text
Choose workload type (VM / server / database / file share / cloud resource / endpoint)
→ connect it (install agent, add hypervisor or cloud account, or assign resource)
→ workload appears in the protected inventory
```

### Define the backup policy

```text
Select what to protect (scope + exclusions)
→ choose backup storage target
→ set schedule and copy levels
→ set retention (how many points, or how long they are kept)
→ save the policy
```

The policy is persistent. It keeps applying on every schedule tick until someone changes or removes it. Some cloud-native products attach policies to resources by tag, so that newly created resources inherit protection automatically.

### Execute, monitor, and operate

```text
Scheduler triggers a backup job
→ source data is read (agent, hypervisor snapshot, or cloud API)
→ data is transferred, deduplicated/compressed, and written to backup storage
→ a new recovery point is registered
→ the run is recorded: succeeded / warning / failed
→ failures raise alerts and get fixed; the next run re-attempts
```

This configure → run → watch → repair loop is the daily operational life of the application. A backup job that silently fails leaves the organization unprotected without anyone noticing, so job-result visibility and alerting are treated as first-class behavior, not a reporting afterthought.

### Let retention run

Recovery points accumulate and age out. Aged points are pruned or deleted automatically; secondary copies replicate points to other storage or sites while they are still retained. Restore is only possible while a recovery point is within its retention window.

### Restore

```text
Pick the protected item
→ pick a recovery point (time)
→ choose granularity (entire machine / disk / file / application item)
→ choose target (original location or alternate)
→ run the restore as a tracked operation
```

Restores are themselves recorded jobs with results — particularly in incident response, where restoring many machines from known-clean recovery points is a coordinated operation.

### Core vs Common vs Optional

**Defining core** — without these, not Backup Management:

- protected scope under management
- backup policy (scope, target, schedule, retention)
- recovery points held on dedicated backup storage
- restore from a chosen recovery point

**Standard capabilities** — present in most mature products:

- job execution with tracked results and failure alerting
- central multi-workload console
- agent / agentless / API connectors
- incremental levels, deduplication, compression
- content catalog and item-level restore
- restore granularity spectrum and alternate-target restore
- retention expiration and pruning
- secondary copies
- recovery verification
- restore permissions, reports, notifications

**Variant / optional** — depends on era, segment, deployment, security posture:

- media substrate: tape libraries, disk, dedup appliances, object storage, cloud cold tiers
- immutability and anti-ransomware machinery: retention locking, malware scanning of backups, gated "safe" restores
- near-continuous copy cadence (CDP-style)
- SaaS application data, identity data, and endpoint coverage
- DR-adjacent modules: cloud failover from backups, replica failover, DR orchestration
- delivery and business form: self-hosted software, appliance, fully-managed cloud service, multi-tenant MSP platform, consumer product

## Interfaces

The following surfaces are described conceptually. Exact layouts and names vary by product, and the same functions may appear as a web console, a desktop application, or configuration files plus commands.

### Protected workload inventory

The entry surface listing everything under protection.

- typical information: workload name/type, protection state, last recovery point, policy attached
- primary actions: add workload, attach or detach policy, run backup now

### Policy / job editor

Where protection is defined — commonly a step-by-step wizard or a plan form.

- typical information: scope and exclusions, target storage, schedule, copy levels, retention rules
- primary actions: create/edit policy, save, assign to workloads

### Job / activity dashboard

The operational heart: what ran, what succeeded, what failed.

- typical information: job runs with status, durations, sizes, per-workload outcomes, history
- primary actions: filter failures, retry, edit schedule, configure alerts

### Restore browser

The recovery surface.

- typical information: workload → available recovery points → browsable content inside a point
- primary actions: select recovery point, choose files/objects or full recovery, pick destination, run restore

### Backup storage view

The custody surface.

- typical information: repositories/vaults, capacity and growth, recovery-point counts, secondary-copy status
- primary actions: add/extend storage, set immutability or tiering rules, manage copies

### Reports, alerts, administration

- reports on protection coverage, job success rates, retention and compliance evidence
- alert routing (email, webhook, monitoring integrations)
- administration: credentials, user roles, notification settings, backup infrastructure components

## Important Rules / Behaviors

### Recovery points, not mirrors

Backup storage deliberately does not track the source's current state. Data deleted from the source remains recoverable from earlier recovery points until retention expires — this is the structural difference from synchronization, and the reason backup survives destructive events (including human error and attacks on the source).

### Restore is bounded by retention

Once a recovery point is expired, pruned, or deleted, nothing within it can be restored. Retention settings therefore function as a data-protection contract; some products allow retention to be locked so it cannot be shortened even by administrators.

### Backup storage is a separate custody layer

Copies live in storage managed by the backup application, separate from the source. Products increasingly harden this boundary — access policies on the vault, independent encryption, write-once retention — because an attacker who controls the source should not automatically control the copies.

### A failed job is an unprotected workload

The meaningful state of the system is per-workload protection health, derived from the latest job results. Silent failure is the primary operational risk; hence alerting and success-rate reporting are structural.

### Consistency matters for applications

For databases and application servers, a raw copy taken mid-write may not be restorable cleanly. Mature products offer application-consistency mechanisms (quiescing, log handling) so that the recovery point is internally consistent; the achievable consistency depends on the workload type and connector.

### Restore is permissioned

Who may restore what — and to where — is administrable, because restore is also a data-exfiltration path. Larger deployments restrict restore rights and destinations independently of backup administration.

## Variants

Common forms of the Type:

- **virtualization-centric backup** — agentless protection of hypervisor VMs as the dominant workload, with image-level copies and rapid VM recovery (e.g. Veeam Backup & Replication)
- **enterprise data-protection suite** — one platform covering many workload classes with a control node and data movers, broad reporting and scale (e.g. Commvault)
- **cloud-native managed backup** — the backup layer is a managed cloud service: policies attached to tagged resources, vaults as custody, recovery points as first-class resources (e.g. AWS Backup, Azure Backup)
- **self-managed open-source network backup** — daemon architecture, configuration-file resources, catalog database, tape and disk media (e.g. Bacula)
- **MSP multi-tenant platform** — backup delivered as a service to many client companies from one console, one agent, per-workload billing (e.g. Acronis Cyber Protect Cloud)
- **endpoint/laptop backup** — bundled into endpoint or security suites; user-file and disk-image protection
- **SaaS data backup** — protecting cloud-application data (mailboxes, collaboration suites, identity objects) into separate custody
- **consumer disk-image backup** — personal machines, simple schedules, image restore; historically widespread
- **tape-era network backup** — historical form: scheduled jobs writing labeled tape volumes under rotation and retention rules; the defining core in its oldest implementation

A variant remains a Variant as long as the Core Model applies. When the recovery unit or the primary loop changes — failover orchestration instead of copy-and-restore, or record retention instead of recovery points — it is a different Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Disaster Recovery Platform | restores *service availability* by orchestrated failover to standing secondary infrastructure with recovery-time commitments; backup restores *data* from retained copies on (possibly the same) infrastructure. Backup vendors ship DR as separate modules; a backup application whose copy-and-restore loop is removed is not DR, and vice versa |
| Storage Management | administers production storage (capacity, performance, provisioning); backup merely writes to dedicated backup storage as a custody target. Administering the vault for its own sake is not backup, and backing it up is not storage administration |
| Archive Storage Management | keeps data no longer in active use for long-term, compliance-oriented retention, rarely restored and not rotated; backup keeps restore-oriented recovery points on schedules that expire. The seam blurs when backups are tiered to archive storage |
| File Sync Application | mirrors the current state of a file set across devices or locations; deletions usually propagate and history is incidental. Backup accumulates deliberate, policy-governed recovery points with an explicit restore path |
| Data Replication Platform | maintains continuously updated live copies in another system for availability or consumption; backup stores point-in-time positions in managed backup storage. Near-continuous CDP features straddle the seam; the restore-from-custody side is backup |
| Endpoint Management / UEM | administers devices (configuration, apps, security); backup may be bundled but device administration does not create recovery-point custody |
| Storage-system snapshots | snapshot features are a copy mechanism inside storage systems; backup products may leverage them but add cross-platform policy, catalog, retention, and restore. Snapshot tooling without managed recovery-point custody is not this Type |

## Representative Products

- Veeam Backup & Replication
- Commvault
- AWS Backup
- Bacula
- Acronis Cyber Protect Cloud

The Core Model was checked against cloud-native managed services (Microsoft Azure Backup as an additional sample), open-source tape-era lineage, and consumer disk-image backup tools to avoid over-fitting the definition to the current virtualization/cloud pattern.

## Sources

Research date: **2026-09-06**

- Veeam — Veeam Backup & Replication 13 User Guide, "About" and "Creating Backup Jobs": https://helpcenter.veeam.com/docs/backup/vsphere/overview.html , https://helpcenter.veeam.com/docs/backup/vsphere/backup_job.html
- AWS — AWS Backup Developer Guide, "What is AWS Backup?": https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
- Microsoft — "What is Azure Backup?": https://learn.microsoft.com/en-us/azure/backup/backup-introduction-to-azure-backup
- Bacula.org — "What is Bacula?" and project homepage: https://www.bacula.org/what-is-bacula/ , https://www.bacula.org/
- Acronis — Cyber Protect Cloud backup product page and documentation index: https://www.acronis.com/en-us/products/cloud/cyber-protect/backup/ , https://www.acronis.com/en-us/support/documentation/
- Commvault — documentation portal root (structure only): https://documentation.commvault.com/

> Sourcing limitations: Commvault's documentation portal loads its content pages dynamically and could not be read beyond the portal structure, so Commvault is used as a market anchor with positioning-level evidence only. Rubrik's documentation site is behind a sign-in wall and was excluded from evidence. Acronis operational statements come from vendor product pages and FAQ rather than the product knowledge base. Precise operational details (numeric RPO thresholds, exact retention limits, default schedules, per-feature edition availability) are intentionally not stated in this document; such vendor claims are recorded in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample check are recorded in the paired Research Notes.
