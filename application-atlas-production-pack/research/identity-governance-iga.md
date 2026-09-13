# Research Notes — Identity Governance / IGA

## Research Goal

Understand what an Identity Governance / IGA application actually is and how it works, from real products: what objects it governs, what structures it maintains, who uses it, what workflows it runs, where its loop begins and ends, and where it sits relative to neighboring Types (IAM, SSO/MFA, PAM, CIAM, Data Access Governance, GRC/Compliance Management, ITSM).

## Initial Boundary (hypothesis before research)

- Working hypothesis: IGA is the *governance* plane over identity-based access — deciding, reviewing, and proving who should have what access — while IAM is the *operating* plane (authentication, runtime grant enforcement). IGA does not authenticate anyone.
- Likely confusions: IAM (closest sibling), PAM (privileged accounts), CIAM (different population), Data Access Governance (name collision on "governance"), GRC/Compliance Management (name collision on "governance"), approval-workflow platforms (mechanics overlap).
- Unknowns going in: Is lifecycle automation definitional or common? Is certification/attestation definitional or a compliance-era layer? Is native provisioning definitional or can the loop close by delegated remediation? Is reconciliation (desired vs actual state) a cross-product concept or one vendor's framing?

## Research Questions

1. What are the core objects? (identity, account, entitlement, role, application/source, request, campaign/review, policy, violation)
2. How does the product learn "who has what access"? (connectors, aggregation, correlation)
3. How does the identity lifecycle work? (joiner/mover/leaver, HR as authoritative source, birthright access)
4. How do access requests and approvals work? (catalog, multi-stage approvals, adaptive approval)
5. What is certification/attestation? (campaigns, reviewer populations, decisions, sign-off, outcomes)
6. How do policies work? (separation of duties, least privilege, policy violations)
7. Does the loop close? (provisioning back to targets, delegated remediation, reconciliation of actual vs desired state)
8. How does compliance reporting work? (audit trail, evidence, reports)
9. Who uses it, and what does each user see?
10. Boundary behavior vs IAM, PAM, CIAM, DAG, GRC, ITSM.

## Representative Products

| Product | Pole | Evidence tier reached |
|---|---|---|
| SailPoint Identity Security Cloud (SaaS, formerly IdentityNow) | pure-play IGA market leader, SaaS | Tier 1 — admin help center (full TOC + feature pages) |
| SailPoint IdentityIQ (on-prem) | pure-play IGA, on-prem enterprise heritage | Tier 1 — product documentation (overview + module pages) |
| Microsoft Entra ID Governance | suite-embedded governance product on top of an IAM directory | Tier 1 — Microsoft Learn overview docs |
| Omada Identity Cloud / Omada Identity | European enterprise IGA, best-practice process framework (IdentityPROCESS+) | Tier 2 — product + functionality pages (operationally detailed) |
| Saviynt | cloud-native IGA (market anchor only) | Unreachable — docs JS-blocked, product URL 404; no claims drawn |
| One Identity (Identity Manager) | legacy enterprise IGA (market anchor only) | Unreachable — two empty responses; no claims drawn |

Selection rationale: market representativeness (pure-play leader + suite-embedded pole + process-framework European vendor), different product philosophies (governance-as-suite vs governance-as-standalone vs governance-as-process), different customer tiers (enterprise pure-play, Microsoft-tenant customers, regulated European enterprise/government), and documentation depth where reachable.

## Sources

- SailPoint Product Documentation portal — https://documentation.sailpoint.com/ (researched 2026-09-08)
- SailPoint Identity Security Cloud admin help — https://documentation.sailpoint.com/saas/help/index.html
- SailPoint IdentityIQ 8.5 overview — https://documentation.sailpoint.com/identityiq/help/
- Microsoft Entra ID Governance overview — https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview
- Omada Identity Cloud — https://omadaidentity.com/products/omada-identity-cloud/
- Omada Identity Governance functionality — https://omadaidentity.com/products/functionality/identity-governance/
- Saviynt — https://docs.saviyntcloud.com/ (JS-blocked), https://saviynt.com/identity-governance/ (404) — abandoned after 2 attempts
- One Identity — https://www.oneidentity.com/products/identity-manager/ and /identity-manager/ (empty responses) — abandoned after 2 attempts

