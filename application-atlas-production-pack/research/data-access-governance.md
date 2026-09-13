# Research Notes — Data Access Governance

Research date: 2026-09-07

## Research Goal

Understand what a Data Access Governance (DAG) application actually is and how it works, from real products: what data it governs, what structures it maintains, who uses it, what workflows it runs, and where it begins/ends relative to neighboring Types (IGA, DSPM, DLP, Data Governance/Catalog, PAM, Insider Risk).

## Initial Boundary (hypothesis before research)

- Hypothesis: DAG products read the access-control state of data stores (especially unstructured data — file shares, collaboration sites, cloud storage), compute "who can actually access what," evaluate exposure risk, and drive access decisions (reviews, certifications, requests, remediation) toward least privilege.
- Likely confusions: Identity Governance / IGA (identity-centric access governance), DSPM (cloud data posture), DLP (egress prevention), Data Governance Platform / Data Catalog (data-as-asset governance — name collision), PAM (privileged accounts).
- Unknowns going in: Is sensitive-data classification definitional? Is activity monitoring definitional? Is automated remediation definitional or do some products stop at analysis? How deep does IGA integration run?

## Research Questions

1. Which data stores do DAG products connect to (file servers, NAS, SharePoint/OneDrive/Teams, cloud object storage, databases, SaaS)?
2. How is the "who can access what" map built — permission discovery, group nesting, inheritance, sharing links, effective-access computation?
3. What access-risk findings do products surface (open access, over-permission, stale entitlements, broken inheritance, external sharing, ghost accounts)?
4. What governance actions exist — access reviews/certifications, access requests, remediation, ownership assignment? Who decides?
5. What role does sensitive-data discovery/classification play?
6. What role does activity/usage monitoring play (actual use vs granted access)?
7. Who are the users and what are the interfaces (admin console, owner portal, self-service request portal, reports)?
8. How do products relate to identity providers / IGA platforms?
9. Boundary behavior vs DSPM, IGA, DLP, Data Governance Platform, PAM, Insider Risk.

## Representative Products

Chosen for market representation, documentation completeness, and different product philosophies/customer tiers:

| Product | Pole | Evidence tier reached |
|---|---|---|
| Varonis Data Security Platform — "Data access governance" pillar | data-security platform pole; automation-heavy; heritage in file-share analysis | Tier 2 (official product pages); operational docs behind login |
| SailPoint Data Access Security (formerly File Access Manager) | IGA-integrated pole — extends identity governance to data | Tier 2 (product page) + Tier 1 (product documentation index) |
| Netwrix Access Analyzer (formerly Enterprise Auditor; STEALTHbits heritage) + Access Information Center | on-premises audit/analysis pole; mid-market; owner-review workflows | Tier 1 (operational docs, 4 pages) |

Attempted and dropped: Securiti (docs site JS-only; marketing page returned an image only — no textual evidence), Lepide (transport error / 404), Microsoft SharePoint-native "data access governance" page (404). These are recorded as source-access limitations; no claims are made about them from memory.

## Sources

- Varonis — Data Access Governance product page: https://www.varonis.com/platform/data-access-governance (fetched 2026-09-07)
- Varonis — Data Security Platform page: https://www.varonis.com/products/data-security-platform (fetched 2026-09-07)
- SailPoint — Data Access Security product page: https://www.sailpoint.com/products/data-access-security/ (fetched 2026-09-07)
- SailPoint — Data Access Security documentation index: https://documentation.sailpoint.com/das/help/index.html (fetched 2026-09-07)
- SailPoint — documentation root: https://documentation.sailpoint.com/ (fetched 2026-09-07)
- Netwrix — documentation root: https://docs.netwrix.com/ (fetched 2026-09-07)
- Netwrix — Access Analyzer docs (v2601) main + Overview + Key Concepts: https://docs.netwrix.com/docs/accessanalyzer/2601 , /overview/ , /overview/keyconcepts (fetched 2026-09-07)
- Netwrix — Access Information Center docs (v12.0): https://docs.netwrix.com/docs/accessinformationcenter/12_0 (fetched 2026-09-07)

