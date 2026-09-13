# Research Notes — Outreach Sequencing Platform

Research date: 2026-09-06
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what an "outreach sequencing platform" actually is as an Application Type: what objects exist inside it, how a prospect moves through an outreach program, what the system automates vs. what the rep does manually, how responses change the flow, and where the Type's boundary sits against Sales Engagement Platform, Email Marketing, CRM, and prospecting tools.

## Initial Boundary (hypothesis before research)

- Hypothesis: a platform where a sales rep defines a repeatable ordered set of touches (email / call / social / manual task) with waits between them, enrolls a batch of prospects, and the system executes and tracks the touches, interrupting the flow when the prospect responds.
- Likely confusions:
  - "Sales Engagement Platform" (immediate sibling leaf in the directory) — suspected to be the same market category at broader scope.
  - Email Marketing Platform — both send email at scale; suspected boundary is per-prospect state machine + reply handling.
  - CRM — sequencing platforms sync contacts from CRM; some add deal management.
  - Sales Prospecting / Contact Discovery — finds contacts; sequencing contacts them; products increasingly bundle both.

## Research Questions

1. What is a "sequence" exactly — steps, delays, channels, branching?
2. How do prospects get enrolled (manual, bulk import, CRM sync, triggers)?
3. What is the per-prospect state machine (active, paused, finished, bounced, opted out, out-of-office)?
4. What does the system execute automatically vs. what becomes a manual task for the rep?
5. How are replies detected and handled (auto-stop, classification, unified inbox)?
6. What sending infrastructure is assumed (connected mailbox, schedules, limits, warmup, deliverability)?
7. What analytics exist (per-step, per-contact, team)?
8. What team/governance structures exist (sharing, roles, team modes)?
9. Where is the boundary to Email Marketing, CRM, SEP, prospecting tools?
10. Is the directory leaf "Outreach Sequencing Platform" the same Type as "Sales Engagement Platform"?

## Representative Products

Selected for market coverage + documentation quality + different philosophies + different customer tiers:

| Product | Segment / philosophy | Object name for the sequence | Evidence quality |
|---|---|---|---|
| Outreach | Enterprise; category-defining sales engagement platform, repositioned (2025–2026) as "Agentic AI Revenue Platform" | Sequences (inside Sales Engagement capability) | Tier 2 only (platform/product pages); support site unreachable |
| Salesloft | Enterprise/mid-market; "Predictive Revenue System" built around the cadence | **Cadence** | Tier 2 (Cadence product page + FAQ); help center JS-blocked |
| Reply.io | SMB/mid-market; multichannel sequencing + deliverability stack + AI SDR | **Sequence** | Tier 1 (Intercom help center, 61 sequence articles) + Tier 2 |
| lemlist | SMB cold outreach; email-first, deliverability-obsessed | **Campaign** (contains the sequence) | Tier 1 (Intercom help center, deep mechanics articles) |

Note: HubSpot "Sequences" (a sequencing capability embedded in a CRM suite) was identified as an additional structural data point but was not fetched; not used as evidence.

## Sources

Tier 1 (official operational documentation, directly fetched 2026-09-06):

- lemlist Help Center — https://help.lemlist.com/en/ (hub)
  - Understand campaign sequencing in lemlist — https://help.lemlist.com/en/articles/12875247
  - Understand lemlist's sending algorithm — https://help.lemlist.com/en/articles/4452763
  - Campaigns collection — https://help.lemlist.com/en/collections/17109612
  - Sequences & Steps collection — https://help.lemlist.com/en/collections/17345322
- Reply Help Center — https://support.reply.io/en/ (hub)
  - Sequences collection — https://support.reply.io/en/collections/111814
  - Triggers — https://support.reply.io/en/articles/4794327
  - Handling Out-of-Office replies — https://support.reply.io/en/articles/4614513
  - Contacts' progress in a sequence — https://support.reply.io/en/articles/6247076

Tier 2 (official product/marketing pages, directly fetched 2026-09-06):

- Outreach — https://www.outreach.io/ , https://www.outreach.ai/platform
- Salesloft — https://salesloft.com/ , https://salesloft.com/platform/sales-engagement-software
- Reply.io — https://reply.io/