## Product A — SailPoint Identity Security Cloud (SaaS) [Evidence A — directly observed]

Positioning (own words): "Identity governance is about enforcing and maintaining least privilege access, where every identity has the access needed, when it's needed."

Observed admin structure (help-center TOC + landing pages):

- **Loading identity and access data**: configuring Sources (connectors); loading account data; identity profiles; account schemas; correlation ("Assigning Source Accounts" — matching source accounts to identities); manager correlation; identity processing. Entitlement loading: entitlement types, aggregating entitlements, privilege classification.
- **Managing Access**: entitlements; access profiles (bundles of entitlements); roles; metadata; access applications; just-in-time access provisioning; governance on SSO providers.
- **Managing Users**: identities (identity list, control panels); Access History (per-identity record of access and attribute changes); governance groups; work reassignment; user levels/permissions; data segmentation; non-employee identities.
- **Managing Sources**: native change detection (detecting changes made directly in target systems); multi-host aggregation groups.
- **Access Requests**: requesting roles/access profiles/entitlements; requests for others; requests for machine identities; approval re-authentication; global approval settings; request segments; approvals administration; adaptive approvals.
- **Certifications**: understanding certifications; campaigns started from search; campaign filters; manager campaigns and source-owner campaigns; reassignment; campaign status reports; completing campaigns.
- **Provisioning**: source account provisioning; lifecycle states; automating role assignment; attribute synchronization; provisioning tracking.
- **Separation of Duties**: managing policies; handling policy violations; violation reports.
- **Workflows**: triggers, actions, templates (generic automation over identity events).
- **AI layer (era-current)**: Activity Insights (usage data for access); Access Insights (identity outliers, access intelligence); Access Modeling (role discovery, role insights, common access); Access Recommendations (approve/revoke suggestions); AI application onboarding.
- **Extensions in the same family (separate products/modules)**: Machine Identity Security (machine accounts, requests, application identities); Agent Identity Security (AI agents); SailPoint CIEM (cloud entitlements per cloud platform); Non-Employee Risk Management; Data Access Security (separate product — data/unstructured); Access Risk Management (SoD risk + GRC integration); password management; identity graph.

Reading of the loop: sources are connected → accounts and entitlements are aggregated → accounts are correlated to identities (the unified identity is the pivot) → access is organized into entitlements / access profiles / roles → humans request and approve access → lifecycle events and role assignment automate changes → provisioning writes changes back to targets → certifications periodically re-decide existing access → SoD policies flag toxic combinations → everything lands in access history, search, and audit reports.

## Product B — SailPoint IdentityIQ (on-prem) [Evidence A — directly observed]

Own positioning: "an identity and access management software platform custom-built for complex enterprises. It delivers full lifecycle and compliance management for provisioning, access requests, access certifications, and separation of duties."

Observed structure:

- **Identity Warehouse**: the central aggregated identity record; identity correlation; identity detail page; rights and capabilities.
- **Application Configuration / Application Management**: applications as connected targets; correlation; **Entitlement Catalog** (discovered entitlements organized for review/request); native change detection; application risk.
- **Compliance Manager module**: Access Certification ("frequently reviewing and rechecking user access"); automated policy management; audit reporting and analytics. Certification types include manager, application owner, advanced, targeted, role membership, entitlement owner, role composition, account-group reviews; access review decisions/operations; electronic signatures; certification events; scheduling.
- **Lifecycle Manager module**: access requests (self-service request + approval work items); automated provisioning triggered by joiner/mover/leaver; lifecycle events; batch requests. **Rapid Setup**: explicit Joiner / Mover / Leaver configuration.
- **Roles**: role management concepts; role modeling/mining; role versioning; certifying roles; start/end dates for temporary access; workgroups; populations.
- **Policies**: policy types; policy violations; violations in certifications; compensating controls.
- **Access History**: "confirm that attributes, entitlements, and access were provisioned, changed, or removed as expected, discover which identities have entitlements to a given application and how they were acquired."
- **Provisioning**: provisioning plans/requests; identity cube refresh; attribute synchronization.
- **Reports**: policy violation, risk, role management, identity and user reports; risk scores for identities and applications.
- **Extensions**: Privileged Account Management module (containers, approvals, credential cycling); Password Manager; SaaS Management; File Access Manager/classifications (data side — separate product).

