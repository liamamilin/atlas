# Research Notes — Privacy-focused Browser

Research date: 2026-09-08
Methodology: v1.1 (update-v1/)

> **Source-access limitation (dominant constraint of this pass).** Live fetch of official
> documentation failed for every attempted source in this environment:
>
> | Source | URL attempted | Attempts | Result |
> |---|---|---|---|
> | Tor Browser Manual | tb-manual.torproject.org (/about/, /) | 2 | timeout |
> | DuckDuckGo Help Pages | duckduckgo.com/duckduckgo-help-pages (root + desktop/browser) | 2 | timeout |
> | Mullvad Browser | mullvad.net/en/help/what-mullvad-browser, /en/browser | 2 | timeout |
> | Brave | support.brave.com (Shields article), brave.com/privacy-features/ | 2 | timeout |
> | Wikipedia (Tier-3) | en.wikipedia.org/wiki/Tor_Browser, /Brave_(web_browser) | 3 | timeout |
> | Mozilla Support (boundary pole) | support.mozilla.org ETP article | 1 | JS client challenge (blocked) |
>
> A control fetch (example.com) succeeded, so the environment has network access but the
> target hosts are unreachable/blocked. Per the source-access limitation rule: the
> limitation is recorded, assertion strength is reduced, and **no precise operational
> facts (numeric limits, exact default values, exact toggle/level names, list contents)
> are asserted from model memory.** All product observations below are therefore
> **evidence-degraded**: they rest on well-established, structural, long-public
> background knowledge of these products, not on documents fetched this session. They
> are marked **[B/bg]** (cross-product background commonality) or **[C/bg]** (canonical
> inference from background comparison). Nothing in this pass qualifies as Layer A
> (directly observed from a fetched official source). The final document is written to
> the same calibration, and its Sources section records the limitation.

## Research Goal

Understand what a Privacy-focused Browser is as an Application Type: what its defining
structure is, how the privacy machinery actually enters the browsing path, how it
differs from a mainstream Web Browser that merely offers privacy *settings*, and where
the boundary with adjacent Types (Web Browser, Browser Security Platform, VPN, content
blockers, Web Archive Viewer) lies.

## Initial Boundary

- Hypothesis before research: a browser whose **defining differentiator** is that
  user-privacy protection is a **structural, default-on component of the browsing
  path**, plus a **data-minimization posture** over the user's own browsing record —
  not a general browser with optional privacy features.
- Nearest neighbors: Web Browser (shares the entire browsing substrate), Browser
  Security Platform (enterprise security layer over browsing/traffic), VPN (network
  tunnel, no page semantics), ad/tracker blockers (no browsing substrate), Web Archive
  Viewer (historical snapshots, not live browsing).
- Key taxonomy risk: this leaf could be only a positioning Variant of Web Browser.
  The research must decide whether the privacy machinery is a genuine defining
  structure (→ distinct Type) or mere marketing packaging (→ Variant).

## Research Questions

1. What does the privacy machinery concretely consist of in real products — at which
   layer does it operate (request, storage, identity surface, transport, network)?
2. Is the machinery default-on and structural, or optional configuration? How does that
   distinguish the Type from a mainstream browser's private/incognito mode?
3. What does the product do with the user's *own* browsing record (history, cookies,
   cache) by default? Is an account required? What erasure affordances exist?
4. What is shared with the Web Browser substrate (tabs, address bar, bookmarks,
   downloads, extensions) and what is additive?
5. Which strategies vary: tracker blocking, cookie partitioning/purging, fingerprinting
   resistance, HTTPS upgrading, anonymity-network routing, private search bundling?
6. What business models and vendor postures exist (nonprofit, VPN company, search
   company, ad/rewards economy) and do any of them leak into the definition?
7. Would older / differently-positioned products still satisfy the definition
   (historical / market-sample check)?
8. Where exactly is the seam with Web Browser, Browser Security Platform, VPN, and
   Web Archive Viewer?

## Representative Products

Chosen for market representativeness, documentation tradition, philosophy spread, and
audience spread (all consumer, but different tiers of privacy need):

