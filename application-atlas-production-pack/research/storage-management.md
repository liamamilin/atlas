# Research Notes — Storage Management

Research date: 2026-09-09
Directory leaf: Storage Management (§14 IT, Cloud & Infrastructure)
Slug: storage-management

---

## Research Goal

Understand what a "Storage Management" application is as an Application Type: what the operator manages, what objects exist inside it, what workflows it carries, and where its boundaries sit against the neighboring §14 infrastructure-management Types (Backup Management, Archive Storage Management, Disaster Recovery Platform, Cloud Management Platform, Virtualization Management, Hyperconverged Infrastructure Management, Infrastructure Monitoring, Capacity Management, Network/Server Management) and against content-level Types (File Manager, Personal Cloud Drive, Database consoles).

## Initial Boundary (hypothesis before research)

- Hypothesis: Storage Management is the operator-facing management layer over storage infrastructure — storage systems/arrays, software-defined storage, NAS appliances, and cloud storage services — covering inventory, provisioning, capacity/performance/health operations, and storage-layer data protection (snapshots, replication, tiering).
- Likely confusions:
  - Backup Management (protection copies vs live estate)
  - Archive Storage Management (retirement vs live estate)
  - Infrastructure Monitoring (observation vs management/control)
  - Cloud Management Platform (all-resource estate vs storage-specific depth)
  - Virtualization Management / HCI Management (hypervisor-suite pole serves both depending on deployment subject — pre-recorded by the HCI pass)
  - File Manager / Personal Cloud Drive (end-user files vs infrastructure storage)
- Known prior constraints from sibling passes (STATUS.md):
  - hyperconverged-infrastructure-management (2026-09-08): "the hypervisor-suite pole (vCenter-class console) serves BOTH types depending on deployment subject — over external SAN storage it operates as virtualization management, over its own software-defined storage on the same hosts as this [HCI] Type; the two Types are distinguished by the managed subject (converged compute+storage cluster vs VMs-over-arbitrary-infra), not by product identity — the future virtualization-management pass should treat converged-storage deployments as this leaf's territory."
  - archive-storage-management (2026-09-06): boundary held vs Storage Management = "live estate operations".
  - backup-management (2026-09-06): boundary held vs Storage Management = "backup storage as custody target vs administered production infra".

## Research Questions

1. What is the managed subject? (storage systems, pools, volumes/LUNs, file shares, object buckets, drives)
2. What does the physical→logical layering look like, and is it universal?
3. What does provisioning look like? (create pool/volume/share/bucket; map to hosts; quotas)
4. What does the operating loop look like? (capacity, performance, health, alerts, actions)
5. What storage-layer protection exists? (snapshots, replication, scrub/integrity, encryption, WORM)
6. What interfaces exist? (web console, CLI, REST API, SaaS fleet portals)
7. Who uses it and with what roles/permissions on the management plane itself?
8. Where is the line vs Backup / Archive / DR / Monitoring / CMP / Virtualization / HCI?
9. Does the definition survive older/platform-native/smaller-scale products (Windows Disk Management, LVM, 2000s array managers)?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Tier | Evidence |
|---|---|---|---|
| NetApp ONTAP (System Manager + ONTAP CLI + REST API) | enterprise storage array vendor; per-system management | enterprise | Tier-1 docs fetched (5 pages) |
| TrueNAS SCALE 25.04 (web UI + API) | open-source storage appliance OS (ZFS) | SMB/enterprise edge | Tier-1 docs fetched (2 pages) |
| Ceph Dashboard | open-source software-defined storage cluster management | enterprise/open-source | Tier-1 docs fetched (full dashboard page) |
| Amazon S3 (Management Console + CLI + REST) | cloud object storage service console | cloud, all tiers | Tier-1 docs fetched (getting-started + protect/monitor sections) |

Rejected/unreachable (recorded, not used for claims):
- Dell PowerStore (infohub blocked by bot-verification) — second enterprise-array pole unavailable
- IBM Storage Insights (ibm.com/docs 403) — multi-vendor SaaS SRM pole unavailable
- Pure Storage Fusion (support.purestorage.com timeout ×2) — cloud-operated fleet pole unavailable
- Synology DSM Storage Manager (kb.synology.com JS-gated, page shell only) — consumer/SMB NAS pole unavailable; TrueNAS carries the appliance pole instead

