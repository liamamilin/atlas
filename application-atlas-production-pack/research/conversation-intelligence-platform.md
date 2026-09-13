# Research Notes — Conversation Intelligence Platform

Date: 2026-09-07
Directory leaf: Conversation Intelligence Platform (§07 Sales, Customer & Revenue, between Sales Dialer and Sales Call Coaching Platform)
Slug: conversation-intelligence-platform

Joint-review obligations carried into this pass (discharged in Boundary Findings):
1. research/ai-meeting-assistant.md flagged "ai-meeting-assistant vs conversation-intelligence-platform: gradient, not a wall — primary object (single-meeting record + immediate use vs org-scale analytics/coaching over many recorded calls); flagged for joint review when CI is processed."
2. research/sales-call-coaching-platform.md flagged "sales-call-coaching-platform vs conversation-intelligence-platform: sharpest seam in the family — working split = primary object/end product (managed seller-development loop vs org-scale conversation analytics/market insight as the end product); flagged for joint review."

## Research Goal

Understand what a Conversation Intelligence Platform actually is as a software Type: what it captures, how it turns conversations into machine-readable and analyzed assets, what surfaces exist to work with one conversation vs the whole corpus, who uses it, and where its boundaries sit against the crowded neighbor family (coaching, meeting assistants, recorders, revenue intelligence, dialers, contact-center QA).

## Initial Boundary

Initial hypothesis: a sales-tech system that records customer-facing sales calls, transcribes them, analyzes content (keywords, topics, talk-time, objections), and aggregates the corpus into searchable libraries and team/org-scale insight for managers and leaders.

Neighbors to separate from:
- Sales Call Coaching Platform (§07 sibling) — same machinery, seller-development end product
- AI Meeting Assistant (§03.10) — same capture+transcription, single-meeting unit
- Meeting Recording & Transcription Application (§03.10) — verbatim record only
- Revenue Intelligence Platform (§07) — consumes conversation signals; end product is the revenue model
- Sales Dialer (§07) — places the calls that CI analyzes
- Call Center Platform / Cloud Contact Center (§07) — the calling operation itself
- Contact Center Quality Management (§07, unprocessed) — same evaluation machinery over support-agent populations
- Support Conversation Analytics (§07, unprocessed) — same analytics family over support conversations
- Sales Intelligence Platform (§07) — external market data vs internal conversation data

The leaf name is generic ("Conversation Intelligence"), but the directory places it in the Sales section. A key question: is the Type definition population-neutral (any recorded customer conversation corpus) with sales as the dominant market realization, or sales-only? Contact-center "interaction analytics" products (1990s–2000s lineage) share the machinery — this drives the §24 historical check.

## Research Questions

1. How do conversations enter the system? (integration types, bots, native recording, telephony, calendar scanning, email)
2. What does the platform do to a captured conversation? (transcription, speaker attribution, analysis layers)
3. What is the single-conversation work surface? (player, transcript, comments, snippets, summaries)
4. What is the corpus surface? (search, folders, streams, libraries, playlists)
5. What aggregation exists? (team/rep dashboards, initiative tracking, market intelligence, deal views)
6. How does it link to the CRM, and which system is the record of what?
7. Who uses it and for what decisions? (rep, manager, enablement, RevOps, exec, product/marketing)
8. What governance exists? (consent, per-user scope, privacy, redaction, retention)
9. What fails? (capture exceptions — bot not admitted, consent denied, lobby timeout)
10. Where does the Type end — coaching, RI, meeting assistant, recorder, contact-center QA?

## Representative Products

Selection logic: market archetype + different packaging poles + different customer tiers + different philosophies; documentation accessibility weighted.

