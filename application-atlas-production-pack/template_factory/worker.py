"""Detached single scheduler; concurrent jobs have independent CLI workspaces."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import fcntl
import json
import os
from pathlib import Path
import signal
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


def stop_orphans(store):
    """Run only under the scheduler lock; match the unique workspace marker."""
    from template_factory.cli import CLI
    import hashlib

    for record in store.root.glob("jobs/job_*/attempt-*/*/process.json"):
        try:
            value = json.loads(record.read_text())
            pid = value.get("pid")
            if type(pid) is not int or pid <= 1:
                continue
            found = subprocess.run(
                ["ps", "-p", str(pid), "-o", "command="],
                capture_output=True,
                stdin=subprocess.DEVNULL,
                text=True,
                timeout=5,
            )
            marker = "Task workspace: " + str(record.parent.resolve()) + "."
            executable = CLI().executable or "opencode"
            if (
                found.returncode == 0
                and marker in found.stdout
                and executable in found.stdout
            ):
                os.killpg(pid, signal.SIGTERM)
        except (OSError, ValueError, subprocess.TimeoutExpired):
            continue
    docker = __import__("shutil").which("docker")
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
        worker_id = uuid.uuid4().hex
        pipeline = pipeline or Pipeline(store)
        with (
            ThreadPoolExecutor(max_workers=8) as production_pool,
            ThreadPoolExecutor(max_workers=2) as acceptance_pool,
        ):
            lanes = {
                "production": (production_pool, 8, set()),
                "verification": (acceptance_pool, 2, set()),
            }
            idle_since = time.monotonic()
            while not stop.is_set():
                store.expire_leases()
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
