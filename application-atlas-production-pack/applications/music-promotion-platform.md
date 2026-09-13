# Music Promotion Platform

## Overview

A **Music Promotion Platform** is a two-sided service that connects makers and representatives of music recordings with independent music curators — the people who control channels through which new music reaches audiences, such as playlist owners, blogs and other media, radio shows, and content creators. The artist submits a track for consideration; curators review it and record a decision to feature it on their own channel or to decline, commonly with written feedback; the platform governs the terms that make this exchange accountable — what a submission costs, what a curator owes in response, and what is refunded or guaranteed when the terms are not met.

It solves a structural problem of the recorded-music business: the people who decide what gets exposure (curators) are scattered across thousands of independent channels, and contacting them directly is slow, unaccountable, and easy to fake. The platform concentrates both sides in one place, vets the curator side, standardizes the pitch format, and turns "get my music heard" from cold outreach into a recorded, refundable, reportable process.

The defining structure is deliberately small: a submitted recording, a curator network, a review-decision loop, and governed terms of exchange. Everything else the market attaches — genre-matching engines, pre-release campaigns, ads studios, AI track checkers, influencer hiring — is common but optional, and some of it drifts toward neighboring Application Types.

## Users & Context

**Primary users (demand side)** are the people responsible for getting a recording heard:

- **independent artists** — the dominant audience; they assemble a track, choose or attract curators, and run campaigns themselves
- **labels** — pitch releases across a roster, often maintaining the platform relationship on artists' behalf
- **managers and publicists** — run pitching on behalf of artists as part of a release campaign

**Supply side** — the platform's other constituency:

- **playlist curators** — manage playlists on streaming services and review submitted tracks for possible adds
- **bloggers, journalists and media outlets** — review, interview, and feature artists
- **radio stations and show producers** — decide what gets airplay
- **content creators** (short-video creators especially) — make videos using submitted tracks
- **industry professionals** — labels' A&R, bookers, managers, publishers looking for discoveries

The work context is a web dashboard on both sides, with the rhythm of use organized around a release: a burst of campaign setup in the weeks around a release date, a waiting period while curators respond, then reading results and following up on placements. Curators work from a review inbox on their own schedule.

## Core Model

### The defining core

Four structures, jointly held. Remove any one and the product stops being a music promotion platform.

- **The submitted recording** — a track (or release) is the unit of promotion. Both already-released and unreleased music are promotable, and unreleased submissions are a standard part of the pre-release playbook. Everything in the system — the pitch, the curator's listen, the decision, the feedback — attaches to this submitted piece of music. Without it there is no music-submission core.
- **The independent curator network** — the supply side: third parties who own channels of music exposure and can be reached through the platform. Curators have profiles with genre tags and channel information, and they are independent: the platform delivers submissions to them, but they decide editorially what they feature. Without them there is only a marketing tool.
- **The review-decision loop** — each submission is put to curators, who listen and respond with a recorded outcome: feature it on their own channel (a playlist add, a review, an interview, airplay, a video, a label conversation) or decline. Feedback is commonly attached to the response. The decision belongs to the curator, not the platform — the platform sells consideration and response, not placement. Without the loop, the service is either unaccountable cold pitching or paid placement, which the legitimate market explicitly rejects.
- **The governed terms of exchange** — explicit platform rules that make the exchange real: what a submission costs (per-submission credits, campaign fees, or campaign budgets), what a curator owes in response, and what happens when they don't deliver (credits refunded, fees returned, fees guaranteed back). Every researched product leads with this accountability as its core promise. Without it, the product is a message board.

```text
Maker (artist / label / publicist)
  ↓ submits a recording (released or unreleased)
Platform-governed terms (cost per submission · response obligations · refunds)
  ↓ delivers to
Independent curator network (playlists · blogs/media · radio · creators · industry)
  ↓ reviews and decides
Recorded outcome: featured (placement / coverage / offer) — or declined
  ↓ accumulates into
Campaign results (responses · placements · coverage · feedback)
```

