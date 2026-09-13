# Research Notes — Police Records Management System

## Research Goal

Understand what a "Police Records Management System" (market label: **RMS**) actually is, as distinct from the neighboring public-safety types — CAD (live dispatch), Law Enforcement Case Management (investigations), Evidence Management System (item custody), Corrections Management System (custody episodes), Court/Prosecutor Case Management (judicial phases), Fire Department Records / Operations System (fire-service records). Derive the smallest defining core, the standard mature capability set, and the variant space, from real product documentation.

Prior-pass obligations carried into this pass:

- **law-enforcement-case-management (processed 2026-09-08) joint-review recommendation**: vendors state the seam verbatim ("An RMS records incidents and arrests. [Case management] manages investigations"), but the market packages investigation management as a named module inside RMS/operational platforms (NicheRMS365 "Investigation & Crime Management"; Omnigo ships Records + Evidence + ICM as separately named solutions). This pass must treat investigation management as **interlocked packaging, not identity**, and run the removal tests both directions.
- **computer-aided-dispatch-cad (processed)**: CAD owns the live incident and unit state; RMS owns the post-incident record; the seam is the automatic hand-off of closed incident data (Motorola: "automatic data transfer from CAD to records management systems"; Mark43 suite splits CAD vs RMS).
- **corrections-management-system (processed)**: CentralSquare sells RMS and Jail as separate products; the RMS records arrests about people who may never be booked; corrections begins at lawful custody.
- **fire-department-records-operations-system (processed)**: same "agency system of record" family; law-enforcement records follow different domain semantics and standards (NIBRS-class, not NERIS-class). That pass held standardized national reporting NOT definitional — this pass must make its own call on the police side.

## Initial Boundary

Working hypothesis at start:

- The Type is the **police agency's system of record for its official operational records**: incident reports, arrests, citations — written, classified, linked, retained, and reported under the jurisdiction's rules.
- Nearest neighbors: CAD (upstream, live), Law Enforcement Case Management (interlocked sibling), Evidence Management System (item custody), Corrections (booking/custody seam), Court/Prosecutor CMS (downstream), Fire RMS (sibling family), Government Records Management (agency-wide retention discipline), FOI/Public Records Request Platform (downstream consumer).
- Main uncertainties at start: (1) is the master person/vehicle/location index definitional or just common? (2) is statutory statistical reporting (NIBRS-class) definitional or standard-mature? (3) is supervisor approval of reports definitional? (4) how much of the "operational platform" breadth (intelligence, custody, forensics, case prep) belongs to this Type vs. being suite packaging?

## Research Questions

1. What is the unit of record — the incident report? the arrest? the "case"? How do report, arrest, citation, and case relate?
2. What record classes exist inside the system (incident, arrest, citation, person, vehicle, location, property/evidence, use of force, warrant)?
3. What is the master index — how do records link to persons/vehicles/places across events, and why does that matter?
4. What is the report lifecycle: field entry → validation → approval → statistics/court? Where does CAD data enter?
5. What compliance machinery exists: NIBRS/State IBRS validation, national standards (UK), CJIS-class security, retention/audit?
6. Who uses it: patrol officer (field entry), records clerk/supervisor, detective, command staff, administrator?
7. What interfaces exist: report entry, approval queue, search/inquiry, master record pages, submission, admin/config?
8. Where are the boundaries: CAD hand-off, investigation packaging, evidence custody, booking/jail seam, court handoff?
9. What varies: packaging (standalone/module/suite), agency scale, jurisdiction (US NIBRS vs UK national standards), deployment (cloud vs heritage on-prem)?

## Representative Products

| Product | Pole | Why selected | Evidence |
|---|---|---|---|
| Mark43 RMS | cloud-native modern SaaS pole (US mid/large agencies; entering UK) | clearest report-centric cloud RMS; named sub-modules (Booking, Use of Force, eCitations) expose the record-class structure | A — RMS product page, Booking page, UK solution page (fetched 2026-09-09) |
| NicheRMS365 (Niche Technology) | large-agency operational platform pole (UK/Canada/US; "world's most widely used RMS" claim) | shows the Type at the largest agency scale, as a module platform spanning front line to courtroom; regional (UK) breadth | A — homepage + NicheRMS365 product page (fetched 2026-09-09) |
| Omnigo Records Management | municipal/institutional suite-module pole (30-year heritage; campus, sheriff, small municipal) | shows the Type as a named module inside a public-safety suite at the small-agency scale; regional data sharing | A — Records product page + public-safety industry page (fetched 2026-09-09) |
| CentralSquare Records | public-sector suite pole (Enterprise/Pro/ONESolution tiers; 8,000+ agencies) | shows the Type inside a whole-agency suite (911/CAD/RMS/Jail/Mobile) with tiered packaging and NIBRS submission integration | A — Records product page + Records Supervisor page + public-safety page (fetched 2026-09-09) |

