# Tee Time Booking Platform

## Overview

A **Tee Time Booking Platform** is a golfer-facing application for finding and reserving tee times — the dated, time-stamped starting slots on golf courses from which a round of golf begins. The golfer searches courses, compares prices and availability, books a starting time for a party (or takes a spot in an organized game), pays, and manages the reservation up to arrival at the course.

The defining structure is small:

```text
Bookable tee-time inventory across golf courses
└── Tee time reservation (the golfer's booking of record:
    a named party holding a specific starting time)
    └── Mediated course relationship (course-set prices,
        policies and privileges; platform settles per booking)
```

Everything else commonly associated with these products — maps and destination browsing, prepaid deals, loyalty rewards, member tee-sheet visibility, mobile check-in, handicap verification, games and competitions, travel packages — is widespread in current products but is not part of the defining core. The platform is the demand side of golf commerce: the courses themselves remain independent businesses whose sheet of record, check-in desk, and revenue accounting live in their own systems (Golf Course Management). Remove the demand-side loop and what remains is a course directory; add the operator's system of record and you have crossed into the operator Type.

## Users & Context

**Primary users:**

- the public/visitor golfer: finds a course (often one they are not a member of), books a starting time for themselves and playing partners, pays, and arrives with a confirmation
- the club member: books within their club's booking rules — advance windows by membership type, guest privileges, member rate types — through the platform rather than by phoning the pro shop
- the playing partner: named on someone else's reservation, receives the confirmation, and may need to remove themselves from a booking they did not create

**Secondary users:**

- the course (supply side): lists its bookable inventory with the platform, sets the prices, cancellation policy and privileges that the platform enforces on its behalf, and receives the bookings into its own tee sheet
- support staff: handle changes that self-service cannot make — for example, liaising with the club when a booked date must change after the self-service cutoff

The context is consumer commerce: single golfer accounts, per-booking payments, mobile apps and websites used evenings and weekends to plan rounds — at home for discovery and booking, and on the phone at the course for confirmation and check-in.

## Core Model

### The traded object: a tee time

The unit of commerce is a **tee time**: a reserved starting position on a course's schedule for a round of golf (18 or 9 holes where offered), on a specific date and time, **priced per player**. Unlike an hourly court rental, what is sold is not duration of a space but a starting slot in the course's playing order for that day; the golfers then flow through the course at the course's pace. The price attaches to each player as a green fee, with add-ons — cart rental above all — attached per player unless the course states otherwise. The party is small and personal: the booker plus named playing partners (guests, friends from a buddy list, or strangers joining an organized game).

### The defining core

Three structures, held together:

**1. Bookable tee-time inventory across golf courses.** The platform holds courses — with locations, hole layouts, photos, reviews, and from-prices — and, for each, the starting times a golfer can actually reserve. Inventory is surfaced for discovery: search by place or map, browse by region or destination, filter by holes format, price promotions, ratings, or facility features. Availability must be real enough to book from; a listing that cannot be booked from the golfer's side is a directory entry, not inventory.

**2. The tee time reservation as the golfer's booking of record.** When a golfer books, a reservation is created **in the golfer's own account**: course, date and starting time, hole format, number and identity of players, rate selections. It persists as the golfer's upcoming tee time (and later as history), it is the golfer's proof — a confirmation to the booker and the named players — and it is self-managed: the golfer can view, edit, cancel, or exit it, under the course's rules, through to the day of play. Per-player management is normal: a player can be added to a reservation, and a player can remove themselves from a reservation they did not create.

**3. The mediated third-party course relationship.** The courses on the platform are not the golfer's organization and are not governed by the platform. Their green fees, cancellation policies, membership privileges, and property rules are what actually govern the booking; the platform mediates the loop — discovery → booking → payment → confirmation → arrival — and enforces the course's rules on its behalf. Settlement is per booking and online-dominant: full payment at checkout for prepaid rates and deals, card-on-file payment at check-in where the course supports it, pay-at-course in some configurations. A platform booking fee may sit on top of the course's price without changing it.

The joint hold is load-bearing. Inventory without reservations is a listings site; reservations without browsable inventory are a bare widget; mediation without both is a review or discovery surface; and inventory plus reservations without the third-party relationship is simply the course's own booking channel — the operator's system, not this Type.

### Standard capabilities

Around the core, mature products add most of the following — with different products emphasizing different ones, and some capabilities conditional on how the course operates:

- **discovery richness** — map and region search, trending destinations, course profiles with reviews and ratings, weekday/weekend price display, filters (holes format, promos, rating thresholds, night golf, indoor golf, driving range)
- **party machinery** — guests by name or buddy list, adding golfers to an existing reservation, per-player removal, confirmations to every named player
- **self-service reservation management** — cancel and edit under the course's cutoff rules
- **deals economics** — limited-time online-only discounted tee times, promo filters, prepaid non-refundable rates, weather rain-check handling
- **member mode** — where the course runs a club membership: member login, visibility of the course's online tee sheet ("who's playing"), advance booking windows that scale with membership type, guest inclusion, member rate types per player
- **arrival surface** — confirmation to present at the course, and mobile self-check-in where the course enables it, marking each player as checked in
- **golfer identity** — handicap tracking, verification, or official-index posting as the golf-native layer of player identity
- **rewards** — points or credit earned for booked and played rounds and referrals

The same structures are realized differently across products: some aggregate hundreds of independent courses into one marketplace; some are the consumer face of a course-software platform; some embed booking inside a GPS-and-scoring super-app; some start from finding people to play with and resolve the game into a booking.

## How It Works

### The public booking loop

```text
Search or browse (place, map, region, filters)
→ open a course profile (photos, reviews, from-prices)
→ pick a date and a starting time from the bookable times
→ set the hole format and the number of players
→ name the players (self, guests, buddy-list picks)
→ pay (full charge at checkout for prepaid rates; other settlement variants exist)
→ confirmation to booker and named players
→ manage (view / edit / cancel / a player exits) until the course's cutoff
→ arrive: present the confirmation; check in (pro shop or mobile self-check-in)
→ play
```

The booking is complete as a platform record before the round is played; after play, it turns into the golfer's history.

### The member loop

A member of a course that runs its club membership through the platform signs in, opens the course's tee sheet from their member dashboard, and reserves within their privileges: an advance window set by their membership type, member rate types selected per player, guests included by name. The course's sheet remains the course's record; the member's reservation also exists in the member's own platform account.

### The deal loop

A golfer buys a limited-time, online-only discounted tee time: payment is charged in full at checkout, the offer cannot be booked by phone or in person, cart inclusion depends on the specific deal's terms, and the purchase is typically non-refundable — with weather policies providing rain checks where play is prevented. The golfer brings the confirmation email to the course.

### The join-a-game loop (social variant)

In products that organize games, a golfer joins a posted game or competition — often taking one of several open player spots — and the game reservation resolves into the same tee time booking, with the platform's community machinery (ratings, verified handicap, rewards) standing in for knowing the other players in advance.

## Interfaces

### Marketplace home / search

The golfer's entry surface.

- typical information: search bar, map, regions and destinations, course cards with photos, review counts, ratings, from-prices
- primary actions: search, filter, open a course

### Course profile with booking calendar

The conversion surface.

- typical information: course photos, hole layouts, description, reviews, price display, the bookable times laid out as a calendar or time picker
- primary actions: choose date, choose tee time, set holes format and player count, proceed to book

### Checkout

- typical information: rate summary per player, cart and add-on options, fees, terms attached to the specific rate or deal
- primary actions: pay, confirm booking

### My tee times / reservation management

The golfer's booking of record.

- typical information: upcoming and past tee times, per-reservation player lists, confirmations
- primary actions: view, edit, cancel, remove a named player, check in where supported

### Member dashboard / course tee sheet

The member's surface for their own club.

- typical information: the course's online tee sheet with upcoming reservations, the member's privileges and advance window, buddy list
- primary actions: reserve a slot, include guests, manage member bookings

### Check-in surface

The arrival surface, typically mobile.

- typical information: the day's tee time, players on the reservation with check-in state
- primary actions: check in selected players, pay any balance with a card on file

## Important Rules / Behaviors

### The course's rules govern; the platform enforces them

Cancellation, editing, and privilege rules belong to the course, not the platform. The recurring shape: self-service cancellation and edits are allowed only while the reservation is unpaid (or not under a prepaid term) and outside the course's advance cutoff; inside the cutoff, changes run through the course or the platform's support. Membership privileges — how far in advance a member may book, which times they may book, whom they may bring — are the course's member policy, mediated by the platform.

### Prepaid deals trade flexibility for price

Discounted online-only tee times are typically charged in full at booking and are non-refundable; their terms (cart inclusion, restrictions) are attached per deal, and bad-weather handling is its own mechanism (rain checks) rather than ordinary cancellation.

### Pricing is per player, and fees ride on top

Rates attach to each player (with member, guest, senior and similar classifications where the course uses them); carts and extras attach per player unless stated; a platform booking fee may be added without altering the course's price.

### A reservation is a party of named players

Players are named on the booking, receive confirmations individually, can be added before play, and can remove themselves subject to the same cutoff rules — the reservation is shared property of the party, anchored by the booker.

### Check-in is course-enabled

Where mobile self-check-in exists, it works only at courses that have enabled it, applies on the day of play, and marks each player individually; otherwise the golfer checks in at the pro shop with the confirmation.

### The platform is not the system of record for the course

