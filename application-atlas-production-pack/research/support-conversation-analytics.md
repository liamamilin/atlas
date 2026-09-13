# Research Notes — Support Conversation Analytics

## Research Goal

Understand the Application Type the directory calls **Support Conversation Analytics** (§07 Sales, Customer & Revenue, listed between Contact Center Quality Management and Remote Customer Support Platform): what the product family actually consists of in the market, what its defining structure is, how it works, and where its boundaries sit against the two already-processed siblings (Conversation Intelligence Platform, Contact Center Quality Management) and its neighbors (Customer Service Platform, CCaaS, Voice of Customer, BI).

Market naming observed: this family is sold as **interaction analytics**, **speech analytics**, **text analytics**, **contact center analytics**, **CX analytics**, and — increasingly — **conversation intelligence (for contact centers)**. The directory leaf name describes the function (analytics over support conversations); the market names describe the technology or the category wave.

## Initial Boundary

Working hypothesis before research:

1. Core use: analyze recorded/transcribed customer–service conversations at scale to answer "what are customers contacting us about, what is driving experience/cost/risk".
2. Users: contact center leaders, CX/insight analysts, quality/compliance teams, plus downstream business stakeholders.
3. Nearest neighbors: Contact Center Quality Management (per-agent evaluation), Conversation Intelligence Platform (sales corpus), Customer Service Platform reporting, Voice of Customer, BI.
4. Likely seam: org-scale conversation insight (no evaluated population, no scored standard) vs per-agent evaluation; service population vs sales population.
5. Unknowns: whether the corpus leg requires native capture or ingestion counts; how the topic/category model is configured; whether real-time is core or extension; how platform-native analytics (inside CCaaS/help desk) relates to standalone products.

Both prior sibling passes left explicit advance notes for this leaf:
- conversation-intelligence-platform (2026-09-07): "CI was defined population-neutral over recorded external conversations with the sales/revenue corpus as the dominant realization; the contact-center interaction-analytics lineage (1990s–2000s) satisfies the same machinery with service populations — apply the population/purpose split (service-operations analytics vs agent-QA evaluation workflow vs sales corpus insight); real-time contact-center products (Balto-class) blend the poles."
- contact-center-quality-management (2026-09-07): "seam flagged for unprocessed sibling support-conversation-analytics: per-agent evaluation vs org-scale conversation insight (topics/trends/VoC signals, no evaluated population, no scored standard); MaestroQA's QA-company→'conversation data platform' repositioning shows the families converging at the data layer while QA workflows remain the action layer."

## Research Questions

1. What is the analyzed subject — which channels and artifacts (calls, chats, emails, tickets, social, surveys)?
2. How do conversations enter the system — native recording, platform integrations, transcript ingestion?
3. What structure is derived per conversation — transcription, topics/intents/categories, sentiment, metrics?
4. How is the analysis configured — predefined phrase models, out-of-the-box categories, AI-defined concepts, auto-discovery?
5. What aggregate surfaces exist — dashboards, reports, search, alerts, trend/root-cause views, NL query?
6. Who consumes the insight and for what decisions?
7. How does the analytics layer relate to quality management, coaching, and VoC in the same vendors?
8. What governance machinery exists (redaction, access, retention)?
9. Where are the boundaries — vs QM, vs CI, vs platform reporting, vs VoC, vs BI?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Tier | Why sampled |
|---|---|---|---|
| Verint (Interaction Analytics; Speech Analytics; Text Analytics) | enterprise workforce-engagement suite; speech+text analytics lineage | enterprise | the classic enterprise category leader; also absorbed Calabrio (consolidation evidence) |
| NICE (AI Interaction Analytics, CXone) | enterprise CX platform suite (Enlighten AI) | enterprise | the other enterprise suite pole; explicit Essentials/Advanced packaging |
| CallMiner (Eureka — Analyze/Visualize) | independent pure-play conversation analytics | mid-market→enterprise | the pure-play pole; Forrester Wave leader for CI for contact centers |
| Genesys Cloud (Speech and Text Analytics) | CCaaS-native module | enterprise cloud | platform-native realization with rich Tier-1 help-center documentation |
| Zendesk (Analytics, with AI intent insights) | help-desk/service-suite-native | SMB→enterprise | service-suite-native pole; also a boundary probe (operational reporting vs conversation structure) |

