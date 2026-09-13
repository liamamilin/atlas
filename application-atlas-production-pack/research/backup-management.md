# Research Notes — Backup Management

Research date: 2026-09-06
Slug: backup-management
Directory leaf: Backup Management (§14 IT, Cloud & Infrastructure)

## Research Goal

Understand, from real products, what a Backup Management application is: what objects exist inside it, how protection is configured and executed, how backed-up data is stored and retained, how restore happens, and where the boundary lies against Disaster Recovery Platform, Storage Management, Archive Storage Management, File Sync, and Data Replication.

## Initial Boundary

Working hypothesis before research:

- Core use: centrally define what data/systems to protect, execute scheduled backup copies, keep multiple point-in-time copies, and restore data from those copies after loss, corruption, or attack.
- Users: IT administrators, backup operators, backup architects, MSPs.
- Nearest neighbors: Disaster Recovery Platform (failover orchestration), Storage Management (production storage administration), Archive Storage Management (compliance retention), File Sync (current-state mirroring), Data Replication (live copies), Endpoint Management (device administration that may bundle backup).
- Unknowns: whether "management" implies multi-workload centrality; how cloud-native managed services change the model; whether job execution/monitoring belongs to the defining core.

## Research Questions

1. What is a "protected workload" and how does it get registered into the backup system (agent / agentless / API)?
2. How is protection configured: what does a backup policy or job definition contain (scope, target, schedule, retention)?
3. What is the storage side: repositories, vaults, pools, volumes? How are recovery points kept and expired?
4. How does restore work: granularity options, targets, tracked restore operations?
5. What does the operational loop look like: job execution, status, alerts, reports?
6. How do products differ by deployment and era: software (self-hosted), appliance, cloud-native managed service, MSP platform, open source?
7. Where is the edge with DR, archive, sync, and replication?

## Representative Products

Selected for market position, philosophy diversity, customer-tier diversity, and documentation accessibility:

| Product | Philosophy / tier | Docs access |
|---|---|---|
| Veeam Backup & Replication | market leader, virtualization-centric, self-hosted software | A evidence (user guide fetched) |
| Commvault | enterprise suite, single-platform data protection | positioning only (docs portal root reachable; content pages JS-gated) |
| AWS Backup | cloud-native fully-managed service | A evidence (docs fetched) |
| Microsoft Azure Backup | cloud-native managed service (second cloud sample) | A evidence (docs fetched) |
| Bacula Community | open-source classic network backup, tape-era lineage | A evidence (official pages fetched) |
| Acronis Cyber Protect Cloud | SMB/MSP integrated backup + security platform | positioning + FAQ evidence (product pages fetched; KB not fetched) |
| Rubrik | modern converged data security platform | NOT DOCUMENTED — docs login-gated 2×; used only as market anchor |

## Sources

- Veeam Backup & Replication 13 User Guide — About page (helpcenter.veeam.com/docs/backup/vsphere/overview.html), fetched 2026-09-06; Creating Backup Jobs page (backup_job.html), fetched 2026-09-06 (nav structure + step names observed).
- AWS Backup Developer Guide — "What is AWS Backup?" (docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html), fetched 2026-09-06.
- Microsoft Learn — "What is Azure Backup?" (learn.microsoft.com/en-us/azure/backup/backup-introduction-to-azure-backup), fetched 2026-09-06.
- Bacula.org — "What is Bacula?" (bacula.org/what-is-bacula/) and homepage (bacula.org), fetched 2026-09-06.
- Acronis — Cyber Protect Cloud Backup product page (acronis.com/en-us/products/cloud/cyber-protect/backup/) and documentation index (acronis.com/en-us/support/documentation/), fetched 2026-09-06.
- Commvault — Documentation portal root (documentation.commvault.com), fetched 2026-09-06 (portal structure only).
- Rubrik — docs.rubrik.com pages returned Okta sign-in wall (2 attempts, 2026-09-06) — abandoned per network-restriction rule.