| Product | Philosophy / pole | Audience tier |
|---|---|---|
| **Brave** | mainstream-consumer privacy browser; Chromium-based; protection + opt-in ads/rewards economy | mass consumer |
| **Tor Browser** | anonymity maximalism; Firefox-based; all traffic through the Tor network | high-sensitivity users (journalists, activists) |
| **DuckDuckGo Private Browser** | simplicity-first consumer privacy; bundled private search; minimal configuration | mass consumer |
| **Mullvad Browser** | anti-fingerprinting maximalism; Firefox-based; goal of blending into the Tor Browser user population | privacy maximalists without network anomaly |

**Boundary pole:** **Firefox** — a mainstream general-purpose browser with a
substantial privacy feature set (enhanced tracking protection, private browsing
windows). Used only to locate the seam; not a sample of this Type.

## Sources

Research date: 2026-09-08. **No official source could be fetched this session** (see
limitation notice at top). The URLs below are the canonical official documentation
surfaces for the sampled products, recorded for future re-verification; all claims in
this pass are calibrated to background-knowledge strength, not to these URLs:

- Brave — support.brave.com (Help Center), brave.com/privacy-features/
- Tor Browser — tb-manual.torproject.org (official manual), torproject.org
- DuckDuckGo — duckduckgo.com/duckduckgo-help-pages (official help)
- Mullvad Browser — mullvad.net/en/help, mullvad.net/en/browser
- Firefox (boundary pole) — support.mozilla.org

## Product Observations (evidence-degraded: background knowledge, structural level only)

### Brave [B/bg]

- Chromium-based browser whose product identity centers on the built-in "Shields"
  protection layer, on by default, operating on the page-load path: blocking of
  third-party ads/tracker requests, cookie control, upgrading/forcing HTTPS where
  possible, and fingerprinting mitigation via randomized perturbation of browser-API
  surfaces (vendor term: "farbling" — vendor-specific vocabulary).
- A per-site shield panel surfaces what was blocked and allows per-site weakening
  (exceptions) when a page breaks.
- Data posture: browsing record (history, bookmarks, settings) persists locally;
  optional sync exists that does not require an email/account identity (sync-chain
  passphrase model) — structural claim only, no operational details asserted.
- Private windows exist; a private-window-with-Tor mode routes that window's traffic
  through the Tor network — anonymity-network routing is an *option*, not the default
  posture.
- Bundled economy: opt-in private-ad "Rewards" system with a creator/token economy, a
  built-in crypto/Web3 wallet, customizable new-tab content. Product additions, not
  part of the privacy machinery (vendor-specific).
- Vendor advertises not building user profiles from browsing. Not verified this
  session.

### Tor Browser [B/bg]

- Firefox-ESR-based browser produced by the Tor Project in which **all traffic is
  routed through the Tor anonymity network** by default — the network layer itself is
  part of the privacy machinery. This is the defining, universally documented property
  of the product.
- Hardening on top of the network: limiting of browser surfaces usable for
  fingerprinting and active attacks; a small number of named, user-selectable security
  levels that progressively disable risky web features; first-party isolation so that
  state (cookies/storage) does not leak across different sites.
- Session posture: ephemeral by default — no persistent browsing history written;
  full-identity reset and per-activity circuit-change affordances are first-class
  surfaces (vendor terms: "New Identity", "New Tor circuit" — vendor-specific labels).
- Fingerprinting strategy: **uniformity** — making users look like other Tor Browser
  users (including window letterboxing), rather than randomizing per session.
- No account, no sync; no bundled economy; nonprofit/NGO provenance.

### DuckDuckGo Private Browser [B/bg]

- Consumer-simplicity pole: a browser whose protection is always-on by default and
  whose settings surface is deliberately shallow — "privacy without configuration".
- Built-in blocking of third-party trackers (vendor markets its tracker knowledge base
  as "Tracker Radar" — vendor-specific term), cookie-consent-popup handling, and HTTPS
  upgrading are the core machinery layers.
- A one-action data-erasure control (vendor label: "Fire" button) is a first-class
  surface: clear tabs and browsing data in one gesture.
- Bundled private search engine as the default search source; the search product and
  the browser are one brand posture.
