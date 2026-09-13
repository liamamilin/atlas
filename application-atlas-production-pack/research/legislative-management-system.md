# Research Notes — Legislative Management System

## Research Goal

Understand the software that legislatures themselves run: the systems operated by a legislative body's own secretariat/clerk apparatus to manage its legislative business — bills, member business instruments, the chamber's calendar of business, committees, and the official record. Establish what this Type is at its core, and settle the boundary against the two neighbors that share its vocabulary:

1. **Government Meeting / Agenda Management (§24, processed 2026-09-07)** — which left an explicit joint-review flag naming this leaf as its boundary counterparty (market vocabulary collides: the agenda-market leader brands its products "digital legislative management").
2. **Legislative Tracking Platform (§24 sibling, unprocessed)** — the external/observer-side bill monitoring market (Quorum class), which prior passes (advocacy-platform, regulatory-change-management) also flagged as a distinct direction.

## Initial Boundary

Working hypothesis before research:

- This is the legislature's own process system: the chamber-scale counterpart to agenda management — bill/measure lifecycle, calendars of business, journals/verbatim records, committees — at state/national parliament scale.
- Nearest neighbors: Government Meeting / Agenda Management (local meeting cycle vs chamber business workflow — joint review pending), Legislative Tracking Platform (external monitoring vs internal operation), Court Case Management (adjudication vs production), Board / Corporate Governance Platform (confidential corporate bodies vs public legislative bodies).
- Unknowns: whether the US local-government "legislative management" vocabulary (Legistar) describes this Type or the agenda Type; how deep the bill workflow goes in products; whether member business instruments (parliamentary questions) are core or regional variant; whether any US state-legislature commercial vendor is reachable.

## Research Questions

1. What is the core object — the bill/measure, the daily business (calendar/LOB), or the meeting?
2. How does a bill enter, advance (stages), and close (as introduced / as passed / bicameral / committee referral)?
3. How is the chamber's daily business instrument built and published (event types, approval, public visibility)?
4. What member-facing machinery exists (submission of questions/notices, e-book, attendance)?
5. What executive/department participation exists (drafting, replies, papers laid)?
6. How is the official record produced (verbatim/journal pipelines)?
7. Who operates the system (secretariat/clerk roles) and what does the role structure look like?
8. Where is the boundary vs the agenda-management family (joint review counterparty) and vs external legislative tracking?

## Representative Products

Selected for market coverage + philosophy spread + institutional-level spread. The market reality: inside-pole software is dominated by government-built programs and a small commercial vendor set, most of which do not expose operational documentation.

1. **NeVA — National eVidhan Application (Government of India, Ministry of Parliamentary Affairs + NIC)** — a national "One Nation One Application" program deploying a paperless "Digital House" workflow system to Indian state legislatures and councils, per-house. The only reachable source with step-level operational documentation (227 published FAQs covering every module). Anchors the inside pole.
2. **Granicus — Agenda LE (Legistar)** — the long-standing market leader for US local government, self-styled "digital legislative management," the specimen straddling this Type and Government Meeting / Agenda Management (its role was flagged by the counterparty pass).
3. **Quorum** — external legislative tracking / public affairs platform (federal, 50 states, EU). Sampled only as the boundary counterpart: the observer/actor side of the same bills, operated by advocacy and government-affairs teams rather than the legislature.

Counterparty (documented, not re-fetched in full): **research/government-meeting-agenda-management.md** (2026-09-07 pass; Granicus LE/OE, Diligent Community, OpenMeeting at product-page depth) — used as the boundary opponent for the joint review.

Rejected / unreachable samples (recorded per source-access rules):

- **AOT (American Office Technologies)** — US state-legislature legislative-suite vendor (bill drafting/chamber/journal). aot.com and www.aot.com both timed out (2 attempts) — abandoned. US state-legislature commercial pole therefore under-sampled.
- **SAPL / Interlegis (Brazil, open-source legislative process system)** — sapl.readthedocs.io 404; github.com/interlegis/sapl timed out ×2 — abandoned. Latin-American open-source pole under-sampled.
- Court-adjacent and codification vendors (Municode etc.) — different Type; not pursued.