## Product Observations

### Veeam Backup & Replication (evidence layer A)

- Self-description: "a comprehensive data protection and disaster recovery solution… create image-level backups of virtual, physical and cloud machines and restore from them"; "a centralized console for administering backup, restore and replication operations in all supported platforms… automate and schedule routine data protection operations."
- Main features enumerated by vendor: Backup; Restore (multiple recovery options: Instant Recovery, image-level restore, file-level restore, application-item restore); Replication; CDP; Backup Copy (copy backup files to a secondary repository); Storage-system snapshot integration; Tape device support; Recovery verification (SureBackup — testing backups before recovery); Scale-Out Backup Repositories (distribute data across performance/capacity/archive tiers).
- Protected objects: many hypervisors (vSphere, Hyper-V, Nutanix AHV, Proxmox, oVirt, Xen, Scale, Sangfor…), cloud workloads (AWS/Azure/GCP VMs and managed services), Microsoft Entra ID, unstructured data (file servers, file shares, NAS, object storage), physical machines via per-OS agents (Windows/Linux/macOS/Solaris/AIX) with Veeam acting as "a centralized control center for deploying and managing agents."
- Backup infrastructure components (separate roles): Backup Server (control), Backup Proxies (data path), Backup Repository (backup storage), Tape Server, WAN Accelerator, Mount Server, Enterprise Manager (self-service/reporting), desktop console + Web UI.
- Backup jobs are created through a wizard (objects → storage → schedule/retention → guest processing → notifications); job scheduling, priorities, concurrent-task limits, throttling exist.
- Administration: users and roles with inventory scope, repository scope, restore permissions, restore-target scope; four-eyes authorization; SAML; email/SNMP/syslog notification configuration; session history; security & compliance analyzer; malware detection (scan backups, secure restore with AV/YARA scans); backup encryption with password-loss protection.

### Commvault (evidence layer C — portal structure only)

- Documentation portal organizes product content by protected workload class: Virtualization, Applications (Exchange, AD, M365), Databases (SQL, Oracle, MySQL), File Servers, Snapshots (IntelliSnap array-snapshot integration); control node "CommServe" and data-mover "MediaAgent"; "Command Center" web console; CommCell environment concept; multi-tenant CommCell configuration; HyperScale Appliance; Threatwise cyber-recovery content.
- Claims kept conservative because operational doc pages were not reachable (JS-loaded index).

### AWS Backup (evidence layer A)

- Self-description: "fully-managed service… centralize and automate data protection across AWS services, in the cloud, and on premises… configure backup policies and monitor activity for your AWS resources in one place."
- Central concepts in vendor docs: **backup plans** (policies defining schedule, lifecycle, vault, copies) applied to **resources** (assignable by tag); **backup vaults** (storage containers separating backups from source, with encryption and resource-based access policies); **recovery points** stored in vaults; **backup jobs** and **restore jobs** (both monitorable in a console dashboard); lifecycle (warm→cold storage transition); cross-Region and cross-account backup copies (fan-in/fan-out via AWS Organizations); **Audit Manager** (controls + daily compliance reports); immutable backup content, **Vault Lock** (WORM, retention cannot be altered or shortened); incremental backups for supported resource types; CloudWatch/EventBridge/CloudTrail/SNS monitoring integrations; broad resource table (EC2, S3, EBS, DynamoDB, RDS/Aurora, EFS, FSx, Redshift, SAP HANA, EKS, VMware Cloud…).
- Full-management properties: independent encryption with vault KMS key, `arn:aws:backup` identity for backups, centralized billing — the backup layer is a distinct custody layer over the source resources.

### Microsoft Azure Backup (evidence layer A)