Rejected/considered: Talkdesk (Interaction Analytics) — unreachable (4 URL attempts, 404s); Balto/Observe.AI/Level AI — real-time agent-assistance pole, blends toward QM/CI (noted, not sampled); Medallia/InMoment — VoC-platform pole, different Type; ZoomInfo Chorus/Gong — sales corpus, already covered by the CI pass.

## Sources

Research date: 2026-09-08. All Layer A unless noted.

- Verint — Interaction Analytics product page + FAQ — https://www.verint.com/interaction-analytics/
- Verint — Speech Analytics product page + FAQ — https://www.verint.com/speech-analytics/
- NICE — AI Interaction Analytics product page + FAQ — https://www.nice.com/products/interaction-analytics
- CallMiner — Eureka platform page — https://callminer.com/products/eureka/
- CallMiner — Analyze product page — https://callminer.com/products/analyze
- Genesys Cloud Resource Center — Speech and text analytics overview — https://help.mypurecloud.com/articles/speech-and-text-analytics-overview/
- Genesys Cloud Resource Center — About programs, topics, and phrases — https://help.mypurecloud.com/articles/about-programs-topics-and-phrases/
- Zendesk — Analytics (service) product page — https://www.zendesk.com/service/analytics/ (reached via /explore/ redirect)
- Sibling documents: applications/conversation-intelligence-platform.md, applications/contact-center-quality-management.md, applications/customer-service-platform.md

Failed/unreachable: Talkdesk (talkdesk.com/platform/interaction-analytics/, /products/interaction-analytics, /platform/explore/, /contact-center/interaction-analytics/ — all 404); NICE /products/nexidia-analytics, /products/speech-analytics (404; the /products/interaction-analytics path succeeded); Verint /service/interaction-analytics/, /products/interaction-analytics/ (404; /interaction-analytics/ succeeded); Zendesk /service/platform/explore/, /service/ticketing-support-analytics/, /service/ai/intelligent-triage/ (404; /service/analytics/ succeeded via redirect).

## Product Observations

### Verint — Interaction Analytics / Speech Analytics / Text Analytics (Layer A)

- Vendor's own definition (FAQ): "Interaction analytics is the process of using AI, NLP, and speech/text analysis to convert unstructured customer conversations (calls, chats, emails) into structured data. This allows businesses to extract insights, detect trends, analyze sentiment, and improve customer experiences, agent performance, and operational efficiency."
- Vendor's own mechanism description (FAQ): "Interaction analytics captures customer conversations across channels, transcribes them, and uses AI to analyze language, tone, emotion, intent, and uncover customer issues. The data is categorized into themes, emotions, or actions to surface hidden issues and opportunities for performance improvement."
- Definition of the parent category (contact center analytics software): "captures and analyzes every customer interaction across your channels, transforming unstructured conversation data into structured intelligence… identifies patterns in customer sentiment, agent behavior, emerging topics, and operational trends that manual review would never surface."
- Explicit connection to action workflows: "connect those insights directly to the workflows where action happens, including quality management, agent coaching, compliance monitoring, and CX improvement."
- What it reveals (product page): analyze every channel in one place; unified view of speech and text data; built-in alerts ("notify you the moment interaction data signals a problem… can also be used to trigger automated actions"); sentiment drivers ("Surface the topics and behaviors behind your sentiment trends, then dig into root causes. See which interaction categories, agent behaviors, or product issues are responsible and track whether the actions you take are working"); coaching opportunities ("By tracking negative changes in sentiment for specific employees…").
- Channels (FAQ): voice calls, live chats, emails, social media messages, SMS, agent desktop activity (Verint-specific extension).
- Users (FAQ): contact centers, CX teams, compliance officers, quality assurance teams, sales and support managers.
- Product family: Verint CX Intelligence (unified omnichannel analytics), Verint Speech Analytics ("market-leading speech analytics from 100% of recorded calls"), Verint Text Analytics (web chat, email, social media, call notes; chat-specific metrics incl. average handle time, sentiment, message count; "can separate interactions into employee and customer streams"; "out-of-the-box adapters to automatically ingest and analyze chat conversations from a variety of vendors"), Verint Data Insights Bot (natural-language search over CX data; "automatically surfaces trends, anomalies, and correlations across interaction, experience, and workforce data"; real-time dashboards).
- Speech Analytics page: "automatically discover and analyze words, phrases, categories, and themes"; "surfaces insights from 100% of voice interactions, helping your teams quickly identify inefficiencies, coaching opportunities, compliance issues, and revenue drivers"; unified visual player ("combines transcripts, emotions, topics, screen recordings, and QA evaluations in a single view"); "Pinpoint what is driving handle time, silence, holds, and repeat contacts. Surface process inefficiencies, knowledge gaps, and technical failures so you fix root causes, not symptoms"; "Automatically extracts issues, service gaps, competitor mentions, and emerging customer needs"; "Identify what drives conversions, surfaces objections, and flags missed upsell opportunities"; bot family (Exact Transcription, Genie [NL Q&A over unstructured data], PII Redaction, Sentiment, Playback Summary).
- FAQ distinctions: speech analytics (voice) vs text analytics (written) vs interaction analytics (both, unified); real-time speech analytics as a distinct mode ("processes voice interactions as they happen… live agent guidance, in-call next-best-action prompts, and immediate supervisor alerts").
- Consolidation: "Calabrio is Now Verint" banner (Calabrio Conversation Intelligence now a Verint solution).
- Marketing outcome figures ($3M revenue, 10% capacity, 90% transcription accuracy) treated as vendor claims — excluded from canonical claims.

