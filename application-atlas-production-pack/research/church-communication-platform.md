# Research Notes — Church Communication Platform

Research date: 2026-09-06
Leaf: Church Communication Platform (DIRECTORY.md §25 Nonprofit, Membership & Religious Organizations)
Slug: church-communication-platform

## Research Goal

Understand what a "Church Communication Platform" actually is as an Application Type: what objects exist inside it, how a church staff member uses it, how it relates to the neighboring leaves in §25 (Church Management System / ChMS, Church Giving Platform, Church Website Builder, Ministry Scheduling, etc.) and to generic messaging Types (Email Marketing Platform, SMS Marketing Platform, Employee Communication Platform).

## Initial Boundary (hypothesis before research)

- Hypothesis: software a church (or faith organization) uses to send managed messages to its congregation — email, SMS/text, sometimes voice or app push — with audiences drawn from people/membership data, plus scheduling, automation, and engagement tracking.
- Likely confusions:
  - Email Marketing Platform / SMS Marketing Platform (same message grammar, different audience substrate and job frame)
  - Church Management System / ChMS (the people/group record system; communication is often a module inside it)
  - Employee Communication Platform (§09) — internal staff comms vs congregation comms
  - Church Website Builder (public web presence vs targeted messaging)
  - Member Community Platform / Member Portal (member-facing surfaces vs organization-side sending)
- Key open question: is this leaf a distinct Type, or an audience/domain-specialized variant of email/SMS marketing?

## Research Questions

1. What are the core objects (people records, groups/lists, messages/notes, templates, schedules, keywords, connect cards)?
2. How does a typical send flow work (compose → audience → channel → schedule → send → track → reply)?
3. Which channels appear (email, SMS, voice broadcast, app push, calling) and how do their rules differ?
4. Where do audiences come from — member database, imports, ChMS sync, keyword opt-ins, connect cards?
5. What church-specific communication jobs appear (guest follow-up, volunteer coordination, prayer, event reminders, weather cancellations, giving campaigns)?
6. What rules matter (opt-in/opt-out, consent for texting, reply handling, permissions for who may send)?
7. What is the relationship to ChMS — standalone tool with integrations, module inside ChMS, or absent from some ChMS?
8. Historical check: do older forms (church email newsletters via generic tools, phone trees/prayer chains, printed bulletins) fit the same core?

## Representative Products

| Product | Posture | Tier of evidence |
|---|---|---|
| Text In Church | standalone church communication platform, texting-first (SMS + email + calling) | Tier 1 (marketing site + Intercom help center, multiple collections/articles) |
| Flocknote | standalone email+texting platform with group/note model; household database in higher tier; Catholic/diocesan segment | Tier 1 (marketing site + Help Scout help center, collections + articles) |
| Tithe.ly Messaging (inside Tithe.ly Church Management, formerly Breeze ChMS) | ChMS-embedded messaging module (email + SMS) | Tier 1–2 (dedicated product page with detailed FAQ; ChMS product page) |
| Planning Center | boundary anchor: large ChMS whose current product line has no dedicated communications product (People + Groups only); communication delegated to integrations | Tier 2 (site navigation; help index is a JS shell) |
| Subsplash | app-platform posture (church apps + push) — unreachable | none (2 timeouts; market anchor only) |
| Clearstream | texting-first standalone — blocked | none (403; market anchor only) |
| Gloo | drifted to broad "faith & flourishing ecosystem" platform (public company, AI, enterprises) | Tier 2 root page only; treated as market context |

Sample rationale: two standalone poles with different philosophies (texting-first vs note/group-first), one ChMS-embedded module, one ChMS-without-comms boundary anchor, plus app-platform posture via Tithe.ly Church App product page. Clearstream/Subsplash/Gloo recorded as market context only.

## Sources

Fetched 2026-09-06 (all successful unless noted):

