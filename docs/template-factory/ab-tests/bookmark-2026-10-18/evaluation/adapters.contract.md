# Blind browser adapter contract

Each adapter exports `createAdapter(page, baseUrl)`. It uses the product's own rendered UI only; no direct HTTP API or database writes. X and Y may use different selectors but must implement identical operations and observations.

- `ready()` navigates to the app and waits for its initial UI.
- `save(record)` fills and submits the product's save form. Record fields are `url`, optional `title`, `note`, and `category` (null means unclassified).
- `createCategory(name)` uses the product UI.
- `viewCategory(name)` chooses `all`, null (unclassified), or an actual category name.
- `move(record, destination)` moves one existing record through the UI.
- `search(query)` enters and submits or applies the search; empty clears it.
- `records()` returns the currently visible record cards as `{url, title, note, text}`. Exact URL comes from the product's original-page link; text and fields come from rendered DOM. It must not invent fields from test fixtures.
- `openOriginal(record)` clicks the original-page link and returns its actual `href` observed immediately before the click. The harness blocks external navigation.
- `submitEmptyUrl()` opens a blank save form and clicks its submit control, accepting browser validation.
- Optional `doubleSave(record)` prepares one save form and clicks its submit control twice to explore duplicate submission behavior. If the UI makes a second click unavailable, return that observation.

Adapter failures (e.g. selector timeout) are unresolved test/tool errors until manually inspected; they are never automatically product failures. `records()` must faithfully extract the product UI without weakening field/record assertions. The harness stores body text and screenshots at each check and all actions/events in JSON.
