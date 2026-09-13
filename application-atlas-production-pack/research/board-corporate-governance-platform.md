# Research Notes — Board / Corporate Governance Platform

## Research Goal

Understand what board / corporate governance software (market names: "board portal", "board management software", "board meeting software") actually is as an Application Type: its core objects, its defining workflow, its roles, its rules, and where its boundary lies against neighboring Types (corporate governance suites, association board management, public-sector meeting/agenda management, virtual data rooms, meeting scheduling).

## Initial Boundary (hypothesis before research)

- Core hypothesis: software that replaces the physical board pack and supports the board meeting cycle: agenda → materials → secure distribution → meeting → minutes → governance record.
- Likely users: corporate secretary / board administrator (operator), directors/trustees (consumers, often senior and non-technical).
- Likely confusions:
  - "Corporate Governance Platform" as a broader GRC-adjacent suite (Diligent One) vs the board-centric application.
  - Association "Committee / Board Management" (§25 leaf) — same software sold to associations.
  - Public-sector meeting/agenda management (§24 leaves) — school boards and councils use board-portal-lineage products.
  - Virtual Data Room — document sharing without the governance meeting cycle.
- Unknowns: exact meeting state machines per product; how deep minutes workflows go; whether public-sector variants are the same Type or a separate one.

## Research Questions

1. What are the core objects? (board/committee, member, meeting, agenda, board pack, minutes, decisions, actions, resolutions, repository)
2. What is the defining workflow, and does it have a state machine?
3. Who operates the system vs who consumes it, and how do their interfaces differ?
4. What rules matter? (permissions, versioning, confirmation/locking, audit, confidentiality)
5. What is common-but-not-defining? (voting, e-signatures, questionnaires, evaluations, AI, secure messaging, video integration)
6. What variants exist? (enterprise vs SMB vs nonprofit vs public sector; suite vs pure-play; regional/data-residency)
7. Where are the boundaries vs adjacent Types, and what would have to be removed to become that other Type?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Vendor | Tier / philosophy | Why selected |
|---|---|---|---|
| Diligent Boards | Diligent | Enterprise flagship; security-grade; part of the Diligent One governance suite | Market leader; shows suite-extension direction |
| OnBoard | Passageways | Mid-market modern SaaS; "governance system of record" + director-adoption focus | Shows the four-pillar structure and board-lifecycle vocabulary |
| Azeus Convene | Azeus Systems | International (HK-origin, global); all-in-one portal; separate AGM product line | Non-US/regional sample; shows AGM adjacency |
| BoardPro | BoardPro Ltd | ANZ SMB / nonprofit / schools; workflow-first, simple | SMB tier; best-in-class public help documentation of the meeting workflow |

Also observed (variant evidence, not primary sample): Diligent BoardEffect (nonprofits/higher-ed), Diligent Community (school boards / local government — public-sector variant), OnBoard industry pages (associations, government, healthcare, higher-ed, nonprofits).

## Sources

All fetched 2026-09-06.

- Diligent Boards product page — https://www.diligent.com/products/boards/ (Tier 2)
- Diligent Community product page — https://www.diligent.com/products/community/ (Tier 2)
- OnBoard homepage / platform navigation — https://www.onboardmeetings.com/ (Tier 2)
- BoardPro homepage / feature navigation — https://boardpro.com/ (Tier 2)
- BoardPro Help Centre — https://help.boardpro.io/en/ (Tier 1)
- BoardPro Help Centre: Meeting Workflow collection (91 articles, index) — https://help.boardpro.io/en/collections/3796866-meeting-workflow-from-building-the-agenda-to-confirming-the-minutes (Tier 1)
- BoardPro Help Centre: "Meeting Stages and Flow" — https://help.boardpro.io/en/articles/376886-meeting-stages-and-flow (Tier 1)
- Azeus Convene homepage — https://www.azeusconvene.com/ (Tier 2)

Source-access limitations:

- OnBoard support/help center (support.onboardmeetings.com / help.passageways.com) was not reachable in this environment (transport error on first attempt; not retried further per network rules). OnBoard observations are therefore positioning/navigation-level (Tier 2), not operational-doc-level.
- Diligent and Convene operational help docs were not fetched; their observations are positioning/navigation-level.
- Vendor marketing statistics on the fetched pages (e.g., hours saved, % of Fortune 500, customer counts, ROI figures) were deliberately not used as evidence for any claim.
- Only BoardPro provided Tier-1 operational documentation in this pass; cross-product claims about workflow mechanics are calibrated accordingly (see Evidence Calibration).

