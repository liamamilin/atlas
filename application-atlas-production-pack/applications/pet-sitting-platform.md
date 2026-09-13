# Pet Sitting Platform

## Overview

A **Pet Sitting Platform** is a consumer-facing, two-sided platform that connects pet owners with individual pet sitters. Owners find, evaluate, and book sitters through structured sitter profiles; the platform mediates contact and payment; and the service being arranged is the **sit** — a period during which the sitter takes over care of the owner's animal while the owner is away or unavailable, with care delivered in the animal's own home or in the sitter's home.

The defining structure is small:

```text
Pet owner (care-seeker)  ── discovers & selects ──▶  Sitter profile (care-provider)
                          via platform
                                     │
                          books a sitting engagement
                                     │
              sitter cares for the animal in its home or the sitter's home
                     and reports back until the owner returns
```

Everything else commonly associated with modern products — pet profiles with medication notes, daily photo updates, in-app payments, protection plans, home-care extras like watering plants — is widespread in current products but is implementation and maturity, not the definition. An older, simpler site with sitter profiles, owner search, and direct contact still belongs to this Type.

Pet sitting platforms sit in a family of pet-care marketplace Types. In practice, most current products realize sitting as one service inside a broader pet-care marketplace that also offers walking, boarding, and daycare; this document describes the Type from the sitting side — the matching, booking, execution, and reporting of custody care. Two features give the Type its character: the care happens **in a home, not a facility**, and the engagement spans a **period of the owner's absence**, not an hour-long outing.

## Users & Context

**Primary users — pet owners.** People who need someone to care for their animals while they cannot: travelers and holidaymakers, business travelers, weekenders, owners of pets that do not tolerate boarding environments (stressed cats, senior dogs, caged animals such as fish, rabbits, or birds), and owners who prefer their pets to stay in familiar surroundings. Owners are the selecting side: they review sitters, judge trust signals, and choose whom to let into their home — or whose home to entrust their pet to.

**Primary users — pet sitters.** Individuals who care for other people's animals — from occasional sitters who enjoy animal company (in the exchange variant, their compensation is the homestay itself) to side-income and full-time professional sitters. Sitters maintain a profile, set their own availability, respond to requests or applications, perform the sits, and report back. They are independent providers, not platform employees; products consistently position themselves as a venue, with sitters responsible for their own conduct and compliance.

**Context.** Sitting engagements are local and trust-heavy: the owner is granting access to their home, or placing a dependent animal in a stranger's home, for days at a time. The pet's temperament, habits, medication, and routines travel with every booking. A first engagement between strangers is normally preceded by a meet & greet, and during the sit the owner — away and unable to see for themselves — relies on the sitter's updates for peace of mind.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product is no longer recognizable as a pet sitting platform:

- **Two-sided participation** — differentiated owner and sitter roles, each with its own account and registration path. Without the two roles, the product is either a sitter's personal page or generic advertising.
- **Sitter profiles** — persistent, structured, searchable identities of individual sitters carrying pet-care-relevant attributes: photo, bio and experience, which animals and services they care for, capabilities (such as administering medication), availability, verification badges, and accumulated reviews. Without this, the product becomes a classifieds board of transient ads.
- **Owner-driven discovery and selection** — owners find and choose sitters. Products differ in mechanics — searching profiles, posting a sit listing that sitters apply to, or requesting quotes — but in every observed shape the owner compares candidates and selects. The platform supplies candidates and trust information, not assignments.
- **Platform-mediated sitting engagement** — the engagement arranged through the platform is a sit: the sitter assumes care responsibility for the owner's animal over a bounded period while the owner is away or unavailable, with care delivered in the animal's own home or the sitter's home — not in a commercial facility. Without custody care as the service unit, the same skeleton becomes a different pet-care Type.

### Objects Inside the System

```text
Owner account
└── Pet profile           (species/breed/age, temperament, habits,
│                          medication and care requirements)
│   └── Sit booking       (sitter, dates, service shape, price, state)
│       └── Sit updates   (photos/messages from the sitter during the sit)
│
Sitter profile            (identity, experience, capabilities, availability,
│                          verification badges, reviews)
└── accepts / applies / declines
└── receives payout (or homestay, in the exchange variant)

Trust layer               (verification, reviews, platform protection)
```

