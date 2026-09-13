# Research Notes — Procedure Management

## Research Goal

Understand how real products govern the lifecycle of an organization's operational instruction documents (procedures / SOPs / work instructions): what the core managed object is, what the controlled lifecycle looks like, how employees interact with published procedures, what audit evidence is produced, and where the boundary lies against Policy Management, ECM/Document Management, LMS, BPM, and knowledge-base tools.

## Initial Boundary

Hypothesis before research:

- Core purpose: author → review/approve → publish single current version → distribute to workforce → acknowledge → periodically review → archive/supersede, with attributable records.
- Nearest neighbors: Policy Management (directory sibling, line above), Enterprise Content/Document Management, Compliance Policy Management / GRC, Corporate LMS, Workflow Management / BPM, Wiki / Knowledge Base.
- Known ambiguity going in: the market largely sells "policy & procedure management" as one product. The directory has both "Policy Management" and "Procedure Management" as separate leaves. Research must determine whether these are separable Types or one Type.

## Research Questions

1. What is the central object, and what content types does one system manage (policy vs procedure vs SOP vs work instruction vs directive)?
2. What lifecycle states and gates exist (draft → review → approval → published/effective → periodic review → archived/obsolete)?
3. Who participates (author, reviewer, approver, document controller, employee) and with what permissions?
4. How is versioning handled (single active version? archives? change visibility)?
5. How do employees receive and interact with procedures (library, search, mobile, acknowledgment, e-signature, training)?
6. What compliance/audit evidence is produced and how is it retrieved?
7. How do products differ by philosophy: governance/audit-driven vs knowledge/how-to-driven?
8. Where are the real boundaries vs ECM, LMS, BPM, KB?

## Representative Products

Selected for market representativeness, document completeness, different philosophies, different tiers and industries:

| Product | Segment / Philosophy | Why selected |
|---|---|---|
| PowerDMS Policy (by NEOGOV) | Public safety / accreditation-driven governance; enterprise-mid | Richest public lifecycle documentation; acknowledgment + accreditation mapping model |
| RLDatix Policy Management (ex-PolicyMedical) | Healthcare / survey-readiness; enterprise | Healthcare governance framing; explicitly brands the module "Procedure & Policy Management" |
| MasterControl Document Control | Life-sciences QMS document control; regulated enterprise | The strict regulated-manufacturing model (approval/distribution/obsolescence, Part 11 e-signatures) |
| ComplianceBridge TotalCompliance | Mid-market, cross-industry, attestation-centric | Distribution + attestation + renewal automation as the core pitch |
| SweetProcess | SMB SOP documentation; knowledge/how-to philosophy | The opposite pole: procedures as living how-to docs with tasks, lighter governance |

## Sources

Research date: 2026-09-06. All sources fetched live (Layer A direct observation of official product pages). Note: **no Tier-1 help-center / user-guide articles were fetched** — the deepest source is PowerDMS's product/tour page, which is unusually operational but still a marketing/product surface. Assertion strength in both notes and final document is calibrated accordingly: no precise limits, windows, defaults, or state-name standards asserted unless directly observed.

