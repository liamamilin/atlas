#!/usr/bin/env python3
'''Acceptance probe for the desktop Personal Month-Grid Calendar blueprint.

This file is a verifier, not the product. It imports the target package
(calendar_app) and drives its real controller, model, store and month-frame
code; when a graphical display is available it also drives the real Tk widget
tree (header controls, day cells, event blocks, editor dialog).

    python3 probe.py [--app-path DIR] [--keep]

Guarantees
  * every run uses a fresh temporary data directory; only records created by
    this probe are deleted, and only inside that directory;
  * checks that cannot be executed (widget-tree checks without a display) are
    reported as NOT_RUN and never as PASS;
  * the exit status is 0 only when every executed check passed.
'''

import argparse
import calendar as _calendar
import datetime as dt
import json
import shutil
import sys
import tempfile
import traceback
from pathlib import Path

UTC8 = dt.timezone(dt.timedelta(hours=8))
RESULTS = []
NOT_RUN = []


class ProbeFailure(AssertionError):
    '''A pinned requirement of the blueprint was not met.'''


def require(condition, message):
    if not condition:
        raise ProbeFailure(message)


def note_not_run(reason):
    NOT_RUN.append(reason)
    print('  NOT_RUN: %s' % reason)


def month_days(year, month):
    last = _calendar.monthrange(year, month)[1]
    return set(dt.date(year, month, day) for day in range(1, last + 1))


def in_month_dates(grid, year, month):
    cells = set()
    for week in grid.weeks:
        for cell in week:
            if cell.in_current_month:
                cells.add(cell.date)
    return cells


def detect_display():
    try:
        import tkinter  # noqa: F401
    except Exception as exc:
        return False, 'the tkinter module is unavailable (%s)' % exc
    try:
        root = tkinter.Tk()
        root.withdraw()
        root.destroy()
    except Exception as exc:
        return False, 'no usable graphical display (%s)' % exc
    return True, ''


def ui_snapshot(win):
    '''Read the event block titles out of the live Tk widget tree.'''
    import tkinter
    snapshot = {}
    for cell in win.grid_frame.winfo_children():
        day = getattr(cell, 'cell_date', None)
        if day is None:
            continue
        titles = []
        for child in cell.winfo_children():
            if isinstance(child, tkinter.Frame):
                for block in child.winfo_children():
                    try:
                        titles.append(block.cget('text'))
                    except Exception:
                        pass
        snapshot[day] = titles
    return snapshot


def _parse(text):
    return dt.datetime.strptime(text, '%Y-%m-%d %H:%M').replace(tzinfo=UTC8)


def _call_save(function, args, start_index):
    '''Call a controller save method with editor text; fall back to datetimes.'''
    try:
        return function(*args)
    except TypeError as exc:
        if 'strptime' in str(exc):
            raise
        alternative = list(args)
        alternative[start_index] = _parse(alternative[start_index])
        alternative[start_index + 1] = _parse(alternative[start_index + 1])
        return function(*alternative)


def save_new(controller, title, start_text, end_text, location='', notes=''):
    return _call_save(
        controller.save_new,
        (title, start_text, end_text, location, notes),
        1,
    )


def save_existing(controller, uid, title, start_text, end_text, location='', notes=''):
    return _call_save(
        controller.save_existing,
        (uid, title, start_text, end_text, location, notes),
        2,
    )