Rejected/unreachable samples (recorded, not used as evidence): Zuercher Technologies (timeout ×2 across passes), Motorola Solutions records/Spillman pages (404 ×2 this pass; 404 in prior pass), Hexagon (transport error ×2, prior pass), Tyler Technologies (403, prior pass), Sun Ridge Systems (timeout), eFORCE Software (transport error), Cody Systems (transport error), LeadsOnline (geolocation-blocked, prior pass), Mark43 Help Center (JS-gated, CSS error). Alert Protection Service (alertps.com) turned out to be a medical-alert device vendor — product mismatch, discarded.

## Sources

- Mark43 — RMS product page: https://mark43.com/platform/mark43-rms/ — fetched 2026-09-09
- Mark43 — Booking product page: https://mark43.com/platform/rms/booking/ — fetched 2026-09-09
- Mark43 — UK & Ireland solution page: https://mark43.com/solutions/united-kingdom/ — fetched 2026-09-09
- Niche Technology — homepage: https://nicherms.com/ — fetched 2026-09-09
- Niche Technology — NicheRMS365 product page: https://nicherms.com/nicherms-365/ — fetched 2026-09-09
- Omnigo — Police Records Management Software (RMS): https://www.omnigo.com/solution/police-records-management-software — fetched 2026-09-09
- Omnigo — Public Safety Software industry page: https://www.omnigo.com/industry/public-safety-software — fetched 2026-09-09
- CentralSquare — Records and Digital Evidence Management Systems: https://www.centralsquare.com/solutions/public-safety-software/records-management-system — fetched 2026-09-09
- CentralSquare — Records Supervisor page: https://www.centralsquare.com/solutions/public-safety-software/records-supervisor — fetched 2026-09-09
- CentralSquare — Public Safety & Justice page: https://www.centralsquare.com/solutions/public-safety-software — fetched 2026-09-09
- Prior passes used for boundary alignment: applications/law-enforcement-case-management.md (+ research), applications/computer-aided-dispatch-cad.md, applications/corrections-management-system.md, applications/fire-department-records-operations-system.md, applications/evidence-management-system.md, applications/court-case-management-system.md, applications/animal-control-management.md

> Source-access limitation: vendor help centers and support portals were not reachable for any sampled product (JS-gated Salesforce site for Mark43; no public help-center URLs surfaced for the others). Evidence is at the official product-page structural level — named modules, capability descriptions, workflow claims, customer quotations, vendors' own category definitions — not at the level of exact procedures, field lists, or numeric limits. No precise counts, durations, status vocabularies, retention periods, or default settings are asserted in the final document. NIBRS/UCR-class standard details are described only as far as vendor pages reference them.

## Product A — Mark43 RMS (cloud-native pole)

### Key observations

- Positioning: "comprehensive, cloud-native RMS" for public safety; "The Modern Records Management System for Public Safety"; hero claim "Less paperwork. More time to protect and serve." (A)
- **Report writing is the center**: "Write Reports Faster and Easier"; "mobile-first design, intuitive workflows, and AI tools"; "Slash Report Writing Time by up to 80%" (vendor claim, marketing figure — not asserted in final doc). (A)
- **Compliance validation built in**: "NIBRS and State IBRS compliance validation improves accuracy and data quality"; "Mark43 was built around NIBRS and State IBRS compliance to materially reduce the need for correcting and resubmitting reports. Error validation is easy with plain-language callouts and direct links." (A)
- **Linking**: "Work with all information at your fingertips by linking records, documents, and multimedia from external systems to your agency's active reports and cases." (A)
- **Record classes visible in the module set**: reports; **Booking** ("A comprehensive custody solution": booking photos, property, legal information, scars/marks/tattoos, events during custody — medical appointments, housing arrangements, financial transactions; "Historical Detainee Log — centralized record for detainees. Historical data is always searchable, retaining labels or cautions if the individual is rebooked"; "sync data between Mark43 RMS and Mark43 Booking to automatically populate data collection forms with offense codes and arrest information"); **Use of Force Reporting**; **eCitations** (OnScene); **Crime Gun Interfaces**. (A)
- **CAD integration**: Mark43 CAD is a sibling product; "Alternate CAD" for agencies keeping another CAD. (A)
- **Analytics**: Modern Data Platform (Insights, Data Lake, Integrated Ecosystem). (A)
- **Security**: FedRAMP High; "Mark43 Fortified"; UK page shows ISO certifications. (A)
- **Audience breadth**: Law Enforcement, Dispatch, Federal, Campus, Port and Transportation, United Kingdom solutions. UK page: "first cloud-native public safety platform" for UK forces; customer quotes from UK chief constables. (A)
- Customer evidence: Scottsdale PD ("reach conclusions and decisions faster, all based on good, accurate data"), Mariposa County SO ("NIBRS and CIBRS reporting... accessible to our deputies while they are out in the field"), Hempstead PD ("write and submit their reports, error free and on-the-go"). (A)

