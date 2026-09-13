# Research Notes — Research Compliance Management

Research date: 2026-09-09
Slug: research-compliance-management
Directory leaf: Research Compliance Management (§23 Education, Research & Knowledge Institutions)

---

## Research Goal

Understand what "Research Compliance Management" software really is as an Application Type: what objects exist inside it, who uses it, how compliance work flows through it, what rules and states matter, and how it differs from the neighboring research-domain Types (IRB / Research Ethics Management, Animal Research Ethics / IACUC Platform, Research Administration Platform) and from generic corporate compliance Types.

## Initial Boundary (pre-research hypothesis)

Hypothesis: software used by universities, academic medical centers, and research institutions to operate their research compliance programs — collecting protocols/disclosures from researchers, routing them through committee and administrator review, recording determinations, tracking training, monitoring ongoing compliance, and producing audit-ready evidence. Expected to span multiple compliance domains (human subjects, animal welfare, conflicts of interest, biosafety, export control), which would distinguish it from the single-domain IRB and IACUC leaves.

Potential confusions flagged up front:
- IRB / Research Ethics Management (single-domain protocol review)
- Animal Research Ethics / IACUC Platform (single-domain)
- Research Administration Platform (grants/pre-award — money, not obligations)
- Compliance Management Platform / GRC (§11 — generic corporate compliance)
- EHS / lab safety platforms (chemical inventory, inspections)
- eRegulatory / clinical-trial site regulatory binders

## Research Questions

1. What are the core objects (protocols, disclosures, registrations, plans, reviews, determinations, training records, events)?
2. Which compliance domains do products cover, and is multi-domain coverage definitional for this leaf?
3. What is the canonical workflow from submission to determination to ongoing compliance?
4. Who are the roles, and how do their surfaces differ (researcher vs administrator vs committee member vs leadership)?
5. How does this Type relate to the IRB / IACUC leaves — module vs suite, domain vs program?
6. What regulatory regimes drive the rules, and how do products encode them?
7. What interfaces exist?
8. What evidence/reporting does the system produce, and for whom?

## Representative Products

| Product | Vendor posture | Customer tier / geography | Why sampled |
|---|---|---|---|
| Cayuse (Compliance Management Suite / Risk & Compliance Suite) | commercial SaaS compliance suite | US higher ed (R1/R2), healthcare, nonprofits | market-leading US compliance suite; enterprise tier documented |
| Kuali Research (compliance modules) | higher-ed platform with modular compliance products | US higher ed, mid-to-large | modular philosophy — each domain a separate product over shared substrate |
| InfoEd (Research Compliance suite) | legacy enterprise eRA suite (30+ years) | US/international universities, corporations | oldest lineage; broadest domain set incl. environmental safety |
| Infonetica (Ethics RM + Research Flow) | international research platform | UK/EU/Canada/Australia universities, healthcare, national orgs | non-US regulatory regime (GDPR/DPIA, trusted research, export controls) |

Rejected/failed samples (recorded, not used):
- Huron Click (Click Compliance) — product page 404 twice; Huron's technology index no longer lists it. Sourcing limitation recorded.
- Key Solutions ResearchManager — site unreachable (522).
- iRIS — vendor could not be identified via available search engines (regional noise).
- SciShield/SciSure — repositioned as lab ELN/LIMS/EHS platform; belongs to the neighboring EHS territory, not the institutional research compliance program. Used only as boundary evidence.

## Sources

Tier 1/2 official vendor surfaces (fetched 2026-09-09):

- Cayuse — Compliance Management: https://www.cayuse.com/products/compliance/
- Cayuse — Risk & Compliance Suite: https://www.cayuse.com/compliance-management/risk-and-compliance-suite/
- Kuali — Research Administration & Compliance overview: https://www.kuali.co/
- Kuali — Conflict Management: https://www.kuali.co/products/conflict-management
- Kuali — Human Ethics Review: https://www.kuali.co/products/human-ethics-review
- Kuali — Export Control: https://www.kuali.co/products/export-control
- InfoEd Global — Research Compliance: https://www.infoedglobal.com/products/research-compliance/
- Infonetica — platform overview: https://www.infonetica.net/
- Infonetica — Ethics RM: https://www.infonetica.net/solutions/ethics-rm