## Sources

Fetched 2026-09-09 (all Tier-1 official documentation):

- NetApp ONTAP 9 documentation root — https://docs.netapp.com/us-en/ontap/
- NetApp ONTAP — SAN management overview — https://docs.netapp.com/us-en/ontap/san-admin/index.html
- NetApp ONTAP — Volume administration — https://docs.netapp.com/us-en/ontap/volume-admin/index.html
- NetApp ONTAP — Monitoring cluster performance with System Manager — https://docs.netapp.com/us-en/ontap/task_cp_monitor_cluster_performance_sm.html
- NetApp ONTAP — Disks and ONTAP local tiers — https://docs.netapp.com/us-en/ontap/disks-aggregates/index.html
- TrueNAS 25.04 — Documentation Hub — https://www.truenas.com/docs/
- TrueNAS 25.04 — Storage (UI Reference) — https://www.truenas.com/docs/scale/25.04/scaleuireference/storage/
- Ceph Reef — Ceph Dashboard — https://docs.ceph.com/en/reef/mgr/dashboard/
- Amazon S3 — Getting started with Amazon S3 — https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html

Unreachable (limitation recorded; no claims drawn from them): Dell PowerStore infohub (bot-wall), IBM Storage Insights docs (403), Pure Storage support/Fusion (timeout ×2), Synology DSM KB (JS-gated shell).

---

## Product A — NetApp ONTAP (System Manager / CLI / REST API)

### Key observations (Evidence layer A unless noted)

- Positioning (docs root): ONTAP docs cover "set up or upgrade ONTAP, provision storage for clients, and protect and manage your data with System Manager or the ONTAP CLI." Management surfaces: System Manager (web), ONTAP CLI, ONTAP REST API; a fleet surface ("NetApp Console", console.netapp.com) is referenced from the docs header.
- Physical→logical layering: "Local tiers (also called aggregates) are logical containers for the disks managed by a node." Uses: isolate workloads with different performance demands, tier data with different access patterns, segregate data for regulatory purposes. Hybrid forms: Flash Pool (SSD+HDD), FabricPool (all-SSD local tier with attached object store = cloud tiering).
- Logical storage management (volume administration): "Manage logical storage, including FlexVol volumes and LUNs. Perform operations like adding, deleting, moving volumes, or managing quotas." FlexVol/FlexGroup (scale-out)/FlexCache (cache volumes); FlexClone (efficient copies); qtrees (partition volumes); quotas; storage efficiency (deduplication, compression).
- SAN provisioning: storage targets are LUNs presented to hosts as standard block devices; "You create LUNs and then map them to initiator groups (igroups)"; igroups are tables of FC WWPNs / iSCSI IQNs controlling which initiators access which LUNs.
- NAS: NFS and SMB configuration and management sections; S3 object storage management (configure S3 access; protect S3 buckets with SnapMirror).
- Performance/health monitoring (System Manager Dashboard): displays alerts and notifications, efficiency and capacity of storage tiers and volumes, nodes in the cluster, HA-pair status, most active applications/objects, and performance metrics; four overviews — Health ("How healthy is the cluster?"), Capacity ("What capacity is available?"), Performance (latency, IOPS, throughput; hour/day/week/month/year windows), Network (ports, interfaces, storage VMs). Dedicated SVM-administrator dashboard (multi-tenant administration).
- Protection/DR: SnapMirror (incl. active sync), SnapLock (archive/compliance WORM), tape backup + NDMP.
- Management-plane security: authentication and RBAC section, SAML, MFA, OAuth2, multi-admin verification (approval gates for sensitive operations).
- Event monitoring: EMS configuration (event management system).

## Product B — TrueNAS SCALE 25.04

### Key observations (Evidence layer A)