## Product B — NicheRMS365 (large-agency operational platform pole)

### Key observations

- Positioning: "Police Records Management System for Large Agencies"; "The world's most widely used RMS"; "NicheRMS365: The World's Premier Police Operational Platform"; "captures every aspect of policing from the front line to the courtroom." (A)
- **Named module set**: Intelligence Management, Vulnerability Management, General Incident Management, Investigation & Crime Management, Property Management, Forensics Management, Custody Management, Case Preparation & Criminal Justice. (A) — investigation management is a named, isolable module inside the RMS platform (the joint-review packaging point), distinct from case preparation (prosecution-side) and custody.
- **Workflow**: "Configurable built-in workflow sends tasks to individuals or teams, tracks overdue work and manages approvals. NicheRMS365 workflow makes sure that the right work gets to the right people and nothing is forgotten or misplaced." (A)
- **Mobility**: "Train Once, Use Anywhere On Any Device" — same UI on phone/tablet/laptop/desktop. (A)
- **Multi-agency sharing**: "advanced, shared information management among participating agencies... full information about persons, vehicles, or locations across the region is at your fingertips, in real-time"; "Shared or per-agency data management: each agency controls what data is shared"; "Per-agency configuration." (A)
- **Integration**: "full set of common interfaces, including ones to state and national systems"; NicheRMS365 Interface Toolkit. (A)
- **Customer quotations (records-function evidence)**: Toronto Police Service — "streamlines the flow of information from cruisers to courts, eliminates manual transcription and allows officers to create links for suspects, vehicles, addresses, and digitizes property collection, all on officer's mobile devices"; Regina Police Service — "We used to have to send records 45 days before a court date…we now exchange them in real time"; Peel Regional Police — "With a picture of the tattoo and with the search capabilities within NicheRMS, she/we were able to locate a suspect"; Ontario Provincial Police — "the search features are extremely flexible"; North Wales Police — "The improved recording and investigation has led to a rise in detections, particularly people being charged, summonsed and cautioned"; Merseyside Police — "Electronic tasking means...improving the quality and speed of providing victim and witness case progress updates"; Hampshire Constabulary — "more than 70,000 hours of police time will be freed up by NicheRMS"; Temple (TX) PD — "Niche is so singularly focused on the need for records management." (A)
- **UK announcements**: South Yorkshire Police — "modernize crime recording, strengthen data integrity, support compliance with national standards, and help ensure alignment with the Victims' Code"; Durham Constabulary and Warwickshire Police — "centralizes operational data." (A)
- Scale claims: 174k+ sworn officers in over 180 agencies worldwide; 3,000 officers in the average project; 20,000+ users in the largest project. (A — vendor claims, not asserted in final doc)

## Product C — Omnigo Records Management (municipal/institutional suite-module pole)

### Key observations

