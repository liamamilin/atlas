# Research Notes — Litigation Management Platform

## Research Goal

Understand, from real products, what a "Litigation Management Platform" is as an Application Type: what object the market means by "litigation management", who operates such systems, what litigation-specific structures (parties, proceedings, discovery, dispute economics, guidelines/reserves) the software carries, how the Type relates to the many already-processed legal siblings, and whether the leaf stands as an independent Type or collapses into Law Practice Management / Legal Matter Management.

Context from prior passes (carried obligations this pass must discharge):
- legal-matter-management pass: "litigation appears in this sample as a matter-type/use case inside matter management (proceeding-level detail, litigation events, litigation use case), keep-both presumed with the claims-posture seam left to that pass."
- legal-docket-management pass: "vs Litigation Management Platform (unprocessed) — litigation management centers oversight of litigated matters (claims posture, budgets, outside counsel, insurer/corporate pole); docketing is one embedded capability. Flag for that pass."
- law-practice-management-system pass: "litigation management centers the oversight of litigated matters (often insurer/corporate-driven claims litigation), not the firm's whole-practice business system. Noted; left to that pass."
- outside-counsel-management pass: "those [Litigation Management / eDiscovery] center the case work itself; OCM centers the vendor relationship and its cost."
- insurance-claims-management pass: "claim litigation management ('centralize legal documentation and track litigation status')" observed as a module inside RMIS/claims products (Origami Risk, Sapiens) — claims-side embedding evidence.

## Initial Boundary

- Working hypothesis: the Type centers the *litigated case* (a dispute prosecuted or defended in a court/arbitration/tribunal) as the system of record, with litigation-specific machinery that generic matter or practice management does not carry: procedural stages, litigation events and deadline/limitation calendaring, discovery/evidence tracking, adverse-party and representation structure, and the dispute's value-and-resolution economics (claims, demands/offers, settlements, budgets, guidelines, reserves).
- Suspected two poles: (a) firm-side litigation case management (firms running plaintiff/defense caseloads) and (b) dispute-owner-side oversight (corporate legal, insurers, government — often realized inside matter management or claims systems). Sample must test whether both poles share a core or whether pole (b) is just matter management.
- Nearest neighbors: Legal Matter Management (matter as system of record), Law Practice Management System (client-anchored firm business system), Legal Docket Management (deadline register), Court Case Management System §24 (court's official record), Insurance Claims Management (claim as system of record), eDiscovery / Legal Hold (pipeline machinery on the case's documents), Legal E-filing, Case Law Research (external cases), Prosecutor/Public Defender Case Management (§24, government courtroom side), Outside Counsel Management (firm relationship).
- Known ambiguity: "litigation management" is also the name of a *managed service* discipline (litigation-management programs providing bill review, counsel management, outcome reporting for insurers/self-insureds). The software leaf must be defined independently of that service form.

## Research Questions

1. What is the central record: case, matter, claim? What does a case carry (parties, representation, forum, posture, amounts)?
2. What litigation-specific machinery exists (stages/phase plans, litigation events, discovery requests/productions, experts, depositions, statutes of limitation)?
3. How is the dispute's economy recorded: demands, offers, settlement, liens, costs, budgets, billing-guideline compliance, reserves?
4. Who operates the system (law firm vs in-house/insurer/government) and how does the operator change the object model?
5. Where do deadlines come from (court rules engines, event calculators, manual entry) and how does docketing embed?
6. What is shared across the two suspected poles, and what is pole-specific?
7. Where are the boundaries vs LMM (matter record), LPM (firm business system), docket (deadlines), claims (claim record), court CMS (official record)?
8. Historical check: does a pre-software litigation practice (paper case files, calendar books, settlement ledgers, claims-litigation ledgers) satisfy the core?

## Representative Products