- Storage Dashboard: "allows users to configure and manage storage resources such as pools (VDEVs) and disks."
- Pool lifecycle: Pool Creation Wizard; Import Pool (ZFS pools detected on attached disks but "not yet connected in TrueNAS"); Export/Disconnect (destructive — typed confirmation, warning that data becomes unavailable, option to destroy data, deletes configuration of shares using the pool); Expand Pool (grow to match available disk space); pool Upgrade (OpenZFS feature flags — irreversible, documented warnings).
- Widgets per pool: Unassigned Disks (add disks to new/existing pool; disks of exported pools warn on reuse); Topology (VDEV types: data/metadata/log/cache/spare/dedup; stripe/mirror/RAID/mixed); Usage (color-coded donut; blue 0–80%, red above 80% with warning; Used / Available / Used by Snapshots); ZFS Health (pool status online/offline, total ZFS errors, scheduled scrub task, auto TRIM, last scan time/errors/duration); Disk Health (temperature alerts, SMART tests).
- Pool status indicator: healthy (green) / offline (orange) / warning (purple) on every pool widget.
- Datasets: add/manage datasets and zvols (block volumes), user/group quotas, snapshots (create/manage), storage encryption, ACL permissions.
- Shares: SMB, NFS, iSCSI block-share targets, Fibre Channel, multiprotocol shares.
- Data Protection section: scrub tasks (scheduled integrity checks), periodic snapshot tasks, replication tasks (local/remote/encrypted), cloud sync tasks, rsync tasks, VMware snapshots, S.M.A.R.T. tests, TrueCloud backup tasks.
- Platform: Reporting screens; Alerts (alert settings, email); Credentials (admin roles, users/groups, directory services, 2FA); services (NFS/SMB/iSCSI/SMART/SNMP/SSH/UPS); API reference (REST API); audit screen.

## Product C — Ceph Dashboard

### Key observations (Evidence layer A)

- Self-definition: "a web-based Ceph management-and-monitoring tool that can be used to inspect and administer resources in the cluster," implemented as a Ceph Manager daemon module. Original dashboard was read-only; demand grew for "richer, web-based management capabilities."
- Monitoring/management capabilities: overall cluster health (performance and capacity metrics, cluster status); cluster logs; hosts (drives, services, versions); performance counters per service; monitors (quorum status); Prometheus alert integration (silences, firing alerts); configuration editor (all options with defaults and current values).
- Capacity card: Used / Warning (nearfull threshold) / Danger (full threshold). Cluster utilization: used capacity, IOPS, latency, client throughput, recovery throughput.
- Inventory card: "An inventory for all assets within the cluster" with direct access to subpages.
- Resource management: Pools (applications, pg-autoscaling, placement groups, replication size, EC profile, CRUSH rules, quotas); OSDs (status/usage, mark up/down/out, purge, reweight, scrub, deploy OSDs on new drives, device classes); device management (drives, health predictions, SMART data, enclosure LED blink); RBD images (create/copy/modify/delete, snapshots with protect/rollback/clone/flatten, I/O and bandwidth limits); RBD mirroring to a remote cluster (sync progress); CephFS (clients, quotas, snapshots, directory browsing); Object Gateway (users, buckets, quotas, versioning, MFA); NFS exports (Ganesha); iSCSI targets (gateways, initiators).
- Management-plane RBAC: security scopes (hosts, pool, osd, rbd-image, rgw, cephfs, nfs-ganesha, monitor, manager, config-opt, log, grafana, prometheus, dashboard-settings) × permissions (read/create/update/delete); predefined system roles (administrator, read-only, block-manager, rgw-manager, cluster-manager, pool-manager, cephfs-manager); custom roles; account lock-out; SSO via SAML 2.0; audit logging of PUT/POST/DELETE API requests (origin, path, method, user, payload).

## Product D — Amazon S3 (Management Console / CLI / REST)

### Key observations (Evidence layer A)