## Sources

All fetched 2026-09-08 unless noted:

- NeVA — homepage / live public portal: https://neva.gov.in/ (house roster with Digital House / Onboarded / Prospective states; live notice board with House Proceedings, session calendars, bills, bulletins; module icons: Notices Received, Questions, Government Bills, Paper-Laid, Committee Reports)
- NeVA — About NeVA: https://neva.gov.in/Home/AboutNeVA ("work-flow system deployed on NIC Cloud, MeghRaj"; member-centric; information classes: member contact details, rules of procedure, list of business, notices, bulletins, bills, starred/unstarred questions and answers, papers laid, committee reports)
- NeVA — FAQ (227 operational questions, step-level): https://neva.gov.in/Home/NevaFAQ (question-processing workflow sections; LOB module; Bills module; Committee module; Reporter module; Department reply module; role/access model; publication rules)
- Granicus — Agenda LE (Legistar) product page (also fetched 2026-09-07 in the counterparty pass): https://granicus.com/product/agenda-management-legistar/ ("digital legislative management"; "support the full legislative process"; document-typed item forms: resolutions, contracts, ordinances; in-meeting conduct; public portal)
- Quorum — homepage: https://www.quorum.us/ ("AI Public Affairs Software"; "legislation and dialogue tracking across the US and the EU"; legislative tracking / grassroots advocacy / stakeholder engagement / PAC)
- Counterparty research: research/government-meeting-agenda-management.md + applications/government-meeting-agenda-management.md (2026-09-07)

**Source-access limitation (load-bearing for assertion calibration):**

- Help-center / user-guide depth was reachable **only for NeVA** (its published FAQ is effectively user documentation). Granicus and Quorum were reachable at product-page depth only. US state-legislature commercial vendors (AOT) and regional open-source (SAPL) were unreachable entirely.
- Therefore: NeVA observations are step-level [A]; Granicus/Quorum observations are positioning/feature level [A]; cross-product claims about the inside pole rest on NeVA + the counterparty pass's product-page evidence; precise numeric limits (submission deadlines, counts, retention periods) are NOT asserted beyond what NeVA documents.
- NeVA is a national government program, not a commercial product market — its philosophy (member-centric paperless, per-house deployment, Westminster question machinery) partially reflects India's parliamentary tradition. Regional generalization is constrained accordingly; the question/notices machinery is treated as a regional variant, not an invariant.

## Product Observations

### NeVA — National eVidhan Application [Evidence layer A — step-level FAQ + live portal]

Positioning (About page): "NeVA is a work-flow system deployed on NIC Cloud, MeghRaj which helps the Chair of the House to conduct the proceedings of the House smoothly, Hon'ble Members to carry out their duties in the House efficiently and to conduct Legislative Business of the House in a Paperless manner." "Device neutral and member centric." Hosts "a secure page for each Member of the House for submitting questions & other notices." Information classes: member contact details, rules of procedure, list of business, notices, bulletins, bills, starred/unstarred questions and answers, papers laid, committee reports.

Structure (FAQ + portal):