- Self-description: service to "back up your data and recover it from the Microsoft Azure cloud."
- Protectable: on-premises files/folders/system state via MARS agent; on-prem VMs via DPM/MABS; Azure VMs (via backup extension); managed disks; Azure Files; SQL Server/SAP HANA in VMs; PostgreSQL; Blobs (operational/vaulted); AKS; MySQL Flexible; SAP ASE; Data Lake Storage; Elastic SAN.
- Concepts: **Recovery Services vault / Backup vault** ("independent and isolated backups… stored in a Recovery Services vault with built-in management of recovery points"); short- and long-term retention; application-consistent backups ("a recovery point has all required data to restore"); centralized monitoring/alerting in the vault, scale via Azure Monitor; storage redundancy choices (LRS/GRS/ZRS); ransomware security features; automatic storage management (pay-per-use).

### Bacula Community (evidence layer A)

- Self-description: "a set of computer programs that permits the system administrator to manage backup, recovery, and verification of computer data across a network of computers of different kinds… a network Client/Server based backup program," scalable from one computer to hundreds; media include tape and disk; positions itself as the step up from tar/dump (catalog services) and as comparable to commercial packages (Legato Networker, ARCserveIT, Arkeia) — historical lineage evidence.
- Five components: **Director** (supervises all backup, restore, verify and archive operations; scheduling), **Console** (TTY/QT/wxWidgets interfaces to Director), **File daemon** (client-side agent providing file attributes/data and performing restore-side file handling), **Storage daemon** (reads/writes tapes or disk files), **Catalog** (SQL database of all Volumes, Jobs and Files saved — "permits efficient restoration and Volume management").
- Terminology: **Job** (config resource: type backup/restore/verify, level full/incremental/differential, FileSet, Storage, Pool), **Schedule** resource, **FileSet** (includes/excludes, compression/encryption/signatures), **Volume** (archive unit: tape or named disk file, software-labeled), **Pool** (volumes), **Retention Periods** (File/Job/Volume retention — catalog pruning vs volume reuse; "Bacula will normally never overwrite a Volume that contains the only backup copy of a file"), **Restore** (operation choosing files, normally a small set; full restore after disk crash), **Verify** (compare current attributes vs catalog, or verify volume contents), **Bootstrap file** (restore without catalog), **Scan** (rebuild catalog from volumes).
- Explicit boundary statement: "Bacula is a backup, restore and verification program and is not a complete disaster recovery system in itself, but it can be a key part of one."
- Feature list (homepage): migration/copy jobs (multi-tier), incremental/differential/synthetic (VirtualFull), verify volume data, compression, cloud storage support, tape autochangers, plugins (Exchange, Docker, Kubernetes), LDAP console auth, TLS.

### Acronis Cyber Protect Cloud (evidence layer A positioning / B for operational claims)

- Positioning: MSP platform combining "backup, disaster recovery, cybersecurity, and endpoint management in one integrated solution… one console and one agent."
- Backup service claims: physical (file/disk/image backup, forensic backups, CDP), virtual (agentless VMware/Hyper-V/Nutanix AHV; agent-based guest OS), SaaS (M365, Google Workspace), Entra ID backup; Instant Restore; P2V/V2V/V2C conversions; one-click recovery for many machines; integrated DR add-on for cloud failover from backups; anti-malware scanning of backup images and "Safe Recovery" to avoid restoring infected machines; geo-redundant and immutable storage, replication, encryption; archival retention; multi-tenant management (customers/accounts, plans, monitoring, alerts, reporting); pay-per-workload/GB, bring-your-own or Acronis cloud storage.
- FAQ operational statements (vendor, treat as claims): agents downloadable from management console per customer account; deduplication at archive level per machine (no centralized dedup server); backup runs low-priority; restore disk-size flexibility rules; bootable-media bare-metal restore; RPO bounded by workload size/bandwidth with a vendor-stated minimum threshold of 10 minutes (precise vendor claim — kept out of canonical document).

### Rubrik (not documented)

