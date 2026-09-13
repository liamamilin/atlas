# Research Notes — Clinical Trial Site Management

## Research Goal

Understand the software category operated by **clinical research sites** — dedicated research sites, site networks/SMOs, hospital/health-system research departments, academic medical centers and cancer centers — to run their clinical research operations and business, and determine how this directory leaf relates to its processed sibling **Clinical Trial Management System / CTMS** (researched 2026-09-07), whose notes left an explicit joint-review flag: "site-operated products self-label CTMS … either confirm the pole-variant framing or split by operator object (trial-operational system vs site-business management)."

## Initial Boundary

Working hypothesis at start:

- This leaf refers to software whose operator/subject is the **research site organization** — the place where trials are conducted — not the trial itself.
- Its nearest neighbors: CTMS (sibling leaf, same product population), Clinical Trial Recruitment Platform (processed; sponsor-side funnel), eRegulatory/eISF and eTMF (document systems), EDC/eSource (data capture), patient scheduling/practice management (care-side), research administration/grant management (institutional pre-award).
- Known risk: the market's site-side products self-label "CTMS" (RealTime-CTMS, Advarra Clinical Conductor, OnCore), so the boundary question is whether this leaf is a distinct Type (operator-object inversion: site-business management) or the site/institution pole of the CTMS Type under an alias label.

## Research Questions

1. What is the central object for a site-side system — the study, the site, the participant?
2. How do studies arrive at a site (sponsor/CRO-originated demand), and what does the site track before first participant in (feasibility, contract, budget, start-up)?
3. What does the site's participant operation look like (database, recruitment funnels, screening, enrollment, visits, retention)?
4. What site-owned resources exist as first-class objects (staff, exam rooms/locations, participant panel)?
5. How does the site's money work: budgets/contracts, visit/procedure/milestone billing, receivables, sponsor reimbursements, participant stipends, billing compliance?
6. What regulatory-document duties sit at the site (eISF/essential documents, inspection readiness, monitor access)?
7. What changes at network/enterprise scale (multi-site rollups, opportunity distribution, BI)?
8. How does this differ from sponsor/CRO CTMS, recruitment platforms, eRegulatory, EDC, EMR scheduling?

## Representative Products

Selected for market coverage across operator types and product philosophies (all official sources, fetched 2026-09-07):

| Product | Vendor | Operator pole | Philosophy |
|---|---|---|---|
| RealTime-CTMS / SOMS / Devana | RealTime Software Solutions (RealTime eClinical Solutions) | dedicated sites, SMOs, site networks, AMCs/health systems | site-operations suite ("Site Operations Management System"), recruitment+finance-led, explicit "beyond traditional CTMS" framing |
| Site CTMS | CRIO (Clinical Research IO) | independent sites, site networks, academic research, DCT | modern site-centric platform: eSource-led with Site CTMS + eRegulatory modules |
| Clinical Conductor CTMS | Advarra | research sites, site networks, hospitals, health systems | "run your research as a business" — profitability/financial-recovery-led |
| OnCore CTMS | Advarra | academic medical centers, cancer centers, some health systems (50–500+ active trials per vendor FAQ) | institutional: protocol lifecycle, billing compliance, enterprise integrations |
| Florence platform (eBinders / Site Feasibility / SiteLink) | Florence Healthcare | 88,000+ research sites (vendor claim), 90 countries | **boundary sample**: "Site Enablement Platform" — document workflows, feasibility response, sponsor exchange; no CTMS operations/finances |

## Sources

All fetched 2026-09-07 (Layer A unless noted):

- RealTime eClinical Solutions — homepage, CTMS solution page, Devana product page: https://realtime-eclinical.com/ , https://realtime-eclinical.com/solutions/ctms/ , https://realtime-eclinical.com/solutions/devana/
- CRIO — homepage, Site CTMS product page: https://clinicalresearch.io/ , https://clinicalresearch.io/products/site-ctms/
- Advarra — Clinical Conductor page, OnCore page: https://www.advarra.com/solutions/sites/ctms/clinical-conductor/ , https://www.advarra.com/solutions/sites/ctms/oncore/
- Florence Healthcare — homepage, Florence for Sites: https://www.florencehc.com/ , https://www.florencehc.com/florence-for-sites/
- Context (prior pass, 2026-09-07): research/clinical-trial-management-system-ctms.md and applications/clinical-trial-management-system-ctms.md (Clinion sponsor-pole evidence; suite context).

