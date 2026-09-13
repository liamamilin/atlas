# Research Notes — Nonprofit Event Management

Research date: 2026-09-08
Slug: nonprofit-event-management (DIRECTORY.md §25 "Nonprofit, Membership & Religious Organizations")

## Research Goal

Understand what software of the "Nonprofit Event Management" Type actually is and how it works: its core objects, its lifecycle, its users, and — critically — whether it is a genuine Application Type or merely an industry variant of generic event management (§26 Event Management Platform / Event Registration Platform). Produce the evidence base for a vendor-neutral Application Document.

## Initial Boundary (hypothesis before research)

- Likely software: tools for nonprofits to plan, promote, run, and settle fundraising events — galas, benefit auctions, walks/runs, golf tournaments, community events.
- Expected core tension: these products sit between two families — event management (§26: logistics/attendee-experience-first) and fundraising platforms (§25: giving-first). The defining question: is the **giving economy of the event** (donations, auctions, sponsorship, receipting) definitional, or just common?
- Nearest neighbors: Event Management Platform, Event Registration Platform, Event Ticketing Platform (all §26); Online Donation Platform, Fundraising Management Platform, Peer-to-peer Fundraising Platform, Donor Management System / Nonprofit CRM, Volunteer Management System (all §25); sibling leaves Association Event Management and Religious Event Management (§25).
- Known unknowns going in: volunteers in/out? sponsorship in/out? auctions definitional? receipting definitional? relationship to donor CRM?

## Research Questions

1. What core objects does this software maintain (event, registration, ticket, guest, donation, auction item, bid, sponsorship, payment, receipt)?
2. What is the lifecycle of an event from creation to post-event close, and who performs each step?
3. How do donations attach to the event (at registration, on-site appeals, paddle raises, auctions, raffles, non-attendee gifts)?
4. How is the event's money settled and acknowledged (checkout, statements, balances, receipts/thank-you letters)?
5. How do event contributions reach donor records / CRM?
6. What differentiates this Type from generic event management (§26) and from donation/fundraising platforms (§25)?
7. Historical check: does a paper-era charity event (RSVP cards, bid sheets, pledge cards, receipt letters) still fit the Type?

## Representative Products

Selected for market representation, documentation quality, and different product philosophies / customer tiers:

| Product | Positioning | Philosophy / pole | Docs reached |
|---|---|---|---|
| Bloomerang Fundraising (formerly Qgiv) | Mid-market fundraising suite | Events as one module of a giving platform (separate Auctions and P2P product lines) | Tier-2 product pages (events, auctions, CRM, platform) |
| OneCause | Event & auction fundraising specialist | Event-fundraising-first (Auctions & Events line), now part of Bonterra | Tier-2 product pages (event fundraising, ticketing, event admin) |
| GiveSmart | Event/auction fundraising platform (Momentive Software; formerly Community Brands; merged with MobileCause) | Auction/ticketing/guest-management-first with donor management attached | Tier-2 product page + customer quotes |
| Auctria | Dedicated charity auction & event software | Event-as-operation tool with unusually open documentation | **Tier-1**: full user guide (Academy) + product pages |

Rejected as primary samples: Givebutter (all help + main pages HTTP 403), Classy / GoFundMe Pro (403), BetterWorld (403), Blackbaud-family products (not attempted; time budget). Recorded as research limitation.

## Sources

Fetched 2026-09-08 (evidence tiers per product page type):

- Qgiv / Bloomerang Fundraising:
  - https://www.qgiv.com/ (platform overview; nav taxonomy: Donation Forms / Event Management / Text / Peer-to-peer / Auctions / Donor Management CRM / Data & Reports) — Tier-2
  - https://www.qgiv.com/events (Event Registration & Management product page) — Tier-2
  - https://support.qgiv.com/ — FAILED (transport error ×2; abandoned per retry rule)