- Object model: bucket = container for objects; object = file + metadata. Create bucket (region-bound — "After you create a bucket, you can't change its Region"; name unique within partition, 3–63 characters, lowercase/digits/periods/hyphens); upload/download/copy objects; create folders; delete objects; empty bucket (typed confirmation "permanently delete"); delete bucket (typed name confirmation; must be emptied first).
- Bucket configuration at creation: Object Ownership / ACLs (default: ACLs disabled, bucket-owner enforced); Block Public Access (all four settings enabled by default); Bucket Versioning (off by default); Tags (cost allocation); Default encryption (SSE-S3 default; SSE-KMS / DSSE-KMS options; S3 Bucket Keys); Object Lock (retention/legal hold; automatically enables versioning).
- Protect and monitor (official section): S3 Versioning, S3 Replication, Multi-Region Access Point failover controls for disaster recovery, AWS Backup integration, Object Lock for compliance; monitoring via Storage Lens ("29+ usage and activity metrics and interactive dashboards to aggregate data for your entire organization, specific accounts, Regions, buckets, or prefixes"), Storage Class Analysis (access patterns → move data to more cost-effective storage class), S3 Lifecycle (cost management).
- Access control: IAM identities, bucket policies, ACLs, Access Analyzer for S3.
- Interfaces: Management Console, AWS CLI (high-level s3 + API-level s3api/s3control), REST API, SDKs.

---

## Cross-product Comparison

| Dimension | NetApp ONTAP | TrueNAS SCALE | Ceph Dashboard | Amazon S3 |
|---|---|---|---|---|
| Managed subject | storage system cluster (disks→local tiers→volumes/LUNs/shares/S3 buckets) | appliance (disks→pools/VDEVs→datasets/zvols→shares) | distributed cluster (drives→OSDs→pools→RBD/CephFS/RGW/NFS/iSCSI) | cloud object service (buckets→objects) |
| Estate inventory | cluster dashboard, nodes, HA pairs, SVMs | storage dashboard, pool widgets, disks screen | inventory card, hosts, OSDs, monitors | bucket list, Storage Lens org-wide dashboards |
| Provisioning | add volume/LUN (System Manager or CLI), map LUN→igroup, qtrees, quotas | pool creation wizard, datasets/zvols, shares (SMB/NFS/iSCSI/FC), quotas | pools, RBD images, CephFS, RGW users/buckets, NFS exports, iSCSI targets | create bucket + settings, folders |
| Capacity observation | capacity overview (tiers, volumes) | usage widget, Used/Available/Used-by-snapshots | capacity card (used/warning/danger), pool quotas | Storage Lens usage metrics, per-bucket metrics |
| Performance observation | latency/IOPS/throughput, hour→year windows, most active objects | reporting screens | IOPS, latency, client/recovery throughput, per-service counters | request metrics (monitoring section) |
| Health/alerts | health overview, alerts/notifications, EMS | pool status indicator, alerts, ZFS errors | cluster health status, health alerts, Prometheus silences | monitoring section (CloudWatch-class) |
| Storage-layer protection | SnapMirror, snapshots (FlexClone-class copies), SnapLock WORM | snapshots, replication tasks, scrub, encryption | RBD snapshots, RBD mirroring, scrub | versioning, replication, Object Lock |
| Tiering | Flash Pool (SSD+HDD), FabricPool (SSD+object store) | (ZFS cache/log VDEVs) | device classes per OSD | storage classes, Intelligent-Tiering, lifecycle |
| Drive-level care | disk management, RAID configs | disk health, SMART tests, disk replace/wipe | device management, SMART, health predictions, LED blink | n/a (abstracted by service) |
| Management-plane access | RBAC, SAML, MFA, multi-admin verification, OAuth2 | admin roles, 2FA, directory services | scopes×roles RBAC, SSO SAML, account lockout, audit log | IAM, bucket policies, Access Analyzer |
| Interfaces | System Manager (web) + CLI + REST API | web UI + REST API + shell | web dashboard + CLI + REST API | console + CLI + REST API + SDKs |
| Destructive-op gating | multi-admin verification (sensitive ops) | typed confirmation for export/destroy | audit logging of mutations | typed confirmations for empty/delete |

### Cross-product commonalities (Evidence layer B)

