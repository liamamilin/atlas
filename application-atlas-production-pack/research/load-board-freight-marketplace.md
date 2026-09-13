# Research Notes — Load Board / Freight Marketplace

## Research Goal

Understand the shared market venue of truckload freight (directory leaf §18 "Load Board / Freight Marketplace", slug `load-board-freight-marketplace`): what the venue's world consists of, how a load moves from posting to match, what makes the venue structurally different from the brokerage platform (one intermediary's system of record), the TMS (operational system), the trucking TMS (carrier's own system), and the Job Board (same venue shape, different domain).

This leaf owes answers to two recorded seams:

1. The processed **Freight Brokerage Platform** pass (2026-09-08) flagged this leaf for joint review: "market venue (many brokers ↔ many carriers) vs one brokerage's system of record; board integration is standard capability in 3/3 sampled brokerage platforms while venue membership is not; internal coverage/dispatch boards inside brokerage platforms are surfaces, not the marketplace." Its structural test also pre-named this Type: "1+3 without 2 = matching with no held economics = load-board territory."
2. The processed **service-marketplace** pass (2026-09-07) listed load-board §18 among the domain-structured marketplace siblings under the generic marketplace umbrella — consistent with keeping this as its own domain-structured Type.

## Initial Boundary

Working hypothesis before research:

- A load board is a market venue where holders of freight (freight brokers, shippers) publish load postings and motor carriers / owner-operators search them and respond (call, bid, book). The venue aggregates many posters' supply into one searchable pool. It is not any single company's system of record and (in the neutral posture) holds no transaction economics.
- A freight marketplace is the same venue with deeper in-platform transaction (instant booking, platform-held pricing) — the directory names both in one leaf, so the booking-depth axis is expected to be a variant, not two Types.
- Nearest neighbors: Freight Brokerage Platform (system of record vs venue), TMS (execution system), Trucking Management System (carrier's own ops), Job Board (same shape, employment domain), Classifieds / Listing Marketplace (generic venue), Dispatch Management (assignment act), Shipment Visibility (watching layer).
- Unknowns: is rate/market data definitional? Are truck postings (reverse direction) definitional? How deep does trust machinery go? Regional variants (European freight exchanges)?

## Research Questions

1. What is the unit of market record (the posting), and what does it carry (lane, equipment, dates, rate, weight)?
2. Who are the two sides, and what does each do on the venue?
3. What does the search/discovery loop look like (filters, saved searches, alerts, maps)?
4. What response paths exist (call, bid, book-now), and where does the commitment happen (on/off platform)?
5. Is rate/market data definitional or common?
6. What trust machinery exists (carrier verification, broker credit, days-to-pay)?
7. Do truck postings (reverse direction) exist across products?
8. What monetization models exist (subscription, free, transaction)?
9. How do neutral venues vs principal-operated marketplaces differ, and where is the seam vs the brokerage platform?
10. Historical check: does the physical/phone-based board era fit the same core?
11. Boundary tests vs brokerage platform, TMS, trucking TMS, job board, classifieds, dispatch, visibility.

## Representative Products

| Product | Segment / philosophy | Why chosen | Evidence tier |
|---|---|---|---|
| Uber Freight | Principal-operated digital freight marketplace; the operator is itself a licensed freight broker; instant booking, upfront pricing; enterprise shippers + carriers | The marketplace-deep pole and the straddle pole (operator holds the transaction); explicit broker disclaimer | Tier-1/2 official pages (root, carriers, freight-shipping) |
| TruckSmarter | Neutral free venue + aggregator; "not a broker, or a dispatcher"; in-app bid & book; AI dispatch assistant; owner-operator/small-carrier segment | The neutral-venue pole with modern aggregator posture; richest official FAQ/glossary | Tier-1 official pages (root, free-load-boards, brokers, glossary, help center index) |
| Direct Freight | Classic subscription load board; two-direction (loads + trucks); rate tool, credit/authority info; SMB carriers and brokers | The classic board pole with the reverse (truck) direction and poster-side trust info | Tier-1/2 official homepage + feature list |

Rejected/abandoned samples (per source-abandonment rule): DAT (root and product pages HTTP 403 ×3; help.dat.com resolves to a dead Bitly domain), Truckstop (root and /support/ 403; Zendesk help center closed), 123Loadboard (root 403; help subdomain timeout), TimoCom (European freight exchange; two timeouts — the regional variant is recorded as an uncertainty, not asserted). DAT, Truckstop, and 123Loadboard are nonetheless documented **indirectly**: they appear by name in the Tier-1 integration lists of the brokerage-platform pass (Tai TMS: "integrated load-board access (DAT, Truckstop, 123Loadboard)"; Alvys: "Post and source freight on DAT, Truckstop, and other boards"), and in TruckSmarter's comparison table (competitor-claimed pricing/figures — Tier-3, recorded but not asserted).

## Sources

- Uber Freight — homepage: https://www.uberfreight.com/ (2026-09-09)
- Uber Freight — Carriers / "Haul with us": https://www.uberfreight.com/en-US/carriers (2026-09-09)
- Uber Freight — Uber Freight Shipping (shipper platform): https://www.uberfreight.com/en-US/technology/freight-shipping (2026-09-09)
- TruckSmarter — homepage: https://www.trucksmarter.com/ (2026-09-09)
- TruckSmarter — Free load board page + FAQs: https://www.trucksmarter.com/free-load-boards (2026-09-09)
- TruckSmarter — Brokers page + Broker FAQs: https://www.trucksmarter.com/brokers (2026-09-09)
- TruckSmarter — Glossary: https://www.trucksmarter.com/glossary (2026-09-09)
- TruckSmarter — Help Center index: https://help.trucksmarter.com/ (2026-09-09)
- Direct Freight — homepage + feature list: https://www.directfreight.com/ (2026-09-09)
- Prior sibling research (context, not new fetches): research/freight-brokerage-platform.md, applications/freight-brokerage-platform.md, applications/job-board.md, applications/transportation-management-system-tms.md, STATUS.md seam notes.

## Product Observations

### Uber Freight (principal-operated digital marketplace)

Evidence layer: A (direct, official pages).

- Self-definition of posture, verbatim footer on every page: "Uber Freight is a licensed freight broker and is not a motor carrier." The operator is a principal, not a neutral venue.
- Carrier side ("Haul with us"): "Access freight from the world's largest shippers on one of the industry's largest and most secure networks." "Uber Freight is one of the only brokerages that provides real-time, upfront pricing to help you book and haul with confidence."
  - "Keep your trucks moving with **instant load bookings**" — in-platform booking is the response path.
  - "upfront, real-time visibility into linehaul and fuel rates" — the price is shown before booking.
  - Equipment: "dry van, flatbed, reefer, and power-only loads."
  - Supply breadth: "power-only tours, dedicated lanes, and dedicated fleet opportunities" — spot AND contract freight; app + web portal surfaces.
- Shipper side (Uber Freight Shipping): "quoting, booking, and tracking shipments in less than five minutes"; "get and compare quotes for both full truckload and less-than-truckload shipments, allowing you to **book instantly or lock in rates for 90 days**"; FTL priorities ("set priorities for FTL shipments to access better rates based on your flexibility"); ERP integration (NetSuite); LTL insurance via third-party partner.
- Company posture has widened beyond the marketplace: managed transportation, capacity solutions ("comprehensive carrier marketplace"), an enterprise TMS ("marketplace technology… continuously match freight to the optimal carrier"), integrations/APIs. The marketplace surface sits inside a multi-product logistics company — the straddle pole.
- Scale claims (marketing, recorded not asserted): $17B+ freight under management, 18M shipments annually, 1.8B transactions annually.

### TruckSmarter (neutral free venue + aggregator)

Evidence layer: A (direct, official pages incl. FAQs and glossary).

- The vendor's own definition of the Type (FAQ): "A load board is a freight matching service that helps connect shippers to carriers, connecting demand with capacity. **Originally a cork board and push pins**, today's most common load boards are online marketplaces where truck owner-operators, shippers, and freight brokers can post the loads they have available and find available loads." — includes the historical anchor.
- Neutral-venue posture, verbatim: "Our load board **pulls loads from other sources into one location**… We are **not a broker, or a dispatcher**. We also do not control the prices or conditions of the loads — this is information set by the brokers themselves."
- Aggregator mechanics: "some brokers don't agree with this and restrict access to their loads. In order to view, bid, or book their loads, you need to **connect your load board account for that broker**. We recommend linking all of your existing load boards…" — postings sourced from other boards; linked-account access control.
- Carrier-side loop: "Find loads, compare rates, check market and fuel data, and book freight through one conversation" (AI Dispatch); "Compare, bid on, and book the best loads from one easy place"; "Instant bid and book — Connect with trusted brokers and bid and book right in the app."
- Load detail fields: "Rate, RpM, deadhead, weight, equipment, pickup windows, everything you need to size up a load before you ever call a broker."
- Search machinery: filters (truck type, location, broker; include/exclude specific brokers), sliders (trailer length, price, rate per mile, weight, distance), saved favorite lanes, saved loads.
- Backhaul support: "Find the best backhaul before you drop… accurate deadhead estimates, and the ability to book multiple legs at once."
- Trust machinery, both directions: carriers — "Every carrier on our app has been vetted… we require carriers to verify their carrier identity by either uploading documents to verify insurance and authority or connecting a broker account" (required to view/bid/book); brokers — "Every broker we partner with goes through a credit check."
- Poster side (brokers): "Post loads, get bids, and book carriers directly"; posting via "TMS, integrated partnerships with Parade, Newtrul, and LoadBoard Network, email or CSV upload, and direct API integration"; Broker Dashboard to "monitor and adjust loads"; unlimited free postings.
- Monetization: 100% free board (both sides); the company monetizes adjacent fintech — "Factoring for OTR," banking services (footer disclosures). AI Dispatch as the differentiating layer.
- Equipment scope: "Van, reefer, flatbed, power only, step deck, conestoga, container, box truck, hot shot, and car hauling."
- Comparison table vs DAT / 123LoadBoard / Truckstop (competitor-claimed figures — Tier-3, recorded not asserted): DAT $49–$149/mo, 700,000+ daily loads, lane rate insights paid-only; 123LoadBoard from $35/mo, 123,000+; Truckstop from $45/mo. Confirms the market structure: paid subscription incumbents vs free entrant.
- Glossary (official domain vocabulary): "Load board: An online marketplace where carriers can find available freight posted by brokers and shippers, displaying details like pickup/delivery locations, rates, weight, and equipment requirements." Also: Rate Confirmation ("the 'contract' between the driver and broker listing the load details and agreed upon rate"), deadhead, backhaul, RPM, line haul, load-to-truck ratio, lane, quick pay, factoring terms, MC/DOT numbers, FMCSA, HOS, equipment taxonomy.

### Direct Freight (classic subscription board)

Evidence layer: A (direct, official homepage/feature list).

- Two-direction structure in the site's own navigation: Carriers/Owner Operators — "Find Loads, Loads Map, **Post Trucks**, View My Trucks, Recent Searches & Alerts"; Shippers/Brokers — "Find Trucks, Truck Map, **Post Loads**, View My Loads, Recent Searches & Alerts." Both sides both post and search.
- "Thousands of loads available daily from trusted brokers and shippers."
- Rate data as a product: "Our lane pricing tool uses millions of load records to give you reliable spot market rates for thousands of lanes."
- Feature list (vendor's own enumeration): Load and Truck Searching; Load and truck posting; **Credit Scores; Full Credit Reports; Days to Pay; Broker Authority, Bond, and Insurance Info**; Deadhead miles and Trip miles; Turn-by-turn truck-specific routing; Email alerts; Custom Columns and Categories; Alert Scheduling; **Private Loads**; Improved Load Filtering; Private Load Information; **Store and Send Documents**; Text Alerts; Notes.
- Driver app: "search more than 300K loads daily from reputable brokers & shippers on the Direct Freight network" (vendor claim, recorded not asserted).
- Ecosystem: TMS integration partners (McLeod, MercuryGate, Aljex, Trimble, FMS), **PostOnce.Net** (cross-posting to multiple boards), Quick Pay via Riviera Finance (factoring partner), links to FMCSA authority registration and the FMCSA carrier database.
- No in-platform booking is advertised — the classic model ends at contact/documents; the commitment happens between carrier and broker off-venue (rate confirmation per the domain's own vocabulary).

## Cross-product Comparison

| Dimension | Uber Freight | TruckSmarter | Direct Freight | Reading |
|---|---|---|---|---|
| Unit of market record | Load offered on the carrier app at an upfront price; shipper creates shipments | Load posting pulled from brokers/other boards | Load posting (+ reverse: truck posting) | **All three: the load posting is the unit** |
| Who posts | The operator (as broker) holds/originates the freight; shippers book via platform | Brokers (post via TMS/API/CSV/email/partner); aggregator pulls from other sources | Brokers and shippers post directly | **Posters are capacity holders (brokers/shippers); in the principal pole the operator itself is the poster** |
| Who searches | Carriers (app/web) | Carriers/owner-operators (app/web) | Carriers/owner-operators (+ brokers searching trucks) | **Searchers are capacity seekers (carriers)** |
| Pooled population | One network's freight ("one of the industry's largest networks") | Many brokers' loads pulled into one location ("100K+ daily available loads" claim) | Many brokers'/shippers' loads ("thousands daily"; "300K" app claim) | **All three aggregate many postings into one searchable pool** |
| Search machinery | Browse/book by equipment type; upfront rates shown | Filters (type/location/broker), sliders (price/RPM/weight/distance), saved lanes, saved loads | Search + map, custom columns/categories, filtering, alerts (email/text) | **Common: structured search/filter over lane, equipment, rate, distance; saved searches/alerts** |
| Response path | **Instant booking in-platform** at upfront price | **In-app bid and book** | Contact/documents; classic call-the-broker model (no advertised in-platform booking) | **All three have a response path; depth varies from contact to instant book — variant axis** |
| Who holds the transaction | The operator (licensed broker) — principal | Nobody — "not a broker or a dispatcher"; prices set by brokers | Nobody — venue only | **Neutral venue vs principal-operated marketplace — posture variant, both in-Type** |
| Price display | Upfront real-time linehaul + fuel rates | Rate, RPM on each posting; market/fuel data via AI Dispatch | Lane pricing tool from "millions of load records" | **Common: rate information on/around the posting; depth varies** |
| Trust machinery | Operator vets carriers (shipper FAQ topic); "most secure networks" claim | Carrier verification (insurance/authority docs or linked broker account) required to bid/book; broker credit checks | Credit scores, full credit reports, days-to-pay, broker authority/bond/insurance info | **Common: two-sided trust layer; carrier-side verification gates participation; poster-side credit/credential info** |
| Reverse direction (truck postings) | Not advertised (carrier signs up, gets matched freight) | Not advertised (carrier-side search only) | **Yes — Post Trucks / Find Trucks / Truck Map** | **Variant: classic boards are two-direction; marketplace poles are loads-direction** |
| Documents | In-platform (booking, tracking) | Store/send documents (feature inherited from classic set) | "Store and Send Documents" | **Common-optional: document exchange around the match** |
| Posting management | Shipper platform (create/quote/book) | Broker Dashboard; posting automation via TMS/API/CSV/partners | View My Loads; private loads | **Common: poster-side management surface** |
| Monetization | Transaction economics (operator is the broker) | Free board; fintech (factoring/banking) adjacent | Subscription (market norm per comparison table) | **Variant: subscription / free / transaction** |
| Surfaces | Mobile app + web portal (both sides) | Mobile app + web (both sides) | Web + driver app | **Common: mobile-first for carriers, web for posters** |

Commonality reading: all three realize the same spine — capacity holders publish load postings; the venue pools them into one searchable population; carriers search/filter/evaluate (lane, equipment, rate, weight, dates, deadhead); a response path returns interest to the poster (call, bid, or instant book); trust machinery gates participation on both sides. Around the spine: rate/market data, saved searches and alerts, posting automation and dashboards, document exchange, backhaul/deadhead tooling, mobile apps. What varies: who holds the transaction (nobody vs the operator-as-broker), booking depth (call vs bid vs instant), directionality (loads-only vs loads+trucks), monetization (subscription vs free vs transaction), and rate-data depth.

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal, jointly-held)

Three jointly-held structures:

1. **The load posting as the unit of market record** — a persistent, identified offer of one specific freight movement, published on the venue by an identified capacity holder (broker or shipper), carrying the freight frame: origin→destination lane, equipment type, dates/pickup window, weight, and a rate or rate expectation. (Remove → a chat/forum or a bare rate-data service; nothing to match on.)

2. **The pooled two-sided market** — postings from many independent capacity holders aggregated into one searchable population that capacity seekers (motor carriers / owner-operators) can filter and compare across posters; the venue is a shared market surface operated by a party separate from the participants, not any single participant's system of record. (Remove → one broker's private posting feed = a brokerage platform's coverage surface; or a single company's dispatch board.)

3. **The response path from seeker to poster** — a carrier acts on a posting (contact/call, bid, or book), returning interest to the posting party and producing a match between a specific load and a specific carrier; the venue mediates the introduction, and the commitment may be completed on or off the platform. (Remove → a read-only rate/analytics service or a directory; the market is gone.)

Jointly-held is load-bearing: 1 alone = a listing feed with no market; 2 alone = a rate-data/analytics service; 3 alone = cold-calling; 1+2 without 3 = read-only board (rate view only); 1+3 without 2 = a private tender portal for one broker's carriers; 2+3 without 1 = a chat room.

### L1 — Common Mature Structure

- **Search and discovery machinery** — structured filters over lane (origin/destination, radius), equipment type, pickup/dates, rate (absolute and per-mile), weight, deadhead distance; maps; saved searches/favorite lanes; alerts (email/text/push).
- **Rate and market data** — per-posting rates (and rate-per-mile); lane rate tools derived from load records; market/fuel context. Depth varies; presence is common.
- **Trust machinery, both directions** — carrier-side verification (operating authority, insurance documents) required before bidding/booking; poster-side credit and credential information (credit scores, days-to-pay, authority/bond/insurance).
- **Poster-side management** — posting dashboards, posting automation (TMS/API/CSV/email integrations, cross-posting services), private loads, team posting management.
- **Booking depth spectrum** — contact details + off-platform call (classic), in-app bidding, instant book-now at a displayed price.
- **Document exchange** — rate confirmation/BOL/POD storage and sending around the match (depth varies).
- **Mobile apps for carriers; web consoles for posters.**
- **Backhaul/deadhead tooling** — deadhead estimates, backhaul search, multi-leg booking (documented in two of three samples; common in the driver-value proposition).

### L2 — Variant / Optional Structure

- **Operator posture** — neutral venue (holds no economics; prices set by posters) vs principal-operated marketplace (operator is itself a licensed broker holding the transaction) vs aggregator (pulls postings from other boards/sources into one surface, with linked-account access for restricted posters).
- **Booking depth** — off-platform commitment (call the broker; rate confirmation exchanged off-venue) vs in-platform bid vs instant book.
- **Directionality** — loads-direction only vs two-direction boards (truck postings: carriers post available trucks; brokers search trucks/maps).
- **Mode and equipment scope** — van/reefer/flatbed/power-only/step deck/hot shot/container etc.; FTL-dominant; some LTL coverage (Uber Freight shipper side).
- **Access/monetization model** — paid subscription tiers (market norm for the classic incumbents), free (fintech-funded), transaction economics (principal marketplaces).
- **Embedded finance** — factoring, quick pay, fuel programs, banking (adjacent-product monetization).
- **Regional regime** — the researched sample is North American; European freight exchanges exist (TimoCom unreachable — recorded as uncertainty); the definition is written regime-neutral (authority/insurance credentials, no specific regulator named).
- **AI layers** — AI dispatch/matching assistants (chat-based load finding, broker calling, monitoring) at the era's edge.

### L3 — Vendor-specific (research notes only)

- TruckSmarter: AI Dispatch assistant (conversational load finding, "call brokers without waiting on hold," background monitoring); free model funded by factoring/banking; aggregator posture with linked load-board accounts; competitor comparison table (DAT $49–149/mo, 700K+ loads/day, paid-only rate insights; 123LoadBoard $35+/mo; Truckstop $45+/mo — competitor-claimed, unverified); "120K+ new carriers a day" and "100K+ daily loads" marketing claims; Spot/Armstrong case studies; posting partnerships (Parade, Newtrul, LoadBoard Network).
- Uber Freight: "licensed freight broker and not a motor carrier" disclaimer; 90-day rate lock; FTL priority-for-flexibility pricing; NetSuite ERP integration; LTL insurance via third-party partner; Carrier of the Year awards; power-only tours/dedicated fleets; the company's wider product lines (managed transportation, enterprise TMS) — the marketplace is one surface of a multi-product company.
- Direct Freight: lane pricing tool "uses millions of load records"; full credit reports/days-to-pay; broker authority/bond/insurance info; private loads; truck-specific turn-by-turn routing; PostOnce cross-posting; Quick Pay via Riviera Finance; TruckerSearch (driver-finding sister service); "300K loads daily" app claim.
- DAT / Truckstop / 123Loadboard: unreachable directly; named in brokerage-platform Tier-1 integration lists (Tai TMS, Alvys) as the canonical boards brokers integrate; market-dominant status per competitor comparisons (Tier-3). No mechanism claims made about them in this research.

## Rejected Findings

- **"Rate/market data is definitional"** — REJECTED as L0. Rate data is common (all three samples carry some) but the historical cork-board/phone-desk pole matched loads without any rate-data product; a board without rate tools is still a board. L1.
- **"Truck postings (reverse direction) are definitional"** — REJECTED. Classic boards are two-direction (Direct Freight), but both marketplace poles are loads-direction only and remain squarely in-Type. L2 variant.
- **"Instant booking is definitional"** — REJECTED. The classic board's response path ends at contact; the commitment happens off-venue. Booking depth is the Type's main variant axis, not its definition. L2.
- **"Carrier verification is definitional"** — REJECTED as L0. Universal in the modern sample and trust-critical, but the physical/phone-board era operated on references and phone trust; the venue-as-market exists without software verification modules. L1 (strongly documented).
- **"The venue must be neutral (hold no economics)"** — REJECTED as a definitional requirement. Uber Freight is a licensed broker operating a marketplace; the venue leg (postings + pool + response) is intact. Neutrality is a posture variant; the principal-operated pole straddles toward brokerage and is documented as such.
- **"Aggregation from other boards is definitional"** — REJECTED. TruckSmarter-specific posture (aggregator); classic boards and the principal marketplace originate their own postings. L2/L3.
- **"AI dispatch/matching is definitional"** — REJECTED. Era-typical edge layer; one sample. L2/L3.

## Boundary Findings

1. **vs Freight Brokerage Platform (§18, processed)** — RATIFIED from this side. The venue vs the system of record: the load board is the shared market where many brokers/shippers post and many carriers search; the brokerage platform is one intermediary's business system (load as business record, two-sided price/margin, carrier network as procured supply). The brokerage pass's structural test — "matching with no held economics = load-board territory" — is confirmed: the neutral venue holds no transaction economics; prices and conditions are set by the posters (TruckSmarter states this verbatim). Board integration is standard capability in brokerage platforms (3/3 sampled there); venue membership is not part of the brokerage Type. Internal coverage/dispatch boards inside brokerage platforms are surfaces, not the marketplace. The principal-operated marketplace pole (Uber Freight) straddles: its marketplace surface is this Type's venue leg; its held economics are the brokerage legs. Structural test: strip the pooled multi-poster market → a brokerage's private coverage feed; give the venue its own two-sided books on each load → a brokerage.
2. **vs Transportation Management System / TMS (§10, processed)** — the TMS is one company's operational system for executing moves; the load board is the market for finding/covering capacity. TMSs integrate with boards (posting/sourcing — Tier-1 evidence from the brokerage and TMS passes); the board is not the system of record for the haul. Product families straddle (Uber Freight sells both a marketplace and a TMS).
3. **vs Trucking Management System (§18, unprocessed)** — the carrier's own operations system (whose trucks/whose authority) vs the market where the carrier finds loads. A carrier uses both; the board holds no dispatch/fuel/maintenance/driver-settlement machinery. Flag for joint review when trucking-management-system is processed.
4. **vs Job Board (§09, processed)** — same venue shape (many independent posters, one separate operator, posting as unit, seeker-side discovery, response path back to the poster), different domain: the unit is a freight movement (lane/equipment/weight/rate/pickup window) vs a job opening; participants are companies trading capacity vs employers hiring people; the response is a bid/booking on commercial terms vs a job application; freight boards commonly carry market-rate data, credit information, and equipment/authority verification that job boards do not. Domain structuring keeps them separate Types (consistent with the service-marketplace umbrella precedent).
5. **vs Classifieds Platform / Listing Marketplace (§05.03)** — generic listing venue vs freight-domain-structured marketplace: the load posting's structured freight semantics (equipment taxonomy, lane, weight, pickup window, rate/RPM), the two-sided trust machinery (authority/insurance verification, broker credit), and the booking/bid response path are the domain structuring. Consistent with the domain-structured-sibling precedent.
6. **vs Dispatch Management (§18, processed)** — dispatch is the assignment act inside one company's live operation; the board is the open market before/around dispatch. A brokerage's internal coverage board is a dispatch-like surface, not the marketplace.
7. **vs Shipment Visibility Platform (§18)** — matching moves that don't exist yet vs tracking moves in flight. The board's job ends at the match; visibility begins after commitment.
8. **vs Freight Forwarding System (§18, unprocessed)** — international consignment/document/charge machinery vs the domestic spot-market venue. Light touch; flag noted for that pass.

## Uncertainties

- **Market-dominant incumbents unverified directly** (DAT, Truckstop, 123Loadboard all blocked): their mechanisms are documented only via brokerage-platform integration lists (Tier-1, indirect) and competitor comparisons (Tier-3). No mechanism claims about them appear in the final document; they are named only as representative market products with the sourcing limitation disclosed.
- **European freight exchanges** (TimoCom et al.) unreachable: the regional variant is hypothesized from market structure, not observed. The L0 is written regime-neutral as a hedge.
- **Booking-depth boundary inside the principal pole**: how much of Uber Freight's carrier experience is marketplace-style browsing vs allocated/tendered contract freight could not be fully separated from public pages (spot vs contract freight are both advertised). The final document treats booking depth as a spectrum without asserting product internals.
- **LTL depth on boards**: LTL appears on the shipper side of the principal pole; classic boards are truckload-centric. Mode breadth recorded as variant, not asserted as common.
- **Truck-posting prevalence**: directly evidenced in one sample (Direct Freight); market knowledge suggests it is widespread in classic boards, but per the single-source rule it is held as a variant with one direct observation.

## Historical / Market-Sample Check (§24-style)

The sampled vendor's own historical anchor: "Originally a cork board and push pins, today's most common load boards are online marketplaces…" (TruckSmarter FAQ). The conceptual analog pole: a physical truck-stop board or a phone-based matching desk — brokers phone in their loads (postings, attributed to identified brokers), the board/desk pools many brokers' offers in one shared place (the market), drivers read the board or phone the desk and claim a load by phone (the response path); the match is completed off-venue with a rate confirmation. All three L0 legs are satisfied at analog level with zero software: no search filters, no rate data product, no verification module, no instant booking, no subscription. The digital check therefore passes: the definition names none of the modern machinery.

Regional check: the L0 names no regulator, no currency, no country; the credentials leg is written as "operating authority/insurance" generically. European exchange-style venues are expected to fit, though unverified (recorded above).

## Final Synthesis

A Load Board / Freight Marketplace is the shared market venue of truckload freight. Its defining core is three jointly-held structures: the load posting as the unit of market record (an identified offer of one freight movement — lane, equipment, dates, weight, rate — published by a broker or shipper); the pooled two-sided market (many independent posters' offerings aggregated into one searchable population for carriers, on a venue operated by a party separate from the participants and distinct from any participant's system of record); and the response path (a carrier's call, bid, or booking returning interest to the poster and producing the match). Around this core, mature products add structured search and alerts, rate and market data, two-sided trust machinery (carrier verification, poster credit information), posting automation and dashboards, document exchange, backhaul tooling, and mobile-first carrier surfaces. The Type's main variant axes: operator posture (neutral venue vs principal-operated marketplace vs aggregator), booking depth (off-platform call vs in-platform bid vs instant book), directionality (loads-only vs loads+trucks), and monetization (subscription vs free vs transaction). The venue is separated from the brokerage platform by venue-vs-system-of-record (ratified jointly with that pass), from the TMS by market-vs-execution, from the trucking TMS by whose operation, from the job board by domain, from classifieds by domain structuring, from dispatch by market-vs-assignment, and from visibility by matching-vs-tracking.
