"""File identity evidence used to refuse stale plans and changed data.

Default evidence is the cheap metadata tuple dev+ino+size+mtime_ns (falling
back to seconds when the platform lacks st_mtime_ns). A content sha256 is only
recorded when the caller explicitly asks for it, because hashing large batches
or large files has a real cost (see DECISIONS.md, D01).
"""

import hashlib
import os


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def capture_identity(path, hash_contents=False):
    """Return the identity evidence block recorded in a plan/receipt."""
    st = os.lstat(path)
    ident = {
        "dev": int(st.st_dev),
        "ino": int(st.st_ino),
        "size": int(st.st_size),
    }
    mtime_ns = getattr(st, "st_mtime_ns", None)
    if mtime_ns is not None:
        ident["mtime_ns"] = int(mtime_ns)
    else:
        ident["mtime"] = float(st.st_mtime)
    if hash_contents:
        ident["sha256"] = sha256_of(path)
    return ident


def identity_matches(path, ident):
    """True when the live file still matches every recorded evidence field."""
    st = os.lstat(path)
    if "dev" in ident and int(ident["dev"]) != int(st.st_dev):
        return False
    if "ino" in ident and int(ident["ino"]) != int(st.st_ino):
        return False
    if "size" in ident and int(ident["size"]) != int(st.st_size):
        return False
    if "mtime_ns" in ident:
        current = getattr(st, "st_mtime_ns", None)
        if current is None or int(ident["mtime_ns"]) != int(current):
            return False
    if "mtime" in ident:
        if abs(float(ident["mtime"]) - st.st_mtime) > 1e-9:
            return False
    if "sha256" in ident:
        if sha256_of(path) != str(ident["sha256"]):
            return False
    return True