## Product A — Diligent Boards (Diligent)

### Key observations (evidence layer A, positioning-level)

- Self-description: "board management software" / "board portal"; "automate meeting prep, secure sensitive data"; "the full meeting lifecycle — from book creation to decision making".
- Meeting-cycle capabilities named on the product page: agenda building, board book compilation ("Smart Builder": upload source materials → complete first draft of the board book), AI book summary, AI-generated minutes ("Smart Minutes"), action tracker ("turn notes and minutes into clear, trackable action items"), secure voting with e-signature and audit logs, board messaging, live streaming of meetings inside the platform.
- Governance compliance machinery: "From D&O questionnaires to pre-reads and voting, everything lives in one place. Automated reminders and built-in workflows."
- Security framing: "Share confidential updates and documents with confidence. Role-based permissions, encryption, and audit trails."
- Roles addressed: Corporate Secretary, Executive Assistant (board admin), C-Suite, Directors & Trustees; also General Counsel.
- Suite context: Diligent One Platform = board management + GRC (risk, compliance, audit) + Entities (subsidiary/corporate record). Board management is one product line inside a governance suite.
- Sibling variants from the same vendor: BoardEffect ("secure, flexible board management software for nonprofits and higher education"); Diligent Community ("increase transparency, streamline governance and empower your school board or local government").
- Company-type solutions: public companies, private companies, nonprofits, education & local government; corporate service providers (delivering governance at scale for many client boards).

## Product B — OnBoard (Passageways)

### Key observations (evidence layer A, positioning-level)

- Self-description: "board management software & board portal"; platform organized into four named pillars:
  1. **Meeting Lifecycle Management** — Agenda Builder (drag-and-drop), Committee Management & Multi Org Support ("organize and direct subsidiary boards & committees"), Minutes Builder ("create minutes within the Agenda"), Task Management, Microsoft 365 integration.
  2. **Governance System of Record** — Dashboard homepage, Director & Officer Questionnaires, eSignatures & DocuSign integration, File & Document Management, Secure Messenger.
  3. **Director Prep & Engagement** — Approvals ("secure built-in decision-making" / voting-and-approvals), iOS & Android apps, Meeting Analytics, Notes & Annotations, Zoom & Teams video conferencing integration.
  4. **Board History & Continuity** — Board Assessments, Diversity Reporting, Roles & Terms Management, Surveys, Skills Tracking.
- Governance-library framing: "Place policies and past packets in one secure hub… Keep drafts and downloads out of email and control access by role, replace documents in place, and keep clean records for audits."
- Security framing: "no inbox copies and no stray downloads… access with role permissions, log every action, and set automatic retention by default."
- Continuity framing: "Carry board history into every meeting… a living record… incoming leaders learn the why behind past choices."
- Pain-point framing (what the Type replaces): "Tired of Manual Board Book Assembly — ditch the paper, PDFs, and endless emails"; "Worried About Director Pushback on New Software."
- Roles: Administrators & Board Professionals, CoSecs & General Counsels, CEOs & Executive Leadership, Directors & Trustees, IT leaders.
- Industries: associations, financial services, government, healthcare, higher education, nonprofits, technology, VC/PE.
- AI suite: AI Agenda, AI Book, AI Minutes, AI Assist, AI Meeting Insights.

## Product C — Azeus Convene

### Key observations (evidence layer A, positioning-level)

- Self-description: "board portal", "all-in-one AI-powered board portal… for intelligent governance"; "turn meeting minutes into a reliable source of truth".
- Capabilities named: Automated Minutes (live discussions/transcripts/recordings → structured minutes), AI Companion, Board Dashboard ("meetings, decisions, and actions in one unified dashboard"), Skills Tracking, Voting & Resolutions ("secure voting anytime, anywhere; track decisions and resolutions in a centralized dashboard"), integrations (calendar, video conferencing, e-signature, document storage, authentication — including national digital-identity schemes such as Norwegian BankID / UAE Pass / Nafath), security (AWS hosting, document encryption, GDPR).
- Ecosystem adjacency: ConveneAGM (separate product: registration, voting, Q&A for shareholder/member general meetings in physical/virtual/hybrid formats), Convene Assure (board evaluation), Convene in Teams, ESG reporting (separate brand).
- Industry editions: nonprofits, banks, credit unions, healthcare, universities.
- Pricing model: per-user, per-year license.
- User-profile pages exist for corporate secretaries and board members.

