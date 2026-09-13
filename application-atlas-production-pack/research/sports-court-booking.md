# Research Notes — Sports Court Booking

## Research Goal

Understand what "Sports Court Booking" software actually is from real products: the player/consumer-side application for finding and booking sports court and facility time (tennis, padel, pickleball, badminton, squash, football pitches, and similar). Determine the defining core, the standard capability set, the variant axes, and the boundary against neighboring Types — especially Racquet Club Management (operator side, processed 2026-09-09, which left an explicit seam flag for this leaf), Sports Facility Management, Tee Time Booking Platform, Amenity Booking Platform, Fitness Class Booking, and Appointment Scheduling.

## Initial Boundary

Working hypothesis going in (from the directory position and sibling passes):

- The leaf sits in §28 between Sports Facility Management and Golf Course Management / Tee Time Booking Platform / Racquet Club Management.
- The **racquet-club-management** pass (2026-09-09) characterized this leaf as: "consumer demand-side booking channel or marketplace; no operator-of-record side (member governance, programming, revenue record). A club system's own booking engine is one channel of the same system." It also assigned "anonymous court booking widget" to this territory.
- The **golf-course-management** pass characterized it as: "per-court hourly rental; no per-player pricing or round lifecycle."
- The **fitness-class-booking** pass characterized it as: "reserve time on a facility resource vs reserve a participant spot in a staffed program."
- The **sports-club-management** pass grouped it with Sports Facility Management as "capability slice / demand side | rentable-space inventory and booking channels."
- The **amenity-booking-platform** pass (2026-09-06) established the contrasting pole: closed resident/tenant booker population, building-owned amenities, building-side control surface.

Nearest neighbors: Racquet Club Management (operator side, racquet sports), Sports Facility Management (operator side, generic rentable sports spaces — unprocessed), Tee Time Booking Platform (demand side, golf — unprocessed), Amenity Booking Platform (closed residential population), Fitness Class Booking (participant spots in staffed programs), Appointment Scheduling Application (generic), Service/Sports Marketplace, Restaurant Reservation Platform (structural sibling in a different domain), Outdoor Recreation Discovery (discovery without slot inventory).

Risk going in: this leaf could collapse into Racquet Club Management (both show bookable courts) or into a generic scheduling Type. The research must decide keep-vs-merge on evidence, and must fix the demand-side/operator-side seam precisely.

## Research Questions

1. What exactly is being booked — court, venue, slot, spot in a game? How is court-time inventory presented to players?
2. Who books — anonymous users, registered players, club members? What identity does the product hold, and how does it relate to venue membership?
3. What is the booking loop — search → availability → select → pay → confirmation → play → manage/cancel? Where does it start and end?
4. Is per-booking payment definitional or common? What payment forms exist (in-app, split, wallet, pay-at-venue)?
5. Whose rules govern the booking — cancellation cutoffs, prices, access restrictions? Where does operator authority show through the demand-side surface?
6. What player-community features exist (find players, open games, buddies, ratings/levels, chat) — core, common, or optional?
7. How does the operator side relate — does every demand-side product have a sibling operator product? Where is the seam line?
8. What are the boundary judgments against Racquet Club Management, Tee Time Booking, Amenity Booking, Fitness Class Booking, Appointment Scheduling, and marketplace Types?

## Representative Products

Selected for market representation, documentation completeness, and distinct product philosophies / geographies / sport scopes:

1. **Playtomic** — global racket-sport player app + club network (padel/tennis/pickleball); marketplace + open-match community pole; Spain-origin, 50+ countries. Player help center (Zendesk) reachable — Tier-1 operational documentation.
2. **Playo** — multi-sport venue booking + community app for urban adults (India, Gulf, SE Asia); venue-booking + games + trainers pole. Freshdesk knowledge base reachable — Tier-1.
3. **GotCourts** — tennis/padel/squash/badminton player app in Switzerland/EU; single-region single-sport-family pole with municipal + resort + private-club venues. Help center (Zendesk, Playtomic-owned) reachable — Tier-1.
4. **Playfinder** — UK/Ireland sports facility booking marketplace (19 sports; pitches, courts); council/school venue pole with enquiry-based booking; operator sibling product Bookteq. Terms & conditions reachable — Tier-1 for the agency/payment model.