The course's tee sheet, check-in desk, and revenue records live in the course's own management system; bookings from every channel — phone, walk-in, the course's own site, and this platform — converge there. What the platform owns is the golfer's side: the account, the reservation record, the payment, the confirmation.

## Variants

- **Standalone tee-time marketplace** — the multi-course marketplace as the entire product; discovery breadth and deals depth are the competitive surface
- **Platform-affiliated marketplace** — the consumer face of a course-software platform; its marketplace fronts courses that run on the same vendor's operator system, with member and public booking side by side
- **Super-app attachment** — booking embedded in a golfer app centered on GPS, scoring, statistics and social play, sometimes split out to a separate booking portal under the same brand
- **Social game-first booking** — finding golf buddies and organized games first; the tee time is booked as the game's venue; strongest in mobile-first regional markets
- **Member-heavy vs public-heavy posture** — products and deployments lean toward visitor commerce (marketplace pole) or club-member commerce (member pole) depending on the courses they front
- **Regional market shapes** — marketplace giants in large single markets, mobile-first community booking in emerging golf markets, cross-border destination browsing in tourism-heavy regions
- **Inventory breadth variants** — night golf, indoor golf and driving-range slots appearing alongside (or instead of) full course rounds; stay-and-play packages bundling hotel stays with rounds

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Golf Course Management | the other side of the same tee time | operator-side system of record: tee-sheet configuration, check-in/starter flows, golfer classifications, play-and-revenue records; a course's own booking engine is a channel of that system, not this Type |
| Sports Court Booking | demand-side sibling (different sport) | same demand-side loop, different inventory semantics: exclusive hourly rental of a court/space vs a per-player starting slot on a course's tee sheet for a round |
| Sports Marketplace | market vs loop | aggregates venues, games and coaching as a market to browse; here the tee-time booking loop is the spine, with market features optional |
| Golf Tracking / Handicap Application | round record vs round reservation | the golfer's scoring, statistics and handicap system; the two Types share products but trade different objects — a recorded round vs a reserved round |
| Amenity Booking Platform | closed vs open population | residents booking building-owned shared facilities under a building rulebook vs an open golfer population booking third-party courses |
| Fitness Class Booking | spot vs slot | reserving a participant spot in a staffed, scheduled program vs a starting slot on a course |
| Appointment Scheduling Application | generic vs domain-typed | generic time-slot booking lacks course inventory, per-player green fees, rounds, tee-sheet anchoring and member privileges |
| Restaurant Reservation Platform | structural sibling, other domain | reserves time at a third-party venue, but with table/service semantics rather than round, green-fee and party-of-golfers semantics |
| Online Travel Agency / Tour & Activity Marketplace | adjacent via packages | travel bundling exists here only as an optional stay-and-play attachment; the center is the single-round reservation |

The boundary with Golf Course Management is the most important one, because both deal in tee times daily. The structural difference is whose record it is: the platform holds the golfer's path to the booking; the operator holds the course's capacity, check-in and revenue. When one vendor ships both, the two surfaces remain two Types.

## Representative Products

- Chronogolf (by Lightspeed) — platform-affiliated marketplace with member and public booking
- Deemples — social game-first booking (Southeast Asia)
- 18Birdies — super-app with tee-time booking as one surface
- Golfshot — super-app with a separate tee-time booking portal

The largest tee-time marketplaces of the biggest golf market were not directly documentable at product level in this research pass (their sites refused automated access); they are established in market structure as the distribution channels into which course software feeds tee-sheet inventory.

## Sources

Research date: **2026-09-09**

- Chronogolf — marketplace homepage: https://www.chronogolf.com/ ; golfer help center: https://support.chronogolf.com/ (articles: Booking as a public player; Booking as a member; Booking an online deal; Cancelling and editing reservations; Removing yourself from a booking; Checking in from a mobile app; Booking through Google; and the Booking Management section index)
- Deemples — https://www.deemples.com/ (homepage: positioning, filters, course/region listings, feature claims, community testimonials)
- 18Birdies — https://www.18birdies.com/ (homepage feature map; help-center surface map cited from the paired Golf Tracking / Handicap research of 2026-09-08)
- Golfshot — https://www.golfshot.com/ (homepage feature map and Tee Times navigation)

> Sourcing limitation: the dominant US marketplace products (GolfNow, Supreme Golf, TeeOff, GolfPass, EZLinks) and several regional booking portals refused automated access or were unreachable during this pass (repeated 403s, transport errors, or empty responses). Their market role is documented indirectly (named as tee-time distribution channels in course-side vendor documentation). Claims about those products' internal features are intentionally absent here; operational parameters observed in reachable products (cancellation cutoff values, advance-window lengths, check-in distance rules) were kept product-specific and are recorded in the paired Research Notes rather than asserted as type-wide rules.

Detailed product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