- Mobile-first heritage (app-store distribution, desktop client added later); on
  Android, an OS-level app-tracking feature extends the posture beyond the browser
  (adjacent capability, vendor-specific).
- Normal network routing (no Tor/anonymity layer); local data posture; no account
  required to browse; the vendor is a search company whose privacy positioning spans
  both products.

### Mullvad Browser [B/bg]

- Firefox-ESR-based browser produced with the Tor Project, explicitly designed so that
  its fingerprinting surface **blends into the Tor Browser user population** —
  fingerprint uniformity without forcing traffic through the Tor network (avoiding the
  speed/exit-node trade-off for users who do not need network anonymity).
- Built-in content/tracking blocking; ephemeral-by-design data posture (no persistent
  history); no account, no telemetry, no bundled economy; desktop-only.
- The vendor is a VPN company; the browser is deliberately stripped of cloud services
  — the anti-service posture itself is part of the product philosophy.

### Firefox (boundary pole, not a sample) [B/bg]

- General-purpose browser with a substantial, partially default-on privacy stack
  (enhanced tracking protection with standard/strict postures, private windows, cookie
  isolation work). Positioned and marketed as a general browser for everyone, with
  privacy as one important feature among many, not as the defining posture.
- Illustrates the seam: the difference from the sampled Type is not the existence of
  privacy technology but (a) whether protection is the product's defining, default-on
  structural posture and (b) whether the product's whole data posture (record keeping,
  accounts, services) is minimized around that posture.

## Cross-product Comparison

| Dimension | Brave | Tor Browser | DuckDuckGo Browser | Mullvad Browser |
|---|---|---|---|---|
| Engine base | Chromium fork | Firefox ESR fork + Tor integration | Chromium-based (WebKit on iOS per public descriptions) | Firefox ESR fork (same base as Tor Browser) |
| Protection default state | default-on, per-site adjustable | default-on, fixed posture | default-on, minimal config | default-on, fixed posture |
| Request-level tracker/ad blocking | built-in (Shields) | not the primary mechanism (network routing + hardening instead) | built-in (tracker knowledge base) | built-in |
| Storage/cookie handling | blocking, control, partitioning-style behavior | first-party isolation, ephemeral | blocking + consent-popup handling + erasure | ephemeral-by-design |
| Fingerprinting strategy | randomization/perturbation | uniformity (blend into Tor population) | limited surfaces (weakest of the four) | uniformity (blend into Tor population) |
| Transport | HTTPS upgrading where possible | end-to-end through overlay network | HTTPS upgrading | HTTPS upgrading |
| Network layer | normal network (Tor optional in special window) | Tor network always | normal network | normal network |
| Own browsing record | persists locally; optional no-email sync | ephemeral by default; full-reset affordance | local; one-action erasure control | ephemeral by design |
| Account requirement | none | none | none | none |
| Bundled search | own search among choices | private search default (DDG per public descriptions) | own private search default | user choice |
| Business model | freeware + opt-in private ads/rewards economy | nonprofit/NGO | search company; browser ad-free | VPN company; browser free, no telemetry |
| Platforms | desktop + mobile | desktop + Android (per public descriptions) | desktop + mobile | desktop only |
| Bundled extras | Web3 wallet, rewards, new-tab content | none | app-tracking feature on Android | none |

All four satisfy the structural definition of the Type with entirely different
mechanisms — the definition cannot name any single mechanism.

## Canonical Abstraction

### Level 0 — Defining Invariant

Three jointly-held structures:

1. **Live web-browsing substrate.** Fetches and renders arbitrary URL-addressed web
   content interactively (address bar, tabs, page rendering, history/bookmarks/
   downloads as substrate furniture). Inherited from the Web Browser Type; this leaf
   does not restate the substrate's own definition. Remove → not a browser at all
   (blocker/VPN/proxy territory).
2. **Structural counter-surveillance machinery on the browsing path, default-on.** The
   product *itself*, as a built-in part of loading pages, interferes with third-party
   observation and collection of the browsing session: blocking or partitioning
   third-party tracking content and its storage, resisting identification of the
   browser instance (fingerprinting resistance), and hardening transport. This is
   structural and on by default — not an optional extension, not a per-user mode that
   ships off, not an after-the-fact cleaner. Remove → an ordinary Web Browser
   (mainstream browsers offer privacy *settings*; the Type requires a privacy
   *posture*).
