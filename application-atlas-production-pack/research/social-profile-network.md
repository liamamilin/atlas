# Research Notes — Social Profile Network

## Research Goal

Understand what real products exist whose center of gravity is the **personal profile itself** — not a content feed, not an organizational channel — and determine whether "Social Profile Network" is a defensible independent Application Type, an alias, or a substrate capability.

This pass also discharges a standing request from the general-social-network and microblogging passes (§01.05 family): the leaf was provisionally defined from those sides by a removal test ("remove the post stream + feed → profiles + connections, a people directory") and this pass was asked to **ratify or replace** that definition with first-hand product evidence.

## Initial Boundary

- Neighboring Types: General Social Network, Professional Social Network, Friend Discovery Application, Member Directory, Identity Verification, Customer Identity / CIAM, Directory Application.
- Working hypothesis: the leaf names products where the **profile is the primary object of record and the primary consumption surface**, and where the profile is designed to be consumed *outside* the product itself. If no such product population exists, the leaf is a substrate/capability, not a Type.
- The provisional sibling definition ("profiles + connections directory") needed testing: do real profile-centric products actually carry person-to-person connection graphs?

## Research Questions

1. What is the unit of record — what does a "profile" hold, who owns it, how is it identified?
2. Is there a shared namespace / addressability layer (handle, iD, URL slug, email hash)?
3. Is the profile consumed inside the product only, or designed for consumption elsewhere (embedding, APIs, sharing, verification)?
4. Do these products carry person-to-person connection graphs (the "network" leg of the provisional definition)?
5. What is the primary consumption loop — browsing profiles, or consuming a stream?
6. Where is the boundary vs a social network's built-in profile page, vs an identity registry, vs a contact manager?

## Representative Products

Selected for market representativeness, documentation quality, and deliberately different product philosophies and customer tiers:

| Product | Pole / philosophy |
|---|---|
| ORCID | scholarly identity registry — persistent identifier + record connected to works and affiliations; non-profit infrastructure |
| Gravatar | global profile layer — email-keyed profile consumed across millions of third-party sites via API |
| Linktree | link-in-bio — the profile as a hub page consumed inside other platforms' bios |
| HiHello | digital business card — profile card exchanged person-to-person, exchanged cards stay live-synced |
| Lens Protocol | decentralized social-graph protocol — profile + follow graph owned on-chain, consumed by many frontends |

## Sources

Live WebFetch of vendor help centers timed out repeatedly on 2026-09-10 (support.orcid.org, help.linktr.ee, gravatar.com/support all failed). Evidence was instead obtained via web search returning content from the **official** vendor domains (support.orcid.org, info.orcid.org, orcid.org, linktr.ee, help.linktr.ee, support.gravatar.com, docs.gravatar.com, api-v2-docs.lens.xyz, contracts-v2-docs.lens.xyz, github.com/lens-protocol, support.hihello.com). This is official-source content but retrieved as search excerpts, not full-page reads — assertion strength is calibrated accordingly and no precise numeric/limit claims are made from it.

## Product Observations

### ORCID (evidence layer A — official support/about pages, search-retrieved)

- ORCID provides "a persistent digital identifier (an ORCID iD) that distinguishes you from other researchers and a record that supports automatic links among all your professional activities. Your ORCID iD and connections are stored in the ORCID Registry, in an account you own and manage."
- The iD is a name-independent person identifier solving name ambiguity; the holder maintains and updates the record, controls sharing/privacy settings, and can search the Registry.
- The record connects the person to **contributions and affiliations** (works, funding, employment) — often populated automatically by member organizations via APIs ("nearly six thousand systems now using ORCID iDs" per vendor).
- **No person-to-person social ties.** The "connections" in ORCID's own language are links between the iD and contributions/affiliations/other identifiers (PIDs), not friend/follow edges.
- The profile is explicitly designed for consumption elsewhere: presented in manuscript submission, grant application, institutional profile pages, email signatures.

### Gravatar (evidence layer A — official support/developer docs, search-retrieved)

- "Gravatar (Globally Recognized Avatar) is a service that allows users to create profiles linked to their email addresses. These profiles are used across millions of sites, providing consistent avatars and user identity."
- Profile data model (official API docs): hash of primary email as universal identifier, display name, profile URL, avatar, location, description, job title, company, verified accounts, pronouns, languages, links.
- The email hash "is the foundation of all Gravatar functionality… Email, the ultimate username" — addressability is by email hash / profile URL slug in a shared namespace (gravatar.com/ slug).
- Consumption is overwhelmingly **outside** the product: third-party sites fetch avatar + profile data by hash via a public API; the vendor frames it as solving the "Cold Start Problem" for other services' user profiles, "like bringing a digital business card to every site."
- Profile pages exist on gravatar.com and are public; verified social-media accounts link the profile outward to other identity surfaces.
- **No person-to-person connection graph.**