Sourcing limitations: deep user manuals / admin guides for all four management products sit behind customer logins or were not indexed publicly; evidence is predominantly official product pages, FAQ text, and annotated product screenshots. Precise operational parameters (exact visit-window rules, invoice defaults, permission matrices) are therefore NOT asserted anywhere. Enterprise sponsor-side eClinical suites (Veeva Vault CTMS, Medidata, Oracle) remained unfetchable (same transport failures recorded in the CTMS pass); the sponsor-side reading of "site management" is treated through the CTMS document, not re-researched here. Vendor-published scale claims (3000+ sites, 600,000+ visits/year, 88,000+ sites, "9 of 10 top site networks", ROI percentages) are marketing claims and are kept out of the Application Document.

## Product Observations

### RealTime eClinical Solutions (RealTime-CTMS, SOMS, Devana)

Key observations (Layer A):

- Suite is explicitly framed for **"Sites, Networks, SMOs, AMCs & Health Systems"** with a separate sponsor/CRO product line; self-description: "purpose-built to empower clinical research sites to streamline all aspects of trial execution, including recruitment, CRC activities, finances, site management, and more"; company tagline: "Manage the research and business of clinical trials, together." Demo-form company-type taxonomy: Academic Medical Center, CRO, Health System/Hospital, Integrated Research Organization, Physician Practice/Group, Single Site, Site Management Organization, Site Network, Sponsor — a useful map of the operator universe.
- Bundled suite branded **SOMS ("Site Operations Management System")** — the vendor coinage for the site-operated category; footer claims platform "goes beyond traditional CTMS".
- **Recruitment**: grow a patient database via website integration, Facebook ads, SubjectWell-class integrations; view upcoming/overdue visits and pending actions; electronic visit log; "remarket directly from your database" per new study (Mailchimp email blasts, mass texting); web tools to list enrolling studies, build landing pages, run pre-screening; "Instant CTMS sync creates subject profiles automatically from website form submissions".
- **CRC management**: automated study target dates and **window calculations**, text reminders, Outlook integration, task alerts/notifications, visit tracking logs, prescreening logs, staff-productivity reporting.
- **Study finances**: contracts and budgets with "study procurement milestone tracking", accounting for simple and complex study budgets, **automated screen-fail ratio and max tracking** (budget compensation caps), study milestone payment tracking, automated earnings/expenses/receivables/payables at visit and study level, custom report builder (inSites) for collections, study financial reconciliation, company-level financials.
- **Enterprise CTMS** (network tier): centrally manage sites/studies/personnel/finances "in over 30 countries", aggregate reporting with built-in BI connectivity, unlimited user profiles, MFA + SAML, single-click launch into per-site study areas, network-wide enrollment drill-down.
- **Devana** (separate product, network/business layer): pipeline management — "track and monitor new trial leads from CROs and sponsors", auto-log business-development emails/calls tied to trial opportunities; automated study start-up — milestones "from CDA and Award Letter to Site Activation"; timing metrics for contract/budget turnaround; import screening/enrollment data from CTMS; dashboards to "impress sponsors … helping win more opportunities"; **Devana Enterprise for site networks**: distribute new trial opportunities to sites within the platform, collect site interest responses, PI/site selection "based on capabilities, therapeutic expertise, physical site facilities", track site startup/screening/enrollment centrally. Devana integrates with third-party CTMS (shows RealTime, CRIO, Clinical Conductor logos).
- Companion modules: eReg/eISF, eSource (sites & AMCs; separate sponsor/CRO line), Engage! (MyStudyManager participant portal, eConsent), SitePay (digital participant payments), Text (two-way patient communication/reminders), GlobalPay (sponsor-side site payments/study funding), TrialAlign (sponsor-side site selection), mobile app, API/integrations.

