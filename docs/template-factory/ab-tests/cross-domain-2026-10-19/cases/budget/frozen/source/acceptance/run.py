#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""acceptance/run.py — 个人月度预算与消费前剩余额度：独立可运行的真实目标验收检查器。

仅使用 Python 3 标准库。它不是下游应用，不安装依赖、不执行任意用户命令、不使用 mock 目标响应。

目标由操作员显式提供（二选一）：
  Web 模式：--target-url http://127.0.0.1:PORT
      仅允许给定的精确 loopback origin/port；在传输层拒绝跨源重定向。
  CLI 模式：--app-path /path/to/app.py --data-root /path/to/owned-root
      以 shell=False 启动被检应用（python3 app.py --port PORT --data-dir DIR），
      只使用受控临时根目录；A10 会在同一 data-dir 上重启以验证持久化。

--month 可选，默认当月（YYYY-MM）。覆盖 A01–A14；任一行断言失败即以非零退出码结束。

生成阶段未运行任何程序；所有用例状态为 not_run，由独立操作员在隔离的真实目标上执行。
"""

import argparse
import csv
import io
import json
import os
import re
import socket
import subprocess
import sys
import time
import uuid
from datetime import date
from decimal import Decimal
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

RUN_TOKEN = uuid.uuid4().hex[:6]
TWO_PLACES = Decimal("0.01")
LOOPBACK_HOSTS = frozenset({"127.0.0.1", "localhost", "::1"})
REQUIRED_TESTIDS = [
    "month",
    "category-name",
    "category-budget",
    "category-save",
    "expense-date",
    "expense-category",
    "expense-amount",
    "expense-note",
    "expense-save",
]

CASES = {
    "A01": "启动：GET / 返回中文 UI 且含全部 data-testid 控件；GET /api/state?month 返回该月实时状态。",
    "A02": '通过 UI 控件与 POST /api/categories 建立分类与月预算；state 中该分类 spent 为 "0.00"。',
    "A03": "同一月份重复名称创建分类返回非 2xx JSON 错误，且不产生隐藏的第二条分类。",
    "A04": "记录含日期/分类/金额/备注的支出后，state 列表包含该笔且汇总与之一致。",
    "A05": "非正数或超过两位小数的金额被拒绝（非 2xx JSON），既有数据与汇总保持原样。",
    "A06": "交易日期与分类所属月份不一致时被拒绝，且既有数据不变。",
    "A07": "分类与整月 budget/spent/remaining/totals 正确；未使用分类可见；超支显示负 remaining 且不阻止继续记账。",
    "A08": "修改或删除支出后，交易列表与汇总即时一致地重算。",
    "A09": "不存在或非法 id 的 PUT/DELETE 返回非 2xx，原记录保持不变。",
    "A10": "月份数据互相隔离；同一 data-dir 重启后数据保留，且数据仅写入指定目录。",
    "A11": "GET /api/export?month 返回 UTF-8 CSV，含表头与当月行；中文、引号、换行按 RFC 4180 往返可解析。",
    "A12": "PUT /api/categories/{id} 更新目标月预算，且不误改其他月份的同名分类。",
    "A13": "UI 控件反映与 JSON API 相同的真实状态（共用 /api/state 状态源）。",
    "A14": "API 校验失败返回非 2xx JSON 错误说明；UI 对失败给出可理解反馈。",
}
CASE_ORDER = [f"A{i:02d}" for i in range(1, 15)]


class CheckFailure(Exception):
    """任一行断言失败。"""


class SkipCase(Exception):
    """当前模式无法完整验证该用例（不计为通过）。"""


class ConfigError(Exception):
    """CLI/目标配置错误，在发起请求前退出。"""


class CrossOriginRedirect(CheckFailure):
    """在传输层拒绝跨源重定向。"""


# --------------------------------------------------------------------------
# 断言辅助
# --------------------------------------------------------------------------
def expect_true(cond, label):
    if not cond:
        raise CheckFailure(label)


def expect_eq(actual, expected, label):
    if actual != expected:
        raise CheckFailure(f"{label}：期望 {expected!r}，实际 {actual!r}")


def expect_money(value, label):
    if not isinstance(value, str) or not re.match(r"^-?\d+\.\d{2}$", value):
        raise CheckFailure(f"{label} 必须是两位小数字符串，实际 {value!r}")


def expect_error(resp, label):
    if 200 <= resp.status < 300:
        raise CheckFailure(f"{label}：期望非 2xx 错误，实际 HTTP {resp.status}")
    data = resp.json_or_none()
    if not isinstance(data, dict) or not isinstance(data.get("error"), str) or not data["error"].strip():
        raise CheckFailure(
            f"{label}：期望非 2xx 且 JSON 含非空 error 说明，实际 HTTP {resp.status} body={_short(resp.body)}"
        )


def _short(body, limit=200):
    if isinstance(body, (bytes, bytearray)):
        text = bytes(body).decode("utf-8", "replace")
    else:
        text = str(body)
    text = re.sub(r"//[^/\s@]+@", "//***@", text)
    text = text.replace("\r", " ").replace("\n", " ").strip()
    return text[:limit] + ("…" if len(text) > limit else "")


# --------------------------------------------------------------------------
# 金额辅助（整数分/Decimal，避免二进制浮点误差）
# --------------------------------------------------------------------------
def _q(value):
    return format(Decimal(str(value)).quantize(TWO_PLACES), "f")


def _sum_money(values):
    total = Decimal("0")
    for value in values:
        total += Decimal(str(value))
    return _q(total)


def _assert_totals_consistent(state):
    cats = state.get("categories", [])
    totals = state.get("totals", {})
    expect_eq(totals.get("budget"), _sum_money(c.get("budget") for c in cats),
              "totals.budget 应等于分类预算之和")
    expect_eq(totals.get("spent"), _sum_money(c.get("spent") for c in cats),
              "totals.spent 应等于分类支出之和")
    expect_eq(totals.get("remaining"), _sum_money(c.get("remaining") for c in cats),
              "totals.remaining 应等于分类剩余之和")
    expect_money(totals.get("budget"), "totals.budget")
    expect_money(totals.get("spent"), "totals.spent")
    expect_money(totals.get("remaining"), "totals.remaining")


# --------------------------------------------------------------------------
# 月份与唯一名称辅助
# --------------------------------------------------------------------------
def default_month():
    return date.today().strftime("%Y-%m")


def shift_month(month, delta):
    year, mon = int(month[:4]), int(month[5:7])
    total = year * 12 + (mon - 1) + delta
    return f"{total // 12:04d}-{total % 12 + 1:02d}"


def day_in(month, day):
    return f"{month}-{day:02d}"


_UNIQ = {"n": 0}


def uniq(prefix):
    _UNIQ["n"] += 1
    return f"{prefix}-{RUN_TOKEN}-{_UNIQ['n']}"


# --------------------------------------------------------------------------
# HTTP 适配层：仅发往给定 origin，禁用跨源重定向，不回显凭据
# --------------------------------------------------------------------------
_TARGET = None
_OPENER = None


class Resp:
    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body

    def text(self):
        try:
            return bytes(self.body).decode("utf-8")
        except UnicodeDecodeError:
            raise CheckFailure("响应不是合法 UTF-8 文本")

    def json(self):
        try:
            return json.loads(bytes(self.body).decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            raise CheckFailure(f"响应不是合法 JSON（HTTP {self.status}）")

    def json_or_none(self):
        try:
            return json.loads(bytes(self.body).decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            return None


def _build_opener(pin):
    class _PinnedRedirect(HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            target = urlsplit(newurl)
            host = (target.hostname or "").lower()
            try:
                port = target.port
            except ValueError:
                port = None
            if port is None:
                port = 80 if target.scheme == "http" else 443
            if (target.scheme, host, port) != pin:
                raise CrossOriginRedirect(f"拒绝重定向到非目标源（HTTP {code}）")
            return super().redirect_request(req, fp, code, msg, headers, newurl)

    # 显式禁用环境代理，杜绝被路由到目标 origin 之外。
    return build_opener(ProxyHandler({}), _PinnedRedirect)


def configure_http(raw_url):
    global _TARGET, _OPENER
    parts = urlsplit(raw_url)
    if parts.scheme != "http":
        raise ConfigError("--target-url 仅支持 http 的本地实例。")
    host = (parts.hostname or "").lower()
    if host not in LOOPBACK_HOSTS:
        raise ConfigError("--target-url 主机必须是 loopback（127.0.0.1/localhost/::1）。")
    if parts.username or parts.password:
        raise ConfigError("--target-url 含内嵌凭据；该目标不需要认证，已在发起任何请求前退出。")
    if parts.path not in ("", "/") or parts.query or parts.fragment:
        raise ConfigError("--target-url 必须是精确 origin（不含 path/query/fragment）。")
    try:
        port = parts.port
    except ValueError:
        raise ConfigError("--target-url 端口非法。")
    if port is None:
        port = 80
    netloc = f"[{host}]:{port}" if ":" in host else f"{host}:{port}"
    pin = ("http", host, port)
    _TARGET = {"base": f"http://{netloc}", "pin": pin}
    _OPENER = _build_opener(pin)


def _request(method, path, json_payload=None, timeout=20):
    if _TARGET is None or _OPENER is None:
        raise ConfigError("尚未配置目标。")
    data = None
    headers = {"Accept": "application/json, text/csv, text/html;q=0.9, */*;q=0.5"}
    if json_payload is not None:
        data = json.dumps(json_payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json; charset=utf-8"
    req = Request(_TARGET["base"] + path, data=data, headers=headers, method=method)
    try:
        with _OPENER.open(req, timeout=timeout) as resp:
            return Resp(resp.status, dict(resp.headers), resp.read())
    except HTTPError as exc:
        return Resp(exc.code, dict(exc.headers), exc.read())
    except CrossOriginRedirect as exc:
        raise CheckFailure(str(exc))
    except URLError as exc:
        raise CheckFailure(f"无法连接目标 {method} {path}：{exc.reason}")
    except OSError as exc:
        raise CheckFailure(f"目标请求失败 {method} {path}：{exc}")


def http_get(path):
    return _request("GET", path)


def http_post(path, json_payload=None):
    return _request("POST", path, json_payload)


def http_put(path, json_payload=None):
    return _request("PUT", path, json_payload)


def http_delete(path):
    return _request("DELETE", path)


def json_body(resp):
    return resp.json()


def _state_path(month):
    return "/api/state?" + urlencode({"month": month})


def get_state(month):
    resp = http_get(_state_path(month))
    expect_eq(resp.status, 200, f"GET /api/state?month={month}")
    data = resp.json()
    expect_true(isinstance(data, dict), "state 应为 JSON 对象")
    expect_eq(data.get("month"), month, "state.month 必须回显请求月份")
    expect_true(isinstance(data.get("categories"), list), "state.categories 应为数组")
    expect_true(isinstance(data.get("transactions"), list), "state.transactions 应为数组")
    expect_true(isinstance(data.get("totals"), dict), "state.totals 应为对象")
    return data


def find_category(state, name):
    for cat in state.get("categories", []):
        if cat.get("name") == name:
            return cat
    return None


def categories_named(state, name):
    return [c for c in state.get("categories", []) if c.get("name") == name]


def find_txn(state, tid):
    for txn in state.get("transactions", []):
        if txn.get("id") == tid:
            return txn
    return None


def require_category(state, name):
    cat = find_category(state, name)
    expect_true(cat is not None, f"state 应包含分类 {name!r}")
    return cat


def require_txn(state, tid):
    txn = find_txn(state, tid)
    expect_true(txn is not None, f"state 应包含支出 id={tid!r}")
    return txn


def create_category(month, name, budget):
    resp = http_post("/api/categories", {"month": month, "name": name, "budget": budget})
    expect_true(200 <= resp.status < 300,
                f"创建分类 {name!r} 应成功，实际 HTTP {resp.status} body={_short(resp.body)}")
    data = resp.json()
    expect_true(isinstance(data, dict) and "id" in data, "创建分类应返回 {id}")
    return data["id"]


def create_txn(date_str, category_id, amount, note):
    payload = {"date": date_str, "category_id": category_id, "amount": amount, "note": note}
    resp = http_post("/api/transactions", payload)
    expect_true(200 <= resp.status < 300,
                f"记录支出应成功，实际 HTTP {resp.status} body={_short(resp.body)}")
    data = resp.json()
    expect_true(isinstance(data, dict) and "id" in data, "记录支出应返回 {id}")
    return data["id"]


# --------------------------------------------------------------------------
# CSV 辅助（RFC 4180 往返）
# --------------------------------------------------------------------------
def parse_csv_text(text):
    return list(csv.reader(io.StringIO(text, newline="")))


def serialize_csv(rows):
    buf = io.StringIO(newline="")
    writer = csv.writer(buf, lineterminator="\r\n")
    for row in rows:
        writer.writerow(row)
    return buf.getvalue()


# --------------------------------------------------------------------------
# UI 辅助
# --------------------------------------------------------------------------
def _has_testid(html, testid):
    return f'data-testid="{testid}"' in html or f"data-testid='{testid}'" in html


def _extract_embedded_state(html):
    for match in re.finditer("""<script[^>]*type=["']application/json["'][^>]*>(.*?)</script>""",
                             html, re.S | re.I):
        try:
            return json.loads(match.group(1))
        except ValueError:
            continue
    return None


