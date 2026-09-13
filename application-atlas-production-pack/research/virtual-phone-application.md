# Research Notes — Virtual Phone Application

Research date: 2026-09-09
Directory leaf: Virtual Phone Application (§01.03 Voice & Calling)
Slug: virtual-phone-application

---

## Research Goal

Understand what a Virtual Phone Application actually is as an Application Type — from real products, not from the "virtual phone number" marketing label — so that a reader who has never used one can understand its core structure, how it is used, and where its boundaries lie against neighboring calling Types (Internet Calling Application, Softphone Application, Conference Calling, Push-to-Talk, Contact Center).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: the core object is a **real telephone number operated as a software line** — held by a service, used through an app over the internet, on devices the user already has, separate from a carrier SIM line.
- Likely users: individuals wanting a second/private number; small businesses wanting a business line without hardware or carrier contracts.
- Nearest neighbors: Internet Calling Application (service-account identity), Softphone Application (enterprise PBX client), second-SIM products, Contact Center (organizational queues).
- Open questions going in: Is SMS definitional or common? What are the number lifecycle rules (acquire / hold / expire / port)? Where exactly is the line between this Type and internet calling / softphone / contact center?

## Research Questions

1. What exactly is the managed object — how is the number acquired (choose area code, toll-free, vanity, port-in), and what is its relationship to the user's carrier line?
2. What does the number do: inbound/outbound calls, SMS/MMS, voicemail, transcription, forwarding?
3. How do calls and texts actually flow — over what connection, on which devices, with what caller-ID presentation?
4. What is the number's lifecycle: active, expired, deleted, ported out? What happens to history?
5. Personal vs shared use: one user with multiple numbers vs a team sharing one number; what roles exist?
6. What rules matter: retention/expiry, porting, caller ID, carrier registration/compliance, verification-code limitations, acceptable use?
7. What interfaces do users actually operate: dialer, message inbox, voicemail, call history, settings, web/desktop/mobile?
8. Where are the boundaries: vs internet calling, vs softphone, vs contact center, vs second SIM, vs disposable-number/verification services?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Why selected |
|---|---|---|
| Grasshopper | classic small-business "virtual phone system" | the category's long-standing SMB archetype; number + extensions + forwarding |
| Quo (formerly OpenPhone) | modern SMB shared-number platform | richest current Tier-1 documentation; team/shared-number philosophy |
| Burner | consumer privacy second number | "second number app" archetype; disposable/switchable numbers |
| Hushed | consumer temporary/private numbers | prepaid/expiry lifecycle pole; international area codes |
| Google Voice | consumer/prosumer market anchor | biggest consumer virtual-number service — **unreachable in this environment (see Sources)** |

TextNow (free consumer VoIP line pole) was also considered but unreachable (403 ×2).

## Sources

Fetched 2026-09-09:

- Grasshopper — https://grasshopper.com/ (home), https://grasshopper.com/features/voip-phone-system (Tier-2 product/feature pages; support center at https://support.grasshopper.com/ returned only a JS shell title)
- Quo / OpenPhone — https://www.quo.com/ (home; brand renamed from OpenPhone to Quo per Sept 2025 changelog), https://support.quo.com/ (Tier-1 help center incl. llms.txt index), https://support.quo.com/core-concepts/phone-numbers/overview (Tier-1)
- Burner — https://www.burnerapp.com/ (home), https://www.burnerapp.com/how-burner-works, https://support.burnerapp.com/ (support center root + "Managing your Burners" category; individual articles not fetched)
- Hushed — https://hushed.com/ (home), https://support.hushed.com/ (Tier-1 help center root), https://hushed.zendesk.com/hc/en-us/sections/360002177311-Numbers (Numbers section), https://hushed.zendesk.com/hc/en-us/articles/360015502732 (Number Expiry article, Tier-1)

**Source-access limitations:**

- Google Voice: https://support.google.com/voice/ and https://voice.google.com/about both timed out (×2 each domain). Abandoned per network rules. Google Voice is retained as a market anchor only; **no operational claims** about it are made in the final document. Indirect Tier-1 evidence from Quo's side: Quo publishes port-out guides for Google Voice numbers, confirming such numbers are portable — nothing more.
- TextNow: https://www.textnow.com/ and https://support.textnow.com/ returned 403 (×2). Abandoned. The free-consumer-line pole is therefore under-sampled; assertions about "free/ad-supported" economics are NOT made.
- Grasshopper support center is JS-rendered; only its title fetched. Grasshopper evidence is Tier-2 (product/feature pages), not Tier-1 help articles.
- Burner individual support articles not fetched (category listing only); Burner lifecycle rules are asserted at the level the category structure supports (prepaid vs subscription numbers, burning/changing numbers, message retainment as documented topics).

