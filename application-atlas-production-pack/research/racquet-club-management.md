# Research Notes — Racquet Club Management

## Research Goal

Understand what "Racquet Club Management" software actually is from real products: the operator-side system used to run racquet-sport clubs and facilities (tennis, pickleball, padel, squash, racquetball, table tennis). Determine the defining core, the standard capability set, the variant axes, and the boundary against neighboring Types (Golf Course Management, Sports Court Booking, Sports Club Management, Sports Facility Management, League/Tournament Management, Amenity Booking, Gym/Fitness Management).

## Initial Boundary

- Hypothesis: operator-side system of record for a racquet club — court-time booking + membership + programming (lessons/clinics/leagues) + pro scheduling + billing.
- Nearest neighbors: Golf Course Management (the golf analog, already documented — its pass recorded this leaf as "membership + booking, court-based hourly booking, no tee-time/round semantics"), Sports Court Booking (consumer demand side), Sports Club Management (membership-org-first, any sport), Sports Facility Management (generic rentable spaces), Amenity Booking Platform (residential shared facilities), League Management / Tournament Management (competition machinery), Gym Management / Fitness Studio Management (member billing + classes, no courts).
- Risk: this leaf could collapse into "Sports Court Booking" or "Sports Club Management". The research must decide keep-vs-merge on evidence.

## Research Questions

1. What is the court-time inventory model (courts, slots, intervals, prime times, indoor/outdoor)?
2. What is the reservation lifecycle and who books (member self-service vs front desk)?
3. How do member/customer accounts gate booking (privileges, windows, fees, counts)?
4. How does programming (lessons, clinics, programs, leagues, tournaments, events) occupy court inventory and generate revenue?
5. How are pros/coaches managed (schedules, lesson packages, pay)?
6. How does money flow (court fees, guest fees, POS, member billing, statements)?
7. What interfaces exist (admin console, member portal/app, front desk, kiosk/TV)?
8. What rules matter (booking windows by member type, prime-time rules, cancellation/no-show)?
9. Where are the boundaries vs neighboring Types?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| **RacquetDesk** (US; formerly 10sPortal, founded 2007) | racquet-specific club suite | names the category ("Racquet Sports Club Management"); serves tennis/pickleball/padel/racquetball/table tennis/squash; feature/pricing page enumerates the club-suite capability set |
| **Playtomic Manager** (Spain; global) | marketplace-first, padel-led | club tools embedded in the world's largest racquet player network (6,700+ clubs, 25,000+ courts claimed); pay-and-play pole; Academy product line documents the coaching leg |
| **Jonas Club Software — Court Booking module** (Canada) | private-club suite embedding | court booking as one module of a multi-amenity private-club suite (golf, F&B, spa, marina); documents member/guest/privilege machinery at Tier-1 depth |
| **SportyHQ** (global; squash/tennis/badminton heritage) | competition-first | leagues/ladders/rankings/tournaments as the center, with court bookings + membership attached; governing-body solutions |

Rejected/abandoned samples (source-access limitations, see Sources): CourtReserve (leading US tennis/pickleball SaaS — all domains 403/timeout), Club Locker (US Squash — JS-rendered SPA, no content), EZFacility (403/timeout), PlayByPoint (403), MyCourts/Wosofe/BookMyCourt/CourtMaster (transport errors), CourtHive (JS-rendered). Skedda fetched but is a generic workplace space-booking product — used only as boundary context, not a representative product.

## Sources

Fetched 2026-09-09 (official vendor pages):

