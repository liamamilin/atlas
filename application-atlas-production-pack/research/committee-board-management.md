# Research Notes — Committee / Board Management

Research date: **2026-09-07**
Slug: `committee-board-management` — DIRECTORY §25 Nonprofit, Membership & Religious Organizations

---

## Research Goal

Understand what "Committee / Board Management" software actually is as practiced in the nonprofit / association / member-governed market: what objects it manages, who operates it, how the meeting cycle runs, how committees relate to boards, and — critically, because of the pre-existing flag in STATUS.md — how it relates to the already-documented Board / Corporate Governance Platform (§10).

## Initial Boundary

Working hypothesis at start:

- The leaf sits in §25 among AMS / membership / chapter-management leaves, so it plausibly means "managing committees and boards inside a membership organization" — either (a) the AMS-style committee roster module, or (b) board-portal software sold to nonprofits/associations.
- STATUS.md line 1216 (from the §10 pass) flags: "board-corporate-governance-platform (§10) vs committee-board-management (§25): association-market instance of the same software (OnBoard maintains an association industry page; BoardPro sells nonprofit/school editions) — core model identical, vocabulary differs; probable audience-variant/alias — flagged for joint review when Committee / Board Management is processed."
- Neighbors to check: Board / Corporate Governance Platform (§10), Association Management System (§25), Chapter Management Platform (§25), Legislative Management / Government Meeting & Agenda Management (§24), HOA / Community Association Management (§17), Church Management System (§25), Meeting Scheduling / AI Meeting Assistant (§03).

## Research Questions

1. What are the core objects: body, member, role, term, meeting, agenda, packet/book, minutes, decisions, actions?
2. What does "committee" add beyond "board" in these products — is a committee the same object type as the board, or a different structure?
3. Is there roster/term/officer machinery (terms, term limits, expirations, succession)? How deep, and is it definitional?
4. Who operates the software in this market, and how does the role structure differ from the corporate secretary model?
5. How does the meeting cycle run in volunteer/member-governed organizations, and what stages exist?
6. What distinguishes this leaf from the §10 board-portal leaf — structure, or market/audience?
7. What is the boundary against AMS committee modules (registry-attached rosters) and public-sector meeting/agenda systems?
8. Historical check: would older / regional / smaller volunteer-body software still fit the definition?

## Representative Products

Selection rationale: market representation in the association/nonprofit board segment + documentation quality + different product philosophies + different customer tiers. Two overlap with the §10 sample (OnBoard, BoardPro — which is itself evidence for the alias question), two are additional.

| Product | Pole | Evidence tier this pass |
|---|---|---|
| **BoardPro** | nonprofit/SMB/school boards, ANZ; workflow-first, fully documented meeting lifecycle | Tier-1 help center (root, Committees collection, "What is a Committee?") |
| **Boardable** | small nonprofits/community organizations; collaboration-first, transparent per-user pricing | Tier-2 product + Groups & Committees feature page; Tier-1 help center (root, Groups section) |
| **BoardEffect** (Diligent) | mission-driven organizations at scale (healthcare, associations, foundations, churches); suite member | Tier-2 product pages (root, platform, board-management-software); help center not reachable without login |
| **OnBoard** | mid-market SaaS; association industry vertical; governance-system-of-record + AI posture | Tier-2 product site + Roles & Terms feature page; Tier-1 help center + Administrator Getting Started Guide |

## Sources

All fetched 2026-09-07.

**BoardPro (Tier-1)**
- Help Centre root: https://help.boardpro.io/en/ — collections: Meeting Workflow (91 articles), Managing your Board Account (43), Committees (5), Board Members Guide (36), Between Meetings and Action List (20), General Knowledge (29), BoardPro AI (8), Onboarding Guide for New Roles
- Committees collection: https://help.boardpro.io/en/collections/11591805-committees
- "What is a Committee?": https://help.boardpro.io/en/articles/11103553-what-is-a-committee