- Text In Church — https://www.textinchurch.com/ (root: positioning, features, FAQ)
- Text In Church Help Center — https://help.textinchurch.com/en/ (collection index)
- Text In Church Help Center — Groups collection: https://help.textinchurch.com/en/collections/62510-groups
- Text In Church Help Center — Messaging collection: https://help.textinchurch.com/en/collections/62500-messaging
- Flocknote — https://www.flocknote.com/ (root: positioning, product scope)
- Flocknote Help Center — https://help.flocknote.com/ (collection index)
- Flocknote Help Center — Email & Text Basics category: https://help.flocknote.com/category/364-sending-emails-texts
- Flocknote Help Center — "What is a Note and how do I send one?": https://help.flocknote.com/article/18-what-is-a-note-and-how-do-i-send-one
- Tithe.ly — https://www.tithely.com/ (product line)
- Tithe.ly Messaging product page + FAQ — https://www.tithely.com/product/church-text-messaging-and-email
- Breeze ChMS — https://www.breezechms.com/ (rebrand notice: "Breeze has been rebranded as Tithely Church Management"; core feature list)
- Planning Center — https://www.planningcenter.com/ (product navigation; no communications product)
- Planning Center help index — https://help.planningcenter.com/en/index-en.html (JS shell, no content)
- Gloo — https://www.gloo.us/ (root only; ecosystem positioning)

Failed / abandoned (per source-access limitation rules):

- Subsplash — https://subsplash.com/ and https://subsplash.com/platform — timeout ×2 → abandoned; no claims rest on it
- Clearstream — https://clearstream.io/ — 403 → abandoned
- Planning Center /communications — 404 (product not in current nav)
- Breeze /features/text-messaging/ and Tithe.ly /products/engage — 404 (URL guesses; roots fetched instead)

## Product A — Text In Church (standalone, texting-first)

### Key observations (evidence layer A unless noted)

- Self-description: "#1 Trusted Communication Platform for Churches"; "one place to text, email, and call, so every person gets cared for"; "The leader in church communication technology."
- Product split: **Messaging** (SMS + email) and **Calling** (church phone line).
- Messaging features (site nav): Two-Way Texting, Automated Workflows, Integrations, Text A Keyword, Connect Cards, Email Sending, Video Messaging, Local Phone Number, Messaging Templates, Plan A Visit.
- **People**: people records with Logs tab ("track profile changes, syncs, and group updates"), Internal Notes ("tag members & leave contextual notes for better teamwork").
- **Groups**: create/edit/duplicate/remove/restore groups; Members tab with bulk actions; testimonial: "different groups of people that we can create in order to message to specific groups."
- **Messaging** (help center): Messaging Glossary; **Automated vs Scheduled Messages** ("the two types of messaging options"); Templates; **Opting in and out** (how to opt in/out and how to know if a person opted out); mobile app (iOS/Android); Multiple Inboxes (by phone number).
- SMS mechanics: one-time scheduled SMS; reply inbox ("check for New Messages… responding to the replies"); block a number; carrier filtering + deliverability best practices; Sent & Pending sections; export sent-message data as CSV; archive messages.
- Email mechanics: compose/address/send or schedule one-time email; images; reply-to address; newsletter-style email; opens/clicks tracking with an explicit caveat that opens/clicks are not an accurate delivery status.
- Personalization: merge fields ("have a name or info placed into the message automatically"); send to all people.
- **Automated Workflows**: "prebuilt follow-up sequences to every guest"; Wait Steps ("schedule messages a specific number of days later… deliver them on a specific day of the week").
- **Capture machinery**: Digital Connect Cards ("capture guest information instantly"); Text a Keyword ("guests respond in real time and enter your follow-up flow automatically"); QR Code builder (Tools collection).
- **Calling** (separate product): church number instead of personal cell; digital receptionist routing; direct extensions; smart voicemails with transcription; automated greetings; call forwarding; **Voice Broadcast** ("update your whole church").
- **Permissions**: "Account Users & Permissions let you add staff and volunteers to your account while controlling what they can see and do."
- **Integrations**: Planning Center ("real-time sync ensures your messages always reach the most up-to-date list"), Pushpay ChMS / Church Community Builder ("You've built the lists, and we'll send the messages for you"), Mailchimp, Rock RMS, Zapier, Tithe.ly Church Management, Elvanto, MinistrySafe, Open API.
- Use cases (site): follow up with guests, encourage prayer requests, re-engage community, invite new guests, enhance outreach, attract & nurture volunteers.
- Audience segments named on site: guests, members, volunteers, youth, staff; churches under/over 2,000 attendance; church plants; nonprofits.
- Sender identity: local phone number ("No spammy shortcodes around here"); web-based + mobile app.
- AI Messaging Tools exist (help article: "shorter, clearer messages").
- Vendor-specific (L3): message-count billing with per-message overage; Boomerang book / IGNITE framework / ENGAGE conference (content marketing); PastorsLine migration collection (PastorsLine accounts moved to TIC); Australia pricing page.

