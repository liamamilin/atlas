"""Detached single scheduler; concurrent jobs have independent CLI workspaces."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import fcntl
import json
import os
from pathlib import Path
import signal
import shutil
import sqlite3
import subprocess
import sys
import threading
import time
import uuid

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.pipeline import Pipeline
from template_factory.store import FactoryStore


def ensure_worker(store):
    if os.environ.get("ATLAS_FACTORY_DISABLE_WORKER") == "1":
        return
    lock = (store.root / "worker.lock").open("a+")
    try:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return
    finally:
        lock.close()
    with (store.root / "worker.log").open("ab") as log:
        subprocess.Popen(
            [
                sys.executable,
                str(Path(__file__).resolve()),
                "--root",
                str(store.root),
                "--pack",
                str(store.pack),
            ],
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=log,
            start_new_session=True,
        )


def execute(store, job, pipeline):
    done = threading.Event()

    def heartbeat():
        while not done.wait(10):
            if not store.heartbeat(job["id"], job["token"]):
                return

    pulse = threading.Thread(target=heartbeat, daemon=True)
    pulse.start()
    try:
        pipeline.run(job)
    except Exception:
        # Pipeline persists safe error details and keeps the old attempt.
        pass
    finally:
        done.set()
        pulse.join(timeout=2)


def _process_table():
    found = subprocess.run(
        ["ps", "-axo", "pgid=,pid=,stat=,command="],
        capture_output=True,
        stdin=subprocess.DEVNULL,
        text=True,
        timeout=5,
    )
    if found.returncode != 0:
        raise OSError("unable to inspect process table")
    rows = []
    for line in found.stdout.splitlines():
        fields = line.strip().split(None, 3)
        if len(fields) != 4:
            continue
        try:
            rows.append({
                "pgid": int(fields[0]), "pid": int(fields[1]),
                "state": fields[2], "command": fields[3],
            })
        except ValueError:
            continue
    return rows


def _group_members(pid, process_table=None):
    rows = (process_table or _process_table)()
    return [row for row in rows if row["pgid"] == pid]


def _live_group_members(pid, process_table=None):
    # Zombie processes no longer execute. The OS may retain them briefly while
    # reparenting/reaping, so they are not evidence that work is still running.
    return [row for row in _group_members(pid, process_table) if not row["state"].startswith("Z")]


def _owns_process_group(pid, directory, executable, process_table=None):
    try:
        rows = (process_table or _process_table)()
    except (OSError, subprocess.TimeoutExpired):
        return False
    marker = "Task workspace: " + str(directory.resolve()) + "."
    executable_name = Path(executable).name
    for row in rows:
        if row["pid"] == pid and row["pgid"] == pid:
            command_parts = row["command"].split()
            return marker in row["command"] and any(
                Path(part.strip("\"'",)).name == executable_name
                for part in command_parts
            )
    return False


def _stop_owned_process_group(
    pid, directory, executable, *, process_table=None, killpg=None,
    sleep=time.sleep, monotonic=time.monotonic,
):
    """Stop one verified CLI process group and return proof that it exited."""
    process_table = process_table or _process_table
    killpg = killpg or os.killpg
    if not _owns_process_group(pid, directory, executable, process_table):
        return False
    try:
        killpg(pid, signal.SIGTERM)
    except ProcessLookupError:
        try:
            return not _live_group_members(pid, process_table)
        except (OSError, subprocess.TimeoutExpired):
            return False
    except OSError:
        return False

    deadline = monotonic() + 2.0
    while monotonic() < deadline:
        try:
            if not _live_group_members(pid, process_table):
                return True
        except (OSError, subprocess.TimeoutExpired):
            return False
        sleep(0.05)

    # Only escalate while the original marked leader still anchors this group.
    # If it vanished while an unmarked child remains, ownership is ambiguous;
    # leave the budget reservation active instead of risking another process.
    if not _owns_process_group(pid, directory, executable, process_table):
        return False
    try:
        killpg(pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    except OSError:
        return False

    deadline = monotonic() + 2.0
    while monotonic() < deadline:
        try:
            if not _live_group_members(pid, process_table):
                return True
        except (OSError, subprocess.TimeoutExpired):
            return False
        sleep(0.05)
    return False


def _running_job_processes(store):
    with store.connect() as con:
        jobs = con.execute(
            "SELECT id,attempt,stage FROM job WHERE state='running'"
        ).fetchall()
    for job in jobs:
        stage = job["stage"]
        job_id = job["id"]
        if (
            not isinstance(job_id, str)
            or not job_id
            or Path(job_id).name != job_id
            or not isinstance(stage, str)
            or not stage
            or Path(stage).name != stage
            or stage in {".", ".."}
        ):
            continue
        job_root = store.root / "jobs" / job_id
        attempt = job_root / f"attempt-{job['attempt']}"
        record = attempt / stage / "process.json"
        try:
            if (
                job_root.is_symlink()
                or attempt.is_symlink()
                or record.parent.is_symlink()
                or record.is_symlink()
                or not record.resolve().is_relative_to(attempt.resolve())
            ):
                continue
            value = json.loads(record.read_text())
        except (OSError, ValueError):
            continue
        pid = value.get("pid") if isinstance(value, dict) else None
        if type(pid) is int and pid > 1:
            yield job_id, record.parent, pid


def _recover_orphan_budgets(store, job_ids):
    ids = sorted(set(job_ids))
    if not ids:
        return 0
    placeholders = ",".join("?" for _ in ids)
    try:
        with store.connect() as con:
            campaigns = [
                row[0] for row in con.execute(
                    f"SELECT DISTINCT campaign_id FROM tf_budget_reservation WHERE job_id IN ({placeholders}) AND status IN ('reserved','started','uncertain')",
                    ids,
                )
            ]
    except sqlite3.OperationalError:
        return 0
    from template_factory.budget import BudgetLedger

    recovered = 0
    for campaign_id in campaigns:
        try:
            recovered += BudgetLedger(store, campaign_id=campaign_id).mark_recovered_unknowns(
                ids, proof_owned_processes_stopped=True
            )
        except (OSError, sqlite3.Error, ValueError):
            continue
    return recovered


def stop_orphans(store):
    """Recover CLI calls only after proving each owned group stopped.

    This function is called only by the scheduler while holding worker.lock.
    A reservation stays active if its job has no current-stage process marker,
    its PID/PGID/command does not match, process inspection fails, or cleanup
    cannot prove the group is gone.
    """
    from template_factory.cli import CLI
    import hashlib

    executable = CLI().executable
    proven_job_ids = set()
    if executable:
        for job_id, directory, pid in _running_job_processes(store):
            if _stop_owned_process_group(pid, directory, executable):
                proven_job_ids.add(job_id)
    _recover_orphan_budgets(store, proven_job_ids)

    docker = shutil.which("docker")
    if docker:
        owner = hashlib.sha256(str(store.root).encode()).hexdigest()[:16]
        try:
            result = subprocess.run(
                [docker, "ps", "-aq", "--filter", "label=atlas.factory=" + owner],
                capture_output=True,
                stdin=subprocess.DEVNULL,
                text=True,
                timeout=10,
            )
            for container in result.stdout.splitlines():
                if __import__("re").fullmatch(r"[0-9a-f]{12,64}", container):
                    subprocess.run(
                        [docker, "rm", "-f", container], stdin=subprocess.DEVNULL, capture_output=True, timeout=20
                    )
        except (OSError, subprocess.TimeoutExpired):
            pass


def run(store, stop=None, pipeline=None):
    stop = stop or threading.Event()
    lock = (store.root / "worker.lock").open("a+")
    try:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return
        lock.seek(0)
        lock.truncate()
        lock.write(str(os.getpid()))
        lock.flush()
        stop_orphans(store)
        store.recover()
        store.reconcile_outbox()
        worker_id = uuid.uuid4().hex
        pipeline = pipeline or Pipeline(store)
        with (
            ThreadPoolExecutor(max_workers=2) as production_pool,
            ThreadPoolExecutor(max_workers=2) as acceptance_pool,
        ):
            lanes = {
                "production": (production_pool, 2, set()),
                "verification": (acceptance_pool, 2, set()),
            }
            idle_since = time.monotonic()
            while not stop.is_set():
                store.expire_leases()
                store.reconcile_outbox()
                active = False
                claimed = False
                for lane, (pool, capacity, pending) in list(lanes.items()):
                    futures = {f for f in pending if not f.done()}
                    if len(futures) < capacity:
                        job = store.claim(worker_id, lane)
                        if job:
                            futures.add(pool.submit(execute, store, job, pipeline))
                            idle_since = time.monotonic()
                            claimed = True
                    active = active or bool(futures)
                    lanes[lane] = (pool, capacity, futures)
                if claimed:
                    continue
                if not active and time.monotonic() - idle_since > 120:
                    break
                stop.wait(0.5)
    finally:
        lock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--pack", required=True)
    args = parser.parse_args()
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))
    run(FactoryStore(args.root, args.pack))
