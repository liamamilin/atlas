"""Deterministic first-round priority, with scenario diversity and no star cutoff."""
from datetime import datetime, timezone
import math
import re

VERSION = "scenario-balanced-v1"
STOP = {"a", "an", "and", "the", "for", "to", "of", "in", "with", "application", "platform", "software", "system"}


def terms(value):
    return set(re.findall(r"[a-z0-9][a-z0-9+#.-]*|[\u3400-\u9fff]{2,}", value.casefold())) - STOP


def priority(candidate, scenarios, category, at=None):
    meta = candidate["data"]["meta"]
    hits = candidate["data"].get("search_hits", [])
    text = " ".join([meta.get("name") or "", meta.get("full_name") or "", meta.get("description") or "",
                     " ".join(meta.get("topics") or [])]).casefold()
    query_terms = {s["id"]: terms(" ".join(s.get("search_queries", []))) for s in scenarios}
    query_terms[""] = terms(category)
    matches = {key: sum(t in text for t in words) / max(1, len(words)) for key, words in query_terms.items()}
    ranks = {}
    for hit in hits:
        key = hit.get("scenario_id") or ""
        position = max(1, int(hit.get("position", 100)))
        ranks[key] = max(ranks.get(key, 0), 5 / (4 + position))
    relevance = max((0.65 * matches.get(key, 0) + 0.35 * ranks.get(key, 0)
                     for key in set(matches) | set(ranks)), default=0)
    at = at or datetime.now(timezone.utc)
    try:
        pushed_at = meta.get("pushed_at")
        if not isinstance(pushed_at, str):
            raise ValueError("Unknown repository push time")
        age = max(0, (at - datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))).days)
        activity = 1 / (1 + age / 365)
    except (ValueError, KeyError, TypeError):
        activity = 0
    stars = max(0, int(meta.get("stargazers_count") or 0))
    maturity = min(1, math.log1p(stars) / math.log1p(100000))
    description = bool(meta.get("description"))
    metadata = (description + bool(meta.get("topics")) + bool(meta.get("language"))) / 3
    score = round(60 * relevance + 20 * activity + 15 * maturity + 5 * metadata, 4)
    scenario_scores = {s["id"]: 0.65 * matches.get(s["id"], 0) + 0.35 * ranks.get(s["id"], 0) for s in scenarios}
    reasons = []
    if any(hit.get("scenario_id") for hit in hits):
        reasons.append("命中场景任务检索")
    if max(matches.values(), default=0):
        reasons.append("名称、简介或主题包含任务相关词")
    if activity >= 0.5:
        reasons.append("最近一年有仓库推送")
    if stars:
        reasons.append("Stars作为成熟度的小权重参考，无最低门槛")
    return {"version": VERSION, "score": score, "scenario_scores": scenario_scores,
            "signals": {"relevance": round(relevance, 4), "activity": round(activity, 4),
                        "maturity": round(maturity, 4), "metadata": round(metadata, 4)}, "reasons": reasons}


def select_first_round(candidates, scenarios, category, limit=60, at=None):
    ranked = [{**c, "priority": priority(c, scenarios, category, at)} for c in candidates]
    def key(candidate):
        return (-candidate["priority"]["score"], candidate["repository_id"])
    ranked.sort(key=key)
    queues = []
    for scenario in scenarios:
        sid = scenario["id"]
        group = [c for c in ranked if c["priority"]["scenario_scores"].get(sid, 0) > 0]
        group.sort(key=lambda c: (-c["priority"]["scenario_scores"].get(sid, 0), *key(c)))
        queues.append((sid, iter(group)))
    selected, seen = [], set()
    while len(selected) < min(limit, len(ranked)) and queues:
        remaining = []
        for sid, queue in queues:
            item = next((c for c in queue if c["repository_id"] not in seen), None)
            if item is not None:
                if len(selected) < limit:
                    selected.append({**item, "priority": {**item["priority"], "allocated_scenario": sid}})
                    seen.add(item["repository_id"])
                remaining.append((sid, queue))
        queues = remaining
    for item in ranked:
        if len(selected) >= limit:
            break
        if item["repository_id"] not in seen:
            selected.append({**item, "priority": {**item["priority"], "allocated_scenario": None}})
            seen.add(item["repository_id"])
    return selected
