# Research Notes — Government Meeting / Agenda Management

## Research Goal

Understand the clerk-run public meeting cycle software market: what the application actually is, what objects it manages, how the agenda-to-record loop works, and where it borders the board-portal family (§10 Board / Corporate Governance Platform, already processed with a pending joint-review flag against this leaf) and the legislative/chamber family (§24 sibling Legislative Management System).

## Initial Boundary

Working hypothesis before research:

- This is the local-government "agenda management" / "meeting management" category: the clerk's system for building council/board agendas, publishing public notice, running the meeting, and producing minutes.
- Nearest neighbors: Board / Corporate Governance Platform (confidential board pack vs public legislative workflow — prior pass flagged real overlap via Diligent Community), Legislative Management System (chamber/bill workflow vs local meeting cycle), Event Agenda Management (conference programs vs official government business), Meeting Scheduling Application (time-finding vs the whole cycle).
- Unknowns: whether the public-transparency axis is definitional or just common; how deep the legislative-item lifecycle goes in typical products; whether in-meeting conduct tooling (voting, speaker management) is core or variant.

## Research Questions

1. What is the core object — the meeting, the agenda, or the legislative item?
2. How do agenda items enter the system (intake), and how are they routed/approved?
3. What does "publishing the agenda" mean operationally (public notice, portal, deadlines)?
4. What happens in-meeting (roll call, votes, speakers, video) and what is captured?
5. How is the official record produced (minutes), approved, and retained/published?
6. Who are the users (clerk vs officials vs public) and how asymmetric are the surfaces?
7. Where is the boundary vs board portals (confidential pack) and vs legislative/chamber systems?
8. What regional/institutional variants exist (council vs school board vs commission; US vs non-US)?

## Representative Products

Selected for market coverage + different product philosophies + different customer levels:

1. **Granicus — Agenda LE (Legistar Agenda Management)** — the market-leading lineage for large US local government; deepest legislative-process framing ("digital legislative management").
2. **Granicus — Agenda OE (OneMeeting Agenda Management)** — same vendor's cloud product for medium-to-large organizations; shows the modern SaaS form of the same workflow.
3. **Diligent — Diligent Community** — board-portal lineage (Diligent Boards / BoardEffect family) re-purposed for public-sector boards: school boards, municipal councils, special districts; the between-Types specimen flagged by the board-portal pass.
4. **OpenMeeting (Open Meeting Technologies)** — independent specialist centered on in-room meeting conduct (electronic roll call/voting, request-to-speak, displays) wrapped around an agenda/minutes portal; county/city/school-board customer base.

Rejected/unreachable samples (recorded per source-access rules):
- CivicClerk (CivicPlus) — civicplus.com and civicclerk.com returned 403; help.civicplus.com transport error. Abandoned after 3 failures.
- Municode Meetings — municode.com/meetings 403.
- eScribe (Canada) — escribesoftware.com 522 ×2 (regional pole under-sampled).
- NovusAGENDA (Hyland) — timeout.
- PrimeGov — now redirects to Granicus (acquired); treated as market consolidation evidence, not a separate sample.

## Sources

All fetched 2026-09-07:

- Granicus — Agenda & meeting management (solution page): https://granicus.com/solution/agenda-meeting-management/
- Granicus — Agenda LE (Legistar Agenda Management) product page: https://granicus.com/product/agenda-management-legistar/
- Granicus — Agenda OE (OneMeeting Agenda Management) product page: https://granicus.com/product/agenda-management-onemeeting/
- Granicus — corporate homepage (product directory, market stats): https://www.granicus.com/
- Diligent — Diligent Community product page: https://www.diligent.com/products/community/
- OpenMeeting — homepage: https://openmeeting.us/ (serves openmeetingtech.com content)
- OpenMeeting — Agenda Management & Automatic Minutes feature page: https://openmeetingtech.com/agenda-management-automatic-minutes/

