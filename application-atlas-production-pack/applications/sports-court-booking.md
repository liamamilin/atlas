# Sports Court Booking

## Overview

A **Sports Court Booking** application is the player-side application for finding and reserving time on sports courts and facilities — tennis, padel, pickleball, badminton, squash, football pitches, and similar — at venues the player does not own or operate. The player searches for a venue, sees which courts are free at which times, reserves a slot alone or with a party (or takes a spot in a shared game), pays for the booking, and manages it — reschedule, cancel, review history — up to the moment of play.

The defining core is small:

```text
Player-facing bookable court-time inventory
└── Court reservation (the player's booking of record)
    └── Mediated third-party venue relationship
        (venue's prices and policies govern; platform mediates
         discovery → booking → payment → arrival)
```

Everything else commonly associated with these products — open matches and player-matching communities, skill levels and ratings, loyalty points, chat, waiting lists, coaching discovery — is widespread in current products but is not part of the defining core. A regional single-sport booking portal with real-time availability and self-service cancellation satisfies the same structure without any of those extras.

The boundary that matters most: this is the **demand side** of court-time booking. The venue is a third party whose prices, cancellation policies, and access rules govern the booking. When the center shifts to the venue operator's own system of record — court inventory of record, member governance, programming, revenue accumulation — the product is a different Application Type (Racquet Club Management, Sports Facility Management).

## Users & Context

The primary user is a **player** — an individual (or a small group organizer) who wants to play a sport at a specific time and needs somewhere to play:

- find a court near them, for their sport, at a time that suits
- reserve it, alone with a party of friends or by taking a spot in a game with others
- pay for the slot (often splitting the cost with co-players)
- manage the booking afterwards — reschedule, cancel, keep track of upcoming and past games

Secondary actors sit on the other side of the mediated relationship:

- **venues** (commercial sports centers, municipal sports offices, resorts, schools and councils, private clubs) — they set prices, slot durations, cancellation policies, and access rules; the platform enforces and displays these but does not own them
- **co-players** — friends added to a reservation, or strangers joining an open game; they commonly pay their own share
- **coaches/trainers** — discoverable through the same account in some products

The work environment is everyday life, not a workplace: the dominant surface is the mobile app, with web applications as the companion. Bookings are made days, hours, or minutes before playing; the loop is short and repeats for as long as the person plays the sport.

## Core Model

### The Defining Core

```text
Player-facing bookable court-time inventory
└── Court reservation (the player's booking of record)
    └── Mediated third-party venue relationship
```

Three structures. If any one is removed, the product is no longer recognizable as sports court booking:

- **Player-facing bookable court-time inventory** — sports venues held with their courts and bookable time slots, surfaced for player discovery and searchable by location, sport, and time, with availability kept current (real-time where the venue's calendar is integrated; an enquiry channel where it is not). This is the supply side as the player sees it. Without it, the product is a venue directory — or an operator's calendar that players cannot see.
- **Court reservation** — a specific court held for a specific slot by a player, who may organize a party (friends added to the booking, often each paying a share) or take a spot in a shared game. The reservation persists in the player's own record — upcoming and past bookings — and is self-managed: rescheduled or cancelled under the venue's rules, through to the played slot. Without it, the inventory is a listing with nothing to book.
- **Mediated third-party venue relationship** — the venue is not the player's organization. Its prices, cancellation policy, and access rules govern the booking; the platform mediates the loop from discovery to booking to payment to arrival, and per-booking settlement is the dominant completion — in-app payment (full or split among players), a platform wallet, or pay-at-venue arrangements. Without this posture, the product is the venue's own booking channel — the operator's system, not the player's.

### Standard Capabilities

Mature products commonly carry most of the following. They make the product practical; they do not define the Type.

- **Search and discovery** — by location, sport, date and time; venue pages with photos, amenities, prices, and in many products player reviews/ratings; favorites for repeat venues
- **Real-time availability** — slot grids per venue, with instant confirmation on booking; slot durations configured by the venue
- **Per-booking payment** — in-app card/wallet payment due at booking, with split payment so each player pays a share; refunds processed back to the payment method
- **Self-service cancellation and rescheduling** — available within the venue's cancellation window; the venue's policy is displayed at booking and on the booking screen
- **The player's booking record** — upcoming and past reservations, confirmations, reminders, calendar export, receipts
- **Player profiles** — display identity, self-described skill level, and in several products platform-computed ratings or levels
- **Find-players machinery** — open games and matches others can join, activities and buddy lists, "join a game near you" as a first-class alternative to booking a private court
- **Chat with co-players** — inside a reservation or match

### One Structure, Many Implementations

The core model is written in conceptual terms. Implementations vary:

```text
Concept:            Bookable inventory
Implementations:    racket-sport courts only; multi-sport venues (courts,
                    turfs, pools); pitches and courts across many sports

Concept:            Reservation form
Implementations:    private court booking with a party; spot in an open
                    public match; platform-organized games; enquiry-based
                    booking handled by the venue

Concept:            Settlement
Implementations:    in-app payment at booking (full or split); platform
                    wallet; pay-at-venue (tracked as offline by the
                    platform); enquiry with later invoicing

Concept:            Venue relationship
Implementations:    marketplace of independent venues; venues running the
                    platform's own booking system; council/school venues
                    with agency-managed enquiries
```

A reader who has only seen one implementation — say, a padel marketplace app — should still be able to recognize a municipal tennis portal or an enquiry-based pitch-booking site as the same Type.

## How It Works

### The booking loop

```text
Search: location + sport + date/time
→ browse venues and their courts; check amenities, prices, reviews
→ open a venue's availability and pick a free slot
→ choose the booking form: book the court (add friends, or take the
  whole court) or take a spot in an open game
→ see the venue's price and cancellation policy
→ pay — in full or split with co-players
→ confirmation; the slot is held
→ reminders; chat with co-players; add to calendar
→ play
→ the reservation settles into history; repeat
```

### The open-game loop

Where products carry a player community, a second loop runs alongside booking:

```text
Create or find an open game (a court slot with free spots)
→ reserve and pay only your spot
→ other players join until the game is full
→ the court reservation is confirmed once enough players are in
→ if the game does not fill, it is cancelled automatically
  and the players are refunded
→ after play, results may be recorded and ratings/levels updated
```

This loop converts individual spots into a court reservation through aggregation — the platform, not a single booker, is responsible for filling the game.

### The manage loop

```text
Open my bookings
→ upcoming reservations with venue, court, time, co-players
→ reschedule (move to another slot, sometimes another court or venue)
→ cancel — possible within the venue's cancellation window;
  outside it, only the venue can make exceptions
→ refunds return to the payment method per the policy
→ past bookings remain as history (and often as match records)
```

### Core vs Common vs Optional

**Defining core** — without these, not sports court booking:

- player-facing bookable court-time inventory
- court reservation as the player's booking of record
- mediated third-party venue relationship

**Common mature structure** — present in most modern products:

- search/discovery with venue pages
- real-time availability with instant confirmation
- per-booking payment, including split payment
- self-service cancellation/reschedule under venue-set cutoffs
- the player's booking record (upcoming + history)
- player profiles, ratings/levels
- find-players machinery (open games, buddies, activities)
- chat, reminders, favorites

**Variant / optional** — depends on market, sport, and product philosophy:

- sport scope: single-sport-family vs multi-sport vs pitches+courts
- booking mode: instant vs enquiry-based
- social depth: none → buddies → open-match marketplace with auto-fill logic
- competition layers: championships, leagues, level systems tied to bookings
- coaching/trainer discovery attached to the same account
- waiting lists for full slots, with notification when a slot opens
- guest play — bringing a non-player-account guest, billed to the booker
- loyalty and rewards — points for bookings and participation, redeemable as discounts
- premium subscriptions and platform wallets
- membership linkage for private clubs (mediated, not governed, by the platform)

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Search / discovery surface

The entry surface.

- location, sport, date/time selectors; map or list of venues
- venue cards with photos, prices, amenities, ratings, distance
- primary actions: search, filter, open a venue, favorite a venue

### Venue availability view

One venue's bookable time.

- courts × time slots for the chosen date, with free/held states and prices
- slot durations as configured by the venue
- primary actions: select a slot, choose booking form (court or open-game spot), proceed

### Booking / checkout

The reservation and payment surface.

- court, date, time, duration, party members or game spots
- the venue's cancellation policy displayed before payment
- payment: full or split; saved payment methods; price breakdown including any platform fee
- primary actions: add players, choose payment mode, pay, confirm

### My bookings

The player's booking record.

- upcoming reservations (venue, court, time, co-players, payment state) and past history
- primary actions: reschedule, cancel, invite/share, chat, add to calendar, review receipt

### Open games / community surface

Where the product carries a player community.

- list of open games near the player, filterable by sport, level, time
- game detail with spots filled/remaining, players, level band
- primary actions: join a game (pay your spot), create a game, request a spot, chat with players

### Player profile

- identity, skill level or platform rating, match history, buddies
- primary actions: edit profile, manage privacy/blocked players, view history

## Important Rules / Behaviors

### The venue's rules govern; the platform enforces

Prices, slot durations, cancellation windows, and access restrictions are set by each venue. The platform displays them at booking time, enforces them in the app (cancellation is simply not offered outside the window), and directs the player to contact the venue for exceptions — weather calls, late changes, oversized groups. The platform is a mediator, not the rule-maker.

### A held slot removes capacity

The reservation is a real commitment against the venue's calendar: once confirmed, the slot is no longer bookable by other players. Cancellations and no-shows are visible states; venues counter them with cancellation cutoffs, no-refund policies inside the window, and (in some products) automatic cancellation of unfilled open games.

### Payment is per booking, and split payment is native

The dominant settlement is payment at booking time, in full or split among the players — each co-player pays a share of the same reservation. Platform service or convenience fees may sit on top and are commonly non-refundable even when the slot price is refunded. Pay-at-venue arrangements exist; where they do, platforms can treat them as offline bookings outside the tracked record.

### Open games aggregate before they commit

In community-driven products, a spot in an open game is not yet a court reservation: the court is reserved once enough players have joined, and if the game does not fill in time it is cancelled automatically with refunds to the players. The individual booker is not responsible for filling a game they joined.

### Private-club access is mediated, not granted

Where a venue is a private club, booking its courts may require club membership. The platform mediates the relationship — in some products a membership request can be sent from the player's account — but membership itself is the club's to grant. The demand-side product carries the channel; the operator side carries the governance.

### The player's record is the memory

Upcoming and past bookings persist in the player's account — this is what makes the loop repeatable: favorites, history, receipts, and (where present) match results and ratings accumulate around the same identity.

## Variants

- **Racket-sport marketplace** — a player network across many commercial clubs, with open matches, levels, and results as first-class surfaces alongside booking; strongest in padel/tennis markets
- **Multi-sport venue booker** — broad sport coverage (courts, turfs, pools) in dense city networks, with games, groups, and trainer discovery around the booking core
- **Single-region single-sport portal** — one sport family in one region, spanning municipal, resort, and private-club venues; lighter community layer, strong club integration
- **Facility-booking marketplace with enquiry mode** — council/school/leisure venues; instant booking where integrated, enquiry-managed booking otherwise; minimal social layer
- **Municipal / public-venue pole** — public sports offices listing their courts on booking platforms; same loop, public-sector supply
- **Community-organized games pole** — platform-organized guaranteed games and join-a-game mechanics as the headline, with court booking as the substrate

A variant remains a variant unless it changes the core users, objects, workflow, or rules so much that the core model no longer applies.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Racquet Club Management | the operator's system of record for a racquet club: court-time inventory of record, member governance, programming, play-and-revenue record. This Type is the player's demand-side loop; a club system's own booking engine is one channel of the operator system |
| Sports Facility Management | operator side for generic rentable sports spaces (halls, rinks, fields); this Type is the demand side |
| Tee Time Booking Platform | the golf demand-side analog: per-player green fees and round/tee-sheet semantics rather than per-court hourly rental |
| Amenity Booking Platform | closed resident/tenant population booking building-owned shared facilities under a building rulebook; here the population is open and the venues are third-party sports businesses |
| Fitness Class Booking | reserves a participant spot in a staffed, scheduled program; this Type reserves time on a facility resource. Both appear as sibling capabilities inside some products |
| Appointment Scheduling Application | generic time-slot booking without sport-typed inventory, court semantics, or venue-mediated price/policy |
| Service / Sports Marketplace | discovery and transactions across many verticals; here the court-time booking loop is the spine, with marketplace features around it |
| Restaurant Reservation Platform | structural sibling (reserve time on a resource at a third-party venue) in a different domain |
| Outdoor Recreation Discovery | discovery-first without slot inventory or reservations |

The most important boundary is with Racquet Club Management: both show bookable courts. The structural difference is which side of the transaction the system lives on — the player's booking loop versus the operator's system of record.

## Representative Products

- Playtomic — global racket-sport player app and club network (padel, tennis, pickleball); private bookings and open matches, levels, club-configured policies
- Playo — multi-sport venue booking and community app for urban adults (India, Gulf, SE Asia); venues, games, trainers, ratings
- GotCourts — tennis/padel/squash/badminton player app in Switzerland/EU; municipal, resort, and private-club venues; club championships and leagues
- Playfinder — UK/Ireland sports facility booking marketplace (pitches and courts across 19 sports); council/school venues; instant and enquiry-based booking

The sample deliberately spans the marketplace pole, the multi-sport city-network pole, the single-region single-sport pole, and the enquiry-based facility-marketplace pole.

## Sources

Research date: **2026-09-09**

- Playtomic — homepage; Player Help Center (Reservations & Payments; Open Matches & Community) — https://playtomic.io/ , https://playerhelp.playtomic.com/hc/en-gb
- Playo — homepage; Customer Support knowledge base (Booking Venues & Experiences; Cancellation & Refunds; Payments) — https://www.playo.co/ , https://playo.freshdesk.com/support/solutions
- GotCourts — homepage; Help Centre (Suchen & Buchen; Reservations; Payment Services) — https://www.gotcourts.com/en/ , https://playtomic-gotcourts.zendesk.com/hc/en-gb
- Playfinder — homepage; Terms and Conditions — https://www.playfinder.com/ , https://www.playfinder.com/terms

> Sourcing limitation: one candidate product (OpenSports) could not be reached from the research environment and was dropped after repeated failures; the social game-organizing pole is covered indirectly through the sampled products' open-game features. All evidence above comes from official vendor pages and help centers; precise operational parameters observed in help articles (cancellation windows, refund timings, auto-fill thresholds) are product-specific and are stated in this document only as attributed product behavior, not as Type-level rules. Detailed observations, the cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
