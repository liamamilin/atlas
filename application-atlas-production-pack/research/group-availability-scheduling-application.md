# Research Notes — Group Availability Scheduling Application

## Research Goal

Understand the Application Type "Group Availability Scheduling Application" (Directory §03.09 Scheduling): what products sold under this category actually do, what their core objects and workflows are, and — because this leaf sits in a three-sibling family (Meeting Scheduling Application, Appointment Scheduling Application, Group Availability Scheduling Application) — how it holds its own boundary against both siblings, against Calendar Applications, and against the generic polling Types in §03.11.

## Initial Boundary

- The leaf sits in §03.09 Scheduling with two processed siblings. The family signature noted in prior passes: "publish availability → another party books a time". The appointment pass already separated this leaf by the **persistent-appointment test**: "poll output = a chosen time, not a managed appointment" (STATUS.md boundary issue, 2026-09-06).
- The interview-scheduling pass recorded: "group-availability tools find a time among peers and end at a chosen time; interview scheduling maintains persistent managed interview records" (research/interview-scheduling-platform.md).
- Initial hypothesis: the defining activity is *time-finding among participants* — an initiator proposes options, participants declare availability, the tool aggregates, a time is chosen. No provider, no service catalog, no persistent booking record.
- Potential confusions: generic Polling Application (§03.11) — a date poll is structurally a poll; Meeting Scheduling — organizer-imposed time with accept/decline; Calendar "find a time" features.

## Research Questions

1. What is the central object? (poll/event-for-time-finding) What does it carry?
2. How are candidate time options defined? (discrete proposed options vs continuous availability grid)
3. How do participants express availability? (vote ladder yes/if-need-be/no; grid marking; anonymity)
4. How does the tool aggregate responses, and who decides the final time?
5. What happens after a time is chosen? (announcement, calendar invites, close) — and is there any persistent appointment record?
6. What identity does participation require? (accounts? name+email? anonymous?)
7. Which capabilities are common-but-not-defining: calendar integration, reminders, deadlines, per-option capacity limits, timezone handling, exports, comments?
8. How do platform-embedded realizations (Outlook Scheduling Poll) and scheduling-suite bridge features (meeting polls inside booking products) differ from pure-play products?

## Representative Products

| Product | Pole | Why chosen |
|---|---|---|
| Doodle | market-defining classic, consumer/prosumer SaaS | created the category; Group Poll is its flagship; documents the full loop incl. finalize |
| Rallly | modern standalone poll-first SaaS + open source | full official documentation of create→invite→vote→schedule; shows the minimal modern form |
| Nextcloud Polls | open-source, self-hosted, platform-app | confirms the structure outside SaaS; shows confirm-after-close, anonymity, calendar hints |
| When2meet | minimalist account-less pure-play | availability-grid style; observed live; contrasts option-list style |
| Outlook Scheduling Poll (Microsoft) | platform-native, calendar-embedded | market anchor for the embedded pole; **unreachable this pass** — no product claims |

Calendly (meeting-poll features inside a booking product) serves as the bridge toward the Appointment/Meeting siblings; it was documented in the appointment-scheduling pass ("Calendly meeting polls" as a variant) and its current help center was unreachable this pass — no fresh claims.

## Sources

Tier 1 (official operational documentation, directly fetched 2026-09-07):

- Doodle Help Center — collections "Group Poll" (27 articles), "Participation"; articles: Introduction to Group Poll (9823082), How do I create a group poll? (9457353), How do I select the final option for my group poll? (9457342), How do I participate in a group poll? (9457279); article list reviewed for settings (deadline/limits/reminders/hidden), edit behavior, export, duplicates
- Doodle product pages — https://doodle.com/en/ , https://doodle.com/en/product/polls/ (Group Poll, Sign-up Sheet, 1:1, Booking Page taxonomy; "Book it"; deadlines/reminders; invite-anyone)
- Rallly official documentation — https://support.rallly.co/ (Introduction, Create a poll, Invite participants, Schedule, Participant Guide, index llms.txt)
- Nextcloud Polls — official project README, https://github.com/nextcloud/polls
- When2meet — live application surface, https://www.when2meet.com/ (rendered date-grid UI)

Unreachable / degraded:

- Microsoft Scheduling Poll (support.microsoft.com): guessed article URL → 404; support search → timeout. Search engines (DuckDuckGo timeout, Bing regionalized) unusable this pass. Platform-embedded pole documented structurally; no Microsoft-specific feature claims.
- Calendly: old help-center article ID redirects to generic help home (help-center migration); new help center search is JS-only. Rely on the appointment-scheduling pass's documented observation of meeting-poll features; no fresh Calendly claims.
- When2meet: the product ships no help docs; only the live surface was observed.

Research date: 2026-09-07.

## Doodle — Key observations (evidence layer A unless noted)

Product family (from product pages): Group Poll ("Find the time that works best for everyone in your group"), Sign-up Sheet, 1:1, Booking Page. Group Poll is positioned as "Doodle's first and most popular scheduling feature".

Group Poll loop (Introduction article):

1. **Create**: enter event details (name, description, location; optional video conferencing via Google Meet/Zoom/Webex) → choose duration → click into a calendar grid ("Week" or "Month" view) to propose times → "Create and share".
   - Week view: select duration (custom range documented as 5 minutes to 12 hours; all-day option for 24-hour events; events cannot span two calendar dates), time zone auto-check, participants' polls adjust to each participant's time zone.
   - Month view: pick days, set start time and duration per slot, flexible start times.
   - Optional calendar connection shows the organizer when they are busy/free while proposing times.
2. **Share**: copy poll link (email/Slack/WhatsApp/Teams/embed), or send email invitations from Doodle (paid); Google/Outlook contacts autofill; "Group polls live on their own. Just send one and anyone can participate — with or without an account."
3. **Participate** (Participation articles): participant opens link → sees occasion context (organizer, location, description, invitees) → votes per proposed slot: YES (one click), IF-NEED-BE (two clicks), NO (empty) → "Continue" → name + email (no Doodle account required; logged-in users auto-filled) → "Submit vote". A "decline" action records a No for all slots. Auto-notification when the organizer selects the final date; optional "get updates when others vote"; votes editable.
4. **Finalize** ("How do I select the final option"): organizer selects the best option (star on the winning date) → "Book it" → only one final option can be selected → Doodle confirms with all participants: with a connected calendar, a calendar invitation goes to all participants (even those who voted No on the final option; non-participants get nothing); without a calendar, a confirmation email with event details goes to organizer + participants, who add it to their own calendars.
5. **Settings** (paid tier): deadline (after it, no new responses and no vote changes), limit participants (max participants per time slot), automatic reminders to non-voters, hide participant list (only organizer sees names/votes).
6. Other documented behaviors: the organizer automatically votes yes on all proposed times at creation (can change); editing the poll after votes arrive produces mismatched/question-mark responses; organizers cannot un-invite a participant (paid can delete/edit a response); duplicate-as-template; export to Excel; invite-list and response tracking; email invitation limits; maximum poll size documented (1,000 respondents — product-specific, not carried into the Type document); free accounts limited to 1 group poll (product-specific); admin link recovery; subscribe/unsubscribe to per-poll email notifications.

## Rallly — Key observations (evidence layer A)

Official docs, full workflow:

- **Create a poll**: title, optional location, optional description → select options via **Month view** (pick dates, adjust times per option) or **Week view** ("draw time slots on a weekly calendar") → duration per option (30m/1h/1h30m/2h or **All day** for whole-day voting) → time zones automatically shown in each participant's own zone; **Lock time zone** forces everyone to see the same times → "Create poll" → Share dialog opens.
- **Invite**: invite **link** (anyone with the link can vote) or invite **by email** (paid) with per-invitee tracking: "sent, opened or responded".
- **Vote** (Participant Guide): toggle each option through Yes → If need be → No ("If you leave an option unselected, it will be counted as a No vote") → Continue → name + email → Submit. Editing: cookie-recognized by default; entering an email yields a magic link to edit from anywhere. Loss of recognition → ask the poll administrator to delete/edit the response.
- **Review**: results page shows "which dates are preferred".
- **Schedule** ("Pick a final date for your event", paid): each option shows how many participants are available and a breakdown of votes → select preferred date → "Schedule" → (1) calendar invite emailed to the host, (2) calendar invite emailed to participants, (3) **poll closes to new responses**; the final date is displayed on the poll and "can be added to a calendar with one click".
- Team usage: Spaces (centralized billing, member management, collaboration mode), custom branding; self-hosting (Docker, SSO via Google/Microsoft/OIDC, white labeling, control panel, licensing) — deployment variant.

## Nextcloud Polls — Key observations (evidence layer A)

Official README ("Polls — an app, similar to doodle … for Nextcloud"):