- OneCause:
  - https://www.onecause.com/ (solution taxonomy: Auctions & Events / Peer-To-Peer / Online Fundraising / Text2Give; Payments) — Tier-2
  - https://www.onecause.com/solutions/auction-events/event-fundraising/ (feature detail) — Tier-2
- GiveSmart:
  - https://www.givesmart.com/ (solutions taxonomy incl. Ticketing & Guest Management, Mobile Bidding & Silent Auction, Donor Management, Nonprofit Accounting) — Tier-2
- Auctria:
  - https://auctria.com/ (features + Plan/Run/Close framing) — Tier-2
  - https://guide.auctria.com (Academy home) — Tier-1
  - https://guide.auctria.com/guide (full User Guide index: Event, Participants, Tickets, Items, Auctions, Donations, Raffles, Sponsorships, Item Donors, Financials, Credit Cards, Communication, Check-In, Checkout, Reports, Websites, Organizations, Printing, Import/Export) — **Tier-1, deepest source of this pass**
- givebutter.com + help.givebutter.com — FAILED (403 ×2); support.classy.org + classy.org — FAILED (403 ×2); betterworld.org — FAILED (403)

**Source-access limitation**: For Qgiv/OneCause/GiveSmart only marketing/product pages were reachable; their help centers were not. Precise operational mechanics (receipt templates, refund windows, fee defaults, exact ticket rules) are therefore NOT asserted from those products. Auctria's Tier-1 guide carries the detailed-mechanics burden. Givebutter and Classy absence means the freemium all-in-one pole and the enterprise campaign-suite pole are under-sampled; assertions were calibrated accordingly (no claims made about those two products).

## Product Observations

### Auctria (dedicated charity auction/event software) — evidence layer A (Tier-1 user guide unless noted)

- **Lifecycle naming**: the product's own guide is organized Plan → Run → Close ("from event creation to final reports"). Plan = set up organization + admins, add donors and items, connect credit cards, create event website. Run = participants register, bid, buy, donate (mobile or paper bid sheets; text-to-register). Close = record final bids and paddle-raise donations, send statements with payment links, close out and collect payments. (Tier-2 home page; confirmed by guide structure.)
- **Event as record**: Add/Change/Copy/Archive Event; Event Details; Event Permissions; "Health Checks" (configuration validation); Create Test Event (sandbox); multiple event types documented: In-Person, Online, Event With Tickets, **Donation Only Event**, Online Store event.
- **Participants (guests)**: participant records with **participant/bidder numbering** (incl. turning off paddle numbers, sharing numbers, printing paddles); link/unlink/merge participants (dedup); duplicate maintenance; multiple tickets per participant; catering choices; Registration/Checkout actions; **Statements** (emailed, printed, texted).
- **Tickets**: Add/Edit tickets incl. early-bird, early-bird **table** tickets, multi-day tickets; activate/deactivate; transfer tickets; repair/reissue; **Tables and Seating** (assign seating); **meal choices**; e-tickets; ticket claim; ticket statements; sell free/discount tickets; stop selling; refund tickets; ticket sales time windows.
- **Items** (auction/sale/giving units) with typed catalog: paper-bidding, live-bidding, online-bidding, for-sale, **donation items**, raffle prizes, buy-it-now-only, partial items; baskets/packages; item numbering & ordering (incl. live auction order); Fund-A-Need; **Peer-to-Peer as an item type**; pricing policy; coupon codes; sales tax; **Taxable Value**; gift certificates; after-event sales; multiple winners; re-open unsold items.
- **Auctions**: Online / **Paper** / Live auctions as first-class modes; kiosk-mode bidding (incl. device locking, slide shows); monitor auction; pre-bidding; max bidding; bid extension for bidders; promote/demote/edit/remove bids (bid correction is an organizer duty).
- **Donations**: Donations Dashboard; **Paddle Raise** (track paddle raise donations); Dessert Dash; record donation; donation items; text-to-give.
- **Sponsorships**: add & sell sponsorships; display sponsors (website sponsor catalog).
- **Item Donors** (in-kind): track who donated auction items; solicited items tracking; **Donor Receipts for item donors**; in-kind donation records. Distinct from monetary donors.
- **Money**: payment processors (Stripe, Authorize.Net) with test/live modes; registered cards on file; mobile card readers/swipers; **participant fee coverage** options; **"Make cc.fees Tax Deductible"** page; refunds (full/partial); record payment (non-card too); transfer payments; split bids at checkout; give event credits; batch checkout; **online pay-later**; "Email Participants With A Balance"; online payment links.
- **Financials**: Expenses (with categories); **Consignments** (items acquired on consignment).
- **Raffles**: create raffles, raffle tickets & prizes, run raffles.
- **Communications**: system emails (transactional) + custom emails; email ticket holders; **email participants with a balance**; text messages incl. text-to-give; ticket sales communication; transactional vs marketing distinction.
- **Websites**: per-event website with editor (item catalog, donation element, donor catalog, sponsor catalog/row, leaderboard, progress tracker, countdown); QR code; visitor tracking.
- **Guest-facing**: event website; self check-in request; My Account; **Ticket Hub** (update ticket details); placing bids; mobile bidder app; text bidding.
- **Day-of surfaces**: Check-In (by organizer; self check-in; settings), Bidding dashboard, Donations dashboard, Sales dashboard, **Admin mobile app** (check-in, checkout, sales, scan QR, charge cards, card readers).
- **Reports**: item / donor / participant / ticket & sponsorship / financial reports; bulk editing; tags; export; **LGL (Little Green Light) export** — explicit donor-CRM handoff.
- **Printing**: bid sheets (customizable, pre-populated), participant paddles, thank-you letters ("Generate Donor Thank You Letters"), event catalog booklet, labels, stationery, gift certificates.
- (Tier-2 home page adds: sectors served — education, animal, healthcare, religion, arts, corporate, international; "From the first donation to the last receipt".)