**Boardable (Tier-2 + Tier-1)**
- Product site: https://www.boardable.com/
- Groups & Committees feature page: https://boardable.com/features/groups/
- Help Center root: https://docs.boardable.com/knowledge
- Help Center Groups section: https://docs.boardable.com/knowledge/groups (Roles in Groups, Group Page, Create/Delete, Add/Remove Users, Group Owner, Discussions on Group Page)

**BoardEffect (Tier-2)**
- Root: https://www.boardeffect.com/
- Platform: https://www.boardeffect.com/platform/
- Board management software features: https://www.boardeffect.com/board-management-software/

**OnBoard (Tier-2 + Tier-1)**
- Product site: https://www.onboardmeetings.com/
- Roles & Terms Management: https://www.onboardmeetings.com/board-portal/roles-and-terms-management/
- Help Center root: https://help.passageways.com/hc/en-us
- Administrator Getting Started Guide: https://help.passageways.com/hc/en-us/articles/41213465822605-Administrator-Getting-Started-Guide

**Local corpus (boundary evidence, no network)**
- research/board-corporate-governance-platform.md + applications/board-corporate-governance-platform.md (§10 pass, 2026-09-06)
- research/association-management-system-ams.md (§25 pass, 2026-09-06) — "committees… are common but optional suite extensions whose depth belongs to sibling Types"
- research/chapter-management-platform.md — already cross-references this leaf

Evidence tags: **[A]** directly observed on an official source for a specific product; **[B]** cross-product commonality; **[C]** canonical inference.

---

## Product A — BoardPro

From help-centre root + Committees collection + "What is a Committee?" [A]

- Self-organized help structure: Meeting Workflow ("From Building the Agenda to Confirming the Minutes", 91 articles, for Administrator / Board Secretary / Chair / Senior Executive access levels), Managing your Board Account, Committees, Board Members Guide ("From Annotating to Voting"), Between Meetings and Action List, General Knowledge for the whole Board, BoardPro AI. The help center itself mirrors the meeting cycle as the product's spine.
- **Committees are dedicated sub-accounts** nested under the main board: "While they are nested under the main board and have the same features, they operate independently. There is no crossover between meetings, actions, decisions, or documents." [A]
- **Per-body people isolation**: "The people in committees are also separate from the main board. Committee Members cannot access board information, and board members cannot access committee content." People (including their interests) can be imported from the main board into a committee; external people can be added. [A]
- Only the Chair, Administrator, and Board Secretary roles can manage the committee page. [A]
- Committees are listed on a Committees page in the main menu; a user can request access from the Account Owner. [A]
- Commercial structure: committees are added as licensed entities at a flat per-committee rate (subscription-level detail — vendor-specific, kept here only). [A]
- From the §10 pass (same vendor, Tier-1): six-stage meeting state machine (No Agenda → Draft Agenda → Published Agenda → Draft Minutes → Minutes in Review → Minutes Confirmed); agenda builder with cloning; action list with owners/reminders; board-details section (people/roles). Segment: ANZ SMB/nonprofit/schools. [A]

## Product B — Boardable

From product site + Groups & Committees page + help center [A]

- Positioning: "Board management software built for nonprofits"; industry verticals: Associations, Healthcare, Community Organizations, Education, Government. [A]
- Feature set: Agenda Builder, Document Center, Digital Board Packet, Minutes Maker ("keep your board's decisions, actions, and institutional history in one secure place"), Discussions, Polls ("vote on motions"), Tasks & Goals, eSignatures, Boardable Video (built-in video + AI transcription/minutes), Surveys, Reporting, Public Sites ("ADA-compliant public hub for agendas, minutes, and policies"), Accessibility ("compliance-focused accessibility features"), Security. [A]
- **Groups = dedicated workspaces** for boards, teams, and committees/task forces. Group home surfaces "meetings, documents, discussions, tasks, polls, goals, and members." [A]
- Group vs Meeting ontology (FAQ): "A Group is an ongoing workspace (with meetings, documents, discussions, tasks, polls, goals, and members). A Meeting is a single event connected to a group, with its own agenda, minutes, and attendees." [A]
- **New-member visibility rule**: "New members automatically see group documents, goals, meetings, discussions, tasks, and polls created after joining. Past discussions, tasks, and polls remain private" (history can be shared by manual add). [A]
- **Cross-group membership**: a person can sit on both the finance committee and the executive committee and access both workspaces; each group keeps its own content separate. [A]
- Continuity framing: "Boards evolve—roles change, leaders rotate, and new members join… keep history centralized so new stakeholders can see past meetings, files, and decisions while respecting role-based access." [A]
- Help center sections: Meetings (create/configure, invitees, agendas, minutes, calendar), Groups (roles in groups, group owner, add/remove users), People (roles & permissions), Polls ("vote on motions and gather opinions"), Motions & Votes, Tasks & Goals, Discussions, Public Site, Reports & Data. [A]
- Pricing posture: transparent per-user pricing with volunteer discounts (vendor commercial detail — kept here only). [A]

