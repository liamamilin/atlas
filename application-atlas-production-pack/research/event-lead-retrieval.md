# Research Notes — Event Lead Retrieval

Research date: 2026-09-07
Slug: event-lead-retrieval
Directory leaf: Event Lead Retrieval (§26 Travel, Hospitality, Food Service & Events)

---

## Research Goal

Understand what "event lead retrieval" software actually is as an Application Type: what objects exist inside it, who operates it (organizer vs exhibitor vs sales/marketing consumers), how a booth conversation becomes a followable lead, which rules and state matter, and where the Type ends relative to Lead Capture Platform (§06), Lead Management/Generation (§07), Event Registration, Event Credential / Badge Management, Attendee Management, Event Mobile App, and Exhibitor/Sponsor Management.

## Initial Boundary (pre-research hypothesis)

- Core use: exhibitors at trade shows/exhibitions capture attendee contact information by scanning the badge credential the event issued, qualify it in the moment, and hand the captured set to their CRM/marketing/sales follow-up.
- Users: exhibitor booth staff (primary), exhibitor marketing/sales ops (consumers of the export), event organizers (provision/sell the capability), event registration systems (upstream source of badge data).
- Nearest neighbors: Lead Capture Platform (§06 marketing forms), Lead Management Platform (§07), CRM (destination), Event Registration Platform (credential issuance), Event Credential / Badge Management (issuer of the code being scanned), Event Mobile App (attendee-facing surface), Exhibitor/Sponsor Management (organizer-side relationship).
- Unknowns at start: whether session scanning/attendance is part of this Type; the organizer-vs-exhibitor control split; whether matchmaking/appointment features are definitional; historical forms (rental scanner era); regional variants (European fair systems).

## Research Questions

1. What exactly is a "lead" in this system — what data model does one scan create?
2. Who operates the application — exhibitor staff, organizer, or both? What does each side control?
3. How does capture physically work (badge types: barcode/QR/NFC; devices: rented handhelds, BYOD phones, kiosk cameras; fallbacks: business cards, manual entry)?
4. What do exhibitors do to a lead at the booth (notes, tags, ratings, custom questions, tasks)?
5. How do leads leave the system (CSV export, CRM/MA sync, API) and how quickly?
6. What adjacent functions get bundled (session scanning, gamification, in-app messaging, meeting booking, enrichment)?
7. What role does offline operation play at exhibition venues?
8. How does the Type differ from generic marketing lead capture?
9. What older/regional realizations look like (rental-scanner service era, European fair systems).

## Representative Products

Selected for market representation, documentation reachability, product philosophy, and customer tier:

| Product | Philosophy / tier | Why sampled |
|---|---|---|
| Cvent LeadCapture | Organizer-provided capture locked to the organizer's platform (Cvent events); exhibitors are the users | Market anchor; explicit organizer-vs-exhibitor framing; Exhibitor Portal ROI story |
| Cvent iCapture | Exhibitor-owned universal capture across third-party events (any show, any venue) | The deliberately opposite pole: badge-provider integrations, enrichment, routing rules, cross-show consistency |
| Whova | Event-app-embedded exhibitor lead tools; gamification-led booth traffic; SMB/mid-market conference pole | App-native pole; virtual-booth lead capture; QR + card + manual methods |
| vFairs Event Lead Capture App | Platform module configured in the organizer backend with a dedicated exhibitor portal; AI enrichment | Richest operational detail in reachable sources (roles: booth managers/booth reps; tags/voice notes; explicit capture-vs-retrieval FAQ) |
| Zenus (exhibitor solutions) | AI-first complement: hands-free kiosk badge scanners + booth analytics funnel | Documents the zero-touch capture variant and the impressions→captured funnel framing |

Note: Expo Logic (specialist), EventMobi, Swapcard, and Visit Connect (European fair pole) were unreachable from the research environment (403 / timeout / 502 / transport errors; see Sources). The specialist-services and regional poles are therefore not directly evidenced and are flagged in Uncertainties.

