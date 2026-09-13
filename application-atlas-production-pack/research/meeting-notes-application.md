# Research Notes — Meeting Notes Application

Research date: 2026-09-08
Leaf: Meeting Notes Application (DIRECTORY 03.10 Meeting Productivity)
Slug: meeting-notes-application

## Research Goal

Understand what a Meeting Notes Application really is as an Application Type: what the unit of record is, how notes bind to meetings, what structure the record carries, how the before/during/after meeting workflow flows, and where the Type's boundaries sit against Note-taking Application, Meeting Recording & Transcription Application, AI Meeting Assistant, Meeting Action-item Management, Meeting Scheduling Application, and public-sector meeting machinery.

## Initial Boundary

Family context: DIRECTORY 03.10 Meeting Productivity contains four sibling leaves:

- Meeting Notes Application (this leaf)
- Meeting Recording & Transcription Application
- AI Meeting Assistant
- Meeting Action-item Management

Working hypothesis at start:

- The unit of record is the meeting note / minutes document, anchored to a specific meeting occurrence.
- The human is the author; transcription/AI products are neighboring Types.
- Nearest neighbors: Note-taking Application (general, not meeting-anchored), Meeting Recording & Transcription (audio/transcript is the record), AI Meeting Assistant (machine is the author), Meeting Action-item Management (action item is the tracked object), Meeting Scheduling Application (creates the meeting, does not record it), Government Meeting / Agenda Management (public-sector statutory machinery).

## Research Questions

1. What is the unit of record — the note document, the meeting, or the agenda?
2. How is a note bound to a meeting occurrence (calendar event, in-app meeting registry, room container)?
3. What structure does a meeting note carry (agenda, attendees, discussion, decisions, action items)? Is structure definitional or common?
4. What is the lifecycle: agenda preparation, live capture, finalization, distribution, follow-up?
5. Who uses it, and which roles matter (chair, note-taker, participant, absent manager)?
6. How do decisions and action items behave — prose, or addressable tracked elements?
7. How do distribution, sharing, and permissions work?
8. Where does transcription/AI sit — inside this Type or in a neighboring Type?
9. What distinguishes this Type from generic note-taking used during meetings?
10. Historical check: do paper minutes / handwritten notes satisfy the definition?

## Representative Products

Selected for market position + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy | Tier / context | Evidence |
|---|---|---|---|
| MeetingKing | Formal minutes + task follow-up, "agenda → notes → minutes + tasks" | SMB, associations, clubs, schools, non-profits | A (fetched) |
| MeetingBooster | Professional/formalized meeting management with governance posture (approval, redaction, archive, on-premise) | Mid-market/enterprise, city councils, boards | A (fetched) |
| Lucid Meetings | Full meeting management platform (Organization → Rooms → Meetings → records) | Mid-market/enterprise, meeting-culture programs | A (fetched) |
| Decisions | Microsoft Teams-native meeting management; agendas, minutes, decisions, votes; AI minutes; no recording bots | Enterprise (Microsoft 365 shops), governance-heavy | A (fetched) |
| Notion (AI Meeting Notes) | Platform-embedded meeting notes inside a workspace/doc tool; AI transcription + summary; calendar-linked | Broad team/enterprise (Business/Enterprise plan) | A (fetched) |

Attempted but unreachable (source-access limitation):

- Fellow (fellow.app, help.fellow.app) — HTTP 403 on both root and help center.
- Hugo (hugo.team, help.hugo.team) — HTTP 403 / transport error.
- Google "Take notes in Google Docs" support article (support.google.com) — timed out twice.

