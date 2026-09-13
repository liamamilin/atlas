# Research Notes — Prosecutor Case Management

## Research Goal

Understand what a Prosecutor Case Management application actually is from real products: what objects exist inside it, what prosecutors and their staff do with them, how a case moves from police referral to final disposition, and where the boundary lies with neighboring justice-system Types (law enforcement RMS, court case management, public defender case management, legal matter management).

## Initial Boundary

- Leaf: **Prosecutor Case Management** (DIRECTORY §24 Government, Public Sector & Civic)
- Hypothesis: software used inside a prosecutor's / district attorney's office to track criminal cases from law-enforcement referral through charging, court proceedings, and disposition — distinct from the police-side records system and the court-side docket system.
- Nearest neighbors: Law Enforcement Case Management, Police Records Management System, Court Case Management System, Public Defender Case Management, Legal Matter Management, eDiscovery Platform, Legal Docket Management.

## Research Questions

1. What is the unit of record? What does a "case" bind together?
2. How does a case enter the system (referral → charging decision)?
3. What is the role of the **charge** — is it a first-class managed object?
4. How is the court process tracked (hearings, dockets, deadlines, disposition)?
5. Which support services are standard (discovery, evidence, victim/witness, subpoena, restitution, conflict checking, diversion)?
6. Who are the users and what roles exist inside a prosecutor's office?
7. What external exchanges exist (law enforcement, courts, defense, victims)?
8. What distinguishes this from court CMS and police RMS?

## Representative Products

| Product | Vendor | Why selected |
|---|---|---|
| PROSECUTORbyKarpel (PbK) | Karpel Solutions | claims to be the most widely used US prosecutor CMS; 30-year lineage; feature-structured site |
| eProsecutor | Journal Technologies | purpose-built CMS on a justice-suite framework; detailed feature documentation; sibling products (eCourt, eDefender) clarify boundaries |
| prosecutorDATA | Justice Works | prosecutor-specific case tracking; feature-matrix packaging; also serves public defenders (sibling view) |
| Case 365 (Prosecution) | 365 Labs | modern cloud/mobile pole; explicit "referral to disposition" framing; police/court integration emphasis |
| SEARCH PCMS Functional Requirements | SEARCH Group (industry consortium) | neutral functional specification for prosecutor case management systems — cross-vendor baseline |

## Sources

- https://www.prosecutorbykarpel.com/ (fetched 2026-09-10) — product positioning, feature taxonomy (Efficiency / Information Management / Integrations / Evidence Tracking / Investigative Services / Victim Services)
- https://www.journaltech.com/eprosecutor (fetched 2026-09-10) — full feature page: charging process, eDiscovery, case involvements/conflict check, document management, victim services, subpoena management, public portal
- https://www.justiceworks.com/prosecutor-data (search excerpt, 2026-09-10) — case tracking, automated workflows, calendaring, centralized case materials, collaboration
- https://365labs.com/case365/prosecution and https://365labs.com/case365/ (search excerpts, 2026-09-10) — "from referral to disposition", automatic case creation, court activity tracking, eDiscovery portal, media repository, financial tracking
- https://www.search.org/files/pdf/PCMS_Functional_Specifications.pdf (search excerpt, 2026-09-10; full PDF not text-extractable in this environment — see limitation below)
- https://www.isabellacounty.org/wp-content/uploads/2019/10/PAO_Karpel_Software.pdf (search excerpt, 2026-09-10) — legacy-system context: office previously used ~40-year-old association-built Adult/Juvenile Case Tracking programs plus separate file storage; also documents victim portal, LEO portal, eDiscovery capabilities
- https://www.suffolkva.us/306/Case-Management-System (search excerpt, 2026-09-10) — office-side description of a deployed PbK system
- https://www.nccourts.gov/assets/inline-files/eDiscovery-Prosecutor-QRG-092922.pdf (search excerpt, 2026-09-10) — Tyler Technologies eDiscovery: packet/binder/release/recall workflow between law enforcement, prosecutors, defense