**Source-access limitation (load-bearing for assertion calibration):** no help-center / user-guide level operational documentation was reachable for ANY sampled product in this pass. All evidence is from official product/solution pages (positioning + feature level). Therefore: workflow mechanics are described at capability level, never step level; no numeric limits, notice deadlines, retention periods, or state-machine labels are asserted; vendor marketing statistics (75% time reduction, 60% engagement increase, 250% engagement, 123K meetings streamed, 14,000 organizations) were collected but excluded from evidence.

## Product Observations

### Granicus — Agenda & meeting management (solution page) [Evidence layer A]

- Positioning: "Simplify the public meeting process — internally and externally — to emphasize efficiency, promote transparency, and reduce the burden on staff."
- "Meeting solutions designed by clerks for clerks"; "serving clerks since 1999" (category age anchor).
- Outcomes quoted from clerks: agenda-publishing day as the stress peak; council members accessing materials on iPads; "Give the public digital access to meeting agendas, live and video-on-demand streaming, video recording, and minutes in a central, searchable portal."
- Features: "fully automating agenda creation, approvals, and meeting minutes management"; "clerks, council members, and administrators can access meeting materials from anywhere on mobile devices to view and edit agenda items in real time"; "ADA-compliant templates and video closed captioning… translation, and transcription services."
- Add-on continuum: "indexed meeting minutes and video recordings, boards and commissions management, virtual public comments, email agenda distribution, public records request management."
- Product family under one solution: Agenda PE (Peak), Agenda OE (OneMeeting), Agenda LE (Legistar), Video (Swagit partially/fully-managed; self-managed), Boards and Commissions.

### Granicus — Agenda OE (OneMeeting) [Evidence layer A]

- "From prep to publish… for medium to large-sized government organizations"; "comprehensive, modern, and cloud-based."
- "Ensure regulatory compliance with ADA-friendly meeting materials and adherence to open meeting laws."
- "Custom forms for agenda item submission — generate professional and polished agendas and minutes documents… create unique forms for each document type such as resolutions, contracts, ordinances, and more."
- "Route items through a fully configurable automated approval process that notifies assigned users when items are ready for review. Office 365 integration enables staff to edit system-generated agenda docs in Word, and multi-user editing allows everyone to see changes in real time."
- "Split workflows, dynamic routing, and missed deadline alerts ensure complete meeting packets without the last-minute scramble. Finish the process with a few simple clicks to post agendas to a public web portal."
- "OneMeeting's in-meeting features simplify roll call, minute taking, voting, and public comments and requests to speak."
- "Timestamped videos sync to each agenda item for easy search-and-locate. Closed captioning and transcription services…"
- "Capture roll calls, minutes, votes, and actions efficiently during the meeting. Manage speaker lists, facilitate public comments, and automatically time speakers."
- "Generate and publish ADA-friendly agendas and minutes to a searchable public web portal in just a few clicks. Enable social media sharing."

### Granicus — Agenda LE (Legistar) [Evidence layer A]

- "The original end-to-end agenda and meeting management solution designed specifically for government… ideal for large government organizations."
- Framing: "digital legislative management solutions… streamline cross-departmental workflows, modernize the public meeting experience."
- Same core functionality set as OneMeeting (item forms for resolutions/contracts/ordinances; approval routing with Word integration; in-meeting roll call/minutes/votes/speakers; public portal publishing; ADA templates).
- Distinctive: "Legislate — the online agenda review and notation tool for elected officials"; "Unlimited users and data storage"; "granular permission levels enable users to limit access to confidential or sensitive information"; integrations with Laserfiche and (announced) DocuSign.

### Diligent — Diligent Community [Evidence layer A]