## Product B — Flocknote (standalone, note/group model)

### Key observations (evidence layer A)

- Self-description: "Church Communication, Online Giving and Household Database"; "Communication, household database, online giving and more – all in one place."
- Headline capability: "Unlimited Email & Texting — Communicate the inspiring things you're doing, reach your members (and hear back)." Two-way emphasis: "Reach your people, and hear back."
- **The Note is the message unit**: "A Note is what you send out to your people from Flocknote. Notes are text messages or emails, and can be sent to a single group, multiple groups, or just a few individuals." Sent via "Send an Email (Envelope icon)" or "Send a Text Message (Phone icon)".
- **Permission model tied to groups**: "To post new Notes to a Group, you must either be an admin over at least one Group." Groups: "Create unlimited groups, assign unlimited admins."
- **Members**: "Host a Signup Sunday, add individual members, or import in bulk"; member joins groups.
- **Note delivery**: "Will members get my message as an email or text?" — delivery mode resolved per member (email and/or text).
- **Note lifecycle**: compose (Email Note Composer / Text Message Note Composer), schedule ("How do I schedule a note to go out later?"), delete draft/sent/scheduled, templates + church-specific color/theme, pre-made content Library.
- **Return path**: comments section on notes; public vs private replies; notifications for new comments; **STOP replies** ("How do STOP replies work?"); "How do I stop texts or emails from being sent to me?" (member-side opt-out).
- **Analytics**: "Note Analytics (opens, unsubscribes, bounces, etc.)".
- **Sharing**: share a link to an email/text message with someone outside the group or network.
- Sending to individual members; sending to multiple groups.
- **Flocknote Complete tier** adds: "All-in-One Household database — All-in-one household database with communication at its core" (households, attendance tracking, parental contacts for children), Giving & Financial Tracking, Reports ("filter and track information on members, like attendance"), Word on Fire ENGAGE integration.
- Other modules: Registration & Event Signups ("Religious Education, Sacrament tracking, Sunday school, Family Registration, volunteer signups, ticket sales, event RSVPs, potlucks"), Signups/Events/Polls category (registrations, RSVPs, polls, surveys), Online & Mobile Giving (text-to-give, reply-to-give).
- Segment: "10,000+ churches", "50+ Diocesan and Archdiocesan partners in the U.S & Canada" — strong Catholic parish/diocesan posture; free migration of member + giving data.
- Vendor-specific (L3): Word on Fire ENGAGE partnership; employee-owned positioning; diocese partner program; Starter vs Complete packaging.

## Product C — Tithe.ly Messaging (ChMS-embedded module)

### Key observations (evidence layer A for the product page + FAQ)

- Positioning: "Text messaging service for churches… With the messages features in Tithely Church Management you can text and email your congregation instantly—whether it's a last-minute update, a volunteer reminder, or a quick word of encouragement."
- "Tithely Messaging is a church text messaging software and email newsletter tool packed in one simple to use solution… communicate with visitors, congregation members, volunteers, staff, and regular attenders… store contact information, send a text or email directly, create lists, send follow-ups."
- Features: Unlimited Emails; monthly text allowance with paid overage (exact numbers = L3); drag-and-drop email editor + pre-built templates + mail merge fields; **Group Targeting** ("send messages to specific roles, groups, or the entire church in just a few clicks"); **Email Delivery Tracking** ("See what was delivered, what bounced, and keep your list clean"); **Send Now or Schedule Later**.
- **Keyword opt-in**: "You can set up specific keywords that your members or guests can text. This will trigger a response where people can update their contact info, be added to a list, and even trigger a follow-up sequence. For example, if a guest… texted the word 'NEW,' the system could add them to a list called 'Visitors' and start an automatic follow-up sequence."
- Lists: "create and send follow-ups to lists of people or… send a mass message (eg. text blasts) to your entire database"; import contact lists from Tithe.ly ChMS or other services.
- Return path: inbound messages don't count against quota; "small green 'sent ✓' next to the message" as received indicator.
- Admins: "Set as admin" on contacts.
- Sender identity: church email address on the product's domain (@messaging.church); 800 number rather than local number for SMS blasts (vendor rationale: local numbers flagged as spam); no custom domains; no existing-number porting.
- Regional availability: email in US/Canada/Australia; SMS only US/Canada (L2/L3).
- Context: Breeze ChMS rebranded as "Tithely Church Management" — same product; Breeze core feature list includes Text Messaging, Unlimited Emails, People, Groups, Events, Forms, Check-in, Member Directories, Mobile App.
- Tithe.ly Church App (separate product): "Two-Way Push Notifications", "Groups with Chat", "Prayer Wall" — the app-platform posture for congregation communication (evidence layer A, Tier 2 product page).
- Vendor-specific (L3): exact text quotas/pricing; 160-character SMS segmentation explanation; All Access bundling; @messaging.church domain.