## Sources

Reachable (fetched 2026-09-07):

- Cvent — LeadCapture product page + FAQs: https://www.cvent.com/en/event-marketing-management/lead-capture
- Cvent — iCapture product page + FAQs: https://www.cvent.com/en/event-marketing-management/cvent-icapture
- Whova — homepage: https://whova.com/
- Whova — Exhibitor & Trade Show Management / Lead Retrieval page: https://whova.com/trade-show-app-lead-retrieval/
- vFairs — homepage: https://www.vfairs.com/
- vFairs — Event Lead Capture feature page + FAQs: https://www.vfairs.com/features/event-lead-capture/
- Zenus — Solutions for Exhibitors: https://www.zenus.ai/solutions-for-exhibitors
- Zenus — homepage: https://zenus.ai/

Unreachable (recorded limitation; claims lowered accordingly):

- https://www.eventmobi.com/en/lead-retrieval/ (403 — abandoned)
- https://www.swapcard.com/ (timeout, then 502 — abandoned after 2 failures)
- https://whova.com/features/lead-retrieval/ (404; correct path found via site nav)
- https://www.expologic.com/ (403 — abandoned; lead-retrieval specialist not directly sampled)
- https://www.fromvisit.com/ (transport error ×2 — abandoned; European fair-system pole not directly sampled)
- Cvent support knowledge base (support.cvent.com) is a JS-only app, not fetchable — consistent with the Event Credential / Badge Management pass.

Evidence-layer convention used below: **A** = directly observed in an official source of that product; **B** = cross-product commonality across the sampled products; **C** = canonical inference from comparison + Type-boundary reasoning.

---

## Product Observations

### Cvent LeadCapture (evidence: A; Tier 2 product page + FAQ)

- Positioning is organizer-voiced: "One scan. One consistent lead capture tool for every exhibitor and sponsor on the floor… They leave with qualified leads and proof of impact — you leave with an event worth repeating." (A)
- Capture: exhibitors "scan badges or business cards with a mobile device" to capture contact details; "No more jotting notes on the back of business cards or manually entering in contact information." (A)
- Qualification at the booth: "Add custom questions for better sales qualification"; exhibitors "add notes, answer qualification questions, and rate leads in real time, helping prioritize follow-up by lead quality and intent." (A)
- Export/delivery: "Export leads on-demand to any database"; "Import leads directly into their CRM system"; "Sync and integrate leads into your CRM to help sales connect… before you ever leave the event." (A)
- Exhibitor Portal: "full access to lead count and quality… Real-time access to lead count and quality; intuitive reporting… Justify future participation." (A)
- Multi-staff: "multiple booth staff can use LeadCapture simultaneously… ensures all data is centralized and accessible in a single system." (A)
- Organizer value: "Organizers gain visibility into exhibitor performance… create stronger sponsorship offerings backed by measurable outcomes." (A)
- Privacy: "built with enterprise-grade security and privacy controls… compliance with global data protection standards." (A)
- Product split inside one vendor: LeadCapture is "used at events you manage on the Cvent platform," while Cvent iCapture is "designed for third-party events and trade shows where you are an exhibitor… where event data is not managed in Cvent." (A)

### Cvent iCapture (evidence: A; Tier 2 product page + FAQ) — the exhibitor-owned universal pole

