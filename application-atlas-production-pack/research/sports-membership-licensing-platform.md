# Research Notes — Sports Membership / Licensing Platform

## Research Goal

Understand what "Sports Membership / Licensing Platform" software actually is from real products: what the membership relationship and the license instrument are in sports-governance software, what objects exist (member, membership product/category, license, credential, benefits, fees), who operates and who consumes it, how the join → purchase → credential → rights-consumption → renewal cycle actually runs, and where the boundary lies against the neighboring §28 leaves (Sports Federation Management, Sports Eligibility Management, Sports Registration Platform) and against §25 Membership Management System / Certification Management and §28 Fitness Membership Management.

## Initial Boundary

- The leaf sits in §28 between Sports Federation Management (processed), Referee Management Platform (processed), Sports Eligibility Management (processed), and Youth Sports Management (unprocessed).
- Two prior passes left forward flags for this leaf:
  - Sports Federation Management pass: "membership" is the federation register's participant leg; "licensing" appears as certification/credential instruments. The dedicated membership/licensing Type (if distinct) centers the membership/licensing transaction itself; the federation platform centers the governance register that membership feeds.
  - Sports Eligibility Management pass: membership = belonging + dues; licensing = permission to practice a role; eligibility = the participation gate over a requirement set. "Narrow to the credential/dues relationship → Sports Membership / Licensing Platform."
- Working hypothesis: the Type centers the standing member/licensee relationship (dues + credential + rights), not the governance register, not the requirement-set gate, not the one-off signup transaction.
- Vocabulary risk: "licensing" could be misread as media/merchandise licensing (Media Rights Management exists in §27). The §28 context and market evidence (competition licences, race licenses, coach/official licenses) support the participant-license reading. Recorded as a taxonomy note.

## Research Questions

1. What is a "membership" in this context — what does the member buy, for how long, and what does it entitle?
2. What is a "license" — how does it relate to membership (fused or separate instrument)?
3. What does the credential look like (confirmation number, digital card, physical card) and who verifies it?
4. How does the purchase/renewal cycle work (self-service, auto-renewal, reminders, payment methods)?
5. How do fees split across the sport hierarchy (national + affiliate + club)?
6. What rights does the membership/license carry (compete, practice a role, benefits, insurance) and where are they consumed/enforced?
7. What role do waivers/consents/acknowledgements play at purchase?
8. Where is the boundary vs federation management, eligibility, registration, generic §25 membership management, fitness membership, certification management?

## Representative Products

Selection rationale: two platform vendors serving governing bodies (different regions, different philosophies) + three governing bodies operating their own member-facing membership/license systems (different sports, different structures: license-fused, license-graded, season-registration). Different customer tiers (platform B2B2C vs NGB direct-to-member).

1. **Sport:80** (UK/US platform vendor; serves 80–90+ NGBs incl. USA Track & Field, USA Cycling, USA Pickleball) — membership management as one feature of a governance platform; B2B + B2C membership; digital cards; certification/licence administration.
2. **revolutioniseSPORT** (Australian platform vendor; 260 governing bodies, 18,000 local clubs) — memberships as the lead pillar of a club/association platform.
3. **USA Cycling** (US NGB for cycling) — membership and race license combined into one purchase; license families (race / support-role / club / fan); runs on Sport:80.
4. **Motorsport UK** (UK governing body for motorsport) — competition licences with types and grades; free RS Clubman licence; membership + licence as related instruments; runs on Sport:80.
5. **USA Hockey** (US NGB for ice hockey) — season-based member registration with confirmation numbers, local program registry processing, role certifications; independent platform (not Sport:80).

**Sampling dependency note:** USA Cycling and Motorsport UK both operate on the Sport:80 platform (their member portals are sport80.com subdomains). Their membership/license structures are still each NGB's own configuration, but vendor-level mechanics (portal behavior) are shared. USA Hockey provides the independent-system control. British Cycling (the ideal benefits-led consumer membership sample) was unreachable (403 ×2) and was abandoned per the network rule.

## Sources

Fetched 2026-09-09:

- Sport:80 — https://www.sport80.com/ (root), https://www.sport80.com/features/membership-management, https://www.sport80.com/features/certification-management
- revolutioniseSPORT — https://www.revolutionise.com.au/ (root), https://www.revolutionise.com.au/platform-features
- USA Cycling — https://usacycling.org/membership (join/renew page with license catalog)
- Motorsport UK — https://www.motorsportuk.org/competitors/competition-licences/, https://www.motorsportuk.org/competitors/rs-clubman-licence/, https://www.motorsportuk.org/sport80-guide/
- USA Hockey — https://membership.usahockey.com/ (root), https://membership.usahockey.com/faq

Unreachable: British Cycling https://www.britishcycling.org.uk/membership (timeout ×1, then 403 ×2 — abandoned).

## Product Observations

### Sport:80 (platform vendor)

Evidence layer: A (directly observed on official product pages).

- Membership Management is a first-class platform feature: "Simplify Membership Registrations and Renewals"; payment options incl. credit/debit cards, Google/Apple Pay, Direct Debit; auto-renewal functionality; automated renewal reminders.
- "Seamless Member Management Across Your Entire Pyramid": individuals purchase Governing Body and club memberships; clubs, leagues, colleges and other affiliated bodies manage their affiliation — "grow your membership on a single platform."
- Capability list: multiple membership tiers; **3-in-1 membership (club, affiliated body, and governing body)**; configurable data collection; intelligent forms; waivers and collection of consents; digital membership cards (storable in mobile wallets); automated renewal reminders; member portal access; cross-sell and upsell items.
- Member portal: members "manage their sporting profiles, renew memberships, update qualifications, enter competitions, and track results."
- Membership Management FAQ distinguishes membership management software from CRM (member data/subscriptions/events vs customer interactions/sales).
- Certification Management (sibling feature): members upload certifications with validation; educational-pathway logic; **multi-layer dependencies** restrict certifications based on prerequisites (qualification history, valid background checks); public registries (coach finder) display only compliant members; automated invalidation for expired certifications; renewal reminders; sell course placements and certifications; approve/reject via email; LMS integration. The feature page explicitly says it administers "a variety of certifications, licences and awards."
- Membership Management page describes the audience split: "B2B members — clubs, leagues and regions — and B2C members — athletes, coaches, officials and supporters."

### revolutioniseSPORT (platform vendor, AU)

Evidence layer: A (directly observed).

- Root page: "memberships — We help take care of your most important asset." Clients: 260 governing bodies, 18,000 local clubs. Serves local clubs/associations, state/national sport bodies, and industry bodies.
- Platform features → memberships: "Membership data is your most critical asset"; one member profile; tailor your membership form; linked member profile photos; age verification capabilities; track ongoing participation; filtered demographic reporting.
- Finances pillar: collect & process payments online; auto-reconciliation; payment plans; export to MYOB/Xero.
- Competitions pillar includes "restrict participant eligibility" (the eligibility machinery — one feature among many; the membership pillar is separate).
- Governance tools: meeting minutes, motions/resolutions, incident reporting, granular administrator access.
- Observation: memberships are the data asset at the center; the platform is broader (events, shop, website, rostering). Membership product mechanics (categories/fees/renewal states) are not detailed on public pages — weaker evidence on product configuration depth.

### USA Cycling (NGB, license-fused pole)

Evidence layer: A (directly observed).

- "Your membership and race license are now combined into one, making your purchase even easier. If you'd like to add an additional license (for example, a commissaire license), you can do so manually at checkout." — membership and license fused into one purchase; additional role licenses added at checkout.
- License catalog organized in families:
  - **Race Licenses** (rider): Domestic U19 / U23 / Adult; International & Domestic UCI license "required for international or UCI-sanctioned events"; New Racer introductory licenses. "Joining USA Cycling gives you access to racing, ranking points, and our exclusive upgrade tracker… you'll be able to race in any sanctioned event."
  - **Support Licenses** (roles): Coach, Commissaire ("ensuring compliance and safety at sanctioned events"), Mechanic ("providing technical service at sanctioned events"), Team Director ("access to restricted race areas"), Race Director ("required to host sanctioned events"), Domestic Driving (MVR required), UCI Support.
  - **Clubs & Teams** (organization membership): Team, Junior Team, Interscholastic, Collegiate, Bike Shop — "register your club or team to gain access to insurance benefits, support resources, and official recognition."
  - **Fan Membership** (non-racing): "deals and discounts from 50+ industry partners via the member rewards portal," newsletter, store discount, members-only events.