class Context(object):
    '''One isolated run: fresh temporary data directory, own target instances.'''

    def __init__(self, app_path):
        self.tmp = Path(tempfile.mkdtemp(prefix='calendar-probe-'))
        self.data_dir = self.tmp / 'data'
        self.data_dir.mkdir(parents=True, exist_ok=True)
        if str(app_path) not in sys.path:
            sys.path.insert(0, str(app_path))
        try:
            import calendar_app
        except Exception as exc:
            raise SystemExit(
                'the target package calendar_app could not be imported from %s (%s: %s)'
                % (app_path, type(exc).__name__, exc)
            )
        self.module = calendar_app
        self.tk_ok, self.tk_reason = detect_display()
        self._tk_app = None
        self._tk_broken = False

    def new_app(self, data_dir=None, headless=True):
        return self.module.create_app(
            data_dir=str(data_dir or self.data_dir), headless=headless
        )

    def controller(self):
        app = self.new_app()
        return app, app.controller

    def tk_app(self):
        if self._tk_broken:
            return None
        if self._tk_app is not None:
            try:
                if self._tk_app.window is not None and self._tk_app.window.winfo_exists():
                    return self._tk_app
            except Exception:
                self._tk_app = None
        try:
            self._tk_app = self.new_app(headless=False)
        except Exception as exc:
            self._tk_broken = True
            self.tk_reason = 'the desktop window could not be opened (%s)' % exc
            return None
        return self._tk_app

    def cleanup(self, keep):
        if keep:
            print('probe data directory kept: %s' % self.tmp)
        else:
            shutil.rmtree(str(self.tmp), ignore_errors=True)


def case_a01(ctx):
    '''A01 - the month frame is 7 columns by 4-6 rows and navigation moves one month.'''
    notes = []
    app, controller = ctx.controller()
    controller.open_month(2026, 10)
    grid = controller.grid
    require(
        len(grid.weekday_labels) == 7,
        'the month frame must expose exactly 7 weekday labels, got %d' % len(grid.weekday_labels),
    )
    require(
        4 <= len(grid.weeks) <= 6,
        'the month frame must have 4-6 week rows, got %d' % len(grid.weeks),
    )
    for index, week in enumerate(grid.weeks):
        require(len(week) == 7, 'week row %d must hold 7 day cells, got %d' % (index, len(week)))
    require(
        in_month_dates(grid, 2026, 10) == month_days(2026, 10),
        'the October 2026 frame must contain exactly the 31 days of October',
    )
    require(grid.header_label == 'October 2026', 'unexpected month header label %r' % grid.header_label)
    notes.append('model frame: 7 columns x %d week rows' % len(grid.weeks))

    controller.previous_month()
    require(
        (controller.year, controller.month) == (2026, 9),
        'previous must move exactly one month back, got %r' % ((controller.year, controller.month),),
    )
    controller.next_month()
    require(
        (controller.year, controller.month) == (2026, 10),
        'next must move exactly one month forward, got %r' % ((controller.year, controller.month),),
    )
    controller.next_month()
    require(
        (controller.year, controller.month) == (2026, 11),
        'next must move exactly one month forward, got %r' % ((controller.year, controller.month),),
    )
    require(
        in_month_dates(controller.grid, 2026, 11) == month_days(2026, 11),
        'the re-rendered frame must contain the days of November 2026',
    )

    controller.open_month(2026, 12)
    controller.next_month()
    require((controller.year, controller.month) == (2027, 1), 'December must roll over to January')
    controller.open_month(2026, 1)
    controller.previous_month()
    require((controller.year, controller.month) == (2025, 12), 'January must roll back to December')

    before_grid = controller.grid
    controller.open_month(2026, 8)
    require(controller.grid is not before_grid, 'navigating must rebuild the month frame')
    require(
        controller.grid.header_label == 'August 2026',
        'navigating back to a past month must re-render that month',
    )
    require(
        in_month_dates(controller.grid, 2026, 8) == month_days(2026, 8),
        'the past frame must contain the days of August 2026',
    )
    notes.append('navigation moves exactly one month, re-renders and rolls the year over')

    tk_app = ctx.tk_app()
    if tk_app is None:
        note_not_run('Tk widget-tree checks for the month frame: %s' % ctx.tk_reason)
    else:
        win = tk_app.window
        columns, rows = win.grid_geometry()
        require(columns == 7, 'the rendered frame must have 7 columns, got %d' % columns)
        require(4 <= rows <= 6, 'the rendered frame must have 4-6 rows, got %d' % rows)
        require(len(win.header_weekday_labels()) == 7, 'the rendered header must show 7 weekday labels')
        tk_app.controller.open_month(2026, 8)
        win.update_idletasks()
        require(win.header_label_text() == 'August 2026', 'unexpected rendered header %r' % win.header_label_text())
        win.next_button.invoke()
        win.update_idletasks()
        require(
            win.header_label_text() == 'September 2026',
            'the next control must advance the rendered month, got %r' % win.header_label_text(),
        )
        win.prev_button.invoke()
        win.update_idletasks()
        require(
            win.header_label_text() == 'August 2026',
            'the previous control must go back exactly one rendered month',
        )
        notes.append('rendered Tk frame: %d columns x %d rows, header navigation verified' % (columns, rows))
    return notes


