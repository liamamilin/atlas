# Research Notes — Disaster Recovery Platform

## Research Goal

Understand, from real products' official documentation, what a Disaster Recovery Platform (DR) actually is: its core objects, its standing operation, its recovery execution, its testing posture, and its boundaries against Backup Management, Data Replication, Business Continuity Management, and High Availability.

## Initial Boundary (hypothesis before research)

- **What**: an IT-operations application that keeps designated workloads recoverable at a secondary location by continuously replicating them, and executes their recovery (failover) when the primary is lost — plus testing, monitoring, and return-to-primary.
- **Who**: infrastructure/IT operations admins, DR/BC managers, MSPs.
- **Nearest Types**: Backup Management, Data Replication Platform, Business Continuity Management Platform, Incident Management, Cloud Management Platform, Storage Management.
- **Open questions**: Is failback definitional? Are RPO/RTO first-class managed objects? Does traffic redirection belong inside the product? What exactly separates DR from backup when one product does both?

## Research Questions

1. What is the unit of protection, and how is a workload enrolled?
2. What does replication concretely maintain at the recovery location (mechanism, cadence, consistency, retention)?
3. What is a recovery plan, and what does orchestration include (order, waits, scripts, manual steps)?
4. What failover modes exist (test / planned / unplanned), and how does non-disruptive testing work?
5. How do failback / reprotect / permanent failover work?
6. How are RPO and RTO configured, measured, surfaced?
7. What monitoring, alerting, and readiness reporting exist?
8. What roles and interfaces does the platform expose?
9. What structurally changes when the recovery location is a public cloud (DRaaS)?
10. Where are the boundaries: vs backup, vs data replication, vs BCM, vs HA?

## Representative Products

Selected for market representation, documentation completeness, and different product philosophies:

| Product | Philosophy / position | Evidence access |
|---|---|---|
| Azure Site Recovery (Microsoft) | Cloud DR service (DRaaS); orchestrates replication + failover + failback; also used for migration | Tier 1 docs fetched (multiple pages) |
| AWS Elastic Disaster Recovery (Amazon) | Cloud DR service; agent-based continuous block replication into customer's AWS account; explicitly separates recovery from traffic failover | Tier 1 docs fetched (multiple pages) |
| Veeam Backup & Replication (replication + CDP) | Backup-led suite where DR is a capability (VM replication, CDP, failover/failback); boundary probe vs Backup Management | Tier 1 docs fetched (multiple pages) |

Considered but **not reachable** in this pass (see Sources — access limitations): VMware Site Recovery Manager (docs.vmware.com and techdocs.broadcom.com both redirect to a generic search page), Zerto (zerto.com/docs and help.zerto.com timed out / portal-only), Commvault DR (specific doc pages not located), IBM GDPS (ibm.com/docs 403). No claims about these products are made from memory.

## Sources

Fetched 2026-09-08:

- Azure Site Recovery — Overview: https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview
- Azure Site Recovery — Recovery plans (create/customize): https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-create-recovery-plans
- Azure Site Recovery — About recovery plans: https://learn.microsoft.com/en-us/azure/site-recovery/recovery-plan-overview
- Azure Site Recovery — Run a failover: https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-failover
- Azure Site Recovery — Failover/failback overview (modernized): https://learn.microsoft.com/en-us/azure/site-recovery/failover-failback-overview-modernized
- Azure Site Recovery — Monitoring dashboard and alerts: https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-monitor-and-troubleshoot
- Azure Site Recovery — Azure-to-Azure architecture: https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-architecture
- Azure Site Recovery — Hyper-V support matrix (via failover-failback URL redirect): https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-azure-support-matrix
- AWS Elastic Disaster Recovery — What is DRS: https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html
- AWS Elastic Disaster Recovery — Recovery plans: https://docs.aws.amazon.com/drs/latest/userguide/recovery-plans.html
- AWS Elastic Disaster Recovery — Recovery and failback (terminology): https://docs.aws.amazon.com/drs/latest/userguide/failback.html
- AWS Elastic Disaster Recovery — Concepts (RPO/RTO, PIT snapshots): https://docs.aws.amazon.com/drs/latest/userguide/CloudEndure-Concepts.html
- Veeam Backup & Replication 13 User Guide — Replication for VMware vSphere: https://helpcenter.veeam.com/docs/backup/vsphere/replication.html
- Veeam — Failover and Failback for Replication: https://helpcenter.veeam.com/docs/backup/vsphere/failover_failback.html
- Veeam — Continuous Data Protection (CDP): https://helpcenter.veeam.com/docs/backup/vsphere/cdp_replication.html
- Veeam — SureReplica: https://helpcenter.veeam.com/docs/backup/vsphere/recovery_verification_surereplica.html

