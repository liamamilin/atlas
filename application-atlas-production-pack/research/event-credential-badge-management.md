# Research Notes — Event Credential / Badge Management

Research date: 2026-09-07
Slug: event-credential-badge-management
Directory leaf: Event Credential / Badge Management (§26 Travel, Hospitality, Food Service & Events)

---

## Research Goal

Understand what "event credential / badge management" software actually is as an Application Type: what objects exist inside it, who operates it, how the work flows from event preparation through on-site issuance to enforcement and reporting, which rules matter, and where it ends relative to Event Registration, Ticketing, Attendee Management, Lead Retrieval, and Building Access & Visitor Management.

## Initial Boundary (pre-research hypothesis)

- Core use: design, produce, personalize, issue, and enforce the badges/credentials that identify people at an event and authorize what they can access (zones, sessions, days).
- Users: event ops / registration managers, check-in staff and volunteers, security, workforce coordinators.
- Nearest neighbors: Event Registration Platform (pre-event data capture), Event Ticketing Platform (admission transaction), Attendee Management (broader lifecycle), Event Lead Retrieval (exhibitor-side scanning), Building Access & Visitor Management (permanent facility), Digital Credential Platform (§23 education — homonym only), Cashless Venue Platform (RFID payment).
- Unknowns at start: the industry distinction between "credential" and "badge"; whether access-control machinery is definitional or scale-dependent; the production modes (pre-print vs on-demand); the reissue/lost-badge discipline.

## Research Questions

1. What is a "credential" vs a "badge" vs a "ticket" in this domain?
2. What is the core object model? (holder, credential type, design template, entitlement, produced artifact, scan/arrival event, lifecycle states)
3. Who operates the system, and with what rights (desk staff vs admins)?
4. What is the canonical workflow (define → design → collect holders → produce → issue → enforce → maintain → report)?
5. Which rules are load-bearing (fee gates, role restrictions, reprint discipline, data currency)?
6. What interfaces exist (designer, register, check-in console, kiosk, scanners, dashboards, settings)?
7. What variants exist (conference badging vs sports/festival accreditation vs luxury guest lists vs academic mail-merge)?
8. How does it interlock with registration, ticketing, and the event app?

## Representative Products

Selected for market representation, documentation quality, product philosophy, and client tier:

| Product | Philosophy / tier | Why sampled |
|---|---|---|
| Cvent (OnArrival / Onsite Solutions) | Enterprise conference platform; check-in & badging as a named platform category | Market anchor; explicit per-attendee-type badge layouts; session admit/deny |
| Stova | Enterprise event ecosystem (Aventri/etouches/Meetingplay lineage); bespoke badging + out-of-the-box BadgeNext | Full platform with explicit "Access Control & Session Scanning" capability; NFC encoding evidence |
| RainFocus | Enterprise flagship events; data-first platform; kiosk-led onsite | Offline-tolerant kiosks; "coded badge data" + session access control |
| zkipster | Luxury/special events; guest-list-first; check-in app + printing | Desktop + on-site dual production mode (Tier 1 help center); wallet passes |
| ConfTool | Academic conferences; organizer-led, low-cost; no access-control machinery | Tier 1 admin documentation; the deliberately minimal pole — critical for the abstraction check |

Note on alternatives: EventMobi, Bizzabo, Whova (help centers) and Accredit Solutions (accreditation specialist) were unreachable from the research environment (transport errors after retries; see Source-access Limitation). The accreditation pole is therefore only indirectly covered (via Stova/Cvent/RainFocus access-control evidence) and is flagged in Uncertainties.

## Sources

Reachable (fetched 2026-09-07):