- Feature set: easy poll creation; **hide results until revealed** (confidential polls); obfuscate participant names / strong anonymous mode; automatic expiry date; **participants can add more options**; limit votes per option or user; invite everyone; export to spreadsheet formats or HTML; automatic reminders for invited users; comments; **confirm options after poll closing**; subscribe to notifications per poll; **hints about possible conflicting calendar entries** around a date option; REST API; Nextcloud app integrations (Circles, Contacts, Activity).
- Confirms: the option-poll structure, the close/confirm step, anonymity variants, calendar-conflict hints, and participant-added options exist outside the SaaS consumer market.

## When2meet — Key observations (evidence layer A, limited)

- Live surface (fetched): presents a multi-week **date grid** (day-of-week × date rows across a month-spanning window) as the entry surface for marking availability. The product ships no help documentation.
- Structurally, When2meet represents the **availability-grid style** (participants mark when they can, rather than voting on discrete proposed options) and the **no-accounts, no-frills pole**. Claims beyond the observed grid are NOT asserted from this pass.

## Outlook Scheduling Poll (Microsoft) — observation status

- Not directly verified this pass (source unreachable; see Sources). Recorded as the market anchor for the **platform-embedded pole**: a scheduling poll that lives inside a calendar/mail suite, proposes candidate times from attendee free/busy, collects votes, and is confirmed by the organizer into a calendar event. No precise feature claims are made for Microsoft in this document; the pole's existence is corroborated conceptually by the Type's structure and by market ubiquity, and is flagged in Uncertainties.

## Calendly meeting polls — bridge observation

- Fresh fetch failed (help-center migration). The appointment-scheduling pass directly documented "Calendly meeting polls" as a bridge feature toward the group-availability sibling (research/appointment-scheduling-application.md §Boundary Findings). Used here only as conceptual corroboration that scheduling-suite products embed group-poll features; no fresh product claims.

## Cross-product Comparison

| Structure / capability | Doodle | Rallly | Nextcloud Polls | When2meet | Evidence |
|---|---|---|---|---|---|
| Shared poll object for one occasion (title/context/options) | ✔ | ✔ | ✔ | ✔ (grid) | A×4 |
| Candidate time options defined by initiator | ✔ (grid pick) | ✔ (month/week views) | ✔ | grid range | A×4 |
| Participants declare availability / vote | yes / if-need-be / no | yes / if-need-be / no | votes (+limits) | grid marking | A×3 + A(when2meet surface) |
| Accountless participation | ✔ "with or without an account" | ✔ (name/email, cookie/magic link) | ✔ (public share) | ✔ (name only) | A×4 |
| Aggregated availability view (per-option counts / overlap) | ✔ votes table | ✔ counts + breakdown | ✔ results (+hidden until revealed option) | intersection grid | A×4 |
| Finalize: choose final option & announce/close | ✔ "Book it" (one option) | ✔ "Schedule" (closes poll) | ✔ confirm after closing | none documented | A×3 |
| Calendar integration | optional connect (busy overlay, invites on finalize) | none in docs; email invites | conflict hints | none observed | A×3, differing depth |
| Deadline / expiry on responses | ✔ (paid) | not documented | ✔ auto expiry | not observed | A×2 |
| Reminders to non-responders | ✔ (paid) | not documented | ✔ | not observed | A×2 |
| Per-option capacity limits | ✔ "limit participants" per slot | not documented | ✔ votes per option/user | not observed | A×2 |
| Hidden/anonymous responses | ✔ hide participant list (paid) | not documented | ✔ confidential + anonymous | not observed | A×2 |
| Timezone handling | auto per participant | auto per participant + lock | not documented | not observed | A×2 |
| Participant-added options | not documented | not documented | ✔ | not observed | A×1 |
| Editable responses | ✔ (vote changes; paid can edit others') | ✔ (cookie/magic link) | not documented | not observed | A×2 |
| Exports / duplicates / comments / API | ✔ Excel, duplicate, notifications | not documented (spaces/branding instead) | ✔ export HTML/CSV-class, comments, REST API | none | A×2 |
| Team/enterprise wrapper | Team plans, branding | Spaces, SSO (self-host) | Nextcloud tenancy | — | A×3 |
| Option-list vs availability-grid interface | both (month list-ish / week grid) | both | option-list | grid | A×4 |

Reading: the first five rows are observed in every sampled product with accessible evidence and form the Type's stable core. Everything below the line is common-but-variable or single-product.

## Canonical Model (abstraction levels)

### L0 — Defining Invariant

Four properties. Remove any one and the product stops being a Group Availability Scheduling Application:

1. **The time-finding poll for one occasion** — an identified shared object created by an initiator for a single event or occasion that needs a time, carrying the occasion's context (title, optionally location/description/video link) and its candidate options. Remove → generic polling/survey.
2. **Candidate time options** — discrete proposed date-times (or whole-day options; or a date-time availability range presented as a markable grid). Options are the shared candidates everyone answers against. Remove → not time-finding.
3. **Participant-declared availability** — each participant answers for themselves which options work (a yes / if-need-be / no ladder, or availability marks on a grid). The participants are the source of the availability data; no participant owns the time and no provider's bookable availability defines it. Remove → organizer-imposed accept/decline (Meeting Scheduling) or provider-slot booking (Appointment Scheduling).
4. **Aggregated comparison converging on a chosen time** — the tool's central computed artifact is the cross-participant aggregate (per-option availability counts, or the group's overlap grid), used to converge on **one final option**; the choice is made by people (initiator/organizer or group consensus) with the tool surfacing the overlap, and ends the poll. Remove the aggregation → a pile of individual responses (a spreadsheet); remove the convergence → an availability survey rather than scheduling.