### OneCause (event & auction fundraising specialist) — evidence layer A (Tier-2 product pages)

- Nav taxonomy splits **Auctions & Events** (event fundraising, mobile bidding, ticketing, virtual fundraising, event admin, golf events) from **Peer-To-Peer** (runs/walks/rides, giving days, DIY, ambassador) and **Online Fundraising** (donation forms, giving sites, personal pages, Text2Give) — the market itself separates event fundraising from P2P and from pure online giving.
- **Integrated Ticketing**: sell tickets and manage fundraising in one platform; ticket types for in-person and virtual guests; ticket packages, questions, promo codes; attendees manage their own ticket preferences.
- **Registration & Checkout**: QR code check-in; **volunteers equipped with event-day tools**; guests manage/update their own profiles; self-checkout and item pickup to minimize lines.
- **Table Management**: drag-and-drop seating (seated/unseated guests); group tables by **captains, sponsors, VIPs**; per-table analytics; table scoreboards.
- **Sponsorship Sales**: create and sell sponsorship packages online; logo sizing **by contribution level**; gamification; track impressions/engagement for sponsor ROI.
- **Donation Appeals**: in-person or virtual donation appeals and **paddle raises**; configure **seed amounts and donation commitments**.
- **Live & Silent Auctions**: item procurement, item galleries, AI assistance.
- **Real-time Scoreboards**: current bids, donation progress, donor recognition.
- **Guest Communication**: automated/custom text messages; event-specific and year-round messages.
- **Donor Management**: view all donor contributions and purchases; **configure post-event donor receipts**; donor activity **at the individual event level or across events**.
- Events connect to online campaigns (in-person + virtual giving); "unlimited events" per contract (plan page).

### GiveSmart (event/auction platform + donor management) — evidence layer A (Tier-2 product page; quotes are customer voices)