- Positioning is exhibitor/marketing-team-voiced: "Give reps a familiar capture flow at every show, enrich from providers you can name, and hand sales a record they'll act on the same day." (A)
- Capture methods: "Capture leads your way with badge scans, business cards, photos, or manual entry"; "Use your own phone or tablet — no extra hardware or rental fees." (A)
- Badge interop: "Integrates with 130+ badge providers and other capture methods, pulling the official registration data behind the badge instead of relying on guesswork or manual typing." (A)
- Consistency across shows: "every rep captures the same trusted way, at every show"; "standardized forms… one consistent workflow across all your shows… marketing finally gets a complete, comparable dataset for every event." (A)
- Enrichment/validation: "Validate first, then enrich from providers you can name, control, and govern" (ZoomInfo with the customer's own seats/credits; AI-predicted email suggestions "marked as predictions"; Apollo firmographics "company-level data only"). (A)
- Routing: "Set the rules once, and every answer from the floor routes the lead accordingly"; "Send leads directly to Salesforce, HubSpot, Marketo, Eloqua, and more"; leads "land in rep queues and nurture programs almost immediately after a scan, often while the show is still live." (A)
- Meeting booking in the capture flow: "Connect Calendly or HubSpot and book meetings without leaving the capture flow"; individual/round-robin/multi-host rep matching. (A)
- Offline: "Capture leads offline and connect booked meetings to lead records once your connection returns." (A)
- ROI: "See which shows create pipeline, which reps create momentum… Compare shows and booked meetings before next year's budget is set"; closed-loop attribution "show, campaign, and qualification data." (A)

### Whova — Exhibitor & Trade Show Management / Lead Retrieval (evidence: A; Tier 2 product page)

- Framing is organizer-retention + exhibitor-ROI: "Help your exhibitors generate more business so they come back to your trade show year after year." (A)
- Capture methods: "Exhibitors collect leads with QR code scanning, manual entry, and virtual booth interactions"; "No more expensive hardware." (A)
- Export: "With just the push of a button, exhibitors can export contacts to their CRM, and message or schedule meetings with their leads." (A)
- In-event follow-up: "Connect effectively with 1-1 messaging — exhibitors can easily follow up on leads within the event through video and text chat"; "Exchange virtual business cards — scan mobile business cards in-person or exchange them virtually." (A)
- Booth-traffic machinery: "Attract booth visitors with coupons and giveaways"; "The Passport Contest and Leaderboard encourage attendees to interact with booths to win a prize." (A)
- Lead insight: "Empower exhibitors to explore SmartProfiles, identify leads, and schedule meetings." (A)
- Virtual extension: virtual booths and virtual exhibitor halls are first-class lead surfaces ("more time in the Virtual Exhibitor Hall"; leads counted from "virtual booth interactions"). (A)
- Scale proof points published on the page (e.g., "17,593 Leads Captured") are vendor-published case figures — treated as marketing evidence, not operational rules. (A, marketing-grade)

### vFairs Event Lead Capture App (evidence: A; Tier 2 feature page + FAQ — richest operational detail in sample)

- Setup split: "Configure the lead capture app within the same vFairs backend as the rest of your event" (organizer side) + "Give exhibitors access to a dedicated portal to configure their booth and invite teammates for collaboration" (exhibitor side); "Give varying degrees of access to each member of your team, booth managers, and booth reps"; configuration templates reusable across events. (A)
- Capture: "Capture leads with QR code scanning, business card scanning, and manual entry"; "Edit or delete entries easily to keep data accurate and clean"; custom per-exhibitor lead forms ("product interest, budget, requirements"). (A)
- AI enrichment: "Turn a Name & Email Into a Full Lead Profile Instantly… Tap once to enrich with company name, title, and more… Double-check lead information you already have." (A)
- Qualification context: "Create custom tags for your leads like hot, cold, urgent, interested in product A"; "Add written or audio notes with each lead"; filters by tag/keyword; sorting "all leads from one booth, or captured by one teammate." (A)
- Follow-up comms: "Send emails or make direct calls to most important leads"; "Chat with leads within the app"; "Personalize follow-ups with custom email templates"; "Reassign leads to different representatives." (A)
- Delivery: "Transfer leads' data to your CRM or Martech systems and obtain data as a CSV"; Salesforce, HubSpot, Marketo, Zoho CRM, Zapier, Mailchimp named; "Generate secure custom APIs easily through our Apps Marketplace." (A)
- Reporting: "Track scan counts, leads gathered, and identify the most engaged participants"; "real-time dashboard with current lead and follow-up status"; "Measure leads generated by each team or individual team member"; "organization-level dashboard" across events. (A)
- Terminology FAQ: "'Lead capture' refers to the process of collecting attendee information during an event… 'Lead retrieval' is a more specific term used for systems or tools that allow exhibitors to access and retrieve the contact details of event attendees in real-time, often through scanning badges or QR codes." (A)
- Setup authority: "Organizers can set up and configure the app… define data fields, set up lead scoring, and integrate with CRM systems." (A)
- Page subtitle: "Works at any event, any venue" (universal posture marketed even though configured in the vFairs backend). (A)

### Zenus — exhibitor solutions (evidence: A; Tier 2 solution page) — the AI/hands-free complement pole

- "Easy Lead Retrieval — Generate more leads with an automated, hands-free solution." (A)
- Positioning relative to handheld apps: "Compliment your handheld lead scan app with our hands-free kiosk scanners. Continue to collect opt-in marketing leads even when your whole team is engaged or if you are not physically there." (A)
- Opt-in capture: "Intuitive opt-in scanning takes 3 seconds; get more leads from your booth investment." (A)
- Booth analytics funnel: "How many people passed by (total impressions); Number of qualified, engaged, and captured leads; Demographics and sentiment data." (A)
- Device posture: smart camera; "All video is analyzed locally to address privacy concerns… Our devices work just as hard offline." (A)

---

## Cross-product Comparison

| Structure | Cvent LeadCapture | Cvent iCapture | Whova | vFairs | Zenus |
|---|---|---|---|---|---|
| Capture keyed to attendee identity (badge/QR scan) | A — scan badges | A — badge scans via "130+ badge providers" | A — QR code scanning | A — QR code scanning | A — kiosk badge scanners (opt-in) |
| Fallback capture (card/manual/photo) | A — business cards | A — cards, photos, manual | A — manual entry, mobile card scan | A — business card scanning, manual | n/e (kiosk only) |
| Operator = exhibitor booth staff | A | A — "reps" | A | A — booth reps / booth managers | A — staff-less complement |
| Operator-entered context at capture | A — notes, questions, ratings | A — qualification questions | A — notes implied, SmartProfiles | A — tags, text+voice notes, custom forms | n/e — hands-free mode |
| Shared team capture / one pool | A — multi-staff simultaneous | A — "every rep… one consistent workflow" | implied (exhibitor account) | A — invite teammates, per-capturer attribution | n/e |
| Edit/correct captured records | implied (visibility control) | n/e | n/e | A — edit or delete entries | n/e |
| Central dashboard / portal for exhibitors | A — Exhibitor Portal, real-time lead count/quality | A — manager visibility "even at shows they aren't attending" | implied (exhibitor portal) | A — real-time dashboard, lead + follow-up status | A — live dashboard (analytics framing) |
| Organizer-side provisioning/control | A — organizer sells/delivers the tool; visibility into exhibitor performance | n/e (exhibitor-owned) | A — bundled for exhibitors by organizer | A — organizer configures in backend, defines fields/scoring | n/e (exhibitor buys directly) |
| Delivery: export/CSV | A — "export on-demand to any database" | A — CRM/MAP sync | A — "push of a button… to CRM" | A — CSV + CRM sync | A — API/dashboard supply |
| Delivery: CRM/MA integration | A — import into CRM | A — Salesforce/HubSpot/Marketo/Eloqua | A — export to CRM | A — named CRM/MA list + Zapier + API | n/e (API) |
| Routing rules / lead assignment | A — "route them directly to the correct rep via their CRM" (case study) | A — rules route by floor answers; round-robin meeting matching | n/e | A — reassign leads to reps | n/e |
| Offline tolerance | n/e | A — capture offline, connect later | n/e | n/e | A — devices work offline |
| Enrichment from data providers | n/e | A — ZoomInfo/Apollo, AI-predicted emails flagged | n/e | A — AI enrichment (name/email → profile) | n/e |
| Follow-up comms in product | n/e (delegated to CRM) | A — meeting booking in capture flow | A — 1:1 chat, schedule meetings | A — emails, calls, in-app chat, templates | n/e |
| Gamification / booth traffic | n/e | n/e | A — Passport Contest, Leaderboard, coupons | n/e (separate feature) | n/e (dynamic displays adjacent) |
| Virtual-event lead capture | n/e | n/e | A — virtual booth interactions | A (virtual platform sibling product) | n/e |
| ROI / attribution reporting | A — lead count/quality, ROI justification | A — show/rep/pipeline attribution | A — exhibitor ROI framing | A — per exhibitor/team/individual + org-level | A — funnel metrics (impressions→captured) |
| Universal (third-party events) | n/e — platform-locked | A — "every show" | n/e — platform-embedded | partial — "any event, any venue" marketing, backend-configured | A — booth-side, event-agnostic |

Legend: A = direct official evidence; n/e = not evidenced in reachable sources.

### Cross-product reading

- **B-layer commonalities (all 5):** capture is triggered by reading the attendee's event identity (badge/QR/opt-in kiosk); the captured record is exhibitor-attributed; captured leads are delivered out of the application (export, CRM sync, API); reporting surfaces lead counts and quality to the exhibitor.
- **B-layer commonalities (4 of 5):** operator-entered qualification at the booth (notes/tags/ratings/questions — absent only in Zenus's hands-free mode, which still frames its output as "captured leads"); central dashboard/portal view; organizer involvement in provisioning or bundling; ROI framing.
- **B-layer commonalities (3 of 5):** CRM/marketing-automation integrations by name; offline tolerance; enrichment; in-product follow-up comms; routing/assignment.
- **Polarities, not omissions:** who owns the tool (organizer-provided and platform-locked ↔ exhibitor-owned and universal — the same vendor ships both poles as two products); capture device (BYOD phone ↔ rental-grade hardware ↔ staff-less kiosk camera); where follow-up starts (delegated to CRM ↔ inside the product); in-person badge scan ↔ virtual booth interaction.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

The Type is recognizable iff all three hold:

1. **Capture keyed to the event's attendee identity.** A lead record is born by reading the identity credential the event issued to the attendee — badge barcode/QR/NFC code at minimum, with business-card scanning, photo capture, and manual entry documented as fallbacks in the sample. Remove the event-credential anchoring → a generic contact-capture/CRM mobile tool or a marketing form; not this Type.
2. **The captured lead record.** A persistent, identified record per captured attendee contact, attributed to the exhibitor (and commonly to the capturing staff member), accumulated as the event's working list — editable/correctable before handoff. Remove → a raw scan counter / attendance log.
3. **Delivery of the captured set to the exhibitor's follow-up.** The captured leads leave the application — file export, CSV, CRM/marketing-automation sync, or API — into the systems where post-event sales and marketing act on them. Remove → a booth scanner with a log and no business purpose; the "lead" ceases to exist as a lead.

Historical check (older / regional / platform-native realizations): the rental-scanner service era — organizer-rented handheld barcode guns scanning badge codes, leads delivered to the exhibitor as a file after the show — satisfies all three structures without apps, real-time dashboards, notes-at-capture, or CRM sync. The pre-software booth practice (business cards collected and annotated at the booth, transcribed into follow-up lists) matches the structure at the fallback-capture level. Nothing in the L0 requires smartphones, real-time sync, enrichment, or gamification. Check passed. (Direct Tier-1 documentation of the rental era was not reachable this pass — see Uncertainties; the check rests on the structure plus the observed fallback-capture continuity.)

### L1 — Common Mature Structure (very common; not definitional)

- On-the-spot qualification: notes (text and voice in one product), tags (hot/warm/cold-style), lead ratings/grades, and custom qualification questions/fields configured per exhibitor (Cvent, iCapture, Whova implied, vFairs; Zenus is the hands-free exception).
- Shared team capture: multiple booth staff capturing into one exhibitor lead pool, with per-capturer attribution (Cvent, iCapture, vFairs explicit).
- Real-time central view: exhibitor portal/dashboard with lead counts, quality, and capture activity during the event (Cvent, iCapture, vFairs; implied Whova).
- Organizer-side provisioning: the organizer configures/permits capture, exposes (or withholds) registration data behind the badge, and often resells the capability to exhibitors/sponsors (Cvent LeadCapture, vFairs, Whova; absent by design in the exhibitor-owned pole).
- CRM/marketing-automation integrations alongside CSV export (Cvent, iCapture, vFairs, Whova).
- ROI/attribution reporting: leads per show/booth/rep, quality vs quantity, follow-up status (all five at varying depth).
- Record hygiene: edit/delete captured entries before delivery (vFairs explicit; consistent with the record structure).
- Follow-up starting inside or beside the product: in-app chat/messaging, email templates, direct calls, meeting booking connected to the capture flow (Whova, vFairs, iCapture; Cvent LeadCapture delegates to CRM).
- Routing/assignment of leads to the right rep (iCapture rules + round-robin meetings; vFairs reassignment; Cvent case-study routing claim).
- Offline capture with later sync (iCapture, Zenus).

### L2 — Variant / Optional Structure

- Capture technology: phone-camera QR/barcode scanning, dedicated handheld/rented devices, NFC/RFID, staff-less kiosk cameras (Zenus), smart badges (vFairs lists a Smart Badges feature in its onsite family), business-card OCR, manual entry.
- Deployment pole: platform-locked capture sold by the organizer's platform (Cvent LeadCapture, vFairs, Whova) vs exhibitor-owned universal capture used across many organizers' shows (Cvent iCapture; vFairs markets a "any event, any venue" posture while configured in its backend).
- Virtual/hybrid extension: virtual booth visits and interactions counted as leads; virtual exhibitor halls (Whova, vFairs).
- AI posture: enrichment from named data providers (ZoomInfo/Apollo in iCapture), AI enrichment of name+email into full profiles (vFairs), AI-predicted contact fields explicitly marked as predictions (iCapture), hands-free opt-in capture (Zenus).
- Booth-traffic machinery: gamification (passport contests, leaderboards), coupons/giveaways (Whova; vFairs ships gamification as a separate sibling feature).
- Booth analytics funnel: impressions → engaged → captured, with demographics/sentiment (Zenus; adjacent in vFairs reporting).
- Services-led pole: organizer-arranged rental hardware and onsite services (era-legacy; not directly documented this pass — see Uncertainties).

### L3 — Vendor-specific (kept out of the final document)

- Cvent: LeadCapture vs iCapture two-product split; Exhibitor Portal branding; case-study figures ($8,000 labor saved, 6,000 MQLs, etc.); Jifflenow as the sibling "trade show meetings" product; CventIQ framing.
- Cvent iCapture: "130+ badge providers" integration count; ZoomInfo/Apollo named enrichment partners; AI-predicted-email labeling; Calendly/HubSpot meeting connections; individual/round-robin/multi-host routing modes.
- Whova: Passport Contest, Leaderboard, SmartProfiles branding; published event metrics (17,593 leads; 88% adoption); "no more expensive hardware" positioning.
- vFairs: Apps Marketplace; MCP server (AI-assistant data access); organization-level multi-event dashboard; booth manager/booth rep access tiers; voice notes; explicit capture-vs-retrieval FAQ; "Hot/Warm/Cold" tag vocabulary.
- Zenus: Smart Camera hardware; "3 seconds" opt-in claim; local video processing; "Return-On-Engagement" reports; 16/16 booth-renewal case framing.

## Vendor-specific Findings

See L3. Additionally: only Cvent documents the platform-locked vs third-party split as two distinct products; only vFairs documents an explicit organizer-configured vs exhibitor-configured split of setup authority (organizer defines data fields/scoring; exhibitor defines its own custom lead forms); only Zenus frames capture as a complement to handheld apps ("compliment your handheld lead scan app") rather than the capture tool itself.

## Rejected Findings (considered and excluded from the defining core)

- "Gamification/booth-traffic contests are definitional" — rejected: present strongly in one sampled product; booth traffic is a precursor concern, not the capture structure.
- "AI enrichment is definitional" — rejected: two of five sampled products; enrichment improves record quality but the Type exists without it (rental-scanner era).
- "CRM sync in real time is definitional" — rejected: real-time CRM sync is the modern delivery form; the defining structure is delivery itself (file delivery satisfies it historically).
- "Custom qualification questions are definitional" — rejected to standard capability: universal in the current sample but absent in the minimal historical form; notes/tags/ratings are the common mechanisms, not the invariant.
- "Real-time dashboards are definitional" — rejected: real-time visibility is modern; the exhibitor's post-event list is the older sufficient form.
- "Lead scoring/grading is definitional" — rejected: grading scales are widespread but product-defined (labels vary); the capability, not any scale, is standard.
- "Rental hardware is definitional" — rejected: BYOD is explicitly marketed as the replacement ("no extra hardware or rental fees"); devices are variants.
- "Session/attendance scanning is part of this Type" — rejected: session scanning serves the organizer's attendance/access data with the same scan mechanics but a different actor and object; where bundled (platform suites), it is a sibling module, not the lead structure.
- "Matchmaking/appointment scheduling is definitional" — rejected: meeting machinery appears as adjacent products/modules (Cvent's separate trade-show-meetings product; meeting booking as an iCapture add-on flow); the lead record, not the meeting, is this Type's object.

## Boundary Findings

| Neighbor | Relationship | "Remove what → becomes the other Type" test |
|---|---|---|
| Lead Capture Platform (§06 Marketing) | nearest sibling, different actor/anchor | Remove the event-credential anchoring and the show-floor exhibitor operation (keep web forms/campaign capture for marketing) → generic Lead Capture Platform. Remove campaign-form machinery (keep badge-keyed booth capture) → this Type. The same vendors span both (Cvent ships both), which is packaging, not Type identity. Joint review recommended. |
| Lead Management Platform / CRM (§07) | downstream destination | The captured lead leaves this Type at handoff; pipeline/relationship machinery lives there. Remove delivery-to-follow-up → this Type stops functioning; remove capture-at-booth → CRM with manual entry. Both directions hold ⇒ separate Types with a designed handoff seam. |
| Event Registration Platform | upstream issuer of the identity being read | Registration owns attendee data capture and credential issuance; this Type consumes the issued code. Remove credential issuance (keep booth capture) → this Type still stands against any badge provider; remove booth capture (keep registration) → registration platform. |
| Event Credential / Badge Management | issuer of the artifact; this Type is the consumer | Badge management designs/produces/issues/enforces the credential; lead retrieval only reads its code at booths. Remove badge production/issuance (keep exhibitor-side reading) → this Type; remove reading (keep credential machinery) → badge management. DISCHARGES the badge pass's "downstream consumer" note from this side. |
| Attendee Management | organizer-side lifecycle vs exhibitor-side capture | Organizer works the attendee relationship (comms, engagement); this Type captures the exhibitor's point-of-contact record. Different operator, different owner of the record. |
| Event Mobile App | attendee-facing surface vs exhibitor-facing capture | The event app serves attendees (agenda, networking); lead capture serves exhibitors. Where one platform ships both (Whova, vFairs), they are distinct surfaces with distinct users; the app is a delivery vehicle, not the core. |
| Exhibitor / Sponsor Management | organizer-side relationship machinery | Booth sales, profiles, logistics, and document collection are the organizer's exhibitor relationship; lead retrieval is the capture service sold to exhibitors. Remove capture (keep booth logistics) → Exhibitor Management. |
| Event Management Platform | umbrella container | Lead retrieval is one named module inside event platforms across the sample; standalone exhibitor-owned capture products also exist. Module packaging is a variant, consistent with sibling event leaves. |
| Session/attendance scanning (inside check-in/OnArrival-class products) | same mechanics, different actor+object | Organizer staff scan badges to record session attendance; exhibitor staff scan badges to capture leads. Remove the exhibitor/lead framing (keep attendance) → organizer-side attendance tracking. |
| Trade-show meetings/appointment products (no directory leaf) | adjacent commercial flow | Meeting scheduling between exhibitors and attendees is its own product family (Cvent's separate offering); appointment machinery attaches to leads but the lead record remains this Type's object. |
| Contact/business-card scanner tools | fallback method only | Card OCR/manual entry are documented fallbacks inside this Type; a standalone card scanner without event anchoring, organizer relationship, or exhibitor pool is a generic utility. |

Boundary Issues to carry into STATUS.md:
1. Terminology overlap: the market uses "lead capture" and "lead retrieval" interchangeably for the same show-floor tools (vFairs documents the distinction in its FAQ; Cvent brands platform-locked capture "LeadCapture" and universal capture "iCapture"). The directory leaf name ("Event Lead Retrieval") matches the exhibition-floor standard term; no re-draw needed, but the sibling Lead Capture Platform (§06) seam needs joint review when that leaf is processed.
2. Capability-vs-Type packaging: realized as standalone universal products (iCapture class), platform modules (Cvent LeadCapture, vFairs, Whova), and organizer-arranged services with rental hardware (era-legacy pole, not directly documented). Type stands; packaging is variant.

## Uncertainties

1. **Specialist and regional families unverified**: Expo Logic (lead-retrieval/badge specialist) and Visit Connect (European fair pole) unreachable; EventMobi and Swapcard (platform-native poles) unreachable. The specialist-services pole and regional variations are inferred from structure only — no precise claims made.
2. **Rental-device service era**: the organizer-rented handheld + post-show file delivery model is described structurally (and partially by iCapture's "no extra hardware or rental fees" contrast) but no Tier-1 documentation of a current rental-era product was reachable; the historical check therefore rests on structure, not on a sampled product.
3. **What a scan returns** (exactly which registration fields flow to the exhibitor, and what the attendee consented to) is governed by each organizer's registration data and privacy configuration — only indirect evidence (iCapture's "official registration data behind the badge"; Zenus "opt-in"; Cvent privacy-controls statement). No field lists asserted.
4. **Duplicate handling**: only vFairs documents edit/delete; whether products deduplicate scans automatically is unknown — not asserted.
5. **Pricing/packaging** (per-exhibitor purchase, device rental fees, tier gating): not evidenced anywhere in the sample — no pricing claims made.
6. **Cvent knowledge base** (Tier 1) is JS-only; Cvent workflow detail rests on product pages/FAQs (Tier 2), so fine-grained operator steps are unstated.
7. **Whova qualification depth** (whether notes/tags exist in its capture flow) is implied but not explicitly documented in reachable pages; treated as implied.

## Final Synthesis

Event Lead Retrieval is the exhibitor-side show-floor capture system. Its defining core is exactly three structures: (1) capture keyed to the event's attendee identity — the lead is born by reading the badge/QR/NFC credential the event issued, with business-card scanning, photo capture, and manual entry as documented fallbacks; (2) the captured lead record — a persistent, identified, exhibitor-attributed record per booth contact, accumulated as the exhibitor's working list and correctable before handoff; (3) delivery of the captured set to the exhibitor's follow-up systems — file/CSV export, CRM/marketing-automation sync, or API. Everything else commonly associated with the category — on-the-spot qualification (notes, tags, ratings, custom questions), shared multi-staff capture pools, real-time dashboards and exhibitor portals, organizer provisioning, named CRM integrations, ROI/attribution reporting, offline capture, AI enrichment, in-product follow-up (chat/email/calls/meeting booking), gamification, virtual-booth lead counting — is standard mature capability or variant, not definition. The Type's two packaging poles (organizer-provided platform-locked capture vs exhibitor-owned universal capture) are sold side by side by the same vendors, and the rental-scanner service era satisfies the defining core without any modern machinery — the definition is deliberately technology- and era-neutral.