- Positioning: "Police Records Management Software (RMS)" / "Public Safety RMS"; "built from decades of experience supporting law enforcement"; "Refined Over 30 Years." (A)
- **Record hub**: "links incidents, arrests, citations, and case information in one secure, searchable hub. Integration with dispatch, CAD, and evidence management creates a complete operational picture from initial call to case closure." (A)
- **Capture/store/link**: "Securely capture, store, and link reports, case files, and records in a searchable platform integrated with dispatch and access control." (A)
- **Guided entry**: "Simplify reporting with guided workflows, auto-populated fields, and templates that reduce errors and ensure compliance." (A)
- **Sharing outward**: "Collaborate on reports from any device and share data seamlessly with law enforcement and prosecution systems." (A)
- **Supervision**: "supervisors can easily track report status and accuracy." (A)
- **Regional Data Sharing (RDS)**: "authorized personnel can access relevant information from nearby jurisdictions without needing to contact them directly." (A)
- **Mobile field entry**: "Streamline incident report entry and evidence gathering while on the scene using a mobile patrol app... protecting their personal devices from being opened to discovery in court." (A)
- **Suite context**: Quartermaster Asset Management | Investigation Case Management | Evidence Management | Records Management | Command and Planning | CAD — Records is one named solution among siblings; customer quote: "We don't have a different system for dispatch. We don't have a different system for evidence. We don't have a different system for report writing. It's all in one." (A)
- **Audience**: municipal police departments, campus police agencies, sheriff's offices, public safety units; the platform also serves healthcare/education/gaming/corporate security. (A)
- Customer quote: Signal Mountain PD sergeant — "Since implementing Omnigo Records Management, the time spent on reporting and paperwork has been drastically reduced." (A)

## Product D — CentralSquare Records (public-sector suite pole)

### Key observations

- Positioning: "Records and Digital Evidence Management Systems"; "Input Once, Access Anywhere"; "an interconnected, full suite from the call to the case." (A)
- **NIBRS submission integration**: "Spend less time and submit better NIBRS data with full submission integration." (A)
- **Configurable records system**: "custom fields, forms, modules, dashboards and a built-in report generator"; "customizable, cloud-based solution." (A)
- **Compliance**: "Maintaining NIBRS and CJIS compliance doesn't have to be complex or time-consuming... Our integrated RMS reduces manual entry and reporting time by sharing data across multiple systems"; vendor publishes a CJIS Security Policy document. (A)
- **Records Supervisor persona**: "Increase accuracy and NIBRS compliance with software that easily keeps track of your data" — the records unit is a named user persona. (A)
- **Digital evidence pairing (DEMS)**: "Gather video and sensor data from disparate sources, including body-worn cameras, in-car systems, public and private camera networks. Locate your media quickly based on automatic associations between files and cases"; "automatically synchronized with CentralSquare's CAD and Records." (A) — evidence media management sold alongside Records; custody machinery is the Evidence Management System's territory.
- **Suite**: "Bring 911, CAD, RMS, Jail, and Mobile together in one connected suite"; "True Interoperability... CAD-to-CAD connectivity links agencies and systems in real time." (A)
- **AI**: "automates transcription and report creation, turning hours of work into minutes of review" (Centerline AI). (A — era machinery)
- **Tiered packaging**: Public Safety Suite Enterprise / Pro / ONESolution; Records Enterprise and Records Pro overview PDFs exist (not fetched). (A)
- Scale claim: "More than 8,000 public sector agencies trust CentralSquare." (A — vendor claim)

## Cross-product Comparison