- **Per-house deployment with onboarding states**: Lok Sabha/Rajya Sabha "Prospective"; assemblies/councils "Onboarded (MoU Signed)"; "Digital House — Live on NeVA Platform" (~20 houses live). Each house gets its own portal (e.g. gujarat.neva.gov.in) and its own "NeVA Unit" login; public portal in 12+ languages.
- **Session spine**: House → Session → Session Date parameters organize documents (FAQ Q11: "view the House Documents laid in the House for any date" via Assembly/Session/Date). "Session Status" dashboard summarizes questions/notices for the session (Q115). Previous-session data accessible (Q114).
- **Member online submission**: members submit Starred Questions, Unstarred Questions, Short Notice Questions, and Notices (by "Business Type" = rule types, Q2) via web and mobile app. After the announced last date, sending options are disabled (Q6). Submission auto-assigns an immutable dairy number and SMS confirmation (Q3, Q4). Counts of submitted items visible to the member (Q7).
- **Question-processing secretariat workflow** (Q177–178 + Q179–201): "processed online by the Legislative House Secretariat using Workflow based NeVA CMS application. The final list of Questions/Notices so prepared is auto generated and the question book is uploaded directly to NeVA Public Website of respective House." Sections in order: Diary → Legislation (assign typist) → Typist → Proof Reader → Legislation (send for approval) → Secretary (approve; send for fixing) → Legislation (fix question) → Translator (generate PDF) → Secretary (final approval for publishing). Type change allowed Starred→Unstarred only (Q34); content editable at translator stage (Q35); clubbing of questions done by the House, not members (Q126).
- **Department reply workflow**: departments log in, see questions pending for reply (starred/unstarred), draft replies (both .doc and .pdf uploads required, Q40), send — reply goes to the Minister and to the House (Q45). Wrong-department transfer supported (Q44). Drafts editable until sent; attachments can be overwritten (Q41–43).
- **Bills module** (Q57–71): departments draft bills in their login (Bills tab → New → details → Send to house). Mandatory unique Reference No. (Q58–59). Legislation login updates Bill No. and status (Q60, Q66). System generates stage-stamped versions: "to be introduced", "as introduced", "as passed" files (Q62). Distribution per stage: To-Be-Introduced file to members and table officers (Q63); As-Introduced copy to the other house in bicameral legislatures (Q64); to committee for consideration (Q65 — "bills need to be considered by the committee"). Multiple dates of consideration recorded (Q67). Bills cannot be deleted (Q69). Draft may change any number of times, "but once it is forwarded to the next stage, then that document is locked for any further modification" (Q70).
- **List of Business (LOB) module** (Q80–110): "To create the daily agenda of the house digitally" (Q99). Business items entered under **Event Types** — "the Heads according to the rules and procedures of the legislature. Under these heads various business content is entered in the LOB. E,g. Papers laid in the House, Questions, Bills-to be introduced" (Q86). Papers attached from local system or from departments (Q89–91); annexures (Q96); bilingual creation in English + local language simultaneously (Q83–84); one-click submission to the Legislative Secretary; Secretary approves or returns the LOB (Q97–98, Q110). "After approval by the Secretary, the approved LOB will be visible on the Public Portal" (Q109).
- **Committee module** (Q127–150): committee type masters, committee creation/formation/constitution (chairman & member mapping), room masters with photo, room booking (single/multiple dates, half/full day) with administrator approval, committee e-files and draft papers with forwarding to users.
- **Reporter module — verbatim record production** (Q202–226): "a work flow based web application for preparation of Verbatim Records of House Proceedings." Chief Reporter assigns time slots (turns) to reporters; each prepares a turn file; chief reporter merges, approves, returns for changes; Reporter Admin (Director) gives final approval; "Publishing of hourly verbatim on public portal" — final PDF. Rotation time of reporters managed (Q22).
- **Member e-book** (Q16–19, Q117): biometric attendance in the House; reading budget files; reading replies; receiving papers in the member inbox; committee membership visible.
- **Roles/access** (Q51–55, Q111–128): role-request-based access control; roles include Member, Secretary, Legislation, Diary, Typist, Proof Reader, Translator, LOB, Reporter/Chief Reporter, Department/Nodal Officer, Admin, Super Admin.
- **Public axis** (Q152–167, Q109, Q223): public portal shows Notices Received, Questions, Government Bills, Members, Paper Laid, Committee Reports; House Proceedings (unedited) and provisional session calendars appear on the live notice board; LOB and hourly verbatim publish to the public portal upon approval.

### Granicus — Agenda LE (Legistar) [Evidence layer A — product page]

- Positioning: "The original end-to-end agenda and meeting management solution designed specifically for government… ideal for large government organizations." "Built for the largest organizations with the most complex legislative processes." "Legistar scales and adapts to support the full legislative process." Framing sentence: "Using digital legislative management solutions allows government to streamline cross-departmental workflows, modernize the public meeting experience…"
- Functionality: custom forms for agenda item submission "for resolutions, contracts, ordinances, and more"; configurable automated approval routing with deadline alerts; Office 365/Word integration for staff reports; in-meeting roll call, minutes, votes, speaker lists, public comment; Legislate — online agenda review/notation tool for elected officials; granular permissions limiting access to confidential/sensitive items; public web portal publishing ADA-friendly agendas and minutes; unlimited users/storage.
- Reading: the center of gravity is the **meeting cycle** (agenda → meeting → minutes → portal). Legislative vocabulary (ordinances, resolutions, "full legislative process") attaches to document-typed items, but no bill-stage machinery (no introduction/as-introduced/as-passed versioning, no bicameral exchange, no member submission workflow) is claimed on the page. This is the between-poles specimen.