- Solutions taxonomy: Mobile Bidding & Silent Auction / Virtual & Hybrid / Event & Campaign Fundraising / Online Fundraising / **Nonprofit Accounting (MIP)** / Peer-to-Peer / Data & Integrations / **Ticketing & Guest Management** / Growth Fundraising / **Donor Management**.
- Event ticketing: **assign seats, automate reports, distribute bidder numbers, contactless check-in**.
- Auction management, mobile bidding, **live event displays**, streaming/chat/backstage for virtual-hybrid, **sponsor activation**, text-to-donate.
- Donor management: track donors, thanking, retention; **thank-you letter wizard**; **multi-payment pledges, gifts of stock or property, in-kind services**; wealth capacity screening; reporting for stewardship.
- Customer quote (volunteer/access): "add other users and **volunteers for different levels of access**".
- Customer quote (scope): "from simple registration and check-in, to full-scale galas with complex order forms, **onsite upsells**, live auctions, seating management".
- Customer quote (close): "ease in auction bookkeeping, payments, and generating **post-event thank you/tax letters**".
- Customer quote (sponsors): platform used "to make sales online and to track and display ads for our sponsors" (Rotary club).

### Bloomerang Fundraising / Qgiv (fundraising suite, events module) — evidence layer A (Tier-2 product pages)

- Suite taxonomy: Donation Forms / **Event Management** / Text Fundraising / **Peer-to-Peer** / **Auction Fundraising** / **Donor Management CRM** / Data & Reports. Auctions and P2P are **separate product lines from Events** — auction is NOT bundled into the events module by this vendor (packaging evidence, not capability absence).
- Events page: customizable mobile-friendly **registration forms**, branded pages, **multi-attendee sign-ups**, website integration.
- **Guest management**: flexible ticketing, discounts, multi-attendee options, **QR code check-in**, **drag-and-drop table seating**.
- **Custom fields** for guests (dietary needs, preferences) to personalize and follow up.
- **Donations and appeals**: "adding donation options to event registration", fee coverage via **GiftAssist**, **personalized donor receipts**.
- **Promotion tools**: social sharing, email invites, reminders.
- **Reports & analytics**: dashboards, reports, **CRM integration** — "all your registration and attendance data in one place"; events framed as increasing "registrations, sponsorships, and donations" (sponsorship named, not detailed).
- Platform positioning: giving platform for nonprofits; CRM manages "donors, volunteers, sponsors, foundations".

## Cross-product Comparison