- "Governance software for public sector boards… Empower your public and elected boards to lead with clarity, transparency and efficiency. Run effective meetings, simplify agenda preparation, collaborate seamlessly on policies, and keep your community informed – all from one secure platform."
- Audience (FAQ): "purpose-built for public sector organizations, including school boards, municipal councils, and special districts."
- Pillars: efficiency ("Seamlessly build agendas, distribute meeting materials, capture votes and actions and create meeting minutes"); protection ("sensitive documents and materials are protected through… customizable user permissions"); transparency ("Keep board members and the public informed with easy access to agendas, policies and supporting documents through an accessible, ADA-compliant public transparency site"); trust ("a single source of truth for the public, staff and board or council members").
- Named tools: "Agenda & meeting management — Automate workflows for agenda creation, approvals, and publishing"; "Livestream manager — Broadcast public meetings directly to your website"; "AI-supported minutes — Generate… meeting minutes with closed captions from livestreamed meetings"; "Committee manager — Oversee boards and committees from one platform"; "Digital voting — Capture, record, and automatically calculate votes"; "Customizable document library"; "Goal tracking — …share progress on board goals publicly"; "Streamlined policy lifecycle management."
- Lineage note: same vendor family as Diligent Boards/BoardEffect (board portals); Community is the public-sector expression — the specimen sitting between the two Types.

### OpenMeeting [Evidence layer A]

- "Modern Legislative Meetings… Boards | Councils | School Boards | Government Associations."
- Three-phase structure: Before the Meeting (Agenda Management: "Reusable Templates, Streamlined Approvals, Intuitive Workflows") → During the Meeting (Meeting Management: "Gov-Grade Streaming, Electronic Roll Call & Voting, Request-to-Speak, Real-time Meeting Display") → After the Meeting (Automatic Minutes: "Automatic Meeting Minutes, Easy Review & Customization, Quick Publishing").
- Agenda Builder: "templates, drag-and-drop functionality, file attachments… All work is automatically saved… formatted and branded automatically."
- Agenda Templates: "cover pages, headers, footers, individual agenda items, or entire agendas."
- Document Creator: "exportable agenda and packet documents and an interactive agenda… customize what's included… cover pages, disclaimers, file attachments."
- Approval tools: "give certain members of your organization special permission to approve documents… request their approval through our Portal."
- Publishing: "publish your documents directly through our Portal with a few simple clicks, creating a shareable URL that you can copy and paste on your website."
- Automatic Minutes: "captures data (roll call, requests to speak, voting, etc.) as the meeting progresses. The data is then formatted automatically into minutes after the meeting ends"; edited in the Portal; Minutes Builder customizes "attachments, vote totals, and timestamps."
- Conduct machinery: Request-to-Speak with automatic speaker queue; Public Comment Sign-Up; Voting Display showing real-time results to the room/public; member mobile apps.
- Customer testimonials are overwhelmingly from clerks (County Clerk, City Clerk, Commission Clerk, district IT) — role evidence.

## Cross-product Comparison

| Dimension | Granicus LE/OE | Diligent Community | OpenMeeting |
|---|---|---|---|
| Primary operator | clerk | clerk / board secretary | clerk |
| Bodies served | councils, commissions, committees (many bodies per jurisdiction) | school boards, municipal councils, special districts, committees | boards, councils, school boards, associations |
| Item intake | custom forms per document type (resolutions, contracts, ordinances) | agenda builder + workflows (intake depth not detailed) | templates + drag-and-drop + attachments |
| Approval routing | configurable automated approval process, split workflows, deadline alerts | "workflows for agenda creation, approvals, and publishing" | approval requests through portal, special approver permission |
| Authoring substrate | Office 365 / Word integration, multi-user editing | not detailed | portal-native builder, branded templates |
| Public notice | post agenda to public web portal | ADA-compliant public transparency site | publish → shareable URL for the website |
| Meeting conduct | roll call, votes, speaker lists, timers, public comment | digital voting, livestream manager | electronic roll call & voting, request-to-speak queue, voting display, streaming |
| Record | minutes + votes + actions; timestamped video synced to agenda items | AI-supported minutes with closed captions from livestream | automatic minutes formatted from captured meeting data |
| Confidential handling | granular permissions for confidential/sensitive items | sensitive-document protection + permissions | not detailed |
| Distinctive extras | Legislate review tool; boards & commissions add-on; video product family | policy lifecycle, goal tracking (public), committee manager | in-room conduct hardware/display, member apps |