Unreachable / not used:
- https://www.huronconsultinggroup.com/technology/click-compliance (404), https://www.huronconsultinggroup.com/click (404)
- https://researchmanager.com/ (522)
- Vendor help-center-level operational documentation (exact form fields, exact state names, exact deadlines) was not fetched in this pass; evidence is product-page and module-page level. Assertion strength calibrated accordingly (no precise numeric limits, deadlines, or state names claimed in the final document).

## Product Observations

### Cayuse (Compliance Management Suite / Risk & Compliance Suite)

Evidence layer: A (directly observed on official product pages).

- Positioning: "Research Compliance Software… helps higher education, healthcare, and nonprofit institutions adhere to changing regulations, expedite protocol submissions and reviews, and ensure ethical conduct."
- Domain modules: IRB (Human Ethics), IACUC (Animal Oversight), IBC (Hazard Safety), COI (Outside Interests); enterprise "Risk & Compliance Suite" covers "COI, IRB, IACUC, and IBC management".
- Cross-domain data linking: "Data linking between IRB, IACUC, IBC, COI, and Sponsored Projects ensures easy information access and congruency between protocols, disclosures, and funded projects."
- Submission machinery: "smart forms that guide users through complex regulatory requirements", "automated research workflows", "automated notifications", "expedited reviews".
- Review machinery: "automated handoffs and system alerts notify board and committee members as soon as a submission is ready for their review"; enterprise: "built-in support for multi-level ancillary reviews and routing"; IBC: "streamline protocol management, IBC meetings, and reporting"; COI: "streamlined committee collaboration and decision-making", "automated multi-level reviews".
- Determination outcomes: "approvals received sooner than with manual handoffs"; COI "standardized management plans that accelerate resolution".
- Record/evidence: "Stay audit-ready with a single platform for research compliance data and records; transparent review histories and role-based dashboards simplify reporting and inspections"; "21 CFR Part 11 compliant" (repeated per module); "comprehensive audit trails and real-time reporting simplify AAALAC site visits and USDA inspections" (IACUC); IRB: "Simplify accreditation and audit readiness with AAHRPP reporting".
- Multi-site/multi-institution: "Seamlessly manage multi-site studies and Single IRB (sIRB) submissions"; "support for ancillary reviews, single IRBs, reliance agreements, and CTMS integrations".
- Training: "Integrated CITI tracking ensures essential up-to-date researcher training"; "Ensure consistent, up-to-date training compliance across all stakeholders" (IACUC/IBC).
- Regulatory monitoring: "industry experts constantly monitor regulatory bodies and standards — including HIPAA, GDPR, NIH, AAALAC, USDA, and CDC — to ensure any changes are reflected in Cayuse's workflows, libraries, flags, and forms."
- Integrations: HR, LMS, CTMS, ERP; "flexible APIs".
- Analytics: "Compliance Management Insights provides role-based dashboards for accessing, visualizing, and analyzing up-to-date compliance data to help PIs and leadership make data-driven decisions."
- Users: "academic institutions, healthcare organizations, and research nonprofits"; roles named in testimonials: Assistant VP for Academic Research and Regulatory Compliance, Director of Research and Compliance, Research Facilitator.

### Kuali Research (compliance modules)

Evidence layer: A (directly observed on official product pages).

