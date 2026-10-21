# Acceptance probe - Personal Month-Grid Calendar (desktop)

## What this is
`probe.py` is a **verifier**, not the product. It imports the target package
`calendar_app` and drives its real controller, model, store and month-frame code.
When a graphical display is available it also drives the real Tk widget tree
(header buttons, day-cell frames, event-block labels, editor dialog).

The blueprint in `authored.arch` pins the contract the probe checks, including
the exact public API (`create_app`, `CalendarController.save_new`,
`save_existing`, `delete`, `open_month`, `grid.weeks`, `grid.blocks_on`,
`grid.header_label`, `store.path`) and the Tk seams
(`window.grid_geometry()`, `window.header_weekday_labels()`,
`window.header_label_text()`, `window.next_button`, `window.prev_button`,
`window.open_editor(...)`, `dialog.title_var/start_var/end_var/location_var/notes_var/error_var`,
`dialog.save()`).

## Prerequisites
- Python 3.9+ (standard library only; nothing to install).
- The target implementation next to this file:

      calendar_app/__init__.py
      calendar_app/timeutil.py
      calendar_app/model.py
      calendar_app/store.py
      calendar_app/gridmodel.py
      calendar_app/controller.py
      calendar_app/app.py
      calendar_app/ui_tk.py
      calendar_app/__main__.py

- Optional but recommended: a graphical display (X11/Wayland/macOS Aqua/Windows).
  Without one the Tk assertions are reported as `NOT_RUN`, never as `PASS`.

## Run

      python3 probe.py
      python3 probe.py --app-path /path/to/checkout        # package elsewhere
      python3 probe.py --keep                             # keep the temp data dir

Exit status is `0` only when every executed check passed, `1` otherwise.

## Cases
| Case | What is asserted | Layer |
|---|---|---|
| A01 | exactly 7 weekday columns and 4-6 week rows; every day of the month is present; previous/next move exactly one month with year rollover and re-render; a past month is reachable | model + Tk |
| A02 | 2026-10-05 10:00-11:00 (+08:00) is created with title/location/notes, persisted with the `+08:00` offset, rendered on the October grid and read back by the editor; end==start, end<start, blank title and unparsable dates are refused and leave the store byte-identical; no recurrence/all-day/attendee/alert/time-zone field exists | model + store + Tk |
| A03 | 2026-10-31 22:00 to 2026-11-01 02:00 shows in the October and the November grid and in no filler cell; an end at exactly 00:00 does not touch that day; two overlapping appointments are both accepted and both rendered in one cell | model + store |
| A04 | an edit/reschedule keeps the uid, empties the old slot and shows the new title/time/location/notes in the new slot; a refused edit changes nothing; deleting a probe-created record removes it from the grid and the store while other records stay; deleting an unknown id is a no-op | model + store + Tk |
| A05 | a restart over the same data directory keeps every record with identical values, does not rewrite the store file, and still allows navigating back to a past month that shows its appointments; a separate data directory starts empty | model + store + Tk |

## Layers and honest limits
- **Layer 1 (always runs)** - model, store, controller and the month-frame model,
  driven through the public API, including assertions on the on-disk JSON.
- **Layer 2 (runs only with a display)** - the live Tk widget tree: real header
  buttons, real day-cell frames, real event-block labels, real editor variables
  and the real validation message. Reported as `NOT_RUN` otherwise.
- **Layer 3 (manual)** - the operator journey below.

## Data boundary
- Every run creates a fresh temporary directory (`calendar-probe-*`) and points
  the target at it; the probe never reads or writes the user's real store.
- Only records the probe itself created are deleted, and only inside that
  temporary directory.
- The temporary directory is removed at the end unless `--keep` is passed.

## Operator steps for the desktop journey (manual layer)
1. Run `python3 -m calendar_app --data-dir "$HOME/.local/share/personal-calendar"`.
2. The month frame opens with 7 weekday columns and 4-6 week rows; the header names the month.
3. Double-click an empty day cell (or press the new-appointment action): the editor opens pre-filled with 09:00-10:00.
4. Type a title, set start and end, optionally location and notes, press Save. The block appears on the grid.
5. Set the end equal to the start and press Save: a message appears and nothing is written.
6. Create a second appointment overlapping the first: both blocks are shown, neither save is refused.
7. Double-click the first block, change the title and move it to another day/time, press Save: the old slot is empty and the new slot shows the new title and time.
8. Use the header arrows to step to the next month and back to a past month; the frame re-renders each time.
9. In the editor of the probe-created record press Delete: the block disappears from the grid and from the store, and the other records stay.
10. Close the application, start it again, navigate back to the month of step 7: the appointments are still there.

## Limits (not_run)
- The upstream project was never installed, built or executed while authoring this blueprint; all upstream statements are read-only observations.
- The target implementation is not present in this workspace, so the probe is expected to fail loudly rather than pass until the code lands.
- On a headless machine the Tk assertions are `NOT_RUN`; they are never reported as passed.
- No certification, conformance or performance claim is made by a `PASS` result.
