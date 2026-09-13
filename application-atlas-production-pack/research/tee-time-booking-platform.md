# Research Notes — Tee Time Booking Platform

## Research Goal

Understand what a Tee Time Booking Platform actually is as an Application Type: the golfer/consumer demand side of golf tee-time commerce. Extract the smallest defining structure, the standard mature capabilities around it, the variant poles, and the boundaries against adjacent leaves — especially Golf Course Management (operator side, processed 2026-09-08, which left an explicit seam), Sports Court Booking (demand-side sibling, processed 2026-09-09, which left a proposed discriminator), Sports Marketplace (processed 2026-09-09, forward flag), Golf Tracking / Handicap Application (processed 2026-09-08), and Amenity Booking / Fitness Class Booking / Appointment Scheduling.

## Initial Boundary

Working hypothesis at start:

- Core use: a golfer finds a course, picks a starting time, books it for a party (or takes a spot in an existing game), pays, and manages the reservation up to arrival.
- Primary users: golfers (public/visitor players and club members); secondary: courses (supply side, usually as "list your course" onboarding).
- Nearest neighbors: Golf Course Management (operator system of record — the same tee time seen from the sheet side), Sports Court Booking (same demand-side loop, different inventory semantics), Sports Marketplace (market-first vs booking-first), Golf Tracking / Handicap (round-record vs booking), OTA / Tour & Activity (travel packages that include golf).
- Suspected boundary: demand-side booking loop vs operator system of record (mirror of the racquet/court seam already ratified in sibling passes).
- Unknowns going in: whether the golf economy (green fees per player, carts, member advance windows, deals/rain checks) is definitional or merely common; how far the social/game-organizing layer extends the Type; whether the big US marketplace pole is documentable.

## Research Questions

1. What is the traded object — what exactly does a golfer reserve (slot, round, player spot)?
2. How is tee-time inventory structured and surfaced (course profiles, search, filters, maps, regions, price display)?
3. What does a reservation carry (course, date/time, holes format, players, rate/cart, source) and what lifecycle does it move through (booked → confirmed → paid → checked-in/played → cancelled/no-show)?
4. How does the party model work (named players, guests, buddy lists, adding/removing golfers, joining games)?
5. How does payment settle (pay-at-booking, deals prepay, booking fees, card-on-file check-in, pay-at-course)?
6. What course-governed rules does the platform mediate (cancellation cutoffs, non-refundable deals, advance windows by membership type, cart inclusion, weather/rain checks)?
7. How does the member pole work (member login, member tee sheet visibility, guest privileges, member types)?
8. What non-booking machinery recurs (handicap identity/verification, rewards, games/competitions, packages, course discovery content)?
9. What separates this Type from Golf Course Management / Sports Court Booking / Sports Marketplace / Golf Tracking?
10. Would older / regional / platform-native products still fit the definition (historical check)?

## Representative Products

| Product | Positioning | Why sampled | Evidence tier |
|---|---|---|---|
| **Chronogolf (by Lightspeed)** | Consumer marketplace of golf courses run on the Lightspeed Golf platform ("Powered by Lightspeed Golf"); public-player booking + member booking; deals; global (Canada/US/international) | Demand surface attached to an operator platform — documents both the marketplace pole and the mediated member pole from Tier-1 golfer help docs | A (golfer help center, 7 articles + marketplace homepage) |
| **Deemples** | Southeast Asia social booking app: "Find Golf Buddies \| Golf Booking"; book tee times + join competitions/games; Malaysia/SEA focus | Social game-first pole; regional (non-US) coverage; shows the demand loop re-centered on finding people to play with | A (official homepage incl. feature claims and community testimonials) |
| **18Birdies** | US super-app: GPS/scorecard/handicap/games/tournaments first; tee-time booking as one help-center surface | Super-app pole — booking embedded in a play-assist product; boundary anchor against Golf Tracking / Handicap | A (own homepage fetch) + A via sibling pass (help-center category list incl. "Tee Times") |
| **Golfshot** | US super-app with a separate "Tee Times" consumer marketplace portal (play.golfshot.com/teetimes) | Second super-app pole; shows booking split off as an attached marketplace surface | A (homepage nav/feature map; portal itself unreachable) |

