#!/usr/bin/env python3
"""Standalone, loopback-only dinner poll application. Python standard library."""

import argparse
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlencode

from model import Store
from web_support import Error, Handler, h


STYLE = """+:root{--ink:#322a24;--muted:#796e64;--accent:#9d4729;--line:#e6d9c9;--paper:#fffdf8;--bg:#f6efe5}*{box-sizing:border-box}body{margin:0;font:15px/1.65 -apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC',sans-serif;color:var(--ink);background:var(--bg)}a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}header{border-bottom:1px solid var(--line);background:var(--paper)}.top,main{max-width:1160px;margin:auto;padding:23px 28px}.top{display:flex;justify-content:space-between;align-items:center;gap:14px}.brand{font-size:22px;font-weight:750;letter-spacing:-.5px}.brand span{color:var(--accent);margin-right:10px}.local{font-size:12px;color:var(--muted)}main{padding-top:38px}.eyebrow{font-size:12px;letter-spacing:2px;color:var(--accent);font-weight:700;margin:0 0 8px}h1{font-size:36px;line-height:1.3;letter-spacing:-1px;margin:0 0 14px;overflow-wrap:anywhere}h2{font-size:20px;margin:0 0 16px}p{margin:0 0 14px}.sub,.hint{color:var(--muted)}.hint{font-size:12px}.trust{padding:12px 16px;border:1px solid #dfc9a5;border-radius:9px;background:#fdf5e5;margin:20px 0 28px;font-size:13px}.layout{display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:28px;align-items:start}.panel{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:26px;margin-bottom:22px}.intro{margin-bottom:25px}.field{margin-bottom:18px}label{display:block;font-size:13px;font-weight:650;margin-bottom:7px}input,textarea{font:inherit;color:var(--ink);border:1px solid #cfbfab;border-radius:8px;background:white;padding:11px 12px;width:100%}textarea{resize:vertical}input:focus,textarea:focus,button:focus-visible,a:focus-visible{outline:3px solid #d3a282;outline-offset:3px}button,.button{display:inline-block;cursor:pointer;font:inherit;border:1px solid #cbb9a4;padding:10px 17px;border-radius:8px;color:var(--ink);background:var(--paper)}button:hover,.button:hover{background:#f0e4d5;text-decoration:none}.primary{background:var(--accent);border-color:var(--accent);color:white}.primary:hover{background:#7b341d}button:disabled{cursor:not-allowed;opacity:.5}fieldset{margin:0;padding:0;border:0;min-width:0}legend{font-size:13px;font-weight:650;margin-bottom:10px}.choice{border:1px solid var(--line);border-radius:9px;padding:14px;display:flex;align-items:center;gap:12px;font-size:15px;font-weight:500;overflow-wrap:anywhere}.choice:has(input:checked){background:#f8eadb;border-color:#ae7250}.choice input{width:18px;height:18px;accent-color:var(--accent);margin:0;flex-shrink:0}.row{display:flex;justify-content:space-between;align-items:center;gap:15px}.pill{border-radius:20px;background:#e8eedf;color:#4c603c;padding:4px 11px;font-size:12px;white-space:nowrap}.pill.closed{background:#eee3da;color:#75604c}.poll-card{display:block;padding:20px;border:1px solid var(--line);background:var(--paper);border-radius:12px;margin:13px 0;color:var(--ink)}.poll-card:hover{text-decoration:none;border-color:#b48362}.poll-title{font-size:19px;font-weight:650;overflow-wrap:anywhere}.poll-card .hint{margin:8px 0 0}.empty{padding:36px 24px;border:1px dashed #c9bba8;border-radius:12px;text-align:center;color:var(--muted)}.notice{padding:13px 16px;border-radius:9px;background:#e8efdf;color:#405538;margin-bottom:20px}.error{background:#fae4da;color:#8a351e}.stats{display:flex;align-items:baseline;gap:7px;margin:0 0 15px}.stats strong{font-size:42px;line-height:1.2}.result{padding:13px 0;border-top:1px solid var(--line)}.result .row span{overflow-wrap:anywhere}.result strong{white-space:nowrap}.track{height:7px;border-radius:10px;background:#f0e6d8;margin-top:9px;overflow:hidden}.bar{height:100%;background:#be754e;border-radius:10px}.summary{font-size:13px;background:#f4ebde;border-radius:8px;padding:12px;margin-top:16px;overflow-wrap:anywhere}.action-note{font-size:13px;color:var(--muted);margin:12px 0 18px}.back{display:inline-block;margin-bottom:24px;font-size:13px}footer{border-top:1px solid var(--line);padding-top:20px;margin-top:40px;font-size:12px;color:var(--muted)}@media(max-width:800px){.layout{grid-template-columns:1fr}.top,main{padding:20px}.panel{padding:21px}h1{font-size:29px}.local{max-width:140px;text-align:right}main{padding-top:28px}}
"""


