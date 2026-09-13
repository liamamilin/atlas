# Research Notes — Controls Management Platform

Research date: 2026-09-07
Directory leaf: Controls Management Platform (§11 Legal, Risk, Compliance & Governance)
Slug: controls-management-platform

## Research Goal

Understand what a "Controls Management Platform" actually is as an Application Type: what the managed object is (the control), what the standing lifecycle of that object is (library → mapping → testing/monitoring → results → remediation → assurance state), who operates it, how the automation-first and finance-controls-first product families differ, and — per the joint-review flags carried from sibling passes — how it differs from Compliance Management Platform (requirements-centered), Internal Audit Management (program/engagement-centered), Audit & Assurance Platform (engagement spine), GRC Platform (shared-data-core umbrella), ERM (risk-centered), Compliance Policy Management (policy-document-centered), and Accreditation/Certification Management (credential-spine-centered).

## Initial Boundary

- Nearest neighbors: Compliance Management Platform (processed; flagged this leaf as "softest new seam"), Internal Audit Management (processed; vendor-stated product-type distinction), Audit & Assurance Platform (processed), GRC Platform (processed), Enterprise Risk Management (processed), Compliance Policy Management (processed), Regulatory Change Management (processed), Accreditation/Certification Management (processed; capability-relationship call), Security Compliance Platform (§15, unprocessed).
- Working hypothesis before research: the control is the primary managed object and the testing/validation loop over that control is the organizing workflow; requirements, risks, policies, and audits are mapping targets, not the center.
- The word "control" is overloaded: industrial process control, environmental instrument control, and financial "internal control" are different universes. This leaf sits in §11 (GRC cluster), so the scope is the internal-control universe (COSO/SOX heritage) generalized across compliance frameworks.

## Research Questions

1. What is a "control" as a record? What fields/structure does it carry?
2. What does the control lifecycle look like (creation → mapping → testing → results → remediation → status)?
3. What do controls map to (requirements, risks, policies, tests, evidence) and is mapping mandatory?
4. Manual periodic testing vs automated continuous monitoring — which is definitional, which is a mechanism variant?
5. Who are the users and roles (compliance managers, control owners, internal audit, auditors, executives)?
6. How does the finance-controls pole (SOX/ICFR) differ structurally from the security-compliance pole (SOC 2/ISO 27001)?
7. What is the assurance output (readiness/status/reporting, auditor collaboration)?
8. Boundary discriminators vs the sibling Types above.
9. Historical check: do pre-integration, pre-automation, spreadsheet-era, and non-US products still fit the definition?

## Representative Products

Selection rationale: market representativeness + documentation completeness + different product philosophies + different customer tiers.

| Product | Family / pole | Customer tier | Evidence tier reached |
|---|---|---|---|
| Drata | Compliance automation, control-monitoring-first (cloud-native security frameworks) | mid-market → enterprise | Tier 1 (Help Center articles) |
| Vanta | Compliance automation / trust management (automation-first, trust-center-led) | SMB → mid-market | Tier 1 (Help Center articles) |
| Optro (AuditBoard lineage; product support at support.soxhub.com) | Controls Management product inside a GRC Intelligence Platform; SOX/ICFR heritage | enterprise | Tier 2 (product page + operational FAQ) |
| Hyperproof | GRC platform with controls-operations center of gravity; Continuous Controls Monitoring as a marketed capability | mid-market → enterprise | Tier 2 (product + CCM pages) |
| Secureframe | Compliance automation (light sample, root pages only) | SMB → mid-market | Tier 2 (root only) |

Sampling notes: FloQast attempted twice (404 ×2) — abandoned. ServiceNow GRC not attempted (recorded unreachable timeout ×2 in the internal-audit-management pass). No claims below rest on unreachable vendors.

## Sources

- Drata Help Center (Tier 1):
  - Create, Edit, and Manage Controls — https://help.drata.com/en/articles/13380335-create-edit-and-manage-controls
  - Assess and Manage Individual Controls — https://help.drata.com/en/articles/13372784-assess-and-manage-individual-controls
  - Help center index (Controls, Monitoring, Evidence, Frameworks, Risk collections) — https://help.drata.com/
- Vanta Help Center (Tier 1):
  - Controls Page — https://help.vanta.com/en/articles/11345373-controls-page
  - Navigation index — https://help.vanta.com/hc/en-us