## Product C — BoardEffect (Diligent)

From product pages (positioning + feature level; operational help not reachable — Diligent support requires an account) [A, positioning level]

- Positioning: "board software of choice for over 5000 mission-driven organizations" (vendor figure — not used as evidence); named customers/quotes span churches, healthcare foundations, nonprofits, a state corrections department. [A]
- Meeting cycle tools: AI Board Book Summarization; Agenda Builder ("assemble, approve and distribute agendas… drag-and-drop"); Meeting Minutes ("draft, approve and send AI-enhanced minutes and action items"); Digital Board Books; in-product Video Conferencing. [A]
- Collaboration tools: **"Create secure virtual workspaces for committees and working groups"**; Digital Signatures; Surveys, Polls & Voting; Task Management ("track action items… on board and committee projects"); Permission Controls; Annotations & Notes (private or shared, on minutes/policies/documents). [A]
- Development cycle tools: Archive & Document Management; Director Dashboard (KPIs); Assessments & Reports (board evaluations); D&O Questionnaires; Integrations & APIs. [A]
- Platform membership: BoardEffect is part of the Diligent One Platform (GRC suite). [A]

## Product D — OnBoard

From product site + Roles & Terms page + help center + admin guide [A]

- Feature taxonomy (site navigation): Meeting Operations (Agenda Builder; **Committee Management & Multi Org Support — "Organize and direct subsidiary boards & committees with ease"**; Minutes Builder "create minutes within the Agenda"; Task Management; Microsoft 365 integration); Governance System of Record (Dashboard; D&O Questionnaires; eSignatures; File & Document Management; Secure Messenger; Approvals/voting); Director Prep & Engagement (iOS/Android apps; Meeting Analytics; Notes & Annotations; Zoom & Teams integration); Board History & Continuity (Board Assessments; Diversity Reporting; **Roles & Terms Management**; Skills Tracking; Surveys); AI suite (AI Agenda, AI Assist, AI Book, AI Meeting Insights, AI Minutes). [A]
- **Roles & Terms Management (feature page)**: "Centralize director roles, term limits, and tenure"; per-director role, term dates, current term number, and group assignments; flags "roles ending within 180 days, recently expired terms, and members with missing role assignments"; role/class/term settings; notifications when terms near expiry; export "for use in governance reports, nominating committee presentations, and regulatory filings"; tenure visualizations; supports "multiple role types and term structures." Succession framing: "line up candidates before seats open." [A]
- Administrator setup flow (Tier-1 help): Add Members to the Directory (individual/bulk/CSV) → Manage Permissions (Admins/Creators) → **Create Groups** ("organize members into groups for your board and committees") → Review Settings (download permission, 2FA, feature settings) → populate the Resource Library (folders for board and committee documents, folder permissions) → Create a Meeting (invitees & permissions; agenda & meeting book assembly; publish via "Meeting Visibility States") → customize Homepage → invite members → train (OnBoard Academy, training videos). [A]
- Industry verticals include Associations ("enhancing the engagement and productivity of association boards"), Government, Healthcare, Education, Nonprofits. [A]
- Marketing scale claims (meetings/year, customers) — excluded from evidence. [A]

---

## Cross-product Comparison

