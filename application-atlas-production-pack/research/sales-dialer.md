# Research Notes — Sales Dialer

Research date: **2026-09-07**

## Research Goal

Understand what a Sales Dialer actually is as an Application Type: what objects and machinery it consists of, how an individual seller's calling work is structured (list → session → call → outcome → next), what gets captured and where it flows, how it is packaged in the market, and where its boundaries lie against the neighboring §07 leaves that share this family (Call Center Platform, Sales Engagement Platform / Outreach Sequencing Platform, Softphone Application, Conversation Intelligence Platform, Sales Call Coaching Platform, CRM, Lead Management Platform).

## Initial Boundary (hypothesis before research)

- **What**: the individual sales rep's outbound calling workstation — place outbound sales calls efficiently against a managed list of sales records, see who is being called and why, and log what happened back into the sales system of record.
- **Who**: individual sellers (SDRs/BDRs, inside sales reps, account executives), plus vertical agents (real estate, mortgage, insurance).
- **Primary problem solved**: manual dialing is slow, context is scattered, post-call admin is heavy, and connection rates are poor; the dialer compresses all of it into one record-driven calling loop.
- **Likely confusables**: Call Center Platform (team-scale ACD + campaigns + compliance), Sales Engagement Platform (multi-touch sequences where the call is one step), Softphone (generic telephony endpoint), Conversation Intelligence (analyzes calls rather than places them).
- **Known family context from prior sibling passes**: call-center-platform pass recorded "Sales Dialer = individual-rep outbound inside sales workflow vs team-scale campaign machinery + compliance"; outreach-sequencing-platform pass recorded "the dialer is a channel surface; standalone dialers center the live call, not the multi-touch program"; sales-call-coaching-platform pass recorded "SEP/dialer products execute outbound work; this Type develops the seller."

## Research Questions

1. What are the core objects? (prospect record, call list/queue, calling session, live call, call record/outcome, caller ID/line)
2. What does the seller's calling loop look like, step by step?
3. How are calls physically placed (browser softphone, dial-in bridge, forwarding, carrier relay)?
4. What automation levels exist (click-to-call → power dial → parallel/predictive/AI answer detection)?
5. What is captured per call (disposition, notes, recording, transcript) and where does it go (native store, CRM, SEP)?
6. What productivity machinery is standard (voicemail drop, local presence, scripts, SMS)?
7. How much compliance belongs to this Type (DNC checks, dialing windows, recording consent, abandonment) vs. being call-center territory?
8. Is this an independent Type or a capability embedded in CRM/SEP? What is the "remove what → becomes what" test for each neighbor?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different packaging/customer tiers:

| Product | Philosophy / packaging | Tier |
|---|---|---|
| PhoneBurner | standalone classic power dialer with native contact management; SMB/mid-market | mid |
| Kixie | standalone dialer as browser-based app layered over CRMs; SMB; connection-rate tooling pole | SMB |
| Orum | AI-first parallel dialer platform ("calling performance system"); enterprise SDR teams | enterprise |
| Close (Calling + Predictive Dialer) | calling embedded natively inside a CRM | SMB/mid-market |
| Gong (Gong Dialer inside Engage) | dialer as module of a conversation-intelligence + engagement suite | enterprise |

## Sources

- PhoneBurner Help Center (Zendesk): Dialing section index + "QuickStart Start Dialing" article — https://support.phoneburner.com/hc/en-us/sections/115001617186-Dialing , https://support.phoneburner.com/hc/en-us/articles/36410902719252-QuickStart-Start-Dialing (fetched 2026-09-07). Section index surfaced articles: Click to Call Caller ID, Connect Score, Creating a Phone Script, Call Transfer, Enhanced Click to Call, QuickStart Start Dialing, Call Transcription Overview, AI Note Taker (Premium), Live Answer Rate FAQ, Dialer Pause and Preview, Dialer Presets, Caller ID verification policy, dialing-time restrictions, ARMOR, call recording during transfer, live voicemail. Help-center top-level sections: Contact Management, Emailing, Dialing, SMS, Numbers, LeadStream, Integrations, Inbound, ARMOR, Team Accounts. www.phoneburner.com marketing pages returned 403 (limitation noted).
- Kixie: root page https://www.kixie.com/ and Power Dialer feature page https://www.kixie.com/features/power-dialer/ (fetched 2026-09-07).
- Orum: root page https://orum.com/ incl. product FAQ (fetched 2026-09-07). /platform/dialer returned 404 (limitation noted).
- Close Help Center: "Calling" guide https://help.close.com/feature-guide/calling.md and "Using the Predictive Dialer" https://help.close.com/feature-guide/power-predictive-dialing/using-the-predictive-dialer.md (fetched 2026-09-07).
- Gong Help Center: "Gong Dialer FAQs" https://help.gong.io/docs/gong-dialer-faqs (fetched 2026-09-07).
- Prior sibling research notes in this repo: research/call-center-platform.md, research/outreach-sequencing-platform.md, research/sales-call-coaching-platform.md.

