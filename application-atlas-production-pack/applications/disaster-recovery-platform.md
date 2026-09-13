# Disaster Recovery Platform

## Overview

A **Disaster Recovery Platform** is an IT-operations application that keeps designated workloads recoverable at a separate location: it continuously replicates each protected workload to a recovery site, and when the primary site is lost — or ahead of planned downtime — it brings the workload up and running at that recovery location.

The defining core is small:

```text
Protected workload (unit of record)
└── Standing replication to a separate recovery location
    └── Recovery execution at that location (failover)
```

Everything else commonly associated with DR products — recovery plans, test drills, failback, RPO dashboards, cloud targets — is standard capability that mature products add, not what makes the product a DR platform. A product that only replicates one workload and recovers it manually on demand is still recognizably this Type; a product that only makes scheduled copies for restoring data is not (that is backup).

## Users & Context

Primary users are infrastructure and IT operations administrators who own the availability of servers and applications:

- **Infrastructure / platform administrators** — enroll workloads for protection, configure replication targets and policies, keep replication healthy.
- **DR / continuity coordinators** — define recovery plans, run and review drills, report readiness.
- **Operations responders** — execute failover during an event, verify recovered workloads, decide commit or rollback.

Secondary concerns sit with IT management (recovery objectives, readiness reporting, compliance evidence) and, in service-provider variants, with MSP operators running DR for many customers.

The work context is normally steady-state: the platform runs quietly in the background, and most operator time goes to monitoring replication health, remediating warnings, and rehearsing recovery. The dramatic use — actual failover — is rare, planned for, and rehearsed. Recovery objectives (how much data loss and downtime the organization tolerates) are set outside the tool, but the platform is the machinery that makes them achievable and measurable.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being a DR platform:

- **Protected workload** — the unit of record. A designated server, virtual machine, or application stack enrolled for recovery. Enrollment records what is protected, where it will recover to, and how (replication settings, target resources). The workload is the thing every other structure hangs from; without a designated subject there is nothing to protect or recover.
- **Standing replication to a separate recovery location** — continuous or near-continuous copying that maintains a recoverable copy of the workload at a location other than the primary (another datacenter, another cloud region, or a provider's cloud). The copy is kept current to a defined recovery point objective; its currency is the platform's key property. Without this, there is nothing to recover.
- **Recovery execution** — the ability to bring the workload up and running at the recovery location from the replicated copy, on demand, when the primary is lost or ahead of planned downtime. Without this, the platform is a data-copy pipeline, not a recovery capability.

Note what is *not* in the core: no virtualization or hypervisor concepts, no cloud, no snapshots, no agents, no recovery plans, no testing, no failback. The core is deliberately implementation-neutral — the same triple describes mainframe-era, virtualization-era, and cloud-era DR.

### Standard Capabilities of Mature Products

Mature products carry most of the following. They make DR practical; they do not define the Type.

- **Recovery plans (orchestration)** — interdependent multi-tier applications must come back in order: database before application tier, application tier before web tier. A recovery plan captures that order once: workloads grouped into ordered steps, started in parallel within a step and sequentially across steps, with wait intervals, automation hooks (scripts or runbooks), and pauses for manual actions that a human confirms.
- **Non-disruptive testing** — the same recovery machinery run in isolation: a test failover or recovery drill brings workloads up at the recovery location (or in an isolated sandbox) without affecting production or ongoing replication, then cleans up. Testing history is surfaced to operators; some products additionally flag workloads that have not been tested.
- **Failback and the return path** — after a failover, the recovered workload is typically unprotected at its new location. Reprotection starts replication back toward the original site; a planned failover then returns the workload; protection is re-armed in the forward direction. The explicit alternative is **permanent failover**: the recovery copy becomes the new primary and no return is made.
- **Recovery point selection** — at failover, the operator chooses the point to recover to: the latest available data, the latest already-processed point (faster but older), the latest application-consistent point, a common point across a group of interdependent workloads, or a specific earlier point in time.
- **Consistency tiers** — crash-consistent recovery points (equivalent to the on-disk state after a power loss) versus application-consistent points (memory and in-flight transactions flushed, typically via application-aware snapshot mechanisms). Some products support consistency groups so several workloads recover to a shared point in time.
- **Recovery objectives as managed properties** — the current RPO surfaced per protected workload, replication health states (healthy / warning / critical), alerts when replication falls behind or fails, and readiness checks that validate a failover would succeed (missing target resources, quota, agent currency, connectivity).
- **Network handling at recovery** — recovered workloads need addresses and routing: IP retention or re-addressing, network mapping between sites, and integration with load balancers or DNS-based traffic steering. Where this sits varies: some products handle it in-product, others leave traffic redirection to the customer's routing layer.

### One Structure, Many Implementations

The core model is conceptual. Implementations differ on every axis:

```text
Concept:            Protected workload
Implementations:    virtual machine, physical server, cloud instance, application group

Concept:            Recovery location
Implementations:    secondary datacenter, secondary cloud region, provider cloud, staging area in a cloud account

Concept:            Replication machinery
Implementations:    hypervisor snapshot-based incremental replication, host-agent block replication,
                    I/O-filter continuous replication, storage-array replication

Concept:            Recovery execution
Implementations:    orchestrated plan run, per-workload failover command, instance launch from replicated data
```

A reader who has only seen one shape (say, cloud DR with agents) should still be able to recognize the others from the core model.

## How It Works

### Enroll a workload for protection

```text
Select the workload (VM / server / instance)
→ choose the recovery location and target resources
→ configure replication settings (recovery point retention, consistency frequency)
→ initial replication copies the workload to the recovery location
→ continuous/incremental replication keeps the copy current
```

From this point the workload has a standing, recoverable copy elsewhere. The platform never stops watching whether that copy is keeping up.

### Run steady state (the normal loop)

```text
Replication runs continuously
→ platform tracks replication health and current RPO per workload
→ warnings/errors surface when replication lags or breaks
→ operator remediates (connectivity, capacity, agents)
→ periodically: run a non-disruptive drill to prove recovery works
→ readiness views show what is protected, healthy, and tested
```

### Fail over (the defining operation)

```text
Primary site lost — or planned downtime declared
→ operator triggers failover (single workload or recovery plan)
→ optional: attempt to shut down source and synchronize final changes
→ platform materializes the workload at the recovery location from the replicated copy
   (for a plan: groups start in order, machines in parallel, scripts/manual steps execute)
→ operator verifies the recovered workload
→ commit: the recovery is finalized (recovery point choice locked)
→ traffic reaches the recovered workload (in-product networking, or the customer's routing layer)
```

Two failover postures exist. **Unplanned failover** accepts some data loss (whatever had not yet replicated) and proceeds even if the source cannot be shut down. **Planned failover**, used ahead of known downtime, shuts the source down first, synchronizes the last data, and completes with zero data loss — it refuses to run if the source cannot be shut down.

### Return to normal

```text
Primary site restored
→ reprotect: replicate the recovered workload back toward the original site
→ planned failover back (original or alternate location)
→ re-arm forward protection; steady state resumes
```

If return is not intended — the old site is abandoned, or the recovery copy should simply become the new primary — the operator performs a **permanent failover** instead, and the recovery location becomes home.

### Capability tiers

**Defining core** — protected workload; standing replication to a separate recovery location; recovery execution at that location.

**Standard capabilities** — recovery plans; non-disruptive testing; failback/reprotect (or permanent failover); recovery point selection; consistency tiers; RPO/health monitoring and alerts; readiness checks; network handling.

**Optional / variant** — cloud-operated recovery (DRaaS); continuous data protection tier (near-zero RPO); cost-optimized staging; automatic conversion of workloads to run natively on the recovery platform; migration use (one-way failover); physical and cross-cloud workload coverage; multi-tenant/MSP delivery; compliance reporting.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Protected-workload inventory

The primary entry surface: every enrolled workload with its replication health, current RPO, recovery location, and last-test status.

- typical information: workload identity, source/target locations, replication state, health (healthy/warning/critical), RPO, recovery points, readiness
- primary actions: enable/disable protection, edit target/settings, run test failover, run failover, drill into details

### Recovery plans

The orchestration surface for multi-workload recovery.

- typical information: plan name, source/target, ordered groups of workloads, attached scripts/runbooks/manual steps, last run results
- primary actions: create/edit plan, reorder groups, add automation or manual steps, run test failover of the plan, run failover

### Failover / drill execution view

The run surface showing an operation in progress.

- typical information: step-by-step progress (prerequisites, failover, start), per-workload status, prompts for manual actions, recovery point selection
- primary actions: choose recovery point, start/cancel (where allowed), confirm manual steps, commit, undo

### Monitoring / dashboard

The steady-state surface.

- typical information: replication health summary, configuration issues (missing targets, quota, agent versions), error summary with impacted-workload counts, infrastructure connectivity view, job history, test-failover recency
- primary actions: drill into a workload, acknowledge/route alerts, export/report

### Workload detail

- typical information: replication status and health, current RPO and when computed, latest recovery points, failover readiness, errors and events
- primary actions: failover, test failover, edit settings, view events

## Important Rules / Behaviors

### The recoverable copy must stay current

The platform's promise is only as good as its replication. Health states and RPO visibility exist because replication falls behind (network, churn, capacity) and because a stale copy silently breaks the recovery promise. Alerting on replication lag is a structural behavior, not an add-on.

### Failover is a two-phase act

Bringing the workload up and finalizing the recovery are separate steps. Between them, the operator can verify the recovered workload and even choose a different recovery point. Commit locks the choice (and typically discards retained recovery points); before commit, the operation can be undone or redirected. This mirrors the reality that a failover performed in panic may need correction.

### Planned and unplanned failover have opposite guarantees

Planned failover trades speed for zero data loss: it shuts the source down, synchronizes, and refuses to proceed if shutdown fails. Unplanned failover trades data for availability: it proceeds even if the source cannot be shut down, to the latest available point. A platform that behaved the same way in both situations would not serve its purpose.

### Failover stops the protection relationship

Failing over typically ends forward replication; the recovered workload is unprotected until reprotect runs. Cancelling a failover mid-flight can leave replication stopped. The return path (reprotect → planned failover back → re-arm) is therefore not optional bookkeeping — it is how the safety net is restored.

### Testing must not touch production

Drills and test failovers run the same machinery in isolation — separate network, sandbox, or drill instances — and clean up after themselves. Testing history is tracked and surfaced, because an untested recovery path is not a recovery path.

### Consistency is a choice with consequences

Crash-consistent points are cheap and frequent; application-consistent points cost production performance and are taken on a schedule. Multi-workload consistency groups tighten guarantees further at additional cost. Operators choose per workload; the platform enforces the trade-offs.

## Variants

- **Cloud DR (DRaaS)** — the recovery location is a cloud region or provider cloud; workloads are converted to run natively there. The dominant current packaging; structurally identical core.
- **On-premises secondary site** — the classic shape: a second datacenter receives replication; recovery runs there. Still common where data cannot leave premises.
- **Backup-suite DR** — DR delivered as a capability inside a backup product (replicas + failover next to backups + restore). The two capability sets remain distinct even when packaged together.
- **Pure-play replication/CDR products** — continuous-replication specialists emphasizing near-zero RPO.
- **MSP / multi-tenant DR** — providers operate the platform for many customers; tenancy and billing layers added.
- **Migration-flavored use** — the same machinery run one-way to move workloads to a new site or cloud; protection relationship intentionally not re-armed.
- **Ransomware-resilient posture** — emphasis on recovering to points before corruption, isolated recovery environments, and clean-room verification. A growing emphasis layer, not a separate Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Backup Management | closest neighbor, often bundled | Backup makes scheduled point-in-time copies to restore **data** (files, VMs, objects) with long retention; DR keeps a **ready-to-run copy of workloads** at a separate location and executes recovery there. Seam test: restore-the-data vs bring-the-workload-up-elsewhere. |
| Data Replication Platform | same transport, different purpose | Data replication moves data between live systems for distribution/consistency/analytics; DR replication exists for recoverability, bound to a recovery location and recovery execution. Remove recovery semantics → data replication. |
| Business Continuity Management Platform | organizational vs technical | BCM manages the process: impact analysis, plans, exercises, compliance across people and facilities. The DR platform executes technical recovery of IT workloads; its "recovery plan" is a technical runbook, not a BCM plan. |
| Incident Management | response coordination vs machinery | Incident tools coordinate the human response to outages; the DR platform is the technical machinery a responder triggers. Different objects (incidents vs protected workloads and recovery operations). |
| High Availability / clustering | same-site vs cross-site | HA keeps services up through component failure within a site, automatically, at seconds scale. DR handles location-level loss, operator-triggered or planned, at minutes scale, across sites. |
| Cloud Management Platform | adjacent infrastructure tooling | CMP provisions and manages cloud resources generally; the DR platform's objects are protected workloads, replication, and recovery operations, not resources in general. |
| Storage Management / array replication | substrate vs platform | Array-based replication can be the transport underneath DR; the DR platform adds workload designation, recovery orchestration, testing, and the return path. |

The backup boundary is the most consequential one, because the market bundles the two. The structural test survives the bundling: if recovery means restoring data from copies, it is backup; if it means bringing workloads up at another location, it is DR.

## Representative Products

- **Azure Site Recovery** — cloud DR service; replicates VMs and physical servers to Azure regions or secondary sites; recovery plans with automation; test failover; reprotect/failback cycle.
- **AWS Elastic Disaster Recovery** — agent-based continuous block replication into a staging area in the customer's cloud account; recovery drills; recovery plans; failback via reverse replication; traffic redirection explicitly left to the customer's routing layer.
- **Veeam Backup & Replication (replication / CDP)** — DR as a capability inside a backup suite: VM replicas, continuous data protection, failover/planned/permanent failover, failback with commit/undo, sandbox-based replica verification.

Also prominent in this market but not verified from primary documentation in this research pass: VMware Site Recovery Manager, Zerto, Commvault, Arcserve, IBM GDPS (mainframe DR). No claims in this document depend on them.

## Sources

Research date: **2026-09-08**

- Azure Site Recovery — overview, recovery plans, failover, failover/failback overview, monitoring dashboard, Azure-to-Azure architecture: https://learn.microsoft.com/en-us/azure/site-recovery/ (pages: site-recovery-overview, site-recovery-create-recovery-plans, recovery-plan-overview, site-recovery-failover, failover-failback-overview-modernized, site-recovery-monitor-and-troubleshoot, azure-to-azure-architecture)
- AWS Elastic Disaster Recovery — what-is-drs, recovery-plans, failback (terminology), concepts (RPO/RTO, point-in-time snapshots): https://docs.aws.amazon.com/drs/latest/userguide/
- Veeam Backup & Replication 13 User Guide — replication, failover and failback, continuous data protection, SureReplica: https://helpcenter.veeam.com/docs/backup/vsphere/

> Sourcing limitation: official operational documentation for VMware Site Recovery Manager, Zerto, Commvault, and IBM GDPS was not reachable from the research environment on 2026-09-08 (redirects to generic portals, timeouts, access denied). The analysis rests on three products; single-product findings were kept out of the general claims, and precise vendor-specific figures (defaults, limits, cadences) were deliberately omitted from this document and remain in the Research Notes.