### Standard capabilities of mature products

These are widespread in the current market but do not define the Type:

- **Curator discovery** — searchable, filterable curator profiles (genre, channel type, country, audience signals) so the artist can target the right people
- **Campaign object** — a campaign bundles the submitted track, its targeting, and all its submissions into one managed unit with a budget
- **Written feedback as a deliverable** — curators commonly respond with comments on the production, vocals, or fit; some products guarantee feedback as the thing you buy, others explicitly sell results instead
- **Curator vetting and authenticity control** — application screening for influence and editorial quality, plus ongoing monitoring for fake engagement; "no bots" is an industry-wide selling point, aimed at the real problem that fraudulent playlists and streams make promotion worthless
- **Campaign reporting** — a dashboard recording responses, placements and coverage obtained, and feedback received, per campaign
- **Pre-release submission windows** — campaigns can run before the release date so placements and coverage land around launch
- **Two-sided consoles** — an artist-side campaign surface and a curator-side review inbox

### One structure, many implementations

The core is conceptual; products realize it differently:

```text
Concept:              Submitted recording
Implementations:      streaming-link pitches · uploaded audio for unreleased tracks · full release submissions

Concept:              Curator network
Implementations:      self-applied curator pools · team-screened rosters · heavily vetted networks with low acceptance rates

Concept:              Terms of exchange
Implementations:      per-submission credits · campaign fees · campaign budgets with pay-per-review · refund rules when curators don't respond

Concept:              Recorded outcome
Implementations:      response inbox · live campaign dashboards · end-of-campaign coverage reports
```

## How It Works

### The artist-side campaign loop

```text
prepare the recording (released, or unreleased with a future date)
→ choose the promotion surface (pitch to curators directly, or set targeting and let the platform match)
→ define targeting: genres, moods, languages, curator types, regions
→ set spend: credits per submission, a campaign fee, or a campaign budget
→ submit; the platform delivers the track to the targeted curators
→ curators review; responses arrive — feature/offer or decline, commonly with feedback
→ placements and coverage accumulate on the release (playlist adds, reviews, interviews, airplay, videos, label conversations)
→ close the campaign: report of responses, coverage, and curators worked with
```

Three initiation patterns exist across the market:

- **Artist picks curators** — the artist browses curator profiles, filters by fit, and sends the track to specific chosen curators. Maximum control, manual work.
- **Curators come to the artist** — the artist submits once (commonly passing a platform-side quality check first); interested curators discover the release and send coverage offers, which the artist accepts or declines. The marketplace runs in reverse.
- **Platform matches** — the artist describes the track (genre, mood, language); the platform's matching engine selects the curators, and submissions flow automatically until the budget is spent.

### The curator-side loop

```text
apply / get screened into the network
→ receive submitted tracks in a review inbox (chosen by the curator, matched, or offered)
→ listen within the platform's response window
→ decide: add to playlist / write review / book interview / use in video / make an offer — or decline
→ receive compensation where the model provides it (review fees, credits, paid offers)
```

### Pre-release campaigns

A standard variant of the loop runs before the release: the artist uploads the unreleased track, the platform delivers it securely to curators ahead of the launch date, and placements or coverage commitments land as the track goes live. The span of these windows is platform-specific.

### Capability tiers

**Defining core** — without these, not this Type:

- submitted recording as the unit of promotion (released or unreleased)
- independent third-party curator network reachable through the platform
- recorded review-decision loop with the curator's editorial decision
- governed terms of exchange (cost, response obligations, refunds/guarantees)

**Standard capabilities** of mature products:

- curator discovery and filtering; genre/mood/language targeting
- campaign object with budget and reporting
- written feedback attached to responses
- curator vetting and authenticity/bot controls
- pre-release submission windows
- two-sided consoles

**Optional / advanced**, depending on product and tier:

- ad-creation studios and link tools inside the same account
- AI track checkers, playlist analyzers, artist-audience checkers
- influencer hiring (booking creators directly for content)
- in-campaign service marketplaces (extra promo services from curators)
- label/roster-scale accounts

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Campaign setup

Where a release becomes a campaign.

- track selection (from a link or an upload), targeting options (genres, moods, curator types, regions), spend configuration
- pre-release date entry when applicable
- primary actions: set targeting, set budget, submit

### Curator discovery

The supply side as a browsable surface (in products where the artist chooses curators).

- curator profiles: channel kind, genres, reach signals, editorial description
- primary actions: filter by fit, inspect a curator's channel, send the track

### Responses / inbox

Where the waiting resolves.

- list of submissions with their per-curator status: pending, responded, declined, featured
- written feedback attached to responses; offers presented for acceptance
- primary actions: read feedback, accept offers, follow up

### Campaign report / dashboard

The accountability surface.

- responses received, placements and coverage obtained (playlist adds, reviews, airplay, videos), spend against budget, sometimes downstream performance signals
- primary actions: review results, export/share coverage, plan the next campaign

### Curator review inbox

The supply-side console.

- queue of submitted tracks, response deadline indicators, decision actions
- primary actions: listen, accept (add/feature), decline, write feedback, view earnings

## Important Rules / Behaviors

### The platform sells consideration, not placement

No legitimate product guarantees that curators will add a track. The sampled market states this openly — one vendor explicitly ties the rule to streaming-service terms of service, and the same vendor's pricing pages disclaim placement guarantees. Guarantees that do exist are one level down: a guaranteed *response* (credits refunded if a curator doesn't reply within the platform's window), a guaranteed *review* (fee returned if a curator never reviews), or a guaranteed minimum *coverage* (campaign fee refunded if no curator covers the release). This rule is also the boundary against pay-for-placement services, which the market treats as manipulation.

### The decision belongs to the curator

Submissions are delivered "for placement consideration" — the platform routes the pitch, but the feature/decline decision is editorial and belongs to the channel owner. A rejection consumes the review's cost in pay-per-review models: the artist paid for the listen and response, not for the add.

### Unanswered submissions are refundable

Response obligations are enforced mechanically. If a curator does not respond within the platform's window, the cost of that submission is returned to the artist's balance automatically. This is the enforcement layer that distinguishes the platform from cold outreach.

### Curators are vetted — and the market polices itself

Curator quality is the industry's central trust problem (fake playlists, botted streams). Products screen curator applications, monitor channels continuously, and reject most applicants; several publish explicit policies against artificial playlists and AI-generated submissions. The artist-facing framing is constant: real human curators, organic audiences.

### Both released and unreleased music qualify

The submitted unit can be a finished release or an unreleased track with a future date; some products also accept unfinished demos pitched for feedback or development rather than exposure. Pre-release promotion is a first-class mode, not an exception.

### Results accumulate on the release, downstream effects are attributed loosely

What the platform can record precisely is its own exchange: responses, decisions, feedback, coverage obtained. Streams or audience growth following a placement happen on external services, and platforms attribute them only as directional campaign signals.

## Variants