Reading: IdentityIQ makes the two-module decomposition explicit — Compliance Manager (certifications + policies + audit) and Lifecycle Manager (requests + provisioning + JML) — over a shared Identity Warehouse + Application/Entitlement Catalog + Role model.

## Product C — Microsoft Entra ID Governance [Evidence A — directly observed]

Own framing — identity governance addresses four questions:

- Which identities should have access to which resources?
- What are those identities doing with that access?
- Are there organizational controls in place for managing access?
- Can auditors verify that the controls are working effectively?

Observed structure — three governance pillars:

- **Identity lifecycle**: inbound provisioning from HR sources (Workday, SuccessFactors named) to maintain user identities; lifecycle workflows running tasks at key events (before start date, on status change, on departure); automatic assignment policies (attribute-driven group/app-role/SharePoint-role assignment); provisioning user accounts into apps via connectors (SCIM, LDAP, SQL, SAP named). Guest/B2B variant: business groups decide which external identities get access; entitlement management creates/removes guest accounts with access expiration; recurring access reviews of guests with removal of denied identities.
- **Access lifecycle**: entitlement management (access packages = bundles of group memberships, app roles, SharePoint roles); request + multi-stage approval flows (manager, department lead/resource owner, security risk officer named as example approvers); separation-of-duties checks on requests; recurring access reviews (re-certification) with AI-identified peer outliers; access packages expiring/reviewed.
- **Privileged access lifecycle**: Privileged Identity Management (PIM) — just-in-time activation of admin roles, role-change alerting, access reviews of privileged roles.
- **Enforcement note**: sign-in enforcement (Conditional Access) remains a Microsoft Entra ID capability, not a governance-product capability — the governance product operates above the runtime plane. Directly visible in the doc structure.
- **Audit framing**: "Can auditors verify that the controls are working effectively?" is one of the four founding questions; governance dashboard; automation table mapping scenarios to controls.
- **Era-current extension**: agent identities (AI agents) governed through the same entitlement management/access packages, human sponsor accountability, sponsor transfer, blueprints. (Product-family L3 detail: shipped under Agent ID.)