## Product D — Planning Center (boundary anchor: ChMS without a comms product)

### Key observations (evidence layer A for navigation, Tier 2)

- Current product navigation: People ("Free membership database"), Groups ("Community engagement & chat"), Calendar, Registrations, Check-Ins, Services, Music Stand, Church Center ("Custom mobile app for your church"), Publishing, Giving, Home, App, AI. Category heading "People & Communication" contains People and Groups — no standalone messaging/campaign product.
- Church Center (member-facing app): "Check in kids, view volunteer schedules, chat with group members, register for events, submit prayer requests, and give."
- Changelog shows per-product email features (Calendar emails, Giving emails, Services emails) — email used as a notification mechanism inside modules, not a congregation-messaging product.
- Third-party communication tools integrate with it: Text In Church advertises "real-time sync… your messages always reach the most up-to-date list" via Planning Center integration.
- Interpretation: a major ChMS can ship **without** a dedicated congregation-messaging product; the communication loop is then supplied by standalone platforms syncing people/lists from the ChMS. This supports treating "Church Communication Platform" as its own center of gravity (the communication loop), not merely a ChMS submodule.
- Uncertainty: whether a "Planning Center Communications" product existed historically and was retired was NOT verified; no claim made either way.

## Cross-product Comparison

| Structure | Text In Church | Flocknote | Tithe.ly Messaging | Planning Center (anchor) |
|---|---|---|---|---|
| Organization sender identity | church phone number (+ email) | church account; per-group sending | church 800 number + @messaging.church address | n/a (no comms product) |
| People records | People (logs, internal notes) | Members (+ households in Complete) | Contacts/lists; import from ChMS | People (membership DB) |
| Audience container | Groups (CRUD, members tab, bulk actions) | Groups (unlimited; group admins) | Lists; roles/groups/entire church | Lists in People |
| Message unit | message (SMS/email/voice broadcast/video) | **Note** (email or text) | message (SMS/email) | — |
| Channels | SMS, email, voice broadcast, video messaging, calling | email, text | email, SMS | — |
| Send modes | one-time scheduled + automated workflows (sequences, wait steps) | one-time scheduled | send now or schedule; follow-up sequences | — |
| Return path | two-way inbox, multiple inboxes, archive, block | comments (public/private), STOP replies | replies (free), sent ✓ indicator | — |
| Opt-in capture | keywords, digital connect cards, QR | Signup Sunday, member joins group | keywords → list + follow-up | — |
| Opt-out | explicit opt-in/out management | STOP replies; member self-stop | (implied by SMS rules; not detailed) | — |
| Tracking | sent/pending views, CSV export, email opens/clicks (caveated) | note analytics (opens, unsubscribes, bounces) | delivery tracking (delivered/bounced) | — |
| Templates/content | messaging templates | templates + pre-made content library | drag-drop editor + templates + merge fields | — |
| Personalization | merge fields | (not observed) | mail merge fields | — |
| Permissions | account users & permissions | group-admin model (must admin ≥1 group to send) | set-as-admin contacts | — |
| ChMS relationship | integrations (Planning Center, CCB, Rock RMS, Mailchimp, Zapier, Tithe.ly ChMS, Elvanto, API) | is the database (Complete tier) | built into ChMS | ChMS without comms product |
| Extras | calling product, AI messaging tools | giving, signups/polls/events, reports | church app w/ push, prayer wall | church center app, per-module emails |

### Convergent findings (evidence layer B — cross-product commonality)

