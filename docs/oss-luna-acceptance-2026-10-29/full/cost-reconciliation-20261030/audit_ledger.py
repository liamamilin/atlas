"""Atomic request reservations; integer micro-USD, including uncertain charges."""
from contextlib import contextmanager
from decimal import Decimal, ROUND_CEILING
from pathlib import Path
import json
import math
import sqlite3
import uuid

MICRO = 1000000
CAP = 50 * MICRO


def micro(value):
    return int((Decimal(str(value)) * MICRO).to_integral_value(rounding=ROUND_CEILING))


def reservation(body, provider):
    # UTF-8 byte count bounds byte-level text tokens; generously include framing.
    # Models are forced to non-thinking with a bounded output and explicit tier.
    size = len(json.dumps(body, ensure_ascii=False).encode()) + 8192
    if provider == "openai":
        long = size > 272000
        # Reserve the larger cache-write rate for ALL input; do not bank on cache.
        return micro(Decimal(size) * Decimal("0.000000125") * (2 if long else 1)
                     + Decimal(2400) * Decimal("0.0000005") * (Decimal("1.5") if long else 1))
    # Highest published DeepSeek peak rates, even when called off-peak.
    return micro(Decimal(size) * Decimal("0.0000003") + Decimal(2400) * Decimal("0.0000012"))


def charges(usage, provider, peak=False):
    if not isinstance(usage, dict):
        return None
    if not isinstance(usage.get("prompt_tokens"), int) or not isinstance(usage.get("completion_tokens"), int):
        return None
    p, o = usage["prompt_tokens"], usage["completion_tokens"]
    if p < 0 or o < 0:
        return None
    cached = usage.get("prompt_cache_hit_tokens") or (usage.get("prompt_tokens_details") or {}).get("cached_tokens") or 0
    cached = min(max(int(cached), 0), p)
    if provider == "openai":
        long = p > 272000
        estimated = (Decimal(p-cached) * Decimal("0.1") + Decimal(cached) * Decimal("0.01")) * (2 if long else 1)
        estimated += Decimal(o) * Decimal("0.5") * (Decimal("1.5") if long else 1)
        # Higher uncached/cache-write bound for budget enforcement, not the bill.
        upper = Decimal(p) * Decimal("0.125") * (2 if long else 1) + Decimal(o) * Decimal("0.5") * (Decimal("1.5") if long else 1)
    else:
        factor = 2 if peak else 1
        estimated = (Decimal(p-cached) * Decimal("0.15") + Decimal(cached) * Decimal("0.003") + Decimal(o) * Decimal("0.6")) * factor
        # Enforce the published peak ceiling even when the estimate is off-peak.
        upper = Decimal(p) * Decimal("0.30") + Decimal(o) * Decimal("1.20")
    estimated, upper = estimated / MICRO, upper / MICRO
    reported = usage.get("cost")
    if isinstance(reported, (float, int)) and math.isfinite(reported) and 0 <= reported < 100:
        estimated = max(estimated, Decimal(str(reported)))
        upper = max(upper, Decimal(str(reported)))
    return micro(estimated), micro(upper)