### NICE — AI Interaction Analytics (Layer A)

- Positioning: "NiCE Interaction Analytics surfaces root causes and trends, so you know what's driving CX, cost and performance — faster." "Stop relying on sampled data and guesswork. NiCE Interaction Analytics analyzes every conversation."
- Four headline capabilities: reveal what customers feel ("sentiment, customer intents, and agent soft-skill behaviors… with speech and text analytics powered by AI at scale"); act on root causes proactively ("Quickly spot what's driving repeat contact, churn, or poor CSAT — Copilot flags the cause with proof from real conversations"); improve quality and compliance ("Monitor 100% of interactions and prioritize coaching opportunities, identify compliance issues, and accelerate quality evaluations automatically"); boost productivity at scale ("Help managers, analysts, and QA teams focus on outcomes while AI surfaces outliers and prioritizes what to fix").
- Channels (FAQ): "every type of customer interaction from voice call analysis to text to digital, including social… applies advanced analysis such as automatic speech recognition (ASR) or speech analytics, natural language processing (NLP), machine learning (ML), transcription, sentiment analysis, and industry-specific gen AI models to any channel."
- Pre-built metrics (FAQ): First Call Resolution, Frustration ("detects language that signals customer frustration"), Silence ("measures the duration of non-engagement"), Sentiment ("for both the agent and the customer").
- AutoDiscovery: "surfacing new patterns and themes by clustering unknown topics and showing how they're connected — offering AI customer interaction insights you didn't know to look for."
- Topic AI: "combines the latest generative AI LLM technologies with purpose-built, industry-specific AI models to analyze every interaction for intents, actions and outcomes and then categorize the results into a hierarchy. You can enrich the AI models with your own CX data to align with your organizational processes and terminology."
- Dashboards (FAQ): "unified view of your CX data, all in one customizable user-friendly dashboard… the intent analysis widget allows users to view metrics associated with the intents of calls, such as Total Interactions, Average Duration, Average Silence, Total Interactions %, Positive Client Sentiment, Negative Client Sentiment, Outcomes"; "Ask Analytics LLM conversational chat window to easily search and filter interactions… identify metrics, trends, performance outliers and even find that 'needle in the haystack'… without requiring analytics expertise."
- Reporting (FAQ): "Role-based out of the box and customizable dashboards… Tracking a full omnichannel view of call and chat analytics; Providing real-time insights to act on issues as they happen; Analyzing historical data for early insights into performance trends; Addressing complex business challenges with interactive drill-down views to uncover root causes."
- Packaging: Interaction Analytics Essentials vs Advanced tiers (Advanced adds AutoDiscovery, Topic AI Intent/Activity Models, Copilot for Analytics); add-on modules (CSAT soft-skill behaviors; Sales Effectiveness); also bundled in Complete/Ultimate suites.
- Suite context: listed under "Workforce Empowerment" beside Workforce Management, Quality Management, Performance Management, Recording Management, Feedback Management; Related Products: Feedback Management, Quality Management, Performance Management.