Source-access limitations: PhoneBurner marketing site blocked (403) — evidence for that product comes from its help center only; Orum evidence comes from its root page + FAQ (product subpage 404); Salesloft dialer help article could not be located (404) and was replaced by Gong as the suite-embedded sample. No pricing/plan/numeric claims in the final document rely on any of these degraded paths.

## Product Observations

### PhoneBurner (standalone power dialer) — Evidence Layer A

From help center (operational documentation):

- Setup elements before dialing: import contacts, record outgoing voicemail, configure outbound caller ID, organize folders in the **Contact Manager**.
- **Dial session** is the work container: select a folder/contacts → "Begin Dial Session" → configure: phone script (displayed on screen during calls), dispositions (previously configured sets), voicemail recording, caller ID (e.g., a purchased number), dialer mode, call recording.
- **Dialer modes**: Power Dialing (auto-calls the next contact immediately; "most popular") vs. Pause and Preview (reviews each contact before dialing).
- Connection: browser + headset (plan-dependent) or dial in using a telephone.
- During session: click to leave a **pre-recorded voicemail without waiting for the beep**; or wait and leave a live voicemail; **Live Answer** button during the conversation (no delay when prospect picks up); End Call; **Follow-Up disposition requires a follow-up date** before it can be saved; add notes; create appointments; put contact on hold; transfer calls (requires designated transfer agents).
- Help-center structure implies standard capability set: Contact Management, Emailing, SMS, Numbers (caller-ID management incl. verification policy), LeadStream (lead distribution among users), Inbound, Integrations (Salesforce install articles), **ARMOR** (anti-spam-label protection), Connect Score, call transcription + AI note taker (premium), restrictions on dialing times.
- Evidence of compliance posture: dialing-time restrictions, caller-ID verification policy, spam-label remediation (ARMOR), spam-flag education article.

### Kixie (standalone browser dialer over CRMs) — Evidence Layer A (product pages)

- Multi-line power dialer; auto-dial numbers in parallel; **AI human-voice detection** automatically connects the rep when a live person answers (vs. a recording).
- **Power Dialer session UI** with live session statistics: Live / Queued / Dialed / Connected / Avg duration / Currently dialing.
- **ConnectionBoost**: local presence + number monitoring + progressive caller ID to manage outbound number reputation and pickup rates; separate **caller-ID reputation** tooling to monitor/remediate "Spam Risk"/"Scam Likely" labels.
- **DNC support**: checks against the National Do Not Call Registry and internal suppression lists (vendor states customers remain responsible for legal review).
- **Auto-logging**: "All of your calls, texts, outcomes and recordings are logged in your CRM automatically."
- Native CRM integrations: HubSpot, Salesforce, Pipedrive, HighLevel, Zoho, Close, Copper, etc. (long list).
- Also ships a "Contact Center" feature (enterprise-grade call management) — a deliberate expansion pole noted for boundaries; and Conversation Intelligence (AI call analysis and coaching).
- Vendor's own educational FAQ defines power vs. progressive vs. predictive dialers (power = 1:1 dial-down of a list; progressive/predictive = multiple numbers per agent using availability prediction) — consistent with cross-industry usage but treated as vendor-educational content.

### Orum (AI parallel dialer platform) — Evidence Layer A (root page + FAQ)

