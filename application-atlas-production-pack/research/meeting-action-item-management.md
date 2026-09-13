# Research Notes — Meeting Action-item Management

## Research Goal

Understand what a "Meeting Action-item Management" application really is, from real products: what the core object is, how action items are created/assigned/tracked/closed, how they relate to the meeting record, and where the boundary lies against Task Management, Meeting Notes, AI Meeting Assistants, and Meeting Scheduling.

## Initial Boundary

Directory placement: §03.10 Meeting Productivity, siblings: Meeting Notes Application, Meeting Recording & Transcription Application, AI Meeting Assistant.

Working hypothesis before research:

- Core object: the action item — a commitment made in a meeting, tracked to closure.
- Nearest confusions: Task Management Application (generic tasks), Meeting Notes Application (record of what was said), AI Meeting Assistant (capture layer that outputs action items), Meeting Scheduling (arranging the meeting).
- Key question: is the meeting anchoring definitional, or is this just task management with a meeting flavor?

## Research Questions

1. What exactly is an "action item" in these products — object, attributes, lifecycle?
2. How are action items created? (during note-taking, from agenda, before/after meeting, AI extraction)
3. How is ownership modeled? One owner? Multiple? Visibility of who owes whom?
4. How are items tracked and closed? Statuses, views, reminders, overdue handling?
5. How do items relate to the meeting record (minutes, agenda, decisions)? Link-back? Carry-over to follow-up meetings?
6. How do these products relate to external task managers (Jira, Asana, Outlook, Trello)? Sync vs export?
7. What roles exist (chair/organizer, minute-taker, participant/owner)?
8. Historical check: would paper minutes with an action list + follow-up review satisfy the definition?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| MeetingKing | lightweight minutes+tasks (SMB/clubs/non-profits) | dedicated action-item tracking documented in depth; older-generation product good for historical check |
| MeetingBooster | professional meeting management (enterprise, formal minutes, on-prem option) | has a dedicated "Meeting Action Items" feature page; MS-ecosystem integration pole |
| adam.ai | governance/board & committee pole (AI-era repositioning) | action accountability as a named capability inside a meeting-operations module |
| Lucid Meetings | meeting-expert vendor; conceptual source | canonical "Who/What/When" action-item definition in its glossary; software now services-led (limitation noted) |
| Fireflies.ai | boundary reference only (AI Meeting Assistant pole) | action items as AI-extracted output pushed to external task tools — clarifies the boundary |

Rejected/abandoned samples: Fellow (fellow.app and help center returned 403 on three attempts — abandoned per network rules; Fellow is known as a major modern player, so its absence is a documented limitation), Hugo (403), adam.ai docs subdomain (transport errors ×2).

## Sources

- MeetingKing — https://meetingking.com/ (root), https://meetingking.com/control-feel-good-manage-tasks-effectively/ (task management), https://meetingking.com/managing-meeting-task-and-action-items/ (action-item practice article) — fetched 2026-09-08
- MeetingBooster — https://www.meetingbooster.com/ (root), https://www.meetingbooster.com/meeting-action-items (dedicated action-items page) — fetched 2026-09-08
- adam.ai — https://adam.ai/ (root), https://adam.ai/platform/meeting-operations (Meeting Operations module) — fetched 2026-09-08
- Lucid Meetings — https://www.lucidmeetings.com/ (root; services-led), https://www.lucidmeetings.com/glossary/action-item (glossary) — fetched 2026-09-08
- Fireflies.ai — https://fireflies.ai/ (root; boundary reference) — fetched 2026-09-08

Source-access limitations: Fellow (major modern vendor in this exact space) unreachable (403 ×3); Hugo unreachable (403); adam.ai documentation subdomain unreachable (transport errors ×2 — only product pages used); Lucid Meetings' meeting software product pages not reachable this pass (site now services-led; only the glossary and root used). Assertion strength calibrated accordingly: no claims rely on Fellow/Hugo behavior; adam.ai claims limited to what its product pages state.

## Product Observations

### MeetingKing (evidence layer A)