def case_a02(ctx):
    '''A02 - create with title/location/notes, read back, and refuse invalid saves.'''
    notes = []
    app, controller = ctx.controller()
    controller.open_month(2026, 10)
    title = 'Probe Meeting'
    location = 'Room A'
    notes_text = 'probe notes'
    result = save_new(controller, title, '2026-10-05 10:00', '2026-10-05 11:00', location, notes_text)
    require(result.ok, 'a valid appointment must be accepted, errors=%r' % (result.errors,))
    appointment = result.appointment
    require(bool(appointment.uid), 'a created appointment must carry a uid')
    require(appointment.title == title, 'the title must round-trip, got %r' % appointment.title)
    require(
        appointment.start == dt.datetime(2026, 10, 5, 10, 0, tzinfo=UTC8),
        'the start must be stored at 2026-10-05 10:00 +08:00, got %r' % appointment.start,
    )
    require(
        appointment.end == dt.datetime(2026, 10, 5, 11, 0, tzinfo=UTC8),
        'the end must be stored at 2026-10-05 11:00 +08:00, got %r' % appointment.end,
    )
    require(appointment.location == location, 'the location must round-trip, got %r' % appointment.location)
    require(appointment.notes == notes_text, 'the notes must round-trip, got %r' % appointment.notes)

    store_path = Path(controller.store.path)
    require(store_path.exists(), 'the store file must exist after the first save')
    document = json.loads(store_path.read_text(encoding='utf-8'))
    require(document.get('schema_version') == 1, 'the store must carry schema_version 1')
    stored = [r for r in document['appointments'] if r['uid'] == appointment.uid]
    require(len(stored) == 1, 'the new appointment must be persisted exactly once')
    require(
        stored[0]['start'] == '2026-10-05T10:00:00+08:00',
        'the stored start must carry the fixed +08:00 offset, got %r' % stored[0]['start'],
    )
    require(
        stored[0]['end'] == '2026-10-05T11:00:00+08:00',
        'the stored end must carry the fixed +08:00 offset, got %r' % stored[0]['end'],
    )
    require(
        stored[0]['title'] == title
        and stored[0]['location'] == location
        and stored[0]['notes'] == notes_text,
        'the persisted record must keep title, location and notes',
    )

    blocks = controller.grid.blocks_on(dt.date(2026, 10, 5))
    require(
        any(b.uid == appointment.uid for b in blocks),
        'the appointment must render as a block on the October 2026 grid',
    )

    allowed = set(['uid', 'title', 'start', 'end', 'location', 'notes', 'created_at', 'updated_at'])
    require(
        set(stored[0].keys()) == allowed,
        'unexpected record fields: %r' % sorted(set(stored[0].keys()) - allowed),
    )
    forbidden = set([
        'rrule', 'recurrence', 'repeat', 'all_day', 'allday', 'attendees',
        'alerts', 'reminders', 'calendar', 'timezone', 'tzid',
    ])
    present = forbidden & set(stored[0].keys())
    require(not present, 'the record must not carry %r' % sorted(present))
    for record in document['appointments']:
        require('T' in record['start'], 'every appointment must carry a time of day')
        require(record['end'] > record['start'], 'every appointment must have a positive range')

    baseline = store_path.read_bytes()
    count = len(controller.all_appointments())

    same = save_new(controller, 'Bad', '2026-10-05 12:00', '2026-10-05 12:00', '', '')
    require(not same.ok, 'an appointment whose end equals its start must be refused')
    require('end' in same.errors, 'the refusal must be reported on the end field, got %r' % (same.errors,))
    require(store_path.read_bytes() == baseline, 'a refused save must not change the store file')
    require(len(controller.all_appointments()) == count, 'a refused save must not create a record')

    backwards = save_new(controller, 'Bad', '2026-10-05 13:00', '2026-10-05 12:00', '', '')
    require(not backwards.ok, 'an appointment whose end precedes its start must be refused')
    require(store_path.read_bytes() == baseline, 'a refused save must not change the store file')

    untitled = save_new(controller, '   ', '2026-10-05 12:00', '2026-10-05 13:00', '', '')
    require(not untitled.ok, 'an appointment without a title must be refused')
    require('title' in untitled.errors, 'the refusal must be reported on the title field')
    require(store_path.read_bytes() == baseline, 'a refused save must not change the store file')

    unparsable = save_new(controller, 'Bad', 'not-a-date', '2026-10-05 13:00', '', '')
    require(not unparsable.ok, 'an unparsable start must be refused')
    require('start' in unparsable.errors, 'the refusal must be reported on the start field')
    require(store_path.read_bytes() == baseline, 'a refused save must not change the store file')
    notes.append('create, read-back and record shape verified; refusals leave the store byte-identical')

    tk_app = ctx.tk_app()
    if tk_app is None:
        note_not_run('Tk editor read-back checks: %s' % ctx.tk_reason)
    else:
        win = tk_app.window
        dialog = win.open_editor(uid=appointment.uid)
        require(dialog.title_var.get() == title, 'the editor must show the stored title')
        require(dialog.start_var.get() == '2026-10-05 10:00', 'the editor must show the stored start')
        require(dialog.end_var.get() == '2026-10-05 11:00', 'the editor must show the stored end')
        require(dialog.location_var.get() == location, 'the editor must show the stored location')
        require(dialog.notes_var.get() == notes_text, 'the editor must show the stored notes')
        baseline = store_path.read_bytes()
        dialog.end_var.set('2026-10-05 09:00')
        require(dialog.save() is False, 'the editor must refuse an invalid range')
        require(dialog.error_var.get().strip() != '', 'the editor must show a validation message')
        require(store_path.read_bytes() == baseline, 'a refused editor save must not change the store file')
        try:
            dialog.destroy()
        except Exception:
            pass
        notes.append('editor read-back and refusal verified on the live widget tree')
    return notes


