# Core verification for the feedreader service

`probe.py` is a portable acceptance orchestrator for the self-hosted feed reader service. It does **not** implement the target: it drives the JSON API of a running instance and asserts observable results, including negative cases.

## 1. Requirements

- Python 3.9 or newer, standard library only (`urllib`, `http.server`, `xml.etree`).
- A running `feedreader` instance with the JSON API enabled (`FEEDREADER_API_KEY` set on the service, same value in the probe environment).
- A **disposable instance**. `mark all as read` is account wide, so the probe refuses to run when the instance already holds subscriptions it did not create, and it only deletes records whose category starts with `probe-` or whose feed title starts with `Probe `.

## 2. Start the service (acceptance environment)

```sh
export FEEDREADER_DATABASE_URL='postgres://feedreader:feedreader@127.0.0.1:5432/feedreader_acceptance?sslmode=disable'
export FEEDREADER_API_KEY='acceptance-key'
export FEEDREADER_USERNAME=reader
export FEEDREADER_PASSWORD='reader-pass'
export FEEDREADER_POLLING_INTERVAL=5s      # short interval so the scheduled intake is observable in seconds
feedreader migrate
feedreader serve
```

`FEEDREADER_POLLING_INTERVAL=5s` is what makes the standing-intake check observable. With the default one hour interval the probe reports that single check as `not_run` and falls back to the explicit refresh endpoint, so the scheduler path stays unverified in that run.

## 3. Run the probe

```sh
FEEDREADER_BASE_URL=http://127.0.0.1:8080 \
FEEDREADER_API_KEY=acceptance-key \
python3 acceptance_files/probe.py
```

Optional environment variables:

| Variable | Meaning |
| --- | --- |
| `FEEDREADER_BASE_URL` | Base URL of the service (default `http://127.0.0.1:8080`) |
| `FEEDREADER_API_KEY` | Value sent in the `X-Api-Key` header |
| `FEEDREADER_INTAKE_TIMEOUT` | Seconds to wait for the scheduled intake (default 60) |
| `FEEDREADER_STRICT` | `1` turns a `not_run` result into a failure |
| `FEEDREADER_FIXTURE_HOST` / `FEEDREADER_FIXTURE_PORT` | Bind address of the probe's own fixture server (default `127.0.0.1`, ephemeral port) |
| `FEEDREADER_FIXTURE_BASE` | Base URL the **service** must use to reach the fixture server (default: the loopback address of the fixture server) |

Exit codes: `0` every executed check passed, `1` at least one check failed, `2` the target was unreachable or not configured so nothing was executed. The summary lists every `not_run` check with its reason; no check ever reports success without an assertion behind it.

## 4. The fixture server

The probe starts its own loopback HTTP server that serves RSS 2.0 fixtures (`/feed/alpha.xml`, `/feed/beta.xml`, `/feed/gamma.xml`, `/feed/delta.xml`) plus `/not-a-feed`, which returns HTML and must be refused. The `delta` fixture declares `<ttl>120</ttl>`. The server answers conditional requests with `304` when the `ETag` still matches, and the probe publishes new items through its own `/publish` control endpoint. The service must be able to reach that address; when the service runs in a container, publish the fixture port and set `FEEDREADER_FIXTURE_BASE` to the address the container sees.

## 5. What each case asserts

- **A01 standing intake** — subscribing a feed URL stores its first item as unread with the feed title and the canonical link; the unread counts move by one; a newly published item reaches the unread view through the background scheduler and is listed exactly once even though the publisher re-delivers the older item; a repeated forced refresh inserts nothing; a feed that declares a TTL gets its next check pushed beyond the polling interval.
- **A02 reading state** — marking one item read removes it from the unread view and lowers both the per feed and the total count; starring is independent; marking an already read item again changes nothing; an intake refresh keeps `read` and `starred`; bulk marking by feed, by category, on an empty scope and over the whole account; the starred flag survives the bulk read; an unknown item id returns 404 and an invalid status returns 400.
- **A03 OPML round trip** — the export holds exactly one outline per subscribed feed, each inside its category outline; deleting a subscription and re-importing the exported file recreates it with the same url and category; importing the same file again creates nothing; malformed XML is rejected with 400 and changes nothing; a folder-only outline creates no subscription.
- **A04 subscription list** — the list shows every feed with its category; a duplicate feed url, an unknown category, a url that is not a feed and a malformed url are all rejected without creating a subscription; a newly subscribed feed appears in the list; every stored item belongs to a subscribed feed, which is the list-is-the-selector rule.
- **A05 reader view** — the reader view returns the item content, its feed title and its canonical link; previous/next entries are drawn from the already-read items only; an unread item never appears as a neighbour; an unknown item id returns 404 and a malformed id is rejected.

## 6. Cleanup

The probe deletes only what it created: the feeds it subscribed and the `probe-` categories it made, then prints how many subscriptions and categories are left. A failed run may leave records behind; the next run removes the leftovers that match the probe prefixes before it starts.

## 7. Honest limits

- The probe was authored but not executed while writing this blueprint. No case outcome is claimed until an operator runs it against a live instance.
- Only RSS 2.0 fixtures are exercised; Atom and JSON Feed parsing is specified in the service contract but not covered here.
- The scheduled-intake check depends on a short polling interval; with the default one hour interval it is reported as `not_run` rather than silently passed.
- The probe talks to the JSON API only. The web surfaces (sidebar, unread view, reader view, settings) are checked by the operator in the browser, using the same steps as the morning routine described in the architecture note.