### Access limitations

- VMware SRM, Zerto, Commvault DR, IBM GDPS: official operational documentation not reachable from this environment on 2026-09-08 (redirects to generic search/portal pages, timeouts, 403). Consequence: the sample is 3 products, all cloud-era. Cross-product claims below are marked accordingly; single-product findings are marked product-specific. No precise claims about unreachable products were filled from model memory.
- The historical/market-sample check (older, mainframe, host-based DR products) could not be grounded in fetched primary sources this pass; it is performed as an abstraction-level check and flagged in Uncertainties.

---

## Product A — Azure Site Recovery

### Key observations (evidence layer A unless noted)

- **Positioning**: "keeps business apps and workloads running during outages"; replicates workloads (Azure VMs, on-prem VMware/Hyper-V VMs, physical servers) from a primary site to a secondary location; fail over on outage; fail back after recovery. Explicitly a *different service* from Azure Backup ("Backup service keeps your data safe and recoverable").
- **Replication machinery (Azure-to-Azure)**: Mobility service extension installed on VM → registers VM → continuous replication; disk writes go to a **cache storage account** in the source region, then processed to target storage/replica managed disks. Target resources (resource group, VNet, storage account, replica disks, availability set/zone) are auto-created with defaults and customizable.
- **Replication policy**: recovery point retention (default one day) and app-consistent snapshot frequency (default disabled). Crash-consistent recovery points generated every five minutes by default (setting not modifiable); app-consistent points via VSS at configured frequency. **Multi-VM consistency**: replication groups produce common crash-/app-consistent points across VMs (performance impact noted).
- **Recovery plans**: named plan bound to source/target; machines in groups (default Group 1; up to seven groups); machines in one group start in parallel, groups start in order; scripts (VMM scripts / Azure Automation runbooks) and **manual actions** (plan pauses, dialog confirms completion) attachable as pre/post steps per group; plan usable for failover and failback; a machine can appear in multiple plans (subsequent plans skip already-started machines).
- **Failover**: run per VM or per plan; **recovery point selection**: Latest (lowest RPO; processes pending data), Latest processed (low RTO), Latest app-consistent, Latest multi-VM processed / app-consistent, Custom (single VM only). Optional "shut down machine before failover" (failover continues even if shutdown fails). Jobs page tracks prerequisites check → failover → start. **Commit** finalizes; after commit the recovery point can no longer be changed and recovery points are deleted. Failover must not be cancelled mid-run (replication stops and does not resume).
- **Failover types**: Test failover (drill; creates copy VMs in an isolated test network; no impact on ongoing replication or production; automatic cleanup), Planned failover (Hyper-V: zero data loss — shutdown first, sync latest data, then failover; does not run if machine can't be shut down), unplanned failover (minimal data loss; runs even if shutdown fails). Planned failover is also the mechanism for failing back Azure→on-prem.
- **Recovery cycle (4 stages)**: fail over → **reprotect** (start replicating Azure VMs back to on-prem; on-prem VM powered off during reprotect) → fail over back (planned failover; original or alternate location — OLR/ALR) → reprotect on-prem machines (resume forward replication). After failover, Azure VMs are in an "unprotected state" until reprotect.
- **Monitoring**: vault dashboard; replicated items health states **Healthy / Warning / Critical / Not applicable**; per-VM details include current **RPO** and when it was last computed, latest recovery points, **failover readiness** (whether a test failover was run, agent version, configuration issues), errors, events; configuration issues (missing configurations/resources, subscription quota, software updates) checked by a periodic validator; infrastructure view with connectivity health; jobs; email notifications and Azure Monitor alerts for critical events (replication health critical, failover failure, agent expiry); "Failover test success" section tracks test-failover status per machine ("Test recommended" / "Performed successfully"); recommendation to test at least every six months; Business Continuity Center for at-scale multi-vault view.
- **RTO/RPO framing**: "Keep recovery time objectives (RTO) and recovery point objectives (RPO) within organizational limits"; continuous replication for Azure/VMware VMs; replication frequency as low as 30 seconds for Hyper-V; RTO reducible via Traffic Manager integration.
- **Migration**: the same machinery serves one-way migration (failover without failback intent) — overview lists migration deployment scenarios.

## Product B — AWS Elastic Disaster Recovery

### Key observations (evidence layer A unless noted)

- **Positioning**: "minimizes downtime and data loss with fast, reliable recovery of on-premises and cloud-based applications"; replicate source servers into a **staging area subnet in the customer's AWS account** (affordable storage, minimal compute); launch instances for **drills or recovery**; automatic conversion of servers to "boot and run natively on AWS".
- **Terminology (explicit, load-bearing)**: **Recovery** = launching recovery instances on AWS from replicated data (start-recovery API). **Recovery drill** = non-disruptive test launching drill instances; "use the same process as recovery but do not affect your source servers or ongoing replication". **Failover** = redirecting production traffic to recovery instances — "performed outside of AWS Elastic Disaster Recovery, typically using a DNS routing service such as Amazon Route 53". **Failback** = returning workloads to the original source infrastructure; DRS "assists with failback by replicating data from recovery instances back to your source servers". Summary: the product handles recovery + failback; traffic redirection is the customer's.
- **Replication**: AWS Replication Agent continuously monitors blocks written to source volumes and copies them into the staging area; **continuous block-level replication**; recovery points are **crash-consistent**; in-memory application data not replicated until written to volumes. RPO "typically in the sub-second range"; RTO "typically measured in minutes" (average Linux boot ~5 min, Windows ~20 min; depends on instance/volume performance). RPO degrades temporarily if write rate exceeds network/staging capacity.
- **Point-in-Time (PIT) snapshots**: crash-consistent recovery points stored per retention policy; default schedule (per 10 min for prior hour; hourly for prior 24 h; daily for prior 7 days; day-retention adjustable 1–365 days; frequencies not configurable) — product-specific detail. "Use most recent data" attempts an on-demand PIT snapshot at job submission (with timeout behavior). **Any/All** selection semantics for multi-server jobs.
- **Recovery plans**: group source servers into **ordered steps** with optional wait times; run whole plan with a single action; within a step servers recover in parallel and the plan waits for terminal state before the next step; plan can run as **drill** (non-disruptive) or in **recovery mode**; constraint: all servers in a plan must be in one account and Region; sub-topics: pre-recovery validation, **impact levels** (controlling how a server failure affects the plan), retry/skip/cancel, execution monitoring, quotas.
- **Failback mechanisms** vary by source infrastructure: on-premises (Failback Client ISO or DRS Failback Automation), AWS same-account (start **reverse replication** on the protected recovery instance), cross-account, other cloud (varies per provider).
- **Readiness posture**: "During normal operation, maintain readiness by monitoring replication and periodically performing non-disruptive recovery and failback drills."
- **RPO/RTO**: headline properties; dedicated concepts page defines how each is measured.

## Product C — Veeam Backup & Replication (replication + CDP)

### Key observations (evidence layer A unless noted)

- **Positioning**: backup-led suite; **replication** is a distinct technology from backup: "creates an exact copy of the VM in the native VMware vSphere format on the target host … maintains this copy in sync with the source VM. Replication provides minimum RTO … because VM replicas are in a ready-to-start state." Guidance: replication for RPO of **hours**; **CDP** for RPO of **seconds**.
- **Replication mechanism**: leverages vSphere snapshots; first cycle full copy, subsequent cycles incremental (changed block tracking); replicas stored decompressed in native format; on-site replication for HA scenarios vs remote (off-site) replication for DR; WAN optimization (filtering, compression, WAN accelerators, throttling).
- **CDP**: constantly replicates I/O operations via VAIO (vSphere APIs for I/O filtering) without snapshots; near-zero RPO; short-term restore points maintained in a **journal** (product-specific limit: 168 hours / 7 days); long-term restore points for older states.
- **Failover operations (rich state machine)**: **Failover** (shift to replica; intermediate step that must be finalized), **Planned failover** (proactive switch before known downtime; no restore-point selection — designed to transfer current workload), **Permanent failover** (replica becomes the source VM — legitimate end state when source unrecoverable), **Undo failover** (shift back, discard replica changes — used after test/troubleshooting), **Failback** (shift back and send replica-side changes to the source; changes not published until verified), **Commit failback** / **Undo failback** (test results decide). Batch processing for multiple VMs/hosts.
- **Failover plans**: define the order of VM failovers and a wait interval between VMs.
- **SureReplica**: automated verification of every restore point of every replica in an isolated **Virtual Lab** sandbox without impacting production; On-Demand Sandbox for testing/training/troubleshooting.
- **Same product, different Type**: the same console also does backups (restore points, restores, SureBackup) — the DR capability set (replicas, failover, failback) is a distinct module inside a backup product. This product is the boundary probe: DR semantics (ready-to-run replicas + failover) are separable from backup semantics (restore from copies).

---

## Cross-product Comparison

| Dimension | Azure Site Recovery | AWS Elastic DR | Veeam replication/CDP |
|---|---|---|---|
| Unit of protection | "Replicated item" — Azure VM / VMware VM / Hyper-V VM / physical server | "Source server" (agent-protected physical or cloud server) | VM replica / CDP-protected VM |
| Recovery location | Secondary Azure region, or secondary on-prem site, or Azure (from on-prem) | Staging area subnet in customer's AWS account | Target host/datastore at DR site (or service-provider cloud via Cloud Connect) |
| Replication posture | Continuous (Azure/VMware); interval-based for Hyper-V; crash-consistent points every 5 min; app-consistent per policy | Continuous block-level; crash-consistent; PIT snapshots per retention policy | Snapshot-based incremental (RPO hours) or CDP I/O-replication (near-zero RPO) |
| Recovery objectives | RPO shown per VM; policy settings (retention, app-consistent frequency) | RPO seconds / RTO minutes as measured product properties | RPO hours (replication) vs seconds (CDP); "minimum RTO" via ready-to-start replicas |
| Orchestration object | Recovery plan (groups, order, scripts/runbooks, manual actions) | Recovery plan (ordered steps, waits, validation, impact levels) | Failover plan (ordered VMs, wait intervals) |
| Non-disruptive testing | Test failover into isolated test network; auto cleanup; tracked per machine | Recovery drill (same machinery as recovery); periodic drills recommended | SureReplica in isolated Virtual Lab |
| Recovery point selection | Latest / latest processed / latest app-consistent / multi-VM variants / custom | Most recent data / PIT snapshot (Any/All) | Restore point selection (CDP short/long-term points) |
| Failover finalization | Commit (point locked; points deleted) | Recovery launch (instances run; traffic redirected outside product) | Permanent failover / failback commit / undo |
| Return to primary | Reprotect → planned failover back → reprotect (OLR/ALR) | Failback (reverse replication / failback client / automation) | Failback with commit/undo; permanent failover as alternative |
| Monitoring | Replication health states, per-VM RPO, config issues, jobs, alerts, test-failover tracking | Replication state monitoring; drill/recovery job monitoring | Job sessions; replica status; SureReplica results |
| Traffic redirection | Network integration (IP retention, load balancers, Traffic Manager) inside product scope | Explicitly outside product (DNS/traffic management by customer) | Not documented as in-product traffic redirection (network mapping/remediation at replica level) |

### Cross-product commonalities (evidence layer B)

All three sampled products, despite different architectures, share:

1. A designated **protected workload** (replicated item / source server / protected VM) as the unit of record.
2. **Standing replication** to a separate recovery location, maintaining a recoverable copy whose currency is the platform's key property (RPO).
3. **Recovery execution**: bringing the workload up at the recovery location from the replicated copy (failover/recovery), selectable to a recovery point.
4. **Non-disruptive rehearsal** of recovery (test failover / drill / SureReplica) using the same machinery without touching production.
5. **Multi-workload ordered recovery** (recovery plans / failover plans) with parallel-within-step, sequential-across-steps semantics and wait/automation/manual-step hooks.
6. **Return path**: failback/reprotect machinery (or permanent failover as an explicit alternative).
7. **Readiness monitoring**: replication health, RPO visibility, configuration/readiness checks, alerts.
8. **Consistency semantics**: crash-consistent vs application-consistent recovery points (all three name both concepts).

### Divergences (implementation, not Type)

- Where traffic redirection lives: inside the product's scope (ASR network integration) vs explicitly outside (AWS DRS).
- Replication substrate: hypervisor/snapshot-based vs host agent block-level vs I/O-filter CDP.
- Recovery location: cloud region vs on-prem site vs service-provider cloud.
- Failover state machine granularity (Veeam's undo/commit/permanent variants vs ASR's commit vs DRS's launch-and-redirect split).

---

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a Disaster Recovery Platform:

1. **The protected workload as unit of record** — a designated IT workload (server, VM, or application stack) enrolled for recovery, carrying its recovery configuration (recovery location, replication/recovery settings). Remove → generic replication or backup tooling with nothing designated for recovery.
2. **Standing replication to a separate recovery location** — continuous or near-continuous copying that maintains a recoverable copy of the workload at a location other than the primary, kept current to a defined recovery point objective. Remove → nothing recoverable exists; the platform cannot promise recovery.
3. **Recovery execution at the recovery location** — the ability to bring the protected workload up and running at the recovery location from the replicated copy (failover/recovery), on demand, when the primary is lost or ahead of planned downtime. Remove → a data-copy pipeline, not a recovery capability.

Deliberately **not** in L0 (checked against the sample and against older/other-shaped products): virtualization or hypervisor specifics, cloud, snapshots, agents, DRaaS packaging, recovery plans/orchestration, testing, failback, RPO/RTO dashboards, traffic redirection. A single-workload, manually-triggered, replication-plus-failover product is still recognizably this Type.

### L1 — Common Mature Structure

Present across the sample; expected of mature products; not required to recognize the Type:

- **Recovery plans / orchestration** — ordered, grouped recovery of interdependent multi-tier workloads; parallel within groups, sequential across groups; wait intervals; automation hooks (scripts/runbooks); manual-action pauses.
- **Non-disruptive DR testing** — test failover / recovery drills / sandbox verification using the same recovery machinery in isolation, with cleanup; readiness tracking of test recency.
- **Failback / reprotect cycle** — reverse replication after failover, planned failover back, re-arming forward protection; original-location vs alternate-location recovery; **permanent failover** as the explicit alternative when return is not intended.
- **Recovery point selection** — choosing the point to recover to (latest, latest processed, app-consistent, custom point in time).
- **Consistency tiers** — crash-consistent vs application-consistent recovery points; multi-VM consistency groups.
- **RPO/RTO as managed properties** — current RPO surfaced per workload; RTO expectations documented; replication health states (healthy/warning/critical) with alerts.
- **Readiness/configuration checks** — validation that failover would succeed (missing targets, quotas, agent currency, connectivity).
- **Network/IP handling at recovery** — mapping, IP retention or re-addressing, load balancer/routing integration (scope varies: in-product vs customer-side).

### L2 — Variant / Optional Structure

- **DRaaS packaging** — recovery location operated as a cloud service (hyperscaler regions or service-provider clouds) vs customer-operated secondary site.
- **Continuous data protection tier** — near-zero RPO I/O-level replication alongside interval replication (product-specific implementations differ).
- **Cost-optimized staging** — minimal-compute/affordable-storage staging areas vs full pre-provisioned secondary capacity.
- **Automatic platform conversion** — converting workloads to boot natively on the recovery platform (cloud-native conversion).
- **Migration use** — one-way failover as a migration mechanism (explicitly supported by at least one sampled product).
- **Physical-server and non-VM workload coverage**; multi-cloud/cross-cloud recovery.
- **MSP / multi-tenant delivery**; compliance/reporting layers; at-scale multi-site management centers.
- **Ransomware/logical-corruption posture** — recovery to points before corruption (implied by point-in-time recovery; explicit anti-ransomware framing not uniformly documented in the sample).

### L3 — Vendor-specific (research notes only)

- Azure: Recovery Services vault; cache storage account; `-ASRReplica` replica disks; "asr"-suffixed auto-created targets; crash-consistent points every 5 minutes (non-modifiable); Hyper-V 30-second replication floor; 24h/72h retention windows per scenario; Business Continuity Center; Traffic Manager integration; VMM scripts.
- AWS: staging area subnet; AWS Replication Agent; PIT snapshot default retention schedule (10-min/hourly/daily tiers; day retention 1–365 days adjustable); "Use most recent data" with 10-minute wait; Any/All PIT selection; Failback Client ISO; reverse replication; impact levels; single account/region plan constraint; Linux ~5 min / Windows ~20 min boot expectations.
- Veeam: SureReplica / SureBackup / Virtual Lab / On-Demand Sandbox; CDP journal 168-hour limit; VAIO-based CDP; WAN accelerators; failover plan wait intervals; permanent failover / undo failover / commit-undo failback state machine; Veeam Cloud Connect for provider-hosted replicas.

## Rejected Findings

- "DR platform = backup product" — rejected. The sample itself refutes it: Azure ships Site Recovery and Backup as separate services; Veeam documents replication (ready-to-start replicas, failover) as a distinct technology from backup (restore points, restore). Backup semantics (long-retention copies, data restore) are not DR semantics (ready-to-run copies at an alternate site, workload recovery).
- "DR platform = data replication platform" — rejected. Replication in DR exists to maintain a recoverable copy bound to a recovery location and recovery execution; data-replication platforms move data for distribution/consistency/analytics with no recovery semantics.
- "Failover must include traffic redirection" — rejected as definitional. AWS DRS explicitly places traffic failover outside the product; ASR treats network integration as in-scope. The invariant is bringing the workload up at the recovery location, not redirecting users.
- "Failback is definitional" — rejected. Veeam documents permanent failover as a first-class alternative end state; a platform whose recovery ends with the workload running at the recovery location is still a DR platform. Failback/reprotect is common mature structure.
- "Recovery plans are definitional" — rejected. All sampled products support single-workload recovery without a plan; plans are the mature multi-workload layer.
- "RPO/RTO dashboards are definitional" — rejected as objects; the *currency of the recoverable copy* (which RPO measures) is folded into L0 leg 2, while RPO/RTO surfacing and alerting are L1.

## Boundary Findings

- **vs Backup Management**: backup produces scheduled point-in-time copies for restoring *data* (files, VMs, objects) with long retention; DR maintains a *ready-to-run* copy of *workloads* at a separate location and executes recovery there, with near-continuous currency. Seam test: if recovery means "restore the data from a copy onto (re)built infrastructure", it's backup; if recovery means "bring the workload up at the other location", it's DR. Suite products (Veeam) carry both as distinct modules; Azure ships them as separate services. Ransomware-era convergence (immutability, isolated recovery points) blurs marketing but not the structural seam.
- **vs Data Replication Platform**: same transport machinery, different purpose. Data replication serves distribution/consistency/analytics between live systems; DR replication serves recoverability, bound to a recovery location and recovery execution. Remove recovery location + recovery execution → data replication.
- **vs Business Continuity Management Platform**: BCM manages the organizational process (impact analysis, plans, exercises, compliance) across people and facilities; the DR platform executes technical recovery of IT workloads. The DR platform's "recovery plan" is a technical runbook, not a BCM plan. They integrate; they do not substitute.
- **vs High Availability (clustering)**: HA keeps services up through component failure within a site, automatically, at seconds scale; DR handles site/location-level loss, typically operator-triggered (or planned), at minutes scale, across sites. Veeam's own framing (on-site replication for HA scenarios vs off-site for DR) marks the seam from the replication side. Same-site automatic failover belongs to HA; cross-site orchestrated recovery belongs to DR.
- **vs Incident Management / On-call**: incident tools coordinate the human response; the DR platform is the technical machinery a responder may trigger. Different objects (incidents vs protected workloads/recovery operations).
- **vs Migration tools**: one-way failover performs migration; at least one sampled product explicitly lists migration as a deployment scenario. Migration is a variant use of the machinery, not the defining purpose (no standing protection relationship).

### "Remove what to become the other Type" judgments

- Remove the standing replication and recovery execution, keep scheduled copies for restore → **Backup Management**.
- Remove recovery location/recovery execution, keep cross-system data movement → **Data Replication Platform**.
- Remove the technical workload machinery, keep organizational plans/exercises/compliance → **Business Continuity Management Platform**.
- Remove cross-site scope and recovery execution, keep same-site automatic failover → **High Availability / clustering** territory (adjacent Type space, not a single directory leaf).

## Uncertainties

- **Sample breadth**: 3 products, all cloud-era (2 DRaaS + 1 backup-suite module). VMware SRM (the classic on-prem orchestration product), Zerto (pure-play CDP DR), Commvault, and mainframe DR (IBM GDPS) were not reachable this pass. Claims about orchestration depth and on-prem secondary-site patterns are therefore grounded in 3 products, not 5; single-product nuances are marked.
- **Historical check**: performed at the abstraction level only (L0 contains no virtualization/cloud/snapshot/agent concepts, so pre-virtualization host-based replication DR and mainframe DR fit structurally), but not grounded in fetched primary sources for old products. Flagged as an uncertainty rather than asserted as verified.
- **Traffic redirection scope**: only 3 data points (ASR in-scope, DRS out-of-scope, Veeam not documented as in-product). The L0/L1 placement (workload-up vs traffic) is safe; the *typical* market split is uncertain.
- **Testing cadence recommendations** (e.g., "at least every six months", "quarterly") are vendor recommendations, not market standards; kept out of the final document's rules.
- **Pricing/edition boundaries** (which capabilities sit behind which tiers) not researched; excluded.

## Final Synthesis

A Disaster Recovery Platform is an IT-operations application whose defining core is the triple: **protected workload of record + standing replication to a separate recovery location + recovery execution at that location**. Around that core, mature products add orchestration (recovery plans), non-disruptive rehearsal (test failover/drills), the return path (failback/reprotect or permanent failover), recovery point selection with consistency tiers, RPO/RTO visibility, readiness checks, and network handling. The market's dominant current packaging is DRaaS (cloud as the recovery location), but the Type is older and broader than its cloud packaging: the same triple describes on-prem secondary-site DR and predates virtualization. The sharpest boundary is against Backup Management (restore data vs bring workloads up elsewhere) and against Data Replication (recoverability purpose vs distribution purpose).