---

## Product Observations

### Grasshopper (Tier-2: product + feature pages)

Evidence layer: A (directly observed on official pages)

- Self-positioning: "virtual phone system that separates business calls, messages, and contacts from personal ones"; "business phone app for entrepreneurs"; priced/positioned for small business.
- Number acquisition: pick a custom number — toll-free, vanity, or local — or port an existing number in.
- Line operation: VoIP/Wi-Fi calling — "make and receive business calls using any internet connection — no landlines or cell service required"; mobile app (turn on Wi-Fi Calling) and desktop app (VoIP by default).
- Structure around the number: customized **extensions** for employees/departments, each with its own call-forwarding options; multiple users; "share one number across your entire team"; additional numbers as paid add-ons.
- Communication surface: calls, texts, and voicemails "together in a single conversation thread for each contact"; business SMS on the business number; voicemail delivered as audio to email + voicemail transcription; instant text response (auto-text to missed callers); virtual fax (receive faxes as PDF).
- Inbound control: call forwarding (to personal phone or another team member), call recording (automatic, per extension), custom greetings, business hours routing, incoming call control (screen/block/schedules), simultaneous calls, call blasting (add-on).
- Admin: setup assistant (extensions, greetings, call flow, permissions), contacts management with dedicated business lists, reporting.
- Apps: iOS, Android, desktop.

### Quo / OpenPhone (Tier-1: help center)

Evidence layer: A (directly observed in official operational documentation)

- Self-positioning: "shared business phone and inbox… one place for every call, text, and customer"; rebranded from OpenPhone to Quo (changelog 2025-09-22).
- Phone numbers (core-concepts/phone-numbers/overview):
  - Add **unlimited** numbers to an account; additional numbers purchased or ported, attached to the subscription as "slots".
  - Search numbers by city name, area code, or toll-free option.
  - Types: local (US — every state except Alaska; Canada — all provinces; Puerto Rico port-in only), North American toll-free (800/833/844/855/866/877/888 prefixes, all text-enabled), **no international numbers** (US/Canada only).
  - Numbers can be named and given emojis; names/emojis appear with incoming calls.
  - **Deleting a number permanently removes all data associated with it** (call and messaging history); deletion doesn't cancel the subscription — the slot stays billable until renewal, can be reused free, or left empty.
  - Porting: in (from carriers and from Google Voice/RingCentral/Dialpad/Grasshopper/Aircall/Verizon/AT&T/T-Mobile/NumberBarn) and out (dedicated porting-out page).
- Carrier registration: A2P 10DLC registration (business and sole-proprietor paths) required for text delivery/anti-filtering; toll-free registration for messaging compliance.
- Calling: make/receive calls; caller ID name setup ("increase answer rates"); call recording (manual + automatic); call transfer (cold/warm/with notes); hold; call waiting; conference calling (up to 10 participants); international calling via pre-paid credits; SHAKEN/STIR spam-label protection; click-to-call; call-quality metrics.
- Call flows (admin): visual call-flow builder; business hours; voicemail (greetings, transcriptions, routing); phone menu (IVR); ring groups (ring strategies/orders); call forwarding (external numbers, answering services); play-audio steps; temporary call flows; contact routing (different handling for saved contacts vs new callers).
- Messaging: SMS/MMS; group messaging (up to 9 people); scheduled messages; snippets; reactions; international messaging; opt-out handling; deliverability best practices.
- Team collaboration: **shared numbers / inbox sharing** ("share phone numbers with team members"); internal threads on calls/messages/voicemail; team messaging (internal DMs); tasks; roles/permissions (admin/owner required to delete shared numbers); groups; analytics; work schedules/statuses.
- Contacts: custom properties, notes, sharing, import (CSV/Google/device), blocking.
- Trust/compliance: HIPAA-ready on Business/Scale plans; SOC 2 Type II; data export.
- AI layer: Sona AI voice agent (answers calls 24/7, transfers to team), AI call summaries/transcripts/tags, auto-replies, AI contact suggestions.