- docs.rubrik.com returns an Okta sign-in wall (2 attempts). Market position (converged backup/instant recovery/data security) is common knowledge; no operational claims from Rubrik used anywhere in this research. Listed as a market anchor only.

## Cross-product Comparison

| Dimension | Veeam | Commvault | AWS Backup | Azure Backup | Bacula | Acronis CPC |
|---|---|---|---|---|---|---|
| Protected-scope registration | add hypervisor/agent/cloud account to inventory; select objects in job | agents per workload class (portal structure) | resource assignment to plan (incl. by tag) | enable protection in vault; extensions/agents | Client/File daemon per machine + FileSet | agent install per workload/account; agentless for hypervisors |
| Policy object | backup job (wizard: objects, storage, schedule, retention, guest processing) | backup plan/job per agent (not directly observed) | backup plan (schedule, lifecycle, vault, copy) applied via assignment/tag | backup policy (schedule, retention) + protection config | Job + FileSet + Schedule + Storage + Pool resources | backup plan per device/account |
| Backup storage unit | Backup Repository; Scale-Out Repository (perf/capacity/archive tiers) | MediaAgent storage pools / HyperScale | backup vault (separation + access policies + immutability) | Recovery Services vault / Backup vault | Volume in Pool, managed by Storage daemon | Acronis cloud storage, local, network, BYO public cloud; immutable/geo-redundant options |
| Point-in-time unit | restore points in backup files | recovery points (not directly observed) | recovery point (ARN-identified, immutable content) | recovery points with "built-in management" | saved job data on labeled Volumes + Catalog records | backup archives per machine |
| Job execution & tracking | sessions with status; notifications email/SNMP/syslog; priorities; throttling | jobs (not directly observed) | backup jobs monitorable in dashboard; EventBridge/CloudWatch/CloudTrail/SNS | centralized monitoring and alerting in vault; Azure Monitor | Director schedules; Catalog records jobs/status; Monitor service | centralized plans, monitoring, alerts, reporting |
| Restore | Instant Recovery, image-level, file-level, application items, to original/new location | not directly observed | restore jobs; per-resource-type restore | full VM / disk / file browse / item-level per resource | restore operation (small set or full), bootstrap-file restore, bare-metal via rescue media | instant restore, P2V/V2V/V2C, item-level for M365, bare metal via bootable media |
| Retention | retention policy in job; GFS-style scheme options | yes (not directly observed) | lifecycle policy; retention enforced by vault; Vault Lock WORM | short- and long-term retention in policy | File/Job/Volume retention periods; never overwrite sole copy | archival retention options |
| Secondary copies | Backup Copy job to secondary repository; tape; Cloud Connect | copy jobs (not directly observed) | cross-Region / cross-account copies | GRS/ZRS redundancy; cross-region options (not directly observed on this page) | Copy/Migration jobs; multiple volumes | replication, geo-redundant storage |
| Verification | SureBackup recovery verification; malware scans of backups | not observed | Audit Manager controls & reports (compliance verification) | not observed on this page | Verify jobs; Verify Volume Data | anti-malware scan of images; Safe Recovery |
| Delivery form | self-hosted software (+ appliance) | software / appliance / SaaS | fully-managed cloud service | fully-managed cloud service | open-source daemons, self-hosted | SaaS platform for MSPs, multi-tenant |
| Identity of "backup layer" | dedicated console + infrastructure components | dedicated platform | separate custody layer (`arn:aws:backup`, vault KMS, centralized billing) | vault-based isolated layer | separate Director/Storage/Catalog | one agent/one console but separate backup service module |

## Canonical Abstraction

### L0 — Defining Invariant

Smallest structure without which the application stops being recognizable as Backup Management:

1. **Protected scope** — a managed registry of what is to be protected (data sets / machines / applications / cloud resources), explicitly brought under protection.
2. **Backup policy** — a persistent definition of how each protected item is copied: what to include/exclude, where to write, when to run, how long to keep. (Bacula: Job+FileSet+Schedule+Storage+Pool; Veeam: backup job; AWS: backup plan + assignment; Azure: backup policy.)
3. **Recovery points on dedicated backup storage** — executed copies are stored as point-in-time recovery points in backup storage managed by the application (repository / vault / pool of volumes), distinct from the source, retained over time under the policy; multiple recovery points per protected item accumulate and expire.
4. **Restore** — the ability to recover data by choosing a protected item, a recovery point, and a target, and to carry out the recovery as a tracked operation.

Remove protected scope → it is storage management or a copy tool. Remove recovery points/retention → it is sync or replication (current-state mirroring). Remove restore → it is not backup at all. Remove the policy/schedule layer and copy-from-source step → it is archive storage or snapshot tooling.

### L1 — Common Mature Structure (evidence layer B)

- Backup job execution as the unit of work, with tracked status (success/warning/failed), history, and failure alerting — present in all six samples.
- Central management console across many workloads: dashboards, job history, reports, configuration of infrastructure/credentials.
- Workload connectors: agents for physical/endpoint, agentless or hypervisor-integrated for VMs, native APIs for cloud resources, per-application plugins for databases/mail.
- Storage efficiency: incremental/differential/synthetic-full levels, deduplication, compression (Bacula explicitly; Veeam "optimizes data transfer and resource consumption"; AWS incremental; Acronis per-machine dedup).
- Catalog/index of backed-up content enabling browse and item-level restore (Bacula Catalog as the explicit differentiator vs tar/dump; Veeam file-level/item-level restores; Azure file browse; AWS resource-type restores).
- Restore granularity spectrum: full/VM/system recovery (incl. instant recovery, bare-metal), file/folder-level, application item-level; restore to original or alternate location.
- Retention management: expiration, pruning, GFS-style schemes; lifecycle tiering to cheaper storage.
- Secondary copies: backup copy to second repository/site/region/account, offsite/offline media (tape) — the 3-2-1 practice is productized as copy jobs.
- Backup verification: test-recovery/sandboxed verification (Veeam SureBackup), Verify jobs (Bacula), compliance-style control checks (AWS Audit Manager).
- Role-restricted restore (Veeam restore-permission roles with target scope; AWS vault access policies; Acronis per-tenant accounts) — administration of who may restore.
- Notifications and reporting for operations and compliance (email/SNMP/syslog in Veeam; CloudWatch/EventBridge/SNS in AWS; Azure Monitor; Acronis reporting; Bacula console/monitor status).

### L2 — Variant / Optional Structure

- Media and target substrate: tape/autochangers (Bacula, Veeam tape server), disk/dedup appliances, object storage, cloud tiers incl. cold storage (AWS lifecycle), managed vaults (AWS/Azure).
- Immutability and anti-ransomware posture: WORM/vault-lock retention locking, immutable storage, malware scanning of backups, secure/safe restore gates (AWS Vault Lock; Veeam secure restore; Acronis immutable storage + Safe Recovery). Strong current-market driver, but tape-era and plain products fit the Type without it.
- Cross-site copy topologies: cross-region/cross-account (AWS Organizations fan-in/fan-out), backup-copy chains, replication of backup data (Veeam backup copy; Acronis replication).
- Workload-class emphasis variants: VM-centric, endpoint/laptop backup, database/application backup, NAS/file share backup, SaaS data backup (M365/Google Workspace), identity-data backup (Entra ID).
- Near-continuous protection: CDP/very short RPO (Veeam CDP; Acronis CDP claim) — shades into replication.
- Deployment/business-model variants: self-hosted software, appliance, fully-managed cloud service, MSP multi-tenant platform, consumer/home product line (Acronis True Image; historical home backup tools).
- DR-adjacent modules: cloud failover from backups, replica failover, DR orchestration (Acronis DR add-on; Veeam replication) — module, not core.
- Archive-tier integration: move aged recovery points to archive storage; compliance retention on backup data.