def _ui_has_feedback(html):
    low = html.lower()
    if "aria-live" in low:
        return True
    if re.search("""(id|class)\s*=\s*["'][^"']*(error|feedback|message|status)""", low):
        return True
    if re.search("""data-testid\s*=\s*["'][^"']*(error|feedback|message)""", low):
        return True
    return False


# --------------------------------------------------------------------------
# A01–A14 用例实现
# --------------------------------------------------------------------------
def _a01():
    resp = http_get("/")
    expect_eq(resp.status, 200, "GET / 应返回 200")
    expect_true("text/html" in resp.headers.get("Content-Type", "").lower(),
                "GET / 应返回 text/html")
    html = resp.text()
    expect_true(any("\u4e00" <= ch <= "\u9fff" for ch in html), "GET / 应包含中文界面文本")
    for testid in REQUIRED_TESTIDS:
        expect_true(_has_testid(html, testid), f"UI 缺少 data-testid={testid} 控件")
    expect_true("/api/state" in html, "GET / 的 UI 必须与 JSON API（/api/state）共用真实状态")
    state = get_state(CTX.month)
    _assert_totals_consistent(state)


def _a02():
    name = uniq("A02")
    create_category(CTX.month, name, "100.00")
    state = get_state(CTX.month)
    cat = require_category(state, name)
    expect_eq(cat.get("budget"), "100.00", "分类 budget")
    expect_eq(cat.get("spent"), "0.00", "分类 spent 初始应为 0.00")
    expect_eq(cat.get("remaining"), "100.00", "分类 remaining 初始应等于预算")
    _assert_totals_consistent(state)