| Dimension | Mark43 RMS | NicheRMS365 | Omnigo Records | CentralSquare Records |
|---|---|---|---|---|
| Unit of record | report (NIBRS/State-IBRS-validated); reports + cases as link targets | incident/crime recording ("General Incident Management"; "modernize crime recording") | reports, case files, records — "incidents, arrests, citations, and case information" | records entered once, "from the call to the case" |
| Compliance machinery | built around NIBRS/State IBRS validation; plain-language error callouts | "compliance with national standards" (UK); data integrity | "reduce errors and ensure compliance" | "submit better NIBRS data with full submission integration"; NIBRS + CJIS |
| Linking / master data | link records, documents, multimedia to active reports and cases | "create links for suspects, vehicles, addresses"; persons/vehicles/locations across the region in real time | links incidents, arrests, citations, case info in one hub | automatic associations between files and cases; "information entered once is available everywhere" |
| Search | real-time access, smart auditing tools | "search features are extremely flexible"; tattoo-photo search anecdote | "secure, searchable hub" | access anytime, anywhere; dashboards |
| CAD relationship | sibling CAD product; Alternate CAD for mixed estates | interfaces incl. state and national systems | "integrated with dispatch" | "from the call to the case"; 911+CAD+RMS+Jail+Mobile suite |
| Arrest/booking side | Booking module (custody events, detainee log) | Custody Management module | arrests as record class | Jail as separate suite product |
| Investigation | not named on RMS page (contrast sample in prior pass) | Investigation & Crime Management module | separate ICM solution | not named on Records page |
| Evidence/property | multimedia linked to reports | Property Management + Forensics Management modules | separate Evidence Management solution | DEMS paired product, auto-synced with Records |
| Field/mobile | mobile-first RMS; OnScene; eCitations | mobile-first, same UI on all devices | mobile patrol app; personal-device protection | Mobile suite product |
| Multi-agency sharing | (not explicit on page) | shared information management among participating agencies; per-agency control | Regional Data Sharing (RDS) | CAD-to-CAD interoperability |
| Workflow/approval | smart auditing tools; validations | configurable workflow: tasks, overdue tracking, approvals | guided workflows; supervisors track report status | streamlined data entry, validation |
| Analytics | Insights, Data Lake | (not detailed on page) | "analyze data trends, identify hotspots" | built-in analytics, customizable dashboards |
| AI | ReportAI, BriefAI | (not on page) | (not on page) | Centerline AI transcription/report creation |
| Security regime | FedRAMP High; ISO (UK) | large-agency regime (not detailed) | secure platform | CJIS Security Policy published |
| Packaging | standalone cloud platform (RMS+CAD+Data) | operational platform with 8 named modules | named module in public-safety suite | tiered suite (Enterprise/Pro/ONESolution) |
| Market anchor | US mid/large; entering UK | UK forces, Canadian services, US counties; 180+ agencies | municipal/campus/sheriff, small-mid | 8,000+ public-sector agencies, North America |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures:

1. **The police event record of record** — a persistent, individually identified, agency-authored official record of a law-enforcement event (incident, arrest, citation), classified in the jurisdiction's offense vocabulary, carrying narrative and structured data. Remove → a dispatch log (transient, CAD's territory) or a report-writing tool with no memory.
2. **The subject index linking records across events** — persons, vehicles, locations, and property held as retrievable master records linked into events with roles, so the agency's history is addressable by subject ("everything about this person/vehicle/place"), not just by event. Remove → a pile of disconnected reports; retrieval-by-subject — the historical core of police records work (the master name index) — collapses.
3. **The official-record discipline** — the record is maintained as the agency's official record under its jurisdiction's rules: standardized, validated entry; commonly supervisory approval before finalization; retention and audit; and the jurisdiction's statistical reporting (NIBRS-class in the US, national crime-recording standards elsewhere). Remove → personal notes or a case-notes archive with no official standing; the "records" in records management stops meaning what courts, oversight bodies, and statistics consume.

Jointly-held is load-bearing: 1 alone = report-writing tool/archive; 2 alone = a person/vehicle registry (intelligence-registry shape); 3 alone = a compliance form machine; 1+2 without 3 = searchable report pile without official standing; 1+3 without 2 = validated archive with no subject retrieval; 2+3 without 1 = registry + compliance with no event record.

Domain anchor: law-enforcement events (offenses, arrests, citations) — separates from fire RMS (response records under fire standards), corrections (custody episodes), court CMS (charges/dockets), and generic government records management (retention discipline over all agency records).

### L1 — Common Mature Structure

Present across the sampled products and expected in the market, but not what makes the Type:

- guided report entry: templates, auto-populated fields (commonly from CAD dispatch data), mobile field capture
- validation against the jurisdiction's statistical standard with user-visible error callouts; submission integration
- supervisory review/approval of reports; report-status tracking
- searchable central repository over the whole record corpus; flexible search (subject, alias, location, property)
- master person/vehicle/location/property records accumulating history (labels, cautions, prior events)
- CAD/dispatch integration; interfaces to state and national systems; prosecution/court sharing
- record classes beyond the incident: arrest, citation, use of force, property/evidence linkage
- role-scoped access and audit under criminal-justice security regimes (CJIS-class in the US)
- multi-agency/regional data sharing under per-agency control
- analytics/dashboards over the record corpus
- configurable vocabulary: custom fields, forms, modules, per-agency configuration

### L2 — Variant / Optional Structure