def case_a03(ctx):
    '''A03 - half-open spans, cross-month visibility and accepted overlaps.'''
    notes = []
    app, controller = ctx.controller()
    controller.open_month(2026, 10)

    span = save_new(controller, 'PROBE cross month', '2026-10-31 22:00', '2026-11-01 02:00', '', '')
    require(span.ok, 'the cross-month appointment must be accepted, errors=%r' % (span.errors,))
    span_uid = span.appointment.uid

    controller.open_month(2026, 10)
    require(
        any(b.uid == span_uid for b in controller.grid.blocks_on(dt.date(2026, 10, 31))),
        'the span must be visible in the October 2026 grid',
    )
    require(
        not controller.grid.blocks_on(dt.date(2026, 11, 1)),
        'the November filler cell of the October frame must stay empty',
    )

    controller.open_month(2026, 11)
    require(
        any(b.uid == span_uid for b in controller.grid.blocks_on(dt.date(2026, 11, 1))),
        'the span must be visible in the November 2026 grid',
    )
    require(
        not controller.grid.blocks_on(dt.date(2026, 10, 31)),
        'the October filler cell of the November frame must stay empty',
    )

    half = save_new(controller, 'PROBE half open', '2026-10-29 23:00', '2026-10-31 00:00', '', '')
    require(half.ok, 'the half-open appointment must be accepted')
    controller.open_month(2026, 10)
    require(
        any(b.uid == half.appointment.uid for b in controller.grid.blocks_on(dt.date(2026, 10, 29))),
        'the first day of the span must be touched',
    )
    require(
        any(b.uid == half.appointment.uid for b in controller.grid.blocks_on(dt.date(2026, 10, 30))),
        'the second day of the span must be touched',
    )
    require(
        not any(b.uid == half.appointment.uid for b in controller.grid.blocks_on(dt.date(2026, 10, 31))),
        'the end is exclusive, so 2026-10-31 must not be touched',
    )

    first = save_new(controller, 'PROBE overlap A', '2026-10-20 10:00', '2026-10-20 11:00', '', '')
    second = save_new(controller, 'PROBE overlap B', '2026-10-20 10:30', '2026-10-20 11:30', '', '')
    require(first.ok, 'the first overlapping appointment must be accepted')
    require(
        second.ok,
        'the second overlapping appointment must not be rejected, errors=%r' % (second.errors,),
    )
    controller.open_month(2026, 10)
    blocks = controller.grid.blocks_on(dt.date(2026, 10, 20))
    uids = set(b.uid for b in blocks)
    require(
        first.appointment.uid in uids and second.appointment.uid in uids,
        'both overlapping blocks must be rendered in the same day cell',
    )
    require(len(uids) == 2, 'the day cell must hold exactly the two overlapping blocks, got %d' % len(uids))
    notes.append('half-open ends, cross-month visibility and overlap acceptance verified')
    return notes