| Structure | Auctria (T1) | OneCause (T2) | GiveSmart (T2) | Qgiv/Bloomerang (T2) | Layer |
|---|---|---|---|---|---|
| Event as persistent record (create/config/copy/archive, multiple event types) | ✔ explicit | ✔ "unlimited events", event admin | ✔ contracts, unlimited events | ✔ event creation | B |
| Public event website / branded registration page | ✔ website editor | ✔ ticket page, personalized | ✔ customizable site + order forms | ✔ branded pages | B |
| Ticket/RSVP registration (tiers, packages, promo codes, discounts) | ✔ incl. tables, early-bird | ✔ | ✔ | ✔ | B |
| Multi-attendee registration under one purchaser | ✔ (multiple tickets) | ✔ (ticket packages, questions) | ✔ (order forms) | ✔ explicit | B |
| Custom questions (meals, dietary, preferences) | ✔ (catering, custom questions) | ✔ (ticket questions) | — (implied by order forms) | ✔ explicit | B |
| Table / seating management | ✔ (table tickets, assign seating) | ✔ (drag-drop, captains/sponsors/VIP) | ✔ (assign seats) | ✔ (drag-drop) | B |
| Check-in (QR / contactless) + credentials (paddles/bidder numbers) | ✔ (organizer + self check-in; numbering; print paddles) | ✔ (QR check-in) | ✔ (bidder numbers, contactless) | ✔ (QR check-in) | B |
| Guest self-service (profile, tickets, self check-in) | ✔ (My Account, Ticket Hub, self check-in) | ✔ (manage own profiles) | — | — | B (3/4) |
| Donations captured in event context (registration giving, appeals) | ✔ (donation items, record donation) | ✔ (donation appeals, paddle raise, seed amounts, commitments) | ✔ (text-to-donate; onsite upsells) | ✔ explicit ("donation options on registration") | B |
| Paddle raise / fund-a-need | ✔ (paddle raise, fund-a-need, dessert dash) | ✔ (paddle raise) | — (implied by mobile bidding events) | — | B (2/4) |
| Auctions (silent/live/online, items, bids) | ✔ deep (paper/live/online) | ✔ | ✔ (mobile bidding, auction mgmt) | separate product line (not in events module) | B — **common but packaging varies** |
| Raffles | ✔ (raffle module) | — | ✔ (blog/resources; 50/50 guidance) | — | B (2/4), thin |
| For-sale items / merchandise / onsite upsells | ✔ (for-sale items, after-event sales) | ✔ (item pickup, self-checkout) | ✔ ("onsite upsells") | — | B (3/4) |
| Sponsorship packages + recognition | ✔ (sell, display, sponsor catalog) | ✔ (levels, logo sizing, ROI) | ✔ (activation; sponsor ads) | ✔ named | B |
| Text giving / text engagement | ✔ (text-to-give, text bidding, text-to-register) | ✔ (Text2Give) | ✔ (text-to-donate) | ✔ (text product line) | B |
| Day-of admin surfaces (check-in/checkout screens, admin app, live displays) | ✔ (dashboards, admin app, kiosks) | ✔ (event-day tools, scoreboards) | ✔ (live displays) | — | B (3/4) |
| Settlement incl. balances owed / pay-later / statements with payment link | ✔ explicit (statements, balances, pay later, split bids, transfers) | ✔ (self-checkout) | ✔ ("auction bookkeeping, payments") | — | B (3/4), Auctria deepest |
| Refunds / payment correction | ✔ (full/partial refunds, transfer payments, delete purchases) | — | — | — | A only (T1) — keep qualified |
| Receipts / thank-you / tax letters | ✔ (donor receipts, thank-you letter printing, cc fees deductible) | ✔ (post-event donor receipts) | ✔ (thank-you/tax letters wizard) | ✔ (donor receipts) | B — **strongest cross-product signal of the nonprofit overlay** |
| Fee coverage (donor pays processing fee) | ✔ (participant fee coverage; fees deductible) | — | — | ✔ (GiftAssist) | B (2/4), named differently |
| Event expenses / financial reporting | ✔ (expenses, consignments, financial reports) | ✔ (ROI framing) | ✔ (bookkeeping quote) | ✔ (ROI framing) | B, depth varies |
| Contributions attributed to donors per event, viewable across events | ✔ (donor reports) | ✔ explicit | ✔ (donor management) | ✔ (CRM integration) | B |
| Donor CRM handoff (export/integration/embedded) | ✔ (LGL export) | ✔ (embedded donor mgmt) | ✔ (embedded + integrations) | ✔ (suite CRM) | B — **embedded vs external is packaging, handoff is structural** |
| Volunteers (event-day tools / access levels) | — (guide is volunteer-training-friendly) | ✔ (volunteer event-day tools) | ✔ (volunteer access levels) | ✔ CRM mentions volunteers | B (weak) — L2 |
| Virtual / hybrid events (streaming, displays, chat) | ✔ (online events, kiosks) | ✔ (virtual guests, virtual fundraising) | ✔ (virtual & hybrid line) | — | B (3/4) — era machinery, L2 |
| Goal / progress displays | ✔ (progress tracker, leaderboard) | ✔ (scoreboards, progress) | — | — | B (2/4) — common but keep moderate |

**Reading of the table** (Step 6 — Compare):
- Registration machinery + event record + giving-in-event-context + settlement/acknowledgment appear across all four samples → **Core**.
- Auctions are the most emblematic giving mechanic but are **packaged inconsistently** (bundled deeply in 3; separate product line in 1) → Common, NOT definitional.
- Receipting/acknowledgment is the **only structure whose presence is both universal and nonprofit-specific** (generic event platforms have no receipts) — but it is the closing behavior of the money leg rather than a standalone leg.
- Volunteers, virtual/hybrid, raffles, goal displays → Common-to-Optional.
- Bid correction, consignments, expenses, refunds detail → documented deeply only by the Tier-1 source; keep qualified in the final document (the *actions exist*, exact depth is product-specific).

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (jointly held; remove any one → different Type)