### CallMiner — Eureka (Analyze / Visualize) (Layer A)

- Platform frame: "Capture, analyze and automate customer interactions at scale"; four layers — Capture (Record, Screen Record, Redact), Intelligence (Analyze, Visualize), Augmentation (Coach, RealTime), Automation (Outreach, OmniAgent). "Capture and analyze 100% of omnichannel interactions."
- Analyze page: "Harness AI and ML to automatically uncover insights from 100% of your interactions in the contact center and beyond"; "Go beyond the contact center to harness… omnichannel capabilities and capture customer data from 100% of interactions across all channels"; "Uncover trends, build prediction models and identify the most impactful insights"; "Break down silos and democratize data by routing insights to the departments and leaders who need them."
- Key features: omnichannel ingestion (text and voice); robust API ("route data to your platforms and repositories"; "connect customer insights to CRM, BI tools, data lakes"); advanced transcription ("hundreds of languages… or bring your own transcription engine"); AI-driven analytics ("uncovering trends, building prediction models"); easy data visualization ("Visually represent the entire customer journey. Drill-down details reveal insights into customer behaviors, agent performance, process challenges and other root cause indicators"); organization-wide alerting ("raising alerts regarding critical feedback. Shorten the time to act"); customizable dashboards and reports ("Individual and supervisor dashboards"); secure redaction ("Auto redact sensitive data including PCI DSS and custom entities"); contact summarization ("automatic AI and topic-based summarization").
- Analysis mechanics: "Look beyond text search by sentiment analysis of voice and text"; "Reveal unexpected topics and trends within conversations using customizable searches or pre-built analytics content"; "Discover related terms and phrases to identify trends"; "Unsupervised ML offers insights necessary to predict NPS scores, anticipate customer churn and likelihood to buy."
- Pre-built content: Solution Catalogue ("Pre-built, customizable scores, indicators and other analytics").
- Category framing: self-described "global leader in AI-powered conversation intelligence and customer experience (CX) automation"; Forrester Wave "Conversation Intelligence Solutions for Contact Centers, Q2 2025" leader badge. (Confirms the naming convergence with the CI sibling.)

### Genesys Cloud — Speech and Text Analytics (Layer A, Tier-1 help center)

- Definition (help center): "Speech and text analytics is a set of features that uses natural language processing (NLP) to provide an automated analysis of an interaction's content, to provide insight into customer-agent conversations. Speech and text analytics includes the transcription of voice interactions, analysis for customer sentiment and topic spotting, to create meaning from otherwise unstructured data."
- Use cases: "agent performance improvement (for example, decrease AHT, increase FCR, sales conversion, and so on), compliance, customer satisfaction (for example, NPS), and customer business intelligence."
- Key features: voice transcription and digital transcripts ("internal participant can be an IVR, voice bots, ACD, agent, conference or voicemail… For digital interactions (for example, email, message, or chat) the internal participant can be bots or agents"); customer sentiment analysis ("Recognize a customer's attitude during an interaction based on the language used"); topic spotting ("Detect topics of interest within conversations that are relevant to the business. For example, customer contact reasons, customer experience indicators, or expected agent behaviors based on a set of predefined phrases. A number of Out-of-the-box topics are provided"); interaction overview ("visual representation of the voice or digital interaction that enable agents and supervisors to review… play, pause, annotate, live monitoring, adjust volume and speed, sentiment and topic markers"); content search ("Search for interactions based on the content of the interaction including words or phrases, customer sentiment and topics detected"); analytics views ("View aggregated data from speech and text in agent, queue and flow views").
- Timing: "analysis is performed against the interaction immediately after it is completed. However, if voice transcripts are needed with lower latency, it is possible to subscribe to transcripts through the Notifications API."
- Getting started: "you must first enable voice transcription or select a default expected dialect for digital interactions."
- Topic model (programs/topics/phrases article): "Topics are a collection of phrases that indicate a business level intent… topics help boost the recognition of the programed words and phrases in voice transcription and lists them as events in the interaction overview." "Programs are a package of topics that instruct speech and text analytics what business level intents to look for in recorded conversations… Programs can also control customer sentiment analysis and agent empathy analysis for interactions associated with the program." "Phrases are a string of words that outline the various ways in which a topic can be expressed. Phrases can be added one by one, or in bulk using the file upload option." Topic Miner: "mine topics and phrases, import topics from a JSON file, and create new or update existing topics from mined data." Purpose: "automatically tag interactions for specific business level intents that subsequently provide analytics about the customer's and agent's motivations and goals during the interaction." Permissions required for topic/program administration.