| Structure | BoardPro | BoardEffect | Boardable | OnBoard | Strength |
|---|---|---|---|---|---|
| Body container: board + committees as parallel units | committees = sub-accounts under the board, independent | secure workrooms for committees/working groups | Groups = dedicated workspaces (board/committee/task force) | Committee Management & Multi-Org; groups for board + committees | **B** — all four |
| Per-body member isolation | explicit (no crossover of meetings/actions/decisions/documents; separate people) | permission controls | per-group content separation; cross-group membership | per-group/per-meeting permissions | **B** |
| Member roster with roles | Chair / Administrator / Board Secretary roles manage | permission controls per user | People; roles in groups; group owner | Directory; roles & permissions; per-director roles | **B** |
| Meeting as the unit of work, with stages | six-stage state machine (§10 pass) | agenda→approve→distribute; minutes draft/approve | meeting = event connected to a group, own agenda/minutes/attendees | meeting visibility states; agenda → book → publish | **B** |
| Agenda-structured pack distributed to members | meeting workflow incl. pack | digital board books | board packet builder | meeting book assembly & publish | **B** |
| Minutes → confirmed record | confirmation stage; locked record | draft/approve, AI-enhanced | Minutes Maker; institutional history | Minutes Builder; AI Minutes | **B** |
| Decisions machinery (motions/votes/polls) | voting in Board Members Guide | surveys/polls/voting | polls; Motions & Votes | approvals/voting | **B** |
| Actions/tasks between meetings | Between Meetings + Action List collection | task management (board & committee projects) | tasks & goals | task management | **B** |
| Governance document library | between-meetings content | archive & document management | document center | resource library w/ folder permissions | **B** |
| Meeting logistics (notices/calendar/video) | meeting scheduling in workflow | in-product video conferencing | calendar; Boardable Video | video integrations; notifications | **B** |
| Between-meeting collaboration surface | action list focus | workrooms; private/shared annotations | discussions, polls | secure messenger, annotations | **B** (shape varies) |
| Roles/terms depth (term dates, limits, expiry signals, succession view) | roles present; term depth not verified this pass | D&O questionnaires (officer records) | roles/permissions only at this evidence level | **Roles & Terms Management: term dates, term number, expiry flags, export, succession framing** | **A** — deep form documented in one product; shallow role fields common |
| Public transparency site | — | — | Public Sites (ADA-compliant hub for agendas/minutes/policies) | — | A (one product here) + §10 pass public-sector variant [B across passes] |
| Accessibility emphasis | — | — | WCAG 2.1 AA / ADA claims | director-adoption emphasis | A (one product explicit) |
| AI assistance | BoardPro AI | AI book summaries, AI minutes | AI recaps/transcription | AI suite (agenda/book/minutes/insights) | **B** — era-common |
| Security baseline (permissions, 2FA/SSO, audit) | role-based access levels | permission controls | roles/permissions, SSO, encryption claims | 2FA, security settings, audit framing | **B** |

Reading: the meeting cycle + body/roster + member-scoped materials + confirmed record is present in all four products regardless of segment — identical to the §10 finding. The **committee-as-parallel-body** is likewise universal, realized through three different mechanisms (sub-account / group / workroom). What varies by market is emphasis: collaboration between meetings, affordability, transparency, accessibility, and volunteer lifecycle support.

## Canonical Model — Four Abstraction Layers

### L0 — Defining Invariant

```text
Governed body (board or committee) with an identified member roster carrying roles
└── Meeting as the unit of governance work for that body
    ├── Agenda structuring the meeting
    ├── Meeting materials distributed to the body's members
    │   under member-scoped access
    └── Confirmed governance record (minutes, decisions, actions)
        retained as the body's official account
```

Test: remove the body/roster → generic meeting or document software; remove member-scoped distribution → shared drive; remove the confirmed record → a document portal or meeting-notes tool. Each removal destroys the Type. Note that this L0 is **identical** to the §10 Board / Corporate Governance Platform L0 — see Boundary Findings.

### L1 — Common Mature Structure

