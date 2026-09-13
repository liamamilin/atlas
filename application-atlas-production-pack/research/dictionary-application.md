# Research Notes — Dictionary Application

Research date: 2026-09-07
Slug: dictionary-application
Directory leaf: Dictionary Application (§02.05 Reference & General Knowledge)

---

## Research Goal

Understand what a Dictionary Application is as an Application Type: what its corpus and entry structure look like, how lookup works, what surfaces users operate, what rules govern content and access, and where the boundary lies with neighboring reference/learning Types (Online Encyclopedia, General Reference Database, Knowledge Graph Explorer, Language Learning Application, Software Localization Management).

## Initial Boundary (hypothesis before research)

- Core use: consult the meaning, spelling, pronunciation, and usage of a word by entering a word form.
- Users: general readers, students, language learners, writers/editors, translators, professionals.
- Nearest neighbors: Online Encyclopedia (topical articles vs lexical entries), Language Learning Application (consultation vs curriculum), Software Localization Management (consumer lookup vs enterprise term bases), Knowledge Graph Explorer (entities vs words).
- Open questions: is the bilingual dictionary the same Type? Is the learner's dictionary a variant or its own Type? Is the community-edited model inside the Type?

## Research Questions

1. What is the unit of the corpus, and what does an entry contain across products?
2. How does lookup work (input forms, suggestions, multiple matches, misspellings)?
3. How are senses organized and labeled (grammar codes, register/region/domain labels, learner levels)?
4. What related-vocabulary machinery exists (thesaurus, synonyms, related words, collocations)?
5. Do products carry one dictionary or many references in one product?
6. What user-created data exists (saved words, word lists, history, quizzes)?
7. What engagement features exist (word of the day, games, blogs)?
8. What access/delivery models exist (free web, premium, institutional, platform-native, API/data licensing)?
9. Where are the boundaries with encyclopedia / language learning / translation / terminology management?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Role in sample |
|---|---|---|
| Cambridge Dictionary (Cambridge University Press & Assessment) | free web reference, learner-oriented, publisher lexicography | learner + bilingual breadth |
| Oxford Learner's Dictionaries (Oxford University Press) | free web + premium products, learner-oriented | learner depth, collocations, word lists |
| Oxford English Dictionary (OED, OUP) | subscription scholarly/historical record, personal + institutional access | scholarly/historical pole |
| Merriam-Webster (via its Developer Center / Dictionary API) | US commercial publisher; consumer site unreachable, API center reachable | multi-reference product family, audience-tiered dictionaries, data licensing |
| Apple Dictionary (macOS) | platform-native, offline, multiple licensed sources | platform-native pole, chained lookup |

Rejected/limited: Wiktionary (community-edited open dictionary) — unreachable during research (timeouts ×3); used only as a positioning example for the community-edited variant, with no product-specific claims. Dictionary.com not sampled (aggregator pole left as variant, unverified).

## Sources

Fetched 2026-09-07 (all Layer A unless noted):

- Cambridge Dictionary — root: https://dictionary.cambridge.org/
- Cambridge Dictionary — Help (FAQ): https://dictionary.cambridge.org/help/
- Cambridge Dictionary +Plus — Help: https://dictionary.cambridge.org/howto.html
- Cambridge Dictionary — entry "run": https://dictionary.cambridge.org/dictionary/english/run
- Oxford Learner's Dictionaries — root: https://www.oxfordlearnersdictionaries.com/
- Oxford Learner's Dictionaries — entry "run" (verb): https://www.oxfordlearnersdictionaries.com/definition/english/run_1
- Oxford English Dictionary — root: https://www.oed.com/
- Apple — Dictionary User Guide for Mac: https://support.apple.com/guide/dictionary/welcome/mac
- Merriam-Webster — Developer Center: https://dictionaryapi.com/ and https://dictionaryapi.com/products/index

Access limitations:

- https://www.merriam-webster.com/ returned 403 (consumer site not reachable). Merriam-Webster evidence is limited to its Developer Center/API documentation. No consumer-side feature claims (Word of the Day, games, etc.) are made for Merriam-Webster.
- Wiktionary (www.wiktionary.org, en.wiktionary.org) timed out ×3. Included only as a named positioning example; zero product-specific claims.
- Apple evidence covers the macOS Dictionary app only; iOS behavior not separately verified.

---