### Zendesk — Analytics (service) (Layer A)

- Positioning: "Reporting and analytics: Turn service insights into better outcomes… Optimize operations with intuitive, flexible insights."
- Capabilities: out-of-the-box insights (prebuilt dashboards/templates, "no analyst required"); custom reports ("customize every report and dashboard—or ask questions in your own language with quick reports"); share/export ("secure email, link, or export"); unified data ("complete view of your service activity with unified data across channels and teams… with your human and AI agents"); trends ("historical reporting and prebuilt dashboards, helping you anticipate demand"); real-time monitoring; quick reports ("describing the insights you want in simple, natural language").
- Conversation-derived layer: "AI insights dashboard showing detected intents, reply time, top intents, languages, and enrichment by channel" (AI agent and copilot analytics section).
- Customer evidence (HotDoc): "By setting up dashboards on Zendesk Explore, we're actually able to hone in on why customers are contacting us, and the tickets that need the most focus."
- Boundary-relevant: WFM and QA analytics are separate surfaces ("Zendesk WFM and QA analytics… spot quality gaps"); the analytics product is largely operational reporting (volumes, resolution times, CSAT, agent activity) with the AI-intent layer as the conversation-structure component. This makes Zendesk the thin pole of the sample and a useful boundary probe against pure service reporting.

## Cross-product Comparison

| Dimension | Verint | NICE | CallMiner | Genesys Cloud | Zendesk |
|---|---|---|---|---|---|
| Corpus channels | voice + chat + email + social + SMS + desktop | voice + text + digital + social | voice + text omnichannel + surveys | voice (IVR/bots/ACD/agent/conference/voicemail) + email/message/chat | tickets/chats/calls across service channels |
| Transcription | own transcription engine (bot-named) | ASR + industry-specific gen AI models | own recognizer or bring-your-own | native transcription engine | n/a for text; voice via platform |
| Derived structure | words/phrases/categories/themes, sentiment, emotions | intents, actions, outcomes hierarchy; sentiment; soft-skill behaviors; AutoDiscovery clusters | sentiment/emotion tags, topics/trends, prediction models | topics (phrase-based), sentiment, events in interaction overview | AI-detected intents, languages, enrichment |
| Configuration model | categories/themes + bots; adapters for ingestion | pre-built + custom AI models, enrichable with own data | customizable searches + pre-built Solution Catalogue | programs ⊃ topics ⊃ phrases; out-of-the-box topics; Topic Miner | prebuilt dashboards + custom reports; AI intents automatic |
| Aggregate surfaces | dashboards, root-cause views, alerts, Data Insights Bot NL Q&A | role-based dashboards, drill-down, Ask Analytics LLM | Visualize dashboards, journey views, alerts | analytics views (agent/queue/flow), content search | dashboards, trends, quick reports (NL) |
| Alerts | built-in alerts trigger actions/workflows | Copilot flags causes | organization-wide alerting | (via APIs/notifications) | (via monitoring) |
| Per-conversation surface | unified visual player (transcript+emotion+topics+screen+QA) | proof from real conversations | drill-down to single agent/customer | interaction overview with playback/annotation | drill into tickets |
| Privacy | PII Redaction Bot | (not detailed on page) | Redact (PCI DSS + custom entities) | (permissions on topics/programs) | (enterprise security posture) |
| Real-time | real-time speech analytics as distinct mode | "real-time insights to act on issues as they happen" | RealTime module (separate product) | post-completion norm; Notifications API for lower latency | real-time monitoring dashboards |
| QM relationship | feeds quality management workflows; separate Quality Automation product | "accelerate quality evaluations"; separate QM product | Coach module separate; QM solution separate | programs can control "agent empathy analysis"; QM separate | QA separate product |
| Packaging | suite modules (Speech/Text/CX Intelligence) + bots | Essentials/Advanced tiers + suite bundles | standalone platform, modular | CCaaS platform feature | service-suite analytics product |