### Quorum [Evidence layer A — product page, boundary counterpart only]

- Positioning: "AI Public Affairs Software" for government affairs teams; "Stay ahead of policy changes with legislation and dialogue tracking across the US and the EU"; products Federal/State/Local/School Board for tracking bills, regulations, dialogue; plus grassroots advocacy, stakeholder management, PAC, contacts (KnowWho), reporting.
- Reading: the bills here are **objects of monitoring and influence**, consumed from outside; the operator never creates, advances, or records legislation. Confirms the observer/actor position as a different Type (Legislative Tracking Platform / advocacy family), not this one.

### Counterparty pass evidence — Government Meeting / Agenda Management [Evidence layer A — product pages, 2026-09-07]

Summarized from the paired research (Granicus LE/OE, Diligent Community, OpenMeeting): clerk-run cycle of agenda assembly → public notice → conducted meeting (roll call, votes, speakers) → approved minutes as public record; public axis (notice + record) as the discriminator vs confidential board portals; legislative-item depth (persistent numbered items, ordinance types, readings) varies by jurisdiction and is explicitly recorded as a variant there.

## Cross-product Comparison

| Dimension | NeVA (chamber inside pole) | Legistar / agenda family (between poles) | Quorum (external pole) |
|---|---|---|---|
| Operator | House secretariat (clerk apparatus) with departmental roles | clerk / clerk's office | government-affairs / advocacy team |
| Whose business | the House's own legislative business | the body's public meeting cycle | other organizations' policy interests |
| Central object | bill lifecycle + member business + daily LOB | agenda item → meeting → minutes | bill as monitored object |
| Bill/measure machinery | stage-stamped versions (to be introduced / as introduced / as passed), status, consideration dates, bicameral send-to-other-house, committee referral | document-typed items (ordinances, resolutions) through approval routing | read-only tracking |
| Daily business instrument | LOB — event types from the rules of procedure, secretary approval, public publication | agenda assembled from items, published as notice | n/a |
| Member/executive participation | members submit questions/notices; departments draft bills and replies; papers laid | elected-official review tool; departmental item submission | n/a (users are watchers) |
| Official record | verbatim proceedings (turn-based reporter pipeline, hourly publication); question books | minutes + votes; timestamped video | n/a |
| Public axis | per-house public portals, multilingual | public portal (ADA) | n/a |
| Confidentiality | role-scoped access (secretariat roles) | granular permissions for confidential items | n/a |

Stable across the inside-pole + between-pole samples (layer B):

- a **bill/measure-like tracked item** with document versions tied to process stages and approval gates
- a **daily/periodic business instrument** (agenda / list of business) whose item vocabulary is set by the body's rules, approved before publication
- **operator asymmetry**: a secretariat/clerk apparatus operates the process; members and (in chamber systems) executive departments are participants; the public receives publications
- **stage-stamped document production and publication** as the system's output

Not common to both poles (therefore variant, not invariant):

- parliamentary question machinery (starred/unstarred/short-notice) — Westminster-tradition feature, deep in NeVA, absent from the agenda family's claims
- bicameral exchange — present in NeVA; unknown/not claimed in the agenda family
- verbatim (Hansard-style) record pipeline — deep in NeVA; the agenda family produces minutes instead
- in-meeting conduct tooling — central in the agenda family (roll call, voting, speakers), incidental in NeVA's evidence

## Canonical Abstraction

### L0 — Defining Invariant (three jointly-held properties)