Stable across all sampled products (cross-product commonality, layer B):
- clerk as primary operator; officials as reviewing members; the public as the third audience
- agenda assembled from items with attachments, through an approval step, before publication
- publication of agenda (notice) and minutes (record) to a public-facing surface
- in-meeting capture of attendance/votes/speeches feeding the minutes
- video streaming increasingly indexed to agenda items
- accessibility (ADA) treated as a first-class requirement
- multi-body support (council + commissions + committees)

## Canonical Abstraction

### L0 — Defining Invariant (four jointly-held properties)

1. **Public governing body as container** — an identified public body (council, board, commission, committee) with a roster of elected/appointed officials, meeting on a recurring formal schedule. Remove → generic meeting/event tool.
2. **Agenda as assembled official instrument** — business items (with attachments) are submitted into the system, routed through approval, and compiled into the body's official agenda, which structures the meeting and constitutes the public notice of business. Remove → scheduling/calendar or document tool.
3. **Conducted meeting with captured outcomes** — the meeting is run from the agenda; attendance (roll call), motions, votes, actions, and public participation are captured as structured data. Remove → document publisher.
4. **Approved public record** — minutes are drafted from the meeting's captured data, approved (in practice at a subsequent meeting), retained as the body's official record, and published for public access. Remove → webcasting/streaming tool.

The public axis is distributed across properties 2 (notice) and 4 (public record) and is what separates this Type from the board portal: here the default posture is publication and restricted access is the exception (closed sessions, confidential items); in board portals the default is confidentiality and publication is the add-on.

### L1 — Common Mature Structure

- searchable public transparency portal (agendas, packets, minutes, video archive)
- agenda approval workflows with deadline alerts; templates and cloning; Word/Office integration
- video: live streaming + on-demand, timestamped/indexed to agenda items, captions/transcripts
- public participation machinery: speaker sign-up/queues, timers, virtual public comment
- roll call + per-member vote recording; digital voting
- official/member review surfaces (agenda review, annotation, mobile access)
- notifications/subscriptions (email agenda distribution)
- accessibility compliance tooling (templates, captions)
- multi-body support under one deployment
- AI assistance (minutes generation, captions/summaries)

### L2 — Variant / Optional Structure

- legislative-item lifecycle depth: persistent file-numbered items, ordinance/resolution types with readings, codification handoff — depth varies with jurisdiction type (deep in large-city Legistar deployments; lighter in board-portal lineage)
- boards & commissions management (rosters, terms, applications, vacancies)
- closed-session / confidential-item handling with restricted permissions
- in-room conduct hardware (electronic voting pads, chamber displays, request-to-speak microphones)
- policy lifecycle management, public goal tracking (board-portal lineage extras)
- hybrid/remote meeting support
- regional/institutional forms (council-manager, commission, school board, parish/police jury, non-US councils — non-US under-sampled in this pass)
- packaging: government-experience-suite module vs standalone vs board-portal lineage vs conduct-technology specialist

### L3 — Vendor-specific (research notes only)

- Legistar's "Legislate" elected-official review tool; Granicus's three-product agenda line (LE/OE/PE) and Swagit managed-video services; Laserfiche/DocuSign integration claims.
- Diligent Community's Goal tracking, Policy lifecycle management, Committee manager naming; Diligent One platform context.
- OpenMeeting's Voting Display, member mobile apps, SOC 2 compliance claim.
- Marketing statistics (Granicus 75%/60%/250%/123K; Diligent 14,000+ organizations) — excluded from evidence.

### Historical / market-sample check

The paper-era clerk practice — typed agenda, posted public notice, packet distributed to members, minutes recorded and approved at the next meeting, records retained for public inspection — satisfies all four L0 properties with no portal, streaming, or workflow engine. The digital portal is the modern standard implementation of the notice/record properties, not the invariant. Legistar-lineage products date to the 1990s and Granicus states it has served clerks since 1999; the category is a digitization of a much older civic practice. Check passes; the definition is not over-fitted to the modern portal-and-streaming implementation.

## Vendor-specific Findings