class Ledger:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as con:
            con.execute("PRAGMA journal_mode=WAL")
            con.executescript("""
              CREATE TABLE IF NOT EXISTS meta(key TEXT PRIMARY KEY,value TEXT NOT NULL);
              CREATE TABLE IF NOT EXISTS projects(
                rid INTEGER PRIMARY KEY, full_name TEXT NOT NULL, data_sha TEXT NOT NULL,
                domain TEXT NOT NULL, primary_status TEXT NOT NULL DEFAULT 'pending',
                secondary_status TEXT NOT NULL DEFAULT 'none', outcome TEXT NOT NULL DEFAULT 'pending',
                payload_sha TEXT, coverage TEXT, primary_review TEXT, secondary_review TEXT,
                primary_version TEXT, secondary_version TEXT, error_code TEXT);
              CREATE INDEX IF NOT EXISTS primary_queue ON projects(primary_status,rid);
              CREATE INDEX IF NOT EXISTS secondary_queue ON projects(secondary_status,rid);
              CREATE TABLE IF NOT EXISTS requests(
                id TEXT PRIMARY KEY, rid INTEGER, stage TEXT NOT NULL, provider TEXT NOT NULL,
                model TEXT NOT NULL, state TEXT NOT NULL, reserved INTEGER NOT NULL,
                charged INTEGER NOT NULL DEFAULT 0, estimated INTEGER NOT NULL DEFAULT 0,
                created TEXT NOT NULL, finished TEXT, payload_sha TEXT, prompt_sha TEXT,
                receipt TEXT, error_code TEXT, legacy_path TEXT UNIQUE);
            """)

    @contextmanager
    def connect(self):
        con = sqlite3.connect(self.path, timeout=30)
        con.row_factory = sqlite3.Row
        try:
            yield con
            con.commit()
        except BaseException:
            con.rollback()
            raise
        finally:
            con.close()

    @staticmethod
    def balance(con):
        row = con.execute("SELECT COALESCE(SUM(charged),0),COALESCE(SUM(estimated),0),COALESCE(SUM(CASE WHEN state IN ('reserved','uncertain') THEN reserved ELSE 0 END),0) FROM requests").fetchone()
        return {"charged_upper_micro": row[0], "estimated_micro": row[1], "reserved_micro": row[2], "available_micro": CAP-row[0]-row[2], "cap_micro": CAP}

    def reserve(self, rid, stage, provider, model, amount, created, payload_sha, prompt_sha):
        assert amount > 0 and stage in {"primary", "secondary"}
        with self.connect() as con:
            con.execute("BEGIN IMMEDIATE")
            project = con.execute("SELECT " + stage + "_status FROM projects WHERE rid=?", (rid,)).fetchone()
            if not project or project[0] != "pending":
                return None
            if self.balance(con)["available_micro"] < amount:
                return None
            key = uuid.uuid4().hex
            con.execute("INSERT INTO requests(id,rid,stage,provider,model,state,reserved,created,payload_sha,prompt_sha) VALUES(?,?,?,?,?,'reserved',?,?,?,?)", (key,rid,stage,provider,model,amount,created,payload_sha,prompt_sha))
            con.execute("UPDATE projects SET " + stage + "_status='inflight' WHERE rid=?", (rid,))
            return key

    def settle(self, key, receipt, charge, finished, error_code=None, certain_no_charge=False):
        with self.connect() as con:
            con.execute("BEGIN IMMEDIATE")
            row = con.execute("SELECT * FROM requests WHERE id=?", (key,)).fetchone()
            assert row and row["state"] == "reserved"
            if charge is None and not certain_no_charge:
                # Keep the full reservation against the cap on unknown billing.
                con.execute("UPDATE requests SET state='uncertain',receipt=?,finished=?,error_code=? WHERE id=?", (json.dumps(receipt,ensure_ascii=False),finished,error_code,key))
            else:
                estimated, upper = charge or (0,0)
                # Stop future work if a provider violates the published bound.
                if upper > row["reserved"]:
                    con.execute("INSERT OR REPLACE INTO meta VALUES('fatal',?)", (json.dumps("provider_cost_exceeded_reservation"),))
                con.execute("UPDATE requests SET state='settled',charged=?,estimated=?,reserved=0,receipt=?,finished=?,error_code=? WHERE id=?", (upper,estimated,json.dumps(receipt,ensure_ascii=False),finished,error_code,key))

    def import_receipt(self, rid, stage, provider, model, path, receipt, created):
        cost = charges(receipt.get("usage",{}), provider)
        if cost is None:
            raise ValueError("historical receipt has no measured usage")
        with self.connect() as con:
            con.execute("INSERT OR IGNORE INTO requests(id,rid,stage,provider,model,state,reserved,charged,estimated,created,finished,receipt,legacy_path) VALUES(?,?,?,?,?,'settled',0,?,?,?,?,?,?)", (uuid.uuid4().hex,rid,stage,provider,model,cost[1],cost[0],created,created,json.dumps(receipt,ensure_ascii=False),str(path)))

    def recover_inflight(self):
        with self.connect() as con:
            # A crashed HTTP call could be billed. Its reservation is never lost.
            con.execute("UPDATE requests SET state='uncertain',error_code='process_interrupted_unknown_billing' WHERE state='reserved'")
            con.execute("UPDATE projects SET primary_status='pending' WHERE primary_status='inflight'")
            con.execute("UPDATE projects SET secondary_status='pending' WHERE secondary_status='inflight'")
