# Outreach Sequencing Platform

## Overview

An **Outreach Sequencing Platform** is a sales execution application in which a sales team defines a repeatable, multi-touch outreach program — a **sequence** of steps across channels such as email, calls, and social touches, separated by waiting periods — and enrolls individual prospects into it. The system then carries the program out: it sends the email steps automatically on schedule, surfaces the human steps (calls, social touches, notes) as tasks for the rep, tracks where each prospect is in the flow, and changes or halts that prospect's progression when the prospect responds — a reply stops the sequence, a bounced email excludes the prospect from further email steps, an opt-out removes them.

The defining structure is small:

```text
Prospect (identified person with a reachable channel)
└── enrolled into
    Sequence (ordered steps + waits, defined once, reused for many prospects)
        └── per-prospect progression state
            ├── system-executed touches (automatic email sends)
            ├── rep-executed touches (call / social / note tasks)
            └── response events that interrupt or redirect the flow
                (reply → stop · bounce → exclude · opt-out → remove)
```

Everything else commonly associated with these products — template libraries, deliverability tooling, unified inboxes, AI drafting, dialers, CRM sync, analytics — is standard equipment that makes the core practical, but the product remains recognizable as this Type without any of it. The Type spans a scope gradient: from standalone email-first sequencers used by small teams, up to enterprise sales engagement platforms where the same sequencing machinery is the core of a much broader revenue suite.

## Users & Context

Primary users:

- **Sales development reps (SDRs/BDRs)** — the main operators. They build or adopt sequences, import or select prospect lists, launch and monitor sequences, and work the human steps (calls, LinkedIn touches) and replies that the system queues for them.
- **Account executives** — typically enroll their own prospects into nurture or follow-up sequences around deals they own, and handle replies from engaged prospects.
- **Sales managers / revenue operations** — standardize the team's outreach by publishing shared sequence templates, setting sending rules and governance, and reading team-level performance.

The work context is high-volume prospecting: a rep runs many prospects through the same program simultaneously, interleaving automated touches with personally executed ones. The application is normally used alongside a CRM (which holds the relationship record) and often alongside prospecting/data tools (which supply the contacts). The sequencing platform sits between them as the execution layer: it takes contacts in, runs the outreach program, and hands engagement outcomes back.

## Core Model

### The Defining Core

**Prospect record.** The unit of work is an identified person — name, email address, and usually company, title, and phone. The prospect is not merely a row in a mailing list: the system maintains a per-prospect state that records which step the prospect is waiting on, what has been sent, and how they have responded.

**Sequence.** A sequence is a reusable program: an ordered chain of steps with a wait (delay) between consecutive steps. Each step specifies a channel and an action — send an email (usually from a template), make a call, perform a LinkedIn action, send an SMS, or complete a generic task. The same sequence is executed independently for every enrolled prospect, so one definition drives hundreds of parallel, individually-tracked outreach flows. Mature products also allow conditional branching — a step or wait that depends on what the prospect did at the previous step (opened, clicked, replied, accepted a connection) — so the program adapts per prospect rather than running as a rigid line.

**Enrollment.** Putting a prospect into a sequence creates a per-prospect instance with its own state: active, waiting on step N, paused, finished, bounced, opted out, out-of-office. Enrollment happens manually (select contacts and add them), in bulk (import a list), on a schedule (start date), or automatically (a trigger or CRM sync adds prospects when conditions are met). A prospect can typically be paused, resumed, skipped past a step, or removed at any time.

**Scheduled execution.** The system, not the rep, drives the timeline. Email steps are sent automatically when the prospect's wait elapses and the sending schedule allows. Human steps are converted into tasks in the rep's queue — the sequence waits until the rep completes the task before progressing that prospect. Sending is throttled by schedules (which days and hours sending is allowed) and per-mailbox daily limits, because volume that looks automated damages deliverability.

**Response interruption.** The platform watches for prospect-side events and lets them override the plan:

- a **reply** stops the sequence for that prospect (continuing to send follow-ups to someone who answered would be both useless and harmful);
- a **bounce** excludes the prospect from further email steps and feeds the sender's reputation;
- an **opt-out** removes the prospect from outreach entirely;
- an **out-of-office** reply typically pauses the prospect temporarily, with resumption after a delay or by hand.