- Suite framing: "Research Administration & Compliance… flexible, reliable enterprise research administration & compliance product suite." Compliance modules listed: Conflict Management, Export Control, Human Ethics Review, Animal Ethics Review, Biosafety Review, GrantRisk.
- Conflict Management data types ("What's in the box"): COI Disclosures ("financial interests, outside professional activities, project sponsors, types of research, and completed training"), COC Disclosures (conflict of commitment), Outside Entities ("Manage outside entities in a single place"), Management Plans ("Create, review and track management plans to ensure compliance"), Meetings ("Manage COI/COC committee meetings and meeting agendas").
- Human Ethics Review data types: Protocol/Application Submissions ("Collect, review, approve, and monitor research protocols to assess the risks and benefits of research involving the rights and welfare of human research participants"), Protocol Renewal & Closeout, Meetings (IRB committee meetings/agendas), Reportable Events ("adverse events that occur during the course of a study"), IRB Reviews/Checklists, NHSR & 118 Determinations (non-human-subjects research determinations).
- Export Control data types: Projects ("export-controlled projects… built-in checklists help researchers understand what they need to disclose"), Technology Control Plans ("Create, review and approve technology control plans. Conduct ongoing monitoring"), Events ("international shipping, licenses, purchases, and more"), Review Checklist.
- Configurability: "Our intuitive Form Designer and powerful Workflow Builder allow you to configure and maintain the software independently. Modify the data types below and even create additional data types"; "Flexible, configurable forms and workflow make it easy to adapt when regulations change"; "dynamic, multi-branched workflows".
- Shared substrate: "Shared configuration makes it easy to keep track of outside entity, training and person data" (Conflict Management); "sponsor, training & person data" (Human Ethics/Export Control); "Link protocol data to proposals, awards, disclosures, other ethics reviews, and more, for a comprehensive view."
- Roles/access: "Sophisticated Group and Role Management gives you fine-grained control over access"; "Easy to use interface ensures that PIs and administrators understand how to stay compliant."
- Triage/review: "Tame the triage and review process with flexible, powerful workflow that matches your process, and convenient committee management tools."
- Reporting: "Dashboard and reporting capabilities provide quick access to your data"; "Document dashboard and clear status information provides transparency and visibility of data to key stakeholders."
- Extensibility: add-on forms/workflows (training certification, travel approval, foreign entity approval, etc.).

### InfoEd (Research Compliance suite)

Evidence layer: A (directly observed on official product pages).

- Positioning: "Research Compliance Software… easily managing compliance with federal, state and institutional governing bodies, as well as the facilitation of timely and accurate approvals from the appropriate committees and institutional governing bodies."
- Domain modules: Human Studies IRB/Ethics, Animal Studies IACUC, Environmental Safety (radiation safety, biological agents, hazardous chemicals, genome studies/rDNA), Conflict of Interest, Export Controls.
- Cross-domain linking: "Animal (IACUC/EC), Human (IRB/EC), and Environmental Safety protocols are linked – reduces duplicated effort"; "data integrations between Grants, Compliance and COI records" (customer quote); "Institutions can model the interwoven relationships between conflict of interest management and the approval of research funding, research protocols and contracts."
- Submission machinery: "Investigators create their own submissions and route them electronically"; eForms with mandatory questions/uploads; templates reused; "Simple version control accelerates approvals"; "Easily clone safety plan amendments"; "compare and contrast a new submission against currently approved versions."
- Review machinery: "Compliance workflow supports multiple reviews and levels of oversight for each submission, from intake to full committee review"; "All aspects of committee and meeting management can be handled within the system, from agenda generation to distribution of meeting minutes and notifications to investigators"; "Reviewer comments are captured electronically, forming the basis for meeting minutes and related correspondence"; committees "Evaluate the risk-benefit ratio of research and document rationale for approval."
- Administrator machinery: "A single system with protocol tracing, conditional alerts, reporting, and electronic letters"; "Workflow Manager allows immediate view of status of all safety plans"; "Automated monitoring of renewal dates"; "Automatically generates communications."
- COI machinery: "Electronically disclose statements of external interests"; "Automatically triage submissions for review based on the responses provided"; "Create management plans that are referenced appropriately against the relevant disclosure and research activities"; "Track ongoing review to ensure compliance with management plans"; contact management for "relationships with external organizations across research efforts."
- Training: "Tracks personnel development programs to ensure compliance with institutional training requirements."
- Events/audits (Environmental Safety Management): "Track and manage Incident Reports"; "Track current audits and past audit history."
- Stakeholder views: "Researchers And Principal Investigators / Research Administrators / Committees And Reviewers — individual, customized stakeholder views."
- Document storage: "All administrative and protocol actions support document storage… electronic versions of committee review, communications, management plans."
- Profiles: GENIUS faculty profile data shared into COI and other modules.

