# Research Notes — Web Browser

Research date: 2026-09-10
Directory leaf: Web Browser (§02.01 Web Browsing & Access)
Slug: web-browser

## Research Goal

Understand the Web Browser as an Application Type from real products: what its defining structure is, what its standard capability set is, how the browsing loop actually works, and where its boundaries lie against the already-processed siblings (Privacy-focused Browser, Browser Security Platform, Browser Compatibility Testing Platform) and other neighbors (Search Engine, Web Archive Viewer, embedded webviews).

## Initial Boundary

Working hypothesis before research:

- Core use: access and interact with pages of the live web by address.
- Users: effectively everyone; the default access instrument for the web.
- Nearest neighbors: Privacy-focused Browser (same substrate + privacy posture), Search Engine (finds pages, does not render destinations), Web Archive Viewer (snapshots, not live), Browser Security Platform (enterprise control over browsers), Browser Compatibility Testing Platform (browsers as test substrate), embedded webviews (component, not standalone application).
- Known unknowns: whether tabs / bookmarks / history / downloads are definitional or merely universal; how to state the L0 so that first-generation and text-mode browsers still fit; how to hold the seam with Privacy-focused Browser given that mainstream browsers now ship default-on tracker blocking.

## Research Questions

1. What are the core objects in a browser's world? (address, page, browsing context/tab/window, navigation state, history, bookmarks, downloads, site data/permissions, settings)
2. What is the defining interaction loop?
3. What does the browser do on the user's behalf (fetch, render, execute page code, enforce the web security model, keep state)?
4. What state does it keep, and what is session-scoped vs persistent?
5. How do the sampled products differ in philosophy (ecosystem vs independent engine vs platform-native vs platform-bundled)?
6. Where exactly is the seam with Privacy-focused Browser, given mainstream browsers increasingly block trackers by default?

## Representative Products

Selected for market representativeness, documentation quality, and distinct product philosophies:

| Product | Philosophy pole | Customer layer |
|---|---|---|
| Google Chrome | ecosystem-led (account + services around the browser) | consumer + enterprise, market leader |
| Mozilla Firefox | independent engine / open-web champion | consumer, values-driven segment |
| Apple Safari | platform-native (browser as part of the OS) | Apple-platform users |
| Microsoft Edge | platform-bundled (browser shipped with the OS, extended with services) | Windows users + enterprise |

## Sources

| Source | Tier | Result |
|---|---|---|
| Safari User Guide for Mac — https://support.apple.com/guide/safari/welcome/mac | Tier 1 (official user guide) | Fetched 2026-09-10. Full guide TOC obtained: go to a website, search the internet, cookies, translate, download items, bookmarks, favorites, Reading List, tabs, profiles, default browser, homepage, window customization, start page, extensions, cookie management, clear history, pop-up blocking, Private Browsing, prevent cross-site tracking, tracker report, Apple Pay in Safari, settings, keyboard shortcuts. |
| Microsoft Edge help & learning — https://support.microsoft.com/en-us/microsoft-edge | Tier 1 (official help hub) | Fetched 2026-09-10. Quick-access topics obtained: sign in to sync across devices, save/forget passwords, change home page, Copilot in Edge, Collections, print, SmartScreen, tracking prevention, block pop-ups, delete cookies, clear cache, troubleshooting. |
| Firefox product page — https://www.mozilla.org/en-US/firefox/browsers/ | Tier 2 (official product page) | Fetched 2026-09-10. Confirms positioning ("fast, private browser"), built-in tracker blocking by default ("Blocks trackers automatically. No setup."), tab groups, reader mode, picture-in-picture, pinned tabs, customizable sidebar, Firefox View, migration of bookmarks/passwords/history, sync ("Take your tabs, history, and passwords wherever you go"), extensions ecosystem, "we don't sell your personal data". |
| Chrome Help — https://support.google.com/chrome | Tier 1 | Timed out twice (2026-09-10). Abandoned per network-restriction rule. Chrome evidence downgraded to Layer B (structural background). |
| Mozilla Support KB — https://support.mozilla.org/ | Tier 1 | Bot/client challenge, content not retrievable (2026-09-10). Not used. |

Evidence calibration: Safari and Edge observations are Layer A (directly observed from official documentation). Firefox observations are Layer A from the official product page (marketing tier — positioning and feature names only, no operational detail). Chrome observations are Layer B (cross-product structural background; no direct fetch). No precise numeric claims anywhere (no limits, counts, defaults, timings) — none are supported by fetched evidence.

