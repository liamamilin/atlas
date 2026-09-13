# Research Notes — Law Enforcement Case Management

## Research Goal

Understand what "Law Enforcement Case Management" software actually is, as distinct from the neighboring public-safety types (Police Records Management System, Evidence Management System, CAD, Prosecutor Case Management, Court Case Management System) and from corporate/HR case management. Derive the smallest defining core, the standard mature capability set, and the variant space, from real product documentation.

## Initial Boundary

Working hypothesis at start:

- The Type is the **investigative case system of record**: what detectives/investigators use to run an investigation — cases built from reports/tips/referrals, persons and entities linked with roles, leads/tasks worked, supplemental documentation, supervisory review, and a recorded outcome (clearance, closure, prosecution referral).
- Nearest neighbors: Police Records Management System (report/incident/arrest records), Evidence Management System (item custody), CAD (real-time response dispatch), Prosecutor Case Management (prosecution phase), Court Case Management (court phase), Corporate Investigation Management (corporate matters, already documented), Code Enforcement Management (property-anchored civil enforcement, already documented).
- Main uncertainty: how much of the "case" world is genuinely investigation-specific vs. shared with the agency-wide RMS; and whether the leaf is really a distinct Type or a module/variant of the RMS.

## Research Questions

1. What is a "case" in this context — how does it relate to the incident/report in the RMS?
2. What objects exist inside the system (case, person, organization, vehicle, location, property/evidence, document, task/lead, warrant, informant, timeline event)?
3. How does the investigation flow: intake → triage → case opening → leads/tasks → documentation → review → disposition?
4. Who uses it: investigator, supervisor, task force, analyst, external partners (prosecutors)?
5. What rules matter: supervisory approval, case statuses and clearance, audit trails, CJIS-class security, agency-configurable terminology, retention?
6. What interfaces exist: case list, case folder, entity records, link analysis, timelines, dashboards, external sharing?
7. Where is the boundary with RMS, evidence custody, and CAD — what does each system of record hold?

## Representative Products

| Product | Pole | Why selected | Evidence |
|---|---|---|---|
| Case Closed Software (CaseClosed) | standalone pure-play LE case management (cloud, US; task forces, multi-jurisdiction) | clearest pure-play expression of the Type; vendor states the RMS distinction verbatim | A — homepage + Law Enforcement product page (fetched 2026-09-08) |
| Omnigo Investigation Case Management | named ICM module inside a public-safety platform; institutional/campus pole (municipal PDs, campus police, sheriff, healthcare/gaming security) | shows the Type as a named product category and at the institutional-agency scale | A — ICM solution page + public safety industry page (fetched 2026-09-08) |
| NicheRMS365 (Niche Technology) | large-agency police operational platform (UK/global) with "Investigation & Crime Management" module | suite-embedded pole at the largest agency scale; regional (UK) breadth; module family structure | A — homepage (module set, UK force quotes) (fetched 2026-09-08) |
| Mark43 RMS | cloud RMS (records pole, contrast sample) | confirms what the records side holds and that "cases" there are report-anchored records, not investigation management | A — Mark43 RMS product page (fetched 2026-09-08) |

Rejected/unreachable samples (recorded, not used as evidence): LeadsOnline (geolocation-blocked), Motorola Solutions (404), Hexagon HxGN OnCall (transport error ×2), Tyler Technologies (403), Zuercher (timeout), Unisys HOLMES 2 (404), CrimePad (transport error).

## Sources

- Case Closed Software — https://caseclosedsoftware.com/ and https://caseclosedsoftware.com/cms/ (Law Enforcement Case Management page) — fetched 2026-09-08
- Omnigo — https://www.omnigo.com/solution/investigation-case-management-software/ and https://www.omnigo.com/industry/public-safety-software — fetched 2026-09-08
- Niche Technology — https://nicherms.com/ — fetched 2026-09-08
- Mark43 — https://mark43.com/platform/mark43-rms/ — fetched 2026-09-08
- Prior passes used for boundary alignment: applications/evidence-management-system.md, applications/computer-aided-dispatch-cad.md, research/corporate-investigation-management.md, research/code-enforcement-management.md (STATUS entries), applications/court-case-management-system.md