### Infonetica (Ethics RM + Research Flow)

Evidence layer: A (directly observed on official product pages).

- Platform framing: "All research related workflows, data and documents in one Integrated Platform" — Research Flow spans Pre-award, Ethics RM, Contracts, DPIA (data protection impact assessment), Export Controls, Due Diligence, ReDA (clinical trials), Post-award.
- Ethics RM positioning: "research ethics compliance management software"; three-stage framing: Apply (researchers craft application "following a clear and guided workflow") → Approve ("Ethics committees and administrators efficiently review submissions using digital tools") → Administer ("Administrators configure the system to their institutions, and optimise it through data-driven insights").
- Application machinery: "Smart forms and dynamic workflows"; "guided application process together in real-time"; "Collaborate with review and administration teams in-app"; "Submit your application for review in one click"; "Track your journey to approval through status updates."
- Review machinery: "automated application assignment rules"; "Manage all tasks in the application activity dashboard"; "Reviewers and researchers collaborate in real-time"; "Send application responses to all relevant stakeholders"; "Ethics committees gain access to all the tools they need to conduct rigorous yet efficient reviews."
- Administration machinery: "Configure your organisation's digital forms and workflows (no programming required)"; "Set up scheduled or recurring data reports"; "Monitor all of your operations in the application activity dashboard."
- Features: form/workflow templates, "limitless form & workflow reconfigurability", customisable automation rules, automated quality checks, virtual meetings, in-app messaging/commenting, automated routing/assignment, task notifications/reminders, digital signatures, permission-based role system, dashboards, scheduled & recurring reports, version change tracking, GDPR compliance, integrations + API, "complete data visibility and real-time tracking".
- KPIs named: "Time to approval", "Time for review".
- Export Controls module: "Export Compliance Management Software" (UK trusted-research context; case studies at Liverpool/Salford/Kingston about export-controls processes).
- Customers: universities (Manchester, Monash, KCL, Bath, Leicester, Salford, Kingston, Hertfordshire, Stellenbosch, RMIT, Antwerpen), healthcare (NHS Research Scotland, Sunnybrook), national organizations (Clinical Trials Ontario, Research Manitoba, AgResearch).
- Case-study outcomes: Manchester "reduces ethics review time by 50%"; Monash "reduced committee review time by more than 30%".

## Cross-product Comparison