- **Owner account** — the care-seeking side's identity, holding payment methods, bookings, and one or more pet profiles.
- **Pet profile** — a first-class object on the owner's account. It carries the animal-specific facts a sitter needs: species, breed and age, temperament and habits, medication and care requirements. Search, listings, and requests are pet-aware: the animal is part of the engagement, not a footnote in a message.
- **Sitter profile** — the central, persistent, searchable object of the marketplace. It aggregates everything an owner uses to choose: experience and self-description, which animals and care shapes the sitter offers, capabilities such as medication administration, availability, verification badges, and reviews from past owners. It is simultaneously a marketing surface, a trust surface, and the sitter's work identity.
- **Sit booking** — the engagement record between a specific owner (and pet) and a specific sitter: dates, service shape (in the pet's home, in the sitter's home, or drop-in visits), and price. Bookings move through a request→confirmation→sit→completion lifecycle and anchor payment and protection.
- **Sit updates** — the feedback the owner receives during the sit: photos and messages as a minimum; some products add a structured report (visit times, care events such as feeding and toilet breaks, notes).
- **Trust layer** — verification and reputation signals that accumulate on profiles (identity checks, background checks or references where offered, reviews) plus platform protection that wraps booked sits.
- **Held payment** — where sitters are paid, payment is made on the platform and released after the service, rather than settled privately. In the membership-exchange variant, no sitter payment exists at all; the platform charges memberships instead.

### Concept vs Implementation

The core is written conceptually; products implement it differently:

```text
Concept:               Owner-driven discovery
Implementations:       profile search with filters; posting a sit listing
                       that sitters apply to; posting a request and
                       receiving quotes from interested sitters

Concept:               Care responsibility in a home
Implementations:       sitter stays in the owner's home (house sitting);
                       pet stays in the sitter's home; recurring
                       drop-in visits to the owner's home

Concept:               Sit updates
Implementations:       chat photos and messages; daily photo updates;
                       structured visit report with care-event log

Concept:               Compensation
Implementations:       per-booking commission on sitter rates;
                       percentage of quoted amounts; membership fees
                       with unpaid sitters (exchange model)
```

## How It Works

### 1. Owner onboarding

```text
Create account → add pet profile (species, temperament, habits,
medication and care requirements) → set location
```

There is no team, no workspace, no organization. The account is personal, and the pet profile is the main configuration object — matching and booking are pet-aware from the start.

### 2. Find and choose a sitter

```text
Search sitter profiles near you            (search-and-book shape)
   or  post a sit listing and receive      (listing-and-applications shape)
       applications from sitters
   or  post a request and receive quotes   (request-and-quotes shape)
→ shortlist by profile, reviews, verification
→ arrange a meet & greet before the sit
```

Discovery is owner-driven in every observed form; the shapes differ in who initiates, not in who decides. The meet & greet is a normalized step — the owner, pet, and sitter meet before the owner leaves the animal (and often the house keys) with the sitter.

### 3. Book and pay

```text
Send booking request (dates, service shape, pets)
→ sitter reviews and accepts (or declines)
→ final price shown
→ owner pays on the platform — funds are held, not sent to the sitter yet
```

Where sitters are paid, the characteristic pattern is held payment: the owner pays the platform when booking, and the sitter is paid out after the sit completes. In the membership-exchange variant, this step becomes a membership arrangement instead — sitters are not charged and do not charge; both sides pay the platform for access.

### 4. The sit itself

```text
Sitter takes over care at the agreed start
→ cares for the animal in its home (feeding, walks, medication,
   companionship — commonly also home duties: plants, mail, presence)
   or hosts the animal in the sitter's home
   or makes agreed drop-in visits
→ sends the owner photo updates during the sit
→ hands back the animal (and home) at the agreed end
```

The owner is away — the sit exists precisely because the owner can't be there. That is why updates matter: the owner's peace of mind is produced by photos and messages arriving during the sit, and on some products by a structured report of what happened (times, feeding, toilet breaks, notes). In-home sits commonly carry a home-care adjunct: the sitter's presence also keeps the home lived-in and tended.

### 5. After the sit

```text
Sit completes → sitter receives payout (where applicable)
→ owner leaves a review → trust accumulates on the sitter's profile
```

Reviews are the reputation mechanism that makes the next owner's selection easier. Cancellation policies govern the edges of the lifecycle, and platform support handles disputes and emergencies — including what happens when a sitter falls ill mid-sit.

### 6. The sitter's side

```text
Create profile (photo, bio, experience, capabilities)
→ complete verifications → set availability
→ receive requests / apply to sit listings (accept / decline)
→ perform sits, send updates
→ receive payouts after completed sits (or homestays, in the exchange variant)
```

Sitters are advised to keep availability current, respond promptly, and use meet & greets to filter for compatible animals and households. Declining is normal and allowed; ignoring requests is not — responsiveness is an explicit marketplace expectation.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Marketplace search / browse

The owner's entry surface.