### Linktree (evidence layer A — official site + help center, search-retrieved)

- "A link in bio is a single URL in your social media profile that opens a page of curated links to your content, products, and channels."
- The product IS a profile page: username-addressable URL (linktr.ee/username), profile picture, title, bio description, curated links, theme/design.
- The entire consumption model is external: the URL is pasted into Instagram/TikTok/LinkedIn/YouTube bios and email signatures; the profile exists to be consumed from other platforms' profile surfaces.
- Editing loop: add/reorder links, customize design, view click analytics.
- **No person-to-person connection graph**; the audience relationship lives on the other platforms.

### HiHello (evidence layer A — official help center, search-retrieved)

- Digital business card platform: the user's card is a profile (name, title, company, contact details, branding) hosted on the vendor's servers, shareable via QR code, text, email.
- **Person-to-person linkage exists here**: "When you exchange digital business cards with another HiHello user, you become Live Contacts… Any time you update your card, that information will automatically be updated for all of your live contacts." Exchanged cards form a live-synced connection graph between profiles.
- Contact manager ("Self-Healing Address Book") holds the inbound copies; team/enterprise plans add admin profiles, card templates, CRM integrations.
- The profile is again designed for consumption elsewhere: shared into other people's address books, email signatures, CRM systems.

### Lens Protocol (evidence layer A — official contract/API/SDK docs, search-retrieved)

- "The Lens Protocol is a decentralized, non-custodial social graph… participants own their own social graph."
- Profile is the primary on-chain object: "Profiles are the accounts that create publications and are owned by wallets"; creating a profile mints a Profile NFT; a handle is bound to the profile in a shared namespace.
- Follow relationships are first-class protocol objects (Follow NFT minted on follow; follow modules can gate follows, e.g. fee-gated); block/mute operations exist between profiles; profile stats (followers/following) are protocol data.
- The protocol deliberately separates the **social graph substrate** (profiles + follow graph) from any frontend: many apps consume the same profiles and graph.
- Publications/feeds exist in the ecosystem, but at the protocol level the profile + follow graph is the owned, portable unit.

## Cross-product Comparison

| Structure | ORCID | Gravatar | Linktree | HiHello | Lens |
|---|---|---|---|---|---|
| Persistent personal profile of record, owner-controlled | ✓ (record in Registry) | ✓ (profile on account) | ✓ (page on account) | ✓ (card on account) | ✓ (Profile NFT) |
| Shared-namespace addressability | ✓ (ORCID iD) | ✓ (email hash / slug) | ✓ (username URL) | ✓ (hosted card URL/QR) | ✓ (handle) |
| Designed for consumption outside the product | ✓ (APIs, 6000 systems) | ✓ (API/embed across sites) | ✓ (link pasted into other bios) | ✓ (card shared/synced out) | ✓ (many frontends) |
| Person-to-person connection graph | ✗ | ✗ | ✗ | ✓ (Live Contacts) | ✓ (follow graph) |
| Content feed / stream as primary surface | ✗ | ✗ | ✗ | ✗ | ✗ (protocol-level; frontends add feeds) |
| Verification of the person | ✓ (community/registry governance) | ✓ (verified accounts) | ✗ | ✗ | partial (on-chain identity integrations) |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

Three jointly-held structures:

1. **Personal profile of record** — a persistent, owner-controlled profile bound to one person, held in the application's own registry (not a transient form, not a settings page inside someone else's product).
2. **Shared-namespace addressability** — the profile carries a stable identifier (iD, handle, slug, hash-keyed URL) in a namespace shared across the user population, by which other people *and other systems* can find and reference it.
3. **Outward consumption design** — the profile is built to be consumed outside the application itself: embedded, linked, shared, verified, or synced into other surfaces and systems. The product's success metric is the profile's circulation, not time spent in a feed.

Remove (1) → an identity-assertion service with no user-maintained record (identity-verification territory). Remove (2) → a private account page (a capability of any product, not a Type). Remove (3) → just another product's internal profile page (capability, not Type). All three together, with profile consumption as the primary loop, is what makes the Type.

### L1 — Common Mature Structure

- Profile content model: display name, avatar/image, bio/description, role/affiliation, location, links.
- Verification linkage: verified accounts / institutional connections attaching external trust to the profile.
- Profile search / directory browsing over the namespace.
- Privacy / visibility controls over profile fields.
- Analytics on profile consumption (views, clicks) where the profile is audience-facing.