Rejected/abandoned: **OpenSports** (www.opensports.net — transport error then timeout; abandoned after 2 attempts per network rule). CourtReserve, EZFacility — operator-side products, out of scope for this sample (Racquet Club Management / Sports Facility Management territory).

## Sources

All fetched 2026-09-09.

- Playtomic — homepage (https://playtomic.io/); Player Help Center (https://playerhelp.playtomic.com/hc/en-gb); articles: How to make a reservation in Playtomic app; How to cancel a reservation; Cancellation Policy for Open Matches (Padel & Tennis); Private Bookings vs Open Matches.
- Playo — homepage (https://www.playo.co/); Customer Support knowledge base (https://playo.freshdesk.com/support/solutions); articles: What is Playo?; Cancellation Policies for Pay & Join/GameTime Activity; I have made full payment at the venue… ('payment to be made' in the app).
- GotCourts — homepage (https://www.gotcourts.com/en/); Help Centre (https://playtomic-gotcourts.zendesk.com/hc/en-gb); articles: How can I book a court?; How do I become a member of a private club?; How can I cancel a reservation?; Who gets the bill if I play with a guest?
- Playfinder — homepage (https://www.playfinder.com/); Terms and Conditions (https://www.playfinder.com/terms).

## Product A — Playtomic

### Key observations (evidence layer A unless noted)

- Positioning: "Find courts and players near you… Find matches and courts worldwide." Self-described "world's leading App for racket sport players and clubs." Player side (book padel/tennis/pickleball courts, find a club) is distinct from club side (Playtomic Manager — separate operator product).
- Player value loop (homepage): Find (create private matches with friends, make them public to find partners, or search active matches nearby to join) → Book → Join the community.
- Reservation flow (help center, Tier-1): Home → "Book a court" → select sport → choose where (place, club name, postcode) → select date and time → select court and duration → choose pay-your-part (split payment) or pay everything — the club's cancellation policy is displayed on the same screen → Continue payment → review → payment method → Pay. Prices are "set individually by each club." Booking can be simulated up to the payment step without charge.
- Two booking forms (help center, Tier-1): **Private booking** — you are the "owner," responsible for the reservation, pay full or split, follows the club's cancellation policy, won't auto-cancel if players don't join; duration (60/90/120 min common) is configured per club. **Open match** — reserve and pay only your spot, to challenge new players from the community; online payment required; if not all players enroll the system automatically cancels and refunds; courts are automatically reserved based on players joined (2 players → if >12h to match time; 3 → >4h; 4 → always). A private booking can be converted to an open match; not vice versa.
- Cancellation (help center, Tier-1): possible in-app "as long as it's within the club's cancellation policy timeframe"; the club's policy is displayed on the booking screen; outside the policy, cancellation is not possible and Playtomic "will not be able to cancel or reschedule" — contact the club (weather exceptions are the club's call). Refunds to original payment method; processed immediately, appears in 2–15 business days. For private bookings the refund excludes Playtomic's service fee and cancellation fee.
- Money instruments: card payments; **Club Wallet** (instant refunds for cancelled open matches); service fee + cancellation fee retained by the platform on private bookings; Premium subscription tier exists (Subscriptions & Offers category).
- Community layer: open matches (sign-up, request a spot, gender of match, casual vs competitive), built-in chat with registered players, player level system ("How the Playtomic level system works"), match results entry with validation (results auto-confirm after 24h; players have up to 7 days to add/update), reservation history and match stats in the app, share booking link, add to calendar.
- Club linkage: players may need to "Accept Club Legal Documents"; club-configured durations, prices, cancellation policies.
- Scale claims (homepage, third-party quote): "connects 4 million players with 5500 partner clubs in over 52 countries" (Forbes quote on vendor page — treat as vendor-published, layer A for existence of network, not for precision).

## Product B — Playo

### Key observations

- Positioning (help center, Tier-1): "Book Venues, Meet Players, Train, and Play" — "world's largest online sports platform designed for urban adults." Offers: 1) Discover and Book Sports Venues (badminton court, cricket turf, swimming pool — "locate and reserve sports facilities near you"), 2) Find Playpals and build a sports network (join games, host your own), 3) Track progress and rate Playpals, 4) Sports discussions, 5) Find coaching academies and trainers, 6) Tournaments and events.
- Site navigation: PLAY (games) / BOOK (venues) / TRAIN (trainers). Popular sports: badminton, football, cricket, swimming, tennis, table tennis. City landing pages (Bangalore, Chennai, … Dubai, Qatar, Australia, Oman, Sri Lanka).
- Venue booking features (help center): "Book hourly slots and enjoy exclusive discounts. Check amenities, reviews, and ratings before booking. Easily cancel or reschedule games." Knowledge-base sections: Venues: Places to Play (search by venues, contact venue management, rate a venue); Booking Venues & Experiences (book more than one hour in advance, multiple days in one transaction, offline bookings); Rescheduling (change court after booking, transfer booking between venues); Cancellation & Refunds (12 articles; "When can a booking not be cancelled?"; "I am not able to cancel my booking 1-2 hours prior to a slot").
- Cancellation policy (Tier-1, Pay & Join/GameTime): GameTime activity — user can revoke up to 2 hours before; 100% of slot price refunded, convenience fee not refunded; if Playo cancels, both refunded. Regular Pay & Join — host cancellation retires the user with full gross refund incl. convenience fee. Venue bookings carry venue-set cutoffs (1–2 hour boundary issues documented in FAQ titles).
- Payment model (Tier-1): in-app payment is what makes a booking a "Playo Booking" — "Only partial/complete payments made through the Playo app will be trackable as a 'Playo Booking'." Paying at the venue = "offline booking"; confirmation/rescheduling/cancellation for those must be taken up with the venue directly. Saved cards; receipts for past/upcoming bookings; transaction identification on bank statements.
- Community layer: Playpals (find players by skill set, host activities, leave-by rules), Groups/Squad, Playostats & player ratings (rate Playpals, overall rating calculation), GameTime ("Playo organizes guaranteed games for you. Just show up and play"), Karma loyalty points for booking and joining, gift cards.
- Trainer layer: find certified coaches/trainers and academies; trainer self-registration.
- Operator side: "Partner with us" venue onboarding.