## Product A — Varonis (Data Security Platform, "Data access governance" pillar)

Evidence layer: A (direct observation of official product pages); no operational help content reachable (community/product docs behind my.varonis.com login) — recorded as limitation.

### Key observations

- Positioning (T2): "Visualize access to sensitive data across your environment... Streamline how you implement least-privilege in your enterprise." Tagline: "See exactly who can touch sensitive data at all times."
- DAG is one named pillar inside a wider data security platform (alongside data discovery & classification, DSPM, database activity monitoring, UEBA, DLP, identity posture, ITDR, email security). The platform does NOT collapse DAG into DSPM — they are separate named capabilities.
- **Effective permissions analysis**: "unravels nested groups, permissions, and inheritance to provide you with an accurate picture of what users can access. Discover all associated permissions normalized across files, sites, mailboxes, S3 buckets, databases, and more." — direct evidence for the effective-access-map concept and multi-store coverage.
- **Bi-directional view of access** ("Get a bi-directional view of access"): from a user to their data, and from data to its users.
- **Blast-radius framing**: "Overexposed data is the #1 concern... central to removing errant data permissions and reducing data risk." Marketing metric ("reduces your blast radius by 90% in just 180 days") — vendor claim, not a structural fact; excluded from canonical doc.
- **Self-service access**: "Users can easily request access to applications, cloud resources, and security groups from an intuitive web UI. Users who no longer need access are automatically recommended for removal to maintain least-privilege." — evidence for access-request workflow + usage-based removal recommendations.
- **Entitlement management**: "tracks and reports on elevated entitlements, prevents errors with logic checks, and rolls back changes when needed. Manage access control changes in a sandbox... and commit them when ready." — evidence for managed, reversible permission changes.
- **Access remediation**: "Eliminate unnecessary permissions at scale with comprehensive rules and policies... fixes problems at the source continuously and automatically." — evidence for policy-automated remediation.
- **Comprehensive auditing**: normalized, human-readable audit trail; scheduled reports on data access and exposure.
- Coverage surfaces: Microsoft 365/SharePoint/OneDrive/Exchange, Windows file shares & NAS, Google Workspace, Box, AWS/Azure/GCP, databases, Salesforce, etc.
- Problem framing: broad default access ("every employee has access to more than 17 million files" — vendor stat, excluded from canonical doc).

## Product B — SailPoint Data Access Security

Evidence layer: A (product page + official documentation index). Documentation index is operational (Tier 1); section bodies not fetched individually.

### Key observations

- Positioning (T2): "Govern and secure access to sensitive data for humans and machines." "Data Access Security extends identity security and access controls to data." Blurb: "Enhance governance and protection for critical unstructured data." Integrated SaaS solution with Identity Security Cloud (ISC).
- Vendor's own definition of the practice (FAQ): "Data access governance is the practice of controlling and monitoring who has access to data across an organization. It ensures only authorized users — including employees, bots, contractors, and AI agents — can access sensitive or regulated information."
- Use cases (T2): (1) **Discover and classify sensitive data** (automatic classification, sensitivity labels, import third-party classification tags, cloud/on-prem/SaaS); (2) **Govern and secure sensitive data** (identify over-privileged access, detect externally shared sensitive content, remove defunct accounts with sensitive access, "automatically right-size data access and limit blast radius based on roles, usage, and customizable policy"); (3) **Accelerate compliance readiness** — "Traditional certifications lack context. Data Access Security adds data-centric risk insight to SailPoint access certifications — showing who accessed what data, how often, and why... automate data owner reviews... Enable fine-grained access reviews to data assets."
- Monitoring: "detects risky behavior such as unauthorized downloads, off-hours access, and external file sharing, and automatically triggers alerts or remediation workflows."
- Documentation index (T1) reveals the full operational object model:
  - **Account and Entitlement Aggregation** — sources (e.g., Active Directory), identity collectors, virtual appliances, collecting accounts and entitlements. Identity-side plumbing feeds the data-access model.
  - **Administrator Help — Crawling; Permissions; Data Dictionary; Business Resource Owners** — crawling of data resources; permission analysis; a data dictionary; owner assignment.
  - **Access Certification — Campaign Management / Campaign Creation / Making Decisions / Templates** — certification campaigns are a first-class workflow with decisions and templates.
  - **Data Ownership Election — campaigns, voting for data owner candidates, reviewing** — owners are not only assigned; they can be *elected* through campaigns where candidates vote. (Notable structure: ownership is treated as a governance problem of its own.)
  - **Data Classification — policies, rules, global rules, OCR, re-scanning, results** — classification is a policy-driven subsystem.
  - **Forensics — Activity Forensics, Permissions Forensics, Identity Forensics, Data Classification Forensics; queries; reports** — four query surfaces over activity, permissions, identity, and classification.
  - **Alerts — alert rules, discard rules, viewing.**
  - **Resources — Permissions, Data, Owners.**
  - Reports (My Reports, templates); Test Connection.