From root page, task-management page, and action-item practice article:

- Positioning: "Automate your meeting agenda and meeting minutes"; flow = Prepare (agenda) → Meet (notes + assign tasks) → Follow-up (email minutes, track tasks).
- Problem framing: "Productive meetings result in action items. If the meeting ends without a concise task list, it could have been done with an email."
- Task creation: "simply write in your note taking area the task, and save it as a task"; assign owner (autocomplete field), due date, notes, files (photo on iPad).
- On creation, the system automatically: emails the task to the owner; adds it to the meeting minutes template; adds it to the meeting tasks summary; shows it in the organizer's dashboard and the owner's dashboard; and — for a follow-up meeting — adds it to the next meeting's agenda.
- Ownership rule (explicit): "Each task must have one main owner. A task may be completed by more than one person, but only one person can own the task."
- Record guidance: what the task is (+ expected outcome), the one responsible person, a completion date.
- Link-back: "All tasks also include a link back to the minutes" — context of the discussion/decision.
- Owner actions: comment, mark complete, attach the deliverable ("use MeetingKing as the delivery platform").
- Task overview: three columns — Ideas (no due date), To dos (green future due date, red overdue), Completed; filter by department, project, person, or combination; calendar view (drag to change due date); dashboard (upcoming meetings, your tasks for next 5 days, tasks others owe you).
- Auto-categorization of meeting tasks by department and/or project.
- Stand-alone tasks can be created from anywhere (not only in a meeting).
- Export: tasks exportable via Zapier to Asana, Trello, Todoist, Google Calendar, "hundreds" of task managers.
- Audience: businesses, schools, non-profits, towns, churches, sports clubs, Rotary/Lions — broad civic/SMB.

### MeetingBooster (evidence layer A)

From root page and dedicated /meeting-action-items page:

- Positioning: "Professional Meeting Management Software"; three-step flow: agendas → note-taking ("turn discussions into action plans") → professional minutes (publish and distribute).
- Pain framing: "What were those action items from the meeting? Who remembers what they were? Anyone know how to find them? It doesn't have to be that way."
- Action-item capabilities (dedicated page):
  - "Assign actions items before, during and after the meeting"
  - "Create projects to track cross meeting tasks"; "Follow tasks across multiple meetings"; "Manage unlimited projects"; "Create teams for specific projects"
  - "Track Status, Priority and Completion"
  - Automated reminders: "Notify people when they have a new task", "Set up action items reminders", "Send personalised reminders"
  - "Populate outstanding tasks on the meeting agenda" (carry-over)
  - Integration: "Not another task management system! Synchronize your MeetingBooster action items with popular task management tools" — Microsoft Outlook, Microsoft Planner, Jira, Slack, Trello "and more"
- Root page: "Leave the meeting with total confidence of who needs to do what, when, and how with clear Action Items. Track due dates, priority... Automate your follow up's and integrate with tasks systems such as MS Outlook."
- Meeting series: recurring meetings (board/committee) with minutes, decisions, and tasks tracked per series.
- Case study (Illzach town hall): minutes formalized during the meeting and distributed shortly after; "Attendees no longer have to wait for several days to find out about their action items."
- Deployment: cloud, on-premise, scalable SaaS; integrates with MS Teams/Outlook; meeting analytics module.

### adam.ai (evidence layer A — product pages only; docs unreachable)

From root and /platform/meeting-operations:

- 2026 positioning: "An Intelligent Governance Ecosystem" for boards, committees, executive offices, ministries (repositioned from general meeting management; meeting operations remains the operational module).
- Meeting Operations module: "Intelligent Orchestration across the Full Meeting Lifecycle — from scheduling and agenda-setting, through preparation and decision-making, to follow-through."
- Named capability: "Action Accountability — Assign owners and deadlines. Track status without chasing."
- Named capability: "Follow-through Status — Actions move from assigned to completed with visible ownership."
- Agenda control: "Build structured agendas with timings, owners, and decision points."
- Decision capture: "Record resolutions, votes, and rationales in a format built for governance."
- Committee continuity: "Carry context forward across cycles. Preserve institutional memory."
- Security: "Control access by role and committee. Maintain confidentiality and auditability."
- Board workflow: "Board members see what changed, what is pending, and what requires approval."