- lists sitter profiles near a location, filterable by animal type, service shape, availability, and other attributes
- typical information: photo, headline, rating, review count, verification badges, rate or exchange terms
- primary actions: open a profile, save favorites, start a search, post a listing or request

### Sitter profile detail

The trust and selection surface.

- experience and bio, animals and care shapes offered, capabilities (e.g. medication), availability, verification badges, reviews from past owners
- primary actions: message, request a booking, invite to apply, arrange a meet & greet

### Sit listing / request editor

The owner's engagement-creation surface (in listing- and request-based shapes).

- dates, location, pets and their care requirements, home notes, service shape
- primary actions: publish, review incoming applications or quotes, select a sitter

### Pet profile editor

The owner's configuration surface for the animal.

- name, species/breed/age, temperament, habits, medication and care requirements
- primary actions: add/edit pets, attach pets to a listing or booking

### Bookings / requests dashboard

The lifecycle surface for both roles.

- request and booking states (requested, confirmed, in progress, completed), upcoming sits, date ranges
- primary actions: request, accept/decline, pay, cancel, track status

### Chat

The communication surface between a specific owner and a specific sitter.

- per-booking or per-relationship threads; sit updates arrive here
- primary actions: send messages/photos, coordinate logistics and handover
- safety behavior: mature products keep first contact on the platform — for example by blocking phone numbers and emails from chat until a booking exists, and by staging the reveal of addresses

### Sit updates surface

The execution feedback surface.

- photos and notes from the sitter during the sit; on some products a structured report (visit times, care events, personalized note)
- primary actions: view updates, respond to the sitter

### Review surface

- post-sit rating and review of the sitter, attached to their profile; on some products sitters also review owners and their listings

### Earnings / sit dashboard (sitter side)

- completed and upcoming sits, amounts and payout status (where applicable), availability calendar, request/application inbox

## Important Rules / Behaviors

### Payment is held, not handed over — or replaced by membership

Where sitters are paid, the owner pays the platform when booking and the sitter is paid after the sit completes. This protects both sides and keeps the engagement inside the protection and dispute mechanisms; paying off-platform is discouraged and can void protection. The membership-exchange variant shows the boundary of this rule: the invariant is the platform-mediated engagement, not the sitter's wage — one established product class charges memberships and leaves sitters unpaid.

### The meet & greet precedes the sit

First engagements normally include a face-to-face introduction before the owner leaves the animal — and often the home — with the sitter. Platform protection attaches to the booked sit, not to informal pre-booking meetings; the meet builds personal trust, while the platform's trust layer starts with the booking.

### Trust accumulates on sitter profiles

Reviews, ratings, and verification badges attach to the sitter's persistent profile and are visible to future owners. Verification intensity varies by product — identity checks are the baseline, with background checks, external references, and contact verification layered on at some products, sometimes as a prerequisite before a sitter may apply at all.

### Contact is platform-mediated at first

Chat safety controls — blocking phone numbers and emails before a booking exists, staging the reveal of addresses — keep discovery and negotiation on-platform. They reflect the privacy reality of two strangers arranging access to a home.

### Both sides can say no

Sitters may decline bookings (a mismatch discovered at the meet & greet is a normal outcome); owners may walk away before confirming. What both sides owe is responsiveness: timely answers to requests are an explicit marketplace expectation on the sitter side.

### The platform is a venue, not an employer

Sitters are independent providers who set their own terms and are responsible for their own compliance. The platform brokers, holds payment (or sells access), and provides protection — it does not employ or place sitters. Products that employ sitters as staff are operationally an agency or service business, not this Type.

### Protection is real but limited

Booking protection (veterinary-cost coverage for incidents, property damage, theft, sitter accidents, rebooking guarantees when a sitter cancels) is a standard feature, but it is a limited commercial guarantee with caps, exclusions, and claim procedures — products state this in their own terms. Because in-home sitting involves the owner's property as well as the animal, some products extend protection to home and contents.

### Sits are dated custody periods

A sit has a start and an end: the owner leaves and returns on agreed dates, and the care responsibility is bounded by them. This cadence — same home, same animal, multi-day trust — shapes the whole model: the marketplace optimizes for lasting owner–sitter relationships and repeat sits, not one-off transactions.

### Care requirements travel with the pet

The pet's temperament, habits, medication, and routines are structured inputs to matching and to the sit itself, not free-text afterthoughts. Sitters are expected to read and follow them; the ability to administer medication is a profile-level capability owners filter for.

## Variants