def _a03():
    name = uniq("A03")
    create_category(CTX.month, name, "10.00")
    resp = http_post("/api/categories", {"month": CTX.month, "name": name, "budget": "20.00"})
    expect_error(resp, "同月同名分类应被拒绝")
    state = get_state(CTX.month)
    expect_eq(len(categories_named(state, name)), 1, "同月同名不应产生第二条分类")


def _a04():
    name = uniq("A04")
    cid = create_category(CTX.month, name, "80.00")
    txn_date = day_in(CTX.month, 15)
    note = "午餐"
    tid = create_txn(txn_date, cid, "23.45", note)
    state = get_state(CTX.month)
    txn = require_txn(state, tid)
    expect_eq(txn.get("date"), txn_date, "支出日期")
    expect_eq(txn.get("category_id"), cid, "支出分类")
    expect_eq(txn.get("amount"), "23.45", "支出金额")
    expect_eq(txn.get("note"), note, "支出备注")
    cat = require_category(state, name)
    expect_eq(cat.get("spent"), "23.45", "分类 spent 应含该笔")
    expect_eq(cat.get("remaining"), "56.55", "分类 remaining 应重算")
    _assert_totals_consistent(state)


def _a05():
    name = uniq("A05")
    cid = create_category(CTX.month, name, "50.00")
    before = get_state(CTX.month)
    for amount in ["0", "0.00", "-1.00", "1.234", "10.000", "abc", ""]:
        resp = http_post("/api/transactions",
                         {"date": day_in(CTX.month, 10), "category_id": cid,
                          "amount": amount, "note": "非法"})
        expect_error(resp, f"金额 {amount!r} 应被拒绝")
    for amount in ["0", "-5.00", "1.234"]:
        resp = http_post("/api/categories",
                         {"month": CTX.month, "name": uniq("A05b"), "budget": amount})
        expect_error(resp, f"分类预算 {amount!r} 应被拒绝")
    after = get_state(CTX.month)
    expect_true(after == before, "非法金额不得改变既有数据或汇总")