- Cvent — Onsite Solutions product page: https://www.cvent.com/en/event-marketing-management/onsite-solutions
- Cvent — OnArrival check-in & badging product page + FAQs: https://www.cvent.com/en/event-marketing-management/onarrival-event-check-in-software
- Cvent — Event Badge Printing page: https://www.cvent.com/en/event-marketing-management/event-badge-printing
- Stova — homepage: https://stova.io/
- Stova — Onsite Services: https://stova.io/platform/capabilities/onsite-services/
- RainFocus — homepage: https://www.rainfocus.com/
- RainFocus — On-Site Experience: https://www.rainfocus.com/platform/on-site-experience/
- zkipster — homepage: https://www.zkipster.com/
- zkipster Help Center root: https://support.zkipster.com/en/
- zkipster Help Center — Name Badge Printing collection: https://support.zkipster.com/en/collections/1561540-zkipster-name-badge-printing
- ConfTool — Admin Documentation index: https://www.conftool.net/en/administrator-documentation.html
- ConfTool — Creating Name Badges and the List of Participants (Tier 1): https://www.conftool.net/en/administrator-documentation/creating-name-tags.html
- ConfTool — Using the Front Desk Feature (Tier 1): https://www.conftool.net/en/administrator-documentation/frontdesk.html

Unreachable (recorded limitation; claims lowered accordingly):

- https://support.eventmobi.com/… (transport error ×2 — abandoned)
- https://support.bizzabo.com/… (transport error ×2 — abandoned)
- https://support.whova.com/… (transport error ×2 — abandoned)
- https://www.accreditsolutions.com/ (transport error ×2 — abandoned)
- https://support.cvent.com/s/knowledgebase (Salesforce LEX page; "CSS Error" — JS-only, not fetchable; product pages/FAQs used instead)
- https://support.swapcard.com/… (transport error ×2 — abandoned)

Evidence-layer convention used below: **A** = directly observed in an official source of that product; **B** = cross-product commonality across the sampled products; **C** = canonical inference from comparison + Type-boundary reasoning.

---

## Product Observations

### Cvent — OnArrival / Onsite Solutions (evidence: A, Tier 2 product pages + FAQs)

- Platform nav carries "Check-in & badging" as a named product category; OnArrival described as "event check-in, on-demand badge printing, and attendance tracking." (A)
- Check-in: search attendees by name, email, company, confirmation number; staffed desks, self-serve kiosks, or desktop/phone/tablet; real-time check-in alerts; supports "different guest types or complex event setups." (A)
- On-demand badge printing: badges "generated dynamically from registration data, enabling real-time personalization, last-minute updates, and easy reprints"; explicitly framed as eliminating the need to "pre-print, sort, or manually reissue badges." (A)
- Badge Designer: on-brand badges from attendee names, roles, logos, brand colors; "unique layouts for different attendee types — VIPs, sponsors, speakers, and staff"; preview before print. (A)
- Session handling: "Capture attendance with a quick scan of a name badge. For sessions needing pre-registration or attendee verification, OnArrival helps identify who to admit or deny"; session check-in + capacity control; "With badge scanning and optional RFID or NFC, organizers can monitor who attends each session, enforce access permissions, and track room capacity as it fills." Kiosks or mobile scanners. Signature tracking for CE credits/legal compliance. (A)
- Reporting: "Real-time event stats every 15 minutes"; check-ins vs registrations; session attendance; social-event attendance. (A)
- Payments: secure onsite payment collection for registrations/upgrades at check-in. (A)
- Walk-ins: register and check in on-site; onsite changes "automatically sync with the broader event system." (A)
- Deployment poles: "Event-in-a-Box" self-service badging/check-in kits (VIP events, roadshows, recruiting) vs "OnArrival 360" full service (dedicated PM, kiosks, printers, scanners, onsite setup/support/take-down). (A)
- Resilience: "optimized for high-volume environments and continues to function even with limited connectivity." (A)
- Sustainability: sustainable badge materials and lanyards; print-only-what-you-need; enclosed kiosk setups or thermal badge boxes. (A)

### Stova (evidence: A, Tier 2 product pages + FAQ + case-study mention)