> Source-access limitation: vendor help-center / support-article bodies were not reachable for any sampled product (block, 403, 404, timeout, or transport error across seven attempted vendors). Evidence is therefore at the marketing/product-page structural level — named modules, capability descriptions, workflow claims, vendor FAQ — not at the level of exact procedures, field lists, or numeric limits. No precise counts, durations, or defaults are asserted in the final document. The product-philosophy claims used (RMS-vs-investigations distinction) are vendors' own statements.

## Product A — Case Closed Software (pure-play)

### Key observations

- Positioning: "law enforcement case management software designed for police departments, investigative units, task forces, and multi-jurisdictional agencies to manage cases, evidence, intelligence, reports, and operations securely." Lifecycle claim: "from first tip to final disposition" / "from intake to prosecution."
- **Intake**: "Tip & Complaint Intake — capture every tip, complaint, or referral in a structured intake workflow. Assign for triage and promote to an active case with one click." (A)
- **Digital Case Folder**: "Store people, locations, reports, evidence, and attachments in one centralized case file — fully organized and searchable." (A)
- **Supplemental Reports**: "Document interviews, surveillance, warrants, and investigative actions with timestamped reports linked permanently to the case." (A)
- **Entity Management**: "Build a system-wide database of people, vehicles, and locations. Automatically surface connections across cases and aliases." (A)
- **Workflow & Task Management**: "Assign tasks, track progress, and enforce accountability with approvals, notifications, and supervisor oversight." (A)
- **Approvals & Case Closure**: "Move cases through structured approval workflows with supervisor sign-off and automatic alerts for aging cases." (A)
- **Remote Case Review**: "Share time-limited case access with prosecutors and external partners without requiring system licenses." (A)
- **Dashboards & Reporting**: "Monitor caseloads, track performance, and generate reports across investigators, case types, and regions." (A)
- Modules (named): Investigations & Case Management, Confidential Informants (CI profiles, reliability ratings, payment records), Tips & Leads, Physical Evidence (log + barcode + chain-of-custody + storage history), Gangs & Organizations (members, affiliations, events), Criminal Intelligence (link analysis), Supplemental Reports, Reports & Statistics, Operations/Event Planning, Agent Wallet & Payments. (A)
- **RMS distinction (vendor's own statement)**: "An RMS records incidents and arrests. Case Closed manages investigations. It links people, locations, vehicles, evidence, warrants, and reports across complex cases from first tip through final disposition. It complements your RMS rather than replacing it." (A)
- Configuration: "Every dropdown value, field label, case type, and subtype is configured to your agency's terminology during implementation." (A)
- Security/compliance: CJIS Security Policy, TX-RAMP, SOC 2 alignment, 28 CFR Part 23 (criminal-intelligence systems regulation) named; AES-256, MFA, audit trails, role-based sharing; cloud (Azure US) or on-premises; browser-based responsive; full data export on exit. (A)
- Multi-agency: task forces, deconfliction named (narcotics task force testimonial: "case tracking and deconfliction"); ICAC CyberTips triage; multi-jurisdictional sharing "while maintaining jurisdictional rules." (A)

## Product B — Omnigo Investigation Case Management (suite module, institutional pole)

### Key observations

- Omnigo sells **"Investigation Case Management"** as a named solution inside a public-safety platform portfolio: Quartermaster Asset Management | Investigation Case Management | Evidence Management | Records Management | Command and Planning | CAD. "Investigation Case Management Software works with other Omnigo solutions, including Incident Reporting, Dispatch, RMS, and Evidence Management." (A)
- Category self-definition (vendor FAQ): "Investigation case management software helps law enforcement agencies organize incidents, case work, documents, and evidence. It supports cases from intake to closure. It gives teams one place to record facts, track investigative steps, and keep cases complete and defensible." (A)
- **Case files**: "Build organized case files from incident reports, narratives, and follow-up activity"; "one place to manage narratives, notes, attachments, and supplemental reports"; "templates, structured forms, automatic timestamps, and version tracking." (A)
- **Evidence within the case**: "manage digital and physical evidence in each case file, including photos, videos, documents, audio recordings, descriptions, storage locations, transfers, and reviews. The system logs every action... date, time, and user for every action. This creates a complete chain-of-custody record... supports prosecutor review." (A — note: Omnigo also ships a separate Evidence Management module; the ICM page claims custody-adjacent logging inside the case file)
- **Cross-case connections**: "Query across all cases to discover connections between your suspects and bad actors, weapons, or locations established in other cases"; "Automatically generate investigation timelines, logging each step including when evidence was collected and individuals became involved." (A)
- **Tasks & supervision**: "Assign follow-up tasks, support review steps, and keep investigations moving"; supervisors "see case activity, workload, and follow-up needs in real time"; automated reminders for assignments, deadlines, pending reviews. (A)
- **Configuration**: "Configurable workflows help align case activity with reviews, approvals, checkpoints, and policy needs"; "Every agency follows its own investigative process." (A)
- **Dashboards**: "open cases, investigator assignments, evidence activity, overdue tasks, and case progress." (A)
- **Field access**: investigators "add narratives, attach files, update case information, and document follow-up activity from any location." (A)
- **Audience breadth**: "municipal police departments, campus police agencies, sheriff's offices, and public safety units"; healthcare/education/gaming/corporate security organizations use the platform; lifecycle phrase "from call open to case close." (A)

## Product C — NicheRMS365 (large-agency operational platform, suite pole)

### Key observations

- Positioning: "Police Operational Platform" / RMS "that captures every aspect of policing from the front line to the courtroom"; deployed in very large agencies (UK forces, Canadian services, US counties). (A)
- Named module set: Intelligence Management, Vulnerability Management, General Incident Management, **Investigation & Crime Management**, Property Management, Forensics Management, Custody Management, Case Preparation & Criminal Justice. (A) — investigation management is a named, isolable module inside the operational platform, distinct from case preparation (prosecution-side) and custody.
- Customer quotes about the investigation function: "The improved recording and investigation has led to a rise in detections, particularly people being charged, summonsed and cautioned" (UK force); "Electronic tasking means... improving the quality and speed of providing victim and witness case progress updates and less internal chase-up enquiries" (UK force). (A)
- Depth limitation: homepage evidence only; no module-level documentation fetched. Module structure is Layer A; module internals are NOT evidenced. (limitation recorded)

## Product D — Mark43 RMS (records pole, contrast sample)

### Key observations

- RMS positioning: "comprehensive, cloud-native RMS" centered on **report writing**: "Write Reports Faster and Easier," NIBRS and State IBRS compliance validation, Booking, Use of Force Reporting, eCitations. (A)
- Case mentions are report-anchored: "linking records, documents, and multimedia from external systems to your agency's active reports and cases." No investigations module named on the product page. (A)
- Together with Case Closed's verbatim statement, this anchors the records-vs-investigation boundary: the RMS holds the report of record; the investigation Type holds the case work built on it. (A + cross-product inference)

## Cross-product Comparison

| Dimension | Case Closed (pure-play) | Omnigo ICM (suite module) | NicheRMS365 (operational platform) | Mark43 RMS (contrast) |
|---|---|---|---|---|
| Unit of record | case, from tip/complaint/referral intake | case file from incident reports + follow-up | investigation inside "Investigation & Crime Management" module | report (NIBRS-validated) + cases as report-anchored records |
| Entity layer | people/vehicles/locations database, cross-case & alias connections | suspects/weapons/locations connections across cases | (not evidenced at module depth) | records linkable to reports |
| Work management | tasks, approvals, supervisor oversight, aging alerts | follow-up tasks, deadlines, reminders, supervisor review in real time | "electronic tasking," victim/witness progress updates | (report workflow only) |
| Documentation | supplemental reports (interviews, surveillance, warrants) permanently linked | narratives, notes, attachments, supplemental reports, timestamps, version tracking | (not evidenced) | reports of record |
| Outcome | structured approval → case closure | intake → closure, "complete and defensible" | detections → charge/summons/caution | report submission/compliance |
| Evidence relationship | native physical-evidence module w/ chain of custody | evidence logged in case file + separate Evidence Management module | separate Property/Forensics/Custody modules | multimedia linked to reports |
| External handoff | time-limited prosecutor/partner access | prosecutor review support | Case Preparation & Criminal Justice module | sharing with prosecution systems |
| Security posture | CJIS, 28 CFR Part 23, MFA, audit trails, role-based sharing | role-based permissions, secure system | (large-agency regime; not detailed on page) | FedRAMP High named elsewhere |
| Deployment | cloud (Azure) or on-prem; browser-based | suite platform | enterprise platform, mobile | cloud-native |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures:

1. **The investigation case of record** — a persistent, individually identified case bound to an agency investigative matter, opened from an intake (report, tip, complaint, or referral) and carrying its classification, status, assigned investigator(s), and the accumulating investigative record. Remove → a report archive or file store; nothing is being "managed."
2. **The investigative entity web** — the people, organizations, vehicles, locations, weapons, and property held as records that link into the case with roles (suspect, victim, witness, informant), maintained so connections can be surfaced within the case and across cases/aliases. Remove → a narrative document or folder with no addressable who/what; the investigative value collapses.
3. **The supervised investigative lifecycle** — investigative work (tasks/leads/follow-ups, documented investigative actions) assigned, tracked, and reviewed through configurable statuses under supervisory approval, ending in a recorded disposition (cleared, closed, referred onward). Remove → a static case folder or generic task list; the "management" is gone.

Jointly-held is load-bearing: 1 alone = case file storage; 2 alone = an entity/intelligence registry; 3 alone = generic task tracking; 1+3 without 2 = a checklist with no subject web; 1+2 without 3 = an archive with no work management.

Domain anchoring: the case is a law-enforcement investigative matter (typically a suspected criminal offense; the same machinery also serves specialized unit matters such as internal or task-force investigations). The criminal-justice framing is what separates this Type from corporate investigation management, even where the machinery overlaps.

### L1 — Common Mature Structure

Present across the sampled products and expected in the market, but not what makes the Type:

- digital case file with narratives, supplemental reports, attachments, timestamps, version tracking
- task/lead assignment with deadlines, reminders, follow-up tracking
- supervisor dashboards: open cases, assignments, workload, overdue/aging
- entity connections surfaced across cases (aliases, repeat actors, locations); investigation timelines
- evidence/property linkage (native or via a dedicated evidence module)
- integration spine: RMS, CAD, evidence systems, prosecution/court handoff surfaces
- role-based access, audit trails, CJIS-class security expectations
- configurable terminology and workflow (agency-defined case types, statuses, review checkpoints)
- reporting/statistics on caseload and outcomes

### L2 — Variant / Optional Structure

- packaging: standalone pure-play vs named module inside an RMS/operational platform vs institutional/campus pole
- multi-jurisdiction task-force operation with deconfliction
- specialized domain configurations: narcotics, gangs, ICAC/child exploitation, human trafficking, criminal intelligence (28 CFR Part 23-class), confidential informant management
- deployment: government cloud vs on-premises; browser vs mobile/field capture
- analysis depth: link-analysis/visualization vs plain cross-case search
- external collaboration surfaces: prosecutor/partner portals, time-limited access

### L3 — Vendor-specific (research notes only)

- Case Closed: Agent Wallet & Payments, CI reliability ratings/payment vouchers, "Tracker" and "CaseNexus" modules in development, 30-day implementation claim, TX-RAMP certification specifics
- Omnigo: portfolio packaging (Quartermaster, Command and Planning, EverSure support service), "call open to case close" phrasing
- NicheRMS365: module naming (Custody Management, Case Preparation & Criminal Justice, Vulnerability Management), agency-scale statistics
- Mark43: ReportAI/BriefAI, crime-gun interfaces, FedRAMP High tier

## Rejected Findings

- **"Case management = NIBRS reporting"** — rejected: NIBRS/state reporting is the records side (Mark43); the investigation Type consumes reports, it does not produce statutory report compliance.
- **"The Type includes full chain-of-custody custody machinery"** — rejected as definitional: the custody chain is the Evidence Management System's defining core (documented in that pass). Case-side products either link evidence records or ship adjacent modules; Omnigo's case-file logging is a packaging realization, not the Type's invariant. Remove custody and the ICM still stands; remove the case and the custody system still stands.
- **"CJIS compliance is definitional"** — rejected: it is a dominant deployment expectation in US products, not a structural property; the defining core is jurisdiction-independent.
- **"Link analysis / intelligence databases are the core"** — rejected: cross-case connection surfacing is standard (2/2 products that document it) but an entity registry without case lifecycle is a different product shape; it stays L1.
- **"Cases are always criminal offenses"** — softened: sampled products anchor on suspected offenses, but the same machinery serves task-force, specialized-unit, and institutional matters; the invariant is the agency investigative matter with criminal-justice framing, not a specific offense taxonomy.

## Boundary Findings

- **vs Police Records Management System** (sibling leaf, unprocessed): the RMS is the agency's record of incidents, arrests, and reports (statutory/reporting semantics — Mark43 evidence). Case Closed states the distinction verbatim: RMS records incidents and arrests; this Type manages investigations, linking people, locations, vehicles, evidence, warrants, and reports across cases. Suite platforms ship investigation management as a named module inside the RMS (Niche) — suite packaging, not Type identity. Remove-tests: remove investigation workflow → RMS remains; remove report-of-record compliance and add case lifecycle → this Type.
- **vs Evidence Management System** (processed): custody of items (chain of custody, storage, disposition) vs the case's investigation record (narratives, persons, outcomes). The evidence pass already defines this boundary: "the case is the system of record for investigation narratives, persons, and outcomes; the evidence system of record is the item in custody." Designed to interlock.
- **vs CAD** (processed): CAD is real-time dispatch of status-tracked units to live incidents; incident data flows downstream to records and then to investigation. No real-time unit status here.
- **vs Prosecutor Case Management** (sibling leaf, unprocessed): prosecution phase (charges, court process) belongs to the prosecutor's system; this Type's products provide handoff surfaces (prosecutor review portals, case-preparation modules), not prosecution management.
- **vs Court Case Management System** (processed): court-phase docket/hearing machinery; downstream consumer of case outcomes.
- **vs Corporate Investigation Management** (processed): same case machinery family, different domain semantics — corporate matters with legal/HR/compliance actors vs criminal-justice matters with suspects/victims/offenses.
- **vs Code Enforcement Management** (processed): civil, property-anchored enforcement with violation/notice/fine progression; no investigative entity web or clearance semantics.
- **vs Public Sector Case Management** (sibling leaf, unprocessed): citizen-service request handling (311-class); the "case" is a service request, not an investigative matter.
- **vs Digital Forensics Platform** (processed): technical examination tooling whose findings feed into cases; it is evidence-producing, not case-managing.
- **Type-boundary verdict**: the leaf stands as a distinct Type. It is not merely an RMS variant (pure-play products exist; vendors name and sell investigation case management as its own category), and it is not a variant of corporate case management (different actors, semantics, security regime).

## Uncertainties

- Exact case-status vocabularies (active/inactive/cleared classifications) were not evidenced from official docs at the field level; the final document describes the lifecycle conceptually and avoids asserting specific status names or clearance codes.
- Depth of NicheRMS365's investigation module is not evidenced (homepage-level evidence only).
- Whether warrant/informant/charge objects are universal or market-segment-dependent: Case Closed documents them; Omnigo does not name them; treated as common-to-variant, not core.
- Historical/regional samples (e.g., UK major-enquiry systems, paper-era detective files) could not be fetched; the historical check is reasoned from the defining core (paper case folders with person cards, lead sheets, supervisor sign-off satisfy all three legs) rather than documented vendor history.
- The exact relationship to the unprocessed sibling leaves (Police Records Management System, Prosecutor Case Management, Public Sector Case Management) should be revisited when those passes run; a joint review with police-records-management-system is recommended.

## Final Synthesis

Law Enforcement Case Management is the investigative case system of record for law enforcement agencies: it opens cases from reports, tips, complaints, and referrals; holds the investigation's entities (people, vehicles, locations, weapons, property) as records linked with roles, with connections surfable across cases; runs the supervised work of investigation (tasks, leads, documented actions) through configurable statuses under supervisor review; and ends in a recorded disposition handed onward to prosecution or closed. It is defined by the case-of-record + entity-web + supervised-lifecycle triad; everything else — task-force sharing, intelligence modules, custody integration, CJIS regimes, link analysis, dashboards — is the standard or variant capability space. The market expresses the Type as pure-play products, named modules inside police operational platforms, and institutional public-safety suites.