def _a06():
    name = uniq("A06")
    cid = create_category(CTX.month, name, "40.00")
    before = get_state(CTX.month)
    other_date = day_in(shift_month(CTX.month, -1), 15)
    resp = http_post("/api/transactions",
                     {"date": other_date, "category_id": cid, "amount": "5.00", "note": "跨月"})
    expect_error(resp, "日期与分类所属月份不一致应被拒绝")
    after = get_state(CTX.month)
    expect_true(after == before, "跨月交易失败不得改变既有数据")


def _a07():
    unused = uniq("A07u")
    unused_budget = "50.00"
    create_category(CTX.month, unused, unused_budget)
    over = uniq("A07o")
    ocid = create_category(CTX.month, over, "30.00")
    txn_date = day_in(CTX.month, 12)
    create_txn(txn_date, ocid, "45.00", "超支1")
    state = get_state(CTX.month)
    ucat = require_category(state, unused)
    expect_eq(ucat.get("spent"), "0.00", "未使用分类 spent")
    expect_eq(ucat.get("remaining"), unused_budget, "未使用分类 remaining")
    ocat = require_category(state, over)
    expect_eq(ocat.get("spent"), "45.00", "超支分类 spent")
    expect_eq(ocat.get("remaining"), "-15.00", "超支应显示负 remaining")
    create_txn(txn_date, ocid, "5.00", "超支2")
    state2 = get_state(CTX.month)
    ocat2 = require_category(state2, over)
    expect_eq(ocat2.get("spent"), "50.00", "超支不阻断后续记账，spent 累计")
    expect_eq(ocat2.get("remaining"), "-20.00", "继续超支 remaining 更负")
    _assert_totals_consistent(state2)