## Product D — BoardPro

### Key observations (evidence layer A, Tier-1 operational documentation — strongest evidence in this sample)

- Self-description: "board management software & board portal" for SMEs and non-profits (also schools); ANZ-focused.
- Feature set organized explicitly by meeting phase:
  - **Before**: Meeting Schedule, Agenda Builder, Interest Register, Board Packs, Annual Work Plan.
  - **During**: Actions, Voting, Minutes, Decision Register, Board Pack Annotations.
  - **After**: Governance Repository (document centre), eSignatures, Flying Minutes, Sub-committees.
- Pack mechanics (homepage): "Build the agenda, and the board pack builds itself. Clone last meeting's agenda, attach papers as they come in, and publish — BoardPro compiles the pack, page-numbers it, and sends it securely to your board. Late change? Republish and it re-numbers itself."
- Security framing: "Packs, minutes and decisions live inside BoardPro — never as email attachments, with sensitive papers behind access controls"; MFA, encryption, "board-grade permissions… revoke access anytime", data residency in Australia.
- Help Centre structure (Tier 1) confirms the operational workflow:
  - Collections: "Meeting Workflow — From Building the Agenda to Confirming the Minutes" (91 articles), "Managing your Board Account", "Board Members Guide — From Annotating to Voting", "Between Meetings and Action List", "Committees".
  - Meeting workflow sub-collections in order: Adding a Meeting → Draft Agenda → Smart Agenda Items → Publishing the Agenda and Building the Board Pack → Draft Minutes → Minutes in Review → Confirming Minutes → Signing Minutes → Voting.
  - Draft-agenda mechanics: add/edit/delete agenda items, sections, presenters, per-item time, breaks, attachments (uploaded documents or governance documents), external links, appendices, multi-day meetings, email draft agenda for collaboration, official meeting notice + agenda email, clone/copy previous agenda, rebuild.
  - Smart Agenda Items: Action List (auto-carried actions from previous meetings), Confirm Minutes (link a past meeting so its minutes are included for confirmation), Interests Register.
  - Pack mechanics: publish agenda → board pack generated; email pack; edit published agenda → republish → new pack version; Agenda Change Log; previous versions of agenda documents retained; replace a document without losing director annotations; roll back from Draft Minutes to Published Agenda; board pack read receipts ("see who has opened the Board Pack"); meeting reminders; email history.
  - Minutes mechanics: take minutes per agenda item (notes, decisions, actions); auto-save; edit attendees to actual attendance; reassign a minute to another agenda section; email draft minutes; minutes lifecycle "Draft → In Review → Confirmed"; minutes can still be edited during review; confirmation typically at a subsequent meeting; reverse confirmed minutes (with governance implications); minutes signing (request signatures from chair/designated signatory; sign in-product).
  - Voting: set up a formal vote on the agenda; minute taker records votes; FAQs.
  - Roles/permissions: Administrator, Board Secretary, Chair, Senior Executive access levels; board members as consumers.
- Meeting state machine (Tier 1, "Meeting Stages and Flow"):
  - Agenda stages: **No Agenda → Draft Agenda → Published Agenda**. Meeting status controls which actions/options are available. Draft agenda restricted to certain roles; PDF titled "Draft Agenda". Publishing makes the agenda visible to members and enables pack generation; agenda can still be edited and republished (new pack version; original retained; changes logged).
  - Minutes stages: **Draft Minutes → Minutes in Review → Minutes Confirmed**. Draft minutes editable, agenda can be corrected to reflect what actually happened; roll-back possible. In Review: PDF distributed for review/feedback, still editable. Confirmed: "the meeting is locked to preserve the approved record"; minutes typically confirmed at a subsequent meeting.
  - Draft minutes remain visible to board members throughout draft/review (product-specific policy).

## Product E (variant evidence) — Diligent Community (public-sector variant)

### Key observations (evidence layer A, positioning-level)