def case_a04(ctx):
    '''A04 - edit, reschedule and delete of a probe-created appointment.'''
    notes = []
    app, controller = ctx.controller()
    controller.open_month(2026, 10)

    created = save_new(controller, 'PROBE resched', '2026-10-12 09:00', '2026-10-12 10:00', 'Room A', 'first')
    require(created.ok, 'the fixture appointment must be created')
    uid = created.appointment.uid
    require(
        any(b.uid == uid for b in controller.grid.blocks_on(dt.date(2026, 10, 12))),
        'the new block must render in its slot',
    )

    updated = save_existing(
        controller, uid, 'PROBE rescheduled', '2026-10-13 14:00', '2026-10-13 15:00', 'Room B', 'second'
    )
    require(updated.ok, 'a valid edit must be accepted, errors=%r' % (updated.errors,))
    require(updated.appointment.uid == uid, 'an edit must keep the identity of the record')
    require(
        not any(b.uid == uid for b in controller.grid.blocks_on(dt.date(2026, 10, 12))),
        'the previous slot must be empty after a reschedule',
    )
    moved = [b for b in controller.grid.blocks_on(dt.date(2026, 10, 13)) if b.uid == uid]
    require(len(moved) == 1, 'the new slot must show exactly one updated block')
    block = moved[0]
    require(block.title == 'PROBE rescheduled', 'the new slot must show the updated title')
    require(
        block.start == dt.datetime(2026, 10, 13, 14, 0, tzinfo=UTC8),
        'the new slot must show the updated start, got %r' % block.start,
    )
    require(
        block.end == dt.datetime(2026, 10, 13, 15, 0, tzinfo=UTC8),
        'the new slot must show the updated end, got %r' % block.end,
    )
    require(
        block.location == 'Room B' and block.notes == 'second',
        'the new slot must show the updated location and notes',
    )

    store_path = Path(controller.store.path)
    baseline = store_path.read_bytes()
    refused = save_existing(
        controller, uid, 'PROBE rescheduled', '2026-10-13 15:00', '2026-10-13 15:00', 'Room B', 'second'
    )
    require(not refused.ok, 'an edit whose end is not after its start must be refused')
    require(store_path.read_bytes() == baseline, 'a refused edit must not change the store file')

    disposable = save_new(controller, 'PROBE disposable', '2026-10-15 08:00', '2026-10-15 09:00', '', '')
    keeper = save_new(controller, 'PROBE keeper', '2026-10-16 08:00', '2026-10-16 09:00', '', '')
    require(disposable.ok and keeper.ok, 'the deletion fixtures must be created')
    require(
        controller.delete(disposable.appointment.uid) is True,
        'deleting an existing record must report success',
    )
    require(controller.find(disposable.appointment.uid) is None, 'a deleted record must be gone from the schedule')
    require(
        not any(b.uid == disposable.appointment.uid for b in controller.grid.blocks_on(dt.date(2026, 10, 15))),
        'a deleted record must disappear from the grid',
    )
    require(
        controller.find(keeper.appointment.uid) is not None,
        'deleting one record must leave the other records untouched',
    )
    remaining = json.loads(store_path.read_text(encoding='utf-8'))['appointments']
    remaining_uids = [r['uid'] for r in remaining]
    require(keeper.appointment.uid in remaining_uids, 'the untouched record must stay in the store')
    require(disposable.appointment.uid not in remaining_uids, 'the deleted record must be gone from the store')

    baseline = store_path.read_bytes()
    require(controller.delete('no-such-uid') is False, 'deleting an unknown id must report failure')
    require(store_path.read_bytes() == baseline, 'deleting an unknown id must not change the store file')
    notes.append('edit, reschedule and delete verified against the store and the month frame')

    tk_app = ctx.tk_app()
    if tk_app is None:
        note_not_run('Tk reschedule checks: %s' % ctx.tk_reason)
    else:
        win = tk_app.window
        win.controller.open_month(2026, 10)
        win.update_idletasks()
        dialog = win.open_editor(uid=uid)
        dialog.title_var.set('PROBE ui rescheduled')
        dialog.start_var.set('2026-10-13 16:00')
        dialog.end_var.set('2026-10-13 17:00')
        require(dialog.save() is True, 'the editor must accept a valid reschedule')
        win.update_idletasks()
        snapshot = ui_snapshot(win)
        require(
            'PROBE ui rescheduled' in snapshot.get(dt.date(2026, 10, 13), []),
            'the new slot must show the updated title in the widget tree',
        )
        require(
            'PROBE ui rescheduled' not in snapshot.get(dt.date(2026, 10, 12), []),
            'the previous slot must be empty in the widget tree',
        )
        notes.append('reschedule verified on the live widget tree')
    return notes