### CRIO (Site CTMS)

Key observations (Layer A):

- Product literally named **"Site CTMS"**: "The site clinical trial management system (CTMS) software that seamlessly integrates with your eSource platform to streamline site operations"; homepage FAQ: "Beyond eSource, CRIO connects the full site workflow: eConsent, eRegulatory, and CTMS all live within a single platform."
- Serves **Sites** (Site Networks, Independent Sites, Academic Research, DCT) plus Sponsors/CROs (via Central eSource).
- **Patient recruitment**: "Manage your patient database, search for patients that meet feasibility criteria, and have website leads come in automatically"; in-system calls and texts "to move patients through the funnel"; interactive phone-screening questionnaires; book patients for special prescreening visits; recruitment-vendor partnerships.
- **Finance**: "Set visit or procedure-level receivables, patient stipends, and payables in different currencies; generate and automatically track invoices and payment vouchers; record and reconcile sponsor reimbursements; support GAAP and financial reporting requirements."
- **Patient stipends**: cash-card payments (Dash Solutions), configurable stipend amounts, prepayments, 1099 year-end reporting.
- Annotated **schedule screenshot**: calendar day view listing per-patient appointments with time ranges, visit labels ("Visit 1 – Screening", "Visit 2 – Treatment", "Unscheduled Visit", "Baseline"), **exam-room assignment** ("Exam Room 1/2/3"), and per-appointment status ("READY").
- eConsent integrated into eSource visit flow (in-person or remote signature launch with PIN by phone/email).
- Compliance badges: HIPAA, EU Annex 11, FDA, GDPR, GCP, WHODrug.

### Advarra Clinical Conductor CTMS

Key observations (Layer A):

- Positioning: "A scalable CTMS designed to optimize operational and financial efficiency for **research sites, site networks, hospitals, and health systems**."
- Value pillars: "Boost profitability — **run your research as a business** with budgeting, billing, and reporting tools designed specifically for clinical research sites"; "Enhance visibility"; "Streamline enrollment — patient recruitment and enrollment tools"; "Improve participant engagement"; "Connect your technology and EHR".
- Customer-evidence themes (site operators): "recovered in unbilled payments" (health-system research business analyst: "manual reconciliation would have been prohibitive"); dashboards "especially helpful with audits"; "real-time visibility into patient journeys across all sites, real-time financial projections and compliance monitoring"; "manage appointments and stipends from a single screen".
- Participant-engagement add-ons: **CCText** (CTMS-embedded two-way texting, HIPAA-compliant, for health systems/hospitals/networks/sites), **CCPay** (real-time reimbursements to secure debit cards issued and tracked in the CTMS, with payment analytics).
- Integrations: Advarra eReg (21 CFR Part 11 eRegulatory/eConsent), Advarra eSource+EDC, Epic, APIs.
- Customer logos: large site networks (Velocity, Alcanza, CCT), health systems (Norton, Ascension), integrated research organizations (Javara, Tekton).

### Advarra OnCore CTMS

Key observations (Layer A):

