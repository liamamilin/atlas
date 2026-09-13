# Research Notes — Compliance Management Platform

## Research Goal

Understand what a generic (domain-agnostic) Compliance Management Platform really is: what objects it keeps as records, what work it tracks, how compliance state is evidenced and reported, and how it differs from the surrounding cluster of §11 types (GRC umbrella, Regulatory Change Management, Controls Management, Internal Audit, Accreditation/Certification, Policy Management) and from the domain-specific compliance types that already have their own leaves (financial, HR, privacy, entity, environmental, security).

## Initial Boundary

Working hypothesis at start:

- Core: an organization-side system of record for running a compliance program — obligations/requirements mapped to the organization → tracked compliance activities → retained evidence and compliance status.
- Nearest neighbors: GRC Platform (umbrella), Regulatory Change Management (change feed), financial-compliance-management (domain instance), accreditation-certification-management (credential spine), security-compliance-platform (§15 sibling), controls-management-platform and compliance-policy-management (§11 siblings, unprocessed).
- Confusable: task management, policy management, audit management, law/regulation content services.

## Prior-pass obligations this pass must discharge or cross-reference

1. **governance-risk-compliance-platform (§11, processed 2026-09-07)** — explicit joint-review flag: "compliance-management-platform (obligations-program-centered child vs umbrella — candidate outcomes keep-both or documented containment)". GRC's recorded removal test: "remove the requirement side → ERM, remove the risk side → compliance management". → This pass must rule on keep-both vs containment.
2. **financial-compliance-management (§08, processed 2026-09-06)** — recorded as "closest boundary pair in the taxonomy"; candidate outcomes "two domain Types (finance vs generic) or a consolidation view treating financial as the finance-domain variant pole". → This pass must rule from the generic side.
3. **regulatory-change-management (§11, processed)** — seam recorded from RCM side: RCM centers the change event; Compliance Management centers the standing obligations/activities program the changes feed; joint review recommended. → Confirm from this side.
4. **internal-audit-management (§11, processed)** — recommendation: future §11 audit/compliance-family passes cross-reference the internal-audit vs audit-assurance resolution to avoid re-divergence. → Cross-referenced below.

## Research Questions

1. What is the primary record? Requirement/obligation? Control? Activity? Assessment? Evidence?
2. How do requirements enter the system (vendor template libraries, custom authoring, regulatory change feeds)?
3. What does the tracked work look like (actions/tasks/tests/attestations), and how are owners/deadlines/statuses handled?
4. How is evidence captured, stored, and reused (manual upload vs automated collection vs continuous monitoring)?
5. How is compliance state computed and presented (scores, readiness, posture) and to whom?
6. How do audits and auditors participate (evidence requests, exports, external access)?
7. Where does the employee appear (task portal, attestations, training) vs the compliance officer?
8. How does risk attach (risk register linkage) — is a risk model definitional?
9. What separates this type from domain-specific compliance types and from the GRC umbrella?

## Representative Products

Selected for market representation, documentation quality, differing product philosophy, and differing customer tier:

| Product | Pole | Tier / segment | Evidence level reached |
|---|---|---|---|
| Microsoft Purview Compliance Manager | assessment/score-led machinery bundled in a hyperscaler compliance estate | any org on M365; free tier + premium content | Tier-1 (Microsoft Learn operational docs ×2) |
| Drata | security-framework compliance automation (continuous monitoring, evidence collection) | tech/SaaS; SMB→enterprise | Tier-2 product pages (help center documented by the accreditation pass) |
| Hyperproof | mid-market pure-play compliance-operations platform inside a GRC suite | mid-market/enterprise | Tier-2 site + product structure (help center unreachable in prior passes) |
| NAVEX (NAVEX One) | enterprise ethics & compliance program suite (training, policy, hotline, portal, program modules) | enterprise; SMB bundle | Tier-2 platform/module pages |
| SAI360 | enterprise GRC/ethics suite with a regulatory-compliance module | enterprise | Tier-2 platform/module pages |