- Self-description: "governance software for public sector boards"; "purpose-built for public sector governance boards, councils, and committees" — school boards, municipal councils, special districts.
- Same core loop as corporate products: "build agendas, distribute meeting materials, capture votes and actions and create meeting minutes"; agenda creation/approval/publishing workflows.
- Public-sector additions: "accessible, ADA-compliant public transparency site" giving the public access to agendas, policies and supporting documents; livestream manager broadcasting public meetings to the website; AI minutes with closed captions from livestreams; goal tracking shared publicly; policy lifecycle management.
- Security framing retained: role-based access, permissions, protection of sensitive documents.

## Cross-product Comparison

| Dimension | Diligent Boards | OnBoard | Azeus Convene | BoardPro | Diligent Community (variant) |
|---|---|---|---|---|---|
| Governed bodies & committees | yes (suite context; multi-body) | yes (Committee Management & Multi Org) | yes (dashboard over meetings/decisions) | yes (Sub-committees; Committees collection) | yes (boards, councils, committees) |
| Member roster / roles & terms | roles addressed (CoSec, directors) | Roles & Terms Management explicit | user profiles | roles: Administrator/Secretary/Chair/Member | role-based access |
| Meeting as work unit | "full meeting lifecycle" | Meeting Lifecycle Management | meetings in dashboard | meeting object with status machine | pre-/during-/post-meeting |
| Agenda builder | yes (AI-assisted) | yes (drag-and-drop) | yes (Agenda Builder page) | yes (sections/items/time/presenters; draft→publish) | yes (creation/approval/publishing) |
| Board pack / book compile & distribute | yes (Smart Builder) | yes (book assembly pain-point framing) | yes | yes (compile, page-number, republish, versions, change log) | yes (distribute materials) |
| Member-scoped confidential access | role-based permissions, encryption, audit trails | role permissions, no inbox copies, retention, audit log | encryption, AWS, GDPR | board-grade permissions, revoke, MFA, data residency | permissions + public split |
| Director-side reading & annotation | yes (AI summaries, prep insights) | Notes & Annotations, apps | yes | Board Pack Annotations (preserved across republish) | yes |
| Minutes workflow | AI minutes generation | Minutes Builder within agenda | Automated minutes from transcripts | Draft → In Review → Confirmed + signing | AI minutes from livestream |
| Decisions / resolutions / actions | Action tracker | Task Management; approvals | Voting & Resolutions dashboard; actions | Actions, Decision Register, Flying Minutes | capture votes and actions |
| Voting | secure voting, e-signature, audit logs | Approvals (voting-and-approvals) | secure voting anytime/anywhere | formal vote setup; minute-taker recording | digital voting with auto-calculation |
| E-signatures | yes (DocuSign integration) | yes (eSignatures & DocuSign) | yes (e-signature integrations) | yes (minutes signing; eSignatures) | — |
| Repository / governance library | yes (suite) | yes ("governance library", policies + past packets) | yes | Governance Repository | document library (internal + public) |
| Notices / reminders / calendar | automated reminders | yes | calendar integrations | meeting notice, reminders, email history | yes |
| Video / hybrid meeting | live streaming in platform | Zoom & Teams integration | video conferencing + integrations | remote meeting URL in agenda | livestream to public site |
| Secure messaging | board messaging | Secure Messenger | — | — | — |
| AI layer | book builder, summaries, minutes, prep insights, news | AI Agenda/Book/Minutes/Assist/Insights | automated minutes, AI companion | AI Assistant, AI Minutes | AI minutes + captions |
| Governance-suite extensions | D&O questionnaires, entity management, GRC, market intelligence | D&O questionnaires, assessments, skills/diversity tracking, surveys | board evaluation (Assure), AGM product, ESG brand | annual work plan, interest register | goal tracking, policy lifecycle |
| Public transparency surface | no (Community is the separate variant) | no | no | no | yes (ADA-compliant public site) |
| Customer tier | enterprise (public/private cos, CSPs) | mid-market + associations/higher-ed | international mid/enterprise, banks | SMB / nonprofit / schools | public sector |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as this Type:

```text
Governed body (board or committee) with an identified member roster
└── Meeting as the unit of governance work (dated occasion of a specific body)
    ├── Agenda structuring the meeting
    ├── Board pack: meeting materials assembled against the agenda
    │   and distributed to the body's members under member-scoped confidential access
    └── Governance record: minutes with recorded decisions/resolutions/actions,
        confirmed/approved and retained as the body's official record
```

Four properties. Remove any one and the product drifts into a different Type:

1. **Governed body with member roster** — without bodies/members, it is generic document sharing or generic meetings.
2. **Meeting as the governance work unit** — without the meeting cycle, it is a document repository.
3. **Agenda-structured board pack under member-scoped confidential distribution** — without the pack addressed to the body's members, it is email/file sharing; without confidentiality scoping, it is an intranet.
4. **Confirmed governance record retained over time** — without minutes/decisions as an approved, persistent official record, it is meeting productivity software.

Historical / market-sample check: early board portals (paper-pack replacement era), regional products (ANZ, Asia), nonprofit/school/credit-union boards, and association boards all satisfy this L0 — none of them require AI, voting modules, questionnaires, evaluations, or public transparency sites to be recognizable. The L0 deliberately excludes: AI assistance, voting/e-signature, D&O questionnaires, evaluations, entity management, public sites, video integration, secure messaging.

### L1 — Common Mature Structure

Present across the researched sample (evidence layer B), expected in any mature product, but not definitional:

- Agenda builder with sections/items, presenters, time allocations; draft → publish lifecycle; cloning of previous agendas
- Pack compilation: automatic assembly and page numbering; republishing on late change with new version; change log; retention of prior versions; document replacement that preserves director annotations
- Director-side reader: agenda-linked document reading, personal annotations/notes, mobile/tablet apps, offline access, read receipts
- Minutes workflow: minutes drafted against the agenda; review; confirmation (typically at the next meeting); signing (e-signature)
- Decisions/resolutions and action items with owners and follow-up tracking; decision register
- Voting on motions (in-meeting or out-of-cycle)
- Governance repository: policies, past packs, searchable library
- Meeting notices, reminders, calendar integration; video-conferencing links/integration
- Role-based permissions, audit trail, encryption, MFA; materials kept inside the platform rather than email
- Multi-body support (boards + committees; sometimes multi-organization/subsidiary boards)
- AI assistance (2026 market): book drafting, summarization, minutes generation, Q&A over board history — now present in all four sampled products, but a recent layer, not definitional

### L2 — Variant / Optional Structure

Depends on segment, geography, regulatory posture, business model:

- **Public-sector variant**: public transparency site (agendas/minutes/policies publicly accessible, accessibility compliance), livestreaming, public goal tracking (Diligent Community; also the school-board/council market)
- **Governance-suite extensions**: entity/subsidiary management, D&O questionnaires, conflict-of-interest/interest registers, board evaluations/assessments, skills & diversity tracking, board education, proxy/shareholder analytics (suite vendors)
- **Annual governance planning**: annual work plan / meeting schedule planner
- **Out-of-cycle governance**: flying minutes / written resolutions outside meetings
- **AGM support**: shareholder/member general meetings as a separate product line (ConveneAGM)
- **Deployment & residency**: multi-tenant SaaS vs private cloud/on-prem; data-residency commitments (e.g., ANZ-only storage); regional identity integrations (national eID schemes)
- **Industry editions**: banks/credit unions, healthcare, universities, nonprofits, associations
- **Corporate service provider model**: one platform administering many client organizations' boards

### L3 — Vendor-specific Structure (research notes only)

- Diligent: Smart Builder / Smart Minutes / Smart Risk Scanner naming; Diligent One platform bundling; proxy & shareholder insights; executive compensation benchmarking; BoardEffect/Community product split
- OnBoard: "Governance IQ" framing; Meeting Analytics; Diversity Reporting; four-pillar navigation naming
- BoardPro: Smart Agenda Items; Flying Minutes; Impact subscription/partner program; "Draft Agenda"/"Agenda" PDF title convention; draft minutes visible to members policy
- Convene: ConveneAGM / Convene Assure / Convene in Teams product lines; per-user-per-year licensing; national-ID integrations
- All marketing statistics (hours saved, ROI, customer counts, market-share claims) — not usable as evidence

## Evidence Calibration

- Layer A (directly observed): BoardPro meeting state machine and workflow mechanics (Tier-1 help docs); product capability inventories of Diligent/OnBoard/Convene (Tier-2 positioning pages).
- Layer B (cross-product commonality): agenda→pack→minutes loop; member-scoped security; decisions/actions; repository; AI layer — observed across all four sampled products.
- Layer C (canonical inference): the four-element L0; the "meeting status gates available actions" principle generalized beyond BoardPro (only BoardPro documented it explicitly — written qualitatively in the final document, not as a universal rule with named stages).
- Precision rule: no numeric limits, no exact retention periods, no specific encryption modes asserted. BoardPro's stage names are cited as one product's implementation, not as an industry standard.