- Pricing shows auto-renewal rate vs one-time purchase rate; 365 insurance add-on purchasable with license or standalone.
- Category upgrades exist as a member-facing process ("Category Upgrades" nav item; "upgrade tracker").
- Member portal at usacycling.sport80.com (Sport:80 deployment — dependency noted).

### Motorsport UK (NGB, license-graded pole)

Evidence layer: A (directly observed).

- "To compete in UK motorsport you will need a Motorsport UK Competition Licence." Grassroots: "you just need a free RS Clubman Licence and club membership." Higher events need "a higher grade of competition licence."
- "There are various different licence types, and grades within those licence types." Some grades "purchased off the shelf"; Race/Rally/Kart require buying a Starter Pack then passing a test (ARDS/BARS/ARKS). Upgrade Card records upgrade signatures toward higher grades.
- RS Clubman licence page: "In order to compete as a driver, co-driver, navigator, or passenger at Motorsport UK Clubman permitted events, an RS Clubman licence is necessary." RS Clubman members can compete in a range of disciplines, join local clubs, access the member benefits programme (discounts), receive the free digital member magazine. Criteria: medically fit, British citizen; "apply now and access your licence online immediately" (digital licence).
- Paid upgrade (£24.99) from digital-only to a physical personalised licence card + enhanced benefits (personal accident insurance at permitted events, retail discounts).
- Platform guide: "Our Motorsport Management platform, Sport:80, is your gateway to motorsport. It's where you can join as a member for the first time, take out a licence (to compete or volunteer), renew your licence year-on-year, access knowledge and training, explore your exclusive member benefits and more."
- Renewal guides per member class (competitors, marshals & officials); FAQs per class (competitors, RS Clubman, esports members, marshals, officials, clubs, club safeguarding officers, coaches).
- Licence machinery around the credential: medical requirements, replacement/lost/duplicate licences, Licence Suspensions Register, entrant licence (parent/guardian PG for under-18s).

### USA Hockey (NGB, season-registration pole, independent platform)

Evidence layer: A (directly observed).

- "Join as a player, coach, referee or volunteer" — season-scoped registration ("2026-2027 Season").
- "All participants must complete the USA Hockey registration process prior to participation in a USA Hockey sanctioned event."
- Registration completes in two stages: national purchase ("The USA Hockey fee and Affiliate fees, if applicable, are paid online with a credit card") + local processing ("Participant registration is complete when… the participant is processed by a USA Hockey member program" — confirmation numbers transmitted into the Local Program Registry by entering, scanning, or importing).
- The credential: a confirmation number ("a series of 9 numbers and 5 letters… different for each person, each season"), emailed immediately; duplicate confirmation retrievable by identity fields. "This receipt does not guarantee your membership in any local program or placement on a team."
- Waiver of Liability, Concussion Acknowledgement, SafeSport Policies Acknowledgement completed during registration; per-person self-registration required (parent/guardian for youth).
- Role machinery: coaches need the confirmation page to access SafeSport Training, Screening, Coaching Education; benefits pages describe coach certification and official certification requirements; background screening required for adults with youth access.
- Benefits by member class (all members / youth / parents / coaches / officials / adult players / administrators): insurance, magazine, playing rules, partner offers, national championship access, program-administration portal.
- Member Login: "Sign in to manage your existing USA Hockey membership."

## Cross-product Comparison