1. **The fundraising event as the managed record.** A persistent, identified event run by a cause organization (charity, school, faith body, service club, association chapter) whose purpose includes raising money. The event is created, configured, published, run, and closed as the organizing unit to which registrations, giving, and money all attach.
   *Remove →* unconnected registration/donation tools; or a generic calendar/project entry.
2. **Attendee registration & admission machinery.** The event takes registrations (paid tickets, table packages, free RSVPs), records guests as identifiable records (commonly purchaser + multiple attendees, with tables/seating and per-guest details), and admits them (check-in, credentials).
   *Remove →* a giving campaign with an event flyer: Online Donation Platform territory. Without admission machinery the Type loses "event" as an operational object.
3. **Event-linked giving machinery.** Donations are captured as a first-class outcome in the event's context — giving options at registration, on-site appeals (paddle raises / fund-a-need), event-run auctions/raffles/sales as giving mechanics, sponsorship purchases — with money raised tracked against the event, alongside (and distinguished from) ticket revenue.
   *Remove →* a generic event registration platform (ticket sales only): §26 territory.
4. **Settlement & acknowledgment of the event's money.** The event's takings (tickets, bids, purchases, donations, sponsorships) resolve into recorded payments and balances owed; balances are settled at on-site checkout or post-event via statements/payment links; contributions are acknowledged (receipts, thank-you/tax letters) and recorded as donor-attributed contributions that flow to the organization's donor records.
   *Remove →* RSVP list + an opaque tip jar; the "management" of the money side disappears, and the nonprofit overlay (acknowledgment, donor attribution) disappears with it.

**Jointly-held test**:
- 1 alone = event entry in a calendar/project tool
- 2 alone = Event Registration / Ticketing Platform (§26)
- 3 alone = Online Donation / giving campaign (§25)
- 4 alone = payment collection
- 1+2 without 3+4 = generic event management/registration
- 1+3 without 2 = online fundraiser wearing an event's name
- 2+3 without 1 = scattered tools with no event of record
- 3+4 without 1+2 = donation processing
- 1+2+3 without 4 = money side unmanged — no close, no receipts; fails all four samples' documented Close phase (Auctria's explicit "Close"; OneCause "post-event donor receipts"; GiveSmart "post-event thank you/tax letters"; Qgiv "personalized donor receipts")

### §24 Historical / market-sample check

Paper-era charity ball / benefit auction: event file with budget and committee notes (leg 1); invitation + RSVP card + ticket/table list + seating card + door list (leg 2); silent-auction bid sheets, paddle raise, raffle tickets, pledge cards, sponsor banners (leg 3); treasurer's tally, settled bills, receipt/thank-you letters, ledger entries per donor (leg 4). **All four legs satisfied in analog form.** Modern machinery — mobile bidding, text-to-give, event websites, QR check-in, scoreboards — is era tooling, not definition. Continuity is vendor-documented: Auctria still operates **paper auctions** and prints **bid sheets and paddles** from the system alongside online bidding; the invariant is "bids/gifts recorded against identifiable participants," not "mobile." **Check passed; definition names no specific technology.**

### L1 — Common Mature Structure (market-expected, not definitional)

- Public event website / branded registration page with content blocks (item catalog, sponsor recognition, goal progress)
- Ticket tiers & packages (early-bird, tables, multi-day), promo codes/discounts, multi-attendee under one purchaser, custom questions (meals, dietary)
- Check-in (QR, self-service) and credentials (paddle/bidder numbers)
- Table/seating management with drag-and-drop
- Auctions (silent/live/online) with item catalog and mobile bidding; raffles; for-sale/merchandise items
- Donation appeals: at registration, paddle raise / fund-a-need; donation progress displays
- Sponsorship packages with level-based recognition
- Guest/donor communications: confirmations, reminders, statements (email/SMS)
- Dashboards & reports (income, items, donors, participants); event expenses in the deepest product
- Receipts/statements/thank-you letters; payment processing with donor fee coverage; refunds
- Donor CRM handoff (export, integration, or embedded donor management)
- Organizer/volunteer roles with limited access; day-of admin surfaces