def case_a05(ctx):
    '''A05 - the schedule survives a restart and past months stay reachable.'''
    notes = []
    app, controller = ctx.controller()
    controller.open_month(2026, 10)
    first = save_new(controller, 'PROBE persist a', '2026-10-05 10:00', '2026-10-05 11:00', 'L1', 'N1')
    second = save_new(controller, 'PROBE persist b', '2026-10-31 22:00', '2026-11-01 02:00', '', '')
    third = save_new(controller, 'PROBE persist past', '2026-07-04 08:00', '2026-07-04 09:00', '', '')
    require(first.ok and second.ok and third.ok, 'the fixture records must be created')

    store_path = Path(controller.store.path)
    require(
        str(store_path).startswith(str(ctx.data_dir)),
        'the store must live inside the isolated probe data directory, got %s' % store_path,
    )
    baseline = store_path.read_bytes()

    restarted = ctx.new_app()
    controller2 = restarted.controller
    uids = set(record.uid for record in controller2.all_appointments())
    require(
        first.appointment.uid in uids
        and second.appointment.uid in uids
        and third.appointment.uid in uids,
        'every appointment must survive a restart',
    )
    restored = [r for r in controller2.all_appointments() if r.uid == first.appointment.uid]
    require(len(restored) == 1, 'the restored schedule must hold the record exactly once')
    record = restored[0]
    require(
        record.title == 'PROBE persist a'
        and record.location == 'L1'
        and record.notes == 'N1',
        'the restored record must keep its title, location and notes',
    )
    require(
        record.start == dt.datetime(2026, 10, 5, 10, 0, tzinfo=UTC8),
        'the restored start must keep the fixed +08:00 instant, got %r' % record.start,
    )
    require(
        record.end == dt.datetime(2026, 10, 5, 11, 0, tzinfo=UTC8),
        'the restored end must keep the fixed +08:00 instant, got %r' % record.end,
    )
    require(store_path.read_bytes() == baseline, 'restarting must not rewrite the store file')

    controller2.open_month(2026, 7)
    require(controller2.grid.header_label == 'July 2026', 'a past month must be reachable after a restart')
    require(
        any(b.uid == third.appointment.uid for b in controller2.grid.blocks_on(dt.date(2026, 7, 4))),
        'a past month must still show its appointments after a restart',
    )
    controller2.open_month(2026, 11)
    require(
        any(b.uid == second.appointment.uid for b in controller2.grid.blocks_on(dt.date(2026, 11, 1))),
        'the cross-month appointment must still be visible after a restart',
    )

    other = ctx.new_app(data_dir=ctx.tmp / 'other-data')
    require(
        other.controller.all_appointments() == [],
        'a separate data directory must start with an empty schedule',
    )
    notes.append('restart keeps every record and past-month navigation working')

    tk_app = ctx.tk_app()
    if tk_app is None:
        note_not_run('Tk restart checks: %s' % ctx.tk_reason)
    else:
        win = tk_app.window
        win.controller.open_month(2026, 10)
        win.update_idletasks()
        dialog = win.open_editor(date=dt.date(2026, 10, 21))
        dialog.title_var.set('PROBE ui persisted')
        dialog.start_var.set('2026-10-21 15:00')
        dialog.end_var.set('2026-10-21 16:00')
        require(dialog.save() is True, 'the editor must accept a valid new appointment')
        win.update_idletasks()
        snapshot = ui_snapshot(win)
        require(
            'PROBE ui persisted' in snapshot.get(dt.date(2026, 10, 21), []),
            'the new appointment must appear in the widget tree',
        )
        try:
            win.destroy()
        except Exception:
            pass
        reopened = ctx.new_app(headless=False)
        reopened.controller.open_month(2026, 10)
        reopened.window.update_idletasks()
        snapshot2 = ui_snapshot(reopened.window)
        require(
            'PROBE ui persisted' in snapshot2.get(dt.date(2026, 10, 21), []),
            'the appointment must still be in the widget tree after restarting the application',
        )
        notes.append('desktop restart verified on the live widget tree')
    return notes