def _a08():
    name = uniq("A08")
    cid = create_category(CTX.month, name, "100.00")
    txn_date = day_in(CTX.month, 8)
    t1 = create_txn(txn_date, cid, "10.00", "n1")
    t2 = create_txn(txn_date, cid, "20.00", "n2")
    state = get_state(CTX.month)
    expect_eq(require_category(state, name).get("spent"), "30.00", "两笔合计")
    resp = http_put(f"/api/transactions/{t2}",
                    {"date": txn_date, "category_id": cid, "amount": "25.00", "note": "n2改"})
    expect_true(200 <= resp.status < 300, "修改支出应成功")
    state = get_state(CTX.month)
    expect_eq(require_txn(state, t2).get("amount"), "25.00", "修改后金额")
    expect_eq(require_category(state, name).get("spent"), "35.00", "修改后汇总即时重算")
    _assert_totals_consistent(state)
    resp = http_delete(f"/api/transactions/{t1}")
    expect_true(200 <= resp.status < 300, "删除支出应成功")
    state = get_state(CTX.month)
    expect_true(find_txn(state, t1) is None, "删除后列表不含该笔")
    expect_eq(require_category(state, name).get("spent"), "25.00", "删除后汇总即时重算")
    _assert_totals_consistent(state)


def _a09():
    before = get_state(CTX.month)
    for bad_id in ["999999", "abc", "-1"]:
        resp = http_put(f"/api/transactions/{bad_id}",
                        {"date": day_in(CTX.month, 5), "category_id": 1,
                         "amount": "1.00", "note": "x"})
        expect_error(resp, f"PUT 交易 {bad_id!r} 应报错")
        resp = http_delete(f"/api/transactions/{bad_id}")
        expect_error(resp, f"DELETE 交易 {bad_id!r} 应报错")
        resp = http_put(f"/api/categories/{bad_id}", {"budget": "9.99"})
        expect_error(resp, f"PUT 分类 {bad_id!r} 应报错")
    after = get_state(CTX.month)
    expect_true(after == before, "非法 id 操作不得改变既有数据")