**Source-access limitation:** the SEARCH.org PCMS functional-specification PDF could not be text-extracted in this environment; its content is used only at the level of the search-index excerpt (document structure, section titles, and quoted requirements such as "Must track which agency initiated the investigation or referred the charges" and "Should support electronic filing of charging documents… and transfer designated data from the PCMS to the court case processing system"). No precise numeric requirements are asserted from it.

## Product Observations

### PROSECUTORbyKarpel (PbK) — Evidence Layer A (official site)

- Positioned as "criminal case management" for prosecutors and DA offices; "designed by prosecutors for prosecutors"; deployed at county DA / solicitor-general / city attorney / state AG offices (US state & local government market).
- Feature taxonomy (site navigation):
  - **Efficiency**: go paperless; document management & generation; workflow management; in-court use; **person-centric** data model.
  - **Information Management**: power search; **eDiscovery**; comprehensive **financial tracking** (restitution etc.); reporting.
  - **Integrations**: law-enforcement and court RMS integration; courts integration; calendar/email integration; **external agency portal**; legal-research integration.
  - **Evidence Tracking**: case evidence "entered and tracked either off site or on a shelf in your evidence room"; integration with a third-party digital-evidence platform.
  - **Victim Services**: integrated victim services; victim engagement platform; VOCA and grant reporting; two-way texting.
  - **Investigative Services**: tools for office investigators (reports, time tracking).
- County procurement documents describe: victim portal (approved updates, court dates, document signing, text/email alerts), LEO portal for police report transmission, e-discovery delivery, statewide search across contributing agencies (defendant/co-defendant/court-date/charge/case info).
- Legacy context (Isabella County doc): predecessor systems were "Adult Case Tracking / Juvenile Case Tracking" programs in use "for nearly four decades" plus separate file storage — i.e., the historical artifact was case tracking + files, without portals, e-discovery, or cloud.

### eProsecutor (Journal Technologies) — Evidence Layer A

- "Purpose-built Case Management System designed exclusively for prosecutors"; configurable screens, data elements, business rules, workflows per office.
- **Charging process**: "review law enforcement referrals and seamlessly handle the amendment, addition, or rejection of charges"; data-entry tools, charging decisions, "automated charging language with drop-down selections", **charge history**.
- **Integrated eDiscovery**: compile, organize, disclose digital discovery; portal notifies opposing counsel for automated disclosure.
- **Case Involvements** (conflict checking): searches for prior attorney involvement, personal relationships, other conflicts; runs "each time a person is added to a case".
- **Document management**: auto-populated templates, file-cabinet folders, redaction/stamping/notation/highlighting, word search.
- **Victim services**: track victimizations, classifications, services provided; one-click VOCA statistical report.
- **Subpoena management**: generate/track subpoenas, mass batch, delivery options.
- **Public portal**: victims submit rights statements, file restitution, view court schedule, communicate with the office.
- Security: role-based access control, authentication, audit trails.
- Sibling products: eCourt (court side), eDefender (defense side), eAttorney (AG configuration), eProsecutor Online (small-office SaaS "light" version).

### prosecutorDATA (Justice Works) — Evidence Layer B (official marketing page via search index)

- "Designed and built exclusively for prosecutor case tracking."
- Centralized case materials: "evidence, discovery documents, motions, schedules, and communications" accessible in office, at trial, or remotely.
- Automated workflows: "trigger the generation of charging documents, assign tasks to staff based on case type, or notify attorneys of upcoming deadlines."
- Integrated calendaring to prevent missed hearings; batch editing.
- Collaboration between "attorneys, investigators, victim-witness coordinators, and administrative staff"; internal messaging, tasking; "integrated connections with law enforcement, courts, and correctional facilities."
- Vendor also sells public-defender case management (sibling product line).