1. **Organization-operated sending identity** — all three documented products give the church its own sending identity (phone number and/or email address) distinct from any staff member's personal devices.
2. **People records as the audience substrate** — recipients are identified individuals (members, visitors/guests, volunteers, staff) held as records in the same system or synced from a ChMS.
3. **Groups/lists as audience containers** — every product organizes people into named audiences (Groups in TIC and Flocknote; Lists + roles in Tithe.ly) and sends to one or many.
4. **Email + SMS as the base channel pair** — all three support both; additional channels (voice broadcast, video messaging, calling, app push) vary.
5. **Compose → schedule → send → track** — one-time sends with scheduling exist everywhere; automation/sequences in most.
6. **Managed return path** — replies/comments captured in-system; opt-out (STOP/unsubscribe) handled in-system.
7. **Opt-in capture machinery tied to church life** — keywords and connect cards/signups (TIC, Tithe.ly; Flocknote's Signup Sunday) turn in-person contact into audience membership.
8. **Templates + personalization** — reusable message templates and merge fields.
9. **Permissions for who may send** — account users/permissions (TIC), group admins (Flocknote), admins (Tithe.ly).
10. **ChMS interplay** — either integrated (TIC), embedded (Tithe.ly), or absent-with-delegation (Planning Center). The communication loop is a distinct center of gravity.

### Divergent findings

- Message-unit philosophy: Flocknote's Note (one object, delivered as email or text per member preference, with comments) vs TIC/Tithe.ly's channel-specific messages.
- Calling as a product line (TIC only in sample).
- Database depth: Flocknote Complete and Tithe.ly ChMS carry households/attendance/giving; standalone TIC keeps people records light and syncs from ChMS.
- Sender-identity rules differ (local number vs 800 number vs shortcode; product domain vs custom domain) — implementation detail, not structure.
- Segment shapes: Flocknote Catholic/diocesan; TIC evangelical church-plant/growth posture; Tithe.ly giving-first bundle.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

A Church Communication Platform is definable by four properties. Remove any one and the product stops being recognizable as this Type:

1. **Organization-operated sending identity** — the church (parish/ministry) itself is the sender, with its own message identity (phone number and/or email address) operated from the application, not a staff member's personal account.
2. **People-based audience drawn from the church's own people** — recipients are identified individuals (members, guests/visitors, volunteers, staff) held as records in the system or synced from a church database, and audiences are selected from those records (groups/lists/segments), not from anonymous subscriber lists.
3. **Composed outbound message as a managed object** — messages are composed in the application, optionally scheduled, and delivered over message channels (email and SMS being the base pair).
4. **Managed return path** — replies and opt-outs from recipients are captured and handled within the same system (the loop closes: send → hear back → honor opt-out).

§24 historical check: the pre-software forms map onto this core — the church office newsletter (organization → member list → message), the phone tree/prayer chain (organization-initiated voice contact with a return path), the bulletin with a reply card (message + response mechanism). A church using a generic email-marketing tool performs the same *job* but the *product* is not purpose-built around congregation records, church-life capture, or pastoral return paths — that distinction is what separates the Type from the tool used incidentally. The four properties hold across old and new forms.

### L1 — Common Mature Structure

Present in essentially all mature modern products; not required for the definition:

- Groups/lists with membership management (create/edit/duplicate/restore; bulk member actions; member joins via signup or import)
- ChMS integration or embedding (people/list sync; "most up-to-date list")
- Templates + content library; personalization/merge fields
- Scheduling (send now or later); automated follow-up sequences with timed steps
- Two-way inbox (reply handling, archiving, blocking, multiple inboxes)
- Delivery/engagement tracking (sent/delivered/bounced/opens/unsubscribes) + export
- Opt-in capture machinery: text-a-keyword, digital connect cards/forms, QR codes, signup events
- User accounts & permissions (staff + volunteers; group-admin model)
- Mobile app for staff; web console as primary surface

### L2 — Variant / Optional Structure

- Calling/phone-system layer (church number, digital receptionist, extensions, voicemail transcription) — one sampled product
- Voice broadcast — one sampled product
- App push notifications via church app platforms (Tithe.ly Church App; Subsplash posture) — push as a channel variant
- Video messaging — one sampled product
- Database depth: household database, attendance, giving/donor tracking attached to the same people records (Flocknote Complete; ChMS-embedded products)
- Attached engagement objects: signups, RSVPs, polls, prayer walls
- Denominational/segment shapes: Catholic parish/diocesan hierarchies; church plants; multi-campus; nonprofits
- Regional availability and sender-identity regimes (local vs toll-free vs shortcode; product-domain vs custom-domain email)
- AI assistance (message drafting/shortening)
- Packaging: standalone subscription vs ChMS module vs all-in-one bundle

### L3 — Vendor-specific (research notes only)

- Text In Church: per-message overage billing; Wait Steps; Boomerang/IGNITE/ENGAGE content programs; PastorsLine account migration; Australia pricing; "no spammy shortcodes" positioning.
- Flocknote: Note terminology; Word on Fire ENGAGE; employee-owned story; diocese partner program; free data migration; Starter vs Complete packaging.
- Tithe.ly: exact text quotas and overage pricing; @messaging.church domain; 800-number-only SMS rationale; 160/153-character segmentation; All Access bundling; Breeze rebrand.
- Planning Center: per-module email notifications; Church Center app details; changelog cadence.
- Subsplash/Clearstream/Gloo: unreachable or out-of-scope; no claims.

## Vendor-specific Findings

See L3 above. None of these entered the canonical model.

## Boundary Findings

1. **vs Email Marketing Platform / SMS Marketing Platform (§06)** — closest grammar match: both compose messages, manage lists, schedule, track, honor unsubscribe. Distinguishing structure of this Type: the audience substrate is the church's own people records (membership/attendance/group context, often synced from a ChMS), consent is captured through church-life mechanisms (keywords, connect cards, group membership), and the message jobs are congregational (guest follow-up, volunteer coordination, prayer, care) rather than commercial promotion. A church using a generic marketing tool is doing the job without the Type's product. **Flag: probable audience/domain-specialized sibling relationship — joint review recommended.**
2. **vs Church Management System / ChMS (§25 sibling)** — ChMS is the record system (people, groups, events, giving); this Type is the communication loop over those records. The market forms a spectrum: standalone comms tools with ChMS integrations (Text In Church), ChMS-embedded messaging modules (Tithe.ly), and ChMS with no comms product that delegate to integrations (Planning Center). Remove the sending loop → ChMS; remove the people-record substrate → generic email/SMS marketing.
3. **vs Employee Communication Platform (§09)** — that Type targets an organization's workforce with internal-comms semantics; this Type targets a congregation (members + guests + volunteers) with pastoral/organizational semantics. Volunteer/staff messaging overlaps but is a subset job here.
4. **vs Member Community Platform / Member Portal (§25 siblings)** — those are member-facing surfaces (content, community, self-service); this Type is organization-side sending with a return path.
5. **vs Church Website Builder (§25 sibling)** — public web presence vs targeted messaging to known people.
6. **vs Business Messaging Application / Customer-to-Business Messaging (§01.01)** — commercial conversation between business and customer vs congregational broadcast + care; different identity frame (brand ↔ customer vs church ↔ member/guest).
7. **vs Event Management / Ministry Scheduling (§25 siblings)** — event reminders are a message job of this Type; the event/schedule record belongs to those Types.
8. **"Remove what to become another Type" tests**: remove the congregation people-substrate and church-life capture → Email/SMS Marketing Platform; remove the sending loop → ChMS; remove the organization sender (personal 1:1 threads) → Instant Messaging; remove the return path and people records (anonymous broadcast) → mass-notification/blasting tool, not this Type.

## Uncertainties

- Subsplash unreachable (timeout ×2): the app-platform posture (push-centered congregation communication) is evidenced only through Tithe.ly Church App's product page; Subsplash-specific structure unknown.
- Clearstream blocked (403): the "second texting-first product" was not documented; texting-first commonality rests on Text In Church + Tithe.ly FAQ + market context (TIC's own comparison pages list Clearstream/Flocknote/Gloo/PastorsLine as peers).
- Planning Center: current absence of a communications product is verified from navigation; any historical "Communications" product was not verified — no claim made.
- Flocknote Starter automation depth (whether sequences exist outside Complete) not verified; kept generic.
- Exact numeric limits (message quotas, character limits, group-size caps) are vendor-specific and were deliberately kept out of the final document.
- Opt-out handling for Tithe.ly SMS was not explicitly documented on the fetched page (implied by SMS norms and keyword mechanics); assertion kept weak in the final document.

## Final Synthesis

A Church Communication Platform is the church-side communication loop: the organization operates a sending identity, selects audiences from its own people records (grouped into lists/groups), composes and schedules messages over email/SMS (plus optional voice/push/video channels), and manages the return path — replies, comments, and opt-outs — in the same system. Around that loop, mature products add capture machinery that turns church life into audience membership (keywords, connect cards, signups), automation for follow-up, templates, tracking, permissions for staff and volunteers, and either integration with or embedding inside a church management system. The Type's center of gravity is the loop itself, which is why it exists both as standalone products beside ChMS offerings and as modules inside them — and why at least one major ChMS ships without it, delegating the loop to integrated specialists.