Deliberately not sampled: Ncontracts Ncomply (banking pole — already sampled by the financial-compliance-management pass; used only for that seam), Vanta/Secureframe (same pole as Drata — already Tier-1-sampled by accreditation-certification-management pass), Optro/AuditBoard and LogicGate (sampled by GRC and audit passes), ServiceNow IRM (docs unreachable in three prior passes).

## Sources

Fetched 2026-09-07 (research date):

- Microsoft Learn — "Microsoft Purview Compliance Manager" (https://learn.microsoft.com/en-us/purview/compliance-manager) — Tier-1
- Microsoft Learn — "Build and manage assessments in Microsoft Purview Compliance Manager" (https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) — Tier-1
- Drata — https://drata.com/ and https://drata.com/products/compliance-automation — Tier-2 (product/positioning); Tier-1 help-center evidence for the same pole exists via the accreditation-certification-management pass (Vanta/Drata/Secureframe)
- Hyperproof — https://www.hyperproof.io/ — Tier-2 (platform/module structure, framework library); help portals previously unreachable (404 ×2 + transport error in accreditation pass; help.hyperproof.app listed but not fetched)
- NAVEX — https://www.navex.com/en-us/, /en-us/platform/, /en-us/platform/compliance-hub/ — Tier-2 (module structure, employee portal)
- SAI360 — https://www.sai360.com/ — Tier-2 (module map)

Source-access limitations: NAVEX, SAI360, Hyperproof, and Drata product surfaces are marketing/product-structure pages; no operational detail (states, fields, limits, defaults) is asserted from them. Microsoft Learn is the only Tier-1 operational source; precise state vocabulary below is therefore Microsoft-documented and treated as a realization, not a canon.

## Product Observations

### Microsoft Purview Compliance Manager (evidence layer A)

- Self-description: "a solution that helps you automatically assess and manage compliance across your multicloud environment… from taking inventory of your data protection risks to managing the complexities of implementing controls, staying current with regulations and certifications, and reporting to auditors."
- Key elements documented as the product's data model:
  - **Control** — "a requirement of a regulation, standard, or policy"; three responsibility types: Microsoft-managed, customer-managed ("your controls"), shared; organized in control families (e.g., Configuration Management, Incident Response).
  - **Assessment** — "a grouping of controls from a specific regulation, standard, or policy", scoped to a set of services (multi-cloud: M365, Azure, AWS, GCP); carries an assessment score; assessments are organized into **groups** (by year, regulation, division, geography); groups are structural containers, not security boundaries.
  - **Regulations** — vendor-supplied **regulation templates** (vendor-published count: over 360) plus **custom regulation templates** the org authors; availability gated by licensing (free vs premium template licenses; AI-regulation premium templates).
  - **Improvement actions** — the work unit: "centralize your compliance activities", each with recommended guidance, assignable to users, with stored **evidence, notes, and recorded status updates**; technical actions (auto-detected from tenant signals, incl. via Defender for Cloud) vs non-technical actions (manual, e.g., instituting a workplace policy); **shared actions** satisfy multiple requirements across assessments/groups ("implement one improvement action and meet several requirements simultaneously").
  - **Compliance score** — risk-based, points awarded per completed improvement action, weighted by potential risk; initial score from the default **Data Protection Baseline** assessment (draws from NIST CSF, ISO, FedRAMP, GDPR).
- Status machinery (Microsoft-specific vocabulary, documented): control test statuses Passed / Failed / None / Out of scope / In progress; assessment statuses derived from control statuses (Complete / Incomplete / None / In progress); improvement-action test statuses incl. "partial credit".
- Assessment **update mechanism**: when the underlying regulation template changes (regulatory or product changes), assessments show a **pending update**; the org reviews changes and accepts or defers; accepted changes are permanent; updates apply per group. This is an in-product realization of regulatory-change intake feeding the standing program.
- **Reporting**: export an assessment as an Excel snapshot "for compliance stakeholders… or for external auditors and regulators"; per-assessment **user access roles** (Reader / Assessor / Contributor) including **external users** (auditors) via directory roles.
- Deletion discipline: assessments permanently deleted; last assessment cannot be deleted (need ≥1 for the system to function).
- AI-era extensions: AI-regulation templates (EU AI Act, ISO/IEC 23894, ISO/IEC 42001, NIST AI RMF), automated assessments for AI apps/agents syncing evaluation results from Azure AI Foundry, Copilot baseline assessment auto-provisioned.

### Drata (evidence layer A for positioning; help-center depth exists via prior pass)

- Self-positioning (2026): "Agentic Trust Management Platform"; the relevant module is **Compliance Automation**: "Automate evidence collection and control monitoring across frameworks so you're always prepared for your next audit."
- Product structure: **Controls and Evidence** ("define controls once, manage control ownership clearly, keep evidence linked in a single platform"); **Monitoring and Tests** ("run automated tests across your environment… surface failures and determine remediation plans"); **Audit Hub** ("centralize auditor collaboration, evidence requests, and approvals in one secure hub"); internal risk register; vendor risk; policy & personnel management.
- Framework orientation: pre-mapped frameworks (SOC 2, ISO 27001/42001, GDPR, HIPAA, PCI DSS, DORA, FedRAMP, CMMC + custom frameworks).
- Narrative structure of the pitch maps the pain points the type solves: spreadsheets don't scale (evidence lost, control status stale), audit prep chaos (chasing screenshots), unclear ownership (control owners, remediation routing), reporting difficulty (point-in-time vs real-time readiness).
- Anti-pattern framing: "Early compliance programs often start in shared documents and spreadsheets… a brittle system no one trusts." → the pre-software baseline the type replaces.

### Hyperproof (evidence layer A for structure; Tier-2)

- Self-positioning: "The GRC Platform That Makes Compliance Easy" / "GRC Platform That Gets Work Done" — a GRC-suite carrier whose lead module is Compliance ("achieve continuous compliance; automate control operations, connect controls to risks, maintain a common control set across your enterprise").
- Companion modules: Risk Management, Audit Management ("connect evidence to requests, collaborate securely with auditors"), TPRM, Policy Management; a "Continuous Controls Monitoring" product line; Gov edition (FedRAMP-certified environment).
- Framework content supply: vendor-published count 160+ pre-built frameworks (HIPAA, CMMC, PCI DSS, SOC 2, ISO 27001, NIST SP 800-53, NIST CSF, DORA, NIS2, FedRAMP, GDPR, HITRUST, custom) — the "largest framework library" is their claimed differentiator.
- Integration spine: vendor-published count 200+ integrations (identity, cloud, ticketing, HRIS, storage, security tooling) — the substrate for automated evidence/monitoring.
- Industry solutions: healthcare, technology, fintech, aviation, manufacturing compliance — domain tuning as packaging.

### NAVEX (evidence layer A for structure; Tier-2)

- NAVEX One GRC platform with modular suite: Whistleblowing & Incident Management, Ethics & Compliance Training, Policy & Procedure Management (PolicyTech), Risk & Governance (IRM), Third-Party Screening/Risk, Regulatory Change Management, Analytics & Benchmarking, and "Compliance Software Bundle" (Compliance Essentials).
- **NAVEX One Compliance Hub** = the **employee-facing compliance task portal**: "one to-do list for all compliance activities" — a personal portal consolidating assigned compliance tasks (training, disclosures, deadlines), a policy/code-of-conduct resource library, issue-reporting channels, AI answers to policy questions; role/department/location-based task targeting; onboarding compliance tasks. → Documents the "employee as compliance subject" surface of the program.
- The officer-side program machinery is distributed across modules (IRM, RCM, policy, training) — i.e., at the suite pole, "compliance management" is realized as a bundle of program surfaces rather than one obligations register screen.
- Vendor-published marketing numbers (13,000+ customers; 88M people supported) kept here only.

### SAI360 (evidence layer A for structure; Tier-2)

- Enterprise GRC/ethics platform ("GRC Elevate 6.0"), 20+ configurable modules: Enterprise Risk, Incident, External Risk Intelligence, TPRM, IT Risk, Internal Audit, **Regulatory Compliance** (module URL sits under regulatory-change-management — consistent with the RCM pass's observation that suite vendors realize "regulatory compliance" as change-driven machinery), Policy Management, Whistleblower Hotline, COI, Gifts & Hospitality, Disclosure Management, Internal Controls (SOX), Ethics & Compliance Training, Code of Conduct, CSRD/EUDR reporting.
- The compliance-program spine is expressed as connected signals: training exposure, attestation completion, overdue third-party reviews feeding risk-prioritized dashboards — i.e., program elements (training, attestations, disclosures) tied back to compliance state.
- Framework/regulation anchor pages (COSO, CSRD, EU AI Act, DORA, ISO, NIST, SOC 2, SOX) mirror the content-library pattern.

## Cross-product Comparison

| Structure / capability | Microsoft CM | Drata | Hyperproof | NAVEX | SAI360 | Layer |
|---|---|---|---|---|---|---|
| Compliance requirements held as records (regulation/standard/policy controls, frameworks) | ✔ assessments × controls × regulation templates | ✔ frameworks × controls | ✔ frameworks × controls | ✔ program modules + regulation content | ✔ modules + regulation anchors | A (all five) |
| Vendor-supplied requirement content libraries + custom authoring | ✔ 360+ templates (vendor-published) + custom templates | ✔ pre-mapped + custom frameworks | ✔ 160+ frameworks (vendor-published) + custom | ✔ regulation content/services | ✔ regulation anchors | A |
| Tracked compliance work (actions/tasks/tests) with owners, deadlines, status | ✔ improvement actions, assignments, test status | ✔ control owners, remediation routing, tests | ✔ control operations | ✔ Compliance Hub task portal w/ deadlines; program tasks | ✔ workflows | A (all five) |
| Evidence stored against requirements, auditable | ✔ evidence/notes/status in actions; Excel snapshot exports | ✔ evidence library linked to controls | ✔ evidence-to-requests, audit module | ✔ defensible-evidence positioning (RCM page) | ✔ audit-ready claims | A (all five) |
| Program-level compliance state (score/readiness/posture) | ✔ compliance score (risk-weighted points) | ✔ real-time readiness/control health | ✔ compliance posture visibility | ✔ progress insights/benchmarking | ✔ AI risk-prioritized dashboards | A |
| Common-control / one-action-many-requirements mapping across frameworks | ✔ shared improvement actions across assessments/groups | ✔ map controls to multiple frameworks | ✔ common control set, control mapping automation | module-level | module-level | A (3 of 5 direct) |
| Auditor participation (requests, external access, collaboration) | ✔ external auditor roles, exports | ✔ Audit Hub | ✔ audit module + auditor collaboration | via services/RCM evidence | via internal-audit module | A (3 of 5 direct) |
| Automated evidence collection / continuous monitoring | ✔ technical actions auto-detected (tenant + Defender for Cloud signals) | ✔ automated tests, continuous monitoring | ✔ continuous controls monitoring line, integrations | not direct | not direct | A (3 of 5 direct; B overall) |
| Risk linkage (controls↔risks, risk register adjacency) | indirect (NIST CSF-derived baseline) | ✔ internal risk register | ✔ controls connected to risks | ✔ IRM module | ✔ risk modules | A (3 of 5 direct) |
| Regulatory change intake feeding the program | ✔ template-update accept/defer mechanism | ✔ framework updates (positioning) | ✔ framework library updates (positioning) | ✔ separate RCM module | ✔ Regulatory Compliance module | A |
| Employee-facing program surfaces (task portal, attestation, training) | assignments to users | personnel management, policy workflows | partial (work distribution) | ✔ dedicated Compliance Hub portal | ✔ training/attestation/disclosure modules | A |
| Policy management linkage | nontechnical actions | policy management module | ✔ policy module, policies↔controls | ✔ PolicyTech module | ✔ policy module | A/B |
| AI assistance | ✔ AI-era assessment features | ✔ Drata AI/agentic | ✔ Hyperproof AI | ✔ Nira assistant | ✔ AI platform claims | A (era-current) |
| Domain tuning as packaging (healthcare/fintech/finance…) | data-protection/regulation orientation | security/privacy frameworks | ✔ industry solutions | ✔ industries | ✔ industries | A |
| Content licensing as monetization | ✔ free vs premium regulation licenses | plan tiers | plan tiers | bundling | bundling | A (Microsoft direct) |

### What never appears alone

No sampled product ships compliance work-tracking *without* a requirement structure; none ships a requirement register without tracked work or evidence. The trio (requirements → work → evidence/status) co-occurs in all five — the strongest cross-product signal in the sample (layer B).

### What varies structurally

- Where the center of gravity sits: assessment+score machinery (Microsoft), continuous control testing (Drata), framework library + control operations (Hyperproof), program bundle around people/policies/hotline (NAVEX, SAI360).
- How much of the compliance program is in-product vs adjacent modules: point tools vs suites.
- Whether the employee is a task recipient (all) or has a dedicated portal surface (NAVEX).
- Whether requirements are predominantly technical-control-shaped (Microsoft/Drata/Hyperproof security-privacy flavors) or program-shaped (training, conduct, disclosures — NAVEX/SAI360).

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

A generic Compliance Management Platform is an organization-side system of record for running the organization's compliance program. Remove any of these and it stops being recognizable:

1. **The compliance requirement register** — the requirements the organization has determined it must meet (from laws, regulations, industry standards/frameworks, and internal policy), held as structured records scoped/mapped to the organization. Without it: a task manager or a law library.
2. **Tracked compliance work against those requirements** — implement/test/attest/remediate activities with owners, due dates, and recorded status, feeding each requirement's standing. Without it: a static catalog.
3. **Retained evidence and reported compliance state** — evidence artifacts and status kept against requirements over time, aggregated into a program-level state that is reportable to auditors, regulators, and leadership. Without it: a to-do list.

Historical/market-sample check: the pre-software compliance officer's binder (obligation register + assigned remediation log + evidence folder), SOX-era spreadsheet trackers, and document-control-centric compliance in regulated manufacturing all satisfy these three structures without frameworks libraries, automation, scores, portals, or cloud delivery — the definition survives the historical check. Modern implementations (automated evidence, scoring, portals) are NOT part of the invariant.

### L1 — Common Mature Structure (standard capabilities in mature products)

- Vendor-maintained regulation/framework template libraries with custom requirement authoring.
- Cross-framework common-control mapping (one control/action satisfying requirements in multiple frameworks).
- Program-level compliance score / readiness / posture view, usually with drill-down.
- Recurring-cycle and deadline machinery (reminders, calendars, due-state tracking).
- Evidence repository with version/history discipline and audit-ready exports/reports.
- Auditor collaboration surfaces (evidence requests, external read access, request lists).
- Roles and permissions (program admin / assessor / contributor / reader), audit trails; SSO at enterprise depth.
- Integration spine into the org's systems (identity, cloud, HRIS, ticketing, storage, security tooling) feeding evidence and personnel context.
- Policy-management linkage (policies as requirement sources and evidence objects; attestation tracking).
- Regulatory-change intake feeding requirements/activities (native or as a feeder module — see boundary with RCM).
- Risk linkage (requirements/controls connected to risk records; risk assessments as program inputs).
- Employee-facing program surfaces: assigned tasks, training, attestations, disclosures.
- AI assistance (policy Q&A, drafting, evidence suggestions, agentic automation) — era-current.

### L2 — Variant / Optional Structure

- Center-of-gravity poles: assessment/score-led; continuous-control-test-led; framework-library/operations-led; program-suite-led (people/policy/hotline bundle).
- Requirement-domain emphasis: security/privacy standards (SOC 2/ISO/GDPR/HIPAA) vs cross-domain regulatory obligations vs ethics/conduct program content.
- Content monetization: free vs premium template licensing; content included vs licensed.
- Automation depth: manual evidence upload → automated collection via integrations → continuous control monitoring.
- Employee-subject depth: task recipient vs dedicated branded portal.
- Industry tuning as packaged solutions (healthcare, fintech, aviation, manufacturing, financial services…).
- Deployment: SaaS dominant; regulated-government environments (FedRAMP-class); suite-embedded vs standalone.
- Realization as a module of a GRC/ethics suite vs a standalone product.

### L3 — Vendor-specific (research notes only)

- Microsoft: Data Protection Baseline default assessment; exact status vocabulary (Passed/Failed/None/Out of scope/In progress; partial credit); group mechanics (non-security containers, one product-certification pair per group); permanent-deletion discipline and ≥1-assessment requirement; licensing counters; Defender for Cloud-sourced service progress; Azure AI Foundry action sync; Copilot baseline auto-provisioning.
- Drata: "Agentic Trust Management Platform" rebrand; Audit Hub naming; SafeBase pairing.
- Hyperproof: published ROI claims (66% duplicative-control reduction, $150K saved); GRC Elevate naming is SAI360's; Hyperproof Gov FedRAMP Rev5 environment; community/help portals unreachable.
- NAVEX: Nira AI assistant; Compliance Hub branding; EthicsPoint/PolicyTech/RiskRate lineage; 13,000+ customer claims.
- SAI360: GRC Elevate 6.0; 20+ module map; 5M-user claims; regulatory-compliance module's URL under regulatory-change-management.

## Vendor-specific Findings

- The only Tier-1 operational model obtained is Microsoft's; its assessment/action/score machinery is documented here as a realization. All cross-product claims above rest on marketing/product-structure pages for the other four vendors and are worded accordingly in the final document.
- Vendor-published counts (360+ templates, 160+ frameworks, 200+ integrations) are marketing claims, recorded but not promoted.
- The security-framework automation pole (Drata, and by prior-pass evidence Vanta/Secureframe) is the same machinery with a framework-domain emphasis; the accreditation pass documented its help-center depth.

## Boundary Findings

1. **vs GRC Platform (§11 umbrella; joint-review flag from the GRC pass DISCHARGED here)** — Verdict: keep both. GRC's defining core is the *interlocking* risk×control×requirement record core + evaluation-and-issue loop + consolidated cross-domain oversight; Compliance Management's defining core is the obligations→work→evidence program loop, which stands without a risk register (only risk *linkage* is standard). The GRC pass's own removal test supports this: remove the risk side → compliance management. In the live market the generic type is *usually delivered inside* GRC/ethics suites (Hyperproof, NAVEX, SAI360 all carry it as module(s); Drata markets an "Enterprise GRC" neighbor) — documented containment-with-seam: the child application remains a legitimate standalone Type (Microsoft ships it unbundled; Drata/Hyperproof ship compliance-led editions), exactly as ERM was kept as GRC's register-centric child.
2. **vs Regulatory Change Management (§11; RCM pass seam confirmed from this side)** — RCM's system of record is the change event + applicability/impact decision + response trail; this type's system of record is the standing requirement register + program loop. The change feed arrives as (a) a separate module at the suite pole (NAVEX RCM, SAI360's regulatory-compliance module), or (b) an in-product mechanism at the assessment-led pole (Microsoft's template-update accept/defer). Market bundles heavily in both directions — joint review still recommended when consolidating §11, but the two leaves hold.
3. **vs Financial Compliance Management (§08; their pass flag DISCHARGED from this side)** — Verdict: two domain Types, parallel to HR/privacy/entity compliance. Financial compliance = the finance-domain instance (financial-regulator obligations, examiner-facing posture, finance-specific conduct objects); the generic type lacks the conduct-object layer and exam posture and runs on framework/regulation templates for any domain. The obligations-led banking pole (Ncontracts-class) satisfies the generic machinery — consistent with the financial pass's removal test. The consolidation-view candidate is resolved in favor of domain-generic Type + domain instances.
4. **vs Accreditation/Certification Management (§11, processed)** — Their organizing spine is the external recognition event (assessment event + credential validity/renewal). This type's spine is the standing obligations program; certification support (e.g., SOC 2 audit prep) is a common *purpose* but the credential lifecycle is not the record structure. Security-framework automation products straddle the seam (framework readiness ↔ audit-to-credential); cross-reference both documents.
5. **vs Internal Audit Management / Audit & Assurance (§11, processed)** — Cross-referenced per that pass's recommendation: the audit function/engagement spine manages examination of the organization; this type manages the compliance program that audits then examine. The seam is operationalized in-product as auditor evidence requests against the compliance evidence library (Drata Audit Hub; Hyperproof audit module; Microsoft external auditor roles). No core containment either direction.
6. **vs Controls Management Platform (§11 sibling, unprocessed)** — Softest new seam: controls-as-primary-managed-objects vs obligations-program-as-center. In this sample, controls appear as the standard *activity layer* under requirements (control = the operative unit of requirement implementation at three of five poles). Flag for joint review when controls-management-platform is processed; candidate discriminator: whether the control library + testing program is the center (that leaf) or the requirement→activity→evidence loop is (this leaf).
7. **vs Compliance Policy Management (§11 sibling, unprocessed)** — Policies appear here as requirement sources and evidence objects (attestations, acknowledgments); the policy document lifecycle (draft→approve→publish→attest→version) is the sibling leaf's center. Flag for joint review.
8. **vs Security Compliance Platform (§15 sibling, unprocessed)** — The security-framework realization (Drata-class) is a major market chunk with the same machinery and a domain-scoped framework set + technical control tests. Documented here as the security-flavored pole of the generic type; recommend joint review with the security-compliance leaf to ratify containment vs separate Type.
9. **vs domain compliance Types (HR/privacy/entity/environmental — all processed)** — Confirmed pattern: domain types carry domain-specific object models (privacy processing records, entity registers, employment obligations); the generic type is domain-agnostic with template-supplied requirements. The financial pass's "closest boundary pair" concern is fully resolved by the two-domain-Types reading.
10. **Naming note** — "Compliance management software/platform" is used by the market for both the generic type and domain instances (banking, healthcare, security). No alias problem: the directory leaf is the generic type; domain leaves exist separately. One sampled vendor's module name ("Compliance Hub") collides with the leaf name — feature naming, not taxonomy.

## Uncertainties

- NAVEX's officer-side obligations machinery could not be examined at help-center depth (product pages only); the NAVEX observation is structural (suite + employee portal), not operational.
- Hyperproof's operational model (states, program mechanics) rests on marketing/product-structure pages; its help portal has failed across two passes — no operational claims asserted.
- SAI360 evidence is Tier-2 only.
- Drata evidence is positioning-level here; deeper help-center evidence for the same pole exists via the accreditation pass and was not re-fetched to avoid re-divergence.
- Whether the market would rather call the generic type "compliance program management" is untestable from this sample; the directory name matches the dominant market label.

## Final Synthesis

The Compliance Management Platform is the obligations-program-centered member of the §11 compliance/GRC family: a system of record that keeps the organization's compliance requirements as records, tracks the work of meeting them (owners, deadlines, status), and retains the evidence that makes the organization's compliance state auditable and reportable. Vendor-supplied regulation/framework content, cross-framework control mapping, scores/readiness views, auditor collaboration, and system integrations for evidence collection are the standard capabilities mature products add; assessment/score machinery, continuous control testing, framework-library operations, and people/policy/hotline program bundles are the four observed centers of gravity; delivery is overwhelmingly as a module of a GRC/ethics suite, with standalone and hyperscaler-bundled realizations keeping the type independent.