- The product exists in two generations: on-prem File Access Manager ("Govern access to unstructured resources on prem and in the cloud") and SaaS Data Access Security — same Type across deployment models.

## Product C — Netwrix Access Analyzer + Access Information Center

Evidence layer: A (operational documentation, strongest source in sample).

### Key observations (Access Analyzer v2601 docs)

- Self-description: "an on-premises Data Security Posture Management (DSPM) platform that helps security and compliance teams discover where sensitive data lives, **who has access to it, and where access risks exist**... enables data governance — without sending data to the cloud." (Vendor label-drift toward DSPM noted; behavior is classic DAG.)
- Problem statement: "Permissions expand over time, inheritance breaks, and stale data sits untouched for years — all without anyone knowing."
- Sources connected: **File servers** (SMB/CIFS — "permissions, folder-level ACLs, file ownership, and sensitive data content"), **SharePoint Online** ("permissions, sharing links, and sensitive data"), **Active Directory** (users/groups/memberships/risks), **Entra ID** (users/groups/roles, MIP sensitivity labels).
- **Scans are read-only**: "Access Analyzer doesn't modify files, permissions, or directory objects on any scanned source." — critical variation: analysis-first posture; the same vendor family ships enforcement elsewhere.
- Key capabilities table: **Sensitive Data Discovery** (PII/PHI/credentials/financial patterns; taxonomies mapped to GDPR, HIPAA, PCI DSS, CCPA); **Access Risk Analysis** ("open access, overly permissive ACLs, broken permission inheritance, and stale entitlements... Shows effective permissions for any user or group"); **Identity Inventory** (group nesting, stale accounts, roles); **File Activity Monitoring** (real-time file/SharePoint events "from Netwrix Activity Monitor... Requires a separate Netwrix Activity Monitor deployment") — activity monitoring as an optional add-on product.
- Key Concepts (T1 vocabulary):
  - **Identity** — "A user or group account from an IAM source"; **Entitlement** — "A permission or access right granted to an identity on a data source"; "Access Analyzer maps identities to entitlements to show effective permissions and identify overly permissive access."
  - Scan types: **Access scans** ("Enumerate files, folders, and permissions... to identify who has access to what"), **Sensitive data scans**, **Identity sync scans**, local users/groups scans; scheduled (cron) or on demand; **scan executions** tracked with status/history.
  - Source groups / connectors / edge scanners; service accounts per source.
  - Roles: Administrator / User Admin / Viewer.
  - Dashboards ("sensitive data exposure, access permissions, open access, and file activity") + pre-built reports per source: File Server — Access (8 reports), Content, Activity, Sensitive Data; SharePoint Online — **Shared Links, High-Risk ACLs, Open Access**, Content (**ROT Analysis**, **Stale Files**), Activity, Sensitive Data; AD summary. "My Reports" saved views.