- RacquetDesk — homepage (https://racquetdesk.com/), tennis vertical page (https://racquetdesk.com/tennis-software/)
- Playtomic — homepage (https://playtomic.io/), Playtomic Manager (https://playtomic.io/playtomic-manager), Playtomic Academy (https://playtomic.com/academy)
- Jonas Club Software — homepage (https://www.jonasclub.com/), Court Booking module page (https://www.jonasclub.com/court-booking/)
- SportyHQ — homepage (https://www.sportyhq.com/), Court & Facility Booking feature (https://www.sportyhq.com/features/facility-bookings), Membership Management feature (https://www.sportyhq.com/features/membership-management)
- Boundary context: Skedda homepage (https://www.skedda.com/) — generic space booking, sports-facility use case spun off to a separate product (AllBooked)
- Neighbor pass: research/golf-course-management.md + applications/golf-course-management.md (boundary recorded from the golf side)

Evidence layers used below: **A** = directly observed on an official page of a specific product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + Type-boundary reasoning.

## Product A — RacquetDesk

### Key observations (Layer A unless noted)

- Self-labels "Racquet Sports Club Management"; "cloud-based sports club management software provides 24/7 access via computer or our mobile app".
- Feature enumeration (homepage + pricing tiers): online sports club booking system; point of sale; **group, lesson, and open-court management**; electronic billing; member and employee management; payroll; **court/pro lesson reservations**; social/player matching; white label; branded mobile app; inventory management/print labels; kiosk; **stringing**; **lesson package management (unit tracking)**; **advanced player ratings management**; seasonal court management (add-on); e-check/bank draft; time & attendance.
- "Online scheduling for open-court, lesson, and group play, with real-time availability. Our customer-facing court scheduling software saves your staff members time and effort."
- Tennis page: "Group, program, lesson, event, seasonal, and open-court management"; online court reservation; "social features, including group games, open play, player matching, tournaments, leagues, in-app networking"; "client self-service"; web and mobile app registration; autobilling; real-time performance and revenue tracking; automated reporting.
- "Unlimited members, employees, and courts per facility" — courts are a first-class countable resource.
- Pricing is per facility, not per member — the club is the customer entity.
- Integrations: WorldPay embedded payments, marketing automation, tennis video streaming, and a third-party **league & tournament management** product (Swish) — competition machinery is integrated out, not native.
- Heritage: formerly 10sPortal (2007) — a decade-and-a-half-old racquet-specific lineage.

## Product B — Playtomic Manager

### Key observations (Layer A unless noted)

- Self-labels "racket sports club management platform"; club-side product of a two-sided network (player app + manager). Network claims: 6,700+ clubs, 25,000+ courts, 1.7M monthly active players, 4M registered users, 1.5M monthly transactions, 63+ countries.
- Feature set: "smarter booking system — automate reservations, avoid double bookings, and keep your courts full"; **Open Matches** ("fill your off-peak hours with the help of the Playtomic player app. Users can join matches on their own, with no extra work for you"); "create leagues, tournaments and classes with just a few clicks"; integrated payments "within the manager tool or in the player app"; "coach discovery & private lesson booking — players find, connect with, and book lessons with your coaches directly through the app"; real-time analytics (occupancy, cancellations, busiest courts); billing; reporting.
- **Academy** (coaching product line): **Courses** (multi-session recurring programs, "linked to coach and court availability", custom player levels & pricing), **Clinics** (one-off group sessions, level-based filtering), **Private classes** (1:1 coach-player, "flexible coach availability settings", player-led booking, custom pricing per coach). "All discoverable and bookable in the Playtomic player app… managed entirely through Playtomic Manager." "Turn off-peak hours into structured training sessions."
- Player app side: find courts/players, book, leveling system, match stats, reservation history — the club's inventory is exposed to a consumer marketplace.
- Testimonials name occupancy ("court occupancy is up"), multi-site operators, booking-pattern analytics.
- Playtomic help center for clubs was not reachable (transport error) — operational parameter detail (cancellation windows, no-show mechanics) unverified for this product.

## Product C — Jonas Club Software (Court Booking module)

### Key observations (Layer A unless noted)

- Private-club suite: Golf & Tee Times ("The Sheet"), F&B (POS/KDS/online ordering/dining reservations/inventory), Events & Catering, **Booking & Scheduling (Courts, Spa, Classes, Appointments)**, CRM & Member Management, Member Engagement, Finance & Back Office (Accounting, Billing, Payroll), Operations (Marina, Hotel), Member Digital (websites, mobile app).
- Court Booking module page: "Court Booking for Tennis & Racquet Clubs — the Court Booking application allows your members to conveniently book any court or facility. Meeting rooms, Tennis courts, swimming lanes, golf simulators, pickleball, you name it."
- **Four-step staff booking flow**: 1) "Select the available time and booking type (single, double, lesson, etc.)" 2) "Select an existing member/guest, or add a new guest for the booking" 3) "Assign various resources such as equipment or instructors to the booking" 4) "Save the booking". "Staff to easily manage bookings and **bill members directly once a booking has been confirmed**"; "Members will receive booking confirmation upon booking."
- **Privileges**: "Set predetermined booking rules based on member status, dues category or even by specific member. These privileges can be based on: court/facility fees, advanced booking allowance, number of bookings."
- **Court control**: "Create custom time intervals. Access and record detailed member/guest preferences. Create booking time slots specific to court and day of week."
- Amenities attachable to a booking: "Add amenities such as a ball machine to their booking"; search "by date and court type".
- Mobile app mockup surfaces: "Court Reserved — Sunday · 10:00 AM · Court 3", guest passes, statements, chit-style member charging (suite context).

## Product D — SportyHQ

### Key observations (Layer A unless noted)

- Self-labels "web-based sports competition and membership platform… to power sports facilities and governing bodies, run competitions, manage membership". Racket-sports heritage (squash/tennis/badminton); claims 250,000 users, 50+ countries, 4,000 facilities.
- **Court bookings feature page** (richest operational detail in the sample):
  - Courts as **"assets"**: "add and group all of your courts, rooms or anything else that you'd like to accept reservations for. Each court (or 'asset') can be setup with flexible booking increments that can change for each day of the week. Set **prime & non-prime times** and configure a full range of booking permissions."
  - **Booking types**: "Playing With [Name]" (member-to-member; "friendly matches don't count towards rankings but are recorded under player stats" — challenge matches do count toward rankings); "Solo Practice" ("As a facility you have full ability to allow this type of booking or only allow it during certain times"); "Still Looking For Player" ("book a court notifying other members they are looking for a match. Members who see this can join the match with a single click").
  - **Booking payments**: "rates can be customized based on the time of day, length of booking and the booking type being selected."
  - **Booking policies**: "add as many membership types, with accompanying policies, as you need… from restricting juniors during certain hours, to managing prime time hours."
  - **Booking history**: "go back and search each day individually as well as run detailed reports for any dates you select."
  - **Block bookings**: "book off and group hundreds of courts with the click of a button… recurring event? Simply click the day(s)."
  - **TV display mode**: "displaying current court and facility bookings in real time."
  - **Booking statistics**: "bookings by type, bookings by day of the week, court usage, bookings by asset, bookings by sport, by member demographics."
- **Membership management feature page**: CRM for players/coaches/officials/contacts; players carry "affiliation status, membership type, **playing privileges**"; member self-service login ("signing up and managing event entries, recording their match results"); auto-issued membership IDs; membership syncing up regional/national bodies; "membership payments on auto-pilot" (payment plans, auto-recurring or fixed-date periods; "as soon as your members complete payment, their membership status automatically updates"); user agreements; membership analytics.
- Competition machinery native: tournaments, team/solo/box leagues, ladders, rankings & sanctioning.

## Cross-product Comparison

| Structure | RacquetDesk | Playtomic Manager | Jonas (Court Booking) | SportyHQ | Layer |
|---|---|---|---|---|---|
| Courts as identified bookable units ("unlimited courts per facility" / 25,000+ courts network / "any court or facility" / courts as "assets") | ✓ | ✓ | ✓ | ✓ | B |
| Time-slot inventory with operator-configured intervals & per-court/per-day rules | ✓ (seasonal court mgmt) | ✓ (booking system) | ✓ ("custom time intervals… slots specific to court and day of week") | ✓ ("flexible booking increments… each day of the week") | B |
| Court reservation by a named party; booking type encodes play shape | ✓ (court/pro lesson reservations; open-court) | ✓ (bookings; open matches) | ✓ ("single, double, lesson, etc."; member/guest selection) | ✓ (singles/doubles/solo/still-looking types) | B |
| Club-side accounts for bookers with governed access | ✓ (member management) | ✓ ("manage your customers") | ✓ (member status/dues category privileges) | ✓ (membership types + policies + playing privileges) | B |
| Charges raised against bookings/accounts | ✓ (POS + electronic billing + autobilling) | ✓ (integrated payments in-app) | ✓ ("bill members directly once a booking has been confirmed") | ✓ (booking payments by time/length/type) | B |
| Programming occupying court inventory (lessons/clinics/programs/events) | ✓ (group/program/lesson/event/open-court) | ✓ (Academy courses/clinics/private classes "linked to coach and court availability") | ✓ (lesson booking type; class scheduling module) | ✓ (leagues/tournaments + event registration) | B |
| Pro/coach management | ✓ (pro lesson reservations, lesson packages, payroll) | ✓ (coach discovery, private classes, coach availability) | ✓ (instructors assigned to bookings) | ✓ (coach records/credentials) | B |
| Member self-service booking surface (web/app) | ✓ (customer-facing scheduling, branded app) | ✓ (player app) | ✓ (member booking + ClubHouse app) | ✓ (bookings app, member login) | B |
| Utilization/occupancy & revenue analytics | ✓ (real-time performance and revenue tracking) | ✓ (occupancy, cancellations, busiest courts) | ○ (suite reporting) | ✓ (booking statistics, court usage) | B |
| Social/player matching (open play, "looking for player", open matches) | ✓ (social/player matching, open play) | ✓ (Open Matches) | — | ✓ (Still Looking For Player) | B (3/4) |
| Guest machinery (guest in party, guest passes/fees) | ○ (implied) | — | ✓ (member/guest selection, guest passes) | ✓ (guest booking type) | B (2–3/4) |
| Prime/non-prime time differentiation | ○ | ○ | ○ | ✓ (explicit) | A→B (1 explicit; others implied by fee-by-time) |
| Tournaments/leagues | ✓ via integration (Swish) + in-app features | ✓ native | ○ (suite event mgmt) | ✓ native + rankings/sanctioning | B |
| Ratings/ladders/rankings | ✓ (advanced player ratings management) | ✓ (leveling system) | — | ✓ (rankings, ladders, sanctioning) | B (3/4) |
| POS / pro shop / stringing / inventory | ✓ (POS, stringing, inventory) | — | ✓ (suite POS) | — | B (2/4) |
| Membership dues billing / statements / autobilling | ✓ (autobilling, electronic billing) | ○ (billing; pay-and-play pole) | ✓ (suite billing, statements, chits) | ✓ (membership payments on auto-pilot) | B (3/4; Playtomic pole thinner) |
| Payroll / time & attendance | ✓ | — | ✓ | — | B (2/4) |
| Kiosk / TV display surfaces | ✓ (kiosk) | — | ○ | ✓ (TV display mode) | B (2/4) |
| Marketplace distribution of club inventory | — | ✓ (player app network, open matches) | — | ○ (public event explore) | A (1/4 — Playtomic-pole) |
| Multi-amenity suite embedding | — | — | ✓ (golf/F&B/spa/marina) | — | A (1/4 — suite pole) |

Legend: ✓ observed (Layer A on that product); ○ implied/partial; — not observed.

## Canonical Model

### L0 — Defining Invariant

The racquet club's operator-side system of record whose defining core is exactly four jointly-held structures:

1. **The court-time inventory as the club's playing capacity of record** — the club's courts held as individually identified bookable units laid out over dated time slots, with operator-configured intervals and per-court/per-day rules (prime/non-prime distinctions common). Remove → a member CRM or generic scheduler with no playing-capacity model.
2. **The court reservation as the booking of record** — a dated court slot held by a named party (one or more players, commonly with guests), the booking's type encoding the play shape (singles/doubles/lesson/solo practice/open play), moving through a booked → played / cancelled / no-show lifecycle. Remove → an empty capacity calendar.
3. **Identified bookers under governed access** — the people who book are held as club-side accounts (members/customers) whose status carries booking privileges — advance windows, eligible times, fee bases, booking counts — so access to court time is governed, not anonymous. Membership is the dominant realization; pay-and-play customer accounts the variant. Remove → an anonymous court booking widget (Sports Court Booking territory).
4. **The play-and-revenue record** — court usage and the charges raised against it (court fees, guest fees, lesson/program revenue) accumulate as the club's operating record, feeding utilization and revenue reporting. Remove → a reservation board with no management memory.

Jointly-held load-bearing:
- 1 alone = capacity calendar / generic room booking
- 2 without 1 = appointment list
- 3 without 1+2 = member CRM
- 4 without 1–3 = POS/reporting shell
- 1+2 without 3 = anonymous booking widget
- 1+2+3 without 4 = booking board, the "management" gone

### L1 — Common Mature Structure

- Member self-service booking (web/app) with real-time availability; booking confirmations
- Booking types encoding play shape (singles/doubles/lesson/solo/open play)
- Guest machinery (guests in the party, guest passes/fees)
- Programming: lessons, clinics, programs, leagues, tournaments, events occupying court inventory
- Pro/coach management: schedules, lesson packages (unit tracking), coach profiles
- Social/player matching: open play, "still looking for player", open matches
- Fee differentiation by time of day / booking length / booking type
- Cancellation / no-show policies (implied by occupancy analytics naming cancellations; exact mechanics unverified)
- Utilization/occupancy analytics and revenue reporting
- Member communications

### L2 — Variant / Optional Structure

- Membership dues billing, autobilling, member statements/chits (private-club pole)
- POS / pro shop / inventory / racket stringing (full-service club pole)
- Payroll / time & attendance (club-as-employer pole)
- Ratings / ladders / rankings / sanctioning (competition-first pole; federation context)
- Multi-amenity embedding (golf, F&B, spa, pool, marina — club-suite pole)
- Marketplace distribution of club inventory to a consumer network (Playtomic pole)
- Multi-sport breadth (tennis+padel+pickleball+squash+racquetball+table tennis) and multi-site operators
- Indoor/simulator courts; seasonal court management (winter/seasonal operations)
- Kiosk / TV display surfaces
- Membership syncing to regional/national governing bodies (federation-linked clubs)

### L3 — Vendor-specific (kept out of final document)

- RacquetDesk: tier names (Seasonal/Lite/Standard/Pro), per-facility pricing, Seasonal Court Management add-on, Track Tennis/Swish/Gleantap/WorldPay integrations, USPTA/RSPA sponsorship, 10sPortal heritage, "Advanced Player Ratings Management" branding
- Playtomic: network statistics, "Open Matches" branding, Academy product line naming, leveling system, setup-session onboarding
- Jonas: "The Sheet" (golf), ClubHouse Online app, chits/dues categories, marina/hotel/spa modules, four-step booking flow framing
- SportyHQ: box leagues, sanctioning, governing-body solutions, TV display mode, membership-ID formats, membership syncing mechanics

## Historical / Market-Sample Check (§24 reasoning)

- Paper-era racquet club: court reservation book (courts × hours grid), member register with dues and guest policies, pro's lesson book, wall-mounted league/ladder sheets, pro-shop till, monthly member statements — satisfies all four L0 legs with no software. ✓
- 1990s/2000s Windows-era tennis club packages and UK squash club booking sheets: same structure. ✓
- Pay-and-play municipal tennis center with punch cards / customer accounts: satisfies via the customer-account realization of leg 3 (membership not required). ✓
- Modern padel club running entirely on a marketplace (Playtomic pole): satisfies — court inventory + reservations + customer accounts with pricing rules + revenue record; membership absent. Confirms membership is the dominant realization, not the invariant. ✓
- Conclusion: the definition does not depend on the current US SaaS pattern (branded apps, autobilling, ratings) — none of those are in L0.

## Vendor-specific Findings

See L3. Additionally: marketplace distribution of club inventory is documented at only one sampled product (Playtomic) — held as a pole/variant, not promoted. TV display mode documented at SportyHQ only; kiosk at RacquetDesk only — both held product-specific realizations of an on-site display surface, mentioned (if at all) as optional.

## Boundary Findings

| Adjacent Type | Shared surface | Decisive difference | "Remove → becomes" test |
|---|---|---|---|
| **Golf Course Management** (documented neighbor) | membership + booking + programming + pro shop | golf's unit is a starting position on a shared course (tee sheet, per-player green fees, round lifecycle, pace); racquet's unit is exclusive hourly use of a court (court fees per booking, no round semantics) | Remove court-time semantics, add tee sheet → golf |
| **Sports Court Booking** | court reservations | booking platform is the consumer demand surface/channel; RCM is the operator's system of record (member governance, programming, revenue record). A RCM's own booking engine/app is a channel of the same system | Remove operator-of-record side → consumer booking platform |
| **Sports Club Management** | member organization management | club-first Type centers the member organization (any sport: teams, seasons, registration); RCM centers court capacity and play. SportyHQ straddles (competition-first with bookings) — its bookings leg is RCM-shaped, its league/ranking leg is Sports Club/League-shaped | Remove the court-time center → sports club management |
| **Sports Facility Management** | rentable spaces by hour | generic spaces (halls, rinks, fields) without racquet semantics; Jonas's own copy ("meeting rooms, tennis courts, swimming lanes, golf simulators… you name it") shows the suite module is facility-generic, while racquet-first products center courts | Remove racquet semantics → facility management |
| **Amenity Booking Platform** | court/slot booking | amenity booking is one shared-facility surface for residents of a community; RCM is the club's whole business system (programming, pros, revenue) | Remove club business scope → amenity booking |
| **League Management / Tournament Management** | leagues, tournaments, ladders | competition machinery is the other Type's center; RCM hosts club-level programming and commonly integrates out to dedicated competition products (Swish at RacquetDesk) or embeds light versions (SportyHQ native) | Remove court/member center → league/tournament management |
| **Gym Management / Fitness Studio Management** | member billing + class scheduling | fitness classes vs court-time inventory; no court semantics, no guest-on-court play shape | Remove courts → gym management |
| **Appointment Scheduling Application** | time-slot bookings | generic slots lack court-configured capacity, member governance, play-shape types, play/revenue record | Remove club context → appointment scheduling |
| **Skedda-class generic space booking** (boundary context, not a Type neighbor in the directory) | slot booking of named spaces | generic space booking has no member governance, programming, or racquet revenue semantics; its sports use case is spun off to a separate product | — |

Taxonomy check: the leaf stands as an independent Type. It is the racquet-sport analog of Golf Course Management (court-time capacity model vs tee sheet), distinct from Sports Court Booking (demand side), Sports Club Management (org-first), and Sports Facility Management (generic spaces). No directory change proposed.

## Uncertainties

- CourtReserve (leading US tennis/pickleball standalone SaaS), Club Locker (US Squash federation platform), and EZFacility could not be fetched (403/timeout/JS-rendered). The sample therefore lacks the biggest standalone US SaaS name and the federation-backed squash pole; assertions are calibrated to the four fetched products and worded cross-product where supported.
- No help-center KB articles were reachable for any sampled product (RacquetDesk KB not publicly indexed; Playtomic help transport error; Jonas/SportyHQ evidence is feature pages). Operational parameters — default slot lengths, cancellation windows, no-show fee mechanics, exact check-in behavior — were NOT verified and are deliberately absent from the final document.
- Reservation lifecycle detail (explicit check-in state at the court, like golf's starter check-in) is unverified; on-site display surfaces (kiosk/TV) were observed but their exact role in the lifecycle was not documented.
- Whether membership dues billing is universal is uncertain: 3/4 sampled products document it clearly; the Playtomic pole documents billing/payments without membership semantics. Held as dominant-realization (L1/L2), not invariant.
- RacquetDesk's "Advanced Player Ratings Management" depth undocumented beyond the name; ratings treated as a competition-pole capability (3/4) without claiming mechanics.

## Final Synthesis

Racquet Club Management is the operator-side business system of record for a racquet-sport club or facility. Its world is built on court time: the club's courts laid out as dated, individually slot-ted bookable capacity. Every booking channel — the member app/portal, the front desk, the club's website, and (in the marketplace pole) a consumer player network — writes court reservations into that one inventory. Each reservation carries a named party (members and their guests), a play shape (singles, doubles, lesson, solo practice, open play), and moves through booked → played / cancelled / no-show, generating the club's play-and-revenue record. Around this core, mature products add the commercial periphery a racquet club actually runs on: member accounts with governed booking privileges (windows, prime times, fees, counts), programming that occupies court inventory (lessons, clinics, programs, leagues, tournaments, events), pro/coach management with lesson packages, social player matching, guest policies, utilization and revenue analytics, and member communications. Variant axes organize the market: the private membership club pole (dues billing, statements, chits, multi-amenity suites), the pay-and-play/marketplace pole (per-booking payments, open network distribution), and the competition-first pole (leagues, ladders, rankings, federation sanctioning). The Type spans standalone racquet-first platforms to the court-booking module of wider club-management suites.