1. **The measure of record under the body's rules** — a persistent, individually identified legislative instrument (bill / resolution / ordinance-class measure) carrying the chamber's stage-based lifecycle — entry/numbering, stage-by-stage advancement (introduction, referral, consideration, passage), with official versions stamped by stage ("as introduced" / "as passed" class outputs) and stage-locked documents. Remove → a document library or meeting tool, not legislative management.
2. **The chamber's business instrument** — a rulebook-governed daily/periodic business schedule (calendar of business / list of business / order paper, labels vary) that brings measures and other business before the body, assembled by the secretariat and approved before it takes effect. Remove → a bill-tracking database or drafting tool with no chamber business.
3. **The body's own apparatus as operator** — the legislature's secretariat/clerk (not external watchers or the executive alone) runs intake, numbering, advancement, approval, and publication inside the system; members and executive departments participate as counterparties. Remove → legislative tracking platform (external operator) or an executive workflow tool.

Load-bearing jointness: (1) without (2) = drafting/tracking tool; (2) without (1) = agenda/meeting management (the counterparty Type); (1)+(2) without (3) = external legislative tracking.

### L1 — Common Mature Structure

- public publication axis (bills, business instruments, records published to a public portal on approval)
- official record production — journal/verbatim proceedings pipelines (turn-based reporting, staged approval, publication) and/or minutes
- committee machinery as working containers (constitution, members, papers/e-files, rooms, referral of measures)
- member self-service surfaces (submission of business, receipt of papers, e-book/reader)
- executive/department participation interfaces (drafting entry, replies, papers laid)
- document-typed forms/templates, approval routing, deadline alerts, version locking at stage advance
- multi-language document production
- bill drafting support (composition tooling) — claimed as a market category for chamber vendors; only weakly evidenced in the reachable sample

### L2 — Variant / Optional Structure

- parliamentary question machinery (starred/unstarred/short-notice questions with minister rotation, question books) — Westminster/post-colonial tradition
- bicameral exchange (send-to-other-house states)
- papers-laid machinery as a first-class document class
- member services beyond business (attendance capture, salary/billing)
- in-meeting conduct tooling (roll call, e-voting, speaker queues) — central in the meeting-cycle pole
- meeting-cycle packaging for local bodies (agenda/notice/minutes loop) — the Legistar pole, where legislative-item depth varies by jurisdiction
- codification handoff (adopted measures to the statute book) — inferred from market structure, not evidenced
- AI drafting/summarization (era-current)
- on-premise vs government-cloud vs vendor SaaS deployment

### L3 — Vendor-specific / program-specific (research notes only)

- NeVA: "One Nation One Application" program structure; MoU-based per-house onboarding (Prospective/Onboarded/Digital House states); NIC Cloud MeghRaj hosting; per-house "NeVA Unit" logins; dairy-number SMS confirmations; hourly verbatim publication by the Chief Reporter; mNeVA Android app (Android-only per FAQ); bilingual LOB generation; 227-question published FAQ as de facto user documentation.
- Granicus Legistar: Legislate elected-official review tool; Office 365/Laserfiche/DocuSign integrations; LE/OE/PE product line; marketing statistics (75% workflow time reduction etc.) — excluded from evidence per counterparty pass.
- Quorum: Quincy AI assistant, KnowWho contact data, 50-state + EU coverage — boundary evidence only.

### Historical / market-sample check

The paper-era chamber practice — clerk's bill file with engrossed copies per stage, printed calendars of business, committee reports filed in, journals/verbatim produced by reporters — satisfies all three L0 properties with no digital system at all. NeVA is explicitly a digitization ("paperless") program, confirming the direction of travel. The definition does not depend on portals, member e-books, AI, or Westminster question machinery. Check passes; older, regional, and platform-native implementations (a state legislature's in-house LIS, a national parliament's document system) fit the core.

## Vendor-specific Findings

See L3. Additional: the vocabulary collision itself is a market fact — the agenda-management leader brands its product line "digital legislative management" while its functionality is meeting-cycle-centered; the one program with deep documentation (NeVA) does not use the phrase "legislative management" prominently (it says "work-flow system" / "Digital House" / "Digital Legislatures"). The market phrase "legislative management system" therefore has no single canonical implementation to point at; the Type must be defined structurally.

## Boundary Findings