| Structure | Cayuse | Kuali | InfoEd | Infonetica | Layer |
|---|---|---|---|---|---|
| Multi-domain compliance program (≥3 domains) | IRB+IACUC+IBC+COI | COI+Export+Human+Animal+Biosafety(+GrantRisk) | IRB+IACUC+EnvSafety+COI+Export | Ethics+Export+DPIA+DueDiligence(+CTMS) | B |
| Researcher-initiated submission objects (protocols/disclosures/plans) | ✓ smart forms | ✓ protocol/disclosure/project data types | ✓ eForms/templates | ✓ smart forms | B |
| Configurable forms + workflow builder | ✓ configurable workflows | ✓ Form Designer + Workflow Builder | ✓ configurable eForms/routing | ✓ no-programming configuration | B |
| Review-and-determination loop with recorded outcomes | ✓ approvals, multi-level reviews | ✓ review/approve/monitor, determinations | ✓ intake→full committee review, approvals | ✓ apply→approve, status to approval | B |
| Committee machinery (meetings/agendas/minutes/checklists) | ✓ IBC meetings, committee collaboration | ✓ Meetings data type, review checklists | ✓ agenda/minutes automation, reviewer comments | ✓ virtual meetings, assignment rules | B |
| Post-approval life (renewals/amendments/reportable events/closeout) | ✓ renewals (IBC), ongoing oversight | ✓ Renewal & Closeout, Reportable Events | ✓ renewal-date monitoring, amendments, incident reports | ✓ version tracking, ongoing monitoring (TCPs) | B |
| Shared person/training/entity substrate across domains | ✓ data linking across modules | ✓ shared person/training/entity config | ✓ linked protocols, GENIUS profiles, contact mgmt | ✓ one integrated platform | B |
| Training tracking | ✓ CITI integration | ✓ training data + add-on | ✓ personnel development programs | not evidenced on fetched pages | B (3/4) |
| Audit-ready records / reporting to oversight parties | ✓ audit trails, AAHRPP/AAALAC/USDA framing | ✓ dashboards/reports | ✓ audit history, document storage | ✓ version tracking, scheduled reports | B |
| Linked research context (proposals/awards/contracts) | ✓ Sponsored Projects linking | ✓ proposals/awards linking | ✓ grants/contracts modeling | ✓ Research Flow platform | B |
| Role-based access (researcher/admin/reviewer/leadership) | ✓ role-based dashboards | ✓ group/role management | ✓ stakeholder views | ✓ permission-based roles | B |
| Multi-site / sIRB / reliance agreements | ✓ (enterprise tier) | not evidenced | not evidenced | not evidenced | A (single-product) |
| Regulatory-regime machinery named | US (NIH/USDA/AAALAC/AAHRPP/HIPAA/21 CFR 11) | US (NHSR/118 determinations) | US federal/state + institutional | UK/EU (GDPR, trusted research) | B (regime = variant) |
| Determination-without-full-review (exempt/NHSR class) | not evidenced on fetched pages | ✓ NHSR & 118 determinations | ✓ auto-triage of disclosures | not evidenced | A/B (partial) |
| Incident/misconduct machinery | not evidenced | reportable events (adverse) | ✓ incident reports (env safety) | not evidenced | A (partial) |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

The Type is held together by three jointly-held structures:

1. **The institution's research-compliance program as the managed system.** The system's organizing frame is the institution's obligations for how research may be conducted — protection of human subjects, animal welfare, conflicts of interest, biosafety/hazardous materials, export control, data protection — held as managed compliance domains. The domain set varies by institution and jurisdiction; the *program frame over multiple obligation domains* does not. Remove → a generic forms/workflow platform.

2. **The compliance submission as the unit of record, entering a review-and-determination loop.** Researcher-initiated records (protocol applications, disclosures, registrations, control plans, determination requests) are created through guided forms, routed through configured review paths — administrative triage, reviewer/committee evaluation — and resolved into recorded determinations (approval, approval with conditions, deferral, denial, or exempt-class determinations). Remove → a policy/document library with nothing to advance.

3. **The audit-ready compliance record.** Submissions, determinations, conditions, events, training, and correspondence are retained as the institution's evidence of compliance — the record regulators, auditors, accreditors, and institutional leadership are served from. Remove → an ephemeral review tool; the "management" is gone.

Jointly-held load-bearing analysis:
- 1 alone = generic workflow/forms platform
- 2 without 1 = generic submission-review workflow tool
- 3 without 1+2 = records archive
- 1+2 without 3 = review tool with no institutional memory
- 1+3 without 2 = compliance document library with no operational loop
- 2+3 without 1 = single-purpose review system → collapses toward the IRB / IACUC leaf territory

### L1 — Common Mature Structure