## Product Observations

### Safari (Layer A — official user guide TOC)

- The guide's structure itself is evidence of the Type's capability inventory: "Browse the web" (go to a website, search the internet, cookies, translate a webpage, download items from the web); "Organize your browsing" (bookmark webpages, favorites, Reading List, use tabs for webpages, create profiles); "Customize your browsing" (make default browser, homepage, customize window, start page, get extensions); "Keep your browsing private" (manage cookies, clear history, block pop-ups, browse privately, prevent cross-site tracking, see who tried to track you); Apple Pay in Safari.
- Reading List = a save-for-later surface (read-it-later capability embedded in the browser).
- Profiles = separate browsing containers within one browser.
- Private Browsing = a mode, distinct from the default posture.
- Cross-site tracking prevention and a tracker report exist as features of a general-purpose browser — the boundary pole for the Privacy-focused Browser seam.

### Microsoft Edge (Layer A — official help hub topics)

- Help hub organizes around: Get started; Privacy & security (SmartScreen, tracking prevention, pop-ups, cookies, cache); Personalize (home page, passwords, sync across devices via sign-in); "Get more done with Edge" (Copilot, Collections, print, accessibility); iOS & Android.
- Sync is account-based ("Sign in to sync Microsoft Edge across devices").
- Collections = a vendor-specific content-clipping/organization surface.
- Copilot = a vendor-specific AI assistant embedded in the browser.
- Tracking prevention is a first-class settings topic in a mainstream browser.

### Firefox (Layer A from official product page — positioning/feature names only)

- Self-positioning: "The fast, private browser that keeps you safe"; "Blocks trackers automatically. No setup. No guesswork." — default-on tracker blocking is now a mainstream-browser feature, not only a privacy-browser feature.
- Focus features: tab groups, reader mode, picture-in-picture, pinned tabs, customizable sidebar, Firefox View.
- Switching/migration: bookmarks, passwords, history come with the user.
- Sync: "Take your tabs, history, and passwords wherever you go."
- Extensions ecosystem (large catalog), themes.
- Independence posture: not shareholder-owned, "we don't sell your personal data".

### Chrome (Layer B — structural background; official help not reachable this session)

- Treated only at structural level: the same browsing substrate (address bar, tabs, rendering, history, bookmarks, downloads, settings) plus account-based sync and ecosystem services. No operational detail asserted; no numeric claims. Chromium-family structure is additionally represented at Layer A by Edge (same engine family, directly documented).

## Cross-product Comparison