See L3 above. Additionally: Granicus brands the whole category "legislative management" (vocabulary collision with the §24 Legislative Management System leaf — see Boundary Findings). Diligent Community inherits board-portal concepts (pack distribution, member-scoped access) into the public sector. OpenMeeting is the only sampled product that leads with in-room conduct technology (displays, electronic voting) rather than document workflow.

## Boundary Findings

1. **vs Board / Corporate Governance Platform (§10, processed)** — DISCHARGES the prior pass's joint-review flag from this side. The boundary holds on the public axis: board platforms administer a governed body's confidential meeting cycle (member-scoped pack, corporate record; publication is the public-sector variant add-on); this Type administers the public legislative/clerk workflow (agenda as public notice, record as public record; confidentiality is the closed-session exception). Diligent Community is confirmed as the between-Types specimen: board-portal lineage (pack distribution, member-scoped access, policy library) sold to school boards/councils with an ADA-compliant public transparency site. Removal tests: strip the public notice/record axis → board portal; strip the confidential member-scoped pack → agenda management. Keep both Types; the public-sector board variant should be cross-referenced by both documents.
2. **vs Legislative Management System (§24 sibling, unprocessed)** — vocabulary collision: the market leader brands its agenda products "digital legislative management," and OpenMeeting says "modern legislative meetings" for county boards. Working seam: this Type centers the recurring public meeting cycle of local/regional governing bodies (agenda → notice → meeting → minutes → public record); Legislative Management System should center the chamber/bill process (bill drafting, calendars of business, journals, readings at institutional scale). The two likely form a spectrum; joint review recommended when that leaf is processed.
3. **vs Event Agenda Management (§26, processed)** — different object and stakes: event programs manage sessions/speakers for an occasion; here the agenda is an official instrument of a standing public body with notice obligations and an approved record. No overlap risk.
4. **vs Meeting Scheduling Application (§03.09)** — time-finding vs the whole public meeting cycle; scheduling is a minor logistics capability here.
5. **vs Petition / Public Comment Platform (§24 sibling, unprocessed)** — citizen-initiated input vs clerk-run meeting cycle; virtual public comment is a capability inside this Type, not the center.
6. **vs Government Transparency Portal (§24 sibling, unprocessed)** — the transparency portal is a publishing destination; this Type is the producing system of record that feeds it.
7. **vs AI Meeting Assistant / Meeting Recording & Transcription (§03.10)** — capability donor (minutes-from-captured-data); no official-record status, no agenda assembly, no notice obligations.
8. **vs Government Records Management (§24 sibling)** — agendas/minutes/video are public records that this Type produces and retains; enterprise records management is the broader retention discipline.

## Uncertainties

- No operational (help-center) documentation reachable for any sampled product; all workflow mechanics are capability-level. Exact approval chains, notice-deadline handling, minutes-approval states, and retention rules are NOT asserted.
- Mid-market (CivicClerk, Municode Meetings) and non-US (eScribe) poles unreachable — regional variance under-sampled; US open-meetings context dominates the evidence.
- Codification handoff (adopted ordinances flowing to the code of ordinances) is inferred from ordinance document types + market structure (Municode's codification position); not directly evidenced as an integration in the sampled products — kept weak.
- Closed-session mechanics beyond "granular permissions limit access to confidential information" not directly evidenced.
- Whether every product supports public comment intake digitally (vs in-person only) — virtual public comment evidenced as a Granicus add-on and OpenMeeting sign-up; treated as common-not-universal.

## Final Synthesis

Government Meeting / Agenda Management is the clerk-side system of record for the public meeting cycle of government's legislative and governing bodies. Its defining core is four jointly-held properties: the public governing body as container; the agenda assembled from approval-routed business items as the official instrument and public notice; the conducted meeting whose attendance, motions, votes, actions and public participation are captured; and the minutes that, once approved, become the retained, publicly accessible official record. Everything else — transparency portals, video indexing, eComment, workflow engines, AI minutes, in-room voting hardware — is standard or variant capability layered on that civic loop. The Type's identity is anchored by the public axis (notice + record) that separates it from the confidential board-portal family, and by the meeting-cycle center that separates it from chamber-scale legislative systems.