### Burner (Tier-2: product pages + support-center structure)

Evidence layer: A (directly observed on official pages)

- Self-positioning: "Your phone's other number"; "the original second phone number app, built to maintain your privacy, organize your social circles, and protect your anonymity."
- Multiple numbers per user: "create different numbers for different types of contacts" (work, family, selling, dating); documented cap of 3 numbers on the consumer product (marketing page).
- Number lifecycle: **delete or switch numbers** ("burning" a number); changing your number; prepaid numbers vs subscription numbers (documented distinction in support center); "Can I keep my Burner forever?" as a support topic; message-retainment rules when changing numbers; lost-number recovery.
- Communication: unlimited calls & texts; picture messages; voicemail per line; auto-reply texts; muting & blocking; spam blocking; contacts organized by color/labels.
- Privacy framing: the Burner number protects the primary number; anonymity controls (who can reach you, when — blocking, do-not-disturb).
- Variant surface: a **Dual SIM** support category — a second iPhone number tied to the device's SIM hardware, managed through the app (SIM-realized line as an alternative substrate); "Verified Numbers" subscription category.

### Hushed (Tier-1: help center + Tier-2 home)

Evidence layer: A (directly observed in official operational documentation)

- Self-positioning: "Second phone numbers. Call and text on temporary phone numbers in one easy-to-use app"; local numbers from 300+ area codes in the US, Canada, UK (multiple countries).
- Line operation: "Make calls and send texts over Wi-Fi or mobile data"; "Hushed works over the internet, so it doesn't rely on traditional cellular" (support article); VoIP calling with restricted-country list.
- Number lifecycle (Numbers section + expiry article):
  - Buy numbers; prepaid and pay-as-you-go numbers carry an **expiry date** set at purchase (package-defined spans, e.g. 7/30/90/365 days); extendable any time via Number Settings.
  - On expiry: restoration not guaranteed; **call history, voicemails, and message conversations remain accessible** on the expired number but no new calls/texts can be made/received; remaining minutes/SMS are deleted.
  - Deleting numbers; changing/swapping numbers; restoring accidentally deleted or expired numbers; trial numbers; "lifetime numbers" promotion; vanity numbers (choose digits); port-in supported; multiple numbers per account; naming numbers.
- Privacy behaviors: recipients see only the Hushed number ("No other information is shared"); the number is managed entirely in the app and has no effect on the real phone number (uninstall-safe).
- **Verification-code limitation**: third-party verification codes / 2FA (e.g. WhatsApp, Uber) generally do NOT work on Hushed numbers — documented as a known limitation.
- Other: auto-reply messages; multiple devices (up to 5 per account); separate contacts; custom voicemail greetings; call forwarding; call routing; account suspension for abuse; harassment/spam reporting.

### Google Voice (market anchor only — no direct evidence)

- Not fetched (timeouts ×2). Retained in the sample as the consumer/prosumer market anchor. The final document makes no operational claims about it. (Indirect: Quo documents porting numbers out of Google Voice.)

---

## Cross-product Comparison

| Dimension | Grasshopper | Quo/OpenPhone | Burner | Hushed |
|---|---|---|---|---|
| Managed object | real business number (local/toll-free/vanity) or ported-in | real numbers (local US/CA, N.A. toll-free) or ported-in | real second numbers ("burners") | real numbers, 300+ area codes, multiple countries |
| Acquire | choose from inventory / port in | search by city/area code/toll-free / port in | choose number in app | buy in app / port in / trial numbers |
| Calls over internet | VoIP/Wi-Fi calling, no landline/cell required | app calling on mobile/desktop/web | app calls & texts | VoIP over Wi-Fi/data, "doesn't rely on traditional cellular" |
| Caller ID | business number presented | caller ID name configurable | Burner number presented | recipients see only the Hushed number |
| SMS/MMS | business SMS on the number | SMS/MMS, group (≤9), scheduled, snippets | unlimited texts, picture messages | SMS & MMS |
| Voicemail | voicemail → email audio + transcription | voicemail greetings/transcription/routing in call flows | voicemail per line | custom voicemail greetings |
| Unified history | calls+texts+voicemails in one thread per contact | shared inbox, call views, conversation states | inbox per number; message retainment rules | history persists on expired numbers |
| Multiple numbers | paid additional numbers | unlimited numbers, named/emoji'd, slot-based | up to 3 (consumer) | multiple numbers per account |
| Number lifecycle | port in/out; plan-bound | delete (data destroyed) / port out; slot economics | burn / change / switch; prepaid vs subscription | buy / extend / expire / restore / swap / delete |
| Sharing | one number across team; extensions per user | shared numbers/inboxes, roles, internal threads | personal (no team layer observed) | personal (multi-device, no team layer observed) |
| Routing machinery | forwarding, greetings, business hours, call blasting | call-flow builder, IVR, ring groups, business hours, forwarding | auto-reply, DND, blocking | auto-reply, forwarding, call routing |
| Compliance/regulatory | — | A2P 10DLC registration, toll-free registration, SHAKEN/STIR, HIPAA/SOC 2 | — | verification-code limitation documented; abuse suspension |
| Business model | subscription (SMB) | subscription + number slots + usage credits | prepaid numbers + subscriptions | prepaid packages with expiry + subscriptions |

