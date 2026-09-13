# Research Notes — Rail Booking & Ticketing

## Research Goal

Understand what Rail Booking & Ticketing actually is as an Application Type: what objects exist inside it (train services, fares, seats/reservations, tickets, bookings, passengers), how the search→book→pay→issue→travel loop works, how fare conditions drive changes/refunds, how the ticket is realized and checked, who sells (operator self-run vs third-party reseller vs industry layer), and where the boundary lies against neighboring Types (Airline Reservation / Passenger Service System, Public Transit Passenger App, Event Ticketing, OTA, MaaS, Rail Operations Platform).

Directory context: leaf "Rail Booking & Ticketing", section 18 (Transportation, Mobility & Logistics). Research date: 2026-09-09.

## Initial Boundary (working hypothesis before research)

- Hypothesized core: a system that sells rail travel — the traveler searches timetabled train services between stations, selects a fare, pays, receives a ticket (paper or digital), travels, and can change/refund under fare rules. Behind the passenger surface sits the operator's inventory and fare machinery.
- Suspected confusions:
  - Airline Reservation / Passenger Service System (§18 sibling): same deep booking structure, different transport domain.
  - Public Transit Passenger App (§18 sibling): urban fare products (passes, zones, tap-to-pay) vs intercity rail ticketing; commuter rail blurs the seam.
  - Event Ticketing Platform (§26): both sell seats, but one sells admission to a venue event, the other travel on scheduled transport services.
  - Online Travel Agency (§26): multi-vertical travel commerce vs the rail ticketing system; resellers (e.g. Trainline) sit between.
  - Rail Operations Platform (§18 sibling): the operator's internal operations (dispatch, rolling stock, crew) vs the passenger commerce side.
  - Mobility-as-a-Service Platform (§18 sibling): multi-provider integration vs single-network/deep-carrier ticketing.

## Research Questions