- Optro (Tier 2):
  - Controls Management product page with operational FAQ — https://optro.ai/product/controls-management
- Hyperproof (Tier 2):
  - Home — https://hyperproof.io/
  - Continuous Controls Monitoring Software — https://hyperproof.io/continuous-controls-monitoring/
  - Help Center root located (https://help.hyperproof.app/en/) but not article-crawled
- Secureframe (Tier 2, light): https://www.secureframe.com/

## Product Observations

### Drata (Evidence Layer A — direct observation, Help Center)

Definition quoted from product docs: "Controls implement and articulate the policies, processes, and activities your organization uses to meet compliance requirements."

- **Control object**: Name (required), Code (required; editable only for custom controls, not vendor-framework controls), Description (required), optional Question and Activities fields. Control detail page tabs: Overview, Evidence, Monitoring, Policies, Frameworks, Risks.
- **Mapping is mandatory**: "Controls must be mapped to at least one requirement." A control also maps to automated tests, evidence items, policies, and risks.
- **Vendor-maintained control framework**: the Drata Common Framework (DCF) ships a pre-built control set; organizations edit DCF controls or add custom controls, can revert a control to the latest DCF template, and can bulk-import controls.
- **Control ownership**: one or more Control Owners per control, responsible for keeping evidence linked, keeping monitoring tests passing, and supporting audits. Owner eligibility restricted by role (Administrators, Information Security Leads, Control Managers, Workspace Managers); owners auto-removed when role/employment status changes. Owners may be admins/analysts rather than business stakeholders — explicitly flexible.
- **Testing/monitoring**: a Monitoring tab per control shows mapped tests with pass/fail history; a Test Library provides the tests; tests can be run manually; findings can be excluded; custom tests can be authored. Test states (inactive, not tested/disabled, non-production, erroring) are explicitly *not factored into readiness*.
- **Readiness model**: per-control readiness indicators for Evidence, Monitoring, Policies, Approvals; a control is "Not Ready" without *positive* evidence (passing tests, valid artifacts, published policies, completed required approvals).
- **Required Approvals**: stakeholder reviews/approvals tracked per control as governance evidence for auditors.
- **Evidence**: link/unlink at any time; evidence items live in an Evidence Library with renewal dates; miscellaneous evidence can exist only on the control.
- **Scope & retention**: controls marked in or out of scope; **controls cannot be deleted** (audit-trail preservation); all updates logged on an Events page (full history).
- **Roles**: Admins, Information Security Leads, Control Managers, Workspace Managers; separate read-only auditor access; workspaces for multi-program accounts.
- Adjacent objects in the same platform (not controls-centered): policies, personnel, assets, vulnerabilities, vendors, risks, access reviews, trust center.

### Vanta (Evidence Layer A — direct observation, Help Center)

- **Controls Page**: lists all of the account's controls; filter, edit, assign. Left navigation surfaces Controls Page alongside Tests Page, Frameworks Page, Policies Page.
- **Control status (product-documented definition)**: "Ok" = all automated tests and mapped documents for the control are passing; "Needs evidence" = no mapped tests or documents, or one or more are not passing. Explicitly: status "reflects the current state of those tests and documents—it does not represent an auditor's assessment of the control." Status is not visible to auditors but *is* shared to the Trust Center where present.
- **Mapping**: from a control you map tests, documents, frameworks, and risk scenarios. Controls map to policies (policy templates come pre-mapped; additional mappings manual or AI-suggested).
- **Custom fields** per control (typed fields: revision number, date last updated, applicability, process/procedure, frequency, statuses); fields can be flagged "share with auditor" and become columns on the Controls page; bulk import populates them.
- **Lifecycle of removal**: removing a custom control permanently deletes it (with a mapped-frameworks warning); bulk deactivation supported; deactivated controls viewable and re-addable with **effective dates** (deprecation date / effective date) — an effective-dating model for control retirement.
- Editing a control "may affect your audit" — the product instructs informing the auditor and success manager of changes.
- Plan-gating note: "Some controls features may require an upgrade or add-on."

### Optro / AuditBoard lineage (Layer A on FAQ answers; Layer B otherwise — product page, Tier 2)

- **Positioning**: "Controls management software… within the GRC Intelligence Platform"; "fundamentally built for controls management."
- **Lifecycle framing**: "streamlined risk assessments, planning, testing, and reporting" — planning documentation, testing fieldwork, remediation, reporting.
- **Out-of-the-box RCM** (Risk Control Matrix) to stand up the initial program — the control↔risk matrix is the entry artifact.
- **Fieldwork machinery**: sample selection, evidence validation, tickmarking audit evidence (AI-assisted); AI-generated narratives and flowcharts mapping in risks and controls.
- **Continuous control testing**: "continuous monitors"; real-time data surfaces deficiencies sooner; FAQ confirms continuous-monitoring support; contrast framed as point-in-time assessments vs real-time monitoring.
- **Certification/attestation**: automated certification workflows linking management attestation directly to audit evidence (CEO/CFO certification for SOX 302/404).
- **Frameworks named**: SOX, FDICIA, MAR, J-SOX, UK Corporate Governance code, "general controls management" — multiple financial/compliance frameworks on one control structure.
- **Evidence automation**: integrations to 150+ systems (Oracle, Workday, Okta, IT systems) to automate evidence collection for internal controls.
- **Control rationalization** (customer quote): "rationalize our control structure. We can see where we have too many, too few, or the right number of controls" — the control population itself is a managed subject.
- **Interlock with audit** (customer quote): within controls, reference operational audit work steps, and within audits reference controls, "link back and forth."
- **First-line + external auditor collaboration**: "Customizable workflows and permissions enable both the first line and external auditors to execute tasks independently."

### Hyperproof (Layer A on CCM page steps/FAQ; Layer B otherwise — product pages, Tier 2)

- **Control operations**: "Automate control operations, connect controls to risks, and maintain a common control set across your enterprise"; headline stat "66% reduction in duplicative controls" — common-control reuse across frameworks is a marketed capability.
- **CCM setup narrative (6 steps)**: 1) import controls from a spreadsheet or build them, organize by criticality/domain/owner; 2) connect data sources (identity providers, endpoint management, vulnerability scanners) — optional; 3) identify automation candidates (high-frequency processes generating structured data; the system recommends tests from collected data); 4) build automated tests with an Excel-formula-like syntax, per control or per group of related controls; 5) define failure responses — who is notified, escalation path, urgency triage, configurable at the control level; 6) monitor through live dashboards; reports become "the strongest evidence artifact at audit time."
- **Ownership + accountability**: "Assign control ownership directly… When a test fails, the right person is notified immediately — not weeks later during a review cycle."
- **Manual vs automated posture** (FAQ): manual testing is typically quarterly/annual; continuous monitoring runs on a defined schedule (daily/weekly/continuous) and immediately surfaces failures; "controls that rely on narrative or judgment-based evidence are better managed through traditional testing workflows" — automated monitoring and manual testing workflows coexist in one product.
- **Use-case examples**: IAM access reviews/orphaned accounts, endpoint encryption/patching compliance, vulnerability patch timelines, SIEM/log evidence trails, code deployment approval checks.
- **Suite context**: Compliance, Risk, Audit, TPRM, Policy Management products; policies "connect to the controls that enforce it"; a FedRAMP-class deployment variant exists.