### Case 365 — Prosecution (365 Labs) — Evidence Layer B (official marketing pages via search index)

- "Manage … cases from arrest to sentencing"; "from referral to disposition"; "record, manage & prosecute cases from arrest to sentencing."
- Automatic case creation; "booking to formal charges"; "rap sheets + electronic police reports"; court activity tracking; calendar/task sync; workflows based on key dates; team workload balancing.
- eDiscovery portal "for defense attorneys to log in & receive discovery documents"; auditable.
- Electronic trial packages (searchable tablet case files for court); media repository (documents/photos/video/audio per case); case inquiry portal for partner organizations.
- Financial tracking: restitution, discovery fees, bad checks, diversion programs.
- Integration with police and court databases; CJIS-compliant security framing.

### SEARCH PCMS Functional Requirements — Evidence Layer B (neutral industry spec, excerpt-level)

- Defines a PCMS as "a collection of capabilities … that address the functional requirements of a prosecutor's office"; "case management and tracking remain the core activities supported with other business service activities."
- Case lifecycle coverage: pretrial, trial, post-adjudication; special case types (grand jury, juvenile, civil forfeiture).
- Case support services: discovery, evidence management, investigations, motions, victim services/assistance, restitution and compensation management, witness management, diversion/deferred prosecution.
- Referral tracking: "Must track which agency initiated the investigation or referred the charges."
- Charging documents: "Must allow the user to create all documents needed for filing"; "Should support electronic filing of charging documents (e.g., complaint, indictment, etc.) and transfer designated data from the PCMS to the court case processing system"; should handle court acknowledgement.
- Data exchanges with courts: docketing/calendar information, court minutes, discovery information, hearing requests; speedy-trial and other deadline compliance.

## Cross-product Comparison

| Structure | PbK | eProsecutor | prosecutorDATA | Case 365 | SEARCH spec | Strength |
|---|---|---|---|---|---|---|
| Persistent case file as unit of record (person/defendant-centric) | ✓ (person-centric) | ✓ | ✓ ("centralized case materials") | ✓ | ✓ | Core (5/5) |
| Law-enforcement referral intake | ✓ (LE integration/portal) | ✓ ("review law enforcement referrals") | ✓ (connections with law enforcement) | ✓ ("booking to formal charges", auto case creation) | ✓ ("must track which agency … referred") | Core (5/5) |
| Charge as managed object (accept/amend/reject; charging documents; charge history) | implied via document generation & workflows | ✓ explicit | ✓ ("generation of charging documents") | ✓ ("booking to formal charges") | ✓ explicit | Core (5/5) |
| Court-process tracking (hearings, dockets, calendars, deadlines, disposition) | ✓ (courts integration, calendar) | ✓ | ✓ (calendaring, deadlines) | ✓ ("court activity tracking", "referral to disposition") | ✓ (pretrial/trial/post-adjudication, speedy-trial) | Core (5/5) |
| Discovery compilation & disclosure to defense | ✓ (eDiscovery) | ✓ (portal, notify opposing counsel) | ✓ | ✓ (defense portal) | ✓ | Common-mature (5/5) |
| Evidence tracking / media repository | ✓ | ✓ (document mgmt) | ✓ | ✓ (media repository) | ✓ | Common-mature (5/5) |
| Victim & witness management | ✓ (victim services, portal, VOCA) | ✓ (victim services, VOCA) | ✓ (victim-witness coordinators) | ✓ (VAC notes) | ✓ | Common-mature (5/5) |
| Subpoena management | — (not surfaced on fetched pages) | ✓ | — | ✓ (subpoena docs) | ✓ | Common (3/5) |
| Conflict / case-involvement checking | — | ✓ explicit | — | — | — | Optional (1/5, product-specific in sample) |
| Financial tracking (restitution, fees, diversion) | ✓ | ✓ (restitution via portal) | — | ✓ | ✓ (restitution/compensation) | Common (4/5) |
| Diversion / deferred prosecution | — | — | — | ✓ (diversion programs) | ✓ | Common (2/5 + spec) |
| External portals (LEO, defense, victim, partner) | ✓ | ✓ | — | ✓ | — | Variant (3/5) |
| Court/LEA system integration (data exchange) | ✓ | ✓ (API integrations) | ✓ | ✓ | ✓ | Common-mature (5/5) |
| Role-based access, audit, CJIS-style security | ✓ (implied) | ✓ explicit | ✓ ("secure") | ✓ (CJIS) | ✓ (security section) | Common-mature (5/5) |
| Investigator support (office investigators) | ✓ | — | ✓ (investigators named) | ✓ (FieldNotes app) | ✓ (investigations) | Common (4/5) |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Three jointly-held structures; remove any one and the product stops being recognizable as prosecutor case management:

1. **The prosecution case of record** — a persistent, identified case file binding a defendant (person-centric) to alleged offenses in a jurisdiction, accumulating the office's work product (documents, events, people, money) across the case's whole life, from referral to final disposition. Remove → a docket viewer or a document folder.
2. **The charge as the managed prosecutable object** — the case enters on a law-enforcement referral; the office reviews it and exercises the charging decision: accept, add, amend, or reject charges; charging documents are produced for filing; charge history is retained. Remove → police records system (no charging decision) or court CMS (no charging discretion).
3. **Prosecution-side tracking of the court process** — the office's own view of the case's movement through the court process: court events/hearings, calendars and deadlines (including speedy-trial-type constraints), case status, and final disposition recorded on the case. Remove → a static case file with no operational lifecycle.

Binding semantics: criminal-prosecution case semantics (defendant × charges × court process). Remove the prosecution/charge semantics → generic legal matter management.

### L1 — Common Mature Structure

- Discovery compilation and disclosure to the defense (increasingly via a defense-facing portal)
- Evidence / media tracking bound to the case
- Victim and witness management (victim services, notifications, VOCA-type reporting)
- Document management & generation from templates (charging documents, subpoenas, motions, victim letters)
- Subpoena generation and tracking
- Financial tracking (restitution, fees, diversion-related money)
- Integration/data exchange with law-enforcement RMS and court case-processing systems
- Role-based access control, audit trails, criminal-justice-grade security
- Office workflow automation (task assignment by case type, deadline notifications)
- Investigator support for in-house investigators

### L2 — Variant / Optional Structure

- External portals: law-enforcement portal (report submission), defense discovery portal, victim portal (updates, court dates, document signing, texting), partner-agency inquiry portal
- Conflict / case-involvement checking (present in one sampled product explicitly; likely more widespread but unverified in sample)
- Electronic filing / direct data transfer to court systems (spec says "should" — not universal)
- Electronic trial packages (searchable tablet case files for in-court use)
- Special case types: juvenile, grand jury, civil forfeiture, appeals
- Diversion / deferred-prosecution program management
- Statewide/multi-agency shared deployments (statewide search across contributing offices)
- Deployment: on-premise vs hosted/SaaS; small-office "light" editions
- AI assistance (emerging)

### L3 — Vendor-specific (Research Notes only)

- PbK: "Power Search", Evidence.com integration, Westlaw integration, two-way victim texting, person-centric framing, "Why Not The Cloud" positioning (on-premise heritage now offering SaaS)
- eProsecutor: eSeries framework, eAttorney (AG configuration), eProsecutor Online light edition, VOCA one-click report, Case Involvements feature name
- Case 365: Windows-11-native positioning, FieldNotes investigator app, RTCC/CSU prevention modules, electronic trial packages branding
- Justice Works: voucher management (public-defense heritage), Standard/Premier/Add-Ons packaging
- Tyler eDiscovery (adjacent module, not a PCMS): packet → binder → mark-for-release → release → recall workflow vocabulary