- packaging: standalone cloud RMS vs operational platform with named modules vs suite module vs tiered editions
- agency scale: very large agencies (multi-thousand officers) to small municipal/campus forces
- jurisdiction: US NIBRS/State IBRS regimes; UK national crime-recording standards and Victims' Code alignment; other national regimes
- deployment: cloud-native vs hosted vs heritage on-premises
- agency type: municipal PD, sheriff's office, state/provincial, federal, campus, port/transportation
- adjacent modules sold beside the records core: booking/custody, jail, digital evidence, intelligence, forensics, case preparation, field mobile apps, AI assistance
- regional data sharing depth: none → bilateral → regional shared databases

### L3 — Vendor-specific (research notes only)

- Mark43: ReportAI/BriefAI, Crime Gun Interfaces, "Alternate CAD" for mixed CAD estates, FedRAMP High tier, "Slash Report Writing Time by up to 80%" marketing figure, Mark43 Fortified
- NicheRMS365: module naming (Vulnerability Management, Forensics Management, Case Preparation & Criminal Justice), Interface Toolkit, SharePoint/DLC customer portal, scale statistics (174k+ officers, 180+ agencies), "world's most widely used RMS" claim
- Omnigo: EverSure support service, Quartermaster asset management, "call open to case close" phrasing, mobile-app personal-device-discovery protection claim, Regional Data Sharing branding
- CentralSquare: Centerline AI, Public Safety Suite Enterprise/Pro/ONESolution tiering, FirstTwo, Unify CAD-to-CAD, Vertex NG911, Sourcewell cooperative purchasing, DEMS solution sheet

## Rejected Findings

- **"RMS = NIBRS reporting machine"** — rejected as definitional: NIBRS/State IBRS is the US realization; UK forces record against national standards with Victims' Code alignment (Niche). The invariant is the official-record discipline under the jurisdiction's rules, not any specific standard.
- **"Investigation management is part of the RMS"** — rejected as identity: it ships as a named module (Niche "Investigation & Crime Management") or separate solution (Omnigo ICM), and the prior pass's vendor statement draws the seam verbatim. Removal test: remove investigation workflow → the RMS remains a records system. Interlocked packaging, not identity.
- **"Evidence/property custody is part of the RMS"** — rejected as definitional: custody chains belong to the Evidence Management System (documented in that pass). RMS products hold property/evidence as linked records (Niche Property Management, CentralSquare DEMS, Mark43 multimedia links); Omnigo and CentralSquare sell evidence management as separate solutions. Remove custody machinery → RMS remains.
- **"Booking/jail is part of the RMS"** — rejected as definitional: CentralSquare sells Jail as a separate suite product; the corrections pass fixes the seam at lawful custody. Mark43 Booking straddles the seam (arrest documentation + custody-event logging) — a packaging realization, recorded as such. Arrest records and booking documentation are RMS record classes; the custody episode is corrections territory.
- **"Cloud-native delivery is definitional"** — rejected: heritage on-premises deployments remain widespread in the installed base (corrections/CAD passes document the same pattern); the UK pole and US pole both include non-cloud heritage.
- **"AI report writing is definitional"** — rejected: era machinery (Mark43 ReportAI, CentralSquare Centerline AI); absent from other sampled products' pages.
- **"Multi-agency regional sharing is definitional"** — rejected: present in 3/4 sampled products but absent from Mark43's page; held as common-to-variant.
- **"Supervisor approval is definitional"** — softened: approval workflows are documented in 3/4 sampled products (Niche approvals, Omnigo report-status tracking, CentralSquare validation) but the evidence does not establish that no RMS can exist without in-system approval; held as standard behavior, not invariant.

## Boundary Findings