### Lucid Meetings (evidence layer A — glossary; software product not directly documented this pass)

From glossary entry "Action Item":

- "Action items describe a discrete task that must be accomplished, usually by a single individual. Action items have a limited scope that can typically be accomplished in one to two weeks."
- Standard format: Who / What / When —
  - Who: "ideally one person who takes responsibility for making sure the task gets done"
  - What: "a short description of the task. Descriptions that start with a verb work best"
  - When: "the expected date for completing the action item. Specific dates work best"
- Related glossary terms: Accountability; "action review meeting" (a meeting type dedicated to reviewing action progress).
- Site status: company now leads with consulting/services ("We've helped organizations... build better ways to meet"); the meeting software product was not directly reachable this pass. Glossary used as a conceptual/practice source from a meeting-expert vendor.

### Fireflies.ai (evidence layer A — boundary reference, AI Meeting Assistant pole)

From root page:

- Positioning: AI meeting assistant — "Transcribe, summarize, search, and analyze all your team conversations."
- Action items appear as an AI summary output: "Get detailed notes, action items, and customized summaries instantly after every meeting."
- Tasks: "Create tasks automatically after every meeting" in external project-management tools (Asana, Trello, etc.); users can "bookmark action items" in the transcript.
- Center of gravity is capture/transcription/search — the tracked action-item lifecycle is delegated to external task tools. This clarifies the boundary: extraction without lifecycle ownership is the AI-assistant pole, not this Type.

## Cross-product Comparison

| Dimension | MeetingKing | MeetingBooster | adam.ai | Lucid (glossary) | Fireflies (boundary) |
|---|---|---|---|---|---|
| Action item as tracked record | ✓ (task saved from notes) | ✓ (dedicated feature) | ✓ ("Action Accountability") | ✓ (defined term) | output only |
| Single accountable owner | ✓ explicit rule | ✓ ("who needs to do what") | ✓ ("assign owners") | ✓ ("usually by a single individual") | assignee in external tools |
| Due date | ✓ | ✓ ("due dates") | ✓ ("deadlines") | ✓ (When) | — |
| Status → completion tracking | ✓ (To dos/Completed, overdue red) | ✓ (Status, Priority, Completion) | ✓ ("assigned to completed") | implied (accountability) | — |
| Link back to meeting context | ✓ (link to minutes) | ✓ (minutes machinery) | ✓ (decision traceability) | ✓ (minutes practice) | transcript |
| Carry-over to next meeting agenda | ✓ (auto-added) | ✓ ("populate outstanding tasks on the meeting agenda") | ✓ ("carry context forward across cycles") | practice-level (action review) | — |
| Notifications/reminders | ✓ (email on assignment) | ✓ (automated + personalized reminders) | "track status without chasing" (implied) | — | — |
| Personal vs organizer views | ✓ (dashboards both sides) | ✓ (managers keep team on track) | ✓ (board members see pending) | — | — |
| Cross-meeting aggregation (projects/series) | ✓ (dept/project categorization) | ✓ (cross-meeting projects, meeting series) | ✓ (committee continuity) | — | — |
| External task-tool integration | ✓ (Zapier export) | ✓ (Outlook/Planner/Jira/Slack/Trello sync) | not stated on fetched pages | — | ✓ (auto-create tasks in PM tools) |
| Decisions/resolutions as sibling objects | minutes include decisions | ✓ (minutes + decisions) | ✓ (resolutions, votes, rationales) | ✓ (minutes practice) | summary bullets |
| AI extraction of action items | — | — | ✓ (AI-era platform) | — | ✓ (core mechanism) |
| Formal minutes publishing | ✓ (email minutes) | ✓ (professional minutes, distribute) | ✓ (governance format) | ✓ | — |
| Analytics | dashboard-level | ✓ (meeting analytics module) | ✓ (team dashboard) | — | ✓ (conversation intelligence) |
| Deployment | cloud SaaS | cloud / on-prem / SaaS | cloud (SOC2/ISO) | — | cloud |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **The action item as persistent tracked record** — a discrete commitment captured from a meeting (what must be done), held as an individually addressable record that survives the meeting.
2. **An accountable owner** — one person responsible for the item (the Who).
3. **Tracked status through to closure** — the item moves from open to done, and that movement is the system's operational content.
4. **Traceability to the source meeting** — the item is linked to the meeting (its minutes/notes/agenda context) where it was raised.