### Secureframe (Layer B, root pages only)

Same family as Drata/Vanta: automated tests, continuous monitoring, remediation guidance, "manage failing controls and assess risk to easily improve your security posture", framework breadth (SOC 2, ISO 27001, HIPAA, PCI DSS, GDPR, NIST, CMMC), AI assistance. No structural detail beyond root level; used only to corroborate cross-product commonality.

## Cross-product Comparison

| Structure / capability | Drata | Vanta | Optro | Hyperproof | Secureframe | Layer |
|---|---|---|---|---|---|---|
| Control as named, described record in a library/register | ✔ (Controls page + detail page) | ✔ (Controls Page list) | ✔ (RCM + control structure) | ✔ (import/build/organize) | implied | B |
| Control fields: name/code/description + descriptive extras | ✔ (+ question, activities) | ✔ (summary, description, custom fields) | ✔ (narratives, flowcharts) | ✔ (criticality, domain, owner tags) | — | B |
| Mapping control ↔ framework requirements | ✔ mandatory (≥1 requirement) | ✔ (map frameworks) | ✔ (RCM; multi-framework) | ✔ (common control set) | ✔ (frameworks) | A/B |
| Mapping control ↔ risks | ✔ (Risks tab) | ✔ (risk scenarios) | ✔ (RCM; risks+controls in flowcharts) | ✔ ("connect controls to risks") | — | B |
| Mapping control ↔ policies | ✔ | ✔ (pre-mapped templates + AI suggestions) | — (policies in sibling products) | ✔ ("policies… connect to the controls that enforce it") | — | B |
| Testing loop: scheduled/manual tests with pass-fail results | ✔ (Test Library, manual runs, pass/fail history) | ✔ (automated tests drive status) | ✔ (planning→testing→reporting; sampling, tickmarks) | ✔ (manual workflows + automated tests) | ✔ (automated tests) | B |
| Continuous/automated control monitoring | ✔ | ✔ | ✔ (continuous monitors) | ✔ (CCM product page) | ✔ | B |
| Mechanism is variant, not definition (manual-only era products exist) | — | — | ✔ (contrast framed by vendor) | ✔ (FAQ: judgment-based controls stay manual) | — | C |
| Recorded evidence artifacts per control | ✔ (Evidence Library, renewal dates) | ✔ (mapped documents) | ✔ (automated evidence collection; tickmarked workpapers) | ✔ (reports as evidence artifacts) | ✔ | B |
| Failure → remediation/deficiency handling | ✔ (findings, exclusions) | ✔ (failing tests → status) | ✔ ("surface deficiencies sooner") | ✔ (failure responses, notification, escalation) | ✔ ("manage failing controls") | B |
| Control ownership/accountability | ✔ (owners, eligibility rules, auto-removal) | ✔ (assign) | ✔ (first-line workflows) | ✔ (ownership + failure notification) | — | B |
| Per-control assurance status/readiness roll-up | ✔ (Ready/Not Ready + per-domain readiness) | ✔ (Ok / Needs evidence; explicitly not an auditor opinion) | ✔ (reporting stage) | ✔ (live control-health dashboards) | ✔ (posture) | B |
| Common control reuse across multiple frameworks | ✔ (one control → many requirements; export mappings) | ✔ (map multiple frameworks) | ✔ (SOX/FDICIA/MAR/J-SOX/UK CGC on one structure) | ✔ (headline capability) | — | B |
| Control population rationalization ("too many/too few") | — | — | ✔ (customer quote) | ✔ (duplicative-controls stat) | — | B |
| Auditor/external collaboration | ✔ (auditor access role) | ✔ (share-with-auditor fields) | ✔ (external auditors execute tasks independently) | ✔ (evidence for auditors) | — | B |
| Management certification/attestation linkage | — | — | ✔ (SOX 302/404 certification workflows) | — | — | A (product-specific) |
| Bulk import / pre-built control content | ✔ (bulk import; DCF; revert-to-template) | ✔ (import; pre-mapped templates) | ✔ (OOTB RCM) | ✔ (spreadsheet import; recommended tests) | — | B |
| Effective-dated retirement / no-delete retention | ✔ (cannot delete; out-of-scope instead) | ✔ (deactivation + effective dates; custom-control delete) | — | — | — | A (product-specific) |
| History/audit trail of control changes | ✔ (Events page) | — (changes flagged as audit-affecting) | — | — | — | A/B |
| AI assistance (era-current) | ✔ (suggestions, summaries) | ✔ (AI-suggested mappings) | ✔ (narratives, fieldwork) | ✔ (test recommendations) | ✔ | B |
| Data-source integrations feeding tests/evidence | ✔ | ✔ | ✔ (150+ systems) | ✔ | ✔ | B |
| Trust-center publication of control-derived posture | ✔ | ✔ (status shared to Trust Center) | — | — | — | A (pole-specific) |