- PowerDMS — homepage (https://www.powerdms.com/) and Policy product page (https://www.powerdms.com/policy-management-software) — fetched 2026-09-06
- SweetProcess — homepage (https://www.sweetprocess.com/) — fetched 2026-09-06
- MasterControl — Document Control page (https://www.mastercontrol.com/document-control-software/) — fetched 2026-09-06 (first attempt /solutions/documents/ 404)
- RLDatix — Policy Management module page (https://www.rldatix.com/en-nam/module/policy-management/) — fetched 2026-09-06 (policymedical.com redirects to rldatix.com; first attempt symplr.com 404)
- ComplianceBridge — Policy & Procedure Software page (https://www.compliancebridge.com/policy-procedure-software/) — fetched 2026-09-06

## Product Observations

### PowerDMS Policy (public safety)

Evidence layer: A (direct observation of official product page; detailed role walkthrough).

- Positions as "manage, distribute, and track policies, procedures, SOPs, and other critical operational documents" — one system, one lifecycle for policies **and** procedures and SOPs/SOGs/directives/memorandums. Content types are a vocabulary continuum, not separate subsystems.
- Lifecycle machinery (directly described): edit with Word/Google or in-system editor → configurable review/approval workflows routing through legal / command staff / accreditation managers, with monitored routing steps, reminders, ability to skip steps when approvers unavailable, re-evaluation assignment, approve/deny with written explanations → publish; publishing **automatically archives previous versions**; "only one active version is available to employees"; side-by-side color-coded change compare before acknowledgment → assign acknowledgments to individuals/groups/org units with due dates/timeframes, auto-reminders, real-time completion dashboards → e-signature (timestamped, mobile-supported) → automated recurring (annual) review reminders with progress workflows → reports/export, audit trail logging views and workflow actions.
- Roles: Administrator (lifecycle oversight, workflow monitoring, e-sign progress, version control, can publish selected docs to a public transparency site), Supervisor (to-dos, monitor employee compliance, approve/deny with written explanations, comments in review), Employee (to-do list, compare versions, e-sign, mobile app with offline documents and bookmarks, keyword search, AI natural-language search over approved policies with source links, permission-respecting).
- Compliance framing: "court-ready audit records", proof of "which guidance was available, when it was acknowledged, and which version was in effect"; accreditation mapping (map written directives + proofs to accreditation standards; assessor workspace); AI-generated quizzes/microlearning tied to policies as an add-on; links between policy sections and internal-affairs cases.
- Access control by user/role/group/unit; folders; supports many file types; historical archives accessible to administrators.
- Vendor-specific (L3): AI search answer history window (30 days), file size cap (100MB), implementation "~90 days", cooperative purchasing contracts, dark mode, CJIS-aligned security, public open-records site.

### RLDatix Policy Management (healthcare; ex-PolicyMedical)

Evidence layer: A (module page; medium depth).

- Module literally titled "Procedure & Policy Management": "Streamline your healthcare policies and documents"; "manage, access and collaborate on policies and documents while keeping your organization compliant across locations."
- "Document lifecycle management" with search-as-you-type; "turning static documents into searchable webpages" (controlled docs rendered as internal web content).
- Procedure Management block: "Remain survey-ready at all times when you link policies and procedures directly to standards set by organizations such as TJC, DNV, ACHC, CMS and SoPs. Empower your staff with easy access to the most up-to-date policy information."
- Reporting: "Identify compliance gaps, measure efficiency and promote accountability with data and reports"; documents linked into other healthcare risk/safety modules (event reporting, audits & standards).
- Vendor-specific (L3): named surveyor/standard sets, module linking into RLD360 platform, multi-location networks.

### MasterControl Document Control (life sciences QMS)

Evidence layer: A (product page; concise).

- Document control as part of a QMS: "Simplifies the approval, distribution, retrieval and obsolescence of documents, and automatically tracks revision history."
- "Centralized location that is easily searchable and provides a time-stamped audit trail, reporting and electronic signatures that are 21 CFR Part 11 compliant."
- Interconnection: document control "simplifies training, CAPA, supplier management, audits" — document lifecycle feeds other quality processes (training-on-revision, change control).
- Vendor-specific (L3): Part 11 validation toolkit, change control module, QMS suite modules, ERP/MRP integrations.

### ComplianceBridge TotalCompliance (mid-market, cross-industry)

Evidence layer: A (product/landing page; medium depth).

- Pitch: "automates policy renewals, distribution efforts, attestation, and much more" — renewal cycles, targeted distribution, attestation as the core triad.
- Onboarding questionnaire reveals the operating model: "How many users will need to create, collaborate and approve policies?" / "How many people will receive policies?" / "How many users will be asked to acknowledge policies?" — i.e., authors/approvers vs recipients vs acknowledgers are distinct populations.
- Features: real-time analytics, targeted distribution, flexible testing (quizzes), automated workflows, cloud-hosted; multi-format distribution (Word, Excel, PowerPoint, PDF, HTML, video, images, links).
- Sibling modules: risk assessment/audit, conflict of interest, dynamic workflow (adjacent compliance suite).
- Vendor-specific (L3): usage-based pricing model, named modules (TotalCompliance).

### SweetProcess (SMB SOP documentation)

Evidence layer: A (homepage; medium depth).

- Philosophy pole: procedures as living how-to documentation. Objects: Procedure (step-by-step doc), Policy (rules doc), Process (combine multiple procedures into an overarching workflow), Task (run a procedure/process as an assignable, check-off task), Team (access scoping), Knowledge Base (public/private publishing of the same content).
- Version history "with tracked highlighted changes for every change... Roll back to any version at any time."
- Improvement loop: teammates suggest improvements; managers approve them. Real-time collaboration; approval on submission to manager.
- Comprehension: quizzes on policies/processes/procedures. AI document drafting. Process maps (diagrams). Embedded files/videos/images. Print/export PDF/Word for offline manuals. Browser-capture plugin ("smart record" clicks into procedure steps).
- No mention of formal attestation/e-signature records, scheduled periodic reviews, or archival version states on the homepage — governance machinery is lighter than the compliance-driven products.
- Vendor-specific (L3): task/check-off execution model, migration service, smart browser recorder, SCIM.

## Cross-product Comparison

| Capability | PowerDMS | RLDatix | MasterControl | ComplianceBridge | SweetProcess | Reading |
|---|---|---|---|---|---|---|
| Controlled doc as central object (policy+procedure/SOP in one system) | ✔ | ✔ | ✔ | ✔ | ✔ | Defining |
| Review/approval workflow with attributable decisions | ✔ (route, approve/deny, explanations) | implied (lifecycle mgmt) | ✔ (approval automation) | ✔ (create/collaborate/approve) | ✔ (manager approval of suggestions) | Defining |
| Version control, one current version, history preserved | ✔ (auto-archive, single active) | implied ("up-to-date") | ✔ (revision history) | not explicit on page | ✔ (version history + rollback) | Defining |
| Targeted distribution to workforce | ✔ (indiv/groups/units, due dates) | ✔ ("easy access", locations) | ✔ (distribution automation) | ✔ (targeted distribution) | ✔ (teams, sharing, KB) | Defining |
| Acknowledgment / attestation with records | ✔ (e-sign, tracking) | implied (accountability reports) | ✔ (e-signatures) | ✔ (attestation core) | ✖ (quizzes instead) | Common mature (not definitional) |
| Periodic review / renewal cycles | ✔ (automated recurring reviews) | implied (survey-readiness) | implied (audit readiness) | ✔ (policy renewals automation) | ✖ | Common mature |
| Audit trail / compliance evidence retrieval | ✔ (court-ready records) | ✔ (compliance-gap reports) | ✔ (time-stamped audit trail) | ✔ (real-time analytics) | ✖ (history only) | Common mature |
| Standards/accreditation mapping | ✔ (PowerStandards) | ✔ (TJC/DNV/ACHC/CMS linking) | ✖ (standards via QMS context) | ✖ (sibling audit module) | ✖ | Optional / vertical |
| Training linkage (courses/quizzes on revision) | ✔ (Recall/Ready/training suite) | ✖ observed | ✔ (training mgmt integrated) | ✔ (flexible testing) | ✔ (quizzes) | Common optional |
| Execution of procedures as tasks/checklists | ✖ | ✖ | ✖ | ✖ | ✔ (task check-off) | Product-specific drift toward checklist tools |
| Searchable library, web/mobile reader | ✔ (mobile, offline, AI search) | ✔ (search-as-you-type webpages) | ✔ (searchable central location) | ✔ (anytime access) | ✔ (KB, search) | Common mature |
| AI assistance | ✔ (NL search over docs) | ✔ ("AI-enabled") | ✔ (platform AI) | ✖ observed | ✔ (AI drafting) | Common optional (2026 market) |

## Abstraction Levels

### L0 — Defining Invariant

1. **Controlled procedure document** — the organization owns a defined, attributed record describing how specific work is performed (procedure/SOP/work instruction; often cohabiting with policies and directives in the same repository).
2. **Gated review/approval before use** — content reaches the workforce only through an explicit, attributable review/approval act by authorized people.
3. **Single-current-version control with retained history** — exactly one approved version is presented as current; superseded versions are archived (retrievable), never silently replaced or mixed into circulation.
4. **Controlled distribution to the performing workforce** — the current version is made accessible/assigned to the people expected to follow it, scoped by the organization.

Removing any one: without (1) it is generic workflow/approval software; without (2) it is a wiki/knowledge base; without (3) it is a shared drive / generic document management; without (4) it is a personal authoring tool, not an organizational distribution system.

Historical/market-sample check (per §24): paper SOP binders run by a document controller with sign-off sheets, 1990s ISO 9001 document-control modules, SharePoint + Word policy libraries, and modern SaaS — all satisfy (1)–(4). L0 is not over-fitted to the modern SaaS acknowledgment workflow.

### L1 — Common Mature Structure

- acknowledgment / read-and-understood attestation (e-signature, per-person records, deadlines, reminders, completion tracking)
- scheduled periodic review / renewal cycles with reminders and review workflows
- document metadata & numbering (owner, effective date, review date, doc number, folder/organization taxonomy)
- change visibility (side-by-side compare, revision logs) at revision time
- searchable document library / reader surfaces (web; commonly mobile)
- role-based access control to content
- audit trails and reporting (who viewed/signed which version when; compliance-gap dashboards)
- authoring support (templates, office-suite or online editing, import of existing documents)
- distribution notifications of new/updated procedures

### L2 — Variant / Optional Structure

- acknowledgment/regulatory formality depth: regulated-manufacturing variant (validated system, legally-binding e-signatures e.g. Part 11) vs lighter attestation
- training linkage: quizzes, microlearning, courses triggered by revisions; competency/field-training integration
- accreditation/standards mapping: link documents and proofs to external standard clauses (accreditation bodies, survey readiness); assessor workspaces
- suite embedding: document control inside a QMS (change control, CAPA, audit) or inside a healthcare GRC platform (event reporting, claims) or public-safety platform (IA cases, scheduling)
- content provenance: self-authored vs licensed third-party model policies
- publishing variants: public transparency site (open-records), knowledge-base rendering of procedures
- execution overlay: running a procedure as a per-instance task/checklist (drifts toward checklist/workflow tools)
- AI: natural-language search over approved docs; AI drafting
- deployment: SaaS vs intranet/collaboration-platform-based builds

### L3 — Vendor-specific (kept out of final doc)

PowerDMS: PowerRecall/PowerStandards/PowerReady module coupling, 30-day AI-search answer history, 100MB file cap, ~90-day implementation, dark mode, cooperative purchasing, CJIS alignment, public open-records publishing. RLDatix: TJC/DNV/ACHC/CMS standard sets, RLD360 module links. MasterControl: Part 11 toolkit, change-control/CAPA/training suite. ComplianceBridge: usage-based pricing, COI/risk sibling modules. SweetProcess: task check-off execution, smart browser recorder, process maps, migration service, SCIM.

## Rejected Findings

- "Procedure management = BPM/process automation" — rejected: no sampled product executes procedures; SweetProcess's task model is the only execution overlay and is product-specific.
- "Policy and procedure are separate subsystems" — rejected by evidence: all five products manage policies and procedures (plus SOPs/SOGs/directives/work instructions) in one repository with one lifecycle; the distinction is content semantics, not system structure.
- "E-signature/attestation is definitional" — rejected as L0: SweetProcess (a genuine procedure-management product) has no formal attestation; it is common but not defining. (MasterControl/PowerDMS/ComplianceBridge/RLDatix all support some attestation/records layer.)
- "SMB SOP tools and enterprise policy suites are different Types" — rejected: same L0; differences are governance depth (L1/L2), not core structure.

## Boundary Findings

- **vs Policy Management** (directory sibling): identical lifecycle machinery; difference is content semantics (policy = normative rule "what must be done and why"; procedure = operational instruction "how to do it"). The market sells them as one combined product ("policy & procedure management"; RLDatix module literally titled "Procedure & Policy Management"). Likely the same Application Type or inseparable siblings — flagged in STATUS Boundary Issues; documented here with a procedure/SOP emphasis.
- **vs Enterprise Content/Document Management**: ECM manages any document with generic workflows; this Type's lifecycle semantics (approval gate → single effective version → acknowledgment → scheduled review → archived history as legal evidence) exist specifically for compliance defensibility of work instructions. Remove those semantics and it is ECM.
- **vs Corporate LMS / Training**: LMS manages courses/completions; this Type manages controlled documents and (commonly) acknowledgments. Overlap occurs where procedure revision triggers training; products couple them but neither collapses into the other.
- **vs Workflow Management / BPM / Approval Workflow Platform**: those execute or automate processes; this Type documents and controls the description of how work is done. Approval workflow *inside* this Type is for the document, not for business transactions.
- **vs Wiki / Knowledge Base**: KB optimizes findability of knowledge with no controlled lifecycle; a procedure library without approval/version/governance is a KB, not Procedure Management. SweetProcess straddles but retains version control + approval + access scoping.
- **vs Checklist / SOP-execution tools** (directory-adjacent, not listed): running a procedure per work instance is a different unit of work (a run) than the controlled document.
- **vs Accreditation/Certification Management**: accreditation management governs the credential/assessment cycle; procedure management supplies documents and evidence that accreditation tools map to standards.

## Uncertainties

- No Tier-1 help-center articles fetched; workflow state names and precise mechanics (e.g., how archiving interacts with effective dating) are asserted only at the level the product pages support. Final doc uses conceptual states and notes label variance.
- RLDatix detail is comparatively thin (module page); acknowledgment handling is implied by "accountability"/reports rather than directly described — treated as implied, wording calibrated.
- Whether the directory should keep Policy Management and Procedure Management as separate leaves is a taxonomy question, not resolvable from product evidence alone (products combine them). Flagged, not resolved.
- Segment boundary vs "document management" products marketed for policy use (e.g., SharePoint-based builds) was not separately sampled; deployment variant recorded as L2 without product-level evidence beyond the general pattern.

## Final Synthesis

Procedure Management is the compliance-governed cousin of documentation tools. Its defining core: the organization's procedure as a **controlled document** moving through a **gated, attributable approval lifecycle** into a **single current version**, **distributed to the workforce expected to follow it**, with history retained as evidence. Around this core, mature products add attestation, scheduled reviews, metadata/search, access control, change visibility, and audit reporting; variants add training, accreditation mapping, suite embedding, regulated e-signature formality, and execution overlays. Policies and procedures live in the same machinery in every sampled product; "Procedure Management" is best understood as the procedure/SOP-facing face of the policy-and-procedure management Application Type.