1. Physical→logical layering: drives/disks → pools (aggregates/VDEVs/placement) → logical resources (volumes/datasets/LUNs/images/buckets) → protocol surfaces (file shares, block mappings, object endpoints). Present in all four.
2. Provisioning as the defining "management" act: create logical resources from capacity and attach them to consumers (hosts, clients, applications). Present in all four.
3. The operating triad: capacity + performance + health observed continuously, with thresholds/alerts and operator actions (expand, rebalance, replace, scrub, protect). Present in all four.
4. Storage-layer protection primitives: snapshots (or object versioning), replication/mirroring, integrity scrubbing. Present in all four.
5. Management-plane identity/permission layer distinct from data access: RBAC roles/scopes, SSO/MFA, audit of management actions. Present in all four.
6. Multi-surface management: web console + CLI + REST API as peer surfaces. Present in all four.
7. Destructive operations are explicitly gated (typed confirmations, approval workflows, audit). Present in all four.
8. Quotas/limits on consumption. Present in three of four (S3 expresses limits via lifecycle/retention rather than quotas).

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

Storage Management is the operator-facing management application over storage infrastructure. Its defining core is three jointly-held structures:

1. **The storage estate as managed inventory** — the storage resources under management (physical drives/devices and the logical resources built on them: pools, volumes/LUNs, file shares, object buckets) held as persistent, individually identified records the operator can enumerate, inspect, and organize. Remove → one-off disk utilities with no estate picture.
2. **Storage provisioning/allocation** — creating, growing, and mapping storage resources from capacity to consumers (create a volume/share/bucket from a pool; map a LUN to a host; set quotas), as the normal course of operation. Remove → observation-only tooling = storage monitoring territory, not management.
3. **The storage operating loop** — capacity, performance, and health of the estate continuously observed against thresholds, surfaced as states/alerts, and acted on by the operator (expand, rebalance, replace drives, protect, retire). Remove → a static registry; the "management" dies.

Jointly-held load-bearing analysis:
- 1 alone = storage asset inventory/CMDB slice
- 2 without 1 = scripted provisioning with no estate memory
- 3 without 1+2 = a monitoring dashboard over storage metrics (Infrastructure Monitoring territory)
- 1+2 without 3 = provisioning catalog with no operations
- 1+3 without 2 = storage observability with an inventory
- 2+3 without 1 = point tools that forget

### L1 — Common Mature Structure

Very common in mature products, not required to recognize the Type:

- physical→logical layering (drives → pools → logical resources → protocol surfaces)
- storage-layer snapshots (and object versioning as the object-storage analog)
- replication/mirroring between storage systems
- quotas/reservations on consumption
- data-integrity machinery (scrub, checksums)
- drive-level health care (SMART, temperature, predictions, replacement)
- encryption at rest; WORM/compliance retention (SnapLock/Object Lock class)
- tiering across media/classes (hybrid pools, cloud tiers, storage classes)
- storage efficiency (dedup/compression)
- alerts with thresholds and state colors
- RBAC on the management plane + audit of management actions
- multi-surface management (web console + CLI + REST API)
- multi-system/fleet view (vendor SaaS portals, org-wide dashboards)

### L2 — Variant / Optional Structure

- substrate: enterprise array vs software-defined cluster vs appliance OS vs cloud object service
- protocol surface emphasis: block (iSCSI/FC/NVMe) vs file (NFS/SMB) vs object (S3-compatible)
- cloud tiering to object stores; lifecycle policies moving data to archive classes (bridge toward Archive Storage Management)
- HA/clustering machinery (HA pairs, monitor quorum, failover)
- multi-tenancy (storage VMs / tenant scoping)
- analytics depth (file-system analytics, storage-class analysis, org-wide storage lenses)
- cost dimension (cost-allocation tags, cost views)
- tape/NDMP backup integration
- app ecosystems and platform extras on appliance OSes
- vendor-operated SaaS fleet management (cloud-operated storage management posture)

### L3 — Vendor-specific (research notes only)