- Nav capability: "Access Control & Session Scanning — Manages who can enter what sessions or zones, tracks attendance, and ensures compliance for certified events." (A)
- Onsite Services: "Deliver Bespoke Badging & Check-In"; hardware options include mobile check-in carts, tablets, mobile devices, laptops, NFC hot spots; "Badges can be plastic or paper card stock, and can be scanned via NFC, QR, BLE, or UHF technology." (A)
- BadgeNext: out-of-the-box badging/check-in for smaller events; FAQ: "On-demand badge printing is integrated into the check-in process using badgeNEXT"; attendees check in with mobile QR codes "at kiosks or by staff." (A)
- Session tracking: "Use handheld or RFID scanners to monitor session attendance and capacity in real time"; session dashboards "give you a bird-eye-view of current attendee data." (A)
- Digital badge: "a custom mobile app as your digital badge" — the event app can serve as the credential surface. (A)
- Data currency: remote check-in options "fully integrated with Stova Registration, meaning that badges will always reflect the most recent, accurate information"; "Check-in can also integrate easily with any other registration provider." (A)
- Remote issuance points: "Portable check-in carts can be set up anywhere from airports to hotel lobbies." (A)
- Services: onsite support specialists cover "session access control to badging & registration"; onsite training/staffing; managed services 24/7. (A)
- Case-study line (Informa / The Aesthetic Show): "Stova's on-demand badge printing and NFC encoding technology." (A)
- Sustainability: "eco-friendly badges and lanyards … onsite recycling and responsible disposal of consumables" (homepage). (A)

### RainFocus (evidence: A, Tier 2 platform page)

- On-Site Experience module: check-in kiosks ("speed attendees through the door"); "Our network fault-tolerant system can even run offline if the internet goes out." (A)
- Badging: "Customized badges are the key to unlocking rich engagement data. Our stunning badges also show off your brand" — badging explicitly tied to data capture. (A)
- Session access: "Session Access and Scanning — Easy-to-use scanners quickly verify coded badge data. Control access to sessions and collect valuable data on attendee behavior." (A)
- Lead devices: exhibitor scanning apps consume "coded badge data." (A)
- Kiosks also used for gift redemption; mobile app as attendee surface; real-time onsite data monitoring. (A)

### zkipster (evidence: A, Tier 2 product page + Tier 1 help-center collections)

- Market: luxury/fashion/art/sport-hospitality/diplomacy events; guest-list-first philosophy. (A)
- Name Badge Printing is a first-class product area in both "Produce" and "Manage" journeys. (A)
- Help-center structure (12 articles in the Name Badge Printing collection) documents a dual production mode: **Desktop printing** ("Compatible Avery Sheet Labels", "How to Print Name Badges on Desktop") and **On-site printing** ("Compatible On-site Printers and Paper Options", "Set Up On-Site Badge Printers with zkipster", "Print Name Badges at Check-In via the zkipster App"). (A)
- Design layer: "Designated Label Sizes for Specific Badge Dimensions", "How to Customize Your Badge Design", "How to use QR Codes on Name Badges"; same data also drives adjacent print artifacts ("How to Create Place or Escort Cards"). (A)
- Check-in app: iOS/Android, kiosk mode, QR/barcode scanning, offline mode; sessions and capacity management as a separate collection; troubleshooting/FAQ collection for badge printing. (A)
- Digital credential surface: Wallet Pass product — "Issue digital passes that your guests can save to their Apple or Google Wallet." (A)
- Guest "facesheets" (guest pictures) support visual verification at check-in (product-specific presentation of holder data). (A)

### ConfTool (evidence: A, Tier 1 administrator documentation)

