"""Avoid paid re-generation when the old live validator rejects valid cumulative coverage."""

from pathlib import Path
import sys
import time

root = Path(__file__).resolve().parents[4]
pack = root / "application-atlas-production-pack"
sys.path.insert(0, str(pack))
from template_factory.store import FactoryStore  # noqa: E402

s = FactoryStore(
    pack / "atlas/template-factory/cognition-pilots/bookmark-2026-10-17", pack
)
jid = "job_4acc2b952d174c9a8fc06cfa706bf183"
while True:
    j = s.job(jid)
    if j["state"] != "running":
        print("Guard finished: job no longer running", flush=True)
        break
    if j["stage"] == "blueprint-generate-1":
        with s.connect() as c:
            token = c.execute("select token from job where id=?", (jid,)).fetchone()[0]
        if s.owned(jid, token):
            s.update(
                jid,
                token,
                j["stage"],
                "Reload corrected cumulative phase validator; keep all completed files and pinned plan",
                "failed",
                "Old live validator rejected a legitimate later regression of an earlier capability; retry with updated validator, not regenerated content",
            )
            print(
                "Stopped stale structural re-generation; all completed file checkpoints retained",
                flush=True,
            )
        break
    time.sleep(0.25)