| Dimension | Sport:80 | revolutioniseSPORT | USA Cycling | Motorsport UK | USA Hockey |
|---|---|---|---|---|---|
| Operator posture | platform vendor serving NGBs | platform vendor serving clubs→NGBs | NGB direct (on Sport:80) | NGB direct (on Sport:80) | NGB direct (own system) |
| Membership product | multiple tiers; 3-in-1 (club+affiliated body+governing body) | membership forms/profiles; fees via finance pillar | license families: race / support roles / clubs / fan | licence types with grades; free RS Clubman; paid upgrade | season registration by role (player/coach/referee/volunteer) |
| License instrument | certifications/licences administered as sibling feature | eligibility restriction inside competitions | license fused with membership; role licenses at checkout | licence = the central instrument; membership wraps it | registration confirmation = participation credential; role certifications attached |
| Credential | digital membership cards (mobile wallets) | member profile (photos) | license purchase → race rights | digital licence, physical card upgrade | confirmation number (per person, per season) |
| Renewal | auto-renewal + reminders | payment plans; ongoing participation tracking | auto-renewal rate vs one-time | "renew your licence year-on-year"; renewal guides | per-season re-registration; member login |
| Rights carried | compete/enter events via portal | participate (eligibility-restricted) | race in sanctioned events; ranking points; role practice | compete at permitted events by grade | participate in sanctioned events; role training access |
| Benefits | cross-sell/upsell | shop, events, communications | partner discounts, newsletter, insurance add-on | benefits programme, magazine, insurance upgrade | insurance, magazine, partner offers by class |
| Hierarchy fees | 3-in-1 across pyramid | club↔state/national structure | (not surfaced on page) | club membership separate from licence | USA Hockey fee + Affiliate fees in one transaction |
| Enforcement | registries show only compliant members | restrict participant eligibility | race in sanctioned events requires license | licence checked at permitted events; suspensions register | registration required prior to sanctioned participation; local registry processing |
| Waivers/consents | waivers and consents collected | (not surfaced) | (not surfaced on page) | (not surfaced on page) | waiver + concussion + SafeSport acknowledgements at registration |

## Canonical Model (working)

```text
Sports organization (governing body / association / club network)
└── Member (identified person; commonly also organizations — clubs/teams)
    └── Membership / license product (category by role/age/discipline × term × fee × entitlements)
        ├── purchased & renewed through self-service (payment; auto-renew; reminders)
        ├── produces a credential (confirmation number / digital card / licence card)
        │   └── carries defined rights (compete in sanctioned activity / practice a role / benefits / insurance)
        └── consumed & verified at the point of use (sanctioned events, local programs, public registries)
```

## Abstraction Levels

### L0 — Defining Invariant

Three jointly-held structures:

1. **The standing member/licensee relationship of record** — an identified person (or organization) holds a renewable relationship with a sports organization, defined for a term (season/annual), maintained by renewal. Remove → a one-off signup transaction (Sports Registration Platform) or a contact list.
2. **The purchasable membership/license product** — the organization defines purchasable categories (by role, age, discipline) each with a fee and defined entitlements, bought and renewed through the platform. Remove → a CRM with no product structure.
3. **The rights-carrying credential** — the purchase/renewal produces an artifact (number, digital card, licence card) that evidences the standing relationship and carries defined rights — to compete in sanctioned activity, to practice a role, to access benefits — which are consumed/verified at the point of use. Remove → a billing relationship with no operational meaning.

Jointly-held load-bearing: (1 alone = dues/billing list; 2 alone = product catalog; 3 without 1+2 = credential with nothing behind it; 1+2 without 3 = subscription with no evidence of rights; 1+3 without 2 = ad-hoc credentialing; 2+3 without 1 = one-off license purchase with no standing relationship — drifts to registration).

### L1 — Common Mature Structure

- Self-service member portal (profile, membership status, renewals, qualifications)
- Online payment (cards, wallets, direct debit), auto-renewal, automated renewal reminders
- Digital membership cards (mobile wallets); physical card fulfillment in some products
- Role-structured license families (competitor / coach / official / volunteer) alongside or fused with membership
- Waivers, consents, policy acknowledgements collected at purchase
- Insurance attached to membership (or as add-on)
- Member benefits program (partner discounts, magazine, members-only access)
- Age verification / demographic data collection at purchase
- Hierarchy fee collection (national + affiliate/regional + club in one transaction)
- Renewal communications per member class
- Membership reporting (demographics, retention, revenue)

### L2 — Variant / Optional Structure

- License grades with upgrade paths and test/prerequisite gates (Motorsport UK grades + ARDS/BARS/ARKS tests; USA Cycling category upgrades)
- Free entry-level licenses (RS Clubman free licence)
- Paid physical-card / enhanced-benefit upgrade tiers (Motorsport UK £24.99 upgrade)
- Local-program validation stage after national purchase (USA Hockey Local Program Registry)
- Organization membership (clubs/teams as members — USA Cycling Clubs & Teams; Sport:80 B2B members)
- Non-participant supporter/fan membership (USA Cycling Fan Membership)
- Course/education sales tied to licensing (Sport:80 sell course placements)
- Safeguarding/background-check requirements attached to roles (USA Hockey screening; Sport:80 prerequisites)
- Payment plans / installments (revolutioniseSPORT)
- Public compliance registries / coach finders (Sport:80)
- Suspension/lapse machinery (Motorsport UK Licence Suspensions Register; Sport:80 automated invalidation)