Deliberately NOT in L0 (historical check, see below): accounts/participant identity beyond self-declared name; calendar integration; deadlines/reminders; timezone features; capacity limits; vote ladders (plain yes/no suffices); email distribution; exports; finalize-to-calendar-invite mechanics (the invariant is the chosen time, not what carries it).

### L1 — Common Mature Structure

- Shareable link distribution as the primary participation channel; optional email invitations with per-invitee response tracking.
- Participant identification as self-declared name (+optional email), no account required.
- Editable responses (participants can change votes until the poll closes).
- Automatic reminders to non-responders; response deadlines/auto-expiry.
- Timezone handling: per-participant display conversion; timezone locking where precision matters.
- Finalize mechanics: mark one final option, notify all participants (announcement email; calendar invite when a calendar is connected).
- Per-option capacity limits (max participants/votes per slot) — prevents overbooking a slot.
- Response visibility controls: hidden participant lists, confidential results, anonymous modes.
- Organizer-side management surface: dashboard of polls, edit/duplicate/delete, results export.
- Video-conference link attachment and location fields on the occasion context.

### L2 — Variant / Optional Structure

- Interface style: discrete option lists vs continuous availability grids (many products offer both).
- Platform-embedded scheduling polls (calendar-suite feature proposing times from attendee free/busy, confirmed into an event).
- Group-poll features embedded in booking/scheduling suites (bridge toward the Meeting/Appointment siblings).
- Self-hosting / open-source deployment; SSO; white-labeling; team spaces with centralized billing.
- Participant-added options; comments; notification subscriptions; REST APIs; exports.
- Anonymity depth (obfuscated names vs strong anonymous mode).

### L3 — Vendor-specific (research notes only)

- Doodle: auto-vote-yes for organizer on all proposed times; "Book it" with single-final-option rule; question-mark mismatch behavior after option edits; 1,000-respondent documented maximum; free tier limited to 1 group poll; paid gating of deadline/limits/reminders/hidden list/email invites/built-in email client; admin-link recovery; no un-invite (paid can delete/edit responses).
- Rallly: cookie-based response ownership + email magic link; Pro gating of email invites and Schedule; Lock time zone; Spaces model; self-host license tiers.
- Nextcloud Polls: confirm-after-close naming; calendar-conflict hints; Circles/Contacts/Activity integration; expiry; export formats; REST API; "similar to doodle" self-positioning.
- Outlook Scheduling Poll: existence of the embedded pole is a market anchor only this pass — no internal details asserted.

## Rejected Findings (not canonical)

- "Group availability = voting" — the yes/if-need-be/no ladder is common, but availability-grid marking (When2meet) and plain yes/no voting satisfy the Type; the invariant is availability declaration, not the specific vote ladder.
- "Group availability = email invitations" — link sharing satisfies participation everywhere; email is a channel variant.
- "Group availability requires accounts" — all four observed products support accountless participation; refuted.
- "Group availability produces a calendar event" — several products attach calendar invites on finalize (Doodle with connected calendar, Rallly), but the persistent object the Type owns is the poll and its chosen time, not a managed event/appointment record; When2meet-style flows end at the intersection view.
- "Sign-up sheets are this Type" — Doodle sells Sign-up Sheet as a distinct product; the semantics (claiming a slot among options) differ from declaring availability; kept adjacent, not merged.