- Badge production via data export: "Export Participants for Badges and Vouchers" (CSV/XLS, optional extra columns incl. booked events/items and totals) → mail merge in Word/OpenOffice using vendor-provided templates (name badges, participant list, 2×7 labels, square format, A4/A7). Rationale: "there are countless label sizes and formats … the ideas and concepts to design such printouts differ considerably." (A)
- Badge-specific data fields exist as first-class records: export includes "badge_fullname" and "badge_organization" — the names participants entered "specifically for the purpose to be printed on the name badges." (A)
- Direct bulk printing: filter registrations → "Create Name Badges for Current List" → PDF, one badge per page. (A)
- Registration-desk single-badge printing: configured at "Settings → Settings for Name Badges" (unit, page format/orientation, font — restricted to listed open-source fonts for licensing reasons, background image scaled to full-page width, per-element text with codes such as {person_id} and {event_xx_number}, HTML allowed, live preview). Stated purpose: "printing single badges on-site for people who register late … or people who have lost their badges." Suggests a label printer (e.g., Brother P-touch) for sticking labels on prepared badge stock. (A)
- Front Desk feature: dedicated user role "Front Desk / Registration / Student Volunteer" with deliberately limited rights — record arrival ("Quick Check In" with automatic date/time; undo recorded in the system log), check payment status (Paid/Unpaid), view registration details, record confirmation-of-participation signature and official-list opt-in, register new participants, create user accounts (with or without email). (A)
- Fee gate rule: direct "Arrival" quick check-in is disabled while payment is outstanding — the desk must go through "Front Desk Data" and explicitly confirm; "This is to avoid that participants are marked as arrived without further request." (A)
- Role hygiene: one system account per desk (or dummy accounts like "Front Desk Team 1") "so you can reproduce who did which updates"; payment handling and re-registration of cancelled participants reserved for Administrator/Assistant roles; desk segregation recommended (paid check-in desks vs unpaid/walk-in desks). (A)
- No scanning, RFID, or session/zone access machinery exists in this product — badges are identity artifacts, and access control is not part of the package. (A — absence observed)

---

## Cross-product Comparison

| Structure | Cvent | Stova | RainFocus | zkipster | ConfTool |
|---|---|---|---|---|---|
| Event-defined holder categories driving badges | A — VIPs/sponsors/speakers/staff layouts | A — "bespoke badging" (categories implied) | A — "customized badges" | A — design customization (categories via lists) | A — roles/statuses drive badge fields |
| Holder records from registration/import/walk-in | A — "dynamically from registration data"; walk-ins | A — integrated with Stova Registration or any provider | A — registration module feeds onsite | A — guest lists / RSVP / imports | A — registration module; walk-in account creation |
| Design template + data merge → artifact | A — Badge Designer, preview | A — bespoke badging | A — customized badges | A — design + label sizes + QR | A — mail-merge templates + badge settings |
| Pre-print (bulk, before event) | implied as the displaced mode | A — plastic/paper stock, services | n/e | A — desktop Avery sheet printing | A — mail merge + bulk PDF |
| On-demand at check-in | A — core claim | A — BadgeNext | A — kiosks | A — app printing at check-in | A — desk single-badge printing |
| QR/barcode on badge | A | A | A — "coded badge data" | A — QR article | n/e (no codes documented) |
| RFID/NFC/BLE/UHF | A — "optional RFID or NFC" | A — NFC/QR/BLE/UHF | A — scanners (technology unnamed) | n/e | n/e |
| Session/zone access control (admit/deny, capacity) | A — admit/deny, capacity, RFID/NFC | A — sessions **and zones**, compliance | A — session access & scanning | n/e (sessions = capacity mgmt only) | n/e — absent |
| Arrival/check-in recording | A — real-time alerts, reporting | A — check-in tracking | A — kiosks | A — check-in app | A — Quick Check In, dated/logged |
| Reprint / lost badge | A — "easy reprints" | n/e | n/e | n/e (troubleshooting only) | A — explicit lost-badge desk reprint |
| Fee gate at issuance | A — payment collection at check-in | n/e | n/e | A — payments (in-person) | A — quick check-in blocked while unpaid |
| Limited desk roles | implied (staffed desks) | implied (staffing services) | implied | implied | A — dedicated low-rights role, per-desk accounts, audit log |
| Real-time reporting | A — 15-min stats | A — real-time session dashboards | A — real-time data | A — event reporting | A — arrived/absent lists (simpler) |
| Offline tolerance | A — limited connectivity | n/e | A — offline kiosks | A — offline mode | n/e (local desk workflow) |
| Digital credential surface | weak (badge image shows app/QR) | A — app as digital badge | A — mobile app surface | A — Wallet Pass (Apple/Google) | n/e |
| Sustainability materials | A | A | n/e | n/e | n/e |
| Self-service kit vs full-service | A — Event-in-a-Box vs OnArrival 360 | A — BadgeNext vs bespoke + staffing | n/e | n/e | n/e |
| Adjacent print artifacts (lists, escort/place cards) | n/e | n/e | n/e | A — place/escort cards | A — participant list, labels |