def _a10_isolation():
    month_a = CTX.month
    month_b = shift_month(month_a, 1)
    name = uniq("A10")
    cid_a = create_category(month_a, name, "40.00")
    create_txn(day_in(month_a, 15), cid_a, "12.00", "本月支出")
    cid_b = create_category(month_b, name, "60.00")
    create_txn(day_in(month_b, 15), cid_b, "7.00", "次月支出")
    state_a = get_state(month_a)
    state_b = get_state(month_b)
    expect_true(find_category(state_a, name) is not None, "本月应含该分类")
    expect_true(find_category(state_b, name) is not None, "次月应含同名分类")
    expect_eq(require_category(state_a, name).get("spent"), "12.00", "本月 spent 不受次月影响")
    expect_eq(require_category(state_b, name).get("spent"), "7.00", "次月 spent 不受本月影响")
    expect_true(all(t.get("date", "").startswith(month_a) for t in state_a["transactions"]),
                "本月交易列表应仅含本月")
    expect_true(all(t.get("date", "").startswith(month_b) for t in state_b["transactions"]),
                "次月交易列表应仅含次月")
    return state_a


def _a11():
    name = uniq("A11")
    cid = create_category(CTX.month, name, "200.00")
    txn_date = day_in(CTX.month, 9)
    tricky_note = '午餐, "特价"\n第二行'
    create_txn(txn_date, cid, "12.34", tricky_note)
    resp = http_get("/api/export?" + urlencode({"month": CTX.month}))
    expect_eq(resp.status, 200, "导出应返回 200")
    text = resp.text().lstrip("\ufeff")
    rows = parse_csv_text(text)
    expect_true(len(rows) >= 1, "导出应至少包含表头")
    expect_eq(rows[0], ["date", "category", "amount", "note"], "CSV 表头")
    matched = [r for r in rows[1:] if len(r) == 4 and r[3] == tricky_note and r[2] == "12.34"]
    expect_true(len(matched) == 1, "导出应含该支出且中文/引号/换行往返一致")
    expect_eq(matched[0][0], txn_date, "导出行日期")
    expect_eq(matched[0][1], name, "导出行分类名")
    for row in rows[1:]:
        expect_true(row[0].startswith(CTX.month), "导出行应均为当月")
    expect_eq(parse_csv_text(serialize_csv(rows)), rows, "CSV 重新序列化后应可往返解析")


def _a12():
    name = uniq("A12")
    month_a = CTX.month
    month_b = shift_month(month_a, 1)
    id_a = create_category(month_a, name, "10.00")
    id_b = create_category(month_b, name, "20.00")
    resp = http_put(f"/api/categories/{id_a}", {"budget": "15.00"})
    expect_true(200 <= resp.status < 300, "更新目标月分类预算应成功")
    state_a = get_state(month_a)
    state_b = get_state(month_b)
    expect_eq(require_category(state_a, name).get("budget"), "15.00", "目标月预算已更新")
    expect_eq(require_category(state_b, name).get("budget"), "20.00", "其他月同名分类不得被误改")
    resp = http_put(f"/api/categories/{id_b}", {"budget": "25.00"})
    expect_true(200 <= resp.status < 300, "更新另一月分类预算应成功")
    state_a = get_state(month_a)
    state_b = get_state(month_b)
    expect_eq(require_category(state_a, name).get("budget"), "15.00", "另一月更新不得影响本月")
    expect_eq(require_category(state_b, name).get("budget"), "25.00", "另一月预算已更新")


def _a13():
    html = http_get("/").text()
    expect_true("/api/state" in html, "UI 必须读取同一 /api/state 状态源")
    for testid in REQUIRED_TESTIDS:
        expect_true(_has_testid(html, testid), f"UI 缺少 data-testid={testid} 控件")
    name = uniq("A13")
    cid = create_category(CTX.month, name, "60.00")
    create_txn(day_in(CTX.month, 20), cid, "18.00", "UI一致")
    state = get_state(CTX.month)
    cat = require_category(state, name)
    expect_money(cat.get("spent"), "state.spent")
    expect_money(cat.get("remaining"), "state.remaining")
    expect_eq(cat.get("remaining"), _q(Decimal(cat.get("budget")) - Decimal(cat.get("spent"))),
              "state 数字应自洽（remaining = budget - spent）")
    _assert_totals_consistent(state)
    embedded = _extract_embedded_state(http_get("/").text())
    if isinstance(embedded, dict) and isinstance(embedded.get("categories"), list):
        ecat = find_category(embedded, name)
        expect_true(ecat is not None, "UI 内嵌状态应含该分类")
        expect_eq(ecat.get("spent"), cat.get("spent"), "UI 内嵌 spent 应与 API 一致")


