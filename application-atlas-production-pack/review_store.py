"""Atomic review updates and freshness checks for promotion decisions."""
from pathlib import Path
from contextlib import contextmanager
import fcntl
import hashlib
import json
import re
from atlas_runtime import PACK, atomic_json
from leaf_lint import parse_front


def valid_slug(slug):
    if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError("无效的类型 ID")
    return slug


def load_review(pack=PACK):
    path = Path(pack) / "drafts/review.json"
    return json.loads(path.read_text()) if path.exists() else {}


@contextmanager
def review_lock(pack=PACK):
    path = Path(pack) / "drafts/review.lock"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        yield


def update_review(slug, changes, pack=PACK):
    with review_lock(pack):
        state = load_review(pack)
        state[slug] = {**state.get(slug, {}), **changes}
        atomic_json(Path(pack) / "drafts/review.json", state)
        return state[slug]


def fingerprint(slug, pack=PACK):
    path = Path(pack) / "drafts" / (valid_slug(slug) + ".md")
    front, body = parse_front(path.read_text())
    research = path.with_suffix(".research.md")
    payload = {"name": front.get("name"), "name_zh": front.get("name_zh"),
               "desc": front.get("desc"), "link": front.get("link"), "body": body,
               "research": research.read_text() if research.exists() else ""}
    return hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def corpus_revision(pack=PACK):
    stat = (Path(pack) / "atlas/atlas.sqlite").stat()
    return f"{stat.st_ino}:{stat.st_size}:{stat.st_mtime_ns}"


def review_current(slug, record, pack=PACK):
    return (record.get("draft_fingerprint") == fingerprint(slug, pack)
            and record.get("corpus_revision") == corpus_revision(pack))