Market-structure anchors named but not directly documentable this pass (all unreachable — see Sources): **GolfNow, Supreme Golf, TeeOff, GolfPass, EZLinks**. Their market role is nonetheless evidenced [A] through the sibling Golf Course Management pass: course-side software names them verbatim as "third party tee time distributor partner like PGA Tee Times, Golfback, Supreme Golf, Teeoff.com or GolfNow" into which courses distribute tee-sheet inventory. No feature claims for this pole are drawn from memory.

## Sources

Fetched 2026-09-09 (this pass):

- Chronogolf marketplace — https://www.chronogolf.com/ (homepage: "Best Golf Courses, Discounted Tee Times", deals, destinations, "Add booking extras online… Pay online", "List my golf course", "Powered by Lightspeed Golf")
- Chronogolf golfer help center — https://support.chronogolf.com/ (categories: Account Setup & Settings; **Booking Management**; Accessing your Dashboard; Using Whoosh)
  - Booking as a public player — https://support.chronogolf.com/hc/en-ca/articles/208774136-Booking-as-a-public-player
  - Booking as a member — https://support.chronogolf.com/hc/en-ca/articles/360000036760-Booking-as-a-member
  - Booking an online deal — https://support.chronogolf.com/hc/en-ca/articles/9226867800717-Booking-an-online-deal
  - Cancelling and editing reservations — https://support.chronogolf.com/hc/en-ca/articles/210356333-Cancelling-and-editing-reservations
  - Removing yourself from a booking — https://support.chronogolf.com/hc/en-ca/articles/360001737439-Removing-yourself-from-a-booking
  - Checking in from a mobile app — https://support.chronogolf.com/hc/en-ca/articles/16138059081741-Checking-in-from-a-mobile-app
  - Booking through Google — https://support.chronogolf.com/hc/en-ca/articles/37037140638093-Booking-through-Google
  - Section index — https://support.chronogolf.com/hc/en-ca/sections/9338037475469-Booking-Management (also lists: Booking a service reservation; Adding golfers to your member reservation; Searching multiple courses within a club; Staying connected with your club)
- Deemples — https://www.deemples.com/ (homepage: positioning, filters, region/course counts, "Why Deemples?" feature claims, community testimonials)
- 18Birdies — https://www.18birdies.com/ (homepage feature map; help-center category list cited from sibling pass research/golf-tracking-handicap-application.md, fetched 2026-09-08)
- Golfshot — https://www.golfshot.com/ (homepage: feature map + "Tee Times" nav item)

Cross-pass evidence (Tier-1 official pages fetched by the sibling Golf Course Management pass, 2026-09-08):

- Club Caddie tee-sheet page naming third-party tee-time distributors (GolfNow, Teeoff.com, Supreme Golf, PGA Tee Times, Golfback) as optional booking channels writing into the course's tee sheet — https://clubcaddie.com/solutions/teesheet/

Attempted and unreachable this pass (source-access limitation — no claims drawn from model memory for these):

- GolfNow — golfnow.com 403; help.golfnow.com 403; golfnow.co.uk 403
- Supreme Golf — supremegolf.com 403
- TeeOff — teeoff.com 403 (×2 incl. bare domain)
- GolfPass — golfpass.com 403
- EZLinks — ezlinks.com 403
- tee-times.co.uk — returned empty body ×2
- Last Minute Golfer — request timeout
- Wigoa, Golf Empire — transport errors
- Golfshot tee-times portal — play.golfshot.com/teetimes and golfshot.com/teetimes transport errors ×2
- 18Birdies support center — support.18birdies.com transport error ×2 this pass (reachable to the sibling pass on 2026-09-08)
- Deemples help subdomain — help.deemples.com transport error; deemples.com/faq and /how-it-works 404

## Product Observations

### Chronogolf by Lightspeed (marketplace + member booking; Tier-1 golfer help center)

Key observations [A = direct from official pages this pass]:

- Marketplace homepage: "Best Golf Courses, Discounted Tee Times"; "Find your next favorite course"; course cards with photos, hole configurations ("1 holes·18 holes"), price display ("₱5,500-7,500 — Average weekday price of ₱5,500 and weekend price of ₱7,500"); "View more courses"; trending destinations (Ontario, Quebec, Florida, California); mobile app. [A]
- Two-sided supply: "List my golf course — Interested in listing your course? Join the Chronogolf community today!"; "trusted by more than 2 million golfers and 1,800 courses" (vendor claim). Footer: "Powered by Lightspeed Golf © Lightspeed Commerce" — the consumer marketplace is the demand surface of a course-side platform. [A]
- Booking Management help section: "How to create and manage bookings" — articles: Booking through Google; Booking an online deal; Booking a service reservation; Booking as a public player; Booking as a member; Checking in from a mobile app; Adding golfers to your member reservation; Removing yourself from a booking; Searching multiple courses within a club; Staying connected with your club; Cancelling and editing reservations. [A]
- **Public player flow**: "You can book tee times as a public player at participating golf courses through the Chronogolf by Lightspeed marketplace. Whether you're using the website or mobile app…"; search bar to find the course → "On the course profile page, follow the steps in the booking calendar on the right-hand side to complete your reservation." App: sign in with the same login details, search, "follow the on-screen instructions to complete your reservation." "A small booking fee may apply to support platform improvements, without affecting course pricing." [A]
- **Member flow**: "If you're a member at a golf course that uses Chronogolf by Lightspeed, you can reserve tee times directly from the member dashboard, calendar, or mobile app." "Member Tee-Sheet … will open your dashboard and give you access to the course's online tee sheet. Use the tee sheet to view upcoming reservations and select your preferred time slot." "Depending on your membership type, you may be able to book 5, 7, 10, or 14 days in advance." "To include guests, search by last name or select someone from your buddy list." "After completing your reservation, you and your guests will receive a confirmation email." Calendar booking: "Select the date, game type, course, number of players, and member types." "Complete the booking based on your membership privileges." [A]
- **Party model**: "Adding golfers to your member reservation" (article exists); "Removing yourself from a booking — You can remove yourself from a tee time as long as the reservation hasn't been paid and it's more than 24 hours in advance… click View or modify next to your tee time… Click the X next to your name." Individuals are named members of a shared reservation and can exit it. [A]
- **Self-management rules**: "Cancelling and editing reservations — You can cancel a tee time as long as the reservation hasn't been paid and it's more than 24 hours in advance… click Cancel next to your tee time… click Edit instead." [A]
- **Deals**: "Lightspeed Golf offers exclusive online-only deals through chronogolf.com. These limited-time discounts can be booked directly on the website… These limited-time offers can't be booked by phone or in person. Payment is charged in full at checkout. Cart rentals are not included unless stated by the course. Bring your confirmation email (printed or digital) to the course. Deals are non-refundable and can't be canceled. Rain checks may be issued if bad weather prevents play." Each deal "provides specific booking terms and any additional conditions, such as cart rental inclusion or restrictions." [A]
- **Arrival / check-in**: "The mobile self-check-in feature lets golfers check in for their tee times directly from a mobile device without needing to visit the pro shop… available through club-branded mobile apps, as long as it has been enabled by the golf course." "Check-in buttons appear on the home page under Upcoming Tee Times and in the Upcoming and Past Tee Times section." "Choose the players who are checking in. Proceed to payment using the card on file, or add a new payment method… checked-in players will be clearly marked." (Day-of window, GPS-proximity gating and distance threshold are product-specific parameters.) [A]
- **Channel funnels**: "Booking through Google — Some golf courses let you book tee times directly from Google Search or Maps using the Book Online button… If prompted, choose to book with Chronogolf. Select a tee time. Use the filters… Set the number of holes and players. Click Reserve to finish the booking." [A]
- Other surfaces observed by title: "Booking a service reservation" (services beyond tee times); "Searching multiple courses within a club" (club → multiple courses); "Staying connected with your club"; "Tracking your handicap with Chronogolf" and "Scoring Factor" (consumer handicap machinery); "Adding a bank account (ACH) to your profile"; Whoosh integration (driving-range account). [A]

### Deemples (social game-first booking; Southeast Asia)

Key observations [A = direct from official homepage]:

- Positioning: "Find Golf Buddies | Golf Booking | Deemples Golf — Golf Everywhere… Trusted by 100,000+ Golfers Across SEA — Book your golf games easily." [A]
- Search + Map with filters: "18 Holes / 9 Holes / Accept 1 Player / with Promo / Rating 4.5+ / Night Golf / Indoor Golf / Driving Range." [A]
- Region browse: "Golf Courses In Malaysia — Find the golf course you love, select when you'd like to play, and complete your booking to receive an instant confirmation." Region pages with course counts (KL/Selangor 78, Johor 36, …); international destinations (Thailand, Singapore, Brunei, Bintan, Vietnam, Batam). [A]
- Course cards: name, region, review count ("226"), starting price ("From MYR 60/70/185/280…"). [A]
- "Why Deemples?": **Book tee times** — "Secure your tee times with the best online rates offered by golf courses"; **Golf competitions** — "play with new golfers and win some prizes"; **Golf stay and play packages** — "Bundle in hotel stays with our preferred hotel partners"; **Trusted handicap** — "With double user verification, the legitimacy of your handicap on deemples is unlike any other"; **Reward programs** — "Get rewarded for every game you play and every friend you refer"; **Meet new golfers** — "Connect with thousands of golfers already on Deemples." [A]
- Community testimonials [A — user quotes on the official page]: "book golf games, manage your handicap, pay in advance, and find the best rates online"; "It also allows you to book a full flight without going thru more hustle" (party booking); "rates are very competitive if not cheaper than club direct"; "From checking if courses are open, available tee times and having the contact of the courses for cross checking"; a user reports the support team "liaised with the golf club to make the necessary changes" after a wrong-date booking. [A]

### 18Birdies (super-app pole)

- Own homepage fetch [A]: "THE #1 RATED GOLF GPS APP — Get accurate GPS distances, easily track scores, stats, and your handicap, and connect and compete with friends"; games (Skins, Wolf, Nassau…); "AI-Powered Swing Analyzer"; "Discover over 40,000 Courses — Preview course GPS & scorecard for your next round, and view course reviews & pictures from other golfers"; tournaments hosting; community; vendor-reported scale (10M users, 120M rounds scored, 46K courses). Tee-time booking is not the homepage's headline surface — the play-assist loop is.
- Help-center category list (sibling pass, 2026-09-08) [A]: Play a Round, Formats & Scoring, Round History & Performance, Shot Tracking, Statistics, Handicap, Courses, GPS, Wearables, Side Games, Tournaments & Leagues, Community, Practice, **Tee Times** — booking exists as a help-supported surface inside the super-app.

### Golfshot (super-app with a separate booking portal)

- Own homepage fetch [A]: on-course GPS/scoring/statistics/auto-shot-tracking app ("TRUSTED BY 5 MILLION GOLFERS WORLDWIDE", "over 45,000 courses"); feature map (GPS Distances, Auto Shot Tracking, Strokes Gained, Green Maps, Swing ID, Golfscape AR, Handicap Index via GHIN linking/purchase, Tournament Management). Navigation includes a distinct **"Tee Times"** item — a consumer marketplace portal (play.golfshot.com/teetimes per the sibling pass [A]); the portal itself was unreachable this pass (transport error ×2), so its internal flow is not documented here.

### Market-structure cross-evidence (via sibling Golf Course Management pass, 2026-09-08 [A])

- Club Caddie (course-side suite): "book tee times over the phone, in person, online or optionally by… third party tee time distributor partner like **PGA Tee Times, Golfback, Supreme Golf, Teeoff.com or GolfNow**"; "No matter the type of tee time, no matter how or when it is booked… keep your tee sheet organized." This is the operator-side view of this Type: tee-time marketplaces are distribution channels into the course's tee sheet. [A — sibling pass, official page]
- Same pass documented course-side countermeasures that shape the demand-side ruleset: prepay/no-show controls, booking restrictions (member/guest advance windows), waitlists, dynamic pricing ("Flash Price"). [A]

## Cross-product Comparison