def _a14():
    name = uniq("A14")
    cid = create_category(CTX.month, name, "10.00")
    resp = http_post("/api/categories", {"month": CTX.month, "name": name, "budget": "10.00"})
    expect_error(resp, "重复分类应返回非 2xx JSON error")
    resp = http_post("/api/transactions",
                     {"date": day_in(CTX.month, 3), "category_id": cid, "amount": "0", "note": "x"})
    expect_error(resp, "非法金额应返回非 2xx JSON error")
    html = http_get("/").text()
    expect_true(_ui_has_feedback(html), "UI 应提供可理解的失败反馈区域")


_HTTP_CASES = {
    "A01": _a01, "A02": _a02, "A03": _a03, "A04": _a04, "A05": _a05,
    "A06": _a06, "A07": _a07, "A08": _a08, "A09": _a09, "A10": _a10_isolation,
    "A11": _a11, "A12": _a12, "A13": _a13, "A14": _a14,
}


# --------------------------------------------------------------------------
# 运行器：run_http_case / run_file_case
# --------------------------------------------------------------------------
def run_http_case(case):
    func = _HTTP_CASES.get(case)
    if func is None:
        raise ConfigError(f"未知用例 {case}")
    func()
    if case == "A10" and CTX.mode != "file":
        raise SkipCase("月份隔离已通过；‘同 data-dir 重启保留’与‘仅写指定目录’需要 --app-path/--data-root 模式")


def run_file_case(case):
    if case != "A10":
        return run_http_case(case)
    baseline = _a10_isolation()
    CTX.app.stop()
    CTX.app.start()
    after = get_state(CTX.month)
    expect_true(after == baseline, "同一 data-dir 重启后当月状态应保留")
    stray = _new_files(CTX.app_dir_snapshot, CTX.app_dir)
    expect_true(not stray, f"被检应用目录出现越界写入（数据应仅写入 data-dir）：{sorted(stray)}")
    expect_true(_has_files(CTX.data_root), "指定 data-root 中未发现持久化数据")


# --------------------------------------------------------------------------
# 进程与文件系统辅助（CLI 模式）
# --------------------------------------------------------------------------
class AppProcess:
    def __init__(self, app_path, data_dir, port):
        self.app_path = app_path
        self.data_dir = data_dir
        self.port = port
        self.proc = None

    def start(self):
        cmd = [sys.executable, self.app_path, "--port", str(self.port), "--data-dir", self.data_dir]
        self.proc = subprocess.Popen(
            cmd,
            cwd=os.path.dirname(self.app_path),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=False,
        )
        self._wait_ready()

    def _wait_ready(self):
        deadline = time.time() + 30
        last = None
        while time.time() < deadline:
            if self.proc.poll() is not None:
                raise CheckFailure("被检应用启动后立即退出（请检查 app.py 及其启动参数）")
            try:
                resp = http_get(_state_path(CTX.month))
                if 200 <= resp.status < 300:
                    return
                last = f"HTTP {resp.status}"
            except CheckFailure as exc:
                last = str(exc)
            time.sleep(0.3)
        raise CheckFailure(f"被检应用就绪超时（最后状态：{last}）")

    def stop(self):
        if self.proc is None:
            return
        try:
            if self.proc.poll() is None:
                self.proc.terminate()
                try:
                    self.proc.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    self.proc.kill()
                    self.proc.wait(timeout=10)
        finally:
            self.proc = None


def _iter_files(root):
    out = set()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != "__pycache__" and not d.startswith(".")]
        for filename in filenames:
            if filename.endswith(".pyc"):
                continue
            out.add(os.path.relpath(os.path.join(dirpath, filename), root))
    return out


def _new_files(before, root):
    return _iter_files(root) - before


def _has_files(root):
    return bool(_iter_files(root))


def find_free_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]
    finally:
        sock.close()


# --------------------------------------------------------------------------
# 上下文与入口
# --------------------------------------------------------------------------
class Context:
    def __init__(self):
        self.mode = None
        self.month = None
        self.app_path = None
        self.app_dir = None
        self.app_dir_snapshot = set()
        self.data_root = None
        self.app = None


CTX = Context()


