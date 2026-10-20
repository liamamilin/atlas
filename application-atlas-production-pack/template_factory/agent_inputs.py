"""Pure construction of the model JSON and its byte-faithful leaf companion."""
from __future__ import annotations

import json


def build_agent_input(payload):
    leaf = payload.get("leaf")
    companion = None
    if isinstance(leaf, dict) and isinstance(leaf.get("content"), str):
        companion = leaf["content"].encode("utf-8")
        payload = {**payload, "leaf": {**leaf, "content_file": "leaf.md"}}
    raw = (json.dumps(payload, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    return payload, raw, companion