Legend: A = direct official evidence; n/e = not evidenced in reachable sources (absence only treated as evidence where noted, e.g., ConfTool access control).

### Cross-product reading

- **B-layer commonalities (all or most of 5):** holder categories → badge differentiation; registration data as the holder source; design-template + data-merge rendering; on-demand issuance at check-in; arrival recording; real-time visibility for operators; walk-in/late-change handling.
- **B-layer commonalities (4 of 5, scale-correlated):** encoded badges (QR/barcode) readable by scanners; session-level access control with admit/deny and capacity; offline resilience; lead-retrieval consumption of badge codes.
- **Polarities, not omissions:** production mode (pre-print batches ↔ on-demand kiosk printing — both coexist across products, and zkipster ships both); credential medium (paper/plastic badge ↔ app/wallet pass); enforcement depth (identity badge ↔ session/zone access control). ConfTool proves the Type exists without scanning/RFID/access control; Cvent/Stova/RainFocus prove the same Type grows enforcement machinery at enterprise scale. Hence enforcement is a common mature extension, not a defining structure.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

The Type is recognizable iff all four hold:

1. **The event's credential-type program.** The event defines a set of holder categories (attendee, staff/crew, speaker, exhibitor, VIP, press, …; the set may be as small as one category), and the category determines the produced credential's content, appearance and — commonly — its access meaning. Remove → undifferentiated label printing.
2. **Holder assignment records.** Identified persons (from registration feeds, imports, or walk-in capture) are assigned to categories as maintained records — edited, moved between categories, voided — across the event's preparation-to-operation window. Remove → a mailing list / generic label sheet.
3. **Design-to-artifact rendering.** A design template per category (layout, brand, data fields such as name/organization/role/code) is merged with holder data to produce the credential artifact — a physical badge or an encoded/digital credential — with preview before production. Remove → a participant database.
4. **Issuance and replacement operations.** Production (pre-event batches and/or on-demand at check-in) and handover are managed operations with tracked state, including replacement printing for lost, damaged, or changed credentials. Remove → a one-shot design/print tool.

Historical check (older / regional / platform-native realizations): the paper-era workflow — badge stock, colored category passes, mail-merge or typewritten labels, desk reprints for late registrants and lost badges — satisfies all four structures when realized with software; nothing in the L0 requires RFID, kiosks, apps, or access control. ConfTool (academic, no scanning) and zkipster (luxury, desktop sheet printing) both pass; Cvent/Stova/RainFocus pass with modern machinery. Check passed.

### L1 — Common Mature Structure (very common; not definitional)

- Check-in integration: holder lookup (name/email/confirmation/QR/barcode) → issue badge → record arrival with timestamp.
- Encoded credentials: QR/barcode on the badge readable by handheld/kiosk scanners.
- Session/zone access control: scanners verify coded data; admit/deny decisions; capacity tracking; attendance analytics (dominant at enterprise scale; absent in the academic pole).
- Per-category badge layouts with brand controls and preview.
- Real-time operator reporting: check-ins vs registrations, per-session attendance, walk-in counts.
- Walk-in and last-minute edit handling with data currency ("badges reflect the most recent information" — Stova; "changes in real time" — Cvent).
- Reissue/reprint discipline for lost/damaged badges (explicit in ConfTool and Cvent).
- Registration-data integration spine (native platform modules or import/export; Stova claims provider-agnostic check-in integration).
- Fee interlock at the desk: payment collection at check-in (Cvent) or express check-in blocked until fees are settled (ConfTool).
- Low-rights desk roles so volunteers/staff can issue without touching payments/configuration (explicit in ConfTool; implied by staffed-desk services elsewhere).
- Offline-tolerant operation at the door (Cvent, RainFocus, zkipster).