### Key observations (Access Information Center v12.0 docs)

- A companion surface layered on Access Analyzer results for non-administrator participants:
  - **Resource Owners interface** — "managing ownership of resources and groups... Managing ownership is core component for both the Resource Reviews and the Self-Service Access Requests workflows." Owners are assigned by Security Team/Admin.
  - **Resource Reviews** — "enables business owners to conduct resource and group reviews **and recommend changes**."
  - **Self-Service Access Requests** — "enables domain users to request access to resources or to request membership in Active Directory groups... The approval process involves the business owners."
  - **Your Access Portal** — for domain users "to request access or view their own request history."
  - **Resource Audit** — "reports on resources, users, groups, computer, and sensitive content," available to assigned roles and owners of specific resources.
- Confirms the canonical role set: administrator/security team (configure, analyze), resource owner (review, approve), domain user (request, see own access).

## Cross-product Comparison

| Dimension | Varonis | SailPoint DAS | Netwrix AA + AIC |
|---|---|---|---|
| Governed stores | files, sites, mailboxes, S3 buckets, databases + SaaS/cloud | unstructured data: file servers, NAS, SharePoint, cloud, SaaS; Snowflake mentioned | SMB/CIFS file servers, SharePoint Online (+ identity stores) |
| Access map construction | "unravels nested groups, permissions, and inheritance"; permissions "normalized" across stores | account/entitlement aggregation + crawling + permissions analysis | access scans of permissions/ACLs + identity sync; effective permissions per user/group |
| Sensitive-data layer | discovery & classification as separate platform pillar feeding DAG | classification policies/rules/OCR; third-party tag import | sensitive data patterns + taxonomies → compliance frameworks; MIP labels |
| Risk findings | errant/excessive permissions, ghost users, sharing links, misconfigurations | over-privileged access, public sharing, defunct accounts with sensitive access | open access, overly permissive ACLs, broken inheritance, stale entitlements, shared links, ROT, stale files |
| Usage/activity | monitor and query all data activity (platform pillar) | monitor + alerts (downloads, off-hours, external sharing); "who accessed what, how often, why" | optional add-on product (Activity Monitor); anomaly detection |
| Ownership | — (owner role implied in reviews) | Business Resource Owners + ownership-election campaigns | Resource Owners assignment (prerequisite for reviews & requests) |
| Reviews / certifications | entitlement reviews facilitated | certification campaigns with decisions/templates, integrated with ISC | Resource Reviews: owners review and *recommend changes* |
| Access requests | self-service requests to apps/cloud resources/groups; auto-removal recommendations | via ISC (implied) | self-service requests with owner approval + user portal |
| Remediation posture | policy-automated, at scale; sandbox + rollback | policies + remediation workflows; right-size by roles/usage/policy | read-only analysis; changes flow through owner decisions/recommendations |
| Decision machinery | automation-heavy (remediation policies) | campaign-based certification | manual owner reviews + approvals |
| Deployment | cloud-native SaaS | SaaS (with on-prem FAM heritage) | on-prem containerized ("no data leaves your infrastructure") |
| Primary users | security teams, admins | security teams, data owners, compliance | administrators/security team + resource owners + domain users |

### Stable commonalities (Layer B — cross-product)