### L3 — Vendor-specific (kept in Research Notes)

- Veeam: Scale-Out Backup Repository tiering, SureBackup/vPower instant recovery machinery, Backup Proxy / WAN Accelerator / Mount Server roles, Veeam Cloud Connect (service-provider backup target), Enterprise Manager self-service, four-eyes authorization, password-loss protection with Enterprise Manager keys, Security & Compliance Analyzer, Threat Hunter/YARA secure restore, Veeam Intelligence AI assistant.
- Commvault: CommServe/MediaAgent/CommCell, IntelliSnap, HyperScale Appliance, Threatwise.
- AWS Backup: backup-plan cron semantics, Vault Lock compliance/governance modes, Audit Manager control framework and daily reports, `arn:aws:backup` resource identity, cross-account fan-in/out via Organizations, cold-storage eligibility per resource type, restore testing as a paid capability.
- Azure Backup: Recovery Services vault vs Backup vault distinction, MARS agent, DPM/MABS, LRS/GRS/ZRS replication options, operational vs vaulted Blob backup, 10-year PostgreSQL retention (vendor claim).
- Bacula: daemon architecture (Director/File/Storage/Monitor), catalog on MySQL/PostgreSQL/SQLite, resource files (Job/FileSet/Pool/Volume/Schedule), bootstrap files, bscan catalog rebuild, VirtualFull synthetic backups, Bacularis web UI (third-party).
- Acronis: one-agent/one-console architecture, Active Protection anti-ransomware, per-workload/GB MSP billing, "10-minute minimum RPO threshold" FAQ claim, forensic backups, Cyber Frame IaaS.

## Rejected Findings (considered, rejected as canonical)

- "Backup requires an agent on every protected machine" — rejected: Veeam/Acronis/AWS/Azure protect VMs/cloud resources agentlessly or via hypervisor/cloud-native extension; connectors are implementation, not invariant.
- "Backup targets are tape" — rejected: historical; disk/object/vault dominate current products; tape survives as a variant (Veeam Tape Server, Bacula, tape autochanger support).
- "Backup = 3-2-1 multi-copy discipline" — rejected: the 3-2-1 rule (Acronis FAQ cites it) is an operational practice productized via copy jobs; single-copy products are still Backup Management.
- "Application-aware processing / VSS is core" — rejected: it is a per-workload enhancement; file-level backup products work without it.
- "Immutability is definitional" — rejected: ransomware-era addition (Vault Lock, immutable storage); absent in tape-era and many current deployments.
- "Daily schedule" or any specific cadence — rejected: cadence varies from near-continuous (CDP) to monthly; no invariant cadence.
- "Central web console is definitional" — partially rejected: every sampled product has one, but Bacula's primary surface is a TTY console + config files; the *management function* is invariant, a particular GUI form is not.
- "Backup Management includes DR failover" — rejected: sampled vendors ship DR as separate module/add-on; Bacula explicitly disclaims being a DR system.

## Boundary Findings