- ONTAP: aggregate/local tier, FlexVol/FlexGroup/FlexCache, FlexClone, qtree, SnapMirror, SnapLock, FabricPool, Flash Pool, SVM, igroup, EMS, multi-admin verification
- TrueNAS: VDEV topology types, ZFS health/scrub/auto-TRIM, zvols, SLOG/L2ARC references, TrueCloud, pool feature-flag upgrade semantics, 80% usage color threshold
- Ceph: OSD/MON/PG/CRUSH machinery, RBD/RGW/CephFS naming, ceph-mgr module architecture, security-scope RBAC vocabulary, dashboard port/SSL defaults
- S3: partitions, Block Public Access settings, Object Ownership/ACL modes, S3 Bucket Keys, Storage Lens metric count, bucket-name rules (3–63 chars), region immutability

## Vendor-specific Findings

- NetApp's multi-admin verification (approval gates for sensitive operations) is a distinctive governance feature not observed in the other samples.
- TrueNAS's pool feature-flag upgrade is explicitly irreversible — a documented one-way door.
- Ceph's dashboard is a module inside the storage system itself (ceph-mgr), illustrating that the management surface can be embedded in the substrate.
- S3's console is one section of a broader cloud console; storage management appears as a service area within a provider console (variant posture vs standalone product).

## Rejected Findings (considered and NOT promoted)

- "Storage management = array management only" — rejected: appliance, SDS, and cloud object poles satisfy the same core.
- "Storage management = fleet/SaaS monitoring" — rejected: the sampled poles manage a single system/cluster/service; the fleet layer is common-mature (L1), not definitional.
- "Snapshots/replication are definitional" — rejected: a storage management application without them (basic provisioning + operations) is still recognizably the Type; they are L1.
- "Drive-level SMART care is definitional" — rejected: the cloud object pole abstracts drives entirely and remains in-type.
- "Cost management is definitional" — rejected: only the cloud pole carries a first-class cost dimension; L2.
- "Web UI is definitional" — rejected: CLI-only and API-only management satisfy the core (LVM-class CLI storage management is the historical pole); surfaces are L1/variant.

## Boundary Findings

