# Research Notes — Sports Marketplace

## Research Goal

Understand what software sits under the directory leaf "Sports Marketplace" (§28 Sports, Fitness & Recreation, line 2050, between "Recreation Center Management" and "AI Fitness Coach"): what market this Type operates, what is traded on it, who the two sides are, how discovery and transactions work, and where the boundary lies against the neighboring sports Types — above all **Sports Court Booking** (processed 2026-09-09, which flagged this leaf as "Service/Sports Marketplace — discovery and transactions across many verticals; here the court-time booking loop is the spine") and the **Service Marketplace** umbrella (§05.02, processed 2026-09-07, whose domain-structured-sibling list did not yet include sports).

## Initial Boundary

Working hypothesis going in (from directory position and sibling passes):

- The leaf names the **operator-run two-sided market for the recreational sports economy** — the platform where venue/facility time, organized games, and coaching are aggregated from independent providers and transacted by players, with cross-vertical discovery as the center.
- The sports-court-booking pass (2026-09-09) sampled the venue-booking products (Playtomic, Playo, GotCourts, Playfinder) and drew the seam from its side: "a marketplace aggregates many verticals with discovery as the center; here [court booking] the center is the court-time booking loop itself." A center-of-gravity seam, expected to be ratified from this side.
- The service-marketplace pass (2026-09-07) established the umbrella + domain-structured sibling pattern (beauty, babysitting, home-services, local-service; food-delivery/tour §26; insurance §08; load-board §18; brand-creator §27; volunteer §25). Sports was not in its sibling list — this pass is expected to establish the sports sibling.
- Ambiguity going in: in common usage "sports marketplace" can also name **gear resale markets** (buy/sell equipment). The §28 habitat (surrounded by venue/booking/recreation leaves) and the sibling passes' framing point to the playing-economy reading. Gear resale is treated as adjacent territory (§05.19 Resale family) and pursued only as a boundary pole.

Nearest neighbors: Sports Court Booking (demand-side booking loop), Service Marketplace (generic umbrella), Sports Facility Management (operator-side system of record, processed 2026-09-09), Tee Time Booking Platform (golf demand sibling, unprocessed), Athlete Recruiting Marketplace (processed 2026-09-06 — traded subject is athletic talent), Resale Marketplace family (§05.19 — traded subject is goods), Tournament Management / League Management Platforms (competition administration), Fitness Class Booking (participant spots in staffed classes), Outdoor Recreation Discovery (discovery without transactions).

## Research Questions

1. What is traded on this market? Which offering verticals does it span?
2. Who supplies, and how is supply authored (venues/clubs, game organizers, coaches/academies)?
3. How does demand discover — by what axes, and across what verticals?
4. What transactions exist (book slot, join game, book lesson) and what does the engagement of record look like?
5. What community/matching machinery exists (find players, levels, ratings, chat) — definitional or common?
6. Where does money sit (payment timing, platform fees, provider plans/payouts)?
7. What does the provider side look like (onboarding, verification, consoles)?
8. What rules govern (cancellation policies, verification/removal, participation rules)?
9. Boundary judgments: vs Sports Court Booking, Service Marketplace umbrella, Sports Facility Management, Athlete Recruiting Marketplace, Resale Marketplace, Tee Time Booking, Tournament/League Management, Fitness Class Booking, Outdoor Recreation Discovery.

## Representative Products

Selected for market representation, documentation completeness, distinct product philosophies, and distinct customer levels:

1. **Playtomic** — global racket-sport (padel/tennis/pickleball) player-club-coach market; the market+community pole where court booking, open matches, classes/academies, tournaments, and leagues share one surface. Tier-1 player help center + Tier-2 official product pages (Academy).
2. **Playo** — multi-sport urban market across India, the Gulf, SE Asia, Australia; explicit three-vertical framing (PLAY / BOOK / TRAIN); venue + games + trainer verticals each documented in a Tier-1 knowledge base.
3. **CoachUp** — US private-coaching marketplace (1-on-1, camps/clinics, virtual training); the coaching-vertical pole with strong trust machinery and a different demand posture (parents/athletes buying instruction, not joining games). Tier-2 official pages.

Rejected / abandoned:

- **OpenSports** (game-organizing marketplace) — transport error ×2 (www and app hosts; consistent with the sports-court-booking pass's two failures on the same domain). Abandoned per network rules; the join-games pole is covered through Playtomic's Open Matches and Playo's GameTime/Playpals, both Tier-1.
- **SidelineSwap** (gear-resale pole) — 403 on site + timeout on help center; abandoned. The goods-resale boundary is held structurally against the §05.19 Resale family; no product-specific claims made.
- **GotCourts / Playfinder** — already sampled by the sports-court-booking pass; used here only for seam reasoning, not re-researched.

## Sources

All fetched 2026-09-09 unless noted.

- Playtomic — homepage (https://playtomic.io/); Academy product page (https://playtomic.io/academy); Player Help Center home (https://playerhelp.playtomic.com/hc/en-gb); Learn & Compete category (https://playerhelp.playtomic.com/hc/en-gb/categories/19506582401425-Learn-Compete). (Reservation/cancellation/level articles in the same help center were documented by the sports-court-booking pass the same day and are cited there.)
- Playo — homepage (https://www.playo.co/); Customer Support knowledge base (https://playo.freshdesk.com/support/solutions); articles: How Do I find Coach/Trainers in the app?; I am a coach, how can i register myself in the playo app?
- CoachUp — homepage (https://www.coachup.com/); How CoachUp Works (https://www.coachup.com/how_it_works).
- Unreachable: opensports.net / app.opensports.net (transport error ×2); sidelineswap.com (403) and help.sidelineswap.com (timeout).

## Product A — Playtomic

### Key observations (evidence layer A unless noted)

- Positioning (homepage): "Find courts and players near you… Find matches and courts worldwide"; "world's leading App for racket sport players and clubs"; "the place where players, clubs, and coaches come together." Nav splits: For players (book padel/tennis/pickleball courts; find a club) vs For clubs (Playtomic Manager; Playtomic Coach; Academy; Pricing).
- Player value loop (homepage): **Find** (create private matches with friends, make them public to find new partners, or search active matches nearby to join) → **Book** → **Join the community**. Player level estimation system is presented as part of the match experience ("play knowing your level and that of your opponents").
- Help-center category structure (Tier-1) mirrors a multi-offering market: App & Settings; Reservations & Payments; **Open Matches & Community** ("Find open matches near you and connect with other players"); **Level & Results**; **Learn & Compete** ("Improve your game with classes and test your skills in tournaments and leagues"); Subscriptions & Offers (Premium subscription, club offers). Promoted articles include Leveling Clubs.
- Learn & Compete articles (Tier-1): **Classes** (join classes offered at a club; leave a course; recurring payments for courses); **Tournaments** (What is Open Play in padel/pickleball; how to join a tournament); **Leagues** (join a league; cancel my spot; league standings; find matches and matchdays; reschedule a league match).
- Coaching vertical — Academy (official product page): "Playtomic's built-in training solution"; clubs publish recurring courses, one-off clinics, and private lessons; "all discoverable and bookable in the Playtomic player app"; sessions "visible to 2M+ players" (vendor-published reach figure); "players sign up and pay directly in-app"; "managed entirely through Playtomic Manager." Course types: Courses (multi-session, recurring, custom player levels & pricing, linked to coach and court availability), Clinics (one-off group sessions, level-based filtering), Private classes (1:1, flexible coach availability, player-led booking, custom pricing per coach or session type). Clubs are urged to use off-peak hours for training programs ("fill empty courts", "grow coaching revenue").
- Operator side: Playtomic Manager — "manage your racket club all in one place. Receive online bookings, manage your customers, create social activities and increase the occupancy of your courts."
- Scale (vendor-published, third-party quote on vendor page): "connects 4 million players with 5500 partner clubs in over 52 countries" — evidence of network shape, not of precision.
- Layer-B note: reservation flow, private-booking vs open-match mechanics, cancellation policy enforcement, split payment, Club Wallet, and level-system mechanics were documented at Tier-1 by the sports-court-booking pass from the same help center; not re-researched here.

## Product B — Playo

### Key observations

- Positioning (homepage): "Book sports venues. Join games. Find trainers near you." — "The World's Largest Sports Community to Book Venues, Find Trainers, and Join Games Near you"; "YOUR ONE STOP PLATFORM". Main navigation is the market's own taxonomy: **PLAY** (games) / **BOOK** (venues) / **TRAIN** (trainers) / **PARTNER** (partner with us). Popular sports: badminton, football, cricket, swimming, tennis, table tennis. City landing pages: Bangalore, Chennai, Hyderabad, Pune, Mumbai, Delhi NCR, …, plus Dubai, Qatar, Australia, Oman, Sri Lanka.
- Venue vertical (help center, Tier-1): "Venues: Places to Play" (search by venues; contact venue management; rate a venue/submit feedback); "Booking Venues & Experiences" (book more than one hour in advance; multiple days in one transaction; **offline bookings** — pay at venue; FAQ: "I have made full payment at the venue… but it still shows 'payment to be made' in the app"); "Rescheduling" (change court; transfer booking between venues); "Cancellation & Refunds" (12 articles, incl. venue-set cutoffs).
- Games vertical (help center, Tier-1): "GameTime by Playo" (11 articles — platform-organized games: participation cancellation, bringing a friend, equipment); "Meet Playpals" (23 articles — find activities matching skill set; host activities; notify Playpals about a hosted activity; leave-by rules); "Playo Groups/Squad".
- Ratings: "Playostats & Player Ratings" (12 articles — how rating works, overall rating calculation, can I know who rated me).
- Trainer vertical (help center, Tier-1): "How Do I find Coach/Trainers in the app?" — Train tab → location → sport → browse coach list; filter by sport, age group, preferred batches. "I am a coach, how can i register myself in the playo app?" — Train → "I am an Individual" → fill details → add certifications → choose a starter plan → verification → "you will be a registered coach on our platform and our users can view your profile." Academies can register through a parallel article.
- Money & loyalty: Payments section (saved cards, transaction identification, receipts), "Karma, Offers & Venue Loyalty" (accumulate/redeem Karma; booking on the app earns Karma discounts), gift cards.
- Operator side: "Partner with us" venue onboarding.

## Product C — CoachUp

### Key observations

- Positioning (homepage): "Private and Group Coaching Lessons and Local Sports Training Courses"; "Train with the largest network of expert coaches with a proven track record." Demand framing: athletes/parents seeking instruction — no game-joining, no venue booking.
- Flow (How It Works, official): **Step 1 Search** — enter location + training goals; the platform recommends three coaches; browse all coach profiles sorted by distance, price, reviews, and training types (in-person or online). **Step 2 Book** — "Message Coach" with questions, or "Book Now"; after booking, each party receives the other's contact information and arranges the first session directly. **Step 3 Train**.
- Training types: 1-on-1 training; Camps and Clinics (small-group); Virtual training (custom plans, video analysis, game-film review).
- Trust machinery (official): "Coaches You Can Trust — all of our coaches have extensive coaching experience and are required to pass rigorous background checks"; benefits section details **3 distinct background checks** (identification verification, sex-offender check, national criminal search); verified reviews with quality enforcement ("If coaches don't perform up to our expectations, we remove them from our community"); **Good-Fit Guarantee** ("100% money back"); payments by credit card, "securely processed online."
- Supply side: "Apply to Coach" / "Coach With Us"; CoachUp U — collegiate athletes legitimized as coaches ("early entrepreneurs"); sports browse pages (soccer, lacrosse, baseball, basketball with skill topics).
- Community: CoachUp Nation (content community — articles, Q&A) — content, not participation matching.
- Note: no venue-time or game-spot inventory is traded — the market's subject is instruction. This bounds what can be claimed as definitional for the Type.

## Cross-product Comparison

| Aspect | Playtomic | Playo | CoachUp |
|---|---|---|---|
| Traded offerings | court slots + open-match spots + classes/clinics/private lessons + tournaments/leagues | venue slots + games (platform-run GameTime, hosted activities) + coach/academy programs | coaching sessions (1-on-1, camps/clinics, virtual) |
| Supply side | partner clubs (via Playtomic Manager), coaches/academies publish programs | venues onboard via Partner-with-us; coaches/academies self-register, verified | individual coaches apply; background-checked; removed for poor performance |
| Discovery axes | sport, location/club, date/time, level | sport × city; PLAY/BOOK/TRAIN tabs; filters (age group, batches) | location + training goal; sort by distance/price/reviews/type |
| Supply authoring | clubs publish courses/clinics/lessons; club availability | venues manage slots; coaches author profiles+certifications | coaches author profiles; platform curates |
| Transaction | book court; join open match (pay spot); enroll course; join league | book venue slot; join/host activity | book coach (optionally message first) |
| Money | in-app payment, split payment; service fee (sibling pass); Premium | in-app payment defines a tracked booking; offline booking variant; Karma | secure online card payment; money-back guarantee |
| Participation community | open matches, level system, results, chat | playpals, ratings, groups, hosting | none (content community only) |
| Provider console | Playtomic Manager + Academy management | partner onboarding; coach registration | coach onboarding (dashboard not fetched in detail) |
| Geography | global racket network | city networks (India/Gulf/SEA/Australia) | US national |

**Cross-product commonalities (evidence layer B):**

- All three are operator-run two-sided markets in the recreational sports economy: many independent providers (venues/clubs; game organizers; coaches/academies) reach players through one shared, operator-branded surface; the operator hosts the market and its rules and does not itself run the venues or deliver the coaching (Playo's GameTime and Playtomic's league programming are platform-organized offerings layered on partner supply — see layer notes below).
- Supply is **provider-authored** and **sport-typed**: venue pages with courts/slots and venue-set prices/policies; coach profiles with certifications and session types; club-published courses/clinics. The platform verifies providers before they face the market (Playo coach verification; CoachUp background checks; club onboarding).
- Discovery is organized by **sport as the primary axis**, combined with location and time/level; the market's offerings are typed by sport, and (in the multi-vertical products) discovery spans more than one offering vertical.
- The on-platform transaction creates a **persistent player-side engagement of record** — a booked slot, a joined spot, a booked lesson — held in the player's account (upcoming + history, receipts) and carried through a managed lifecycle with cancellation/reschedule machinery under provider-set policies.
- Provider-side consoles exist for managing the provider's market presence (venue manager products; coach registration/management).

**Layer-C canonical inference:** the Type is the sports-domain sibling of the Service Marketplace umbrella: an operator-run market whose traded subject is **playing sports** — facility time for play, participation in games, and instruction — organized by sport, with the market (cross-vertical discovery + participation matching), not the single booking loop, as the center of gravity.

## Canonical Abstraction Hierarchy

### Level 0 — Defining Invariant

Three jointly-held structures:

1. **The operator-run two-sided sports market** — one platform-operated market over many independent sports providers (venues/clubs, game organizers, coaches/academies); the operator aggregates the supply, hosts the shared surface, and enforces market rules, but does not itself run the venues or deliver the instruction. Remove → a single venue's booking channel or one operator's own programs (Sports Facility Management / operator territory).
2. **Sport-organized, provider-authored supply with platform verification** — each offering is typed by sport (court/turf/pool time, a game to join, a course or lesson) and authored by its provider (venue slots with venue-set prices/policies; coach profiles with credentials; club-published programs), with the platform verifying providers before they face the market. Remove → generic classifieds, or an operator-configured catalog below the market bar.
3. **The on-platform participation transaction of record** — discovery across the market (by sport, location, time, level) ends in a transacted engagement binding player × offering × time (a booked slot, a joined game spot, a booked lesson), held as the player's persistent record and carried through a managed lifecycle (confirmed → played / cancelled / refunded) with platform-mediated money. Remove → directory/forum/discovery-only surface (Outdoor Recreation Discovery territory).

Jointly-held load-bearing: 1 alone = venue directory; 2 without 1 = scattered provider profiles; 3 without 1+2 = bare booking widget; 1+2 without 3 = browse/review surface with no transaction; 1+3 without 2 = operator's own program catalog; 2+3 without 1 = un-mediated service list.

### Level 1 — Common Mature Structure

- provider verification and trust machinery: background checks, certification checks, verified reviews, money-back/good-fit guarantees, removal for poor performance
- player participation community: open games/matches to join, find-players by level, hosting your own games, chat (structural in the venue/game poles — absent at the pure coaching pole → common, not definitional)
- player level/skill systems and ratings as market currency (level-based filtering, matchmaking quality, player ratings)
- venue and coach ratings/reviews submitted by players
- provider-set cancellation policies enforced through the platform; refunds per policy
- platform-organized offerings layered on partner supply (platform-run games, leagues)
- tournaments/leagues as market offerings (join, spot cancellation, standings)
- provider consoles (venue manager: calendar, bookings, customers, programs; coach dashboards)
- loyalty/rewards, premium subscriptions, offers, gift cards
- player-created supply in the game economy (making private matches public; hosting activities)

### Level 2 — Variant / Optional Structure

- vertical breadth: multi-vertical market (venues + games + coaching, + tournaments/leagues) vs single-vertical coaching market vs venue-listing market
- sport scope: single sport family (racket) vs multi-sport; golf as a structurally sibling domain (Tee Time Booking leaf)
- booking mode: instant vs enquiry-based (documented in the sports-court-booking pass)
- community depth: none → find-players → open-match marketplace with auto-fill/auto-cancel economies
- geography: city-density network models vs national/niche coverage
- monetization: commission/service fees, provider starter plans, premium player subscriptions, loyalty economies
- offline money variants (pay at venue) alongside in-app payment

### Level 3 — Vendor-specific Structure

- Playtomic: Academy course/clinic/private-class machinery linked to coach-and-court availability; Open Play; league matchdays/standings/rescheduling; Leveling Clubs; Club Wallet; Premium
- Playo: GameTime (platform-organized guaranteed games) with participation-cancellation rules; Playostats rating calculation; Karma loyalty; coach starter plans; offline-booking category
- CoachUp: three-check background stack; Good-Fit Guarantee (100% money back); recommended-three-coaches flow; CoachUp U

## Vendor-specific Findings

- Playo's "offline booking" category (payment at the venue leaves the booking outside the tracked app flow) shows the platform's own boundary: in-app payment is the platform's operating definition of a tracked booking — while the Type-level invariant remains the transaction of record, not its payment rail.
- Playo's coach "starter plan" shows a monetization variant where providers pay for market access rather than (or alongside) per-transaction fees — consistent with the umbrella's fee-form variance.
- CoachUp's post-booking contact exchange (parties arrange sessions directly) shows the engagement's execution sitting partly off-platform in the coaching pole — the transaction and trust machinery, not the session delivery, are the market's product.
- Vendor consolidation: GotCourts is Playtomic-owned (noted by the sibling pass); not material here beyond seam reasoning.

## Boundary Findings

- **vs Sports Court Booking (processed)** — RATIFIED from this side, on the seam that pass itself proposed. Center of gravity: in Sports Court Booking the court-time reservation loop is the spine (find court → book → play), and the sampled products are venue-booking-first; in Sports Marketplace the **market** is the spine — the operator aggregates multiple offering verticals (venue time, games, coaching, and in some products tournaments/leagues), and the player-facing surface is a market to browse and join, of which court reservation is one transaction form. Straddle: Playtomic and Playo instantiate both Types (booked here from the market view; documented there from the loop view). Removal tests: strip the market aggregation and participation matching, keep the slot loop → Sports Court Booking; strip the slot-only loop and keep multi-vertical aggregation + participation matching → this Type. Keep-both; no directory change.
- **vs Service Marketplace (§05.02 umbrella, processed)** — the domain-structured sibling, per the beauty/babysitting/home-services/local-service precedent: the domain binding is the **playing economy of sports** (sport-typed playing supply: facility time for play, participation in games, instruction), sport as the primary discovery axis, and player identity (levels, ratings, sport profiles) as market machinery. Settlement-timing divergence at the venue pole (pay at booking) matches the beauty sibling's appointment-model divergence from the umbrella's hold-until-completion invariant. This pass adds the sports sibling to the umbrella's recorded sibling list; no directory change.
- **vs Sports Facility Management (processed)** — that Type is one venue operator's business system of record (rentable-space inventory, bookings, money); this Type is the cross-venue market over many operators. Consistent with that pass's recorded note that "demand-side marketplace integrated as a channel" is distribution, not operation.
- **vs Athlete Recruiting Marketplace (processed)** — traded subject: playing capacity/instruction vs **athletic talent** (profiles marketed to recruiting coaches); different demand side (players/parents vs recruiting programs).
- **vs Resale Marketplace family (§05.19)** — a "sports marketplace" reading as **gear resale** trades goods (item listings, condition, shipping); this Type trades playing capacity, participation, and instruction. Boundary pole unreachable (403/timeout) — seam held structurally against the processed §05.19 family; no product-specific claims. Taxonomy ambiguity flagged in STATUS.
- **vs Tee Time Booking Platform (unprocessed)** — expected domain sibling for golf (tee-sheet/round semantics vs court-hour semantics); per the established domain-sibling pattern; flag left for that pass.
- **vs Tournament Management / League Management Platforms (processed)** — those Types are competition bodies' administration systems (season loop, rosters, scheduling); here tournaments/leagues appear as **market offerings** players join and pay for (Playtomic's league join/cancel/standings; Playo's tournaments/events layer). A league body running its own registration is the admin Type; the market listing tournaments across organizers is this Type.
- **vs Fitness Class Booking (processed)** — that Type reserves participant spots in a single fitness operator's staffed class schedule; here classes/clinics are one offering vertical inside a cross-provider market. Same capability appears in both contexts; the aggregation posture separates the Types.
- **vs Outdoor Recreation Discovery (§28, unprocessed)** — discovery content without a participation transaction of record stays discovery; this Type ends in transacted engagements.
- **vs Community/social surfaces** — levels, ratings, chat, and groups serve the market's matching quality; they are market machinery, not a social-network Type.

## Historical / Market-Sample Check

- Paper-era ancestor: club notice boards for finding games and partners + facility directories with phone booking + coach listings in club halls — a two-sided sports market without software: many providers, sport-typed offerings, recorded engagements (sign-up sheets, phone bookings, prepaid lesson cards). All three L0 structures are satisfiable in paper form.
- Early-web form: venue directories with email enquiry (enquiry pole, documented in the sibling pass), forum-based game organization, coach directory sites with contact forms.
- The L0 deliberately does not require: mobile apps, multi-vertical breadth (single-vertical coaching market in-sample), player matching (absent at the coaching pole), instant booking, exclusive in-app payment (offline variant in-sample), city-density coverage, or any specific sport. A regional single-sport venue-and-coach directory with verified providers, sport-organized search, and a tracked paid booking satisfies all three structures.
- Check passes: the definition is not an artifact of the current racket-boom or super-app patterns.

## Uncertainties

- **OpenSports unreachable** (transport error ×2, matching the sibling pass) — the pure game-organizing pole is covered indirectly through Playtomic Open Matches and Playo GameTime/Playpals (both Tier-1). No claims rest on OpenSports.
- **SidelineSwap unreachable** (403 + timeout) — the gear-resale boundary is argued structurally against the §05.19 family; no product-specific assertions.
- **CoachUp's help center** (support.coachup.com) was not fetched — payment timing, cancellation windows, and payout mechanics for the coaching pole are not asserted anywhere.
- **Provider payout mechanics** (commission timing, payout cycles) are only weakly evidenced across the sample — no precise claims made; the beauty sibling's sourcing caution is mirrored here.
- **Taxonomy ambiguity**: whether the directory intends gear-resale markets under this leaf cannot be excluded a priori; the playing-economy reading is supported by the §28 habitat and both sibling passes' framing, and is the reading documented here. Flagged for STATUS.
- The seam vs Sports Court Booking is a **center-of-gravity judgment on overlapping products**; the straddle (Playtomic/Playo in both samples) is documented rather than hidden. The sibling pass already ratified the seam from its side; joint review not strictly required, but the overlap note is recorded in STATUS.

## Final Synthesis

Sports Marketplace is the operator-run two-sided market for the recreational sports economy. Its defining core is three jointly-held structures: the operator-run market over many independent sports providers (the operator aggregates supply and hosts the shared surface under market rules, but does not run the venues or deliver the coaching); sport-organized, provider-authored supply with platform verification (each offering typed by sport — venue time, a game to join, a course or lesson — authored by its provider and verified before facing the market); and the on-platform participation transaction of record (discovery by sport/location/time/level ends in a transacted engagement — booked slot, joined spot, booked lesson — held as the player's persistent record through a managed lifecycle with platform-mediated money). Around this core, mature products add provider trust machinery, player participation communities (open games, levels, ratings, chat), provider consoles, loyalty and premium layers, platform-organized offerings, and tournaments/leagues as market offerings. The Type's identity is the market: strip the aggregation and participation matching down to the single slot-reservation loop and you have Sports Court Booking; strip the sports domain and you have the Service Marketplace umbrella; change the traded subject to talent or goods and you are in Athlete Recruiting or Resale territory. The leaf stands as an independent, domain-structured sibling Type; no directory change proposed.