This interruption loop is what separates a sequencing platform from a bulk sender: every prospect is an individual conversation that can end or change course at any moment.

### Standard Capabilities of Mature Products

These are widespread across the researched market and expected in practice, though no single one defines the Type:

- **Templates and personalization variables** — email templates with merge fields (first name, company, custom fields) and reusable snippets; sequence template libraries that teams share and standardize on.
- **Connected mailboxes** — the product sends through the rep's real mailbox (connected via OAuth or SMTP), so outreach arrives as personal 1:1 email rather than bulk marketing mail. Multiple mailboxes per user or per sequence are common in high-volume products.
- **Unified reply inbox** — replies from all sequences land in one inbox inside the product, where the rep answers and classifies the prospect (interested / not interested / do not contact). Classification often feeds automation.
- **Task queue** — all manual steps across all sequences aggregated into a daily work list, often with local-time awareness for calls.
- **Multi-channel steps** — LinkedIn actions and calls are near-universal step types; SMS and WhatsApp steps are common in some markets and products.
- **Progress and performance views** — per-contact progress (which step, what's next), per-step funnel counts, and sequence statistics (sent, opened, clicked, replied, bounced, opted out), plus team-level reporting.
- **A/B testing** — testing variants of email steps against each other.
- **Triggers / automation rules** — event-driven rules (on reply, on open, on opt-out, on call logged…) that change stages, move prospects between sequences, or remove them.
- **Deliverability tooling** — sender authentication guidance (SPF/DKIM/DMARC), custom tracking domains, mailbox warm-up, bounce-rate monitoring with automatic throttling or suspension, plain-text sending options, mailbox rotation.
- **CRM synchronization** — contacts, activity, and engagement outcomes synced with the CRM of record.
- **Team structure** — shared vs. private sequences, roles, and admin controls.

### Concept vs. Implementation

The core model is conceptual; products realize it differently, and the naming varies:

```text
Concept:  the reusable program      → implementations: "sequence", "cadence", "campaign"
Concept:  the processed person      → implementations: "prospect", "lead", "contact", "person"
Concept:  per-prospect state        → implementations: status fields (active/paused/finished/bounced…)
Concept:  response interruption     → implementations: auto-stop rules, triggers, inbox categories
Concept:  sending identity          → implementations: connected mailbox, sender rotation
```

A reader who has only seen one product should still be able to recognize the others from this model.

## How It Works

### Build the sequence

The rep (or a manager, for team-wide plays) creates a sequence: a first email step, a wait, a call task, a wait, a follow-up email, and so on — often with a conditional branch (e.g., different path if the prospect replied or opened). Each email step pulls from a template with personalization variables; each human step defines what the rep should do. The sequence is saved, tested, and — in team settings — shared as a standard play.

### Connect sending infrastructure

The rep connects one or more mailboxes; the admin configures sending schedules (days, hours, time zones), daily sending limits, and deliverability basics (authentication, tracking domain, warm-up where offered). This step exists because the platform sends as the rep, from the rep's own domain, under real-world deliverability constraints.

### Enroll prospects

Prospects come from a CRM sync, a CSV import, a prospecting tool, or manual selection. The rep reviews the list (skipping or removing unsuitable entries), assigns senders if needed, and launches — immediately or on a schedule. Each prospect now has its own progression clock.

### The execution loop

Once launched, the system runs each prospect independently:

```text
prospect enrolled
→ wait elapses (counted against the sending schedule)
→ email step: sent automatically from the connected mailbox
→ human step: task created in the rep's queue; sequence waits until done
→ prospect responds?
     reply    → sequence stops for that prospect; reply lands in the unified inbox
     bounce   → prospect excluded from further email steps
     opt-out  → prospect removed from outreach
     out-of-office → prospect paused, resumed later
→ no response → next wait → next step
→ all steps done → prospect marked finished
```

The rep's daily work is shaped by this loop: work the task queue (calls, LinkedIn touches), answer replies in the inbox, classify prospects, and let the machine keep the rest moving.

### Measure and iterate

Sequence statistics show where prospects stall and which steps earn replies; teams A/B test content, adjust delays, retire weak steps, and publish improved versions as new templates. Automation rules turn recurring judgments (e.g., "reply classified as not interested → remove from all sequences") into standing policy.

## Interfaces

Exact layouts and names vary by product; the surfaces below are described conceptually.

### Sequence editor

The authoring surface for the program itself.

- typical information: step list with channel icons, per-step content, waits between steps, branch conditions
- primary actions: add/reorder/delete steps, edit templates and variables, set delays, configure conditions, save as template, A/B test

### Sequence list / library

The overview of available programs.

- typical information: sequence names, status (active/draft), enrolled-prospect counts, performance summaries
- primary actions: create, duplicate, archive, share with team, start from template

### People / enrollment view (inside a sequence)

The per-prospect state machine made visible — the operational heart of the product.

- typical information: each prospect's current step, status (active/paused/finished/bounced/opted out), last activity, next scheduled touch, per-step waiting counts
- primary actions: enroll, pause/resume, skip a step, remove, change status, filter by progress

### Unified inbox

The reply-handling surface.

- typical information: conversations across sequences and channels, prospect identity and sequence context, classification controls
- primary actions: reply, classify (interested / not interested / do not contact), assign, snooze, hand off

### Task queue

The rep's daily action list for human steps.

- typical information: due tasks with prospect, channel, and sequence context; local-time indicators
- primary actions: complete a call/task, log the outcome, skip, reschedule

### Analytics / reporting

- typical information: sent/open/click/reply/bounce/opt-out rates per sequence and step, team performance, trend views
- primary actions: filter, compare sequences, export, drill into prospects

### Settings (admin)

- typical information: mailboxes, sending schedules and limits, deliverability status, team members and roles, CRM integration, automation rules
- primary actions: connect mailboxes, set schedules/limits, configure triggers, manage sharing and permissions

## Important Rules / Behaviors

- **A reply ends the automated flow.** When a prospect replies, the sequence stops for that prospect automatically — the conversation has become human, and further automated touches would be wrong. This behavior is documented explicitly in products that describe their sequencing mechanics, and the reply lands in the product's inbox for the rep to continue.
- **Bounces protect the future.** A bounced email both excludes that prospect from subsequent email steps and counts against the sender's reputation; products monitor bounce rates and will slow down, suspend, or auto-stop sending when thresholds are exceeded.
- **Opt-out is absolute.** An unsubscribe removes the prospect from outreach regardless of sequence state; products expose opt-out management as a first-class list.
- **Human steps block progression.** A sequence containing a call or task step waits for the rep to complete it before that prospect advances — the rep's action is part of the program's timeline, not an aside to it.
- **Delays respect the sending calendar.** Waits between steps are typically counted against configured sending days/hours, so a "one-day delay" that crosses a weekend or a disabled day lands on the next eligible sending day. Time-zone handling for recipients is a common configuration concern.
- **Sending is throttled.** Daily limits act as caps shared across a sender's campaigns; pacing controls spread sends over the day. Products treat these as protective (deliverability) rather than as targets, and some algorithmic throttling cannot be overridden by the user.
- **Active sequences resist structural edits.** Because prospects are mid-flight, products commonly restrict reordering or replacing steps in a running sequence (or apply changes only to prospects that have not yet reached the affected step); per-prospect skip/pause remains available.
- **One prospect, possibly many sequences.** Products differ on whether a prospect may sit in several sequences at once; where allowed, this is the rep's judgment call, and duplicate-contact handling is a known operational hazard.
- **Out-of-office is a pause, not an end.** OOO replies typically pause the prospect automatically and resume later (on a configured delay or by hand), since the absence is temporary.
- **Consent and anti-spam constraints shape design.** Opt-out links, plain-text options, authentication, and warm-up exist because the product sends 1:1 sales email at volume from personal domains — a context with real deliverability and legal exposure.

## Variants

- **Standalone email-first sequencer** — small-team cold-outreach tools centered on email steps with light call/social support and heavy deliverability tooling; the sequence object is the whole product.
- **Multichannel SMB/mid-market sequencer** — adds native SMS/WhatsApp/calls/LinkedIn steps, built-in warm-up and mailbox management, and increasingly bundled contact data.
- **Enterprise sales engagement platform** — the same sequencing core embedded in a broad revenue suite with native dialer, conversation intelligence, deal management, forecasting, and enterprise governance (SSO, role-based access, audit). Vendors in this tier often market the sequencing capability under a platform brand.
- **Embedded capability inside a CRM or sales suite** — the same core structure (sequence + enrollment + scheduled sends + reply-stop) shipped as a feature of a CRM rather than a standalone product; the Type does not require standalone packaging.
- **AI-assisted to AI-run** — a posture gradient rather than a separate Type: AI drafts or generates sequence content, prioritizes tasks, and — at the far end — autonomous "AI SDR" agents run research-personalize-reply loops with human approval modes on top of the same sequencing machinery.
- **Agency / multi-tenant operation** — client workspaces, consolidated reporting, white-labeling for teams that run outreach on behalf of many companies.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Sales Engagement Platform | closest sibling — probable same Type at broader scope | The market defines sales engagement platforms by exactly this sequencing machinery; enterprise SEPs add dialer, deal management, conversation intelligence, and forecasting around it. The sequencing core is shared; scope differs. Flagged for joint review. |
| Email Marketing Platform | adjacent, frequently confused | Both send email at scale, but email marketing targets audience lists with broadcast/drip campaigns from a marketing sender; sequencing runs a per-prospect state machine with reply interruption, personal sender identity, and human task steps. Remove reply-handling and per-prospect progression and only email marketing remains. |
| Customer Relationship Management / CRM | complementary system of record | The CRM holds relationships and pipeline; the sequencer executes outreach over contacts and syncs outcomes back. Some vendors extend their sequencer with deal management, but pipeline objects are not part of the sequencing core. |
| Sales Prospecting Platform / Contact Discovery / Sales Data Enrichment | upstream feeder | These find and enrich contacts; the sequencer contacts them. Products increasingly bundle both, but the sequencing core does not require a data product. |
| Sales Dialer | channel surface | The dialer centers the live call; in a sequencing platform the call is one step type whose outcome feeds the prospect's state. |
| Marketing Automation Platform | different owner and audience | MAP runs marketing-owned lifecycle programs over broad audiences with forms/landing pages; sequencing is sales-owned, prospect-level, and reply-driven. |
| Lead Management Platform | overlapping lifecycle scope | Lead management spans capture-to-qualification; sequencing is the touch-execution instrument within that span, not the qualification record itself. |

The most important boundary is the first one: in current market usage, "outreach sequencing" names the core capability, and "sales engagement platform" names the same capability plus its enterprise extensions. This document therefore defines the Type by the sequencing core and treats the enterprise bundle as a variant, so that both narrow and broad products are recognized without collapsing the distinction the directory draws between them.

## Representative Products

- **Outreach** — enterprise; the category-defining sales engagement platform, now positioned as an agentic AI revenue platform with sequencing ("Revenue Agents handle sequencing") as a named core capability.
- **Salesloft** — enterprise/mid-market; its sequence object is the "Cadence", the module around which the rest of its revenue platform is organized.
- **Reply.io** — SMB/mid-market; multichannel sequences with built-in deliverability infrastructure (mailbox provisioning, warm-up, rotation) and an AI SDR layer.
- **lemlist** — SMB; email-first cold-outreach tool (sequence object packaged as "campaign") known for deliverability tooling and deep sequence-conditioning mechanics.

## Sources

Research date: **2026-09-06**

Official operational documentation (help centers, directly fetched):

- lemlist Help Center — https://help.lemlist.com/en/ — incl. "Understand campaign sequencing in lemlist", "Understand lemlist's sending algorithm", Campaigns / Sequences & Steps collections
- Reply Help Center — https://support.reply.io/en/ — incl. Sequences collection, "Triggers", "Handling Out-of-Office replies", "Contacts' progress in a sequence"

Official product/platform pages (directly fetched):

- Outreach — https://www.outreach.io/ , https://www.outreach.ai/platform
- Salesloft — https://salesloft.com/ , https://salesloft.com/platform/sales-engagement-software
- Reply.io — https://reply.io/

> Sourcing limitation: Outreach's support site and Salesloft's help center could not be accessed from the research environment on 2026-09-06 (404s / script-rendered pages). Claims about those two products are therefore limited to their official product-page positioning; operational mechanics (step types, reply-stop behavior, limits) are asserted only where directly documented for Reply.io and lemlist. Precise numeric limits and vendor-specific defaults are intentionally omitted from this document and remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis (including the relationship to the Sales Engagement Platform leaf) are recorded in the paired Research Notes.
