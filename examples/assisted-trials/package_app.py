"""Package a standalone auxiliary app without its user database or runtime state."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import zipfile


def package(app, destination):
    destination = destination.resolve()
    receipt = destination.with_name("SOURCE_MANIFEST.json")
    files = [
        p
        for p in app.rglob("*")
        if p.is_file()
        and p.resolve() not in {destination, receipt}
        and not ({"data", "__pycache__"} & set(p.relative_to(app).parts))
    ]
    rows = [
        {
            "path": str(p.relative_to(app)),
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "bytes": p.stat().st_size,
        }
        for p in sorted(files)
    ]
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as out:
        for row in rows:
            out.write(app / row["path"], app.name + "/" + row["path"])
    manifest = {
        "at": datetime.now(timezone.utc).isoformat(),
        "archive": destination.name,
        "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
        "files": rows,
        "user_database_included": False,
    }
    receipt.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    )
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()
    result = package(args.app.resolve(), args.destination.resolve())
    print(result["sha256"])
