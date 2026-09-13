# Research Notes — Scripture Study Application

## Research Goal

Understand what a Scripture Study Application is as an Application Type: what exists inside it, what users do with it, how study work flows, and where its boundary lies against e-book readers, reference applications, note-taking applications, and the church-institution software family (§25 siblings).

## Initial Boundary

Initial hypothesis (before research):

- Core use: reading and studying religious scripture (Bible, Jewish texts, and by extension other traditions' canonical texts).
- Expected core structure: a scripture text corpus addressed by a canonical reference system (book/chapter/verse or tradition-equivalent), multiple translations/editions aligned at the reference level, passage-anchored notes/highlights, study resources (commentaries, dictionaries, cross-references) keyed to passages, reading plans.
- Likely users: individual believers, students of scripture, small groups, pastors/teachers preparing lessons.
- Nearest neighbors: E-book Reader, Note-taking Application, Dictionary/Reference Application, Digital Library Platform, Sermon Management, Worship Presentation Software, Religious Education Management, Church Management System.
- Main risk of confusion: collapsing into "E-book Reader with religious content" or into the church-institution family.

## Research Questions

1. What is the core object structure? Is there a canonical reference system, and what role does it play?
2. How do multiple translations/editions relate to each other?
3. How are study resources (commentaries, dictionaries, cross-references, original-language tools) attached to the text?
4. What do users annotate, and what do annotations attach to?
5. What roles do reading plans / devotionals / calendars play?
6. What interfaces exist, and what is the primary interaction loop?
7. What business models and access rules govern the resource layer?
8. Where is the boundary against e-book readers, reference apps, note apps, and church-institution software?
9. Would older / regional / differently-positioned products still fit the definition? (historical check)

## Representative Products

Selected for market representation, different product philosophies, different customer tiers, different traditions, and different eras:

| Product | Philosophy / tier | Why sampled |
|---|---|---|
| e-Sword | Free desktop classic (~25 years), module-based, integrated editor | long-lived desktop pole; historical check |
| Blue Letter Bible | Free web ministry study suite (~30 years), donation-funded, original-language heavy | web ministry pole; verse-anchored tool design |
| Sefaria | Open-source/open-access Jewish text library, linked-corpus philosophy, web-first | different tradition; open-data philosophy; reference-system-as-core evidence |
| Bible Hub | Free web study suite, anonymous (no accounts), passage-keyed study tabs | account-less pole; proves annotation features are not definitional |
| Bible Gateway | Commercial reading/search site (150+ versions, 50 languages), subscription study layer (Plus), publisher-owned | reading-first posture; subscription resource layer; publisher integration |

Attempted but unreachable (network limitation, 2–3 failures each, abandoned per sourcing rules): YouVersion/Bible App (bible.com JS challenge; youversion.com and support subdomain timeouts), Logos Bible Software (logos.com and support.logos.com timeouts), Olive Tree (olivetree.com and help subdomain timeouts). These represent the consumer mass-market mobile pole and the professional paid-library pole; no assertions about them are made in the final document beyond noting the gap.

## Sources

- e-Sword — https://www.e-sword.net/ (home/features) — fetched 2026-09-09
- Blue Letter Bible — https://www.blueletterbible.org/ (home/study/tools) — fetched 2026-09-09
- Sefaria — https://developers.sefaria.org/ (home, llms.txt index), /docs/text-references.md, /docs/index-and-versions.md, /docs/commentaries.md — fetched 2026-09-09
- Bible Hub — https://biblehub.com/ (home/about) — fetched 2026-09-09
- Bible Gateway — https://www.biblegateway.com/ (home) — fetched 2026-09-09

Evidence layers: A = directly observed on the fetched official page; B = cross-product commonality across the sample; C = canonical inference from comparison and boundary reasoning.

## Product Observations

### e-Sword (Layer A unless noted)

- Self-description: "Free Bible Study for the PC"; "Bibles, commentaries, dictionaries, and more — every resource is just a click away."
- Parallel Bible view; Compare Bibles (multiple translations against the same passage).
- Integrated editor "for sermons, Bible studies, notes, and journaling. Everything you write stays right alongside the resources that informed it." → user writing is verse-anchored and lives beside the resources.
- Strong's tooltips (original-language word studies keyed to Strong's numbers); Scripture tooltips (references inside text become interactive).
- Searches "by Strong's numbers"; powerful/expansive search.
- Reference library; copy verses; highlighted verses; WYSIWYG printing.
- ~25 years refined; "trusted by students, teachers, and pastors alike"; PC + Android + Mac + iPad + iPhone editions.
- Module-shaped resource model (Bibles / commentaries / dictionaries as separate resources) [B: wording implies modules; exact store mechanics not verified].