### L2 — Variant / Optional Structure

- **Person-to-person connection graph** — present in only 2 of 5 sampled products (HiHello Live Contacts, Lens follow graph). NOT definitional. This refines the provisional sibling definition: the "network" leg is better abstracted as *linkage into a wider identity web* (to systems, works, accounts, exchanged cards, followers) than as a mandatory social graph.
- Identity substrate: email hash, scholarly iD, username, on-chain wallet-owned NFT.
- Governance model: non-profit registry (ORCID), corporate SaaS (Linktree/HiHello), open protocol (Lens).
- Monetization/business model: membership-funded infrastructure, freemium SaaS, protocol tokenomics.
- Feed/publication layers built on top (Lens frontends) — variant, and where they dominate, the product drifts toward a feed-centered social Type.

### L3 — Vendor-specific

- ORCID's 16-digit checksummed iD structure, member-organization API tiers, trust/sandbox infrastructure.
- Gravatar's SHA256 email-hash URL scheme, avatar rating system.
- Linktree's specific commerce/shops modules, auto-reply, QR generator.
- HiHello's admin-vs-personal profile split, self-healing address book branding, CRM integrations.
- Lens's Follow NFT delegation/governance-power mechanics, guardian/cooldown account recovery.

These stay in Research Notes.

## Vendor-specific Findings

See L3 above. None promoted to the canonical document.

## Boundary Findings

- **vs General Social Network**: the general SNS's core consumption loop is a content stream over a self-curated graph; here the core consumption loop is **profile lookup/viewing and profile circulation**. Remove the profile-of-record primacy and outward-consumption design → general social network. Remove the stream from a general SNS and what remains is exactly this Type's substrate — which is why the sibling passes provisionally named it the "substrate sibling."
- **vs Professional Social Network**: professional SNS centers an audience/context (career) with a feed and recruiting machinery; a profile network has no feed and no audience-specific workflow — the profile is the whole product.
- **vs Member Directory**: member directories are organization-scoped rosters maintained (largely) by the organization; here the profile is self-maintained by the person and the namespace is public/cross-org.
- **vs Identity Verification / KYC**: those assert real-world identity against documents; here the profile is **self-authored** presentation, with verification only as an optional trust attachment.
- **vs Customer Identity / CIAM**: CIAM is authentication/authorization infrastructure; here there is no access-control contract — the profile is presentation and circulation.
- **vs Contact Manager**: the contact manager holds *your inbound copies* of other people's details; the profile network holds *the person's own record of themselves*. HiHello interestingly bundles both (card + address book), with the card/profile as the anchor.
- **Removal test vs the §01.05 family**: remove the update stream + feed from a social network → profiles + linkage. That substrate, standing alone as the product, is this Type. **Ratified with refinement**: the "connections" leg is not necessarily a person-to-person graph; the load-bearing structure is the profile's addressability and outward circulation.

## Uncertainties

- Live full-page fetches failed; evidence is from official-domain search excerpts. Product-specific details (exact field lists, plan limits, API quotas) were deliberately not promoted.
- About.me (the classic consumer profile-page product) was not sampled; its current operational state is unclear. The historical form it represents (standalone profile page + directory) is covered conceptually by Linktree/Gravatar poles.
- Whether the market *names* this category ("link-in-bio", "digital business card", "identity registry") rather than "social profile network" — the directory leaf's name does not match any vendor category name; the Type is real but the label is an atlas coinage. Recorded as a taxonomy note, not changed unilaterally.
- Lens frontends blur into feed-centered social products; the protocol-level sample was used deliberately to keep the substrate visible.

## Historical / Market-Sample Check

Would older, differently-positioned products still fit the refined definition? Yes: early-2000s Gravatar (avatar-only profiles keyed to email, consumed across blog platforms), the early-2010s standalone profile-page products (About.me-class: one self-authored page at a username URL, browsed as a directory), and the paper business card that the digital-card pole explicitly digitizes all satisfy the three-structure core without feeds, follow graphs, analytics, or on-chain ownership. The Type is older than its current market labels; the historical check passes and confirms the connection graph must not sit in the defining core.

## Final Synthesis

The leaf is **ratified as an independent Type with a refined definition**. The provisional "profiles + connections directory" framing from the sibling passes is correct in direction but over-specifies the connection graph: across the sample, person-to-person ties are the minority structure, while **profile-of-record + shared-namespace addressability + outward consumption design** are jointly held by all five products across five very different philosophies. The defining core is the profile as a portable, addressable identity object whose consumption happens largely outside the product. The Type stands between social networks (which embed profiles as one surface among feeds) and identity infrastructure (which asserts or authenticates identity without presenting a self-authored profile).