- Committee machinery: meeting management, agendas, minutes, reviewer assignment, review checklists, reviewer comments, digital signatures.
- Institution-configurable forms and workflows (form builders, workflow designers, automation rules) — the mechanism by which institutional policy and changing regulations are encoded.
- Shared compliance substrate: person records, training/certification records, and external-entity records reused across all domains; research context (proposals, awards, contracts, other protocols) linked into compliance records.
- Training tracking (e.g., external training-provider integrations), often gating participation.
- Post-approval lifecycle: renewals/continuing review, amendments/modifications, reportable events/incidents, closeout.
- Determination machinery beyond full committee review: exempt/not-human-subjects determinations, automatic triage of disclosures.
- Dashboards, KPIs (e.g., time-to-approval), scheduled/recurring reports, role-based access, notifications/reminders.
- Multi-level/ancillary reviews and multi-site support at the enterprise tier.

### L2 — Variant / Optional Structure

- Domain set (which regimes the institution runs — driven by jurisdiction and institutional portfolio).
- Regulatory-regime machinery: US federal-grantee regime (Common Rule-class human-subjects rules, FCOI rules, animal welfare oversight, AAHRPP/AAALAC accreditation, USDA inspections, 21 CFR Part 11 support) vs UK/EU regime (GDPR/DPIA, trusted research, export controls) vs national-organization regimes.
- Suite packaging: standalone compliance suite vs compliance modules inside a wider research-administration platform.
- Deployment: SaaS vs on-premises; regulated-record support (Part 11-class).
- Depth of incident/misconduct handling.
- Integration breadth: HR/LMS/CTMS/ERP.

### L3 — Vendor-specific (Research Notes only)

- Cayuse module names (Human Ethics, Animal Oversight, Hazard Safety, Outside Interests, Compliance Management Insights), Vivarium Management, ROI claims (45% faster protocol lifecycles, 60% admin reduction, 10+ hours saved per protocol, 35%/40% figures).
- Kuali GrantRisk; "What's in the box" data-type packaging; add-on form examples.
- InfoEd GENIUS (faculty profiles), SPIN (funding opportunities), eRAI; "less is more" framing.
- Infonetica ReDA, Open Flow, Due Diligence module; specific case-study percentages (50%, 30%).
- Huron Click — unreachable; no claims made.

## Rejected Findings (anti-overfitting)

- **"Compliance suite = IRB + IACUC + IBC + COI" as a fixed domain set.** Rejected: the domain set varies (Kuali adds Export Control and GrantRisk; Infonetica adds DPIA and Due Diligence; InfoEd adds Environmental Safety). The invariant is the program frame over the institution's obligation domains, not any specific domain list.
- **Committee/meeting machinery as definitional.** Rejected: determinations can be made by administrators (expedited review, disclosure triage, NHSR-class determinations); committee machinery is the dominant realization, not the invariant.
- **Training tracking as definitional.** Rejected: 3/4 sampled products document it; the paper-era office used certificate files; it is common mature structure.
- **Configurability as definitional.** Rejected: a hard-coded compliance system would still be recognizable; configurability is how mature products encode varying institutional processes.
- **US regulatory regime as definitional.** Rejected: Infonetica's UK/EU regime and national-organization customers satisfy the same core with different machinery.
- **"Audit trail" as a literal named feature.** Calibrated: the *retained compliance record* is the invariant; audit-trail machinery is documented explicitly at two products and implied by version tracking/reporting at the others.
- **SciShield/SciSure as a sample.** Rejected: repositioned as lab ELN/LIMS/EHS — neighboring territory (lab safety operations), used only as boundary evidence.

## Boundary Findings