### L3 — Vendor-specific (research notes only)

- Sport:80's "3-in-1 membership" packaging label; Memberwise/ISO badges; specific feature names.
- USA Cycling's specific prices ($40 U19 … $220 UCI), 365 insurance product, "Encyclingpedia" content brand.
- Motorsport UK's grade names (RS Clubman, RS Inter Club, K-I/K-X), £24.99 upgrade price, Halfords/Tastecard/Pirelli benefit partners, 10-day dispatch claim.
- USA Hockey's confirmation-number format (9 numbers + 5 letters), April registration-opening date, specific staff contacts.
- revolutioniseSPORT's MYOB/Xero export, cog logo, award listings.

## Vendor-specific Findings

- The "membership and race license are now combined into one" fusion is USA Cycling's current packaging (their own announcement); Motorsport UK keeps membership and licence as related-but-separate instruments ("join as a member… take out a licence"); USA Hockey's registration is the participation credential without a separate "license" vocabulary. → The fusion vs separation of membership and license is a variant axis, not the invariant.
- License grades with mandatory tests (ARDS/BARS/ARKS) are Motorsport UK-specific depth; USA Cycling expresses progression as category upgrades; USA Hockey as certification requirements. → Graded licenses are L2.
- The two-stage national-purchase → local-program-processing flow is documented in detail only at USA Hockey; other products imply single-stage activation. → Held as a variant (hierarchical enforcement), not invariant.
- Sport:80's B2B/B2C member split and 3-in-1 membership is vendor packaging of the hierarchy-fee pattern that USA Hockey shows natively (USA Hockey fee + Affiliate fees).

## Boundary Findings

### vs Sports Federation Management (processed)