| Product | Pole | Why chosen |
|---|---|---|
| Litify | modern AI-native legal platform; litigation-firm poles (plaintiff PI + insurance defense) + ELM for corporate legal | explicitly spans both suspected poles in one product family; Salesforce-native architecture; platform-page evidence |
| CasePeer (8am) | firm-side litigation case management, personal-injury specialization; SMB/mid plaintiff firms | deepest publicly documented litigation-specific feature set (discovery tracking, expert witnesses, defense-counsel communication, settlement management, liens, litigation event plans); help center index reachable |
| TrialWorks (Assembly Software) | classic Windows-era litigation case management (Needles/Neos lineage) | support/training documentation exposes the object model (Docket tab, Negotiations tab, Production Tracker, Settlements, Mass Tort module, service lists) unusually clearly |
| Legal Files (Onit) | in-house / government / insurer case & matter management pole (incl. staff counsel and litigation workflows) | the buyer-side pole with litigation as a use case; government agencies + insurance organizations documented |
| Xakia | in-house matter management with dispute log (Australian origin; global) | carried A- evidence from the LMM pass (Dispute Log: proceedings, claim amounts, insurance); root refetched this pass — tests whether the buyer pole carries dispute-specific records |

Boundary probes (not full samples): Onit ELM suite pages (Unity/SimpleLegal product line), Mitratech portfolio pages (TeamConnect ELM; CaseCloud/AdvoLogix case management), plus carried evidence from the insurance-claims pass (claims-side litigation modules).

## Sources