- Positioning: "built in collaboration with leading **academic medical centers and cancer centers**"; FAQ: "typically addresses the needs of academic medical centers and cancer centers, as well as some health systems, conducting fifty to 500+ active trials" (vendor's own segmentation statement).
- Pillars: **compliant billing processes** ("centralize billing information … simplify routing across teams and systems"); research operations management with financial oversight; **EMR integration** ("Epic or Cerner … patient safety, billing compliance, operational efficiency"; RPE integration for protocol/subject information; IHE CRPC billing designations); protocol lifecycle management ("protocol setup and activation to subject screening, registration, and study close-out"); dashboards co-developed with the Onsemble customer community.
- Integration list: CRPC Billing Grid (EMR), demographics (EMR), subject/protocol information (EMR), general ledger, eIRB (via OnCore API), Advarra eReg, Advarra eSource, Advarra Analytics, Advarra Payments.
- **Biospecimen management** as separately licensed module; enterprise license includes clinical research management + billing compliance.
- Customer logos: Yale, Inova, University of Florida, Michigan, Rochester, Medical College of Wisconsin; billing-compliance quote from Yale center leadership.

### Florence Healthcare (boundary sample — Site Enablement Platform)

Key observations (Layer A):

- Self-label: **"Site Enablement Platform"**; "automates document workflows and participant journeys … while providing remote access to sponsors and CROs"; claims 88,000+ sites in 90 countries (vendor claim).
- Site-side products: **eBinders** ("Digitize, automate, and integrate your investigator site files, participant binders, and logs — while providing remote monitoring for sponsors and CROs"), **Site Feasibility** ("Faster, more consistent feasibility responses for research sites" — AI-powered assessments), **eConsent**, **StudyOrganizer** (free study bookmarks/passwords/contacts manager).
- Sponsor-side counterparts: SiteLink (document exchange + remote monitoring), eTMF, Contracting (CTA negotiation).
- Site outcome claims: faster study start-up, "100% document inspection readiness", increased study capacity.
- Explicitly integrates **with** "your CTMS, EDC, eReg solution, identity providers" — i.e., Florence is adjacent to, not a member of, the site-management category; it holds no participant visit operations, no enrollment operations, no site finances.

## Cross-product Comparison

| Dimension | RealTime-CTMS | CRIO Site CTMS | Clinical Conductor | OnCore | Florence (boundary) |
|---|---|---|---|---|---|
| Operator subject | site/network/AMC/health system (explicit) | sites: networks, independent, academic, DCT | sites, networks, hospitals, health systems | AMCs, cancer centers, health systems | sites & networks (enablement only) |
| Study portfolio from sponsors/CROs | yes; Devana tracks leads/opportunities & start-up milestones | implied (site conducts sponsor studies; recruitment partnerships) | yes ("run your research as a business") | yes (50–500+ active trials; protocol setup→activation) | studies present as document contexts + feasibility responses |
| Site-owned participant database | yes (grow/remarket database) | yes (database + feasibility-criteria search) | yes (patient lists, recruitment tools) | less prominent (subject registration per protocol) | no |
| Recruitment machinery | deep (web/ads/prescreening/remarketing) | deep (funnel, calls/texts, questionnaires) | deep (recruitment/enrollment tools, CCText) | not headline | no (eConsent only) |
| Visit ops w/ protocol windows | yes (auto target dates & window calculations) | yes (schedule w/ visit labels & statuses) | yes (appointments, no-show reduction) | yes (subject screening/registration; visit lifecycle) | no |
| Exam-room/location resources | phase-I oriented suite | yes (screenshot: exam-room per appointment) | not surfaced | not surfaced | no |
| Staff workload/productivity | yes (staff productivity reporting) | not headline | yes (staff visibility themes) | effort/accrual analytics | no |
| Site finances (budget→billed→paid) | yes (visit & study level; screen-fail caps; receivables/payables) | yes (visit/procedure receivables, invoices/vouchers, sponsor reimbursements, GAAP) | yes (headline: budgeting, billing, unbilled recovery) | yes (billing compliance, GL, financial management) | **no** |
| Participant stipends | yes (SitePay) | yes (cash cards, 1099) | yes (CCPay debit cards) | Advarra Payments listed | no |
| Regulatory docs / inspection readiness | eReg/eISF module | eRegulatory module | Advarra eReg integration | Advarra eReg + eIRB API | core purpose (eISF/eBinders) |
| Monitor/sponsor access | eReg/eSource connectivity | eSource remote monitoring | eReg integration | eReg integration | core purpose (SiteLink) |
| Billing compliance (payer-correct billing) | not surfaced | not surfaced | not headline (Ascension is a health system) | headline (CRPC billing grid, EMR routing) | no |
| Pipeline / business development | yes (Devana) | not in this product | not surfaced | not surfaced | feasibility response only |
| Network/enterprise rollup | yes (Enterprise CTMS, Devana Enterprise) | site networks served | network oversight framing | enterprise license | network case studies |
| EMR integration | not headline | not headline | yes (Epic) | yes (Epic/Cerner, RPE, CRPC grid) | no |
| eSource/EDC | companion module | core platform | companion | companion | no |

Stable commonalities across all four management products (Layer B): site organization as the operator subject; a portfolio of externally sponsored studies each carrying its own budget/billing relationship; per-study participant operation (screening → enrollment → visits) recorded in the system; regulatory-document coordination and inspection readiness; participant communication; reporting/dashboards; integrations outward (EMR, document systems, IRB/eIRB, ledger).

Pole-dependent structures (Layer B, partial): recruitment-database-and-funnel depth (strongest in RealTime/CRIO/Clinical Conductor, muted in institutional OnCore); billing-compliance machinery (headline only in institutional OnCore); pipeline/BD layer (RealTime Devana; feasibility-response in Florence); exam-room resources (observed directly at CRIO only); network opportunity-distribution (Devana Enterprise).

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which software stops being recognizable as clinical-trial site management:

```text
The research site organization (operator subject: single site, SMO/network,
hospital/health-system department, academic center)
└── Study portfolio: externally sponsored studies as the site's managed demand,
    each tracked through the site's own lifecycle
    └── Per-study record of conducted operation
        (participants screened/enrolled, visits due/done, staff work performed)
        └── The site's side of the money per study
            (negotiated budget → billed → paid; stipends paid out)
```

Four properties; removal tests:

- Remove the **site as subject** (invert to study-as-subject with sites as resources) → sponsor/CRO CTMS view. Still eClinical, but this Type's subject is gone.
- Remove the **portfolio of externally sponsored studies** (no sponsor-originated demand object) → clinic/practice scheduling or generic operations software.
- Remove the **recorded per-study operation** (no participant/visit/work record) → a CRM or a pipeline tracker.
- Remove the **site-side money record** (nothing about what each study owes the site, was billed, was paid, was paid to participants) → pure document/enablement (Florence pole) or pure visit tracking; the "management as business" character of the Type collapses.

§24 historical check: paper-era and spreadsheet-era site operations (paper regulatory binders, paper visit logs, invoice-by-hand against contract budgets, homegrown departmental databases in academic offices) satisfy this minimal definition — the invariant predates the modern suite. An SMO of the 1990s running multi-site operations with ledgers and binders would still be recognized. Modern suites add everything else.

### L1 — Common Mature Structure

Present across the sampled products; expected by the market; not required for recognition:

- participant panel / patient database as a reusable site asset (recruitment-oriented products make it central)
- recruitment machinery: website/landing-page integration, ad-channel and vendor integrations, pre-screening questionnaires, funnel tracking, re-marketing of the database to new studies
- visit operations with protocol-derived target dates and window calculations; reminders; overdue surfacing; task/alert machinery
- regulatory-document coordination (eISF/essential documents) and inspection/audit readiness; document exchange with sponsors/CROs and remote-monitor access (often via companion/integrated eReg products)
- participant engagement: reminders, two-way texting, participant portals, eConsent
- participant stipend handling and payment rails
- reporting/dashboards: enrollment, cycle times, staff productivity, financial reconciliation
- multi-site/enterprise tier: centralized management of many sites/studies/personnel/finances, aggregate reporting/BI, SSO/MFA
- integrations: EMR/EHR, eSource/EDC, eRegulatory, IRB/eIRB systems, general ledger, sponsor/CRO-side systems
- role separation (coordinators, regulatory, finance, management) with audit-facing records

### L2 — Variant / Optional Structure

- operator form: single independent site / SMO / site network / hospital or health-system research office / academic cancer center (each changes emphasis, not structure)
- emphasis poles: recruitment+finance-led (community/SMO pole) vs billing-compliance/institutional pole
- pipeline & business-development layer (opportunity tracking, start-up automation, performance metrics used to win studies; network-scale opportunity distribution with PI/site selection)
- physical-resource scheduling (exam rooms) — observed directly at one product; phase-I units intensify it
- billing-compliance machinery (payer-correct billing of research procedures; CRPC-style billing grids; EMR routing) — institutional pole
- eSource/eConsent embedded vs integration-only; decentralized-trial support; biospecimen modules; multi-country operation; mobile apps

### L3 — Vendor-specific Structure (kept out of the Application Document)

- RealTime: SOMS bundle naming; Devana / Engage! / MyStudyManager / SitePay / GlobalPay / TrialAlign / inSites product names; Mailchimp/Twilio/SubjectWell/Outlook/EDC Connect integrations; "30+ countries", "3000+ sites", "600,000+ visits/year", "9 of 10 top site networks" claims; ROI-calculator figures
- CRIO: Central eSource® (sponsor-published template model), Reviewer EDC, Dash Solutions cash cards, 1099 reporting, Veeva Vault EDC / Medidata Rave integrations; 40%/90% claims
- Advarra: Clinical Conductor CCText/CCPay module names; OnCore biospecimen module, RPE / IHE CRPC billing-grid integration names, Onsemble community/co-developed dashboards, Braid data & AI engine, Advarra Cloud (ISO 27001 / SOC 2 statements); "50 to 500+ active trials" segmentation statement; "recovered in unbilled payments" case-study figure
- Florence: eBinders/SiteLink/StudyOrganizer naming; 88,000+ sites / 600+ sponsors / 90 countries claims; 25-year retention option; "50% faster CTA negotiation" claim

## Vendor-specific Findings

(Consolidated from L3 above; none promoted to the canonical model.)

- The category name drift is itself a finding: the same site-operated software is labeled "CTMS" (RealTime-CTMS, Clinical Conductor, OnCore), "Site CTMS" (CRIO), "Site Operations Management System" (RealTime SOMS), and "Site Enablement Platform" (Florence, for the enablement-adjacent pole). The referent — running the site's research business — is stable across labels.

## Rejected Findings

- **"Site management = sponsor-side site feasibility/selection/activation module"** — rejected as the primary referent: the sponsor-side reading (site selection, feasibility, activation inside sponsor CTMS/start-up tools) is a capability cluster of the CTMS Type, and the site-facing tools observed (RealTime TrialAlign, Florence Site Feasibility, Devana opportunity distribution) are tool-level, not a management system. The leaf name in the directory sits in the Healthcare & Life Sciences family next to CTMS/EDC/eTMF, and the sampled software population that answers to "site management" is site-operated.
- **"Participant database is part of the defining core"** — rejected: institutional OnCore does not lead with a persistent patient panel; the database is the recruitment pole's centerpiece. Common mature structure, not invariant.
- **"Exam-room scheduling is defining"** — rejected: directly observed at one product only (CRIO screenshot); single-source → optional.
- **"eRegulatory/eISF is part of the Type"** — rejected: document management appears as modules/integrations in all management products and as standalone products (Complion; Florence eBinders) that lack participants/visits/finances entirely. Capability/seam, not the Type.
- **"Recruitment is defining"** — rejected: recruitment machinery is deep at three products but the institutional pole demonstrates the Type functions without it being the center; recruitment's own leaf (Clinical Trial Recruitment Platform) is sponsor-side with a distinct L0.
- **"SMO software is a separate Type"** — rejected: SMO/network operation is an operator-form variant; structures carry over.

## Boundary Findings

1. **vs Clinical Trial Management System / CTMS (sibling leaf) — the central tension.** The two directory labels cover overlapping product populations: RealTime-CTMS, Clinical Conductor, and OnCore all self-label CTMS while serving sites/networks/institutions, and the CTMS document already carries a "site/institution-centric pole." What distinguishes the frames is the **operator object**: CTMS is organized around a study with sites as its resources (plan-vs-actual execution of one protocol across a network); site management is organized around the site organization with studies as its portfolio (many sponsors, one business). The observed products support both readings simultaneously — one shared skeleton (study × participant × visit × money), two seats. Recommendation for joint review: keep both leaves only if the site-side leaf is documented from the site-business seat (as done here), and revise the CTMS document's site pole to defer to it; otherwise treat "Clinical Trial Site Management" as the alias/umbrella label of the CTMS site pole. Either resolution requires editing the CTMS document, which this pass did not do.
2. **vs Clinical Trial Recruitment Platform (processed)**: the recruitment leaf's subject is the study-as-demand-object with a candidate pool and screening decisions, feeding referral/handoff at the consent seam; here the subject is the site, recruitment is one operational capability (the site's own panel and funnels), and the pipeline object is the site's study portfolio rather than a candidate funnel. Overlap is real in site products (RealTime Engage!, CRIO recruitment) but the defining structures differ.
3. **vs eRegulatory / eISF products and eTMF**: document systems hold the regulatory file; site management records operations and money and *coordinates* the documents (often by integrating the document system). Removal test: strip participants/visits/finances from a site-management product and you get an eRegulatory product (Florence pole); that is the seam.
4. **vs EDC / eSource**: source-data capture at the visit vs operational/business management of the site; modern site suites bundle both (CRIO, RealTime), which is packaging, not identity.
5. **vs EMR / practice / patient scheduling**: care visits vs research visits; research visits carry protocol-derived windows, visit-schedule procedures, stipends, and sponsor-side billing. EMR appears as the integration partner (demographics, billing-compliance routing), not the system of record for the site's research business.
6. **vs Research Administration / Grant Management (institutional)**: pre-award/funding administration vs conducting sponsored studies; some institutional deployments connect both, but the objects differ (awards vs conducted study portfolios).
7. **Removal-test summary (what makes it another Type)**: remove site-as-subject → CTMS; remove sponsor-originated portfolio → clinic scheduling; remove participant/visit records → CRM; remove the money record → site enablement (eISF/feasibility platforms).