Reading: Microsoft ships governance as a distinct SKU/product on top of the directory — market confirmation that governance is a separate purchasable structure (matches the IAM pass's observation).

## Product D — Omada Identity Cloud / Omada Identity [Evidence A for capability inventory; page tier = 2]

Own positioning: "full-featured IGA solution covering identity lifecycle management, access governance, intelligent provisioning, and risk analytics."

Observed structure:

- **Identity Governance process area** (IdentityPROCESS+ framework — a published best-practice process framework with named process groups):
  - Generate report — "who has or has had access to what, why, and when that access was granted, who approved it, and when it was revoked"; real-time compliance dashboards.
  - Perform attestation — design certification campaigns; administrate campaigns (start, monitor, reassign, report, close); respond to campaign questions; transfer ownership; account ownership; access review for managers/resource owners. Campaign scope configured by what data, who certifies, how often, consequences of responses/non-responses, notifications/reminders.
  - **Perform reconciliation** — "check if the desired security and compliance state matches the actual access granted"; compares defined desired state with actual state gathered from target systems; per-assignment states include 'under control', explicitly/implicitly approved, not approved, **orphan assignment**, **pending deprovisioning**, **in violation**, implicitly assigned.
  - Apply data classification — classification tags on identities/systems/resources (e.g., GDPR categories).
  - Separation of duties — evaluate violation ("toxic combinations of access rights are not assigned to an individual").
  - Orphan account handling — accounts without owners reassigned or deleted.
- **Other platform capability areas**: Identity Lifecycle Management; Access Management; Identity Administration; Business Alignment; Auditing (compliance status dashboards, cross-system certification campaigns, audit report templates); Identity Security Breach Management; AI capabilities; Connectivity Framework (connector library); adaptive data model (add attributes/entity types without code).
- **Deployment variants**: SaaS (Omada Identity Cloud), dedicated/private tenant (Omada Identity Cloud Private — "for regulated enterprises and government organizations"), on-premises/hybrid (Omada Identity).
- **Era-current extension**: Omada Agent Governance (govern AI agents: ownership, access, usage evidence).

Reading: Omada contributes the most explicit statement of the *reconciliation* concept — desired state vs actual state as the maintained invariant — plus process stakeholders: line managers, system/resource owners, compliance team, external auditors.

## Cross-product Comparison

| Structure | SailPoint ISC | SailPoint IdentityIQ | Entra ID Governance | Omada | Layer verdict |
|---|---|---|---|---|---|
| Connector-based aggregation of accounts+entitlements from target systems | yes (sources, aggregation) | yes (applications, entitlement catalog) | yes (HR + app connectors) | yes (connectivity framework) | defining |
| Unified identity as pivot (accounts correlated to one identity) | yes (correlation, identity profiles) | yes (identity warehouse/cube) | yes (directory identity + HR-driven) | yes (adaptive identity data model) | defining |
| Access object hierarchy (entitlement → bundle → role) | entitlements / access profiles / roles | entitlements / profiles / roles | access packages (groups+app roles) / roles | entitlements / roles | defining (bundle layer name varies) |
| Access request + structured approvals | yes (+requests for others/machines, adaptive approvals) | yes (Lifecycle Manager work items) | yes (entitlement management packages, multi-stage approval) | yes (self-service access requests) | defining |
| Human decision over *existing* access (certification / attestation / access review) | yes (campaigns: manager, source owner) | yes (Compliance Manager; many review types) | yes (recurring access reviews, guest reviews) | yes (attestation campaigns) | defining |
| Policy layer (SoD, least privilege) | yes (SoD policies module) | yes (policy engine, violations) | yes (SoD checks on requests) | yes (SoD violation evaluation) | defining |
| Lifecycle automation (joiner/mover/leaver driven) | yes (lifecycle states, role assignment automation) | yes (Rapid Setup JML, lifecycle events) | yes (lifecycle workflows, HR provisioning) | yes (lifecycle management area) | common-mature (not definitional — see below) |
| Provisioning writes decisions back to targets | yes | yes | yes | yes ("intelligent provisioning") | common-mature (execution leg) |
| Reconciliation of actual vs desired/authorized state | yes (native change detection + provisioning tracking) | yes (identity refresh, effective access indexing) | implicit (provisioning + review removals) | **explicit** (dedicated process group with named states) | defining (concept), implementation visibility varies |
| Decision/audit trail (who approved what when) | yes (access history, audit events, search) | yes (audit configuration, access history, reports) | yes (auditor-verification framing) | yes (audit trail reporting) | defining |
| Role mining / AI role discovery | yes (Access Modeling) | yes (role mining) | not asserted in researched pages | not asserted (AI capabilities area) | common, era-current |
| Review recommendations / outlier detection | yes (Access Recommendations, Identity Outliers) | yes (AI-driven) | yes (AI-identified outliers in reviews) | AI capabilities area | common, era-current |
| Machine/non-human identity governance | yes (Machine Identity Security, Agent Identity Security) | via Agentic Fabric integration | yes (agent identities in entitlement management) | yes (Agent Governance) | common, era-current |
| Privileged slice (JIT activation) | JIT access config; PAM via module | PAM module (containers, credential cycling) | PIM inside the governance product | not asserted | common; privileged *session/credential* brokering stays PAM |
| Password management | yes (module) | yes (module) | directory capability (not governance) | not asserted | common; IAM-flavored capability |
| Data-store/unstructured-data governance | separate product (Data Access Security) | separate product (File Access Manager) | not in governance scope | data classification tags only (not full DAG) | adjacent Type (→ DAG) |
| On-prem / SaaS / private-tenant deployment | SaaS | on-prem | cloud (within Entra tenant) | SaaS / private tenant / on-prem | variant |
| Published process framework / implementation methodology | partner-driven implementation | professional services | deployment guides | **IdentityPROCESS+** (published) | vendor-specific |

Layer verdicts for the two candidate-definitional items I went in uncertain about:

- **Lifecycle automation**: common-mature, not definitional. A product with unified access visibility + request/approval + certification + SoD but without HR-driven JML automation is still recognizable IGA; a product with only JML provisioning and none of the decision structures is identity provisioning (an IAM capability), not IGA. Entra's own pillar naming ("govern the identity lifecycle") shows how strongly associated it is, which is why it sits at the top of the common tier.
- **Certification/attestation**: present in all four researched products and pre-dating the modern SaaS era (IdentityIQ's Compliance Manager heritage; the compliance-era origin of access certification). I initially treated it as definitional; on the historical check (below) a pre-certification provisioning product (legacy identity management with reconciliation + approvals) still satisfies the rest of the core, so certification sits at the top of the common tier rather than in the invariant — but it is the signature capability of the Type and nearly universal in mature products.

## L0 — Defining Invariant

Three jointly-held structures. If any one is removed, the product stops being recognizable as IGA:

```text
L0.1  Access model of record
      a maintained, identity-resolved state of "who has what access",
      aggregated from connected target systems (accounts, entitlements)
      and correlated into unified identities
      remove → per-system admin consoles / directory; nothing unified to govern

L0.2  Structured human decision processes over access
      access decisions routed to accountable decision-makers
      (requests with approvals; certifications/attestations of existing access;
       policy-violation handling), each decision recorded
      remove → a permission reporting/audit tool, not a governance system

L0.3  Desired-state direction with reconciliation
      recorded decisions drive the actual access state toward the defined
      desired state (provision/revoke/remediate — native execution or delegated),
      and actual state is kept reconciled against the model of record
      remove → decision records that never change anything = audit snapshot;
               state changes with no decision loop = provisioning automation
```

Jointly-held is load-bearing:

- 1 alone = access reporting / permission audit tool (identity-app-level DAG territory)
- 2 alone = generic approval workflow / ITSM
- 3 without 1+2 = provisioning automation (IAM capability)
- 1+3 without 2 = automated provisioning with no human governance
- 2+3 without 1 = workflow engine moving tickets with no access semantics
- 1+2 without 3 = review-and-report tool (detect-only pole exists at the market edge; the loop must at minimum record outcomes against the model and hand off remediation)

## L1 — Common Mature Structure

Present in the large majority of mature products; expected by the market; not required to recognize the Type:

- identity lifecycle automation (joiner/mover/leaver events, HR as authoritative source, birthright access, automated role/attribute assignment)
- provisioning integration (writing grants/revocations back to target systems; provisioning tracking)
- role model (bundles of access assigned by attribute or request) and role lifecycle (request-driven creation, certification of roles)
- certification/attestation machinery at full depth (campaign design, scoping, reviewer reassignment, reminders/escalation, campaign reports, sign-off)
- SoD policy engine with violation reports and pre-grant checks
- access history / decision trail (who approved what when; how an identity got an entitlement)
- self-service access request catalog; requests for others (delegate/manager-initiated)
- orphan account detection and ownership assignment/transfer
- dashboards, compliance status reporting, audit report templates
- entitlement catalog (discovered entitlements described for humans — descriptions, ownership, risk)
- native change detection (changes made directly in target systems reconciled back into the model)
- search over identities/entitlements/access
- delegated administration (governance groups, data segmentation, user levels)
- temporary/time-bound access (start/end dates, expiring packages, JTA)
- guest/non-employee lifecycle governance
- AI assistance (era-current): review recommendations, outlier detection, role discovery/mining, usage-based insights, GenAI entitlement descriptions

## L2 — Variant / Optional Structure

- Deployment: multi-tenant SaaS; on-premises; dedicated/private tenant for regulated industries; hybrid
- Packaging: standalone pure-play platform; suite-embedded governance product on an IAM directory; platform family with separately licensed capability products (privileged, data, cloud entitlements, machine identities)
- Governance framework formality: published process framework + methodology vs free-form configuration
- Identity population scope: workforce only; + guests/partners/non-employees; + machines/service accounts; + AI agents (era-current)
- Data-side adjacency: classification tags on resources (light) vs full unstructured-data governance (→ separate Data Access Governance product)
- Privileged depth: JIT role activation inside governance vs full PAM (vaulting, session brokering) as separate product
- Regional/compliance emphasis: SOX/audit-driven vs GDPR/regulatory-driven (same structure)
- Implementation depth: connector breadth, custom connector SDKs, cloud gateways for on-prem targets
- Ecosystem: GRC-tool integration for SoD risk (extension module in one sampled family); ITSM integration for delegated remediation

## L3 — Vendor-specific Structure (research notes only)

- **SailPoint**: Identity Cube / Identity Warehouse terminology; access profiles as the bundle layer; governance groups; work reassignment; data segmentation; user-level permission matrix; Configuration Hub (backups, tenant connections); virtual appliances as connector infrastructure; manager correlation; Adaptive Approvals; Access Risk Management module (GRC/SoD risk, formerly SecurityIQ lineage); Non-Employee Risk Management; Harbor Pilot / Agentic Fabric (era-current agent fabric); certification campaign types (source owner, from search, with filters).
- **Microsoft Entra ID Governance**: entitlement management / access packages terminology; lifecycle workflows with task templates (e.g., temporary access pass email to manager — named example); B2B guest removal machinery; PIM bundled inside the governance SKU; Conditional Access stays in Entra ID (not governance); Microsoft Entra Suite licensing; Agent ID blueprints/sponsor transfer (era-current); governance dashboard URL in Entra admin center.
- **Omada**: IdentityPROCESS+ (published best-practice framework with named process groups: Generate report / Perform attestation / Perform reconciliation / Apply data classification / SoD); reconciliation states vocabulary ('under control', explicitly/implicitly approved, orphan assignment, pending deprovisioning, in violation, implicitly assigned); adaptive data model (add entity types/attributes in UI); Cloud Management Portal (customer-controlled upgrade windows); 12-week deployment program; "Javi" AI assistant branding.
- Numeric limits, campaign cadence defaults, licensing gates: not asserted anywhere (not researched to that precision).

## Rejected Findings

- "IGA = IAM + access reviews" (the framing the IAM pass pre-hung). Rejected as a *definition* — although governance consumes identity data from IAM substrates, the market ships governance as a distinct product, and the governance loop (decision processes + desired-state reconciliation + audit evidence) is its own structure an IAM can lack entirely. Refined framing: two planes over the same subject — IAM operates access, IGA governs it. Keep-both ratified.
- "Certification is the defining invariant" (initial hypothesis). Rejected on the historical check: pre-certification legacy provisioning products with reconciliation + approvals satisfy the rest of the core; certification is the signature common capability (top of L1), not the invariant.
- "HR-driven lifecycle automation is definitional" (Entra's pillar naming tempts this). Rejected: a governance product over a static population with requests/certifications/SoD is still IGA; conversely pure JML provisioning without decision structures is IAM provisioning.
- "IGA must natively provision" (common but not invariant). Rejected in its strong form: the loop must *close* (decisions drive state change), but execution can be delegated (e.g., ITSM handoff); all four researched products provision natively, which makes native provisioning the common implementation.
- "IGA includes data/file access governance" (name adjacency + SailPoint FAM/DAS bundling). Rejected: that is a separate product in the same vendor families and a separate Type (DAG) in this atlas.
- Marketing framings ("AI-driven insights", "12 weeks to value", "75% risk reduction"): recorded as vendor claims only, not structure.

## Boundary Findings

### vs Identity & Access Management / IAM (closest sibling — DISCHARGES the IAM pass's pre-hung flag)

- The IAM pass recorded: governance is "a layer on top of the IAM core" whose objects are IAM objects; boundary test "an IAM without reviews is still IAM; a governance product without an identity store/authN has nothing to govern."
- Confirmed from the IGA side, with one refinement: the dependency direction is real but looser than "IAM objects" — IGA aggregates from *any connected target systems holding accounts/entitlements* (directories, apps, cloud platforms) and authoritative sources (HR); an IAM directory is the most common substrate but not logically required. The IAM pass's test holds both ways: strip reviews/policy/reconciliation from IGA and something IAM-like remains (that's how the market used to sell it); strip governance from IAM and it is still fully IAM (confirmed: Entra ID's Conditional Access/authN is *outside* its Governance product; IdentityIQ's password/SSO capabilities are module-level).
- Distinctness evidence: separate SKUs in the same vendor (Entra ID vs Entra ID Governance); separate product families (SailPoint's whole catalog); the four Entra governance questions are governance questions (should / doing / controls / verifiable), not operating questions.
- **Plane test (the keep-both判据)**: IAM = operating plane — verify the identity (authentication) and enforce grants at runtime; IGA = governance plane — decide what grants should exist over time (requests, reviews, policies), drive access state toward the desired state, and prove it to auditors. Remove runtime enforcement/authN → IGA survives (governs federated identity data); remove the decision/reconciliation loop → IAM survives. Neither collapses into the other; the seam is the decision loop, not the objects.

### vs Data Access Governance / DAG (DISCHARGES the DAG pass's pre-hung claim from the IGA side)

- Confirms the DAG pass's claim: IGA's governed object is the identity→application/entitlement relationship across connected systems; DAG's governed object is the data store's access state (file shares, unstructured data permissions).
- Market confirmation: SailPoint ships Identity Security Cloud and Data Access Security as separate products; IdentityIQ's File Access Manager is a separate product; Omada only touches the data side with classification tags.
- Test from this side: replace governed object (app entitlements) with data-store permissions → DAG; strip data-store permission structures from the IGA sample → pure IGA remains.

### vs Privileged Access Management / PAM

- PAM's objects: privileged accounts, credential vaulting, session brokering/monitoring. IGA's object: access grants of all sensitivity, governed through the decision loop.
- Overlap: privileged *entitlements* are governed in IGA (IdentityIQ PAM module governs privileged accounts through IGA processes: containers, approvals, certification; Entra PIM does JIT activation + reviews of admin roles). JIT *activation* (time-bound elevation via approval) is governance-shaped and appears inside IGA; credential vaulting and session brokering are operational PAM. The privileged **session/credential** machinery keeps PAM a distinct Type; the privileged **grant** belongs to IGA.

### vs Customer Identity / CIAM

- Population + administration model: IGA's population is org-administered (employees, workers, guests the org sponsors); CIAM's population is self-enrolled customers. Confirmed consistent with the CIAM/IAM passes' population test.

### vs GRC / Compliance Management / Internal Audit

- IGA *produces* compliance evidence (attestation sign-offs, decision trails, SoD reports) but does not manage the compliance program (controls, obligations, audits across domains). GRC platforms consume IGA evidence; SailPoint's Access Risk Management (GRC integration) is an extension module, and GRC-family products treat identity as one control domain. Test: strip the access model of record and access decision loop → GRC/audit tool; add controls-across-domains → GRC.

### vs ITSM / Approval Workflow Platform

- Approval mechanics overlap, but IGA approvals are bound to the access model of record (entitlement semantics, ownership, SoD consequences, provisioning execution). Generic workflow platforms move tasks without access semantics. One Identity-style legacy IGA even *delegates* remediation to ITSM, which proves the boundary (delegated execution ≠ different Type).

### vs HRIS

- HR is the authoritative *source* of worker truth feeding identity lifecycle; IGA governs access, not employment records. Direction of data flow is the seam: HR→IGA identity facts; IGA→HR nothing (in the researched products).

### 去掉什么就变成另一个 Type (removal tests)

- Remove aggregation/correlation (L0.1) → per-system consoles or a plain directory → IAM substrate territory
- Remove decision processes (L0.2) → permission auditing/reporting (identity-app-level DAG / audit utility)
- Remove desired-state reconciliation (L0.3) → review-and-report snapshot tool
- Replace governed object with data-store permissions → DAG
- Add runtime authentication/enforcement as the center → IAM
- Restrict population to self-enrolled customers → CIAM
- Restrict object to privileged accounts/sessions → PAM
- Generalize decisions to arbitrary business tasks → approval workflow / ITSM

## Historical / Market-Sample Check

- Older and on-prem products: IdentityIQ (on-prem, current) satisfies the core directly. Legacy enterprise IGA of the 2000s–2010s (Oracle/IBM/SAP lineage — market anchors, not fetched) was built on the same invariant: HR/dir-driven provisioning + reconciliation of resource state + request approvals (+ later certification campaigns under audit regimes). A pre-certification provisioning product (reconciliation + approvals, no campaigns) still satisfies L0.1–L0.3. Historical check **passes**: the core is era-stable; certification campaigns, role mining, and AI assistance are era layers.
- Regional check: European compliance-driven IGA (Omada, GDPR emphasis, private-tenant pole) and US audit-driven IGA (SailPoint) share the structure; regional emphasis changes vocabulary and framework formality, not the loop.
- Platform-native check: governance built inside a cloud suite (Entra ID Governance) satisfies the core while packaging differs (no independent directory — borrows the suite's). Confirms packaging is L2.
- Era-current check: machine identity and AI-agent governance (all three families) extends the *population*, not the loop — L2/L1 presence, watch for future divergence.

## Uncertainties

- **Certification-only market pole**: whether standalone certification/attestation-only products (no provisioning integration, decisions exported for manual action) exist as a meaningful standalone market today, or only as entry editions of full IGA. If they exist standalone, L0.3's "delegated remediation" phrasing is what keeps them inside the Type; if not, native provisioning could be promoted. Not resolved this pass (no such product fetched).
- **Reconciliation visibility**: only Omada makes desired-vs-actual reconciliation an explicit named process group with published states; SailPoint reaches it via native change detection + provisioning tracking; Entra implicitly. I treat the concept as defining (it is the mechanism by which L0.1 stays true) but the *named* feature is not universal — noted as evidence-strength asymmetry.
- **Saviynt / One Identity structure**: unreachable; assumed market-standard structure for anchoring only, zero claims drawn from them.
- **Mid-market/SMB IGA shape**: sample is enterprise-weighted; a genuinely mid-market product (if structurally thinner) unverified.
- **Numeric operational parameters** (campaign cadence defaults, connector counts, limits): not asserted; not researched to that precision.

## Final Synthesis

Identity Governance / IGA is the organization-side application Type whose defining core is a **closed governance loop over identity-based access**:

1. an **access model of record** — a maintained, identity-resolved state of who has what access, aggregated from connected target systems and correlated into unified identities;
2. **structured human decision processes** over that access — self-service requests with approval chains, periodic certifications/attestations of existing access, and policy-violation handling (separation of duties), each decision recorded against accountable decision-makers;
3. **desired-state direction** — recorded decisions drive the actual access state toward the defined desired state (provisioning, revocation, remediation — native or delegated) while actual state is continuously reconciled back into the model.

Everything else is layered on this loop: lifecycle automation and provisioning integration (common-mature), the role model and entitlement catalog (common), certification machinery at full depth (common, signature), SoD policy engines (common), audit reporting and decision trails (defining-adjacent, universal in sample), AI assistance (era-current common). Deployment, packaging, population scope, and framework formality are variants. The plane distinction settles the IAM boundary: IAM operates access (verify + enforce), IGA governs it (decide + reconcile + prove); the market consistently ships them as separate products, and this Type stands alone.
