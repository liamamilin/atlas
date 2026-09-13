# Research Notes — Expert Q&A Platform

Research date: 2026-09-07
Slug: expert-q-a-platform
Directory leaf: Expert Q&A Platform (§02.03 Answering & Research)

---

## Research Goal

Understand what an Expert Q&A Platform is as an Application Type: what its defining structure is, how a question becomes an expert answer, who the actors are, how the exchange is governed (vetting, payment, trust), and where its boundaries lie against Q&A Community, Answer Engine, Tutoring, Expert Network, and Telehealth.

## Initial Boundary

Working hypothesis at start:

- Core purpose: a person with a specific, situation-bound question gets an answer/advice from a vetted expert, mediated and monetized by the platform.
- Users: askers (consumers or professionals), experts (vetted individuals), platform operators (vetting, moderation, payments, disputes).
- Nearest neighbors: Q&A Community (01.06), Answer Engine / Knowledge Question Answering Application (02.03 siblings), Tutoring Platform (23), Service Marketplace (05.02), Telehealth (22), Customer Support (07).
- Known ambiguity: the directory has no "Expert Network" leaf; enterprise expert networks (GLG / Guidepoint / Maven class) may or may not belong inside this Type.

## Research Questions

1. What is the unit of record — a question, a consultation, a call, an engagement?
2. How are experts vetted and represented (credential profile, verification)?
3. How does a question reach an expert (category routing, directory selection, staff/AI matching)?
4. What is the session lifecycle (submitted → routed → answered → follow-up → closed/rated → archived)?
5. How is the exchange monetized (per-question, per-minute, subscription/membership, enterprise retainer)?
6. What trust machinery exists (ratings, guarantees, refunds, privacy, compliance)?
7. Where are the Type boundaries (crowd Q&A, algorithmic answering, tutoring, expert networks, telehealth, support)?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| JustAnswer | consumer pay-per-question, broad categories | largest consumer expert-Q&A brand; blocked to fetch — kept as named representative with reduced evidence |
| Clarity.fm | expert-call marketplace (business advice) | reachable Tier-1 docs; call-based exchange variant |
| Experts Exchange | tech Q&A with expert answers + subscription | tech-vertical hybrid; blocked to fetch — kept as named representative with reduced evidence |
| HealthTap | health vertical (doctors) | reachable Tier-1 docs; shows Q&A machinery inside a telehealth product (drift example) |
| Guidepoint | enterprise expert network | reachable Tier-1 docs; boundary pole for the expert-network question |
| Maven | enterprise expert network platform | reachable Tier-1 root; second boundary-pole data point |

PrestoExperts was considered and dropped (fetch timeout).

## Sources

Fetched 2026-09-07 (Layer A unless noted):

- Clarity — https://www.clarity.fm/ (root, JS shell), https://www.clarity.fm/how-it-works , https://www.clarity.fm/help (index), /help/articles/2/how-does-clarity-work , /help/articles/29/expert-standards , /help/articles/50/are-the-calls-off-the-record-and-private , /help/articles/15/what-is-your-refund-policy
- Guidepoint — https://www.guidepoint.com/ (root), /company/faqs/ , /services/1-to-1-calls/
- Maven — https://maven.co/ (root; help.maven.co timed out)
- HealthTap — https://support.healthtap.com/ (help index), /hc/en-us/articles/360035455991-What-is-HealthTap
- JustAnswer — https://www.justanswer.com/ and https://help.justanswer.com/ both returned 403 (not examined)
- Experts Exchange — https://www.experts-exchange.com/ returned 403 (not examined)
- Pearl.com (JustAnswer corporate brand) — 403 (not examined)

Source-access limitation: the consumer pay-per-question pole (JustAnswer, Experts Exchange) could not be examined directly. Claims about that pole are kept at reduced strength and marked below as "not directly examined in this pass". No precise operational details for those products are asserted anywhere.

---

## Product A — Clarity.fm (Layer A, strong)

Positioning: "On Demand Business Advice" — entrepreneurs connect with experienced professionals for advice calls.

Key observations:

- **Roles**: Member (asks) and Expert (answers, gets paid); one account can be both. Personal identity is mandatory — "Some people try and create business accounts on Clarity. That's not how we work... Real people and reputation is the key."
- **Expert profile**: areas of expertise, professional bio, ratings and reviews from other members. Experts apply to join; "Expert standards" article defines seven standards (accuracy of profile, respond within 24 hours, availability, commitment, punctuality, helpfulness, leave reviews within 30 days).
- **Exchange flow (call variant)**: browse/search expert directory → "Request a Call" with a short reason, estimated call length, 3 suggested time slots, card added for authorization (not billing) → expert has 72 hours to respond (confirm a slot, propose alternatives, or cancel; requester can keep proposing times) → confirmation email + SMS with conference line and access code; up to 8 team members may join; personal phone numbers are not shared → call happens → member billed automatically after the call at the expert's per-minute rate based on actual time used → member leaves rating and review.
- **Trust machinery**: ratings/reviews; refund policy — full refund if the call hasn't taken place ("no questions asked"); refunds for completed calls are conditional (platform must be allowed to contact the expert; no suspicion of fraud). Marketing claim "99% of calls completed with 5-star rating" (vendor claim, not independently verified).
- **Privacy posture**: "Clarity calls are completely off the record and treated as private"; no NDA required; conflict-of-interest disclosure encouraged during the call.
- **Other surfaces**: inbox messaging between member and expert; help topics for payments & fees (service fee, exporting earnings, pricing advice), "what if I can't find an expert", screen/document sharing explicitly not supported.
- **Rules of conduct**: community etiquette guidelines (open-mindedness, punctuality, no selling/hawking, preparation, authenticity).

Interpretation: the unit of record is a scheduled advice call bound to a request; the platform mediates discovery, scheduling, payment, and reputation. The "answer" is delivered live rather than as text, but the structure (specific request → vetted expert → addressed advice → recorded transaction → rating) is the same as text Q&A.

## Product B — Guidepoint (Layer A, strong)

Positioning: "Global Expert Network & Research Platform" for research teams (institutional investors, corporations, banks, consulting).

Key observations:

- **Demand shape**: an organization starts from a hypothesis/decision, reviews existing research, defines information gaps, and submits a research brief (topic, decision objective, target industries/companies/geographies/roles, unresolved questions).
- **Matching**: dedicated project teams + "agentic AI matching" over a proprietary knowledge graph surface a shortlist; the client reviews and approves the final experts inside Guidepoint360. Calls can be arranged "within hours".
- **Expert pool**: 1.75M+ vetted professionals (2M+ claimed on homepage), 300+ industries; recruitment driven by live client demand (15,000+ new experts/month); "Every expert undergoes identity verification, conflict screening, and ongoing eligibility review."
- **Exchange**: 1-to-1 calls led by the client; optional recording, multilingual transcription, AI summaries at no cost; transcripts stored in Guidepoint360 or delivered via API; third-party/AI moderation available so the client need not attend.
- **Compliance**: customizable compliance controls, structured training, dedicated oversight, real-time transparency; compliance function led by a former senior SEC enforcement counsel; conflict screening is structural.
- **Adjacent formats**: surveys, moderated interviews, custom engagements, a Transcript Library (120k+ transcripts, compliance-reviewed), AskGP (AI answers grounded in the client's authorized expert content with traceable attribution).
- **Monetization**: enterprise engagement (trial/contract; per-engagement economics not published on fetched pages).

Interpretation: this is the enterprise pole. The demand unit is a project brief, not a single asker question; the unit of record is an engagement/call + transcript treated as a research asset; governance is compliance-grade. It shares the L0 skeleton (specific information need → vetted expert → addressed response → recorded) but the workflow, buyer, and governance differ enough to treat it as a boundary pole rather than the Type's center.

## Product C — Maven (Layer A, root page only)

Positioning: "Expert Network — Human Intelligence. On Demand. At Scale."

Key observations:

- Research offerings: Expert Interviews (1:1 with vetted experts), Surveys (credentialed panels), AI-Moderated Interviews, Consulting Projects (scoped SOW), B2B Panel licensing; HITL AI services (RLHF, evaluation); licensing (Expert Exchange interconnection, OpenITM internal talent marketplace, Branded Expert Network private-label).
- Platform decomposition (vendor-published): apps (project authoring, search & matching, scheduling, live calls, transcription, AI summarization, AI question sets, report generation) over a MavenX engine (compliance, conflict management, AI matching, search, payments, content management, self-service) drawing on one vetted network (1M+ experts, 220+ countries, <24hr average fulfillment).
- Open Projects marketplace: posted projects that network experts can pick up; experts apply to join the network and earn compensation for sharing knowledge.
- Help center (help.maven.co) timed out — expert-side operational detail not examined.

Interpretation: confirms the expert-network pole's shape (brief → match → engagement → transcript/report) and shows the same machinery being licensed/white-labeled — evidence that the machinery (vetted pool + matching + engagement + payment + compliance) is a reusable structure, independent of any one vendor.

## Product D — HealthTap (Layer A, strong)

Positioning (2024-dated help article): "the only virtual primary care practice available everywhere in the U.S." — i.e., the product has drifted to telehealth, but the classic expert-Q&A machinery is still documented as member capabilities:

- "Search HealthTap's library of **member-asked, doctor-answered questions** on any health-related topic or symptom" — a public Q&A archive generated by the platform's own exchanges.
- "Ask their own **anonymous question** and get an answer from a **real doctor in hours**" — asker anonymity as a first-class option; response-time expectation stated qualitatively ("in hours").
- Doctor network: "90,000 U.S.-licensed, board certified doctors in 147 different specialties" — vetting = licensure + board certification; specialty taxonomy = routing dimension.
- AI-powered symptom checker alongside the human Q&A — algorithmic answering as a front door, human expert answer as the governed exchange.
- The rest of the product is scheduled clinical care: video visits with the first available doctor, treatment plans, prescriptions, lab orders, insurance.

Interpretation: two valuable findings. (1) The Q&A archive ("member-asked, doctor-answered") is a real, documented pattern — past exchanges become a searchable public knowledge asset. (2) The drift boundary is visible inside one product: when the exchange becomes a scheduled clinical encounter with prescriptions, it is a Telehealth Platform; the Q&A remains a capability of it. HealthTap is therefore a boundary/drift sample, not the Type's center.

## Product E — JustAnswer (NOT directly examined)

- Root and help center returned 403 on 2026-09-07. Named as the canonical consumer pay-per-question representative (broad categories: medical, legal, mechanical, veterinary, tech; verified experts; satisfaction guarantee; public Q&A archive) — these characteristics are widely reported but were **not verified from official sources in this pass**; the final document does not assert any precise JustAnswer mechanics.

## Product F — Experts Exchange (NOT directly examined)

- Root returned 403. Named as the tech-vertical representative (subscription + expert-answered tech questions). Same evidence limitation as JustAnswer.

---

## Cross-product Comparison

| Dimension | Clarity (call marketplace) | Guidepoint / Maven (expert network) | HealthTap (vertical health) | JustAnswer / Experts Exchange (not examined) |
|---|---|---|---|---|
| Demand unit | call request with reason + time slots | research brief / project | member question (anonymous option) | question (reported) |
| Expert pool | self-applied experts, profile + reviews | vetted professionals, identity + conflict screening | licensed, board-certified doctors | verified experts (reported) |
| Routing | asker browses/searches directory, picks expert | platform team + AI matching, client approves shortlist | specialty taxonomy / first-available | category routing (reported) |
| Exchange surface | scheduled live conference call | scheduled live call (+ surveys, moderated formats) | text Q&A thread + video visits | text Q&A thread (reported) |
| Response-time expectation | 72h to accept; 24h communication standard | "within hours" to shortlist | "in hours" to answer | not examined |
| Record | private call + rating/review | engagement + transcript (research asset, compliance-reviewed) | private answer + public archive library | private answer + public archive (reported) |
| Payment | per-minute after call; card authorized upfront | enterprise engagement | membership/insurance + visits | per-question / subscription (reported) |
| Trust machinery | ratings, conditional refunds, etiquette rules | compliance program, conflict screening, eligibility review | licensure, anonymity, symptom-checker front door | guarantee (reported) |
| Governance posture | community guidelines, off-the-record privacy | compliance-grade (SEC-counsel-led program) | medical/regulatory posture | not examined |
| Buyer | individual member (prosumer) | organization/research team | consumer member | consumer |

## Canonical Model (synthesis)

The stable skeleton across all poles:

```text
Asker's specific question/request
  → routed/matched to a vetted expert (platform-mediated selection)
    → addressed expert answer/advice (text thread or live call, follow-up possible)
      → recorded exchange (private record and/or archived knowledge)
        → governed by trust machinery (vetting, ratings, guarantees, payment, privacy/compliance)
```

## L0 — Defining Invariant (minimal)

1. **A specific question/request from an asker** — situation-bound demand for expert judgment, not a generic topic lookup and not a standing service relationship.
2. **A vetted expert pool** — identified individuals whose domain expertise the platform curates/verifies (credential profile); answering is restricted to this pool rather than the open crowd.
3. **Platform-mediated routing/matching** — the platform determines which expert(s) receive the question (directory selection, category routing, or staff/AI matching).
4. **An addressed expert answer** — a personalized response to the asker's specific situation, attributed to the named expert, delivered through the platform (text or live), with follow-up exchange typical.
5. **A recorded exchange** — the Q&A/consultation is retained as a record (private to the asker, and/or archived as searchable knowledge).

Remove the vetted pool + addressed answers → Q&A Community (crowd answers) or Answer Engine (algorithmic). Remove routing → generic contact form. Remove the record → ephemeral chat. Remove the question→answer transaction in favor of scheduled learning → Tutoring. Make the unit expert time under an organizational project brief → Expert Network (boundary pole).

## L1 — Common Mature Structure

- Expert profile surface: bio, credentials/specialties, ratings & reviews (Clarity A; Guidepoint/Maven A — vetting + profiles; HealthTap A — licensure/specialties).
- Ratings and reviews of experts (Clarity A; Guidepoint/Maven A — rating experts is part of the platform loop; HealthTap — doctor ratings exist in product, not fetched directly).
- Payment machinery with a platform fee: per-question, per-minute, membership, enterprise engagement (Clarity A; Guidepoint/Maven A; HealthTap A — membership; consumer pole reported).
- Satisfaction guarantee / refund policy (Clarity A — full refund pre-call, conditional post-call; consumer pole reported, not examined).
- Follow-up exchange: threaded clarification after the initial answer (Clarity A — inbox messaging; HealthTap A — ongoing doctor messaging; consumer pole reported).
- Search/browse of experts by specialty and search over past Q&A (Clarity A — directory search; HealthTap A — archive search; Guidepoint A — library search).
- Response-time expectations and availability rules (Clarity A — 72h/24h; Guidepoint A — hours; HealthTap A — "in hours").
- Notifications, scheduling, and confirmation machinery for call-based variants (Clarity A; Guidepoint/Maven A).
- Community/conduct rules and moderation (Clarity A — etiquette + expert standards; Guidepoint A — compliance program).
- Web + mobile surfaces (Guidepoint A — mobile apps; Clarity/HealthTap A — web-first).

## L2 — Variant / Optional Structure

- Exchange surface: text Q&A thread vs scheduled live call vs live chat (Clarity = call; HealthTap = text + video; consumer pole = text).
- Monetization model: pay-per-question, per-minute billing, membership/subscription, insurance-covered, enterprise retainer/credits (all poles differ — not definitional).
- Record visibility: private exchange vs public searchable archive (Clarity explicitly private/off-the-record; HealthTap documents a public member-asked/doctor-answered library; Guidepoint transcripts are private research assets).
- Asker anonymity (HealthTap documents anonymous asking; Clarity requires real personal identity — opposite poles).
- Vertical specialization and regulatory posture: health (licensure), legal, tech, business/finance (compliance) — verticals change vetting and rules, not the core.
- Expert-side economics: application/vetting to join, earnings dashboards, payouts, open-project marketplaces (Maven A — open projects; Clarity A — expert earnings export).
- AI layer: symptom-checker front door (HealthTap A), AI matching (Guidepoint/Maven A), AI summaries/transcription (Guidepoint A), corpus-grounded AI answers over past expert content (Guidepoint AskGP A).
- Enterprise governance: conflict screening, eligibility review, recording/transcripts, compliance controls (Guidepoint/Maven A).
- White-label/licensing of the whole machinery (Maven A — branded expert networks).

## L3 — Vendor-specific (research notes only)

- Clarity: 72-hour expert response window; 3 suggested time slots; card authorization (not billing) at request; conference line + access code; up to 8 team participants; no personal numbers shared; no screen/document sharing; "off the record" privacy stance; refund conditions (permission to contact expert; no fraud suspicion); "99% 5-star" vendor claim; seven expert standards; 30-day review window; service fee + earnings export; donation of earnings.
- Guidepoint: Guidepoint360 platform; AskGP AI; 1.75M/2M+ experts; 15k+/month recruitment; 120k+ transcripts; 80k+ companies; 19 offices; 300+ industries/500+ subsectors; agentic AI matching + proprietary knowledge graph; compliance led by former SEC senior counsel; recording/transcription/AI summaries at no cost; API/MCP delivery.
- Maven: MavenX engine; HITL AI services; OpenITM internal talent marketplace; Expert Exchange network interconnection; Branded Expert Network private label; open-projects marketplace; 1M+ experts / 220+ countries / <24hr fulfillment; credits or à-la-carte purchasing.
- HealthTap: 90,000 US-licensed board-certified doctors; 147 specialties; AI symptom checker; free dependents (ages 1–17); Quest Diagnostics lab-order flow; COVID recovery letter refusal; insurance acceptance breadth.

## Vendor-specific Findings

See L3. None of these are promoted to the canonical document.

## Boundary Findings

- **vs Q&A Community (01.06)**: community = open crowd answering with voting/reputation as the quality mechanism; Expert Q&A Platform = closed vetted pool with platform governance as the quality mechanism. Blends exist (community products with paid expert features); the discriminator is who may answer and how quality is enforced.
- **vs Answer Engine / Knowledge Question Answering Application (02.03 siblings)**: algorithmic retrieval/generation vs human expert judgment addressed to one asker. AI front doors (symptom checker, AskGP) exist inside sampled products but the governed human exchange remains the product's transactional core.
- **vs Expert Network (no directory leaf)**: Guidepoint/Maven/GLG-class products serve organizations running research programs: demand is a project brief, the unit of record is a compliance-governed engagement + transcript, and the buyer consumes expert time at scale. They share the L0 skeleton but differ in buyer, demand unit, record semantics, and governance. Treated here as a boundary pole; flagged for taxonomy review (see Boundary Issues).
- **vs Tutoring Platform (23)**: tutoring = scheduled learning sessions with progression; Expert Q&A = transactional answers to specific questions. On-demand homework-help products blur this; the discriminator is whether the deliverable is an answer/advice or a learning progression.
- **vs Telehealth Platform (22)**: HealthTap demonstrates the drift — when the exchange becomes a scheduled clinical encounter with prescriptions/treatment plans, the product is telehealth; the Q&A machinery remains a capability inside it.
- **vs Service Marketplace (05.02)**: service marketplaces sell execution of tasks/time (bookable jobs); Expert Q&A sells answers/advice to a specific question. Expert networks sell consultations (time) — the seam is thin and flagged.
- **vs Help Desk / Customer Support (07)**: support = an organization serving its own customers; Expert Q&A = a third-party expert serving an unrelated asker.
- **"去掉什么就变成另一个 Type" 判据**: remove vetting + addressed answers → Q&A Community / Answer Engine; remove the record → ephemeral chat; make it scheduled learning → Tutoring; make the unit organizational engagements with transcripts → Expert Network; make it clinical encounters → Telehealth.

## Historical / Market-Sample Check (§24)

Would older, regional, platform-native products still fit the L0?

- Newspaper/magazine "ask the expert" columns and radio advice segments: reader sends a specific question; an identified expert answers it in a later issue; the column is an archived record. Fits (routing = editorial selection; vetting = editorial credentialing; payment = not per-question).
- "Ask a Librarian" reference services: patron question → librarian (credentialed expert) → addressed answer → recorded reference transaction. Fits.
- Early-web volunteer expert sites (AllExperts-class, free, category-manager-vetted volunteers): fits without payment.
- Premium phone/SMS advice lines (legal, medical, psychic): specific question → routed expert → addressed advice → billed call. Fits with call surface.
- None of these require per-question payment, public archives, ratings, or AI. Therefore: payment model, archive visibility, ratings, and AI are NOT definitional; the L0 survives the historical check.

## Uncertainties

1. Consumer pay-per-question mechanics (JustAnswer, Experts Exchange) were not directly examined; their characteristics in this document are carried at reduced strength and without precise numbers.
2. Whether the taxonomy should carry "Expert Network" as a separate Type or fold it here — flagged in STATUS Boundary Issues; this pass treats it as a boundary pole.
3. HealthTap's current product center of gravity is telehealth; its Q&A capability's current prominence (vs 2024-dated documentation) is uncertain.
4. Expert-side vetting depth varies (self-application + reviews vs identity + conflict screening vs licensure verification); the canonical concept "vetted pool" abstracts across these, but the market may be splitting into loosely-vetted and compliance-vetted sub-markets.

## Final Synthesis

An Expert Q&A Platform is a mediated exchange between askers with specific questions and a vetted pool of experts: the platform routes each question to qualified expert(s), the expert delivers an addressed answer/advice (text or live), the exchange is recorded, and trust is manufactured by the platform through vetting, ratings, guarantees, payment handling, and privacy/compliance rules. Monetization, exchange surface, archive visibility, anonymity, verticals, and AI layers are variants. The nearest Type-boundaries are Q&A Community (who may answer), Answer Engine (human vs algorithmic), Tutoring (answer vs learning progression), Expert Network (question vs research engagement), and Telehealth (advice vs clinical encounter).