3. **Local-first, minimized record of the user's own browsing.** The default posture
   keeps the browsing record on-device and non-profiled — history held only locally or
   not at all, no account required to browse, a one-action erasure affordance, and no
   server-side behavioral profile built by the product. Remove → a browser with an
   ad-blocker but a fully cloud-profiled user; not recognizable as privacy-focused.

Jointly-held is load-bearing: (1) alone = generic Web Browser; (2) alone = a privacy
tool/extension, not a browser; (3) alone = an offline data cleaner; (1)+(2) without
(3) = hardened browser inside a profiling ecosystem (the mainstream-plus-blocker
posture); (1)+(3) without (2) = a browser with tidy local storage and no protection on
the page path; (2)+(3) without (1) = privacy software that cannot browse.

The definition deliberately names **what** the machinery must do (interfere with
third-party observation, resist identification, minimize the record) and not **how**
(no named technique, network, list, or algorithm — see variants).

### Level 1 — Common Mature Structure

Present across the sample without being definitional:

- per-site privacy status surface showing what was blocked, with per-site exceptions
- bundled/default private search, or a search-choice surface favoring private engines
- HTTPS/transport upgrading where possible
- cookie handling beyond simple storage: blocking, partitioning, or consent-popup
  management
- a private window that is meaningfully stronger than a mainstream incognito mode
- no-account operation as the normal path; where sync exists, accountless/encrypted
  identity rather than email identity (some products)
- one-action data erasure ("clear everything") as a first-class control
- standard substrate furniture: tabs, bookmarks, downloads, history management,
  password storage, extension support (varies by product)

### Level 2 — Variant / Optional Structure

- **anonymity-network routing**: always-on (Tor Browser) vs optional mode (private
  window in Brave) vs absent (DuckDuckGo, Mullvad)
- **fingerprinting strategy**: uniformity (blend into a population: Tor, Mullvad) vs
  randomization (per-session noise: Brave) vs limited surface reduction
- **record posture**: ephemeral-by-default (Tor, Mullvad) vs persistent-local (Brave,
  DuckDuckGo)
- **bundled economy/services**: opt-in private ads/rewards and Web3 wallet (Brave);
  none (Tor, Mullvad); search-only (DuckDuckGo)
- **platform coverage**: desktop-only (Mullvad), desktop+mobile (Brave, DDG),
  Android-first (Tor)
- **engine substrate**: Chromium vs Firefox base — implementation, not definition
- **configuration depth**: fixed posture (Tor, Mullvad) vs rich per-site controls
  (Brave) vs deliberately shallow (DDG)
- adjacent extras: OS-level app tracking, built-in firewall/VPN bundles, news/new-tab
  content ecosystems

### Level 3 — Vendor-specific (research notes only)

- Brave: "Shields" panel mechanics; "farbling" randomization vocabulary; Brave
  Rewards/BAT token economy; Web3 wallet; sync-chain passphrase model; private window
  with Tor.
- Tor Browser: security levels (named tiers disabling web features); "New Identity" /
  "New circuit" affordances; circuit-per-domain isolation; window letterboxing;
  socks-proxy configurability.
- DuckDuckGo: "Tracker Radar" knowledge base; "Fire" button; "App Tracking Protection"
  (Android); Email Protection as an adjacent product.
- Mullvad: explicit design goal of being fingerprint-indistinguishable from Tor
  Browser users; vendor's no-logging posture across product line.
- Firefox (boundary pole): enhanced tracking protection standard/strict postures,
  total-cookie-isolation lineage, private browsing mode — a privacy stack inside a
  general browser.

## Historical / Market-Sample Check

Ask: would older, regional, platform-native or differently positioned products still
fit?

- **Tor Browser lineage (early 2000s, e.g. Torpark-era)**: browser substrate + routing
  through an anonymity network by default + ephemeral record. Satisfies all three L0
  legs; the definition names no modern technique, so era holds.