- **vs Computer-aided Dispatch / CAD** (processed): CAD owns the live incident and status-tracked units; the RMS owns the post-event official record. The seam is the automatic hand-off of closed incident data into report entry (CentralSquare "from the call to the case"; CAD pass: "automatic data transfer from CAD to records management systems"). Remove real-time unit dispatch → RMS remains; remove the durable classified record → CAD.
- **vs Law Enforcement Case Management** (processed; joint review discharged this pass): the RMS is the agency's record of incidents, arrests, and field documentation kept for statutory and reporting purposes; the case-management Type holds the investigation the report generates — leads, tasks, entity webs, supervised progression to disposition. Vendors state the seam verbatim ("An RMS records incidents and arrests. Case Closed manages investigations... It complements your RMS rather than replacing it"). The market packages investigation management as a named module inside RMS platforms (Niche) — interlocked packaging, not identity. Remove-tests: remove investigation workflow → RMS remains; remove the report-of-record role and add case lifecycle/entity web/supervised investigative progression → the other Type.
- **vs Evidence Management System** (processed): the evidence system of record is the held item — chain of custody, storage, authorized disposition; the RMS holds event records and links property/evidence to them. RMS products pair with evidence systems (CentralSquare DEMS auto-synced with Records; Omnigo separate Evidence Management; Niche Property/Forensics modules). Remove custody machinery → RMS remains.
- **vs Corrections Management System** (processed): the RMS records arrests about people who may never be booked; corrections begins at lawful custody and manages the person while held (housing, counts, movements). Suite vendors sell RMS and Jail as separate products (CentralSquare). Mark43 Booking straddles the seam — arrest/booking documentation inside the records platform, custody-event logging adjacent to jail territory.
- **vs Court Case Management System / Prosecutor Case Management** (court processed; prosecutor unprocessed): downstream consumers. The RMS hands records onward to prosecution and courts (Niche "from the front line to the courtroom", Case Preparation module; Regina quote: records exchange with courts in real time; Omnigo "share data seamlessly with law enforcement and prosecution systems") but does not manage dockets, hearings, or prosecution.
- **vs Fire Department Records / Operations System** (processed): same "agency system of record" family; different domain semantics and standards (NIBRS-class vs NERIS-class; offense classification vs incident response attribution). The fire pass's structure (incident record + resource attribution + department as record owner) parallels this Type's but with different record classes and standards.
- **vs Government Records Management** (unprocessed sibling): agency-wide records lifecycle discipline (retention schedules, disposition over all public records); the RMS produces and maintains one record family — law-enforcement event records — under criminal-justice rules. The RMS is a producer; government records management governs the corpus.
- **vs FOI / Public Records Request Platform** (processed): the request platform manages external requests for records; the RMS holds the records being requested. Downstream consumer relationship.
- **vs Emergency Management Platform** (processed): multi-hazard EOC coordination for large-scale events; the RMS is the day-to-day recordkeeping of one agency's law-enforcement events.
- **vs Animal Control Management** (processed): police-adjacent ordinance enforcement with its own citation/case machinery; integration with police RMS varies by jurisdiction and was not directly observed (that pass recorded it as an uncertainty).
- **Type-boundary verdict**: the leaf stands as a distinct Type. It is not a variant of case management (different unit of record, different lifecycle, vendors name and sell both), not a variant of corrections (booking seam), and not generic records management (domain-specific record classes, offense vocabularies, statistical reporting, criminal-justice security).

## Uncertainties

- Exact report-status vocabularies (draft → submitted → approved → supplemental) were not evidenced at field level from official docs; the final document describes the lifecycle conceptually without asserting specific status names.
- Whether warrant management is a standard RMS record class: Case Closed (case-management pass) documents warrants on the investigation side; no sampled RMS page named warrants directly. Held as common-to-variant, not asserted.
- Depth of NicheRMS365's modules is homepage-evidenced only; module internals not documented.
- CentralSquare Records Enterprise/Pro overview PDFs exist but were not fetched; tier differences not asserted.
- Historical/regional samples (e.g., heritage on-prem RMS products, non-US national systems) could not be fetched this pass; the historical check is reasoned from the defining core (paper-era records room: numbered report file, offense classification, card-index master name file, supervisor sign-off, monthly crime counts, retention — satisfies all three legs) rather than documented vendor history.
- The exact relationship to the unprocessed sibling leaves (Prosecutor Case Management, Public Sector Case Management, Government Records Management) should be revisited when those passes run.

## Final Synthesis

A Police Records Management System is the police agency's system of record for its official law-enforcement records. Its defining core is a triad: the police event record of record (incident, arrest, citation — classified, narrated, structured), the subject index that links records to persons, vehicles, locations, and property across events so the agency's history is addressable by subject, and the official-record discipline under which records are standardized, validated, approved, retained, audited, and reported under the jurisdiction's rules. Around that core, mature products add guided and mobile report entry, CAD hand-off, supervisory review, searchable repositories, statistical submission machinery, prosecution/court sharing, regional sharing, analytics, and configurable vocabulary. The market expresses the Type as cloud-native standalone platforms, large-agency operational platforms with named modules, and suite modules inside public-safety portfolios — with investigation management, evidence custody, and jail/custody episodes as interlocked neighboring Types whose machinery is packaged beside the records core but does not define it.
