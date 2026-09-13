"""Shared paths, lazy credentials and atomic local file operations."""
from contextlib import contextmanager
from pathlib import Path
import fcntl
import filecmp
import json
import os
import shutil
import tempfile

PACK = Path(os.environ.get("ATLAS_PACK", Path(__file__).resolve().parent)).resolve()


def api_key():
    key = os.environ.get("ATLAS_API_KEY")
    if key:
        return key
    with open(Path.home() / ".local/share/opencode/auth.json") as stream:
        return json.load(stream)["opencode-go"]["key"]


def atomic_write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix="." + path.name + "-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data.encode("utf-8") if isinstance(data, str) else data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def atomic_json(path, value):
    atomic_write(path, json.dumps(value, ensure_ascii=False, indent=1) + "\n")


def atomic_copy(source, target):
    target = Path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix="." + target.name + "-", dir=target.parent)
    try:
        with os.fdopen(fd, "wb") as dest, open(source, "rb") as src:
            shutil.copyfileobj(src, dest)
            dest.flush()
            os.fsync(dest.fileno())
        os.replace(tmp, target)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def recover_publication(pack=PACK):
    """Called under corpus_lock. Roll back a cutover interrupted by process exit."""
    journal_dir = Path(pack) / "atlas" / ".publish"
    journal = journal_dir / "journal.json"
    if journal.exists():
        state = json.loads(journal.read_text())
        if not state.get("committed"):
            for item in reversed(state["files"]):
                if item["backup"]:
                    atomic_copy(journal_dir / item["backup"], item["target"])
                else:
                    Path(item["target"]).unlink(missing_ok=True)
    if journal_dir.exists():
        shutil.rmtree(journal_dir)


def publish_files(mapping, pack=PACK):
    """Replace prepared files, with durable rollback records; caller holds lock.

    Each replacement is atomic. Put the database last in mapping so readers of
    the classifier switch only after all accompanying files are in place.
    """
    recover_publication(pack)
    journal_dir = Path(pack) / "atlas" / ".publish"
    journal_dir.mkdir()
    entries = []
    try:
        for source, target in mapping:
            source, target = Path(source), Path(target).resolve()
            if target.exists() and filecmp.cmp(source, target, shallow=False):
                continue
            backup = str(len(entries)) if target.exists() else None
            if backup is not None:
                shutil.copy2(target, journal_dir / backup)
            entries.append({"source": str(source), "target": str(target), "backup": backup})
        state = {"files": entries, "committed": False}
        atomic_json(journal_dir / "journal.json", state)
        for item in entries:
            atomic_copy(item["source"], item["target"])
        state["committed"] = True
        atomic_json(journal_dir / "journal.json", state)
    except BaseException:
        recover_publication(pack)
        raise
    recover_publication(pack)


@contextmanager
def corpus_lock(pack=PACK):
    path = Path(pack) / "atlas" / "corpus.lock"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError("已有语料更新正在运行，请等待完成") from None
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)
