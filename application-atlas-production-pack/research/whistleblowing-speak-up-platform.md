# Research Notes — Whistleblowing / Speak-up Platform

## Research Goal

Understand what "Whistleblowing / Speak-up Platform" software actually is as an Application Type: what its central objects are, how a report moves through the system, how reporter protection is implemented, who uses it on both sides, what rules govern it, and where its boundaries lie against the neighboring Types in §11 and adjacent sections — especially the three sibling Types that share the same market bundle (corporate investigation management, ethics & conduct management, employee relations case management) and complaint & escalation management.

Pre-hung flags this pass must discharge (from earlier passes):

- research/employee-relations-case-management.md: "employee-relations-case-management vs whistleblowing-speak-up-platform / corporate-investigation-management: sampled products bundle anonymous-reporting/hotline intake with case handling (intake auto-converts to cases)... flagged for joint review when those leaves are processed."
- STATUS.md Boundary Issues: "corporate-investigation-management (§11, processed 2026-09-07) — DISCHARGES the employee-relations pass's flag from that side: whistleblowing-speak-up-platform (intake channel + reporter protection) vs corporate-investigation-management (handled case lifecycle) vs employee-relations-case-management (HR-owned slice) are three distinct Types over one bundled market pattern."
- research/ethics-conduct-management.md: "speak-up products center on the reporting channel + report record + reporter protection + case handling... Test: remove disclosure/attestation/register machinery and keep the channel → whistleblowing platform."
- STATUS.md Boundary Issues: "complaint-escalation-management (§07, processed) vs whistleblowing-speak-up-platform (§11 sibling, unprocessed): reporter-population seam (external customer/consumer vs internal employee)... recommend joint review when the sibling is processed."

## Initial Boundary (hypothesis before research)

- What: an organization-provided, protected reporting infrastructure through which people (employees and often external stakeholders) report suspected wrongdoing, independent of line management.
- Users: reporters (any employee, often also suppliers/customers/students/residents), compliance/ethics officers, designated report recipients, hotline operators.
- Nearest neighbors: corporate investigation management (handled case), ethics & conduct management (self-disclosure + attestation), employee relations case management (HR slice), complaint & escalation management (external customer), employee survey platform, policy management, HR compliance management.
- Boundary hypothesis: this Type owns the *channel + report record + reporter protection + follow-up loop*; the handled case lifecycle belongs to corporate investigation management.
- Unknowns: how much case handling lives inside speak-up products; how anonymity is actually implemented; whether the feedback loop is definitional or merely common; how regulation shapes the core.

## Research Questions

1. What is the report object? What does intake capture? What states does a report move through?
2. How do intake channels work (web portal, phone hotline, mobile app, embedded form)? Who can use them?
3. How is reporter protection implemented — anonymity vs confidentiality, access restriction, exclusion of the reported-about party?
4. Does a protected follow-up loop exist (reporter acknowledgment, status, two-way Q&A)? Is it definitional or optional?
5. How much case handling (triage, workflow, investigation) lives in these products vs in the investigation sibling?
6. What regulatory machinery exists (EU Whistleblowing Directive, SOX, national laws, timelines, data residency, languages)?
7. What interfaces exist on each side (reporter-facing, recipient-facing, program oversight)?
8. Where exactly are the boundaries vs corporate investigation management, ethics & conduct management, employee relations case management, and complaint & escalation management?

## Representative Products

| Product | Pole | Why selected | Evidence tier |
|---|---|---|---|
| NAVEX (Whistleblowing & Incident Management: EthicsPoint Essentials / WhistleB / Professional) | US enterprise, hotline-lineage, GRC suite with a three-tier ladder | Market leader; the definitional product page states the category's own definition; hotline heritage | Tier 2 (official product pages) |
| Vault Platform (now part of Diligent) | Modern, employee-first, mobile-app-native speak-up | Different philosophy (Active Integrity, app-first, group reporting); UK origin | Tier 2 (official product pages) |
| Whispli | EU-directive-native, security/sovereignty-led | Explicit anonymization mechanics described in FAQ; voice-AI hotline; data-residency choice | Tier 2 (official site + FAQ) |
| SpeakUp (People Intouch heritage, Amsterdam) | EU heritage (20+ years), dialog/checkback-led, separate reporting vs disclosures products | Literally named for the behavior; explicit "checkback rate" evidence for the follow-up loop; SMB+enterprise spread | Tier 2 (official site + FAQ) |

