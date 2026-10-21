# Core verification for the feedreader service

`probe.py` is a portable acceptance orchestrator for the self-hosted feed reader service. It does **not** implement the target: it drives the JSON API of a running instance and asserts observable results, including the negative cases.

## 1. Requirements

- Python 3.9 or newer, standard library only (`urllib`, `http.server`, `xml.etree`, `hashlib`).
- A running `feedreader` instance with the API enabled (`FEEDREADER_API_KEY` set on the service, same value in the probe environment).
- A **disposable instance**. `read-all` is account wide, so the probe refuses to run when the instance already holds subscriptions outside its own `probe-` categories, and it deletes only feeds inside those categories and categories whose title starts with `probe-`. It never deletes a record it did not create.
- The service must be able to reach the probe's loopback fixture server. The probe starts that server on `127.0.0.1` with an ephemeral port and stops it at the end; the feed URLs it subscribes point at that address.

## 2. Start the service (acceptance environment)

```sh
export FEEDREADER_DATABASE_URL='postgres://feedreader:feedreader@127.0.0.1:5432/feedreader_acceptance?sslmode=disable'
export FEEDREADER_API_KEY='acceptance-key'
export FEEDREADER_USERNAME='reader'
export FEEDREADER_PASSWORD='reader-pass'
export FEEDREADER_LISTEN_ADDR='127.0.0.1:8080'
export FEEDREADER_POLLING_INTERVAL='5s'
feedreader migrate
feedreader serve
```

`FEEDREADER_POLLING_INTERVAL=5s` is legal: the configured interval is used verbatim and is **not** clamped to a lower floor (architecture, section 2.1). This is what makes the standing-intake check observable in seconds. With the default one hour interval the probe reports that single check as `not_run`, falls back to the explicit refresh endpoint for the remaining A01 checks, and the scheduler path stays unverified in that run.

Use a disposable database: the probe creates and removes its own categories and feeds, and A02 marks the whole account read.

## 3. Run the probe

```sh
FEEDREADER_BASE_URL=http://127.0.0.1:8080 FEEDREADER_API_KEY=acceptance-key python3 acceptance_files/probe.py
```

| Variable | Default | Meaning |
| --- | --- | --- |
| `FEEDREADER_BASE_URL` | `http://127.0.0.1:8080` | Base URL of the service |
| `FEEDREADER_API_KEY` | empty | Value sent in the `X-Api-Key` header |
| `FEEDREADER_INTAKE_TIMEOUT` | `60` | Seconds the probe waits for the scheduled intake; the wait is `max(this, 4 x polling interval)` |
| `FEEDREADER_HTTP_TIMEOUT` | `30` | Per-request timeout of the probe |
| `FEEDREADER_REPORT` | empty | Path of a JSON report with every check and its status |

Exit codes: `0` every executed check passed, `1` at least one check failed, `2` the service was unreachable or the instance was not disposable (nothing ran). `not_run` checks are listed in the summary and do not fail the run.

## 4. What each case does

| Case | Checks |
| --- | --- |
| A01 standing intake | subscribes a fixture feed, checks the item published before subscribing is stored unread, publishes a new item and waits for the **scheduler** to deliver it, checks the delivered item carries the feed title and its canonical link, republishes a known identifier and checks no second row appears, checks the fetch was conditional (`If-None-Match` / `If-Modified-Since`) |
| A05 reader view | opens the middle item of a three item feed, checks the reader view returns the content, the feed title and the canonical link of the entry the probe selected, checks previous/next point at the read entries on either side, and checks that an unknown id is reported as not found |
| A02 reading state | stars an item while it is unread, marks it read and checks the starred flag survives, checks the unread view and the unread counts fall, checks the bulk marks per feed, per category and for the whole account, and checks that an unknown status value is refused |
| A03 OPML round trip | exports the list, checks one feed outline per subscribed feed with its `xmlUrl` inside its category outline, deletes only the probe feeds, imports the file back and checks the same subscriptions return, imports it again and checks nothing is duplicated |
| A04 subscription list | subscribes a feed URL and a site URL (the page that advertises a feed) and checks both are listed in the category with the feed title, and checks that a duplicate feed URL, an unknown category, a malformed URL, a page without a feed and a body that is not a feed are all refused without creating a subscription |

The probe never assumes the order in which the service returns entries: it selects an entry by its URL and compares the reader view against that same entry.

## 5. Operator steps for the HTML surface (checked by hand, not asserted)

The probe drives the JSON API. The operator checks the web surface of the target separately:

1. open `http://127.0.0.1:8080/` and confirm the unread view lists what arrived, newest first, with the per feed unread counts in the sidebar;
2. open an item, confirm the reader view shows the stored content, the feed title and a link to the source, then use the mark read and star toggles and the previous/next links;
3. open `/feeds`, add a feed by URL and by site URL, delete a feed and confirm the per feed unread count updates;
4. export the list and import it again, confirming the same subscriptions reappear without duplicates.

Human decisions that stay with the operator: which category a new feed goes into, whether a feed that stopped parsing is deleted, and what to star versus what to read.

## 6. Honest limits

- The scheduled-intake check of A01 is `not_run` when the service does not report `polling_interval_seconds` on `GET /api/v1/config`, or when the configured polling interval is longer than `FEEDREADER_INTAKE_TIMEOUT`. In that run the scheduler path is unverified.
- The probe exercises RSS 2.0 fixtures only. Atom 0.3/1.0 and JSON Feed 1.0/1.1 parsing is in the contract but has no acceptance case.
- The HTML surface is not asserted; only the JSON API is.
- The probe was not executed in this workspace: no target service was built or run here, so the results it reports are the results of a real run, never a claim about one.
- The upstream project was read as a design reference only and was never built, installed or run.