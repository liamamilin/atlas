# Research Notes — Government Records Management

## Research Goal

Understand what a Government Records Management application is as an Application Type: what its world consists of, who operates it, how the record lifecycle is governed in the public-sector regime, and how it differs from its nearest neighbors — Enterprise Records Management (the general Type), Enterprise Content Management, FOI / Public Records Request Platform, Archives Management System, and Government Open Data / Transparency portals.

Date: 2026-09-08.

## Initial Boundary (hypothesis before research)

- Core use: agencies must keep records of public business as legal evidence, retain them per legally anchored schedules, and dispose of them (destroy or transfer to archives) only through an authorized, evidenced process.
- Likely users: agency records officers, departmental record coordinators, clerks, archivists, legal counsel, IT.
- Expected confusion zones: (a) Enterprise Records Management — same machinery, different regime; (b) ECM — the working content lifecycle; (c) FOI request platforms — request processing vs record governance; (d) Archives Management Systems — permanent custody vs active lifecycle.
- Prior pass note: the Enterprise Records Management document (2026-09-06) classified Government Records Management as a "regime variant" of ERM and pointed to this leaf for separate documentation. This pass must decide whether the regime delta is audience seasoning or a structural difference, and record the verdict in STATUS.md Boundary Issues.

## Research Questions

1. What are the core objects? (record, retention/disposal schedule, record class/series, disposition action, hold, physical containers/locations, transfers)
2. Who operates the system and how do roles differ from private-sector records management?
3. How does the government retention schedule differ from an organization-defined file plan? (who issues/approves disposition authority?)
4. What is the record lifecycle and its canonical states (active → inactive → cutoff → disposition)?
5. Which endings are possible — destruction, transfer/accessioning to an archives authority?
6. What rules are structurally enforced (no destruction without authority, unlawful destruction, holds, audit)?
7. How is physical (paper/box) records management handled alongside electronic?
8. Where do public records requests and transparency obligations connect?
9. Do older / regional / paper-era products fit the proposed definition? (historical check)

## Representative Products

Selected for market structure spread (postures, geographies, government levels); all evidence at product-page strength unless noted:

| Product | Posture | Government market |
|---|---|---|
| Laserfiche | ECM/document & records platform | US state & local government stronghold (clerk/recorder/official records departments listed in its own demo form) |
| Objective Nexus | Records-centric information-governance suite + process automation | AU/NZ federal & state government, regulated orgs |
| RecordPoint | Cloud manage-in-place records/data governance | Public sector (US + AU); municipal customer cited |
| OpenText Content Manager (ex-HPE Records Manager / HP TRIM lineage) | Classic records-centric government EDRMS | Federal/state governments (AU, UK, US) — **unreachable during research; used only as unverified market reference** |

Regime (domain-authority) sources — these define the statutory machinery the products must serve, and are the strongest available evidence for the government-specific leg:

- NARA (US National Archives) — Federal Records Management FAQs: what records management is (44 U.S.C. 2901), agency/employee responsibilities, life-cycle stages, records schedules as the main disposition tool, schedule approval by the Archivist of the United States, records officers, storage facilities, accessioning.
- State Records NSW (Australia) — recordkeeping resources: Retention and Disposal Authorities ("identify which records ... are required as State archives. They provide approval for the destruction of other records after minimum retention periods have been met"), State Records Act 1998, regulator compliance monitoring.

## Sources

Attempted / used (all fetched 2026-09-08):

- https://www.recordpoint.com/platform/records-management — fetched, product-page evidence
- https://www.laserfiche.com/products/records-management/ — fetched, product-page evidence
- https://doc.laserfiche.com/laserfiche/Default.htm — JS redirect, dead end (1 try, abandoned)
- https://doc.laserfiche.com/laserfiche.documentation/ — redirect shell only
- https://support.laserfiche.com/ — generic support portal, no RM operational content
- https://www.opentext.com/products/content-manager — HTTP 444 blocked (1 try, abandoned)
- https://docs.microfocus.com/doc/Content_Manager/23.4/ContentManagerHome — portal shell only, no content (1 try, abandoned)
- https://www.hyland.com/en/solutions/government — HTTP 403 blocked (1 try, abandoned)
- https://www.archives.gov/records-mgmt/faqs — index, fetched
- https://www.archives.gov/records-mgmt/faqs/general.html — fetched, full content
- https://www.archives.gov/records-mgmt/faqs/rcs.html — fetched, full content
- https://staterecords.nsw.gov.au/recordkeeping — fetched, page-level evidence for RDA machinery
- https://www.tsl.texas.gov/slrm/records/schedule — 404 (1 try, abandoned; not needed — NARA+NSW sufficient for cross-jurisdiction support)