Consequence: the lightweight calendar-anchored personal notes pole (Hugo-style) is covered only indirectly (through Notion's calendar-linked notes and the general market shape). Assertions about that pole are kept weak.

## Sources

Fetched 2026-09-08 (all Layer A unless noted):

- MeetingKing — https://meetingking.com/ (home), https://meetingking.com/what-is-meetingking/, https://meetingking.com/meeting-minutes-software/
- MeetingBooster — https://www.meetingbooster.com/ (home), https://www.meetingbooster.com/meeting-minutes-software, https://www.meetingbooster.com/how-to-take-minutes
- Lucid Meetings — https://www.lucidmeetings.com/ (home), https://www.lucidmeetings.com/knowledge/how-work-is-organized-in-lucid-meetings
- Decisions — https://www.meetingdecisions.com/ (home; product/use-case structure)
- Notion — https://www.notion.com/help/ai-meeting-notes (help center article)

## Product Observations

### MeetingKing (Layer A — directly observed)

Positioning: "meeting agenda & meeting minutes software". Stated loop: Prepare (create agenda) → Meet (write notes, assign tasks) → Follow-up (email minutes, track tasks).

- Each meeting gets its own **meeting workspace** collecting all information; the application converts it into an agenda or minutes.
- Agenda created before the meeting "serves as the basis to make your notes and assign tasks".
- Automation: user takes short notes during the meeting; the application formats them into professional minutes afterward.
- Minutes are emailed to all participants directly from the application; invitees do NOT need an account; participants can update tasks and comment by replying to email notifications.
- Meeting header data (title, participants, date, time, location) can be copied from Google Calendar / Outlook / iCal meeting requests.
- Tasks: assigned while taking notes; emailed to the task owner; central task list with automatic reminders; in a meeting series, incomplete tasks from the previous meeting are automatically added to the new meeting's task summary.
- Attachments included in minutes and delivered with the emailed minutes.
- **Parking Lot**: off-topic issues captured during the meeting and moved to another meeting.
- Archive: search past discussions and decisions ("see what was decided").
- Templates: board meetings, staff meeting, management team, sales, rotary, etc.; custom templates possible.
- Audience: businesses, schools, non-profits, towns, churches, sports clubs, Rotary/Lions — "anyone who has meetings".
- Tasks exportable to external task managers (Asana, Trello, Todoist, Google Calendar) via Zapier.
- Robert's Rules of Order content present (blog/guides) — formal-meeting orientation.

### MeetingBooster (Layer A — directly observed)

Positioning: "Professional Meeting Management Software" — formalized meetings, accountability. Three-step pitch: Agendas (templates) → Note-Taking (notecard, decisions, action plans) → Professional Minutes (select style, edit/proofread, publish and distribute).

Minutes page:

- Take minutes during the meeting: capture notes and decisions instantly; assign action items; park topics for later; execute votes and record results; time tracker.
- Finalize: minutes templates; edit minutes; edit action items; **submit minutes for approval**.
- Distribute: after approval, automated email delivery with customized filters; send as PDF with supporting files embedded; publish online with a hyperlink; **redact information based on recipient permissions**.
- Archive: secure/encrypted storage; built-in search of all minutes past and present; granular access control; onboarding new members "with full appropriate permissions"; customizable storage including **100% on-premise hosting**; pitched for regulatory compliance.

Notecard page (running a meeting):

- Notes and decisions are added **to agenda topics**; drag-and-drop to rearrange or move notes to another topic.
- Conversations converted into action items; tasks grouped into projects and teams; task list viewable live during the meeting.
- **Park topics and roll unfinished business**: park a topic, move it to the next meeting; roll topics with notes from one meeting to another; tags identify topics to move.
- Voting tool with recorded results; time trackers; presenters/co-presenters defined.
- DropZone: attendees share files; note-taker associates files with topics; files embedded in minutes.
- Handwritten notes can be entered later (capture during the meeting is supported, not forced).
- Access rule: "only the meeting attendees will have access to the minutes within the software" as the basic rule; exceptions configurable (e.g., CEO sees all minutes, department head sees department meetings).
- **Meeting Series** for recurring meetings (board, committee, team): minutes, decisions, tasks tracked per series.
- Integrations: Outlook/Teams (email-calendar integration); tasks synchronize with other task systems (e.g., MS Outlook).
- Meeting analytics module. On-premise hosting option. Customers include city councils, health insurers, manufacturers — governance contexts.

### Lucid Meetings (Layer A — directly observed)

Positioning: meeting management platform + meeting-culture services. Knowledge base documents the organizational model:

- Hierarchy: **Organization → Rooms → Meetings → Meeting records**.
- Rooms contain groups of people who work together (projects, teams, departments, Board of Directors); all meetings are scheduled and held within a room; a room shows the calendar of meetings held there, invited people, and **meeting records**.
- Team members within a room can access the records of all meetings held there; guests can only access meetings they are invited to; guests do not see the organization or rooms.
- Enterprise customers can run multiple Organizations (per department/division).
- Personal Dashboard shows all your meetings for the current week across rooms; menu pages roll up **Action Items** and Meetings specific to the user.
- Account: personal profile, integrations control.
- (Homepage is services-oriented; software product documented via knowledge base. Some marketing claims on homepage — treated as positioning only.)

### Decisions (Layer A — directly observed)

Positioning: "AI Meeting Management for Microsoft Teams" — meeting management system "built for people and AI", secured inside Microsoft 365.

- Stated problem framing: "Agendas live in emails… Notes depend on whoever remembered to write them. Decisions are hard to find after the call. Action items slip without clear ownership."
- **Before**: structured agendas with time allocations, presenters, attachments; participants add input/suggest topics before the meeting.
- **During**: side panel in the live Teams meeting — timed agenda, assigned presenters, Time Tracker; logging decisions, capturing tasks and votes as they happen; "No recording bots. No external tools listening in."
- **After**: AI summaries / recaps / detailed minutes ready when leaving the call; every decision logged; every task has owner and deadline; tasks sync to Microsoft Planner with assignees and due dates.
- Record vocabulary: agendas, pre-reads, minutes, decisions, votes, approvals, reviews, actions, updates, notes flowing between steering committees, leadership teams, audit committees, all-hands, project teams through a central hub.
- Use cases: management & leadership, project & program, **board & committee ("governance-grade structure and audit trail")**, **government/public sector ("secure, compliant public-sector meetings")**, hybrid/remote.
- Security posture: runs natively inside the customer's Microsoft 365 tenant; SOC 2 Type II, ISO 27001:2022, GDPR; EU AI Act aligned.
- Install: Teams app store; works with existing Teams meetings; templates for agendas.

### Notion — AI Meeting Notes (Layer A — directly observed)

Positioning: help-center documentation of a meeting-notes surface inside the Notion workspace. "Notion AI transcribes your meeting and identifies key points and action items that you can share with your entire team."

- Creation: `/meet` slash command on any page, or from the `Upcoming events` tile / Notion Calendar event / `Meetings` sidebar tab.
- **Agenda/context leg**: "Write any agenda items or context under `Notes` before the meeting. When generating the summary, Notion AI will take these notes into consideration."
- Capture: live transcription (system audio + mic on desktop; mic-only on browser/mobile); upload an existing audio recording to transcribe and summarize after the fact.
- Output: transcript with speaker labels and citations; AI summary; identified action items; summary instructions selectable per meeting type (sales call, standup, team meeting) or custom instructions.
- Calendar anchoring: notes linked to calendar events; `Add meeting note` / `Open meeting note` / `Join and transcribe` / `View summary` actions on the event; default meetings database for storage; `Meetings` tab lists upcoming meetings and all notes you created or attended.
- Sharing: notes private to the creator by default; optional auto-share with internal calendar-event participants (workspace members); notes inherit page permissions; default database must be shared with the right people.
- Consent machinery: disclosure message (text/voice/auto-play), workspace-owner enforcement setting, recording-indicator via browser add-on; extensive legal-considerations section (consent laws, retention).
- Retention/deletion: transcript deletion, automatic transcript deletion schedules (Enterprise), local audio storage opt-in, audio retention windows.
- Plan-gated (Business/Enterprise); daily usage limit; workspace owner can disable.
- (Precise numeric/retention details are vendor-specific — recorded here, excluded from the final document.)

## Cross-product Comparison

| Dimension | MeetingKing | MeetingBooster | Lucid Meetings | Decisions | Notion AI Meeting Notes |
|---|---|---|---|---|---|
| Unit of record | Meeting workspace → minutes document | Meeting (in series) → minutes | Meeting → meeting record (in room) | Meeting → minutes/decisions record | Meeting notes page (linked to calendar event) |
| Meeting anchor | In-app meeting + copy from Google/Outlook/iCal | Scheduled meeting in MeetingBooster; series | Meeting scheduled and held in a room | Existing Teams/Outlook meeting | Calendar event (Notion Calendar/external) |
| Agenda before | Yes — agenda is basis for notes/tasks | Yes — agenda editor + templates | Yes — meetings have agendas | Yes — structured agendas, time, presenters, pre-reads | Yes — agenda/context notes before meeting |
| Live capture surface | Notes in meeting workspace | Notecard (notes/decisions on agenda topics) | Meeting record during meeting | Teams side panel during meeting | Transcription + notes block |
| Decisions as elements | Yes (searchable decisions) | Yes (decisions captured, votes recorded) | Yes (in record) | Yes (decision log) | Yes (AI-identified, human-editable) |
| Action items | Tasks with owner, emailed, reminders, series carry-over | Action items with owner/due/priority, projects, sync to Outlook | Action items rolled up per user | Tasks with owner + deadline, sync to Planner | AI-identified action items in notes |
| Unfinished-business roll-over | Incomplete tasks auto-added to next meeting in series | Park topics, roll to next meeting | — (rooms persist) | — (not observed) | — (not observed) |
| Distribution | Email minutes to participants; no account needed | Email PDF after approval; publish link; redaction by permission | Room members access records; guests per meeting | In-tenant (M365); recaps/minutes to team | Private by default; optional auto-share with participants |
| Archive/search | Search past discussions/decisions | Encrypted archive, search all minutes | Room meeting records | Searchable decision record | Meetings list view, default database, workspace search |
| Templates | Board/staff/sales/rotary + custom | Agenda + minutes templates, styles | Meeting templates/agenda library | Agenda templates | Summary instructions per meeting type |
| Formal machinery | Robert's Rules content | Votes/motions, approval workflow, redaction | Board rooms | Votes, approvals, audit trail | Consent machinery (recording) |
| AI | None observed | None observed | None observed | AI minutes/recaps | AI transcription + summary (core of the feature) |
| Deployment | SaaS web | SaaS or on-premise | SaaS | Microsoft 365 tenant-native | Notion workspace (SaaS) |
| Tier | SMB/clubs/non-profits | Mid-market/enterprise/government | Mid-market/enterprise | Enterprise (M365) | Team → enterprise |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures:

1. **The meeting occurrence as the anchoring context of record.** The note is bound to a specific, identified meeting — a dated gathering with participants and purpose. The meeting, not a topic, project, or person, is what the record hangs from. (Remove → generic note-taking / document editor.)
2. **The meeting note as the persistent, human-authored record of the meeting.** A document capturing what happened — discussion, decisions — authored/edited by a person in the application and retained as the meeting's record, retrievable later. (Remove → calendar/scheduling tool with no record; or an archive with no authoring surface.)
3. **Meeting-anatomy capture.** The application structures the record around the meeting's own anatomy: what was planned (agenda/topics) and what was decided/assigned (decisions and action items as addressable elements of the record, not buried prose). (Remove → freeform document editor that merely holds a page titled "meeting".)

Jointly-held is load-bearing:

- 1+2 without 3 = a note/document tool used for meetings (the meeting is just a title).
- 2+3 without 1 = a minutes template in a word processor (anatomy without meeting anchoring).
- 1+3 without 2 = an agenda/scheduling surface with no record of what happened.

### L1 — Common Mature Structure

Observed across the sample (Layer B):

- Agenda preparation as the first phase (agenda builder, templates, time allocations, presenters, pre-reads/attachments; collaborative input before the meeting).
- Action items as tracked elements: owner, due date, reminders; carry-over of incomplete items into the next meeting of a series.
- Distribution to participants: emailed minutes (often PDF), participants without accounts can receive/comment; publish-as-link.
- Meeting series / recurring meetings as containers linking consecutive meetings and their records.
- Archive with search over past notes and decisions.
- Templates per meeting type (board, staff, sales, 1:1, standup…).
- Parking lot / roll-over of unfinished topics.
- Calendar integration (import title/participants/date from Outlook/Google/iCal; or notes linked to calendar events).
- Sharing/permissions scoped to participation (attendees see the record; guests per meeting; redaction in the formal pole).
- Approval workflow before distribution (formal pole).
- Comments/collaboration on the record.

### L2 — Variant / Optional Structure

- AI transcription + summary as the capture engine (drift toward AI Meeting Assistant / Recording & Transcription; present in 2/5 sampled products as of 2026).
- Recording-consent machinery (disclosure messages, indicators, retention controls) — required where transcription exists.
- Voting/motions recording, Robert's Rules orientation (formal/governance pole).
- Meeting analytics.
- On-premise deployment (governance/regulatory posture).
- Platform-embedded vs standalone (Teams-native; workspace/doc-tool-native).
- Export of action items to external task managers.
- Multi-language, multi-organization hierarchies (enterprise).

### L3 — Vendor-specific (Research Notes only)

- MeetingKing: Parking Lot concept; Zapier task export; "invitees need no account" email-reply task updates.
- MeetingBooster: Notecard and DropZone as named surfaces; redaction based on recipient permissions; 100% on-premise option; MatchWare lineage.
- Lucid Meetings: Organization/Room hierarchy; "16 types of business meetings" methodology; Meeting School.
- Decisions: Planner sync; "no recording bots" posture; EU AI Act alignment claim; Teams app-store install.
- Notion: `/meet` slash command; sub-processor list; 10h/day usage limit; local audio storage of last 10 recordings; automatic transcript deletion schedules; plan gating.

## Historical / Market-Sample Check

Ask: would older, regional, platform-native products still fit the L0?

- **Paper minutes book / handwritten notes**: meeting occurrence (date, attendees, purpose), persistent human-authored record, standard anatomy (agenda items, decisions, action items with owners). Satisfies all three L0 legs with no software. Passed.
- **Platform-native thin pole** (a notes document attached to a calendar event, e.g. the "meeting notes" pattern in calendar/doc suites): meeting anchor + human-authored note; anatomy present only as a template skeleton. Satisfies legs 1–2; leg 3 holds weakly (template-level anatomy). This is the thin edge of the Type — a document editor doing meeting notes. Recorded as boundary-leaning, not a counter-example to the L0.
- **Formal governance minutes** (board, council, public-sector): same core, plus formal machinery (motions, votes, approval, redaction, statutory retention). Fits; the machinery is L1/L2, not core.
- **AI-era products**: transcription/summary products keep the human-editable note as the record and the meeting as the anchor — they fit, with the AI as capture assistance. When the machine-generated transcript/summary *replaces* the human-authored record as the primary object, the product is drifting to Meeting Recording & Transcription / AI Meeting Assistant.

Conclusion: the L0 survives the historical check; no era-, region-, or vendor-specific pattern (email distribution, PDF, calendar sync, AI) is inside the core.

## Vendor-specific Findings

See L3 above. None promoted to the canonical model.

## Boundary Findings

| Neighboring Type | Relationship | Distinction — what makes it NOT this Type |
|---|---|---|
| Note-taking Application | closest general neighbor | notes are personal/general-purpose; no meeting occurrence as anchor, no participant context, no meeting anatomy. Remove the meeting anchor from this Type → note-taking. |
| Meeting Recording & Transcription Application | sibling (03.10) | the audio recording/transcript is the primary record; here the human-authored note is the record. Products drift when transcription becomes the core object. |
| AI Meeting Assistant | sibling (03.10) | the machine is the primary capture/summary agent acting for the user; here the human is the author and AI at most assists. |
| Meeting Action-item Management | sibling (03.10) | the action item is the tracked object of record with its own lifecycle; here action items are elements inside the meeting record. |
| Meeting Scheduling Application | adjacent (03.09) | creates and coordinates the meeting (time, invites, rooms); does not produce the record. |
| Collaborative Document Editor | adjacent (03.01) | general document authoring; no meeting anchoring or anatomy. |
| Government Meeting / Agenda Management | adjacent (24) | public-sector statutory machinery: public agendas, legislative bodies, public records law; meeting notes here serve internal/organizational record-keeping. |
| Committee / Board Management | adjacent (25) | governance containers (member rosters, packets, resolutions) for board/committee bodies; meeting notes may document their meetings but governance is the core there. |
| Virtual Meeting Platform / Conference Calling | adjacent (01.04) | hosts the live meeting itself (audio/video); may integrate notes but the live session is the object. |

"Remove what, and it becomes the other Type" tests:

- Remove the meeting anchor → Note-taking Application / Document Editor.
- Remove the human-authored record (keep only scheduling) → Meeting Scheduling Application.
- Replace the human-authored note with machine transcript as the record → Meeting Recording & Transcription Application.
- Promote action items from note elements to the tracked object → Meeting Action-item Management.
- Promote the AI from assistant to primary author/capture agent → AI Meeting Assistant.

## Uncertainties

- Lightweight calendar-anchored personal-notes pole (Hugo-style) could not be fetched; its exact sharing/anchoring defaults are unverified. Assertions about that pole kept weak; the pole is covered indirectly via Notion's calendar-linked notes.
- Google's "meeting notes" doc pattern could not be fetched; described only as a thin-pole shape, without product-specific claims.
- Whether agenda support is strictly definitional could not be proven by counter-sample (no sampled product lacks it); kept inside L0 as "meeting anatomy" phrased broadly (planned topics + outcomes), which the thin pole also satisfies at template level.
- Lucid Meetings' current product depth (post-pivot toward services) is documented only via its knowledge base; feature-level claims kept minimal.
- Market drift: AI transcription is entering this Type from the AI Meeting Assistant side (2/5 sampled products). The boundary is drawn on the object of record (human-authored note vs machine transcript), but products increasingly span both; flagged for future re-check.

## Final Synthesis

A Meeting Notes Application is the meeting's documentation system of record: it anchors a persistent, human-authored note to a specific identified meeting occurrence, structures the capture around the meeting's anatomy (planned topics; decisions and action items as addressable outcomes), and works that record across the meeting's lifecycle — prepare the agenda, capture during the meeting, finalize and distribute to participants, retain and search the archive, and carry unfinished business into the next meeting. Everything else — templates, series, approval, redaction, analytics, AI transcription, platform embedding — is common mature or variant structure, not the definition.