Jointly-held is load-bearing:
- 1+2+3 without 4 = a generic task manager (Task Management Application).
- 1+4 without 2+3 = meeting minutes with an action column (a record, not management).
- 2+3+4 without 1 = verbal commitments with a checklist (no persistent record).
- 1 alone = a to-do note.

Historical check (§24): paper minutes with an "Actions" section (Who/What/When), reviewed at the next meeting with the secretary chasing status, satisfies all four legs — the minutes are the meeting record, the action list is the tracked record, the owner is named, status is reviewed to closure. No cloud, AI, apps, or integrations in L0. Board/committee secretariat practice (resolutions → action register → follow-up review) also satisfies the core. The definition is not over-fitted to the modern AI-extraction pattern.

### L1 — Common Mature Structure

Present across the sampled products, not definitional:

- due dates with overdue visibility
- automated notifications/reminders to owners (assignment notices, follow-up reminders)
- personal "my action items" view and organizer/chair view (items I owe others / others owe me)
- automatic carry-over of outstanding items into the next meeting's agenda
- link-back from item to meeting minutes/discussion context
- aggregation views: by project, department, or meeting series; cross-meeting projects
- comments and attachments on items; deliverable attachment as completion evidence
- recap/distribution of minutes including the action list
- integration/export/sync with external task systems (Outlook, Jira, Asana, Trello, Todoist, Slack, Planner)
- calendar view of dated items

### L2 — Variant / Optional Structure

- **Capture mechanism**: manual capture during note-taking (classic pole) vs AI extraction from transcripts/summaries (current-generation pole; boundary with AI Meeting Assistant).
- **Governance elaboration**: decisions/resolutions/votes as sibling first-class objects; committee-scoped access control; auditability; institutional-memory continuity (board/committee pole).
- **Formal minutes machinery**: agenda editor, structured notecard, minutes publishing/distribution (professional-meetings pole).
- **Meeting series management**: recurring meeting containers holding items across occurrences.
- **Analytics**: completion rates, overdue counts, participation/meeting analytics.
- **Packaging**: standalone lightweight tool vs professional meeting-management suite vs governance ecosystem module.
- **Deployment**: cloud SaaS vs on-premise (enterprise/regulated).
- **Integration posture**: one-way export vs two-way sync with external task tools.

### L3 — Vendor-specific Structure

- MeetingKing: "Ideas" column for due-date-less tasks; GTD (David Allen) framing; Zapier-based export; civic/club audience positioning.
- MeetingBooster: MS Outlook/Planner ecosystem depth; MatchWare heritage; on-premise hosting; ROI calculator; formal three-step agenda→notecard→minutes workflow.
- adam.ai: governance-ecosystem repositioning (boards/committees/ministries); named modules (Meeting Operations, Governance Foundations, Executive Intelligence); decision traceability language; SOC2/ISO posture.
- Lucid Meetings: 16-types-of-meetings framework; "action review meeting" as a named meeting type; meeting-performance maturity model; services-led business model.
- Fireflies: AskFred AI, AI Skills store, MCP server, conversation-intelligence analytics (all capture-layer, outside this Type).

## Vendor-specific Findings

- MeetingKing's explicit one-owner rule ("only one person can own the task") is the sharpest written statement of the ownership convention; Lucid's glossary states the same convention ("usually by a single individual", "ideally one person"). Treated as cross-product commonality (B-layer), with MeetingKing as the most explicit source.
- MeetingBooster's "Not another task management system!" positioning is direct vendor evidence that this Type deliberately positions itself as complementary to — not a replacement for — general task managers.
- adam.ai's 2026 repositioning from meeting management to "governance ecosystem" is a positioning drift observation; the action-accountability capability persists inside the Meeting Operations module.

