# Research Notes — Polling Application

## Research Goal

Understand the Application Type "Polling Application" (Directory §03.11 Forms & Data Collection): what products sold as poll makers actually do, what their core objects and workflows are, and — because §03.11 is a four-sibling family (Online Form Builder, Survey Platform, Polling Application, Questionnaire Application) — how the Polling Application holds its own boundary against its siblings and against the two adjacent Types whose passes pre-hung flags on it (Audience Response System §26; Group Availability Scheduling Application §03.09).

This pass is the designated counterparty for three pre-hung flags:
1. **audience-response-system** (processed): "boundary with Polling Application held on the session-instrument test (facilitator-run live session + real-time aggregate shown back to the same room — async/embedded poll tools without the live loop are polling, not ARS); flagged for joint review when Polling Application is processed."
2. **online-form-builder** (processed): "vs polling-application — poll = small instrument + live aggregate loop without persisted per-response records; form = multi-field instrument whose defining output is persisted per-response records."
3. **group-availability-scheduling-application** (processed): "NEW thin-seam flag vs Polling Application: a date poll is structurally a poll… proposed discriminators are occasion focus, availability semantics, and the scheduling endpoint; the polling-application pass should treat this document as boundary counterparty."

## Initial Boundary

- A Polling Application is assumed to be a tool for creating small question instruments (polls) that are distributed to a group, answered by lightweight voting, and whose defining output is an aggregate result (counts/percentages per option).
- Suspected confusions: vs Survey Platform (both "questions + results"); vs Online Form Builder (both "collect answers"); vs Audience Response System (both "live polls"); vs Group Availability Scheduling (both "polls with votes"); vs social-media polls and meeting-platform polls (embedded capabilities vs standalone Type); vs formal voting/election systems (both "voting").
- Unknowns: whether identity/anonymity is a settings axis or a defining property; whether "live results" is definitional or common; how the standalone pole relates to chat-platform-native polls (Polly/Simple Poll); whether per-response records are kept (and whether keeping them changes the Type).

## Research Questions

1. What is the poll object, and what does it consist of (question, options, vote type, settings)?
2. What is the canonical create → share → vote → results loop, and where does it end?
3. Who votes, with what identity posture (anonymous / self-declared name / platform account), and what duplicate-control machinery exists?
4. What does the results surface show, when, and to whom?
5. How is a poll closed (deadline, manual close, close-on-create modes)?
6. Which capabilities are common vs variant: vote-type catalog, option mutability, embeds, comments, exports, recurrences, APIs?
7. Where exactly are the boundaries: vs ARS (session container), vs Form Builder (per-response records), vs Survey Platform (measurement), vs Group Availability Scheduling (occasion/time semantics), vs social/meeting-platform embedded polls (capability vs Type)?

## Representative Products

Selection rationale: market representation across the three realization poles of the Type, documentation completeness, different product philosophies (consumer-anonymous vs multi-mode decision tool vs collaboration-platform-native), different customer tiers.

| Product | Pole | Tier | Why sampled |
|---|---|---|---|
| StrawPoll | standalone web poll maker, anonymous-first, ad-funded free | consumer | The category's clearest self-naming product; vendor documents its own definition of a straw poll and its own boundary disclaimers; strong help center (FAQ + First Steps + guides) |
| PollUnit | standalone freemium multi-mode decision tool (votings, tables, surveys, contests) | consumer → business | Documents the full poll object (option types, vote types, targets, share rights) at Tier-1 depth; shows where polls sit inside a wider decision-tooling family |
| Polly | collaboration-platform-native polls (Slack/Teams/Zoom/Meet) | business/enterprise | The embedded-platform pole; shows the poll object transported into chat/meeting surfaces; explicit market positioning vs surveys (its own comparison pages) |