1. **vs IRB / Research Ethics Management.** The IRB leaf is the single-domain machinery for human-subjects protocol review. This leaf is the institution's multi-domain compliance program. Suite products bundle the IRB domain as a module (Cayuse IRB, Kuali Human Ethics Review, InfoEd Human Studies). Test: remove all domains but human subjects → the product is an IRB system (other leaf). Keep both leaves; the seam is program-vs-domain.
2. **vs Animal Research Ethics / IACUC Platform.** Same pattern as (1) for the animal domain.
3. **vs Research Administration Platform.** Research administration centers on the funding lifecycle (proposals, awards, compliance-with-terms); this Type centers on the institution's conduct obligations (protocols, disclosures, determinations). Products integrate deeply (data linking both ways) and are often sold as one suite — packaging, not identity.
4. **vs Compliance Management Platform (§11) / GRC.** Generic corporate compliance centers on policies, controls, risk, audits across business domains; research compliance centers on researcher-facing submission/review machinery over research-specific regulatory regimes. A GRC platform does not run IRB/IACUC protocol lifecycles; a research compliance system does not run enterprise control testing.
5. **vs EHS / lab safety (SciShield/SciSure pole).** Lab safety operations (chemical inventory, inspections, SDS) are facility/EHS territory; biosafety protocol review (IBC-class) sits inside the research compliance program. Adjacent, sometimes bundled.
6. **vs eRegulatory / clinical-trial site regulatory tools.** Clinical-site regulatory binders serve study-site regulatory readiness for trials; different unit of record (study regulatory documents vs institutional compliance submissions).
7. **vs Research Data Management / Privacy.** DPIA modules (Infonetica) bring data-protection assessment into the compliance program; the RDM leaf centers on data stewardship/planning, not determination loops.

## Uncertainties

- Misconduct/research-integrity case machinery: not directly evidenced on fetched pages for any sampled product (InfoEd documents incident reports for environmental safety; Kuali documents reportable adverse events). Whether misconduct case management is a standard domain of this Type is unverified — not claimed either way.
- Single-domain deployments: institutions likely buy individual modules (e.g., only Human Ethics Review); not directly evidenced. If common, the market realization includes "compliance program system deployed one domain at a time" — recorded as uncertainty, does not change the L0.
- Exact lifecycle state names, form fields, deadlines, and review-path specifics: not fetched (help-center level); no precise values claimed.
- Huron Click (major US product) unreachable — the US enterprise pole is represented by Cayuse only.
- Whether external/commercial IRB platforms (Advarra/WCG class) belong to this Type or to the IRB leaf: not researched in this pass; tentatively assigned to the IRB/Research Ethics territory (external-review posture), flagged for that leaf's pass.

## Historical / Market-Sample Check

- Paper-era research compliance office: protocol files, committee minute books, disclosure forms, training-certificate files, approval letters, inspection/audit files — satisfies all three L0 legs (obligations frame, submission→review→determination, retained evidence) with no software.
- 1990s–2000s eRA compliance modules (InfoEd's 30-year lineage) satisfy without SaaS, form builders, or AI.
- The definition names no specific regulation, no SaaS delivery, no committee-software specifics, no US-only regime. Regional regimes (US/UK/EU/national) and era machinery are held as variants.

## Final Synthesis

Research Compliance Management is the research institution's compliance-program system of record. Its defining core is three jointly-held structures: (1) the institution's research-conduct obligations held as managed compliance domains (human subjects, animal welfare, conflicts of interest, biosafety, export control, data protection — set varies by institution and jurisdiction); (2) the compliance submission as the unit of record — researcher-initiated protocols, disclosures, registrations, and plans that enter a configured review-and-determination loop resolved by compliance staff and committees into recorded determinations; (3) the audit-ready compliance record — determinations, conditions, events, training, and correspondence retained as the institution's evidence of compliance for regulators, auditors, accreditors, and leadership. Mature products add committee machinery, configurable forms/workflows, a shared person/training/entity substrate, training tracking, post-approval lifecycle handling, and cross-linked research context. The Type is distinct from single-domain IRB/IACUC systems (program vs domain), from research administration (obligations vs funding), and from generic corporate compliance/GRC (researcher-facing submission-review machinery over research-specific regimes vs enterprise controls).