Source-access limitations:

- Outreach support site (support.outreach.io) returned 404 on all attempted paths; Outreach operational detail (step types, limits, sequence mechanics) could not be verified. Outreach claims are kept at platform-positioning level.
- Salesloft help center (help.salesloft.com) is a JS-rendered Salesforce site that fails to render ("CSS Error"); Salesloft operational detail comes from the Cadence product page and its FAQ only. Assertion strength reduced accordingly.
- help.reply.io transport-errored twice; the live help center was found at support.reply.io and used instead.
- No third-party reviews were needed; official documentation was sufficient for three of four products.

## Product Observations

### lemlist (evidence layer A — direct observation of official help docs)

Object structure:

- The top-level working object is the **campaign**; inside it sits the **sequence** of steps (email, LinkedIn invitation/message/profile visit, call, task). Help center organizes under "Campaigns → Sequences & Steps".
- Leads are imported into a campaign and launched (manually or on a schedule); per-lead launch controls include skip/un-skip, remove, pause/resume, and "reverse launch".

Sequence mechanics (from "Understand campaign sequencing in lemlist"):

- Steps progress by configured **delays**, but delays are counted in **sending days**, not calendar days (non-sending days don't count).
- **Branches based on lead behavior**: if a lead doesn't take the expected action (e.g., doesn't accept an invitation within the configured timeframe), the lead moves to a different branch ("no" branch) with different follow-ups. Conditional steps like "If email is opened" require a delay to allow detection.
- **Bounces stop future email steps** for that lead.
- **Reply stops the sequence** automatically for that lead (marked completed) to prevent duplicate communication.
- **Manual tasks block progression**: a follow-up email after a call task only triggers after the task is marked Done. Manual tasks can still send when the campaign is paused (if marked done), but no new tasks are generated while paused.
- **Active-campaign edit restrictions**: steps cannot be reordered or replaced after launch; per-lead skip is available; changing a step from automatic to manual only affects leads whose tasks haven't been created yet.
- Optional company-level pause: pause the campaign for all leads of a company when one lead engages.

Sending infrastructure (from "Understand lemlist's sending algorithm"):

- Sending algorithm spreads first-step emails at intervals (e.g., "reach a new lead every 20 minutes" applies to the first step), monitors bounce rates, open rates, domain age, SPF/DKIM, tracking-domain quality, and engagement signals; it slows sending when reputation is at risk and cannot be overridden.
- Daily sending limits act as **caps, not guarantees**; a rolling 24-hour window is used; the limit is shared globally per sender across all campaigns. Provider defaults documented (Gmail/Workspace 500/day, Outlook/O365 300/day per account) — product-documented defaults, kept out of the canonical document.
- Schedule configuration: timezone, sending days, sending window, pacing; campaigns can be scheduled to start on a future date.
- Deliverability tooling: lemwarm (warmup, 2–4 weeks recommended), DNS health (SPF/DKIM/DMARC), custom tracking domain, Deliverability Hub, sending-limits settings.

Reply handling:

- Unified **lemlist Inbox** for all conversations (email + LinkedIn); replies can be answered from the product; leads can be marked **interested / not interested**; an Unsubscribes section manages opt-outs; out-of-office detection exists.
- Tasks section aggregates manual steps with a local-time filter for calls/emails.

Analytics:

- Campaign stats (open/click/reply), negative metrics (bounces, unsubscribes, skipped steps), reports overview with filters/widgets, export.

Other capabilities observed:

- A/B tests, inbox rotation, dynamic senders, AI sequence generation, LinkedIn automation collection, calling & messaging (phone/WhatsApp/SMS), CRM integrations, API.

### Reply.io (evidence layer A — direct observation of official help docs + product page)

Object structure:

- Top-level object is the **sequence**; contacts ("people") are enrolled into sequences; a **People tab** inside each sequence tracks per-contact progress (current step, waiting counts per step, history per step, red badge for missing data with a Skip action).
- Sequences can be duplicated (with people moved over), saved as templates, run in Team Edition (private vs. public modes; visibility of teammates' sequences).

Steps and channels (from "Steps and Channels" collection):

- Step types documented: email, **call step**, **WhatsApp step**, **LinkedIn step (manual connections)**, **Zapier step**, **task step**, **SMS step**; A/B testing for emails.
- Multiple email accounts per sequence; contacts can be assigned to matching email providers; plain-text sending mode; same-thread follow-ups; CC/BCC; custom opt-out link.

Enrollment and automation (from "Triggers"):

- **Triggers** = built-in event→condition→action automations. Events include: contact created/updated, contact replied to sequence email, opened email, clicked link, finished sequence, inbox category set for reply (Interested / Not Interested / Do Not Contact…), opted out, call logged, sequence email sent/bounced, LinkedIn connection accepted / message reply received / connection forbidden (privacy settings / missing email) / invalid LinkedIn URL.
- Actions include: move to sequence, remove from sequence, add to list, set contact stage, mark as finished, pause contact, update field, assign owner (Team Edition).
- Example automations: opt-out → remove from sequence + set Do-Not-Contact stage; positive call outcome → set stage Interested.
- Contacts can be scheduled to start a sequence at a future time.

Reply handling:

- **Unified Inbox** with sorting and per-sequence inbox; inbox categories (Interested, Not Interested, Do Not Contact, etc.) drive triggers.
- **Out-of-Office handling**: automatic mode (enabled by default) assigns Out-of-Office status, pauses the contact, and resumes after a configured number of days (system cannot parse return dates from the email); manual mode (change status back to Active). When an OOO contact later replies, status changes per sequence settings (mark finished or continue sending).
- Sequence suspension: bounce-rate threshold handling; auto-stop sequences if the email account gets blocked; account-restore guides for Google/Microsoft.

Sending infrastructure:

- Email accounts connected via OAuth/SMTP; inbox sync; **mailbox purchase inside the product** (Google/Microsoft mailboxes, new or pre-warmed, DNS configured automatically), automatic **warmup** (MailToaster; peer-to-peer network), **mailbox rotation** across sequences, email validation add-on, anti-spam/deliverability suite.
- Product page: "Multichannel conditional sequences" — email + follow-ups, LinkedIn touchpoints, WhatsApp, SMS, calls, or any channel via Zapier, "adapt based on replies and actions".

AI layer (product page + AI SDR collection):

- Jason AI SDR: AI-generated sequences, AI variables, AI response generation, research agents; **autopilot vs. copilot modes**; approval mode for human review; mobile app for review/notifications.

Analytics:

- Sequence stats; reports on sequence errors; team performance and channel-efficiency reports; CSV export.

### Salesloft (evidence layer B-limited — product page + FAQ only; help center inaccessible)

- The sequence object is the **Cadence**: "a structured sequence of touchpoints — emails, calls, social messages — designed to engage prospects consistently over time" (vendor FAQ).
- Cadence product page shows: multi-channel cadences; email step builder with dynamic merge fields and live preview; templates and snippets; cadence template library; automation rules; AI agents (buyer identification, account research, email drafting); Salesloft Meetings (buyers book from emails); **native sales dialer** (call or text, auto-capture interactions; third-party dialer integration supported); mobile app ("23 tasks due today, prioritized by AI" — cadence steps as a task queue).
- Platform context: Cadence is one module of a broader platform (Conversation Intelligence, Deals, Rhythm, Clari Forecast, Inspect, Revenue Cadences, Analytics).
- Vendor FAQ defines the category: "Sales engagement software is a platform that helps sales teams manage, automate, and optimize their prospecting across multiple channels — email, phone, and social. It combines sales cadence tool capabilities, automation rules, and AI…"
- Operational mechanics (reply-stop behavior, delay counting, state machine) could not be verified — not asserted.

### Outreach (evidence layer B-limited — product/platform pages only; support site inaccessible)

- Outreach is the category-defining "sales engagement platform"; in 2025–2026 it repositioned as an "Agentic AI Revenue Platform" unifying prospect engagement, deal management, forecasting, coaching, account management.
- Sales Engagement capability description (platform page): "Capture all sales activity as it happens and engage customers across every channel, at scale. Revenue Agents handle sequencing so reps focus on conversations, not coordination." Sequencing remains a named core capability.
- Enterprise posture: SSO, role-based access controls, governance ("fully configurable agent controls… audit trails"), 90+ integrations.
- Operational sequence mechanics could not be verified — not asserted.

## Cross-product Comparison

| Dimension | lemlist | Reply.io | Salesloft | Outreach |
|---|---|---|---|---|
| Sequence object name | Campaign (contains sequence) | Sequence | Cadence | Sequences (capability) |
| Prospect record | Lead | Contact / Person | Contact | Prospect |
| Enrollment | Import + launch (manual/scheduled), per-lead controls | Import, schedule start, triggers, CRM sync | Add to cadence (page evidence) | (unverified) |
| Email steps with delays | Yes (sending-day delays) | Yes (step delays management) | Yes (multi-day multi-step builder) | Yes (capability claim) |
| Branching / conditions | Yes (behavior branches, open/click conditions) | Yes (conditional sequences) | Automation rules (page) | (unverified) |
| Reply stops sequence | Yes (auto-stop, marked completed) | Yes (reply handling; OOO pause/resume) | (unverified) | (unverified) |
| Bounce handling | Stops future email steps | Bounce-rate threshold; suspension; resend | (unverified) | (unverified) |
| Manual task steps | Yes (block until Done) | Yes (task step) | Yes (task queue, mobile) | Yes (capability claim) |
| Call step | Yes (calling & messaging) | Yes (call step; dialer add-on) | Yes (native dialer) | (unverified; platform includes dialing) |
| LinkedIn step | Yes (automation) | Yes (manual + automated) | Yes (social touches) | (unverified) |
| SMS/WhatsApp | Yes (calling & messaging) | Yes (SMS, WhatsApp steps) | Text from dialer | (unverified) |
| Unified inbox | Yes (lemlist Inbox) | Yes (unified inbox, categories) | (not observed on page) | (unverified) |
| Reply classification | Interested / not interested | Inbox categories → triggers | (unverified) | (unverified) |
| OOO handling | Yes (detection) | Yes (auto pause/resume + manual) | (unverified) | (unverified) |
| Sending schedule/limits | Yes (days, window, pacing, caps, rolling window) | Yes (schedules; plain-text; provider matching) | (unverified) | (unverified) |
| Warmup / deliverability | lemwarm, DNS health, tracking domain, Deliverability Hub | Built-in warmup, mailbox purchase, rotation, validation | (not observed) | (not observed) |
| A/B testing | Yes | Yes (emails) | (unverified) | (unverified) |
| Templates/snippets | Yes | Yes (save as template) | Yes (templates + snippets) | (unverified) |
| Triggers/automation rules | Conditions in sequence | Triggers (event→action) | Automation rules | (unverified) |
| CRM sync | Yes (integrations) | Yes (Salesforce, HubSpot, Pipedrive…) | Yes (platform) | Yes (90+ integrations) |
| Team features | Team collaboration | Team Edition (private/public), roles | Platform teams | Enterprise RBAC/SSO/governance |
| AI layer | AI sequence generation | Jason AI SDR (autopilot/copilot/approval) | AI agents (research/draft/prioritize) | AI Agents (Revenue Agents handle sequencing) |
| Analytics | Campaign stats + negative metrics + reports | Sequence stats + error reports + team reports | Platform analytics | Platform analytics |
| Adjacent modules in same vendor | lemcal, Signal Agents, lemwarm | Data (1B+ contacts), Findy, MailToaster, Email API | Conversation Intelligence, Deals, Rhythm, Forecast | Deal mgmt, forecasting, coaching, account mgmt |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being an outreach sequencing platform:

1. **Prospect record** — an identified person (with at least one reachable channel) who is the unit being processed.
2. **Sequence definition** — an ordered set of steps across one or more channels, separated by waits/delays, defined once and reused for many prospects.
3. **Enrollment** — placing a specific prospect into a specific sequence, creating a per-prospect instance with its own state and progress.
4. **Scheduled execution** — the system itself performs or schedules the touches according to the plan (sends the email automatically; surfaces call/manual steps as tasks) without the rep triggering each touch.
5. **Response interruption** — prospect-side events (reply, bounce, opt-out) are detected and change or halt that prospect's progression.

Remove the sequence definition → contact manager. Remove enrollment → template library. Remove scheduled execution → to-do list. Remove response interruption → one-way email blast tool (email marketing). All five are required.

### L1 — Common Mature Structure

Present across the researched sample (evidence B unless noted):

- Email templates with variables/merge fields and snippets; reusable sequence template libraries
- Connected sending mailboxes (OAuth/SMTP) with per-user sending identity
- Sending schedules (days/hours/timezone) and pacing/daily-limit controls
- Unified inbox for replies; reply classification (interested / not interested / do-not-contact)
- Manual task steps (call, LinkedIn, note) aggregated in a task queue
- Multi-channel steps beyond email (LinkedIn, calls; SMS/WhatsApp in several products)
- Per-step and per-contact progress views; sequence-level stats (sent/open/click/reply/bounce/opt-out)
- Pause/resume/skip/remove per contact; finished state
- A/B testing of sequence content
- Out-of-office detection and pause/resume handling
- Bounce handling and deliverability tooling (warmup, authentication guidance, tracking domains, bounce thresholds)
- Triggers / automation rules (event → action) for enrollment and stage management
- CRM synchronization (Salesforce / HubSpot / Pipedrive class)
- Team sharing of sequences; roles; team vs. private visibility modes

### L2 — Variant / Optional Structure

- **Scope posture**: standalone sequencing tool (lemlist, Reply core) vs. sequencing as the core of a broader sales engagement/revenue platform (Outreach, Salesloft with dialer, deal management, conversation intelligence, forecasting)
- **Channel depth**: email-first vs. full multichannel (SMS/WhatsApp/calls); native dialer vs. integrated third-party dialer vs. none
- **LinkedIn automation posture**: automated actions vs. manual-only steps (platform-terms sensitivity)
- **AI posture**: AI-assisted drafting → AI-generated sequences → AI SDR agents with autopilot/copilot/approval modes
- **Data/prospecting bundling**: built-in contact databases, email finders, intent signals, website-visitor identification
- **Deliverability infrastructure depth**: guidance-only vs. built-in warmup vs. in-product mailbox purchase + rotation + validation
- **Meeting scheduling** embedded in sequences (booking links)
- **Agency/multi-tenant operation**: client workspaces, white label, consolidated reporting
- **Enterprise governance**: SSO, RBAC, audit trails, agent governance
- **Object naming**: sequence vs. cadence vs. campaign
- **Deployment of the Type itself**: standalone product vs. embedded capability inside a CRM/sales suite

### L3 — Vendor-specific (research notes only)

- Outreach: Agent Studio, Outreach Omni, Meeting Prep Agent, AI Topics Explorer, Knowledge base, Outreach MCP; "Revenue Orchestration" positioning
- Salesloft: Rhythm (workflow prioritization), Conductor AI, Revenue Cadences, Clari suite (Forecast/Inspect), Drift/Groove
- Reply.io: Jason AI SDR, MailToaster (warmup), Findy (LinkedIn email finder), Generect-powered live data, Email Infrastructure product, MCP/API-led outbound
- lemlist: lemwarm, lemcal, Signal Agents, Dynamic Senders, company-level pause, "reverse launch"

## Rejected Findings

- "Sequencing platforms are defined by LinkedIn automation" — rejected: LinkedIn steps are common but several products treat them as manual steps; email + task sequencing exists without LinkedIn.
- "Warmup/rotation is part of the Type" — rejected: it is deliverability infrastructure that varies from guidance-only to full in-product mailbox commerce; not definitional.
- "AI SDR is the new core" — rejected: all four products still expose the human-directed sequence as the primary structure; AI is an execution/posture layer (L2).
- "Sequencing = email marketing drip" — rejected: the per-prospect state machine, reply interruption, and 1:1 personal-sender model are structurally different from audience-list campaign sending (see Boundary Findings).
- Precise numeric limits (e.g., specific daily caps) — rejected for the canonical document: provider- and product-dependent; only product-documented defaults exist and they are not stable across the sample.

## Boundary Findings

1. **vs Sales Engagement Platform (sibling leaf, §07)** — the strongest issue. The market's own definition of "sales engagement software" (Salesloft FAQ) is "manage, automate, and optimize prospecting across multiple channels… combines sales cadence tool capabilities, automation rules, and AI" — i.e., the sequencing machinery **is** the defining capability of the SEP category. Outreach and Salesloft (the two archetypal SEPs) are sequencers at enterprise scope; Reply.io and lemlist are sequencers at SMB scope. The two directory leaves likely describe one Type seen at two scopes (narrow sequencer ↔ full SEP bundle), or an umbrella/instance relationship. **Flagged for joint review when Sales Engagement Platform is processed.** This document defines the Type so that both narrow and broad products satisfy it, with platform extensions treated as variants.
2. **vs Email Marketing Platform (§06)** — email marketing sends campaigns to audience lists (opt-in, broadcast or drip, marketing-sender identity); sequencing runs a per-prospect state machine with reply detection that halts the flow, 1:1 personal sender identity, and prospecting intent. Drip campaigns overlap on "automated series of emails", but lack enrollment state, reply-stop, and task steps. Test: remove reply-handling and per-prospect progression → email marketing remains.
3. **vs CRM (§07)** — CRM is the system of record for relationships/deals; the sequencer is an execution layer over contacts, normally syncing from the CRM. Some vendors add deal management (Outreach, Salesloft) — that is platform extension, not the sequencing core. Test: remove pipeline/deal objects → sequencer remains; remove sequence/enrollment → CRM remains.
4. **vs Sales Prospecting Platform / Contact Discovery / Sales Data Enrichment (§07)** — discovery finds and enriches contacts; sequencing contacts them. Products increasingly bundle both (Reply data, Salesloft buyer-identification agent), but the sequencing core does not require a data product.
5. **vs Sales Dialer (§07)** — the dialer is a channel surface; inside a sequencing platform the call appears as a step type and its outcome feeds the state machine. Standalone dialers center the live call, not the multi-touch program.
6. **vs Marketing Automation Platform (§06)** — MAP is marketing-owned (forms, landing pages, lifecycle programs, broad audiences); sequencing is sales-owned, prospect-level, and reply-driven.
7. **Historical check**: the L0 holds for older and differently-shaped implementations — CRM-embedded sequence features (e.g., a CRM suite's "sequences" capability), early email follow-up tools, and auto-dialer-era cadences all satisfy sequence + enrollment + scheduled execution + response interruption without LinkedIn, AI, or warmup. The definition is not over-fitted to the current AI/multichannel market.

## Uncertainties

- Outreach and Salesloft operational mechanics (exact step types, reply-stop behavior, delay counting, state names) are unverified; both products' claims in this research are limited to positioning and page-level capability descriptions. The canonical document deliberately avoids asserting their internal mechanics.
- Whether the directory intends "Outreach Sequencing Platform" and "Sales Engagement Platform" as distinct Types is a taxonomy question; evidence suggests one Type at two scopes (see Boundary Findings #1).
- Reply-handling behavior in enterprise products (auto-stop on reply) is verified for lemlist and Reply.io only; generalized in the canonical document with "commonly" wording.
- The relative weight of SMS/WhatsApp channels varies by region; treated as variant channel depth, not core.

## Final Synthesis

An outreach sequencing platform is a sales execution application built around a **per-prospect state machine driven by a reusable multi-touch program**. The vendor-independent core: define a sequence (ordered steps across channels with waits), enroll prospects, let the system execute the scheduled touches (automatic email sends; manual steps surfaced as tasks), detect prospect responses, and let responses interrupt or redirect the flow (reply stops, bounce excludes, opt-out removes). Around this core, mature products add template/personalization machinery, sending infrastructure and deliverability controls, unified reply handling, analytics, triggers, CRM sync, and team governance. The Type spans a scope gradient from standalone email-first sequencers to enterprise sales engagement platforms where sequencing is the core of a broader revenue suite — the latter being the same core structure plus adjacent modules, not a different structure.