- Self-positioning: "The Calling Performance System for Sales Teams"; "purpose-built to maximize live conversations." FAQ explicitly states: "SEPs and CRMs manage sequences and digital outreach; Orum is purpose-built to maximize live conversations. We sit alongside your existing tools, optimizing connect rate, dialing strategy, and coaching." (Vendor-articulated boundary vs. SEP/CRM.)
- **Parallel dialing**: dials multiple numbers simultaneously; if two people pick up, system "detect[s] who answered first down to the millisecond, automatically connect[s] you to that person, and end[s]/cancel[s] the other call — they just see a missed call, and that number is dropped into your **Canceled Calls bucket** so you can easily call them back afterward."
- Platform modules beyond the dialer: Coaching (AI scorecards, coaching portals, AI roleplay), **Salesfloor** (virtual sales floor: reps dial together, leaderboards, live listening), Orum AI trained on sales-call data.
- Integrations: Salesforce, HubSpot, Outreach, Salesloft, Gong Engage, Apollo, webhooks — "calls, outcomes, and recordings flow where your team already works."
- Spam protection: number rotation, country matching, reputation monitoring.
- International calling (plan-dependent); SOC 2 / ISO / GDPR posture; enterprise SDR-team audience.

### Close (CRM-native calling + predictive dialer) — Evidence Layer A (full Tier 1 guides)

Calling guide:

- Calling available on all plans; usage charged per minute (Twilio pricing) — packaging as usage-billed capability of the CRM.
- **Phone popover**: outgoing caller-ID selection (verified external numbers, group numbers, CNAM business name — US carriers only), auto-record toggle, headset/microphone settings, manual dial of any number (incl. outside the CRM).
- **Calling a lead**: click the calling icon on lead/contact → call bar popup with mute, transfer, dialpad, voicemail drop, duration, hang up; **a Call Note is automatically created** at connect and is editable during/after the call.
- Transcription + AI summary via "Call Assistant" (org-level opt-in, requires recording enabled).
- Transfer to any User/Group Number or external number; no warm transfer.
- **Voicemail Drop** (plan-gated): pre-recorded; call note auto-indicates "Left VM."
- **Inbound**: ringing + call bar; known number → lead info displayed; group numbers ring members, first answer wins, hang-up continues ringing others; unknown number → create a new lead; missed calls + voicemails in the Inbox for follow-up.
- **Call dispositions** (product-specific list): Answered, No answer, Busy, Blocked, Error, Left a voicemail, Directed to voicemail (inbound), Abandoned (predictive only); dispositions usable as search filters over call activity.
- Manual call logging for calls made outside the system.
- Call recordings: opt-in auto-record with terms acceptance, pauseable mid-call, playback/download, plan-dependent retention (specific numbers kept here in notes only).
- Call quality indicators (CQI) + post-call quality feedback rating.

Predictive dialer guide (separate org-level mode):

- Enabled per Smart View (a saved lead filter/list); predictive calls originate from a **group caller ID** (system, not a specific user).
- Requires recording an **abandonment message** (must contain organization name + contact number) for answered-but-unstaffed calls; "Abandoned" disposition; org-level exclusion windows for recently called/abandoned leads (precise windows in notes only).
- **Calling queue view**: current list + dialed count, calls made today, other users dialing the same list + their status, leads currently being dialed.
- Auto-adjusts dialing rate based on team size, answer rate, abandonment rate, average talk time; vendor explicitly documents it is designed for multiple concurrent callers (solo ≈ 1x, no benefit).
- On connect: the lead's page opens automatically; call note auto-populated; pause or "Call Next Lead" controls; dialer waits while the lead is edited.
- Automated dialers call only the primary number of the primary contact; not compatible with lead-visibility permissions.

### Gong (dialer inside Engage suite) — Evidence Layer A (Tier 1 FAQ)

- Gong Dialer is available on Gong Engage; reps dial out of Engage or the mobile app.
- Calls relayed through the vendor's telephony (Gong/Twilio); companies not charged per the relayed call; forwarding numbers (personal/company) for the return leg.
- **Inbound routing**: callbacks routed to the rep's browser and, if set, forwarding number; a callback to a business number is routed to the **last rep who dialed that contact** from that number.
- Pre-recorded **voicemail drop** supported (message-length cutoff exists — detail in notes only).
- International calling with country restrictions; **local dialing** is admin-enabled; rep can manually select which available number to call from.
- **Calls from other dialers can be imported** (Telephony Systems page in admin settings) — but imported calls don't appear in Engage flow steps/reporting.
- **No built-in power dialer**: "if your company uses a power dialer integration such as Nooks or Orum, you can use it alongside Gong to load call tasks from Engage and automatically log call outcomes back to Gong and your CRM." (Direct documentation that the dialer surface and the power/parallel machinery can be separate products.)
- Recording: not automatic by default in US/Canada; **admin sets recording method per country/area code**; reps can pause/stop recording during calls.

## Cross-product Comparison