## Canonical Model (abstraction)

### L0 — Defining Invariant

The smallest structure without which the product is not a Controls Management Platform:

1. **The control as the managed object of record** — a persistent, identified register of controls; each control is a named, described safeguard/activity the organization relies on (a policy, process, or technical activity that mitigates risk or satisfies requirements). Remove → policy manager, risk register, or audit tool.
2. **The mapping layer that binds each control to what it serves** — controls are associated with the framework requirements they implement and, commonly, the risks they mitigate and the policies they enforce; a control is never a free-floating record. Remove → a list of test scripts or a framework reference document.
3. **The recurring validation loop with recorded results and consequence** — controls are tested/re-checked over time (scheduled manual testing or automated monitoring; the mechanism is a variant), each validation recorded as pass/fail evidence, and failures become tracked remediation work feeding a per-control assurance state. Remove → a static control catalog.

Ownership, readiness scores, dashboards, and auditor collaboration sit at L1, not L0.

**Historical / market-sample check**: pre-software practice — risk-control matrices in spreadsheets, control binders, periodic testing workpapers, remediation logs — satisfies all three invariants (register + mapping + recurring testing with recorded results). Early web-based SOX tools (pre-integration era) satisfy it without any automation. Non-US regimes (J-SOX, UK Corporate Governance Code) satisfy it. The definition does not depend on integrations, automated tests, AI, cloud delivery, or readiness scores.