### Blue Letter Bible (Layer A)

- Self-description: "a free, searchable online Bible program providing access to many different Bible translations" — KJV…NET plus original-language texts: Westminster Leningrad Codex (Hebrew), Septuagint, Morphological Greek NT, Textus Receptus.
- Verse-anchored tool tabs on Bible pages: **Interlinear, Bibles, Cross-Refs, Commentaries, Dictionaries, Miscellaneous** — the study layer opens against the selected verse.
- Study sections: text commentaries, audio & video commentaries, encyclopedias/dictionaries, study notes, prefaces, introductions, charts/outlines, timelines, maps/images.
- Biblical language resources: inline interlinear, language tools, lexical resources, grammars, concordances, morphology.
- Devotionals (each with Today's Reading / Scripture Index / Calendar Index) and Bible Reading Plans.
- Search surfaces: Bible search, LexiConc search (Hebrew/Greek by English definition), theological FAQ search, dictionary browse; Multiverse retrieval; copy-verses with configurable reference formats.
- Parallel version comparison (two translations side by side; "for over a decade" on mobile apps, newly added to web).
- Verse of the Day; user accounts (login, preferences); ScriptureMark (separate markup tool); BLB Institute (free Bible courses — bundled neighbor).
- ~30 years; 501(c)(3) nonprofit, donation-funded.

### Sefaria (Layer A)

- Self-description: "the largest open-source database of Jewish texts in history"; open API (no keys), open data export, nonprofit.
- **Text references are the core**: "The core of Sefaria's system is the system of text references." Refs are human- and machine-readable, environment-agnostic (no database IDs), tolerant of alternate spellings. Valid refs: `Genesis 1:1`, `Sanhedrin 4b` (daf syntax), `Rashi on Genesis 1:2:1`, ranged refs `Ex. 12:2-8`.
- **Index vs Versions**: a work is an Index (structure schema + metadata); editions/translations are Versions. "All versions of the same text will definitionally share the same Index… the segments will be referred to by the same Ref." Genesis 1:1 exists across ~50 versions (Hebrew with/without nikkud, English, French, Spanish, Yiddish, Ladino, Russian, German…), all addressed by the same ref.
- **Commentaries are texts linked to base texts**: commentary Indexes carry `dependence` (Commentary/Targum), `base_text_titles` (e.g., "Rashi on Genesis" → "Genesis"), and `base_text_mapping` for auto-linking (e.g., `many_to_one`: many comments per verse). Commentary refs inherit the base text's structure and add a "Comment" level.
- Links API returns connections for a ref by category (Commentary, Midrash, Essay, Quoting Commentary…); Related endpoint aggregates links, sheets, notes, media, manuscripts, topics for a ref.
- Lexicons/dictionaries; Topics with ref links; manuscripts metadata.
- **Source sheets**: user-created teaching documents citing refs; public/private; collections; user profiles; "half a million user sheets" referenced in a newsletter item (site-scale claim, single source).
- **Learning schedules**: Calendar API returns the daily/weekly learning schedule for a date (tradition's study cycle); Sefaria-powered Koveah.org builds "personalized Torah learning schedules, with daily reminders".
- The Linker: turns citations on external websites into links to the library (150+ sites listed) — the reference system extends beyond the app itself.

### Bible Hub (Layer A)

- Self-description: "Online Bible Study Suite" — topical, Greek, Hebrew study tools, concordances, commentaries, dictionaries, sermons, devotionals.
- Search: "Enter any combination of book, abbreviation, chapter, verse, or keyword."
- Study tabs per passage: "Click any study tab to view sermons, topics, commentaries, interlinear, Strong's, Greek, or Hebrew **for your passage**."
- Parallel chapters: "over 30 translations and up to 5 in parallel."
- Cross references: Treasury of Scripture Knowledge (TSK) format.
- Reading plan (linked daily-reading site); book overviews; topical indexes; multilingual sister sites.
- Free; mission-driven; **no user accounts or personal annotation features visible** — anonymous study suite.

### Bible Gateway (Layer A)

- Self-description: "A searchable online Bible in over 150 versions and 50 languages."
- Read side: Reading Plans, Advanced Search, Available Versions, Audio Bibles, Verse of the Day, devotionals, apps.
- Study layer is subscription-gated: "Bible Gateway Plus — 70+ trusted Bible study resources beside every passage"; "Study Bibles and commentary beside every verse."
- Free account: "highlight verses, save favorites, and take notes—so you can return to what Scripture has shown you."
- Owned by HarperCollins Christian Publishing (Zondervan, Thomas Nelson in network) — publisher-integrated distribution.
- Posture: reading/search-first distribution site with a paid study layer, rather than a study workbench.

## Cross-product Comparison

| Structure | e-Sword | BLB | Sefaria | Bible Hub | Bible Gateway | Strength |
|---|---|---|---|---|---|---|
| Scripture corpus as base layer | ✓ | ✓ | ✓ | ✓ | ✓ | B (5/5) |
| Canonical reference addressing (book/chapter/verse or tradition-equivalent) | ✓ (verse-keyed tools/notes) | ✓ (verse tool tabs, ref-format copying) | ✓ (refs are the system core) | ✓ (ref search, per-passage tabs) | ✓ (passage lookup) | B (5/5) |
| Multiple versions/editions aligned at the reference level | ✓ (parallel, compare) | ✓ (version selector, parallel) | ✓ (Index/Versions, same ref) | ✓ (up to 5 parallel) | ✓ (150+ versions) | B (5/5) |
| Passage-keyed study resources (commentaries/dictionaries/cross-refs) | ✓ ("every resource a click away") | ✓ (verse tool tabs) | ✓ (linked commentaries, auto-linking) | ✓ (study tabs "for your passage") | ✓ (Plus "beside every passage") | B (5/5) |
| Original-language tools (Strong's/interlinear/lexicon) | ✓ | ✓ | ✓ (lexicons) | ✓ | ✓ (OL texts as versions) | B (5/5) — tool-shaped |
| Search over corpus | ✓ | ✓ | ✓ | ✓ | ✓ | B (5/5) |
| User annotations (notes/highlights) bound to passages | ✓ | (accounts/preferences; markup via sibling tool) | ✓ (notes, sheets) | ✗ (no accounts) | ✓ (free account) | B (4/5) — not definitional |
| Reading plans / devotionals / study calendars | (not on homepage) | ✓ | ✓ (calendar cycle; powered schedulers) | ✓ (linked plan) | ✓ | B (4/5) — common |
| Audio (Bibles/commentaries) | — | ✓ | (in powered projects) | — | ✓ | Optional |
| Teaching/authoring outputs (sermons, sheets) | ✓ (editor) | — | ✓ (source sheets) | — | — | Optional/variant |
| Community/sharing (public content, collections) | — | — | ✓ | — | (social sharing) | Variant |
| Free/open access to resources | ✓ (app free) | ✓ (donation) | ✓ (open) | ✓ | partial (Plus paid) | Variant axis |
| Courses/education surface (bundled) | — | ✓ (BLB Institute) | — | — | (learn section) | Bundled neighbor |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

Two jointly-held structures:

1. **The scripture corpus addressed by canonical reference.** The application's base layer is the tradition's scripture held as a corpus, and the corpus is organized — navigated, cited, addressed — by the tradition's shared reference system (book/chapter/verse for Bibles; tractate/page/daf for Talmud; equivalent schemes elsewhere). A reference is a stable address independent of edition, translation, language, device, or layout. Remove → a generic e-book reader or document site; the reference-addressing is what makes everything else in the Type possible.

2. **The passage-keyed study layer.** Reference works and study helps — commentaries, dictionaries/lexicons, cross-reference systems, original-language tools — are bound to the corpus by reference and opened against specific passages. Remove → a plain text reader; the "study" in the Type name dies.

Joint load-bearing:
- 1 alone = scripture text reader (reading site/app with no study machinery).
- 2 without 1 = a general reference library (commentaries and dictionaries as free-standing books) — not scripture study.
- 1+2 = the Type.

### L1 — Common Mature Structure (present in most sampled products, not definitional)

- Multiple versions/translations of the same work, aligned at the reference level (5/5; conceptually a single-edition study product would still satisfy L0 — unverified in market, held as reasoning not assertion).
- User annotations — notes, highlights, bookmarks, favorites — anchored to references (4/5; account-less pole proves not definitional).
- Original-language study tools: Strong's-number word studies, interlinear, lexicons, morphology (5/5 but tool-shaped).
- Reference-aware search (book/chapter/verse/keyword) (5/5).
- Reading plans, devotionals, tradition study calendars (4/5).
- Copy/export of verses with reference formatting; printing.
- Audio Bibles / audio commentaries (partial).

### L2 — Variant / Optional Structure

- Business/access model: free app + free resources (e-Sword, BLB, Bible Hub), open-access nonprofit (Sefaria), subscription resource layer (Bible Gateway Plus), paid resource libraries (Logos/Olive Tree — unverified, see limitations).
- Teaching/authoring outputs: sermon/study editors (e-Sword), source-sheet builders (Sefaria).
- Community layer: public sheets, collections, profiles (Sefaria); social sharing (Bible Gateway).
- Tradition scope: single-tradition (Bible apps; Jewish text library) is the norm; multi-tradition generalization not observed in sample.
- Form factor: desktop (e-Sword), web (BLB, Bible Hub, Sefaria, Bible Gateway), mobile-first consumer (unreachable in sample).
- Bundled education surfaces (BLB Institute courses; Bible Gateway "learn" section).
- Devotional/community engagement layers typical of consumer Bible apps (YouVersion — unverified).

### L3 — Vendor-specific (research notes only)

- Sefaria's Linker (citation-linking plugin for external sites), MCPs for LLMs, manuscripts metadata, topic ontology with integer-programming curation.
- BLB's LexiConc search, ScriptureMark sibling tool, LiveMap user counter.
- e-Sword's WYSIWYG printing, module ecosystem specifics.
- Bible Gateway's publisher network integration (HarperCollins Christian Publishing / Zondervan / Thomas Nelson).

### Anti-overfitting notes

- Multi-version alignment is universal in the sample but is treated as common mature structure: the L0 invariant (reference addressing) is what *enables* alignment; nothing in the definition requires that more than one edition exist.
- User annotations are NOT definitional (Bible Hub pole).
- Reading plans are NOT definitional (absent from e-Sword's homepage presentation; Sefaria's is tradition-cycle-shaped, not plan-shaped).
- Original-language tools are NOT definitional (tool-shaped; a devotional-depth study product would still be in-type).
- The sample is Christian-majority (4/5) with one Jewish product; claims are worded to avoid universalizing across all religious traditions.

### Historical / market-sample check (§24-equivalent reasoning)

- e-Sword (~25 years) and Blue Letter Bible (~30 years) predate the smartphone/cloud era: both satisfy the two-part core with no modern machinery (no cloud sync, no mobile-first design, no AI). Passed.
- Sefaria: different tradition, open-access philosophy, web-first, no paid resource store — satisfies the core fully. Passed.
- Bible Hub: no accounts, no personalization at all — satisfies the core. Passed.
- Conceptual ancestor (Layer C inference, worded cautiously): the printed study Bible — scripture text with commentary, cross-references, and maps bound by reference — exhibits the same two-part structure in print; the software Type digitizes and interlinks it. The reference system itself (e.g., "Rashi on Genesis 1:2:1") predates software and is the tradition's own citation practice.

## Vendor-specific Findings

See L3 above. None promoted to the final document.

## Boundary Findings

1. **vs E-book Reader** — the sharpest boundary. E-book readers address text by page/location within one edition; scripture study applications address text by canonical reference that is stable across editions and translations, and bind study resources to those references. Remove reference addressing + passage-keyed resources → e-book reader. A scripture app can *contain* reader-like reading flow; the reverse (an e-book reader becoming a study app) requires acquiring the reference system and resource binding.

2. **vs Dictionary/Reference Application, Online Encyclopedia** — in reference apps the reference works are the primary objects; in scripture study applications the scripture corpus is primary and dictionaries/commentaries are keyed resources opened against passages.

3. **vs Note-taking Application** — notes apps hold free-standing notes as primary objects; here notes are anchored to scripture references and live beside the text and resources. Export of notes outward exists (e-Sword editor), but the center of gravity is the corpus.

4. **vs Digital Library Platform / Library Discovery** — libraries hold broad collections for discovery/borrowing; scripture study apps hold a fixed canonical corpus with study machinery bound to it.

5. **vs Sermon Management / Worship Presentation Software / Church Management System** — church-institution tools. Sermon prep *uses* scripture study tools; worship presentation displays scripture live to a congregation (the presentation-application pass's advance note about worship-presentation-software's live scripture display is acknowledged — that Type is defined by live-display/liturgy/service semantics, not by study resources keyed to references); ChMS manages the organization. None of them provide the reference-addressed corpus + passage-keyed study layer as the product's core.

6. **vs Religious Education Management** — institutional administration (classes, teachers, enrollment) vs personal/small-group engagement with the text.

7. **Reading-first distribution sites (Bible Gateway posture)** — a spectrum exists from reading/search-first sites to study-first workbenches. Bible Gateway sits toward the reading pole but carries the study layer (subscription) and annotation features, so it remains in-type; a site with only text + search and no passage-keyed resources would fall outside (scripture text reader).

8. **Scripture memorization apps, devotional-only apps** — not sampled; likely variants or adjacent types. No assertion made.

## Uncertainties

- YouVersion (dominant consumer mobile Bible app) and Logos (dominant professional paid-library) could not be fetched. The consumer mass-market pole and the professional paid-library pole are therefore unverified; the final document's claims are calibrated to the reachable sample and the gap is disclosed in Sources.
- Whether single-edition scripture study products exist in the market (reasoning says they would satisfy L0; no instance verified).
- Multi-tradition breadth (Quran apps, etc.) unverified; wording avoids universal claims.
- Exact resource-licensing mechanics of module-store products (Olive Tree, Logos) unverified.
- Whether reading plans are universal across the whole market (4/5 in sample).

## Final Synthesis

A Scripture Study Application is built on a two-part core: **a scripture corpus addressed by canonical reference** (the tradition's shared citation system as the stable address space — independent of edition, translation, and layout) and **a passage-keyed study layer** (commentaries, dictionaries, cross-references, and original-language tools bound to the corpus by reference and opened against specific passages). Around this core, mature products add version alignment, reference-anchored personal annotation, reference-aware search, reading plans/devotionals, and original-language tooling; business models, community features, teaching outputs, and form factors vary widely. The Type is distinct from e-book readers (page-addressed single editions), from reference/notes apps (different primary objects), and from the church-institution software family (which serves organizational record-keeping and live assembly, not personal study of the text).