## Uncertainties

- Feature-level behavior (exact window-calculation rules, invoice state machines, permission models, delegation-log handling) rests behind customer logins; not asserted anywhere.
- The sponsor/CRO-side reading of "site management" (modules of enterprise CTMS) could not be fetched directly; handled through the CTMS document. If the directory owners intended the sponsor-side reading, this leaf's referent choice should be revisited (recorded in STATUS.md).
- Regional terminology outside the US-centric sample (UK NIHR site processes, EU site agreements) not researched; sample is US-heavy.
- Whether site financials could ever be absent in a recognized product: all four sampled management products carry them, but no minimal product without finances was sampled; the L0 placement of the money record is a canonical inference (Layer C), flagged here for honesty.
- Florence's feasibility product blurs toward the recruitment leaf's screening mechanics; boundary drawn at the panel/funnel object, not verified with a second enablement vendor.

## Final Synthesis

Clinical Trial Site Management is the **site-operated management application** for clinical research: software whose subject is the research site organization and whose managed demand is a portfolio of externally sponsored studies, each carried through the site's own lifecycle — opportunity/feasibility, contract and budget, start-up, conduct (recruit → screen → enroll → visit), monitoring support, close-out — while recording, per study, both the conducted operation (participants, visits, staff work) and the site's side of the money (budget → billed → paid; stipends out). Around this core, mature products add the participant panel and recruitment funnels, protocol-window visit operations, regulatory-document coordination and inspection readiness, participant engagement and stipends, staff/resource management, network/enterprise rollups, and integrations to EMR, eSource/EDC, eRegulatory, IRB, and ledger systems.

Relationship to the CTMS leaf: one shared eClinical skeleton, two operator seats. CTMS is the trial-operational system of record (study as subject, sites as resources); site management is the site-business system (site as subject, studies as portfolio). The market mostly ships one product per seat-vendor and labels it CTMS either way; the documents should tile by seat, and the STATUS.md boundary entry recommends the joint review of both documents to confirm the seat-split or collapse this leaf into the CTMS site pole as an alias.