Boundary-context products (not sampled, recorded as context): Simple Poll (Slack-native, single-purpose — named in Polly's comparison page), social-media polls (X/Instagram/LinkedIn — platform capabilities), meeting-platform native polls (Zoom/Teams — capability of that Type, per the ARS pass finding), Xoyondo (standalone free pole — fetch returned 403, unreachable this pass).

## Sources

Research date: 2026-09-08. All fetched directly this pass.

### StrawPoll (Tier 1–2)
- Homepage: https://strawpoll.com/ — product definition, features (fake detection, deadlines, live results, API), two product lines (poll maker / meeting scheduler), scale claims (2.3M users, 13M polls, 290M votes)
- F.A.Q.: https://strawpoll.com/help/faq/ — poll types (anonymous/group/appointment/ranked-choice), privacy model, duplicate-vote control, representativeness disclaimer, vote-editing rule, free/premium posture
- First Steps guide: https://strawpoll.com/help/first-steps/ — full creation flow (question+options, main settings, advanced settings, share, admin functions, results/analytics)

### PollUnit (Tier 1)
- Homepage: https://pollunit.com/en/ — product family (votings, tables, ideas, surveys, contests), 4-step "Decide Together" loop, vote types, evaluation claims
- Tutorial "Create your first poll": https://pollunit.com/en/tutorials/create_your_first_poll — full creation flow: type selection, option types (date/date range/image-file/free text), vote types (yes/no, star, dot), targets (find best / distribute), steps (basic settings → options → design → advanced), share machinery (participant link, one-time invitation links, QR code, admin link), voting behavior, poll management (edit/close/add options/share)

### Polly (Tier 2 product pages; help center not fetched this pass)
- Homepage: https://www.polly.ai/ — platform-native posture (Slack/Teams/Zoom/Meet/Slides/PowerPoint), feature family (polls & surveys, Q&A, suggestion box, quizzes, pulse, standups, workflows), analytics/anonymity/demographics positioning, comparison-page index (vs Simple Poll, vs Slido, vs SurveyMonkey, vs Google Forms, vs Microsoft Forms)
- Polls & Surveys page: https://www.polly.ai/polls-and-surveys — /polly command creation, question types + audience selection, scheduling/recurrence/reminders, web voting link sharing with combined results, real-time results in-app/dashboard, anonymity options, demographics, workflows/exports, "Ditch the survey and send a polly" positioning

### Counterparty documents (from prior passes, used for boundary ratification)
- research/audience-response-system.md — session-instrument L0, §Boundary Findings #2
- research/online-form-builder.md — submission-record L0 leg, §Boundary Findings #3
- research/group-availability-scheduling-application.md — time-finding-poll L0, §Boundary Findings (vs Polling/Survey)

## Product Observations

### StrawPoll

- Vendor's own definition of the Type (homepage): "A straw poll is a voting that can be used to help people to easily determine the opinion of a group or the public on some issue. Straw polls are very useful when **only the majority opinion is important and not the opinion of each individual participant**." — direct vendor articulation that the aggregate, not the individual response, is the point. (A)
- Two product lines: poll maker + StrawPoll Meetings (meeting scheduler) — the date-finding pole is a **separate product line**, confirming the group-availability boundary from the product side. (A)
- Scale claims: 2.3M+ users, 13M+ polls, 290M+ votes; "No signup required". (A)
- Poll types offered: "anonymous polls, group polls, appointment polls and ranked choice votings" (FAQ). Appointment polls again confirm the date-poll capability inside the generic tool. (A)
- Privacy model: "all polls on StrawPoll are private and only accessible through the link you share"; search restricted to polls you created or participated in; a "Discover" section exists for public listing (opt-out via "private" setting). (A)
- Creation flow (First Steps, Tier-1): (1) question + answer options; (2) main settings — private listing, multiple answers allowed, duplicate-vote check via IP (with cookie fallback for shared-IP environments like schools); (3) advanced settings — deadline date, poll image, VPN-user blocking (default on), registered-users-only option, "Require voters to enter their name" (adds a who-voted-what table to results), reCAPTCHA v3 background check (default); (4) create + share via short link and social/messenger buttons; (5) admin functions — edit title/description/options, change deadline, visibility, comments on/off, "change the way your participants can view the poll results", Excel export, delete; admin rights stored in cookies for accountless creators; (6) results in real time — list of votes + pie chart + "Vote Analytics" (when and from where voters took part). (A)
- Duplicate/integrity machinery: IP check with cookie fallback, VPN blocking, reCAPTCHA, and per the FAQ "The creator of a poll has control over how duplicate votes are handled"; guides include "Obtain a unique code" (vote token). (A)
- Reliability disclaimer: "The reliability of the results… strongly depends on the chosen parameters. If you do not know the poll creator, it indicates that the poll results may not be reliable." — the product acknowledges its informal, non-scientific character. (A)
- Representativeness boundary (FAQ): "Are polls on StrawPoll representative surveys? Short answer: No… we do not use scientific methods to evaluate the demographics of poll participants." — vendor-drawn line vs survey research. (A)
- Vote editing rule: "it is only possible to edit the vote if the participant has included their name." (A)
- Deadlines: "Our polls run indefinitely. You can change that by setting a deadline." (A)
- Results sharing intent: "the polls on StrawPoll are made to be shared… share not only a screenshot, but also the link to it so others can see the live result." (A)
- Monetization: free + ads; premium for CAPTCHA, custom branding, ad disabling. (A)
- Distribution extensions: Discord bot, embed guide ("share a live poll" guide), REST API for poll creation and result analysis. (A)

### PollUnit

- Vendor's canonical loop (homepage, "Decide Together: It's just that easy"): "1. Create a PollUnit and choose the options, users can vote for. 2. Send a link to Your PollUnit to all participants. 3. Wait for Your participants to vote. 4. Send the result of Your PollUnit to all participants." — a four-step create → share → vote → share-result loop, documented verbatim. (A)
- Positioning: "Simplify decisionmaking… Create free polls and surveys without registration. Prioritize ideas, distribute tasks, rate pictures, organize photo contests, create bring lists and find the best date - all with one tool!" (A)
- Poll object (tutorial, Tier-1): Title ("the title or question"), Description, Location, **PollUnit type** (allowed option content: Date, Date and Time, Periods, Free Text, Image or File), **Vote type** (yes/no, star rating 1–5, dot voting, more), **Target** ("find the most frequently chosen option, or distribute the options optimally to your participants"), creator name/email when accountless. (A)
- Creation steps: 1 basic settings → 2 options (add/delete, participants can be allowed to add new options) → 3 design (themes) → 4 advanced settings (comments toggle, "Allow new options", more per account tier). (A)
- Share machinery: participant link (default: anyone with the link can vote, shareable via email/WhatsApp/Facebook), invitations with per-participant one-time links, QR code for presentations, admin link (rights sharing; disableable with account), organizations for managed shared administration. (A)
- Voting behavior: click the option's checkbox (or star rating); participants without an account must assign a name first; account users can comment and edit/delete entries from other devices. (A)
- Management: context menu to edit, close, add new options, share; account needed to fully manage. (A)
- Evaluation: "Access all poll and survey results in real time during and after your online poll. Interactive charts, diagrams, and data tables… Filter results, explore open-ended responses with word clouds, and export your data." (A)
- Family context: surveys (Likert, branching, multi-step) are a separate PollUnit type; so are tables, idea collection (upvoting/commenting), photo/video/music contests, pairwise comparison, advent calendar, "find a date" (separate tutorial) — the generic poll maker hosts date polls as one option type, matching the group-availability seam. (A)
- Duplicate-control area: dedicated tutorial "Prevent multiple participation". (A)
- Monetization: free tier + premium features (themes, orgs, fees/wallets for paid contests). (A)

### Polly

- Platform-native posture: "Polly works where you work" — native apps for Slack, Teams, Zoom, Google Meet, Google Chat, Google Slides, PowerPoint; polls are created **inside** the collaboration surface ("/polly in any channel and Polly will guide you through the rest"). (A)
- Value framing: "Your teams can answer a polly without context switching, which means you more responses, faster" — participation friction is the design driver, same low-friction principle as link-based tools, different channel. (A)
- Poll object: question types + audience selection ("Granular controls around question types and audience selection"); templates for common questions. (A)
- Distribution duality: in-channel/meeting answering AND "Share a polly's web voting link and collect feedback from wherever your team works — meetings, emails, or internal wikis, and then get results combined in the same polly!" — the same aggregate-combining behavior as link tools. (A)
- Results: "Get results in real-time right in-app, or on your dashboard, and then share results with key team members with just a few clicks." (A)
- Identity/anonymity: "clear, simple options for keeping their feedback public or private" (response anonymity settings); platform identities underlie participation; "Demographics" retains metadata for segmentation while feedback stays confidential. (A)
- Recurrence/scheduling: "Powerful scheduling and recurrence options… Achieve 100% participation with friendly automated reminders" — polls as standing/recurring instruments (pulse checks), an extension beyond the one-shot poll. (A)
- Extensions: workflows to external systems (JIRA, ServiceNow, Google Calendar, Sheets, HRIS), exports to analysis tools, API/webhooks. (A)
- Market positioning: "Ditch the survey and send a polly" — and a comparison-page family (vs Simple Poll, vs Slido, vs SurveyMonkey, vs Google Forms, vs Microsoft Forms) that maps the category neighborhood from the vendor's own perspective. (A)
- Feature family around the poll core: Q&A, Suggestion Box, Live Quizzes, Pulse Surveys, Standups, Workflows, Team Building — the poll core sits inside an engagement suite at the business tier. (A)

## Cross-product Comparison

| Dimension | StrawPoll | PollUnit | Polly | Reading |
|---|---|---|---|---|
| Poll object | question + options + settings, stored & shareable | "PollUnit": title/question + typed options + vote type + target | "polly": question + options, in-channel object | B — same object, three substrates |
| Participation path | short link; embed; Discord bot | participant link / one-time links / QR / invitations | in-channel click + web voting link | B — low-friction shared path, channel varies |
| Identity posture | anonymous default; optional name-required; registered-only option | guest with self-declared name; account optional | platform identity; anonymity settings | B — a settings axis, not an invariant |
| Vote semantics | multiple choice (single/multi), ranked choice | yes/no, star rating, dot voting, range | question-type catalog | B — catalog common; specific types vary |
| Option mutability | creator-defined | participants may add options (toggle) | creator-defined + templates | poll-specific / B |
| Results | real-time, pie/bar, vote analytics, Excel export | real-time during and after, charts/word clouds, export | real-time in-app/dashboard, shareable | B — aggregate as deliverable, live-update common |
| Closing | deadline optional; otherwise indefinite | manual close via menu | scheduling/recurrence/reminders | B — lifecycle machinery common, model varies |
| Duplicate control | IP/cookie check, VPN block, reCAPTCHA, unique codes | prevent-multiple-participation settings, one-time links | platform identity | B — integrity machinery common; mechanisms vary |
| Per-response records | list of votes (with names if required); analytics about voters | table view; account entries editable/deletable | results retention, demographics | B — records exist but the aggregate is the deliverable |
| Adjacent modes | meetings (separate product line) | surveys/tables/contests/ideas (separate types) | surveys/Q&A/quizzes/pulse (separate features) | B — all three families bolt adjacent modes beside the poll core |
| Where the poll sits | the core product | one type among many | one feature among many | poles, not contradiction |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

A Polling Application exists where all three hold:

1. **The poll as a small question instrument** — a stored, shareable poll object posing a question (typically one, at most a few) with a predefined set of answer options (creator-fixed, or extendable by participants as a mode). The instrument is *small*: one click/act answers it. Remove it → a chat message or a tally sheet with no structured instrument; enlarge it (many fields, per-response records as the deliverable) → Form Builder / Survey territory.
2. **Lightweight distributed voting** — participants record their choice(s) through a low-friction shared participation path (link, embed, chat command, QR, meeting-app surface), without needing accounts in the default case; participation is a single lightweight act. Remove it → owner-only tally tool (nothing to distribute); make it a multi-field fill → Form Builder.
3. **The computed vote aggregate as the defining output** — the system tallies the choices into an aggregate result (counts/percentages per option, commonly charted) that is the poll's purpose; the poll exists to produce a shared answer to the question, not per-response records to be processed downstream. Remove it → question collection with no outcome (a form/ballot box never opened).

Jointly-held is load-bearing:
- 1+2 without 3 = votes collected with no result surface — a ballot box never opened; the poll never answers anything.
- 1+3 without 2 = a result nobody voted into (a static graphic).
- 2+3 without 1 = a vote counter with no question instrument.
- 1 alone = a question prompt; 2 alone = voting machinery; 3 alone = a tally chart.

Historical/market-sample check: a question posted on a noticeboard with option columns and tally marks; a show-of-hands vote with counted results; a ballot box with a published tally — all satisfy the three legs with no accounts, links, real-time updates, or software. Conversely, sampling-based opinion research (panel + weighting + demographic analysis) fails the "lightweight informal vote" character and belongs to survey/research territory — a line StrawPoll's own FAQ draws ("not representative surveys… no scientific methods"). The definition names no technology, no channel, and no era pattern.

### L1 — Common Mature Structure

- Shareable participation path: short links, website embeds, QR codes; social/messenger share buttons.
- Accountless participation as the default posture; optional identity requirements (enter-name, registered-users-only, one-time invitation links) as settings.
- Vote-type catalog: multiple choice (single/multi-select), ratings, rankings, dot-voting and similar weightings — catalogs differ per product.
- Results surface: counts/percentages per option, commonly charted (pie/bar), commonly updating live as votes arrive; often combined per-response inspection (who voted what when identity is recorded).
- Poll lifecycle: creation → open → (optional deadline / manual close) → results; results typically remain viewable during and after.
- Duplicate/abuse controls: duplicate-vote detection (IP/cookie/device), bot/VPN filtering, CAPTCHA-class checks, unique vote tokens.
- Owner/admin surface distinct from the participant surface: edit, close, re-open, delete, manage sharing rights (admin links/organizations).
- Comments/discussion attached to the poll.
- Export of results (Excel/CSV-class).

### L2 — Variant / Optional Structure

- **Hosting substrate**: standalone web service (StrawPoll, PollUnit) vs collaboration-platform-native app (Polly in Slack/Teams) vs meeting-suite embedded polls (capability of that Type) vs social-media polls (capability of that Type) vs personal-website embeds.
- **Identity substrate**: anonymous / self-declared name / platform account / rostered organizational identity.
- **Vote semantics depth**: plurality choice vs rating vs ranking vs dot/range voting; single vs multiple answers; participant-added options; "find best" vs "distribute among participants" targets (PollUnit).
- **Recurring/scheduled polls**: standing pulse-type polls with reminders (Polly) — extension toward engagement measurement.
- **Enterprise layer**: demographic segmentation, confidential-response retention, workflows into ticketing/HRIS, APIs/webhooks (Polly).
- **Family packaging**: poll makers commonly bolt on adjacent modes — surveys, tables/list collection, idea collection with upvoting, photo/video contests, appointment/date polls (PollUnit; StrawPoll Meetings as a separate line).
- **Monetization/posture**: ad-funded free with premium feature gating; paid contests with entry-fee processing (PollUnit).

### L3 — Vendor-specific (research notes only)

- StrawPoll: "Discover" public listing section; Vote Analytics (when/from-where participation); unique vote-token guide; Discord bot; cookie-stored admin rights for accountless creators; its own definitional blurb of "straw poll".
- PollUnit: build helper (guided/quick creation); Theme Maker; organizations; pairwise-comparison, advent-calendar, photo/video/music contest products; wallets/entry fees; "send the result" step in its loop.
- Polly: /polly command; demographics segmentation; workflows to JIRA/ServiceNow/Google Calendar/Sheets/HRIS; "polly" as the product's own unit noun; comparison-page family.

## Vendor-specific / Rejected Findings

- **Rejected: "a poll is anonymous by definition."** StrawPoll is anonymous-first, but PollUnit requires a self-declared name for accountless voters and Polly rides platform identities. Identity posture is a settings axis, not an invariant.
- **Rejected: "live-updating results define the Type."** Real-time result surfaces are common across the sample (and in ARS), but a poll whose results are revealed on close still satisfies the L0 (aggregate as output). Live update is implementation currency, not structure. The ARS pass's own L0 leg is the *display back to the same live room*, which is a different structure.
- **Rejected: "polls keep no individual records."** All three sampled products keep some response-level data (vote lists, editable entries, demographics metadata). The correct discriminator vs Form Builder is the center of gravity: the aggregate is the deliverable, records are incidental/supporting — not record absence.
- **Rejected: "polling = Slack/Teams bots"** or "polling = web links" — channel is a variant substrate.
- **Rejected: "appointment/date polls are the Type's core."** They are one option-type/poll-type inside generic tools (StrawPoll "appointment polls", PollUnit "Date" option type, both with separate meeting/date product treatments), not the defining content.

## Boundary Findings

1. **vs Audience Response System (§26 — counterparty flag DISCHARGED, keep-both ratified).** The ARS is the session-instrument specialization: a facilitator-run live session container with mass distributed response and the aggregate displayed back to the same co-present room while it happens. A Polling Application has no session container: the poll is a durable shareable object (link/embed/chat object) whose aggregate the owner and participants consult in their own time; there is no host role, no join-the-room act, no room display loop. The poll object itself is shared machinery, but the *container* differs structurally. Product-side confirmation: none of the three sampled products is organized around a facilitated room; Polly integrates into meetings but the poll remains a channel-shared object with combined results, not a room instrument. Removal tests: add a facilitator-run session with the aggregate shown live to the co-present room → ARS; strip the session container from an ARS → polling. This ratifies the ARS pass's session-instrument test from the polling side; the two leaves stand.
2. **vs Online Form Builder (§03.11 sibling — counterparty flag DISCHARGED, seam confirmed).** Both author question instruments and collect answers. The seam is the output object: a form's defining output is the persisted per-submission record that the owner views/exports/routes/works downstream; a poll's defining output is the computed aggregate. Product-side: poll tools surface results-first views (charts/percentages); response-level inspection is supporting (who-voted tables, editable entries), not an inbox/table of records to process. Instrument size is the second marker (one click answers a poll; a form is a multi-field fill). Removal tests: make per-submission records the owner's workable object → Form Builder; make the aggregate the deliverable → Polling. PollUnit's separate "Tables" type and "Surveys" type confirm the market keeps these modes apart inside one vendor.
3. **vs Survey Platform (§03.11 sibling, unprocessed).** Vendor-drawn lines from both sides this pass: StrawPoll FAQ explicitly disclaims representativeness/scientific method; Polly positions "Ditch the survey and send a polly". The poll is a single lightweight question instrument with an instant aggregate; the survey is an instrument battery tuned for measurement with analysis/reporting as the deliverable. Drift path: recurring polls accumulated into measurement programs (Polly pulse) reach toward Employee Survey / Survey territory. Left to the Survey Platform pass with this document as counterparty; Questionnaire Application flagged similarly (likely near-alias of Survey — that pass decides).
4. **vs Group Availability Scheduling Application (§03.09 — counterparty flag ratified, thin seam held).** Date polls are structurally polls and both sampled generic tools offer them (StrawPoll "appointment polls"; PollUnit "Date/Date range" option type + "Find a date" tutorial; StrawPoll even splits Meetings into a separate product line). The seam stays as the availability pass defined it: occasion focus (options are times for one event), availability semantics (can-you-make-it declarations), and the scheduling endpoint (convergence on one chosen time). A generic poll tool *hosting* a date poll is capability overlap, not Type overlap.
5. **vs Meeting/webinar platform native polls and social-media polls.** Native polling inside Zoom/Teams/X/Instagram is a capability of those container Types (consistent with the ARS pass's finding for webinar platforms). The standalone Polling Application is the Type whose *primary surface* is the poll itself; embedded polls are features. Primary-surface test: what does the product exist to do?
6. **vs formal voting/election systems.** Polls are informal and non-binding: no eligibility rolls, quorum, weighted governance voting, or certified ballot machinery. StrawPoll's reliability disclaimer ("results may not be reliable" if parameters are loose) marks the informality structurally. Decision-grade governance voting is a different domain (not a §03.11 leaf).
7. **vs Q&A / idea collection.** Open-text collection with upvoting (PollUnit "Collect ideas", Polly Q&A/Suggestion Box) lacks the predefined-option instrument and aggregate; it drifts toward feedback/idea management. The poll requires the option set.

**"去掉什么就变成另一个 Type" 判据汇总：**
- 加上主持人运营的现场会话容器、把聚合实时投回同一现场 → Audience Response System
- 把输出重心换成逐条提交记录（所有者后续处理/流转） → Online Form Builder
- 扩成多题测量工具、以分析与报告为交付物 → Survey Platform
- 选项限定为单一场合的时间、语义换成可用性声明、终点是定下时间 → Group Availability Scheduling
- 加入名册/法定程序/计票认证 → 选举/正式表决系统（不在本目录）
- 去掉预定选项与聚合（开放文本+点赞） → 反馈/点子收集类

## Uncertainties

- **Polly help-center depth**: evidence is product-page tier; creation mechanics, exact anonymity options, and per-question-type behavior are not Tier-1 verified this pass. No precise limits/defaults asserted from Polly.
- **Xoyondo** (standalone free pole) returned 403 — unreachable; recorded as context only. The standalone free pole is still covered by StrawPoll's Tier-1 documentation.
- **Questionnaire Application** (unprocessed sibling): not studied this pass; from the form/survey/poll seam analysis it looks like a near-alias of the survey instrument family — left to that pass.
- **Exact duplicate-control behaviors** (what happens on detection, token lifetimes, VPN-list sources) — not researched to that precision; the final document describes the machinery conceptually.
- **Historical web-poll tools** (2000s poll scripts, forum poll plugins): the historical check is structural (noticeboard/ballot analog + forum-poll capability context); no specific legacy product was fetched. Research/discussion-board.md independently documents poll threads as a plugin/native capability in forum software — consistent with the "embedded poll = capability" finding.
- **Whether "results revealed only on close" exists as a first-class mode** in sampled products: StrawPoll/PollUnit document real-time surfaces and result-visibility settings exist in the admin surfaces, but a pure hide-until-close mode was not directly evidenced; phrased softly in the final document.

## Final Synthesis

The Polling Application is best understood as **the lightweight poll made into software**: an owner composes a small question instrument with predefined options, distributes it through a low-friction shared path (link, embed, chat command, QR), participants answer with a single lightweight act — usually anonymously or under a self-declared name — and the system's defining output is the computed aggregate of votes, viewable in real time, shareable, and (in mature products) exportable. Around that trio, mature products add the lifecycle machinery (deadlines, closing), integrity machinery (duplicate checks, bot/VPN filtering, unique tokens), identity settings (anonymous ↔ named ↔ rostered), richer vote semantics (ratings, rankings, dot voting), discussion, and exports; the market realizes the Type in three poles — standalone consumer poll makers (StrawPoll), multi-mode decision tools with the poll as one type (PollUnit), and collaboration-platform-native engagement apps with the poll as the core feature (Polly). The Type's boundaries are held by four tests, all confirmed against counterparty documents this pass: the session-container test (vs ARS), the output-object test (vs Form Builder), the measurement test (vs Survey Platform), and the occasion/time test (vs Group Availability Scheduling). Embedded polls inside meeting platforms and social networks are capabilities of those Types, not instances of this one.