- **vs Disaster Recovery Platform**: backup keeps restore-able copies and restores data into (possibly the same) infrastructure; DR orchestrates standing-up services on secondary infrastructure with RTO commitments (failover, runbooks, non-disruptive tests). Sharpest seam: *the unit of recovery*. Backup restores data/objects; DR restores service availability via failover. Bacula states it outright ("not a complete disaster recovery system in itself"). Vendors blur it by shipping DR add-ons (Acronis DR from backups; Veeam replication). Test: remove the copy-and-restore loop, keep only orchestrated failover → DR Platform.
- **vs Storage Management**: backup writes to dedicated backup storage it manages as a custody layer; storage management administers production storage (capacity, performance, pools, provisioning). The backup repository/vault is a managed *target*, not administered production infrastructure. Test: remove the copy/restore purpose and manage the storage for its own performance/capacity → Storage Management.
- **vs Archive Storage Management**: backup copies are restore-oriented, rotated on schedules, and eventually expired; archive is retention-oriented storage of data no longer in active use, kept for compliance, rarely restored. Overlap: long-term backup tiers, backup-to-tape-as-archive. Test: remove rotation/expiry and restore-as-primary-operation, keep write-once long retention → Archive.
- **vs File Sync / Personal Cloud Drive**: sync mirrors current state (deletions usually propagate; version history is incidental and bounded); backup accumulates deliberate recovery points under retention policy with an explicit restore path. Test: remove recovery-point retention and policy, keep mirroring → File Sync.
- **vs Data Replication Platform (§13)**: replication maintains live, continuously updated copies in another system for availability/consumption; backup stores point-in-time restore positions in managed backup storage. CDP products straddle; the seam is *restore from backup storage* vs *serve the replica*.
- **vs Endpoint Management / UEM**: some endpoint suites bundle laptop backup; UEM's core is configuration/app/security administration of devices, not recovery-point custody. Test: remove recovery points → still UEM; that is the direction of the boundary.
- **vs storage-native snapshots**: snapshot features live in storage systems; backup products may *use* them as the copy mechanism (IntelliSnap, Veeam storage-system snapshot integration) but add cross-platform policy, catalog, retention, and restore. Snapshot-only tooling without the managed restore-point custody is not Backup Management.

## Historical / Market-Sample Check

- Tape-era network backup (Bacula lineage; Bacula's own references to tar/dump/Legato Networker/ARCserveIT; tape volumes, pools, rotation, retention periods): fits the L0 fully — protected scope (clients/FileSet), policy (Job+Schedule+Storage+Pool), recovery points (saved jobs on labeled volumes), restore (restore operation, bootstrap files). Definition does not depend on cloud, immutability, or snapshots.
- Cloud-native managed services (AWS/Azure): also fit — the vault is the backup storage, the recovery point is first-class, the plan is the policy; the "management" is centralized across services. The delivery form differs (no local console) but the model is the same.
- Consumer/home backup (disk-image tools): fits with protected scope = personal disks, policy = simple schedules, restore = image restore. Confirms the Type is substrate-agnostic.
- Conclusion: the canonical core holds across eras and delivery forms; era-specific mechanisms (tape, GFS rotation, WORM locking, cold tiers) are variants.

## Uncertainties

- Commvault operational specifics (plan/job object model, restore flows) not directly observed — portal JS-gated; only portal structure used; Commvault claims kept at positioning level.
- Rubrik unreachable (login wall) — excluded from evidence; its absence does not affect the model (over-represented by Veeam in the same philosophy family).
- Acronis operational statements come from product-page FAQ (vendor claims), not the product KB; treated as layer-B evidence; the "10-minute minimum RPO threshold" was not promoted to the canonical document.
- Azure Backup cross-region copy behavior was not verified on the fetched page (only storage-redundancy options observed); no cross-region claim written for Azure.
- Whether "Backup Management" should also cover *personal* backup tools as a variant was decided yes (same defining core); if the directory later splits consumer backup as a separate Type, the Variants section already supports the split.

## Final Synthesis

A Backup Management application is the operator-facing system of record and control plane for data protection: an organization registers the workloads it must protect, defines persistent backup policies (scope, target, schedule, retention), the system executes backup jobs that store point-in-time recovery points in dedicated backup storage it manages, and it restores data from those recovery points — at chosen granularity, to original or alternate targets — as tracked operations, all surfaced through a central administrative console with job status, alerting, and reporting.

The defining core is exactly four things: protected scope, backup policy, retained recovery points on dedicated backup storage, and restore. Everything else — agents vs agentless connectors, dedup, catalogs, verification, secondary copies, immutability, tape, cloud tiers, DR modules, MSP tenancy — is common mature structure, variant, or vendor-specific detail.