### L1 — Common Mature Structure

- control ownership with accountability assignment (owners responsible for evidence, tests, audit readiness)
- per-control assurance status/readiness roll-up (labels vary by product; derived from mapped tests/evidence; in two sampled products explicitly *not* an auditor opinion)
- common-control reuse: one control serving requirements of multiple frameworks
- evidence library / evidence artifacts attached to controls
- deficiency/issue tracking for failures, remediation to closure
- control documentation support (descriptions, narratives, process notes)
- bulk import + vendor pre-built framework/control content
- auditor collaboration (scoped access, shareable fields, audit-ready exports)
- dashboards/reporting of control health across the population
- change history / audit trail of control records
- AI assistance (era-current)

### L2 — Variant / Optional Structure

- automation substrate: integrations to identity/HRIS/cloud/endpoint/vulnerability systems feeding automated tests and evidence (continuous control monitoring); manual test schedules remain a first-class alternative for judgment-based controls
- control population rationalization (too many / too few / duplicated controls)
- management certification/attestation workflows (finance-controls pole)
- framework breadth by domain: financial-reporting (SOX, FDICIA, J-SOX, MAR, UK CGC) vs information-security (SOC 2, ISO 27001, HIPAA, PCI DSS, NIST, CMMC) vs cross-domain
- effective-dated control retirement vs scope-based retention (two documented models)
- trust-center publication of control-derived posture (automation pole)
- deployment/packaging: standalone product vs GRC-suite module vs platform application
- governed/regional deployment (FedRAMP-class environments)

### L3 — Vendor-specific (kept out of the final document)

- Drata: DCF branding, "not factored into readiness" test-state rules, role names, auto-removal of owners on role loss, Events page, revert-to-template, workspace mapping of control info
- Vanta: typed custom fields shared with auditor, deactivated-controls view with effective dates, permanent-delete semantics for custom controls, status invisible to auditors but visible on Trust Center, plan-gated features
- Optro: OOTB RCM, Autonomous Testing as a separate product, tickmarking, CEO/CFO certification workflows, Fortune-500 claim, support.soxhub.com heritage, sibling products (CrossComply, RegComply, RiskOversight, OpsAudit)
- Hyperproof: Hypersyncs, Excel-formula test syntax, control-level failure-response configuration, FedRAMP-class "Gov" deployment, framework/integration counts
- Secureframe: Comply AI branding, Defense/CMMC packaging

## Vendor-specific Findings

- Readiness/status vocabulary is vendor-specific everywhere and no two products agree (Ready/Not Ready; Ok/Needs evidence; live dashboards; reports). Only the *concept* (per-control derived assurance state) is cross-product.
- Effective-dating (Vanta) vs no-delete (Drata) are opposing retention philosophies for the same problem (control retirement) — both Layer A, neither canonical.
- Mandatory requirement-mapping (Drata: "must be mapped to at least one requirement") is a product rule; "controls serve requirements" is canonical, per-product minimum-mapping rules are vendor-specific.

## Boundary Findings