## Product C — GotCourts

### Key observations

- Positioning (homepage): "Find courts near you and connect with the world's largest racket player community" — Tennis, Padel, Squash and Badminton. "Book your next game or practice session with just two taps. Court availability is always up-to-date, and each booking is promptly confirmed – no more endless email chains or voicemails."
- Venue mix (homepage): featured clubs include a municipal sports office (Zürich, "from 15 CHF"), a resort, and commercial centers — the supply side spans public/municipal to private. "Want to see your own club here? Find out how to get listed."
- Booking flow (help center, Tier-1): log in → "Courts" in main menu → select a facility or search for a court in your area → enter search info → the club's **reservation table** appears → reserve units "highlighted in green" → click desired court at desired time → dialog box → "Reserve."
- Club membership gating (help center, Tier-1): "In order to book courts in private clubs you have to be member of the club." Membership is requested from within the player app (club profile → "Send membership request" → club administrator answers; or profile → membership → search club). The player app mediates the membership relationship; the club governs access.
- Cancellation (help center, Tier-1): self-service from the booking table → reservation details → "Cancel reservation"; "every club can decide how many minutes before the beginning of the reservation it is still allowed to cancel it" — outside the window, contact the club by phone. Reschedule and waiting-list machinery exist ("Where do I find all my waiting list entries?"; notifications when a waited slot opens).
- Guest machinery (help center, Tier-1): "How can I play with a guest?"; "Who gets the bill if I play with a guest?" — "The bill will be sent to the player that booked the court. The club sets the price for the court."
- Money (help center): Payment Services section — online payment, deposit credit card, available payment services. Booker pays; club sets price.
- Community layer: Buddies (search, invite a buddy to one of my reservations, private messages), player network (partner matching by criteria/rank, block someone), Activities marketplace ("create and join tennis activities near you… challenge them for a friendly match or find a sparring partner"), favorites.
- Competition layer: GotCourts Club-Championship (leaderboards, point calculation, report results) and GotCourts League (seasons, rating, counts toward Swiss Tennis Ranking) — competition built on top of bookings.
- Surfaces: iOS/Android apps + web application. Operator side: "For Clubs & Centers" (GotCourts' booking system for clubs); help center is co-branded with Playtomic (GotCourts is Playtomic-owned — vendor consolidation noted, products remain distinct surfaces).

## Product D — Playfinder

### Key observations

- Positioning (homepage): "Book sports pitches and courts in the UK and Ireland." Flow framing: Find sports facilities → Book ("Book online or enquire") → Play your game. 19 sports in London; facility counts published (3,250 football pitches, 3,050 tennis courts, 1,050 badminton courts, 390 squash courts — vendor-published).
- Supply side: councils (Waltham Forest, Southwark, Bedford), school academy trusts, leisure operators as venue partners. Operator sibling product: **Bookteq** — "the complete facility booking software for operators such as councils, schools and sports clubs. Manage real-time bookings, payments and customers."
- Booking modes: instant online booking where integrated; **enquiry-based booking** otherwise ("Connect with the venue through the enquiry form to make an online booking"); Playfinder provides "Operational Support — We manage all email and phone enquiries, as well as invoices and block booking waiting lists" for venues.
- App features (homepage): "Instantly book sports facilities across the UK; Split Payments with your friends using PaySplit; Keep track of upcoming bookings; Favorite nearby venues for easy booking."
- Agency/payment model (Terms, Tier-1): "We are an Agent that act on behalf of suppliers, operators or owners of sports venues, facilities, clubs…" — "When you make a booking, you are entering into a contract with suppliers via … 'Playfinder', not with My Local Pitch Limited itself." "All refunds and cancellations are subject to the Facility's terms. In general, there are no refunds granted for the cancellation of bookings." If a paid slot becomes unavailable, the platform finds an alternative or refunds within 2 business days; the Facility may cancel or move a booking. "All fees are due upon a booking being placed"; payments via Stripe; on cancellation "Playfinder may withhold part of the payment as a commission." PaySplit: payment may be reserved but not taken for up to 7 days. Account = email + password; account used "to make bookings and payments."
- No deep social/community layer documented on the consumer side (no open-match marketplace or buddy machinery observed) — the booking loop stands without it.

## Cross-product Comparison

| Aspect | Playtomic | Playo | GotCourts | Playfinder |
|---|---|---|---|---|
| Sport scope | racket family (padel/tennis/pickleball) | multi-sport (badminton, football, cricket, tennis, swimming, …) | racket family (tennis/padel/squash/badminton) | 19 sports incl. pitches (football) and courts |
| Supply side | partner clubs (commercial padel/tennis centers) | commercial venues/turfs/pools | municipal offices, resorts, private clubs, commercial centers | councils, schools, leisure operators, clubs |
| Unit booked | court slot (private booking) or spot in an open match | venue hourly slot; spot in GameTime/Pay & Join | court unit in club's reservation table | pitch/court slot (instant or enquiry) |
| Discovery | search by place/club/postcode + sport + date/time | location → nearby venues; sport & city pages | search form + map; favorites | location + sport search; city landing pages |
| Availability surface | club availability, club-configured durations | venue slot grids, amenities/reviews | reservation table, green bookable units | real-time where integrated; enquiry otherwise |
| Booking forms | private booking vs open match | venue booking; GameTime; Pay & Join | court reservation; activities; buddy invites | direct booking; enquiry booking |
| Payment | in-app pay-all or split; Club Wallet; club-set prices; service fee | in-app payment defines the tracked booking; pay-at-venue = offline; Karma | online payment, stored card; bill to booker; club sets price | Stripe at booking; PaySplit; commission withheld on cancellation |
| Cancellation authority | club's policy timeframe enforced in app; outside → club | venue-set cutoffs; GameTime 2h platform rule | club decides minutes-before cutoff | facility's terms; generally no refunds |
| Player-side record | reservation history, match stats | bookings in app, receipts | active and past reservations, waiting lists | "Manage my Bookings", upcoming bookings |
| Community layer | open matches, level system, chat, results | Playpals, groups, ratings, GameTime | buddies, player network, activities, championships/league | minimal (PaySplit with friends) |
| Operator sibling | Playtomic Manager | Partner with us (venue onboarding) | GotCourts for Clubs & Centers | Bookteq |
| Identity | player account; club legal-document acceptance | player account (registration free) | player account; membership request to private clubs | email+password account |

**Cross-product commonalities (evidence layer B):** all four put a player-facing, searchable bookable inventory (venues × courts/slots) at the center; all four hold the player's reservations as an ongoing record (upcoming + history); all four enforce venue-set prices and cancellation policies through the demand-side surface; all four settle per-booking money in some form (in-app payment dominant; pay-at-venue and enquiry variants exist); all four are paired with a sibling operator-side product; none puts membership governance or operator revenue reporting at the center.

**Layer-C canonical inference:** the Type is the demand side of court-time booking — the player's loop from discovery to a held, paid, self-managed reservation — with the venue as a third party whose terms govern. The operator side (inventory of record, member governance, revenue record) belongs to the neighboring management Types.

## Canonical Abstraction Hierarchy

### Level 0 — Defining Invariant

Three jointly-held structures:

1. **Player-facing bookable court-time inventory** — sports venues/clubs held with their courts and bookable time slots, surfaced for player discovery, searchable by location, sport, and time, with availability kept current (real-time where integrated; enquiry channel where not). Remove → a venue directory/listings, or an operator calendar players cannot see.
2. **The court reservation as the player's booking of record** — a player (organizing a party, or taking a spot in a shared game) holds a specific court for a specific slot; the reservation persists in the player's own record (upcoming + history) and is self-managed — rescheduled or cancelled under the venue's rules — through to the played slot. Remove → listings with nothing to book, or a bare form widget with no player-side memory.
3. **The mediated third-party venue relationship** — the venue is not the player's organization: its prices, cancellation policy, and access rules govern the booking; the platform mediates discovery → booking → payment → arrival; per-booking settlement is the dominant completion (in-app payment, split among players, wallet, or pay-at-venue variants). Remove → the venue's own system of record (Racquet Club Management / Sports Facility Management territory).

Jointly-held load-bearing: 1 alone = venue directory; 2 without 1 = bare booking widget; 3 without 1+2 = review/discovery surface; 1+2 without 3 = the venue's own booking channel (operator side); 1+3 without 2 = search with no reservation.

### Level 1 — Common Mature Structure

- search/discovery by location, sport, date/time; venue pages with photos, amenities, reviews/ratings
- real-time availability grids with instant confirmation; club/venue-configured slot durations
- per-booking in-app payment (card/wallet), split payment among players
- self-service cancellation/reschedule under venue-set cutoffs; refunds per policy
- the player's booking record (upcoming + past), confirmations, reminders/notifications, calendar export
- favorites
- player profiles with skill self-description; ratings/levels
- find-players machinery: open games/matches, activities, buddies, join-a-game
- chat with co-players
- waiting lists (GotCourts documented; Playfinder block-booking waiting lists on operator side)
- guest play with booker-pays billing (GotCourts)
- venue loyalty/rewards (Playo Karma)
- venue reviews/ratings submitted by players (Playo)

### Level 2 — Variant / Optional Structure

- sport scope: single-sport-family vs multi-sport vs pitches+courts breadth
- geography/market shape: city-network density models (India, UK, Switzerland, Spain/global)
- booking mode: instant vs enquiry-based (Playfinder pole)
- social depth: none → buddies → open-match marketplace with auto-fill/auto-cancel logic
- competition layer: club championships, leagues, level/rating systems tied to bookings
- monetization: commission/service fee/convenience fee; premium subscription; loyalty economy
- venue mix: municipal, resort, private club, school/council, commercial center
- training/coaching discovery attached to the same account
- membership linkage: where venues are private clubs, the platform mediates membership requests/verification rather than governing membership itself

### Level 3 — Vendor-specific Structure

- Playtomic: open-match auto-reservation thresholds (2 players >12h / 3 >4h / 4 always); auto-cancel + refund of unfilled open matches; private→open conversion (one-way); level system with result-validation windows (24h auto-confirm, 7-day entry window); Club Wallet instant refunds; Premium subscription; club legal-document acceptance flow
- Playo: GameTime (platform-organized guaranteed games) with 2-hour revoke rule and convenience-fee economics; Playostats rating machinery; Karma loyalty; "offline booking" category for pay-at-venue
- GotCourts: Club-Championship and GotCourts League (Swiss Tennis Ranking linkage); ball-machine court booking; membership-request workflow to private clubs
- Playfinder: PaySplit with 7-day payment reservation; enquiry-managed bookings with vendor-run operational support; Bookteq pairing

## Vendor-specific Findings

- Playtomic's open-match auto-reservation/auto-cancel logic and level system are product-specific machinery (L3) — the underlying concept (spots in shared games that convert into court reservations) appears in weaker forms elsewhere (Playo GameTime/Pay & Join, GotCourts activities) and is held as Common, not defining.
- Playo's "offline booking" category shows the platform's own boundary: a booking not paid in-app is not a platform-tracked booking — evidence that in-app payment is the platform's operating definition, while the Type-level invariant remains the reservation itself.
- GotCourts' membership-request workflow shows how the demand side defers to operator governance without holding it: the club answers the request; the app only mediates.
- Playfinder's agency terms make the third-party posture legally explicit ("entering into a contract with suppliers via … Playfinder") — the clearest statement of the demand-side mediation model in the sample.
- Vendor consolidation: GotCourts is Playtomic-owned (shared help-center infrastructure) but remains a distinct product surface; treated as one vendor with two sampled products only in the sense of shared ownership — evidence from each is still product-specific.

## Boundary Findings

- **vs Racquet Club Management (processed)** — the primary seam, ratified from this side: RCM is the operator's system of record (court-time inventory of record, member governance, programming, play-and-revenue record); Sports Court Booking is the player's demand-side loop with the venue as third party. A club system's own booking engine is one channel of the operator system; a booking platform's center is the player loop. Remove the operator-of-record side from RCM → you get this Type's surface; add operator governance/revenue to this Type → it becomes RCM (or Sports Facility Management for generic spaces). DISCHARGES the racquet-club pass's forward flag from this side.
- **vs Sports Facility Management (unprocessed)** — proposed seam for that pass: operator side for generic rentable sports spaces (halls, rinks, fields) vs this leaf's demand side. Flag left.
- **vs Tee Time Booking Platform (unprocessed)** — the golf demand-side analog; proposed seam: per-player green fees / round / tee-sheet semantics vs per-court hourly rental. Flag left.
- **vs Amenity Booking Platform (processed)** — amenity booking serves a closed resident/tenant population booking building-owned shared facilities under a building rulebook; this Type serves an open public player population booking third-party commercial/municipal sports venues. The booker population and the venue relationship are the discriminators.
- **vs Fitness Class Booking (processed)** — that Type reserves a participant spot in a staffed, scheduled program; this Type reserves time on a facility resource. Both appear as sibling capabilities inside some products (the fitness pass documented facility-rental modules inside class-booking products).
- **vs Appointment Scheduling Application** — generic time-slot booking lacks sport-typed inventory, court semantics, per-venue price/policy mediation, and the player community; the court/facility domain semantics are part of this Type's identity (consistent with the directory carving out domain booking leaves: Tee Time, Amenity).
- **vs Service/Sports Marketplace** — a marketplace aggregates many verticals with discovery as the center; here the center is the court-time booking loop itself. Playtomic/Playo carry marketplace features, but the booking loop is the spine.
- **vs Restaurant Reservation Platform** — structural sibling (reserve time on a resource at a third-party venue) in a different domain; no overlap in inventory semantics.
- **vs Outdoor Recreation Discovery** — discovery-first without slot inventory or reservations.
- **Floor test**: a venue's own embedded booking widget with no player-side account/memory is a channel of the operator's system, below this Type's bar; the Type's floor is the player-side booking loop with the player's own booking record.

## Historical / Market-Sample Check

- Paper-era ancestor: the demand side was phoning the club or signing a reservation sheet the club kept — no software Type; the conceptual loop (learn availability → reserve → pay → play) is the ancestor.
- Early web era: club websites with member booking portals and municipal online booking forms — these are operator-side channels (1+2 without 3), not this Type's center of gravity.
- The sampled Type — third-party player-side booking platforms — is the current dominant form, but the L0 deliberately does not require: marketplace aggregation (single-venue demand surfaces satisfy the loop), mobile apps (web apps in-sample), social layers (Playfinder pole), in-app payment (pay-at-venue variant), or racket-sport specificity (pitches and multi-sport in-sample). A regional single-sport booking portal with player accounts, real-time availability, and self-service cancellation satisfies all three L0 structures.
- Check passes: the definition is not an artifact of the padel-boom marketplace pattern.

## Uncertainties

- **Free-court pole not sampled**: all sampled venues price their courts ("from 15 CHF" municipal pole is the cheapest observed). Whether a materially free-court booking population exists inside this Type is unverified; per-booking payment is therefore held as dominant-common, not definitional, but the free-pole variant is unconfirmed.
- **Anonymous/guest checkout**: all sampled products require accounts for booking. Whether any in-type product supports anonymous booking is unverified; the racquet-club pass's "anonymous booking widget" phrasing was used to locate the demand side, not to assert anonymity inside this Type.
- **OpenSports** could not be fetched (2 failures); the social/game-organizing pole is covered indirectly through Playtomic open matches and Playo GameTime/Playpals.
- Precise numeric parameters observed in help centers (Playtomic's 24h/12h/4h open-match rules, 2–15 business-day refunds, Playo's 2-hour GameTime revoke, GotCourts' club-set cancellation minutes) are product-specific and were kept out of the final document except where a concrete example materially aids understanding — and there attributed as product behavior, not Type behavior.
- Mindbody-class suite poles and operator-side products (CourtReserve, EZFacility) were not sampled — out of scope by design; their booking modules are channels of operator systems.

## Final Synthesis

Sports Court Booking is the player-side application type for reserving sports court and facility time. Its defining core is three jointly-held structures: the player-facing bookable court-time inventory (venues × courts × slots, searchable, availability current); the court reservation as the player's booking of record (held slot, party or shared-game spot, persistent in the player's record, self-managed under the venue's rules); and the mediated third-party venue relationship (venue-set prices/policies govern; the platform mediates discovery → booking → payment → arrival, with per-booking settlement dominant). Around this core, mature products add search-and-discovery richness, in-app and split payment, self-service cancellation with venue-set cutoffs, player profiles and ratings, find-players/open-game machinery, chat, waiting lists, loyalty, and — in some products — competition layers. The Type's identity is the demand side: strip the operator-of-record side (inventory of record, member governance, revenue record) and you have this Type; add it and you are in Racquet Club Management / Sports Facility Management territory. The leaf stands as an independent Type; no directory change proposed.