Selection notes: EQS Group (Integrity Line) was considered as a fifth (EU compliance-suite pole) but its solution URLs returned 404 twice — abandoned per network rules; the EU pole is covered by Whispli and SpeakUp instead. No Tier-1 help-center articles were reached for any sample (login-gated or not fetched); official product/marketing/FAQ pages carry the evidence, so operational specifics are kept general.

## Sources

- NAVEX — "Whistleblowing Software & Solutions" (category definition, tier ladder, channels, compliance framing): https://www.navex.com/en-us/platform/whistleblowing-software-solutions/
- NAVEX — "EthicsPoint Essentials" (hotline pole: 24/7 web+phone intake, anonymity, prebuilt workflows, SOX/EU Directive): https://www.navex.com/en-us/platform/whistleblowing-software-solutions/ethicspoint-essentials/
- Vault Platform — root/product pages (Active Integrity, reporting channels, Resolution Hub, Integrity Insights, use cases): https://www.vaultplatform.com/
- Whispli — root + FAQ (safe intake, Safe Inbox anonymization, protected two-way communication, case management, residency): https://www.whispli.com/
- SpeakUp — root + FAQ (anonymous reports vs self-disclosures, multi-device intake, checkback/dialog evidence, case management, EU Directive): https://www.speakup.com/

Research date: 2026-09-08.

## Product A — NAVEX (EthicsPoint family)

### Key observations (evidence layer A unless noted)