1. **vs Compliance Management Platform** (that pass flagged this as its "softest new seam" — DISCHARGED here): the discriminator candidate is confirmed. In compliance products the requirement register is the center and controls appear as the activity layer under requirements; in controls management the control library + testing program is the center and requirements are one mapping target among several. Vendor behavior supports the split: the Optro family ships Controls Management and RegComply (regulatory compliance) as separate products; the automation pole centers controls while frameworks/requirements hang off them. Keep both Types; overlap (evidence, testing, mapping) is real and suites blur the edges.
2. **vs Internal Audit Management**: program/engagement-centered (universe → risk-based plan → engagements → findings ledger) vs control-record-centered (library → testing loop → assurance state). Vendor-stated distinction (Riskonnect, verbatim, per that pass); Optro ships both as separate products. Interlock documented from both sides: audit findings identify control gaps; control testing informs audit scope; a customer quote shows bidirectional referencing between controls and audit work steps. Cross-reference maintained per the internal-audit pass's recommendation.
3. **vs Audit & Assurance Platform**: engagement-execution spine (side-agnostic) vs the standing lifecycle of the control record itself. The SOX pole's testing fieldwork is the overlap zone; the automation pole has no engagement object of its own.
4. **vs GRC Platform**: controls management is one pillar of the GRC umbrella; GRC's defining property (per that pass) is the shared interlocking record core across risk/compliance/audit. Controls management is definable without the umbrella; suites commonly deliver it as a module.
5. **vs Enterprise Risk Management**: risk register + assessment campaigns centered; controls enter as mitigation/treatment records linked to risks. Reversing the lens (control-centered, risks as mapping targets) is exactly this Type.
6. **vs Compliance Policy Management**: policy *document* lifecycle (draft → approval → published → attested) vs control *activity* lifecycle; policies map to controls in both directions but neither is a variant of the other.
7. **vs Accreditation / Certification Management**: credential/external-recognition spine vs control testing; that pass's call (capability relationship: controls in service of the credential vs control object centered) is consistent with this sample.
8. **vs Security Compliance Platform (§15, unprocessed)**: the security-framework realization (SOC 2/ISO 27001 control monitoring) is documented here as this Type's automation pole. Containment vs separate Type to be ratified at that pass — flagged.
9. **"Remove what → becomes another Type" tests**: center the requirement register instead of the control library → Compliance Management Platform; replace the control library with the engagement spine → audit management; keep the control register but drop the recurring validation loop → a control catalog, not this Type; drop the mapping layer → an isolated test tracker / evidence collector.
10. **Naming hazard**: "controls" in industrial process control, instrument control, and building automation is a different universe; this leaf is the internal-control (COSO/SOX-heritage) universe of §11.

## Uncertainties

- Optro and Hyperproof evidence is Tier 2 (product/FAQ pages); operational details of their testing workflows (sampling mechanics, workpaper structures, RCM editing) were not directly observed and no precise claims about them are made.
- Hyperproof Help Center articles were not crawled; Hyperproof structural claims rest on its product/CCM pages.
- Secureframe was sampled at root level only; used strictly as cross-product corroboration.
- Whether a *pure* controls-management product exists outside GRC/compliance suites (a standalone controls tracker with no frameworks at all) was not confirmed; both sampled poles embed controls in a requirement/risk context, supporting the mapping layer as L0, but the extreme edge case is unverified.
- Role/permission models beyond Drata's were not directly observed; role-specific claims are kept product-specific.
- ServiceNow GRC (enterprise IT-GRC pole where the control is a CMDB-linked object) remains unverified; no claims made.

## Final Synthesis

A Controls Management Platform is the system of record for an organization's **controls**: the safeguard activities (processes, policies-in-operation, technical measures) it relies on to mitigate risk and satisfy compliance frameworks. Its defining structure is three-fold: (1) the **control register** — controls as persistent, identified, described records; (2) the **mapping layer** binding each control to the framework requirements it implements, the risks it mitigates, and the policies that govern it, with common-control reuse so one control serves many frameworks; (3) the **recurring validation loop** — controls are tested over time (scheduled human testing and/or automated continuous monitoring), results are recorded as evidence, failures drive tracked remediation, and the whole rolls up to a per-control assurance state reported to management and auditors.

The market realizes this Type in two poles: a **finance-controls pole** (SOX/ICFR heritage — planning documentation, risk-control matrices, testing fieldwork, management certification) and an **automation pole** (cloud compliance — continuously monitored automated tests, integrated evidence collection, readiness dashboards). Both poles run the same three-part structure; the automation substrate, framework domain, certification machinery, and retention philosophies are variants. The Type stands on its own against its siblings: it is not the requirements program (Compliance Management), not the audit program (Internal Audit / Audit & Assurance), not the risk program (ERM), not the policy library (Compliance Policy Management), and not the credential spine (Accreditation/Certification) — controls are the objects those programs all consume, and here they are the managed subject itself.