| Dimension | PhoneBurner | Kixie | Orum | Close | Gong (Engage) |
|---|---|---|---|---|---|
| Packaging | standalone dialer + native contact mgmt | standalone dialer layered over CRMs | standalone AI dialer platform | dialer native inside CRM | dialer module inside CI/engagement suite |
| Where the call list lives | native Contact Manager folders (+ SF integration) | external CRMs (synced) | CRM/SEP-synced | native CRM lead views (Smart Views) | Engage flow tasks + CRM |
| Dialing automation | power dial; pause & preview | multi-line parallel + AI voice detection | parallel dialing + answer detection | click-to-call default; predictive as separate org mode | click-to-call (power via Nooks/Orum integration) |
| Session container | explicit "Dial Session" with settings | Power Dialer session stats | dialing sessions + salesfloor presence | Smart View calling; predictive queue view | flow/task-driven calling |
| Per-call context | contact + script on screen | CRM contact context | prospect context during parallel session | lead page + auto call note | task/flow context |
| Outcome capture | dispositions (configurable sets) + notes + follow-up date | outcomes + calls + texts + recordings auto-logged to CRM | outcomes/recordings flow to CRM/SEP | fixed disposition list + search filters + auto note | outcomes logged to Gong + CRM |
| Voicemail drop | pre-recorded, click (no beep wait) | yes (one click) | not surfaced on fetched pages | pre-recorded (plan-gated), auto note "Left VM" | pre-recorded supported |
| Caller-ID machinery | purchased numbers + verification policy + ARMOR anti-spam | local presence, ConnectionBoost, reputation remediation | number rotation, reputation monitoring | caller-ID selection (verified/number groups, CNAM US) | number provisioning, admin-enabled local dialing |
| Recording | optional per session | automatic (logged to CRM) | recordings flow to systems | opt-in toggle, pause, plan-gated retention | default off (US/CA), admin-configured per region, rep-pausable |
| Compliance surface | dialing-time restrictions, caller-ID verification, spam remediation | DNC registry + internal suppression checks | spam-avoidance (rotation/reputation) | abandonment message (predictive), disposition records | recording methods per country/area code |
| Inbound | Inbound section + click-to-call inbound notes | yes | callback routing emphasis | full inbound (ring, group numbers, inbox, new-lead creation) | browser + forwarding number routing; last-dialer callback routing |
| SMS | SMS section exists | Business SMS | not surfaced | native (CRM) | via Engage |
| Extras beyond dialing | email, LeadStream (lead distribution), appointments, transcription/AI notes | conversation intelligence, analytics | coaching suite, salesfloor, leaderboards | transcription + AI summaries, CQI | conversation intelligence, coaching, deal/forecast suite |

### Stable cross-product findings (Evidence Layer B)

Across all five products:

1. **Calls are made against prospect records.** Every product's call originates from (or is written back to) a record — lead/contact/task — never dialed blind from a keypad as the primary flow (manual dialing exists everywhere as a secondary convenience).
2. **Outcome capture back to the record.** Every product records per-call outcomes (dispositions or equivalent) plus notes, and writes them back — natively (Close) or via CRM/SEP integration (Kixie, Orum, Gong, PhoneBurner).
3. **Outbound is the center of gravity.** All five lead with outbound calling; inbound exists but as a secondary surface (ring/answer/callback routing), much thinner than a contact-center ACD.
4. **The calling session is the work container** — select a list, configure, work through, dispose, next. Surface names differ (Dial Session, Power Dialer session, Smart View calling, queue view, flow tasks) but the container recurs.
5. **Caller-ID/number management is an operating concern** — every product carries machinery for outbound number identity and reputation (verification, local presence, rotation, group numbers).
6. **CRM-adjacent by design** — every product either contains a CRM or names CRM integration as the load-bearing connection (records in, activities out).

### Findings NOT universal (Layer A only or partial)