### L2 — Variant / Optional Structure

- Contactless media: RFID/NFC/BLE/UHF encoding and handheld readers (Cvent, Stova; RainFocus unnamed scanners).
- Self-service kiosks and portable check-in carts, including remote issuance points (hotel lobbies, airports — Stova).
- Digital credential surfaces: event-app digital badge (Stova, RainFocus) and wallet passes (zkipster).
- Sustainability positioning: eco badge stock/lanyards, recycling, print-only-what-you-need (Cvent, Stova).
- Deployment poles: self-service kits for small/repeatable events vs full-service onsite staffing with PM, kiosks, printers (Cvent, Stova).
- Pre-print desktop pole: sheet labels (Avery-class), mail merge, bulk PDF (zkipster, ConfTool).
- Adjacent print artifacts from the same holder data: participant lists, place/escort cards (ConfTool, zkipster).
- Suspected security-led accreditation pole (sports/festivals/venues): zone-based entitlement matrices, production logistics, strict reissue control — **not directly researched this pass** (Accredit Solutions unreachable); recorded as a variant pole with lowered confidence.

### L3 — Vendor-specific (kept out of the final document)

- Cvent: Event-in-a-Box, OnArrival 360, "real-time event stats every 15 minutes", CE-credit signature tracking.
- Stova: BadgeNext branding; "bird-eye-view" session dashboards; specific hardware list.
- RainFocus: Nexus/AI agents; learning-center badging overlays; gift-redemption kiosks.
- zkipster: facesheets (guest pictures), compatible-printer/paper lists, place/escort card reuse of badge data.
- ConfTool: serial-letter templates, open-source-font licensing restriction, {person_id}/{event_xx_number} codes, HTML-in-PDF badges, Brother P-touch suggestion, per-desk dummy accounts ("Front Desk Team 1"), handout template for desk teams.

## Vendor-specific Findings

See L3. Additionally: RainFocus uniquely (in this sample) frames badges primarily as a data-capture instrument ("the key to unlocking rich engagement data"); Stova uniquely claims integration with third-party registration providers for check-in; ConfTool uniquely documents the fee-gate as an explicit designed rule with rationale.

## Rejected Findings (considered and excluded from the defining core)

- "Access control is definitional" — rejected: ConfTool-class realizations lack scanning/access machinery entirely and remain squarely in this Type; enforcement depth is scale/segment-dependent (L1/L2).
- "On-demand badge printing is definitional" — rejected: pre-printed batches remain a valid mode (ConfTool bulk PDF/mail merge; zkipster desktop); on-demand is the modern common pole, not the definition.
- "RFID/NFC is definitional" — rejected: only some products evidence it, and only as optional.
- "Digital badges / wallet passes are definitional" — rejected: recent layer over the same four structures.
- "Payments are part of the Type" — rejected as a core: payment handling belongs to Registration/Commerce; what this Type has is a fee *interlock* at issuance (verification and/or collection at the desk).
- "Badge design tools are the core" — rejected: design exists to serve issuance and enforcement; a design tool without holder records, categories, and issuance is not this Type.
- "Wristbands are the standard media" — no direct evidence in the reachable sample; not asserted anywhere.

## Boundary Findings