**Cross-product commonalities (Layer B):**

1. Every sampled product's central object is a **real telephone number** held/operated by the service — chosen from an inventory or ported in.
2. Every sampled product operates the line **through an app over the internet** (VoIP/Wi-Fi/data), explicitly contrasted by vendors with landlines/cell service/SIM dependence.
3. Every sampled product presents the virtual number as the **outbound caller identity** and receives inbound calls/texts on it.
4. Every sampled product carries **SMS/MMS on the number** alongside calls.
5. Every sampled product keeps **per-number history** (calls, messages, voicemail) that persists with the number.
6. Every sampled product supports **multiple numbers** in one account.
7. Every sampled product has **blocking/muting/spam controls** and **auto-reply**-class automation.
8. Every sampled product has a **contacts layer** bound to the line's communications.
9. Number **portability** (in, and commonly out) appears across the business pole and the consumer pole (Hushed port-in; Quo in/out; Grasshopper in; Burner prepaid/subscription mechanics).

**Divergences (variant axes, not Type structure):**

- Who uses the line: one person (Burner, Hushed) vs a team sharing numbers (Quo, Grasshopper).
- Line tenure: disposable/short-lived with prepaid expiry (Hushed prepaid, Burner prepaid) vs standing subscription line (Quo, Grasshopper, Burner subscription).
- Routing depth: none-to-auto-reply (consumer pole) vs extensions/IVR/ring-groups/call-flows (business pole).
- Regulatory machinery: A2P 10DLC/toll-free registration, SHAKEN/STIR, HIPAA (Quo — US business texting compliance); absent from consumer-pole documentation.
- Substrate realization: pure app/VoIP (all) vs SIM-tied second line managed by the app (Burner Dual SIM category).
- Geography: US/Canada-only inventories (Quo) vs multi-country area codes (Hushed).

---

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

A Virtual Phone Application is an application through which the user operates a **real, publicly dialable telephone number as a software-managed line**:

1. **A real telephone number as the managed object** — a number that is reachable from the public phone network and presents itself as caller ID, acquired from the service's inventory or ported in, and held by the service rather than bound to a SIM subscription the user operates. *(Remove → internet-calling territory, where identity is a service account; or a plain dialer.)*
2. **App-operated line over the internet** — the number's calls (and commonly messages) are placed, answered, and managed inside the application, carried over an internet connection, on devices the user already has. *(Remove → a second SIM/carrier line, or a forwarding service with no operating surface.)*
3. **A persistent held line with its own record** — the number persists as the user's standing, addressable line, accumulating its call/message/voicemail history until it is released (deleted, expired, or ported out); it is a line, not a per-call session. *(Remove → ephemeral calling/messaging, not a phone line.)*

Jointly-held load-bearing analysis:

- 1 alone = a number-inventory/rental service (DID warehouse; verification-number service) — no communication.
- 2 without 1 = an internet calling application (service-account identity).
- 3 without 1+2 = a contact entry in a directory.
- 1+2 without 3 = a per-call disposable relay, not a line.
- 1+3 without 2 = a call-forwarding virtual number (the conceptual ancestor — number held, no operating surface).
- 2+3 without 1 = a calling/messaging app with ephemeral identity.

### L1 — Common Mature Structure (present across the sample, not definitional)