- **Artist-driven credit marketplaces** — the artist browses and pitches to individual curators with per-submission credits; feedback is commonly the guaranteed deliverable (e.g. SubmitHub, Groover)
- **Automated-match campaign services** — the platform's matching engine picks the curators from targeting; the artist buys a campaign budget, curators are paid per review (e.g. Playlist Push)
- **Inverse offer marketplaces** — the artist submits once, passes a platform quality check, and curators approach with paid or free coverage offers; the campaign fee buys the campaign, with a coverage guarantee (e.g. Musosoup)
- **Channel-specific poles** — streaming-playlist-centric, short-video-creator-centric, blog/press-centric, and radio-centric products emphasize different curator mixes
- **Career-stage poles** — self-serve DIY tools for independent artists at one end; label- and agency-scale pitching with roster accounts at the other
- **Extended suites** — the same account growing ad studios, link tools, and AI checkers; promotion remains the core, but these additions drift toward neighboring marketing Types

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Music Distribution Platform | adjacent, most-confused sibling | distribution delivers a packaged release through a managed store network and passes store-reported earnings back; promotion pitches a recording to curators for editorial consideration, with money flowing toward curators. Distribution platforms may offer playlist pitching as an optional add-on service |
| Influencer Marketing Platform | adjacent | generic brand→creator sponsored-content campaigns; the music promotion platform's supply side controls music-discovery channels and its deliverables are editorial features, reviews, and placements of a recording. Overlap exists at short-video creator campaigns |
| Social Media Management Platform | adjacent | operates the artist's *own* channels; promotion operates *other people's* channels via curator decisions |
| Marketing Campaign / Email Marketing Platforms | adjacent | fan-facing outbound campaigns to a mailing list; no curator review-decision loop |
| Music Marketing & Link Platforms (smart links, pre-save campaigns, fan CRM) | boundary case | structurally different: link/campaign builders and fan-data tools with no curator network and no submission decisions — the market labels them "music marketing" rather than "promotion". No dedicated directory leaf; recorded as a taxonomy observation |
| Artist Booking Platform | adjacent | transacts live-performance engagements; promotion seeks exposure for recordings |
| Record Label Management | broader | runs a label's business operations (catalog, releases, campaigns); the promotion platform is the pitching surface a label uses |
| Public Relations / Media Relations Platforms | generic analog | pitches to journalists exist in both; the music promotion platform is music-native: recordings as units, playlist/radio/creator curators as channels, response/refund machinery built in |

The closest boundary in practice is with Music Distribution Platform, because both are artist/label-facing and both revolve around a release. The seam: distribution asks "where is this release available, and what did it earn"; promotion asks "who considered this recording, what did they decide, and what did it cost".

## Representative Products

- **SubmitHub** — artist-driven submissions to a quality-checked pool of playlisters, bloggers and influencers; freemium credit economy; extended with ads tools and AI checkers
- **Groover** — artist-driven pitch-to-chosen-curators model with a guaranteed-feedback-or-refund credit system; strong network of European media, radio and labels
- **Playlist Push** — premium automated-matching campaigns over heavily vetted Spotify playlist and TikTok creator networks; pay-per-review with fee-return guarantees
- **Musosoup** — inverse marketplace where screened curators approach approved artists with paid or free coverage offers; campaign-fee model with a coverage guarantee

The definition was checked against older and pre-streaming forms (paid radio plugging; the submit-to-industry-opportunity marketplaces of the 2000s) to avoid over-fitting to the current streaming-playlist implementation.

## Sources

Research date: **2026-09-08**

- SubmitHub — official homepage and product navigation: https://www.submithub.com/ , https://www.submithub.com/promotion
- Groover — official homepage with how-it-works, pricing/credits, curator categories and FAQ: https://groover.co/en/
- Playlist Push — official homepage and Spotify promotion page (workflow, review economics, guarantees, vetting): https://www.playlistpush.com/ , https://www.playlistpush.com/spotify-playlists-promotion
- Musosoup — official homepage and artist how-it-works page (lifecycle, offers, coverage guarantee): https://musosoup.com/ , https://musosoup.com/artists-how-it-works
- Feature.fm — official homepage (product line and positioning), used as the boundary probe for the "music marketing platform" family: https://feature.fm/

> Sourcing limitations: SubmitHub's product pages are rendered client-side, so only the homepage copy and navigation structure were retrievable; claims about that product are kept minimal accordingly. Curator-side compensation detail was directly observed for only part of the sample. All counts, prices, and time windows observed during research are point-in-time vendor facts and are deliberately kept out of the body of this document; they are recorded in the paired Research Notes.