def shell(title, content):
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{h(title)} · 聚餐投票</title><style>{STYLE}</style></head><body><header><div class="top"><a class="brand" href="/"><span>◉</span>聚餐投票</a><span class="local">同一台设备 · 本机保存</span></div></header><main>{content}<footer>Atlas 辅助试用 · SQLite 本机持久化 · 不用于正式选举</footer></main></body></html>'''


TRUST = '<div class="trust"><strong>同机共享，代号不是身份认证。</strong> 任何使用这台设备的人都可用相同代号改票，请小组成员自觉使用自己的代号。</div>'


def notice(message, error=False):
    return f'<div class="notice{" error" if error else ""}" role="{"alert" if error else "status"}">{h(message)}</div>' if message else ''


def outcome(poll):
    if poll['total_votes'] == 0:
        return '暂无投票，等大家表达偏好。'
    maximum = max(option['count'] for option in poll['options'])
    leaders = [option['label'] for option in poll['options'] if option['count'] == maximum]
    if len(leaders) > 1:
        return f'并列：{"、".join(leaders)}，各 {maximum} 票。由大家共同决定地点。'
    return f'当前票数最多：{leaders[0]}，{maximum} 票。'


class App(Handler):
    @property
    def store(self):
        return self.server.store

    def home(self, message='', error=False):
        cards = ''.join(f'''<a class="poll-card" href="/polls/{h(p['id'])}"><div class="row"><span class="poll-title">{h(p['title'])}</span><span class="pill {'closed' if p['status']=='closed' else ''}">{'已结束' if p['status']=='closed' else '进行中'}</span></div><p class="hint">查看选项、投票与汇总 →</p></a>''' for p in self.store.listing())
        if not cards:
            cards = '<div class="empty">还没有投票。<br>先提出一个问题，邀请大家轮流选地点。</div>'
        data = self.data
        return shell('一起决定今晚去哪', f'''<div class="intro"><p class="eyebrow">A TABLE FOR EVERYONE</p><h1>一起决定，今晚去哪。</h1><p class="sub">提出问题，留下偏好，让聚餐少一点纠结。</p></div>{TRUST}{notice(message,error)}<div class="layout"><section><div class="row"><h2>聚餐投票</h2><span class="hint">随时查看结果</span></div>{cards}</section><section class="panel"><h2>新建投票</h2><form method="post" action="/polls"><div class="field"><label for="title">聚餐问题</label><input id="title" name="title" maxlength="160" placeholder="例如：周五聚餐，去哪里？" value="{h(data.get('title',''))}" required></div><div class="field"><label for="options">地点选项 · 每行一个</label><textarea id="options" name="options" rows="6" placeholder="巷口面馆&#10;山城火锅" required>{h(data.get('options',''))}</textarea><p class="hint">2–8 个地点，每项最多 80 字；创建后固定。</p></div><button class="primary" type="submit">创建投票</button></form></section></div>''')

    def detail_page(self, poll_id, message='', error=False):
        poll = self.store.detail(poll_id)
        closed = poll['status'] == 'closed'
        data = self.data or self.query
        selected = data.get('option_id', '')
        choices = ''.join(f'''<label class="choice"><input type="radio" name="option_id" value="{h(option['id'])}" {'checked' if selected==option['id'] else ''} required><span>{h(option['label'])}</span></label>''' for option in poll['options'])
        results = ''.join(f'''<div class="result"><div class="row"><span>{h(option['label'])}</span><strong>{option['count']} 票</strong></div><div class="track"><div class="bar" style="width:{option['count']/max(poll['total_votes'],1)*100:.2f}%"></div></div></div>''' for option in poll['options'])
        status_note = '投票已结束。结果已冻结，重开后才能投票或改票。' if closed else '每个代号一票。使用相同代号再次提交，即可替换原来的选择。'
        action = 'reopen' if closed else 'close'
        action_label = '重开投票' if closed else '结束投票'
        return shell(poll['title'], f'''<a class="back" href="/">← 全部投票</a><div class="row"><p class="eyebrow">DINNER POLL</p><span class="pill {'closed' if closed else ''}">{'已结束' if closed else '进行中'}</span></div><h1>{h(poll['title'])}</h1>{TRUST}{notice(message,error)}<div class="layout"><section class="panel"><h2>你的选择</h2><p class="action-note">{status_note}</p><form method="post" action="/vote"><input type="hidden" name="poll_id" value="{h(poll_id)}"><fieldset {'disabled' if closed else ''}><div class="field"><label for="participant">你的代号</label><input id="participant" name="participant" maxlength="40" value="{h(data.get('participant',''))}" placeholder="例如：小林" autocomplete="off" required><p class="hint">1–40 字；忽略首尾空格与字母大小写。</p></div><fieldset class="field"><legend>选择一个地点</legend>{choices}</fieldset><button class="primary" type="submit">提交 / 更改我的票</button></fieldset></form></section><aside><section class="panel"><h2>投票汇总</h2><div class="stats"><strong>{poll['total_votes']}</strong><span class="sub">人已投票</span></div>{results}<div class="summary">{h(outcome(poll))}</div></section><section class="panel"><h2>主持人操作</h2><p class="action-note">{'需要继续收集意见时，可重开投票。已有票会保留。' if closed else '大家都选好后结束投票，即可冻结结果；之后仍可重开。'}</p><form method="post" action="/{action}"><input type="hidden" name="id" value="{h(poll_id)}"><button type="submit">{action_label}</button></form></section></aside></div>''')

    def error_page(self, error):
        if self.route == '/polls':
            return self.home(error.message, True)
        poll_id = self.data.get('poll_id') or self.data.get('id')
        if poll_id:
            try:
                return self.detail_page(poll_id, error.message, True)
            except Error:
                pass
        return shell('无法完成操作', notice(error.message, True) + '<a class="button" href="/">返回投票列表</a>')

    def dispatch(self, method):
        path = self.route
        if method == 'GET':
            if path == '/api/health':
                return self.json(200, {'status': 'ok'})
            if path == '/api/polls':
                return self.json(200, {'polls': self.store.listing()})
            if path.startswith('/api/polls/'):
                return self.json(200, self.store.detail(path[len('/api/polls/'):]))
            if path == '/':
                return self.send(200, self.home())
            if path.startswith('/polls/'):
                messages = {'created': '投票已创建，邀请大家轮流选择吧。', 'voted': '投票已保存；相同代号的旧选择已被替换。', 'closed': '投票已结束，结果已冻结。', 'reopened': '投票已重开，可以继续投票或改票。'}
                return self.send(200, self.detail_page(path[len('/polls/'):], messages.get(self.query.get('notice'), '')))
        elif method == 'POST':
            api = path.startswith('/api/')
            if path in ('/api/polls', '/polls'):
                data = self.data if api else {**self.data, 'options': self.data.get('options', '').splitlines()}
                result = self.store.create(data)
                status, message = 201, 'created'
            elif path in ('/api/votes', '/vote'):
                result = self.store.vote(self.data)
                status, message = 200, 'voted'
            elif path in ('/api/polls/close', '/api/polls/reopen', '/close', '/reopen'):
                closed = path.endswith('/close')
                result = self.store.status(self.data.get('id'), 'closed' if closed else 'open')
                status, message = 200, 'closed' if closed else 'reopened'
            else:
                raise Error('not_found', '找不到这个页面。', 404)
            if api:
                return self.json(status, result)
            query = {'notice': message}
            if message == 'voted':
                query.update(participant=self.data.get('participant', ''), option_id=self.data.get('option_id', ''))
            return self.redirect('/polls/' + result['id'] + '?' + urlencode(query))
        raise Error('not_found', '找不到这个页面。', 404)


def main():
    parser = argparse.ArgumentParser(description='同机聚餐地点投票，仅监听 127.0.0.1')
    parser.add_argument('--port', type=int, default=5278)
    parser.add_argument('--data-dir', type=Path, required=True)
    parser.add_argument('--demo', action='store_true', help='仅全新数据库首次初始化虚构示例')
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), App)
    server.store = Store(args.data_dir, demo=args.demo)
    print(f'聚餐投票：http://127.0.0.1:{args.port} · 数据目录：{args.data_dir.resolve()}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