| Neighbor | Relationship | "Remove what → becomes the other Type" test |
|---|---|---|
| Event Registration Platform | upstream data feed | Remove the produced credential & issuance (keep forms/payment/confirmation) → Event Registration Platform. Remove registration (keep import/walk-in capture + credentials) → this Type still stands. Both directions hold ⇒ separate Types with a near-mandatory integration seam. |
| Event Ticketing Platform | adjacent commercial | Ticket = paid admission entitlement (transaction object). Credential = persistent on-site identity + category privileges (worn/presented continuously). Remove the holder identity/category (keep sellable admissions) → Ticketing. Tickets commonly become badges at the door — the handoff is the seam. |
| Attendee Management | broader lifecycle | Attendee Management owns comms/engagement/networking around the attendee; this Type owns the identity artifact. Remove the credential/issuance, keep engagement → Attendee Management. |
| Event Mobile App | adjacent surface | The app may carry the digital badge, but its center is content/agenda/networking. Remove agenda/engagement (keep the pass surface) → digital credentialing slice of this Type. |
| Event Lead Retrieval | downstream consumer | Exhibitors scan badge codes to capture leads; they do not manage credentials. Remove holder/credential management (keep exhibitor-side capture) → Event Lead Retrieval. |
| Event Agenda Management | sibling event-ops Type | Agenda owns the program of record (sessions/rooms/times); this Type owns who is present and what they may access. Session access control consumes agenda structure (sessions) — interlock, not overlap. |
| Building Access & Visitor Management | structural analog, different domain | Permanent-facility visitor control vs event-cycle credentialing (different cadence, categories, and production model). Remove event scoping/production → facility visitor management. |
| Digital Credential Platform (education) | homonym only | Achievement/verification badges (open badges) vs event admission/identity credentials. No shared core. |
| Cashless Venue Platform | shared hardware | RFID wristband payment loops center on money; this Type centers identity/access. Same media, different object of record. |

Boundary Issues to carry into STATUS.md:
1. Capability-vs-Type packaging: the Type is realized as standalone badging products, as named platform modules (Cvent "Check-in & badging", Stova Onsite, RainFocus On-Site), and as organizer-side features in conference systems (ConfTool). Same presentation pattern as sibling event leaves — Type stands, packaging is variant.
2. The security-led accreditation pole (sports/entertainment) may deserve its own Type if the zone-entitlement matrix (not the badge artifact) is the center of record. Insufficient evidence this pass — flagged for joint review rather than decided.

## Uncertainties

1. **Accreditation specialist family unverified**: Accredit Solutions (and similar sports/festival accreditation systems) unreachable; the zone-matrix accreditation pole is inferred from Stova's "sessions or zones" wording + general industry structure. No precise claims made anywhere.
2. **EventMobi / Bizzabo / Whova / Swapcard help centers unreachable** — the per-category design claim rests on Cvent's explicit VIP/sponsor/speaker/staff layouts plus weaker evidence elsewhere.
3. **Cvent knowledge base is a JS app** (support.cvent.com) — Cvent workflow details rely on product pages/FAQs (Tier 2), so fine-grained operator steps (e.g., exact designer mechanics) are unstated.
4. **Holder photo on the printed badge**: not evidenced (zkipster facesheets are check-in-side pictures); omitted from canonical statements.
5. **Badge return/collection at event exit**: not evidenced; unknown.
6. **Exact category taxonomies** (which products pre-define which categories): only Cvent's example set (VIPs, sponsors, speakers, staff) is documented; generalized cautiously.

## Final Synthesis

Event Credential / Badge Management is the event's identity-and-access artifact system. Its defining core is exactly four structures: (1) the event's credential-type program — holder categories the event defines, which drive content, appearance and (commonly) access meaning; (2) holder assignment records — identified persons bound to the event and a category, maintained through the event cycle; (3) design-to-artifact rendering — per-category templates merged with holder data into a previewed badge or encoded/digital credential; (4) issuance and replacement operations — pre-printed batches and/or on-demand production at check-in, tracked handover, and reprint discipline for loss, damage, or change.

Around that core, mature products add the check-in fusion (lookup → issue → record arrival), encoded credentials and scanner-based session/zone enforcement with capacity control, real-time operator reporting, walk-in handling with data currency, fee interlocks at the desk, deliberately limited desk roles, offline tolerance, and a registration-data integration spine. Variants span the production mode (pre-print ↔ on-demand), the medium (paper/plastic ↔ RFID ↔ app/wallet pass), the deployment pole (self-service kits ↔ full-service staffing), and segment tuning (conference/trade-show, luxury, academic, security-led accreditation). The Type is definable without any single technology: ConfTool's no-scanning academic realization and Cvent's RFID-enabled enterprise realization are both unmistakably this Type.