Tier 1 (official operational documentation):
- CasePeer Help Center (supportcenter.casepeer.com) — collection index fetched 2026-09-08 (CASE 326 articles; TASKS & CASEPLAN; CALENDAR; DOCUMENTS; REPORTS; ACCOUNTING collections)
- TrialWorks support home (support.trialworks.com) — training-document index with per-tab PDFs (Docketing, Negotiations, Production Tracker, Settlements, Mass Tort Cases, Workers' Compensation, Service Lists), fetched 2026-09-08
- Legal Files Academy (onitacademy.com/page/legal-files-academy) — resource index incl. "Top 10 Claims and Litigation Best Practices", intake/LSR, workflow wizards, retention webinars, fetched 2026-09-08

Tier 2 (official product pages):
- Litify root (litify.com) — fetched 2026-09-08
- Litify Platform page (/platform) — fetched 2026-09-08
- Litify Insurance Defense page (/insurance-defense-practice-management-software) — fetched 2026-09-08
- Litify ELM page (/enterprise-legal-management-software) — fetched 2026-09-08
- CasePeer root (casepeer.com) — fetched 2026-09-08
- CasePeer Case Management feature page (/feature-case-management) — fetched 2026-09-08
- Legal Files product page (onit.com/products/elm/legal-files) — fetched 2026-09-08
- Xakia root (xakiatech.com) — fetched 2026-09-08
- Mitratech products index (mitratech.com/products) and Legal Solutions support index (success.mitratech.com/Legal_Solutions) — fetched 2026-09-08
- Onit root (onit.com) — fetched 2026-09-08
- Mitratech Success Center TeamConnect index (success.mitratech.com/TeamConnect) — fetched 2026-09-08

Source-access limitations:
- legalfiles.com and www.legalfiles.com — transport error ×2 each → Legal Files observed at Onit product-page + academy-index level only (Tier 2); no object-level claims made for Legal Files beyond those pages.
- mitratech.com/products/teamconnect-litigation and onit.com/products/litigation-management — 404 (dedicated litigation product pages do not exist at those URLs); no vendor today visited ships a standalone "litigation management" page at the guessed locations — the buyer-side litigation-management form is evidenced through matter-management/claims-module pages instead.
- Mitratech Success Center glossary is an alphabetical subpage index; deep TeamConnect module documentation not crawled — TeamConnect litigation-module specifics rest on the LMM pass's earlier A-level observations.
- CasePeer/Legal Files help-article bodies not fetched (index level only) — object details for those products calibrated to feature pages and collection titles; no precise operational parameters asserted.
- No dedicated standalone "corporate litigation management platform" vendor page was reachable; the buyer-side pole's claims-posture machinery (reserves/coverage linkage) rests on carried evidence (LMM pass: Xakia dispute log with insurance fields; insurance-claims pass: claim litigation management modules) — asserted at B strength.

## Product observations

### Litify — modern legal platform, litigation-firm poles + ELM (evidence layer A at product-page level)

- Positioning: "all-in-one legal platform" / "platform of action"; law-firm solutions per practice area (Personal Injury, **Insurance Defense**, Immigration) and Enterprise Solutions (**Corporate Legal Departments** / ELM). Insurance-defense page headline: "case management software for insurance defense firms".
- Intake layer (platform page): dynamic intake questionnaires, voice agents, legal service requests portal, conflict-check agent ("fuzzy matching" across case history, permanent conflict reports).
- Matter layer: **Matter Plans** ("automated, templatized task lists configurable to practice area, case type"); **Case Activity Timeline** ("files, emails, calendar events, and more on an organized timeline"); AI **Matter Summaries** for handoffs; "case" and "matter" used interchangeably across solutions pages.
- Insurance-defense posture: "client guidelines are automatically applied to each case"; billing-rule compliance before invoices reach the client; pre-bill review from the matter; panel-position reporting ("justify rates based on performance and improve your panel position"); AI transcript processing "from court proceedings and depositions"; AI medical chronologies with "reconciled ledger" of encounters and bills.
- ELM posture (corporate): matters + documents + eBilling + outside counsel collaboration ("inviting both internal stakeholders and outside counsel directly into the platform"); co-counsel recommendation (panel selection per matter from billing data/performance/case criteria); AI invoice review vs billing rules and budgets; legal holds module; matter types "including patents, IP, real estate, **litigation**, and more".
- Integrations relevant to litigation machinery: **CalendarRules** (court-rules deadline engine), **ECFX** (court deadline/docket automation), records-retrieval vendors, Case Status (client portal), NetDocuments/iManage.
- Money: Time & Billing suite (capture, pre-bills, mass bill generation), Spend Management (budgets, invoice review, dynamic discounts).

### CasePeer (8am) — plaintiff PI litigation case management (evidence layer A)

- Positioning: "personal injury case and practice management software"; "From medical treatment tracking to negotiation tools… track a successful personal injury case, from medical treatment to litigation."
- Case objects (feature page): **Cases** ("clean and organized case files… monitor and evaluate a case at a glance from the summary screen"); **Timelines** (activity/communication tracked over the case lifetime); **Task management** (assignee, due dates, priority, reminders); **Calendar management** ("event calculator and litigation event plans", sync Outlook/Google/iCal, "automated statute reminders"); **Litigation** ("Track deadlines, discovery requests and responses, expert witnesses, and defense counsel communication across your cases with litigation tools designed for plaintiffs' law firms"); **Cost tracking** (cost request center, accounting integration); **Medical treatment** (log injuries, doctor visits, payments, status of records and bills requests); **Document management**.
- Settlement management (FAQ, explicit): "track demands, offers, negotiation history, lien balances, and fee calculations from the moment a case enters negotiations through final disbursement"; "attorneys can see each case's financial status at a glance and move from negotiation to payout without switching between spreadsheets or disconnected tools."
- Deadline machinery (FAQ): "court-rule deadline calculator automatically computes filing deadlines based on jurisdiction-specific procedural rules, accounting for weekends, holidays, and service-method extensions"; statutes of limitation "tied directly to each case record"; "missed deadlines are a leading cause of legal malpractice claims" framing.
- Help-center structure (Tier 1 index): collections CASE (326 articles), TASKS & CASEPLAN (16), CALENDAR, DOCUMENTS, REPORTS, ACCOUNTING, E-SIGNATURE, EMAIL/TEXTING — "CasePlan" is the stage-plan object name.
- Business framing: "case performance, settlements, referrals, productivity" reporting; "caseload health and bottlenecks" dashboards.

### TrialWorks (Assembly Software) — classic litigation case management (evidence layer A at documentation-index level)

- Support home exposes the working object model through named tabs and training PDFs: **Docket tab** ("Docketing in Trialworks"), **Negotiations Tab**, **Production Tracker Tab** (discovery production tracking), **Settlements** ("Settlement Feature in TrialWorks"), **Mass Tort Cases** ("Managing Mass Torts in TrialWorks"), Workers' Compensation module, Service Lists ("Service on Attorney By Email"), Contacts/Call Log/History, Document search (TWSearch), SMS/email/fax, DocuSign, Stamps.com.
- Windows/SQL Server desktop lineage with hosted option; v9–v11 version range documented; requirement specs indicate on-prem deployment tradition.
- Lineage note (footer): Assembly Software "brings together two of the legal profession's pioneering case management brands, Needles and Trialworks, both of which have contributed to Neos, Assembly's reimagined cloud-based solution."
- Interpretation: the tab set is the litigation workflow made concrete — docketing, discovery production, negotiation, settlement — plus intake/contact machinery; mass-tort and workers'-comp modules show practice-area instantiation.

### Legal Files (Onit) — in-house / government / insurer pole (evidence layer A at product-page level; academy index)

- Positioning: "centralized legal case and matter management platform used by government agencies, corporate legal departments, law firms, and universities"; "a single system of record for legal work… centralizing matter, document, email, and contract information".
- Audience list includes litigation-specific seats: "Government agencies managing litigation, regulatory matters, and public records requests"; "**Insurance organizations managing staff counsel and litigation workflows**"; investigation teams with controlled access.
- Use-case breadth: "whether teams are managing litigation, contracts, investigations, or compliance matters" — litigation is one managed use case on a matter/case spine.
- Academy (Tier 1 index): "Top 10 Claims and Litigation Best Practices" webinar; intake/legal-service-request/file-opening processes; rules-based Workflow Wizards automating Calendar and To-Do creation; timeslip/time entry; file retention; Outlook integration; v13 navigation/search/folder views.
- Interpretation: buyer-side realization — matters/files with calendaring and workflow automation; litigation workflows sit on the same case/matter spine as contracts/HR/compliance; no standalone proceeding machinery surfaced at the pages reached.

### Xakia — in-house matter management with dispute log (evidence layer B this pass [A- in the LMM pass]; root refetched)

- Root page: matter management, intake & triage, contract lifecycle, spend management, dashboards, document management for in-house teams; AU-origin, multi-region sites (US/AU/UK/JP).
- LMM pass (2026-09-08, A-): **Dispute Log** with proceedings, claim amounts, insurance fields — the buyer-side dispute-economy record; litigation events at Brightflag; litigation use case inside TeamConnect.
- Interpretation: dispute/litigation depth exists inside in-house matter management as a record class (disputes with amounts and coverage), not as a separate proceeding machinery.

### Boundary probes

- **Onit ELM suite** (Unity/OnitX/SimpleLegal pages): "Legal Spend & Matter Management" is the category name; matters/vendors/spend/contracts/workflows; no standalone litigation product page exists in the portfolio (litigation-management URL 404). Confirms: in the ELM market, litigation management is packaged inside matter management.
- **Mitratech portfolio** (products index + Legal Solutions support index): legal products are TeamConnect (eBilling & matter management), CaseCloud/"Case Management" (AdvoLogix lineage, help.advologix.com), LegalHold, AdvanceLaw (panel), Managed Bill Review. No product line named litigation management today; litigation capability historically a TeamConnect module (LMM pass A-).
- **Insurance-claims pass (carried)**: RMIS/claims products ship "claim litigation management — centralize legal documentation and track litigation status" as a module (Origami Risk; Sapiens complex-case handling) — the claims-system embedding of the same discipline.

## Cross-product Comparison

| Dimension | Litify | CasePeer | TrialWorks | Legal Files | Xakia |
|---|---|---|---|---|---|
| Central record | matter/case (Salesforce objects) | case file | case with tab-structured workflow | file/case/matter | matter (+ Dispute Log class) |
| Operator/seat | litigation firms (plaintiff + defense); corporate legal | plaintiff PI firms | litigation firms (incl. mass tort, workers' comp) | government, corporate, insurers (staff counsel), universities | in-house legal teams |
| Parties/representation/conflicts | conflict-check agent; outside counsel collaboration; co-counsel recommendation | defense counsel communication tracked | contacts/service lists | (page-level; not detailed) | (LMM pass; not detailed) |
| Litigation stages/phase plans | Matter Plans per case type | CasePlan; case lifecycle intake→settlement | tab-per-phase structure; mass-tort management | workflow wizards (generic) | templates (generic) |
| Litigation events & deadlines | ECFX/CalendarRules integrations; email/calendar sync | event calculator; litigation event plans; statute reminders | Docket tab | calendar + wizard automation | deadlines on matters |
| Discovery/evidence machinery | AI medical chronology; transcript analysis; document management | discovery requests & responses; expert witnesses; medical treatment/records status | Production Tracker tab; document search | (not detailed) | (not detailed) |
| Dispute economics | billing guidelines; budgets; invoice review; panel economics | demands/offers/negotiation history; liens; fee & disbursement calc; cost tracking | Negotiations tab; Settlements feature | (not detailed) | claim amounts; insurance (LMM pass) |
| Buyer-side oversight (budgets/panel/spend) | ELM: eBilling, co-counsel recommendation, outside counsel performance | — (firm-side product) | — (firm-side product) | litigation/claims workflows (page-level) | spend management; budgets |
| Reporting | no-code dashboards; case performance | caseload health; settlements; referrals | dashboards (on request forms) | reporting options (webinars) | dashboards; legal-value reporting |
| Packaging | standalone platform (Salesforce-based) | standalone SaaS (8am family) | desktop/on-prem + hosted; Neos successor | on-prem/cloud; Onit-owned | standalone SaaS |

Stable across the firm pole (Litify, CasePeer, TrialWorks — layer B): case-anchored records with parties/representation context; litigation events and deadline/limitation calendaring (increasingly rules-engine-driven); discovery/evidence tracking (requests/responses, productions, experts, medical/damages material in PI); negotiation→settlement machinery; document/email/call capture on the case; stage/phase-based task machinery; reporting across the caseload.

Stable across the buyer pole (Litify ELM, Legal Files, Xakia, Onit/Mitratech portfolios — layer B, partially carried): matters/cases as records with dispute-type depth (proceedings, claim amounts, insurance/dispute log), budget/guideline/spend control over litigated work, outside/panel counsel management, and litigation workflows sharing the same spine as other legal work.

The two poles meet on: the litigated case as a persistent record, calendared litigation events/deadlines, the dispute's money (costs, budgets, settlements), and portfolio reporting. They diverge on: proceeding-machinery depth (discovery/experts/stage plans strongest on the firm side) vs oversight machinery (guidelines/panel/spend strongest on the buyer side).

## Canonical Model (abstraction ladder)

### L0 — Defining Invariant

1. **The litigated case of record** — a persistent, individually identified case for one dispute prosecuted or defended in a forum (court, arbitration, tribunal, administrative body), carrying the dispute's parties and representation (who claims, who is claimed against, who represents or defends, with co-counsel/experts as working roles), the forum/court context, and the case's current procedural posture. Remove → generic matter/task management; remove the adverse-party/forum anchoring → Legal Matter Management's matter.
2. **The proceeding worked as litigation** — the application carries the proceeding's own operating machinery: litigation stages/phase plans the case advances through; litigation events (filings, hearings, depositions, conferences, mediations) surfaced through calendar/deadline views with limitation-period risk; and the discovery/evidence layer of the case (requests and responses, productions, expert witnesses, key case documents/evidence material). Remove → a matter tracker with a generic calendar — the LMM/LPM shape, not this Type.

Jointly-held is load-bearing: (1) without (2) is a dispute register (LMM pole); (2) without (1) has nothing to work on.

Historical check (§24, reasoned — canonical inference): pre-software litigation practice satisfies the core without any of the modern machinery — a paper case file organized by a lead attorney or case manager, holding the pleadings, discovery correspondence, expert and witness lists, a calendar/docket book with statute and court dates, a settlement-negotiation ledger, and (insurer side) a claims-litigation ledger with counsel assignment, budget, reserve and outcome columns. No software, no cloud, no rules engine in L0. The check also covers regional breadth conceptually: the discipline exists wherever disputes are prosecuted/defended, though the sampled products are US-procedure-shaped (uncertainty noted).

### L1 — Common Mature Structure

- **The dispute's value-and-resolution record** — what the case is worth and how it ends: claimed/exposure amounts, demands and offers, negotiation history, settlement tracking (liens, costs, fee/disbursement calculations in the plaintiff pole), and the recorded resolution. Present in nearly every sampled product (CasePeer and TrialWorks directly; Litify via its economics layer; Xakia's dispute log carried from the LMM pass). Held just below the defining line: two buyer-side realizations document it thinly at page level, and a proceeding tracker without the economics would arguably remain recognizable — but the discipline's stated purpose (controlling exposure, cost and outcome) lives here.
- **Funded-pole economics** — litigation budgets and billing-guideline compliance, invoice/pre-bill review, panel/defense-counsel selection and performance, and (insurance-funded matters) reserve/coverage linkage (carried B).
- **Court-rules deadline computation** — trigger-event → computed deadlines via jurisdictional rule sets (often via specialist engines: CalendarRules/ECFX-class), consistent with the legal-docket-management pass's model.
- **Case file accumulation** — documents, email, calls/texts, tasks with stage plans, timelines/activity history on the case.
- **Client/constituent communication** — portals, status updates, texting/email (plaintiff pole); LSR intake (buyer pole).
- **Portfolio reporting** — caseload health, stage distribution, spend vs budget, outcomes, counsel/carrier performance.
- **Era-current AI** — matter summaries, medical chronologies, transcript/deposition analysis, document drafting (present in 2 of 5 sampled products; not definitional).

### L2 — Variant / Optional Structure

- **Seat/pole (the most consequential variant)**: firm-run litigation case management (plaintiff PI/mass tort vs insurance defense vs general commercial litigation) vs dispute-owner-run oversight (corporate legal, insurer/staff counsel, government) — the latter usually realized inside matter management, ELM suites, or claims/RMIS systems rather than as standalone products.
- Practice-area instantiation: PI (medical treatment, liens, demand packages), mass tort (inventories across the tort), workers' comp, insurance defense, commercial/employment litigation, government litigation.
- Packaging: standalone platform vs ELM-suite module vs claims/RMIS module vs embedded capability in practice management; managed litigation-management *service* programs (bill review + counsel management as a service) exist beside the software and are a delivery variant, not the Type.
- Jurisdiction machinery depth: US-centric court rules/statutes vs lighter non-US dispute management (sample is US-shaped; Xakia's AU origin is one partial non-US data point).
- Fact/issue/evidence analysis layers (chronology building, case-argument mapping — CaseMap-class lineage) as adjacent capability.
- Deployment: cloud SaaS dominant in current products; desktop/on-prem lineage documented (TrialWorks).

### L3 — Vendor-specific (kept out of the final document)

- Litify: Salesforce substrate; "platform of action" positioning; Litify ACE (Agentic Case Expert); Agentforce; named integrations (ECFX, CalendarRules, Case Status, EvenUp-class); AmTrust panel-management case study.
- CasePeer: 8am family membership (MyCase/LawPay/DocketWise); "8am IQ" AI; EvenUp integration; specific metric claims (11,000+ professionals; review-site scores).
- TrialWorks: Assembly Software/Needles/Neos lineage; specific tab names (Docket, Negotiations, Production Tracker); v9–v11 version range and system requirements; TWSearch.
- Legal Files: Onit ownership (help desk rebranded LegalFiles.Support@onit.com); Workflow Wizards; v12/v13 releases; specific webinar catalog.
- Xakia: Connect-for-law-firms portal; "fraction of the cost" positioning; named customer logos.

## Vendor-specific Findings

- Litify is the only sampled product explicitly packaging both poles (firm solutions + corporate ELM) in one platform — straddling evidence for the pole relationship.
- CasePeer's FAQ carries an unusually explicit canonical statement of settlement management ("demands, offers, negotiation history, lien balances, and fee calculations… through final disbursement") — used as the plaintiff-pole economics definition.
- TrialWorks's tab set (Docket/Negotiations/Production Tracker/Settlements) is the clearest documentation of the classic litigation workflow object model; its own footer documents the Needles→Neos consolidation of the category.
- No sampled vendor today leads with a standalone buyer-side "litigation management" product page — the buyer-side form surfaces only as ELM/claims module capability and, per the LMM pass, as dispute-type fields (Xakia) and litigation events (Brightflag). This is itself a structural market finding.

## Boundary Findings

1. **vs Legal Matter Management (§11, processed — DISCHARGES that pass's flag from this side)**: keep-both RATIFIED. LMM's system of record is the matter (any legal work) with accumulated file and managed progression; this Type's system of record is the litigated case, and its distinguishing leg is the proceeding's own machinery (litigation stages, litigation events with limitation risk, discovery/evidence layer). Test: strip the litigation machinery from this Type → LMM; grow proceeding-level machinery on an LMM matter → this Type. Center-of-gravity, not alias: the market sustains a dedicated litigation case-management product family (TrialWorks/Neos, CasePeer, Litify's litigation solutions) whose identity rests on the machinery, while buyer-side litigation remains matter-management-shaped.
2. **vs Law Practice Management System (§11, processed — DISCHARGES that pass's flag)**: keep-both. LPM is the client-anchored firm business system (intake→work→billing→trust as the organizing loop). Litigation-firm products (Litify, CasePeer) straddle — they carry firm operations — but their litigation identity is the case/proceeding machinery, not the billing/trust loop. Test: remove client-billing/trust anchoring and keep the proceeding machinery → this Type's center; remove the proceeding machinery → generic LPM with a litigation practice area.
3. **vs Legal Docket Management (§11, processed — DISCHARGES that pass's flag)**: docket management's system of record is the dated-obligation register (rules-engine computation, dual-entry control, malpractice accountability); this Type's system of record is the case file/proceeding. Docketing is one embedded capability here (statute reminders, event calculators, rules-engine integrations observed in 3 products) — consistent with that pass's expectation.
4. **vs Court Case Management System (§24, processed)**: the court holds the official record and exercises court authority; this Type is party-side (prosecuting or defending). The court's docket/case events are an input feeding the party's case record (e-filing notices, docket alerts — cf. docket pass). Hand-off seam, not overlap.
5. **vs Insurance Claims Management (§11, processed — carried evidence)**: the claim is the payer's system of record (FNOL→coverage→resolution); litigated claims spawn cases that are worked here (or in a claims-system litigation module). Test: remove the claim/coverage/reserve machinery and keep the case/proceeding machinery → this Type. The "claim litigation management" module observed in that pass is the embedding of this Type's object inside the claims system.
6. **vs eDiscovery Platform / Legal Hold Management (§11, processed)**: pipeline machinery over the case's documents (holds, collection, review, production) vs the case itself as system of record. This Type references discovery state (requests/responses, productions) but does not process document corpora.
7. **vs Outside Counsel Management / Legal Spend Management (§11, processed)**: OCM centers the firm relationship, spend centers the money records; this Type centers the case work those disciplines oversee. Buyer-side products bundle all (Litify ELM; per OCM/LMM passes) — bundling is packaging, not Type merger.
8. **vs Case Law Research Platform / Legal Research (§11, processed)**: research over published law and external dockets vs management of the organization's own litigated cases. Litigation analytics (judge/court/firm) is a research-layer capability, adjacent.
9. **vs Prosecutor Case Management / Public Defender Case Management (§24, unprocessed — new flag)**: government courtroom-side criminal case management (charging, arraignment, hearings, disposition at county/state scale) is a different caseload grammar from civil/commercial litigation management, but the words "case management" collide; those passes should treat this leaf's boundary findings as a counterparty.
10. **Naming note**: "litigation management" also names managed-service programs (insurer/TPA-run bill review, counsel management, outcome reporting). The software Type is defined independently; the service form is recorded as a delivery variant.

## Uncertainties

- Whether any standalone buyer-side "litigation management platform" product (independent of matter management and of claims systems) exists with meaningful market share — not directly evidenced; the buyer pole was documented through matter-management/claims-module realizations. If a later pass finds one (e.g., in public-sector or insurer procurement), check whether it carries the proceeding machinery (L0 leg 2) or only dispute-typed matter fields (→ LMM pole).
- Case-level operational details (permission matrices, stage taxonomies, deletion policies) not reachable for any sampled product; no precise parameters asserted.
- Non-US/regional litigation-management products (UK, EU, APAC beyond Xakia) not sampled; the historical/regional generalization rests on the structure of the discipline.
- Litigation fact/issue analysis tools (CaseMap-class) were not directly sampled; their position (capability vs adjacent Type) is reasoned, not evidenced.
- The exact split between native court-rules engines and partner engines inside sampled products is documented only where vendors name integrations (Litify/CasePeer pages).

## Final Synthesis

A Litigation Management Platform is the party-side system of record for litigated disputes: it holds the litigated case — a persistent, identified case bound to adverse parties, their representation, and a forum — and works that case *as litigation* through the proceeding's own machinery: litigation stage/phase plans, calendared litigation events with limitation-period risk, and the discovery/evidence layer (requests, productions, experts, key documents). Around that core, mature products add the dispute's value-and-resolution record (claims, demands/offers, settlement machinery, costs) and, on the funded side, budgets, billing-guideline compliance, panel/defense-counsel management and reserve/coverage linkage (carried B). The market realizes the Type in two poles: firm-run litigation case management (the standalone product family: plaintiff PI/mass tort and insurance defense) and dispute-owner-run oversight (corporate/insurer/government), the latter usually packaged inside matter management, ELM suites, or claims systems rather than as standalone products. The Type stands independently of Legal Matter Management (matter skeleton vs proceeding machinery), of Law Practice Management (client-billing loop vs case machinery), of Legal Docket Management (deadline register vs case file), and of the court's own case management (official record vs party-side working record) — with all four prior flags discharged from this side. Pre-software litigation practice (case files, calendar books, settlement ledgers, claims-litigation ledgers) satisfies the defining core without any modern machinery.