1. **vs Government Meeting / Agenda Management (§24, processed) — JOINT REVIEW DISCHARGED from this side.** The counterparty pass proposed the seam: its Type centers the recurring public meeting cycle of local/regional bodies (agenda → notice → meeting → minutes → public record); this leaf should center the chamber business workflow. The evidence supports keeping both, with Legistar as the confirmed straddler: it carries meeting-cycle machinery plus document-typed legislative items (ordinances/resolutions) but no bill-stage versioning, no bicameral exchange, no member-submission workflow. Removal tests from this side: strip the bill-stage lifecycle + chamber business machinery, keep the notice/meeting/minutes loop → Government Meeting / Agenda Management; add full bill-stage machinery with member and department participation → this Type. The two Types form a spectrum along **legislative-business depth**; the public axis is shared by both (it is the board-portal family that inverts it). Both documents should cross-reference the straddling products.
2. **vs Legislative Tracking Platform (§24 sibling, unprocessed)** — Quorum evidence confirms the seam proposed by earlier passes: external operator (advocacy/government-affairs teams) monitoring bills across jurisdictions vs the legislature operating its own business. The bill is a monitored object there; a managed record here. Flag for that pass: the boundary is operator position + lifecycle ownership, not the presence of bills.
3. **vs Court Case Management System (§24)** — both have numbered instruments with stages and records; the court adjudicates disputes under procedure, the legislature produces law under its rulebook; participant sets differ (parties/counsel vs members/executive). Different Type.
4. **vs Board / Corporate Governance Platform (§10, processed)** — echo of the two prior passes: a governed body's confidential meeting cycle vs a public legislative body's production workflow; public-sector board portals straddle the board side, Legistar-family straddles this side. Boundary held.
5. **vs Government Transparency Portal (§24, processed)** — the portal publishes; this Type produces and approves what gets published. Producer vs destination.
6. **vs Rulemaking & Public Consultation Platform (§24, unprocessed)** — executive-agency rule processes and public comment collection vs the legislature's own bill/business machinery. Adjacent; no overlap in operator or instrument.
7. **vs Advocacy Platform (§24, processed)** — mobilizing supporters toward legislative targets vs running the legislature. Already separated from the tracking side in that pass; consistent here.
8. **vs Government Records Management (§24)** — legislative instruments are public records that this Type produces; enterprise retention discipline is downstream. Capability donor, not a Type overlap.

## Uncertainties

- **US state-legislature commercial pole under-sampled**: AOT (and any comparable chamber-scale vendor) unreachable; the claim that bill drafting/composition tooling is a common L1 capability rests on weak evidence (market structure only) and is flagged weak.
- **Regional skew**: the deepest inside-pole evidence is India's Westminster-tradition program (questions, minister rotation, papers laid). US-Congress-style and parliamentary chambers outside India are represented only indirectly (counterparty pass is US local government). The question machinery, bicameral exchange, and papers-laid class are treated as variants accordingly.
- **Journal vs verbatim**: the two record forms (proceedings verbatim vs journal of actions) appear in different traditions; NeVA evidences verbatim production; the agenda family evidences minutes. The canonical claim is limited to "official record production" without asserting which form.
- **Codification handoff** not evidenced; kept out of all levels except an inferred market note.
- **Legistar's deeper legislative features** (if any exist beyond the product page) not directly observed; its placement on the spectrum is based on claimed functionality at product-page depth.

## Final Synthesis

A Legislative Management System is the legislative body's own system of record for its business: it manages measures/bills through a rulebook-defined, stage-based lifecycle with stage-stamped official versions; it assembles and approves the chamber's daily/periodic business instrument; and it is operated by the body's own secretariat/clerk apparatus, with members and executive departments as participating counterparties and the public as the recipient of approved publications. Record production (journal/verbatim/minutes), committee machinery, member self-service, executive interfaces, and publication portals are the common mature layer; the question machinery, bicameral exchange, and in-meeting conduct tooling are variants tracking political tradition and body type. The Type's neighbors are defined by what they lack: the meeting-cycle family lacks the bill-stage lifecycle and business machinery; the tracking market lacks the operator position; the court lacks the production purpose. The straddling products (Legistar-class) are the market's honest admission that the two public-sector Types form a spectrum along legislative-business depth.