- Multi-body organization: the board plus several committees run in parallel as separate workspaces, each with independent meetings/documents/decisions; people can hold memberships in multiple bodies
- Agenda builder; pack/board-book assembly, distribution, and controlled republishing
- Minutes workflow: draft → review → confirm (often e-signed); record locked after confirmation
- Decision machinery: motions/votes (in-meeting and out-of-cycle polls), decision/action registers, action items with owners and due dates
- Governance document library (policies, past packs, past minutes)
- Meeting logistics: notices, calendar, video (embedded or integrated)
- Between-meeting collaboration: discussions, annotations, secure messaging
- Security baseline: role-based permissions, encryption, MFA/SSO, audit trails; materials kept inside the platform
- Member onboarding/training aids and a member-facing homepage/dashboard
- AI assistance over the body's own materials/history (era-common)

### L2 — Variant / Optional Structure

- Roles & terms depth: term dates, term numbers/limits, expiry signals, succession/nomination views (deep form evidenced in one product; association market makes this salient because volunteer service rotates on fixed terms set by bylaws)
- Public transparency site for publicly accountable boards (charities, schools, government-adjacent bodies), with accessibility compliance
- Board assessments/evaluations, D&O questionnaires, skills tracking, diversity reporting
- Surveys/forms; e-signatures
- Commercial shapes: per-committee licensing, per-user pricing with volunteer discounts, free trials for volunteer-run bodies
- Deployment/data-residency postures; suite membership (governance suites)

### L3 — Vendor-specific (research notes only)

- BoardPro: committees as separately licensed sub-accounts at a flat per-committee rate; six-stage meeting state machine; interests import when adding people to committees; Account Owner access model
- OnBoard: 180-day term-expiry flag window; role/class/term-number data model; named integrations (Microsoft 365, DocuSign, Zoom, Teams); OnBoard Academy training paths; marketing scale figures (excluded from evidence)
- Boardable: explicit Group-vs-Meeting FAQ semantics; new-member visibility defaults (current content visible, past discussions/tasks/polls private); public-site-as-ADA-hub framing; volunteer-discount pricing
- BoardEffect: Diligent One platform membership; AI board-book summarization; D&O questionnaire module

## Vendor-specific Findings

See L3. Additional: BoardPro's per-committee flat-rate licensing shows committees are commercial objects, not just folders — a signal of how central parallel bodies are in this market's buying model.

## Rejected Findings

- **"Committee management = an AMS roster module."** Rejected as the Type's definition. In the AMS (per the §25 pass), committees are registry-attached roster records — an optional suite extension without meeting machinery. The meeting cycle is what makes this Type.
- **"Term tracking is definitional."** Rejected. Deep term machinery is documented in only one sampled product; products whose help centers do not document term tracking are still unambiguously this Type. Term depth is L1/L2.
- **"Public transparency is definitional."** Rejected — segment variant (publicly accountable boards), not the Type.
- **"Election/nomination management is part of the Type."** Not evidenced as first-class machinery in the sample (only succession signals around term expiry in one product). Kept adjacent/uncertain.
- **"This Type is distinct in structure from the §10 board portal."** Rejected by the evidence — the four sampled products overlap the §10 market almost completely and the core model is the same. The difference is market/audience emphasis, not structure.

## Boundary Findings