- Parallel/multi-line dialing: Kixie, Orum (A); predictive: Close (A, separate org mode); power dialing absent from Close's and Gong's default surfaces (A) — automation level is a spectrum, not a requirement.
- Voicemail drop: surfaced in 4/5 (not on Orum's fetched pages).
- SMS/email adjacent channels: surfaced in 4/5.
- Inbound handling: present in all at varying depth (PhoneBurner has a dedicated Inbound section; Close/Gong document full inbound flows), but never the primary surface.
- Coaching/analytics layers: Orum, Gong, Kixie (A); Close offers transcription/summaries (A); PhoneBurner offers transcription/AI notes (A) — depth varies widely.

## Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The individual seller's **live outbound call as the unit of work**, placed **against managed sales records**, with **the call's outcome captured back onto the record**:

```text
Individual seller (the caller is the rep, not a routed agent pool)
└── Managed prospect/sales records (the call list + per-call context source)
    └── Outbound live call placed against a record
        └── Outcome capture (disposition/log) written back to the record
```

- Remove the individual-seller posture (calls routed from queues, campaigns owned by the operation, team-scale pacing/compliance) → Call Center Platform.
- Remove the record binding (no list-of-records semantics, no context, no write-back) → generic Softphone / telephony endpoint.
- Remove the outbound calling center of gravity (multi-channel program where the call is one step type) → Outreach Sequencing / Sales Engagement Platform.
- Remove outcome capture → a click-to-dial utility, not a sales application.

Historical check (§24): older/leaner inside-sales dialers (manual click-to-call era, single-line preview dialing, CRM-embedded "click to dial" add-ons, vertical power dialers) satisfy this L0 without parallel dialing, without voicemail drop, without recording, without SMS, without AI. The L0 deliberately does not include: automation level, recording, voicemail drop, local presence, session analytics, adjacent channels. Passes.

### L1 — Common Mature Structure

Very common across the sampled mature products (Layer B), but not required to recognize the Type:

- the calling session as an explicit work container (list → configure → work → dispose → next)
- dialing automation levels above manual click-to-call (power dial / multi-line parallel / predictive — with AI answer detection at the modern end)
- live-call controls: mute, hold, transfer, dialpad, duration, note-taking during call
- automatic call-activity logging with disposition; manual logging for off-platform calls
- call recording + playback (with pause/consent handling)
- pre-recorded voicemail drop
- caller-ID/number machinery: number selection, local presence, reputation monitoring/remediation
- CRM/sales-system integration as the record + write-back spine
- per-rep activity statistics (dials, connects, talk time)
- light inbound handling (ring surfaces, callback routing, missed-call follow-up)

### L2 — Variant / Optional Structure

Depends on segment, packaging, and era:

- packaging pole: standalone dialer (with/without native records) ↔ CRM-native capability ↔ SEP/suite module ↔ extension over existing telephony
- automation depth (manual-only default as in Close/Gong baseline vs. parallel-first as in Orum/Kixie)
- outbound-only vs. meaningful inbound/callback handling
- adjacent-channel expansion (SMS, email follow-ups, sequences)
- analytics/coaching depth (session stats → conversation intelligence → AI scorecards/salesfloor)
- compliance depth (DNC checks, dialing windows, recording-consent configuration, abandonment messages) — lighter than call-center-grade campaign compliance but present
- vertical tuning (real estate, mortgage, insurance, recruiting list-calling workflows)
- AI posture (answer detection, parallel orchestration, auto-summaries, live assist)

### L3 — Vendor-specific (research notes only)

- PhoneBurner: LeadStream (lead distribution among users), ARMOR (anti-spam-label product name), Connect Score, "Pause and Preview" mode name, transfer agents concept, purchased VPhone numbers.
- Kixie: ConnectionBoost branding, "up to 10 parallel lines" marketing number, carrier/extension packaging details, VoiceBoost.
- Orum: Canceled Calls bucket, millisecond answer-detection claim, Salesfloor/leaderboards, Scout (AI data agents), "1 billion sales calls" training-data claim.
- Close: Smart Views as dial queues, predictive exclusion windows (1h/72h), CQI quality indicators, per-minute Twilio billing model, no warm transfers, primary-contact/primary-number-only automated dialing, CNAM US-only.
- Gong: forwarding-number model, callback-routed-to-last-dialer rule, Telephony Systems import, Nooks/Orum integration pattern, 60-second voicemail cutoff, per-country/area-code recording methods.

## Vendor-specific Findings (kept out of the canonical document)

All L3 items above; plus Close's specific disposition taxonomy (Answered/No answer/Busy/Blocked/Error/Left a voicemail/Directed to voicemail/Abandoned) — product-specific list, useful as an example only. Orum's parallel-dial collision handling (first answer wins, others become canceled calls) is the most articulated current implementation but should not be generalized as the definition of parallel dialing.

## Boundary Findings

1. **vs Call Center Platform** (§07 sibling, processed): the call-center pass recorded this seam; this pass confirms it from the dialer side. Call center = telephony call as unit of contact + ACD distribution to available agents + team-scale campaign machinery (contact lists, pacing modes, DNC suppression at campaign scale) + agent states. Sales Dialer = the individual rep personally conducts the calls against their own/the team's prospect records; queues/agent-states/ACD do not exist; campaign machinery is absent or vestigial (a single rep working a list). The seam is sharpest in Close: enabling predictive mode requires a group caller ID, an abandonment message, and multiple concurrent dialers — at that point the product momentarily behaves like call-center machinery. Individual-rep posture is the discriminator.
2. **vs Sales Engagement Platform / Outreach Sequencing Platform** (§07 siblings, processed): the sequencing pass recorded "the dialer is a channel surface; standalone dialers center the live call." Confirmed: Gong ships its dialer *inside* Engage (flow tasks), Orum's FAQ explicitly positions itself as sitting *alongside* SEPs, and Gong explicitly documents power-dialer integrations (Nooks/Orum) that consume Engage call tasks. Structural test: does the product center the live call (dialer) or the multi-touch program state machine (SEP)?
3. **vs Softphone Application**: a softphone is a generic telephony endpoint for any calls; a sales dialer's calls are record-bound with context and write-back. Kixie's "Contact Center" feature and Close's manual-dial popover show softphone-ish surfaces existing *inside* these products as secondary conveniences — packaging overlap, not structural identity.
4. **vs Conversation Intelligence Platform / Sales Call Coaching Platform** (§07 siblings): CI analyzes recorded calls; coaching develops the seller; the dialer places calls. Gong and Orum bundle dialer + CI/coaching in one suite — commercially blurred, structurally separable (Gong can run with an external dialer; Orum's coaching is a separate module).
5. **vs CRM / Lead Management**: the record store is usually external (CRM) or lightweight-native (PhoneBurner contact manager). List sourcing/prospecting is upstream. A dialer that grows a full pipeline/deal model would be drifting toward CRM; none of the samples do.
6. **Type-status check**: multiple products are marketed and purchased *primarily* as dialers (PhoneBurner, Kixie, Orum), with independent pricing and categories; embedded variants (Close, Gong) are realizations of the same structure in different host containers. Therefore Sales Dialer stands as an independent Type, not a mere capability — but its most common modern packaging is embedded, which should be documented as the packaging pole, not erased.

## Uncertainties

- Orum's deeper session mechanics (per-session configuration objects) could not be verified (product subpage 404); claims rest on the root page + FAQ — treated as A-level but marketing-proximate.
- PhoneBurner's current marketing positioning (403) unverified; help-center evidence is sufficient for structure but not for packaging/pricing posture.
- Kixie's telephony relay model (own carrier stack vs. customer's existing service) was not confirmable from fetched pages; not asserted anywhere.
- Salesloft's dialer (the other flagship SEP dialer) was not directly documented (404); Gong's Engage dialer was used as the suite-embedded sample; SEP-dialer generalizations are therefore anchored on one direct sample + the Gong↔Nooks/Orum integration doc.
- The exact market share of CRM/SEP-embedded vs. standalone dialing is unknown; the final document describes the packaging pole without claiming a dominant form.
- Historical samples (pre-2010 predictive dialer vendors, real-estate power dialers like Mojo) were not fetched; the historical check relies on the structure of the L0 (manual click-to-call satisfies it) rather than direct archival evidence — assertion strength kept moderate.

## Final Synthesis

A Sales Dialer is the individual seller's outbound-calling workstation. Its defining structure is small: an individual seller places live outbound calls against managed prospect records — the record supplies the call list and the per-call context — and every call's outcome is captured back onto the record. Around this core, mature products add a consistent ring: the calling session as a work container, dialing automation (power → parallel/predictive, increasingly AI answer detection), live-call controls, automatic activity logging with dispositions, call recording, pre-recorded voicemail drop, caller-ID/reputation machinery, CRM integration as the record spine, per-rep activity stats, and light inbound/callback handling. The Type is packaged across a pole from standalone products to capabilities embedded in CRMs and engagement suites; the call-first, individual-rep, record-bound posture — not the packaging — is what makes it a Sales Dialer. It ends where calls become queue-routed team operations (Call Center Platform), where the call becomes one step in a multi-touch program (SEP/Outreach Sequencing), where calls lose their record binding (Softphone), and where recorded calls are primarily analyzed rather than placed (Conversation Intelligence).