## Vendor-specific Findings

See L3 above. Additionally: BoardPro's policy that draft minutes remain visible to board members during draft/review is product-specific and was not generalized. Diligent's corporate-service-provider positioning (administering many client boards) is a business-model variant, not a structural feature.

## Boundary Findings

1. **vs "Corporate Governance Platform" (§11 leaf)** — The directory contains both "Board / Corporate Governance Platform" (§10) and "Corporate Governance Platform" (§11). Market products conflate the two: the leading vendors sell board management as the entry point to broader governance suites (Diligent One adds entities/risk/compliance). Probable duplicate/alias leaves. Recorded for joint review; this document treats the board-centric application as the core and describes suite extensions as optional.
2. **vs "Committee / Board Management" (§25 leaf)** — Association-market instance of the same software (OnBoard markets an association industry page; BoardPro serves nonprofits). The core model is identical; the association context changes vocabulary (trustees, chapters) not structure. Probable audience-variant/alias; flagged.
3. **vs Legislative Management System / Government Meeting / Agenda Management (§24 leaves)** — Real overlap: Diligent Community sells board-portal-lineage software to municipal councils and school boards, with agenda approval workflows and public publishing. Distinguishing center of gravity: this Type is organized around a governed body's confidential meeting cycle and its official record; legislative/agenda management is organized around the public legislative/clerk workflow (readings, ordinances, public comment). The public-sector board variant sits between them — flagged for joint review.
4. **vs Virtual Data Room** — A VDR shares documents with external parties for a transaction; it has no governed body, no recurring meeting cycle, no minutes/record. Remove the meeting cycle and the governance record from this Type and it degrades into a VDR-like document space.
5. **vs Meeting Scheduling / Meeting Productivity (AI meeting assistants, transcription)** — Those Types center on finding times or capturing what was said in any meeting; they have no governed body, no member-scoped pack, no official record. Minutes-from-transcript AI in board software is a capability imported from that adjacent Type, not evidence of Type overlap.
6. **vs Enterprise Content Management / Document Management** — The governance repository is a bounded library for one governance function; ECM is organization-wide content lifecycle. The repository alone is not this Type.
7. **vs Legal Entity Management** — Suite module (Diligent Entities); core object is the legal entity/corporate record, not the board meeting cycle. Adjacent, often bundled.
8. **Degradation tests**: remove the member roster → generic meeting notes tool; remove the pack → minutes-only tool; remove the record → secure file sharing; remove confidentiality scoping → intranet; remove the body/meeting structure → VDR.

## Uncertainties

- Exact meeting-stage names and transition rules beyond BoardPro are unverified (other vendors' help centers not fetched). The final document therefore describes the stage pattern qualitatively and attributes the explicit state machine to the researched implementation pattern, not to an industry standard.
- Whether minutes confirmation "locking" (immutability after confirmation) exists in other products is unverified; written as "the confirmed record is treated as final" without absolute claims.
- Voting mechanics (recorded vs anonymous votes, quorum handling) were not researched in depth; kept qualitative.
- Offline/remote-wipe behavior of director apps is asserted by the market category but was not directly documented in fetched pages; kept out of the final document or phrased as common expectation without specifics.
- The §11 "Corporate Governance Platform" leaf was not separately researched (out of scope for this pass); the duplication judgment is based on the market convergence visible in the sampled vendors.

## Final Synthesis

A Board / Corporate Governance Platform is the organization's system for administering the work of its board and governing committees. Its defining structure is small: governed bodies with member rosters; meetings as the unit of governance work; an agenda-structured board pack distributed to members under member-scoped confidentiality; and a confirmed governance record (minutes, decisions, resolutions, actions) retained as the body's official memory. Around this core, mature products add the pack-assembly machinery (compile, number, republish, version), the director reading experience (annotations, apps, read receipts), decision machinery (voting, resolutions, e-signatures, action tracking), a governance library, and — increasingly — AI assistance over the board's own history. Variants extend the same core to nonprofits, schools, associations, and public bodies (where a public transparency surface is added), and vendors extend it into governance suites (entities, questionnaires, evaluations, risk). The Type exists because board materials are confidential, the meeting cycle is recurring and formal, and the record must be authoritative — none of which email, file sharing, or generic meeting tools provide.