- SMS/MMS texting on the number (4/4 sampled).
- Voicemail with greeting; voicemail transcription (business pole; greetings on consumer pole).
- Unified per-contact conversation view (calls + texts + voicemail together) and call/message history.
- Contacts layer bound to the line (separate from the device's personal address book in the consumer pole; shared/team contact database in the business pole).
- Blocking, muting, spam controls; auto-reply texts.
- Multiple numbers per account; naming/labeling of numbers.
- Number porting (in; out documented at the business pole).
- Multi-device and desktop/web companions of the same line.

### L2 — Variant / Optional Structure

- **Audience variant**: personal second-number (privacy, selling, dating, travel) vs small-business line (professional presence, customer communication) vs team-shared numbers with roles/internal threads.
- **Line-tenure variant**: prepaid/expiring numbers vs subscription lines vs "lifetime" numbers.
- **Routing depth**: auto-reply only ↔ extensions ↔ IVR/auto-attendant, ring groups, business hours, visual call-flow builders.
- **Number kinds**: local, toll-free, vanity; country coverage varies sharply by vendor.
- **Regulatory machinery** (region/segment): A2P 10DLC carrier registration, toll-free registration, SHAKEN/STIR, HIPAA posture — US business-texting compliance in the sampled business pole.
- **Substrate realization**: pure app/VoIP vs SIM-tied second line managed through the app (documented variant at one sampled product).
- **Adjacent capabilities**: call recording, conference calling, international calling/credits, fax (present at one vendor, explicitly absent at another), CRM/integration/API layers, AI answering agents and call summaries (era-current).

### L3 — Vendor-specific (research notes only; excluded from the final document)

- Grasshopper: $14/mo entry framing; $3/mo per additional extension; $9/mo per additional number; $75 professional voice-actor greetings; call blasting add-on; virtual receptionist add-on; "Google Voice can't match" comparative marketing.
- Quo/OpenPhone: Sona AI agent (24/7 answering, jobs, SMS lead capture); group messaging cap of 9; toll-free prefix list (800/833/844/855/866/877/888); Alaska/Puerto Rico availability exceptions; number "slot" billing mechanics; "Danger Zone" deletion flow with typed confirmation; MCP/API/webhook surfaces; HIPAA on Business/Scale plans only; Sept 2025 rebrand OpenPhone→Quo.
- Burner: consumer cap of 3 numbers; "Verified Numbers" subscription; Dual SIM category; credits purchasing; message-retainment specifics; "Can I keep my Burner forever?" policy article.
- Hushed: 5-device limit; prepaid expiry spans (7/30/90/365 days as package examples); lifetime-number promotion; VoIP restricted-country list; verification-code (2FA) non-receipt limitation; account-suspension policy.

---

## Vendor-specific Findings

(See L3 above — all retained here, none promoted to the canonical document.)

Notable single-product behaviors that must NOT be generalized:

- Quo's "deleting a number permanently destroys its data" is Quo-documented; Hushed documents the opposite pole for expiry (history stays accessible on an expired number). The canonical rule is therefore stated as "release of the number ends the line; what happens to the history is product-defined."
- Hushed's verification-code limitation is Hushed-documented; it is recorded as a consumer-pole behavior, not a Type rule.
- Burner's Dual SIM mode is a substrate variant, not the Type's mechanism.

## Boundary Findings

| Neighboring Type | Boundary test | Distinction |
|---|---|---|
| Internet Calling Application | Remove the real PSTN number; identity becomes a service account | Internet calling connects service users; PSTN breakout is an optional metered layer. Here the real number IS the managed object and the identity. Counterparty (internet-calling pass) already records: "the managed object is a phone number… calling is one use of the number, not the core." |
| Softphone Application (unprocessed leaf) | Ask who owns the telephony estate | A softphone is a client of an organization's PBX/UC system — the number/extension belongs to the employer's telephony estate and the user is an employee agent. A virtual phone line is provisioned directly by the service to an individual or small team, with no PBX estate behind it. Flag for the softphone pass to treat this document as counterparty context. |
| Conference Calling Application | Party count and bridge semantics | Conference calling centers a shared multi-party bridge with join addresses and host controls; a virtual phone line is a personal/small-team two-way line. Conference capability may appear inside a virtual phone product as an optional layer (documented at the business pole). |
| Push-to-Talk Application | Transmission model | PTT centers hold-to-talk floor control over standing talk groups (counterparty pass records the seam: "telephony-line semantics (numbers, PSTN calls, voicemail); the PTT gesture and group model are absent"). |
| Contact Center / Call Center Platform | Organizational operation vs a line | Contact centers distribute a queue of customer contacts across agent staffing with routing/SLA/WFM machinery. A virtual phone line serves a person or small team; its routing (IVR, ring groups) serves the line's owners, not a managed agent workforce. |
| Second SIM / eSIM line | Substrate | A second SIM is a carrier-hardware line; a virtual phone line is software-operated over the internet. One sampled product ships a SIM-tied mode managed by the app — a hybrid variant, evidence that the app-management layer, not the radio, is the Type's center. |
| Disposable-number / SMS-verification web services | Communication line vs number rental | Verification services rent numbers to receive one-time codes; there is no ongoing communication line, history, or calling relationship. The sampled consumer pole explicitly documents that third-party verification codes generally do NOT work — reinforcing that this Type is for person-to-person/business communication, not code reception. |
| Business Messaging / SMS Marketing Platform | Two-way line vs campaign machinery | Marketing platforms organize audiences and campaigns; a virtual phone line is a standing two-way communication line with its own identity. |
| Telecom Number Management (carrier-side) | User-facing line vs infrastructure administration | Number management systems administer carrier number inventories; this Type is the end-user's operating surface for a line. |

**"Remove what to become the other Type" judgments:**

- Remove the real number (identity becomes a service account) → Internet Calling Application.
- Remove the app-operated surface (number forwards to another phone) → a forwarding service, the conceptual ancestor, not this Type.
- Remove the line persistence (identity per session) → calling/messaging territory.
- Remove the personal/small-team scale and add queue/agent/workforce machinery → Contact Center territory.

## Historical / Market-Sample Check

- **Conceptual ancestor**: "virtual phone number" services of the pre-app era (DID rental + call forwarding to a real phone) hold a number but have no operating surface — they fail leg 2 and are correctly excluded as ancestry, not membership.
- **Older/regional products**: early consumer virtual-number services (the Google Voice generation) satisfy the core with nothing modern — no team sharing, no AI, no compliance machinery. The definition holds.
- **Platform-native**: carrier second-line services operated through carrier apps satisfy the core with the carrier as the service; the definition does not require an independent software vendor.
- **Regional**: number-kind vocabulary (local/toll-free/vanity) is North-American-flavored in the sample; the definition names only "real telephone number," so non-US DID-based products fit. Country-coverage breadth is a variant, not structure.
- **Era machinery deliberately excluded from the core**: VoIP as a named protocol, apps as app-store products, A2P 10DLC, SHAKEN/STIR, AI agents, cloud delivery. The invariant is "app-operated software line," not any specific protocol generation.

## Uncertainties

1. **Google Voice operational details unverified** (fetch failed ×2). It is retained as a market anchor; no claims made. If a later pass can fetch Google's help center, the consumer/prosumer pole should be re-verified.
2. **TextNow (free consumer line pole) unverified** (403 ×2). The "free/ad-supported line as primary service" economics are therefore absent from the document; the Type definition does not depend on them.
3. **Whether SMS is definitional**: held as common-mature (4/4 sampled) rather than invariant, because voice-only virtual-number services exist in the ancestry and the Type sits in the Voice & Calling family. If a future pass finds a current voice-only virtual-line app, this stays correct; if SMS-only lines prove to be a major product population, the L0 phrasing ("calls, and commonly messages") already accommodates them.
4. **Emergency calling (E911) behavior**: not evidenced in any fetched page; no claim made either way.
5. **Softphone boundary** is argued conceptually because the softphone leaf is unprocessed; the seam should be ratified in that pass.
6. **Burner individual lifecycle articles** were not fetched (category structure only); Burner-specific retention/expiry mechanics are kept out of precise claims.

## Final Synthesis

The Virtual Phone Application is the application form of the "virtual phone number": the user holds a **real telephone number as a software-managed line** — acquired from the service's inventory or ported in, publicly dialable, presenting itself as caller ID — and operates that line **inside the application over the internet** on devices they already have, with the line persisting as a standing asset (with its accumulated history) until released. Around this core, mature products add texting, voicemail, unified history, contacts, blocking/auto-reply, multiple numbers, and porting; variants split along audience (personal second number ↔ team-shared business line), line tenure (prepaid/expiring ↔ subscription), routing depth, number kinds, geography, and regulatory machinery. The Type's identity is the number-as-line; remove the number and it is internet calling; remove the app surface and it is a forwarding service; remove the line and it is ephemeral calling.