## Product Observations

### Cambridge Dictionary (Layer A unless noted)

Root page:

- One product carries many references: English, Learner's Dictionary, Essential British English, Essential American English, Grammar (British), Thesaurus, Pronunciation (British and American with audio), plus ~15 bilingual dictionaries (English–Chinese Simplified/Traditional, Danish, Dutch, French, German, Indonesian, Italian, Japanese, Norwegian, Polish, Portuguese, Spanish, Swedish) and ~17 "semi-bilingual" dictionaries (Arabic, Bengali, Catalan, Czech, Gujarati, Hindi, Korean, Malay, Marathi, Russian, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese).
- Site-wide language switcher (20+ UI languages); dictionary selector ("Choose a dictionary") with Recent and Recommended.
- Word of the Day (with definition); New Words blog; Word of the Year pages (2021–2025); Games hub (e.g. Word Scramble).
- Cambridge Dictionary +Plus: word lists and quizzes, create/download/share.
- Popular searches list; A–Z browse index (browse/english/a … z, plus 0–9) and a full index browse.
- Developer surfaces: Dictionary API, Double-Click Lookup, Search Widgets, License Data.

Help (FAQ):

- Editorial process: a team of lexicographers monitors new words against the Cambridge English Corpus; frequency and range of contexts over time decide inclusion; possibly ephemeral words are recorded and reviewed later.
- SMART Vocabulary: panels in many entries showing related words and phrases; "See more results" shows the topic as a frequency-sized word cloud.
- Pronunciation: most entries have two speaker icons (British and American audio); all entries include IPA transcriptions.
- Grammar codes documented (codes.html); "sb"/"sth" substitution conventions.
- CEFR labels A1–C2 (English Profile) shown on words, phrases, or meanings.
- +Plus app (iOS/Android) account deletion flow — confirms a mobile app exists with account-bound data.

+Plus Help (howto.html):

- Profile: occupation (Student/Teacher/Business/Other) and English level (Beginner/Intermediate/Advanced/Native Speaker).
- Word lists: personal lists + Cambridge-created lists + community public lists; a word is saved per meaning (the save icon sits next to a specific meaning); list cap 500 words (product-specific number); public sharing requires ≥5 words (product-specific); download to Excel; tags for filtering.
- Quizzes generated from word lists: gap fill, multiple choice, audio; answer review; quiz download to Excel. Image quizzes and Grammar quizzes exist as separate +Plus surfaces.

Entry "run" (verb):

- Headword + part of speech; UK and US IPA with audio buttons; inflected forms line (present participle running | past tense ran | past participle run).
- Senses grouped under capitalized sense headers: run verb (GO QUICKLY), (TRAVEL), (OPERATE), (FLOW), (BECOME).
- Per-sense CEFR badge (A1, B2, B1) and grammar codes ([I or T], [+ to infinitive], [T], [L only + adj], [+ two objects]).
- Definitions written with inline links — nearly every word in a definition links to its own entry.
- Example sentences per sense; "More examples / Fewer examples" toggle.
- Phrasal-verb sub-entries inline (run away, run off, run up to, run against) and idiom sub-entries (run a tight ship) with "See more" links to their own entries.
- Per-sense "Thesaurus: synonyms, antonyms, and examples" panel (run/sprint/jog/race/rush/dash, each with an example sentence, "See more results").
- SMART Vocabulary panel per sense, topic-labeled (Moving quickly; Advancing and moving forward; Machines – Functioning; Movement of liquids), plus additional topic links.
- Inline Synonyms block (dribble, drip, flow, spill, trickle) with sense disambiguators.
- Region variants noted inside entries ("run on the spot UK (US run in place)").
- "Add to word list" affordance per sense.

### Oxford Learner's Dictionaries (Layer A unless noted)

Root page:

- Multiple references: English (Oxford Advanced Learner's Dictionary), American English, Academic English, Collocations, German–English (Schulwörterbuch); Grammar (Practical English Usage; Learn & Practise Grammar beta); Word Lists (Oxford 3000/5000, OPAL, Topics, My Word Lists, Recent additions); Resources (Text Checker).
- Oxford 3000/5000: core-word lists aligned to CEFR levels, promoted as the learning spine.
- Topic Dictionaries: topic-related word lists (Animals, Health) with subtopics, each word CEFR-leveled.
- Word of the Day (drawn from a word list, e.g. OPAL written words); "Spread the Word" recent-additions blog.
- Premium products on the same site (OALD premium, Learner's Dictionary of Academic English, Practical English Usage, Collocations Dictionary, Schulwörterbuch); Redeem / Upgrade / Sign in flows.
- API offering (Oxford Learner's Dictionaries API); search widget; browse.

Entry "run" (verb):

- Headword + verb; Oxford 3000 A1 badge; BrE and AmE IPA separately.
- Full Verb Forms table (present simple, he/she/it runs, past simple ran, past participle run, -ing form running) with IPA for each form.
- Senses with short lowercase headers ("move fast on foot", "race", "hurry", "manage", "provide", "buses/trains", "vehicle/machine", "drive somebody", "move somewhere", "lead/stretch", "liquid", "of colour", "melt", "be/become", "continue for time", "happen", "in election", "guns, drugs, etc.", "of story/argument", "of newspaper/magazine", "a test/check", "of tights/stockings").
- Per-sense CEFR badges (A1/B1/B2/C2) and grammar labels ([intransitive], [transitive], + adv./prep., usually used in the progressive tenses).
- Example sentences; expandable "Extra Examples".
- "Topics" links per sense (Health and fitness a1; Business b1; Computers b2; Politics b2; Crime and punishment c2 …).
- Oxford Collocations Dictionary panel per sense (adverb / verb + run / preposition collocations) with "See full entry" into the Collocations dictionary; app cross-promotion.
- "see also" cross-references (mile, runner, runny); inline synonym links (organize, smuggle, ladder); "compare stand" (BrE/AmE usage contrast).
- Word Origin section (etymology: Old English rinnan, irnan …).
- Idioms section (come running, run for it, up and running …) — some idioms hosted at other headwords with pointers.
- Phrasal Verbs section (~25 entries listed).
- "Other results — All matches": all entries sharing the form (run noun, run-in noun, phrasal verbs, idioms).
- Cross-dictionary switches: "See run in the Oxford Advanced American Dictionary", "See run in the Oxford Learner's Dictionary of Academic English".
- "Check pronunciation" link; "Nearby words" alphabetical neighbors (rumpus room, rumpy pumpy, run verb, run noun, runabout).

### Oxford English Dictionary — OED (Layer A)

- Self-description: "the historical English dictionary" — meaning, history, and usage of over 500,000 words and phrases across the English-speaking world (vendor-stated figure).
- Historical Thesaurus: words used for the same concept/meaning over time.
- "Understanding entries" resources: glossaries, abbreviations, pronunciation guides, frequency, symbols.
- Ongoing editorial revision surfaced on the home page: "Recently added" and "Recently updated" entry lists.
- Word of the Day (email subscription); Word stories (etymology/semantic development); Word lists; World Englishes hub; History of English commentaries.
- AI Search Assistant: constructs complex queries and links to results; explicitly not conversational; daily query cap (10/day, vendor-stated).
- Advanced search over Entries.
- Access: personal account (save searches, display settings, purchase subscriptions) and institutional access (Shibboleth SSO, library card, username/password; "recommend to your librarian"); purchasing page; contribute channel ("Contribute to the OED").

### Merriam-Webster — Developer Center / Dictionary API (Layer A; consumer site 403)

- The publisher sells its reference content as a family of JSON APIs: Collegiate Dictionary with Audio, Collegiate Thesaurus, Spanish-English Dictionary with Audio, Medical Dictionary with Audio, Learner's Dictionary with Audio, Elementary Dictionary with Audio (grades 3–5), Intermediate Dictionary with Audio (grades 6–8), Intermediate Thesaurus (grades 6–8), School Dictionary with Audio (grades 9–11).
- Content types named: authoritative definitions, etymologies, audio pronunciations, synonyms and antonyms.
- Access model: free for non-commercial use under a per-key daily query cap (1000/day, vendor-stated, two-reference limit); commercial use negotiated case-by-case.
- Audience-tiered dictionaries (grade bands) are an explicit product dimension.
- Consumer web/app behavior NOT verified (403) — no claims made.

### Apple Dictionary (macOS) — User Guide (Layer A)

- "With Dictionary on your Mac, you can easily get definitions of words and phrases from a variety of sources."
- Multiple sources in one window; the user selects which source to search (e.g. Thesaurus for synonyms/antonyms); sources are selected and reordered in Settings (e.g. Spanish or Korean dictionaries; per-source options such as how pronunciations display, or which language of Wikipedia to search).
- Sources must download completely before searching — offline content packs.
- Search field → definition; while reading, blue links to related words; hovering any word and clicking looks it up (chained lookup).
- SnapBack button returns to the starting definition; Previous/Next buttons (and trackpad swipe) move through viewed definitions — a lookup history navigation model.
- Font size controls; pinch zoom.
- No results → the word may not be in the selected sources or may be restricted by Screen Time; "If possible, Dictionary suggests alternative words."
- Profanity restriction via Screen Time settings (platform-level content control).
- System integration: Spotlight can surface quick definitions; separate "Look up words on Mac" help article (system-wide lookup gesture).

---

## Cross-product Comparison

| Dimension | Cambridge | Oxford Learner's | OED | Merriam-Webster (API view) | Apple Dictionary |
|---|---|---|---|---|---|
| Corpus unit | entry per headword × POS, senses with headers | entry per headword × POS, senses with headers | entry per headword, historical structure | dictionary/thesaurus reference products | entries from multiple licensed sources |
| Lookup key | word form (search bar, double-click lookup) | word form (search box) | word form + advanced search | word form via API | word/phrase via search field, system lookup |
| Inflected forms | listed in entry (running/ran/run) | full verb-forms table with IPA | historical forms | (content types incl. definitions; morphology not verified) | suggestions on no results |
| Pronunciation | UK+US audio + IPA in all entries | BrE+AmE IPA (+audio site-wide) | pronunciation guides documented | audio pronunciations in APIs | per-source display options |
| Sense labels | grammar codes, CEFR A1–C2, region notes | grammar labels, CEFR badges, topic links | glossaries/symbols/frequency resources | (not verified) | — |
| Examples | per sense + More examples toggle | per sense + Extra Examples | historical quotations (implied by "usage/history" positioning; not entry-verified) | (not verified) | (source-dependent) |
| Thesaurus/related | per-sense thesaurus panel + SMART Vocabulary topics + inline synonyms | Collocations panel + synonym links + see-also | Historical Thesaurus (concept over time) | separate Collegiate Thesaurus API | Thesaurus as a selectable source |
| Etymology | (not observed on entry) | Word Origin section | Word stories; core to mission | etymologies in API | (source-dependent) |
| Multiple references in one product | yes (definitions/grammar/thesaurus/pronunciation/bilingual) | yes (English/American/Academic/Collocations/German) | single scholarly corpus + thesaurus | yes (9 reference APIs) | yes (selectable/reorderable sources incl. Wikipedia) |
| Browse | A–Z index | browse + word lists + topics | advanced search + updates feeds | (n/a) | (search-primary; no browse observed) |
| User collections | +Plus word lists (per-meaning save, share, download) | My Word Lists | save searches | (n/a) | (none observed) |
| Learning extras | quizzes (gap fill/multiple choice/audio), games, image/grammar quizzes | Oxford 3000/5000, Topic Dictionaries, Learn & Practise Grammar, Text Checker | word stories, World Englishes, history commentaries | (learner/elementary/school dictionaries as products) | — |
| Word of the Day | yes | yes | yes (email) | (not verified) | — |
| Access model | free web + account (+Plus) + app | free + premium products + redeem codes | personal + institutional subscription | free non-commercial API tier + commercial licensing | bundled with OS |
| Delivery | web + mobile app + API + widgets + data licensing | web + API + apps (collocations app) | web (subscription) | API/data | OS-native app, offline packs |

## Canonical Abstraction

### L0 — Defining Invariant

1. **Lexical-entry corpus** — the content is a structured collection of entries, each keyed to a headword (a word or phrase) and describing that word's linguistic properties. The corpus is organized by word, not by topic.
2. **Word-form lookup** — the primary interaction is entering a word form and being taken to the entry or entries for it.
3. **Definitional content** — each entry explains what the word means (one or more senses/definitions). Without definitional content the product is a spell-checker, index, or word list, not a dictionary.

Test: remove the entry-per-word organization (make it topical articles) → encyclopedia. Remove lookup (make it a feed) → content site. Remove definitions (keep only spellings/sounds) → spell-checker/pronunciation tool. All three properties are required.

Historical/market-sample check (§24): print dictionaries, CD-ROM dictionaries, handheld translators, platform-native OS dictionaries, web dictionaries, community wikis, and API-only dictionary data all satisfy L0. The definition does not depend on audio, apps, CEFR levels, thesaurus panels, or any modern engagement layer. Pass.

### L1 — Common Mature Structure

- **Entry anatomy**: headword + part of speech + inflected forms + pronunciation (IPA; audio common) + ordered senses with definitions + example sentences. (Cambridge, Oxford Learner's directly; MW API names definitions/audio; Apple sources deliver definitions.)
- **Sense organization and labels**: senses grouped under headers or short glosses; grammar codes (transitivity, patterns); register/region/domain labels; learner-level labels (CEFR) in learner products.
- **Related-vocabulary machinery**: synonyms/antonyms (per-sense panels, separate thesaurus references, or thesaurus sources); related-words-by-topic; collocations (learner pole); see-also cross-references; linked words inside definitions enabling chained lookup.
- **Multiple references in one product**: general + learner + thesaurus + grammar + pronunciation + bilingual dictionaries coexisting under one search.
- **Multi-match results**: one form maps to several entries (run verb / run noun / phrases); products present "all matches" or disambiguation.
- **Lookup tolerance**: suggestions/alternative words on misspelling or no-result input (Apple documented; URL disambiguation observed at Oxford/Cambridge).
- **Browse**: A–Z indexes alongside search.
- **User collections**: saved words/word lists (per-meaning save granularity at Cambridge), lookup history (Apple's SnapBack/navigation; implied elsewhere).
- **Engagement layer**: Word of the Day (Cambridge, Oxford, OED), quizzes/games (Cambridge), word lists as learning spine (Oxford 3000/5000), editorial blogs/new-words features.
- **Etymology**: word-origin sections (Oxford), etymologies as API content (MW), word stories (OED).
- **Multi-surface delivery**: web + mobile apps + API/data licensing + platform integration (Apple system lookup/Spotlight).
- **Tiered access**: free ad-supported web, premium products/subscriptions, institutional licensing (OED), data licensing (MW, Cambridge, Oxford APIs).

### L2 — Variant / Optional Structure

- **Dictionary kind**: general monolingual; learner's (controlled defining vocabulary, CEFR levels, collocations, extra examples); scholarly/historical (OED: historical record, revision program, Historical Thesaurus); bilingual and semi-bilingual; specialized domain (medical); audience-tiered (children/elementary/intermediate/school grade bands at MW).
- **Editorial model**: publisher lexicography with corpus-driven word admission (Cambridge documented); licensed multi-source aggregation (Apple); community-edited (Wiktionary — positioning only, unverified); scholarly revision programs (OED recently added/updated).
- **Learning posture**: pure consultation vs learning-oriented (word lists, quizzes, games, level profiles).
- **Platform posture**: standalone web/app vs platform-native bundled (Apple) vs API/data product (MW/Cambridge/Oxford developer offerings).
- **Offline vs online**: downloadable source packs (Apple); web-only (Cambridge/Oxford free tiers).
- **Regional scope**: BrE/AmE dual pronunciation and variant notes; World Englishes (OED); UI language breadth (Cambridge 20+ locales).

### L3 — Vendor-specific (research notes only)

- Cambridge: SMART Vocabulary frequency-sized topic clouds; +Plus 500-word list cap; ≥5-word public-list rule; per-meaning save; semi-bilingual dictionary category; Double-Click Lookup; Word of the Year; profile occupation/level.
- Oxford Learner's: Oxford 3000/5000; OPAL word lists; Text Checker; Practical English Usage online; Collocations app cross-promotion; redeem/upgrade codes; "Nearby words" strip.
- OED: AI Search Assistant with 10-query/day cap; Historical Thesaurus; "recently added/updated" revision feeds; Shibboleth/library-card institutional access; contribute channel; vendor-stated 500,000+ words.
- Merriam-Webster: 1000 queries/day free non-commercial API cap; grade-band dictionary family (3–5/6–8/9–11); brand guidelines for licensees.
- Apple: SnapBack; Screen Time profanity restriction; source download-before-search behavior; per-source pronunciation display options; Wikipedia as a dictionary source; Spotlight integration.

## Rejected Findings (considered, not promoted)

- "Dictionaries have audio pronunciation" — common but not definitional (print dictionaries lack it; platform sources vary). L1.
- "Dictionaries include thesaurus/related words" — very common, but a standalone dictionary without thesaurus is still a dictionary. L1.
- "Learner levels (CEFR) are part of entries" — learner-segment implementation. L2.
- "Word of the Day / games are part of the Type" — engagement layer, absent in platform-native and scholarly poles. L1/L2.
- "Bilingual dictionaries are a separate Type" — same corpus unit (headword-keyed entries), same lookup, different entry content (equivalents instead of definitions). Variant, not separate Type.
- "Community-edited dictionaries are a separate Type" — editorial model differs, corpus unit and lookup identical. Variant.
- "Translation of arbitrary text" — outside the Type (that is a translation product; not a directory leaf here). Dictionary translation surfaces (Cambridge Translate tab) are adjacent extensions.

## Boundary Findings

- **vs Online Encyclopedia**: encyclopedia = topical articles about subjects, retrieved by topic/entity; dictionary = lexical entries about words, retrieved by word form. Remove entry-per-word organization → encyclopedia. The same lookup box over different corpus organization is the seam.
- **vs General Reference Database**: reference databases answer factual questions about entities/data; dictionaries answer word questions (meaning, spelling, pronunciation, usage). Overlap only in that both are consultation reference.
- **vs Knowledge Graph Explorer**: entities and typed relations vs words and senses. A thesaurus/related-words panel is word-neighborhood, not an entity graph.
- **vs Language Learning Application**: consultation (pull, per-word, no curriculum state) vs learning (push, structured lessons, progress, spaced practice). Dictionary quizzes/word lists serve word consolidation; they do not constitute a course. Seam products: learner dictionaries with level labels sit closest.
- **vs Translation Application** (no directory leaf; nearest is Language Learning Application): bilingual dictionary returns per-word equivalents; translation products render arbitrary text. Semi-bilingual dictionaries (headword + native-language equivalents + English definition) are the blur zone — still headword-keyed entries.
- **vs Software Localization Management (§12)**: enterprise terminology/term-base management for product consistency vs consumer word reference. Different users (translators/terminologists vs general readers), different objects (term bases, QA vs entries).
- **vs Answer Engine / AI Research Assistant (§02.03)**: returns canonical editorial entry content for a word vs synthesizes answers to open questions. OED's AI Search Assistant is query assistance over the entry corpus, not answer generation — the assistant itself states it does not generate answers.
- **vs Spell/grammar checkers** (not a directory leaf): correction of user text vs reference about words. No overlap in core object.

## Uncertainties

- Merriam-Webster consumer web/app features unverified (403). Anything about its consumer experience (games, Word of the Day, editor features) is deliberately absent.
- Wiktionary unreachable; community-edited variant described structurally without product claims.
- Whether inflected-form lookup normalization (typing "ran" → "run" entry) is universal: entries document forms (observed), Apple documents alternative-word suggestions (observed), but automatic lemma redirection was not directly observed per product. Kept at moderate wording.
- OED entry-level anatomy (quotations, frequency badges) inferred from "Understanding entries" resource listing, not from a fetched entry page.
- Apple iOS dictionary behavior not verified (macOS guide only).
- Corpus sizes (OED 500,000+; Oxford 3000/5000 counts) are vendor-stated figures, quoted with attribution only.

## Final Synthesis

A Dictionary Application is a consultation reference whose world consists of a corpus of lexical entries keyed by headwords, a word-form lookup as the primary interaction, and definitional content (senses) as the payload. Mature products wrap this core in a standard capability set: rich entry anatomy (part of speech, inflected forms, IPA/audio pronunciation, labeled senses, examples), related-vocabulary machinery (thesaurus, related words, collocations, cross-references, chained lookup), multiple references under one search (general/learner/thesaurus/grammar/bilingual), browse, user collections (word lists/history), an engagement layer (word of the day, quizzes, games), and multi-surface delivery (web, apps, API/data licensing, platform integration). The Type's variants are dictionary kinds (general, learner's, scholarly/historical, bilingual, domain, audience-tiered), editorial models (publisher, licensed aggregation, community), and postures (reference vs learning-oriented). The defining core survives the historical check: it holds for print-era content, CD-ROM and handheld devices, platform-native OS dictionaries, and modern web/API products alike.