- **Search-and-book marketplace** — owner searches sitter profiles and books directly (a common shape).
- **Listing-and-applications marketplace** — owner posts a sit listing; sitters apply; the owner reviews applicants and chooses (the house-sitting exchange shape).
- **Quote-matching marketplace** — owner posts a request; interested sitters respond with quotes; the owner picks one and books.
- **Membership-exchange platform** — sitters are unpaid and care in exchange for homestays; the platform sells memberships to both sides (a distinct product philosophy within the Type).
- **Multi-service pet-care marketplace** — sitting is one service alongside walking, boarding, daycare, grooming (the dominant current structure); the sitting model above applies unchanged to the sitting slice.
- **Sitting-first products** — products focused on sitting/house sitting as the primary service.
- **Service-shape mix** — in-owner's-home sitting (house sitting), at-sitter's-home sitting, drop-in visits, animal-specific lines (cat sitting, bird sitting, small-pet sitting), long-term sits; the mix differs per product and market.
- **Home-care scope** — pet-only sits vs sits that explicitly include home duties (plants, mail, security presence).
- **Fee architecture** — commission on the provider per booking, percentage of quoted amounts, or membership tiers; the conceptual model is unaffected.
- **Geographic scope** — single-country leaders, regional products, and multi-continent platforms.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Dog Walking Platform | sibling marketplace Type over a shared product population; the service unit is the walk (a short outdoor outing, dog collected and returned) rather than custody care in a home; current products commonly serve both |
| Pet Boarding Management | operator-side system of record for a boarding facility with a managed accommodation inventory (kennels, capacity, occupancy); a sitting platform has no facility — care happens in homes |
| Pet Care Business Management | operator-side software for a pet-care company's own clients and staff; not two-sided matching of strangers |
| Pet Daycare Management | operator-side administration of facility-based same-day group care; the animal leaves home for the day instead of being cared for at home |
| Babysitting Marketplace | the same two-sided skeleton in the childcare domain; child-safety trust construction replaces animal-care trust; the pet profile is a standardized first-class object here |
| Home / Local Services Marketplace | brokers generic services, typically by businesses, with generic job objects; no sitter-profile structure, animal-care semantics, or custody-care cadence |
| Classifieds Platform | transient wanted/offered ads without persistent profiled provider identities or role-differentiated accounts |
| Household Staff Management | placement and administration of employed domestic staff; sitting platforms broker dated care engagements between independent strangers, not employment |
| Pet Health Application / Pet Adoption Platform / Lost Pet Platform | shared pet vocabulary only; no service-engagement matching |

The most important boundary is the one with **Dog Walking Platform**: the two Types share a skeleton and often share actual products, and they separate on the unit of service. If the platform's engagement is "someone cares for the animal in its home or theirs while I'm away," it is this Type; if it is "someone comes and takes the dog out for a walk," it is dog walking. A product offering both simply participates in both Types.

## Representative Products

- **TrustedHousesitters** (global) — house-sitting-first platform on a membership-exchange model: verified sitters care for pets (and homes) in exchange for homestays; listing-and-applications discovery; two-way reviews; home & contents protection and a vet advice line.
- **Mad Paws** (Australia) — pet-care marketplace with an explicit sitting taxonomy (sitting in your home / hosting at the sitter's home / house visits); pet-aware search wizard; commission monetization; published guarantee terms.
- **PetBacker** (global, 50 countries) — quote-matching marketplace; drop-in visits vs overnight house sitting as explicit service shapes; per-visit pricing; escrow-style payment; sitting report card.
- **Holidog** (Europe) — request-based marketplace with house sitting (at your home) alongside boarding at the sitter's home and house visits; fully documented request→accept→pay→meet→sit→review lifecycle.

The largest US platform (Rover) could not be reached during research (site access blocked), so US-market sitting structures are not characterized by direct evidence anywhere in this document.

## Sources

Research date: **2026-09-09**

- TrustedHousesitters — homepage (trustedhousesitters.com); How it works — find a sitter; How it works — find a house sit; Trust and safety
- Mad Paws — homepage (madpaws.com.au); Pet Sitting service page (madpaws.com.au/pet-sitters/house-pet-sitting)
- PetBacker — Pet Sitting service page (petbacker.com/pet-sitting)
- Holidog — Austrian homepage (holidog.com/at) with service definitions and booking flow

> Sourcing limitation: rover.com returned HTTP 403 during research (consistent with the earlier dog-walking pass, where Rover and Wag! were likewise inaccessible), and the Mad Paws and PetBacker help centres are rendered client-side and exposed only their indexes. Claims in this document are calibrated to what the reachable official pages directly support; precise vendor numbers (fee percentages, coverage caps, response windows, visit durations) are intentionally omitted and remain in the paired Research Notes.

Detailed product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