1. What is the central object — the train service, the booking/reservation, or the ticket?
2. How does the purchase flow work concretely (search → select → fare → pay → issue)?
3. How is seat commitment handled? Is seat reservation definitional or a common structure? (DB/UK optional; JR reserved/non-reserved fare classes)
4. What fare structures exist and how do fare conditions gate changes/refunds? (advance train-bound vs flexible; JR's two-layer basic-fare + surcharge model; UK's Advance/Off-Peak/Anytime; DB's saver/flexible)
5. What is the ticket artifact (paper, e-ticket/QR, smartcard, ID card) and how is it checked?
6. What happens post-purchase: changes, refunds, missed trains, disruptions/delay compensation?
7. Who sells: operator self-run, industry-neutral layer, third-party reseller? How do carrier rules propagate through resellers?
8. What does the operator side look like (inventory, channels, published fares, release windows)?
9. Boundary: what exactly separates this from airline PSS, from transit passenger apps, from event ticketing?

## Representative Products

| Product | Posture | Philosophy pole |
|---|---|---|
| JR Central / smartEX (Tokaido-Sanyo-Kyushu Shinkansen online reservation service, run by JR Central/JR West/JR Kyushu consortium) | operator-run online reservation service (East Asia) | reserved-seat culture; two-layer fare (basic fare + surcharge); unlimited changes up to departure |
| Deutsche Bahn (DB Fernverkehr, bahn.com) | operator self-run (Europe) | flexible-fare philosophy; ticket decoupled from seat reservation and normally from a specific train |
| National Rail (UK rail industry portal) | industry body — does NOT retail | the industry-standard fare taxonomy and the "impartial routing to retailers" structure |
| Trainline | third-party rail/coach ticket reseller (UK/Europe, 45 countries) | reseller/aggregator model; carrier rules + reseller fee layers |
| China Railway 12306 (12306.cn, China Academy of Railway Sciences) | operator-run national monopoly system (China) | real-name ticketing, registered passengers, waitlist purchase, no authorized third-party resellers |

Selection rationale: two operator-run systems with different fare philosophies and reservation cultures (JR Central reserved-seat-centric; DB flexible), one industry-standard layer that documents the fare taxonomy neutrally (National Rail), one pure reseller showing the retail intermediary structure (Trainline), one operator-monopoly counterpoint showing the retail structure is a variant not a constant (12306). Amtrak and VIA Rail were selected for the North American operator pole but their official surfaces were unreachable (see Sources); the North American market is held as market anchor only.

## Sources

Fetched 2026-09-09 (all official surfaces):

- JR Central / smartEX — https://smart-ex.jp/en/ (service root), https://smart-ex.jp/en/beginner/ (key points of the service), https://smart-ex.jp/en/reservation/reserve_smart/sp/ (step-by-step reservation guide with screen walkthrough), https://smart-ex.jp/en/product/hayatoku7/ (advance-purchase fare product rules), https://smart-ex.jp/en/sitemap/ (site structure)
- JR Central general ticketing — https://global.jr-central.co.jp/en/tickets/ (how to buy and use tickets), .../tickets/buy/ (purchase places + procedure), .../tickets/type/ (ticket rules), .../tickets/type/types.html (types of tickets), .../tickets/type/combinations.html (combinations of tickets), .../tickets/change/ (change & refund rules incl. fee table)
- Deutsche Bahn — https://www.bahn.com/en/help (help & contact incl. cancel/exchange FAQ, compensation FAQ, connection-change FAQ), https://www.bahn.com/en/offers (fare offers: super saver/saver/flexible, BahnCard, seat reservation, group/regional/Europe/pass products)
- National Rail — https://www.nationalrail.co.uk/ (root), /tickets-railcards-and-offers/ticket-types/ (fare taxonomy), /tickets-railcards-and-offers/ticket-types/advance-tickets/, .../anytime-tickets/, .../off-peak-and-super-off-peak-tickets/ (per-type rules), /tickets-railcards-and-offers/buying-a-ticket/ (channels, routeing/validity, retail structure)
- Trainline — https://www.thetrainline.com/ (root: reseller self-description, FAQ), https://www.thetrainline.com/en/help (help center structure), https://support.thetrainline.com/en/support/solutions/78000000017 (refunds & exchanges category), /hc/en-gb/articles/5118073689247-Refunding-a-UK-Train-Ticket (refund workflow + rules), /hc/en-gb/articles/5124895829407-Tiered-refund-and-exchange-fees (fee tables, carrier variance), /en/support/solutions/78000000020 (ticket collection/fulfillment category)
- China Railway 12306 — https://www.12306.cn/index/ (homepage: navigation, account order types, ticket menu, information queries, real-name notices, official-app exclusivity notice)

Unreachable (recorded per evidence rules):

- Amtrak — https://www.amtrak.com/refund-exchange-policy (403), https://www.amtrak.com/train-fares (403). Abandoned after 2 failures. No Amtrak-specific claims are made.
- VIA Rail — https://www.viarail.ca/en (transport error), https://www.viarail.ca/ (transport error). Abandoned after 2 failures. No VIA-specific claims are made.
- JR East / Ekinet — https://www.eki-net.com/pc/english/common/en/guide/ (403), https://www.jreast.co.jp/e/ (403). Abandoned after 2 failures; the Japan reserved-seat pole is carried by JR Central instead.
- Deutsche Bahn detail pages for seat reservations and fare conditions — guessed paths 404 (only the /en/help and /en/offers pages were reachable).

Evidence layers used below: **A** = directly observed on one product's official source; **B** = cross-product commonality; **C** = canonical inference from comparison + boundary reasoning.

## Product Observations

### JR Central / smartEX (Shinkansen online reservation service) — evidence layer A

From the official service site (beginner/key-points, reservation guide, fare product page) and JR Central's general ticketing pages:

- Self-definition: "Tokaido Sanyo Kyushu Shinkansen Online Reservation Service" — "You can purchase tickets and make seat reservations in your own country before arriving in Japan." Membership registration required (credit card required for registration; card holder 18+; 3D Secure). No annual membership fee.
- **JR fare structure is two-layer**: "There are essentially two types of tickets in Japan; tickets that are necessary for riding all types of trains... called 'Basic Fare Ticket' and... 'Limited Express Ticket' and 'Green Car Ticket'." When riding local/rapid trains with no seat reservation "only a basic fare ticket is required." Shinkansen/limited express require a surcharge ticket "valid for the specific train you are going to ride." A combination table maps train class (Shinkansen / limited express / rapid-local) × car class (ordinary / Green first class) × reserved / non-reserved to the surcharge ticket required.
- **Reserved vs non-reserved as fare classes**: on the search results, seat availability is shown per train (○ available / ▲ partly sold / × not available). "When booking a non-reserved seat, choose a random train and select a non-reserved fare... Any non-reserved seat of reserved date and route can be used when non-reserved seat fare is purchased." Reserved seats offer a seat map, window/aisle preference, wheelchair seats, "seat with oversized baggage area", "S Work seat", family-car options.
- **Reservation flow (documented step-by-step)**: 1. Login (membership ID + password) → 2. Menu → "Search Train" → 3. specify boarding date/time, departure/arrival stations, number of persons (one-way / round trip; direct-trains filter) → 4. select train and facility (availability symbols; trains listed "in order of departure time") → 5. select fare and facility, select seat location (seat map; maximum two rows selectable; "Seats can be separated" fallback) → 6. confirm and "OK Purchase" — "Your purchase (payment) will be completed once you tap 'OK Purchase'" (charged to the registered credit card at purchase) → 7. complete: confirmation email + "My Trips"; the boarding method is shown per reservation.
- **Double-booking detection**: selecting a fare duplicating an existing reservation (same date/time/direction/section) triggers an explicit notification screen before proceeding.
- **Gate geography rule**: "You cannot exit the ticket gate at a station other than your arrival station. Tickets for the remaining section will be invalid and you will need to purchase another ticket to board the train again."
- **Boarding = three ticket realizations**: "Boarding with QR-Ticket" (printed or added to Apple Wallet), "Pick up tickets at the stations" (vending machines etc., pickup code), or a **registered IC card** — "by simply touching your card to the ticket gate... payment will automatically be deducted" for the IC balance generally, BUT "the Shinkansen fare in this service is paid from your registered credit card when you make a reservation (it is not deducted from the balance of your IC card)" — the IC card acts as the gate credential while the fare was already purchased.
- **Changes**: "Change your reservation as often as you like!... changes can be made, as many times as you like, right up to the time your train departs."
- **Advance-purchase product (EX Hayatoku 7)**: sold "from 1 month before (10:00) to 7 days before (23:30)"; limited seats per train; exclusion days (Golden Week, Obon, New Year). "This product combines a basic fare ticket and a limited express ticket." Changes: any number of times within 3 months of initial purchase to purchasable products (difference payable); reducing passengers incurs a refund fee (320 yen per person). Refund: self-service before entering the gate / before receiving tickets, fee 320 yen before departure; after departure special handling. "If the Shinkansen is more than 2 hours behind the scheduled arrival time, pay back the 'specified amount' for each use section" (delay refund). "You cannot get off halfway" (no break of journey on this product); valid only for the booked train.
- **JR change/refund rules (general ticketing pages)**: a valid unused ticket "can be changed one time to a ticket of the same type for free"; changes to reserved-seat tickets "must be made before the train's scheduled departure time... a ticket becomes invalid once the train departs." Missed reserved train: reserved tickets "cannot be used and refunds cannot be made after the scheduled departure time" (except riding non-reserved same day). Refund fee table by ticket type and timing (basic fare within validity: 220 yen; reserved-seat tickets: 340 yen until 2 days before, then "30%, but no lower than 340 yen" from 1 day before until departure time). Refunds for ticket portions when combined tickets are partially refunded.
- **Sales channels**: JR ticket offices ("Midori no Madoguchi"), ticket vending machines ("Some of the machines allow you to buy limited express tickets and reserve seats"), JR travel agencies (JR TOKAI TOURS), and this online service. Purchase procedure at counters: departure/destination, date/time, train type, number of persons, seat type.

### Deutsche Bahn (DB Fernverkehr) — evidence layer A

From bahn.com (help & contact FAQ, tickets & offers):

- **Fare ladder with explicit conditions** (domestic and Europe variants): "Super saver fare — No cancellations — Valid only on the train selected"; "Saver fare — EUR 10 cancellation fee — Valid only on the train selected"; "Flexible fare — Not limited to specific trains — Cancellation possible". Age variants (young <27, seniors >65); Group saver fares (from 6 persons, seat reservation included); Regional offers (local transport IRE/RE/RB/S-Bahn, "Any number of journeys on one day"); German Rail Pass (unlimited travel, selectable travel days); Interrail/Eurail Pass (33+ countries); overnight/night trains; BahnCard discount card ("Save 25/50/100% on every trip", valid 3–12 months).
- **Seat reservation is decoupled from the ticket**: "Seat reservation — Book your favourite spot... — Can be booked separately from the ticket — Seat included in first class." This is the operator explicitly selling ticket and reservation as separate products.
- **Ticket normally not tied to a booked connection**: from the help FAQ — "If your booked connection is no longer available or changed, you can use alternative connections without changing your booking. Your ticket is no longer linked to the booked connection. This does not apply for connections with mandatory reservations." (i.e., train-binding is a property of the fare, not of the system).
- **Cancellation vs exchange**: "You can cancel your ticket depending on the applying conditions of your booked ticket. An exchange is not possible." (DB's policy: cancel-and-rebook, not in-place exchange.)
- **Disruption**: "If your train was significantly delayed or cancelled, you can apply for compensation" (passenger rights). Deutschland-Ticket (national local-transport subscription) referenced in FAQ.
- Site structure: Private trips / Business trips; main nav "Tickets & offers / Info & services / Train fleet / My trips"; "My trips" is the booking-management area; payment options footer; conditions of carriage linked.

### National Rail (UK rail industry portal) — evidence layer A

From nationalrail.co.uk (ticket types, per-type pages, buying a ticket):

- **The industry fare taxonomy** ("The name of the ticket usually describes when you can buy or use it"): Advance / Off-Peak (and Super Off-Peak) / Anytime / Season and Flexi Season / Pay As You Go / Oyster and Travelcards / Rover tickets / Ranger tickets.
- **Advance**: "must be bought in advance and are only valid on the date and train specified"; single journeys, combinable; "sold in limited numbers, subject to availability and on a first come, first served basis"; "usually... up to 12 weeks ahead of travel... sometimes up to 10 minutes before departure"; changeable "right up to the time your journey is due to begin" with a fee ("may be charged £10") plus fare difference; "Advance tickets are non-refundable, unless your train is delayed or cancelled and you choose not to travel."
- **Anytime**: "travel on any train on the route shown... no restrictions on what time you can travel"; Anytime Singles valid "within 2 days of the date shown", most Anytime Returns "5 days... outward" / "1 calendar month... return"; refundable "up until 23:59 the day before it becomes valid" with an admin fee "of no more than £5"; change date until 23:59 day before validity; reservation/class/route still changeable after validity begins.
- **Off-Peak / Super Off-Peak**: "available for travelling at less busy times... may require you to travel at specified times, or on specified days or routes"; Off-Peak hours "begin at 09:30 from Monday to Friday in cities and large towns, and at 09:00 everywhere else"; tickets carry a **Restriction Code**; traveling in peak "you will have to pay the difference... you may also be liable for a Penalty Fare"; returns valid 1 month.
- **Seat reservations are optional in the UK model**: "Reservations are not compulsory with Anytime tickets... normally free of charge if made at the same time you buy your ticket. Reservations are recommended on busy services and for longer journeys." For Advance: "Not all services offer seat reservations. Generally, the longer the journey the more likely you are to be able to book a seat... Even if you don't reserve a seat, all Advance tickets must still be used on the date and service specified." Reservation channels: "online, at stations, over the phone, or at Rail Appointed Travel Agents."
- **Season / Rover / Ranger**: "unlimited travel between 2 stations... weekly, monthly or yearly" (Season); "unlimited travel in a specified area... Rangers... valid for 1 day, Rovers... 3, 7 or 8 days" — unlimited-travel products as a fare class.
- **Pay As You Go / contactless / Oyster / smartcards**: "use a contactless card or device to pay as you go... touch your card or device on a card reader at the start of your journey and touch out... at the end"; smartcards store "tickets and pay as you go credit". (Commuter/urban blend living inside the national rail system.)
- **The retail structure**: "National Rail does not retail train tickets, so when you are ready to buy the ticket you have selected we impartially offer all of the train companies that can complete the transaction." Purchase channels: "the National Rail website or app, or visit a station ticket office or ticket machine." Refunds: "return the ticket to the retailer you bought it from."
- **Routeing/validity machinery**: "Your ticket may show a route or train company that you must use... Permitted routes cover all reasonable routes"; the Rail Delivery Group's Routeing Guide; "Ticket Validity Finder" for restriction codes; journey planners display "the cheapest price for both a return and 2 singles"; some fares not shown (sleeper supplements, retailer-exclusive fares).

### Trainline (third-party reseller) — evidence layer A

From thetrainline.com root, help center, and support articles:

- **Reseller self-description**: "Compare prices from over 270 companies and book the right solution for you"; "displaying routes, prices and timetables of more than 270 train and bus companies in 45 countries"; sells tickets FOR named carriers ("Eurostar tickets, Trenitalia tickets, Deutsche Bahn tickets, SNCF tickets, Renfe tickets, ÖBB tickets..."); "Born in 1997... mission to make booking of train and bus tickets easier." Also distributes passes (Eurail as "official distributors"; Japan rail passes).
- **Carrier-rule propagation**: "Can I cancel my booking? It depends on the company the booking was made with and on the type of ticket purchased. If sale conditions allow it, you can easily cancel your booking online." "You can request a refund after canceling your booking, if allowed by the ticket terms and conditions. You can also receive a refund if your train is canceled... by the train company." "For European train bookings, exchange fees vary by carrier. Fees are displayed during the booking process."
- **Booking window knowledge**: "When is the best time to book? Three months in advance! It's when most carriers release their tickets" (Eurostar six months).
- **Search form**: From/To, one-way/return, passenger counts with age bands (e.g. "1 adult (26-59)"), railcards, voucher codes; multi-passenger; currency selection ("Book your tickets in US Dollars"), Apple Pay/PayPal.
- **Refund workflow (documented article)**: "Open your confirmation email and click 'Manage booking'"; or account → My Bookings (web) / My Tickets (app) → "Refund my tickets". Rules by ticket type: Flexible (Anytime/Off-Peak/Super Off-Peak) refundable online with "a small fee", deadline "before your ticket becomes valid for travel"; **"Activated mobile tickets can't be refunded"**; Advance singles "Non-refundable, but you can change the date or time of travel (same stations)"; SplitSave (split-ticketing) — flexible parts refundable, advance parts changeable only. Status lifecycle: "Refunded / Approved... Processing / Action Required: We may need your paper tickets back... Rejected: The ticket was used, scanned, or already activated." "Refunds always go back to the original payment card." Uncollected tickets: "If you haven't collected your tickets by their expiry date, we'll automatically refund them (subject to the refund fee...)."
- **Reseller-side fee schedule**: tiered refund/exchange fees by ticket value (e.g. refund fee £0–£5; exchange fee £0–£10, scaled to ticket value) — a fee layer ON TOP of carrier rules.
- **Ticket fulfillment modes**: "How will I receive my tickets?", "Which stations can I collect my tickets from in the UK?", "How do I collect tickets from a self-service ticket machine?", "Where can I find my ticket collection reference?", "When will my tickets be delivered?" (Next Day Delivery), "How do I collect tickets paid for with PayPal?" — i.e., e-ticket in app, station machine collection with a reference code, or physical delivery.
- **Disruption split**: cancelled train → "use your ticket on the next available train with the same operator... If you decide not to travel, you're entitled to a full refund" (via Trainline); delayed train → "you can claim Delay Compensation directly from the train company" (Delay Repay) — the reseller handles the sale-side refund; delay compensation flows through the carrier's own machinery.
- **App capabilities**: "Access your digital ticket", "Get real-time trip notification", "Manage booking from your phone", QR code display.

### China Railway 12306 — evidence layer A (homepage navigation/menu level, Chinese site)

From 12306.cn homepage:

- Operator-built and operated: copyright "中国铁道科学研究院集团有限公司" (China Academy of Railway Sciences Group); official-app notice states "目前铁路未授权其他网站或APP开展类似服务内容" — the railway has NOT authorized other websites or apps to run similar services — the operator-exclusive retail posture.
- **Real-name ticketing system**: 实名制车票 (real-name tickets) in passenger notice; 身份核验 (identity verification) in the travel guide; "使用居民身份证直接检票乘车" (use resident ID card directly at the gates) — the national ID card is a ticket-checking credential.
- **Account structure**: 我的12306 holds 火车票订单 (train ticket orders), 候补订单 (waitlist orders — a queue/waitlist purchase mechanism), 计次•定期票订单 (multi-ride & periodic ticket orders), 电子发票 (electronic invoices), 待补票订单 (pending ticket-supplement orders), 本人车票 (my tickets), 乘车人 (registered passenger list — the traveler roster bound to identities), 地址管理, 会员/积分账户 (loyalty points account and redemption).
- **Ticket menu**: 购买 (purchase: 单程 one-way / 往返 return / 中转换乘 transfer-interchange / 计次•定期票 multi-ride & periodic), 变更 (change: 退票 refund / 改签 rebooking / 变更到站 change destination), 中铁银通卡 (China Railway UnionPay IC card), 国际列车 (international trains).
- **Information queries**: 正晚点 (punctuality/delay), 时刻表 (timetable), 公布票价 (published fares), 检票口 (boarding gate), **起售时间 (ticket sale start times)**, 天气, 代售点 (ticket agencies), 列车状态 (train status).
- Group sales (团购服务: migrant workers, student groups), station/train services (special-needs passengers, lost items, catering ordering onboard 餐饮•特产, insurance, ski equipment transport), rules corpus (铁路旅客运输规程 railway passenger transport regulations, cross-border Guangzhou-Shenzhen-Hong Kong rules, prohibited items).
- Search form mirrors the family pattern: departure/destination, date, one-way/round-trip/transfer, passenger-type filters (student, high-speed only).

## Cross-product Comparison

| Structure | JR Central/smartEX | Deutsche Bahn | National Rail (industry) | Trainline (reseller) | 12306 | Layer |
|---|---|---|---|---|---|---|
| Timetabled service inventory as the bookable object | A: train search by date/time/stations, per-train availability, "in order of departure time" | A: connection-based offers; flexible fares not limited to specific trains | A: journey planner showing ticket options per service | A: "routes, prices and timetables of more than 270 companies" | A: timetable, train status, sale-start times | B |
| Purchase transaction → issued ticket | A: login→search→select→pay (credit card at purchase)→email+My Trips | A: booking in "My trips"; cancel via account | A: routed impartially to retailers; counter/machine/online | A: online booking, confirmation email + Manage booking | A: 购买 menu; orders in account | B |
| Ticket = checkable travel entitlement with fare conditions | A: QR / paper pickup / IC card credential; gate rules | A: conditions per fare ("applying conditions of your booked ticket") | A: Restriction Codes, permitted routes, penalty fares | A: activated-mobile-ticket non-refundable; ticket scanned = rejected | A: real-name + ID-card gate check | B |
| Seat/berth reservation | A: core of the service; seat map, availability ○▲×, reserved vs non-reserved fare classes | A: "booked separately from the ticket"; included in first class & group fares | A: optional, "not compulsory", normally free at purchase; not on all services | (carrier-dependent; seat-together note at booking) | A: seat selection within booking (menu-level observation) | B |
| Reserved-vs-flexible fare condition spectrum | A: Hayatoku advance fares train-bound; ordinary reserved changes free | A: super saver/saver train-bound vs flexible any-train | A: Advance train-bound vs Off-Peak time-bound vs Anytime open | A: rules depend on carrier + ticket type (Flex vs Advance vs SplitSave) | A: multi-ride/periodic products; rebooking 改签 machinery | B |
| Changes/refunds under fare rules with fees & deadlines | A: free same-type change; refund fee table 220/340 yen + 30% tier; invalid after departure | A: cancellation by fare (none / EUR 10 / possible); no exchange | A: Advance change £10+diff; Anytime/Off-Peak refund ≤£5 admin fee, deadline 23:59 day before | A: online refund workflow, status lifecycle, tiered fee schedule | A: 退票/改签/变更到站 as first-class menu actions | B |
| Disruption handling (delay/cancellation) | A: ≥2h delay → partial payback | A: compensation for significant delay/cancellation | A: refundable if delayed/cancelled and not traveling; Delay Repay page via retailers | A: cancelled → full refund via reseller; delay compensation claimed from train company | A: 正晚点 query; procedures in case of delay/suspension (FAQ category) | B |
| Traveler identity & discount layers | A: membership (credit-card-verified); adults/children; Hayatoku family fare | A: BahnCard discount card; young/senior fares | A: Railcards (16-25, 26-30, Senior, Two Together, etc.), child 50% | A: railcards in search; age-band passengers | A: real-name registered passengers (乘车人), student fares, loyalty points | B |
| Multi-channel sales on one inventory | A: counters, machines, agencies, online | A: online/app, counters, machines | A: train companies + third-party retailers, offices, machines | A: website + app only (retail layer) | A: online + 银通卡 IC + ticket agencies (代售点) + station windows | B |
| Unlimited-travel / pass products | A: (JR passes sold via separate services — not observed on smartEX) | A: German Rail Pass, Interrail/Eurail, Deutschland-Ticket | A: Season, Flexi Season, Rover, Ranger, travelcards | A: Eurail passes, Japan passes distribution, season tickets pages | A: 计次•定期票 multi-ride/periodic | B |
| Operator-exclusive vs reseller retail structure | A: operator consortium runs the service (and counter/machine channels) | A: operator runs retail on own site | A: industry layer "does not retail... impartially offer all of the train companies" | A: independent reseller across 270+ carriers | A: "铁路未授权其他网站或APP开展类似服务" — no third-party resellers | — (variant axis) |
| Real-name identity binding | — (membership-based but tickets not observed as name-bound) | — | — (anonymous tickets; railcards as entitlements) | — | A: real-name ticketing + ID gates | — (variant axis) |
| Waitlist purchase | — | — | — | — | A: 候补订单 waitlist orders | — (product-specific) |
| Commuter PAYG/contactless inside the system | — | A: Deutschland-Ticket (regional transit subscription) | A: Pay As You Go contactless, Oyster, smartcards | — | A: 中铁银通卡 IC card | B (variant) |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures (evidence layer C, supported by B across all five products):

1. **The bookable rail service inventory** — a timetable-organized inventory of scheduled train services between stations, priced under the operator's fare system, with seat/berth capacity where reservation applies. The service (a named train on a date between stations — or, in flexible fares, the set of services a ticket's validity covers) is the thing sold. Remove → a timetable/publication site (information only) or a generic e-commerce checkout with nothing to ride.
2. **The purchase transaction that issues a ticket** — search/choose → price under fare rules → pay → the system issues a ticket. The sale, the payment, and the issuance are one atomic commerce loop, whoever runs it (operator or reseller). Remove → a fare calculator, a payment form, or a gate system without sales.
3. **The ticket as a checkable travel entitlement carrying fare conditions** — the issued record binds origin/destination, validity (date/time window), train-binding where the fare demands it, and passenger entitlement, in a form that can be checked at gates/onboard (paper, barcode/QR, smartcard, ID credential). The fare conditions are part of the object: they are what changes/refunds act on. Remove → a mere reservation (no enforceable entitlement) or a stored-value transit medium with no per-journey conditions (transit territory).

Jointly-held tests:

```text
1 alone                       → timetable/published-fare information site
2 without 1+3                 → checkout with nothing to ride (generic commerce)
3 without 1+2                 → fare card / gate medium without sales (transit territory)
1+2 without 3                 → reservation machinery that never issues an enforceable ticket
2+3 without 1                 → event-style ticketing (no scheduled service inventory)
1+3 without 2                 → gate/access system with no commerce loop
```

Anti-overfitting notes:
- **Seat reservation is NOT definitional.** DB sells it "separately from the ticket"; UK reservations are "not compulsory" and "not all services offer" them; JR sells non-reserved fare classes ("only a basic fare ticket is required" for local trains). The ticket's fare conditions may or may not include a seat commitment; every market has ticket-without-reservation as a first-class case.
- **Train-binding is NOT definitional.** DB's help states the ticket "is no longer linked to the booked connection" (except mandatory-reservation fares); UK Anytime/Off-Peak are train-agnostic. The invariant is that fare conditions govern what the ticket permits — train-binding is one possible condition.
- **Real-name identity is NOT definitional.** China binds tickets to verified identities; UK/Japan/Germany sell anonymously (membership optional). The invariant is the passenger entitlement, not identity verification.
- **The mobile app is NOT definitional.** Counter windows, machines, and paper tickets satisfy the core (JR documents all channels; the window era satisfies the historical check).

### L1 — Common Mature Structure

- **Seat/berth reservation machinery**: seat maps, per-train availability states, reserved/non-reserved as fare classes, preference selection (window/aisle, quiet/family/accessibility seats).
- **Self-service account + booking management**: "My Trips"/"My Bookings" holding purchases, receipts/invoices, boarding instructions.
- **Changes, exchanges and refunds under fare rules**: fee ladders scaled by fare flexibility and by time-to-departure; deadline states (e.g. refund until the day before validity; ticket invalid after the booked train departs); refund to original payment method; uncollected-ticket auto-refund (reseller case).
- **Disruption machinery**: delay thresholds triggering compensation/payback; cancelled-train refunds; entitlement to later trains; separate delay-compensation claims via the carrier (reseller split).
- **Multiple fulfillment/checking realizations of one ticket**: paper, e-ticket/barcode/QR in app, station-collection with reference code, postal delivery, smartcard/ID credentials at gates.
- **Passenger categories and discount layers**: child/adult/senior bands, railcards/discount cards, group fares, family fares, loyalty programs/points.
- **Multi-channel sales on one underlying inventory**: station ticket offices, vending machines, travel agencies, online web/app.
- **Unlimited-travel products**: season tickets, rover/ranger area passes, national/region passes (Interrail/German Rail Pass/multi-ride), as a fare class inside the same system.

### L2 — Variant / Optional Structure

- **Retail structure**: operator-exclusive retail (12306: "railway has not authorized other websites or apps"), operator self-run plus counters/machines (DB, JR), industry-neutral info layer routing to competing retailers (National Rail), independent third-party resellers across many carriers (Trainline). Resellers propagate carrier rules and add their own fee layers.
- **Real-name regime**: identity-verified tickets with registered passenger rosters and ID-as-credential (China) vs anonymous tickets with optional membership (UK/DE/JP).
- **Fare taxonomy shape**: JR's two-layer basic-fare + surcharge structure; UK's Advance/Off-Peak/Anytime time-of-day validity with Restriction Codes; DB's super saver/saver/flexible ladder; naming and condition granularity are regional.
- **Reservation culture**: reservation-centric high-speed lines (Shinkansen) vs reservation-optional networks (UK/DE regional).
- **Waitlist/queue purchase** (12306 候补), **commuter PAYG/contactless** blending into urban transit (UK contactless, Oyster, JR IC cards, 银通卡), **subscription products** (Deutschland-Ticket, BahnCard discount membership).
- **Geographic scope**: national systems, cross-border/international trains, multi-country passes.

### L3 — Vendor-specific (Research Notes only)

- JR Central/smartEX: 10-digit membership ID; fare paid to registered credit card while IC card is gate credential only; QR print or Apple Wallet; EX Hayatoku 1/3/7/21 booking-window naming; 320-yen Hayatoku refund fee; 220/340-yen JR refund fee table with 30% tier; "smartEX-round trip" service ended March 31, 2026; S Work seat; oversized-baggage seat area; 28-day validity of tourist IC cards; foreign-transaction-fee warning on repeated changes; the general-JR change/refund fee tables and the miss-the-train invalidity rules.
- DB: EUR 10 saver cancellation fee; "An exchange is not possible"; BahnCard 25/50/100; group fare from 6 persons; super saver young/senior age gates.
- National Rail: £10 Advance change fee, ≤£5 admin fee, 09:30/09:00 off-peak thresholds, 12-week/10-minute Advance booking windows, 2-day/5-day/1-month validity spans, Penalty Fares, Routeing Guide, Ticket Validity Finder, "impartial" retailer routing, £90 Oyster credit cap.
- Trainline: tiered refund (£0–£5) and exchange (£0–£10) fee schedules by ticket value; refund status lifecycle labels; 3–5 day refund processing; auto-confirm email "Manage booking" flow; SplitSave split-ticketing; Delay Repay routing; 270+ companies / 45 countries (marketing figures).
- 12306: 候补 waitlist orders, 待补票 pending-supplement orders, 计次•定期票 multi-ride/periodic products, 起售时间 sale-start-time queries, 银通卡, student/migrant-worker group sales, credit-blacklist disclosure (失信被执行人), onboard catering ordering.

## Vendor-specific Findings

See L3. None of these enter the canonical core. Notable anti-generalization flags: the JR fee table and the UK/Trainline fee numbers are jurisdiction/product-specific; DB's "no exchange" policy is a DB policy, not a Type rule (JR and UK systems DO exchange); real-name machinery is a Chinese-regime feature, not a Type requirement.

## Boundary Findings

1. **vs Airline Reservation / Passenger Service System (§18 sibling)** — the deep structure is the same family (inventory, booking, seat, fare rules, ticketing). The boundary is the transport domain's semantics: rail sells station-to-station travel on timetabled network services across (often) many operators, with fare products airlines structurally lack (season tickets, rover passes, flexible fares valid on any train, walk-up point-to-point fares, unlimited multi-ride products) and where the ticket is routinely decoupled from a specific seat (DB/UK) — airlines cannot sell a seatless flight. No check-in/baggage/immigration machinery on the rail side. Removal test: re-home the same commerce loop onto aircraft inventory with flight numbers, check-in and baggage → airline PSS; the rail-specific fare-product family (validity windows, permitted routes, season/rover passes) is the recognizable difference. (Layer C — airline PSS docs were not fetched this pass; strength held at conceptual.)
2. **vs Public Transit Passenger App (§18 sibling)** — transit apps center network-wide fare products (passes, zone fares, tap/touch credit, stored value) without named-service booking; rail booking centers the scheduled service inventory with per-journey fare conditions and (commonly) seat inventory. The seam is real and blurred inside single products: UK National Rail sells PAYG contactless and travelcards; 12306 sells 计次•定期票; JR IC cards; DB references Deutschland-Ticket. Working seam: when the product's center of gravity is named-service booking + seat/inventory + per-journey fare conditions → Rail Booking & Ticketing; when it is network fare media + tap-to-ride without service-level sale → Public Transit Passenger App territory. **Flag for joint review when public-transit-passenger-app is processed.**
3. **vs Event Ticketing Platform (§26) / Reserved Seating / Ticket Inventory Management** — both sell seats and issue checkable tickets; the bookable object differs structurally: a scheduled transport service between stations under a timetable and fare system vs an admission to a venue event/session. Rail tickets carry validity windows, route permissions, change/refund ladders and unlimited-travel product classes with no event analog; event tickets carry artist/venue/session semantics with no rail analog. Seat maps appear in both and are NOT distinguishing.
4. **vs Online Travel Agency (§26)** — OTA is multi-vertical travel commerce (flights, hotels, packages). A rail reseller (Trainline) is rail/coach-vertical, deep-integrated with carrier rules and ticket fulfillment; the sale still ends in a rail ticket issued under the carrier's fare system. Adjacent, not the same Type; some OTAs also sell rail as one vertical (adjacency recorded, not researched).
5. **vs Rail Operations Platform (§18 sibling)** — the operator's internal side (dispatch, timetabling, rolling stock, crew) vs the passenger commerce side. The booking system consumes the published timetable as inventory input; it does not manage operations. Removal test: remove passenger sales → operations platform; remove operations → the booking/ticketing system stands alone.
6. **vs Mobility-as-a-Service Platform (§18 sibling)** — MaaS integrates multiple mobility providers behind one account with multimodal journey planning; rail booking systems are single-network/deep-carrier commerce (resellers cover many carriers but do not plan-and-book door-to-door multimodal journeys or operate shared-vehicle access).
7. **What this Type is NOT despite marketing**: a "travel platform" selling rail among other things is still an OTA/marketplace; a gate/validator system with no sales is fare-collection infrastructure; a timetable search with no purchase is a planner. The Type requires the full sale-to-entitlement loop over rail service inventory.

## Historical / Market-Sample Check

- **Ticket-window era**: a station booking office with a printed timetable wall, a fare table, paper tickets issued over the counter, and a conductor/gate check satisfies all three L0 legs with no software — service inventory (the timetable), purchase transaction (cash → printed ticket), ticket as checkable entitlement with fare conditions (validity printed on the ticket). ✔
- **Regional/system-native variations**: China's real-name ID-ticket regime, Japan's two-layer surcharge fare system, the UK's nineteenth-century-origin fare taxonomy (Advance/Off-Peak/Anytime) and Edmondson-card ticket tradition, Germany's flexible-fare culture — all satisfy the core without any of the others' mechanisms. ✔
- **Modern-era machinery** deliberately excluded from the core: e-tickets/QR, apps, seat maps, real-time availability, contactless PAYG, waitlists, loyalty points, dynamic pricing. ✔
- **Reseller structure is a variant, not the definition**: the 12306 operator-monopoly pole ("railway has not authorized third parties") and the UK competitive-retail pole both satisfy the core. ✔

## Uncertainties

1. **North American operator pole unverified** — Amtrak and VIA Rail official surfaces were unreachable (403 / transport errors). The NA fare structure (e.g., Value/Flexible-class systems) is NOT asserted anywhere in this research; NA is held as market anchor only. The operator-run pole is nevertheless well covered by DB + JR Central + 12306.
2. **JR East/Ekinet unreachable** — the Japan evidence comes from JR Central/smartEX surfaces only; JR East's own system was not verified. No JR-East-specific claims made.
3. **12306 evidence is homepage-navigation-level** (Chinese site; no deep article fetch). Real-name ticketing, waitlist orders, change actions and the no-reseller notice are directly observed at menu/notice level; detailed rule parameters were not fetched and are not asserted.
4. **Operator-side machinery (inventory allocation across channels, allotment management, dynamic availability control)** was not directly documented in fetched sources; only inferred from observable behavior (limited Advance inventories, per-train availability states, sale-start times). Held as inference, not asserted as structure.
5. **Seat-selection depth at 12306** observed only at menu level; not used for any L1 claim.
6. **DB detail pages** (seat-reservation product page, fare condition documents) were not reachable; DB claims rest on the help FAQ and the offers page.

## Final Synthesis

Rail Booking & Ticketing is the passenger-commerce system of rail transport: a **bookable inventory of timetabled train services between stations**, sold through a **purchase transaction that issues a ticket**, where the **ticket is a checkable travel entitlement carrying fare conditions** (origin/destination, validity, train-binding where the fare demands it, passenger entitlement). Everything else commonly associated with it — seat reservation and seat maps, accounts and trip management, change/refund ladders, delay compensation, e-tickets and QR codes, railcards and loyalty, multi-channel sales — is common mature structure built on that core, while the retail structure (operator-exclusive vs competitive resellers), the identity regime (real-name vs anonymous), the fare taxonomy shape (two-layer surcharge vs Advance/Off-Peak/Anytime vs saver/flexible), and the reservation culture (mandatory vs optional) are variant axes along which markets differ. The boundary is sharpest against the airline PSS (same family, different transport semantics and fare-product family), the Public Transit Passenger App (network fare media vs per-journey service sales — flagged for joint review), and Event Ticketing (scheduled transport services vs venue admission).