### L2 — Variant / Optional Structure

- Virtual/hybrid events (streaming, live displays, chat, backstage management) — post-2020 era machinery
- Online-only events and donation-only events as event configurations
- Paper bid sheets coexisting with mobile bidding; kiosk-mode bidding
- In-kind item donations: item donors, solicitation tracking, consignments
- Pledges / multi-payment commitments; stock & property gifts; in-kind services
- Wealth-capacity screening of event donors
- Gamification: scoreboards, leaderboards, table competition
- Sales-tax on taxable items / modeling value of goods received vs gift portion (deductibility mechanics; named machinery observed in one product only — treat cautiously)
- Peer-to-peer tie-ins inside the event (fundraising pages as item types)
- Catering/meal operations depth; event-day upsells
- Sandbox/test events; event health checks
- Vendor services layer (event-day staffing, done-for-you setup)

### L3 — Vendor-specific (Research Notes only)

- **GiftAssist** (Qgiv/Bloomerang) — branded donor fee-coverage feature.
- **Text2Give®** (OneCause) — trademarked text-giving; also "Scoreboard" naming.
- **Auctria**: specific item-type taxonomy (paper/live/online bidding types, partial items, dessert dash), "Health Checks", Admin mobile app, Launch/Assist service packages, Little Green Light (LGL) export as a named integration.
- **GiveSmart**: bidder-number workflow naming; Momentive Software suite (MIP nonprofit accounting sibling); MobileCause merger; "thank-you letter wizard".
- **Corporate events in the market**: Bonterra acquiring OneCause; Qgiv rebranding to Bloomerang Fundraising; Community Brands → Momentive for GiveSmart. Market-consolidation context only.
- Sector page claims (e.g., "$X billion raised", customer counts) — marketing, not structure.

## Vendor-specific Findings (summary)

See L3 above. None of these enter the canonical document. Note also the **packaging poles**: embedded donor management (OneCause, GiveSmart) vs suite-CRM sibling (Qgiv/Bloomerang) vs export-to-CRM (Auctria) — three realizations of the same structural handoff; and auctions bundled (Auctria, OneCause, GiveSmart) vs sold as separate module (Qgiv/Bloomerang).

## Rejected Findings (over-fitting guards)

- "Nonprofit event management = auction software" — REJECTED. Qgiv/Bloomerang sells Auctions as a separate product line from Events; auctions are the emblematic giving mechanic, not the definition.
- "Definition includes mobile bidding" — REJECTED. Paper bid sheets and printed paddles are first-class in the deepest Tier-1 sample; the era-neutral invariant is bids/gifts recorded against participants.
- "Definition includes peer-to-peer pages" — REJECTED. P2P is a separate product line in two of four vendors' own taxonomies and appears inside events only as an optional tie-in.
- "Definition includes volunteers" — REJECTED as definitional; evidence is thin (event-day tools, access levels) → L2.
- "Definition includes sponsorship" — REJECTED as definitional (universally present but described shallowly in 1/4, absent as named capability from none) → L1 Common, not Core.
- "Ticket revenue and donations are the same money" — REJECTED. Systems model them as distinct item/transaction classes (for-sale vs donation items; receipting consequences), which is precisely why the settlement leg must distinguish them.
- "Tax-deductibility split of goods vs gift is standard" — NOT ASSERTED. Named machinery (taxable value, deductible fees) observed in one product; kept at L2 with qualified wording.

## Boundary Findings