| Product | Pole | Tier | Evidence level |
|---|---|---|---|
| Gong | Category archetype; CI heritage expanded into revenue platform | Enterprise | Tier 1 — help center rich, machine-readable index (help.gong.io) |
| Jiminny | Mid-market CI pure-play (G2 Conversation Intelligence Mid-Market Leader badge) | Mid-market | Tier 1 — Intercom help center fetchable + product pages |
| Salesloft (Conversation Intelligence module) | CI embedded in a sales engagement/revenue platform; "system of action" philosophy | Enterprise/mid | Tier 2 — product page only (help center JS-rendered) |
| Balto | Real-time conversation machinery applied to contact centers (agent assist, 100% QA auto-scoring) | Contact center / BPO | Tier 2 — product pages + FAQ |
| ZoomInfo Chorus | Data-suite-acquired CI; large installed base | Enterprise | NOT reachable (403 on zoominfo.com; chorus.ai redirects there) — market context only, no structural claims made from it |

## Sources

- Gong: https://help.gong.io/ (index), /docs/understanding-call-recording, /docs/view-a-call-transcript, /docs/understanding-trackers, /docs/find-conversations-and-organize-the-library, /docs/intro-to-insights, /docs/market — fetched 2026-09-07
- Jiminny: https://www.jiminny.com/ , /product/conversation-intelligence , https://help.jiminny.com/en/ (index), /en/articles/14136168-understand-why-meetings-and-calls-are-not-recorded — fetched 2026-09-07
- Salesloft: https://salesloft.com/platform/conversation-intelligence-software — fetched 2026-09-07 (product page; FAQ section included)
- Balto: https://balto.ai/ — fetched 2026-09-07 (product page + FAQ)
- ZoomInfo Chorus: zoominfo.com/products/conversation-intelligence and /products/chorus → 403; knowledge.zoominfo.com unreachable; chorus.ai redirects. Attempted twice; abandoned per source-access rules.