Prior-pass reuse: none directly; boundary alignment against applications/enterprise-records-management.md and applications/foi-public-records-request-platform.md (read 2026-09-08).

## Product Observations

### RecordPoint (evidence layer A, product-page wording strength)

Official records-management platform page states:

- "Centralize records management across all your systems" — connects to Microsoft 365, file shares, legacy archives, cloud platforms; manage-in-place over connected sources.
- "using AI and ML to classify records at scale and reduce human error"; "rules-based logic and machine learning to classify records and apply retention policies consistently across both structured and unstructured content."
- "RecordPoint automatically enforces retention schedules, supports legal holds, and captures audit trails so you can demonstrate compliance."
- "Defensible disposal you can prove — ... automated disposal that lets you capture complete audit trails, apply legal holds, and demonstrate compliance."
- "Unlike tools that rely on periodic scans, RecordPoint applies policies instantly ... governance happens in real-time."
- Platform modules beyond RM: data discovery & classification, data lifecycle management, data permissions, data minimization, risk detection & reporting, compliance, DSAR management, **FOIA management**, AI governance (RexCommand), application retirement. Public-sector solution page listed.
- Customer quote from a "Large municipal organization in North America" (Records Analyst): "With RecordPoint, disposition, authorization, and approval are at my fingertips" — municipal government is a live customer segment; disposition + authorization + approval named as the working loop.

Observations for the model: manage-in-place posture; schedule → classification → protection → disposal-with-proof loop; holds; audit; FOIA as an adjacent bundled module; local government customer.

### Laserfiche (evidence layer A, product-page wording strength)

Official document-and-records-management product page states:

- "Store documents in a centralized repository with audit trails, granular access controls and version history."
- "Records requests: Easily deliver records to citizens or customers with a secure link, and track when and how content is accessed." — the public-facing delivery leg exists inside the same platform.
- AI: "identify, classify and extract information from scanned and digital documents"; document summarization.
- Solutions: "Case management: Capture and securely share requested case data to speed response times and ensure compliance."
- Demo form's own department list includes "Clerk/Recorder/Official Records", "Records Management"; industries list "State, Local, or Regional Government", "Federal and National Government" — confirms the local-government center of gravity.
- Marketing-level claims only for retention/disposal specifics; no operational retention-schedule mechanics visible on reachable pages.

Observations for the model: ECM-platform-with-records posture; citizen-facing records delivery; audit trail; government department fit (clerks). Operational schedule machinery not directly observed — keep at wording strength.

### Objective Nexus (evidence layer A, product-page wording strength)

Official product page states:

- Positioning: "information governance solution providing records compliance, enterprise scale information management and process automation ... designed to meet the needs of modern government agencies and regulated organisations."
- Records management: "Manage the complete records lifecycle from creation to disposal or transfer. Aggregate and manage both physical and electronic content by adding an automated unobtrusive layer of rules, protection, policy, and control to all content. And importantly, in a manner that is transparent to business users while remaining standards-compliant."
- File plan present: "Determine who can see, open, edit, share externally and delete by individual documents or at any level in your file plan."
- Security: policies per users/roles/groups/classifications/projects/caveats.
- Audit: "who did what, and when; both on-screen views and detailed reports show every action"; approvals captured from Teams/email as evidence.
- Capture/governance: M365 (Teams, SharePoint, Exchange) "automatically captured and classified in your system of record"; LOB integration (CRM, financial, HR).
- Process automation: correspondence management, procurement/policy approval, **freedom of information requests**, **Ministerial briefings**, HR onboarding — government-shaped workflows around content.
- Delivery: on-prem, hosted, SaaS; "Designed specifically for government agencies".

Observations for the model: records-centric system-of-record posture; disposal **or transfer** named as the two endings; physical+electronic aggregation; file plan; transparent-to-users governance; FOI/correspondence/ministerial workflows as the bundled government process layer.

### OpenText Content Manager — unverified market reference (no direct evidence)

- opentext.com blocked (444); Micro Focus docs portal renders content by JS only. Known in the market as the records-centric government EDRMS lineage (TRIM). **No operational claims are made from this product anywhere in this research.** The ERM pass (2026-09-06) recorded the same inaccessibility.

### NARA (US federal regime) — evidence layer A, authoritative domain source

From the General FAQs and Records Control Schedule (RCS) FAQs:

- Definition (44 U.S.C. 2901): records management = "systematic control of the creation, maintenance, use, and disposition of records"; life cycle = creation/receipt → maintenance and use → disposition.
- Tools: "file plans, indexes, controlled vocabularies, taxonomies, data dictionaries, and access and security procedures. The main tool used to manage the disposition of records is the records schedule."
- **External disposition authority**: records schedules are approved by the Archivist of the United States (SF-115 paper lineage; ERA digital submissions carry DAA job numbers; approval date = date the Archivist signed). "Federal agencies cannot use inactive items for disposition." Withdrawn/rescinded items likewise unusable; the Archivist may rescind an approved disposition authority (44 U.S.C. 2909, 36 CFR 1226.16).
- General Records Schedules (GRS) exist as government-wide schedule items.
- Agency obligations (44 U.S.C. 3101–3106): make/preserve adequate documentation; maintain a records program; safeguard against removal/loss; **notify the Archivist of any actual, impending, or threatened unlawful destruction of records**.
- Employee obligations: create records, maintain them for retrieval, "carry out the disposition of records under their control in accordance with agency records schedules and Federal regulations."
- Roles: Agency Records Officers (NARA credential/training policy exists), NARA appraisal archivists, Senior Agency Officials; oversight/inspection program; agency reporting to NARA.
- Physical infrastructure: Federal Records Centers (FRC) for inactive records storage; Records Storage Facility Standards; accessioning guidance for permanent records; Electronic Records Archives (ERA) for electronic transfer.
- Appraisal: NARA determines which records have enduring value (permanent) vs temporary.

Observations for the model: the government regime's defining machinery is that **the schedule's authority sits outside the operating agency** — disposition is lawful only under externally approved items, destruction violations are reportable to the oversight archives, and permanent records end in transfer (accessioning) to the archives authority rather than destruction.

### State Records NSW (AU state regime) — evidence layer A, page-level

- "Retention and Disposal Authorities identify which records created and received by NSW public offices are required as State archives. They provide approval for the destruction of other records after minimum retention periods have been met." — same structure as NARA: external authority issues the instrument; archives-vs-destroy split; destruction needs approval.
- State Records Act 1998 as the statutory base; State Records NSW acts as regulator ("Our Regulatory Framework describes our approach to regulating records management, and how we intend to use the powers in the State Records Act"); compliance monitoring exercises ("Recordkeeping Monitoring Exercise", mandatory in 2026), Records Management Assessment Tool, records managers forums.

Observations for the model: cross-jurisdiction confirmation (a second legal system, different country) that the external-authority + archives-transfer + regulated-compliance structure is the government regime, not a US quirk. (UK/other Commonwealth systems are widely described as analogous in the literature but were not directly fetched — noted in Uncertainties.)

## Cross-product Comparison

| Dimension | RecordPoint | Laserfiche | Objective Nexus | Regime sources (NARA / NSW) |
|---|---|---|---|---|
| Records lifecycle governed creation → disposal/transfer | yes (data lifecycle mgmt; disposal) | yes at marketing level (records mgmt platform) | explicit: "creation to disposal or transfer" | life cycle: creation → maintenance/use → disposition |
| Retention schedule | "automatically enforces retention schedules" | implied (records management product; not operationally observed) | file plan with rules/policy per level | records schedule = main disposition tool (NARA); RDA = the instrument (NSW) |
| Who anchors the schedule | customer-configured (wording) | customer-configured (wording) | customer-configured (wording) | **external statutory authority issues/approves disposition authority** |
| Record protection | governed content; holds | granular access controls, audit trails | "rules, protection, policy, and control"; who can edit/delete per file plan level | safeguards against removal/loss (statutory duty) |
| Disposition proof | "defensible disposal you can prove"; audit trails | audit trails | "demonstrate every action"; time-stamped approvals | disposition only under approved items; unlawful destruction reportable |
| Physical records | unstructured+structured content claim; physical not explicit on page | not explicit on page | "Aggregate and manage both physical and electronic content" | FRC storage standards (NARA); paper-era machinery |
| Capture/integration | M365, file shares, legacy archives, cloud platforms; ML classification | AI capture/classification | M365 auto-capture into system of record; LOB integration | n/a (regime) |
| Endings | automated disposal; holds suspend | not directly observed | disposal **or transfer** | destroy (with authority) or transfer/accession to archives (permanent) |
| Public-facing leg | FOIA management module | records requests to citizens via secure link | FOI request workflow; ministerial correspondence | FOI statutes; public accountability |
| Government center of gravity | public sector solutions; municipal customer | state & local; clerk/recorder departments | "designed for government agencies" | the regime itself |

Reading of the comparison:

- The **RM spine** (records under governance + schedule + evidenced disposition with holds/audit) is common to all sampled products — it is the inherited ERM machinery.
- The **government regime delta** (external statutory disposition authority; destroy-or-transfer endings; regulated compliance monitoring; public accountability) is carried by the domain sources in two jurisdictions and visibly shapes the products (FOI modules, ministerial workflows, municipal/Federal positioning, "disposal or transfer" wording, municipal analyst describing "disposition, authorization, and approval").
- Precise operational mechanics (certificate steps, review-chain counts, cutoff procedures, box-location schemas) were NOT reachable in product help documentation for any sampled product — all such specifics stay out of claims entirely.

## Canonical Model (abstraction levels)

### L0 — Defining Invariant

The Type holds three structures jointly:

1. **Agency records as evidence of public business** — identified content under record governance: while governed, change and deletion are controlled by the governing rules, not ordinary user discretion. Remove → not records management at all (becomes document storage).
2. **A legally anchored retention and disposal schedule operating under external statutory authority** — the schedule assigns classes of public records to retention periods and disposition actions, but (the government-specific property) the disposition authority is issued by, or formally approved by, an archives/records oversight authority outside the operating agency; destruction is lawful only under an approved schedule item. Remove the external-authority property → Enterprise Records Management (general Type).
3. **Governed, evidenced disposition ending in destruction or transfer** — disposition is an authorized, reviewable, evidenced act with recorded proof; for material of enduring (permanent/archival) value the ending is transfer to the archives authority, not destruction. Remove → document management with retention labels; remove the transfer ending → the archival half of public recordkeeping collapses.

Joint-hold test: schedule without record state = a policy document; record state + schedule without external authority = ERM; authority + schedule without evidenced disposition = compliance paperwork with no governed end.

### L1 — Common Mature Structure

Very common in current products, not definitional:

- classification/declaration machinery (manual, rules-based, ML) applied to capture and filing
- legal holds / freezes suspending disposition
- audit trails ("who did what when") and compliance/proof reporting for oversight and auditors
- event-based retention triggers (case closed, employee separated, contract ended) with cutoff semantics
- physical records machinery (containers/boxes, storage locations, circulation, transfers to storage facilities) alongside electronic
- capture/integration from collaboration and line-of-business systems into the system of record
- records-officer / departmental-coordinator role separation
- disposition review/approval workflows, often multi-step, producing disposal certificates/reports
- search and retrieval across the governed record population
- connected public-access surfaces: FOI/public-records-request handling, citizen-facing records delivery

### L2 — Variant / Optional Structure

- packaging posture: records module inside an ECM suite; records-centric EDRMS (system of record + process automation); cloud manage-in-place governance layer; physical-records-first vendors
- jurisdiction/regime shape: US federal (national archives approval, government-wide general schedules, federal records-center storage, accessioning), US state/local (state-issued local-government schedules), AU/NZ/Commonwealth (retention & disposal authorities under state/public records acts), UK and others (analogous, not directly verified in this pass)
- certification/testing regimes for records functionality (defense-type standards) — historically significant in this market; current certification claims not verified, not asserted
- digitization programs converting paper holdings into governed electronic records
- essential/vital-records and disaster-recovery programs
- bundled government process automation (correspondence, ministerial/briefing workflows, agenda/clerk processes)
- privacy/DSAR minimization and AI-governance extensions (current-market layer)

### L3 — Vendor-specific (research notes only)

- RecordPoint: connectors library, Data Permissions Assurance, RexCommand (AI governance), application-retirement and data-minimization modules, FOIA module as a named product surface.
- Laserfiche: department-specific solution templates (clerk/recorder/official records), Solution Marketplace, Aspire training platform, LF12 release branding; analyst-quadrant marketing.
- Objective: suite split (Nexus / 3Sixty / Connect / Redact / Keystone / RegWorks), caveat-based security vocabulary, ministerial-briefing solution packaging.
- OpenText Content Manager: TRIM heritage, long government certification history — **unverified this pass; do not cite**.

## Historical / Market-Sample Check

Paper-era government records practice satisfies the L0 skeleton: a file room of records (leg 1), a retention schedule issued/approved by the state archives or equivalent authority with typed disposition authorities (leg 2), destruction certificates and box transfers to the records center/archive (leg 3). No digitization, ML classification, connectors, or even a database is required. Regional check: the two directly verified jurisdictions (US federal, NSW state) instantiate the same three-leg structure with different terminology; the definition does not depend on SF-115s, GRAs/RDAs, FRCs, or any specific instrument name. Digital-only assumptions are therefore excluded from the definition, and physical-records capability is treated as common mature structure rather than optional garnish.