- **vs Backup Management** (ratifies that pass's seam from this side): backup creates recovery copies of data under protection policy (protected-scope registry, recovery points on dedicated backup storage); storage management operates the live production estate. Storage-layer snapshots/replication belong here; backup applications consume storage as a custody target. Removing provisioning+operations leaves backup; removing recovery-point custody leaves storage management.
- **vs Archive Storage Management** (ratifies that pass's seam from this side): archive = governed retirement of data into a lower-cost destination with constrained/delayed access semantics; storage management = the live estate. Object-storage lifecycle policies that move data to archive classes are the documented bridge (the archive pass documented the same seam from its side).
- **vs Disaster Recovery Platform**: DR designates workloads, replicates them to a separate location, and executes recovery there; storage replication (SnapMirror-class, RBD mirroring, S3 replication) is the storage-layer feed that DR platforms orchestrate. Storage management holds no workload-recovery record.
- **vs Infrastructure Monitoring**: monitoring is the observation plane over infrastructure entities; storage management is the control plane over the storage estate (provisioning + actions). Storage metrics land in infra monitoring as ordinary entity metrics; the sharpest test is provisioning authority.
- **vs Capacity Management**: capacity management is the forward-looking supply-vs-demand planning layer (projected exhaustion, right-sizing, what-if); storage management's capacity views are current-state + thresholds feeding such planning. Bundling is common.
- **vs Cloud Management Platform**: CMP holds a unified inventory and lifecycle over cloud estates across resource classes; storage management is storage-specific depth (pools, LUNs, buckets, protection). A cloud provider console's storage section is a storage-management surface embedded in the provider console.
- **vs Virtualization Management / Hyperconverged Infrastructure Management** (ratifies the HCI pass's pre-recorded note from this side): the managed subject decides — VMs over arbitrary infrastructure = virtualization management; converged compute+storage clusters = HCI management; the storage layer itself (drives→pools→volumes/LUNs/shares/buckets) = this Type. A hypervisor console's datastore view touches this Type's objects but its center of gravity is the VM.
- **vs Network Management / Server Management**: same §14 console shape, different estate subject (network devices / machines vs storage resources).
- **vs Database Management Console / SQL Workbench**: databases and their queries vs the storage substrate beneath them.
- **vs File Manager / Personal Cloud Drive / File Sync**: end-user files and folders vs infrastructure storage resources; a file share's *contents* are end-user territory, the share *as a storage resource* is this Type.
- **vs DCIM**: physical facilities (power/cooling/racks) vs logical storage.
- **vs Data Access Governance / DSPM**: content-level security classification and access governance vs infrastructure operations; storage management exposes the access-config surfaces (shares, bucket policies, exports) but does not classify content.
- **"去掉什么就变成另一个 Type" 判据**: remove provisioning+actions → storage monitoring (Infrastructure Monitoring territory); remove the estate inventory → one-off provisioning scripts; remove storage-substrate specificity (manage any resource class) → Cloud Management Platform; move the record to recovery copies of data → Backup Management; move the record to retired data → Archive Storage Management; move the record to workloads-with-recovery-locations → Disaster Recovery Platform.

## Historical / Market-Sample Check (§24)

- **Platform-native pole**: Windows Disk Management (disks/volumes inventory, create/format/extend volumes, online/offline status) satisfies all three L0 legs at single-host scale with no network, no cloud, no fleet. Linux LVM (pv/vg/lv CLI: create/extend logical volumes, report capacity) satisfies the core through a CLI surface alone.
- **Older-generation pole**: 2000s-era array management consoles (array inventory, LUN creation, host mapping, capacity/performance views) satisfy the core without cloud/AI/SaaS. Tape-library management sits adjacent (media/changer care is backup-territory machinery; recorded as variant context, not sampled).
- **Regional/smaller-scale pole**: single-appliance NAS (TrueNAS pole) satisfies the core without multi-system anything.
- Conclusion: the definition is substrate-, scale-, era-, and surface-neutral. The canonical core names no protocol, no vendor machinery, no cloud, no SaaS.

## Uncertainties

1. **Fleet/multi-vendor SRM pole under-evidenced**: IBM Storage Insights (403), Pure Fusion (timeout ×2), Dell (bot-wall) unreachable. The multi-system estate-management layer is evidenced only indirectly (NetApp Console referenced from official ONTAP docs; TrueCommand/TrueNAS Connect existence; S3 Storage Lens org-wide aggregation). Held as L1 common-mature with moderate confidence; no precise claims made about fleet products' internals.
2. **Second enterprise-array vendor absent**: array-side commonality (B-layer) rests on NetApp + generic patterns corroborated by TrueNAS/Ceph (zvols+iSCSI targets, RBD+iSCSI gateways). Vendor-specific array behaviors (e.g., Dell/Hitachi console specifics) unverified — none asserted.
3. **Synology DSM (consumer/SMB NAS)** JS-gated; the appliance pole is carried by TrueNAS. Consumer NAS specifics (e.g., Synology's storage pool/volume terms) unverified — none asserted.
4. **Tape-library management** not sampled; held as adjacent variant context only.
5. **Storage-virtualization appliances** (SAN-volume-controller class, pooling heterogeneous arrays) not sampled; likely a variant of this Type (virtualization of storage resources) — recorded as uncertainty, no claims.

## Final Synthesis

Storage Management is the operator-facing management application over storage infrastructure. Its defining core is the storage estate as managed inventory + storage provisioning/allocation + the storage operating loop (capacity/performance/health → alerts → actions). Everything else commonly associated with the category — snapshots, replication, tiering, encryption, scrubbing, drive care, RBAC, audit, CLI/API surfaces, fleet portals, cost views — is common mature structure or variant machinery, not definition. The Type spans enterprise arrays, software-defined clusters, NAS appliances, and cloud object storage services; the substrate is a variant axis, not the identity. The sharpest boundaries: provisioning authority separates it from monitoring; the live-estate record separates it from backup/archive/DR; storage-substrate specificity separates it from cloud management platforms; the managed subject (storage layer, not VMs, not network devices, not machines, not databases, not files) separates it from every other §14 console sibling.