- **vs Event Management Platform (§26)**: the generic type centers on the attendee experience and logistics — agendas, sessions, speakers, venues, event apps, exhibitor/lead machinery. This Type centers on the **event's fundraising economy**: giving is a first-class outcome, money closes with receipts, and contributions attribute to donors. Removal test in both directions: remove giving machinery + acknowledgment from this Type → generic event registration/management; add donation-appeal/auction/receipt mechanics as the *purpose* of the product → it becomes this Type. Ticket-only money flows belong to §26.
- **vs Event Registration Platform / Ticketing Platform (§26)**: registration is one leg here, not the whole. A product with only registration/ticketing is the §26 type even if a nonprofit uses it.
- **vs Online Donation Platform (§25)**: donation platforms center on the gift campaign; no attendance machinery (registrations, tables, check-in, seating) and no event-of-record operations. A "donation-only event" configuration exists *inside* this Type's products (documented Tier-1) without collapsing the Type — the product still carries the registration machinery.
- **vs Fundraising Management Platform (§25)**: that type runs the year-round development operation (campaigns of many kinds, stewardship pipelines); this type is event-scoped. The structural seam is the donor-record handoff.
- **vs Peer-to-peer Fundraising Platform (§25)**: P2P centers on supporter-led pages recruiting their own networks; events there (walks/runs) are participation vehicles. Market evidence: Qgiv and OneCause both split P2P from Events into separate product lines. Boundary for walk/run events is genuinely thin — overlap flag.
- **vs Donor Management System / Nonprofit CRM (§25)**: the CRM is the year-round constituent record of record. This type records event-level contributions and hands them off (export, integration, or embedded module). Embedded vs external CRM is packaging, not boundary.
- **vs Volunteer Management System (§25)**: program-level volunteer workforce management vs the event-day tools/access levels present here. Thin overlap.
- **vs Association Event Management / Religious Event Management (§25 siblings)**: NOT RESEARCHED this pass. Structural observation only: association events (conferences, CE) and religious events (retreats, services) appear to center on membership/community logistics rather than the fundraising economy; whether they are variants of §26, of this Type, or independent types must be decided by their own passes. Recorded in STATUS.md.
- **vs Online Auction Platform (§05.18)**: commercial auction platforms center on marketplace/seller economics; here the auction is a **giving mechanic inside an event**, with donor receipts and in-kind item donors.

## Uncertainties

1. **Givebutter and Classy unreachable (403)** — the freemium all-in-one pole and the enterprise campaign-suite pole are under-sampled. All cross-product claims rest on 4 products (1 Tier-1 + 3 Tier-2). No claims were made about the two unreachable products.
2. **Help centers of Qgiv/OneCause/GiveSmart unreachable** — mechanics asserted only where product pages state them; precise rules (refund windows, receipt formats, fee defaults) deliberately absent.
3. **Deductibility mechanics** (partial deductibility of ticket/goods value, deductible processing fees) — named pages observed in one Tier-1 source only; final document states the behavior qualitatively, not the mechanics.
4. **Regional market** — sample is US/North America-heavy (all four products US-centric). Older regional charity-event tooling covered only via the analog historical check.
5. **Goal tracking** — progress displays documented in 2/4; kept at moderate strength ("commonly") in the final document.
6. **Association/Religious sibling leaves** — flagged, not resolved here.

## Final Synthesis

Nonprofit Event Management is the cause-organization's **fundraising-event system of record**: a persistent event of record (1) carries registration/admission machinery (2) and event-linked giving machinery (3) through a Plan → Run → Close lifecycle, and ends in settlement and acknowledgment (4) — money resolved, balances chased, receipts issued, contributions attributed to donors. The four legs are jointly held; removing any one yields an adjacent Type (event registration, donation platform, payment collection, or an unmanged tip jar). Auctions, sponsorship, text giving, mobile bidding, and volunteer tools are the common furniture of mature products; virtual/hybrid, pledges, in-kind, wealth screening, and paper/kiosk modes are variants. The nonprofit overlay is visible exactly where the money closes: receipts, thank-you letters, and donor-attributed contribution records handed to the organization's donor records.