## Historical / Market-Sample Check

- Legacy pole: the Isabella County document shows offices running ~40-year-old "Adult Case Tracking / Juvenile Case Tracking" programs plus separate file storage before adopting a modern PCMS. Those predecessors = case tracking + files, without portals, e-discovery, cloud, or workflow automation — they still satisfy the three L0 structures (case of record, charge management, court-process tracking). **Historical check passed.**
- Regional check: sample is US-centric (the market is dominated by US state/local prosecution offices). Non-US prosecution services (e.g., UK CPS case-management systems) were not directly documented in this pass; the L0 is written jurisdiction-neutral (defendant × charges × court process) so that non-US prosecution services plausibly fit, but this is unverified — recorded under Uncertainties.

## Boundary Findings

| Neighbor | Distinguishing test |
|---|---|
| **Police Records Management / Law Enforcement Case Management** | The police side originates the investigation and refers the case; the prosecutor side receives the referral and holds the **charging decision**. Remove the charging decision and referral intake → police RMS. The PCMS explicitly tracks *which agency referred* (spec) and receives police reports — the seam is direction of flow and charging discretion. |
| **Court Case Management System** | The court owns the authoritative docket and hearing record; the PCMS holds the prosecution's own case file and *exchanges* data with the court (spec: "transfer designated data from the PCMS to the court case processing system"). Remove the prosecution-side case file and charging discretion → court CMS. Vendor evidence: Journal Technologies sells eProsecutor and eCourt as separate products. |
| **Public Defender Case Management** | Mirror-image sibling: same case-lifecycle structure, opposite party, plus defense-specific concerns (conflict-free representation of multiple co-defendants, voucher/billing). Vendors ship both as separate products (eDefender, DEFENDERbyKarpel, Justice Works). Keep both; boundary = which party's case file it is. |
| **Legal Matter Management / Law Practice Management** | Generic matters lack charge semantics, the referral→charging→disposition criminal lifecycle, and the statutory discovery-disclosure duty to the opposing party. Remove charge/court-process semantics → generic matter management. |
| **eDiscovery Platform** | In a PCMS, discovery is one support service bound to the prosecution case and driven by the disclosure duty; a standalone eDiscovery platform is a general litigation tool. Tyler's eDiscovery integrates *into* prosecutor workflows (packets linked to binders) — a module, not the Type. |
| **Legal Docket Management** | Docketing is one tracked surface inside the PCMS (court events); docket management as a Type centers on the docket/calendar itself. |

**"Remove what to become another Type" summary:** remove the charging decision → police RMS; remove the prosecution-side case file → court CMS; remove charge/court semantics → legal matter management; remove the case binding → eDiscovery or document management.

## Uncertainties

- Non-US prosecution systems not directly documented; L0 assumed jurisdiction-neutral but unverified outside the US sample.
- Conflict checking's market prevalence: explicit in 1/5 sample; classified Optional rather than Common.
- Whether e-filing to courts is standard or still variant: spec uses "should"; treated as variant/common-mature boundary.
- SEARCH spec details beyond the excerpt level unverified (PDF not text-extractable).
- Prevalence of grand-jury/juvenile/forfeiture special-case handling not individually verified per product.

## Final Synthesis

A Prosecutor Case Management application is the prosecutor's office's case-file system of record for criminal prosecution. Its defining core is three jointly-held structures: (1) the persistent prosecution case of record binding a defendant to alleged offenses and accumulating the office's work product from referral to disposition; (2) the charge as the managed object — referral intake, the accept/amend/reject charging decision, charging-document production, charge history; (3) the office's own tracking of the case's movement through the court process — hearings, calendars, deadlines, status, disposition. Everything else — discovery portals, evidence rooms, victim services, subpoenas, restitution, integrations with police and courts — is mature supporting structure layered on that core, and the historical lineage (decades-old case-tracking programs) confirms the core predates the modern portal/cloud layer.