CASES = [
    ('A01', 'month frame and one-month navigation', case_a01),
    ('A02', 'create, read back and refuse invalid appointments', case_a02),
    ('A03', 'half-open spans, cross-month visibility and overlaps', case_a03),
    ('A04', 'edit, reschedule and delete', case_a04),
    ('A05', 'local persistence across a restart', case_a05),
]


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Acceptance probe for the desktop month-grid calendar blueprint.'
    )
    parser.add_argument(
        '--app-path',
        default=str(Path(__file__).resolve().parent),
        help='directory that contains the calendar_app package',
    )
    parser.add_argument('--keep', action='store_true', help='keep the temporary probe data directory')
    args = parser.parse_args(argv)

    ctx = Context(Path(args.app_path))
    try:
        for cid, title, function in CASES:
            print('')
            print('=== %s %s ===' % (cid, title))
            try:
                case_notes = function(ctx) or []
            except ProbeFailure as exc:
                RESULTS.append((cid, title, 'FAIL', str(exc)))
                print('  FAIL: %s' % exc)
                continue
            except Exception as exc:
                RESULTS.append((cid, title, 'ERROR', '%s: %s' % (type(exc).__name__, exc)))
                print('  ERROR: %s: %s' % (type(exc).__name__, exc))
                traceback.print_exc()
                continue
            RESULTS.append((cid, title, 'PASS', '; '.join(case_notes)))
            print('  PASS')
            for item in case_notes:
                print('    - %s' % item)
    finally:
        ctx.cleanup(args.keep)

    print('')
    print('---- summary ----')
    for cid, title, status, detail in RESULTS:
        print('%s %-5s %s' % (cid, status, title))
        if detail:
            print('       %s' % detail)
    if NOT_RUN:
        print('')
        print('not executed (honest limits, never counted as passed):')
        for item in NOT_RUN:
            print('  - %s' % item)
    failures = [row for row in RESULTS if row[2] != 'PASS']
    print('')
    print(
        '%d/%d cases passed, %d checks not executed.'
        % (len(RESULTS) - len(failures), len(RESULTS), len(NOT_RUN))
    )
    if failures:
        print('RESULT: FAILED')
        return 1
    print('RESULT: PASSED - only the checks listed above were executed; no certification is claimed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