| Finding | Chronogolf | Deemples | 18Birdies | Golfshot | Strength |
|---|---|---|---|---|---|
| Golfer-facing bookable tee-time inventory across courses (search → course → slots) | ✔ (search bar → course profile → booking calendar; 1,800+ courses; destinations) | ✔ (search + map; region pages; course cards with from-prices) | ✔ (course discovery + Tee Times help surface) | ✔ (Tee Times portal nav) | Core (4/4) |
| Round semantics: holes format is part of the traded object | ✔ ("number of holes and players" in booking; "game type") | ✔ (18 Holes / 9 Holes filters) | ○ (not on fetched pages) | ○ (portal unreachable) | Core-leaning (2/4 explicit, plus domain structure) |
| Reservation as the golfer's own booking of record (upcoming/past visible, self-managed) | ✔ ("Cancel/Edit next to your tee time"; "View or modify"; Upcoming and Past Tee Times) | ✔ ("book golf games… pay in advance"; support-mediated changes) | ✔ (booking inside the golfer's app account — help category) | ✔ (booking inside the golfer's app account / portal) | Core (4/4) |
| Party of named golfers (add/remove players; guests) | ✔ (adding golfers; removing yourself; guests by last name or buddy list; per-player check-in) | ✔ ("book a full flight"; "Accept 1 Player" single spots) | ○ | ○ | Core-leaning (2/4 explicit) |
| Course-governed rules mediated by the platform (cancellation cutoffs, policies, privileges) | ✔ (cancel only unpaid + >24h; deals non-refundable; member advance windows by membership type; self-check-in "enabled by the golf course") | ✔ (best rates "offered by golf courses"; support liaises with the club for changes) | — (not documented on fetched pages) | — | Core (2/4 explicit; structurally implied by mediation model) |
| Per-booking payment settlement, online-dominant | ✔ (deals "charged in full at checkout"; booking fee; card-on-file at check-in) | ✔ ("pay in advance") | ○ | ○ | Common-dominant (2/4 explicit) |
| Cart add-ons as part of tee-time commerce | ✔ ("Cart rentals are not included unless stated by the course"; per-deal cart terms) | ○ | ○ | ○ | Golf-economy common (1/4 explicit — kept out of core) |
| Deals / discounted prepaid tee times | ✔ (online-only limited-time deals; non-refundable; rain checks) | ✔ ("with Promo" filter; "best online rates"; "cheaper than club direct") | ○ | ○ | Common (2/4) |
| Member mode: member login, member tee-sheet visibility, member advance windows, member types | ✔ (full member flow) | ○ | ○ | ○ | Variant pole (1/4 strong — worded as member-course variant) |
| Check-in / arrival surface on the reservation | ✔ (mobile self-check-in; per-player marks; payment at check-in) | ○ | ○ | ○ | Common-optional (1/4 explicit) |
| Handicap / golfer-identity machinery | ✔ ("Tracking your handicap"; Scoring Factor) | ✔ (verified handicap) | ✔ (handicap calculator — core of the app) | ✔ (GHIN Handicap Index linking) | Common (4/4) — attachment, not definitional |
| Games/competitions & meeting golfers (social layer) | ○ | ✔ (competitions; meet golfers) | ✔ (games, leaderboards, tournaments) | ○ | Common-optional (2/4) |
| Rewards / loyalty | ✔ (none observed on fetched pages — reward article absent) | ✔ (reward programs) | ○ | ○ | Optional (1/4) |
| Stay-and-play packages / travel bundling | ○ | ✔ (packages with hotel partners) | ○ | ○ | Optional (1/4) — travel adjacency |
| Indoor golf / driving-range slots in inventory | ○ | ✔ (Night Golf / Indoor Golf / Driving Range filters) | ○ | ○ | Optional (1/4) — matches GCM's indoor-simulator variant |
| External channel funnels (Google booking surfaces) | ✔ (Book Online from Google Search/Maps) | ○ | ○ | ○ | Optional (1/4) |
| Two-sided supply onboarding ("list your course") | ✔ | ○ | ○ | ○ | Common for marketplaces (1/4 explicit) |
| Web + mobile app forms | ✔ (website + app) | ✔ (app-led, web booking pages) | ✔ (app-led) | ✔ (app + web portal) | Common (4/4) |

Legend: ✔ documented; ○ not documented on fetched pages (absence of evidence, not evidence of absence).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures (the demand-side pattern, instantiated for golf):

1. **Golfer-facing bookable tee-time inventory across golf courses.** Courses held with their bookable starting times — dated, time-stamped slots for a round (9 or 18 holes where offered) — surfaced for golfer discovery (search, map/region browse, course profiles with prices and reviews) and kept bookable from the golfer's side. Remove → a course directory/listings surface.
2. **The tee time reservation as the golfer's booking of record.** A golfer — organizing a party or taking a player spot — holds a specific starting time at a specific course; the reservation persists in the golfer's own record (upcoming + past), carries the party (named players/guests), and is self-managed (edited, cancelled, or exited under the course's rules) through to arrival at the course. Remove → listings with nothing to book, or a bare widget with no golfer-side memory.
3. **The mediated third-party course relationship.** The course is not the golfer's organization and is not governed by the platform: the course's prices (green fees per player), cancellation policy, membership privileges, and property rules govern; the platform mediates the loop discovery → booking → payment → confirmation → arrival; per-booking settlement is dominant (online prepay; card-on-file at check-in; pay-at-course variants). Remove → the course's own system of record (Golf Course Management territory).

Jointly-held is load-bearing: (1) alone = course directory; (2) without (1) = a booking widget with no inventory to browse; (3) without (1)+(2) = a review/discovery surface; (1)+(2) without (3) = the course's own booking channel (operator side); (1)+(3) without (2) = search with no reservation memory.

Historical/market-sample check (pre-freeze): paper-era demand side = phoning the pro shop or the club reservation book — no software Type (the conceptual loop learn-availability → reserve → pay → play is the ancestor). Early-web course websites with booking forms = operator channels (legs 1–2 satisfied but leg 3 fails when the surface IS the operator's system with no golfer-side record). A regional portal listing several courses with golfer accounts, per-player prices, and self-service cancellation satisfies all three legs — check passes. Non-US/regional products (Deemples SEA, Chronogolf Canada/global) satisfy. Web-only and app-only forms satisfy. Marketplace aggregation is NOT required by the letter of the definition — a single-course demand surface with its own golfer-side booking record satisfies the loop (the aggregation is the dominant form, not the definition). Check passed.

### L1 — Common Mature Structure (not definitional)

- search & discovery richness: location/map search, region and destination browse, filters (holes format, promos, ratings, night golf, indoor/range), course profiles with photos, reviews, ratings, price display (from-prices; weekday/weekend differences)
- golfer accounts & profiles: login, upcoming/past tee times, payment methods on file, booking history
- party management: named players, guests (by name or buddy list), adding/removing golfers, confirmation to all players
- self-service cancellation/editing under course-set rules (unpaid status and advance cutoffs as the recurring rule shape)
- online payment at booking; booking fees layered on top of course pricing; payment at check-in with a card on file (variant)
- deals & pricing machinery: limited-time online-only discounted tee times, promos, non-refundable prepaid deals, weather/rain-check handling
- member mode where the course runs club membership: member login, visibility of the course's online tee sheet, advance booking windows by membership type, guest inclusion, member-type rate selection per player
- check-in / arrival surface (mobile self-check-in where the course enables it; per-player check-in state)
- handicap / golfer-identity machinery (self-computed handicap, verified handicap, or official-index posting) as the golf-native identity layer
- rewards/loyalty for booked and played rounds
- two-sided onboarding ("list your course")

### L2 — Variant / Optional Structure

- product-form poles: **standalone tee-time marketplace** (multi-course aggregation as the center) / **platform-affiliated marketplace** (demand surface of a course-side platform) / **super-app attachment** (booking inside a GPS/score/play product, sometimes split to a separate portal) / **social game-first booking** (find players and join games; the game resolves into tee-time bookings)
- game-organizing social layer: open competitions/games, meeting golfers, party assembly
- stay-and-play packages (travel adjacency; bundles with hotel partners)
- inventory breadth beyond the round: night golf, indoor golf/simulator slots, driving-range bookings, service reservations (e.g., other bookable services at the course)
- external channel funnels: booking actions surfaced in general search/maps products
- regional market shapes: US marketplace giants (documented indirectly this pass), SEA mobile-first social booking, Canada/global platform marketplace
- settlement depth: full prepay, per-player payment, pay-at-course

### L3 — Vendor-specific (kept out of the final document)

- Chronogolf: 24-hour/unnpaid cancellation rule specifics; 5/7/10/14-day advance windows by membership type; self-check-in day-of window, 500 m GPS gating, "check-in window closes two hours after the tee time" parameters; "Scoring Factor"; Whoosh range-account integration; ACH bank account on golfer profile; "Booking through Google" flow; club-branded app check-in enablement; "Powered by Lightspeed Golf" branding
- Deemples: "double user verification" handicap mechanics; promo/rating filter values; "From MYR" price-card format; reward/referral mechanics details; "full flight" party phrasing
- 18Birdies: 10 named side games, AI swing analyzer, vendor scale figures (10M users / 120M rounds / 46K courses)
- Golfshot: Golfscape AR, Swing ID, GHIN purchase/link flow, 45K-course figure, 5M-golfer figure
- US marketplace family (GolfNow/TeeOff/GolfPass/Supreme/EZLinks): unreachable — no vendor-specific claims drawn

## Vendor-specific Findings

- Chronogolf's straddle: one product family carries the operator system (Lightspeed Golf: tee sheet, house accounts, subscriptions, reports — its own operator help center) AND the consumer marketplace/member surfaces. Treated like the Playtomic/Playo straddle in the sports-court-booking pass: documented on both sides, not resolved by merger — the two sides remain different Types.
- Chronogolf's member tee-sheet visibility ("give you access to the course's online tee sheet… view upcoming reservations") is the clearest direct evidence that the demand surface fronts the course's tee sheet without being the system of record.
- Deemples' "liaised with the golf club to make the necessary changes" (user testimonial on the official page) is informal evidence of the mediation model (the platform works with the course to effect changes; the course's rules govern).
- Cancellation-rule shape recurs (unpaid + outside cutoff) in two Chronogolf articles; the specific 24-hour value is product-specific.

## Boundary Findings

- **vs Golf Course Management (processed 2026-09-08) — RATIFIED from this side; DISCHARGES that pass's seam flag.** GCM is the operator's system of record: tee-sheet configuration, check-in/starter flows, golfer profiles with classifications, play-and-revenue records. This Type is the golfer's demand-side loop; the course is a third party whose inventory the platform fronts. A course's own booking engine/member portal is a channel of the operator system, below this Type's bar unless a golfer-side booking record exists. Remove the operator-of-record side from GCM → you get this Type's surface; add sheet configuration/revenue records to this Type → it becomes GCM. Chronogolf/Lightspeed straddles the seam in one product family (documented, not merged).
- **vs Sports Court Booking (processed 2026-09-09) — RATIFIED; DISCHARGES that pass's forward flag.** Same three-leg demand-side core, different inventory semantics: golf trades **starting slots on a course's tee sheet for a round, priced per player** (green-fee classes, carts as add-ons, member advance windows), while court booking trades **exclusive hourly rental of a court/space**. Golf adds the round (9/18 holes) as the unit, per-player party management as the norm, and the golf-native identity/deal economy. The sibling passes' proposed discriminator ("per-player green fees/round/tee-sheet semantics vs per-court hourly rental") is confirmed with direct evidence. Keep both; joint partition of the §28 booking family holds (with Amenity Booking's closed-population pole already separated).
- **vs Sports Marketplace (processed 2026-09-09) — RATIFIED.** That pass flagged this leaf as the golf demand-side sibling with the proposed seam "tee-sheet/round/per-player semantics vs court-hour/game/lesson offerings." Confirmed; additionally: Deemples shows the booking-first product can carry a marketplace-like social layer (games/competitions) while the booking loop remains the spine — the same center-of-gravity seam that pass held against Playtomic/Playo straddles.
- **vs Golf Tracking / Handicap Application (processed 2026-09-08).** The round-record system (score, stats, handicap) vs the booking loop. Products straddle (18Birdies, Golfshot, Chronogolf all carry handicap machinery) — consistent with that pass's finding that tee-time booking is a "consumer marketplace attachment." The traded object differs: a round record vs a round reservation.
- **vs Amenity Booking Platform (processed).** Closed resident/tenant population booking building-owned facilities vs open golfer population booking third-party courses.
- **vs Fitness Class Booking (processed).** Participant spot in a staffed program vs a starting slot on a course for a round.
- **vs Appointment Scheduling Application.** Generic slot booking lacks golf-typed inventory (courses, tee sheets, holes formats), per-player green-fee pricing, party semantics, and course-governed privileges.
- **vs Online Travel Agency / Tour & Activity Marketplace.** Stay-and-play packages flirt with travel bundling, but the Type's center is the single-round tee-time reservation; packages are an optional attachment (Deemples pole).
- **vs Restaurant Reservation Platform.** Structural sibling (reserve a time at a third-party venue) in a different domain; different inventory, pricing and party semantics.
- **Floor test:** a course's bare embedded booking widget with no golfer-side account/memory is a channel of the operator's system, below this Type's bar; the Type's floor is the golfer-side booking loop with the golfer's own reservation record.

## Historical / Market-Sample Check

- Paper-era: tee times were taken by phone at the pro shop; the club kept the sheet. No software Type on the demand side; the loop is the ancestor.
- Early web: course websites and club portals with booking forms are operator channels (the golfer gets no persistent platform-side booking record; the club's sheet is the record).
- The sampled Type — third-party golfer-side booking platforms — is the current dominant form, but the definition deliberately does not require: marketplace aggregation at scale (a single-course demand surface with a golfer-side record satisfies), mobile apps (web-first forms in sample), social/game layers (Chronogolf-style public booking satisfies), in-app prepay (pay-at-course variants), or US market structure (SEA/Canada poles in sample).
- The US marketplace pole (GolfNow family and aggregators) could not be directly documented this pass; its market role is held on sibling-pass [A] evidence (named as tee-time distributor partners in course-side documentation). The definition does not depend on that pole's specifics.
- Check passes: the definition is not an artifact of the US-marketplace pattern.

## Uncertainties

- **US marketplace pole undocumented at product level**: GolfNow/Supreme/TeeOff/GolfPass/EZLinks all blocked (403) this pass. Features commonly associated with that pole (dynamic/consumer-facing pricing, rewards programs, metasearch comparison across providers) are NOT asserted in the final document — only the market-structure fact that courses distribute tee times to such platforms (sibling-pass [A] evidence).
- **Whether marketplace breadth (many courses) is definitional**: held as NOT definitional (mirroring the sports-court-booking anti-overfit ruling), but the dominant market form is clearly multi-course aggregation; a golfer-side record on a single-course demand surface is the theoretical floor, untested against a live product this pass.
- **Anonymous/guest checkout**: every product in the reachable sample requires a golfer account to book ("sign in using the same login details", "log in to your profile"). Whether any in-type product supports anonymous booking is unverified; account-holding is held as dominant-common, not definitional.
- **Per-player pricing explicitness**: green fees are per player in structure (member types per player, per-player check-in, single-player spots in games, cart add-ons), but no fetched page states "price is per player" verbatim; worded as structural, not verbatim-quoted.
- **"Booking a service reservation"** (Chronogolf) was not fetched — services beyond tee times are held as an observed title only.
- Deemples' evidence is homepage-level (feature claims + testimonials), not help-center-level; its internal booking flow details are not documented.
- 18Birdies' tee-time booking surface is evidenced by a help-category title (sibling pass) and its app structure, not by a fetched booking-flow article.

## Final Synthesis

A Tee Time Booking Platform is the golfer-side application for reserving rounds of golf. Its defining core is three jointly-held structures: golfer-facing bookable tee-time inventory across golf courses (courses with their dated, time-stamped starting slots, searchable and comparable, priced per player); the tee time reservation as the golfer's booking of record (a named party holding a specific starting time, persisting in the golfer's upcoming/past record, self-managed — edited, cancelled, or exited player-by-player — under the course's rules, through to arrival and check-in); and the mediated third-party course relationship (the course's green-fee prices, cancellation policy, membership privileges and property rules govern; the platform mediates discovery → booking → payment → confirmation → arrival, with per-booking online settlement dominant). Around this core, mature products add discovery richness (maps, regions, filters, reviews, from-prices), party machinery (guests, buddy lists, per-player management), payment depth (prepaid deals, booking fees, card-on-file check-in), deals economics (limited-time online-only discounts, rain checks), member mode (member tee-sheet visibility, advance windows, guest rights), handicap-based golfer identity, rewards, and — in some products — social game-organizing and travel packages. Product forms span standalone marketplaces, platform-affiliated marketplaces, super-app attachments, and social game-first booking. The Type is the demand-side mirror of Golf Course Management: the operator owns the sheet and the round record; the platform owns the golfer's path to the first tee. No directory change proposed; the leaf stands as an independent Type.
