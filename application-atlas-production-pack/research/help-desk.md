# Research Notes — Help Desk

## Research Goal

Understand what a Help Desk application actually is as an Application Type: what objects exist inside it (ticket, requester, agent, queue), how requests flow from intake to resolution, what rules govern the work (assignment, SLA, lifecycle), and where the Type ends relative to Ticketing System, Customer Service Platform, ITSM, chat tools, and self-service portals.

## Initial Boundary (hypothesis before research)

- What: team-facing support application; requests for help become tracked tickets in a shared agent queue; agents correspond with requesters and drive tickets to resolution.
- Who: support agents (primary operators), support leads/managers, admins; requesters are customers (external) or employees (internal).
- Nearest neighbors suspected: Ticketing System (directory sibling — possible severe overlap), Customer Service Platform (broader suite), ITSM / service desk (internal pole), Customer Support Chat (channel tool), Self-service Support Portal (requester-facing surface), Issue Tracker (engineering work items).
- Unknowns: exact lifecycle states and their rigidity; whether "queue" is definitional or merely common; how conversation-first products differ structurally from ticket-first products; how deep the IT-flavored variant goes before it becomes ITSM.

## Research Questions

1. What is the core object (ticket / conversation / request) and what does it hold?
2. How do requests arrive (which channels, and how do they become tickets)?
3. How are tickets organized and assigned (queues, views, groups, routing, SLA)?
4. What does the agent actually do on a ticket (correspondence, macros, internal notes, collaboration, escalation)?
5. What lifecycle do tickets move through, and what rules bind state changes?
6. What does the requester see (portal, email updates, their own request list, satisfaction ratings)?
7. What role does the knowledge base play, and how does self-service relate to the desk?
8. What automation and AI assistance is standard?
9. What reporting exists?
10. Where does the Type end vs Ticketing System / Customer Service Platform / ITSM / chat / portals?

## Representative Products

Selected for market representativeness, document accessibility, differing product philosophy, and differing customer tier:

| Product | Why sampled | Evidence quality |
|---|---|---|
| Zendesk | Market-defining customer-service incumbent; ticket-centric agent workspace | Tier-1 help-center article fetched + Tier-2 product page |
| Freshdesk (Freshworks) | SMB→mid-market volume leader; same vendor ships a separate internal-IT product (useful boundary evidence) | Tier-1 help-center structure + Tier-2 product page |
| Zoho Desk | Mid-market multi-channel desk; distinct "orchestration" framing | Tier-2 product page + resources hub |
| Help Scout | Conversation-first / shared-inbox philosophy; deliberately different vocabulary from ticket-centric products | Tier-2 product page only (docs unreachable) |
| Jira Service Management (Atlassian) | Internal / IT-service-desk pole; grew out of "service desk" and shows the ITSM-flavored variant | Tier-1 documentation hub fetched (structure; individual articles not fetched) |

## Sources

Research date: 2026-09-07.

- Zendesk — "About Zendesk channels", https://support.zendesk.com/hc/en-us/articles/4408824097050-About-Zendesk-channels (Tier 1, fetched in full)
- Zendesk — Ticketing system product page, https://www.zendesk.com/service/ticketing-system/ (Tier 2)
- Freshdesk — Support home / knowledge-base category map, https://support.freshdesk.com/en/support/home (Tier 1 structure)
- Freshdesk — Ticketing product page, https://www.freshworks.com/freshdesk/ticketing/ (Tier 2)
- Zoho Desk — product page, https://www.zoho.com/desk/ (Tier 2); resources hub, https://www.zoho.com/desk/help/ (Tier 2)
- Jira Service Management — Cloud documentation hub, https://support.atlassian.com/jira-service-management-cloud/resources/ (Tier 1 TOC, fetched; articles not opened individually)
- Help Scout — help desk software page, https://www.helpscout.com/help-desk-software/ (Tier 2)

### Source-access Limitations