1. **vs Board / Corporate Governance Platform (§10)** — probable alias / audience variant. Same software category, largely the same vendor market (OnBoard and BoardPro appear in both samples; BoardEffect is a sibling of Diligent Boards; Boardable competes with both). Core model (L0) identical. What differs is the market expression: governed population (volunteer/member boards vs corporate boards), committee-first organization, terms/rotation, affordability, transparency, accessibility. No structural "remove X → becomes another Type" discriminator exists, because the structure is the same; the discriminating axis is audience/market. **Recorded as a taxonomy issue for joint review** (consistent with the §10 pass's own flag). This leaf is documented below as the membership/volunteer-market expression of the same software.
2. **vs Association Management System (§25)** — AMS: constituent registry + membership records + dues/renewal spine; committee/board records are registry attachments. Discriminator: add the per-body meeting cycle and confirmed record → this Type; remove them, keeping only roster/term → an AMS committee module. AMS suites integrate with this Type's data (people), but the meeting machinery is out of the AMS's depth (per AMS research note).
3. **vs Chapter Management Platform (§25)** — chapters are subordinate operating units (their own members, finances, events, public identity); committees/boards are internal governance bodies (meetings, materials, records). Officer-record machinery overlaps; the operational stack does not.
4. **vs Legislative Management System / Government Meeting & Agenda Management (§24)** — those are publication-first public workflows (agendas/minutes as public records, readings, public comment); this Type is a body-internal confidential cycle. The public transparency site is the overlap zone: public-sector boards use this Type plus a public surface.
5. **vs HOA / Community Association Management (§17)** — that Type manages the community's property/owners/dues/maintenance; its governing board is a *user* of this Type. Swap the object from the community to the board's own work and you cross the boundary.
6. **vs Church Management System (§25)** — ChMS: people/contributions/groups/worship spine; church boards and committees are governance bodies whose work belongs to this Type.
7. **vs Meeting Scheduling / AI Meeting Assistant / Meeting Notes (§03)** — capability donors (scheduling, transcription → minutes); no governed bodies, rosters, member-scoped packs, or confirmed records.
8. **vs Enterprise Content Management (§10/§14)** — generic content lifecycle; here the library is bounded to governance bodies and tied to the meeting cycle and record.

## Historical / Market-Sample Check

- Would older products fit? Association and nonprofit boards have run this cycle for a century with paper board manuals, mailed board books, and a volunteer (or single staff) secretary: bodies with rosters, meetings, agenda papers, and confirmed minutes. Early board portals (including the one sampled here that was built for associations/nonprofits/healthcare from its founding years) digitized exactly this L0. ✔
- Regional/smaller bodies: ANZ school boards and trustees (sampled product's home segment), UK/EU charity trustees, church councils, club committees — all fit the L0 without any corporate-governance-specific machinery (no subsidiary boards, no D&O questionnaires). ✔
- Anti-overfitting check: member-scoped confidential distribution is definitional (it is why the software exists), but *how* confidentiality is enforced (apps, no-email rules, 2FA) is era-dependent. Committee-as-sub-account (one product) vs group workspace (another) confirms the mechanism is variant, the parallel-body structure common. ✔

## Uncertainties

- BoardEffect's operational help center is not reachable without a Diligent account; its evidence is positioning/feature-page level. No operational claims were drawn from it beyond what its product pages state.
- OnBoard's association vertical page was not fetched this pass; the association claim rests on its site navigation + product evidence.
- Election/nomination machinery prevalence in this market is unverified (only succession signals evidenced). Deliberately not asserted.
- AMS committee-module depth was not product-fetched this pass; the boundary rests on the §25 pass's research note plus structural reasoning.
- Older/regional products (e.g., school-governor hubs, club council software) were not directly sampled; the historical check is inference from the L0's minimalism.
- Whether BoardPro carries term-tracking depth was not verified this pass; no claim is made either way.

## Final Synthesis

Committee / Board Management is the membership/volunteer-market expression of board management software: the system a nonprofit, association, church, school, club, or similar member-governed organization uses to run its board and its committees. Its defining core is the §10 core, verbatim: governed bodies (board and committees) with member rosters; meetings as the unit of governance work; agenda-structured materials distributed to each body's members under member-scoped access; and a confirmed governance record — minutes, decisions, actions — retained as each body's official memory.

What this market adds in emphasis: the organization typically runs several small bodies in parallel (board + committees), realized as separate workspaces with independent data and per-body membership; members are volunteers who rotate on fixed terms, making roles/offices and (in some products) term tracking and succession views salient; collaboration between meetings (discussions, polls, tasks) carries more weight because bodies meet infrequently; and publicly accountable segments add transparency surfaces and accessibility compliance. On the evidence, the Type is a probable audience-variant/alias of Board / Corporate Governance Platform (§10) rather than a structurally distinct Type — recorded in STATUS.md Boundary Issues for joint review, while this leaf is documented as its own leaf with the association-market emphasis.