## Boundary Findings

- **vs Task Management Application**: the sharpest seam. Task managers hold tasks that exist independently of any meeting; this Type's records are meeting-anchored and its operating rhythm is the meeting cycle (raise → assign → review at next meeting). Removal test: strip the meeting anchoring and follow-up cadence → a task manager. MeetingBooster states the complementarity explicitly; MeetingKing exports tasks outward rather than replacing them.
- **vs To-do List Application**: personal, single-user, no accountability structure, no meeting record. Removal of owner/accountability collapses this Type to a to-do list.
- **vs Meeting Notes Application**: notes center on capturing what was said and decided; this Type centers on the tracked commitment that results. Notes apps commonly include action lists (capability slice); the dedicated Type makes the action item the system of record with its own lifecycle, views, and rules. The two interlock (items link back to minutes) but the centers of gravity differ.
- **vs Meeting Recording & Transcription Application / AI Meeting Assistant**: capture layer. Fireflies evidence: action items are AI-extracted summary output, and execution is delegated to external task tools. Extraction without lifecycle ownership = the assistant pole. This Type owns the lifecycle after capture.
- **vs Meeting Scheduling Application**: before-the-meeting logistics (finding a time) vs after-the-meeting follow-through. Adjacent phases of the same meeting lifecycle, different objects.
- **vs Project Management Application**: project-level execution planning vs meeting-commitment tracking. Cross-meeting "projects" in this Type are lightweight aggregation containers, not full project machinery (no dependency networks, baselines, resource leveling observed).
- **vs Board portal / governance platforms**: adam.ai drift zone. Board portals also track action items; the governance elaboration (board packs, e-voting, entity governance) exceeds this Type. The action-item core remains the shared spine.
- **Verdict on Type distinctness**: a dedicated market exists where the meeting-anchored tracked commitment is the object of record (MeetingKing, MeetingBooster, adam.ai; historically also Fellow/Hugo/Do/Lucid's software). The leaf is defensible as a distinct Type; suite packaging (meeting-management platforms where action items are the accountability core) is a variant, not a refutation.

## Uncertainties

- Fellow — the most prominent current vendor in this exact space — could not be reached (403 ×3). Its action-item model (known to include two-way sync with Jira/Asana and AI extraction) is NOT incorporated into any claim; the modern suite pole is under-evidenced relative to its market weight.
- Hugo unreachable; adam.ai docs unreachable (product pages only). Claims about adam.ai are limited to its marketing/product-page statements.
- Lucid Meetings' software product could not be documented directly this pass (services pivot); its glossary was used as a conceptual source only.
- Exact status vocabularies vary (MeetingKing: Ideas/To dos/Completed; MeetingBooster: status/priority/completion; adam.ai: assigned→completed). Canonical states are written conceptually (open → done) with labels noted as varying.
- Whether modern AI-era products (Fellow-class) implement two-way sync or one-way export with external task tools could not be verified this pass; both postures are documented from the reachable sample (MeetingBooster "synchronize" vs MeetingKing "export").
- Reminder cadences, retention rules, and permission models beyond adam.ai's committee-scoped access statement were not evidenced; no precise claims made.

## Final Synthesis

A Meeting Action-item Management application is the follow-through system for meetings: its object of record is the action item — a discrete commitment captured from a meeting, owned by one accountable person, dated, and tracked from open to done — with every item traceable back to the meeting where it was raised and carried forward into the next meeting's agenda until closed. The defining core is small (tracked record + owner + status-to-closure + meeting traceability); everything else — reminders, dashboards, projects, minutes machinery, AI extraction, governance elaboration, task-tool sync — is mature but non-definitional structure. The Type sits between the capture layer (notes/recordings/AI assistants) and the execution layer (task/project management), and its reason to exist is precisely that gap: commitments made in meetings otherwise evaporate.