- Zendesk help-center root and several guessed article URLs returned empty/404 (JS-rendered docs site); one full Tier-1 article (channels) was fetched successfully via a link discovered on the product page.
- Help Scout support docs (support.helpscout.com / docs.helpscout.com) — transport errors ×2, abandoned per network-retry rule; Help Scout evidence is Tier-2 only.
- Zoho Desk knowledge base (help.zoho.com portal) — empty responses ×2, abandoned; Zoho evidence is Tier-2 only.
- Jira Service Management individual documentation articles were not fetched; the documentation hub TOC is itself strong structural evidence, but per-article details (exact SLA mechanics, exact states) are not asserted.
- Consequence: no precise numeric claims (SLA defaults, time windows, plan limits, state-name sets) are made in the final document; operational details stay qualitative.

## Product Observations

### Zendesk

Evidence layer: A (Tier-1 article + Tier-2 page).

- Channels article (Tier 1): "Regardless of the channel by which new support requests are submitted, all requests become tickets that agents manage in Zendesk."
- Channels enumerated: email (support address; email becomes tickets; unlimited address variations; forwarding from external addresses; templated outgoing mail; automatic replies per workflow stage), help center (KB + web form; tickets can be created from article/community comments), web & mobile messaging (asynchronous, multi-session, full history retained; bot suggests KB articles), social messaging (messages become tickets; agent replies appear in the user's messaging app), voice (call queuing, greetings, recorded calls added to tickets, voicemail → ticket with recording + transcription), text/SMS (inbound text creates ticket), live chat (chat sessions become tickets; agents can update after session; visitor monitoring; agent-to-agent chat), Web Widget (embed KB search + chat + contact form), Mobile SDK (in-app ticket creation, in-app viewing/commenting on existing tickets, in-app KB), API (programmatic ticket creation), channel integrations / channel framework, CTI integrations, and "closed tickets" as a channel (replies to closed tickets create follow-up tickets instead of reopening).
- Closed-ticket rule: "When a ticket is closed, it can no longer be changed in any way… a follow-up ticket will be created instead."
- Macros: "pre-written responses or actions that agents can apply to tickets with one click."
- Routing: omnichannel routing assigns tickets "based on agent availability and workload"; skills-based and topics-based routing; plan-tier gating for SLA-based timing and urgency/skills prioritization.
- Agent workspace: customer profile with interaction history, side conversations; unified view; AI macro suggestions.
- Automation: alerts for unattended tickets, refund escalations to managers; conditional flows (group assignment triggering Jira issue creation shown in diagram).
- Reporting: ticket volume and agent performance across channels; real-time monitoring ("who's working on what").
- Knowledge: help center KB for self-service; bots suggest articles.
- Positioning: employee service / ITSM use case exists inside the same platform family (ticketing "for employee service").

### Freshdesk

Evidence layer: A− (Tier-1 help-center category structure + Tier-2 product page).

- Help-center categories (Tier 1 structure): Get started (account, configure support channels, customize portal); Ticketing channels (integrate support channels); Configuration and workflows ("workflows such as SLAs, CSAT surveys, ticket forms"); Customer portal setup ("setup your support portal, populate it with useful solutions"); Freshdesk integrations; Reporting and analytics.
- Ticketing page (Tier 2): tickets from every channel (chat, email, voice) handled in one place; prioritize tickets based on customer sentiment and SLAs; AI agent (Freddy) resolves queries autonomously and "hands over with full context"; parent and child tickets ("break big cases into parent and child tickets… divide and conquer"); internal threads for collaboration; routing by agent skill, channel, or capacity; triggers for escalations, re-assignment, and auto-responses.
- Vendor structure: Freshworks ships Freshservice as a separate product "Streamline your IT service and manage internal requests from your employees" — direct vendor-side separation of the external customer help desk from the internal IT service-desk product.

### Zoho Desk

Evidence layer: A− (Tier-2 product page + resources hub).

- "All your support conversations, one tidy inbox" — customer conversations from every channel in one contextual workspace.
- Help center: branded self-service where customers "track tickets, find answers in the knowledge base, join community discussions, and get instant help from an AI bot."
- Work model explicitly narrated in four verbs: Assign (route by skills, workload, availability), Collaborate (shared ticket ownership, internal notes, clear hand-offs), Orchestrate (auto-trigger actions on events, step-by-step resolution processes), Commit (SLAs with automated escalations and deadline tracking).
- AI (Zia): autonomous agents handle routine issues end-to-end with handoff; drafts responses; flags issues early.
- Dashboards: real-time dashboards, detailed reports, customer happiness tracking.
- Resources hub confirms departments/teams setup, automation, AI, self-service, real-time insights as the admin curriculum.

### Help Scout

Evidence layer: A− (Tier-2 product page only).

- Positioning: "The Shared Inbox for B2B Teams"; product vocabulary is conversation-centric (assign *conversations*, not tickets).
- Channels: "email, chat, phone calls, and social under one roof."
- Shared-inbox mechanics: assign conversations automatically or with a click; internal notes "to communicate with teammates before replying"; AI summarize of long threads.
- Customer context: company-level view ("support full accounts"), customer profiles pulling in details from other apps, past conversations and internal notes.
- Happiness: satisfaction ratings "built into every email."
- Productivity: AI drafts; workflows automate assigning/tagging; views = custom-filtered conversation lists (vendor example filters: "VIP", "Waiting over 24 hours"); saved replies for FAQs.
- Companion surfaces: knowledge base (custom help center), proactive messages (alerts/surveys), insights & analytics.

### Jira Service Management

Evidence layer: A (Tier-1 docs hub structure).

- Container object: the service project / "service space" (with templates incl. ITSM space basics).
- Core object vocabulary: requests / work items; agents "raise a request for a customer", "update your customer on your progress", "resolve a customer's request", "close a request when you finish helping a customer".
- Queues: team-level filtered lists ("set up queues for your team", "triage requests for your agents with queues", queue prioritization via groups, best practices for queues at scale).
- Request types: each with its own request form and portal grouping; fields customizable per request type; request types organized into portal groups.
- People model: licensed agents; customers added to the space; customers grouped into "organizations" (e.g., by email domain); request participants.
- Requester surfaces: customer portal + help center; customer-visible "requests list"; knowledge base (Confluence-based) with article suggestions inside request forms; embeddable widget; email channel (processing, allow/blocklists, DMARC); chat via Slack/Teams; mobile.
- Rules: workflows with statuses/transitions per request type; approvals as workflow stages (approvers, approval by email/chat); SLAs (goals, conditions, calendars, priority grouping, JQL-based, auto-close resolved requests); customer notifications; multilingual support.
- Automation: trigger/condition/action rules with presets; automation logs.
- CSAT surveys; reports (default/custom, dashboards).
- Workforce management for routing work to agents (capacity, schedules).
- IT-flavored extensions: ITSM space basics, incidents/changes, virtual service agent (usage limits/billing), on-call/alerts adjacency.

## Cross-product Comparison

| Dimension | Zendesk | Freshdesk | Zoho Desk | Help Scout | JSM |
|---|---|---|---|---|---|
| Core object name | ticket | ticket | ticket | conversation | request / work item |
| Intake channels | email, portal/form, messaging, social, voice, SMS, chat, widget, SDK, API, CTI | "every channel" (chat/email/voice named), channel integrations | every channel, unified inbox | email, chat, phone, social | email, portal, widget, chat (Slack/Teams), API |
| All channels become one tracked record | explicit ("all requests become tickets") | explicit (tickets from every channel) | explicit (one tidy inbox) | implicit (shared inbox) | explicit (requests from any channel into the space) |
| Queue organization | agent workspace views; groups | views; skill/channel/capacity routing | skills/workload/availability assignment | shared inbox + custom-filter views | queues per team, prioritized via groups |
| Assignment/routing | availability + workload; skills/topics routing (tiered) | skill/channel/capacity; triggers | skills/workload/availability; auto-triggers | automatic or click assignment; workflows | manual + WFM routing; queues |
| Agent productivity | macros, AI macro suggestions, side conversations | internal threads, parent/child tickets | internal notes, hand-offs, step-by-step processes | internal notes, saved replies, AI summaries | canned responses, comments (customer vs internal), article sharing |
| SLA machinery | SLA-based routing timing (tiered) | SLAs + sentiment prioritization | SLAs w/ escalations + deadline tracking | (not observed on page) | SLA goals/conditions/calendars, auto-close |
| Knowledge base | help center + bots suggesting articles | portal "useful solutions" | KB + community + AI bot in help center | KB product; saved replies | Confluence KB + article suggestions in forms |
| Requester side | help center, widget, in-app SDK, portal form | customer portal setup category | help center (track tickets) | satisfaction in email thread; (portal implied by KB) | portal, requests list, notifications |
| Satisfaction | (implied via reporting) | CSAT surveys category | customer happiness tracking | ratings built into every email | CSAT surveys |
| Automation | triggers, alerts, conditional flows | triggers (escalation/reassign/auto-response) | auto-triggers, step-by-step processes | workflows (assign/tag) | trigger/condition/action rules |
| Reporting | volume, agent performance, real-time | reporting & analytics | dashboards, reports | insights & analytics | default/custom reports, dashboards |
| Audience pole | customer + employee service | external customers (sibling product for internal) | external customers | external customers (B2B teams) | internal IT/employee service (+ external capable) |
| Surface philosophy | ticket-centric workspace | ticket-centric | ticket-centric with orchestration framing | conversation/shared-inbox-centric | request-centric inside Jira issue engine |

Layer-B cross-product commonalities observed across ≥4 of 5 products:

1. One tracked record per request, regardless of intake channel.
2. Requester-initiated requests; agents work them from organized lists (queue/view/inbox).
3. Correspondence with the requester attached to the record as the primary resolution interaction.
4. Assignment/ownership + team organization (groups/queues/inboxes).
5. Internal (agent-only) notes vs requester-visible replies as a hard separation.
6. Knowledge base + self-service portal as a deflection/companion layer.
7. Satisfaction measurement attached to resolution.
8. Automation rules (trigger/condition/action shape).
9. Reporting over volume, responsiveness, agent performance.
10. Status lifecycle toward a resolved/closed terminal state.
11. AI assistance layer (drafting, summarizing, bots/agents, routing) — present in all five sampled products (era-common).

## Canonical Model (Synthesis Draft)

### L0 — Defining Invariant (deliberately small)

A Help Desk is recognizable only if all of the following hold:

1. **Help request from a requester** — a person outside the support team (customer, user, employee) asks the organization for help. Without an external asker being served, it is a work tracker, not a help desk.
2. **Ticket as persistent tracked record** — each request is captured as an individually identified, persistent record carrying the request, its context, and its history. Without this, it is just a mailbox or chat.
3. **Agent team working an organized queue** — support-team members process the records from structured lists (queues/views/inboxes) with some form of ownership/assignment. Without this, it is personal email.
4. **Correspondence with the requester attached to the ticket as the resolution mechanism** — the work is completed by communicating back to the requester (in any channel). Without this, it is an internal task system.
5. **Managed lifecycle toward resolution/closure** — the record advances through tracked states (open → work → resolved → closed) rather than fading when unanswered. Without this, requests are not "handled" in any accountable sense.

### L1 — Common Mature Structure

- Multi-channel intake: email is the historical backbone; mature products add portal/web forms, chat/messaging, social, voice, SMS, API.
- Thread consolidation: all messages about the same request (across channels) land on one ticket.
- Ticket attributes: priority, category/tags, custom fields; request-type-specific forms (JSM makes this explicit; Freshdesk lists "ticket forms" in its workflow category).
- Routing: rule-based/skill-based/workload-based assignment; round-robin and capacity patterns; team/group scoping.
- SLA machinery: response/resolution targets, business-hour calendars, breach escalations, deadline tracking.
- Agent productivity: macros / canned replies / AI drafts; internal notes; collision avoidance; AI summaries.
- Collaboration: mentions, shared ownership, hand-offs, parent/child ticket decomposition, side conversations with third parties (e.g., other departments).
- Knowledge base + deflection: articles suggested in forms, in conversations, and by bots; KB authoring tied to ticket content.
- Self-service portal: requesters submit via forms and track their own requests; their request list is visible to them.
- Notifications: automatic requester updates on ticket progress; agent notifications.
- CSAT/satisfaction ratings captured at resolution; customer-happiness reporting.
- Reporting/analytics: volume, channel mix, response/resolution times, agent performance, backlog; real-time dashboards in mature products.
- Automation: trigger/condition/action rules for assignment, escalation, follow-ups, auto-replies.
- AI assistance (era-common): autonomous bots/agents for routine requests with human handoff, reply drafting, thread summarization, AI-assisted routing.

### L2 — Variant / Optional Structure

- Audience pole: external customer support vs internal employee/IT help desk. The internal pole drifts toward ITSM: request types mapped to services, approvals as workflow stages, incident/change vocabulary, asset/CMDB adjacency (JSM shows this; Freshworks even splits it into a separate product).
- Surface philosophy: ticket-first (record = ticket) vs conversation-first (record = conversation in a shared inbox). Structurally equivalent; vocabulary and emphasis differ.
- Channel posture: email-first desks, omnichannel desks, messaging-led desks; depth of voice support ranges from "call becomes a ticket" to full telephony.
- Process depth: simple queue-and-reply vs ITSM-grade workflows (approvals, change/incident types, SLA libraries).
- Organizational structuring: multi-team queues, multi-brand/multi-department desks (departments as a structuring concept — observed weakly at Zoho; groups/teams at Zendesk/JSM).
- Scale/segment: SMB lightweight vs enterprise governance (permissions, customer authentication/SSO, safe notifications, multilingual).
- Deployment: SaaS-dominant in the sample; self-managed editions exist in the market (JSM offers a Data Center edition — direct evidence of a non-SaaS deployment pole).

### L3 — Vendor-specific (research notes only)

- Zendesk: Sunshine Conversations channel extensions, Talk Partner Edition (CTI), Web Widget (Classic) vs messaging widget, closed-ticket→follow-up-ticket channel mechanics, plan-tier gating of routing/SLA features, Explore reporting product.
- Freshdesk: Freddy AI Agent with claimed resolution share, Freshdesk Omni packaging, parent/child tickets naming, sentiment+SLA prioritization pairing; Freshservice as the sibling internal product.
- Zoho Desk: Zia assistant/agents, "orchestrate" step-by-step process framing (Blueprint-lineage), community embedded in help center, departmentId-scoped portal ticket submission.
- Jira Service Management: request types vs work types, company-managed vs team-managed spaces, Confluence as the KB substrate, organizations (customer grouping by email domain), virtual service agent usage-limit billing, Opsgenie on-call adjacency, Rovo AI KB, JQL-based SLAs.
- Help Scout: shared-inbox positioning, "Messages" proactive product, collision-detection visuals, deliberate avoidance of "ticket" vocabulary, docs domain unreachable during research.

## Vendor-specific vs Rejected Findings

- Rejected for canonical core: SLA machinery (absent from Help Scout page evidence; common but not defining), knowledge base/portal (a deflection layer — the desk still works without it), omnichannel breadth (email-only desks exist), AI autonomy (era-common enhancement, not structure), satisfaction ratings (measurement, not resolution machinery), parent/child tickets (collaboration pattern).
- Rejected as definitional due to single-source or weak evidence: "closed tickets are immutable, later replies become follow-up requests" (Zendesk-only, A-layer — kept as qualified common behavior in the final doc at most), department/brand structuring as a named concept (weak Zoho evidence), collision detection (imagery evidence only), workforce-management routing (JSM/Zendesk marketing pages — enterprise pole only).
- Kept out entirely (no reliable evidence): precise SLA defaults, exact status-name sets per product, plan/pricing structure, AI resolution-rate claims.

## Boundary Findings

1. **vs Ticketing System (directory sibling)** — the most severe overlap. Ticket machinery (tracked record + queue + lifecycle) is shared. Working seam: a *ticketing system* is the generic machinery for tracking discrete requests/items as tickets in any operational context (facilities, events, IT, engineering), whereas a *help desk* is the requester-serving application of that machinery — the record exists to deliver help back to a person who asked for it, with requester correspondence and resolution semantics at the center. Test: remove requester-facing correspondence and serve internal work-item tracking → ticketing system; keep requester-serving loop → help desk. Recommend joint review when `ticketing-system` is processed.
2. **vs Customer Service Platform / Omnichannel Customer Service Platform** — platforms bundle the desk with routing engines, workforce management, quality assurance, WEM/VOC and contact-center layers. The desk (ticket + queue + correspondence + lifecycle) remains the operational heart; remove the suite layers and a help desk remains. Suite membership is packaging, not structure.
3. **vs ITSM (§14 sibling)** — internal IT service desks are help desks by audience; ITSM adds process governance (incident/problem/change/config) that the help desk core does not require. A help desk that adopts ITSM processes is drifting toward the ITSM Type. Freshworks' separate Freshservice product is vendor-structural evidence for this seam.
4. **vs Customer Support Chat / Customer Service Chatbot Platform** — chat tools own one real-time channel; the desk owns the tracked record and lifecycle. Chat conversations *become* tickets in the desk (explicit in Zendesk's channel model).
5. **vs Self-service Support Portal / Customer Portal** — the portal is the requester-facing surface of the desk (submit/track/KB). Every sampled desk ships a portal component; a portal without a desk behind it is a different Type.
6. **vs Issue Tracker / Bug Tracking System (§12)** — engineering work items are not help requests from an external help-seeker; lifecycle semantics are development-shaped (fix/release), not service-shaped (respond/resolve for a requester).
7. **vs Complaint & Escalation Management** — complaint handling is a specialized complaint-lifecycle slice; the help desk is the general request loop. Escalation exists inside help desks as a rule, not as the object.
8. **vs Contact Center / CCaaS** — voice-first routing/queuing of calls vs record-first processing of requests. A help desk may attach a voice channel (Zendesk voice: calls become tickets); a contact center centers on the live call.
9. **vs Employee Service Portal / ESM (§10)** — requester-facing aggregation vs the fulfillment machinery; the internal help desk is one fulfillment desk behind employee service. (Consistent with the boundary note recorded by the employee-service-portal pass.)

**"Remove one thing" tests:**
- Remove requester correspondence → internal work/ticket tracker (Ticketing System / Issue Tracker pole).
- Remove the ticket as persistent tracked record → shared inbox or chat tool (Email Collaboration / Customer Support Chat).
- Remove the team/queue dimension → personal inbox.
- Remove the requester (no external help-seeker) → project/task management.
- Keep only the voice channel with call queuing → Contact Center.

## Historical / Market-Sample Check

- The defining core above does not depend on the modern SaaS omnichannel pattern. An email-era help desk (support address + ticket records in a shared agent queue + replies + open/solved/closed states) satisfies every L0 element without chat, social, SLA tooling, portals, or AI.
- Internal service desks of the 2000s and IT-flavored service desks (JSM lineage: originally "service desk") satisfy the core with employees as requesters.
- Conversation-first products (Help Scout) satisfy the core with different vocabulary, confirming the core is vocabulary-independent.
- Open-source/self-hosted help desks were not directly sampled (no reliable source fetched); the definition is framed so that they are not excluded, but no claims are made about them.
- Conclusion: the L0 abstraction holds across eras and poles; nothing era-specific (AI, omnichannel, CSAT) was promoted into the core.

## Uncertainties

1. Exact lifecycle state sets per product (e.g., how many states, which are terminal) were not verified across products; only the open→resolved→closed shape is asserted, with labels varying by product.
2. Zoho Desk's department/brand structuring is inferred from weak evidence (portal parameters, admin-curriculum wording) — treated as variant-level, phrased generically in the final doc.
3. Help Scout's requester-facing portal was not directly evidenced (docs unreachable); Help Scout-specific portal claims avoided.
4. SLA mechanics detail (clock start rules, calendars) verified structurally (JSM) and marketing-level (Zoho/Freshdesk) only — final doc keeps SLA claims qualitative.
5. Open-source help desk market (osTicket/Zammad-class) not sampled; not claimed.
6. Whether "collision detection" (agents seeing who is viewing the same ticket) is universal — imagery-only evidence; excluded from final doc.

## Final Synthesis

A Help Desk is the support team's operating application: requests for help arriving over whatever channels the organization offers are captured as individually tracked tickets; agents process them from organized queues, correspond with the requester on the ticket itself, and drive each ticket through a managed lifecycle to resolution, with routing, SLA, automation, knowledge, portal and reporting layers making the loop scalable. The defining core is the requester-serving ticket loop; everything else is scalable maturity or variant. The Type sits between a generic ticketing system (machinery without the requester-serving support context) and a customer service platform (the desk plus an enterprise suite around it), with an internal-employee/IT pole that shades toward ITSM.