## Vendor-specific Findings

See L3 above. Additionally: RecordPoint's municipal-customer quote describes the working loop as "disposition, authorization, and approval" — single-product anecdote, not promoted to canonical. Objective's "disposal or transfer" phrasing is the cleanest product-page confirmation of the two canonical endings (single product; consistent with both regime sources — treated as convergent, B-layer support).

## Boundary Findings

| Neighbor | Test | Verdict |
|---|---|---|
| Enterprise Records Management | Remove the external statutory disposition authority (schedule approval/issuance outside the agency) → ERM. Remove "government regime" seasoning only (terminology, oversight reporting) → still ERM | The structural delta is the external-authority property. This is more than audience seasoning (it changes who owns the schedule instrument and what makes destruction lawful) but the core spine is shared. Separate leaf defensible; alias claim also defensible. **Record for joint review.** |
| Enterprise Content Management | Center of gravity: working content lifecycle (capture/collaborate/version/publish) vs retention/disposition governance | Distinct; products ship both, per the ERM pass |
| FOI / Public Records Request Platform | Object of management: the external request + its statutory clock vs the record population + its schedule | Distinct Types that interlock; FOI modules bundle into records products (RecordPoint FOIA module, Objective FOI workflow, Laserfiche records requests) without becoming the same Type |
| Archives Management System | Lifecycle position: active/inactive governance ending in transfer vs permanent custody, preservation, and public access to material of enduring value | Distinct; the records system hands off to the archive at accessioning |
| Government Open Data Portal / Transparency Portal | Publishing datasets/meetings proactively vs governing records of business | Distinct; different object and lifecycle |
| Document Management | Filing/versioning convenience vs schedule-bound governance and lawful disposition | Distinct |
| Legal Hold Management | The hold primitive is shared; LHM centers the preservation-duty process across sources, not the record schedule | Distinct consumer of the same primitive |

## Taxonomy Problem (for STATUS.md Boundary Issues)

The directory carries both "Enterprise Records Management" (§10) and "Government Records Management" (§24). The ERM pass labeled this leaf a "regime variant ... documented separately in this directory". This pass finds: the three-leg core spine is identical to ERM, but the government regime embeds one structurally distinctive property — disposition authority sits with an external statutory archives/records authority, making destruction lawful only under approved schedule items and making transfer-to-archive a canonical ending. Verdict: keep both leaves (audiences, procurement, jurisdiction shape, and product landscapes differ), but recommend joint review ratify the pair as **regime-specialized siblings** with the external-authority property as the declared seam, rather than aliasing them. No silent directory change made.

## Uncertainties

1. No Tier 1 operational help documentation was reachable for any sampled product (Laserfiche doc portal is JS-rendered; OpenText/Micro Focus blocked; Hyland blocked). All product-level statements are product-page wording strength; no precise operational flows (destruction certificate steps, review chain depth, cutoff mechanics, box-location schemas) are asserted anywhere.
2. The external-authority leg is directly verified in two jurisdictions (US federal via NARA; AU state via State Records NSW). Other jurisdictions (UK TNA, Canadian provinces, US state archives) are described analogously in the literature but were not fetched in this pass — the document therefore states the structure generically and avoids instrument names.
3. Whether current products' government certifications (defense records standards lineage) hold today was not verified; no certification claims are made.
4. OpenText Content Manager — the classic records-centric government EDRMS — could not be verified at all; it is kept as an unverified market reference only.
5. Whether this leaf should remain a separate Type or be an ERM alias is a genuine judgment call (see Taxonomy Problem); resolved as "separate leaf + boundary issue for joint review", not unilaterally.

## Final Synthesis

A Government Records Management application governs an agency's records as evidence of public business: content placed under record governance, classified and retained under a legally anchored retention and disposal schedule whose disposition authority is issued or approved by an external statutory archives/records authority, protected against change and loss, suspended by legal holds, and ultimately disposed of through an authorized, evidenced process that ends in certificated destruction or transfer to the archives authority — with the whole apparatus auditable by oversight bodies and answerable to public-records law. The inherited RM spine is shared with Enterprise Records Management; the government regime's distinguishing property is the external statutory disposition authority (with its destroy-or-transfer endings and regulated compliance). Mature products add classification automation, holds, audit trails, event-based retention, physical-records machinery, capture/integration, role separation, and public-access surfaces (FOI/records delivery); packaging spans ECM-suite modules, records-centric EDRMS, manage-in-place SaaS, and physical-records-first vendors.