1. All three read **existing access-control structures of data stores**; none replaces the store's permission model as the primary control plane.
2. All three compute **effective access** by resolving group nesting/inheritance/sharing (Varonis and Netwrix say it explicitly; SailPoint's aggregation+crawling+permissions forensics serves the same result).
3. All three maintain the map **repeatedly** (continuous scans / crawling / monitoring) — the map drifts and must be re-derived.
4. All three **evaluate** the map: over-permission, open/public exposure, staleness, external sharing, defunct accounts.
5. All three route **decisions to accountable parties** — data/resource owners and security admins — via reviews/certifications and access requests; two of three show self-service access requests explicitly, all three show review/certification or owner workflows.
6. All three tie governance priority to **what the data is** (sensitivity/classification/labels) — classification present in all three, at different depths.
7. All three produce **auditable records** (audit trail, scheduled reports, campaign decisions).

### Divergences (inform Variants, not Core)

- Enforcement: policy-automated remediation (Varonis) vs campaign/policy-driven with workflows (SailPoint) vs read-only analysis with owner recommendations (Netwrix AA core).
- Activity monitoring: built-in pillar vs add-on product vs queryable forensics.
- Store mix: file-server/NAS heritage vs M365/collab vs multi-cloud/database breadth.
- Identity relationship: standalone data-security pole vs IGA-suite integration.
- Ownership: assigned vs elected (SailPoint election campaigns).

## Canonical Abstraction (L0–L3)

### L0 — Defining Invariant

A Data Access Governance application is recognizable when all three hold:

1. **Governed data estate** — the product connects to data repositories and reads their *native access-control state* (permissions/ACLs/sharing), without owning the storage itself. It is a lens over data it does not own.
2. **Effective-access map** — it resolves those raw structures (group membership, inheritance, sharing) into an identity-resolved map of *who can access what*, maintained by recurring re-derivation as the estate changes.
3. **Governed access-decision loop** — the map is turned into access decisions by accountable parties (owners/admins/policies): review & certify, approve/deny requests, and/or revoke/re-permission — with decisions recorded. The loop repeats because access drifts.

Remove #1 or #2 and the product cannot speak about data access at all. Remove #3 and it degrades into a permission-audit/reporting utility — not governance. Historical check: pre-digital and early-era practice (NTFS ACL reports + folder-owner sign-off sheets + ticketed permission fixes; platform-native AD/file-server administration) satisfies all three without classification engines, activity monitoring, cloud, or automation — passes.

### L1 — Common Mature Structure

Very common in mature modern products; not definitional:

- sensitive-data discovery/classification and labels to prioritize access decisions
- access-risk findings: open access, overly permissive ACLs, broken inheritance, stale entitlements, external sharing links, ghost/defunct accounts
- activity/usage monitoring — comparing actual use against granted access; anomaly alerts
- data/resource ownership assignment (and, in one product, election campaigns)
- access reviews / certification campaigns with per-item decisions
- self-service access requests with owner approval and request history
- dashboards and per-audience reports; bi-directional access views (per-user ↔ per-resource)
- remediation machinery at varying depth: recommendations, bulk revoke, policy-automated fixes, change preview/rollback
- audit trail and compliance-framework mapping

### L2 — Variant / Optional Structure

- store mix: file-server/NAS-centric vs M365/collaboration-centric vs multi-cloud/object-storage vs database
- deployment: on-premises vs SaaS vs hybrid
- enforcement posture: observational/read-only vs policy-automated enforcement
- IGA-relationship: standalone vs suite-integrated (certifications/identity context shared)
- activity monitoring: built-in vs separate add-on product
- identity scope: human identities vs also machine/non-human identities
- compliance mapping breadth; regional/regulatory packaging

### L3 — Vendor-specific (research notes only)

- Varonis: "blast radius" metric and reduction claims; "17M files per employee" stat; entitlement-change sandbox with logic checks and rollback; CRUDS illustration; MDDR/concierge services; 99% classification accuracy claim.
- SailPoint: Data Ownership Election voting campaigns; Virtual Appliance aggregation; four-surface Forensics (Activity/Permissions/Identity/Data Classification); FAM→DAS naming; ISC suite integration mechanics.
- Netwrix: source groups/connectors/edge scanners vocabulary; Metabase embedding + ClickHouse/PostgreSQL/Redis architecture; "Access Analyzer = on-prem DSPM" self-label; version split 2601 Linux-containerized vs 12.x Windows.

## Vendor-specific / Rejected Findings

- "Blast radius reduced by 90% in 180 days" (Varonis) — marketing metric; rejected from canonical document.
- "17 million files per employee" (Varonis) — vendor stat; rejected.
- "99% classification accuracy" (Varonis) — vendor claim; rejected.
- "DAG = DSPM" (Netwrix self-label of Access Analyzer) — treated as market label-drift and recorded as a boundary issue; not accepted as structural identity.
- Ownership-election voting (SailPoint) — single-product structure; kept product-specific.
- Sandbox/rollback for entitlement changes (Varonis) — single-product direct evidence; kept as an example of remediation depth, not core.
- Activity-monitoring-as-separate-product (Netwrix) — packaging variation; documented as variant.

## Boundary Findings

- **vs Identity Governance / IGA**: IGA's governed object is the *identity* (lifecycle, roles, entitlements to applications); DAG's governed object is the *data store's access state*. Overlap zone: certifications, access requests, least privilege — SailPoint explicitly frames DAS as "extending identity security to data," which proves these are adjacent-but-distinct poles of one market conversation. Test: strip the data-store permission structures → what remains is IGA; strip identity lifecycle/HR-driven provisioning → what remains is DAG.
- **vs DSPM**: DSPM discovers/classifies data and flags posture misconfiguration (cloud-centric); DAG governs *access* (permission layer + decision loop). Convergence is real (Netwrix self-labels its DAG product as DSPM; Varonis sells DSPM as a separate pillar of the same platform). Test: remove reviews/requests/remediation on access → DSPM posture tool; remove discovery/classification breadth → still DAG (classification is L1, not L0).
- **vs DLP**: DLP acts on data *movement/egress* (block, quarantine); DAG acts on *standing access* (map, review, right-size). Varonis ships both as separate named pillars — vendor-confirmed distinctness.
- **vs Data Governance Platform / Data Catalog**: those govern data-as-asset (metadata, quality, findability, stewardship); DAG governs access-to-data. Name collision on "data governance" umbrella; distinct objects and users (stewards vs security/owners).
- **vs PAM**: PAM manages privileged accounts/credentials/sessions; DAG governs everyday end-user access to data through the store's own permission model.
- **vs Insider Risk Management / UEBA / SIEM**: those detect and investigate behavior; DAG's loop is governance (decisions on access). DAG products may raise alerts (observed in SailPoint/Varonis) but detection is not the defining loop.
- **"去掉什么就变成另一个 Type" 判据**: remove the effective-access map (L0 #2) → becomes generic compliance/policy documentation; remove the decision loop (L0 #3) → permission auditing/reporting utility; replace governed object (data stores) with applications+roles → IGA; replace with data-in-motion → DLP; replace decision loop with cataloging/quality → Data Governance Platform.

## Uncertainties

- Exact breadth of SailPoint DAS governed stores beyond unstructured data (Snowflake blog mentioned; not confirmed in fetched docs).
- Whether Netwrix offers direct remediation execution elsewhere in the product family (docs fetched state scans are read-only; not researched further).
- Varonis operational details (owner portals, review workflows) — behind login; inferred only in general terms from product pages; kept low-strength or omitted.
- Market shares / analyst framing not verified (no analyst report fetched); avoided entirely.
- Microsoft-native DAG feature (SharePoint admin sharing reports) — page 404; existence and shape unverified; excluded.

## Final Synthesis

Data Access Governance is the application Type whose defining core is: **a maintained, identity-resolved map of who can access which governed data (read from the stores' own permission structures), plus a recurring governance loop that turns that map into recorded access decisions — reviews/certifications, access-request approvals, and/or remediation — held to the least-privilege direction.** Sensitivity classification, risk findings, activity monitoring, ownership machinery, self-service requests, and automated enforcement are the standard capability stack that mature products add; store mix, deployment, enforcement posture, and IGA-relationship are variants. The nearest Type boundaries: IGA (identity-centric lifecycle vs data-centric access state), DSPM (posture/discovery vs access decision loop), DLP (egress vs standing access), Data Governance Platform (asset governance vs access governance).