def _configure_file(app_path, data_root):
    app_abs = os.path.abspath(app_path)
    if not os.path.isfile(app_abs):
        raise ConfigError("--app-path 不存在或不是文件。")
    if os.path.basename(app_abs) != "app.py":
        raise ConfigError("--app-path 必须指向被检应用入口 app.py。")
    root_abs = os.path.abspath(data_root)
    if not os.path.isdir(root_abs):
        raise ConfigError("--data-root 必须是已存在的目录（操作员提供的受控临时根）。")
    if root_abs == os.path.abspath(os.path.expanduser("~")) or root_abs == os.path.abspath(os.sep):
        raise ConfigError("--data-root 不得为 HOME 或文件系统根。")
    if os.path.commonpath([root_abs, os.path.dirname(app_abs)]) == root_abs:
        raise ConfigError("--data-root 不得包含被检应用目录。")
    CTX.app_path = app_abs
    CTX.app_dir = os.path.dirname(app_abs)
    CTX.data_root = root_abs


def _parse_args(argv):
    parser = argparse.ArgumentParser(
        prog="run.py",
        description="个人月度预算与消费前剩余额度：真实目标验收检查器（A01–A14）",
    )
    parser.add_argument("--target-url", help="Web 模式：被检实例的精确 loopback origin，如 http://127.0.0.1:8000")
    parser.add_argument("--app-path", help="CLI 模式：被检应用入口 app.py 的路径")
    parser.add_argument("--data-root", help="CLI 模式：自有可弃用的受控数据根目录")
    parser.add_argument("--month", help="目标月份 YYYY-MM，默认当月")
    args = parser.parse_args(argv)

    has_target = args.target_url is not None
    has_file = args.app_path is not None or args.data_root is not None
    if has_target and has_file:
        raise ConfigError("--target-url 与 --app-path/--data-root 互斥，只能选择一种模式。")
    if not has_target and not has_file:
        raise ConfigError("必须提供 --target-url，或同时提供 --app-path 与 --data-root。")
    if has_file and not (args.app_path and args.data_root):
        raise ConfigError("CLI 模式需要同时提供 --app-path 与 --data-root。")
    month = args.month or default_month()
    if not re.match(r"^\d{4}-(0[1-9]|1[0-2])$", month):
        raise ConfigError("--month 必须是 YYYY-MM 形式。")
    return args, month


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    try:
        args, month = _parse_args(argv)
    except ConfigError as exc:
        print(f"[配置错误] {exc}", file=sys.stderr)
        return 2

    CTX.month = month
    if args.target_url is not None:
        CTX.mode = "http"
        try:
            configure_http(args.target_url)
        except ConfigError as exc:
            print(f"[配置错误] {exc}", file=sys.stderr)
            return 2
    else:
        CTX.mode = "file"
        try:
            _configure_file(args.app_path, args.data_root)
        except ConfigError as exc:
            print(f"[配置错误] {exc}", file=sys.stderr)
            return 2
        port = find_free_port()
        configure_http(f"http://127.0.0.1:{port}")
        CTX.app_dir_snapshot = _iter_files(CTX.app_dir)
        CTX.app = AppProcess(CTX.app_path, CTX.data_root, port)
        try:
            CTX.app.start()
        except CheckFailure as exc:
            CTX.app.stop()
            print(f"[启动失败] {exc}", file=sys.stderr)
            return 1

    results = []
    try:
        for case in CASE_ORDER:
            try:
                if CTX.mode == "file" and case == "A10":
                    run_file_case(case)
                else:
                    run_http_case(case)
                results.append((case, "PASS", ""))
            except SkipCase as exc:
                results.append((case, "SKIP", str(exc)))
            except CheckFailure as exc:
                results.append((case, "FAIL", str(exc)))
            except Exception as exc:  # noqa: BLE001 - 归为失败，绝不伪造通过
                results.append((case, "ERROR", f"{type(exc).__name__}: {exc}"))
    finally:
        if CTX.app is not None:
            CTX.app.stop()

    print(f"目标模式：{CTX.mode}；月份：{month}")
    for case, status, detail in results:
        line = f"{case} {status} {CASES.get(case, '')}"
        if detail:
            line += f" | {detail}"
        print(line)
    passed = sum(1 for _, status, _ in results if status == "PASS")
    skipped = sum(1 for _, status, _ in results if status == "SKIP")
    failed = [(c, s, d) for c, s, d in results if s in ("FAIL", "ERROR")]
    print(f"结果：通过 {passed} / 跳过 {skipped} / 失败 {len(failed)}")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