- **Early privacy browsers / anonymizing-proxy browsing services (late 1990s–2000s)**:
  where the product *was* a browser (or browser-plus-service) whose loading path
  stripped identifying data and kept no record, it satisfies the legs at the
  conceptual level. Where it was only a proxy service without a browser surface, it
  fails leg 1 — correctly excluded (proxy/VPN territory).
- **Mainstream browsers of the same era**: protection was optional, partial, and not
  the product's defining posture; fails leg 2 — correctly excluded.
- The definition does not name Chromium/Firefox, third-party-cookie politics of any
  era, specific blocklists, or any specific threat model beyond "third-party
  observation and collection" — so it should hold across engines and eras.

## Vendor-specific Findings

See Level 3 above. The most consequential for the final document: the ad/rewards and
Web3 economy (Brave) is a bundled business-model variant, not part of the Type; the
anonymity-network posture (Tor) is a variant, not the definition, since two of four
samples do not route through overlay networks; fingerprint *uniformity* vs
*randomization* are competing strategies, neither definitional.

## Boundary Findings

| Neighbor | Relationship | Distinction / removal test |
|---|---|---|
| **Web Browser** | substrate sibling; L0 of this Type = L0 of Web Browser **+ legs 2–3 (additive superset)** | a Web Browser offers privacy as optional settings/modes; this Type makes protection structural and default-on and minimizes its own data posture. Remove legs 2–3 → Web Browser. Mainstream private/incognito modes commonly do not stop cross-site tracking in normal mode — the mode-based contrast is the market-visible seam (Firefox = boundary pole showing a general browser can carry strong privacy tech without becoming this Type) |
| **Browser Security Platform** | different layer + different user | enterprise, admin-managed, threat-focused (phishing/malware/isolation), policy-driven; this Type is consumer self-directed privacy from tracking/profiling. Different users, rules, interfaces |
| **VPN Application / network-tunnel products** | adjacent layer | tunneling at network level, no page semantics: does not block trackers, partition storage, or resist fingerprinting; this Type's machinery operates on page loads. Some products bundle both (variant, not definition) |
| **Ad/tracker-blocking extensions** | capability without substrate | blocking lists without browsing; typically optional add-ons to another browser. The Type requires the machinery built in and default-on |
| **Web Archive Viewer** | different object | retrieves historical snapshots of pages; no live-browsing privacy path, no default-on protection loop |
| **Private search engine** | component relationship | search is one bundled surface of the browser; the search product alone is a Search Type |

Taxonomy verdict: **keep-both** (distinct Type, not a mere Variant of Web Browser) —
the privacy machinery is a genuine load-bearing leg (removing it changes what the
software does on every page load), and the market recognizes a distinct product
category with distinct vendors and philosophies. But the L0 relationship to Web
Browser is additive-superset (subtype-like), worth recording for the taxonomy owner.

## Uncertainties

- All observations are background-level (no fetched official docs this session). In
  particular NOT asserted anywhere: blocklist sizes, number of trackers blocked,
  exact default values, exact security-level names, exact sync mechanics, per-product
  telemetry policies, mobile platform details beyond structural level.
- Whether DuckDuckGo's iOS client uses WebKit as publicly described was not verified.
- Brave's no-profiling claims are vendor marketing; not independently verified.
- The DuckDuckGo and Brave desktop browsers' exact engine lineage (which Chromium
  version/forks) not verified — and not needed for the definition.
- Degree to which mainstream browsers' private modes block third-party tracking today
  is changing over time; the boundary wording deliberately uses "commonly" rather
  than a categorical claim.

## Final Synthesis

A Privacy-focused Browser is a live web-browsing application in which protection from
third-party observation is structural and default-on: the product itself interferes
with tracking and profiling on every page load (blocking/partitioning third-party
content and storage, resisting browser identification, hardening transport), and its
default data posture keeps the user's own browsing record local or ephemeral, without
requiring an account, with one-action erasure. Everything else — which techniques it
uses, whether traffic is anonymized at network level, whether the record persists
locally or not at all, what economy or services are bundled — is variant territory.
The Type is an additive superset of the Web Browser substrate; the seam with a
mainstream browser is not the presence of privacy technology but whether protection
is the defining, always-on posture and whether the product's own data posture is
minimized around it.