| Structure | Safari | Edge | Firefox | Chrome (B) | Verdict |
|---|---|---|---|---|---|
| Address-directed retrieval + rendering of live pages | yes (go to a website / search) | yes (core, implicit in hub) | yes | yes | Defining (all products; the Type's reason to exist) |
| Rendered page as navigation surface (links) | yes | yes | yes | yes | Defining |
| Managed navigation state (back/forward, current location per browsing context) | yes | yes | yes | yes | Defining (universal; seed of history) |
| Tabs | yes ("use tabs for webpages") | yes | yes (tab groups, pinned tabs) | yes | Common mature — NOT definitional (absent in first-generation browsers) |
| Bookmarks/favorites | yes | yes | yes (migration) | yes | Common mature — NOT definitional |
| Persistent history | yes (clear history) | yes | yes | yes | Common mature — NOT definitional |
| Downloads | yes (download items) | yes | yes | yes | Common mature — NOT definitional |
| Address bar doubles as search | yes (search the internet) | yes | yes | yes | Common mature — NOT definitional |
| Private/incognito mode | yes (Private Browsing) | yes | yes | yes | Common mature — NOT definitional |
| Per-site state & permissions (cookies, pop-ups, site data) | yes (manage cookies, block pop-ups) | yes (cookies, pop-ups, cache) | yes | yes | Common mature — NOT definitional |
| Sync across devices | yes (platform) | yes (account sign-in) | yes (account) | yes (account) | Common mature — NOT definitional (accountless browsers exist) |
| Extensions | yes (get extensions) | yes | yes (large catalog) | yes | Common mature — NOT definitional |
| Default-on tracker blocking | yes (prevent cross-site tracking) | yes (tracking prevention) | yes ("blocks trackers automatically") | yes (B) | Common mature in current market — NOT definitional; convergence pressure toward the privacy sibling |
| Reader mode / translate | yes (translate; Reading List adjacent) | yes | yes (reader mode) | yes | Optional/variant |
| Profiles | yes (create profiles) | yes | yes | yes | Optional/variant |
| AI assistant embedded | — | yes (Copilot) | yes (configurable AI) | yes (B) | Vendor-specific / emerging variant |
| Bundled content/clipping surfaces | Reading List | Collections | Firefox View | — | Vendor-specific |
| Platform payment integration | Apple Pay in Safari | — | — | — | Vendor-specific |

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures:

1. **Address-directed retrieval and rendering of the live open web.** The user supplies an address — typed URL, search handoff, or a followed link — and the application fetches that page and presents its content as an interactive display. The address space is the open web (any publicly addressable page), not a curated corpus or one provider's content. "Rendering" is defined as presenting the fetched page for interaction — graphical layout in modern products, plain text in text-mode browsers; the engine is implementation, not definition.
   - Remove → a search engine (lists results, never renders destinations), a web archive viewer (snapshots, not live), a single-service portal app.

2. **The rendered page as the steering surface.** Pages carry hyperlinks; following them moves the user within and across sites. The page itself is the primary control of the application — the browser's unit of work is the page, and navigation happens through the content, not through a separate app-level menu of destinations.
   - Remove → a page fetcher/viewer with no navigation semantics; a feed reader (navigates a subscription corpus, not the open address space).

3. **Managed navigation state per browsing context.** The application tracks, for each browsing context (one page's place in the session), the current location and the visited sequence — at minimum back/forward — so navigation is reversible and the session is continuous. This is the seed from which persistent history later grows.
   - Remove → a sequence of unconnected page fetches; a dumb viewer.

Jointly-held load-bearing tests:
- 1 alone (fetch+render without link navigation or state) = page viewer / webview-class display.
- 2 without 1 = a link directory / hypertext browser over a closed corpus.
- 3 without 1+2 = a fetch log.
- 1+2 without 3 = a page fetcher with no reversible navigation.
- 2+3 without 1 = a hypertext system over a fixed corpus (intranet/CD-ROM browsers, help systems).
- 1+3 without 2 = a URL-fetching tool navigated only by retyping addresses.

Scoping condition: a standalone, user-facing application (not an embedded webview component, which is a capability inside another product).

### L1 — Common Mature Structure

Very common in mature modern products; not required to recognize the Type:

- tabs — multiple simultaneous browsing contexts in one window (the modern container; first-generation browsers had one page per window)
- bookmarks/favorites — saved addresses
- persistent browsing history — the cross-session record of visited pages
- downloads management
- address bar doubling as a search entry (search handoff)
- find-in-page
- settings/preferences, including per-site state and permissions (cookies, site data, pop-ups, camera/location/notifications), connection/security indicators
- private/incognito mode
- home/start page
- sync across devices (account-based in the sampled products)
- extension/add-on support
- password/autofill management
- reader mode, translate, picture-in-picture, pinned tabs, tab groups, sidebars

### L2 — Variant / Optional Structure

- identity substrate: platform account (Safari/Apple), vendor account (Chrome/Edge/Firefox), no account, local profiles
- default search engine choice / bundled search
- bundled services: AI assistant (Copilot in Edge), content clipping (Collections, Reading List), rewards/news/shopping surfaces
- platform integration depth: OS default-browser role, platform payments (Apple Pay), OS-level feature sharing
- tracking-prevention strength and posture (feature among many vs defining posture — the Privacy-focused Browser seam)
- engine (Blink / Gecko / WebKit) — implementation, invisible to the canonical model
- web-app installation (PWA), developer tools, kiosk/restricted modes
- mobile-first vs desktop-first packaging

### L3 — Vendor-specific (Research Notes only)

- Edge: Collections, Copilot sidebar, SmartScreen branding, vertical tabs naming
- Safari: Reading List, Apple Pay in Safari, start-page customization, profiles, tracker report
- Firefox: Firefox View, container tabs, about:config depth, ESR channel, "30,000+ extensions" figure (marketing page)
- Chrome: ecosystem services around the account; omnibox specifics

## §24 Historical / Market-Sample Check

Question: would older, regional, platform-native, or differently positioned products still fit the L0?

- First-generation browsers (WorldWideWeb 1990, Lynx 1992, Mosaic 1993, Netscape Navigator 1994): address-directed retrieval + presentation for interaction (Lynx in plain text — confirming "rendering" must not mean "graphical layout"), link-following navigation, back/forward + session history. No tabs, no downloads manager, no sync, no extensions. → L0 holds; tabs/bookmarks-scale furniture correctly stays in L1.
- Text-mode browsers (Lynx class): satisfy L0 without graphics → the definition must say "presents the page for interaction", not "renders graphics". (Absorbed into L0 wording.)
- Platform-native browsers (Internet Explorer, Safari, Edge legacy): fit. Regional browsers (UC, QQ, Yandex classes): fit. Kiosk/restricted browsers: navigation state management is restricted but present → fit as variants.
- Embedded webviews (in-app page displays): fail the scoping condition (component, not standalone application) → correctly outside the Type.
- Conclusion: the L0 is era-robust and platform-robust. The modern sample (tabs, sync, omnibox, extensions) is correctly excluded from the definition.

## Vendor-specific Findings

See L3 above. None promoted to the canonical model.

## Boundary Findings

| Neighbor | Seam | Removal test |
|---|---|---|
| Privacy-focused Browser | additive superset: same substrate + default-on counter-surveillance machinery + minimized own-record posture | remove the protection posture → Web Browser; remove the substrate → privacy utility that cannot browse |
| Search Engine | query → ranked results (finds pages) vs address → rendered page (shows pages); the address bar's search handoff is an implementation inside the browser, not a merger of Types | remove rendering of destinations → search engine |
| Web Archive Viewer | historical snapshots vs live retrieval | remove "live" → archive viewer |
| Browser Security Platform | enterprise admin-managed threat control over a browser population vs consumer access instrument (seam confirmed from that pass's side) | remove organization-administered policy → just a browser |
| Browser Compatibility Testing Platform | browsers as test substrate for someone else's application (seam confirmed from that pass's side) | remove the testing purpose → browsers |
| Feed Reader / Read-it-later | subscription/curation corpus vs address-directed open-web access; save-for-later surfaces inside browsers (Reading List) are embedded capabilities, not the Type | remove address-directed open-web retrieval → reader |
| Web Development IDE / Web Application Builder | authoring vs access; DevTools is an advanced surface inside browsers, not the defining purpose | remove authoring → browser; remove access → authoring tool |
| Embedded webview | component vs standalone application | scoping condition, not a Type boundary |

**Privacy-focused Browser joint review (discharged this pass).** The sibling pass (2026-09-08) recorded: PFB's L0 is an additive superset of a Web Browser L0; keep-both; Firefox held as boundary pole (strong privacy stack, general-purpose defining posture). This pass RATIFIES that reading from the Web Browser side. Additional convergence evidence found: mainstream browsers now ship default-on tracker blocking as a first-class feature (Safari "prevent cross-site tracking", Edge "tracking prevention", Firefox "blocks trackers automatically" — Layer A on all three). This narrows the *behavioral* gap but not the *structural* one: in a general browser, protection is one setting among many and the record/account posture is not minimized by definition; in a Privacy-focused Browser, protection and minimized record are the defining posture. The seam therefore remains: defining posture, not presence of privacy technology. No directory change proposed.

## Uncertainties

- Chrome's operational documentation was not reachable this session; Chrome-specific claims are held at Layer B and none appear in the final document.
- Mozilla Support KB was not retrievable (bot challenge); Firefox operational detail (settings depth, exact feature behavior) is unverified this session — only positioning and feature names from the official product page are used.
- The exact current state of extension support on mobile platforms was not researched; no claim is made about it in the final document.
- Whether "managed navigation state" should be folded into leg 2 rather than standing alone is a judgment call; it is kept separate because it is the seed of history and the discriminator against dumb page fetchers, and it survives the historical check (present from the first generation).

## Final Synthesis

The Web Browser is the general-purpose instrument for accessing the live, open web. Its defining core is three jointly-held structures: address-directed retrieval and rendering of live pages from the open address space; the rendered page as the steering surface (link-following navigation); and managed navigation state per browsing context (reversible navigation). Everything else the market associates with browsers — tabs, bookmarks, history, downloads, search-in-address-bar, private modes, sync, extensions, per-site permissions, even default-on tracker blocking — is common mature structure or variant, not definition. The Type's neighbors are separated by posture (Privacy-focused Browser), by purpose (Search Engine, Web Archive Viewer, testing/security platforms), or by scoping (embedded webviews).