Source-access limitation: ZoomInfo Chorus could not be examined at all; Salesloft evidenced at product-page level only; Balto is a contact-center AI platform (used to evidence the machinery's population variants, not the sales-canonical structure).

## Product A — Gong (Tier 1, evidence layer A unless noted)

### Capture
- Conversations enter via integrations: web-conferencing providers and telephony systems; email/calendar connected at admin level (Google Workspace / Outlook). Gong scans calendars to identify meetings that should be recorded; eligible meetings are imported; after the meeting ends, recording, transcript, and AI insights are available.
- Admin controls: which calls are recorded, whose calls are recorded, how consent is obtained, which providers are supported.
- Internal vs external classification is derived from meeting participants; internal meetings recorded only if configured.
- Two recording methods: native recording through the conferencing platform (no extra participant), or a "Gong assistant" virtual participant that records the call when native is unavailable. Method chosen automatically by company settings.
- Manual recording: inviting the assistant; explicitly does NOT override consent enforcement or a user's "never record" setting.
- Meetings that are not recorded (physical rooms, unsupported providers) may still appear with metadata (date/time/participants) but no recording.
- Consent: dual (all-party) consent with explicit (verbal agreement) or implicit (informed and remained) modes; consent behavior configured at company level; regional-law dependent.

### Transcript
- Auto-transcription; transcript appears alongside recording, synced with audio; click a line to jump; search within transcript; select text to create snippet / share / comment / add to library; translation (per-user, on demand or automatic); download; custom vocabulary to improve accuracy. Transcripts are "the foundation for many AI-powered features".

### Analysis layer (trackers & metrics)
- Trackers identify words, phrases, or concepts in calls AND emails. Two kinds: keyword trackers (literal terms) and smart trackers (AI models identifying concepts even when phrased differently — e.g. trained on "asking for a discount", detects "Is that the best you can do?"). Out-of-the-box "By Gong" trackers exist. Trackers are workspace-scoped.
- Tracker outputs surface in: search filters, call summary emails, Team insights, Initiative boards, deal boards, Win/Loss analysis. Alerts/streams can be configured when tracked elements appear.
- Team insights metric families: Team (call volume, avg duration, total customer time), Interaction (talk ratio, longest monologue, interactivity score, question rate), Responsiveness (email response rate/time), Topics (admin-configured topic models + duration), Trackers (% of calls mentioning), Scorecards (avg score per question), Gong usage (calls listened/commented/scorecards — engagement with the platform itself), Coaching received (distribution of feedback/comments across team).
- Initiative boards: track adoption of strategic initiatives (new messaging, methodology, product launch) via trackers, with adoption goals, over time, by team/individual.
- AI Theme Spotter: automatically identifies recurring patterns/themes across customer conversations ("collective customer voice").
- Market (Insights > Market): trend lines from trackers over time (pre-trained Economic Pulse tracker detecting economy concerns); breakdowns by team/individual; drill into the underlying calls/snippets; win/loss correlation ("how many deals closed when Economic Pulse terms were not mentioned").

### Corpus & library
- Search with "100+ filters" (vendor-stated count): participants, account name (from CRM), words/phrases, trackers, call title. Saved searches.
- Streams: saved filter sets that automatically collect matching calls and notify (Slack/email); standard (visible to all) vs personalized (own+teammates' calls).
- Folders: personal library vs company library (enablement-managed, organization-wide, training/onboarding materials). Snippets can be saved to library.
- Calls and conversations data exposed via API/tables; integrations (Snowflake etc.).

### Deals (adjacent layer — Gong as revenue platform)
- Deal boards, deal likelihood scores, deal drivers, AI Deal Monitor/Reviewer; CRM sync. This is the Revenue Intelligence expansion (see Boundary Findings #5) — the CI core is the conversation layer feeding these.

## Product B — Jiminny (Tier 1 for capture governance + analysis inventory; product pages for positioning)

### Positioning (product pages, layer A for Jiminny-specific claims)
- "Conversation and revenue intelligence platform that captures emails, phone and video calls, provides insights that win deals and syncs them to your CRM."
- Product split: AI Notetaker (capture) / Conversation intelligence (analysis+coaching+intel) / GTM intelligence (revenue/pipeline). Features: call recording, transcription, sales coaching, CRM logging, competitor intelligence, pipeline management.
- "Ask Jiminny": AI Q&A on any call or multi-call deal (next steps, how/why won) — includes "Panorama" (portfolio-level). AI CRM Filling. Proactive deal insights & alerts (risks, stalled deals, missing next steps). Team performance benchmarking.

### Help center (layer A)
- Full collection inventory confirms structure: Dashboard; Data-Driven Coaching; AI Call Scoring; Ask Jiminny (call/deal/Panorama); Playback (meeting transcription, download, share recordings, share conversation, engagement stats, coaching focus, mark call private, delete recordings, snippet a call, private comments, switch speakers); Salesforce App; OnDemand (saved searches, recording uploader — upload external recordings; searching conversations; nudges); Live Coaching (in-call, video); Playbooks & Coaching Frameworks; Key Words Scoring (setup + concept); Transcription/Summaries/Themes/Topics (custom themes+topics creation, AI summaries & action items, transcription language selection, custom vocabulary, language detection); Team Insights (conversations charts; why-not-recorded); Deal Insights (deal risks setup, CRM field management, email sync to deal insights); Playlists; mobile app; in-person meeting recording via app.
- Capture exception taxonomy (Recording Outcomes CSV, Team Insights → Conversations → Conferences): Recorded / Bot denied from lobby / Lobby timeout / Bot kicked / Recording not allowed (Zoom local-recording or consent not given) / User disabled the recording / Recording was stopped / Login required / Wrong URL / Invalid meeting link / Consent denied by customer / Other; plus dialer-specific outcomes (server error, access denied, setup issue, empty recording). Managers use outcomes to spot patterns and follow up.
- Two-party consent recording options article exists; "Should you announce call recording" guidance exists.

## Product C — Salesloft Conversation Intelligence (Tier 2, product page only)

- "automatically records, transcribes, and analyzes every sales call" (FAQ). "Ours captures insights, syncs workflows, automates follow-ups, and gives reps structured data" — "system of action" positioning (CI layered into seller workflows).
- Slide-deck claims: AI call summaries; smart chapters; AI action items by attendee; speaker talk-time analysis; generate follow-up email draft from call context; automated CRM updates; stakeholder sentiment, objections, engagement signals; buying-group AI insights; objection tracking across the pipeline; automatic call scoring; deal-risk visibility; real-time AI guidance during calls (live coaching cards triggered by keywords like "Discount"); battlecards surfacing in real time; feeds buyer signals into forecast.
- Vendor-articulated boundaries (FAQ): CI vs call recording ("Recording tells you what happened. Conversation intelligence tells you what to do next."); CI vs sales intelligence ("Sales intelligence focuses on external data... Conversation intelligence captures what happens inside your actual deals").
- Login URL (copilot.clari.com) confirms the Clari merger absorption; module named "Conversation Intelligence" (formerly Conversations) — consistent with the sales-call-coaching pass.

## Product D — Balto (Tier 2, contact-center pole)

- Self-positions as "Contact Center AI Software": agent assist (real-time answers/prompts/compliance checklists during calls), QA automation ("Evaluate 100% of interactions with AI and replace sampling"), Insights ("Every customer interaction is analyzed to surface clear signals, reveal patterns at scale"), Coaching (AI recommendations linked to outcomes), real-time compliance monitoring with audit trail, real-time PII scrubbing (SSN), real-time notetaker/summaries, omnichannel continuity, voice AI agents (separate product line, Togo).
- Integrations are contact-center telephony (Five9, NICE inContact, Genesys, RingCentral, Convoso, 8x8) + Salesforce.
- Reading: the capture→transcribe→analyze→aggregate machinery with real-time guidance emphasis, applied to a contact-center (service/sales-mixed) population. Blends into Contact Center Quality Management and agent-assist territory. Used here to evidence variant machinery, NOT to define the sales-canonical Type.

## Product E — ZoomInfo Chorus (NOT reachable)

- 403 on both zoominfo.com product paths; knowledge center unreachable; chorus.ai redirects to zoominfo. No structural observations recorded. Chorus's market role (large enterprise CI, acquired into a data-intelligence suite) is common market knowledge and is used only as context, with zero structural claims derived from it.

## Cross-product Comparison

| Dimension | Gong | Jiminny | Salesloft (CI) | Balto |
|---|---|---|---|---|
| Capture channels | web conferencing + telephony + calendar scan + email import | phone (incl. own dialer/voice) + video (Teams etc.) + emails + in-person app | "every sales call" | contact-center telephony platforms |
| Capture mechanism | native recording OR assistant bot (auto-chosen) | bot/notetaker + telephony-side recording; recording uploader for external files | not documented at reachable level | platform integration w/ phone systems |
| Consent machinery | consent profiles (dual/explicit/implicit), admin-governed, regional | two-party consent options; consent-denied is a recorded outcome; announce-recording guidance | not documented | real-time compliance monitoring + PII scrubbing (PCI/HIPAA) |
| Transcript | synced, clickable, searchable, translatable, custom vocab | synced, language detection, custom vocab, speaker switching | yes (assumed from summaries/chapters claims — B-level) | real-time transcription (implied by assist) |
| Concept/keyword layer | keyword trackers + AI smart trackers + By-Gong library; alerts | Key Words Scoring; custom Themes & Topics; competitor intelligence | objection tracking, stakeholder sentiment (marketing-level) | auto-scored interactions, pattern surfacing |
| Conversation metrics | talk ratio, longest monologue, interactivity, question rate, volume, duration | engagement stats | talk-time analysis | QA/scorecards |
| AI summaries/actions | AI briefs, AI Deal Monitor etc. | AI Summaries & Action Items; Ask Jiminny | AI call summaries, action items, follow-up emails, smart chapters | real-time notetaker summaries |
| Corpus surfaces | search 100+ filters, streams, folders, personal+company libraries, snippets | saved searches, playlists, snippets, sharing | searchable conversations | insights dashboards |
| Aggregate insight | Team/Interaction/Responsiveness/Topics/Trackers/Scorecards/Usage/Coaching insights; Initiative boards; AI Theme Spotter; Market trends | Team Insights, Dashboards, Automated Executive Reports | team adoption dashboard; deal-risk visibility | "patterns at scale", QA analytics |
| Deal linkage | deal boards/likelihood/drivers (RI layer), CRM sync | Deal Insights, deal risks, AI CRM filling, Salesforce app | automated CRM updates, buyer signals to forecast | Salesforce integration |
| Real-time guidance | (not a Gong emphasis at reachable level) | Live Coaching (video calls) | live coaching cards, battlecards | core emphasis (agent assist) |
| Population | sales/revenue orgs | sales/revenue orgs (mid-market) | sales orgs | contact centers |

Convergent structure (evidence layer B): capture-by-integration → automatic transcription → organization-configured analysis (keywords/concepts/topics/metrics) → searchable corpus with sharing/collaboration over moments → aggregate dashboards → CRM association. Every directly-examined product exhibits this spine.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (remove any one → different Type)

1. **The recorded conversation as the captured unit of record.** Conversations with external parties (calls, video meetings; email in several products) are captured by the platform itself through integrations with the communication tools the organization already uses — the corpus assembles itself as a byproduct of normal selling; users do not manually author it. Remove → CRM activity log / generic BI.
2. **The machine transcript as analysis substrate.** Each captured conversation becomes speaker-attributed machine-readable text. Remove → call-recording storage / telephony record (audio library without intelligence).
3. **Derived conversation signals computed over the corpus.** Organization-configured concepts/keywords/topics and conversation metrics are computed on transcripts (not merely stored). Remove → Meeting Recording & Transcription Application (verbatim record for human reading only).
4. **Org-scale corpus access and aggregation.** The corpus of many conversations is searchable as a whole and aggregated into team/org-level views. Remove (unit = single meeting record for immediate use) → AI Meeting Assistant.

### L1 — Common Mature Structure (evidence layer B across sample)

- CRM association: conversations auto-associated to accounts/deals/contacts; call logging/outcome sync; the CRM remains the record system for customer/deal data while the platform owns the conversation corpus.
- The conversation detail page: recording player + synced transcript + speakers + AI summary + tracker/topic hits + metrics, with per-moment actions (comment, snippet, share, add to library).
- Collaboration over moments: timestamped comments, snippets, sharing, exemplar libraries (company-level enablement content built from real calls).
- Saved searches / streams / folders / playlists; notifications when tracked elements or matching conversations appear.
- Trackers: keyword and AI-concept variants; organization-defined; surfaced in search, alerts, and dashboards.
- Team/rep dashboards: volume, talk-time, question rate, topics, tracker prevalence; rep-vs-peer comparison.
- AI summaries, action items, follow-up drafting.
- Capture governance: admin-configured scope (who/what is recorded), consent profiles/announcements, private marking, deletion/retention.
- Deal/portfolio views fed by conversation signals (risk alerts, stalled-deal flags) — embedded in CI products at varying depth.

### L2 — Variant / Optional Structure

- Email as a first-class analyzed channel (Gong A-level: trackers run on calls and emails; Jiminny captures emails; others emphasize calls only).
- Real-time in-call guidance (coaching cards, battlecards, agent assist) — strong at Salesloft/Balto poles; not present as emphasis in all products.
- Market-intelligence trend boards over tracked concepts (Gong Market — single-product direct evidence, L2).
- Strategic-initiative adoption tracking with goals (Gong — single-product direct evidence, L2).
- Buying-group/stakeholder analytics (Salesloft marketing-level).
- Auto call scoring (Jiminny AI Call Scoring A-level; Salesloft FAQ; Balto 100% QA — different population).
- Portfolio-level AI Q&A (Jiminny Panorama; Gong deep research — B-level/emergent).
- In-person meeting capture via mobile app (Jiminny; Gong metadata-only import for physical meetings — different depth).
- Multi-language transcription/translation.
- Contact-center population tuning: agent-assist + QA auto-scoring + compliance machinery (Balto pole; neighbors Contact Center Quality Management / Support Conversation Analytics).

### L3 — Vendor-specific (research notes only)

- Gong: "By Gong" pre-trained trackers; Economic Pulse tracker; AI Theme Spotter; Initiative boards; workspaces; Gong credits usage model; deal likelihood scores; Enable/Enable Essentials packaging; MCP server/clients; Snowflake integration.
- Jiminny: Ask Jiminny / Panorama; Key Words Scoring; Sidekick browser extension; OnDemand; recording-outcome taxonomy names; GTM Intelligence product line; 14-day trial.
- Salesloft: Rhythm; "system of action" positioning; Signals; Clari merger login topology; battlecards; 20+ hours saved per week (vendor claim, unverified).
- Balto: Togo voice AI agent; real-time SSN scrubbing; 20-language list; "Go Fast with Balto".

## Rejected Findings (considered and NOT promoted)

- "AI summaries define the Type." → First-generation CI (2013–2016) had no LLM summaries; summaries are L1-era features, not invariant. The transcript + derived signals are the substrate.
- "Real-time guidance is part of CI." → Only some products (Salesloft, Balto); most evidence is post-call. L2.
- "Email analysis is definitional." → Emphasized in 2 of 4 directly-examined products; not universal. L1/L2 boundary; kept out of core.
- "Deal views / likelihood scores define CI." → That is the Revenue Intelligence expansion (Gong, Salesloft, Jiminny all grew it); the CI leaf's end product is conversation understanding, not the revenue model. Kept as L1 deal-linkage only.
- "The Type is sales-only." → Contact-center interaction analytics share the L0 machinery (Balto pole; the 1990s–2000s interaction-analytics lineage). The canonical definition is population-neutral over recorded external conversations, with the sales/revenue corpus documented as the dominant market realization and neighboring leaves holding the support/QA variants.
- "Scorecards are CI." → Scorecards evaluated against a seller-development loop are Sales Call Coaching machinery; in CI they appear as embedded modules (Gong Scorecard insights). The machinery crosses products; the end product distinguishes the Types.

## Boundary Findings

| Neighbor | Relationship | Distinction (remove what → becomes the other) | Status |
|---|---|---|---|
| AI Meeting Assistant (§03.10) | gradient — shared capture layer | Assistant's unit = one meeting's record for immediate participant use (summary, notes, action items); CI's unit = the org's corpus of many conversations aggregated into insight. Fireflies bundles CI-style analytics (per that pass); Zoom sells CI as a separate line. Gradient acknowledged both sides. | Joint-review flag DISCHARGED — both leaves stand. |
| Sales Call Coaching Platform (§07) | sharpest seam — shared machinery | CI's end product = org-scale understanding of conversations/market (what is happening); coaching's end product = the managed seller-development loop (who improves, tracked coaching activity). CI products embed coaching modules (Gong scorecards/coaching insights) and coaching platforms embed analytics — boundary by primary job/end product, not features. | Joint-review flag DISCHARGED — both leaves stand. |
| Meeting Recording & Transcription Application (§03.10) | upstream layer | Remove derived signals (verbatim transcript only, for later human use) → that Type. | consistent with ai-meeting-assistant pass |
| Meeting Notes Application | orthogonal | No capture; human authors notes. | per ai-meeting-assistant pass |
| Revenue Intelligence Platform (§07) | consumer relationship | RI's primary object = the revenue model over CRM-mirrored deals + captured engagement; CI's primary object = the conversation corpus. Conversation analysis inside RI is captured signal. Consistent with RI pass ("coaching is CI's end product → standalone Type"; "RI consumes conversation analysis"). | aligned |
| Sales Dialer (§07) | execution vs analysis | Dialer places record-bound calls; CI analyzes the resulting recordings. Suite bundling (Gong dialer+CI) is commercial, not structural. | consistent with dialer pass |
| Call Center Platform / CCaaS (§07) | operation vs analysis | The call center routes/distributes and hosts the calling operation; CI analyzes recorded conversations (may ingest from it). | aligned with call-center pass lineage |
| Contact Center Quality Management (§07, unprocessed) | same evaluation machinery family, different population/criteria | QM evaluates support-agent interactions against service-quality/compliance criteria with calibration/dispute workflow; CI (this leaf) centers the corpus + org insight over (dominantly) sales conversations. Balto demonstrates the blending at the contact-center pole. | note recorded for that pass |
| Support Conversation Analytics (§07, unprocessed) | sibling in the conversation-analytics family | Same machinery, support/service population and service-operations purpose; this leaf's canonical center is the sales/revenue conversation corpus. | note recorded for that pass |
| Sales Intelligence Platform (§07) | data domain | External market/firmographic/intent data vs internal recorded-conversation data (vendor-articulated by Salesloft FAQ; kept as B-level support). | noted |
| Business Intelligence Platform (§13) | generic vs conversation-native | BI connects arbitrary sources to dashboards; CI carries conversation-native capture/transcription/signal machinery the corpus depends on. | structural |

## Historical / Market-Sample Check (§24)

- First-generation CI products (2013–2016 era: Chorus.ai, ExecVision, early Gong) shipped call libraries, transcripts, keyword/concept analytics, and team dashboards without modern LLM summaries — they satisfy the L0. The definition is not overfitted to the current AI layer.
- Contact-center interaction analytics (NICE/Verint-class lineage, 1990s–2000s) already did record + transcribe + search + aggregate across orgs — they satisfy the population-neutral L0 machinery with a service population. This is why the definition is written over "recorded external conversations" rather than "sales calls"; the sales/revenue corpus is the dominant modern realization and the directory's neighbor leaves (Contact Center Quality Management, Support Conversation Analytics) hold the service-side variants.
- Pre-software practice: managers listening to taped sales calls with paper evaluation forms. Fails machine-transcript + derived-signal tests — correctly the practice the Type organizes, not an earlier form of the Type.
- Regional/platform check: the definition does not depend on any conferencing vendor, telephony stack, bot mechanism (native recording satisfies it), CRM, or language.

## Uncertainties

1. ZoomInfo Chorus entirely unreachable (403s) — no structural observations; canonical claims rest on the four reachable products. Market-share-weighted statements avoided.
2. Salesloft operational mechanics rest on the product page (FAQ + slide claims); help center is JS-rendered and was not readable. Claims about Salesloft kept at marketing-proximate strength and never load-bearing for the canonical core.
3. Whether email-analysis depth is growing into a defining expectation cannot be settled from this sample (2 of 4 emphasize it).
4. The exact prevalence of real-time guidance in the CI category is unverified beyond the two poles where it was observed.
5. "100+ filters" is a vendor-stated count (Gong) — recorded here, excluded from the final document.
6. Precise consent-mode names (explicit/implicit) are Gong-specific documentation; other products document consent differently (Jiminny: two-party options; consent-denied outcomes). The final document phrases consent generically.
7. Interaction-analytics heritage (NICE/Verint-class) is reasoned context, not directly fetched this pass.

## Final Synthesis

A Conversation Intelligence Platform is a system that assembles an organization's recorded external-conversation corpus by capturing calls (and in some products emails/meetings) through integrations with its communication tools; converts every captured conversation into a speaker-attributed machine transcript; computes organization-configured signals over that corpus (tracked words and concepts, topics, conversation metrics, AI summaries); and serves both the single conversation (player, transcript, moments, sharing) and the whole corpus (search, libraries, streams) plus aggregate views (team/rep dashboards, initiative and market trend boards, deal-risk signals) — with conversations auto-associated to CRM records while the CRM remains the customer-data system of record and the platform the corpus system of record.

The defining core is four-part: captured conversation of record; machine transcript; derived conversation signals; org-scale corpus access and aggregation. Mature products add the CRM spine, moment-level collaboration, exemplar libraries, AI summaries/actions, and capture governance. Variants concentrate in: email depth, real-time guidance, market/initiative boards, auto-scoring, portfolio AI Q&A, and population tuning (sales-dominant vs contact-center poles). The Type ends where: the unit becomes a single meeting (AI Meeting Assistant), the end product becomes seller development (Sales Call Coaching), the end product becomes the revenue model (Revenue Intelligence), calls are placed rather than analyzed (Sales Dialer), or the transcript stops being analyzed (Meeting Recording & Transcription).