The federation platform centers the **governance register**: member organizations with affiliation status/approval, participants bound to them, and authority instruments (sanctioning, discipline, certification at governing-body scale). The membership/licensing platform centers the **member relationship itself**: purchasable products, purchase/renewal, credential, benefits, rights consumption. Overlap is real — federation platforms include a membership module (Sport:80 sells both; the federation pass sampled SportyHQ membership enforcement), and membership platforms may carry club affiliation (Sport:80's pyramid). Directional test: strip the governance register (affiliation approval, sanctioning, discipline) → this Type; add the org register + authority instruments as the center → federation management. Evidence for keep-both: pure-play membership/license realizations exist without governance machinery (USA Hockey's registration portal is membership-first with no affiliation-approval machinery surfaced; Motorsport UK's licence system centers the licence, with club recognition handled separately).

### vs Sports Eligibility Management (processed)

Eligibility = the standing participation gate over a requirement set (evidence, evaluation, status). Membership/licensing = the paid standing relationship + credential. Overlap at the input layer: membership is commonly an eligibility input; graded licenses with test prerequisites resemble requirement sets (Motorsport UK ARDS test; USA Hockey coach certification). Directional test: narrow to the dues/credential relationship → this Type; add requirement-set evaluation machinery as the center → eligibility. The eligibility pass's own directional test ("narrow to the credential/dues relationship → Sports Membership / Licensing Platform") is discharged from this side.

### vs Sports Registration Platform (unprocessed sibling)

Registration = the signup transaction (one-off, per program/event/season). Membership = the standing renewable relationship with credential and benefits. USA Hockey shows the seam inside one system: the registration purchase produces a confirmation number that feeds the local registry — but the standing layer (member login, next-season renewal, benefits, role certifications) is the membership layer. Forward flag recorded for that pass: remove the standing renewal relationship → registration platform; add it → this Type.

### vs Membership Management System (§25, unprocessed)

Generic membership software manages dues, members, renewals for any member-based organization. The sports layer is what makes this Type: the membership/license carries participation and role rights in a governed sport, enforced at sanctioned activity; hierarchy fee splitting across sport bodies; role licenses (coach/official); sport-specific compliance attachments (safeguarding, medical). A sports body with thin needs can run on generic AMS (the federation pass observed this) — the sports-governance semantics, not "membership" as such, are the center. Forward flag for that pass: the generic pole belongs to §25; this leaf holds the sports-governance-specific layer.

### vs Fitness Membership Management (§28, processed)

Commercial fitness membership = facility-access subscription sold by a business to consumers. Sports membership/license = governing-body relationship conferring participation/role rights in a governed sport. Different center (access vs participation rights), different operator (business vs governing authority). The fitness pass's log already listed this leaf as unprocessed-adjacent; no conflict.

### vs Certification Management (§25, processed)

Certification management = credential program over persons (qualification, eligibility-gated application, assessment, recertification). In sports platforms, certification tracking is a sibling capability (Sport:80 ships Membership Management and Certification Management as separate features — vendor-side corroboration of the seam). The license-to-practice pole (coach/official license) overlaps; but this Type's center is the dues relationship + participation license, not the qualification program. Where a sports body's coach licensing becomes a full qualification program with CE/recertification machinery, Certification Management territory begins.

### vs Government Licensing Management (§24)

Hunting/fishing licenses are government-issued regulatory permissions. Sports licenses are private-authority instruments issued by governing bodies. Different operator and legal basis. No overlap beyond vocabulary.

### vs Member Portal (§25)

The portal is a surface; this Type is the relationship system of record. Portals appear here as the primary interface (L1), not the center.

## Historical / Market-Sample Check

- **Paper-era club:** the annual membership subscription book + membership card — standing relationship, defined annual product (dues), card as credential conferring access to club activities. Satisfies all three L0 legs with no software. Passes.
- **Paper-era federation licence:** the competition licence card (e.g., motorsport/football registration cards) — purchased annually, graded, checked at events before participation; the physical card is the credential. Satisfies all three legs; the card is the artifact leg. Passes.
- **Regional:** samples span UK (Motorsport UK, Sport:80 UK heritage), US (USA Cycling, USA Hockey), AU (revolutioniseSPORT). The abstract core (dues + credential + rights) describes non-sampled regions' NGB membership systems conceptually, but no non-sampled-region product was fetched. Recorded as a limitation, not a boundary failure.
- **Older software generations:** desktop membership databases with printed cards and renewal letters satisfy the core without portals, wallets, or auto-renewal. Passes.

## Uncertainties

- British Cycling unreachable (403 ×2) — the benefits-led consumer-membership pole is evidenced indirectly (USA Cycling Fan Membership; Motorsport UK RS Clubman benefits programme) but no dedicated benefits-first membership product was sampled. Assertion strength on benefits-led variants kept moderate.
- revolutioniseSPORT's membership product mechanics (category configuration, renewal states) are not detailed on public pages — held weaker; no precise claims rest on it.
- Exact renewal windows, proration, refund policies, and grace periods were not researched — no precise values asserted anywhere.
- Whether the two-stage national→local activation flow (USA Hockey) is common across US NGBs is not established — held as a documented variant.
- The depth of license-grade machinery (tests, upgrade signatures) is evidenced at Motorsport UK only — held as variant, not common structure.
- Sampling dependency: two of five samples run on Sport:80. Portal-level mechanics are shared across those two; the NGB-level structures (license catalogs, grades, confirmation flows) are each organization's own.

## Final Synthesis

Sports Membership / Licensing Platform is the sports organization's member-relationship system of record. Its world: identified members — individual participants (athletes, coaches, officials, volunteers, supporters) and commonly organizations (clubs, teams) — hold standing, renewable relationships with the organization, defined by purchasable membership/license products (categories by role, age, discipline; terms; fees; entitlements). Purchase and renewal run through self-service with payment (auto-renewal and reminders common), collecting waivers/consents and demographic data at the point of sale. The relationship is evidenced by a credential — confirmation number, digital card, physical licence card — that carries defined rights: to compete in sanctioned activity, to practice a role (coach, official, mechanic, volunteer), and to access member benefits (insurance, partner discounts, content). Those rights are consumed and verified at the point of use — sanctioned events, local programs, public registries. Around that spine, mature products add the member portal, role-structured license families, license grades with prerequisite gates, hierarchy fee collection across the sport pyramid, insurance and benefits programs, compliance registries, and renewal communications per member class. The Type is defined by the dues-plus-credential relationship, not by any one instrument: remove the standing renewable relationship and it is a registration platform; remove the purchasable product structure and it is a CRM; remove the rights-carrying credential and it is a billing relationship; add the governance register over member organizations and authority instruments and it is federation management; add requirement-set evaluation machinery and it is eligibility management.