## Boundary Findings

- **vs Meeting Scheduling Application (§03.09 sibling)**: meeting scheduling has an organizer with authority — a time is proposed and invitees accept/decline; booking links publish the organizer's *own* availability; the meeting record lands on calendars. Group availability derives the time *from* participant-declared availability. Test: if participants answer "when should it be?" → this Type; if they answer "can you attend at …?" → Meeting Scheduling. Removing participant-availability-declaration collapses this Type into meeting scheduling. (Meeting Scheduling leaf still unprocessed — joint review already flagged in STATUS boundary issues; this pass's evidence reinforces the availability-declaration discriminator.)
- **vs Appointment Scheduling Application (§03.09 sibling)**: appointment scheduling is a provider-side self-booking machine — service catalog, provider availability machinery, client-initiated booking into slots, persistent appointment record with lifecycle. Group availability has no provider, no bookable availability, no persistent booking; output is a chosen time. Persistent-appointment test ratified in the appointment pass; confirmed here (finalize closes a poll, it does not open an appointment record).
- **vs Interview Scheduling Platform (§09)**: interview scheduling maintains persistent managed interview records anchored to a hiring context, with interviewer-availability reconciliation and notification lifecycle. Confirmed from this side: nothing in the group-availability model is hiring-anchored or record-keeping.
- **vs Calendar Application (§03.08)**: calendars store and display personal time. This Type collects and compares multiple people's declared availability to *create* a new occasion. Calendar-embedded "suggested times"/free-busy features are meeting-scheduling semantics; removing the poll/participation loop leaves a calendar, not this Type.
- **vs Polling Application / Survey Platform (§03.11)**: a date poll is structurally a poll, and products self-describe with poll vocabulary. The distinguishing structure is the occasion focus: options are times for one event, the aggregate is an availability comparison, and the endpoint is a scheduling decision. Generic polling/survey tools answer arbitrary questions with no occasion context. The seam is thin enough that a generic poll tool can *host* a date poll — recorded as a boundary issue note (see STATUS).
- **vs Sign-up Sheet pattern**: participants claim/choose slots (attendance allocation) rather than declaring availability; Doodle treats them as separate products; adjacent, distinct.

**"去掉什么就变成另一个 Type" 判据汇总**：
- 去掉参与者自报可用性（时间由发起人指定，受邀人接受/拒绝）→ Meeting Scheduling Application
- 去掉"选出时间"这个终点、加入持久预约记录/服务目录/客户台账 → Appointment Scheduling Application
- 去掉时间选项与场合语境（任意问题任意选项）→ Polling / Survey
- 去掉多人可用性聚合（只管理个人时间）→ Calendar
- 加入招聘语境与面试记录 → Interview Scheduling Platform

## Uncertainties

- **Outlook Scheduling Poll**: platform-embedded pole not directly verified this pass (source unreachable). The final document describes the embedded pole structurally without Microsoft-specific claims.
- **Calendly meeting polls**: fresh evidence not obtainable; relies on the appointment pass's direct documentation. Conceptual-level only.
- **When2meet depth**: only the live grid surface observed; features beyond it (timezone behavior, exports) unverified.
- **Prevalence of the availability-grid style** vs option lists in the current market: sampled one pure grid product; direction (grid as minority style) is plausible but not measured.
- Historical naming (FindTime→Scheduling Poll, Dud-Poll, 2000s poll tools) comes from memory/context, was not verified against sources, and is not asserted in either document.

## Final Synthesis

The Type is best understood as **a group time-finding poll**: for one occasion that needs a time, an initiator creates a shared poll of candidate time options; every participant declares which options work for them (vote ladder or grid marking, without needing an account); the tool aggregates the declarations into a cross-participant availability comparison; and the group converges on one final option, which the tool announces (and commonly distributes as a calendar invite) while closing the poll. The output of the whole exercise is a chosen time — not a managed appointment record, not a provider's booking machine, not an organizer-imposed meeting. Mature products wrap this core with link/email distribution, response editing, reminders, deadlines, per-slot capacity caps, anonymity/visibility controls, timezone conversion, calendar-optional finalize mechanics, and team/self-host deployments; platform suites embed the same loop inside calendar and scheduling products. The three-sibling boundary is held by two tests: the availability-declaration test (vs Meeting Scheduling) and the persistent-appointment test (vs Appointment Scheduling).