- Category self-definition (vendor's own words, useful as market framing): "Whistleblowing software is a secure system organizations use to receive, document and manage reports of misconduct or compliance concerns. It typically combines reporting channels with structured case records so disclosures are handled consistently and defensibly."
- Three-tier ladder: Essentials (fast-start hotline: "secure web and phone reporting", straightforward case management), WhistleB (EU compliance: "GDPR-first architecture with European hosting", "guided case management workflows and secure reporter communication"), Professional (enterprise: AI-assisted investigations, configurable workflows, advanced analytics, implicated-party screening).
- Intake: "Capture reports securely through web, mobile and phone channels"; "24/7 web and phone access for employees and external partners"; multilingual reporting for employees and third parties.
- Anonymity: "Enable anonymous submissions to maximize potential concerns reported"; "Protect reporter confidentiality through anonymous, secure web and phone channel."
- Report handling: prebuilt categories and guided workflows; "Track actions and updates with a complete, auditable case history"; standardized documentation "so similar cases follow the same fair process"; exportable audit-ready records.
- Oversight: central dashboard of open/closed cases; categories/questionnaires for consistency; share securely with HR/legal/compliance; export for audits.
- Regulatory framing: EU Whistleblowing Directive, SOX, Sapin II, DOJ guidance; "Align report intake flows with local expectations and regulatory timelines."
- Vendor marketing stats (do not generalize): 40% anonymous reporting rate median with 4+ integrated modules vs 58% intake-only; 6.9% fewer material lawsuits etc.

## Product B — Vault Platform

### Key observations

- Positioning: "Active Integrity platform" with three named parts: Reporting channels, Resolution Hub, Integrity Insights.
- Channels: "secure mobile app and Open Reporting solution"; VaultTalk (phone intake); "report misconduct from the privacy of our secure mobile app... either as an anonymous individual or in the safety of numbers with GoTogether®" (group reporting — vendor-specific concept).
- Resolution Hub: "Create clear lines of communication with the reporter. Investigate and quickly manage cases through to resolution, with cross-department collaboration. All in one place."
- Analytics: "See warning signs from a distance and identify patterns before they become scandals... across teams, departments and even continents."
- Use cases: fraud, discrimination, harassment & bullying, bribery & corruption, ESG violations, personal safety.
- Audiences: solutions for employees, HR, legal, compliance, CEOs; EU Whistleblowing Toolkit resource.
- Now part of Diligent (May 2025); demo flows to Diligent "Speak Up" product.

## Product C — Whispli

### Key observations

- Positioning: "the whistleblowing platform for security-conscious organizations"; "Intelligently manage the entire lifecycle of anonymous and non-anonymous disclosures with enterprise-grade case management designed for global teams."
- Intake: "secure, anonymous intake channels for employees to raise misconduct concerns across 70+ languages with protected two-way communication"; "Web, mobile and voice channels options"; Whispli Voice AI (AI-powered voice hotline, transcription, "strong anonymity protections").
- Anonymity implementation (vendor-specific, unusually explicit): "Whispli provides anonymity by design through our proprietary Safe Inbox. We do not collect IP addresses, device identifiers, or metadata. Reporters are represented only by unique pictograms."
- Follow-up loop: "Notifications and follow-ups through a safe inbox"; "protected two-way communication."
- Case handling: "triage reports, automate investigations and ensure consistent resolution"; configurable workflows; AI-assisted transcription and triage; "Secure collaboration with internal and external case managers."
- Governance: "Immutable audit trails with permanent decision logging"; "Board-ready reporting with real-time trend monitoring"; "Custom permissions and roles."
- Separation of anonymous vs non-anonymous intake: a dedicated non-anonymous disclosure module (Conflicts of Interest, Gifts & Hospitality) is packaged separately from the anonymous whistleblowing core — corroborates the ethics-sibling seam.
- Regulatory framing: EU Whistleblowing Directive (+ national transpositions incl. French Waserman/Sapin II), SOX, Australia, China, etc.; "anti-retaliation safeguards, confidential case handling"; data-residency choice (EU/US/UK/UAE/AU/Asia; sovereign cloud).
- Extended populations: industry pages include patients/residents/students/families (healthcare, aged care, education) and supply-chain grievance mechanism use case.

## Product D — SpeakUp

### Key observations

- Positioning: "Trusted reporting and disclosures. Centralized ethics & compliance management." Products split: SpeakUp Report ("Misconduct reporting & case management") vs SpeakUp Paths ("Disclosure & approval management" — COI, gifts, donations) — the anonymous/non-anonymous split as product packaging.
- Intake: "Empower employees (and other stakeholders) to easily submit anonymous reports or self-disclosures without barriers. With 24/7 multi-device access, foster trust through interactive engagement and ensure effective resolution." "100+ languages across web, phone, and app reporting."
- Follow-up loop (strongest evidence in sample): "Checkback rate 20%" headline; FAQ: "the highest reporter check-back rates in the industry (49% average)"; customer case: "2 - 3 conversations on SpeakUp before personal contact was established"; "Driving better outcomes by engaging in dialog."
- Case handling: "Manage all issues, collaborate with other key stakeholders, and resolve cases all within SpeakUp's centralized Case Management System"; customizable intake forms, workflows, routing rules configured by compliance teams themselves.
- Anonymity: customer quote — "The option to remain anonymous makes a real difference... it lowers the barrier to speak up" (Whispli) — for SpeakUp specifically: Sinch quote "anonymity significantly lowers the barriers for reporting"; "Confidential reporting" listed as a core feature.
- Regulatory framing: EU Whistleblowing Directive ("meets all confidentiality, security, and reporting requirements under the Directive"), GDPR, German LkSG, NIS2, DORA; ISO 27001/27701, ISAE 3000 Type II audits.
- Heritage: 20+ years operational experience (hotline-service lineage), 750+ organizations, enterprise + SMB.

## Cross-product Comparison

| Dimension | NAVEX | Vault | Whispli | SpeakUp | Evidence |
|---|---|---|---|---|---|
| Standing intake channel, independent of line management | web + phone 24/7 (+mobile) | mobile app + Open Reporting + VaultTalk phone | web + mobile + AI voice hotline | web + phone + app, 24/7 | A→B |
| Open to employees AND third parties/external stakeholders | "employees and external partners", "employees and third parties" | employees; stakeholders (solutions pages) | employees; industry pages add patients/residents/students/families; supply-chain grievance | "employees (and other stakeholders)" | B |
| Subject matter = suspected wrongdoing/misconduct | "reports of misconduct or compliance concerns" | fraud/discrimination/harassment/bribery/ESG/safety use cases | misconduct concerns; modern slavery; health & safety | "Misconduct reporting" | B |
| Report becomes a persistent structured record with case handling | "reporting channels with structured case records"; auditable case history | Resolution Hub cases to resolution | "lifecycle of... disclosures with enterprise-grade case management" | centralized case management | B |
| Anonymity or confidentiality as a first-class reporting posture | "enable anonymous submissions"; "protect reporter confidentiality" | "as an anonymous individual" | anonymous by design (Safe Inbox, no IP/device/metadata, pictograms) | "anonymous reports"; "confidential reporting" | B |
| Protected two-way follow-up loop | "secure reporter communication" (WhistleB); guided handling | "clear lines of communication with the reporter" | "protected two-way communication"; "notifications and follow-ups through a safe inbox" | "interactive engagement"; "checkback rate"; "2-3 conversations before personal contact" | B |
| Case/triage/workflow machinery inside the product | prebuilt + configurable (tier-dependent) | Resolution Hub | triage, workflows, AI triage | customizable workflows/routing | B (shared with investigation sibling) |
| Regulatory alignment as a first-class concern | EU Directive, SOX, Sapin II, DOJ | EU Whistleblowing Toolkit | EU Directive + national laws, SOX, residency | EU Directive, LkSG, NIS2, DORA | B |
| Multilingual intake | built-in translations, multilingual | (implied by global customers) | 70+ languages | 100+ languages | B |
| Program analytics / trend oversight | dashboards, benchmarking | Integrity Insights | board-ready reporting, trends | advanced analytics, Power BI | B |
| Non-anonymous disclosure modules (COI/gifts) sold beside the core | Disclosure Management product | — | Whispli Disclosures module | SpeakUp Paths product | B (sibling-Type territory) |
| Anonymization mechanics detail | not detailed publicly | not detailed | Safe Inbox / pictograms (unique in sample) | not detailed | C (product-specific) |
| Group/collective reporting | — | GoTogether® | — | — | C (product-specific) |
| Voice-AI hotline | phone reporting (human/telephony) | VaultTalk phone | Whispli Voice AI | phone reporting | B (implementation varies) |
| Outsourced operator hotline service | telephony datasheet/partners | — | — | 20yr hotline-service heritage | C (variant) |

## Canonical Model (abstraction)

### L0 — Defining Invariant (deliberately minimal)

A Whistleblowing / Speak-up Platform is the organization's protected speak-up infrastructure. Four jointly-held structures; remove any one and the product is no longer this Type:

1. **Standing protected intake channel** — the organization provisions channel(s) through which any employee (and commonly external stakeholders) can report suspected wrongdoing directly to designated recipients, deliberately bypassing the normal management line. Remove → line-management/HR-direct reporting, i.e., not this Type.
2. **Report of record** — each submission becomes a persistent, individually identified report record carrying the allegation content, intake channel, timestamp and a status that accumulates follow-up history. Remove → a hotline phone number or feedback widget with nothing to manage.
3. **Reporter identity protection** — anonymity or confidentiality enforced as a system property: the reporter's identity is either not collected or restricted to a small designated recipient circle, structurally shielded from the reported-about party and from general internal visibility. Remove → ordinary complaint intake.
4. **Protected follow-up loop** — the reporter can be acknowledged, exchange questions/answers, and receive status/feedback without surrendering the protection posture. Remove → a one-way drop box (the pre-history the Type digitized).

Domain binding: the subject of a report is suspected wrongdoing — misconduct, fraud, harassment, discrimination, corruption, safety violations, legal/policy breaches — within or touching the organization. Remove the binding → customer feedback or employee survey tooling.

Jointly-held load-bearing tests:

- 1 alone = a suggestion phone number / widget
- 2 alone = generic case intake form (Complaint & Escalation territory)
- 3 alone = an anonymity claim with no channel or record
- 4 alone = anonymous messaging (anonymous Q&A apps)
- 1+2 without 3+4 = an internal complaint register (complaint/HR case territory)
- 1+3 without 2+4 = sealed suggestion box (correctly the analog pre-history)
- 2+3 without 1+4 = confidential archive with no live channel
- 1+4 without 2+3 = ephemeral anonymous messaging with no record or program

### Historical / market-sample check (§24 logic)

- Telephone ethics hotline era (1990s–2000s, before platform software): toll-free number (channel bypassing line management) + operator-taken, logged reports (report record) + anonymity by default (protection) + reference number for call-back status/questions (protected loop). Satisfies all four legs — the modern Type digitizes and hardens this shape; nothing in L0 depends on web forms, apps, the EU Directive, or cloud.
- EU-directive-era pure speak-up tools: satisfy without GRC suites.
- Sealed suggestion box: no record management, no managed loop → correctly fails two legs; it is the pre-history.
- Definition does NOT over-fit to: phone hotlines only (NAVEX heritage), mobile apps only (Vault pole), EU directive compliance only (Whispli/SpeakUp pole), or AI features.

### L1 — Common Mature Structure (cross-product commonality, not definitional)

- Multi-channel breadth (web + phone + mobile at minimum)
- Multilingual intake (dozens of languages)
- Intake forms configured by the organization (categories, guided questions)
- Case management: triage, assignment, workflow states, collaboration between compliance/HR/legal
- Two-way anonymous messaging implemented via a reporter "safe inbox" / access-code pattern
- Audit trails and exportable, audit-ready records
- Role-gated, restricted access; permissions for different teams
- Program dashboards and trend analytics; board-ready reporting
- Regulatory-alignment machinery (EU Directive, SOX, national laws; acknowledgement/feedback timelines)
- Security posture as a selling axis: ISO 27001/SOC 2, encryption, hosting/residency choice

### L2 — Variant / Optional Structure

- Regulatory regime as tuning: EU-directive jurisdictions (anonymity, deadlines, data protection) vs US (SOX hotline heritage, DOJ program guidance) vs Australia/other national regimes
- Outsourced hotline-operation services (vendor-staffed call centers) vs self-operated software
- Extended reporter populations: supply-chain grievance mechanisms, students/residents/patients, communities (modern slavery, CSDDD-style grievance use cases)
- Non-anonymous disclosure modules (COI, gifts & hospitality) — sibling-Type capability commonly bundled
- Adjacent suite modules: training, policy management, third-party screening, pulse surveys
- AI assistance: transcription, triage, summaries, translation
- Group/collective reporting; voice-AI hotlines; anonymous-access mobile apps; benchmarking data programs

### L3 — Vendor-specific (research notes only)

- Whispli Safe Inbox: no IP/device/metadata collection; reporters represented by pictograms
- Vault GoTogether® group reporting; "Active Integrity" framing; acquisition by Diligent (2025)
- NAVEX three-tier ladder (Essentials / WhistleB / Professional), implicated-party screening, benchmark stats (40%/58% anonymous-reporting rates, ROI claims)
- SpeakUp "checkback rate" metrics (20% / 49% claims), Sienna AI branding, ISAE 3000 quarterly audit cadence
- Whispli Voice AI transcription hotline

## Vendor-specific Findings

See L3 above. None of these may enter the canonical document beyond the "Representative Products" anchors.

## Boundary Findings

1. **vs Corporate Investigation Management (§11 sibling — DISCHARGES this pass's half of the employee-relations flag, consistent with that pass's own discharge)**: the seam is the object. This Type centers the *report* — the protected channel, the report record, reporter protection, and the follow-up loop. The sibling centers the *handled case lifecycle* — fact-finding, interviews, findings, recorded determinations. In-market the two are bundled (all four samples include case management; intake commonly converts to a case), but the removal tests hold: strip the case-handling lifecycle and a speak-up platform remains (NAVEX Essentials is packaged as intake + simple case management; a pure intake product is still this Type); strip the channel/anonymity machinery and investigation management remains (HR Acuity direct intake; Case IQ sold standalone per that pass). Keep both Types.
2. **vs Ethics & Conduct Management (§11 sibling, processed)**: this Type captures reports *about others'* suspected wrongdoing through a protected channel; that Type captures *self-disclosed* conduct situations (COI, gifts) plus attestations and program registers. Proof of seam from that pass (LRN has no hotline; Vault has no COI/attestation machinery) reconfirmed here from the other side: Whispli and SpeakUp both package non-anonymous disclosure modules (COI/gifts) as *separate* products beside their anonymous reporting core — the anonymous reporting core is this Type; the disclosure modules are that Type.
3. **vs Employee Relations Case Management (§09 sibling, processed)**: the HR-owned grievance slice. The anonymous/hotline intake machinery belongs to this Type; ER case handling belongs there. Multi-department engines (Case IQ, NAVEX, Vault) share one case spine across both, which is the bundle pattern, not a Type merge. Flag discharged.
4. **vs Complaint & Escalation Management (§07 sibling, processed — DISCHARGES its pre-hung joint-review flag)**: the seam is reporter population + subject matter. Complaint management centers *external customers/consumers* reporting service/product problems for service recovery; this Type centers *employees and other insiders/stakeholders* reporting suspected wrongdoing with identity protection at stake. Case IQ straddles (one case spine serving hotline "internal complaints" and customer complaints per that pass's finding) — a bundle seam, not a Type merge. Anonymous-reporting machinery and retaliation-sensitivity are native here and foreign there.
5. **vs Employee Survey / Engagement Platform**: surveys sample opinion; no wrongdoing subject matter, no report of record, no case consequence, no protection posture. Clear.
6. **vs Policy Management / HR Compliance Management**: adjacent program machinery (policy corpus, obligations, training), commonly bundled in GRC suites; no protected channel at the center. Clear.
7. **"Grievance mechanism" naming (supply chain / CSDDD context)**: Whispli and SpeakUp extend the same core to external supply-chain or community reporters. Treated as a population variant of this Type (same four legs, external reporters), not a separate Type.

## Uncertainties

- No Tier-1 help-center articles reached for any sample (login-gated or not fetched); all evidence is Tier-2 official product/marketing/FAQ pages. Operational specifics (exact acknowledgement/feedback deadlines, retention periods, exact state names, encryption modes) are therefore NOT asserted; the EU Directive's timeline requirements are only reflected as "regulatory timelines" framing, not precise numbers.
- Anonymity mechanics verified in explicit detail only for Whispli (Safe Inbox/pictograms); the other samples assert anonymity/confidentiality without publishing mechanics — the canonical document therefore states the protection posture conceptually (identity not collected or restricted to a recipient circle) without claiming a specific technical implementation.
- The outsourced-operator hotline variant (vendor-staffed call centers taking reports into the system) is evidenced indirectly (NAVEX telephony datasheet reference, SpeakUp's 20-year hotline-service heritage) but no operator-side product page was fetched; held as a variant at moderate confidence.
- Reporter-side follow-up UX (access-code vs account-less link vs in-app session) varies and was not directly observed; the document describes the loop, not its mechanics.
- EQS Group (Integrity Line) unreachable (404 ×2) — the EU compliance-suite pole is covered indirectly via Whispli/SpeakUp; a future pass could add it without changing the model.

## Final Synthesis

A Whistleblowing / Speak-up Platform is the organization's protected speak-up infrastructure: it provisions standing intake channels that deliberately bypass the line-management path, turns each submission into a persistent report of record, enforces reporter identity protection as a system property (anonymous or confidential-to-a-recipient-circle, shielded from the reported-about party), and runs a protected follow-up loop in which the reporter can be acknowledged, converse, and receive feedback without giving up that protection. Around this core, mature products add multilingual multi-channel intake, organization-configured intake forms, case management and triage (the seam shared with the investigation sibling), audit trails, role-gated access, program analytics, regulatory-alignment machinery and hardened security. The market realizes one Type across poles: the US hotline-lineage enterprise suite (NAVEX), the modern app-native employee-first platform (Vault, now Diligent), the EU security/sovereignty platform (Whispli), and the EU heritage dialog-led platform (SpeakUp). The handled investigation belongs to Corporate Investigation Management; self-disclosures and attestations belong to Ethics & Conduct Management; HR grievances belong to Employee Relations Case Management; external-customer service complaints belong to Complaint & Escalation Management.