Cross-product commonalities (Layer B):
1. All five hold a multi-channel corpus of customer–service conversations as the analyzed population.
2. All five derive machine structure per conversation (transcription where voice; classification — topics/intents/categories — and sentiment in all).
3. All five aggregate across conversations into dashboards/reports with drill-down to individual conversations.
4. All five expose search over conversation content (words/phrases/sentiment/topics) — Genesys and CallMiner name it explicitly; NICE via Ask Analytics LLM; Verint via Genie Bot; Zendesk via report filters/quick reports.
5. All five connect insight to action workflows (QM, coaching, compliance, CX improvement) without themselves being the evaluation system.
6. 4/5 expose alerts on detected signals (Genesys documents notifications/API instead on the fetched pages).
7. 4/5 expose AI summaries or NL query over the corpus (Zendesk's quick reports is NL reporting rather than corpus Q&A).
8. 3/5 document configurable topic/category models with organization-specific enrichment (Genesys programs/topics/phrases; NICE enrichable AI models; CallMiner customizable searches + pre-built catalogue); Verint documents categories/themes + ingestion adapters; Zendesk's structure layer is automatic (AI intents) with dashboards configurable.
9. 3/5 document PII/sensitive-data redaction as a named capability (Verint, CallMiner; NICE not on fetched page; Genesys not on fetched pages).
10. 2/5 document prediction models (churn/NPS/conversion) explicitly (CallMiner, NICE churn-risk framing).

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (three jointly-held structures)

1. **The support conversation corpus of record.** The system's subject is the service operation's customer conversations — voice calls, chat/messaging threads, emails/tickets — captured or ingested as recordings, transcripts, or message content, and held as a persistent, identified, analyzable population. Remove → a recording vault / ticket archive with playback, no analytics.

2. **Machine-derived conversation structure.** Each conversation is processed into structured, queryable understanding: transcription with speaker separation for voice, and derived classification over the content — topics/intents/categories, sentiment, computed signals — turning unstructured conversation into data. Remove → raw recordings/transcripts with no analysis; the "analytics" is gone.

3. **Cross-conversation insight for the service operation.** The corpus is aggregated into org-scale surfaces — dashboards, reports, content search, alerts, trend and root-cause views — answering what customers contact about, which drivers are trending, and what is driving sentiment, cost, compliance exposure, and revenue opportunity. The consumer is the service operation and the wider business. There is no evaluated population and no scored standard (that is QM's structure). Remove → per-interaction review tooling (QM territory) or raw data export (BI territory).

Jointly-held is load-bearing:
- 1 alone = recording/ticket archive
- 2 without 1 = one-shot transcription/NLP utility with no standing corpus
- 3 without 1+2 = generic BI over operational metadata (volumes, SLAs, CSAT) — service reporting, not conversation analytics
- 1+2 without 3 = per-conversation review surface (the QM/review shape)
- 2+3 without 1 = analytics over imported/sample data with no standing corpus (thin pole; not observed as a product shape in the sample)

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Omnichannel ingestion breadth (voice + chat + email + SMS + social + tickets; adapters/connectors for third-party platforms)
- Speaker-separated transcription with accuracy machinery (custom vocabularies; bring-your-own transcription in one product)
- Configurable topic/category models: predefined phrase sets, out-of-the-box categories, AI-defined concepts, and auto-discovery of unknown themes
- Sentiment/emotion analysis computed per participant stream (customer vs agent)
- Pre-built metrics (first-contact resolution, frustration, silence, handle-time drivers)
- Content search over the corpus (words, phrases, topics, sentiment)
- Dashboards and reports with drill-down from aggregate to the underlying conversation
- Alerts on detected signals, routed to owners, sometimes triggering workflows
- Root-cause/driver analysis (what is behind sentiment shifts, repeat contact, handle time)
- AI summaries per conversation
- PII/sensitive-data redaction
- APIs/exports to CRM, BI tools, data lakes; integrations with contact center and help desk platforms
- Natural-language query over the corpus or over reports
- Playback surface with synced transcript and sentiment/topic markers (the drill-down endpoint)

### L2 — Variant / Optional Structure

- Packaging: standalone pure-play platform vs workforce-engagement-suite module vs CCaaS-native feature vs service-suite (help desk) native product
- Coverage posture: automated analysis of all interactions vs sampled analysis (the market's own framing: "stop relying on sampled data" implies sampled is the legacy posture)
- Real-time extension: live guidance, in-call prompts, supervisor alerts (blends toward agent-assistance/QM real-time)
- Predictive layer: churn risk, NPS prediction, likelihood to buy, conversion drivers
- VoC-program framing: conversation analytics operated as the organization's VoC engine
- Industry packs: financial-services compliance analytics, healthcare, collections, insurance
- Agent soft-skill/behavior analytics (empathy, ownership) — leans toward QM/coaching consumption
- Native recording capability (own recorder, screen recording) vs ingest-only
- Desktop/process analytics adjacency (one vendor)

### L3 — Vendor-specific (Research Notes only)

- Verint: bot naming (Exact Transcription Bot, Genie Bot, PII Redaction Bot, Sentiment Bot, Playback Summary Bot), CX Data Hub, Da Vinci AI, Data Insights Bot, desktop/process analytics, Calabrio consolidation ("Calabrio is Now Verint"), Hazel business-analyst persona marketing.
- NICE: Enlighten AI framing, Topic AI, AutoDiscovery, Ask Analytics LLM, Copilot for Analytics, Essentials/Advanced tiering, CSAT and Sales Effectiveness add-on modules, "25B+ interactions a year" claim.
- CallMiner: Eureka platform name, module names (Analyze, Visualize, Coach, RealTime, Outreach, OmniAgent, Redact, Record, Screen Record), Solution Catalogue, Open Voice Transcription Standard (OVTS), Forrester/SPARK Matrix leader badges.
- Genesys: programs/topics/phrases hierarchy, Topic Miner, interaction overview, out-of-the-box topics list, agent empathy analysis control at program level, Notifications API.
- Zendesk: Explore heritage name, quick reports, AI insights dashboard (detected intents/top intents/languages), WFM/QA analytics surfaces, HotDoc/GloFox/DutchBros testimonials.

## Vendor-specific Findings

- The category's market vocabulary is converging on "conversation intelligence": CallMiner self-describes as "conversation intelligence and CX automation" and badges a Forrester wave named "Conversation Intelligence Solutions for Contact Centers"; Verint markets "Calabrio Conversation Intelligence" and is cited (DMG) for "conversation analytics"; NICE names the product "AI Interaction Analytics". The directory's CI leaf (sales corpus) and this leaf (service corpus) therefore share a marketing word but hold different populations/purposes — the seam must be drawn on population/purpose, not vendor vocabulary.
- Verint's FAQ explicitly distinguishes speech vs text vs interaction analytics — useful canonical vocabulary: the medium-specific products (speech analytics, text analytics) are specializations; interaction/conversation analytics is the unified form.
- Genesys documents the deepest topic-model mechanics (programs ⊃ topics ⊃ phrases, bulk phrase upload, topic mining, permissions) — the best Tier-1 evidence for how the "define what to look for" layer works.
- NICE and Verint both sell the analytics layer in tiers/bundles beside their QM products — evidence that analytics and quality management are separate products even inside one suite.
- Zendesk shows the thin pole: a service-suite analytics product that is mostly operational reporting with an AI-intent layer — the boundary probe against "service reporting".

## Boundary Findings

1. **vs Contact Center Quality Management (processed).** QM's defining core is the evaluated agent population + interaction records + the evaluation form (defined standard) + the evaluation record. SCA has no evaluated population and no scored standard: agent-level figures appear as aggregate insight (e.g., sentiment by agent), not as evaluations bound to a standard with calibration and appeals. The same vendors ship both as separate products (Verint Interaction Analytics vs Quality Automation; NICE Interaction Analytics vs Quality Management; CallMiner Analyze vs Coach/QM solution; Zendesk Analytics vs QA). Remove the corpus-understanding layer and keep forms+scores → QM; remove forms+scores and keep corpus+structure+aggregate → this Type. Seam held; both Types stand.

2. **vs Conversation Intelligence Platform (processed).** Same machinery family (capture → transcript → derived signals → corpus → aggregate). Seam = population + purpose: CI's canonical center is the sales/revenue conversation corpus (calls/meetings, CRM-linked, revenue questions); this Type's is the service conversation corpus (contact center + support desk) and service-operations questions (contact drivers, cost, CX, compliance exposure, VoC signals). Contact-center-tuned CI products (Balto-class, per the CI pass) blend the poles. Market naming convergence noted above — flag for the taxonomy owner (see STATUS entry).

3. **vs Customer Service Platform / Cloud Contact Center (both processed).** The platform runs the operation (queues, routing, agent workspace) and reports on its own operational data (volumes, SLAs, CSAT). SCA's distinguishing layer is machine-derived structure over unstructured conversation content, often across systems, and its consumer is insight-driven rather than operations-console-driven. When the analytics layer ships inside the platform (Genesys Cloud, Zendesk), it is the same Type realized as a platform-native module — packaging, not Type identity.

4. **vs Voice of Customer Platform.** VoC's unit of record is the solicited survey/metric response; SCA derives signals from unsolicited service conversations. They interlock: NICE lists Feedback Management as a related product; CallMiner ships survey/outreach modules; Verint pairs speech analytics with voice surveys in case studies. Conversation analytics is increasingly marketed as the VoC engine for the unsolicited channel.

5. **vs Business Intelligence Platform.** BI reports over arbitrary data sources it does not understand; SCA is conversation-native — it captures/transcribes/derives the structure it reports on, and exports to BI/data lakes rather than replacing them. The thin pole (Zendesk-style operational reporting) shows what SCA collapses into if the machine-derived structure leg is removed.

6. **vs Customer Feedback Management (processed).** CFM's unit of record is the feedback item about the product, attributed to customers, aggregated into demand signals. SCA's unit is the service conversation; feedback-relevant signals (feature requests, complaints) are read out of the corpus but not managed as a feedback-to-decision pipeline.

7. **vs speech/text analytics as raw technology.** ASR/NLP/sentiment are capabilities; the Type is the productized application over the service conversation corpus with its configuration layer, insight surfaces, and governance. No directory leaf exists for the raw technology; no action needed.

8. **Historical / market-sample check.** The 2000s speech-analytics deployment shape — recorded calls transcribed (or phonetically indexed), categorized into topics, reported as top contact drivers to contact center leadership — satisfies all three L0 structures without GenAI, cloud delivery, real-time analysis, or omnichannel breadth. The text-side thin ancestor — agent-categorized ticket volume/trend reports — holds the corpus and aggregate legs but its categories are human-assigned, not machine-derived: it fails leg 2 and sits below the Type (it is what service reporting still is). The voice-side manual call-monitoring sample report is QM's ancestor, not this Type's. The sampled products' own framing ("stop relying on sampled data and guesswork", "manual call studies that took weeks") corroborates the lineage without needing unreachable historical vendor docs. No current-era capability (GenAI summaries, NL Q&A, real-time, prediction) is required by the definition.

## Uncertainties

- Talkdesk's Interaction Analytics product could not be fetched (4 URL attempts); the CCaaS-native pole is covered by Genesys instead. Talkdesk-specific claims: none made.
- Verint and NICE help-center bodies were not reachable this pass; their evidence is product-page + FAQ level. Operational mechanics (exact configuration flows, tier boundaries beyond what pages state) are asserted only where directly observed (Genesys help center).
- Zendesk's conversation-structure layer is thin (AI intents dashboard); claims about Zendesk are limited to what its analytics page states.
- Historical vendors (Nexidia, pre-consolidation Verint/NICE speech analytics) not directly fetched; the historical check is structural inference corroborated by the sampled products' own category-evolution framing.
- Coverage claims ("100% of interactions") are vendor marketing framing for the automation posture; the definition treats coverage as a configuration posture, not an invariant.
- Numeric details (transcription accuracy percentages, language counts, interaction volumes) excluded as marketing claims.

## Final Synthesis

Support Conversation Analytics is the service-operations member of the conversation-analytics family: it holds the service operation's customer conversations as a standing analyzable corpus, derives structure from each conversation (transcription, topics/intents, sentiment), and aggregates the corpus into org-scale insight — contact drivers, experience drivers, cost drivers, compliance exposure, and customer-voice signals — for service leaders, CX teams, and the wider business. Its three-part defining core (corpus of record + machine-derived structure + cross-conversation insight) separates it from recording archives (no structure), from one-shot transcription utilities (no corpus), from service reporting (no machine-derived conversation structure), from quality management (no evaluated population, no scored standard), and from the sales-side conversation intelligence sibling (different population and purpose). Everything else the market ships — omnichannel breadth, auto-discovery, prediction, real-time, NL query, redaction, VoC framing — is standard or optional machinery layered on that core.
